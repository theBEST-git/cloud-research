"""The pooled feature build's checks (build_pooled.py, POOLED_SPEC D5) on synthetic tables: each gate passes on a
consistent pooled build and fails on the defect it guards against. No real table is read and the pooled corpus is never
activated in this process; the refusal of a non-pooled process is checked in a subprocess.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import build_pooled as bp  # noqa: E402
from topic_maturity import maturity  # noqa: E402

CONF = {"c0", "c1", "c2"}


def variables(ids: list[str], year: list[int], topic: list[str], inc: list[float], team: list[int]) -> pd.DataFrame:
    key = [t > 0 for t in team]
    inc = [v if k else np.nan for v, k in zip(inc, key)]
    return pd.DataFrame({"submission_id": ids, "year": year, "map": "k100", "topic": topic, "has_author_key": key,
                         "team_size": team, "incumbent": inc, "newcomer": [1 - v for v in inc], "incumbent_w2": inc,
                         "incumbent_s4": inc, "prior_growth": 1.0, "hot": [np.nan if y < 2019 else 0.0 for y in year]})


def pooled_pair():
    """A discovery build (d0..d5) and a pooled build that adds c0..c2 (an earlier paper of an author of d4)."""
    ids = ["d0", "d1", "d2", "d3", "d4", "d5"]
    year = [2017, 2018, 2019, 2020, 2021, 2022]
    topic = ["1", "1", "2", "1", "2", "1"]
    d = variables(ids, year, topic, [0, 1, 0, 1, 0, 1], [2, 1, 3, 0, 2, 1])
    pids = ["d0", "c0", "d1", "d2", "c1", "d3", "d4", "c2", "d5"]
    pyear = [2017, 2017, 2018, 2019, 2020, 2020, 2021, 2021, 2022]
    ptopic = ["1", "2", "1", "2", "2", "1", "2", "1", "1"]
    p = variables(pids, pyear, ptopic, [0, 0, 1, 0, 0, 1, 1, 1, 1], [2, 1, 1, 3, 2, 0, 2, 1, 1])
    dm = maturity(pd.Series(topic), pd.Series(year)).assign(map="k100")
    pm = maturity(pd.Series(ptopic), pd.Series(pyear)).assign(map="k100")
    for m in (dm, pm):
        m["topic"] = m.topic.astype(str)
    return d, p, dm, pm


def earlier_pair():
    cols = ["submission_id", "year", "nn_id", "nn_cos", "exact_title_id", "probable_earlier_version"]
    d = pd.DataFrame([["d0", 2017, None, np.nan, None, None], ["d1", 2018, "d0", 0.5, None, None],
                      ["d2", 2019, "d1", 0.95, None, "d1"], ["d3", 2020, "d0", 0.3, "d0", "d0"]], columns=cols)
    p = pd.DataFrame([["d0", 2017, None, np.nan, None, None], ["c0", 2017, None, np.nan, None, None],
                      ["d1", 2018, "d0", 0.5, None, None], ["d2", 2019, "c0", 0.97, None, "c0"],
                      ["c1", 2019, "d1", 0.92, None, "d1"], ["d3", 2020, "d0", 0.3, "c1", "c1"]], columns=cols)
    return d, p


class MapComparison(unittest.TestCase):
    def test_consistent_build_passes_and_counts_flips(self):
        d, p, dm, pm = pooled_pair()
        gates, comp = bp.map_comparison("k100", d, p, dm, pm, CONF)
        self.assertTrue(all(gates.values()), gates)
        self.assertEqual(comp["incumbent"]["discovery_newcomer_to_incumbent"]["incumbent"], 1)     # d4 gains history
        self.assertEqual(comp["incumbent"]["discovery_incumbent_to_newcomer"]["incumbent"], 0)
        self.assertEqual(comp["maturity"]["topic_years_papers_up"], int((pm.merge(dm, on=["topic", "year"]).eval("papers_x > papers_y")).sum()))

    def test_each_defect_fails_its_gate(self):
        d, p, dm, pm = pooled_pair()
        cases = {"discovery_team_size_and_has_author_key_unchanged": lambda p, pm: p.assign(team_size=p.team_size.where(p.submission_id != "d2", 4)),
                 "discovery_topics_unchanged": lambda p, pm: p.assign(topic=p.topic.where(p.submission_id != "d5", "2")),
                 "no_discovery_paper_loses_incumbent_or_incumbent_w2": lambda p, pm: p.assign(incumbent=p.incumbent.where(p.submission_id != "d1", 0.0)),
                 "discovery_rows_in_discovery_order": lambda p, pm: p.iloc[[0, 1, 3, 2, 4, 5, 6, 7, 8]]}
        for gate, broken in cases.items():
            gates, _ = bp.map_comparison("k100", d, broken(p.copy(), pm), dm, pm, CONF)
            self.assertFalse(gates[gate], gate)
        fewer = pm.assign(cum_prior_papers=pm.cum_prior_papers.where(~((pm.topic == "1") & (pm.year == 2022)), 0))
        gates, _ = bp.map_comparison("k100", d, p, dm, fewer, CONF)
        self.assertFalse(gates["discovery_topic_years_keep_papers_and_prior_papers"])


class EarlierComparison(unittest.TestCase):
    def test_consistent_build_passes(self):
        d, p = earlier_pair()
        gates, comp = bp.earlier_comparison(d, p, CONF)
        self.assertTrue(all(gates.values()), gates)
        self.assertEqual((comp["discovery_flagged_pointing_to_confirmation"], comp["confirmation_flagged"],
                          comp["confirmation_flagged_pointing_to_discovery"]), (2, 1, 1))

    def test_moved_neighbour_lost_title_and_lost_flag_fail(self):
        d, p = earlier_pair()
        moved = p.copy()
        moved.loc[moved.submission_id == "d1", "nn_cos"] = 0.6       # another centring mean would move every cosine
        self.assertFalse(bp.earlier_comparison(d, moved, CONF)[0]["discovery_rows_with_a_discovery_neighbour_keep_it_and_its_cosine"])
        lost = p.copy()
        lost.loc[lost.submission_id == "d3", ["exact_title_id", "probable_earlier_version"]] = None
        g = bp.earlier_comparison(d, lost, CONF)[0]
        self.assertFalse(g["discovery_exact_title_matches_kept"])
        self.assertFalse(g["no_discovery_paper_loses_its_probable_earlier_version"])
        lower = p.copy()
        lower.loc[lower.submission_id == "d2", "nn_cos"] = 0.9         # a new (confirmation) neighbour must be closer
        self.assertFalse(bp.earlier_comparison(d, lower, CONF)[0]["discovery_rows_with_a_confirmation_neighbour_gain_cosine"])


class FrameViolations(unittest.TestCase):
    def frame(self) -> pd.DataFrame:
        year = pd.Series([2017, 2018, 2019, 2026])
        return pd.DataFrame({"year": year, "topic": ["1", "2", "1", "2"], "topic_early": ["early_1"] * 4,
                             "primary_class": "method", "primary_type": "method", "maturity": [0.0, 1.0, 2.0, 3.0],
                             "prior_growth": [np.nan, np.nan, 1.0, 1.2], "hot": [np.nan, np.nan, 0.0, 1.0],
                             "has_author_key": [True, False, True, True], "incumbent": [0.0, np.nan, 1.0, 0.0],
                             "buzzword": [np.nan, np.nan, 0.0, 1.0], "has_earlier_version": 0.0})

    def test_whole_frame_has_no_violation(self):
        self.assertFalse(any(bp.frame_violations(self.frame()).values()))

    def test_gaps_are_counted(self):
        for col, row, value in [("topic", 0, "k75_nan"), ("primary_class", 1, np.nan), ("maturity", 2, np.nan),
                                ("hot", 2, np.nan), ("hot", 0, 0.0), ("incumbent", 1, 0.0), ("incumbent", 0, np.nan),
                                ("buzzword", 3, np.nan), ("topic_early", 3, "early_nan")]:
            f = self.frame()
            f.loc[row, col] = value
            self.assertEqual(bp.frame_violations(f)[col], 1, (col, row, value))


class Untouched(unittest.TestCase):
    def test_changed_sees_edits_new_and_removed_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / "a.txt", Path(tmp) / "b.txt"
            a.write_text("x")
            before = bp.snapshot([a, b])
            self.assertEqual(bp.changed(before, bp.snapshot([a, b])), [])
            a.write_text("y")
            b.write_text("z")
            self.assertEqual(len(bp.changed(before, bp.snapshot([a, b]))), 2)

    def test_guarded_covers_freeze_and_discovery_outputs(self):
        files = {bp.rel(f) for f in bp.guarded()}
        self.assertTrue(set(bp.freeze_listed()) <= files)
        self.assertTrue(any(f.startswith("research/topics/output/") for f in files))
        self.assertIn("research/topics/cache/specter2.npy", files)

    def test_refuses_without_the_pooled_corpus(self):
        env = {**os.environ, "ICLR_CORPUS": "discovery"}
        r = subprocess.run([sys.executable, str(HERE / "build_pooled.py"), "--check-only"], cwd=ROOT, env=env,
                           capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("pooled corpus", r.stderr)
        with mock.patch.object(sys, "argv", ["build_pooled.py", "--check-only"]), mock.patch.object(bp, "run_builders") as run:
            with self.assertRaises(SystemExit):
                bp.main()                                   # this process imported common with the discovery corpus
            run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
