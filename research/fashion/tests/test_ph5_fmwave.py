"""PH5 fmwave: estimator, bootstrap, spline and feature checks on synthetic data, and an end-to-end run of compute,
plot and calibrate on simulated outcomes (no real outcome is read).

    python -m unittest research/fashion/tests/test_ph5_fmwave.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd
from scipy.special import logit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import outcomes  # noqa: E402
import panel  # noqa: E402
import ph5_common  # noqa: E402
import ph5_fmwave as m  # noqa: E402
import posthoc  # noqa: E402
from ols import fe_ols  # noqa: E402


def frame(seed: int = 0, n: int = 3000) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    topic = rng.integers(0, 30, n)
    year = rng.integers(2023, 2027, n)
    d = pd.DataFrame({"topic": topic, "topic_early": (topic + rng.integers(0, 2, n)) % 12, "year": year,
                      "cell": topic * 4 + year - 2023})
    cell_adopt = rng.uniform(0.01, 0.95, 120)
    d["adoption"] = cell_adopt[d.cell]
    d["fm"] = (rng.random(n) < 0.2 + 0.6 * d.adoption).astype(float)
    d["no_acc"] = (rng.random(n) < 0.4).astype(float)
    d["framed"] = d.fm * (rng.random(n) < 0.6)
    d["first_time"] = d.no_acc * (rng.random(n) < 0.3)
    d["has_author_key"] = True
    for c in m.CONTROLS:
        d[c] = rng.normal(size=n) if c == "log2_team" else (rng.random(n) < 0.2).astype(float)
    d["accepted"] = (rng.random(n) < 0.35 + 0.1 * d.fm * (1 - d.adoption) + 0.05 * d.cell.map(lambda c: c % 3 - 1)
                     ).astype(float)
    return d


class Estimator(unittest.TestCase):
    def test_fit_matches_dummy_regression_and_fe_ols(self):
        d = m.design(frame(), centre=0.5)
        xs = ["fm", "fm_l"] + m.CONTROLS
        f = m.fit(d, "accepted", xs)
        D = pd.concat([d[xs], pd.get_dummies(d.cell, prefix="c").astype(float)], axis=1).to_numpy(float)
        beta = np.linalg.lstsq(D, d.accepted.to_numpy(), rcond=None)[0]
        np.testing.assert_allclose(f.beta[xs].to_numpy(), beta[:len(xs)], rtol=1e-7, atol=1e-10)
        ref = fe_ols(d.accepted, d[xs], d.cell, d.topic)
        np.testing.assert_allclose(f.beta[xs].to_numpy(), ref.coef.to_numpy(), rtol=1e-8)
        np.testing.assert_allclose(np.sqrt(np.diag(f.V.loc[xs, xs])), ref.se.to_numpy(), rtol=1e-8)
        self.assertEqual(f.G, 30)

    def test_lincom_matches_recentred_regression(self):
        """B1 as a linear combination equals the fm_na coefficient when l is centred at logit(0.10) instead."""
        base = frame(1)
        xs = ["fm", "fm_l", "fm_na", "fm_l_na", "no_acc", "na_l"] + m.CONTROLS
        a = m.fit(m.design(base, centre=0.7), "accepted", xs)
        r = a.lincom({"fm_na": 1, "fm_l_na": float(logit(0.10)) - 0.7})
        b = m.fit(m.design(base, centre=float(logit(0.10))), "accepted", xs).lincom({"fm_na": 1})
        for key in ("coef", "se", "p"):
            self.assertAlmostEqual(r[key], b[key], places=10)
        self.assertTrue(np.isnan(a.lincom({"not_a_term": 1})["coef"]))

    def test_twoway_reduces_to_oneway_when_clusters_coincide(self):
        d = m.design(frame(2), centre=0.0)
        f = m.fit(d, "accepted", ["fm", "fm_l"] + m.CONTROLS, cluster2="topic")
        r = f.lincom({"fm_l": 1})
        self.assertAlmostEqual(r["se_twoway"], r["se"], places=12)
        g = m.fit(d, "accepted", ["fm", "fm_l"] + m.CONTROLS, cluster2="topic_early")
        V, V2 = g.V.loc["fm_l", "fm_l"], g.V2.loc["fm_l", "fm_l"]
        tw = g.lincom({"fm_l": 1})["se_twoway"] ** 2
        self.assertTrue(tw > 0 and (np.isclose(tw, g.Vt.loc["fm_l", "fm_l"]) or np.isclose(tw, max(V, V2))))

    def test_twoway_matches_direct_cgm(self):
        d = m.design(frame(5), centre=0.3)
        xs = ["fm", "fm_l"] + m.CONTROLS
        f = m.fit(d, "accepted", xs, cluster2="topic_early")
        D = pd.get_dummies(d.cell).astype(float).to_numpy()
        M = np.eye(len(d)) - D @ np.linalg.pinv(D)                       # annihilator of the cell dummies
        X, y = M @ d[xs].to_numpy(float), M @ d.accepted.to_numpy(float)
        inv = np.linalg.inv(X.T @ X)
        e = y - X @ (inv @ X.T @ y)
        n, k = X.shape

        def v(groups):
            s = pd.DataFrame(X * e[:, None]).groupby(np.asarray(groups)).sum().to_numpy()
            G = len(s)
            return G / (G - 1) * (n - 1) / (n - k) * inv @ s.T @ s @ inv
        both = d.topic.astype(str) + "/" + d.topic_early.astype(str)
        np.testing.assert_allclose(f.V.to_numpy(), v(d.topic), rtol=1e-8, atol=1e-14)
        np.testing.assert_allclose(f.Vt.to_numpy(), v(d.topic) + v(d.topic_early) - v(both), rtol=1e-8, atol=1e-14)
        self.assertEqual(f.G2, min(d.topic.nunique(), d.topic_early.nunique()))

    def test_bootstrap_draw_equals_fit_on_resampled_topics(self):
        """A draw with topic 0 twice and topic 1 absent equals FE-OLS on that resample (copies as separate cells)."""
        d = m.design(frame(6), centre=0.0)
        xs = ["fm", "fm_l"] + m.CONTROLS
        order = pd.factorize(d.topic)[1]
        w = np.ones(len(order), int)
        w[order.get_loc(0)], w[order.get_loc(1)] = 2, 0

        class Fixed:
            def multinomial(self, n, p, size):
                return np.tile(w, (size, 1))
        names, B = m.boot_betas(d, "accepted", xs, Fixed(), draws=1)
        copy = d[d.topic == 0].assign(cell=lambda x: x.cell + 10_000, topic=-1)
        res = pd.concat([d[d.topic != 1], copy], ignore_index=True)
        np.testing.assert_allclose(B[0], m.fit(res, "accepted", xs).beta[names].to_numpy(), rtol=1e-8)

    def test_bootstrap_with_unit_weights_is_the_full_fit(self):
        d = m.design(frame(3), centre=0.0)
        xs = ["fm", "fm_l"] + m.CONTROLS
        f = m.fit(d, "accepted", xs)

        class Ones:
            def multinomial(self, n, p, size):
                return np.ones((size, len(p)), int)
        names, B = m.boot_betas(d, "accepted", xs, Ones(), draws=2)
        np.testing.assert_allclose(B[0], f.beta[names].to_numpy(), rtol=1e-8)
        star = m.crossing(f, d, 0.0, np.random.default_rng(0))
        self.assertIn(star["status"], {"crossing in range", "not reached in range"})
        self.assertAlmostEqual(star["a_star"], 1 / (1 + np.exp(f.beta["fm"] / f.beta["fm_l"])), places=10)

    def test_declared_rows_and_holm(self):
        d = m.design(frame(4), centre=0.0)
        rows, fits = m.declared(d, 0.0)
        self.assertEqual(list(rows.test), ["A1", "A2", "B1", "B2", "C1", "C2"])
        for _, g in rows.groupby("family"):
            lo, hi = sorted(g.p)
            first = min(1.0, 2 * lo)
            np.testing.assert_allclose(sorted(g.p_holm), [first, max(first, hi)])
        self.assertAlmostEqual(rows.set_index("test").coef["A2"], fits["F1_bins"].beta["fm_b4"])
        self.assertAlmostEqual(rows.set_index("test").coef["C2"], fits["F3"].beta["framed_l"])


    def test_centred_terms_keep_the_fm_mix(self):
        """With fm x centred area dummies, the fm coefficient is the FM-share-weighted mean of the area premia."""
        d = frame(7).assign(area=lambda x: x.topic % 4)
        d = m.design(d.assign(accepted=d.accepted + 0.1 * d.fm * (d.area == 2)), centre=0.0)
        dc, cols = m.centred_terms(d, "area", "fm", d.fm == 1)
        self.assertEqual(len(cols), 3)
        np.testing.assert_allclose(dc.loc[dc.fm == 1, cols].mean(), 0, atol=1e-12)
        full = dc.assign(**{f"fa{a}": d.fm * (d.area == a) for a in range(4)})
        f_full = m.fit(full, "accepted", [f"fa{a}" for a in range(4)] + m.CONTROLS)
        share = d.area[d.fm == 1].value_counts(normalize=True).sort_index()
        r = f_full.lincom({f"fa{a}": share[a] for a in range(4)})
        c = m.fit(dc, "accepted", ["fm"] + cols + m.CONTROLS).lincom({"fm": 1})
        self.assertAlmostEqual(r["coef"], c["coef"], places=10)
        self.assertAlmostEqual(r["se"], c["se"], places=10)

    def test_crossing_in_range_and_open_ends(self):
        d = frame(8, n=6000)
        d["adoption"] = d.cell.map(dict(enumerate(np.linspace(0.02, 0.98, 120)[np.random.default_rng(0).permutation(120)])))
        fade = 0.25 * d.fm * (0.3 - d.adoption)                           # premium crosses zero at 30% adoption
        u = np.random.default_rng(1).random(len(d))
        with mock.patch.object(m, "BOOT", 199):
            dd = m.design(d.assign(accepted=(u < 0.35 + fade).astype(float)), centre=0.0)
            st = m.crossing(m.fit(dd, "accepted", ["fm", "fm_l"] + m.CONTROLS), dd, 0.0, np.random.default_rng(2))
            self.assertEqual(st["status"], "crossing in range")
            self.assertTrue(0.02 <= st["a_star_ci_lo"] < st["a_star"] < st["a_star_ci_hi"] <= 0.98)
            flat = m.design(d.assign(accepted=(u < 0.35 + 0.15 * d.fm).astype(float)), centre=0.0)
            st = m.crossing(m.fit(flat, "accepted", ["fm", "fm_l"] + m.CONTROLS), flat, 0.0, np.random.default_rng(2))
            self.assertEqual(st["status"], "not reached in range")
            self.assertTrue(st["a_star_ci_lo"] in (0.0, 1.0) or st["a_star_ci_hi"] in (0.0, 1.0))


class Features(unittest.TestCase):
    def test_rcs_is_zero_below_and_linear_beyond_the_knots(self):
        t = np.array([-2.0, 0.5, 3.0])
        self.assertTrue(np.all(m.rcs(np.linspace(-5, -2, 7), t) == 0))
        x = np.linspace(3.5, 8, 10)
        np.testing.assert_allclose(np.diff(m.rcs(x, t), 2), 0, atol=1e-9)

    def test_bins_and_logit(self):
        d = m.design(pd.DataFrame({"adoption": [0.0, 0.049, 0.05, 0.149, 0.15, 0.3, 0.5, 0.99, np.nan], "fm": 1.0,
                                   "framed": 0.0, "first_time": 0.0}), centre=0.0)
        self.assertEqual(d.bin.tolist(), [0, 0, 1, 1, 2, 3, 4, 4])
        self.assertAlmostEqual(d.ladopt.iloc[0], logit(0.02))
        self.assertAlmostEqual(d.ladopt.iloc[-1], logit(0.98))

    def test_framing_and_code_link_patterns(self):
        for t in ["LLM-based agents", "Vision-Language Models for X", "GPT-4 as a judge", "Fine-tuning LLaMA-2",
                  "multimodal large language models"]:
            self.assertTrue(m.FRAMING.search(t), t)
        for t in ["Graph neural networks", "Language modeling of proteins", "Diffusion models"]:
            self.assertFalse(m.FRAMING.search(t), t)
        self.assertEqual(m.first_sentence("Models (e.g. LLMs) are big. We study X."), "Models (e.g. LLMs) are big.")
        self.assertEqual(m.first_sentence("We study RL. LLMs are not used."), "We study RL.")
        self.assertFalse(m.CODE_LINK.search("https://github.com/anonymous/repo"))
        self.assertTrue(m.CODE_LINK.search("Code: https://github.com/lab/repo"))

    def test_code_links_difference_and_flag(self):
        k = pd.DataFrame({"year": [2022] * 4 + [2023] * 4 + [2024] * 2, "rq3": True,
                          "accepted": [1, 1, 0, 0, 1, 1, 0, 0, 1, 0.0],
                          "code_link": [1, 0, 0, 0, 1, 1, 1, 0, 0, 0.0]})
        t, s = m.code_links(k)
        np.testing.assert_allclose(t.difference, [0.5, 0.5, 0.0])
        self.assertAlmostEqual(s["difference_2023_2026"], (0.5 * 4 + 0.0 * 2) / 6)
        self.assertEqual(s["F3_label"], "possibly contaminated by camera-ready edits")

    def test_real_features(self):
        f, k = m.features(), panel.frame("k100")
        np.testing.assert_allclose(m.prior_share(k.topic, k.year, k.fm), k.fm_adoption.to_numpy(), equal_nan=True)
        self.assertTrue((k.newcomer[f.first_time.to_numpy() == 1] == 1).all())      # first-timers are topic newcomers
        late = (k.year >= 2023).to_numpy()
        self.assertGreater(f.framed[late & (k.fm == 1).to_numpy()].mean(), f.framed[late & (k.fm == 0).to_numpy()].mean())
        self.assertTrue(f.fm_primary_area[k.year.to_numpy() < 2025].sum() == 0)
        self.assertLess((f.fm2 != k.fm.to_numpy()).mean(), 0.01)

    def test_true_prob_matches_fake_outcomes(self):
        k = ph5_common.simulated_frame(5)
        dec = k[k.rq3 & k.year.between(2023, 2026)]
        rate = dec.groupby("year").accepted.mean()
        p = pd.Series(m.true_prob(dec, None), dec.index).groupby(dec.year).mean()
        np.testing.assert_allclose(rate.to_numpy(), p.to_numpy(), atol=0.03)


class EndToEnd(unittest.TestCase):
    def test_compute_plot_calibrate_on_simulated_outcomes(self):
        k = ph5_common.simulated_frame(7)
        sealed = mock.Mock(side_effect=AssertionError("real outcomes requested"))
        with mock.patch.object(m, "BOOT", 49), mock.patch.object(m, "logit_rows", lambda *a: []), \
                mock.patch.object(outcomes, "load", sealed), mock.patch.object(ph5_common, "outcome_frame", sealed):
            out = m.compute(k)
            cal = m.calibrate(n_null=1, n_planted=1, seed=3)
        sealed.assert_not_called()
        tests = out["tests"]
        self.assertEqual(list(tests.test), ["A1", "A2", "B1", "B2", "C1", "C2"])
        self.assertTrue(tests.p.between(0, 1).all() and tests.p_twoway.between(0, 1).all())
        self.assertEqual(out["summary"]["a_star"]["draws"], 49)
        rob = out["robustness"]
        self.assertEqual(set(rob.variant), {"years_2024_2026", "fm_x_year", "early_map", "fm_x_area", "papers_prev_ge30",
                                            "second_pass_fm", "s9", "without_fm_primary_area"})
        self.assertEqual(list(rob[rob.variant == "fm_x_year"].test), ["A1", "A2", "C1", "C2"])
        self.assertTrue(rob.coef.notna().all())
        a = out["summary"]["a_star"]
        self.assertTrue(0 <= a["a_star_ci_lo"] <= a["a_star_ci_hi"] <= 1)
        self.assertEqual(len(out["bins"]), 25)
        self.assertEqual(set(out["curves"].model), {"F1 spline", "F1 linear", "F2 established", "F2 no acceptance",
                                                    "F3 framing"})
        self.assertEqual({r["plant"] for r in cal["per_test"]}, {"null", "fading", "constant", "calendar"})
        self.assertEqual({r["test"] for r in cal["per_test"]},
                         {"A1", "A2", "B1", "B2", "C1", "C2", "A1 fm_x_year", "A2 fm_x_year", "C1 fm_x_year",
                          "C2 fm_x_year"})
        with tempfile.TemporaryDirectory() as tmp:
            posthoc.write_outputs(out, Path(tmp))
            m.plot(Path(tmp))
            self.assertEqual(len(list(Path(tmp).glob("PH5_fmwave_*.png"))), 4)

    def test_logit_variant(self):
        k = m.prepare(ph5_common.simulated_frame(8))
        pop = m.population(k)
        pop = pop[pop.year == 2026]
        rows = m.logit_rows(m.design(pop, 0.0), m.design(pop, float(logit(0.10))))
        self.assertEqual([r["test"] for r in rows], ["A1", "A2", "B1", "B2", "C1", "C2"])
        self.assertTrue(all(np.isfinite(r["coef"]) for r in rows))

    def test_free_part_reads_no_outcome(self):
        k = m.prepare(panel.frame("k100"))
        self.assertNotIn("accepted", k)
        out = m.free_part(k)
        self.assertEqual(len(out["free_entry"]), 10)
        s = out["free_fm_share"]
        self.assertTrue(s.fm_share.between(0, 1).all())


if __name__ == "__main__":
    unittest.main()
