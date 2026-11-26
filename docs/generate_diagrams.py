#!/usr/bin/env python3
"""
Generates ultra-crisp, high-resolution (300 DPI equivalent) PNG diagrams
for ALL 14 figures in the SarkariPedia Mini Project Report.
Uses Pillow with LiberationSans / LiberationMono fonts.
Saves to /home/dell/Desktop/govsites/report_diagrams/
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

F_SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
F_SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F_MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"
F_MONO_B = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"

def draw_fig_1_3_1():
    W, H = 1600, 420
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 20)
    f_sm = ImageFont.truetype(F_SANS, 14)

    steps = [
        ("Directory Crawl", "seeds.csv & sources.json", (240, 246, 253), (50, 100, 180)),
        ("Normalizer", "Canonical HTTPS, no www", (254, 245, 235), (210, 105, 20)),
        ("Classifier", "State Prefix + 15 Sectors", (254, 245, 235), (210, 105, 20)),
        ("SQLite Store", "gov_sites.db (WAL Mode)", (240, 246, 253), (50, 100, 180)),
        ("REST API", "Flask /api Endpoints", (240, 246, 253), (50, 100, 180)),
        ("Bilingual UI", "Vanilla HTML5 / CSS3", (235, 250, 240), (25, 140, 65)),
    ]

    box_w = 215
    box_h = 130
    x = 35
    for title, sub, bg, border in steps:
        d.rounded_rectangle([x, 100, x + box_w, 100 + box_h], radius=10, fill=bg, outline=border, width=2)
        d.text((x + 18, 125), title, fill=(20, 35, 60), font=f_b)
        d.text((x + 14, 165), sub, fill=(90, 105, 125), font=f_sm)
        if x + box_w < 1400:
            ax = x + box_w
            d.line([(ax, 165), (ax + 40, 165)], fill=(80, 95, 115), width=3)
            d.polygon([(ax + 40, 165), (ax + 28, 157), (ax + 28, 173)], fill=(80, 95, 115))
        x += box_w + 45

    d.rounded_rectangle([520, 290, 1340, 375], radius=10, fill=(235, 250, 240), outline=(25, 140, 65), width=2)
    d.text((550, 318), "Multi-threaded Live Health Daemon (HTTP HEAD / GET Probes)", fill=(20, 120, 50), font=f_b)
    d.line([(930, 230), (930, 290)], fill=(25, 140, 65), width=3)
    d.polygon([(930, 230), (922, 244), (938, 244)], fill=(25, 140, 65))

    p = os.path.join(OUT_DIR, "fig_1_3_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_1_4_1():
    W, H = 1500, 360
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 20)
    f_r = ImageFont.truetype(F_SANS, 16)
    f_loop = ImageFont.truetype(F_SANS_B, 18)

    phases = [
        ("1. Plan Sprint", "Scope & Seeds"),
        ("2. Develop", "Crawler & Heuristics"),
        ("3. Test & Audit", "Politeness & Schema"),
        ("4. Deploy", "Docker & Verification"),
        ("5. Review", "Backlog & Retrospective"),
    ]

    box_w = 220
    box_h = 120
    x = 45
    for title, sub in phases:
        d.rounded_rectangle([x, 100, x + box_w, 100 + box_h], radius=10, fill=(245, 249, 254), outline=(60, 110, 185), width=2)
        d.text((x + 20, 128), title, fill=(20, 35, 60), font=f_b)
        d.text((x + 18, 168), sub, fill=(90, 105, 125), font=f_r)
        if x + box_w < 1300:
            ax = x + box_w
            d.line([(ax, 160), (ax + 55, 160)], fill=(90, 105, 125), width=3)
            d.polygon([(ax + 55, 160), (ax + 42, 152), (ax + 42, 168)], fill=(90, 105, 125))
        x += box_w + 65

    d.arc([100, 25, 1380, 240], start=0, end=180, fill=(215, 105, 25), width=3)
    d.text((530, 35), "Continuous Sprint Retrospective & Backlog Refinement", fill=(210, 95, 15), font=f_loop)

    p = os.path.join(OUT_DIR, "fig_1_4_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_1_4_2():
    W, H = 1500, 520
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 18)
    f_r = ImageFont.truetype(F_SANS, 15)
    f_tag = ImageFont.truetype(F_SANS_B, 15)

    d.rounded_rectangle([30, 190, 230, 290], radius=8, fill=(240, 246, 253), outline=(50, 100, 180), width=2)
    d.text((50, 218), "Directory Source", fill=(20, 35, 60), font=f_b)
    d.text((55, 248), "(sources.json / seeds)", fill=(90, 105, 125), font=f_r)

    d.line([(230, 240), (300, 240)], fill=(70, 85, 105), width=3)
    d.polygon([(300, 240), (288, 232), (288, 248)], fill=(70, 85, 105))

    d.polygon([(400, 150), (500, 240), (400, 330), (300, 240)], fill=(254, 245, 235), outline=(210, 105, 20), width=2)
    d.text((345, 228), "Official TLD?", fill=(160, 70, 5), font=f_b)

    d.line([(400, 330), (400, 410)], fill=(210, 45, 45), width=3)
    d.polygon([(400, 410), (392, 398), (408, 398)], fill=(210, 45, 45))
    d.text((415, 360), "No", fill=(210, 45, 45), font=f_tag)
    d.rounded_rectangle([320, 410, 480, 470], radius=6, fill=(255, 238, 238), outline=(210, 45, 45), width=2)
    d.text((345, 430), "Discard URL", fill=(180, 30, 30), font=f_b)

    d.line([(500, 240), (580, 240)], fill=(25, 140, 65), width=3)
    d.polygon([(580, 240), (568, 232), (568, 248)], fill=(25, 140, 65))
    d.text((525, 215), "Yes", fill=(25, 140, 65), font=f_tag)

    d.rounded_rectangle([580, 190, 780, 290], radius=8, fill=(240, 246, 253), outline=(50, 100, 180), width=2)
    d.text((605, 218), "Robots Check &", fill=(20, 35, 60), font=f_b)
    d.text((615, 248), "Rate Limit (1.2s)", fill=(90, 105, 125), font=f_r)

    d.line([(780, 240), (850, 240)], fill=(70, 85, 105), width=3)
    d.polygon([(850, 240), (838, 232), (838, 248)], fill=(70, 85, 105))

    d.rounded_rectangle([850, 190, 1070, 290], radius=8, fill=(240, 246, 253), outline=(50, 100, 180), width=2)
    d.text((880, 218), "Fetch & Normalize", fill=(20, 35, 60), font=f_b)
    d.text((885, 248), "Extract Canonical URL", fill=(90, 105, 125), font=f_r)

    d.line([(1070, 240), (1140, 240)], fill=(70, 85, 105), width=3)
    d.polygon([(1140, 240), (1128, 232), (1128, 248)], fill=(70, 85, 105))

    d.rounded_rectangle([1140, 190, 1460, 290], radius=8, fill=(235, 250, 240), outline=(25, 140, 65), width=2)
    d.text((1170, 218), "Heuristic Classifier", fill=(20, 120, 45), font=f_b)
    d.text((1175, 248), "Tag Sector & State -> SQLite", fill=(20, 100, 40), font=f_r)

    p = os.path.join(OUT_DIR, "fig_1_4_2.png")
    im.save(p, dpi=(300, 300))

def draw_fig_2_3_1():
    W, H = 1500, 360
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 20)
    f_r = ImageFont.truetype(F_SANS, 16)

    d.rounded_rectangle([40, 30, W - 40, 320], radius=12, fill=(248, 250, 253), outline=(175, 190, 210), width=2)
    d.text((65, 45), "HOST OPERATING SYSTEM (Linux / Ubuntu / Debian)", fill=(40, 55, 75), font=f_b)

    d.rounded_rectangle([80, 85, W - 80, 295], radius=10, fill=(255, 255, 255), outline=(35, 105, 200), width=2)
    d.text((105, 100), "DOCKER CONTAINER (Python 3.11-slim Alpine Base Image)", fill=(20, 85, 170), font=f_b)

    components = [
        ("Gunicorn WSGI Server", "Port 5000 (Exposed)", (240, 246, 253), (50, 100, 180)),
        ("Flask Application Core", "REST API & Template Engine", (254, 245, 235), (210, 105, 20)),
        ("SQLite Database Engine", "WAL Mode (Concurrent Reads)", (240, 246, 253), (50, 100, 180)),
        ("Periodic Cron Jobs", "Nightly Crawler & Health Probe", (235, 250, 240), (25, 140, 65)),
    ]

    bx = 105
    bw = 285
    bh = 125
    for title, sub, bg, border in components:
        d.rounded_rectangle([bx, 140, bx + bw, 140 + bh], radius=8, fill=bg, outline=border, width=2)
        d.text((bx + 16, 165), title, fill=(20, 35, 60), font=f_b)
        d.text((bx + 14, 205), sub, fill=(90, 105, 125), font=f_r)
        bx += bw + 32

    p = os.path.join(OUT_DIR, "fig_2_3_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_3_1_2_1():
    W, H = 1400, 320
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 20)
    f_r = ImageFont.truetype(F_SANS, 16)
    f_loop = ImageFont.truetype(F_SANS_B, 18)

    nodes = [
        ("1. Elicitation", "Audits & Pain Points"),
        ("2. Categorization", "Functional vs NFR"),
        ("3. Feasibility", "Technical & Legal"),
        ("4. Baseline SRS", "Traceable Matrix"),
    ]
    box_w = 265
    box_h = 120
    x = 45
    for t, s in nodes:
        d.rounded_rectangle([x, 85, x + box_w, 85 + box_h], radius=10, fill=(245, 249, 254), outline=(50, 100, 180), width=2)
        d.text((x + 22, 115), t, fill=(20, 35, 60), font=f_b)
        d.text((x + 18, 155), s, fill=(90, 105, 125), font=f_r)
        if x + box_w < 1200:
            ax = x + box_w
            d.line([(ax, 145), (ax + 55, 145)], fill=(90, 105, 125), width=3)
            d.polygon([(ax + 55, 145), (ax + 42, 137), (ax + 42, 153)], fill=(90, 105, 125))
        x += box_w + 65

    d.arc([80, 20, 1320, 220], start=0, end=180, fill=(210, 105, 20), width=3)
    d.text((490, 28), "Continuous Stakeholder Verification & Review", fill=(200, 95, 15), font=f_loop)

    p = os.path.join(OUT_DIR, "fig_3_1_2_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_4_1_1():
    W, H = 1500, 500
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 22)
    f_r = ImageFont.truetype(F_SANS, 16.5)
    f_sub = ImageFont.truetype(F_SANS, 15)

    d.rounded_rectangle([50, 25, W - 50, 155], radius=10, fill=(242, 247, 254), outline=(50, 105, 190), width=2)
    d.text((80, 45), "PRESENTATION TIER (USER INTERFACE)", fill=(20, 60, 140), font=f_b)
    d.text((80, 85), "Bilingual Responsive Client (HTML5 / Vanilla CSS3 / Modern ES6 JavaScript) - Mobile First", fill=(60, 75, 95), font=f_r)
    d.text((80, 115), "Instant Live Search, Debounced Query Filters, Status Badges, Dynamic Suggestion & Broken Link Modals", fill=(100, 115, 135), font=f_sub)

    d.line([(W // 2, 155), (W // 2, 185)], fill=(70, 85, 105), width=3)
    d.polygon([(W // 2, 185), (W // 2 - 8, 173), (W // 2 + 8, 173)], fill=(70, 85, 105))

    d.rounded_rectangle([50, 185, W - 50, 315], radius=10, fill=(254, 245, 235), outline=(210, 105, 20), width=2)
    d.text((80, 205), "APPLICATION LOGIC TIER (CORE ENGINES & REST API)", fill=(170, 75, 10), font=f_b)
    d.text((80, 245), "Flask RESTful API Microservices: GET /api/sites, /api/categories, /api/states, POST /api/suggest, /api/report", fill=(60, 75, 95), font=f_r)
    d.text((80, 275), "Asynchronous Harvester Engine: RFC 9309 BFS Crawler, Canonical Normalizer, Deterministic Classifier, Health Daemon", fill=(100, 115, 135), font=f_sub)

    d.line([(W // 2, 315), (W // 2, 345)], fill=(70, 85, 105), width=3)
    d.polygon([(W // 2, 345), (W // 2 - 8, 333), (W // 2 + 8, 333)], fill=(70, 85, 105))

    d.rounded_rectangle([50, 345, W - 50, 475], radius=10, fill=(235, 250, 240), outline=(25, 140, 65), width=2)
    d.text((80, 365), "DATA PERSISTENCE TIER (STORAGE & CACHING)", fill=(20, 115, 45), font=f_b)
    d.text((80, 405), "SQLite Relational Database (gov_sites.db with WAL Mode) + Covering B-Tree Indices", fill=(60, 75, 95), font=f_r)
    d.text((80, 435), "Structured Schema: 'sites' Table, 'user_suggestions' Table, 'broken_reports' Table, Append-only JSONL Logs", fill=(100, 115, 135), font=f_sub)

    p = os.path.join(OUT_DIR, "fig_4_1_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_4_3_2():
    W, H = 1500, 500
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 20)
    f_mono = ImageFont.truetype(F_MONO, 15)

    cw = 600
    cx = (W - cw) // 2
    d.rounded_rectangle([cx, 30, cx + cw, 470], radius=10, fill=(245, 249, 254), outline=(50, 100, 180), width=2)
    d.rectangle([cx, 30, cx + cw, 80], fill=(50, 100, 180))
    d.text((cx + 210, 42), "sites TABLE", fill=(255, 255, 255), font=f_b)

    fields = [
        ("PK", "id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("  ", "name", "TEXT NOT NULL"),
        ("UQ", "url", "TEXT NOT NULL UNIQUE"),
        ("IX", "domain", "TEXT NOT NULL (B-Tree Index)"),
        ("IX", "category", "TEXT NOT NULL (B-Tree Index)"),
        ("IX", "state", "TEXT NULLABLE (B-Tree Index)"),
        ("  ", "source", "TEXT NULLABLE"),
        ("IX", "is_live", "INTEGER (1=Live, 0=Down, NULL=Pending)"),
        ("  ", "fail_count", "INTEGER DEFAULT 0 (3-Strike Rule)"),
        ("IX", "hidden", "INTEGER DEFAULT 0"),
        ("  ", "last_checked", "TEXT ISO-8601 TIMESTAMP"),
    ]
    fy = 95
    for tag, col, ctype in fields:
        d.text((cx + 25, fy), tag, fill=(200, 90, 15) if tag in ("PK", "UQ") else (40, 100, 180), font=f_mono)
        d.text((cx + 70, fy), col, fill=(20, 35, 55), font=f_b)
        d.text((cx + 220, fy), ctype, fill=(80, 95, 115), font=f_mono)
        fy += 33

    lx = 40
    lw = 360
    d.rounded_rectangle([lx, 110, lx + lw, 390], radius=8, fill=(254, 245, 235), outline=(210, 105, 20), width=2)
    d.rectangle([lx, 110, lx + lw, 155], fill=(210, 105, 20))
    d.text((lx + 90, 120), "user_suggestions", fill=(255, 255, 255), font=f_b)

    sug_fields = [
        ("PK", "id", "INTEGER AUTOINC"),
        ("  ", "name", "TEXT NOT NULL"),
        ("  ", "url", "TEXT NOT NULL"),
        ("  ", "note", "TEXT NULLABLE"),
        ("  ", "ts", "TIMESTAMP"),
    ]
    sy = 175
    for tag, col, ctype in sug_fields:
        d.text((lx + 20, sy), f"{col}: {ctype}", fill=(30, 45, 60), font=f_mono)
        sy += 40

    d.line([(lx + lw, 250), (cx, 250)], fill=(120, 135, 155), width=2)
    d.polygon([(cx, 250), (cx - 12, 242), (cx - 12, 258)], fill=(120, 135, 155))

    rx = W - 40 - lw
    d.rounded_rectangle([rx, 110, rx + lw, 390], radius=8, fill=(255, 238, 238), outline=(210, 45, 45), width=2)
    d.rectangle([rx, 110, rx + lw, 155], fill=(210, 45, 45))
    d.text((rx + 105, 120), "broken_reports", fill=(255, 255, 255), font=f_b)

    rep_fields = [
        ("PK", "id", "INTEGER AUTOINC"),
        ("FK", "site_id", "INTEGER -> sites.id"),
        ("  ", "url", "TEXT NOT NULL"),
        ("  ", "comment", "TEXT NULLABLE"),
        ("  ", "ts", "TIMESTAMP"),
    ]
    ry = 175
    for tag, col, ctype in rep_fields:
        d.text((rx + 20, ry), f"{col}: {ctype}", fill=(30, 45, 60), font=f_mono)
        ry += 40

    d.line([(cx + cw, 250), (rx, 250)], fill=(120, 135, 155), width=2)
    d.polygon([(rx, 250), (rx - 12, 242), (rx - 12, 258)], fill=(120, 135, 155))

    p = os.path.join(OUT_DIR, "fig_4_3_2.png")
    im.save(p, dpi=(300, 300))

def draw_fig_4_4_1():
    W, H = 1400, 350
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 20)
    f_r = ImageFont.truetype(F_SANS, 16)

    d.rectangle([50, 100, 320, 240], fill=(240, 246, 253), outline=(50, 100, 180), width=2)
    d.text((80, 140), "Directory Portals", fill=(20, 35, 60), font=f_b)
    d.text((85, 180), "(india.gov.in, state dirs)", fill=(90, 105, 125), font=f_r)

    d.ellipse([540, 70, 860, 270], fill=(254, 245, 235), outline=(210, 105, 20), width=2)
    d.text((585, 140), "0.0 SarkariPedia", fill=(170, 75, 10), font=f_b)
    d.text((605, 180), "Portal Engine", fill=(170, 75, 10), font=f_r)

    d.rectangle([1080, 100, 1350, 240], fill=(235, 250, 240), outline=(25, 140, 65), width=2)
    d.text((1140, 140), "Citizen User", fill=(20, 115, 45), font=f_b)
    d.text((1120, 180), "(Mobile / Desktop Web)", fill=(20, 115, 45), font=f_r)

    d.line([(320, 170), (540, 170)], fill=(70, 85, 105), width=3)
    d.polygon([(540, 170), (528, 162), (528, 178)], fill=(70, 85, 105))
    d.text((365, 135), "Raw Portal HTML", fill=(70, 85, 105), font=f_r)

    d.line([(860, 145), (1080, 145)], fill=(25, 140, 65), width=3)
    d.polygon([(1080, 145), (1068, 137), (1068, 153)], fill=(25, 140, 65))
    d.text((895, 115), "Verified Links & Badges", fill=(25, 140, 65), font=f_r)

    d.line([(1080, 195), (860, 195)], fill=(50, 100, 180), width=3)
    d.polygon([(860, 195), (872, 187), (872, 203)], fill=(50, 100, 180))
    d.text((915, 205), "Search & Filter Queries", fill=(50, 100, 180), font=f_r)

    p = os.path.join(OUT_DIR, "fig_4_4_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_4_4_2():
    W, H = 1500, 380
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 18)
    f_r = ImageFont.truetype(F_SANS, 15)

    d.ellipse([50, 100, 280, 260], fill=(240, 246, 253), outline=(50, 100, 180), width=2)
    d.text((90, 155), "1.0 Directory", fill=(20, 35, 60), font=f_b)
    d.text((115, 190), "Crawler", fill=(20, 35, 60), font=f_r)

    d.ellipse([380, 100, 610, 260], fill=(254, 245, 235), outline=(210, 105, 20), width=2)
    d.text((410, 155), "2.0 Heuristic", fill=(170, 75, 10), font=f_b)
    d.text((425, 190), "Classifier", fill=(170, 75, 10), font=f_r)

    d.line([(710, 120), (950, 120)], fill=(50, 50, 50), width=3)
    d.line([(710, 240), (950, 240)], fill=(50, 50, 50), width=3)
    d.text((735, 168), "D1: sites Relational Store", fill=(20, 35, 55), font=f_b)

    d.ellipse([1050, 100, 1280, 260], fill=(235, 250, 240), outline=(25, 140, 65), width=2)
    d.text((1085, 155), "3.0 REST API", fill=(20, 115, 45), font=f_b)
    d.text((1115, 190), "Service", fill=(20, 115, 45), font=f_r)

    d.rectangle([1340, 130, 1470, 230], fill=(245, 247, 250), outline=(80, 95, 115), width=2)
    d.text((1355, 168), "Citizen", fill=(30, 45, 60), font=f_b)

    d.line([(280, 180), (380, 180)], fill=(70, 85, 105), width=3)
    d.polygon([(380, 180), (368, 172), (368, 188)], fill=(70, 85, 105))
    d.text((295, 150), "Raw Links", fill=(70, 85, 105), font=f_r)

    d.line([(610, 180), (710, 180)], fill=(70, 85, 105), width=3)
    d.polygon([(710, 180), (698, 172), (698, 188)], fill=(70, 85, 105))
    d.text((615, 150), "Categorized", fill=(70, 85, 105), font=f_r)

    d.line([(950, 180), (1050, 180)], fill=(70, 85, 105), width=3)
    d.polygon([(1050, 180), (1038, 172), (1038, 188)], fill=(70, 85, 105))
    d.text((965, 150), "Records", fill=(70, 85, 105), font=f_r)

    d.line([(1280, 180), (1340, 180)], fill=(25, 140, 65), width=3)
    d.polygon([(1340, 180), (1328, 172), (1328, 188)], fill=(25, 140, 65))

    p = os.path.join(OUT_DIR, "fig_4_4_2.png")
    im.save(p, dpi=(300, 300))

def draw_fig_4_5_1():
    W, H = 1400, 480
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 18)
    f_r = ImageFont.truetype(F_SANS, 15)

    d.ellipse([70, 120, 110, 160], fill=(240, 246, 253), outline=(50, 100, 180), width=2)
    d.line([(90, 160), (90, 240)], fill=(50, 100, 180), width=3)
    d.line([(50, 190), (130, 190)], fill=(50, 100, 180), width=3)
    d.line([(90, 240), (60, 300)], fill=(50, 100, 180), width=3)
    d.line([(90, 240), (120, 300)], fill=(50, 100, 180), width=3)
    d.text((45, 315), "Citizen User", fill=(20, 40, 80), font=f_b)

    cases = [
        ("Search Portals by Keyword / Ministry", 50),
        ("Filter by 15 Sectors & 36 States", 130),
        ("Toggle Bilingual Hindi/English UI", 210),
        ("Suggest New Official Government Portal", 290),
        ("Report Broken / Defunct Portal Link", 370),
    ]

    for ctitle, cy in cases:
        d.rounded_rectangle([320, cy, 780, cy + 55], radius=25, fill=(245, 249, 255), outline=(50, 100, 180), width=2)
        d.text((360, cy + 16), ctitle, fill=(20, 35, 60), font=f_r)
        d.line([(130, 200), (320, cy + 27)], fill=(130, 145, 165), width=2)

    d.ellipse([1270, 150, 1310, 190], fill=(255, 245, 235), outline=(210, 105, 20), width=2)
    d.line([(1290, 190), (1290, 270)], fill=(210, 105, 20), width=3)
    d.line([(1250, 220), (1330, 220)], fill=(210, 105, 20), width=3)
    d.line([(1290, 270), (1260, 330)], fill=(210, 105, 20), width=3)
    d.line([(1290, 270), (1320, 330)], fill=(210, 105, 20), width=3)
    d.text((1225, 345), "Crawler Daemon", fill=(170, 75, 10), font=f_b)

    d.rounded_rectangle([860, 140, 1200, 195], radius=25, fill=(255, 245, 235), outline=(210, 105, 20), width=2)
    d.text((885, 156), "Scheduled Directory Crawl", fill=(170, 75, 10), font=f_r)
    d.line([(1250, 220), (1200, 167)], fill=(210, 105, 20), width=2)

    d.rounded_rectangle([860, 250, 1200, 305], radius=25, fill=(255, 245, 235), outline=(210, 105, 20), width=2)
    d.text((890, 266), "Parallel Live Health Probe", fill=(170, 75, 10), font=f_r)
    d.line([(1250, 220), (1200, 277)], fill=(210, 105, 20), width=2)

    p = os.path.join(OUT_DIR, "fig_4_5_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_4_6_1():
    W, H = 1400, 360
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 18)
    f_r = ImageFont.truetype(F_SANS, 15)

    d.rounded_rectangle([40, 110, 280, 220], radius=8, fill=(240, 246, 253), outline=(50, 100, 180), width=2)
    d.text((75, 145), "Discovered URL", fill=(20, 35, 60), font=f_b)
    d.text((65, 180), "Hostname & Anchors", fill=(90, 105, 125), font=f_r)

    d.line([(280, 165), (370, 165)], fill=(70, 85, 105), width=3)
    d.polygon([(370, 165), (358, 157), (358, 173)], fill=(70, 85, 105))

    d.polygon([(470, 90), (570, 165), (470, 240), (370, 165)], fill=(254, 245, 235), outline=(210, 105, 20), width=2)
    d.text((415, 153), "State Prefix?", fill=(170, 75, 10), font=f_b)

    d.line([(470, 90), (470, 45), (660, 45)], fill=(25, 140, 65), width=3)
    d.polygon([(660, 45), (648, 37), (648, 53)], fill=(25, 140, 65))
    d.text((490, 60), "Yes", fill=(25, 140, 65), font=f_b)
    d.rounded_rectangle([660, 20, 1000, 70], radius=6, fill=(235, 250, 240), outline=(25, 140, 65), width=2)
    d.text((680, 34), "Tag: State Governments (e.g. UP, MP)", fill=(20, 115, 45), font=f_r)

    d.line([(570, 165), (680, 165)], fill=(70, 85, 105), width=3)
    d.polygon([(680, 165), (668, 157), (668, 173)], fill=(70, 85, 105))
    d.text((605, 140), "No", fill=(70, 85, 105), font=f_b)

    d.polygon([(780, 90), (880, 165), (780, 240), (680, 165)], fill=(254, 245, 235), outline=(210, 105, 20), width=2)
    d.text((720, 153), "Sector Match?", fill=(170, 75, 10), font=f_b)

    d.line([(880, 165), (990, 165)], fill=(25, 140, 65), width=3)
    d.polygon([(990, 165), (978, 157), (978, 173)], fill=(25, 140, 65))
    d.text((915, 140), "Yes", fill=(25, 140, 65), font=f_b)
    d.rounded_rectangle([990, 140, 1340, 190], radius=6, fill=(235, 250, 240), outline=(25, 140, 65), width=2)
    d.text((1015, 154), "Tag: 1 of 14 Functional Sectors", fill=(20, 115, 45), font=f_r)

    d.line([(780, 240), (780, 290), (990, 290)], fill=(210, 45, 45), width=3)
    d.polygon([(990, 290), (978, 282), (978, 298)], fill=(210, 45, 45))
    d.text((800, 260), "No", fill=(210, 45, 45), font=f_b)
    d.rounded_rectangle([990, 265, 1340, 315], radius=6, fill=(255, 238, 238), outline=(210, 45, 45), width=2)
    d.text((1015, 279), "Tag: 'Other' (Queued for Audit)", fill=(180, 30, 30), font=f_r)

    p = os.path.join(OUT_DIR, "fig_4_6_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_5_5_1():
    W, H = 1600, 780
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)

    f_title = ImageFont.truetype(F_SANS_B, 22)
    f_sub = ImageFont.truetype(F_SANS, 14)
    f_h2 = ImageFont.truetype(F_SANS_B, 15.5)
    f_body = ImageFont.truetype(F_SANS, 13)
    f_body_b = ImageFont.truetype(F_SANS_B, 13)
    f_mono = ImageFont.truetype(F_MONO, 12.5)
    f_badge = ImageFont.truetype(F_SANS_B, 11.5)

    d.rounded_rectangle([10, 10, W - 10, H - 10], radius=10, fill=(255, 255, 255), outline=(180, 195, 215), width=2)
    d.rounded_rectangle([10, 10, W - 10, 52], radius=10, fill=(238, 242, 248))
    d.rectangle([10, 40, W - 10, 52], fill=(238, 242, 248))
    d.line([(10, 52), (W - 10, 52)], fill=(205, 215, 228), width=1)

    d.ellipse([26, 25, 38, 37], fill=(235, 90, 85))
    d.ellipse([46, 25, 58, 37], fill=(245, 185, 60))
    d.ellipse([66, 25, 78, 37], fill=(70, 195, 90))

    d.rounded_rectangle([120, 18, 920, 44], radius=6, fill=(255, 255, 255), outline=(195, 208, 222), width=1)
    d.text((135, 24), "https://sarkaripedia.gov.in/directory?sector=citizen_services&state=all", fill=(70, 80, 95), font=f_mono)

    d.rectangle([10, 53, W - 10, 125], fill=(250, 252, 255))
    d.line([(10, 125), (W - 10, 125)], fill=(220, 228, 238), width=1)

    d.text((35, 64), "SarkariPedia", fill=(20, 45, 85), font=f_title)
    d.text((35, 96), "National Single-Window Directory of Verified Indian Government Portals", fill=(100, 115, 135), font=f_sub)

    d.rounded_rectangle([W - 310, 68, W - 175, 108], radius=6, fill=(240, 244, 250), outline=(180, 195, 215), width=1)
    d.text((W - 295, 80), "English / Hindi", fill=(30, 60, 110), font=f_body_b)

    d.rounded_rectangle([W - 160, 68, W - 35, 108], radius=6, fill=(225, 110, 25), outline=(200, 90, 15), width=1)
    d.text((W - 145, 80), "+ Suggest Site", fill=(255, 255, 255), font=f_body_b)

    d.rectangle([10, 126, W - 10, 188], fill=(244, 247, 251))
    d.line([(10, 188), (W - 10, 188)], fill=(220, 228, 238), width=1)

    d.rounded_rectangle([35, 138, 550, 176], radius=6, fill=(255, 255, 255), outline=(190, 202, 218), width=1)
    d.text((50, 148), "Search portal name, ministry, or service (e.g. Aadhaar, ITR, Kisan)...", fill=(130, 140, 155), font=f_body)

    d.rounded_rectangle([565, 138, 765, 176], radius=6, fill=(255, 255, 255), outline=(190, 202, 218), width=1)
    d.text((580, 148), "State: All India (Central)  v", fill=(50, 65, 85), font=f_body)

    d.rounded_rectangle([780, 147, 798, 165], radius=3, fill=(25, 135, 84))
    d.line([(784, 156), (788, 161), (795, 151)], fill=(255, 255, 255), width=2)
    d.text((808, 148), "Live Sites Only", fill=(40, 55, 75), font=f_body_b)

    d.text((W - 350, 148), "Showing 42 verified portals in Citizen Services", fill=(80, 95, 115), font=f_body_b)

    chips = [
        ("All Portals (1,240)", False),
        ("Citizen Services (142)", True),
        ("Finance & Revenue (78)", False),
        ("Agriculture & Farmers (86)", False),
        ("Education & Learning (112)", False),
        ("Transport & Highways (62)", False),
    ]
    cx = 35
    for ctitle, is_active in chips:
        cw = int(d.textlength(ctitle, font=f_body_b)) + 26
        if is_active:
            d.rounded_rectangle([cx, 202, cx + cw, 234], radius=16, fill=(24, 75, 150), outline=(20, 60, 120), width=1)
            d.text((cx + 13, 210), ctitle, fill=(255, 255, 255), font=f_body_b)
        else:
            d.rounded_rectangle([cx, 202, cx + cw, 234], radius=16, fill=(245, 247, 250), outline=(210, 218, 228), width=1)
            d.text((cx + 13, 210), ctitle, fill=(80, 95, 115), font=f_body)
        cx += cw + 12

    cards = [
        {
            "title": "UIDAI - Aadhaar Citizen Identity Portal",
            "url": "https://uidai.gov.in",
            "ministry": "Ministry of Electronics & Information Technology (MeitY)",
            "category": "Citizen Services & Identity",
            "scope": "Central / All India",
            "status": "LIVE (200 OK)",
            "latency": "142 ms",
            "services": ["Download Aadhaar", "Order PVC Card", "Verify Mobile / Email", "Enrolment Status"],
        },
        {
            "title": "Income Tax e-Filing Portal (CBDT)",
            "url": "https://incometax.gov.in",
            "ministry": "Central Board of Direct Taxes, Ministry of Finance",
            "category": "Finance & Revenue",
            "scope": "Central / All India",
            "status": "LIVE (200 OK)",
            "latency": "195 ms",
            "services": ["File ITR Online", "Link Aadhaar to PAN", "Verify PAN Status", "View Form 26AS / AIS"],
        },
        {
            "title": "Parivahan Sewa - Driving Licence & RC Portal",
            "url": "https://parivahan.gov.in",
            "ministry": "Ministry of Road Transport and Highways (MoRTH)",
            "category": "Transport & Mobility",
            "scope": "Central / State RTOs",
            "status": "LIVE (200 OK)",
            "latency": "165 ms",
            "services": ["Apply Driving Licence", "Vehicle RC Status", "Pay E-Challan", "International Permit"],
        },
        {
            "title": "PM Kisan Samman Nidhi (PM-KISAN)",
            "url": "https://pmkisan.gov.in",
            "ministry": "Ministry of Agriculture and Farmers Welfare",
            "category": "Agriculture & Farmers",
            "scope": "Central / All India",
            "status": "LIVE (200 OK)",
            "latency": "180 ms",
            "services": ["Beneficiary Status", "Farmer e-KYC", "New Registration", "Installment Ledger"],
        },
    ]

    card_coords = [
        (35, 250, 785, 475),
        (815, 250, W - 35, 475),
        (35, 495, 785, 720),
        (815, 495, W - 35, 720),
    ]

    for (x1, y1, x2, y2), c in zip(card_coords, cards):
        d.rounded_rectangle([x1, y1, x2, y2], radius=8, fill=(255, 255, 255), outline=(215, 225, 235), width=2)
        d.rounded_rectangle([x1, y1, x2, y1 + 36], radius=8, fill=(248, 250, 253))
        d.rectangle([x1, y1 + 25, x2, y1 + 36], fill=(248, 250, 253))
        d.line([(x1, y1 + 36), (x2, y1 + 36)], fill=(225, 232, 240), width=1)

        d.rounded_rectangle([x1 + 14, y1 + 8, x1 + 130, y1 + 28], radius=4, fill=(235, 250, 240), outline=(75, 180, 105), width=1)
        d.ellipse([x1 + 22, y1 + 15, x1 + 28, y1 + 21], fill=(30, 150, 60))
        d.text((x1 + 34, y1 + 10), c["status"], fill=(20, 120, 45), font=f_badge)

        d.text((x1 + 140, y1 + 11), f"Latency: {c['latency']}  •  SSL: TLS 1.3", fill=(100, 115, 130), font=f_badge)
        d.text((x1 + 14, y1 + 46), c["title"], fill=(20, 35, 60), font=f_h2)
        d.text((x1 + 14, y1 + 72), c["url"], fill=(25, 100, 210), font=f_mono)

        d.text((x1 + 14, y1 + 98), f"Department: {c['ministry']}", fill=(75, 85, 100), font=f_body)
        d.text((x1 + 14, y1 + 118), f"Category: {c['category']}   |   Scope: {c['scope']}", fill=(90, 100, 115), font=f_body)
        d.text((x1 + 14, y1 + 142), "Key Citizen Services Available Online:", fill=(40, 50, 65), font=f_body_b)

        tx = x1 + 14
        ty = y1 + 165
        for sname in c["services"]:
            tw = int(d.textlength(sname, font=f_badge)) + 16
            if tx + tw > x2 - 14:
                break
            d.rounded_rectangle([tx, ty, tx + tw, ty + 24], radius=4, fill=(242, 246, 252), outline=(205, 218, 235), width=1)
            d.text((tx + 8, ty + 5), sname, fill=(35, 65, 110), font=f_badge)
            tx += tw + 8

        d.rounded_rectangle([x2 - 140, y1 + 185, x2 - 15, y1 + 213], radius=4, fill=(240, 245, 252), outline=(180, 205, 235), width=1)
        d.text((x2 - 128, y1 + 192), "Open Portal ->", fill=(20, 80, 180), font=f_body_b)

    p = os.path.join(OUT_DIR, "fig_5_5_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_5_6_1():
    W, H = 1600, 550
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)

    f_r = ImageFont.truetype(F_SANS, 16)
    f_num = ImageFont.truetype(F_SANS_B, 16)
    f_axis = ImageFont.truetype(F_SANS, 16)

    x_start = 550
    x_end = 1520
    total_weeks = 6.0
    scale = (x_end - x_start) / total_weeks

    y_top = 30
    y_bottom = 460
    for w in range(0, 7):
        wx = x_start + int(w * scale)
        d.line([(wx, y_top), (wx, y_bottom)], fill=(225, 232, 240), width=1)
        d.text((wx - 6, y_bottom + 10), str(w), fill=(30, 40, 50), font=f_num)

    d.line([(x_start, y_bottom), (x_end, y_bottom)], fill=(30, 40, 50), width=2)
    d.line([(x_start, y_top), (x_start, y_bottom)], fill=(30, 40, 50), width=2)

    x_label = "Weeks from start (planned schedule, approximate)"
    lx = x_start + int((x_end - x_start - d.textlength(x_label, font=f_axis)) / 2)
    d.text((lx, y_bottom + 42), x_label, fill=(30, 40, 50), font=f_axis)

    phases = [
        ("1  Project Setup, Domain Rules & Seeds", 0.0, 1.0),
        ("2  BFS Directory Crawler Implementation", 1.0, 2.0),
        ("3  Domain Normalizer & Heuristic Classifier", 2.0, 3.2),
        ("4  Multi-threaded Live Health Daemon", 3.0, 4.3),
        ("5  SQLite Schema, Indices & REST API", 3.8, 5.0),
        ("6  Bilingual Responsive Web Frontend", 4.5, 5.6),
        ("7  Docker Containerization & Verification", 5.2, 6.0),
    ]

    bar_h = 32
    y_spacing = 58
    curr_y = 45

    for label, w_start, w_end in phases:
        d.text((30, curr_y + 6), label, fill=(20, 30, 45), font=f_r)
        bx1 = x_start + int(w_start * scale)
        bx2 = x_start + int(w_end * scale)
        d.rectangle([bx1, curr_y, bx2, curr_y + bar_h], fill=(142, 170, 212), outline=(44, 77, 117), width=2)
        curr_y += y_spacing

    p = os.path.join(OUT_DIR, "fig_5_6_1.png")
    im.save(p, dpi=(300, 300))

def draw_fig_6_2_1():
    W, H = 1400, 320
    im = Image.new("RGB", (W, H), color=(255, 255, 255))
    d = ImageDraw.Draw(im)
    f_b = ImageFont.truetype(F_SANS_B, 20)
    f_r = ImageFont.truetype(F_SANS, 16)
    f_loop = ImageFont.truetype(F_SANS_B, 18)

    nodes = [
        ("1. Unit Tests", "Classifier & Normalizer"),
        ("2. Crawler Integration", "Robots & 1.2s Rate Limit"),
        ("3. Contract Tests", "API Schema & CORS"),
        ("4. Client E2E", "Bilingual UI & Badges"),
    ]
    box_w = 265
    box_h = 120
    x = 45
    for t, s in nodes:
        d.rounded_rectangle([x, 85, x + box_w, 85 + box_h], radius=10, fill=(245, 249, 254), outline=(50, 100, 180), width=2)
        d.text((x + 20, 115), t, fill=(20, 35, 60), font=f_b)
        d.text((x + 18, 155), s, fill=(90, 105, 125), font=f_r)
        if x + box_w < 1200:
            ax = x + box_w
            d.line([(ax, 145), (ax + 55, 145)], fill=(90, 105, 125), width=3)
            d.polygon([(ax + 55, 145), (ax + 42, 137), (ax + 42, 153)], fill=(90, 105, 125))
        x += box_w + 65

    d.arc([80, 20, 1320, 220], start=0, end=180, fill=(25, 140, 65), width=3)
    d.text((540, 28), "Continuous Agile Verification Cycle", fill=(20, 120, 45), font=f_loop)

    p = os.path.join(OUT_DIR, "fig_6_2_1.png")
    im.save(p, dpi=(300, 300))

if __name__ == "__main__":
    print("Generating all 14 diagrams in report_diagrams...")
    draw_fig_1_3_1()
    draw_fig_1_4_1()
    draw_fig_1_4_2()
    draw_fig_2_3_1()
    draw_fig_3_1_2_1()
    draw_fig_4_1_1()
    draw_fig_4_3_2()
    draw_fig_4_4_1()
    draw_fig_4_4_2()
    draw_fig_4_5_1()
    draw_fig_4_6_1()
    draw_fig_5_5_1()
    draw_fig_5_6_1()
    draw_fig_6_2_1()
    print("All 14 diagrams generated successfully in", OUT_DIR)
