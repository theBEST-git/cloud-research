"""The decision rule with hard-coded expected values (review round B6): Holm-adjusted p-values, the four legs of
'supported' (sign, Holm p < 0.05, >= 75% same-sign variants, both hindsight variants), the other verdicts, the fragile
flag, and the dry-run's detection, false-support and full-rule counts. No expected value is computed with the code
under test.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import analysis  # noqa: E402
import dryrun  # noqa: E402
from variants import HINDSIGHT_VARIANTS, ROBUST_SHARE, holm  # noqa: E402

S11 = "S11_twoway_topic_early"


def est(coef: float, p: float, half90: float = 0.0165, half95: float = 0.0196, **extra) -> dict:
    return {"coef": coef, "se": 0.01, "p": p, "dof": 99, "n": 1000, "clusters": 100, "ci95_lo": coef - half95,
            "ci95_hi": coef + half95, "ci90_lo": coef - half90, "ci90_hi": coef + half90, **extra}


def spec(hid: str = "Hx", sign: int = -1) -> analysis.Spec:
    return analysis.Spec(hid, "y", "x", sign, 0.02, "topic+year", (2019, 2026))


def variants_with(signs: dict[str, int]) -> dict[str, dict]:
    return {v: est(0.05 * s, 0.01) for v, s in signs.items()}


class Holm(unittest.TestCase):
    def check(self, p: dict, expect: dict):
        got = holm(pd.Series(p))
        np.testing.assert_allclose([got[k] for k in p], [expect[k] for k in p], rtol=0, atol=1e-15)

    def test_step_down_values(self):
        self.check({"a": 0.01, "b": 0.02, "c": 0.03}, {"a": 0.03, "b": 0.04, "c": 0.04})
        self.check({"a": 0.04, "b": 0.011, "c": 0.02}, {"a": 0.04, "b": 0.033, "c": 0.04})

    def test_running_maximum(self):
        self.check({"a": 0.01, "b": 0.03, "c": 0.031}, {"a": 0.03, "b": 0.06, "c": 0.06})

    def test_cap_and_single(self):
        self.check({"a": 0.6, "b": 0.5, "c": 0.9}, {"a": 1.0, "b": 1.0, "c": 1.0})
        self.check({"a": 0.02}, {"a": 0.02})

    def test_registered_constants(self):
        self.assertEqual((ROBUST_SHARE, HINDSIGHT_VARIANTS, analysis.ALPHA), (0.75, ("balanced", "early_prospective"), 0.05))


class Support(unittest.TestCase):
    FOUR = ["balanced", "early_prospective", "k75", "k150"]

    def verdict(self, main: dict, signs: dict[str, int], sign: int = -1, supp: dict | None = None) -> dict:
        s = spec(sign=sign)
        return analysis.decide([s], {"Hx": main}, {"Hx": variants_with(signs)}, {"Hx": supp or {}})["Hx"]

    def test_75_percent_share_is_inclusive(self):
        v = self.verdict(est(-0.05, 0.001), {"balanced": -1, "early_prospective": -1, "k75": -1, "k150": +1})
        self.assertEqual((v["verdict"], v["robustness_same_sign"], v["robustness_variants"]), ("supported", 0.75, 4))
        v = self.verdict(est(-0.05, 0.001), {"balanced": -1, "early_prospective": -1, "k75": +1, "k150": +1})
        self.assertEqual((v["verdict"], v["robustness_same_sign"]), ("inconclusive", 0.5))
        self.assertEqual(v["variants_wrong_sign"], ["k150", "k75"])

    def test_both_hindsight_variants_must_agree_and_be_present(self):
        v = self.verdict(est(-0.05, 0.001), {"balanced": +1, "early_prospective": -1, "k75": -1, "k150": -1})
        self.assertEqual((v["verdict"], v["hindsight_variants_same_sign"], v["robustness_same_sign"]),
                         ("inconclusive", False, 0.75))
        v = self.verdict(est(-0.05, 0.001), {"balanced": -1, "k75": -1, "k150": -1})
        self.assertEqual((v["verdict"], v["hindsight_variants_same_sign"]), ("inconclusive", False))
        nan = {**variants_with({"balanced": -1, "k75": -1, "k150": -1}), "early_prospective": est(np.nan, np.nan)}
        v = analysis.decide([spec()], {"Hx": est(-0.05, 0.001)}, {"Hx": nan})["Hx"]
        self.assertEqual((v["verdict"], v["hindsight_variants_same_sign"]), ("inconclusive", False))

    def test_holm_adjusted_p_of_the_family_drives_significance(self):
        specs = [spec("Ha"), spec("Hb"), spec("Hc")]
        counted = {h: variants_with(dict.fromkeys(self.FOUR, -1)) for h in ["Ha", "Hb", "Hc"]}
        main = {"Ha": est(-0.05, 0.03, p_cr1=0.001), "Hb": est(-0.05, 0.5), "Hc": est(-0.05, 0.6)}
        v = analysis.decide(specs, main, counted)
        self.assertAlmostEqual(v["Ha"]["p_holm"], 0.09, places=15)
        self.assertEqual(v["Ha"]["verdict"], "inconclusive")                  # p 0.03, but Holm 0.09; p_cr1 is ignored
        main = {"Ha": est(-0.05, 0.01), "Hb": est(-0.05, 0.02), "Hc": est(-0.05, 1e-6, p_cr1=0.5)}
        v = analysis.decide(specs, main, counted)
        np.testing.assert_allclose([v[h]["p_holm"] for h in ["Ha", "Hb", "Hc"]], [0.02, 0.02, 3e-6], atol=1e-15)
        self.assertEqual([v[h]["verdict"] for h in ["Ha", "Hb", "Hc"]], ["supported"] * 3)
        self.assertEqual(v["Hc"]["p_cr1"], 0.5)

    def test_sign_of_the_main_estimate(self):
        v = self.verdict(est(+0.05, 0.001), dict.fromkeys(self.FOUR, -1))
        self.assertEqual(v["verdict"], "significant in the opposite direction")
        v = self.verdict(est(+0.05, 0.001), dict.fromkeys(self.FOUR, +1))
        self.assertEqual(v["verdict"], "significant in the opposite direction")
        v = self.verdict(est(+0.05, 0.001), dict.fromkeys(self.FOUR, +1), sign=+1)
        self.assertEqual(v["verdict"], "supported")
        v = self.verdict(est(+0.004, 0.6, half90=0.03, half95=0.04), dict.fromkeys(self.FOUR, -1))
        self.assertEqual(v["verdict"], "inconclusive")

    def test_equivalence_uses_the_90_percent_interval_inside_the_bounds(self):
        v = self.verdict(est(0.004, 0.6, half90=0.0155, half95=0.02), dict.fromkeys(self.FOUR, -1))
        self.assertEqual(v["verdict"], "equivalent to null")                 # ci90 (-0.0115, 0.0195), ci95 to 0.024
        v = self.verdict(est(0.004, 0.6, half90=0.0165, half95=0.02), dict.fromkeys(self.FOUR, -1))
        self.assertEqual(v["verdict"], "inconclusive")                        # ci90 upper 0.0205 is outside
        v = self.verdict(est(-0.012, 0.001, half90=0.005, half95=0.006), dict.fromkeys(self.FOUR, +1))
        self.assertEqual(v["verdict"], "equivalent to null")                  # significant, not robust, smaller than SESOI

    def test_tost_uses_t_with_the_estimate_dof(self):
        from scipy import stats
        v = self.verdict(est(0.004, 0.6), dict.fromkeys(self.FOUR, -1))
        expect = max(stats.t.sf((0.004 + 0.02) / 0.01, 99), stats.t.cdf((0.004 - 0.02) / 0.01, 99))
        self.assertAlmostEqual(v["tost_p"], expect, places=15)


class Fragile(unittest.TestCase):
    def verdict(self, main: dict, supp: dict) -> dict:
        counted = {"Hx": variants_with(dict.fromkeys(Support.FOUR, -1))}
        return analysis.decide([spec()], {"Hx": main}, counted, {"Hx": supp})["Hx"]

    def test_only_a_supported_hypothesis_can_be_fragile(self):
        v = self.verdict(est(-0.001, 0.5), {S11: est(+0.05, 0.01)})
        self.assertNotEqual(v["verdict"], "supported")
        self.assertEqual((v["fragile"], v["fragile_by"]), (False, [S11]))     # listed, but no flag without support

    def test_threshold_and_sign(self):
        v = self.verdict(est(-0.05, 0.001), {S11: est(+0.05, 0.07)})
        self.assertEqual((v["verdict"], v["fragile"], v["fragile_by"]), ("supported", False, []))
        v = self.verdict(est(-0.05, 0.001), {S11: est(+0.05, 0.05)})
        self.assertEqual((v["fragile"], v["fragile_by"]), (False, []))          # p = 0.05 is not below 0.05
        v = self.verdict(est(-0.05, 0.001), {"S4_without_own_versions": est(+0.05, 0.01), S11: est(+0.05, 0.2)})
        self.assertEqual((v["fragile"], v["fragile_by"]), (True, ["S4_without_own_versions"]))
        v = self.verdict(est(-0.05, 0.001), {"S1_log_team": est(-0.05, 0.001), S11: est(np.nan, np.nan)})
        self.assertEqual((v["fragile"], v["fragile_by"]), (False, []))


class DryRunCounts(unittest.TestCase):
    def power(self, h: str, p: float, coef: float, p_cr1: float | None = None, tag: str = "", reps: int = 10) -> list[dict]:
        rq = 2 if h.startswith("H2") else 3
        sign = dryrun.RQ2_SPECS[h].sign if rq == 2 else dryrun.RQ3_SPECS[h].sign
        return [{"scenario": f"rq{rq}_power_{h}_m{mult}{tag}", "rep": r, "hypothesis": h, "planted": True,
                 "realised_effect": coef * mult, "coef": coef * mult, "se": 0.01, "p": p,
                 "p_cr1": p if p_cr1 is None else p_cr1, "n": 10, "predicted_sign": sign}
                for mult in dryrun.MULTS for r in range(reps)]

    def test_detection_needs_p_below_alpha_over_family_size_and_the_predicted_sign(self):
        s = dryrun.summarise(pd.DataFrame(self.power("H2a", 0.03, -0.01)))     # 0.03 > 0.05/3
        t = s["power"]["H2a"]["3.0"]
        self.assertEqual((t["detected_alpha_over_m"], t["main_p05_right_sign"], s["mde80"]["H2a"]), (0.0, 1.0, None))
        s = dryrun.summarise(pd.DataFrame(self.power("H2a", 0.0166, -0.01)))   # just below 0.05/3
        self.assertEqual(s["power"]["H2a"]["3.0"]["detected_alpha_over_m"], 1.0)
        s = dryrun.summarise(pd.DataFrame(self.power("H2a", 0.001, +0.01)))    # wrong sign
        self.assertEqual((s["power"]["H2a"]["3.0"]["detected_alpha_over_m"], s["mde80"]["H2a"]), (0.0, None))
        s = dryrun.summarise(pd.DataFrame(self.power("H3a", 0.02, -0.01, tag="_hi")))   # 0.02 < 0.05/2 (RQ3: m = 2)
        self.assertEqual(s["power"]["H3a_hi"]["3.0"]["detected_alpha_over_m"], 1.0)
        s = dryrun.summarise(pd.DataFrame(self.power("H2b", 0.001, -0.01, p_cr1=0.03)))
        self.assertEqual((s["mde80"]["H2b"], s["mde80_cr1"]["H2b"]), (0.005, None))     # CR1 branch: same threshold

    def test_false_support_and_full_rule_count_only_supported(self):
        verdicts = ["supported", "inconclusive", "equivalent to null", "significant in the opposite direction",
                    "inconclusive"] * 2
        null = [{"scenario": "rq2_null_k100", "rep": r, "hypothesis": h, "planted": False, "coef": -0.01, "se": 0.01,
                 "p": 0.5, "p_cr1": 0.5, "p_boot": 0.5, "p_twoway": 0.5, "p_holm": 0.5, "n": 10,
                 "predicted_sign": -1 if h != "H2c" else 1, "verdict": verdicts[r]}
                for r in range(10) for h in ["H2a", "H2b", "H2c"]]
        full = [{**x, "scenario": "rq2_fullrule_H2a_m1.0", "planted": x["hypothesis"] == "H2a", "verdict": v}
                for x, v in zip(self.power("H2a", 0.001, -0.01, reps=1)[:1] * 8,
                                ["supported"] * 3 + ["inconclusive"] * 4 + ["equivalent to null"])]
        for i, x in enumerate(full):
            x["rep"] = i
        s = dryrun.summarise(pd.DataFrame(null + self.power("H2a", 0.001, -0.01) + full))
        self.assertEqual(s["false_support"]["rq2_null_k100"], {"H2a": 0.2, "H2b": 0.2, "H2c": 0.2})
        self.assertFalse(s["criteria"]["b_false_support_at_most_5pct"])
        t = s["power"]["H2a"]["1.0"]
        self.assertEqual((t["full_rule"], t["full_rule_reps"]), (0.375, 8))


if __name__ == "__main__":
    unittest.main()
