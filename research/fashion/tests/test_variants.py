"""The shared variant registry reproduces the finished RQ1 run's sample sizes (variants.py, rq1_rise.py).

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import panel  # noqa: E402
import variants  # noqa: E402


class RegistryReproducesRQ1(unittest.TestCase):
    def test_rq1_sample_sizes(self):
        rq1 = pd.read_csv(HERE / "output" / "rq1_results.csv")
        names = {"main": variants.MAIN, **variants.SHARED}
        names["years_2018_2025"] = names.pop("without_2026")
        for name, v in names.items():
            d = variants.apply(panel.frame(v.map), v)
            d = d[(d.year >= 2018) & (d.year <= 2026)]
            for h, outcome in [("H1a", "method"), ("H1d", "model")]:
                row = rq1[(rq1.variant == name) & (rq1.hypothesis == h)].iloc[0]
                n = int(d.dropna(subset=["fm_adoption"] if h == "H1d" else ["maturity"]).shape[0])
                self.assertEqual(n, row.n, f"{name} {h}")
                self.assertEqual(row["map"], v.map)

    def test_counted_lists_are_as_registered(self):
        shared = ["k75", "k150", "balanced", "early", "early_prospective", "stable_papers", "coherent_topics",
                  "certain_labels", "without_2026"]
        self.assertEqual(list(variants.counted(2)), shared + ["id_consistent_years"])
        self.assertEqual(list(variants.counted(3)), shared + ["logit", "no_earlier_version"])
        self.assertEqual(variants.HINDSIGHT_VARIANTS, ("balanced", "early_prospective"))
        self.assertEqual(variants.ROBUST_SHARE, 0.75)


if __name__ == "__main__":
    unittest.main()
