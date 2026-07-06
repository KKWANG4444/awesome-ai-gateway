"""Unit tests for make_hero_demo.py pure data (no PIL).

Headline invariant (mirrors test_make_landscape / test_make_social_preview):
the hero GIF may never advertise anything the repo doesn't carry — its chips
mirror the README requirements map, its tiers mirror "How to choose safely",
and its scorecard stars mirror BENCHMARKS Part 4. Rendering is not exercised
(Pillow is absent on the CI runner).
"""

import unittest
from pathlib import Path

from make_hero_demo import CHIPS, COST, FRAMES, H, SCORE_ROWS, TIERS, W

ROOT = Path(__file__).resolve().parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")
BENCH = (ROOT / "BENCHMARKS.md").read_text(encoding="utf-8")


class TestHeroDemoData(unittest.TestCase):
    def test_dimensions(self):
        self.assertEqual((W, H), (840, 420))

    def test_four_frames_each_complete(self):
        self.assertEqual(len(FRAMES), 4)
        for f in FRAMES:
            self.assertTrue(f["kicker"] and f["title"] and f["sub"])
            self.assertEqual(len(f["body"]), 2)

    def test_chips_mirror_requirements_map(self):
        # every chip concept must appear in the README requirements map section
        for probe in ("Routing", "Observability", "Supply-chain", "Fidelity"):
            self.assertIn(probe, CHIPS)
        self.assertEqual(len(CHIPS), 9)  # 9 rows in the requirements map

    def test_tiers_mirror_choose_safely(self):
        self.assertEqual(len(TIERS), 3)
        for _color, label, _route in TIERS:
            # tier labels are lifted from the README trust-tier table
            probe = label.split(" /")[0].split()[0]  # Secrets / Internal / Low-stakes
            self.assertIn(probe, README)

    def test_scorecard_rows_match_benchmarks_part4(self):
        # every gateway named must be a Part 4 row, and its Obsv stars must
        # match BENCHMARKS exactly (LiteLLM/Bifrost = 5, Envoy = 4)
        for name, *stars in SCORE_ROWS:
            probe = name.split(" AI GW")[0]
            self.assertIn(probe, BENCH)
        by_name = {r[0]: r for r in SCORE_ROWS}
        self.assertEqual(by_name["LiteLLM"][4], "★★★★★")
        self.assertEqual(by_name["Bifrost"][4], "★★★★★")
        self.assertEqual(by_name["Envoy AI GW"][4], "★★★★")

    def test_cost_numbers_exist_in_repo(self):
        cheap, dear, _what, mult = COST
        for probe in (cheap, dear, mult):
            self.assertTrue(probe in README or probe in BENCH,
                            f"{probe} not found in README/BENCHMARKS")


if __name__ == "__main__":
    unittest.main()
