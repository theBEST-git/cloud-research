"""PH5 pivot: distance features, spline, estimators (FE-OLS, pooled groups, logit reparametrisation, within-author
WLS, bootstrap arg-max, curves) against direct computation on synthetic data, the frozen reference points, and an
end-to-end run of compute, plot and calibrate on simulated outcomes (no real outcome is read).

    python -m unittest research/fashion/tests/test_ph5_pivot.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import panel  # noqa: E402
import ph5_common  # noqa: E402
import ph5_pivot as m  # noqa: E402
import posthoc  # noqa: E402
from logit import fe_logit  # noqa: E402
from ols import fe_ols  # noqa: E402


def frame(seed: int = 0, n: int = 4000) -> pd.DataFrame:
    """Synthetic paper population with every P1 column (F_max spread over the REF knots)."""
    rng = np.random.default_rng(seed)
    topic = rng.integers(0, 30, n)
    year = rng.integers(2023, 2027, n)
    d = pd.DataFrame({"submission_id": [f"p{i}" for i in range(n)], "topic": topic, "year": year,
                      "cell": [f"{t}:{y}" for t, y in zip(topic, year)]})
    d["hot"] = ((topic + year) % 3 == 0).astype(float)
    d["F_max"] = rng.uniform(-0.2, 0.9, n)
    for c in m.CONTROLS:
        d[c] = rng.normal(size=n) if c in ("log2_team", "log_prior_team") else (rng.random(n) < 0.2).astype(float)
    eta = -0.4 + 0.8 * (d.F_max - 0.35) ** 2 - 0.5 * d.hot * (d.F_max < 0.1) + 0.2 * (topic % 3)
    d["accepted"] = (rng.random(n) < 1 / (1 + np.exp(-eta))).astype(float)
    d["established"] = (rng.random(n) < 0.6).astype(float)
    d["primary_class"] = rng.choice(["method", "theory", "empirical"], n)
    return d


def direct_prior_cos(x, year, authors, earlier) -> dict[tuple[int, str], tuple[float, int]]:
    """prior_cos and |P_a| by brute force (the module docstring's definition)."""
    out = {}
    for r, key in authors[["r", "key"]].itertuples(index=False):
        start = m.HISTORY_START.get(int(year[r]))
        if start is None:
            continue
        mine = authors[authors.key == key].r
        prior = [q for q in mine if start <= year[q] < year[r] and q != earlier[r] and x[r] @ x[q] < m.NEAR_DUP]
        if prior:
            c = x[prior].mean(axis=0)
            out[(r, key)] = (float(x[r] @ c / np.linalg.norm(c)), len(prior))
    return out


class Features(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(5)
        self.year = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2026, 2024])
        x = rng.normal(size=(12, 8))
        x[7] = x[4] + 0.01 * rng.normal(size=8)               # near duplicate of an earlier paper by the same author
        self.x = x / np.linalg.norm(x, axis=1, keepdims=True)
        rows = [(0, "A"), (1, "A"), (2, "A"), (3, "A"), (3, "B"), (4, "A"), (4, "B"), (5, "B"), (5, "C"), (6, "A"),
                (6, "C"), (7, "A"), (7, "B"), (8, "C"), (8, "A"), (8, "B"), (9, "C"), (10, "D"), (10, "A"), (11, "B")]
        a = pd.DataFrame(rows, columns=["r", "key"])
        a["first"] = ~a.r.duplicated(keep="first")
        a["last"] = ~a.r.duplicated(keep="last")
        self.a = a
        self.earlier = np.full(12, -1)
        self.earlier[8] = 5                                     # paper 8's probable earlier version

    def test_distances_match_brute_force(self):
        f, ar = m.distances(self.x, self.year, self.a, self.earlier)
        ref = direct_prior_cos(self.x, self.year, self.a, self.earlier)
        got = {(r, k): (c, n) for r, k, n, c in ar[["r", "key", "n_prior", "prior_cos"]].itertuples(index=False)}
        self.assertEqual(set(got), set(ref))
        for key, (c, n) in ref.items():
            self.assertAlmostEqual(got[key][0], c, places=5)
            self.assertEqual(got[key][1], n)
        self.assertEqual(got[(7, "A")][1], 1)                   # paper 4 (near duplicate) dropped, paper 6 kept
        self.assertTrue(np.isnan(f.loc[[0, 1, 4, 5], "F_max"]).all())          # no history window (2017-18, 2021-22)
        self.assertGreater(f.n_excluded[7], 0)                                  # near duplicate dropped
        for r in range(12):
            mine = {k: c for (rr, k), (c, _) in ref.items() if rr == r}
            if not mine:
                self.assertEqual(f.n_exp[r], 0)
                continue
            self.assertAlmostEqual(f.F_max[r], max(mine.values()), places=5)
            self.assertEqual(f.n_exp[r], len(mine))
            mine_a = self.a[self.a.r == r]
            first, last = mine_a[mine_a["first"]].key.iloc[0], mine_a[mine_a["last"]].key.iloc[0]
            self.assertTrue(np.isclose(f.F_first[r], mine[first]) if first in mine else np.isnan(f.F_first[r]))
            self.assertTrue(np.isclose(f.F_last[r], mine[last]) if last in mine else np.isnan(f.F_last[r]))

    def test_team_centroid_and_nearest(self):
        f, _ = m.distances(self.x, self.year, self.a, self.earlier)
        r = 8                                                   # 2025: authors C, A, B; history 2021-2024
        keys = set(self.a[self.a.r == r].key)
        pool = sorted({q for q in self.a[self.a.key.isin(keys)].r if 2021 <= self.year[q] < 2025 and q != 5
                       and self.x[r] @ self.x[q] < m.NEAR_DUP})
        c = self.x[pool].mean(axis=0)
        self.assertAlmostEqual(f.F_team[r], self.x[r] @ c / np.linalg.norm(c), places=5)
        self.assertAlmostEqual(f.F_nn[r], max(self.x[r] @ self.x[q] for q in pool), places=5)
        self.assertEqual(f.n_prior_team[r], len(pool))

    def test_rcs_properties(self):
        kn = m.REF["F_max"]["knots"]
        x = np.linspace(-0.5, 1.2, 400)
        B = m.rcs(x, kn)
        np.testing.assert_allclose(B[:, 0], x)
        self.assertTrue(np.all(B[x <= kn[0], 1:] == 0))
        tail = np.linspace(kn[-1] + 0.01, 1.5, 20)
        np.testing.assert_allclose(np.diff(m.rcs(tail, kn)[:, 1:], 2, axis=0), 0, atol=1e-9)
        for t in kn:                                            # continuous first derivative at every knot
            h = 1e-6
            left = (m.rcs(t, kn) - m.rcs(t - h, kn)) / h
            right = (m.rcs(t + h, kn) - m.rcs(t, kn)) / h
            np.testing.assert_allclose(left, right, atol=1e-4)

    def test_real_features_are_consistent(self):
        f, ar = m.features()
        year = panel.frame("k100").year.to_numpy()
        has = f.F_max.notna().to_numpy()
        np.testing.assert_array_equal(has, f.n_exp.to_numpy() > 0)
        self.assertFalse(has[~np.isin(year, list(m.HISTORY_START))].any())        # 2017-18 and 2021-22: history only
        rows = ar.groupby("submission_id").prior_cos.agg(["max", "size"]).reindex(f.submission_id)
        np.testing.assert_allclose(rows["max"].to_numpy()[has], f.F_max.to_numpy()[has], atol=1e-6)
        np.testing.assert_array_equal(rows["size"].fillna(0).to_numpy(), f.n_exp.to_numpy())
        for v in ["F_first", "F_last", "F_max3"]:
            ok = f[v].notna()
            self.assertTrue((f.F_max[ok] >= f[v][ok] - 1e-6).all(), v)
        for v in m.DIST + ["F_mean"]:
            self.assertTrue(f[v].dropna().between(-1 - 1e-6, 1 + 1e-6).all(), v)
        big = ar.groupby("submission_id").n_prior.agg(["max", "sum"]).reindex(f.submission_id)
        self.assertTrue((f.n_prior_team.to_numpy()[has] >= big["max"].to_numpy()[has]).all())
        self.assertTrue((f.n_prior_team.to_numpy()[has] <= big["sum"].to_numpy()[has]).all())

    def test_frozen_reference_points_match_the_data(self):
        f, ar = m.features()
        ref = m.reference_points(f, ar, panel.frame("k100").year)
        for v, spec in m.REF.items():
            for key, val in spec.items():
                np.testing.assert_allclose(ref[v][key], val, atol=1e-9, err_msg=f"{v} {key}")


