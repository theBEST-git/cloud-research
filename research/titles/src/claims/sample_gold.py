"""Human gold set for the claims study: 200 fresh items in 4 blocks of 50, each block stratified the
same way (title form x era; assertive titles oversampled), excluding every pilot-round item.
Inclusion probabilities are recorded per stratum for design-based (PPI/DSL) correction.
Decisions are never read or exported.

Run: cd research/titles/src && /home/user/venv/bin/python -m claims.sample_gold
Writes outputs/claims_pilot/gold_key.parquet and gold_items.json (labeller view).
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from analyses import _core as C
from claims.sample_pilot import ASSERT, era

OUT = C.OUT / "claims_pilot"
BLOCKS, PER = 4, 50
ALLOC = {"assertive": 20, "name_colon": 13, "other": 12, "question": 5}  # per block of 50


def main():
    rng = np.random.default_rng(20261014)
    df = C.load_analysis_frame(feature_cols=["question", "name_primary"],
                               universe_cols=["submission_id", "year", "title", "abstract"]).reset_index(drop=True)
    used = set()
    for r in (1, 2, 3):
        used |= set(pd.read_parquet(OUT / f"round{r}_key.parquet").submission_id)
    df["form"] = np.select([df.question.astype(bool), df.title.map(lambda t: bool(ASSERT.search(t))), df.name_primary.astype(bool)],
                           ["question", "assertive", "name_colon"], "other")
    df["era"] = df.year.map(era)
    N = df.groupby(["form", "era"]).size().rename("N_stratum")
    pool = df[~df.submission_id.isin(used)].copy()
    picks = []
    for b in range(BLOCKS):
        for form, k in ALLOC.items():
            per_era = np.diff(np.round(np.linspace(0, k, 4)).astype(int))
            for e, ke in zip(["2017-21", "2022-24", "2025-26"], per_era):
                g = pool[(pool.form == form) & (pool.era == e)]
                s = g.sample(min(ke, len(g)), random_state=int(rng.integers(1e9)))
                s = s.assign(block=b + 1)
                picks.append(s)
                pool = pool.drop(s.index)
    S = pd.concat(picks)
    S = pd.concat([g.sample(frac=1, random_state=int(rng.integers(1e9))) for _, g in S.groupby("block")]).reset_index(drop=True)
    S["item_id"] = [f"g_{i + 1:03d}" for i in range(len(S))]
    n = S.groupby(["form", "era"]).size().rename("n_stratum")
    S = S.merge(N, left_on=["form", "era"], right_index=True).merge(n, left_on=["form", "era"], right_index=True)
    S["incl_prob"] = S.n_stratum / S.N_stratum
    S[["item_id", "submission_id", "year", "form", "era", "block", "N_stratum", "n_stratum", "incl_prob"]].to_parquet(OUT / "gold_key.parquet")
    items = [{"id": r.item_id, "block": int(r.block), "title": r.title, "abstract": r.abstract} for r in S.itertuples()]
    json.dump(items, open(OUT / "gold_items.json", "w"), ensure_ascii=False)
    print(S.groupby(["block", "form"]).size().unstack(fill_value=0))
    print("items", len(items), "chars", sum(len(i["abstract"]) + len(i["title"]) for i in items))


if __name__ == "__main__":
    main()
