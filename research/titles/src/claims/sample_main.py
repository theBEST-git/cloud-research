"""Main claims sample (pre-registered): simple random sample of 400 submissions per year 2017-2026
(all of 2017's 384), excluding every item already labelled in pilots and the gold set. A random
1,000-item subset (stratified by year, 100 per year) is flagged for the ChatGPT robustness pass.
Decisions are never read. Weights = N_year / n_year.

Run: cd research/titles/src && /home/user/venv/bin/python -m claims.sample_main
Writes outputs/claims_main/sample.parquet and sample_items.jsonl (labeller view).
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from analyses import _core as C

PILOT = C.OUT / "claims_pilot"
OUT = C.OUT / "claims_main"
PER_YEAR, SUB_PER_YEAR, SEED = 400, 100, 20261013


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    df = C.load_analysis_frame(feature_cols=["name_primary"], universe_cols=["submission_id", "year", "title", "abstract"]).reset_index(drop=True)
    used = set(pd.read_parquet(PILOT / "gold_key.parquet").submission_id)
    for r in (1, 2, 3):
        used |= set(pd.read_parquet(PILOT / f"round{r}_key.parquet").submission_id)
    N = df.groupby("year").size().rename("N_year")
    picks = []
    for y, g in df[~df.submission_id.isin(used)].groupby("year"):
        s = g.sample(min(PER_YEAR, len(g)), random_state=int(rng.integers(1e9)))
        sub = s.sample(min(SUB_PER_YEAR, len(s)), random_state=int(rng.integers(1e9))).submission_id
        picks.append(s.assign(gpt_subset=s.submission_id.isin(sub)))
    S = pd.concat(picks).sample(frac=1, random_state=SEED).reset_index(drop=True)
    S["item_id"] = [f"m_{i + 1:04d}" for i in range(len(S))]
    n = S.groupby("year").size().rename("n_year")
    S = S.merge(N, left_on="year", right_index=True).merge(n, left_on="year", right_index=True)
    S["weight"] = S.N_year / S.n_year
    S[["item_id", "submission_id", "year", "gpt_subset", "N_year", "n_year", "weight"]].to_parquet(OUT / "sample.parquet")
    with open(OUT / "sample_items.jsonl", "w") as f:
        for r in S.itertuples():
            f.write(json.dumps({"item_id": r.item_id, "title": r.title, "abstract": r.abstract}, ensure_ascii=False) + "\n")
    print(S.groupby("year").agg(n=("item_id", "size"), gpt=("gpt_subset", "sum"), N=("N_year", "first")))
    print("total", len(S), "gpt subset", int(S.gpt_subset.sum()), "excluded already-labelled", len(used))


if __name__ == "__main__":
    main()
