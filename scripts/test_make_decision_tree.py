"""Unit tests for make_decision_tree.py pure functions (no PIL).

The headline invariant: every self-hostable gateway the decision tree
recommends must map to a repo actually tracked in data/projects.json — so the
shareable image can never drift from the list it advertises.
"""

import unittest

from make_decision_tree import (
    SELF_HOSTED_REPO,
    build_tree,
    self_hosted_slugs,
    tracked_repos,
)


class TestBuildTree(unittest.TestCase):
    def test_has_two_branches_hosted_and_self(self):
        kinds = [b["kind"] for b in build_tree("en")["branches"]]
        self.assertEqual(sorted(kinds), ["hosted", "self"])

    def test_every_leaf_has_a_condition_and_picks(self):
        for lang in ("en", "zh"):
            for b in build_tree(lang)["branches"]:
                self.assertTrue(b["leaves"])
                for leaf in b["leaves"]:
                    self.assertTrue(leaf["cond"].strip())
                    self.assertTrue(leaf["picks"], f"{lang} leaf has no picks")

    def test_en_and_zh_same_shape(self):
        en, zh = build_tree("en"), build_tree("zh")
        self.assertEqual(len(en["branches"]), len(zh["branches"]))
        for be, bz in zip(en["branches"], zh["branches"]):
            self.assertEqual(be["kind"], bz["kind"])
            self.assertEqual(len(be["leaves"]), len(bz["leaves"]))
            for le, lz in zip(be["leaves"], bz["leaves"]):
                # same recommendation slugs in both languages (only prose differs)
                self.assertEqual(le["picks"], lz["picks"])

    def test_returns_a_copy_not_the_constant(self):
        a = build_tree("en")
        a["branches"][0]["leaves"][0]["cond"] = "MUTATED"
        self.assertNotEqual(build_tree("en")["branches"][0]["leaves"][0]["cond"], "MUTATED")


class TestNoDriftFromList(unittest.TestCase):
    def test_self_hosted_picks_are_all_in_the_repo_map(self):
        # every self-host recommendation must have a known repo mapping
        unmapped = self_hosted_slugs(build_tree("en")) - set(SELF_HOSTED_REPO)
        self.assertEqual(unmapped, set(), f"tree recommends unmapped self-host gateways: {unmapped}")

    def test_repo_map_points_at_tracked_repos(self):
        tracked = tracked_repos()
        missing = {name: repo for name, repo in SELF_HOSTED_REPO.items() if repo not in tracked}
        self.assertEqual(missing, {}, f"tree recommends gateways not tracked in projects.json: {missing}")


if __name__ == "__main__":
    unittest.main()
