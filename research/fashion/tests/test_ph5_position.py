"""PH5 position: feature construction (novelty, twins, author overlap) on toy embeddings against brute force, estimator
and permutation checks on synthetic data, and an end-to-end run of compute, plot and calibrate on simulated outcomes
with synthetic features (no real outcome is read).

    python -m unittest research/fashion/tests/test_ph5_position.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd
from scipy import sparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import panel  # noqa: E402
import ph5_common  # noqa: E402
import ph5_position as m  # noqa: E402
import posthoc  # noqa: E402
from ols import fe_ols  # noqa: E402


def unit(rng: np.random.Generator, n: int, dim: int = 8) -> np.ndarray:
    X = rng.normal(size=(n, dim)).astype(np.float32)
    return X / np.linalg.norm(X, axis=1, keepdims=True)


def frame(seed: int = 0, n: int = 4000) -> pd.DataFrame:
    """Synthetic designed population: 40 topics x 4 years, controls, novelty percentile, twins, groups."""
    rng = np.random.default_rng(seed)
    topic = rng.integers(0, 40, n)
    year = rng.integers(2023, 2027, n)
    d = pd.DataFrame({"submission_id": [f"p{i}" for i in range(n)], "topic": topic, "year": year,
                      "cell": topic * 4 + year - 2023, "pct": rng.random(n), "hot": (topic % 5 == 0).astype(float),
                      "newcomer": (rng.random(n) < 0.4).astype(float),
                      "maturity_tercile": np.array(m.MATURITY)[topic % 3]})
    d[f"twins_{m.tag(m.TAU)}"] = rng.poisson(0.6, n)
    d[f"sibling_{m.tag(m.TAU)}"] = (rng.random(n) < 0.05).astype(float)
    for c in m.CONTROLS:
        if c not in d:
            d[c] = rng.normal(size=n) if c == "log2_team" else (rng.random(n) < 0.2).astype(float)
    d = m.design(d)
    d["accepted"] = (rng.random(n) < 0.35 + 0.05 * (d.cell % 3 - 1) - 0.06 * d.q5).astype(float)
    return d


class Features(unittest.TestCase):
    def test_novelty_matches_brute_force(self):
        rng = np.random.default_rng(0)
        years = np.repeat(np.arange(2014, 2021), 40)
        X = unit(rng, len(years))
        chains = [np.array([], int) for _ in years]
        chains[250] = np.array([200, 120])                                   # paper 250 (2020): two earlier versions
        with mock.patch.object(m, "FIXED_REF", 100):
            f = m.novelty(X, years, chains, chunk=17)
        S = X @ X.T
        for i in [45, 130, 250, 279]:
            prior = np.flatnonzero(years < years[i])
            prior = prior[~np.isin(prior, chains[i])]
            s = np.sort(S[i, prior])[::-1]
            self.assertAlmostEqual(f.nov[i], 1 - s[:10].mean(), places=5)
            self.assertAlmostEqual(f.nov_k5[i], 1 - s[:5].mean(), places=5)
            self.assertAlmostEqual(f.nov_k20[i], 1 - s[:20].mean(), places=5)
            self.assertEqual(f.precedents[i], (S[i, prior] >= m.TAU).sum())
            recent = prior[years[prior] >= years[i] - 3]
            self.assertAlmostEqual(f.nov_prior3[i], 1 - np.sort(S[i, recent])[::-1][:10].mean(), places=5)
        self.assertTrue(np.isnan(f.nov[:40]).all())                          # first year: no earlier papers
        early = years == 2015                                                 # fewer earlier papers than FIXED_REF
        np.testing.assert_allclose(f.nov_fixed[early], f.nov[early], atol=1e-6)
        self.assertTrue(np.isfinite(f.nov_fixed[years == 2020]).all())
        self.assertEqual(f.prior_papers[279], 240)

    def test_pairs_classification_and_counts(self):
        rng = np.random.default_rng(1)
        years = np.repeat([2019, 2020], 60)
        X = unit(rng, len(years), 4)
        p = m.same_year_pairs(X, years, chunk=13)
        S = X @ X.T
        want = {(i, j) for i in range(len(years)) for j in range(i + 1, len(years))
                if years[i] == years[j] and S[i, j] >= m.PAIR_MIN}
        self.assertEqual(set(zip(p.i, p.j)), want)
        np.testing.assert_allclose(p.cos, S[p.i, p.j], atol=1e-6)
        A = sparse.csr_matrix((np.ones(3), ([p.i.iloc[0], p.j.iloc[0], p.i.iloc[1]], [0, 0, 1])), shape=(len(years), 2))
        chains = [np.array([], int) for _ in years]
        chains[p.j.iloc[2]] = np.array([p.i.iloc[2]])
        c = m.classify_pairs(p, A, chains)
        self.assertTrue(c.sibling.iloc[0] and not c.independent.iloc[0])
        self.assertTrue(c.earlier.iloc[2] and not c.independent.iloc[2])
        self.assertEqual(int(c.independent.sum()), len(p) - int((c.sibling | c.earlier).sum()))

    def test_names_percentiles_and_design(self):
        self.assertEqual(m.normalise_name('"Jane   Q.  Doe "'), "jane q. doe")
        self.assertIsNone(m.normalise_name("null"))
        self.assertIsNone(m.normalise_name("not json"))
        x = pd.Series([0.3, 0.1, 0.2, np.nan, 0.5, 0.4])
        g = pd.Series([1, 1, 1, 1, 2, 2])
        np.testing.assert_allclose(m.cell_pct(x, [g]), [5 / 6, 1 / 6, 0.5, np.nan, 0.75, 0.25])
        d = frame(2)
        self.assertTrue((d[[f"q{j}" for j in range(1, 6)]].sum(axis=1) == 1).all())
        self.assertTrue(((d.pct >= 0.8) == (d.q5 == 1)).all() and ((d.pct < 0.2) == (d.q1 == 1)).all())
        self.assertTrue(((d.tercile == "high") == (d.pct >= 2 / 3)).all())
        np.testing.assert_allclose(d.twin_high, d.any_twin * (d.tercile == "high"))
        np.testing.assert_allclose(d.q5_mature, d.q5 * (d.maturity_tercile == "mature"))

    def test_real_alignment(self):
        k = panel.frame("k100")
        self.assertEqual(len(m.early_columns()), len(k))
        chains = m.earlier_chains(k.submission_id.reset_index(drop=True))
        has = np.array([len(c) > 0 for c in chains])
        np.testing.assert_array_equal(has, k.has_earlier_version.to_numpy() == 1)


class Estimators(unittest.TestCase):
    def test_fit_matches_dummies_and_fe_ols(self):
        d = frame(3)
        xs = m.xs("Q1")
        f = m.Fit(d, "accepted", xs)
        D = pd.concat([d[xs], pd.get_dummies(d.cell, prefix="c").astype(float)], axis=1).to_numpy(float)
        beta = np.linalg.lstsq(D, d.accepted.to_numpy(), rcond=None)[0]
        np.testing.assert_allclose(f.beta[xs].to_numpy(), beta[:len(xs)], rtol=1e-7, atol=1e-10)
        ref = fe_ols(d.accepted, d[xs], d.cell, d.topic)
        np.testing.assert_allclose(np.sqrt(np.diag(f.V)), ref.se.to_numpy(), rtol=1e-8)

    def test_p3_is_the_high_minus_low_twin_contrast(self):
        d = frame(4)
        f = m.Fit(d, "accepted", m.xs("Q1"))
        alt = d.assign(twin_low=d.any_twin * d.ter_low)
        g = m.Fit(alt, "accepted", m.Q_TERMS + ["any_twin", "ter_low", "ter_high", "twin_low", "twin_high"] + m.CONTROLS)
        a, b = f.lincom({"twin_high": 1}), g.lincom({"twin_high": 1, "twin_low": -1})
        for key in ("coef", "se", "p"):
            self.assertAlmostEqual(a[key], b[key], places=10)

    def test_null_t_matches_fit(self):
        d = frame(5)
        rng = np.random.default_rng(0)
        Y = (rng.random((len(d), 3)) < 0.4).astype(float)
        t = m.null_t(d, m.xs("Q2"), "twin_hot", Y)
        for b in range(3):
            r = m.Fit(d.assign(accepted=Y[:, b]), "accepted", m.xs("Q2")).lincom({"twin_hot": 1})
            self.assertAlmostEqual(t[b], r["coef"] / r["se"], places=8)

    @staticmethod
    def keys(d: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame({"submission_id": np.repeat(d.submission_id, 2),
                             "key": np.concatenate([[f"a{i % 300}", f"b{i % 500}"] for i in range(len(d))])})

    def test_author_fe_matches_wls_fe_with_fe_count_in_the_factor(self):
        d = frame(10)
        rng = np.random.default_rng(1)
        Y = (rng.random((len(d), 2)) < 0.4).astype(float)
        with mock.patch.object(m, "author_keys", lambda: self.keys(d)):
            r, tn = m.author_fe(d, null=Y)
            r1, _ = m.author_fe(d.assign(accepted=Y[:, 1]))
        a = self.keys(d).merge(d, on="submission_id")
        a["w"] = 0.5
        w = posthoc.wls_fe(a, "accepted", ["nov10", "any_twin"] + m.CONTROLS, ["cell", "key"], "w", "topic", "key")
        same = posthoc.drop_singletons(a, ["cell", "key"])
        n, k, authors = len(same), len(w), same.key.nunique()
        scale = np.sqrt((n - k) / (n - k - (authors - 1)))
        self.assertAlmostEqual(r["coef"], w.coef["nov10"], places=10)
        self.assertAlmostEqual(r["se"], w.se["nov10"] * scale, places=10)
        self.assertAlmostEqual(r["se_twoway"], w.se_twoway["nov10"] * scale, places=10)
        self.assertEqual((r["n"], r["authors"]), (n, authors))
        self.assertAlmostEqual(tn[1], r1["coef"] / r1["se"], places=8)

    def test_declared_family_and_calibrated_p(self):
        d = frame(6)
        with mock.patch.object(m, "author_keys", lambda: self.keys(d)):
            res, fits = m.declared(d)
            self.assertEqual(list(res.test), [t[0] for t in m.TESTS])
            self.assertAlmostEqual(res.set_index("test").coef["P6"], fits["Q4"].beta["q5_mature"])
            self.assertTrue((res.p_holm >= res.p - 1e-12).all() and res.se_twoway.notna().iloc[-1])
            res = m.calibrated_p(d, res, np.random.default_rng(0), draws=19)
        cal = res.set_index("test")
        self.assertTrue(cal.p_calibrated[list(m.CALIBRATED)].between(0.05, 1).all())
        self.assertTrue(cal.p_calibrated.drop(list(m.CALIBRATED)).isna().all())
        want = np.fmax(np.fmax(cal.p, cal.p_calibrated.fillna(0)), cal.p_twoway.fillna(0))
        np.testing.assert_allclose(cal.p_used, want)
        self.assertGreaterEqual(cal.p_used["P7"], cal.p_twoway["P7"])

    def test_surface_and_adjusted_table_match_dummy_regressions(self):
        d = frame(11)
        s = m.surface(d).set_index("group")
        D = pd.DataFrame({g: ((d.quintile == int(g[1])) & (d.any_twin == int(g[-1]))).astype(float)
                          for g in s.index if g != "Q3|0"})
        ref = fe_ols(d.accepted, pd.concat([D, d[m.CONTROLS]], axis=1), d.cell, d.topic)
        np.testing.assert_allclose(s.coef[D.columns], ref.coef[D.columns], rtol=1e-8, atol=1e-12)
        np.testing.assert_allclose(s.p[D.columns], ref.p[D.columns], rtol=1e-8)
        self.assertEqual(s.coef["Q3|0"], 0.0)
        self.assertAlmostEqual(s.raw_rate["Q5|1"], d.accepted[(d.quintile == 5) & (d.any_twin == 1)].mean())
        a = m.adjusted_table(d).set_index("group")
        self.assertEqual(len(a.q_bh.dropna()), 10)
        hot = d[d.hot == 1]
        ref_rate = hot.accepted[(hot.tercile == "mid") & (hot.any_twin == 0)].mean()
        self.assertAlmostEqual(a.adjusted_rate["high|1|1"], ref_rate + a.coef["high|1|1"])

    def test_lind_mehlum(self):
        d = frame(7, n=20000)
        rng = np.random.default_rng(7)
        hump = (rng.random(len(d)) < 0.2 + 0.8 * d.pct * (1 - d.pct)).astype(float)
        r = m.lind_mehlum(d.assign(accepted=hump))
        self.assertLess(r["p_inverted_u"], 0.01)
        self.assertAlmostEqual(r["turning_point"], 0.5, delta=0.05)
        self.assertGreater(m.lind_mehlum(d.assign(accepted=1 - hump))["p_inverted_u"], 0.5)


class Dyadic(unittest.TestCase):
    def test_loo_permutation_and_rho(self):
        rng = np.random.default_rng(8)
        codes = rng.integers(0, 12, 300)
        a = (rng.random(300) < 0.4).astype(float)
        r = m.loo_resid(a[:, None], codes)[:, 0]
        for i in [0, 17, 250]:
            others = a[(codes == codes[i]) & (np.arange(300) != i)]
            self.assertAlmostEqual(r[i], a[i] - others.mean())
        single = m.loo_resid(np.array([[1.0], [0.0], [1.0]]), np.array([0, 0, 1]))
        self.assertTrue(np.isnan(single[2, 0]))
        P = m.permute_within(a, codes, rng, 4)
        for b in range(4):
            for c in range(12):
                self.assertEqual(sorted(P[codes == c, b]), sorted(a[codes == c]))
        i, j = rng.integers(0, 300, 50), rng.integers(0, 300, 50)
        pc = (np.bincount(codes, weights=a) / np.bincount(codes))[codes]
        s = m.dyad_stats(r[:, None], a[:, None], pc, [(i, j)])[0, :, 0]
        self.assertAlmostEqual(s[0], np.mean(r[i] * r[j]) / np.var(r))
        self.assertAlmostEqual(s[1], np.mean(a[i] * a[j]) - np.mean(pc[i] * pc[j]))

    def test_dyadic_detects_shared_fate_only_where_planted(self):
        """600 disjoint same-cell pairs per bin; the >= 0.80 pairs share their outcome, the others are independent."""
        rng = np.random.default_rng(12)
        n, cells = 6000, 40
        cell = rng.integers(0, cells, n)
        idx = [rng.permutation(np.flatnonzero(cell == c)) for c in range(cells)]
        pairs = np.vstack([np.column_stack([v[0:len(v) // 2 * 2:2], v[1:len(v) // 2 * 2:2]]) for v in idx])[:1800]
        p = pd.DataFrame({"i": pairs.min(1), "j": pairs.max(1), "cos": np.repeat([0.65, 0.75, 0.85], 600),
                          "independent": True})
        a = (rng.random(n) < 0.4).astype(float)
        a[p.j[1200:]] = a[p.i[1200:]]
        k = pd.DataFrame({"rq3": True, "year": 2024, "cell": cell.astype(str), "accepted": a})
        X = unit(rng, n, 256)
        with mock.patch.object(m, "build", lambda: (None, p)), mock.patch.object(m, "embeddings", lambda: X), \
                mock.patch.object(m, "authors", lambda: sparse.csr_matrix((n, 1))), \
                mock.patch.object(m, "BASE_PAIRS", 20000):
            r = m.dyadic(k, perms=200).set_index(["variant", "bin"])
        self.assertTrue((r.pairs == 600).all())
        c = r.loc["cell"]
        self.assertLess(c.stat_p[">=0.80"], 0.01)
        self.assertGreater(c.stat_excess[">=0.80"], 0.5)
        self.assertTrue((c.stat_p[["0.60-0.70", "0.70-0.80"]] > 0.05).all())
        self.assertTrue((c.p_holm >= c.stat_p).all() and r.loc["year"].p_holm.isna().all())
        np.testing.assert_allclose(c.stat_excess, c.stat - c.stat_null_mean)

    def test_baseline_pairs_are_same_cell_dissimilar_and_independent(self):
        k = panel.frame("k100").reset_index(drop=True)
        rows = np.flatnonzero(k.year.between(2024, 2024).to_numpy())
        cell = pd.factorize(k.cell.to_numpy()[rows])[0]
        i, j = m.baseline_pairs(cell, rows, np.random.default_rng(0), n_pairs=2000, batch=4000)
        self.assertEqual(len(i), 2000)
        self.assertTrue((cell[i] == cell[j]).all() and (i != j).all())
        X, A = m.embeddings(), m.authors()
        self.assertTrue((np.einsum("ij,ij->i", X[rows[i]], X[rows[j]]) < m.BASE_COS).all())
        self.assertEqual(np.asarray(A[rows[i]].multiply(A[rows[j]]).sum(axis=1)).sum(), 0)


def fake_build() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Synthetic features and pairs for every real paper (fast stand-in for build())."""
    k = panel.frame("k100").reset_index(drop=True)
    rng = np.random.default_rng(0)
    n = len(k)
    f = pd.DataFrame({"submission_id": k.submission_id})
    for c in ["nov", "nov_k5", "nov_k20", "nov_prior3", "nov_fixed"]:
        f[c] = np.where(k.year > 2017, rng.random(n), np.nan)
        f["pct" + c[3:]] = m.cell_pct(f[c], [k.topic, k.year])
    f["pct_class"] = m.cell_pct(f.nov, [k.primary_class, k.year])
    f["pct_early"] = m.cell_pct(f.nov, [k.topic_early, k.year])
    f["precedents"], f["prior_papers"] = rng.poisson(1, n), 1000.0
    f["prior_density"] = np.log1p(f.precedents)
    i = rng.integers(0, n, 60000)
    j = np.array([rng.choice(np.flatnonzero(k.year.to_numpy() == y)) for y in k.year.to_numpy()[i]])
    p = pd.DataFrame({"i": np.minimum(i, j), "j": np.maximum(i, j), "cos": rng.uniform(0.6, 0.95, len(i))})
    p = p[p.i != p.j].drop_duplicates(["i", "j"]).reset_index(drop=True)
    p["sibling"], p["earlier"] = rng.random(len(p)) < 0.05, False
    p["independent"] = ~p.sibling
    for t in (m.TAU, *m.TAU_ALT):
        ind, sib = p[(p.cos >= t) & p.independent], p[(p.cos >= t) & p.sibling]
        f[f"twins_{m.tag(t)}"] = np.bincount(ind.i, minlength=n) + np.bincount(ind.j, minlength=n)
        f[f"sibling_{m.tag(t)}"] = ((np.bincount(sib.i, minlength=n) + np.bincount(sib.j, minlength=n)) > 0) * 1.0
    f["dose"] = np.log1p(f[f"twins_{m.tag(m.TAU)}"])
    f["first_time"] = np.where(k.has_author_key, (rng.random(n) < 0.3) * k.newcomer.fillna(1), np.nan)
    return f, p


class EndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fb = fake_build()
        rng = np.random.default_rng(1)
        X = rng.normal(size=(len(cls.fb[0]), 8)).astype(np.float32)
        cls.X = X / np.linalg.norm(X, axis=1, keepdims=True)

    def patches(self):
        return [mock.patch.object(m, "build", lambda: self.fb), mock.patch.object(m, "embeddings", lambda: self.X),
                mock.patch.object(m, "BASE_PAIRS", 5000), mock.patch.object(m, "logit_rows", lambda d: [])]

    def test_compute_plot_and_calibrate(self):
        ps = self.patches()
        for p in ps:
            p.start()
        try:
            out = m.compute(ph5_common.simulated_frame(9), perms=20, nulls=19)
            cal = m.calibrate(n_null=1, n_planted=1, seed=3, perms=10)
        finally:
            for p in ps:
                p.stop()
        tests = out["tests"]
        self.assertEqual(list(tests.test), [t[0] for t in m.TESTS])
        self.assertTrue(tests.p.between(0, 1).all() and tests.p_holm.between(0, 1).all())
        self.assertEqual(len(out["dyadic"]), 6)
        self.assertEqual(len(out["surface"]), 10)
        self.assertEqual(len(out["adjusted_table"]), 12)
        self.assertEqual(set(out["robustness"].variant), {"tau_065", "tau_075", "k5", "k20", "prior_3_years",
                                                          "fixed_reference", "class_year_percentile",
                                                          "prior_density_control", "early_map", "no_earlier_version",
                                                          "twin_dose"})
        self.assertEqual({r["plant"] for r in cal["per_test"]}, {"null", "inverted_u", "twin_hot", "shared_shock"})
        with tempfile.TemporaryDirectory() as tmp:
            posthoc.write_outputs(out, Path(tmp))
            m.plot(Path(tmp))
            self.assertEqual(len(list(Path(tmp).glob("PH5_position_*.png"))), 4)

    def test_free_part_reads_no_outcome(self):
        with mock.patch.object(m, "build", lambda: self.fb):
            k = m.prepare(panel.frame("k100"))
            self.assertNotIn("accepted", k)
            out = m.free_part(k)
        self.assertTrue(out["free_twin_share"].any_twin.between(0, 1).all())
        self.assertIn("first_time", set(out["free_herding"].term))

    def test_plants(self):
        with mock.patch.object(m, "build", lambda: self.fb):
            k = panel.frame("k100").reset_index(drop=True)
            u = m.inverted_u(k)
            q = np.floor(self.fb[0].pct * 5)
            np.testing.assert_array_equal(u != 0, (q == 0) | (q >= 4))
            s = m.shared_shock(0)
            np.testing.assert_array_equal(s(k), s(k))
            hi = self.fb[1][self.fb[1].independent & (self.fb[1].cos >= 0.8)]
            self.assertTrue((s(k)[hi.i.to_numpy()] == s(k)[hi.j.to_numpy()]).all())
            self.assertTrue((m.twin_hot(k) <= 0).all())


if __name__ == "__main__":
    unittest.main()
