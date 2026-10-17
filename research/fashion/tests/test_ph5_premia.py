"""PH5 premia: cell, DerSimonian-Laird, REML, cross-year moment, shrinkage and fixed-effect estimators against direct
computations on synthetic data; unit and first-stage feature checks; an end-to-end run of compute, plot and calibrate
on simulated outcomes (no real outcome is read).

    python -m unittest research/fashion/tests/test_ph5_premia.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd
from scipy import optimize, sparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import panel  # noqa: E402
import ph5_common  # noqa: E402
import ph5_premia as m  # noqa: E402
import posthoc  # noqa: E402
from common import OUTPUT  # noqa: E402


def direct_dl(g: np.ndarray, v: np.ndarray) -> float:
    w = 1 / v
    mu = (w * g).sum() / w.sum()
    return ((w * (g - mu) ** 2).sum() - (len(g) - 1)) / (w.sum() - (w ** 2).sum() / w.sum())


class Cells(unittest.TestCase):
    def test_gaps_and_variances_match_direct_computation(self):
        rng = np.random.default_rng(0)
        n, U = 3000, 6
        M = rng.random((n, U)) < 0.25                             # overlapping memberships, as for keywords
        yi = rng.integers(0, len(m.YEARS), n)
        y = (rng.random(n) < 0.4).astype(float)
        Y = m.year_matrix(yi, len(m.YEARS))
        c = m.cells(sparse.csr_matrix(M.astype(float)).T.tocsr(), Y, y)
        n1, k1, N, K = posthoc.cell_counts(M, yi, y, len(m.YEARS))
        np.testing.assert_allclose(c["n"], n1)
        for u in range(U):
            for t in range(len(m.YEARS)):
                a, b = y[(yi == t) & M[:, u]], y[(yi == t) & ~M[:, u]]
                p = y[yi == t].mean()
                self.assertAlmostEqual(c["g"][u, t], a.mean() - b.mean(), places=12)
                self.assertAlmostEqual(c["v"][u, t], p * (1 - p) * (1 / len(a) + 1 / len(b)), places=12)
        r = rng.normal(size=n)
        cr = m.cells(sparse.csr_matrix(M.astype(float)).T.tocsr(), Y, r, residual=True)
        s2 = r[yi == 3].var(ddof=1)
        a, b = r[(yi == 3) & M[:, 2]], r[(yi == 3) & ~M[:, 2]]
        self.assertAlmostEqual(cr["g"][2, 3], a.mean() - b.mean(), places=12)
        self.assertAlmostEqual(cr["v"][2, 3], s2 * (1 / len(a) + 1 / len(b)), places=12)

    def test_window_premia_are_paper_weighted(self):
        c = {"n": np.array([[10.0, 0, 30, 0, 0, 5, 5, 0, 0]]), "g": np.array([[0.1, np.nan, -0.1, 0, 0, 0.2, 0.4, 0, 0]]),
             "v": np.full((1, 9), 0.01)}
        g, v, n = m.window_premia(c, (2018, 2022))
        self.assertAlmostEqual(g[0], (10 * 0.1 - 30 * 0.1) / 40)
        self.assertAlmostEqual(v[0], (100 + 900) * 0.01 / 1600)
        self.assertEqual(n[0], 40)
        self.assertAlmostEqual(m.window_premia(c, (2024, 2026))[0][0], 0.4)


class Estimators(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(1)
        self.U, self.T = 40, len(m.YEARS)
        self.v = rng.uniform(0.0005, 0.01, (self.U, self.T))
        self.g = rng.normal(0, 0.04, (self.U, 1)) + rng.normal(0, np.sqrt(self.v))
        self.ok = rng.random((self.U, self.T)) < 0.8
        self.ok[:, 0] = False
        self.ok[:3, 0] = True                                      # a year below MIN_UNITS

    def test_dl_matches_direct_and_frequency_weights_equal_duplication(self):
        t2, mm = m.dl(self.g, self.v, self.ok, np.ones((1, self.U)))
        self.assertTrue(np.isnan(t2[0, 0]))
        for t in range(1, self.T):
            o = self.ok[:, t]
            self.assertAlmostEqual(t2[0, t], direct_dl(self.g[o, t], self.v[o, t]), places=10)
            self.assertEqual(mm[0, t], o.sum())
        f = np.random.default_rng(2).integers(0, 3, self.U).astype(float)
        dup = np.repeat(np.arange(self.U), f.astype(int))
        a = m.dl(self.g, self.v, self.ok, f[None, :])[0]
        b = m.dl(self.g[dup], self.v[dup], self.ok[dup], np.ones((1, len(dup))))[0]
        np.testing.assert_allclose(a, b, rtol=1e-10)
        pooled = m.pooled(*m.dl(self.g, self.v, self.ok, np.ones((1, self.U))))[0]
        w = mm[0, 1:]
        self.assertAlmostEqual(pooled, (t2[0, 1:] * w).sum() / w.sum(), places=12)

    def test_reml_maximises_the_restricted_likelihood(self):
        o = self.ok[:, 4]
        g, v = self.g[o, 4], self.v[o, 4]

        def nll(t2):
            w = 1 / (v + t2)
            mu = (w * g).sum() / w.sum()
            return 0.5 * (np.log(v + t2).sum() + np.log(w.sum()) + (w * (g - mu) ** 2).sum())

        best = optimize.minimize_scalar(nll, bounds=(0, 0.05), method="bounded", options={"xatol": 1e-12}).x
        self.assertAlmostEqual(m.reml(g, v), best, places=7)
        self.assertEqual(m.reml(np.zeros(10), np.full(10, 0.01)), 0.0)

    def test_cross_year_moments_are_unbiased_for_the_signal(self):
        rng = np.random.default_rng(3)
        U, R = 60, 3000
        v = rng.uniform(0.001, 0.02, (U, 2))
        a = rng.normal(0, 0.05, U)                                 # fixed signals, correlation 1 across the two years
        target = m.cross(np.column_stack([a, a]), v, np.ones((U, 2), bool), np.array([0.0025, 0.0025]), [(0, 1)],
                         np.ones((1, U)), noise=np.zeros_like(v))
        e = np.array([m.cross(np.column_stack([a, a]) + rng.normal(0, np.sqrt(v)), v, np.ones((U, 2), bool),
                              np.array([0.0025, 0.0025]), [(0, 1)], np.ones((1, U)))[:3] for _ in range(R)])[:, :, 0]
        se = e.std(axis=0) / np.sqrt(R)
        for j in range(3):
            self.assertLess(abs(e[:, j].mean() - target[j][0]), 4 * se[j])
        self.assertAlmostEqual(m.ratio(*target[:3])[0], 1.0, places=12)
        f = rng.integers(0, 3, U).astype(float)
        dup = np.repeat(np.arange(U), f.astype(int))
        x = np.column_stack([a, a]) + rng.normal(0, np.sqrt(v))
        one = m.cross(x, v, np.ones((U, 2), bool), np.array([0.002, 0.003]), [(0, 1)], f[None, :])
        two = m.cross(x[dup], v[dup], np.ones((len(dup), 2), bool), np.array([0.002, 0.003]), [(0, 1)],
                      np.ones((1, len(dup))))
        np.testing.assert_allclose(np.array(one[:3]), np.array(two[:3]), rtol=1e-10)

    def test_wls_hc3_against_direct_sandwich(self):
        rng = np.random.default_rng(4)
        x, w = rng.normal(size=50), rng.uniform(0.5, 2, 50)
        y = 0.3 * x + rng.normal(size=50) * (1 + np.abs(x))
        b, se, p, dof = m.wls_hc3(x, y, w)
        X = np.column_stack([np.ones(50), x])
        W = np.diag(w)
        beta = np.linalg.solve(X.T @ W @ X, X.T @ W @ y)
        e = y - X @ beta
        A = np.linalg.inv(X.T @ W @ X)
        H = np.sqrt(W) @ X @ A @ X.T @ np.sqrt(W)                    # leverage of the weighted regression
        V = A @ X.T @ W @ np.diag(e ** 2 / (1 - np.diag(H)) ** 2) @ W @ X @ A
        self.assertAlmostEqual(b, beta[1], places=12)
        self.assertAlmostEqual(se, np.sqrt(V[1, 1]), places=12)
        self.assertAlmostEqual(m.slope_draws(x, y, w, np.ones((1, 50)))[0], beta[1], places=12)
        self.assertEqual(dof, 48)

    def test_fit_fe_matches_wls_fe_and_dummy_regression(self):
        rng = np.random.default_rng(5)
        n = 2000
        d = pd.DataFrame({"topic": rng.integers(0, 25, n), "year": rng.integers(0, 6, n), "x1": rng.normal(size=n),
                          "x2": rng.random(n), "w": rng.uniform(0.5, 2, n), "submission_id": np.arange(n)})
        d["y"] = 0.2 * d.x1 + 0.1 * d.topic % 3 + 0.05 * d.year + rng.normal(size=n)
        f = m.fit_fe(d, "y", ["x1", "x2"], ["topic", "year"], "topic", w="w")
        ref = posthoc.wls_fe(d, "y", ["x1", "x2"], ["topic", "year"], "w", "topic")
        np.testing.assert_allclose(f.beta.to_numpy(), ref.coef.to_numpy(), rtol=1e-8)
        np.testing.assert_allclose(np.sqrt(np.diag(f.V)), ref.se.to_numpy(), rtol=1e-8)
        D = pd.concat([d[["x1", "x2"]], pd.get_dummies(d.topic, prefix="t", dtype=float),
                       pd.get_dummies(d.year, prefix="y", drop_first=True, dtype=float)], axis=1).to_numpy()
        sw = np.sqrt(d.w.to_numpy())
        beta = np.linalg.lstsq(D * sw[:, None], d.y.to_numpy() * sw, rcond=None)[0]
        np.testing.assert_allclose(f.beta.to_numpy(), beta[:2], rtol=1e-7)
        diff = f.term({"x1": 1, "x2": -1})
        self.assertAlmostEqual(diff["coef"], f.beta.x1 - f.beta.x2, places=12)
        V = f.V.to_numpy()
        self.assertAlmostEqual(diff["se"], np.sqrt(V[0, 0] + V[1, 1] - 2 * V[0, 1]), places=12)
        self.assertTrue(np.isnan(f.term({"missing": 1})["coef"]))

    def test_select_and_counts(self):
        s = m.select(np.array([0.1, 0.5, 0.5, -0.2, 0.3]), np.array([0, 2, 1, 0, 0]), 0.4, True)
        self.assertEqual(sorted(s.tolist()), [1, 2])
        self.assertEqual(m.select(np.arange(5.0), np.zeros(5), 0.1, False).tolist(), [0])
        F = m.counts(np.array([[0, 0, 2], [1, 2, 2]]), 3)
        np.testing.assert_array_equal(F, [[2, 0, 1], [0, 1, 2]])

    def test_permutation_is_within_year(self):
        rng = np.random.default_rng(8)
        yi, y = rng.integers(0, 5, 500), rng.normal(size=500)
        yp = m.permute_within(y, yi, rng)
        for t in range(5):
            np.testing.assert_allclose(np.sort(yp[yi == t]), np.sort(y[yi == t]))
        self.assertFalse(np.allclose(yp, y))

    def test_winners_against_direct_computation(self):
        rng = np.random.default_rng(6)
        U = 40
        vx, vy = rng.uniform(1e-4, 4e-3, U), rng.uniform(1e-4, 4e-3, U)
        a = rng.normal(0, 0.05, U)
        x, y = 0.02 + a + rng.normal(0, np.sqrt(vx)), -0.01 + 0.5 * a + rng.normal(0, np.sqrt(vy))
        shrink, rows, table = m.winners(x, vx, y, vy, 0.1, np.random.default_rng(0), 30)
        tx, ty = max(direct_dl(x, vx), 0.0), max(direct_dl(y, vy), 0.0)
        xc, yc = x - (x / vx).sum() / (1 / vx).sum(), y - (y / vy).sum() / (1 / vy).sum()
        eb = tx / (tx + vx) * xc
        self.assertAlmostEqual(shrink["tau_w1_pp"], np.sqrt(tx) * 100, places=10)
        np.testing.assert_allclose(table["eb1"], eb)
        sw = np.sqrt(1 / (vy + ty))
        beta = np.linalg.lstsq(np.column_stack([np.ones(U), x]) * sw[:, None], y * sw, rcond=None)[0]
        self.assertAlmostEqual(shrink["b"], beta[1], places=10)
        got = {(r["ranking"], r["side"]): r for r in rows}
        for (ranking, side), r in got.items():
            score = eb if ranking == "eb" else xc
            s = np.argsort(score)[-4:] if side == "top" else np.argsort(score)[:4]
            self.assertEqual(r["units_selected"], 4)
            self.assertAlmostEqual(r["R"], yc[s].mean() / xc[s].mean(), places=10)
            if ranking == "eb":
                self.assertAlmostEqual(r["R_vs_eb"], yc[s].mean() / eb[s].mean(), places=10)

    def test_surge_reading_rule(self):
        cases = {((True, -1.0), (False, 0.0)): "competition", ((True, -1.0), (True, -1.0)): "competition",
                 ((False, -0.1), (True, -2.0)): "dilution", ((False, 0.1), (False, -2.0)): "proportional allocation",
                 ((False, 0.0), (True, 2.0)): "other", ((True, 1.0), (False, 0.0)): "other"}
        for (inc, new), want in cases.items():
            self.assertEqual(m.read_surge(inc, new), want)


class Features(unittest.TestCase):
    def test_units_and_submissions(self):
        sets, (totals, subs) = m.unit_sets(), m.submissions()
        k = panel.frame("k100")
        for name in ("early", "k100", "areas", "seed_refit"):
            names, M = sets[name]
            np.testing.assert_array_equal(np.asarray(M.sum(1)).ravel(), 1.0)      # partitions
        self.assertEqual({n: len(sets[n][0]) for n in m.UNIT_TYPES}, {"early": 100, "k100": 100, "keywords": 68, "areas": 20})
        pa = np.asarray(sets["primary_area"][1].sum(1)).ravel()
        self.assertTrue((pa[k.year.to_numpy() < 2024] == 0).all() and pa[k.year.to_numpy() >= 2024].mean() > 0.95)
        np.testing.assert_allclose(totals, k.groupby("year").size().reindex(m.ALL_YEARS).to_numpy())
        np.testing.assert_allclose(subs["k100"].sum(0), totals)

    def test_prior_growth_and_first_stage(self):
        totals, subs = m.submissions()
        mat = pd.read_csv(OUTPUT / "topic_year_maturity.csv.gz")
        names = m.unit_sets()["early"][0]
        a = {"c": {"g": np.zeros((len(names), 9)), "v": np.ones((len(names), 9))}, "ok": np.ones((len(names), 9), bool),
             "tau2": 0.0}
        p = m.flow_panel(a, subs["early"], totals)
        ref = mat[mat["map"] == "early"].set_index(["topic", "year"])
        got = p[p.year >= 2019].assign(topic=lambda x: np.array(names)[x.unit]).set_index(["topic", "year"])
        np.testing.assert_allclose(np.exp(got.prior_growth), ref.prior_growth.reindex(got.index), rtol=1e-4, atol=1e-6)
        rng = np.random.default_rng(7)
        U = len(names)
        c = {"g": rng.normal(0, 0.05, (U, 9)), "v": rng.uniform(1e-3, 1e-2, (U, 9))}
        b = {"c": c, "ok": rng.random((U, 9)) < 0.7, "tau2": 0.002}
        p = m.flow_panel(b, subs["early"], totals).set_index(["unit", "year"])
        ls = np.log((subs["early"] + 0.5) / totals)
        for t in (2019, 2023):
            j, jj = t - 2018, t - 2017
            u = np.flatnonzero(b["ok"][:, j])
            g, v = c["g"][u, j], c["v"][u, j]
            w = 1 / (v + 0.002)
            mu = (w * g).sum() / w.sum()
            q = p.loc[[(x, t) for x in u]]
            np.testing.assert_allclose(q.eb10, 10 * (mu + 0.002 / (0.002 + v) * (g - mu)))
            np.testing.assert_allclose(q.gc, g - (g / v).sum() / (1 / v).sum())
            np.testing.assert_allclose(q.dshare, ls[u, jj + 1] - ls[u, jj])
            np.testing.assert_allclose(q.growth, ls[u, jj] - ls[u, jj - 1])
            np.testing.assert_allclose(q.g_next, c["g"][u, j + 1])
            np.testing.assert_array_equal(q.next_ok, b["ok"][u, j + 1])
        fs, info = m.first_stage()
        self.assertEqual(len(fs), 800)
        self.assertAlmostEqual(fs.s.std(ddof=1), 1.0)
        X = pd.get_dummies(fs.year, dtype=float).assign(lp=np.log(fs.papers_prev + 0.5), lg=np.log(fs.prior_growth))
        np.testing.assert_allclose(X.to_numpy().T @ fs.resid.to_numpy(), 0, atol=1e-8)
        self.assertGreater(info["within_r2"], 0.3)


class EndToEnd(unittest.TestCase):
    def test_compute_plot_calibrate_on_simulated_outcomes(self):
        k = ph5_common.simulated_frame(11, m.persistent(11))
        with mock.patch.object(m, "analyse", lambda *a, **kw: ANALYSE(*a, **{**kw, "perms": 19, "boot": 49})):
            out = m.compute(k)
            cal = m.calibrate(n_null=1, n_planted=1, seed=5)
        t = out["tests"]
        fam = t[t.family != ""]
        self.assertEqual(sorted(fam.family.unique()), ["F-areas", "F-early", "F-flows", "F-k100", "F-keywords", "F-surge"])
        self.assertEqual(len(fam), 3 * 4 + 2 + 3)
        self.assertTrue(fam.p.between(0, 1).all() and (fam.p_holm >= fam.p - 1e-12).all())
        sp = out["spread"].set_index("unit_type")
        self.assertGreater(sp.loc["early", "tau_pp"], 2.0)                     # planted sd 0.25 log-odds ~ 5.5 pp
        self.assertEqual(set(out["robustness"].variant), {"main", "composition_adjusted", "min_cell_30", "s9",
                                                          "without_2021_22", "seed_refit_map", "primary_area_2024_26"})
        self.assertEqual(set(out["persistence"].lag), {"1", "2", "3", "4", "W1->W2"})
        self.assertIn(out["summary"]["surge_reading"], {"competition", "dilution", "proportional allocation", "other"})
        self.assertEqual({r["plant"] for r in cal["per_test"]}, set(m.PLANTS))
        with tempfile.TemporaryDirectory() as tmp:
            posthoc.write_outputs(out, Path(tmp))
            m.plot(Path(tmp))
            self.assertEqual(len(list(Path(tmp).glob("PH5_premia_*.png"))), 4)

    def test_composition_adjustment_removes_the_controls(self):
        k = ph5_common.simulated_frame(12, lambda f: 0.8 * f.fm.to_numpy(float))
        s = m.sample(k)
        r = m.adjusted(k, s)
        d = posthoc.add_columns(k.iloc[s.rows].copy()).reset_index(drop=True)
        X = d[m.CONTROLS].to_numpy(float) - d.groupby("year")[m.CONTROLS].transform("mean").to_numpy(float)
        np.testing.assert_allclose(X.T @ r.y, 0, atol=1e-6)
        self.assertTrue(r.residual and np.isfinite(r.y).all())

    def test_free_part_reads_no_outcome(self):
        import outcomes
        with mock.patch.object(ph5_common, "outcome_frame", side_effect=AssertionError("outcomes read")), \
                mock.patch.object(outcomes, "load", side_effect=AssertionError("outcomes read")):
            out = m.compute_free()
        u = out["free_units"].set_index("unit_type")
        self.assertEqual(u.loc["early", "units_ge50_both_windows"], 82)
        self.assertEqual(len(out["free_surge_first_stage"]), 800)


ANALYSE = m.analyse

if __name__ == "__main__":
    unittest.main()
