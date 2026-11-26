"""
SarkariPedia — Scraper / Crawler / Health Checker
====================================================

Usage (project root se chalao):
  python -m scraper.crawl seed     # seeds.csv se 79 known sites DB mein load karo
  python -m scraper.crawl crawl    # sources.json ki directories crawl karo
  python -m scraper.crawl check    # har site ka is_live status update karo
  python -m scraper.crawl clean    # duplicates hatao, URLs normalize karo
  python -m scraper.crawl stats    # DB stats dikhao
  python -m scraper.crawl all      # seed + crawl + check + clean

Niyam:
  - robots.txt ka palan karo
  - Har request ke beech DELAY seconds wait karo
  - Sirf .gov.in, .nic.in, .gov domains collect karo
  - Site ke andar ka koi personal data scrape mat karo
"""

import csv
import json
import logging
import os
import sys
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from urllib.parse import urljoin, urldefrag, urlparse
from urllib.robotparser import RobotFileParser

from app.db import connect, upsert_site, mark_health
from scraper.classify import classify, is_official, normalize

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
HERE = os.path.dirname(__file__)
HEADERS = {"User-Agent": "GovSiteIndexer/1.0 (educational directory project; not for commercial use)"}
DELAY = 1.2          # seconds between requests to the same host
TIMEOUT = 20         # seconds per request
HEALTH_WORKERS = 10  # parallel threads for health check
FAIL_THRESHOLD = 3   # consecutive fails before marking hidden

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("govsites")

# ---------------------------------------------------------------------------
# robots.txt cache
# ---------------------------------------------------------------------------
_robots_cache: dict = {}


def _robots_allowed(url: str) -> bool:
    """Check robots.txt (cached per root host)."""
    root = "{0.scheme}://{0.netloc}".format(urlparse(url))
    if root not in _robots_cache:
        rp = RobotFileParser()
        rp.set_url(root + "/robots.txt")
        try:
            rp.read()
        except Exception:
            rp = None
        _robots_cache[root] = rp
    rp = _robots_cache[root]
    return True if rp is None else rp.can_fetch(HEADERS["User-Agent"], url)


# ---------------------------------------------------------------------------
# Phase 1 — Seed loader
# ---------------------------------------------------------------------------

def load_seeds():
    """Load scraper/seeds.csv into the database."""
    con = connect()
    n = 0
    seeds_path = os.path.join(HERE, "seeds.csv")
    with open(seeds_path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            url, host = normalize(row["url"])
            _, state = classify(host, row["name"])
            upsert_site(con, row["name"], url, host, row["category"], state, "seed")
            n += 1
    con.commit()
    log.info(f"[seed] {n} sites loaded from seeds.csv")


# ---------------------------------------------------------------------------
# Phase 2 — Web crawler
# ---------------------------------------------------------------------------

def _fetch_html(url: str) -> str | None:
    """Fetch page HTML. Returns None on error."""
    try:
        import requests  # lazy import
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        return r.text
    except ImportError:
        log.error("requests library not installed. Run: pip install requests beautifulsoup4")
        return None
    except Exception as e:
        log.debug(f"[skip] {url}: {e}")
        return None


def _try_playwright(url: str) -> str | None:
    """Fallback: render JS page using Playwright (if installed)."""
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=30_000)
            page.wait_for_load_state("networkidle", timeout=15_000)
            html = page.content()
            browser.close()
        return html
    except ImportError:
        log.debug("Playwright not installed — skipping JS fallback")
        return None
    except Exception as e:
        log.debug(f"[playwright] {url}: {e}")
        return None


