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

    def test_frozen_run_refuses_a_debugger_or_trace_function(self):
        import subprocess
        code = ("import sys, runpy; sys.settrace(lambda *a: None); "
                f"runpy.run_path({str(HERE / 'run_frozen.py')!r}, run_name='__main__')")
        r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=300, cwd=HERE)
        self.assertIn("debugger", r.stderr)

    def test_remedies_are_applied(self):
        self.assertEqual(run_frozen.remedies_of({"remedies": ["bootstrap:H2b", "bootstrap:H2c"]}), ("H2b", "H2c"))
        with self.assertRaises(SystemExit):
            run_frozen.remedies_of({"remedies": ["something else"]})
        runs = [c for c in calls(HERE / "run_frozen.py", "run") if ast.unparse(c.func) in ("rq2.run", "rq3.run")]
        self.assertEqual([kw(c, "remedies") for c in runs], ["remedies", "remedies"])
        for f in ["rq2_following.py", "rq3_reward.py"]:
            self.assertTrue(calls(HERE / f, "apply_bootstrap"), f)

    def test_e9_carries_the_dry_run_notes(self):
        v = {"H2b": {"verdict": "inconclusive", "coef": 0.0, "ci90": [-0.01, 0.01], "sesoi": 0.02, "tost_p": 0.01}}
        rows = run_frozen.equivalence_table(v, {"H2b": 0.009}, {"H2b": True}, {"H2b": "at or below the smallest planted effect"})
        self.assertEqual(rows[0]["mde80_note"], "at or below the smallest planted effect")

    def test_refused_rerun_verifies_nothing_and_every_attempt_is_released_and_logged(self):
        import outcomes
        calls = []
        saved = (outcomes.require_frozen, outcomes.release, outcomes.sha256, run_frozen.OUT, run_frozen.run, sys.argv)

        def boom(freeze, started):
            raise RuntimeError("boom")
        try:
            outcomes.require_frozen = lambda: calls.append("verify") or {}
            outcomes.release = lambda: calls.append("release")
            outcomes.sha256 = lambda path: "x"
            run_frozen.run = boom
            with tempfile.TemporaryDirectory() as tmp:
                run_frozen.OUT = Path(tmp)
                log = Path(tmp) / "attempts.jsonl"
                log.write_text(json.dumps({"attempt": 1, "status": "started"}) + "\n")
                sys.argv = ["run_frozen.py"]
                with self.assertRaises(SystemExit):
                    run_frozen.main()
                self.assertEqual(calls, [])                                  # refused before any verification
                sys.argv = ["run_frozen.py", "--rerun-reason", "test"]
                with self.assertRaises(RuntimeError):
                    run_frozen.main()
                self.assertEqual(calls, ["verify", "release"])               # released although the run failed
                lines = [json.loads(x) for x in log.read_text().splitlines()]
                self.assertEqual([x["status"] for x in lines], ["started", "started", "failed"])
                self.assertEqual(lines[1]["attempt"], 2)
                self.assertIn("boom", lines[2]["traceback"])
        finally:
            (outcomes.require_frozen, outcomes.release, outcomes.sha256, run_frozen.OUT, run_frozen.run, sys.argv) = saved


