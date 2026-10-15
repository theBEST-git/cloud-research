"""Real outcomes and real RQ2 labels are reachable only through a frozen run_frozen.py (PREREGISTRATION.md D13).

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

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
            exploratory.run({}, pd.DataFrame())

    def test_unknown_mode_rejected(self):
        with self.assertRaises(ValueError):
            outcomes.load("peek", pd.Series(["x"]))


if __name__ == "__main__":
    unittest.main()