def crawl_source(src: dict, con) -> int:
    """
    Breadth-first crawl of one directory site.
    Collects outbound official links; follows same-site links for pagination.
    Returns number of new links found.
    """
    start_url = src["url"]
    max_pages = src.get("max_pages", 30)
    site_host = urlparse(start_url).netloc.replace("www.", "")
    queue = deque([start_url])
    seen = {start_url}
    found = 0
    pages_fetched = 0

    # Lazy imports for crawl-only dependencies
    try:
        import requests as _req
        from bs4 import BeautifulSoup as _BS
    except ImportError as e:
        log.error(f"Missing library: {e}. Run: pip install requests beautifulsoup4")
        return 0

    while queue and pages_fetched < max_pages:
        page_url = queue.popleft()

        if not _robots_allowed(page_url):
            log.info(f"[robots] skipped {page_url}")
            continue

        html = _fetch_html(page_url)

        # JS fallback — try Playwright if page has very few links
        if html is None:
            html = _try_playwright(page_url)
        if html is None:
            continue

        pages_fetched += 1
        soup = _BS(html, "html.parser")

        for a in soup.find_all("a", href=True):
            raw_link = a["href"].strip()
            if not raw_link or raw_link.startswith(("javascript:", "mailto:", "#")):
                continue
            link, _ = urldefrag(urljoin(page_url, raw_link))
            if not link.startswith("http"):
                continue

            parsed = urlparse(link)
            link_host = parsed.netloc.replace("www.", "")

            if link_host == site_host:
                # Same-site: queue for pagination / category pages
                if link not in seen:
                    seen.add(link)
                    queue.append(link)
            elif is_official(link):
                # Outbound official link → save to DB
                canonical, host = normalize(link)
                link_text = a.get_text(" ", strip=True) or host
                cat, state = classify(host, link_text)
                upsert_site(con, link_text[:150], canonical, host, cat, state, src["name"])
                found += 1

        time.sleep(DELAY)

    con.commit()
    log.info(f"[crawl] {src['name']}: {pages_fetched} pages fetched, {found} official links found")
    return found


def crawl_all():
    """Crawl every source listed in sources.json."""
    sources_path = os.path.join(HERE, "sources.json")
    with open(sources_path, encoding="utf-8") as f:
        sources = json.load(f)

    con = connect()
    total = 0
    for src in sources:
        log.info(f"\n━━ Crawling: {src['name']} ({src['url']}) ━━")
        total += crawl_source(src, con)

    log.info(f"\n[crawl] Done. Total new links found: {total}")


# ---------------------------------------------------------------------------
# Phase 3 — Health checker
# ---------------------------------------------------------------------------

def _check_one(row: dict) -> tuple[int, int]:
    """HEAD/GET a single URL. Returns (id, is_live)."""
    import requests as _req  # lazy import
    url = row["url"]
    try:
        # Try HEAD first (lighter)
        r = _req.head(url, headers=HEADERS, timeout=12, allow_redirects=True)
        if r.status_code >= 400:
            raise _req.RequestException(f"HTTP {r.status_code}")
        live = 1
    except _req.RequestException:
        try:
            r = _req.get(url, headers=HEADERS, timeout=12,
                         allow_redirects=True, stream=True)
            live = 1 if r.status_code < 400 else 0
            r.close()
        except _req.RequestException:
            live = 0
    return row["id"], live


def check_all(workers: int = HEALTH_WORKERS):
    """Health-check every site in parallel. Update is_live + last_checked."""
    con = connect()
    rows = con.execute("SELECT id, url FROM sites").fetchall()
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    ok = 0

    log.info(f"[check] Checking {len(rows)} sites with {workers} workers …")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(_check_one, dict(r)): r for r in rows}
        for i, future in enumerate(as_completed(futures), 1):
            try:
                sid, live = future.result()
                if live:
                    ok += 1
                mark_health(con, sid, live, now)
                if i % 50 == 0:
                    log.info(f"[check] {i}/{len(rows)} done …")
            except Exception as e:
                log.debug(f"[check error] {e}")

    con.commit()
    log.info(f"[check] Done — {ok}/{len(rows)} sites are live")


# ---------------------------------------------------------------------------
# Phase 3 — Data cleaner
# ---------------------------------------------------------------------------

