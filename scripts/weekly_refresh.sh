#!/usr/bin/env bash
# ============================================================
# SarkariPedia — Weekly refresh cron script
# ============================================================
#
# Crontab setup (crontab -e):
#   0 2 * * 0 /home/dell/Desktop/govsites/scripts/weekly_refresh.sh
#              (Every Sunday at 2:00 AM)
#
# Or with Docker:
#   0 2 * * 0 cd /home/dell/Desktop/govsites && docker compose run --rm worker
# ============================================================

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/crawl_$(date +%Y%m%d_%H%M%S).log"
PYTHON="python3"

mkdir -p "$LOG_DIR"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Weekly refresh shuru" | tee -a "$LOG_FILE"

cd "$PROJECT_DIR"

# Run crawler (seed + crawl + check + clean)
$PYTHON -m scraper.crawl all 2>&1 | tee -a "$LOG_FILE"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Weekly refresh khatam" | tee -a "$LOG_FILE"

# Stats dikhao
$PYTHON -m scraper.crawl stats 2>&1 | tee -a "$LOG_FILE"

# Purane logs clean karo (30 se zyada nahi rakhne)
ls -t "$LOG_DIR"/crawl_*.log 2>/dev/null | tail -n +31 | xargs -r rm --

echo "Done! Log: $LOG_FILE"

