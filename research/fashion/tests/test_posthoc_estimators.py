"""The post hoc weighted multi-way fixed-effects estimator (posthoc.wls_fe) against explicit dummies and ols.fe_ols.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import posthoc  # noqa: E402
from ols import fe_ols  # noqa: E402


def frame(seed=0, n=1500):
    rng = np.random.default_rng(seed)
    d = pd.DataFrame({"cell": rng.integers(0, 40, n), "key": rng.integers(0, 120, n), "topic": rng.integers(0, 25, n),
                      "submission_id": np.arange(n), "w": rng.uniform(0.2, 1.0, n)})
    a, c = rng.normal(0, 1, 120)[d.key], rng.normal(0, 1, 40)[d.cell]
    d["x"] = rng.normal(size=n) + 0.5 * a
    d["z"] = rng.normal(size=n) - 0.3 * c
    d["y"] = 0.4 * d.x - 0.2 * d.z + a + c + rng.normal(size=n)
    return d


class WeightedTwoWayFE(unittest.TestCase):
    def test_coefficients_match_weighted_dummy_regression(self):
        d = frame()
        r = posthoc.wls_fe(d, "y", ["x", "z"], ["cell", "key"], "w", "topic")
        D = pd.concat([d[["x", "z"]], pd.get_dummies(d.cell, prefix="c").astype(float),
                       pd.get_dummies(d.key, prefix="k", drop_first=True).astype(float)], axis=1).to_numpy()
        sw = np.sqrt(d.w.to_numpy())
        beta = np.linalg.lstsq(D * sw[:, None], d.y.to_numpy() * sw, rcond=None)[0]
        np.testing.assert_allclose(r.loc[["x", "z"], "coef"], beta[:2], rtol=1e-7)

    def test_one_fixed_effect_unit_weights_equals_fe_ols(self):
        d = frame(1).assign(w=1.0)
        r = posthoc.wls_fe(d, "y", ["x", "z"], ["cell"], "w", "topic")
        ref = fe_ols(d.y, d[["x", "z"]], d.cell, d.topic)
        np.testing.assert_allclose(r.loc[["x", "z"], "coef"], ref.loc[["x", "z"], "coef"], rtol=1e-9)
        np.testing.assert_allclose(r.loc[["x", "z"], "se"], ref.loc[["x", "z"], "se"], rtol=1e-9)

    def test_singletons_are_dropped(self):
        d = frame(2)
        d.loc[0, "key"] = 10_000                                            # an author with one row
        r = posthoc.wls_fe(d, "y", ["x"], ["cell", "key"], "w", "topic")
        self.assertEqual(int(r.loc["x", "rows"]), len(d) - 1)


if __name__ == "__main__":
    unittest.main()


class PH4Estimators(unittest.TestCase):
    """PH4 gap, level, trend and BH computations against direct calculations."""

    def test_bh_matches_hand_computation(self):
        p = pd.Series([0.01, 0.04, 0.03, 0.2, np.nan], index=list("abcde"))
        q = posthoc.bh(p)
        np.testing.assert_allclose(q[["a", "b", "c", "d"]].to_numpy(), [0.04, 0.04 * 4 / 3, 0.04 * 4 / 3, 0.2])
        self.assertTrue(np.isnan(q["e"]))

    def test_cell_counts_match_groupby(self):
        rng = np.random.default_rng(1)
        n, U, T = 3000, 5, 6
        member = rng.random((n, U)) < 0.2
        yi = rng.integers(0, T, n)
        acc = (rng.random(n) < 0.4).astype(float)
        n_in, k_in, n_all, k_all = posthoc.cell_counts(member, yi, acc, T)
        for u in range(U):
            for t in range(T):
                sel = member[:, u] & (yi == t)
                self.assertEqual(n_in[u, t], sel.sum())
                self.assertAlmostEqual(k_in[u, t], acc[sel].sum())
        np.testing.assert_allclose(n_all, np.bincount(yi, minlength=T))

    def test_level_is_paper_weighted_mean_and_trend_is_exact_for_linear_gaps(self):
        years = np.arange(2018, 2027)
        n1 = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100], float)
        g = 0.10 - 0.02 * (years - 2022)                         # exactly linear: -2 pp per year
        var = 0.24 / n1
        res = posthoc.summarise_gaps(g, var, n1, years)
        self.assertAlmostEqual(res["level"], float(np.sum(n1 * g) / n1.sum()))
        self.assertAlmostEqual(res["trend"], -0.02)
        X = np.column_stack([np.ones(9), years - 2022])
        se = np.sqrt(np.linalg.inv(X.T @ (X / var[:, None]))[1, 1])  # no overdispersion: RSS = 0, factor 1
        self.assertAlmostEqual(res["trend_se"], se)
        self.assertEqual(res["years_with_min_cell"], 9)

    def test_trend_needs_four_years_and_counts_reproduce_gaps(self):
        years = np.arange(2018, 2027)
        n1 = np.array([0, 0, 0, 0, 0, 0, 12, 15, 20])
        k1 = np.array([0, 0, 0, 0, 0, 0, 6, 6, 8])
        n0 = np.full(9, 1000)
        k0 = np.full(9, 400)
        res = posthoc.gap_summary(n1, k1, n0, k0, years)
        self.assertTrue(np.isnan(res["trend"]))                  # only 3 years with >= 10 papers
        expect = (6 / 12 - 0.4) * 12 + (6 / 15 - 0.4) * 15 + (8 / 20 - 0.4) * 20
        self.assertAlmostEqual(res["level"], expect / 47)

    def test_selection_rule(self):
        res = pd.DataFrame({"unit": list("abcdefghij") + ["federated learning"],
                            "trend": [-.05, -.04, -.03, -.02, -.01, .01, .02, .03, .04, .05, -.001],
                            "trend_q": [.01] * 10 + [.5]})
        self.assertEqual(posthoc.ph4_selected(res), ["a", "b", "c", "d", "j", "i", "h", "g", "federated learning"])