def clean_data():
    """
    Remove duplicates (same domain), normalize URLs, re-classify 'Other' sites.
    """
    con = connect()

    # 1. Re-normalize URLs (force https, strip www)
    rows = con.execute("SELECT id, url FROM sites").fetchall()
    updated = 0
    for row in rows:
        canonical, host = normalize(row["url"])
        if canonical != row["url"]:
            con.execute("UPDATE sites SET url=?, domain=? WHERE id=?",
                        (canonical, host, row["id"]))
            updated += 1

    log.info(f"[clean] {updated} URLs normalized")

    # 2. Remove exact URL duplicates (keep lowest id)
    con.execute("""
        DELETE FROM sites
        WHERE id NOT IN (
            SELECT MIN(id) FROM sites GROUP BY url
        )
    """)
    removed = con.execute("SELECT changes()").fetchone()[0]
    log.info(f"[clean] {removed} duplicate URLs removed")

    # 3. Remove domain-level duplicates (same domain → keep the one with
    #    the best name, i.e. longest name from seed or smallest id)
    con.execute("""
        DELETE FROM sites
        WHERE id NOT IN (
            SELECT MIN(id) FROM sites GROUP BY domain
        )
    """)
    removed2 = con.execute("SELECT changes()").fetchone()[0]
    log.info(f"[clean] {removed2} domain-level duplicates removed")

    # 4. Re-classify sites still in 'Other' category
    others = con.execute(
        "SELECT id, domain, name FROM sites WHERE category='Other'"
    ).fetchall()
    reclassified = 0
    for row in others:
        cat, state = classify(row["domain"], row["name"])
        if cat != "Other":
            con.execute(
                "UPDATE sites SET category=?, state=? WHERE id=?",
                (cat, state, row["id"]),
            )
            reclassified += 1

    log.info(f"[clean] {reclassified} 'Other' sites re-classified")
    con.commit()


# ---------------------------------------------------------------------------
# Stats reporter
# ---------------------------------------------------------------------------

def show_stats():
    con = connect()
    total = con.execute("SELECT COUNT(*) FROM sites").fetchone()[0]
    live = con.execute("SELECT COUNT(*) FROM sites WHERE is_live=1").fetchone()[0]
    other = con.execute("SELECT COUNT(*) FROM sites WHERE category='Other'").fetchone()[0]
    unchecked = con.execute("SELECT COUNT(*) FROM sites WHERE is_live IS NULL").fetchone()[0]

    print("\n" + "=" * 50)
    print(f"  SARKARI SITES — DATABASE STATS")
    print("=" * 50)
    print(f"  Total sites   : {total}")
    print(f"  Live          : {live}  ({live*100//total if total else 0}%)")
    print(f"  Unchecked     : {unchecked}")
    print(f"  'Other' cat   : {other}  ({other*100//total if total else 0}%)")
    print()

    print("  Top categories:")
    rows = con.execute(
        "SELECT category, COUNT(*) AS n FROM sites GROUP BY category ORDER BY n DESC"
    ).fetchall()
    for r in rows:
        bar = "█" * min(r["n"] // 5, 30)
        print(f"    {r['category']:<35} {r['n']:>5}  {bar}")

    print()
    print("  Top states:")
    srows = con.execute(
        "SELECT state, COUNT(*) AS n FROM sites WHERE state IS NOT NULL "
        "GROUP BY state ORDER BY n DESC LIMIT 10"
    ).fetchall()
    for r in srows:
        print(f"    {r['state']:<35} {r['n']:>5}")
    print("=" * 50 + "\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

    if cmd == "seed":
        load_seeds()
    elif cmd == "crawl":
        crawl_all()
    elif cmd == "check":
        check_all()
    elif cmd == "clean":
        clean_data()
    elif cmd == "stats":
        show_stats()
    elif cmd == "all":
        load_seeds()
        crawl_all()
        check_all()
        clean_data()
        show_stats()
    else:
        print(__doc__)