class Estimators(unittest.TestCase):
    def test_fit_matches_dummy_regression_and_fe_ols(self):
        d = m.design(frame())
        xs = m.SPLINE + m.SPLINE_X + m.CONTROLS
        f = m.fit(d, "accepted", xs)
        D = pd.concat([d[xs], pd.get_dummies(d.cell, prefix="c").astype(float)], axis=1).to_numpy(float)
        beta = np.linalg.lstsq(D, d.accepted.to_numpy(), rcond=None)[0]
        np.testing.assert_allclose(f.beta[xs].to_numpy(), beta[:len(xs)], rtol=1e-6, atol=1e-9)
        ref = fe_ols(d.accepted, d[xs], d.cell, d.topic)
        np.testing.assert_allclose(np.sqrt(np.diag(f.V.loc[xs, xs])), ref.se.to_numpy(), rtol=1e-8)

    def test_contrasts_are_curve_differences(self):
        d = m.design(frame(1))
        res, f = m.p1(d)
        kn, ref = m.REF["F_max"]["knots"], m.REF["F_max"]
        b, bx = f.beta[m.SPLINE].to_numpy(), f.beta[m.SPLINE_X].to_numpy()
        curve = lambda v, w=0.0: float(m.rcs(v, kn)[0] @ (b + w * bx))          # noqa: E731
        self.assertAlmostEqual(res["E1"]["coef"], curve(ref["p10"]) - curve(ref["p50"]), places=12)
        self.assertAlmostEqual(res["E2"]["coef"], curve(ref["p90"]) - curve(ref["p50"]), places=12)
        s = d.hot.mean()
        hot = curve(ref["p10"], 1 - s) - curve(ref["p50"], 1 - s)
        cold = curve(ref["p10"], -s) - curve(ref["p50"], -s)
        self.assertAlmostEqual(res["E3"]["coef"], hot - cold, places=12)
        self.assertAlmostEqual(res["E1"]["coef"], s * hot + (1 - s) * cold, places=12)   # population average
        cv = m.curves(f, d)
        for g, w in [("all", 0.0), ("hot", 1 - s), ("not hot", -s)]:
            c = cv[cv.group == g]
            self.assertAlmostEqual(c.p_accept.iloc[40] - c.p_accept.iloc[10],
                                   curve(c.F_max.iloc[40], w) - curve(c.F_max.iloc[10], w), places=10)

    def test_planted_curve_is_recovered(self):
        """y linear in the spline basis (plus cell effects): the contrasts are exact."""
        d = m.design(frame(2))
        kn = m.REF["F_max"]["knots"]
        B = m.rcs(d.F_max, kn)
        true = np.array([0.1, -0.3, 0.2])
        d["y"] = B @ true + (d.topic * 7 + d.year) % 5 / 10
        f = m.fit(d, "y", m.SPLINE + m.SPLINE_X + m.CONTROLS)
        c = m.contrast("F_max", "p10")
        self.assertAlmostEqual(f.lincom(c)["coef"], sum(true[j] * c[f"s{j}"] for j in range(3)), places=8)
        self.assertAlmostEqual(f.lincom(m.contrast("F_max", "p10", "sx"))["coef"], 0.0, places=8)

    def test_pooled_groups_equal_separate_fits(self):
        pop = frame(3)
        groups = {"est": (pop.established == 1).to_numpy(), "no": (pop.established == 0).to_numpy()}
        pooled, _ = m.pooled_e1(pop, groups)
        for g, mask in groups.items():
            sep = m.p1(m.design(pop[mask]))[0]["E1"]
            self.assertAlmostEqual(pooled[g]["coef"], sep["coef"], places=10)
            self.assertAlmostEqual(pooled[g]["se"], sep["se"], delta=0.05 * sep["se"])

    def test_logit_reparametrisation_gives_the_contrast(self):
        d = m.design(frame(4, n=3000)).reset_index(drop=True)
        X = d[m.SPLINE + m.SPLINE_X + m.CONTROLS].astype(float)
        r, _ = fe_logit(d.accepted.astype(float), X, [d.cell.rename("cell")], d.topic)
        rows = {x["test"]: x for x in m.logit_rows(d)}
        for t, at, pre in [("E1", "p10", "s"), ("E2", "p90", "s"), ("E3", "p10", "sx")]:
            w = m.contrast("F_max", at, pre)
            self.assertAlmostEqual(rows[t]["coef"], sum(r.coef[c] * v for c, v in w.items()), places=6)

    def test_within_author_slope_matches_dummy_wls(self):
        rng = np.random.default_rng(6)
        n = 900
        at = pd.DataFrame({"submission_id": [f"s{i // 2}" for i in range(n)], "key": rng.integers(0, 120, n),
                           "topic": rng.integers(0, 12, n), "year": rng.integers(2023, 2025, n)})
        at["cell"] = at.topic.astype(str) + ":" + at.year.astype(str)
        at["prior_cos"], at["n_prior"] = rng.uniform(-0.2, 0.8, n), rng.integers(1, 9, n)
        for c in m.P2_CONTROLS:
            at[c] = rng.normal(size=n) if c in ("log_prior", "log2_team") else (rng.random(n) < 0.3).astype(float)
        at["accepted"] = (rng.random(n) < 0.3 + 0.2 * at.prior_cos).astype(float)
        at["w"] = 1.0 / at.groupby("submission_id").key.transform("size")
        e4 = m.p2(at)
        dd = posthoc.drop_singletons(at, ["key", "cell"])
        xs = ["prior_cos"] + m.P2_CONTROLS
        D = pd.concat([dd[xs], pd.get_dummies(dd.key, prefix="k").astype(float),
                       pd.get_dummies(dd.cell, prefix="c", drop_first=True).astype(float)], axis=1).to_numpy(float)
        sw = np.sqrt(dd.w.to_numpy())
        beta = np.linalg.lstsq(D * sw[:, None], dd.accepted.to_numpy() * sw, rcond=None)[0]
        self.assertAlmostEqual(e4["coef"], 0.1 * beta[0], places=7)
        self.assertEqual(e4["n"], len(dd))
        self.assertGreater(e4["se_twoway"], 0)
        # CR1 by topic with every absorbed author FE counted: partial the dummies out (weighted), then the sandwich
        F = D[:, len(xs):] * sw[:, None]
        X = dd[xs].to_numpy(float) * sw[:, None]
        Xt = X - F @ np.linalg.lstsq(F, X, rcond=None)[0]
        e = (dd.accepted.to_numpy() - D @ beta) * sw
        g = pd.factorize(dd.topic)[0]
        S = np.zeros((g.max() + 1, len(xs)))
        np.add.at(S, g, Xt * e[:, None])
        bread = np.linalg.inv(Xt.T @ Xt)
        n, k, A, G = len(dd), len(xs), dd.key.nunique(), g.max() + 1
        V = G / (G - 1) * (n - 1) / (n - k - (A - 1)) * bread @ S.T @ S @ bread
        self.assertAlmostEqual(e4["se"], 0.1 * np.sqrt(V[0, 0]), places=8)

    def test_author_sample_weights_and_quintiles(self):
        d = frame(9, n=600)
        rng = np.random.default_rng(9)
        ar = pd.DataFrame({"submission_id": rng.choice(d.submission_id, 1500), "key": rng.integers(0, 300, 1500)})
        ar = ar.drop_duplicates(["submission_id", "key"])
        ar["n_prior"], ar["prior_cos"] = rng.integers(1, 6, len(ar)), rng.uniform(-0.3, 0.9, len(ar))
        for min_prior in (1, 3):
            at = m.author_sample(d, ar, min_prior=min_prior)
            self.assertTrue((at.n_prior >= min_prior).all())
            np.testing.assert_allclose(at.groupby("submission_id").w.sum(), 1.0)
            q = at[m.QUINTS].to_numpy()
            self.assertTrue((q.sum(axis=1) <= 1).all())
            edges = m.REF["prior_cos"]["quintiles"]
            middle = (at.prior_cos >= edges[1]) & (at.prior_cos < edges[2])
            np.testing.assert_array_equal(q.sum(axis=1) == 0, middle.to_numpy())
            np.testing.assert_allclose(at.log_prior, np.log1p(at.n_prior))

    def test_quintile_levels_average_to_the_mean(self):
        d = m.design(frame(10))
        rng = np.random.default_rng(10)
        n = 3000
        ar = pd.DataFrame({"submission_id": rng.choice(d.submission_id, n), "key": rng.integers(0, 400, n)})
        ar = ar.drop_duplicates(["submission_id", "key"])
        ar["n_prior"], ar["prior_cos"] = rng.integers(1, 6, len(ar)), rng.uniform(-0.3, 0.9, len(ar))
        q = m.quintile_rows(d, m.author_sample(d, ar))
        p1 = q[q.model.str.startswith("P1")]
        self.assertAlmostEqual(float((p1.coef * p1.papers).sum() / p1.papers.sum()), float(d.accepted.mean()), places=10)
        p2 = q[q.model.str.startswith("P2")].set_index("quintile")
        self.assertEqual(p2.loc["Q3", "coef"], 0.0)
        self.assertTrue(np.isfinite(p2.coef).all())

    def test_bootstrap_with_unit_weights_is_the_full_fit(self):
        d = m.design(frame(7))
        xs = m.SPLINE + m.SPLINE_X + m.CONTROLS
        f = m.fit(d, "accepted", xs)

        class Ones:
            def multinomial(self, n, p, size):
                return np.ones((size, len(p)), int)
        names, B = m.boot_betas(d, "accepted", xs, Ones(), draws=2)
        np.testing.assert_allclose(B[0], f.beta[names].to_numpy(), rtol=1e-8)
        am = m.argmax(f, d, np.random.default_rng(0))
        g = m.grid()
        self.assertEqual(am["all"]["argmax"], g[np.argmax(m.rcs(g, m.REF["F_max"]["knots"]) @ f.beta[m.SPLINE])])
        self.assertTrue(am["all"]["ci95"][0] <= am["all"]["ci95"][1])

    def test_declared_and_secondary_rows(self):
        pop = frame(8)
        pop["F_first"] = np.where(pop.index % 3 == 0, pop.F_max - 0.1, np.nan)
        pop["F_last"] = np.where(pop.index % 2 == 0, pop.F_max - 0.05, np.nan)
        pop["measurement"] = (pop.primary_class == "empirical").astype(float)
        sec = m.secondary(pop)
        self.assertEqual(len(sec), 8)
        self.assertEqual(int(sec.q_bh.notna().sum()), 7)
        self.assertTrue((sec.q_bh.dropna() >= sec.p[sec.q_bh.notna()] - 1e-12).all())


