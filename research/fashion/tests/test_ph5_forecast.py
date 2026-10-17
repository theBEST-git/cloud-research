"""PH5 forecast: growth / EB / hot-flag construction, persistence statistics, Kaplan-Meier, AUC, Wilson, feature and
model checks on small synthetic data against direct computation, and an end-to-end run of compute, plot and calibrate
on a simulated frame (the module reads no outcome; compute drops the simulated outcome columns).

    python -m unittest research/fashion/tests/test_ph5_forecast.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd
from scipy.special import expit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import ph5_common  # noqa: E402
import ph5_forecast as F  # noqa: E402

YEARS = F.YEARS


def counts_frame(rows: dict[str, list[int]]) -> pd.DataFrame:
    return pd.DataFrame(rows, index=YEARS).T


class GrowthPanel(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(1)
        self.counts = pd.DataFrame(rng.poisson(rng.uniform(2, 40, (12, 1)), (12, len(YEARS))),
                                   index=[f"u{i}" for i in range(12)], columns=YEARS)
        self.counts.loc["tiny"] = 0                                   # never eligible: dropped
        self.denom = pd.Series(np.linspace(300, 3000, len(YEARS)), index=YEARS)
        self.d = F.unit_years(self.counts, self.denom)

    def test_growth_variance_eligibility(self):
        d = self.d.set_index(["unit", "year"])
        self.assertNotIn("tiny", d.index.get_level_values(0))
        c, P = self.counts.loc["u3"], self.denom
        for t in (2019, 2023):
            g = np.log((c[t] + .5) / P[t]) - np.log((c[t - 1] + .5) / P[t - 1])
            self.assertAlmostEqual(d.loc[("u3", t), "g"], g)
            self.assertAlmostEqual(d.loc[("u3", t), "v"], 1 / (c[t] + .5) + 1 / (c[t - 1] + .5))
            self.assertEqual(d.loc[("u3", t), "eligible"], c[c.index < t].sum() >= 10)
            self.assertAlmostEqual(d.loc[("u3", t), "share"], c[t] / P[t])

    def test_eb_and_hot_flags(self):
        for t, e in self.d[self.d.eligible].groupby("year"):
            m = e.g.mean()
            tau2 = max(e.g.var(ddof=1) - e.v.mean(), 0) if len(e) > 1 else 0.0
            np.testing.assert_allclose(e.g_eb, m + tau2 / (tau2 + e.v) * (e.g - m))
            np.testing.assert_array_equal(e.hot_raw, e.g.round(10) >= np.percentile(e.g.round(10), 80))
            if tau2 > 0:
                np.testing.assert_array_equal(e.hot_eb, e.g_eb >= np.percentile(e.g_eb, 80))
            rank = e.g.round(10).rank()
            np.testing.assert_array_equal(e.terc_raw, np.ceil(3 * rank / len(e)).clip(1, 3))
        self.assertFalse(self.d[~self.d.eligible].hot_raw.any())

    def test_pairs_and_persistence_statistics(self):
        q = F.pairs(self.d, "raw", 1)
        d = self.d.set_index(["unit", "year"])
        for _, r in q.sample(10, random_state=0).iterrows():
            self.assertEqual(r.hot1, float(d.loc[(r.unit, r.year + 1), "hot_raw"]))
            self.assertEqual(r.up, float(d.loc[(r.unit, r.year + 1), "share"] > d.loc[(r.unit, r.year), "share"]))
        self.assertTrue(q.year.between(*F.ORIGINS[1]).all())
        est = F.a1_stats(F.a1_sums(q).sum().to_numpy())
        hot = q.hot0 == 1
        self.assertAlmostEqual(est["p_hot_given_hot"], q.hot1[hot].mean())
        self.assertAlmostEqual(est["p_hot_given_not"], q.hot1[~hot].mean())
        self.assertAlmostEqual(est["lift"], q.hot1[hot].mean() - q.hot1.mean())
        self.assertAlmostEqual(est["p_down_given_hot"], q.down[hot].mean())
        units = pd.Index(self.d.unit.unique())
        out, bt = F.boot_summary(F.a1_sums(q), units, np.ones((5, len(units))), F.a1_stats)
        np.testing.assert_allclose(bt["lift"], est["lift"])          # weight 1 on every unit: the estimate itself
        self.assertAlmostEqual(out["lift_lo"], est["lift"])
        with mock.patch.object(F, "N_BOOT", 3):
            W = F.unit_weights(len(units), np.random.default_rng(0))
        np.testing.assert_array_equal(W.sum(axis=1), len(units))
        _, bt = F.boot_summary(F.a1_sums(q), units, W, F.a1_stats)
        for w, b in zip(W, bt["lift"]):                                # all pairs of a drawn unit move together
            qq = pd.concat([q[q.unit == u] for u, k in zip(units, w) for _ in range(int(k))])
            self.assertAlmostEqual(b, qq.hot1[qq.hot0 == 1].mean() - qq.hot1.mean())

    def test_eb_flags_at_zero_signal_variance(self):
        i, t = np.indices((12, len(YEARS)))
        counts = pd.DataFrame(20 + (i * t) % 3 + 10 * (i < 3), columns=YEARS)    # dispersion far below Poisson noise
        e = F.unit_years(counts, self.denom)
        e = e[e.eligible]
        self.assertTrue((e.tau2 == 0).all())
        self.assertGreater(e.groupby("year").hot_eb.mean().max(), 0)
        np.testing.assert_allclose(e.g_eb, e.g.groupby(e.year).transform("mean"))
        for _, g in e.groupby("year"):
            score = ((g.g - g.g.mean()) / g.v).round(10)
            np.testing.assert_array_equal(g.hot_eb, score >= np.percentile(score, 80))

    def test_transitions_direct(self):
        with mock.patch.object(F, "N_BOOT", 5):
            tr = F.transitions({"keyword": self.d})
        q = F.pairs(self.d, "raw", 1)
        got = tr[(tr.growth == "raw") & (tr.h == 1) & (tr.band == "all")].set_index(["origin", "destination"]).p
        for origin, sub in (("falling", q[q.state0 == 1]), ("rising", q[q.state0 == 3]), ("entry", q[q.entry])):
            for j, dest in enumerate(F.STATES):
                self.assertAlmostEqual(got[(origin, dest)], (sub.state1 == j).mean())
        exit_ = q.state1 == 0
        d = self.d.set_index(["unit", "year"])
        np.testing.assert_array_equal(exit_, [d.loc[(u, y + 1), "c"] < 3 for u, y in zip(q.unit, q.year)])

    def test_boot_p(self):
        self.assertAlmostEqual(F.boot_p(np.full(99, 0.3)), 2 / 100)
        self.assertEqual(F.boot_p(np.r_[-np.ones(50), np.ones(49)]), 1.0)

    def test_spells_and_kaplan_meier(self):
        d = pd.DataFrame({"unit": np.repeat(["a", "b"], len(YEARS)), "year": np.tile(YEARS, 2),
                          "eligible": True, "band": "50+"})
        d["hot_raw"] = np.r_[[0, 1, 1, 0, 1, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]].astype(bool)
        sp = F.hot_spells(d, "raw")
        self.assertEqual(sp.length.tolist(), [2, 1, 3, 1, 1])
        self.assertEqual(sp.censored.tolist(), [False, False, True, False, True])
        km = F.kaplan_meier(np.array([1, 1, 2, 3, 2]), np.array([False, False, False, False, True]))
        # d=1: at risk 4 uncensored + 1 censored (length 2 lasted beyond 1 year); 2 end -> 3/5
        # d=2: at risk 2 uncensored (the censored spell is not known to outlast 2); 1 ends -> 3/5 * 1/2
        np.testing.assert_allclose(km.S, [0.6, 0.3, 0.0])
        self.assertEqual(km.at_risk.tolist(), [5, 2, 1])


class Screening(unittest.TestCase):
    def test_auc_and_average_precision(self):
        rng = np.random.default_rng(2)
        x, y = rng.integers(0, 5, 120).astype(float), rng.integers(0, 2, 120)

        def direct(i):
            pos, neg = [a for a in i if y[a]], [a for a in i if not y[a]]
            return np.mean([(x[a] > x[b]) + 0.5 * (x[a] == x[b]) for a in pos for b in neg])

        self.assertAlmostEqual(F.auc(x, y), direct(range(120)))
        idx = rng.integers(0, 120, (3, 120))
        np.testing.assert_allclose(F.auc_draws(x, y, idx), [direct(i) for i in idx])
        g = rng.integers(0, 3, 120)
        pairs = [(i, j) for i in range(120) for j in range(120) if y[i] == 1 and y[j] == 0 and g[i] == g[j]]
        strat = np.mean([(x[i] > x[j]) + 0.5 * (x[i] == x[j]) for i, j in pairs])
        self.assertAlmostEqual(F.stratified_auc(x, y, g), strat)
        # precision 1, 1/2, 2/3, 1/2 at recall 1/2, 1/2, 1, 1: AP = 1/2 * 1 + 1/2 * 2/3
        self.assertAlmostEqual(F.average_precision(np.array([1, 0, 1, 0]), np.array([.9, .8, .7, .1])), 5 / 6)
        tp, fp, _ = F.roc_points(np.array([1, 0, 1, 0]), np.array([.9, .5, .5, .1]))   # tied scores form one step
        np.testing.assert_array_equal(tp, [1, 2, 2])
        np.testing.assert_array_equal(fp, [0, 1, 2])

    def test_wilson_and_tercile(self):
        lo, hi = F.wilson(5, 10)
        self.assertAlmostEqual(lo, 0.2366, places=4)
        self.assertAlmostEqual(hi, 0.7634, places=4)
        np.testing.assert_array_equal(F.tercile(np.array([0, 0, 0, 0, 1, 2])), [2, 2, 2, 2, 3, 3])

    def test_components(self):
        lab = F.components([["a"], ["a", "b"], ["c"], None, ["b"], ["d", "c"]])
        self.assertEqual(len(np.unique(lab)), 3)
        self.assertEqual(lab[0], lab[1])
        self.assertEqual(lab[1], lab[4])
        self.assertEqual(lab[2], lab[5])
        self.assertNotEqual(lab[3], lab[0])

    def test_risk_set_targets(self):
        z = [0] * len(YEARS)
        counts = counts_frame({"new": [0, 0, 1, 2, 6, 9, 14, 3, 0, 0],      # first >= 5 in 2021, users_2023 = 14
                               "old": [5, 6, 7, 8, 9, 9, 9, 9, 9, 9],      # born 2017: outside the cohorts
                               "late": [0] * 8 + [5, 9], "never": z})
        denom = pd.Series(1000.0, index=YEARS)
        r = F.risk_set(counts, denom).set_index("keyword")
        self.assertEqual(r.index.tolist(), ["new"])
        x = r.loc["new"]
        self.assertEqual((x.cohort, x.users, x.users_prev, x.users_h), (2021, 6, 2, 14))
        self.assertEqual(x.boom, 1)                                    # 14 >= 2 * 6 and >= 10
        self.assertAlmostEqual(x.F2, np.log(6.5) - np.log(2.5))
        self.assertAlmostEqual(x.target, 0.0)                          # demeaned within a one-keyword cohort
        r3 = F.risk_set(counts, denom, entry=3, horizon=3).set_index("keyword")
        self.assertEqual(r3.index.tolist(), ["new"])                   # "late" is born after the last horizon-3 cohort
        self.assertEqual((r3.loc["new"].cohort, r3.loc["new"].users_h, r3.loc["new"].boom), (2021, 3, 0))

    def test_birth_features(self):
        rng = np.random.default_rng(3)
        x = rng.normal(1.0, 1.0, size=(8, 5))
        mu = {2023: x.mean(axis=0) + 0.3, 2022: np.zeros(5)}           # the cohort year's mean is the one used
        pin = {"keys": [["a"], ["a"], ["b"], None, ["c"], ["a"], ["q"], ["c"]],
               "year": np.array([2023, 2023, 2023, 2023, 2022, 2021, 2023, 2023]),
               "coarse": np.array(["c01", "c01", "c02", "c03", "c01", "c01", "c01", "c01"]),
               "title": np.array(["new kw here", "x", "a new kw", "y", "z", "w", "u", "v"]), "x": x, "mu": mu}
        k = pd.DataFrame({"fm": [1, 0, 0, 1, 0, 0, 0, 0], "measurement": [0, 0, 1, 0, 0, 0, 0, 0]})
        uses = pd.DataFrame({"paper": [0, 1, 2, 3, 6], "keyword": "new kw", "year": 2023})
        r = F.birth_features(pd.DataFrame({"keyword": ["new kw"], "cohort": [2023]}), uses, pin, k).iloc[0]
        self.assertEqual(r.n_groups, 4)                                # {0, 1} linked by key a; 2; 3; 6
        self.assertAlmostEqual(r.F3, 4 / 5)
        self.assertAlmostEqual(r.F4, 2 / 5)
        self.assertAlmostEqual(r.F5, 2 / 5)                            # key a submitted in 2021 (t - 2); c in 2022 has no user
        p = np.array([3, 1, 1]) / 5
        self.assertAlmostEqual(r.F6, -(p * np.log(p)).sum())
        u = x[[0, 1, 2, 3, 6]] - mu[2023]
        cos = [u[i] @ u[j] / np.linalg.norm(u[i]) / np.linalg.norm(u[j]) for i in range(5) for j in range(5) if i != j]
        self.assertAlmostEqual(r.F7, np.mean(cos))
        self.assertAlmostEqual(r.F8, 2 / 5)
        self.assertAlmostEqual(r.F9, 1 / 5)
        self.assertAlmostEqual(r.F10, 2 / 5)


class Models(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(4)
        self.X = rng.normal(size=(300, 3))
        self.y = (rng.random(300) < expit(-1 + self.X @ [1.0, -0.5, 0.0])).astype(float)

    def test_logit_first_order_conditions(self):
        for lam in (0.0, 0.3):
            b = F.fit_logit(self.X, self.y, lam)
            Xa = np.column_stack([np.ones(300), self.X])
            grad = Xa.T @ (expit(Xa @ b) - self.y) / 300 + np.r_[0.0, lam * b[1:]]
            np.testing.assert_allclose(grad, 0, atol=1e-8)

    def test_ridge_normal_equations(self):
        y = self.X @ [0.5, 1.0, -2.0] + np.random.default_rng(5).normal(size=300)
        for lam in (0.0, 0.7):
            b = F.fit_ridge(self.X, y, lam)
            Xc, yc = self.X - self.X.mean(0), y - y.mean()
            slopes = np.linalg.solve(Xc.T @ Xc / 300 + lam * np.eye(3), Xc.T @ yc / 300)
            np.testing.assert_allclose(b[1:], slopes, atol=1e-10)
            self.assertAlmostEqual(b[0], y.mean() - self.X.mean(0) @ slopes)

    def test_rolling_origin_uses_only_past_periods(self):
        rng = np.random.default_rng(6)
        d = pd.DataFrame({"t": np.repeat(np.arange(2019, 2025), 40), "x": rng.normal(size=240)})
        d["y"] = np.where(d.t <= 2022, 2 * d.groupby("t").x.transform(lambda s: (s - s.mean()) / s.std(ddof=0)), 99.0)
        pred, lams = F.oot_predict(d, "t", ["x"], "y", "linear", False, 2, [2021, 2022, 2023, 2024])
        z = d.groupby("t").x.transform(lambda s: (s - s.mean()) / s.std(ddof=0))
        test = d.t >= 2021
        np.testing.assert_allclose(pred[test], 2 * z[test], atol=1e-8)   # the 99s of 2023-24 never enter training
        self.assertTrue(pred[~test].isna().all())
        self.assertEqual(set(lams), {2021, 2022, 2023, 2024})

    def test_choose_lambda_prefers_shrinkage_for_noise(self):
        rng = np.random.default_rng(7)
        X, y = rng.normal(size=(60, 8)), rng.normal(size=60)
        self.assertGreater(F.choose_lambda(X, y, np.repeat([0, 1, 2], 20), "linear", 0), 0)

    def test_forecast_metrics_and_no_label_leakage(self):
        rng = np.random.default_rng(8)
        r = pd.DataFrame({"keyword": [f"k{i}" for i in range(600)], "cohort": np.repeat(np.arange(2019, 2025), 100)})
        for f in F.FEATURES:
            r[f] = rng.normal(size=600)
        r["users"] = rng.integers(5, 30, 600)
        r["boom"] = (rng.random(600) < expit(-2 + r.F8)).astype(int)
        r["target"] = r.F8 + rng.normal(size=600)
        with mock.patch.object(F, "N_BOOT", 19):
            m, te = F.forecast(r)
            later = r.assign(boom=np.where(r.cohort >= 2023, 1 - r.boom, r.boom),
                             target=np.where(r.cohort >= 2023, -r.target, r.target))
            _, te2 = F.forecast(later)                                # labels of 2023-24 never train any model
        cols = ["p_base", "p_full", "y_base", "y_full"]
        np.testing.assert_allclose(te[cols], te2[cols])
        m = m.set_index(["metric", "model"]).estimate
        self.assertAlmostEqual(m[("AUC", "full L2 logit")], F.auc(te.p_full, te.boom))
        self.assertAlmostEqual(m[("Brier", "baseline logit (F1+F2)")], np.mean((te.p_base - te.boom) ** 2))
        sse, sst = ((te.target - te.y_full) ** 2).sum(), ((te.target - te.target.mean()) ** 2).sum()
        self.assertAlmostEqual(m[("R2", "full OLS")], 1 - sse / sst)
        self.assertGreater(m[("AUC", "full L2 logit")], 0.6)               # the planted F8 signal is recovered

    def test_topic_rows_and_conditional(self):
        n = {"a": [5, 8, 12, 15, 20, 10, 9, 30, 40, 50], "b": [20] * 10, "c": [1, 2, 3, 4, 5, 12, 14, 16, 18, 20]}
        f = pd.DataFrame([(t, y) for t, c in n.items() for y, m in zip(YEARS, c) for _ in range(m)], columns=["topic", "year"])
        rng = np.random.default_rng(9)
        for c in ("fm", "newcomer", "measurement", "model", "log_team"):
            f[c] = rng.random(len(f))
        d = F.topic_rows(f).set_index(["topic", "year"])
        N = pd.Series(np.sum(list(n.values()), axis=0), index=YEARS)
        ls = {t: np.log((np.array(c) + .5) / N.to_numpy()) for t, c in n.items()}
        self.assertEqual(set(d.index), {(t, y) for t, c in n.items() for y, m in zip(YEARS, c)
                                        if m >= 10 and 2019 <= y <= 2024})
        raw = {(t, y): ls[t][y - 2017 + 2] - ls[t][y - 2017] for t, y in d.index}
        mean = pd.Series(raw).groupby(level=1).transform("mean")
        for key in d.index:
            t, y = key
            self.assertAlmostEqual(d.loc[key, "target"], raw[key] - mean[key])
            self.assertAlmostEqual(d.loc[key, "past_growth"], ls[t][y - 2017] - ls[t][y - 2018])
            self.assertAlmostEqual(d.loc[key, "fm"], f[(f.topic == t) & (f.year == y)].fm.mean())
        self.assertEqual(d.loc[("a", 2019), "age"], 0)                  # first year with >= 10 papers
        self.assertEqual(d.loc[("a", 2024), "age"], 5)
        self.assertEqual(d.loc[("c", 2022), "age"], 0)
        panel_rows = F.unit_years(pd.DataFrame(n, index=YEARS).T, N)
        cond = F.topic_conditional(d.reset_index(), panel_rows)
        rows = d.reset_index().merge(panel_rows[panel_rows.eligible][["unit", "year", "hot_raw"]],
                                     left_on=["topic", "year"], right_on=["unit", "year"])
        rows["top"] = rows.target >= rows.groupby("year").target.transform(lambda s: np.percentile(s, 80))
        hot = cond[(cond.hot == "hot") & (cond["size"] == "all") & (cond.age == "all")].iloc[0]
        self.assertEqual(hot.topic_years, rows.hot_raw.sum())
        self.assertAlmostEqual(hot.p, rows[rows.hot_raw].top.mean())

    def test_topic_forecast_no_label_leakage(self):
        rng = np.random.default_rng(10)
        d = pd.DataFrame({"topic": np.tile([f"t{i}" for i in range(30)], 6), "year": np.repeat(np.arange(2019, 2025), 30)})
        for c in F.TOPIC_FEATURES:
            d[c] = rng.normal(size=len(d))
        d["target"] = 0.5 * d.past_growth + rng.normal(size=len(d))
        with mock.patch.object(F, "N_BOOT", 19):
            m, te = F.topic_forecast(d)
            _, te2 = F.topic_forecast(d.assign(target=np.where(d.year >= 2023, 0.0, d.target)))
        cols = [f"pred_{k}" for k in F.TOPIC_MODELS]
        np.testing.assert_allclose(te[cols], te2[cols])
        m = m.set_index(["metric", "model"]).estimate
        y, p = te.target, te.pred_momentum
        self.assertAlmostEqual(m[("R2", "momentum")], 1 - ((y - p) ** 2).sum() / ((y - y.mean()) ** 2).sum())
        self.assertAlmostEqual(m[("precision@top quintile", "momentum")], te.real_top[te.top_momentum].mean())


class EndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.k = ph5_common.simulated_frame(seed=3)
        cls.prepared = F.prepare(cls.k.drop(columns=ph5_common.POSTHOC_COLUMNS))

    def test_compute_drops_outcomes(self):
        seen = {}
        with mock.patch.object(F, "compute_free", side_effect=lambda k: seen.setdefault("cols", set(k.columns))):
            F.compute(self.k)
        self.assertFalse(set(ph5_common.POSTHOC_COLUMNS) & seen["cols"])

    def test_compute_plot_and_calibrate(self):
        with mock.patch.object(F, "N_BOOT", 19), mock.patch.object(F, "prepare", return_value=self.prepared):
            out = F.compute(self.k)
            cal = F.calibrate(n_null=1, n_planted=1, seed=1)
        self.assertEqual(len(out["a1_tests"]), 6)
        self.assertEqual(out["b1_screen"].feature.tolist(), list(F.FEATURES))
        self.assertEqual(out["b3_table"].keywords.sum(), len(out["b_risk_set"]))
        self.assertTrue(out["b2_predictions"].cohort.between(2021, 2024).all())
        self.assertEqual(set(out["b4_models"]["map"]), {"early", "k100"})
        self.assertTrue({"main", "entry3", "entry10", "horizon3", "paper_share", "no_llm_family"} <= set(out["robust_b"].variant))
        self.assertTrue(out["a2_transitions"].groupby(["unit_type", "growth", "h", "band", "origin"]).p.sum()
                        .between(1 - 1e-9, 1 + 1e-9).all())
        self.assertEqual(set(cal["a1"]), set(F.UNIT_TYPES))
        self.assertIn("planted_true_auc", cal["b1"]["F3"])
        import posthoc
        with tempfile.TemporaryDirectory() as tmp:
            posthoc.write_outputs(out, Path(tmp))
            F.plot(Path(tmp))
            self.assertEqual(len(list(Path(tmp).glob("forecast_*.png"))), 7)


if __name__ == "__main__":
    unittest.main()
