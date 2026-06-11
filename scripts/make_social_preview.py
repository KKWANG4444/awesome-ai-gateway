#!/usr/bin/env python3
"""Render the 1280x640 GitHub social-preview card to assets/social-preview.png.

Pure Pillow, GitHub-dark palette. Re-run after major README changes so the
mini comparison table on the card stays roughly in sync.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "social-preview.png"

W, H = 1280, 640
BG = "#0d1117"
CARD = "#161b22"
BORDER = "#30363d"
WHITE = "#f0f6fc"
BLUE = "#58a6ff"
GRAY = "#8b949e"
GREEN = "#3fb950"
YELLOW = "#d29922"
DIM = "#484f58"
GOLD = "#e3b341"

F = "/System/Library/Fonts/Supplemental/"
BOLD = F + "Arial Bold.ttf"
REG = F + "Arial.ttf"
UNI = F + "Arial Unicode.ttf"  # has ✓ ★ —


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


# (name, stars, self-host, fallback, caching, guardrails) — mirrors README quick table
TABLE = [
    ("LiteLLM", "★ 50k", "✓", "✓", "✓", "✓"),
    ("Kong", "★ 43.6k", "✓", "✓", "✓", "✓"),
    ("new-api", "★ 38.3k", "✓", "✓", "+", "+"),
    ("Portkey", "★ 12k", "✓", "✓", "✓", "✓"),
    ("Higress", "★ 8.6k", "✓", "✓", "✓", "✓"),
    ("OpenRouter", "SaaS", "—", "✓", "✓", "+"),
]
MARK_COLOR = {"✓": GREEN, "+": YELLOW, "—": DIM}

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# top accent line
d.rectangle([0, 0, W, 6], fill=BLUE)

# ---- left text block ----
x = 64
d.text((x, 78), "A W E S O M E   L I S T   ·   U P D A T E D   D A I L Y",
       font=font(BOLD, 21), fill=BLUE)
d.text((x, 122), "Awesome", font=font(BOLD, 84), fill=WHITE)
d.text((x, 218), "AI Gateway", font=font(BOLD, 84), fill=WHITE)
d.text((x, 336), "Which AI gateway should you use?", font=font(BOLD, 34), fill=BLUE)

for i, line in enumerate(
    ["20+ gateways compared:", "cost · compliance · self-hosted", "routing · China ecosystem · MCP"]
):
    d.text((x, 400 + i * 38), line, font=font(REG, 27), fill=GRAY)

d.text((x, 556), "github.com/cuihuan/awesome-ai-gateway", font=font(BOLD, 27), fill=WHITE)

# ---- right mini-table card ----
cx0, cy0, cx1, cy1 = 700, 88, 1216, 556
d.rounded_rectangle([cx0, cy0, cx1, cy1], radius=16, fill=CARD, outline=BORDER, width=2)

col_name = cx0 + 28
col_star = cx0 + 185
cols = [cx0 + 305, cx0 + 370, cx0 + 435, cx0 + 495]
headers = ["host", "LB", "cache", "guard"]

hy = cy0 + 26
hf = font(REG, 19)
for cxx, htext in zip(cols, headers):
    bb = d.textbbox((0, 0), htext, font=hf)
    d.text((cxx - (bb[2] - bb[0]) / 2, hy), htext, font=hf, fill=GRAY)

row_h = 61
ry = cy0 + 64
name_f = font(BOLD, 26)
star_f = font(UNI, 21)
mark_f = font(UNI, 26)
for i, (name, stars, *marks) in enumerate(TABLE):
    y = ry + i * row_h
    if i % 2 == 0:
        d.rounded_rectangle([cx0 + 14, y - 9, cx1 - 14, y + row_h - 19], radius=8, fill="#1c2128")
    d.text((col_name, y), name, font=name_f, fill=WHITE)
    d.text((col_star, y + 4), stars, font=star_f, fill=GOLD if stars.startswith("★") else GRAY)
    for cxx, m in zip(cols, marks):
        bb = d.textbbox((0, 0), m, font=mark_f)
        d.text((cxx - (bb[2] - bb[0]) / 2, y), m, font=mark_f, fill=MARK_COLOR[m])

# card footer
d.text((cx0 + 28, cy1 - 38), "+ 45 more in the full table →", font=font(REG, 21), fill=GRAY)

OUT.parent.mkdir(exist_ok=True)
img.save(OUT, "PNG")
print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