class FreezeChecksTheDryRun(unittest.TestCase):
    def setUp(self):
        self.fam = {"rq2": ["H2a", "H2b", "H2c"], "rq3": ["H3a", "H3b"]}
        self.prov = dict(dryrun.REGISTERED)
        hyps = lambda sc: self.fam["rq2"] if sc.startswith("rq2") else self.fam["rq3"]
        self.dry = {"code_digest": dryrun.digest()["combined"],
                    "mde80": {h: 0.01 for h in self.fam["rq2"] + self.fam["rq3"]},
                    "power": {k: {"1.0": {"full_rule": 0.5}, "3.0": {"full_rule": 0.9}}
                              for k in ["H2a", "H2b", "H2c", "H3a_hi", "H3b_hi"]},
                    "size": {sc: {h: 0.05 for h in hyps(sc)} for sc in dryrun.NULL_SCENARIOS},
                    "false_support": {sc: {h: 0.0 for h in hyps(sc)} for sc in dryrun.NULL_SCENARIOS},
                    "missing_p": {sc: {h: 0.0 for h in hyps(sc)} for sc in dryrun.NULL_SCENARIOS}}
        self.dry["size"]["rq2_null_k100"]["H2b"] = 0.016

    def test_clean(self):
        self.assertEqual(freeze.check_dryrun(self.dry, self.prov, self.fam), ([], {}))   # a low size is only reported

    def test_missing_null_scenario_or_p_values_or_full_rule_is_fatal(self):
        d = json.loads(json.dumps(self.dry))
        del d["size"]["rq3_null_early_hi"]
        d["missing_p"]["rq2_null_early"]["H2c"] = 0.01
        d["power"]["H3b_hi"] = {"3.0": {"detected_alpha_over_m": 0.9}}
        fatal, _ = freeze.check_dryrun(d, self.prov, self.fam)
        self.assertEqual(len(fatal), 4)                      # H3a and H3b lack early_hi; H2c missing p; H3b no full rule

    def test_false_support_is_remediable(self):
        d = json.loads(json.dumps(self.dry))
        d["false_support"]["rq3_permuted"]["H3a"] = 0.06
        self.assertEqual(list(freeze.check_dryrun(d, self.prov, self.fam)[1]), ["H3a"])

    def test_remedies_must_match_exactly(self):
        self.assertEqual(freeze.validate_remedies([], {}), set())
        self.assertEqual(freeze.validate_remedies(["bootstrap:H2a"], {"H2a": "size"}), {"H2a"})
        for remedies, rem in [(["use bootstrap"], {"H2a": "size"}), (["bootstrap:H2b"], {"H2a": "size"}),
                              ([], {"H2a": "size"}), (["bootstrap:H2a", "x"], {"H2a": "size"})]:
            with self.assertRaises(SystemExit):
                freeze.validate_remedies(remedies, rem)

    def test_dry_run_applied_the_triggered_remedies(self):
        self.assertEqual(dryrun.REMEDIES, ("H2b", "H2c"))

    def test_stale_digest_and_counts_are_fatal(self):
        fatal, _ = freeze.check_dryrun({**self.dry, "code_digest": "x"}, {**self.prov, "reps": 20}, self.fam)
        self.assertEqual(len(fatal), 2)

    def test_upward_size_is_remediable_only(self):
        d = json.loads(json.dumps(self.dry))
        d["size"]["rq2_null_early"]["H2a"] = 0.09
        fatal, rem = freeze.check_dryrun(d, self.prov, self.fam)
        self.assertEqual((fatal, list(rem)), ([], ["H2a"]))

    def test_missing_hypothesis_is_fatal(self):
        d = {**self.dry, "mde80": {"H2a": 0.01}}
        fatal, _ = freeze.check_dryrun(d, self.prov, self.fam)
        self.assertTrue(any("H3b" in f for f in fatal))

    def test_digest_covers_every_topic_input(self):
        files = dryrun.digest()["files"]
        for t in dryrun.TOPIC_INPUTS + ["paper_topic_stability.csv.gz"]:
            self.assertIn(f"research/topics/output/{t}", files)

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

    def test_registered_grid(self):
        self.assertEqual(dryrun.MULTS, (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0))
        self.assertEqual(dryrun.NULL_SCENARIOS, ["rq2_null_k100", "rq2_null_early", "rq3_permuted", "rq3_null_k100_lo",
                                                 "rq3_null_k100_hi", "rq3_null_early_hi"])

    def test_realised_effect_is_the_planted_part(self):
        from analysis import Spec
        rng = np.random.default_rng(0)
        n = 8000
        f = pd.DataFrame({"submission_id": [f"p{i}" for i in range(n)], "topic": rng.integers(0, 40, n).astype(str),
                          "year": rng.integers(2019, 2027, n), "x": (rng.random(n) < 0.4).astype(float)})
        f["cell"] = f.topic + ":" + f.year.astype(str)
        dgp = DGP(base=0.3, sd_topic=0.06, sd_year=0.04, sd_trend=0.02, sd_cell=0.05, effects={"x": -0.03})
        effs = []
        for r in range(3):
            y, p, q = simulate(f, dgp, np.random.default_rng(r), return_p=True)
            spec = Spec("Hx", "y", "x", -1, 0.02, "topic+year", (2019, 2026))
            effs.append(dryrun.realised(f.assign(y=0.0), spec, p - q, f.submission_id.values))
        self.assertLess(np.std(effs), 0.001)                                 # no topic/cell noise in the measurement
        self.assertAlmostEqual(np.mean(effs), -0.03, delta=0.003)

    def test_job_passes_only_the_planted_part_to_realised(self):
        for c in calls(HERE / "dryrun.py", "realised"):
            arg = c.args[2]
            ok = (isinstance(arg, ast.BinOp) and isinstance(arg.op, ast.Sub)) or ast.unparse(arg) == "ps[s.y]"
            self.assertTrue(ok, ast.unparse(c))
        src = (HERE / "dryrun.py").read_text()
        for v in ["p_inc - q_inc", "p_meth - q_meth", "p_meas - q_meas"]:
            self.assertIn(v, src)

    def test_criterion_c_uses_the_hi_setting_under_the_bare_name(self):
        rows = [{"scenario": "rq3_power_H3a_m3.0_hi", "rep": r, "hypothesis": "H3a", "coef": -0.03, "p": 0.001,
                 "predicted_sign": -1, "realised_effect": -0.03, "verdict": np.nan} for r in range(10)]
        rows += [{"scenario": "rq3_power_H3a_m3.0_lo", "rep": r, "hypothesis": "H3a", "coef": -0.03, "p": 0.5,
                  "predicted_sign": -1, "realised_effect": -0.03, "verdict": np.nan} for r in range(10)]
        s = dryrun.summarise(pd.DataFrame(rows))
        self.assertEqual(s["criteria"]["c_detected_80pct_at_3x_sesoi"], {"H3a": True})

    def test_mde80_interpolation_and_notes(self):
        self.assertEqual(dryrun.mde80([(0.01, 0.5), (0.02, 0.9)])[0], 0.01 + 0.3 * 0.01 / 0.4)
        self.assertEqual(dryrun.mde80([(0.01, 0.85), (0.02, 0.95)])[1], "at or below the smallest planted effect")
        self.assertEqual(dryrun.mde80([(0.01, 0.2), (0.02, 0.5)]), (None, "not reached within the grid"))
        self.assertIn("non-monotone", dryrun.mde80([(0.01, 0.5), (0.02, 0.85), (0.03, 0.7), (0.04, 0.99)])[1])

    def test_summary_criteria(self):
        rows = []
        for rep in range(100):
            p = 0.01 if rep < 10 else 0.5
            rows.append({"scenario": "rq2_null_k100", "rep": rep, "hypothesis": "H2a", "coef": 0.01, "p": 0.5, "p_cr1": p,
                         "p_boot": 0.5, "predicted_sign": -1, "verdict": "inconclusive", "realised_effect": np.nan})
        s = dryrun.summarise(pd.DataFrame(rows))
        self.assertEqual(s["size"]["rq2_null_k100"]["H2a"], 0.10)                 # criterion (a) reads CR1
        self.assertEqual(s["size_bootstrap"]["rq2_null_k100"]["H2a"], 0.0)
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
