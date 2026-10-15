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
import variants  # noqa: E402
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


class S11EntersTheFragileFlag(unittest.TestCase):
    def capture(self, module, run):
        seen = {}
        real = module.decide

        def spy(specs, main, counted, supplementary=None):
            seen.update(supplementary or {})
            return real(specs, main, counted, supplementary)
        with mock.patch.object(module, "decide", spy):
            run()
        return seen

    def test_rq2_and_rq3_pass_s11_to_decide(self):
        supp = self.capture(rq2, lambda: rq2.run(F["frames"], False, ys=F["ys"], supplementary=True))
        for s in (s for s in rq2.SPECS if not s.gated):
            ref = analysis.estimate_twoway(F["pop2"], s.y, s.x, s.controls, s.fe, s.years)
            self.assertEqual(supp[s.hid][S11]["se"], ref["se"], s.hid)
        supp = self.capture(rq3, lambda: rq3.run(F["frames"], F["out"], False, supplementary=True))
        for s in (s for s in rq3.SPECS if not s.gated):
            ref = analysis.estimate_twoway(F["pop3"], s.y, s.x, s.controls, s.fe, s.years)
            self.assertEqual(supp[s.hid][S11]["se"], ref["se"], s.hid)

    def test_a_significant_opposite_s11_makes_a_supported_hypothesis_fragile(self):
        s = analysis.Spec("Hx", "y", "x", -1, 0.02, "topic+year", (2019, 2026))
        est = lambda coef, p: {"coef": coef, "se": 0.01, "p": p, "dof": 99, "n": 1000, "clusters": 100,
                               "ci95_lo": coef - 0.02, "ci95_hi": coef + 0.02, "ci90_lo": coef - 0.016, "ci90_hi": coef + 0.016}
        counted = {"Hx": {v: est(-0.1, 0.001) for v in variants.counted(2)}}
        for s11, fragile in [(est(+0.05, 0.01), True), (est(+0.05, 0.2), False), (est(-0.05, 0.01), False)]:
            v = analysis.decide([s], {"Hx": est(-0.1, 1e-6)}, counted, {"Hx": {S11: s11}})["Hx"]
            self.assertEqual(v["verdict"], "supported")
            self.assertEqual((v["fragile"], v["fragile_by"]), (fragile, [S11] if fragile else []))

    def test_holm_treats_a_missing_p_as_one(self):
        specs = [analysis.Spec(h, "y", "x", -1, 0.02, "topic+year", (2019, 2026)) for h in ["Ha", "Hb", "Hc"]]
        est = lambda p: {"coef": -0.1, "se": 0.01, "p": p, "dof": 99, "n": 1000, "clusters": 100,
                         "ci95_lo": -0.12, "ci95_hi": -0.08, "ci90_lo": -0.116, "ci90_hi": -0.084}
        v = analysis.decide(specs, {"Ha": est(0.01), "Hb": est(np.nan), "Hc": est(0.02)}, {})
        expect = holm(pd.Series({"Ha": 0.01, "Hb": 1.0, "Hc": 0.02}))
        self.assertEqual([v[h]["p_holm"] for h in "Ha Hb Hc".split()], [expect[h] for h in "Ha Hb Hc".split()])


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
        from scipy import stats
        for lvl, lo, hi in [(0.975, "ci95_lo", "ci95_hi"), (0.95, "ci90_lo", "ci90_hi")]:
            q = stats.t.ppf(lvl, 24)
            self.assertAlmostEqual(tw[lo], tw["coef"] - q * tw["se"], places=12)
            self.assertAlmostEqual(tw[hi], tw["coef"] + q * tw["se"], places=12)
        self.assertAlmostEqual(tw["p"], 2 * stats.t.sf(abs(tw["coef"] / tw["se"]), 24), places=12)
        self.assertAlmostEqual(tw["coef"], fe_ols(d.y, X, d.topic, d.topic).loc["x", "coef"], places=12)


