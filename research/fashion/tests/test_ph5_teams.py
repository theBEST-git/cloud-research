"""PH5 teams: the LPM, logit, contrast, adjusted-probability and permutation estimators against direct computations
on synthetic data; author-type and paper-feature construction on toy and real (outcome-free) data; an end-to-end run
of compute, plot and calibrate on simulated outcomes (no real outcome is read).

    python -m unittest research/fashion/tests/test_ph5_teams.py
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import logit as logit_module  # noqa: E402
import panel  # noqa: E402
import ph5_common  # noqa: E402
import ph5_teams as m  # noqa: E402
import posthoc  # noqa: E402
from ols import fe_ols  # noqa: E402


def synthetic(n: int = 3000, seed: int = 0, binary: bool = False) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    topic = rng.integers(0, 30, n)
    year = rng.integers(0, 3, n)
    d = pd.DataFrame({"topic": topic.astype(str), "cell": [f"{t}:{y}" for t, y in zip(topic, year)]})
    d["x1"] = rng.normal(size=n) + 0.3 * topic / 30
    d["grp"] = rng.integers(0, 4, n)
    for g in (1, 2, 3):
        d[f"g{g}"] = (d.grp == g).astype(float)
    eta = 0.4 * d.x1 + 0.3 * d.g1 - 0.2 * d.g3 + rng.normal(0, 0.5, 30)[topic] + 0.2 * year
    d["y"] = (rng.random(n) < 1 / (1 + np.exp(-(eta - 0.4)))).astype(float) if binary else eta + rng.normal(size=n)
    return d


class Estimators(unittest.TestCase):
    def test_lpm_matches_fe_ols(self):
        d = synthetic()
        xs = ["x1", "g1", "g2", "g3"]
        f = m.lpm(d, "y", xs)
        r = fe_ols(d.y, d[xs], d.cell, d.topic)
        np.testing.assert_allclose(f.beta.to_numpy(), r.coef.to_numpy(), rtol=1e-10)
        np.testing.assert_allclose(np.sqrt(np.diag(f.vcov)), r.se.to_numpy(), rtol=1e-10)
        self.assertEqual((f.n, f.G), (int(r.n.iloc[0]), int(r.clusters.iloc[0])))
        np.testing.assert_allclose(f.A @ f.yd, f.beta.to_numpy(), rtol=1e-10)

    def test_lpm_drops_collinear_columns(self):
        d = synthetic().assign(dup=lambda x: 2 * x.g1, cellconst=lambda x: x.cell.str.len().astype(float))
        f = m.lpm(d, "y", ["x1", "g1", "dup", "cellconst", "g2"])
        g = m.lpm(d, "y", ["x1", "g1", "g2"])
        self.assertEqual(list(f.beta.index), ["x1", "g1", "g2"])
        np.testing.assert_allclose(f.beta.to_numpy(), g.beta.to_numpy(), rtol=1e-10)
        self.assertTrue(np.isnan(f.contrast({"dup": 1.0})["estimate"]))

    def test_contrast_equals_reparametrised_regression(self):
        d = synthetic().assign(g0=lambda x: (x.grp == 0).astype(float))
        f = m.lpm(d, "y", ["x1", "g1", "g2", "g3"])                       # reference group 0
        r = f.contrast({"g1": 1.0, "g2": -1.0})
        c = np.array([0, 1.0, -1.0, 0])
        self.assertAlmostEqual(r["estimate"], float(c @ f.beta), places=12)
        self.assertAlmostEqual(r["se"], float(np.sqrt(c @ f.vcov.to_numpy() @ c)), places=12)
        g = m.lpm(d, "y", ["x1", "g1", "g0", "g3"])                       # reference group 2
        self.assertAlmostEqual(r["estimate"], g.beta["g1"], places=10)
        self.assertAlmostEqual(r["se"], float(np.sqrt(g.vcov.loc["g1", "g1"])), places=10)

    def test_logit_matches_fe_logit(self):
        d = synthetic(4000, 1, binary=True)
        d.loc[d.cell == d.cell.iloc[0], "y"] = 1.0                        # a cell without outcome variation
        xs = ["x1", "g1", "g2", "g3"]
        f = m.logit(d, "y", xs)
        r, info = logit_module.fe_logit(d.y, d[xs], [d.cell], d.topic)
        self.assertEqual(info["dropped_groups"], [d.cell.iloc[0]])
        np.testing.assert_allclose(f.beta.to_numpy(), r.coef.to_numpy(), rtol=1e-6, atol=1e-8)
        np.testing.assert_allclose(np.sqrt(np.diag(f.vcov)), r.se.to_numpy(), rtol=1e-6)
        self.assertEqual(f.n, int(r.n.iloc[0]))

    def test_adjusted_probabilities(self):
        d = synthetic(2000, 2, binary=True)
        one = d.assign(cell="all")
        a = m.adjusted(one, one.grp, [], y="y")
        np.testing.assert_allclose(a.adjusted.to_numpy(), one.groupby("grp").y.mean().to_numpy(), atol=1e-12)
        b = m.adjusted(d, d.grp, ["x1"], y="y")
        self.assertAlmostEqual(float((b.adjusted * b.papers).sum() / b.papers.sum()), d.y.mean(), places=12)
        np.testing.assert_allclose(b.raw_rate.to_numpy(), d.groupby("grp").y.mean().to_numpy())

    def test_within_permutation_and_permutation_draw(self):
        rng = np.random.default_rng(3)
        groups = rng.integers(0, 7, 500)
        perm = m.within_permutation(groups, rng)
        self.assertEqual(sorted(perm), list(range(500)))
        np.testing.assert_array_equal(groups[perm], groups)
        d = synthetic(1500, 4)
        f = m.lpm(d, "y", ["x1", "g1", "g2", "g3"])
        p = m.within_permutation(f.groups, np.random.default_rng(5))
        refit = m.lpm(d.assign(y=d.y.to_numpy()[p]), "y", ["x1", "g1", "g2", "g3"])
        np.testing.assert_allclose(f.A @ f.yd[p], refit.beta.to_numpy(), rtol=1e-9)


class Features(unittest.TestCase):
    def toy(self) -> pd.DataFrame:
        rows = [("p1", "a", 0, 2020, "T"), ("p2", "a", 1, 2021, "T"), ("p2", "b", 0, 2021, "T"),
                ("p3", "c", 0, 2022, "U"), ("p3", "a", 1, 2022, "U"), ("p3", "b", 2, 2022, "U"), ("p3", "d", 3, 2022, "U"),
                ("p4", "b", 0, 2022, "T"), ("p4", "a", 1, 2022, "T"), ("p4", "e", 2, 2022, "T")]
        return pd.DataFrame(rows, columns=["submission_id", "key", "position", "year", "topic"])

    def test_prior_types_and_paper_level(self):
        at = self.toy()
        at["prior_any"] = m.prior(at, None)
        at["prior_topic"] = m.prior(at, "topic")
        np.testing.assert_array_equal(at.prior_any, [0, 1, 0, 0, 2, 1, 0, 1, 2, 0])
        np.testing.assert_array_equal(at.prior_topic, [0, 1, 0, 0, 0, 0, 0, 1, 2, 0])
        at["type_x"] = m.classify(at.prior_any, at.prior_topic)
        np.testing.assert_array_equal(at.type_x, [0, 2, 0, 0, 1, 1, 0, 2, 2, 0])
        f = m.paper_level(at, ("x",))
        np.testing.assert_array_equal(f.loc[["p1", "p2", "p3", "p4"], "team"], [1, 2, 4, 3])
        np.testing.assert_array_equal(f.loc[["p1", "p2", "p3", "p4"], "n_exp"], [0, 1, 2, 2])
        np.testing.assert_array_equal(f.loc[["p1", "p2", "p3", "p4"], "prior"], [0, 1, 3, 3])
        np.testing.assert_array_equal(f.loc[["p1", "p2", "p3", "p4"], "n_ins_x"], [0, 1, 0, 2])
        np.testing.assert_array_equal(f.loc[["p2", "p3", "p4"], "first_x"], [0, 0, 2])     # by position, not row
        np.testing.assert_array_equal(f.loc[["p2", "p3", "p4"], "last_x"], [2, 0, 0])
        np.testing.assert_array_equal(f.loc[["p1", "p2", "p3", "p4"], "mid_ins_x"], [0, 0, 0, 1])

    def test_keyword_prior(self):
        at = self.toy()
        kw = pd.DataFrame({"submission_id": ["p1", "p2", "p4", "p4"], "kw": ["gnn", "rl", "gnn", "vision"]})
        out = m.keyword_prior(at, kw)
        np.testing.assert_array_equal(out[:3], [0, 0, 0])                 # p1: first; p2: 'rl' never earlier
        self.assertTrue(np.isnan(out[3:7]).all())                          # p3 lists no keyword
        np.testing.assert_array_equal(out[7:], [0, 1, 0])                  # p4: only author a listed 'gnn' before

    def test_alphabetical(self):
        rows = pd.DataFrame({"submission_id": ["a"] * 3 + ["b"] * 3 + ["c"] * 2 + ["d"] * 3,
                             "position": [0, 1, 2, 2, 1, 0, 0, 1, 0, 1, 2],
                             "name": ['"Ann Abel"', '"Bo B\\u00f6hm"', '"Cy Cole Jr."', '"Z Zed"', '"Y Young"',
                                      '"X Xu"', '"A A"', '"B B"', '"Q Quinn"', '"P Park"', '"R Rao"']})
        self.assertEqual(m.surname('"Bo B\\u00f6hm"'), "bohm")
        self.assertEqual(m.surname('"Cy Cole Jr."'), "cole")
        flag = m.alphabetical(rows)
        self.assertEqual(flag.to_dict(), {"a": True, "b": True, "c": False, "d": False})

    def test_real_features_are_consistent(self):
        k = panel.frame("k100").reset_index(drop=True)
        f = m.paper_features()
        self.assertTrue((f.index.to_numpy() == k.submission_id.to_numpy()).all())
        key = k.has_author_key.to_numpy()
        e = f[key]
        np.testing.assert_array_equal(e.team.to_numpy(), k.team_size.to_numpy()[key])
        np.testing.assert_array_equal((e.n_ins_k100 >= 1).astype(float).to_numpy(), k.incumbent.to_numpy()[key])
        for n in ("k100", "early"):
            self.assertTrue((e[f"n_ins_{n}"] <= e.n_exp).all() and (e.n_exp <= e.team).all())
            self.assertTrue((e[f"mid_ins_{n}"] <= e[f"n_ins_{n}"]).all())
        recent = e[k.year.to_numpy()[key] >= 2023].n_ins_k100.clip(upper=3).value_counts().sort_index()
        self.assertEqual(recent.tolist(), [23581, 4703, 2637, 3077])       # the feasibility counts of the spec
        free = m.compute_free()
        self.assertEqual(list(free["summary"]["main"]["papers_by_n_ins"].values()), [23581, 4703, 2637, 3077])
        self.assertEqual(free["summary"]["main"]["familiar_equals_frame_incumbent"], 1.0)
        self.assertEqual(int(free["free_role_grid_main"].filter(like="last_").to_numpy().sum()),
                         int((e[k.year.to_numpy()[key] >= 2023].team >= 2).sum()))

    def test_design_columns(self):
        d = m.population(ph5_common.simulated_frame(0))
        self.assertTrue(d.year.between(*m.YEARS).all() and d.rq3.all() and d.hot.notna().all())
        self.assertTrue(((d.po + d.ui + d.pi) <= 1).all() and ((d.f_only + d.l_only + d.both) <= 1).all())
        self.assertTrue((d[m.TS].sum(axis=1) == (d.team >= 2)).all() and (d[m.EXP].sum(axis=1) == (d.n_exp >= 1)).all())
        np.testing.assert_array_equal(d.ui_x_hot, d.ui * d.hot)
        np.testing.assert_array_equal(d.n_cross + d.n_ins, d.n_exp)


class ContrastTargets(unittest.TestCase):
    """Each family contrast, evaluated on known acceptance probabilities (its expectation), measures what it claims."""

    @classmethod
    def setUpClass(cls):
        cls.d = m.population(ph5_common.simulated_frame(2))

    def targets(self, plant) -> pd.Series:
        d = self.d.assign(p_true=m.true_prob(self.d, plant))
        return m.family_table(m.fit_models(d, "p_true"), adjust=False).set_index("test").estimate

    def test_plants_load_on_the_intended_tests(self):
        t = self.targets(lambda d: 0.3 * (d.n_ins >= 1) * d.hot)         # insider threshold in hot topics only
        self.assertGreater(t.H3, 0.05)
        self.assertLess(abs(t.H6), 0.01)
        t = self.targets(lambda d: 0.3 * (d.first_type == 2))             # first-author insider
        self.assertLess(t.H6, -0.05)
        t = self.targets(lambda d: 0.3 * d.po)                           # proven outsider
        self.assertGreater(t.H4, 0.05)
        self.assertLess(t.H1, -0.03)                                     # T1's reference (no insider) holds them
        t = self.targets(lambda d: 0.3 * d.po * d.hot)                   # proven outsider, hot topics only
        self.assertGreater(t.H5, 0.05)

    def test_experience_and_team_size_are_held_fixed(self):
        for plant in (lambda d: 0.3 * (d.n_exp >= 1) + 0.15 * d.n_exp.clip(upper=m.EXP_CAP),
                      lambda d: 0.2 * np.log2(d.team.clip(upper=m.TS_CAP))):
            np.testing.assert_allclose(self.targets(plant).to_numpy(), 0.0, atol=2e-3)   # logit-scale plants: tiny
            # non-additivity with the year rate on the probability scale


class EndToEnd(unittest.TestCase):
    def test_compute_plot_and_calibrate(self):
        k = ph5_common.simulated_frame(7)
        res = m.compute(k, perms=10)
        fam = res["family"]
        self.assertEqual(fam.test.tolist(), list(m.FAMILY))
        self.assertTrue(fam.estimate.notna().all() and (fam.p_holm >= fam.p - 1e-12).all())
        self.assertTrue(fam.mde80.notna().all())
        self.assertEqual(res["robustness"].variant.nunique(), 6)
        self.assertEqual(set(res["curves"].n_ins), {0, 1, 2, 3})
        self.assertEqual(len(res["role_grid"]), 18)
        multi = m.population(k).query("team >= 2")                       # descriptive groups decode to the right papers
        raw = multi.groupby(["hot", "first_type", "last_type"]).accepted.mean()
        grid = res["role_grid"].assign(f=lambda x: x["first"].map(m.TYPES.index), l=lambda x: x["last"].map(m.TYPES.index))
        np.testing.assert_allclose(grid.raw_rate, [raw[(h, f, l)] for h, f, l in zip(grid.hot, grid.f, grid.l)])
        cur = res["curves"].set_index(["hot", "team", "n_ins"]).papers
        direct = multi.groupby([multi.hot, multi.team.clip(upper=m.TS_CAP), multi.n_ins.clip(upper=m.INS_CAP)]).size()
        self.assertEqual(cur.sort_index().tolist(), direct.sort_index().tolist())
        with mock.patch.object(m, "logit", side_effect=RuntimeError("logit did not converge")):
            rob = m.robustness(k, m.population(k))                       # a failing variant is reported, not fatal
        self.assertIn("did not converge", rob.set_index("variant").loc["logit (log-odds)", "error"])
        self.assertEqual(rob.variant.nunique(), 6)
        with tempfile.TemporaryDirectory() as tmp:
            posthoc.write_outputs(res, Path(tmp))
            self.assertIn("population", json.loads((Path(tmp) / "summary.json").read_text())["summary"])
            m.plot(Path(tmp))
            for name in ("teams_curves", "teams_proven_familiar", "teams_role_grid", "teams_family"):
                self.assertTrue((Path(tmp) / f"{name}.png").exists())
        cal = m.calibrate(1, 1, seed=11)
        per = pd.DataFrame(cal["per_test"]).set_index(["plant", "test"])
        self.assertAlmostEqual(per.loc[("null", "H1"), "mean_target"], 0.0, places=12)
        t1, t2 = per.loc[("threshold", "H1"), "mean_target"], per.loc[("threshold", "H2"), "mean_target"]
        self.assertGreater(t1, 0.04)
        self.assertAlmostEqual(t2, t1, delta=0.01)                          # a pure threshold: 2+ adds nothing
        self.assertGreater(per.loc[("last_author", "H6"), "mean_target"], 0.04)


if __name__ == "__main__":
    unittest.main()
