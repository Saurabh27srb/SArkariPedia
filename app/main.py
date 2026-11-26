"""
SarkariPedia — Flask Backend API
==================================

Endpoints:
  GET /                       → index.html serve karo
  GET /api/health             → API + DB status
  GET /api/categories         → categories with counts
  GET /api/states             → states with counts
  GET /api/sites              → sites list (search, filter, paginate)
  POST /api/suggest           → user ka site suggestion save karo
  POST /api/report            → broken link report save karo

Environment variables:
  GOV_DB   : SQLite DB path (default: ../gov_sites.db)
  PORT     : server port (default: 8000)
  FRONTEND_ORIGIN : allowed CORS origin in production (default: * for dev)
"""

import json
import os
from datetime import datetime, timezone

from flask import Flask, jsonify, request, send_from_directory

try:
    from flask_cors import CORS
    HAS_CORS = True
except ImportError:
    HAS_CORS = False

from app.db import connect

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = Flask(__name__, static_folder="static", static_url_path="/static")

# CORS — dev mein sab allow, production mein FRONTEND_ORIGIN env var set karo
_origin = os.environ.get("FRONTEND_ORIGIN", "*")
if HAS_CORS:
    CORS(app, origins=_origin)
else:
    # Manual CORS fallback if flask-cors not installed
    @app.after_request
    def _add_cors(response):
        response.headers["Access-Control-Allow-Origin"] = _origin
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
        return response


# ---------------------------------------------------------------------------
# Frontend
# ---------------------------------------------------------------------------

@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@app.get("/api/health")
def health():
    try:
        con = connect()
        total = con.execute("SELECT COUNT(*) FROM sites").fetchone()[0]
        live = con.execute("SELECT COUNT(*) FROM sites WHERE is_live=1").fetchone()[0]
        other = con.execute("SELECT COUNT(*) FROM sites WHERE category='Other'").fetchone()[0]
        unchecked = con.execute("SELECT COUNT(*) FROM sites WHERE is_live IS NULL").fetchone()[0]
        return jsonify({
            "status": "ok",
            "total_sites": total,
            "live_sites": live,
            "dead_sites": total - live - unchecked,
            "unchecked_sites": unchecked,
            "other_category": other,
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        })
    except Exception as e:
        return jsonify({"status": "error", "detail": str(e)}), 500


# ---------------------------------------------------------------------------
# Categories
# ---------------------------------------------------------------------------

@app.get("/api/categories")
def categories():
    con = connect()
    rows = con.execute("""
        SELECT category AS name, COUNT(*) AS count
        FROM sites
        WHERE hidden = 0
        GROUP BY category
        ORDER BY count DESC
    """).fetchall()
    return jsonify([dict(r) for r in rows])


# ---------------------------------------------------------------------------
# States
# ---------------------------------------------------------------------------

@app.get("/api/states")
def states():
    con = connect()
    rows = con.execute("""
        SELECT state AS name, COUNT(*) AS count
        FROM sites
        WHERE state IS NOT NULL AND hidden = 0
        GROUP BY state
        ORDER BY state COLLATE NOCASE
    """).fetchall()
    return jsonify([dict(r) for r in rows])


# ---------------------------------------------------------------------------
# Sites list (search + filter + paginate)
# ---------------------------------------------------------------------------

@app.get("/api/sites")
def sites():
    # --- parse & validate inputs ---
    q        = request.args.get("q", "").strip()[:200]
    category = request.args.get("category", "").strip()
    state    = request.args.get("state", "").strip()
    live_only = request.args.get("live") == "1"
    hide_dead = request.args.get("hide_dead") == "1"
    try:
        page = max(int(request.args.get("page", 1)), 1)
        size = min(max(int(request.args.get("size", 50)), 1), 200)
    except (ValueError, TypeError):
        page, size = 1, 50

    # --- build WHERE clause ---
    conditions, params = ["hidden = 0"], []

    if q:
        conditions.append("(name LIKE ? OR domain LIKE ? OR url LIKE ?)")
        params += [f"%{q}%", f"%{q}%", f"%{q}%"]
    if category:
        conditions.append("category = ?")
        params.append(category)
    if state:
        conditions.append("state = ?")
        params.append(state)
    if live_only:
        conditions.append("is_live = 1")
    elif hide_dead:
        conditions.append("(is_live = 1 OR is_live IS NULL)")

    clause = "WHERE " + " AND ".join(conditions)

    con = connect()
    total = con.execute(
        f"SELECT COUNT(*) FROM sites {clause}", params
    ).fetchone()[0]

    rows = con.execute(
        f"""
        SELECT id, name, url, domain, category, state,
               is_live, last_checked, fail_count
        FROM sites {clause}
        ORDER BY name COLLATE NOCASE
        LIMIT ? OFFSET ?
        """,
        params + [size, (page - 1) * size],
    ).fetchall()

    return jsonify({
        "total": total,
        "page":  page,
        "size":  size,
        "pages": max((total + size - 1) // size, 1),
        "items": [dict(r) for r in rows],
    })


# ---------------------------------------------------------------------------
# User suggestions — site suggest karo
# ---------------------------------------------------------------------------
SUGGESTIONS_FILE = os.path.join(
    os.path.dirname(__file__), "..", "user_suggestions.jsonl"
)


@app.post("/api/suggest")
def suggest():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()[:200]
    url  = str(data.get("url", "")).strip()[:500]
    note = str(data.get("note", "")).strip()[:500]

    if not url:
        return jsonify({"ok": False, "error": "url required"}), 400

    entry = {
        "type": "suggest",
        "name": name,
        "url": url,
        "note": note,
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    with open(SUGGESTIONS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return jsonify({"ok": True, "message": "Shukriya! Aapka suggestion record ho gaya."})


# ---------------------------------------------------------------------------
# Broken link reports
# ---------------------------------------------------------------------------
REPORTS_FILE = os.path.join(
    os.path.dirname(__file__), "..", "broken_reports.jsonl"
)


@app.post("/api/report")
def report_broken():
    data = request.get_json(silent=True) or {}
    site_id = data.get("id")
    url     = str(data.get("url", "")).strip()[:500]

    if not url:
        return jsonify({"ok": False, "error": "url required"}), 400

    entry = {
        "type": "broken",
        "id": site_id,
        "url": url,
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    with open(REPORTS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return jsonify({"ok": True, "message": "Report mil gayi. Hum jald check karenge."})


# ---------------------------------------------------------------------------
# OPTIONS preflight (for CORS without flask-cors)
# ---------------------------------------------------------------------------

@app.route("/api/suggest", methods=["OPTIONS"])
@app.route("/api/report", methods=["OPTIONS"])
def _preflight():
    return "", 204


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    debug = os.environ.get("DEBUG", "1") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
