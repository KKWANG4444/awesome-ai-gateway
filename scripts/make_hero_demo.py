#!/usr/bin/env python3
"""Render the above-the-fold animated demo to assets/hero-demo.gif.

Four frames, GitHub-dark palette, ~2.4s each: (1) the problem — pick by
requirement, not vendor; (2) the method — match trust tier to data
sensitivity; (3) the evidence — the five-axis scorecard; (4) the payoff —
the 106x cost spread. Every number/star shown is real and lives elsewhere
in the repo (README tiers, BENCHMARKS Part 4, cost_calc output) — the GIF
may never advertise anything the list doesn't carry.

Data layer (FRAMES, dimensions, palette) is importable WITHOUT Pillow so the
unit tests run on the CI runner; rendering (`render`) lazily imports PIL and
is guarded under `__main__`.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "hero-demo.gif"

W, H = 840, 420
FRAME_MS = 2400
BG = "#0d1117"
CARD = "#161b22"
BORDER = "#30363d"
WHITE = "#f0f6fc"
BLUE = "#58a6ff"
GRAY = "#8b949e"
GREEN = "#3fb950"
YELLOW = "#d29922"
RED = "#f85149"
GOLD = "#e3b341"

F = "/System/Library/Fonts/Supplemental/"
BOLD = F + "Arial Bold.ttf"
REG = F + "Arial.ttf"
UNI = F + "Arial Unicode.ttf"  # has ★ ½ →

# The nine requirement chips — must mirror README "The requirements map".
CHIPS = ["Routing", "Cost", "Observability", "Compliance", "Supply-chain",
         "Caching", "K8s", "MCP/Agents", "Fidelity"]

# Trust tiers — must mirror README "How to choose safely".
TIERS = [
    (RED, "Secrets / regulated", "self-host in your VPC, or first-party + ZDR"),
    (YELLOW, "Internal / business", "compliant hosted, or self-hosted"),
    (GREEN, "Low-stakes / throwaway", "cheapest wins — after a canary test"),
]

# Scorecard sample rows — must mirror BENCHMARKS Part 4 exactly.
SCORE_HEAD = ["Gateway", "Compl.", "Security", "Stability", "Obsv"]
SCORE_ROWS = [
    ("LiteLLM", "★★★", "★★½ !", "★★★★", "★★★★★"),
    ("Bifrost", "★★★", "★★★½", "★★★★½", "★★★★★"),
    ("Envoy AI GW", "★★★", "★★★★", "★★★★", "★★★★"),
]

# Cost payoff — computed numbers from cost_calc (README/BENCHMARKS carry them).
COST = ("$0.03", "$3.01", "the same 100K-token report", "106×")

FRAMES = [
    {"kicker": "100+ GATEWAYS · 9 CATEGORIES",
     "title": "Which AI gateway\nshould you use?",
     "sub": "Organized by requirement, not vendor.",
     "body": ("chips", CHIPS)},
    {"kicker": "STEP 1 · THE METHOD",
     "title": "Match the trust tier\nto your data",
     "sub": "One call decides most of the rest.",
     "body": ("tiers", TIERS)},
    {"kicker": "STEP 2 · THE EVIDENCE",
     "title": "Scores, not vibes",
     "sub": "5 axes · published rubric · daily-refreshed data.",
     "body": ("table", (SCORE_HEAD, SCORE_ROWS))},
    {"kicker": "STEP 3 · THE PAYOFF",
     "title": "The model behind it\ndecides the bill",
     "sub": "github.com/cuihuan/awesome-ai-gateway",
     "body": ("cost", COST)},
]


def render(out=OUT):
    """Render the animated GIF (imports PIL lazily — absent on CI)."""
    from PIL import Image, ImageDraw, ImageFont

    def font(path, size):
        return ImageFont.truetype(path, size)

    def frame(spec):
        img = Image.new("RGB", (W, H), BG)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W, 5], fill=BLUE)
        x = 48
        d.text((x, 40), spec["kicker"], font=font(BOLD, 16), fill=BLUE)
        for i, line in enumerate(spec["title"].split("\n")):
            d.text((x, 74 + i * 46), line, font=font(BOLD, 40), fill=WHITE)
        kind, data = spec["body"]

        if kind == "chips":
            cx, cy = x, 196
            cf = font(REG, 19)
            for chip in data:
                wpx = d.textbbox((0, 0), chip, font=cf)[2] + 28
                if cx + wpx > W - 48:
                    cx, cy = x, cy + 46
                d.rounded_rectangle([cx, cy, cx + wpx, cy + 34], radius=17,
                                    fill=CARD, outline=BORDER, width=1)
                d.text((cx + 14, cy + 6), chip, font=cf, fill=BLUE)
                cx += wpx + 12
        elif kind == "tiers":
            y = 184
            for color, label, route in data:
                d.ellipse([x, y + 5, x + 14, y + 19], fill=color)
                d.text((x + 26, y), label, font=font(BOLD, 21), fill=WHITE)
                d.text((x + 26, y + 27), "→ " + route, font=font(UNI, 18), fill=GRAY)
                y += 58
        elif kind == "table":
            head, rows = data
            cols = [x, x + 210, x + 340, x + 480, x + 630]
            y = 178
            hf = font(REG, 16)
            for cx0, h in zip(cols, head):
                d.text((cx0, y), h, font=hf, fill=GRAY)
            y += 28
            for name, *stars in rows:
                d.rounded_rectangle([x - 12, y - 6, W - 48, y + 26], radius=8,
                                    fill=CARD)
                d.text((cols[0], y), name, font=font(BOLD, 19), fill=WHITE)
                for cx0, s in zip(cols[1:], stars):
                    color = YELLOW if "!" in s else GOLD
                    d.text((cx0, y), s, font=font(UNI, 18), fill=color)
                y += 40
            d.text((x, y + 2), "self-hosted: compliance is yours · ! = patch to current stable",
                   font=font(REG, 15), fill=GRAY)
        elif kind == "cost":
            cheap, dear, what, mult = data
            y = 200
            d.text((x, y), cheap, font=font(BOLD, 56), fill=GREEN)
            wpx = d.textbbox((0, 0), cheap, font=font(BOLD, 56))[2]
            d.text((x + wpx + 24, y + 14), "vs", font=font(REG, 28), fill=GRAY)
            d.text((x + wpx + 84, y), dear, font=font(BOLD, 56), fill=RED)
            d.text((x, y + 74), f"{what} — a {mult} spread, computed by a unit-tested script",
                   font=font(REG, 19), fill=GRAY)

        d.text((x, H - 52), spec["sub"], font=font(BOLD, 19),
               fill=GOLD if kind == "cost" else GRAY)
        return img

    frames = [frame(s) for s in FRAMES]
    out.parent.mkdir(exist_ok=True)
    frames[0].save(out, save_all=True, append_images=frames[1:],
                   duration=FRAME_MS, loop=0, optimize=True)
    print(f"wrote {out} ({out.stat().st_size // 1024} KB, {len(frames)} frames)")
    return out


if __name__ == "__main__":
    render()
