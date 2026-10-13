"""Choose the 300-paper check set for prompt v1.1 (fixed before any v1.1 labels exist).

- all 200 double-labelled training papers (two annotators, disagreements adjudicated): the best reference we have
- 100 single-labelled random-stratum training papers from 2024-2026, where named frameworks/agents and
  foundation-model papers concentrate (the boundaries v1.1 clarifies)
None of these papers were looked at when the v1.1 clarifications were written (those came from the pilot 300).
Writes check_300.csv (reference labels) in a shuffled order so batches mix strata.

    python research/topics/annotation/contribution_types/llm_labeling/prepare_check_set.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SEED, EXTRA_N = 43, 100


def main() -> None:
    t = pd.read_csv(HERE.parent / "training" / "training_labels.csv")
    double = t[t.source != "single"]
    pool = t[(t.source == "single") & (t.stratum == "random") & (t.year >= 2024)]
    extra = pool.sample(n=EXTRA_N, random_state=SEED)
    check = pd.concat([double.assign(check_part="double_labelled"), extra.assign(check_part="single_2024_2026")])
    check = check.sample(frac=1, random_state=SEED).reset_index(drop=True)
    assert len(check) == 300 and check.submission_id.is_unique
    cols = ["submission_id", "year", "stratum", "check_part", "source", "primary_type", "secondary_type", "foundation_model", "primary_class"]
    check[cols].to_csv(HERE / "check_300.csv", index=False)
    print(check.check_part.value_counts().to_dict(), check.primary_class.value_counts().to_dict(),
          "FM yes", int((check.foundation_model == "yes").sum()))


if __name__ == "__main__":
    main()
