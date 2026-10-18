"""PH5 confirmation (ph5_confirm.py): the one-sided rule and MDE interpolation against run_confirmation's, the pooled
frame and its outcome block, the planted contrasts' LPM targets, the out-of-sample premia statistics against direct
computation, the verdict rules, the pinned discovery premia file, and an end-to-end compute and calibrate on stand-in
data: the discovery frames (outcome-free features) with a random quarter of the papers as the pseudo-confirmation split
and simulated outcomes. No real outcome is read (outcomes.load and ph5_common.outcome_frame are patched to fail), the
committed discovery premia are replaced by a synthetic table, and the process never activates the pooled corpus.

    python -m unittest research/fashion/tests/test_ph5_confirm.py
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "tests"))

import common  # noqa: E402
import outcomes  # noqa: E402
import panel  # noqa: E402
import ph5_common  # noqa: E402
import ph5_confirm as m  # noqa: E402
import ph5_pivot  # noqa: E402
import ph5_position  # noqa: E402
import ph5_premia  # noqa: E402
import posthoc  # noqa: E402
import run_confirmation as rc  # noqa: E402
from test_ph5_position import fake_build  # noqa: E402


def stand_in(seed: int = 0, share: float = 0.25) -> tuple[dict[str, pd.DataFrame], np.ndarray]:
    """The discovery frames of every map filtered to a random share of the papers (the pseudo-confirmation split)."""
    pooled = {mp: panel.frame(mp) for mp in panel.MAPS}
    mask = np.random.default_rng(seed).random(len(pooled["k100"])) < share
    return rc.split_frames(pooled, mask), mask


def synthetic_windows(seed: int = 0) -> pd.DataFrame:
    """A stand-in for the committed discovery windows.csv on the real unit names (random premia)."""
    rng = np.random.default_rng(seed)
    rows = []
    for ut in ph5_premia.UNIT_TYPES:
        names = ph5_premia.unit_sets()[ut][0]
        pick = rng.choice(len(names), min(len(names), 60), replace=False)
        w1 = rng.normal(0, 0.04, len(pick))
        v1 = rng.uniform(0.0004, 0.002, len(pick))
        rows.append(pd.DataFrame({"unit_type": ut, "unit": np.array(names)[pick], "w1": w1, "v1": v1,
                                  "eb1": 0.5 * w1}))
    return pd.concat(rows, ignore_index=True)


class Rules(unittest.TestCase):
    def test_one_sided_and_mde80_are_run_confirmations(self):
        for p in (0.001, 0.04, 0.3, 0.9, np.nan):
            for coef in (-0.2, 0.0, 0.3, np.nan):
                for sign in (-1, 1):
                    a, b = m.one_sided(p, coef, sign), rc.one_sided(p, coef, sign)
                    self.assertTrue(a == b or (np.isnan(a) and np.isnan(b)), (p, coef, sign))
        for grid, power in [((0, 1, 2, 3), [0.05, 0.2, 0.6, 1.0]), ((1, 2), [0.9, 1.0]), ((1, 2), [0.1, 0.5])]:
            self.assertEqual(m.mde80(list(grid), power), rc.mde80(grid, power))
        self.assertEqual(m.SIGN["E1"], -1)
        self.assertEqual(m.SIGN["P1b"], -1)
        self.assertTrue(all(m.SIGN[t] == 1 for t in ("E4", "P7", "H1", "A1", "premia_b", "premia_eb")))

    def row(self, test: str, coef: float, p: float, **extra) -> dict:
        return {**m.verdict_row(test, {"coef": coef, "se": 0.01, "ci95_lo": coef - 0.02, "ci95_hi": coef + 0.02},
                                p, "test"), **extra}

    def test_holm_over_the_primary_pair_and_verdicts(self):
        rows = [self.row("E1", -0.05, 0.04), self.row("P1b", -0.03, 0.08), self.row("E4", 0.01, 0.02),
                self.row("P7", -0.01, 0.001), self.row("H1", 0.02, np.nan),
                self.row("A1", 0.03, 0.01, p_null_frames_one_sided=0.2),
                {**self.row("premia_b", 0.4, 0.001), "p": 0.01}, {**self.row("premia_eb", 0.002, 0.04), "p": 0.02}]
        t = m.decide(rows).set_index("test")
        p1 = {"E1": 0.02, "P1b": 0.04}
        self.assertAlmostEqual(t.loc["E1", "p"], p1["E1"])
        self.assertAlmostEqual(t.loc["E1", "p_holm"], 0.04)                  # Holm: 2 x 0.02, then max(0.04, 0.04)
        self.assertAlmostEqual(t.loc["P1b", "p_holm"], 0.04)
        self.assertEqual(list(t.loc[["E1", "P1b"], "verdict"]), ["supported", "supported"])
        self.assertTrue(t.loc[["E4", "P7", "H1", "A1"], "p_holm"].isna().all())  # no family for the secondary tests
        self.assertEqual(t.loc["E4", "verdict"], "supported")
        self.assertEqual(t.loc["P7", "verdict"], "not supported")              # wrong sign: p1 = 1 - p / 2
        self.assertAlmostEqual(t.loc["P7", "p"], 1 - 0.0005)
        self.assertEqual(t.loc["H1", "verdict"], "not estimable")
        self.assertEqual(t.loc["A1", "verdict"], "not supported")              # the null-frame p must also be < 0.05
        self.assertEqual(t.loc["premia_b", "verdict"], "supported")
        self.assertEqual(t.loc["premia_eb", "verdict"], "supported")
        rows[-2] = {**self.row("premia_b", 1.3, 0.001), "p": 0.01}
        rows[0] = self.row("E1", 0.05, 0.001)
        t = m.decide(rows).set_index("test")
        self.assertEqual(t.loc["premia_b", "verdict"], "not supported")        # b must lie in (0, 1)
        self.assertEqual(t.loc["E1", "verdict"], "not supported")
        self.assertAlmostEqual(t.loc["E1", "p"], 1 - 0.0005)

    def test_registration_is_complete(self):
        r = m.REGISTERED
        self.assertEqual(r["primary"]["tests"], ["E1", "P1b"])
        self.assertEqual(set(r["secondary"]) - {"family"}, {"E4", "P7", "H1", "A1", "premia_b", "premia_eb"})
        self.assertIn(m.DISCOVERY_WINDOWS_SHA256, json.dumps(r))
        self.assertEqual(json.loads(json.dumps(r)), r)
        for t in m.SIGN:
            self.assertIn(t, m.__doc__.replace("premia out of sample", "premia_b premia_eb"))


class PooledFrame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.frames, cls.mask = stand_in(1)
        k = cls.frames["k100"]
        cls.out = ph5_common.fake_outcomes(k, 3)

    def test_outcome_block_only_on_the_confirmation_papers(self):
        k, mask = m.pooled_frame(self.frames["k100"], self.out, check_split=False)
        np.testing.assert_array_equal(mask, self.mask)
        self.assertEqual(len(k), len(panel.frame("k100")))
        self.assertFalse(k.rq3[~mask].any() or k.s9[~mask].any() or k.e3[~mask].any())
        self.assertTrue(k.accepted[~mask].isna().all())
        np.testing.assert_array_equal(k.rq3[mask].to_numpy(), self.out.rq3.to_numpy())
        np.testing.assert_array_equal(k.accepted[mask].to_numpy(), self.out.accepted.to_numpy())
        self.assertNotIn("accepted", m.free(k))

    def test_misaligned_or_reordered_input_is_refused(self):
        k = self.frames["k100"]
        with self.assertRaises(SystemExit):
            m.pooled_frame(k, self.out.iloc[::-1].reset_index(drop=True), check_split=False)
        with self.assertRaises(SystemExit):
            m.pooled_frame(k.iloc[::-1], self.out.iloc[::-1], check_split=False)

    def test_the_split_check_needs_the_pooled_corpus(self):
        with self.assertRaises(SystemExit):
            m.pooled_frame(self.frames["k100"], self.out)              # the discovery corpus has no split column


class Plants(unittest.TestCase):
    def test_e1_plant_is_the_registered_contrast(self):
        ref = ph5_pivot.REF["F_max"]
        f = np.array([ref["p10"], ref["p50"], np.nan, 0.5])
        kp = pd.DataFrame({"F_max": f})
        kq = pd.DataFrame({"pct": [0.1, 0.2, np.nan, 0.95]})
        u = m.unit_plants(kp, kq)
        np.testing.assert_allclose(u["E1"][:3], [1.0, 0.0, 0.0], atol=1e-12)
        np.testing.assert_array_equal(u["P1b"], [1.0, 0.0, 0.0, 0.0])

    def test_planted_probabilities_have_the_planted_lpm_target(self):
        """The same models on true probabilities = base(year) + delta x plant recover delta exactly (no clipping)."""
        rng = np.random.default_rng(0)
        n = 3000
        topic, year = rng.integers(0, 30, n), rng.integers(2023, 2027, n)
        d = pd.DataFrame({"submission_id": [f"p{i}" for i in range(n)], "topic": topic, "year": year,
                          "cell": [f"{t}:{y}" for t, y in zip(topic, year)], "hot": ((topic + year) % 3 == 0) * 1.0,
                          "F_max": rng.uniform(-0.2, 0.9, n), "pct": rng.random(n),
                          "newcomer": (rng.random(n) < 0.4) * 1.0, "maturity_tercile": "young"})
        for c in set(ph5_pivot.CONTROLS) | set(ph5_position.CONTROLS):
            if c not in d:
                d[c] = rng.normal(size=n) if c in ("log2_team", "log_prior_team") else (rng.random(n) < 0.2) * 1.0
        d[f"twins_{ph5_position.tag(ph5_position.TAU)}"] = rng.poisson(0.5, n)
        d[f"sibling_{ph5_position.tag(ph5_position.TAU)}"] = (rng.random(n) < 0.05) * 1.0
        u = m.unit_plants(d, d)
        base = m.base_rate(d.year.to_numpy())
        e1 = ph5_pivot.p1(ph5_pivot.design(d.assign(accepted=base - 0.054 * u["E1"])))[0]["E1"]["coef"]
        self.assertAlmostEqual(e1, -0.054, places=8)
        dq = ph5_position.design(d.assign(accepted=base - 0.033 * u["P1b"]))
        p1b = ph5_position.Fit(dq, "accepted", ph5_position.xs("Q0")).lincom({"q1": 1.0})["coef"]
        self.assertAlmostEqual(p1b, -0.033, places=8)


class Premia(unittest.TestCase):
    def test_statistics_against_direct_computation(self):
        rng = np.random.default_rng(4)
        U = 80
        true = rng.normal(0, 0.05, U)
        vx, vy = rng.uniform(0.0005, 0.003, U), rng.uniform(0.002, 0.01, U)
        x = true + rng.normal(0, np.sqrt(vx))
        y = 0.6 * true + rng.normal(0, np.sqrt(vy))
        eb = 0.4 * x
        r = m.premia_stats(x, vx, eb, y, vy, np.random.default_rng(0), boot=99)
        ty = max(ph5_premia.dl(y[:, None], vy[:, None], np.ones((U, 1), bool), np.ones((1, U)))[0][0, 0], 0.0)
        w = 1 / (vy + ty)
        X = np.column_stack([np.ones(U), x])
        beta = np.linalg.solve(X.T @ (X * w[:, None]), X.T @ (w * y))
        self.assertAlmostEqual(r["b"], beta[1], places=10)
        self.assertAlmostEqual(r["p_iut"], max(r["p_b_gt_0"], r["p_b_lt_1"]))
        from scipy import stats
        self.assertAlmostEqual(r["p_b_gt_0"], stats.t.sf(r["b"] / r["b_se"], U - 2))
        yc = y - (y / vy).sum() / (1 / vy).sum()
        d = (yc - x) ** 2 - (yc - eb) ** 2
        self.assertAlmostEqual(r["D"], d.mean(), places=12)
        self.assertAlmostEqual(r["mse_raw"] - r["mse_eb"], r["D"], places=12)
        tt = stats.ttest_1samp(d, 0.0, alternative="greater")
        self.assertAlmostEqual(r["D_p_one_sided"], tt.pvalue, places=10)
        self.assertLessEqual(r["D_boot_ci95"][0], r["D_boot_ci95"][1])
        d0 = yc ** 2 - (yc - eb) ** 2                                   # the registered EB test: against the prediction 0
        self.assertAlmostEqual(r["D0"], d0.mean(), places=12)
        self.assertAlmostEqual(r["mse_zero"] - r["mse_eb"], r["D0"], places=12)
        self.assertAlmostEqual(r["D0_p_one_sided"], stats.ttest_1samp(d0, 0.0, alternative="greater").pvalue, places=10)
        self.assertLessEqual(r["D0_boot_ci95"][0], r["D0_boot_ci95"][1])
        self.assertEqual(len(r["retention"]), 4)
        few = m.premia_stats(x[:3], vx[:3], eb[:3], y[:3], vy[:3], np.random.default_rng(0), boot=9)
        self.assertIn("not estimable", few["note"])

    def test_eb_test_cannot_pass_without_persistence(self):
        """Confirmation premia unrelated to the discovery premia: the descriptive D (raw vs EB) favours shrinkage almost
        always, the registered D0 (EB vs 0) almost never passes (E[D0] = -E[eb^2] < 0); with persistence D0 passes."""
        rng = np.random.default_rng(11)
        U, reps, d_pass, d0_pass, d0_signal = 82, 200, 0, 0, 0
        for _ in range(reps):
            true = rng.normal(0, 0.04, U)
            vx, vy = rng.uniform(0.0005, 0.002, U), rng.uniform(0.0005, 0.002, U)
            x = true + rng.normal(0, np.sqrt(vx))
            eb = x * 0.04 ** 2 / (0.04 ** 2 + vx)
            for y, persist in [(rng.normal(0, 0.04, U) + rng.normal(0, np.sqrt(vy)), False),
                               (true + rng.normal(0, np.sqrt(vy)), True)]:
                r = m.premia_stats(x, vx, eb, y, vy, np.random.default_rng(0), boot=9)
                if persist:
                    d0_signal += r["D0_p_one_sided"] < 0.05
                else:
                    d_pass += r["D_p_one_sided"] < 0.05
                    d0_pass += r["D0_p_one_sided"] < 0.05
        self.assertGreater(d_pass / reps, 0.5)                          # why D is descriptive only
        self.assertLess(d0_pass / reps, 0.025)
        self.assertGreater(d0_signal / reps, 0.5)

    def test_discovery_premia_file_is_pinned(self):
        with tempfile.TemporaryDirectory() as tmp:
            fake = Path(tmp) / "windows.csv"
            fake.write_text("unit_type,unit,w1,v1,eb1\nearly,early_1,0.1,0.001,0.05\n")
            with mock.patch.object(m, "DISCOVERY_WINDOWS", fake), self.assertRaises(SystemExit):
                m.discovery_windows()
        self.assertTrue(str(m.DISCOVERY_WINDOWS).endswith("output/posthoc/ph5_premia/windows.csv"))


class EndToEnd(unittest.TestCase):
    """compute and calibrate on the stand-in split with simulated outcomes; the real outcome loaders are patched to fail,
    the position features are the synthetic fake_build (as in test_ph5_position) and the discovery premia synthetic."""

    @classmethod
    def setUpClass(cls):
        cls.fb = fake_build()
        cls.frames, cls.mask = stand_in(2)
        cls.out = rc.simulated_outcomes(cls.frames["k100"], 7)
        cls.windows = synthetic_windows()
        with cls.patches():
            cls.res = m.compute(cls.frames, cls.out, nulls=5, n_ref=4, boot=19, check_split=False)

    @classmethod
    def patches(cls) -> ExitStack:
        es = ExitStack()
        for obj, name, kw in [(ph5_position, "build", {"new": lambda: cls.fb}),
                              (m, "discovery_windows", {"new": lambda: cls.windows}),
                              (outcomes, "load", {"side_effect": AssertionError("outcomes read")}),
                              (ph5_common, "outcome_frame", {"side_effect": AssertionError("outcomes read")})]:
            es.enter_context(mock.patch.object(obj, name, **kw))
        return es

    def test_registered_rows(self):
        t = self.res["tests"]
        self.assertEqual(list(t.test), ["E1", "P1b", "E4", "P7", "H1", "A1", "premia_b", "premia_eb"])
        self.assertEqual(list(t.family), ["primary"] * 2 + ["secondary"] * 6)
        self.assertTrue(t.verdict.isin(["supported", "not supported", "not estimable"]).all())
        self.assertTrue(np.isfinite(t.coef).all() and t.p.between(0, 1).all(), t[["test", "coef", "p", "note"]])
        prim = t[t.family == "primary"]
        self.assertTrue((prim.p_holm >= prim.p - 1e-12).all() and t.p_holm[t.family == "secondary"].isna().all())
        for r in t.itertuples():
            if r.test not in ("premia_b", "premia_eb"):
                self.assertAlmostEqual(r.p, m.one_sided(r.p_two_sided, r.coef, r.predicted_sign))
        p7 = t.set_index("test").loc["P7"]
        self.assertAlmostEqual(p7.p_two_sided, max(p7.p_cr1, p7.p_twoway, p7.p_calibrated))
        e1 = t.set_index("test").loc["E1"]                              # E1: max(CR1, calibrated from 5 nulls here)
        self.assertTrue(np.isfinite(e1.p_calibrated) and 1 / 6 <= e1.p_calibrated <= 1)
        self.assertAlmostEqual(e1.p_two_sided, max(e1.p_cr1, e1.p_calibrated))
        piv = self.res["pivot"].set_index("test")
        self.assertEqual(int(piv.loc["E1", "null_frames"]), 5)
        self.assertAlmostEqual(piv.loc["E1", "p_used"], e1.p_two_sided)
        eb = t.set_index("test").loc["premia_eb"]                        # the registered EB test is D0 (vs 0)
        prem = self.res["premia"].set_index("unit_type").loc[m.REGISTERED_UNIT]
        self.assertAlmostEqual(eb.coef, prem.D0)
        self.assertAlmostEqual(eb.p, prem.D0_p_one_sided)
        self.assertAlmostEqual(eb.D_raw_minus_eb_descriptive, prem.D)

    def test_populations_are_the_confirmation_papers(self):
        conf = set(self.frames["k100"].submission_id)
        piv, pos = self.res["pivot"], self.res["position"]
        self.assertEqual(list(piv.test), ["E1", "E2", "E3", "E4"])
        self.assertEqual(list(piv.confirmation_test), ["E1", m.NOT_REGISTERED, m.NOT_REGISTERED, "E4"])
        self.assertEqual(sorted(set(pos.confirmation_test)), sorted({"P1b", "P7", m.NOT_REGISTERED}))
        s = self.res["summary"]
        decided = self.out.rq3.to_numpy() & self.frames["k100"].year.between(2019, 2026).to_numpy()
        self.assertEqual(s["populations"]["position"]["papers"], int(decided.sum()))
        self.assertEqual(s["decided_confirmation_papers"], int(self.out.rq3.sum()))
        self.assertEqual(s["confirmation_papers"], len(conf))
        e1 = self.res["tests"].set_index("test").loc["E1"]
        decided_late = self.out.rq3.to_numpy() & self.frames["k100"].year.between(2023, 2026).to_numpy()
        self.assertLessEqual(e1.n, int(decided_late.sum()))
        u = self.res["premia_units"]
        self.assertTrue(set(u.unit_type) <= set(ph5_premia.UNIT_TYPES))
        self.assertTrue((u.papers_w2[u.used] >= ph5_premia.MIN_CELL).all() and u.used.any())

    def test_outputs_are_written_and_json_clean(self):
        with tempfile.TemporaryDirectory() as tmp:
            posthoc.write_outputs(self.res, Path(tmp))
            names = {p.name for p in Path(tmp).iterdir()}
            self.assertTrue({"tests.csv", "pivot.csv", "position.csv", "teams.csv", "kwtiming.csv", "premia.csv",
                             "premia_units.csv", "premia_retention.csv", "summary.json"} <= names)
            text = (Path(tmp) / "summary.json").read_text()
        s = json.loads(text)["summary"]
        self.assertEqual(s["registered"], m.REGISTERED)
        self.assertEqual(len(s["lines"]), 8)
        self.assertNotIn("NaN", text)

    def test_calibrate_targets_and_structure(self):
        with self.patches():
            cal = m.calibrate(nulls=3, reps=2, mults=(1.0, 3.0), mask=self.mask)
        per = pd.DataFrame(cal["per_test"])
        self.assertEqual(sorted(set(zip(per.test, per.mult))), sorted((h, x) for h in m.PRIMARY for x in (0.0, 1.0, 3.0)))
        p = per.set_index(["test", "mult"])
        self.assertAlmostEqual(p.loc[("P1b", 0.0), "mean_target"], 0.0, places=10)
        self.assertAlmostEqual(p.loc[("P1b", 3.0), "mean_target"], 3 * m.DISCOVERY_EFFECT["P1b"], places=8)
        self.assertAlmostEqual(p.loc[("E1", 1.0), "mean_target"], m.DISCOVERY_EFFECT["E1"], places=3)
        self.assertEqual(set(cal["mde80"]), set(m.PRIMARY))
        self.assertTrue(0 <= cal["family_any_holm_null"] <= 1)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "calibration.json"
            path.write_text(json.dumps(cal))
            with mock.patch.object(m, "CALIBRATION", path), mock.patch.object(common, "ROOT", Path(tmp)):
                rec = m.calibration_record()
        self.assertEqual(rec["mde80"], cal["mde80"])


class Wiring(unittest.TestCase):
    def test_the_hook_finds_the_module_and_the_corpus_is_untouched(self):
        self.assertTrue(rc.ph5_available())
        self.assertEqual(common.CORPUS, "discovery")
        self.assertNotIn(common.DISCOVERY_OUTPUT, m.CALIBRATION.parents)
        self.assertIn(common.POOLED_OUTPUT, m.CALIBRATION.parents)


if __name__ == "__main__":
    unittest.main()
