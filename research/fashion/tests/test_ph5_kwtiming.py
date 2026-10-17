"""PH5 kwtiming: estimator checks on synthetic data (weighted FE OLS with full two-way covariance, weighted FE logit,
DerSimonian-Laird), keyword-frame construction on the real outcome-free data, and an end-to-end run of compute, plot
and calibrate on simulated outcomes (no real outcome is read).

    python -m unittest research/fashion/tests/test_ph5_kwtiming.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import panel  # noqa: E402
import ph5_common  # noqa: E402
import ph5_kwtiming as m  # noqa: E402
import posthoc  # noqa: E402
from common import topic_layer  # noqa: E402
from logit import fe_logit  # noqa: E402
from variables import load_authors  # noqa: E402


def frame(seed: int = 0, n: int = 4000) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    d = pd.DataFrame({"i": rng.integers(0, n // 2, n), "topic": rng.integers(0, 30, n), "keyword": rng.integers(0, 45, n),
                      "year": rng.integers(2019, 2023, n)})
    d["cell"] = d.topic * 10 + d.year - 2019
    d["kwyear"] = d.keyword * 10 + d.year - 2019
    d["x1"], d["x2"] = rng.normal(size=n), (rng.random(n) < 0.3).astype(float)
    d["w"] = 1 / rng.integers(1, 4, n)
    eff = rng.normal(0, 0.1, 30)[d.topic] + rng.normal(0, 0.05, 45)[d.keyword]
    d["y"] = (rng.random(n) < 0.35 + 0.05 * d.x1.clip(-2, 2) + 0.1 * d.x2 + eff).astype(float)
    return d


def wls_dummies(d: pd.DataFrame, xs: list[str], fes: list[str]) -> np.ndarray:
    D = pd.concat([d[xs]] + [pd.get_dummies(d[f], prefix=f, drop_first=j > 0).astype(float) for j, f in enumerate(fes)],
                  axis=1).to_numpy(float)
    sw = np.sqrt(d.w.to_numpy())
    return np.linalg.lstsq(D * sw[:, None], d.y.to_numpy() * sw, rcond=None)[0][:len(xs)]


class Estimators(unittest.TestCase):
    def test_fit_matches_dummy_wls_and_posthoc_wls_fe(self):
        d = frame()
        f = m.fit(d, "y", ["x1", "x2"], clusters=("topic",))
        np.testing.assert_allclose(f.beta.to_numpy(), wls_dummies(d, ["x1", "x2"], ["cell"]), rtol=1e-8)
        ref = posthoc.wls_fe(d.assign(submission_id=d.i), "y", ["x1", "x2"], ["cell"], "w", "topic", "keyword")
        np.testing.assert_allclose(f.beta.to_numpy(), ref.coef.to_numpy(), rtol=1e-10)
        np.testing.assert_allclose(np.sqrt(np.diag(f.V)), ref.se.to_numpy(), rtol=1e-8)
        self.assertEqual(f.G, 30)
        two = m.fit(d, "y", ["x1", "x2"])
        k1 = m.fit(d, "y", ["x1", "x2"], clusters=("keyword",))
        k2 = m.fit(d.assign(kt=d.keyword.astype(str) + "|" + d.topic.astype(str)), "y", ["x1", "x2"], clusters=("kt",))
        raw = k1.V.to_numpy() + f.V.to_numpy() - k2.V.to_numpy()
        lam, Q = np.linalg.eigh(raw)
        np.testing.assert_allclose(two.V.to_numpy(), (Q * np.clip(lam, 0, None)) @ Q.T, atol=1e-14)
        self.assertEqual(two.G, 30)
        if lam.min() >= 0:
            self.assertAlmostEqual(float(np.sqrt(two.V.iloc[0, 0])), float(ref.se_twoway.iloc[0]), places=10)

    def test_two_fixed_effects_match_dummies(self):
        d = frame(1)
        f = m.fit(d, "y", ["x1", "x2"], fes=("kwyear", "cell"))
        np.testing.assert_allclose(f.beta.to_numpy(), wls_dummies(d, ["x1", "x2"], ["kwyear", "cell"]), rtol=1e-6)

    def test_twoway_with_identical_clusters_is_oneway(self):
        d = frame(2)
        a = m.fit(d.assign(t2=d.topic), "y", ["x1", "x2"], clusters=("topic", "t2"))
        b = m.fit(d, "y", ["x1", "x2"], clusters=("topic",))
        np.testing.assert_allclose(a.V.to_numpy(), b.V.to_numpy(), atol=1e-14)

    def test_lincom_and_wald(self):
        d = frame(3)
        f = m.fit(d, "y", ["x1", "x2"])
        r = f.lincom({"x1": 0.5, "x2": -1.0})
        c = np.array([0.5, -1.0])
        self.assertAlmostEqual(r["coef"], float(c @ f.beta), places=12)
        self.assertAlmostEqual(r["se"], float(np.sqrt(c @ f.V.to_numpy() @ c)), places=12)
        q = stats.t.ppf(0.975, f.G - 1)
        self.assertAlmostEqual(r["mde80"], (q + stats.t.ppf(0.8, f.G - 1)) * r["se"], places=12)
        w1 = f.wald(["x1"])
        self.assertAlmostEqual(w1["F"], (f.beta["x1"] / np.sqrt(f.V.loc["x1", "x1"])) ** 2, places=8)
        self.assertAlmostEqual(w1["p_nominal"], f.lincom({"x1": 1})["p"], places=8)
        self.assertTrue(np.isnan(f.lincom({"nope": 1})["coef"]))

    def test_weighted_logit_matches_fe_logit_and_replication(self):
        d = frame(4, 1500).assign(w=1.0)
        d["cell"] = d.topic
        f = m.fe_logit_w(d, "y", ["x1", "x2"], fe="cell", clusters=("topic",))
        ref, _ = fe_logit(d.y, d[["x1", "x2"]], [d.cell.rename("cell")], d.topic)
        np.testing.assert_allclose(f.beta.to_numpy(), ref.coef.to_numpy(), rtol=1e-6)
        np.testing.assert_allclose(np.sqrt(np.diag(f.V)), ref.se.to_numpy(), rtol=0.05)  # CR1 factors differ slightly
        reps = np.random.default_rng(0).integers(1, 4, len(d))
        dw = d.assign(w=reps.astype(float))
        rep = d.loc[d.index.repeat(reps)]
        a = m.fe_logit_w(dw, "y", ["x1", "x2"], clusters=("topic",))
        b = m.fe_logit_w(rep, "y", ["x1", "x2"], clusters=("topic",))
        np.testing.assert_allclose(a.beta.to_numpy(), b.beta.to_numpy(), rtol=1e-7)

    def test_dersimonian_laird(self):
        y, v = np.array([0.1, -0.05, 0.2, 0.0, 0.08]), np.array([0.01, 0.02, 0.015, 0.01, 0.03]) ** 2
        r = m.dersimonian_laird(y, v)
        w = 1 / v
        mu = (w * y).sum() / w.sum()
        Q = (w * (y - mu) ** 2).sum()
        tau2 = max(0, (Q - 4) / (w.sum() - (w ** 2).sum() / w.sum()))
        self.assertAlmostEqual(r["tau2"], tau2, places=12)
        ws = 1 / (v + tau2)
        mu2 = (ws * y).sum() / ws.sum()
        np.testing.assert_allclose(r["post_mean"], mu2 + tau2 / (tau2 + v) * (y - mu2))
        flat = m.dersimonian_laird(np.zeros(5) + 0.01, v)
        self.assertEqual(flat["tau2"], 0.0)
        np.testing.assert_allclose(flat["post_mean"], 0.01)

    def test_pooled_variance_removes_mean_variance_bias(self):
        rng = np.random.default_rng(0)
        own, pooled = [], []
        for _ in range(200):                                    # 120 keywords x 40 binary uses, common p = 0.3
            y = (rng.random((120, 40)) < 0.3).astype(float)
            g = pd.DataFrame({"size": 40, "mean": y.mean(1), "var": y.var(1, ddof=1)})
            own.append(m.dersimonian_laird(g["mean"].to_numpy(), g["var"].to_numpy() / 40)["mu"])
            d = m.pooled_dl(g)
            pooled.append(d["mu"])
            self.assertAlmostEqual(d["pooled_var"], float(y.var(1, ddof=1).mean()), places=12)
        self.assertLess(abs(np.mean(pooled) - 0.3), 0.001)
        self.assertLess(np.mean(own), 0.3 - 0.004)              # own variances bias mu towards low-rate keywords

    def test_within_cell_permutation(self):
        rng = np.random.default_rng(1)
        codes = rng.integers(0, 50, 3000)
        y = (rng.random(3000) < 0.4).astype(float)
        yp = m.within_cell_permutation(y, codes, rng)
        np.testing.assert_array_equal(np.bincount(codes, yp), np.bincount(codes, y))
        self.assertFalse(np.array_equal(yp, y))

    def test_mom_shrink_recovers_between_cell_variance(self):
        rng = np.random.default_rng(2)
        group = pd.Series(np.repeat(np.arange(3000), 3))
        se = pd.Series(rng.uniform(0.02, 0.06, len(group)))
        m_ = pd.Series(rng.normal(0, 1, 3000)[group] + rng.normal(0, 0.05, len(group)) + rng.normal(0, se))
        mean, shrink, tau2 = m.mom_shrink(m_, se, group)
        self.assertAlmostEqual(tau2, 0.05 ** 2, delta=0.0003)
        np.testing.assert_allclose(mean, m_.groupby(group).transform("mean"))
        np.testing.assert_allclose(shrink, tau2 / (tau2 + se ** 2))
        self.assertEqual(m.mom_shrink(pd.Series([0.1, 0.1, 0.1]), pd.Series([0.05] * 3), pd.Series([0] * 3))[2], 0.0)

    def test_declared_contrasts(self):
        beta = pd.Series(np.random.default_rng(3).normal(size=len(m.DUMMIES)), m.DUMMIES)
        f = m.Fit(beta, pd.DataFrame(np.eye(len(beta)), beta.index, beta.index), 100, 1, 1)
        full = {s: beta.get(f"st_{s}", 0.0) for s in m.STATES}
        a3 = np.mean([full[f"young_{x}"] - full[f"old_{x}"] for x in m.MOMS])
        self.assertAlmostEqual(f.lincom(m.A_TESTS["A3"])["coef"], a3, places=12)
        self.assertAlmostEqual(f.lincom(m.A_TESTS["A1"])["coef"], full["young_rising"] - full["old_flat"], places=12)
        self.assertAlmostEqual(f.lincom(m.A_TESTS["A2"])["coef"], full["old_falling"] - full["old_flat"], places=12)


class Features(unittest.TestCase):
    def test_terciles_and_ties(self):
        g = pd.Series([1, 2, 3, 4, 5, 6, 1, 1, 1, 5, 9, np.nan], dtype=float)
        yr = pd.Series([0] * 6 + [1] * 6)
        t = m.terciles(g, yr)
        self.assertEqual(t[:6].tolist(), ["falling", "falling", "flat", "flat", "rising", "rising"])
        self.assertEqual(t[6:9].nunique(), 1)                                    # ties share a tercile
        self.assertTrue(pd.isna(t.iloc[-1]))

    def test_arrivals_and_local_stage(self):
        u = pd.DataFrame({"keyword": ["a"] * 7 + ["b"], "area": ["x", "x", "x", "x", "y", "y", "x", "x"],
                          "year": [2018, 2019, 2019, 2021, 2020, 2021, 2023, 2019], "big": [True] * 7 + [False]})
        self.assertEqual(m.arrivals(u, "area", 3).to_dict(), {("a", "x"): 2019})
        le = m.locally_early(u, "area", 3)
        np.testing.assert_array_equal(le[:7], [1, 1, 1, 0, 1, 1, 0])               # area y never reaches 3 users
        self.assertTrue(np.isnan(le[7]))

    def test_real_keyword_frame(self):
        f = m.features()
        u, kw, p = f["uses"], f["keywords"], f["papers"]
        el = u[u.eligible]
        self.assertEqual((len(kw), int(kw.censored.sum()), int(kw.big.sum())), (759, 28, 129))
        self.assertEqual((len(el), el.i.nunique()), (53458, 29816))               # the spec's checked totals
        self.assertTrue((el.agebin[el.censored] == "old").all())
        self.assertTrue(el.year.between(2019, 2026).all())
        ok = el[~el.censored]
        age = ok.year - ok.onset
        self.assertTrue(((age <= 2) == (ok.agebin == "young")).all() and ((age >= 5) == (ok.agebin == "old")).all())
        shares = el.groupby(["year", "mom"]).keyword.nunique().unstack()
        self.assertTrue(((shares.max(axis=1) - shares.min(axis=1)) / shares.sum(axis=1) < 0.25).all())
        self.assertTrue(el[el.year == 2019].state2.isna().all() and el[el.year > 2019].state2.notna().all())
        self.assertTrue(u.le3[~u.big].isna().all() and u.le3[u.big].notna().all())
        k = panel.frame("k100").reset_index(drop=True)
        self.assertTrue((k.newcomer.to_numpy()[p.first_time.to_numpy() == 1] == 1).all())
        self.assertEqual(int(p.n_eligible.sum()), int(u.eligible.sum()))
        corpus = topic_layer().embedded_corpus()[["submission_id", "year", "keywords"]]
        authors = load_authors(corpus.submission_id)[["submission_id", "key"]]
        for kwd in ["federated learning", "diffusion models"]:
            rows = u[(u.keyword == kwd) & u.year.between(2021, 2023)]
            d = k.iloc[rows.i.to_numpy()][["submission_id", "year"]]
            ref = posthoc.keyword_incumbent(kwd, d, corpus, authors)
            np.testing.assert_array_equal(np.nan_to_num(rows.kw_inc.to_numpy(), nan=-1), np.nan_to_num(ref, nan=-1))

    def test_local_stage_is_prospective(self):
        u = m.features()["uses"]
        b = u[u.big]
        cnt = b.groupby(["keyword", "area", "year"]).size().unstack(fill_value=0)
        cum = cnt.reindex(columns=range(2015, 2027), fill_value=0).cumsum(axis=1).stack()
        before = cum.reindex(pd.MultiIndex.from_arrays([b.keyword, b.area, b.year - 2])).fillna(0).to_numpy()
        np.testing.assert_array_equal(b.le3.to_numpy(), (before < 3).astype(float))   # only uses counts up to t - 2

    def test_plants_and_true_prob(self):
        k = ph5_common.simulated_frame(5)
        p = m.features()["papers"]
        t = m.PLANTS["timing"](k)
        self.assertTrue(set(np.unique(t)) <= {-m.PLANT, 0.0, m.PLANT})
        self.assertGreater((t > 0).sum(), 1000)
        self.assertEqual(int((m.PLANTS["local"](k) > 0).sum()), int(p.has_local_early.sum()))
        dec = k[k.rq3 & k.year.between(2019, 2026)]
        pr = pd.Series(m.true_prob(dec, None), dec.index).groupby(dec.year).mean()
        np.testing.assert_allclose(dec.groupby("year").accepted.mean().to_numpy(), pr.to_numpy(), atol=0.03)


class EndToEnd(unittest.TestCase):
    def test_compute_plot_calibrate_on_simulated_outcomes(self):
        k = ph5_common.simulated_frame(7)
        with mock.patch.object(m, "PERMS", 3):
            out = m.compute(k, n_ref=3)
            cal = m.calibrate(n_null=2, n_planted=1, seed=3)
        tests = out["tests"]
        self.assertEqual(list(tests.test[:6]), ["A1", "A2", "A3", "D_E", "D_C", "C1"])
        self.assertTrue(tests.p.between(0, 1).all() and (tests.p_holm[:6] >= tests.p[:6] - 1e-12).all())
        self.assertTrue(tests.mde80_sim[:6].notna().all() and tests.size_in_null_frames[:6].between(0, 1).all())
        om = out["summary"]["omnibus"]
        self.assertEqual((om["df1"], om["null_frames"]), (8, 3))
        st = out["state_effects"]
        self.assertEqual(st.groupby("model").size().tolist(), [9] * 5)
        a = st[st.model == "A"].set_index("state")
        self.assertAlmostEqual(a.coef["young_rising"], tests.coef.iloc[0])
        b = {g: st[st.model == g].set_index("state").coef for g in ("B no acceptance", "B established")}
        for s, t in [("young_rising", "D_E"), ("old_falling", "D_C")]:
            self.assertAlmostEqual(b["B no acceptance"][s] - b["B established"][s],
                                   float(tests.coef[tests.test == t].iloc[0]), places=10)
        self.assertTrue(tests.p_null_frames[:6].between(1 / 4, 1).all())
        self.assertAlmostEqual(a.adjusted_rate[m.REF], out["summary"]["mainstream_rate"])
        self.assertEqual(len(out["profile_cells"]), 27)
        self.assertEqual(set(out["local_early"].block), {"C main", "C by global age", "C grid", "C importer",
                                                         "C robustness"})
        self.assertEqual(out["robustness"].variant.nunique(), 9)
        self.assertGreater(len(out["keyword_premia"]), 20)
        self.assertEqual(out["summary"]["model_d"]["permutations"], 3)
        self.assertEqual({r["plant"] for r in cal["per_test"]}, {"null", "timing", "local"})
        with tempfile.TemporaryDirectory() as tmp:
            posthoc.write_outputs(out, Path(tmp))
            m.plot(Path(tmp))
            self.assertEqual(len(list(Path(tmp).glob("PH5_kwtiming_*.png"))), 5)

    def test_free_part_reads_no_outcome(self):
        k = m.prepare(panel.frame("k100"))
        self.assertNotIn("accepted", k)
        out = m.free_part(k)
        self.assertEqual(len(out["free_profile_states"]), 9)
        self.assertAlmostEqual(float(out["free_profile_states"].coef.sum()), 0.0, places=8)   # shares sum to 1
        s = out["free_state_shares"]
        np.testing.assert_allclose(s.groupby("year").share_weighted.sum(), 1.0)


if __name__ == "__main__":
    unittest.main()
