"""Unit tests for canary_check.py pure logic (no network)."""

import unittest

from canary_check import (
    Reply,
    capability_hit,
    fingerprint_summary,
    normalize,
    parse_models,
    parse_reply,
    token_similarity,
    verdict,
)


class TestNormalize(unittest.TestCase):
    def test_lowercase_collapse_strip_punct(self):
        self.assertEqual(normalize("  The  Ball: $0.05!! "), "the ball 005")

    def test_empty(self):
        self.assertEqual(normalize(""), "")
        self.assertEqual(normalize(None), "")


class TestTokenSimilarity(unittest.TestCase):
    def test_identical(self):
        self.assertEqual(token_similarity("the ball is 5", "the ball is 5"), 1.0)

    def test_disjoint(self):
        self.assertEqual(token_similarity("alpha beta", "gamma delta"), 0.0)

    def test_both_empty_is_one(self):
        self.assertEqual(token_similarity("", ""), 1.0)

    def test_one_empty_is_zero(self):
        self.assertEqual(token_similarity("hello", ""), 0.0)

    def test_partial_jaccard(self):
        # {a,b,c} vs {a,b,d} -> intersection 2 / union 4 = 0.5
        self.assertAlmostEqual(token_similarity("a b c", "a b d"), 0.5)

    def test_punctuation_ignored(self):
        self.assertEqual(token_similarity("0.05", "$0.05!"), 1.0)


class TestCapabilityHit(unittest.TestCase):
    def test_hit_substring_normalized(self):
        self.assertTrue(capability_hit("The ball costs $0.05.", "0.05"))

    def test_miss(self):
        self.assertFalse(capability_hit("The ball costs $0.10.", "0.05"))

    def test_compare_only_returns_none(self):
        self.assertIsNone(capability_hit("anything", None))


class TestVerdict(unittest.TestCase):
    def test_downgrade_when_relay_fails_a_probe_ref_passes(self):
        rows = [
            {"id": "reason", "similarity": 0.8, "relay_hit": False, "ref_hit": True},
            {"id": "echo", "similarity": 0.9, "relay_hit": True, "ref_hit": True},
        ]
        v = verdict(rows)
        self.assertIn("SUSPICIOUS", v["label"])
        self.assertEqual(v["downgrade_flags"], ["reason"])

    def test_suspicious_on_low_similarity(self):
        rows = [{"id": "a", "similarity": 0.2, "relay_hit": None, "ref_hit": None}]
        self.assertIn("SUSPICIOUS", verdict(rows)["label"])

    def test_inconclusive_mid_band(self):
        rows = [{"id": "a", "similarity": 0.6, "relay_hit": None, "ref_hit": None}]
        self.assertIn("INCONCLUSIVE", verdict(rows)["label"])

    def test_ok_high_similarity(self):
        rows = [
            {"id": "a", "similarity": 0.95, "relay_hit": True, "ref_hit": True},
            {"id": "b", "similarity": 0.85, "relay_hit": None, "ref_hit": None},
        ]
        v = verdict(rows)
        self.assertIn("OK", v["label"])
        self.assertEqual(v["downgrade_flags"], [])

    def test_mean_similarity_reported(self):
        rows = [{"id": "a", "similarity": 0.4, "relay_hit": None, "ref_hit": None},
                {"id": "b", "similarity": 0.6, "relay_hit": None, "ref_hit": None}]
        self.assertEqual(verdict(rows)["mean_similarity"], 0.5)


class TestParseReply(unittest.TestCase):
    def test_full_body(self):
        r = parse_reply({
            "choices": [{"message": {"content": "hello"}}],
            "usage": {"prompt_tokens": 42, "completion_tokens": 3},
            "system_fingerprint": "fp_abc",
        })
        self.assertEqual(r, Reply(content="hello", system_fingerprint="fp_abc", prompt_tokens=42))

    def test_missing_fields_tolerated(self):
        r = parse_reply({"choices": [{}]})
        self.assertEqual(r, Reply(content="", system_fingerprint=None, prompt_tokens=None))
        self.assertEqual(parse_reply({}), Reply(content="", system_fingerprint=None, prompt_tokens=None))
        self.assertEqual(parse_reply(None), Reply(content="", system_fingerprint=None, prompt_tokens=None))

    def test_blank_fingerprint_is_none(self):
        r = parse_reply({"choices": [{"message": {"content": "x"}}], "system_fingerprint": ""})
        self.assertIsNone(r.system_fingerprint)


class TestParseModels(unittest.TestCase):
    def test_splits_trims_dedupes_preserving_order(self):
        self.assertEqual(parse_models("gpt-5.5, claude-opus-4-8 ,gpt-5.5"), ["gpt-5.5", "claude-opus-4-8"])

    def test_single(self):
        self.assertEqual(parse_models("gpt-4o"), ["gpt-4o"])

    def test_empty(self):
        self.assertEqual(parse_models(""), [])
        self.assertEqual(parse_models(" , "), [])


class TestFingerprintSummary(unittest.TestCase):
    def _r(self, fp=None, pt=None):
        return Reply(content="x", system_fingerprint=fp, prompt_tokens=pt)

    def test_no_metadata_is_not_comparable(self):
        s = fingerprint_summary([(self._r(), self._r())])
        self.assertEqual(s["comparable"], 0)
        self.assertEqual(s["flags"], [])
        self.assertIsNone(s["fp_mismatch"])
        self.assertIsNone(s["max_prompt_token_skew"])

    def test_matching_fingerprint_and_tokens_clean(self):
        s = fingerprint_summary([(self._r("fp_a", 100), self._r("fp_a", 100))])
        self.assertEqual(s["flags"], [])
        self.assertFalse(s["fp_mismatch"])
        self.assertEqual(s["max_prompt_token_skew"], 0.0)
        self.assertEqual(s["comparable"], 1)

    def test_fingerprint_mismatch_flagged(self):
        s = fingerprint_summary([(self._r("fp_a", 100), self._r("fp_b", 100))])
        self.assertTrue(s["fp_mismatch"])
        self.assertIn("system_fingerprint", s["flags"])

    def test_prompt_token_skew_beyond_tolerance_flagged(self):
        # 100 vs 130 = 30% skew > default 15% tolerance → tokenizer tell
        s = fingerprint_summary([(self._r(pt=130), self._r(pt=100))])
        self.assertIn("prompt_tokens", s["flags"])
        self.assertEqual(s["max_prompt_token_skew"], 0.3)

    def test_small_skew_within_tolerance_not_flagged(self):
        s = fingerprint_summary([(self._r(pt=105), self._r(pt=100))])
        self.assertEqual(s["flags"], [])
        self.assertEqual(s["max_prompt_token_skew"], 0.05)

    def test_max_skew_across_canaries(self):
        s = fingerprint_summary([
            (self._r(pt=102), self._r(pt=100)),  # 2%
            (self._r(pt=140), self._r(pt=100)),  # 40%
        ])
        self.assertEqual(s["max_prompt_token_skew"], 0.4)
        self.assertIn("prompt_tokens", s["flags"])


if __name__ == "__main__":
    unittest.main()
