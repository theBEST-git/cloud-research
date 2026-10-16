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
