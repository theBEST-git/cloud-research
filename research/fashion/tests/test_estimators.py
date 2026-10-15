"""Estimators against statsmodels (PREREGISTRATION.md D4, D8). statsmodels is not a runtime dependency; these tests
are skipped unless it can be imported (e.g. PYTHONPATH pointing at a separate install).

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logit import fe_logit  # noqa: E402
from ols import fe_ols  # noqa: E402

try:
    import statsmodels.api as sm
except ImportError:                                   # pragma: no cover
    sm = None


def clustered(seed: int, n: int = 4000, topics: int = 40, years: int = 6):
    rng = np.random.default_rng(seed)
    topic = pd.Series(rng.integers(0, topics, n), name="topic")
    year = pd.Series(rng.integers(0, years, n), name="year")
    a = rng.normal(0, 0.6, topics)[topic]
    trend = rng.normal(0, 0.15, topics)[topic] * year
    x = pd.Series(rng.normal(size=n) + 0.3 * a, name="x")
    z = pd.Series((rng.random(n) < 0.3).astype(float), name="z")
    eta = -0.8 + a + trend + 0.1 * year + 0.4 * x - 0.5 * z
    y = pd.Series((rng.random(n) < 1 / (1 + np.exp(-eta))).astype(float), name="y")
    return y, x, z, topic, year


@unittest.skipIf(sm is None, "statsmodels not importable")
class AgainstStatsmodels(unittest.TestCase):
    def test_ols_absorbed_topic_and_year_dummies(self):
        y, x, z, topic, year = clustered(0)
        X = pd.concat([x, z, pd.get_dummies(year, prefix="y", drop_first=True).astype(float)], axis=1)
        ours = fe_ols(y, X, topic, topic)
        full = pd.concat([X, pd.get_dummies(topic, prefix="t", drop_first=True).astype(float)], axis=1)
        ref = sm.OLS(y, sm.add_constant(full)).fit(cov_type="cluster", cov_kwds={"groups": topic}, use_t=True)
        np.testing.assert_allclose(ours.loc["x", "coef"], ref.params["x"], rtol=1e-9)
        # statsmodels counts the topic dummies in K; ours does not (they are nested in clusters, as in reghdfe)
        k_full, k_ours, n = full.shape[1] + 1, X.shape[1], len(y)
        np.testing.assert_allclose(ours.loc["x", "se"], ref.bse["x"] * np.sqrt((n - k_full) / (n - k_ours)), rtol=1e-8)

    def test_logit_topic_and_year_dummies(self):
        y, x, z, topic, year = clustered(1)
        X = pd.concat([x, z], axis=1)
        ours, info = fe_logit(y, X, [topic, year], topic)
        Z = pd.concat([X, pd.Series(1.0, index=X.index, name="const"),
                       pd.get_dummies(topic.astype(str), prefix="_topic", drop_first=True).astype(float),
                       pd.get_dummies(year.astype(str), prefix="_year", drop_first=True).astype(float)], axis=1)
        ref = sm.Logit(y, Z).fit(disp=0, method="newton", tol=1e-12, maxiter=200,
                                 cov_type="cluster", cov_kwds={"groups": topic}, use_t=True)
        for c in ["x", "z"]:
            np.testing.assert_allclose(ours.loc[c, "coef"], ref.params[c], rtol=1e-6)
            np.testing.assert_allclose(ours.loc[c, "se"], ref.bse[c], rtol=1e-6)
            np.testing.assert_allclose(ours.loc[c, "p"], ref.pvalues[c], rtol=1e-5)
        me = ref.get_margeff(at="overall", method="dydx")
        np.testing.assert_allclose(ours.loc["x", "ame"], me.margeff[0], rtol=1e-6)
        self.assertEqual(info["dropped_groups"], [])

    def test_logit_drops_groups_without_variation(self):
        y, x, z, topic, year = clustered(2)
        y = y.copy()
        y[topic == 3] = 0.0
        y[topic == 7] = 1.0
        _, info = fe_logit(y, pd.concat([x, z], axis=1), [topic, year], topic)
        self.assertEqual(info["dropped_groups"], ["3", "7"])


class Basic(unittest.TestCase):
    def test_ols_recovers_planted_slope(self):
        rng = np.random.default_rng(3)
        n = 20000
        g = pd.Series(rng.integers(0, 50, n))
        x = pd.Series(rng.normal(size=n), name="x")
        y = pd.Series(rng.normal(size=50)[g] + 0.25 * x + rng.normal(size=n))
        r = fe_ols(y, x.to_frame(), g, g).loc["x"]
        self.assertLess(abs(r.coef - 0.25), 4 * r.se)


if __name__ == "__main__":
    unittest.main()