class EndToEnd(unittest.TestCase):
    def test_compute_plot_and_calibrate_on_simulated_outcomes(self):
        k = ph5_common.simulated_frame(11)
        out = m.compute(k)
        self.assertEqual(list(out["tests"].test), ["E1", "E2", "E3", "E4"])
        self.assertTrue(np.isfinite(out["tests"].coef).all() and (out["tests"].p_holm >= out["tests"].p).all())
        rob = out["robustness"]
        self.assertTrue({"newcomer_control", "team_experience_control", "authors_ge3_prior", "no_earlier_version", "s9",
                         "replication_2019_2020", "early_map", "F_last_as_primary", "F_team_as_primary", "F_nn_as_primary", "team_2_4",
                         "team_5_7", "team_8plus", "logit"} <= set(rob.variant))
        self.assertTrue(np.isfinite(rob.coef).all())
        self.assertEqual(len(out["curves"]), 3 * m.GRID_POINTS)
        self.assertLess(out["free_summary"]["max_abs_drift_from_REF"], 1e-9)
        with tempfile.TemporaryDirectory() as tmp:
            posthoc.write_outputs(out, Path(tmp))
            m.plot(Path(tmp))
            for name in ["PH5_pivot_curve", "PH5_pivot_within_author", "PH5_pivot_heat"]:
                self.assertTrue((Path(tmp) / f"{name}.png").exists())
        cal = m.calibrate(n_null=1, n_planted=1, seed=3)
        per = pd.DataFrame(cal["per_test"])
        self.assertEqual(len(per), 12)
        far = per[(per.plant == "far") & (per.test == "E1")].iloc[0]
        self.assertLess(far.mean_target, -0.03)                 # the planted far-jump penalty shows in the target


if __name__ == "__main__":
    unittest.main()
