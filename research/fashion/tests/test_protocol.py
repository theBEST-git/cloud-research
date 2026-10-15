"""Protocol safeguards around the frozen run and the dry-run (PREREGISTRATION.md D12, D13, D16, review rounds B/B2).
Each test fails if the corresponding fix is reverted. No real outcome is read.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import ast
import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import dryrun  # noqa: E402
import exploratory  # noqa: E402
import freeze  # noqa: E402
import panel  # noqa: E402
import rq2_following  # noqa: E402
import run_frozen  # noqa: E402
from dgp import DGP, calibrate, simulate  # noqa: E402


def calls(path: Path, func: str) -> list[ast.Call]:
    tree = ast.parse(path.read_text())
    return [n for n in ast.walk(tree) if isinstance(n, ast.Call)
            and (getattr(n.func, "attr", None) == func or getattr(n.func, "id", None) == func)]


def kw(call: ast.Call, name: str) -> str | None:
    for k in call.keywords:
        if k.arg == name:
            return ast.unparse(k.value)
    return None


class DescribeOnlyInTheRealRun(unittest.TestCase):
    def test_call_sites(self):
        self.assertTrue(any(kw(c, "describe") == "ys is None" for c in calls(HERE / "rq2_following.py", "fit")))
        self.assertIn("describe = ys is None", (HERE / "exploratory.py").read_text())
        rq3_run = [c for c in calls(HERE / "run_frozen.py", "run") if ast.unparse(c.func) == "rq3.run"]
        self.assertEqual([kw(c, "describe") for c in rq3_run], ["True"])
        for f in ["dryrun.py", "rq3_reward.py", "rq2_following.py", "exploratory.py"]:
            self.assertFalse(any(kw(c, "describe") == "True" for c in calls(HERE / f, "fit") + calls(HERE / f, "estimate")
                                 + calls(HERE / f, "run")), f)

    def test_run_info_records_scipy(self):
        self.assertIn('"scipy": scipy.__version__', (HERE / "run_frozen.py").read_text())


class ExploratoryLabels(unittest.TestCase):
    def test_failed_measure_status(self):
        self.assertEqual(exploratory.measure_status({"accepted", "buzzword", "fm"}, gate=False), exploratory.FAILED)
        self.assertEqual(exploratory.measure_status({"lists_hot", "newcomer"}, gate=False), exploratory.FAILED)
        self.assertEqual(exploratory.measure_status({"accepted", "maturity"}, gate=False), "")
        self.assertEqual(exploratory.measure_status({"accepted", "buzzword"}, gate=True), "")


class FrozenRunBookkeeping(unittest.TestCase):
    def test_attempts_are_counted_by_started_lines(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "attempts.jsonl"
            self.assertEqual(run_frozen.started_attempts(log), [])
            log.write_text("\n".join(json.dumps(r) for r in [{"attempt": 1, "status": "started"},
                                                             {"attempt": 1, "status": "failed"},
                                                             {"attempt": 2, "status": "started"},
                                                             {"attempt": 2, "status": "finished"}]) + "\n")
            self.assertEqual(len(run_frozen.started_attempts(log)), 2)

    def test_e9_marks_missing_mde_as_underpowered(self):
        v = {"H3a": {"verdict": "inconclusive", "coef": 0.001, "ci90": [-0.01, 0.012], "sesoi": 0.01, "tost_p": 0.2},
             "H2b": {"verdict": "supported", "coef": -0.03, "ci90": [-0.04, -0.02], "sesoi": 0.02, "tost_p": 0.9}}
        rows = run_frozen.equivalence_table(v, {"H3a": None}, {"H3a": False})
        self.assertEqual([r["hypothesis"] for r in rows], ["H3a"])
        self.assertTrue(rows[0]["underpowered_at_3x_sesoi"])
        self.assertIn("not reached", rows[0]["mde80_note"])

    def test_remedies_are_not_silently_ignored(self):
        with self.assertRaises(SystemExit):
            run_frozen.run({"remedies": ["bootstrap:H2a"]}, "now")


class FreezeChecksTheDryRun(unittest.TestCase):
    def setUp(self):
        self.fam = {"rq2": ["H2a", "H2b", "H2c"], "rq3": ["H3a", "H3b"]}
        self.prov = dict(dryrun.REGISTERED)
        self.dry = {"code_digest": dryrun.digest()["combined"],
                    "mde80": {h: 0.01 for h in self.fam["rq2"] + self.fam["rq3"]},
                    "power": {"H2a": {}, "H2b": {}, "H2c": {}, "H3a_hi": {}, "H3b_hi": {}},
                    "size": {"rq2_null_k100": {"H2a": 0.05, "H2b": 0.016}}, "false_support": {"rq2_null_k100": {"H2a": 0.0}}}

    def test_clean(self):
        self.assertEqual(freeze.check_dryrun(self.dry, self.prov, self.fam), ([], {}))   # a low size is only reported

    def test_stale_digest_and_counts_are_fatal(self):
        fatal, _ = freeze.check_dryrun({**self.dry, "code_digest": "x"}, {**self.prov, "reps": 20}, self.fam)
        self.assertEqual(len(fatal), 2)

    def test_upward_size_is_remediable_only(self):
        d = {**self.dry, "size": {"rq2_null_early": {"H2a": 0.09}}}
        fatal, rem = freeze.check_dryrun(d, self.prov, self.fam)
        self.assertEqual((fatal, list(rem)), ([], ["H2a"]))

    def test_missing_hypothesis_is_fatal(self):
        d = {**self.dry, "mde80": {"H2a": 0.01}}
        fatal, _ = freeze.check_dryrun(d, self.prov, self.fam)
        self.assertTrue(any("H3b" in f for f in fatal))

    def test_digest_covers_labels_maps_and_the_sealed_table(self):
        import outcomes
        files = dryrun.digest()["files"]
        sealed = [str(f.relative_to(HERE.parents[1])) for f in outcomes.sealed_files()]
        for f in ["research/topics/output/paper_contributions.csv.gz", "research/topics/output/hindsight_assignments.csv.gz",
                  "research/fashion/rq2_following.py", *sealed]:
            self.assertIn(f, files)


class DryRunDesign(unittest.TestCase):
    def test_one_planted_hypothesis_per_power_scenario(self):
        for kind, sc, rep, params in dryrun.tasks(1, 1, 1):
            if "_power_" in sc or "_fullrule_" in sc:
                self.assertIn(params["planted"], sc)
                self.assertGreater(params["mult"], 0)
            else:
                self.assertNotIn("planted", params)
        multiples = {p["mult"] for _, sc, _, p in dryrun.tasks(1, 1, 1) if "_power_" in sc}
        self.assertEqual(multiples, set(dryrun.MULTS))
        self.assertIn(3.0, multiples)

    def test_mde80_interpolation_and_notes(self):
        self.assertEqual(dryrun.mde80([(0.01, 0.5), (0.02, 0.9)])[0], 0.01 + 0.3 * 0.01 / 0.4)
        self.assertEqual(dryrun.mde80([(0.01, 0.85), (0.02, 0.95)])[1], "at or below the smallest planted effect")
        self.assertEqual(dryrun.mde80([(0.01, 0.2), (0.02, 0.5)]), (None, "not reached within the grid"))
        self.assertIn("non-monotone", dryrun.mde80([(0.01, 0.5), (0.02, 0.85), (0.03, 0.7), (0.04, 0.99)])[1])

    def test_summary_criteria(self):
        rows = []
        for rep in range(100):
            rows.append({"scenario": "rq2_null_k100", "rep": rep, "hypothesis": "H2a", "coef": 0.01, "p": 0.01 if rep < 10 else 0.5,
                         "predicted_sign": -1, "verdict": "inconclusive", "realised_effect": np.nan})
        s = dryrun.summarise(pd.DataFrame(rows))
        self.assertEqual(s["size"]["rq2_null_k100"]["H2a"], 0.10)
        self.assertFalse(s["criteria"]["a_size_within_2_8pct"])
        self.assertTrue(s["criteria"]["b_false_support_at_most_5pct"])

    def test_calibration_recovers_known_components(self):
        k = panel.frame("k100")
        f = k[k.has_author_key].copy()
        truth = DGP(base=0.3, sd_topic=0.06, sd_year=0.04, sd_trend=0.01, sd_cell=0.04)
        est = []
        for r in range(3):
            f["ysim"] = simulate(f, truth, np.random.default_rng(r))
            c = calibrate(f, "ysim", (2019, 2026))
            est.append([c.sd_topic, c.sd_trend, c.sd_cell])
        topic, trend, cell = np.mean(est, axis=0)
        self.assertAlmostEqual(topic, 0.06, delta=0.015)
        self.assertAlmostEqual(trend, 0.01, delta=0.004)
        self.assertAlmostEqual(cell, 0.04, delta=0.012)


class S8ReferenceStratum(unittest.TestCase):
    def test_random_stratum_only(self):
        ref = rq2_following.REFERENCE
        n = (pd.read_csv(ref / "pilot_gold_facets.csv").stratum.eq("random").sum()
             + pd.read_csv(ref / "training" / "training_labels.csv").stratum.eq("random").sum())
        rel = rq2_following.label_reliability()
        self.assertLessEqual(rel["method"]["reference_n"], n)
        self.assertGreater(rel["method"]["reference_n"], 0.9 * n - 300)   # overlap between the two sets is dropped


if __name__ == "__main__":
    unittest.main()
