"""Variant registry shared by RQ1-RQ3 (PREREGISTRATION.md "Robustness variants", D9, R1, R2).

A variant is (map, sample filter, estimator). Filters apply after all variables are built on the full corpus (D9).
The counted lists are fixed here before the real run; tests/test_variants.py checks that the RQ1 variants reproduce
the sample sizes of the finished RQ1 run.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import pandas as pd

from rq1_rise import HINDSIGHT_VARIANTS, ROBUST_SHARE, holm  # noqa: F401  (re-exported: the RQ1 rule, unchanged)

Filter = Callable[[pd.DataFrame], pd.Series]


@dataclass(frozen=True)
class Variant:
    map: str
    keep: Filter | None = None
    estimator: str = "ols"


MAIN = Variant("k100")
SHARED = {   # the nine counted variants shared by RQ1, RQ2 and RQ3 (RQ1 names its last one years_2018_2025)
    "k75": Variant("k75"),
    "k150": Variant("k150"),
    "balanced": Variant("balanced"),
    "early": Variant("early"),
    "early_prospective": Variant("early", lambda d: d.year >= 2021),
    "stable_papers": Variant("k100", lambda d: d.stable),
    "coherent_topics": Variant("k100", lambda d: ~d.mixed_topic),
    "certain_labels": Variant("k100", lambda d: ~d.uncertain),
    "without_2026": Variant("k100", lambda d: d.year <= 2025),
}
RQ2 = {**SHARED, "id_consistent_years": Variant("k100", lambda d: d.year.isin([2019, 2020, 2023, 2024, 2025, 2026]))}  # R2
RQ3 = {**SHARED, "logit": Variant("k100", None, "logit"),
       "no_earlier_version": Variant("k100", lambda d: d.has_earlier_version == 0)}                                  # R1


def counted(rq: int) -> dict[str, Variant]:
    return {2: RQ2, 3: RQ3}[rq]


def apply(df: pd.DataFrame, v: Variant) -> pd.DataFrame:
    return df if v.keep is None else df[v.keep(df).astype(bool)]