class TwoWayFallback(unittest.TestCase):
    def test_non_positive_two_way_variance_falls_back_to_the_larger_one_way_variance(self):
        rng = np.random.default_rng(6)
        d = pd.DataFrame({"topic": rng.integers(0, 30, 2000).astype(str), "topic_early": rng.integers(0, 20, 2000).astype(str),
                          "year": rng.integers(2019, 2027, 2000), "x": rng.normal(size=2000), "y": rng.normal(size=2000)})
        from scipy import stats
        for (v1, v2, v12), se in [((1.0, 2.0, 4.0), np.sqrt(2.0)),       # v1 + v2 - v12 < 0
                                  ((1.0, 1.0, 2.0), 1.0),                # = 0: also the fallback
                                  ((1.0, 2.0, 0.5), np.sqrt(2.5))]:      # > 0: the CGM variance
            def fake(Xd, e, q, groups, v=(v1, v2, v12)):                 # by clustering, not by call order
                g = pd.Series(groups).astype(str)
                if g.str.contains("|", regex=False).all():
                    return v[2], 400
                return (v[0], 30) if pd.Series(groups).name == "topic" else (v[1], 20)
            with mock.patch.object(analysis, "_cluster_variance", side_effect=fake):
                tw = analysis.estimate_twoway(d, "y", "x", (), "topic+year", (2019, 2026))
            self.assertAlmostEqual(tw["se"], se, places=12)
            self.assertEqual((tw["dof"], tw["clusters"], tw["clusters2"]), (19, 30, 20))
            q = stats.t.ppf(0.975, 19)
            self.assertAlmostEqual(tw["ci95_lo"], tw["coef"] - q * se, places=12)
            self.assertAlmostEqual(tw["p"], 2 * stats.t.sf(abs(tw["coef"] / se), 19), places=12)


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
               "mde80": {"H2b": 0.01}, "dryrun_criteria": {"c_detected_80pct_at_3x_sesoi": {"H2b": True}},
               "stress_t_inflation": {"H2b": 1.3, "H2c": 1.2}, "remedy_validation": {"size_bootstrap": {"x": 1}}}
        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch.object(run_frozen.panel, "MAPS", MAPS), \
                mock.patch.object(run_frozen.rq2, "run", rq2_run), mock.patch.object(run_frozen.rq3, "run", rq3_run), \
                mock.patch.object(run_frozen.exploratory, "run", lambda *a, **k: exp), \
                mock.patch.object(run_frozen.outcomes, "load", lambda mode, ids, **k: F["out"]), \
                mock.patch.object(run_frozen.outcomes, "sha256", lambda path: "x"), \
                mock.patch.object(run_frozen, "OUT", Path(tmp)), mock.patch("builtins.print") as printed:
            run_frozen.run(frz, "2026-10-15T00:00:00+00:00")
            summary = json.loads((Path(tmp) / "summary.json").read_text())
        self.assertEqual(seen["rq2"], (None, ("H2b", "H2c")))               # real labels in the real run: ys=None
        self.assertEqual(seen["rq3"], (True, ("H2b", "H2c")))
        self.assertEqual(summary["remedies"], ["H2b", "H2c"])
        self.assertEqual(summary["remedy_validation_dryrun_v3"], {"size_bootstrap": {"x": 1}})
        self.assertEqual(set(summary["rq2"]["stress_sensitivity"]), {"H2b", "H2c"})
        self.assertEqual(summary["rq3"]["stress_sensitivity"], {})
        for h, r in [("H2b", 1.3), ("H2c", 1.2)]:
            v = summary["rq2"]["verdicts"][h]
            from scipy import stats
            expect = 2 * stats.t.sf(abs(v["coef"] / v["se"]) / r, v["clusters"] - 1)
            self.assertAlmostEqual(summary["rq2"]["stress_sensitivity"][h]["p_stress"], expect, places=12)
        for h in dryrun.REMEDIES:
            v = summary["rq2"]["verdicts"][h]
            self.assertEqual(v["p"], boot(F["pop2"], spec(rq2.SPECS, h))["p"])
            self.assertIn("bootstrap", v["p_method"])
            self.assertEqual(v["ci_tost_method"], "CR1, t(G-1)")
        self.assertEqual(summary["rq2"]["verdicts"]["H2a"]["p_method"], "CR1, t(G-1)")
        self.assertEqual(set(summary["rq2"]["s11_twoway"]), set(summary["rq2"]["family"]))
        self.assertEqual(set(summary["rq3"]["s11_twoway"]), set(summary["rq3"]["family"]))
        for rq, specs, pop in [("rq2", rq2.SPECS, F["pop2"]), ("rq3", rq3.SPECS, F["pop3"])]:
            for s in (s for s in specs if not s.gated):
                ref = analysis.estimate_twoway(pop, s.y, s.x, s.controls, s.fe, s.years, cluster2="topic_early")
                d = analysis._design(pop, s.y, s.x, s.controls, s.fe, s.years)[0]
                got = summary[rq]["s11_twoway"][s.hid]
                self.assertEqual((got["coef"], got["se"], got["p"], got["ci95"]),
                                 (ref["coef"], ref["se"], ref["p"], [ref["ci95_lo"], ref["ci95_hi"]]), s.hid)
                self.assertEqual((got["clusters"], got["clusters2"]), (d.topic.nunique(), d.topic_early.nunique()), s.hid)
                self.assertNotEqual(got["se"], summary[rq]["verdicts"][s.hid]["se"], s.hid)
        for rq in ["rq2", "rq3"]:
            fam = summary[rq]["family"]
            ph = holm(pd.Series({h: summary[rq]["s11_twoway"][h]["p"] for h in fam}))
            for h in fam:
                v = summary[rq]["verdicts"][h]
                self.assertAlmostEqual(v["s11_p_holm"], ph[h], places=12)
                self.assertEqual(v["qualifier"] != "", v["verdict"] == "supported" and not v["s11_agrees"])
        lines = [str(c.args[0]) for c in printed.call_args_list if c.args]
        for h in summary["rq2"]["family"] + summary["rq3"]["family"]:
            line = next(x for x in lines if x.startswith(h + " "))
            v = summary["rq2" if h.startswith("H2") else "rq3"]["verdicts"][h]
            if h in dryrun.REMEDIES:
                self.assertIn(f"p_boot {format(v['p'], '.3g')} ", line)
                st = summary["rq2"]["stress_sensitivity"][h]
                self.assertTrue(line.endswith(f"[stress p_holm {format(st['p_holm_stress'], '.3g')}]"), line)
                self.assertNotEqual(format(v["p"], ".3g"), format(v["p_cr1"], ".3g"), h)
            else:
                self.assertIn(f" p {format(v['p'], '.3g')} ", line)
                self.assertNotIn("p_boot", line)
        e9 = {r["hypothesis"]: r for r in summary["e9_equivalence"]}
        for h, r in e9.items():
            self.assertEqual(r["p_method"], summary["rq2" if h.startswith("H2") else "rq3"]["verdicts"][h]["p_method"])
            self.assertEqual(r["ci_tost_method"], "CR1, t(G-1)")

    def test_s11_block_maps_each_field_of_the_s11_row(self):
        """Direct check (both real maps have 100 topics, so clusters and clusters2 coincide in the runs above)."""
        rows = pd.DataFrame([{"hypothesis": "H2a", "variant": "main", "coef": 9.0, "se": 9.0, "p": 9.0, "ci95_lo": 9.0,
                              "ci95_hi": 9.0, "clusters": 9, "clusters2": np.nan},
                             {"hypothesis": "H2a", "variant": S11, "coef": 0.1, "se": 0.2, "p": 0.3, "ci95_lo": -0.4,
                              "ci95_hi": 0.6, "ci90_lo": -0.3, "ci90_hi": 0.5, "clusters": 100, "clusters2": 57}])
        self.assertEqual(run_frozen.s11_of(rows), {"H2a": {"coef": 0.1, "se": 0.2, "p": 0.3, "ci95": [-0.4, 0.6],
                                                           "ci90": [-0.3, 0.5], "clusters": 100, "clusters2": 57}})
        self.assertEqual(run_frozen.s11_of(pd.DataFrame()), {})

    def test_s11_qualifiers(self):
        v = lambda verdict, sign=-1: {"verdict": verdict, "predicted_sign": sign, "sesoi": 0.02, "p": 0.001}
        s11 = lambda coef, p, ci90=(-0.01, 0.01): {"coef": coef, "se": 0.01, "p": p, "ci90": list(ci90)}
        Q, QE = run_frozen.S11_QUALIFIER, run_frozen.S11_EQUIVALENCE_QUALIFIER
        verdicts = {"Ha": v("supported"), "Hb": v("supported"), "Hc": v("supported", +1), "Hd": v("inconclusive")}
        cases = {"Ha": s11(-0.1, 0.01), "Hb": s11(-0.1, 0.03), "Hc": s11(-0.1, 0.001), "Hd": s11(-0.1, 0.2)}
        out = run_frozen.labelled(verdicts, cases)
        ph = {"Ha": 0.03, "Hb": 0.06, "Hc": 0.004, "Hd": 0.2}                   # Holm of (0.01, 0.03, 0.001, 0.2)
        for h in out:
            self.assertAlmostEqual(out[h]["s11_p_holm"], ph[h], places=15)
        self.assertEqual({h: out[h]["s11_agrees"] for h in out}, {"Ha": True, "Hb": False, "Hc": False, "Hd": None})
        self.assertEqual({h: out[h]["qualifier"] for h in out}, {"Ha": "", "Hb": Q, "Hc": Q, "Hd": ""})
        # opposite direction: S11 must agree with the opposite sign
        out = run_frozen.labelled({"Ha": v("significant in the opposite direction"),
                                   "Hb": v("significant in the opposite direction")},
                                  {"Ha": s11(+0.1, 0.001), "Hb": s11(-0.1, 0.001)})
        self.assertEqual([(out[h]["s11_agrees"], out[h]["qualifier"]) for h in ["Ha", "Hb"]], [(True, ""), (False, Q)])
        # equivalence: S11's 90% CI inside the bounds
        out = run_frozen.labelled({"Ha": v("equivalent to null"), "Hb": v("equivalent to null")},
                                  {"Ha": s11(0.0, 0.9, (-0.015, 0.019)), "Hb": s11(0.0, 0.9, (-0.015, 0.021))})
        self.assertEqual([(out[h]["s11_agrees"], out[h]["qualifier"]) for h in ["Ha", "Hb"]], [(True, ""), (False, QE)])
        # a missing S11 p counts as 1 in the family's Holm adjustment
        out = run_frozen.labelled({"Ha": v("supported"), "Hb": v("supported"), "Hc": v("supported")},
                                  {"Ha": s11(-0.1, 0.02), "Hb": s11(-0.1, 0.03)})
        self.assertEqual([out[h]["s11_p_holm"] for h in ["Ha", "Hb", "Hc"]], [0.06, 0.06, 1.0])
        self.assertEqual([out[h]["qualifier"] for h in ["Ha", "Hb", "Hc"]], [Q, Q, Q])
        nan = run_frozen.labelled({"Ha": v("equivalent to null")}, {"Ha": s11(np.nan, np.nan, (np.nan, np.nan))})["Ha"]
        self.assertEqual((nan["s11_agrees"], nan["qualifier"]), (False, QE))

    def test_stress_sensitivity_divides_the_cr1_t_by_the_frozen_inflation(self):
        from scipy import stats
        verdicts = {"H2a": {"coef": -0.05, "se": 0.02, "p": 0.04, "clusters": 100},
                    "H2b": {"coef": -0.03, "se": 0.01, "p": 0.001, "clusters": 100},
                    "H2c": {"coef": 0.02, "se": 0.01, "p": 0.03, "clusters": 81}}
        out = run_frozen.stressed(verdicts, {"H2b": 1.5, "H2c": 1.25})
        self.assertEqual(set(out), {"H2b", "H2c"})
        p_b, p_c = 2 * stats.t.sf(2.0, 99), 2 * stats.t.sf(1.6, 80)
        self.assertAlmostEqual(out["H2b"]["p_stress"], p_b, places=15)
        self.assertAlmostEqual(out["H2c"]["p_stress"], p_c, places=15)
        ordered = sorted([("H2a", 0.04), ("H2b", p_b), ("H2c", p_c)], key=lambda x: x[1])
        adj, running = {}, 0.0
        for i, (h, p) in enumerate(ordered):                                  # Holm by hand
            running = max(running, min(1.0, (3 - i) * p))
            adj[h] = running
        self.assertAlmostEqual(out["H2b"]["p_holm_stress"], adj["H2b"], places=15)
        self.assertAlmostEqual(out["H2c"]["p_holm_stress"], adj["H2c"], places=15)
        self.assertEqual(run_frozen.stressed(verdicts, {}), {})

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

    def test_rq3_simulated_null_replication_records_all_three_p_values(self):
        sc, params = "rq3_null_k100_lo", {"mode": "simulated", "map": "k100", "dgp": "lo"}
        rows = pd.DataFrame(dryrun.job(("rq3", sc, 0, params)))
        self.assertTrue(rows.hypothesis.str.endswith(":logit").any())
        rows = rows[~rows.hypothesis.str.contains(":")].set_index("hypothesis")
        seed = dryrun.zlib.crc32(sc.encode()) * 1000
        k = dryrun.FRAMES["k100"]
        base = dryrun.RQ3_DGP["lo"]
        y = dryrun.simulate(k, base, np.random.default_rng(seed))
        out = outcomes.load("simulated", k.submission_id, seed=seed, frame=k, dgp=base)
        out["accepted"] = np.where(out.rq3, y, np.nan)
        out["s9_accepted"] = np.where(out.rq3, y, np.where(out.s9, 0.0, np.nan))
        pop = rq3.attach(k, out)
        pop = pop[pop.rq3]
        for h, s in dryrun.RQ3_SPECS.items():
            cr1 = analysis.estimate(pop, s.y, s.x, s.controls, s.fe, s.years)["p"]
            tw = analysis.estimate_twoway(pop, s.y, s.x, s.controls, s.fe, s.years)["p"]
            self.assertEqual((rows.loc[h, "p_cr1"], rows.loc[h, "p_boot"], rows.loc[h, "p_twoway"]),
                             (cr1, boot(pop, s)["p"], tw), h)
            self.assertEqual(rows.loc[h, "p"], cr1, h)                       # no RQ3 hypothesis is remedied

    def test_mde80_of_a_remedied_hypothesis_uses_the_bootstrap_p_and_mde80_cr1_the_cr1_p(self):
        def power_rows(p, p_cr1):
            rows = []
            for mult in dryrun.MULTS:
                for rep in range(10):
                    rows.append({"scenario": f"rq2_power_H2b_m{mult}", "rep": rep, "hypothesis": "H2b", "planted": True,
                                 "realised_effect": -0.01 * mult, "coef": -0.01 * mult, "se": 0.01, "p": p, "p_cr1": p_cr1,
                                 "n": 10, "predicted_sign": -1})
            return pd.DataFrame(rows)
        s = dryrun.summarise(power_rows(0.001, 0.5))
        self.assertEqual((s["mde80"]["H2b"], s["mde80_cr1"]["H2b"]), (0.005, None))
        self.assertEqual(s["power"]["H2b"]["3.0"]["detected_alpha_over_m"], 1.0)
        s = dryrun.summarise(power_rows(0.5, 0.001))
        self.assertEqual((s["mde80"]["H2b"], s["mde80_cr1"]["H2b"]), (None, 0.005))

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
            d = pd.read_csv(tmp / "rq2_null_k100.csv")
            d.loc[(d.hypothesis == "H2a") & (d.rep == 2), "p_cr1"] = np.nan
            d.to_csv(tmp / "rq2_null_k100.csv", index=False)
            self.assertEqual(len(freeze.check_null_replications(tmp, self.FAM, 3)), 5)

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


