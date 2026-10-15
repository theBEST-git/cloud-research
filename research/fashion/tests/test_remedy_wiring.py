"""Behavioural tests of the D16 remedy and the S11 cross-check (review round B4): FREEZE.json remedies -> run_frozen.run
-> rq2/rq3.run -> bootstrap p-value in the Holm family; S11 rows and the early-map clustering; the dry-run's v3 wiring;
freeze.py's consistency checks. Simulated outcomes only (the RQ2 outcome-side columns are all replaced, RQ3 outcomes come
from the simulated loader); no real outcome is read.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import analysis  # noqa: E402
import dryrun  # noqa: E402
import freeze  # noqa: E402
import outcomes  # noqa: E402
import panel  # noqa: E402
import rq2_following as rq2  # noqa: E402
import rq3_reward as rq3  # noqa: E402
import run_frozen  # noqa: E402
from common import OUTPUT  # noqa: E402
from dgp import DGP  # noqa: E402
from ols import fe_ols  # noqa: E402
from variants import holm  # noqa: E402

MAPS = ("k100", "k75", "k150", "balanced", "early")          # every map a counted variant uses
S11 = "S11_twoway_topic_early"
F: dict = {}


def setUpModule():
    frames = {m: panel.frame(m) for m in MAPS}
    k = frames["k100"]
    ids = k.submission_id
    rng = np.random.default_rng(7)
    topic = pd.Series(rng.normal(0, 0.4, k.topic.nunique()), index=k.topic.unique()).reindex(k.topic).to_numpy()
    early = pd.Series(rng.normal(0, 0.4, k.topic_early.nunique()), index=k.topic_early.unique()).reindex(k.topic_early).to_numpy()
    ys = {c: pd.Series((rng.random(len(k)) < 1 / (1 + np.exp(1.2 - topic - early))).astype(float), index=ids.values)
          for c in sorted(rq2.SIMULATED)}
    out = outcomes.load("simulated", ids, seed=3, frame=k, dgp=dryrun.RQ3_DGP["hi"])
    F.update(frames=frames, ys=ys, out=out, pop2=rq2.population(rq2.with_columns(k, ys)))
    full = rq3.attach(k, out)
    F["pop3"] = full[full.rq3]


def boot(pop, s):
    return analysis.wild_cluster_bootstrap_p(pop, s.y, s.x, s.controls, s.fe, s.years, draws=9999, seed=20261015)


def spec(specs, h):
    return next(s for s in specs if s.hid == h)


class RegisteredBootstrap(unittest.TestCase):
    def test_registered_draws_and_seed(self):
        self.assertEqual((analysis.BOOT_DRAWS, analysis.BOOT_SEED), (9999, 20261015))
        self.assertEqual(dryrun.REMEDIES, ("H2b", "H2c"))


class RQ2Remedy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plain = rq2.run(F["frames"], False, ys=F["ys"], supplementary=True)
        cls.rem = rq2.run(F["frames"], False, ys=F["ys"], supplementary=True, remedies=dryrun.REMEDIES)
        cls.boot = {h: boot(F["pop2"], spec(rq2.SPECS, h)) for h in dryrun.REMEDIES}

    def test_remedied_p_is_the_registered_bootstrap_on_the_rq2_population(self):
        for h in dryrun.REMEDIES:
            v = self.rem["verdicts"][h]
            self.assertEqual(v["p"], self.boot[h]["p"], h)
            self.assertNotEqual(v["p"], v["p_cr1"], h)                       # the test can tell the two apart
            self.assertEqual(v["p_cr1"], self.plain["verdicts"][h]["p"], h)
            self.assertEqual(v["p_method"], "wild cluster restricted bootstrap (Rademacher by topic, 9999 draws)")
            self.assertAlmostEqual(v["p"] * 9999, round(v["p"] * 9999), places=6)

    def test_other_hypotheses_keep_cr1(self):
        v = self.rem["verdicts"]["H2a"]
        self.assertEqual((v["p"], v["p_method"]), (self.plain["verdicts"]["H2a"]["p"], "CR1, t(G-1)"))
        self.assertEqual(v["p_cr1"], v["p"])

    def test_holm_family_uses_the_bootstrap_p(self):
        p = pd.Series({"H2a": self.plain["verdicts"]["H2a"]["p"], **{h: self.boot[h]["p"] for h in dryrun.REMEDIES}})
        expect = holm(p)
        for h in p.index:
            self.assertAlmostEqual(self.rem["verdicts"][h]["p_holm"], expect[h], places=12, msg=h)
        self.assertNotEqual([self.rem["verdicts"][h]["p_holm"] for h in p.index],
                            [self.plain["verdicts"][h]["p_holm"] for h in p.index])

    def test_remedy_changes_nothing_but_the_p_value(self):
        for h in self.rem["verdicts"]:
            a, b = self.plain["verdicts"][h], self.rem["verdicts"][h]
            for k in ["coef", "se", "ci95", "ci90", "tost_p", "robustness_same_sign", "hindsight_variants_same_sign", "n"]:
                self.assertEqual(a[k], b[k], f"{h} {k}")
        cols = ["hypothesis", "variant", "coef", "se", "p"]
        rest = lambda r: r["rows"][(r["rows"].kind != "main") & (r["rows"].variant != "S8_misclassification")][cols]
        pd.testing.assert_frame_equal(rest(self.plain).reset_index(drop=True), rest(self.rem).reset_index(drop=True))
        s8 = lambda r, h: r["rows"].set_index(["hypothesis", "variant"]).loc[(h, "S8_misclassification")]
        for h in dryrun.REMEDIES:                     # S8 rescales the main estimate, so it carries the main p-value
            self.assertEqual((s8(self.rem, h).coef, s8(self.rem, h).p), (s8(self.plain, h).coef, self.boot[h]["p"]))

    def test_main_rows_carry_both_p_values(self):
        rows = self.rem["rows"].set_index(["hypothesis", "variant"])
        for h in dryrun.REMEDIES:
            self.assertEqual(rows.loc[(h, "main"), "p"], self.boot[h]["p"])
            self.assertEqual(rows.loc[(h, "main"), "p_cr1"], self.plain["verdicts"][h]["p"])

    def test_s11_row_for_every_hypothesis_with_early_map_clusters(self):
        rows = self.rem["rows"].set_index(["hypothesis", "variant"])
        for s in rq2.SPECS:
            if s.gated:
                continue
            r = rows.loc[(s.hid, S11)]
            self.assertEqual(r.kind, "supplementary")
            ref = analysis.estimate_twoway(F["pop2"], s.y, s.x, s.controls, s.fe, s.years, cluster2="topic_early")
            self.assertEqual((r.coef, r.se, r.p), (ref["coef"], ref["se"], ref["p"]), s.hid)
            d = analysis._design(F["pop2"], s.y, s.x, s.controls, s.fe, s.years)[0]
            self.assertEqual(r.clusters2, d.topic_early.nunique())
            self.assertNotEqual(r.se, rows.loc[(s.hid, "main"), "se"])


class RQ3Remedy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plain = rq3.run(F["frames"], F["out"], False, supplementary=True)
        cls.registered = rq3.run(F["frames"], F["out"], False, supplementary=False, remedies=dryrun.REMEDIES)
        cls.rem = rq3.run(F["frames"], F["out"], False, supplementary=True, remedies=("H3a",))

    def test_registered_remedies_leave_rq3_on_cr1(self):
        for h, v in self.registered["verdicts"].items():
            self.assertEqual((v["p"], v["p_method"]), (self.plain["verdicts"][h]["p"], "CR1, t(G-1)"))

    def test_a_remedied_rq3_hypothesis_is_bootstrapped_on_the_rq3_population(self):
        v = self.rem["verdicts"]["H3a"]
        self.assertEqual(v["p"], boot(F["pop3"], spec(rq3.SPECS, "H3a"))["p"])
        self.assertNotEqual(v["p"], v["p_cr1"])
        self.assertEqual(self.rem["verdicts"]["H3b"]["p"], self.plain["verdicts"]["H3b"]["p"])
        p = pd.Series({"H3a": v["p"], "H3b": self.plain["verdicts"]["H3b"]["p"]})
        self.assertAlmostEqual(self.rem["verdicts"]["H3b"]["p_holm"], holm(p)["H3b"], places=12)

    def test_s11_row_for_every_hypothesis(self):
        rows = self.plain["rows"].set_index(["hypothesis", "variant"])
        for s in rq3.SPECS:
            if s.gated:
                continue
            ref = analysis.estimate_twoway(F["pop3"], s.y, s.x, s.controls, s.fe, s.years, cluster2="topic_early")
            self.assertEqual((rows.loc[(s.hid, S11), "se"], rows.loc[(s.hid, S11), "p"]), (ref["se"], ref["p"]), s.hid)


class TwoWayClustering(unittest.TestCase):
    def test_topic_early_is_the_early_map_on_every_map(self):
        early = F["frames"]["early"].topic.to_numpy()
        for m in MAPS:
            self.assertTrue((F["frames"][m].topic_early.to_numpy() == early).all(), m)

    def test_cgm_combination_of_one_way_cr1_variances(self):
        rng = np.random.default_rng(5)
        n = 3000
        d = pd.DataFrame({"topic": rng.integers(0, 40, n).astype(str), "topic_early": rng.integers(0, 25, n).astype(str),
                          "year": rng.integers(2019, 2027, n), "c1": rng.normal(size=n)})
        e = rng.normal(0, 0.5, 25)[d.topic_early.astype(int)]
        d["x"] = (rng.random(n) < 0.3 + 0.2 * (e > 0)).astype(float)
        d["y"] = 0.3 * e + 0.2 * d.c1 + rng.normal(size=n)
        tw = analysis.estimate_twoway(d, "y", "x", ("c1",), "topic+year", (2019, 2026))
        X = pd.concat([d[["x", "c1"]], pd.get_dummies(d.year, prefix="y", drop_first=True).astype(float)], axis=1)
        one = lambda g: fe_ols(d.y, X, d.topic, g).loc["x", "se"] ** 2
        v = one(d.topic) + one(d.topic_early) - one(d.topic + "|" + d.topic_early)
        self.assertGreater(v, 0)
        self.assertAlmostEqual(tw["se"], np.sqrt(v), places=12)
        self.assertEqual(tw["dof"], 24)                                    # min(G1, G2) - 1
        self.assertAlmostEqual(tw["coef"], fe_ols(d.y, X, d.topic, d.topic).loc["x", "coef"], places=12)


class FrozenRunPassesRemedies(unittest.TestCase):
    def test_frozen_remedies_reach_both_families_and_the_summary(self):
        seen = {}
        real2, real3 = rq2.run, rq3.run

        def rq2_run(frames, gate, ys=None, supplementary=True, remedies=()):
            seen["rq2"] = (ys, remedies)
            return real2(frames, gate, ys=F["ys"], supplementary=supplementary, remedies=remedies)

        def rq3_run(frames, out, gate, supplementary=True, describe=False, remedies=()):
            seen["rq3"] = (describe, remedies)
            return real3(frames, out, gate, supplementary=supplementary, describe=describe, remedies=remedies)

        exp = {"estimates": pd.DataFrame({"label": [], "measure_status": []}), "acceptance_by_class_year": pd.DataFrame(),
               "dose_response": pd.DataFrame()}
        gate = json.loads((OUTPUT / "h2d_validation.json").read_text())["gate"] == "pass"
        tau = json.loads((OUTPUT / "resubmission_tau.json").read_text())["tau"]
        frz = {"remedies": ["bootstrap:H2b", "bootstrap:H2c"], "h2d_gate_passed": gate, "tau": tau,
               "mde80": {"H2b": 0.01}, "dryrun_criteria": {"c_detected_80pct_at_3x_sesoi": {"H2b": True}}}
        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch.object(run_frozen.panel, "MAPS", MAPS), \
                mock.patch.object(run_frozen.rq2, "run", rq2_run), mock.patch.object(run_frozen.rq3, "run", rq3_run), \
                mock.patch.object(run_frozen.exploratory, "run", lambda *a, **k: exp), \
                mock.patch.object(run_frozen.outcomes, "load", lambda mode, ids, **k: F["out"]), \
                mock.patch.object(run_frozen.outcomes, "sha256", lambda path: "x"), \
                mock.patch.object(run_frozen, "OUT", Path(tmp)), mock.patch("builtins.print"):
            run_frozen.run(frz, "2026-10-15T00:00:00+00:00")
            summary = json.loads((Path(tmp) / "summary.json").read_text())
        self.assertEqual(seen["rq2"], (None, ("H2b", "H2c")))               # real labels in the real run: ys=None
        self.assertEqual(seen["rq3"], (True, ("H2b", "H2c")))
        self.assertEqual(summary["remedies"], ["H2b", "H2c"])
        for h in dryrun.REMEDIES:
            v = summary["rq2"]["verdicts"][h]
            self.assertEqual(v["p"], boot(F["pop2"], spec(rq2.SPECS, h))["p"])
            self.assertIn("bootstrap", v["p_method"])
            self.assertEqual(v["ci_tost_method"], "CR1, t(G-1)")
        self.assertEqual(summary["rq2"]["verdicts"]["H2a"]["p_method"], "CR1, t(G-1)")
        self.assertEqual(set(summary["rq2"]["s11_twoway"]), set(summary["rq2"]["family"]))
        self.assertEqual(set(summary["rq3"]["s11_twoway"]), set(summary["rq3"]["family"]))
        e9 = {r["hypothesis"]: r for r in summary["e9_equivalence"]}
        for h, r in e9.items():
            self.assertEqual(r["p_method"], summary["rq2" if h.startswith("H2") else "rq3"]["verdicts"][h]["p_method"])
            self.assertEqual(r["ci_tost_method"], "CR1, t(G-1)")

    def test_zero_bootstrap_p_is_printed_as_a_bound(self):
        v = {"p": 0.0, "p_method": "wild cluster restricted bootstrap (Rademacher by topic, 9999 draws)"}
        self.assertEqual(run_frozen.p_text(v), "p_boot < 1/9999")
        self.assertEqual(run_frozen.p_text({"p": 0.0123, "p_method": "CR1, t(G-1)"}), "p 0.0123")


class DryRunV3Wiring(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = (dict(dryrun.FRAMES), dict(dryrun.CAL))
        k = F["frames"]["k100"]
        dryrun.FRAMES.update(F["frames"])
        dryrun.FRAMES["k100"] = k.assign(maturity_x_method_c=k.maturity * (k.method - k.method.mean()))
        for c in ["incumbent", "method", "measurement", "buzzword", "lists_hot"]:   # fixed DGPs: no calibration on labels
            dryrun.CAL[c] = DGP(base=0.3, sd_topic=0.05, sd_year=0.02, sd_trend=0.008, sd_cell=0.03)

    @classmethod
    def tearDownClass(cls):
        dryrun.FRAMES.clear(); dryrun.FRAMES.update(cls.saved[0])
        dryrun.CAL.clear(); dryrun.CAL.update(cls.saved[1])

    def test_null_replication_applies_the_remedy_and_records_all_three_p_values(self):
        rows = pd.DataFrame(dryrun.job(("rq2", "rq2_null_early", 0, {"map": "early"}))).set_index("hypothesis")
        ys, _ = dryrun.rq2_outcomes(dryrun.zlib.crc32(b"rq2_null_early") * 1000, "early", None, 0.0)
        pop = rq2.population(rq2.with_columns(dryrun.FRAMES["k100"], ys))
        for h, s in dryrun.RQ2_SPECS.items():
            cr1 = analysis.estimate(pop, s.y, s.x, s.controls, s.fe, s.years)["p"]
            b = boot(pop, s)["p"]
            tw = analysis.estimate_twoway(pop, s.y, s.x, s.controls, s.fe, s.years)["p"]
            self.assertEqual((rows.loc[h, "p_cr1"], rows.loc[h, "p_boot"], rows.loc[h, "p_twoway"]), (cr1, b, tw), h)
            self.assertEqual(rows.loc[h, "p"], b if h in dryrun.REMEDIES else cr1, h)

    def test_power_replication_of_a_remedied_hypothesis_uses_the_bootstrap(self):
        for h in ["H2a", "H2b"]:
            r = dryrun.job(("rq2", f"rq2_power_{h}_m3.0", 0, {"map": "k100", "planted": h, "mult": 3.0, "full": False}))
            self.assertEqual(len(r), 1)
            r = r[0]
            ys, _ = dryrun.rq2_outcomes(dryrun.zlib.crc32(f"rq2_power_{h}_m3.0".encode()) * 1000, "k100", h,
                                        dryrun.RQ2_SPECS[h].sign * 3.0 * dryrun.RQ2_SPECS[h].sesoi)
            pop = rq2.population(rq2.with_columns(dryrun.FRAMES["k100"], ys))
            s = dryrun.RQ2_SPECS[h]
            self.assertEqual(r["p_cr1"], analysis.estimate(pop, s.y, s.x, s.controls, s.fe, s.years)["p"])
            self.assertEqual(r["p"], boot(pop, s)["p"] if h in dryrun.REMEDIES else r["p_cr1"], h)

    def test_summary_size_is_cr1_and_validation_sizes_use_their_own_columns(self):
        rows = []
        for rep in range(20):
            for h, sign in [("H2a", -1), ("H2b", -1), ("H2c", 1)]:
                rows.append({"scenario": "rq2_null_k100", "rep": rep, "hypothesis": h, "planted": False, "coef": 0.01,
                             "se": 0.01, "p": 0.5, "p_cr1": 0.01 if rep < 4 else 0.5, "p_boot": 0.01 if rep < 2 else 0.5,
                             "p_twoway": 0.01 if rep < 1 else 0.5, "p_holm": 0.5, "n": 10, "predicted_sign": sign,
                             "verdict": "inconclusive"})
        s = dryrun.summarise(pd.DataFrame(rows))
        self.assertEqual(s["size"]["rq2_null_k100"]["H2b"], 0.2)          # criterion (a): the CR1 trigger
        self.assertEqual(s["size_bootstrap"]["rq2_null_k100"]["H2b"], 0.1)
        self.assertEqual(s["size_twoway"]["rq2_null_k100"]["H2b"], 0.05)


class FreezeRemedyChecks(unittest.TestCase):
    FAM = {"rq2": ["H2a", "H2b", "H2c"], "rq3": ["H3a", "H3b"]}

    def summary(self):
        hyps = lambda sc: self.FAM["rq2"] if sc.startswith("rq2") else self.FAM["rq3"]
        return {"size_twoway": {sc: {h: 0.05 for h in hyps(sc)} for sc in dryrun.NULL_SCENARIOS},
                "size_bootstrap": {sc: {h: 0.05 for h in hyps(sc)} for sc in dryrun.NULL_SCENARIOS}}

    def test_remedy_validation_must_be_reported(self):
        self.assertEqual(freeze.check_remedy_validation(self.summary(), {"H2b", "H2c"}, self.FAM), [])
        d = self.summary()
        del d["size_bootstrap"]["rq2_null_early"]["H2b"]
        del d["size_twoway"]["rq3_permuted"]["H3a"]
        self.assertEqual(len(freeze.check_remedy_validation(d, {"H2b", "H2c"}, self.FAM)), 2)
        self.assertEqual(len(freeze.check_remedy_validation(d, {"H2c"}, self.FAM)), 1)   # H2a/H2b bootstrap: not required

    def test_null_replications_must_be_complete(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            for sc in dryrun.NULL_SCENARIOS:
                hyps = self.FAM["rq2"] if sc.startswith("rq2") else self.FAM["rq3"]
                rows = [{"rep": r, "hypothesis": h, "p_cr1": 0.5, "p_boot": 0.5, "p_twoway": 0.5} for r in range(3) for h in hyps]
                rows += [{"rep": r, "hypothesis": "H3a:logit", "p": 0.5} for r in range(3) if not sc.startswith("rq2")]
                pd.DataFrame(rows).to_csv(tmp / f"{sc}.csv", index=False)
            self.assertEqual(freeze.check_null_replications(tmp, self.FAM, 3), [])
            self.assertEqual(len(freeze.check_null_replications(tmp, self.FAM, 4)), 2 * 3 + 4 * 2)
            d = pd.read_csv(tmp / "rq2_null_early.csv")
            d.loc[(d.hypothesis == "H2b") & (d.rep == 1), "p_boot"] = np.nan
            d.to_csv(tmp / "rq2_null_early.csv", index=False)
            d = pd.read_csv(tmp / "rq3_permuted.csv").drop(columns="p_twoway")
            d.to_csv(tmp / "rq3_permuted.csv", index=False)
            (tmp / "rq3_null_k100_lo.csv").unlink()
            self.assertEqual(len(freeze.check_null_replications(tmp, self.FAM, 3)), 4)

    def test_dry_run_and_freeze_remedies_must_agree(self):
        freeze.check_remedies_applied(("H2b", "H2c"), {"H2b", "H2c"})
        for asked in [{"H2b"}, set(), {"H2b", "H2c", "H2a"}]:
            with self.assertRaises(SystemExit):
                freeze.check_remedies_applied(("H2b", "H2c"), asked)

    def test_main_runs_every_check_before_writing(self):
        src = (HERE / "freeze.py").read_text().split("def main()")[1]
        order = [src.index(x) for x in ["check_dryrun(", "check_remedy_validation(", "check_null_replications(",
                                        "raise SystemExit", "validate_remedies(", "check_remedies_applied(",
                                        "FREEZE.json\").write_text"]]
        self.assertEqual(order, sorted(order))


if __name__ == "__main__":
    unittest.main()
