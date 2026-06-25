#!/usr/bin/env python3
"""Unit tests for check_stale_gateways — pure logic only (no network)."""
import unittest
from datetime import datetime, timezone

from check_stale_gateways import build_report, classify, is_labeled_stale

NOW = datetime(2026, 6, 25, tzinfo=timezone.utc)


class Classify(unittest.TestCase):
    def test_archived_is_stale(self):
        self.assertEqual(classify({"archived": True, "pushed_at": "2026-06-01T00:00:00Z"}, NOW, 365),
                         (True, "archived"))

    def test_recent_push_not_stale(self):
        is_stale, _ = classify({"archived": False, "pushed_at": "2026-06-01T00:00:00Z"}, NOW, 365)
        self.assertFalse(is_stale)

    def test_old_push_is_stale(self):
        is_stale, reason = classify({"archived": False, "pushed_at": "2024-01-01T00:00:00Z"}, NOW, 365)
        self.assertTrue(is_stale)
        self.assertIn("no push", reason)

    def test_fetch_error_never_flags(self):
        self.assertEqual(classify({"_error": "HTTP 404"}, NOW, 365), (False, ""))

    def test_missing_pushed_at_not_stale(self):
        self.assertEqual(classify({"archived": False}, NOW, 365), (False, ""))

    def test_malformed_pushed_at_does_not_crash(self):
        self.assertEqual(classify({"archived": False, "pushed_at": "2024-13-99T99:99:99Z"}, NOW, 365),
                         (False, ""))

    def test_boundary_exactly_one_year_not_stale(self):
        # exactly 365 days old → NOT stale (strictly >365 required)
        is_stale, _ = classify({"archived": False, "pushed_at": "2025-06-25T00:00:00Z"}, NOW, 365)
        self.assertFalse(is_stale)

    def test_boundary_one_day_past_limit_is_stale(self):
        # 366 days old → IS stale (guards the > vs >= boundary)
        is_stale, _ = classify({"archived": False, "pushed_at": "2025-06-24T00:00:00Z"}, NOW, 365)
        self.assertTrue(is_stale)


class IsLabeledStale(unittest.TestCase):
    README = (
        "- [TensorZero](https://x) <!--s:tensorzero/tensorzero-->⭐ 11k<!--/s--> — ⚠️ **Archived June 2026**.\n"
        "- [Active Gw](https://y) <!--s:foo/active-->⭐ 5k<!--/s--> — A healthy active gateway.\n"
        "- ⚠️ Stale but historically notable: [Glide](https://z) <!--s:einstack/glide-->⭐ 161<!--/s-->.\n"
        "- [Proxy](https://p) <!--s:bar/proxy-->⭐ 9k<!--/s--> — Replaces the deprecated v1 proxy; routes inactive sessions.\n"
    )

    def test_labeled_archived(self):
        self.assertTrue(is_labeled_stale(self.README, "tensorzero/tensorzero"))

    def test_labeled_stale_prefix(self):
        self.assertTrue(is_labeled_stale(self.README, "einstack/glide"))

    def test_active_entry_not_labeled(self):
        self.assertFalse(is_labeled_stale(self.README, "foo/active"))

    def test_prose_words_do_not_count_as_a_label(self):
        # "deprecated"/"inactive" in a normal description must NOT mark it labeled —
        # only the ⚠️ house marker counts (regression for the substring-match bug).
        self.assertFalse(is_labeled_stale(self.README, "bar/proxy"))

    def test_absent_slug_not_labeled(self):
        self.assertFalse(is_labeled_stale(self.README, "no/such"))


class BuildReport(unittest.TestCase):
    def test_unlabeled_makes_it_actionable_exit1(self):
        report, code = build_report([("a/b", "archived", False), ("c/d", "no push in 500d", True)], [], 70)
        self.assertEqual(code, 1)
        self.assertIn("UNLABELED", report)
        self.assertIn("a/b", report)

    def test_all_labeled_is_green_exit0(self):
        report, code = build_report([("c/d", "archived", True)], [], 70)
        self.assertEqual(code, 0)
        self.assertIn("promise holds", report)

    def test_empty_is_green(self):
        report, code = build_report([], [], 70)
        self.assertEqual(code, 0)

    def test_zero_checked_is_coverage_failure_exit1(self):
        report, code = build_report([], ["x/y: HTTP 403"], 0)
        self.assertEqual(code, 1)
        self.assertIn("coverage failure", report.lower())

    def test_partial_errors_surface_but_not_red(self):
        report, code = build_report([], ["x/y: HTTP 403"], 70)
        self.assertEqual(code, 0)  # transient partial errors don't turn it red
        self.assertIn("incomplete", report.lower())
        self.assertIn("x/y", report)


if __name__ == "__main__":
    unittest.main()
