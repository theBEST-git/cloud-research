"""Real outcomes and real RQ2 labels are reachable only through a frozen run_frozen.py (PREREGISTRATION.md D13).

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import analysis  # noqa: E402
import exploratory  # noqa: E402
import outcomes  # noqa: E402
import rq2_following  # noqa: E402


class Guard(unittest.TestCase):
    def test_real_outcomes_refused_outside_run_frozen(self):
        with self.assertRaises(PermissionError):
            outcomes.load("real", pd.Series(["x"]))

    def test_real_rq2_labels_refused_without_simulated_outcomes(self):
        with self.assertRaises(PermissionError):
            rq2_following.run({}, gate=False)

    def test_exploratory_refused_without_simulated_outcomes(self):
        with self.assertRaises(PermissionError):
            exploratory.run({}, pd.DataFrame(), gate=False)

    def test_partial_or_empty_simulated_outcomes_refused(self):
        for ys in [{}, {"method": pd.Series(dtype=float)}, {c: pd.Series(dtype=float) for c in
                                                             rq2_following.SIMULATED - {"lists_hot"}}]:
            with self.assertRaises(ValueError):
                rq2_following.run({}, gate=False, ys=ys)
            with self.assertRaises(ValueError):
                exploratory.run({}, pd.DataFrame(), gate=False, ys=ys)

    def test_simulated_run_derives_newcomer_from_simulated_incumbency(self):
        f = pd.DataFrame({"submission_id": ["a", "b", "c"], "has_author_key": [True, True, False],
                          "incumbent": [1.0, 1.0, np.nan], "incumbent_w2": [1.0, 0.0, np.nan], "incumbent_s4": [1.0, 1.0, np.nan],
                          "newcomer": [0.0, 0.0, np.nan], "newcomer_w2": [0.0, 1.0, np.nan], "newcomer_s4": [0.0, 0.0, np.nan],
                          "n_eligible_keywords": [0, 1, 2]})
        sim = {c: pd.Series([0.0, 1.0, 1.0], index=["a", "b", "c"]) for c in rq2_following.SIMULATED}
        g = rq2_following.with_columns(f, sim)
        self.assertEqual(g.newcomer.tolist()[:2], [1.0, 0.0])
        self.assertEqual(g.newcomer_w2.tolist()[:2], [1.0, 0.0])
        self.assertEqual(g.newcomer_s4.tolist()[:2], [1.0, 0.0])
        self.assertTrue(np.isnan(g.newcomer.iloc[2]))                        # no author key: never a newcomer

    def test_estimates_carry_no_means_unless_asked(self):
        rng = np.random.default_rng(0)
        d = pd.DataFrame({"y": rng.random(400) < 0.3, "x": rng.random(400) < 0.5, "topic": rng.integers(0, 20, 400),
                          "year": rng.integers(2019, 2023, 400)}).astype({"y": float, "x": float})
        self.assertNotIn("regressor_mean", analysis.estimate(d, "y", "x"))
        self.assertIn("regressor_mean", analysis.estimate(d, "y", "x", describe=True))

    def test_posthoc_outcomes_refused_outside_posthoc_py(self):
        with self.assertRaises(PermissionError):
            outcomes.load("posthoc", pd.Series(["x"]))

    def test_posthoc_outcomes_refused_before_the_frozen_run_finished(self):
        import json, sys, tempfile
        from pathlib import Path
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "attempts.jsonl"
            with mock.patch.object(sys.modules["__main__"], "__file__", str(outcomes.POSTHOC), create=True), \
                    mock.patch.object(outcomes, "ATTEMPTS", log), \
                    mock.patch.object(outcomes, "POSTHOC_LOG", Path(tmp) / "access.jsonl"):
                for lines in [[], [{"attempt": 1, "status": "started"}], [{"attempt": 1, "status": "failed"}]]:
                    log.write_text("".join(json.dumps(x) + "\n" for x in lines))
                    with self.assertRaises(PermissionError) as e:
                        outcomes.require_posthoc()
                    self.assertIn("frozen run has finished", str(e.exception))
                self.assertFalse((Path(tmp) / "access.jsonl").exists())

    def test_unknown_mode_rejected(self):
        with self.assertRaises(ValueError):
            outcomes.load("peek", pd.Series(["x"]))


if __name__ == "__main__":
    unittest.main()
