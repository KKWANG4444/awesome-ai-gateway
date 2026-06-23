"""Unit tests for check_freshness.py pure functions (no filesystem/network)."""

import datetime
import unittest

from check_freshness import parse_date, stale_entries

TODAY = datetime.date(2026, 6, 23)


class TestParseDate(unittest.TestCase):
    def test_parses_iso(self):
        self.assertEqual(parse_date("2026-06-12"), datetime.date(2026, 6, 12))
        self.assertEqual(parse_date("  2026-06-12 "), datetime.date(2026, 6, 12))

    def test_rejects_malformed(self):
        with self.assertRaises(ValueError):
            parse_date("June 12 2026")


class TestStaleEntries(unittest.TestCase):
    def test_within_limit_is_fresh(self):
        items = [("models", "2026-06-12")]  # 11 days old
        self.assertEqual(stale_entries(items, TODAY, max_age_days=30), [])

    def test_exactly_at_limit_is_fresh(self):
        items = [("models", "2026-05-24")]  # exactly 30 days old
        self.assertEqual(stale_entries(items, TODAY, max_age_days=30), [])

    def test_one_day_over_limit_is_stale(self):
        items = [("models", "2026-05-23")]  # 31 days old
        out = stale_entries(items, TODAY, max_age_days=30)
        self.assertEqual(out, [("models", "2026-05-23", 31)])

    def test_reports_only_stale_ones_with_ages(self):
        items = [
            ("fresh", "2026-06-20"),   # 3d
            ("stale-a", "2026-04-01"), # 83d
            ("stale-b", "2026-05-01"), # 53d
        ]
        out = stale_entries(items, TODAY, max_age_days=14)
        self.assertEqual(out, [("stale-a", "2026-04-01", 83), ("stale-b", "2026-05-01", 53)])

    def test_empty_input(self):
        self.assertEqual(stale_entries([], TODAY, max_age_days=30), [])


if __name__ == "__main__":
    unittest.main()
