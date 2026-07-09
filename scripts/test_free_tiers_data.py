"""Structural integrity tests for data/free_tiers.json.

The free-tier table's whole value is "verified against primary sources, dated,
never asserted" — these tests enforce the shape that promise depends on: every
row must carry non-empty limits/catch text, at least one https source, a
confidence verdict, and the file-level as_of must be a real ISO date that the
freshness gate (check_freshness.py) can read.
"""

import datetime
import json
import unittest
from pathlib import Path

from check_freshness import TRACKED, load_tracked_dates

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "free_tiers.json").read_text(encoding="utf-8"))

ENTRY_KEYS = ("provider", "free_offer", "limits", "models",
              "card_required", "catch", "sources", "confidence")
NOTE_KEYS = ("provider", "note", "sources", "confidence")


class TestFileLevel(unittest.TestCase):
    def test_as_of_is_iso_date(self):
        datetime.date.fromisoformat(DATA["as_of"])  # raises if malformed

    def test_all_three_lists_present_and_nonempty(self):
        for key in ("free_tiers", "trial_credits_not_free_tiers",
                    "discontinued_or_never_free"):
            self.assertIn(key, DATA)
            self.assertGreater(len(DATA[key]), 0, key)

    def test_tracked_by_freshness_gate(self):
        self.assertTrue(any(rel == "data/free_tiers.json" for _, rel in TRACKED))
        labels = [label for label, _ in load_tracked_dates()]
        self.assertTrue(any("free_tiers" in label for label in labels))


class TestFreeTierEntries(unittest.TestCase):
    def test_entries_carry_all_fields_nonempty(self):
        for entry in DATA["free_tiers"]:
            for key in ENTRY_KEYS:
                self.assertIn(key, entry, entry.get("provider"))
                self.assertTrue(str(entry[key]).strip(),
                                f"{entry.get('provider')}: empty {key}")

    def test_sources_are_https_urls(self):
        for entry in DATA["free_tiers"]:
            self.assertGreater(len(entry["sources"]), 0, entry["provider"])
            for url in entry["sources"]:
                self.assertTrue(url.startswith("https://"),
                                f"{entry['provider']}: {url}")

    def test_providers_unique(self):
        names = [e["provider"] for e in DATA["free_tiers"]]
        self.assertEqual(len(names), len(set(names)))

    def test_unpublished_limits_are_labeled_not_numbers(self):
        # Rows whose provider hides the numbers must say so rather than quote
        # third-hand figures as fact.
        for entry in DATA["free_tiers"]:
            if "unpublished" in entry["limits"]:
                self.assertNotIn("verified\"", entry["limits"])


class TestNoteEntries(unittest.TestCase):
    def test_trial_and_discontinued_shape(self):
        for key in ("trial_credits_not_free_tiers", "discontinued_or_never_free"):
            for entry in DATA[key]:
                for field in NOTE_KEYS:
                    self.assertIn(field, entry, f"{key}: {entry.get('provider')}")
                    self.assertTrue(str(entry[field]).strip())
                for url in entry["sources"]:
                    self.assertTrue(url.startswith("https://"))


if __name__ == "__main__":
    unittest.main()
