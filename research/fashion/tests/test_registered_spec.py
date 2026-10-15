"""The registered specification table, controls and variant definitions, hard-coded from PREREGISTRATION.md (RQ2/RQ3
sections, D7, D9, D12, R1, R2; review round B8). A change to any of them must fail here.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import rq2_following as rq2  # noqa: E402
import rq3_reward as rq3  # noqa: E402
import variants  # noqa: E402
from common import CLASSES  # noqa: E402


class RegisteredSpecs(unittest.TestCase):
    def test_table(self):
        got = {s.hid: (s.y, s.x, s.sign, s.sesoi, s.fe, s.years, s.gated) for s in rq2.SPECS + rq3.SPECS}
        self.assertEqual(got, {
            "H2a": ("incumbent", "hot", -1, 0.02, "topic+year", (2019, 2026), False),
            "H2b": ("method", "newcomer", -1, 0.02, "cell", (2019, 2026), False),
            "H2c": ("measurement", "newcomer", +1, 0.01, "cell", (2019, 2026), False),
            "H2d": ("buzzword", "newcomer", +1, 0.01, "cell", (2019, 2026), True),
            "H3a": ("accepted", "maturity", -1, 0.01, "topic+year", (2018, 2026), False),
            "H3b": ("accepted", "maturity_x_method", -1, 0.01, "topic+year", (2018, 2026), False),
            "H3c": ("accepted", "buzzword", -1, 0.02, "topic+year", (2019, 2026), True)})

    def test_controls(self):
        base = tuple(f"cls_{c}" for c in CLASSES if c != "method") + ("fm",)      # D7: reference class method
        self.assertIn("method", CLASSES)
        self.assertEqual({s.hid: tuple(s.controls) for s in rq3.SPECS},
                         {"H3a": base, "H3b": ("maturity",) + base, "H3c": base})
        self.assertEqual({s.hid: tuple(s.controls) for s in rq2.SPECS}, {h: () for h in ["H2a", "H2b", "H2c", "H2d"]})

    def test_variant_maps_estimators_and_lists(self):
        shared = ["k75", "k150", "balanced", "early", "early_prospective", "stable_papers", "coherent_topics",
                  "certain_labels", "without_2026"]
        self.assertEqual(list(variants.counted(2)), shared + ["id_consistent_years"])
        self.assertEqual(list(variants.counted(3)), shared + ["logit", "no_earlier_version"])
        maps = {k: v.map for k, v in {**variants.RQ2, **variants.RQ3}.items()}
        self.assertEqual(maps, {"k75": "k75", "k150": "k150", "balanced": "balanced", "early": "early",
                                "early_prospective": "early", "stable_papers": "k100", "coherent_topics": "k100",
                                "certain_labels": "k100", "without_2026": "k100", "id_consistent_years": "k100",
                                "logit": "k100", "no_earlier_version": "k100"})
        self.assertEqual({k: v.estimator for k, v in variants.RQ3.items() if v.estimator != "ols"}, {"logit": "logit"})
        self.assertEqual(variants.MAIN, variants.Variant("k100"))

    def test_variant_filters(self):
        d = pd.DataFrame({"year": range(2017, 2027), "has_earlier_version": [0.0, 1.0] * 5,
                          "stable": [True, False] * 5, "mixed_topic": [False, False, True] * 3 + [False],
                          "uncertain": [False] * 9 + [True]})
        keep = lambda v: variants.apply(d, v).year.tolist()
        self.assertEqual(keep(variants.RQ2["id_consistent_years"]), [2019, 2020, 2023, 2024, 2025, 2026])
        self.assertEqual(keep(variants.RQ3["no_earlier_version"]), [2017, 2019, 2021, 2023, 2025])
        self.assertEqual(keep(variants.SHARED["early_prospective"]), list(range(2021, 2027)))
        self.assertEqual(keep(variants.SHARED["without_2026"]), list(range(2017, 2026)))
        self.assertEqual(keep(variants.SHARED["stable_papers"]), [2017, 2019, 2021, 2023, 2025])
        self.assertEqual(keep(variants.SHARED["coherent_topics"]), [2017, 2018, 2020, 2021, 2023, 2024, 2026])
        self.assertEqual(keep(variants.SHARED["certain_labels"]), list(range(2017, 2026)))
        for k in ["k75", "k150", "balanced", "early"]:
            self.assertEqual(keep(variants.SHARED[k]), list(range(2017, 2027)))

    def test_populations(self):
        d = pd.DataFrame({"has_author_key": [True, False, True], "x": [1, 2, 3]})
        self.assertEqual(rq2.population(d).x.tolist(), [1, 3])                 # D2: papers with an author key


if __name__ == "__main__":
    unittest.main()
