"""
Database layer — SQLite schema aur helper functions.
GOV_DB environment variable se DB path override kar sakte hain.
"""
import os
import sqlite3

DB_PATH = os.environ.get(
    "GOV_DB",
    os.path.join(os.path.dirname(__file__), "..", "data", "gov_sites.db"),
)

SCHEMA = """
CREATE TABLE IF NOT EXISTS sites (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT    NOT NULL,
    url          TEXT    NOT NULL UNIQUE,
    domain       TEXT    NOT NULL,
    category     TEXT    NOT NULL DEFAULT 'Other',
    state        TEXT,
    source       TEXT,
    is_live      INTEGER,            -- 1=live, 0=dead, NULL=unchecked
    fail_count   INTEGER DEFAULT 0,  -- consecutive health-check failures
    hidden       INTEGER DEFAULT 0,  -- 1 = hide from frontend (too many failures)
    last_checked TEXT               -- ISO-8601 UTC timestamp
);

CREATE INDEX IF NOT EXISTS idx_sites_category ON sites(category);
CREATE INDEX IF NOT EXISTS idx_sites_state    ON sites(state);
CREATE INDEX IF NOT EXISTS idx_sites_live     ON sites(is_live);
CREATE INDEX IF NOT EXISTS idx_sites_domain   ON sites(domain);
"""

FAIL_THRESHOLD = 3  # consecutive failures before hiding a site


def connect() -> sqlite3.Connection:
    """Return a connected, schema-initialised SQLite connection."""
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


def upsert_site(
    con: sqlite3.Connection,
    name: str,
    url: str,
    domain: str,
    category: str,
    state: str | None = None,
    source: str | None = None,
) -> None:
    """
    Insert or update a site row.
    - category is only overwritten if the existing one is 'Other'.
    - state is only filled in if it was NULL before.
    - Resets hidden=0 when a previously dead site is re-discovered.
    """
    con.execute(
        """
        INSERT INTO sites (name, url, domain, category, state, source, hidden)
        VALUES (?, ?, ?, ?, ?, ?, 0)
        ON CONFLICT(url) DO UPDATE SET
            name       = excluded.name,
            category   = CASE
                            WHEN sites.category = 'Other'
                            THEN excluded.category
                            ELSE sites.category
                         END,
            state      = COALESCE(sites.state, excluded.state),
            source     = COALESCE(sites.source, excluded.source),
            hidden     = 0
        """,
        (name, url, domain, category, state, source),
    )


def mark_health(
    con: sqlite3.Connection,
    site_id: int,
    is_live: int,
    checked_at: str,
) -> None:
    """
    Update is_live, fail_count, hidden for a site after a health check.
    - If live → reset fail_count, unhide.
    - If dead → increment fail_count; hide once FAIL_THRESHOLD is reached.
    """
    if is_live:
        con.execute(
            """
            UPDATE sites
            SET is_live=1, fail_count=0, hidden=0, last_checked=?
            WHERE id=?
            """,
            (checked_at, site_id),
        )
    else:
        con.execute(
            """
            UPDATE sites
            SET is_live      = 0,
                fail_count   = fail_count + 1,
                hidden       = CASE WHEN fail_count + 1 >= ? THEN 1 ELSE hidden END,
                last_checked = ?
            WHERE id=?
            """,
            (FAIL_THRESHOLD, checked_at, site_id),
        )