class FreezeWritesTheRemedyRecord(unittest.TestCase):
    """freeze.main end to end on a fabricated dry-run (temporary directories; the repository's FREEZE.json is untouched)."""
    FAM = {"rq2": ["H2a", "H2b", "H2c"], "rq3": ["H3a", "H3b"]}

    def write_dryrun(self, tmp: Path) -> dict:
        (tmp / "dryrun").mkdir()
        for f in ["h2d_validation.json", "resubmission_tau.json"]:
            (tmp / f).write_text((OUTPUT / f).read_text())
        hyps = lambda sc: self.FAM["rq2"] if sc.startswith("rq2") else self.FAM["rq3"]
        per = lambda v: {sc: {h: v for h in hyps(sc)} for sc in dryrun.NULL_SCENARIOS}
        with mock.patch.object(outcomes, "sha256", lambda path: "x"):          # as inside self.freeze
            digest = dryrun.digest()["combined"]
        dry = {"code_digest": digest, "size": per(0.05), "false_support": per(0.0),
               "missing_p": per(0.0), "size_bootstrap": per(0.055), "size_twoway": per(0.06),
               "mde80": {h: 0.02 for h in sum(self.FAM.values(), [])}, "mde80_lo": {"H3a": 0.03, "H3b": 0.02},
               "mde80_cr1": {"H2b": 0.017, "H2c": 0.011}, "mde80_note": {}, "mde80_lo_note": {},
               "power": {k: {"1.0": {"full_rule": 0.5}, "3.0": {"full_rule": 0.9, "detected_alpha_over_m": 0.9}}
                         for k in ["H2a", "H2b", "H2c", "H3a_hi", "H3b_hi"]},
               "criteria": {"a_size_within_2_8pct": False, "c_detected_80pct_at_3x_sesoi": {}}}
        dry["size"]["rq2_null_early"].update(H2b=0.126, H2c=0.10)
        (tmp / "dryrun" / "summary.json").write_text(json.dumps(dry))
        prov = {**dryrun.REGISTERED, "calibrated_rq2_dgp": {}, "rq3_dgp": {}}
        (tmp / "dryrun" / "provenance.json").write_text(json.dumps(prov))
        for sc in dryrun.NULL_SCENARIOS:
            rng = np.random.default_rng(len(sc))
            rows = [{"rep": r, "hypothesis": h, "p_cr1": 0.5, "p_boot": 0.5, "p_twoway": 0.5,
                     "coef": rng.normal(0, 0.01 * (1 + (h == "H2b"))), "se": 0.01}
                    for r in range(dryrun.REGISTERED["reps"]) for h in hyps(sc)]
            pd.DataFrame(rows).to_csv(tmp / "dryrun" / f"{sc}.csv", index=False)
        return dry

    def freeze(self, tmp: Path, remedies: list[str]):
        argv = ["freeze.py", "--created", "2026-10-15T00:00:00Z"] + [x for r in remedies for x in ("--remedy", r)]
        with mock.patch.object(freeze, "OUTPUT", tmp), mock.patch.object(freeze, "HERE", tmp), \
                mock.patch.object(freeze.outcomes, "sha256", lambda path: "x"), mock.patch.object(sys, "argv", argv), \
                mock.patch("builtins.print"):
            freeze.main()
        return json.loads((tmp / "FREEZE.json").read_text())

    def test_registered_remedies_are_recorded_with_their_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            dry = self.write_dryrun(tmp)
            frz = self.freeze(tmp, ["bootstrap:H2b", "bootstrap:H2c"])
            early = pd.read_csv(tmp / "dryrun" / "rq2_null_early.csv")
        self.assertEqual(frz["remedies"], ["bootstrap:H2b", "bootstrap:H2c"])
        self.assertEqual(run_frozen.remedies_of(frz), dryrun.REMEDIES)
        self.assertEqual(frz["remedy_validation"], {"size_bootstrap": dry["size_bootstrap"], "size_twoway": dry["size_twoway"]})
        self.assertEqual(frz["mde80_cr1_for_remedied"], dry["mde80_cr1"])
        self.assertEqual(sorted(p.split(":")[0] for p in frz["dryrun_problems"]), ["H2b", "H2c"])
        expect = {h: round(float((g.coef / g.se).std(ddof=1)), 4) for h, g in early.groupby("hypothesis") if h != "H2a"}
        self.assertEqual(frz["stress_t_inflation"], expect)
        self.assertEqual(frz["stress_scenario"], "rq2_null_early")
        self.assertGreater(expect["H2b"], 1.5 * expect["H2c"])                 # H2b's simulated t is twice as spread

    def test_refuses_other_remedies_or_missing_bootstrap_p_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            self.write_dryrun(tmp)
            for remedies in [["bootstrap:H2b"], [], ["bootstrap:H2a", "bootstrap:H2b", "bootstrap:H2c"]]:
                with self.assertRaises(SystemExit):
                    self.freeze(tmp, remedies)
            f = tmp / "dryrun" / "rq2_null_early.csv"
            d = pd.read_csv(f)
            d.loc[0, "p_boot"] = np.nan
            d.to_csv(f, index=False)
            with self.assertRaises(SystemExit):
                self.freeze(tmp, ["bootstrap:H2b", "bootstrap:H2c"])
            self.assertFalse((tmp / "FREEZE.json").exists())


if __name__ == "__main__":
    unittest.main()
