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


class Remedies(unittest.TestCase):
    def frame(self, seed=0, n=4000, topics=40, beta=0.0):
        rng = np.random.default_rng(seed)
        d = pd.DataFrame({"topic": rng.integers(0, topics, n).astype(str), "year": rng.integers(2019, 2027, n),
                          "topic_early": rng.integers(0, 30, n).astype(str)})
        d["cell"] = d.topic + ":" + d.year.astype(str)
        d["x"] = (rng.random(n) < 0.4).astype(float)
        d["c1"] = rng.normal(size=n)
        a = rng.normal(0, 0.3, topics)[d.topic.astype(int)]
        d["y"] = (rng.random(n) < 1 / (1 + np.exp(-(-0.5 + a + 0.2 * d.c1 + beta * d.x)))).astype(float)
        return d

    def test_wild_bootstrap_matches_brute_force(self):
        import analysis
        d = self.frame()
        for fe, ctr in [("cell", ()), ("topic+year", ("c1",))]:
            W = np.random.default_rng(1).choice([-1.0, 1.0], size=(30, 40))
            b = analysis.wild_cluster_bootstrap_p(d, "y", "x", ctr, fe, (2019, 2026), weights=W)
            d2, X, absorb, _ = analysis._design(d, "y", "x", ctr, fe, (2019, 2026))
            Xd, yd, _, _, _ = analysis._partial(d2, "y", X, absorb)
            C = Xd[:, 1:]
            yhat = C @ np.linalg.lstsq(C, yd, rcond=None)[0] if C.shape[1] else np.zeros(len(yd))
            cl = pd.factorize(d2.topic)[0]
            brute = [fe_ols(pd.Series(yhat + (yd - yhat) * w[cl]), X.reset_index(drop=True),
                            pd.Series(pd.factorize(absorb)[0]), pd.Series(cl)).iloc[0].t for w in W]
            np.testing.assert_allclose(b["t_star"], brute, atol=1e-10)
            e = analysis.estimate(d, "y", "x", ctr, fe, (2019, 2026))
            self.assertAlmostEqual(b["t"], e["coef"] / e["se"], places=10)

    def test_wild_bootstrap_p_is_the_two_sided_share_of_bootstrap_t_beyond_the_observed_t(self):
        """The aggregation itself (review B5): p = share of |t*| >= |t|, with t from the CR1 estimate. t* is pinned by
        the brute-force test above; cases with negative, positive and very large |t| catch a signed, one-sided or
        complementary p."""
        import analysis
        for beta, seed, lo, hi in [(0.0, 4, 0.3, 0.7), (0.0, 1, 0.1, 0.3), (-0.6, 3, 0.0, 0.0)]:
            d = self.frame(seed, beta=beta)
            for fe, ctr in [("cell", ()), ("topic+year", ("c1",))]:
                W = np.random.default_rng(1).choice([-1.0, 1.0], size=(99, 40))
                b = analysis.wild_cluster_bootstrap_p(d, "y", "x", ctr, fe, (2019, 2026), weights=W)
                e = analysis.estimate(d, "y", "x", ctr, fe, (2019, 2026))
                t = e["coef"] / e["se"]
                self.assertEqual(b["p"], float(np.mean(np.abs(b["t_star"]) >= abs(t))), (seed, fe))
                self.assertTrue(lo <= b["p"] <= hi, (seed, fe, b["p"]))
                if beta:
                    self.assertLess(t, -5)                                   # p = 0: no draw reaches |t|

    def test_default_weights_are_seeded_rademacher_by_topic(self):
        """Without explicit weights, the bootstrap draws a (draws x topics) Rademacher matrix from default_rng(seed),
        columns in order of first appearance of the topic (as pd.factorize), and the registered defaults are 9,999
        draws with seed 20261015."""
        import analysis
        d = self.frame(4)
        G = d.topic.nunique()
        for fe, ctr in [("cell", ()), ("topic+year", ("c1",))]:
            for draws, seed in [(99, 5), (analysis.BOOT_DRAWS, analysis.BOOT_SEED)]:
                W = np.random.default_rng(seed).choice([-1.0, 1.0], size=(draws, G))
                b = analysis.wild_cluster_bootstrap_p(d, "y", "x", ctr, fe, (2019, 2026), draws=draws, seed=seed)
                ref = analysis.wild_cluster_bootstrap_p(d, "y", "x", ctr, fe, (2019, 2026), weights=W)
                self.assertEqual((b["p"], b["t"], b["draws"]), (ref["p"], ref["t"], draws), (fe, draws))
            default = analysis.wild_cluster_bootstrap_p(d, "y", "x", ctr, fe, (2019, 2026))
            self.assertEqual((default["p"], default["draws"]), (b["p"], 9999))
            other = analysis.wild_cluster_bootstrap_p(d, "y", "x", ctr, fe, (2019, 2026), draws=999, seed=6)
            first = analysis.wild_cluster_bootstrap_p(d, "y", "x", ctr, fe, (2019, 2026), draws=999, seed=5)
            self.assertNotEqual(other["p"], first["p"])
            for bad in [np.random.default_rng(5).choice([0.0, 1.0], size=(999, G)), np.random.default_rng(5).normal(size=(999, G))]:
                self.assertNotEqual(analysis.wild_cluster_bootstrap_p(d, "y", "x", ctr, fe, (2019, 2026), weights=bad)["p"],
                                    first["p"])

    @unittest.skipIf(sm is None, "statsmodels not importable")
    def test_twoway_matches_statsmodels(self):
        import analysis
        d = self.frame(2)
        tw = analysis.estimate_twoway(d, "y", "x", ("c1",), "topic+year", (2019, 2026))
        X = pd.concat([d[["x", "c1"]], pd.get_dummies(d.year, prefix="y", drop_first=True).astype(float),
                       pd.get_dummies(d.topic, prefix="t", drop_first=True).astype(float)], axis=1)
        X = sm.add_constant(X)
        groups = np.column_stack([pd.factorize(d.topic)[0], pd.factorize(d.topic_early)[0]])
        ref = sm.OLS(d.y, X).fit(cov_type="cluster", cov_kwds={"groups": groups})
        n, k_ours = len(d), 2 + 7                                  # absorbed topic FE are not counted, as one-way
        np.testing.assert_allclose(tw["coef"], ref.params["x"], rtol=1e-9)
        np.testing.assert_allclose(tw["se"], ref.bse["x"] * np.sqrt((n - X.shape[1]) / (n - k_ours)), rtol=1e-8)


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
