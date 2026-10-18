"""The confirmation and pooled plumbing (POOLED_SPEC D1/D5/D6): the corpus switch in common.py, run_confirmation.py
(one-sided p, Holm families, re-decided registered hypotheses, frames split after construction, attempts, refusals, the
PH5 hook, --simulate end to end), freeze_confirmation.py, run_pooled.py, build_pooled_inputs.py and the pooled branch
of resubmissions.py. Synthetic data and simulated outcomes only: no real outcome is read, and this process never
activates the pooled corpus (other tests compare against the discovery outputs); pooled paths are checked in a
subprocess that only imports modules.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import build_pooled_inputs  # noqa: E402
import common  # noqa: E402
import freeze_confirmation  # noqa: E402
import outcomes  # noqa: E402
import panel  # noqa: E402
import posthoc  # noqa: E402
import resubmissions  # noqa: E402
import rq2_following as rq2  # noqa: E402
import rq3_reward as rq3  # noqa: E402
import run_confirmation as rc  # noqa: E402
import run_pooled  # noqa: E402
from variants import holm  # noqa: E402

PY = sys.executable
DISCOVERY_DIRS = ["research/fashion/output", "research/topics/output"]


def git_status(paths: list[str]) -> str:
    return subprocess.run(["git", "status", "--porcelain", *paths], cwd=ROOT, capture_output=True, text=True,
                          check=True).stdout


def est(coef: float, p: float, se: float = 0.01, **extra) -> dict:
    return {"coef": coef, "se": se, "p": p, "dof": 99, "n": 1000, "clusters": 100, "ci95_lo": coef - 0.02,
            "ci95_hi": coef + 0.02, "ci90_lo": coef - 0.016, "ci90_hi": coef + 0.016, **extra}


def rows_for(main: dict[str, tuple[float, float]], counted_sign: dict[str, int], variants: list[str],
             wrong: dict[str, set] | None = None) -> pd.DataFrame:
    """rq2/rq3-style rows: a main estimate (coef, two-sided p) per hypothesis, counted variants with the given sign
    (except the variants in wrong[h]), and an S11 row."""
    out = []
    for h, (coef, p) in main.items():
        out.append({"hypothesis": h, "variant": "main", "kind": "main", **est(coef, p)})
        for v in variants:
            s = -counted_sign[h] if v in (wrong or {}).get(h, set()) else counted_sign[h]
            out.append({"hypothesis": h, "variant": v, "kind": "counted", **est(0.01 * s, 0.5)})
        out.append({"hypothesis": h, "variant": "S11_twoway_topic_early", "kind": "supplementary", **est(coef, 2 * p)})
    return pd.DataFrame(out)


class CorpusSwitch(unittest.TestCase):
    def test_unset_is_the_discovery_layout(self):
        self.assertEqual(common.CORPUS, "discovery")
        self.assertEqual(common.DATA, ROOT / "data")
        self.assertEqual(common.TOPICS, ROOT / "research" / "topics" / "output")
        self.assertEqual(common.OUTPUT, HERE / "output")
        self.assertEqual(outcomes.FREEZE, HERE / "FREEZE.json")

    def test_pooled_paths_in_a_subprocess(self):
        """Every path a pooled build or run writes is under output_pooled (imports only; nothing runs)."""
        code = ("import json, common, outcomes, run_frozen, posthoc, figures, variables, run_confirmation as rc, "
                "build_pooled_inputs as b, freeze_confirmation as fc, rq1_rise, rq2_following as rq2\n"
                "w = [common.DATA, common.OUTPUT, outcomes.ATTEMPTS, outcomes.POSTHOC_LOG, outcomes.CONFIRMATION_ATTEMPTS,"
                " run_frozen.OUT, posthoc.OUT, figures.FIG, variables.CHECKS, rc.OUT, rc.DRY, b.AUTHORS, b.MANIFEST,"
                " rq1_rise.OUTPUT]\n"
                "print(json.dumps({'write': [str(p) for p in w], 'topics': str(common.TOPICS), 'freeze': str(outcomes.FREEZE),"
                " 'target': str(fc.TARGET), 'reference': str(rq2.REFERENCE), 'corpus': common.CORPUS}))")
        env = {**os.environ, "ICLR_CORPUS": "pooled"}
        r = subprocess.run([PY, "-c", code], cwd=HERE, env=env, capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 0, r.stderr)
        got = json.loads(r.stdout.strip().splitlines()[-1])
        self.assertEqual(got["corpus"], "pooled")
        for p in map(Path, got["write"]):
            self.assertIn(common.POOLED_OUTPUT, [p, *p.parents], p)
            self.assertNotIn(common.DISCOVERY_OUTPUT, [p, *p.parents], p)
        self.assertEqual(Path(got["topics"]), ROOT / "research" / "topics" / "output_pooled")
        self.assertEqual(Path(got["freeze"]), HERE / "FREEZE_CONFIRMATION.json")
        self.assertEqual(Path(got["target"]), HERE / "FREEZE_CONFIRMATION.json")
        self.assertEqual(Path(got["reference"]), ROOT / "research" / "topics" / "annotation" / "contribution_types")

    def test_unknown_corpus_is_refused(self):
        env = {**os.environ, "ICLR_CORPUS": "confirmation"}
        r = subprocess.run([PY, "-c", "import common"], cwd=HERE, env=env, capture_output=True, text=True, timeout=120)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("ICLR_CORPUS", r.stderr)

    def test_write_paths_outside_the_discovery_outputs(self):
        for p in [rc.OUT, rc.DRY, build_pooled_inputs.AUTHORS, build_pooled_inputs.MANIFEST]:
            self.assertIn(common.POOLED_OUTPUT, p.parents)
            self.assertNotIn(common.DISCOVERY_OUTPUT, p.parents)
        self.assertEqual(freeze_confirmation.TARGET, outcomes.FREEZE_CONFIRMATION)
        self.assertNotEqual(freeze_confirmation.TARGET, outcomes.FREEZE_DISCOVERY)
        self.assertEqual(outcomes.CONFIRMATION_ATTEMPTS, rc.OUT / "attempts.jsonl")

    def test_runners_refuse_the_discovery_corpus(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(rc, "OUT", Path(tmp) / "run"), \
                mock.patch.object(rc, "DRY", Path(tmp) / "dry"):
            for argv in [["run_confirmation.py"], ["run_confirmation.py", "--simulate", "1"]]:
                with mock.patch.object(sys, "argv", argv), self.assertRaises(SystemExit):
                    rc.main()
            self.assertEqual(list(Path(tmp).iterdir()), [])
        with self.assertRaises(SystemExit):
            run_pooled.main()
        posthoc.check_corpus()                                              # discovery: nothing to check
        with mock.patch.object(posthoc, "CORPUS", "pooled"), self.assertRaises(SystemExit):
            posthoc.check_corpus()                                          # pooled flag with discovery paths


class OneSidedRule(unittest.TestCase):
    def test_conversion(self):
        self.assertAlmostEqual(rc.one_sided(0.04, -0.2, -1), 0.02)
        self.assertAlmostEqual(rc.one_sided(0.04, 0.2, -1), 0.98)
        self.assertAlmostEqual(rc.one_sided(0.30, 0.1, +1), 0.15)
        self.assertAlmostEqual(rc.one_sided(0.30, 0.0, +1), 0.85)               # a zero estimate is not in the direction
        self.assertTrue(np.isnan(rc.one_sided(np.nan, -0.2, -1)))
        self.assertTrue(np.isnan(rc.one_sided(0.01, np.nan, -1)))

    def test_registered_specs_reuse_the_discovery_models(self):
        by2, by3 = {s.hid: s for s in rq2.SPECS}, {s.hid: s for s in rq3.SPECS}
        for s, src, sign in [(rc.SPECS2[0], by2["H2b"], +1), (rc.SPECS2[1], by2["H2c"], -1), (rc.SPECS3[0], by3["H3a"], -1)]:
            self.assertEqual((s.y, s.x, s.fe, s.years, s.controls, s.sesoi), (src.y, src.x, src.fe, src.years, src.controls, src.sesoi))
            self.assertEqual(s.sign, sign)
        self.assertEqual([s.hid for s in rc.SPECS2], ["H2b'", "H2c'"])
        self.assertEqual((rc.H1D.y, rc.H1D.x, rc.H1D.sign, rc.H1D.years), ("model", "fm_adoption", -1, (2018, 2026)))
        self.assertEqual(rc.FAMILIES, {"rq1": ["H1d"], "rq2": ["H2b'", "H2c'"], "rq3": ["H3a"], "h4fl": ["H4-FL"]})
        for h, v in rc.REGISTERED["hypotheses"].items():
            self.assertEqual(v["sign"], rc.SIGN[h])
        self.assertEqual(rc.RQ3_DGP_HI.sd_cell, 0.04)
        self.assertEqual(rc.MULTS, (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0))


class HolmFamilies(unittest.TestCase):
    VARIANTS = ["k75", "k150", "balanced", "early", "early_prospective", "stable_papers", "coherent_topics",
                "certain_labels", "without_2026", "id_consistent_years"]

    def test_h2_pair_is_one_family_and_h2a_does_not_enter(self):
        signs = {"H2a": -1, "H2b": +1, "H2c": -1}
        for p_a in (0.001, 0.9):
            rows = rows_for({"H2a": (-0.01, p_a), "H2b": (0.03, 0.03), "H2c": (-0.01, 0.06)}, signs, self.VARIANTS)
            v = rc.redecide(rows, rc.SPECS2)
            self.assertEqual(set(v), {"H2b'", "H2c'"})
            self.assertAlmostEqual(v["H2b'"]["p"], 0.015)
            self.assertAlmostEqual(v["H2c'"]["p"], 0.03)
            ph = holm(pd.Series({"H2b'": 0.015, "H2c'": 0.03}))
            self.assertAlmostEqual(v["H2b'"]["p_holm"], ph["H2b'"])
            self.assertAlmostEqual(v["H2c'"]["p_holm"], ph["H2c'"])
            self.assertEqual(v["H2b'"]["verdict"], "supported")
            self.assertEqual(v["H2c'"]["verdict"], "supported")
            self.assertAlmostEqual(v["H2b'"]["p_two_sided"], 0.03)

    def test_singleton_families(self):
        rows = rows_for({"H3a": (-0.02, 0.08), "H3b": (-0.01, 0.0001)}, {"H3a": -1, "H3b": -1}, self.VARIANTS[:9] + ["logit"])
        v = rc.redecide(rows, rc.SPECS3)
        self.assertEqual(set(v), {"H3a"})
        self.assertAlmostEqual(v["H3a"]["p"], 0.04)
        self.assertAlmostEqual(v["H3a"]["p_holm"], 0.04)                  # H3b does not share the family any more
        self.assertEqual(v["H3a"]["verdict"], "supported")

    def test_wrong_sign_is_never_significant(self):
        rows = rows_for({"H2b": (-0.05, 0.0001), "H2c": (0.05, 0.0001)}, {"H2b": +1, "H2c": -1}, self.VARIANTS)
        v = rc.redecide(rows, rc.SPECS2)
        for h in v:
            self.assertGreater(v[h]["p"], 0.5)
            self.assertNotIn(v[h]["verdict"], ("supported", "significant in the opposite direction"))

    def test_counted_and_hindsight_rules_still_apply(self):
        main = {"H2b": (0.03, 0.001), "H2c": (-0.03, 0.001)}
        signs = {"H2b": +1, "H2c": -1}
        v = rc.redecide(rows_for(main, signs, self.VARIANTS, {"H2b": {"balanced"}, "H2c": {"k75", "k150", "early"}}), rc.SPECS2)
        self.assertFalse(v["H2b'"]["hindsight_variants_same_sign"])
        self.assertNotEqual(v["H2b'"]["verdict"], "supported")
        self.assertAlmostEqual(v["H2c'"]["robustness_same_sign"], 0.7)
        self.assertNotEqual(v["H2c'"]["verdict"], "supported")
        rows = rows_for(main, signs, self.VARIANTS)
        rows.loc[(rows.hypothesis == "H2b") & (rows.variant == "k75"), "coef"] = np.nan      # missing = wrong sign (D9)
        self.assertIn("k75", rc.redecide(rows, rc.SPECS2)["H2b'"]["variants_wrong_sign"])

    def test_s11_stress_and_labels(self):
        rows = rows_for({"H2a": (0.01, 0.5), "H2b": (0.03, 0.02), "H2c": (-0.02, 0.04)}, {"H2a": -1, "H2b": 1, "H2c": -1},
                        self.VARIANTS)
        s11 = rc.s11_one_sided(rows, rc.SPECS2)
        self.assertAlmostEqual(s11["H2b'"]["p"], 0.02)                        # S11 two-sided p 0.04, made one-sided
        self.assertAlmostEqual(s11["H2b'"]["p_two_sided"], 0.04)
        v = rc.redecide(rows, rc.SPECS2)
        st = rc.stressed_one_sided(v, rc.SPECS2, {"H2b'": 1.3, "H2c'": 1.2})
        self.assertEqual(set(st), {"H2b'", "H2c'"})
        self.assertLess(st["H2b'"]["p_stress"], 0.5)
        labelled = rc.label_rows(rows)
        self.assertEqual(set(labelled[labelled.hypothesis == "H2a"].confirmation_hypothesis), {rc.NOT_REGISTERED})
        self.assertEqual(set(labelled[labelled.hypothesis == "H2b"].confirmation_hypothesis), {"H2b'"})


class Frames(unittest.TestCase):
    def pooled(self):
        ids = pd.Series([f"p{i}" for i in range(8)])
        k = pd.DataFrame({"submission_id": ids, "year": [2018, 2018, 2019, 2019, 2020, 2020, 2021, 2021],
                          "fm_adoption": np.linspace(0, 0.7, 8)})
        return {"k100": k, "k75": k.assign(topic="t")}, ids

    def test_split_after_construction(self):
        pooled, ids = self.pooled()
        mask = np.array([0, 1, 0, 1, 0, 1, 1, 0], bool)
        got = rc.split_frames(pooled, mask)
        for m in pooled:
            self.assertEqual(list(got[m].submission_id), list(ids[mask]))
            self.assertEqual(list(got[m].index), list(range(mask.sum())))
        self.assertEqual(list(got["k100"].fm_adoption), list(pooled["k100"].fm_adoption[mask]))   # pooled values kept
        bad = {**pooled, "k75": pooled["k75"].iloc[::-1]}
        with self.assertRaises(SystemExit):
            rc.split_frames(bad, mask)

    def test_split_mask_checks(self):
        _, ids = self.pooled()
        split = pd.Series(["discovery", "confirmation"] * 4)
        corpus = pd.DataFrame({"submission_id": ids, "split": split})
        released, discovery = ids[split.eq("confirmation")], ids[split.eq("discovery")]
        self.assertEqual(list(rc.split_mask(ids, corpus, released, discovery)), list(split.eq("confirmation")))
        for args in [(ids, corpus, released[:-1], discovery), (ids, corpus, released, discovery.iloc[::-1]),
                     (ids.iloc[::-1], corpus, released, discovery), (ids, corpus, released, pd.concat([discovery, released[:1]])),
                     (ids, corpus.assign(split="holdout"), released, discovery)]:
            with self.assertRaises(SystemExit):
                rc.split_mask(*args)


class Runner(unittest.TestCase):
    def test_real_labels_are_refused_outside_the_entry(self):
        settings = {"h2d_gate_passed": False, "remedies": [], "stress_t_inflation": {}}
        with self.assertRaises(PermissionError):
            rc.rq_part({}, settings, lambda ids: None)                        # guard before any frame is touched

    def test_attempts_are_logged_and_a_rerun_needs_a_reason(self):
        calls = []
        def boom(freeze, started):
            raise RuntimeError("boom")
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(rc, "OUT", Path(tmp)), \
                mock.patch.object(rc, "POOLED_READS", (Path(tmp) / "none1", Path(tmp) / "none2")), \
                mock.patch.object(rc, "check_corpus", lambda: None), mock.patch.object(rc, "run", boom), \
                mock.patch.object(outcomes, "require_frozen", lambda: calls.append("verify") or {}), \
                mock.patch.object(outcomes, "release", lambda: calls.append("release")), \
                mock.patch.object(outcomes, "sha256", lambda path: "x"):
            log = Path(tmp) / "attempts.jsonl"
            with mock.patch.object(rc, "ph5_available", lambda: False), \
                    mock.patch.object(sys, "argv", ["run_confirmation.py"]), self.assertRaises(SystemExit) as e:
                rc.main()
            self.assertIn("ph5_confirm", str(e.exception))
            self.assertEqual(calls, [])                                      # refused before any verification
            for argv in (["--without-ph5"], ["--without-ph5", "--rerun-reason", "test"]):
                with mock.patch.object(sys, "argv", ["run_confirmation.py", *argv]), self.assertRaises(SystemExit) as e:
                    rc.main()                                                # PH5 always runs in the real run
                self.assertIn("--simulate only", str(e.exception))
            self.assertEqual(calls, [])
            log.write_text(json.dumps({"attempt": 1, "status": "started"}) + "\n")
            with mock.patch.object(sys, "argv", ["run_confirmation.py"]), self.assertRaises(SystemExit):
                rc.main()
            self.assertEqual(calls, [])
            with mock.patch.object(sys, "argv", ["run_confirmation.py", "--rerun-reason", "test"]), \
                    self.assertRaises(RuntimeError):
                rc.main()
            self.assertEqual(calls, ["verify", "release"])                   # released although the run failed
            lines = [json.loads(x) for x in log.read_text().splitlines()]
            self.assertEqual([x["status"] for x in lines], ["started", "started", "failed"])
            self.assertEqual((lines[1]["attempt"], lines[1]["rerun_reason"], lines[1]["with_ph5"]), (2, "test", True))
            self.assertIn("boom", lines[2]["traceback"])

    def test_no_attempt_after_a_pooled_read(self):
        """Once the pooled main run or pooled post hoc has (possibly) read confirmation outcomes, no confirmation
        attempt, rerun included, may start (PH5 or anything else could otherwise be confirmed after pooled results)."""
        calls = []
        self.assertEqual(rc.POOLED_READS, (common.POOLED_OUTPUT / "frozen_run" / "attempts.jsonl",
                                           common.POOLED_OUTPUT / "posthoc" / "access_log.jsonl",
                                           common.POOLED_OUTPUT / "rq1_results.csv", common.POOLED_OUTPUT / "figures"))
        with tempfile.TemporaryDirectory() as tmp:
            reads = (Path(tmp) / "frozen_attempts.jsonl", Path(tmp) / "access_log.jsonl", Path(tmp) / "rq1_results.csv",
                     Path(tmp) / "figures")
            with mock.patch.object(rc, "OUT", Path(tmp)), mock.patch.object(rc, "POOLED_READS", reads), \
                    mock.patch.object(rc, "check_corpus", lambda: None), mock.patch.object(rc, "ROOT", Path(tmp)), \
                    mock.patch.object(rc, "run", lambda *a: calls.append("run")), \
                    mock.patch.object(outcomes, "require_frozen", lambda: calls.append("verify") or {}), \
                    mock.patch.object(outcomes, "release", lambda: None), mock.patch.object(outcomes, "sha256", lambda p: "x"):
                for f in reads:
                    f.write_text("{}\n")
                    for argv in ([], ["--rerun-reason", "after pooled"]):
                        with mock.patch.object(sys, "argv", ["run_confirmation.py", *argv]), \
                                self.assertRaises(SystemExit) as e:
                            rc.main()
                        self.assertIn("no confirmation attempt", str(e.exception))
                    f.unlink()
                self.assertEqual(calls, [])
                with mock.patch.object(sys, "argv", ["run_confirmation.py"]):
                    rc.main()
                self.assertEqual(calls, ["verify", "run"])

    def test_the_freeze_pins_the_ph5_registration(self):
        import ph5_confirm
        frozen = {"registered": json.loads(json.dumps(rc.REGISTERED)), "ph5_hook_present": True,
                  "registered_ph5": json.loads(json.dumps(ph5_confirm.REGISTERED))}
        rc.check_registration(frozen)
        for change, msg in [({"registered_ph5": {**frozen["registered_ph5"], "one_sided_rule": "x"}}, "PH5 registration"),
                            ({"registered_ph5": None}, "PH5 registration"),
                            ({"ph5_hook_present": False}, "without the PH5 module"),
                            ({"registered": {**frozen["registered"], "status": "x"}}, "registration differs")]:
            with self.assertRaises(SystemExit) as e:
                rc.check_registration({**frozen, **change})
            self.assertIn(msg, str(e.exception))
        with mock.patch.object(rc, "ph5_available", lambda: False), self.assertRaises(SystemExit):
            rc.check_registration(frozen)

    def test_ph5_hook(self):
        self.assertEqual(rc.ph5_available(), (HERE / "ph5_confirm.py").exists())
        fake = types.ModuleType("ph5_confirm")
        fake.compute = lambda frames, out: {"tests": pd.DataFrame({"n": [len(frames["k100"]), len(out)]}), "info": {"ok": 1}}
        with mock.patch.dict(sys.modules, {"ph5_confirm": fake}):
            self.assertTrue(rc.ph5_available())
            got = rc.ph5_part({"k100": pd.DataFrame({"a": [1, 2]})}, pd.DataFrame({"b": [1, 2]}))
        self.assertEqual(got["info"], {"ok": 1})
        self.assertEqual(list(got["tests"].n), [2, 2])

    def test_simulate_refuses_a_discovery_output_directory(self):
        target = common.DISCOVERY_OUTPUT / "confirmation_dryrun"
        with self.assertRaises(SystemExit):
            rc.simulate_run({}, pd.DataFrame(), {}, 1, target)
        self.assertFalse(target.exists())

    def test_mde80_interpolation(self):
        self.assertAlmostEqual(rc.mde80((1, 2, 3), [0.2, 0.6, 1.0]), 2.5)
        self.assertEqual(rc.mde80((1, 2), [0.9, 1.0]), 1.0)
        self.assertIsNone(rc.mde80((1, 2), [0.1, 0.5]))


class SimulatedEndToEnd(unittest.TestCase):
    """--simulate on stand-in data: the discovery frames (outcome-free features) with a random quarter of the papers as
    the pseudo-confirmation split, simulated labels and acceptance, a reduced MDE grid. Writes to a temporary
    directory only; the discovery outputs must not change."""

    @classmethod
    def setUpClass(cls):
        cls.before = git_status(DISCOVERY_DIRS)
        pooled = {m: panel.frame(m) for m in panel.MAPS}
        mask = np.random.default_rng(0).random(len(pooled["k100"])) < 0.25
        cls.frames = rc.split_frames(pooled, mask)
        settings = json.loads(outcomes.FREEZE_DISCOVERY.read_text())
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name) / "dry"
        cls.settings, kept, write = settings, {}, rc.write_results
        with mock.patch.object(rc, "GRID", {h: g[::3] for h, g in rc.GRID.items()}), contextlib.redirect_stdout(io.StringIO()), \
                mock.patch.object(rc, "write_results", lambda res, *a: (kept.setdefault("res", res), write(res, *a))):
            cls.summary = rc.simulate_run(cls.frames, pooled["k100"][~mask].reset_index(drop=True), settings, 3, cls.out,
                                          mde_reps=2, with_ph5=False)
        cls.res = kept["res"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs(self):
        for f in ["h1d.csv", "rq2_rows.csv", "rq3_rows.csv", "h4fl.csv", "h4fl_cells.csv", "summary.json", "stdout.txt",
                  "mde.json"]:
            self.assertTrue((self.out / f).exists(), f)
        s = json.loads((self.out / "summary.json").read_text())
        self.assertIn("SIMULATED", s["mode"])
        self.assertEqual(list(s["rq1"]["verdicts"]), ["H1d"])
        self.assertEqual(list(s["rq2"]["verdicts"]), ["H2b'", "H2c'"])
        self.assertEqual(list(s["rq3"]["verdicts"]), ["H3a"])
        self.assertEqual(set(json.loads((self.out / "mde.json").read_text())["mde80"]), set(rc.SIGN))
        self.assertEqual(s["papers"]["confirmation_frame"], len(self.frames["k100"]))

    def test_one_sided_p_and_holm_in_every_family(self):
        s = self.summary
        for part in ("rq1", "rq2", "rq3"):
            v = s[part]["verdicts"]
            p1 = {h: rc.one_sided(x["p_two_sided"], x["coef"], rc.SIGN[h]) for h, x in v.items()}
            ph = holm(pd.Series(p1).fillna(1.0))
            for h, x in v.items():
                self.assertAlmostEqual(x["p"], p1[h])
                self.assertAlmostEqual(x["p_holm"], ph[h])
        p = s["h4fl"]["primary"]
        self.assertAlmostEqual(p["p"], rc.one_sided(p["p_two_sided"], p["coef"], -1))
        boot = s["rq2"]["bootstrap_exact_one_sided"]
        for h in ("H2b'", "H2c'"):                     # the sensitivity uses exactly the registered draws
            self.assertAlmostEqual(boot[h]["p_two_sided_same_draws"], s["rq2"]["verdicts"][h]["p_two_sided"])

    def test_no_sesoi_means_no_underpowered_flag(self):
        """With a confirmation MDE80: H1d and H4-FL (no SESOI) are never 'underpowered at 3 x SESOI' (None), in the
        verdicts and in E9; a hypothesis with a SESOI is flagged against 3 x its SESOI; H4-FL carries its MDE80."""
        for m, flag in [(0.05, True), (0.001, False)]:
            st = {**self.settings, "confirmation_mde80": {"mde80": {h: m for h in rc.SIGN}}}
            s = rc.summarise(self.res, st, "test", self.frames)
            self.assertIsNone(s["rq1"]["verdicts"]["H1d"]["underpowered_at_3x_sesoi"])
            self.assertEqual(s["rq3"]["verdicts"]["H3a"]["underpowered_at_3x_sesoi"], flag)       # SESOI 0.01
            self.assertEqual((s["h4fl"]["primary"]["mde80"], s["h4fl"]["primary"]["underpowered_at_3x_sesoi"]), (m, None))
            for r in s["e9_equivalence"]:
                if r["hypothesis"] == "H1d":
                    self.assertIsNone(r["underpowered_at_3x_sesoi"])
                    self.assertIn("no SESOI", r["mde80_note"])
                elif r["hypothesis"] == "H3a":
                    self.assertEqual(r["underpowered_at_3x_sesoi"], flag)
        s = rc.summarise(self.res, self.settings, "test", self.frames)                       # no confirmation MDE
        self.assertTrue(all(r["underpowered_at_3x_sesoi"] is None for r in s["e9_equivalence"]))

    def test_label_reliability_is_the_confirmation_second_pass(self):
        rel = self.summary["rq2"]["label_reliability"]
        lab = pd.read_csv(common.TOPICS / "paper_contributions.csv.gz")
        ids = set(self.frames["k100"].submission_id)
        sp = lab[lab.submission_id.isin(ids) & lab.second_pass_primary_type.notna()]
        conf = rel["confirmation_second_pass"]
        self.assertEqual(conf["second_pass_papers"], len(sp))
        self.assertLess(len(sp), rel["pooled_second_pass_and_s8_reference"]["second_pass_papers"])
        first, second = sp.primary_type.map(common.class_of), sp.second_pass_primary_type.map(common.class_of)
        self.assertAlmostEqual(conf["main_class"]["agreement"], round(float((first == second).mean()), 4))
        a, b = first.eq("method"), second.eq("method")
        pe = a.mean() * b.mean() + (1 - a.mean()) * (1 - b.mean())
        self.assertAlmostEqual(conf["method"]["second_pass_kappa"], round(((a == b).mean() - pe) / (1 - pe), 4))
        self.assertIn("false_positive_rate", rel["pooled_second_pass_and_s8_reference"]["method"])

    def test_rows_are_labelled_and_h1d_has_every_variant(self):
        rows = pd.read_csv(self.out / "rq2_rows.csv")
        self.assertEqual(set(rows[rows.hypothesis == "H2a"].confirmation_hypothesis), {rc.NOT_REGISTERED})
        h1 = pd.read_csv(self.out / "h1d.csv")
        self.assertEqual(list(h1.variant), ["main"] + list(rc.variants.SHARED))

    def test_discovery_outputs_untouched(self):
        self.assertEqual(git_status(DISCOVERY_DIRS), self.before)


class FreezeConfirmation(unittest.TestCase):
    def test_refuses_once_an_attempt_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            log, target = Path(tmp) / "attempts.jsonl", Path(tmp) / "FREEZE_CONFIRMATION.json"
            log.write_text(json.dumps({"attempt": 1, "status": "started"}) + "\n")
            with mock.patch.object(outcomes, "CONFIRMATION_ATTEMPTS", log), mock.patch.object(freeze_confirmation, "TARGET", target), \
                    mock.patch.object(sys, "argv", ["freeze_confirmation.py", "--created", "x"]), self.assertRaises(SystemExit) as e:
                freeze_confirmation.main()
            self.assertIn("attempted", str(e.exception))
            self.assertFalse(target.exists())

    def test_refuses_a_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "FREEZE_CONFIRMATION.json"
            with mock.patch.object(outcomes, "CONFIRMATION_ATTEMPTS", Path(tmp) / "none.jsonl"), \
                    mock.patch.object(freeze_confirmation, "TARGET", target), \
                    mock.patch.object(freeze_confirmation, "TOPIC_CODE", ["no_such_module.py"]), \
                    mock.patch.object(sys, "argv", ["freeze_confirmation.py", "--created", "x"]), self.assertRaises(SystemExit) as e:
                freeze_confirmation.main()
            self.assertIn("no_such_module.py", str(e.exception))
            self.assertFalse(target.exists())

    def test_file_list(self):
        with tempfile.TemporaryDirectory() as tmp:
            pooled, topics = Path(tmp) / "output_pooled", Path(tmp) / "topics_pooled"
            for f in [pooled / "inputs" / "a.csv.gz", pooled / "frozen_run" / "x.json", pooled / "confirmation_run" / "attempts.jsonl",
                      pooled / "confirmation_dryrun" / "mde.json", pooled / "__pycache__" / "c.pyc", topics / "topic_assignments.csv.gz"]:
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text("x")
            with mock.patch.object(freeze_confirmation, "POOLED_OUTPUT", pooled), mock.patch.object(freeze_confirmation, "POOLED_TOPICS", topics):
                files = set(freeze_confirmation.files())
            for f in [pooled / "inputs" / "a.csv.gz", pooled / "frozen_run" / "x.json", pooled / "confirmation_dryrun" / "mde.json",
                      topics / "topic_assignments.csv.gz"]:
                self.assertIn(f, files)
            for f in [pooled / "confirmation_run" / "attempts.jsonl", pooled / "__pycache__" / "c.pyc"]:
                self.assertNotIn(f, files)
        cache = ROOT / "research" / "topics" / "cache"
        required = [*outcomes.sealed_files_all(), *freeze_confirmation.AUTHOR_TABLES, HERE / "PREREGISTRATION.md",
                    HERE / "FREEZE.json", HERE / "run_confirmation.py", HERE / "outcomes.py", HERE / "tests" / "test_sealed_loader.py",
                    cache / "specter2.npy", cache / "specter2_ids.csv",
                    *[ROOT / "research" / "topics" / c for c in freeze_confirmation.TOPIC_CODE]]
        if (cache / "specter2_released.npy").exists():
            required += [cache / "specter2_released.npy", cache / "specter2_released_ids.csv"]
        files = set(freeze_confirmation.files())
        for f in required:
            self.assertIn(f, files)
        discovery = {f for f in files if common.DISCOVERY_OUTPUT in f.parents}
        self.assertEqual(discovery, set(freeze_confirmation.DISCOVERY_RECORDS))
        self.assertFalse(any("output_pooled" in f.parts and f.suffix == ".py" for f in freeze_confirmation.code_files()))

    def test_pooled_copies_and_author_table_are_checked(self):
        frozen = json.loads(outcomes.FREEZE_DISCOVERY.read_text())
        with tempfile.TemporaryDirectory() as tmp:
            pooled = Path(tmp)
            for c in build_pooled_inputs.COPIES:
                shutil.copyfile(common.DISCOVERY_OUTPUT / c, pooled / c)
            authors, manifest = pooled / "inputs" / "a.csv.gz", pooled / "pooled_inputs.json"
            authors.parent.mkdir()
            authors.write_bytes(b"rows")
            manifest.write_text(json.dumps({"authors": {"sha256": hashlib.sha256(b"rows").hexdigest()}}))
            with mock.patch.object(freeze_confirmation, "POOLED_OUTPUT", pooled), \
                    mock.patch.object(freeze_confirmation, "AUTHORS", authors), mock.patch.object(freeze_confirmation, "MANIFEST", manifest):
                freeze_confirmation.check_pooled_inputs(frozen)
                authors.write_bytes(b"other rows")
                with self.assertRaises(SystemExit):
                    freeze_confirmation.check_pooled_inputs(frozen)
                authors.write_bytes(b"rows")
                (pooled / "resubmission_tau.json").write_text("{}")
                with self.assertRaises(SystemExit):
                    freeze_confirmation.check_pooled_inputs(frozen)


class RunPooled(unittest.TestCase):
    def test_needs_a_finished_confirmation_attempt(self):
        calls = []
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(run_pooled, "check_corpus", lambda: None), \
                mock.patch.object(run_pooled.run_frozen, "main", lambda: calls.append("rq2/rq3")), \
                mock.patch.object(run_pooled.rq1_rise, "main", lambda: calls.append("rq1")):
            log = Path(tmp) / "attempts.jsonl"
            with mock.patch.object(outcomes, "CONFIRMATION_ATTEMPTS", log):
                for statuses, ph5 in [(None, True), (["started"], True), (["started", "failed"], True),
                                      (["started", "finished"], False), (["started", "finished"], None)]:
                    if statuses is not None:                         # a run without PH5 opens nothing
                        log.write_text("".join(json.dumps({"status": s, **({} if ph5 is None else {"with_ph5": ph5})})
                                               + "\n" for s in statuses))
                    with mock.patch.object(sys, "argv", ["run_pooled.py"]), self.assertRaises(SystemExit):
                        run_pooled.main()
                self.assertEqual(calls, [])
                log.write_text("".join(json.dumps({"status": s, "with_ph5": True}) + "\n" for s in ["started", "finished"]))
                with mock.patch.object(sys, "argv", ["run_pooled.py"]):
                    run_pooled.main()
                with mock.patch.object(sys, "argv", ["run_pooled.py", "rq1"]):
                    run_pooled.main()
                with mock.patch.object(sys, "argv", ["run_pooled.py", "rq1", "--out", "x"]), self.assertRaises(SystemExit):
                    run_pooled.main()
        self.assertEqual(calls, ["rq2/rq3", "rq1"])

    def test_pooled_rq1_and_figures_need_the_confirmation_run(self):
        """H1d is a confirmation test: rq1_rise.main (and figures.main, whose F2 shows the labels by year) refuse under
        ICLR_CORPUS=pooled until the confirmation run has finished with PH5, before reading anything; unset, no check.
        In subprocesses with the attempts log pointed at a temporary file, so nothing pooled can ever run here."""
        import rq1_rise
        rq1_rise.require_confirmation_finished()                             # discovery: a no-op
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "attempts.jsonl"
            with mock.patch.object(rq1_rise, "CORPUS", "pooled"), mock.patch.object(outcomes, "CONFIRMATION_ATTEMPTS", log), \
                    mock.patch.object(rq1_rise.pd, "read_csv", side_effect=AssertionError("read before the gate")):
                for content in [None, {"status": "finished", "with_ph5": False}, {"status": "started", "with_ph5": True}]:
                    if content is not None:
                        log.write_text(json.dumps(content) + "\n")
                    with mock.patch.object(sys, "argv", ["rq1_rise.py"]), self.assertRaises(SystemExit) as e:
                        rq1_rise.main()
                    self.assertIn("confirmation run", str(e.exception))
                log.write_text(json.dumps({"status": "finished", "with_ph5": True}) + "\n")
                rq1_rise.require_confirmation_finished()
            env = {**os.environ, "ICLR_CORPUS": "pooled"}
            stop = "lambda *a, **k: sys.exit('past the gate')"                  # even a broken gate computes nothing
            for mod, stubs in [("rq1_rise", ["pd.read_csv", "topic_maps"]),
                               ("figures", ["f1_forest", "f2_trends", "f3_hot_topics", "f4_dose", "f5_validation",
                                            "f6_power", "f7_acceptance"])]:
                code = (f"import sys; from pathlib import Path; import outcomes; outcomes.CONFIRMATION_ATTEMPTS = "
                        f"Path({str(log.with_name('none.jsonl'))!r}); import {mod}; "
                        + "".join(f"{mod}.{f} = {stop}; " for f in stubs) + f"sys.argv = ['{mod}.py']; {mod}.main()")
                r = subprocess.run([PY, "-c", code], cwd=HERE, env=env, capture_output=True, text=True, timeout=300)
                self.assertNotEqual(r.returncode, 0, mod)
                self.assertIn("only allowed after the confirmation run has finished with PH5", r.stderr, mod)


class PooledInputs(unittest.TestCase):
    COLS = ["submission_id", "family_id", "year", "source_list_position", "declared_name_json", "declared_id_key",
            "native_id_kind"]

    def tables(self, d: Path) -> dict[str, Path]:
        """Two synthetic author tables (fake strings only), each sorted by year, paper and position, with commas,
        quotes, \\N and empty fields."""
        def table(prefix: str, years: list[int], n: int) -> pd.DataFrame:
            rows = []
            for i in range(n):
                for pos in range(1 + i % 3):
                    rows.append([f"{prefix}{years[i % len(years)]}_{i:03d}", f"f{i}", years[i % len(years)], pos,
                                 json.dumps([f"A, {i}", 'q"x']), r"\N" if pos == 2 else f"key{(i + pos) % 7}",
                                 "" if pos == 1 else "profile"])
            t = pd.DataFrame(rows, columns=self.COLS)
            return t.sort_values(["year", "submission_id", "source_list_position"], kind="stable")
        out = {"discovery": d / "disc.csv.gz", "confirmation": d / "conf.csv.gz"}
        table("d", [2019, 2020, 2021], 12).to_csv(out["discovery"], index=False)
        table("c", [2020, 2021], 7).to_csv(out["confirmation"], index=False)
        return out

    def constants(self, d: Path) -> tuple[Path, Path]:
        src = d / "src"
        src.mkdir()
        for c in build_pooled_inputs.COPIES:
            (src / c).write_text(f"constant {c}")
        freeze = d / "FREEZE.json"
        freeze.write_text(json.dumps({"sha256": {str(src / c): outcomes.sha256(src / c) for c in build_pooled_inputs.COPIES}}))
        return src, freeze

    def test_build_is_deterministic_ordered_and_exact(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            sources = self.tables(d)
            src, freeze = self.constants(d)
            runs = [build_pooled_inputs.build(sources, d / f"out{i}" / "inputs" / "a.csv.gz", src, d / f"out{i}", freeze)
                    for i in (1, 2)]
            self.assertEqual(runs[0]["authors"]["sha256"], runs[1]["authors"]["sha256"])
            pooled = build_pooled_inputs.read_text(d / "out1" / "inputs" / "a.csv.gz")
            key = list(zip(pooled.year.astype(int), pooled.submission_id, pooled.source_list_position.astype(int)))
            self.assertEqual(key, sorted(key))
            for split, path in sources.items():
                part = pooled[pooled.submission_id.str[0] == split[0]].reset_index(drop=True)
                pd.testing.assert_frame_equal(part, build_pooled_inputs.read_text(path))
            self.assertIn(r"\N", set(pooled.declared_id_key))
            self.assertEqual(runs[0]["authors"]["by_split"]["confirmation"]["papers"], 7)
            for c in build_pooled_inputs.COPIES:
                self.assertEqual((d / "out1" / c).read_bytes(), (src / c).read_bytes())

    def test_refusals(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            sources = self.tables(d)
            src, freeze = self.constants(d)
            target = lambda: (d / "o" / "inputs" / "a.csv.gz", src, d / "o", freeze)
            clash = pd.read_csv(sources["confirmation"])
            clash.loc[0, "submission_id"] = pd.read_csv(sources["discovery"]).submission_id[0]
            clash.to_csv(d / "clash.csv.gz", index=False)
            with self.assertRaises(SystemExit):
                build_pooled_inputs.build({**sources, "confirmation": d / "clash.csv.gz"}, *target())
            pd.read_csv(sources["confirmation"]).rename(columns={"family_id": "family"}).to_csv(d / "hdr.csv.gz", index=False)
            with self.assertRaises(SystemExit):
                build_pooled_inputs.build({**sources, "confirmation": d / "hdr.csv.gz"}, *target())
            (src / "resubmission_tau.json").write_text("changed")
            with self.assertRaises(SystemExit):
                build_pooled_inputs.build(sources, *target())
            with self.assertRaises(SystemExit):
                build_pooled_inputs.build(sources, common.DISCOVERY_OUTPUT / "inputs" / "a.csv.gz", src, d / "o", freeze)
        self.assertFalse((common.DISCOVERY_OUTPUT / "inputs").exists())


class FrozenCentringMean(unittest.TestCase):
    def test_pooled_resubmissions_reuse_the_frozen_mean_and_tau(self):
        with tempfile.TemporaryDirectory() as tmp:
            pooled = Path(tmp)
            with mock.patch.object(resubmissions, "OUTPUT", pooled):
                with self.assertRaises(SystemExit):                          # no pooled copy yet
                    resubmissions.frozen_constants(None)
                shutil.copyfile(common.DISCOVERY_OUTPUT / "specter2_centring_mean.npy", pooled / "specter2_centring_mean.npy")
                mean, tau = resubmissions.frozen_constants(None)
                self.assertTrue(np.array_equal(mean, np.load(common.DISCOVERY_OUTPUT / "specter2_centring_mean.npy")))
                self.assertEqual(tau, 0.9)
                self.assertEqual(resubmissions.frozen_constants(0.9)[1], 0.9)
                with self.assertRaises(SystemExit):
                    resubmissions.frozen_constants(0.95)
                np.save(pooled / "specter2_centring_mean.npy", mean + 1e-3)
                with self.assertRaises(SystemExit):
                    resubmissions.frozen_constants(None)


if __name__ == "__main__":
    unittest.main()
