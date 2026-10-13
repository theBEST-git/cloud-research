"""Claims codebook pilot: stratified sample of title+abstract items (decisions never exported).

Strata: title form (assertive verb phrase / question / NAME-colon / other) x era (2017-21, 2022-24,
2025-26). Assertive titles are oversampled. Writes outputs/claims_pilot/round{R}_items_chunk{c}.jsonl
and round{R}_key.parquet. Items already used in earlier rounds are excluded.

Run: cd research/titles/src && /home/user/venv/bin/python -m claims.sample_pilot ROUND N
"""
from __future__ import annotations

import json
import re
import sys

import numpy as np
import pandas as pd

from analyses import _core as C

OUT = C.OUT / "claims_pilot"
ASSERT = re.compile(r"\b(is|are|was|were|can|cannot|can't|could|will|does|do|did|doesn't|don't|isn't|aren't|improves?|outperforms?|beats?|solves?|enables?|matters?|helps?|hurts?|needs?|makes?|yields?|leads?|works?|fails?|suffices?|reveals?|shows?|proves?|guarantees?|achieves?|boosts?|surpasses?)\b", re.I)
SHARE = {"assertive": 0.40, "question": 0.10, "name_colon": 0.25, "other": 0.25}


def era(y):
    return "2017-21" if y <= 2021 else ("2022-24" if y <= 2024 else "2025-26")


def main(rnd: int, n: int, chunks: int = 2):
    rng = np.random.default_rng(1000 + rnd)
    df = C.load_analysis_frame(feature_cols=["question", "name_primary"],
                               universe_cols=["submission_id", "year", "title", "abstract"]).reset_index(drop=True)
    used = set()
    for r in range(1, rnd):
        p = OUT / f"round{r}_key.parquet"
        if p.exists():
            used |= set(pd.read_parquet(p).submission_id)
    df = df[~df.submission_id.isin(used)].copy()
    df["form"] = np.select([df.question.astype(bool), df.title.map(lambda t: bool(ASSERT.search(t))), df.name_primary.astype(bool)],
                           ["question", "assertive", "name_colon"], "other")
    df["era"] = df.year.map(era)
    picks = []
    for form, share in SHARE.items():
        k = int(round(n * share))
        per_era = np.diff(np.round(np.linspace(0, k, 4)).astype(int))
        for e, ke in zip(["2017-21", "2022-24", "2025-26"], per_era):
            g = df[(df.form == form) & (df.era == e)]
            picks.append(g.sample(min(ke, len(g)), random_state=int(rng.integers(1e9))))
    S = pd.concat(picks).sample(frac=1, random_state=int(rng.integers(1e9))).reset_index(drop=True)
    S["item_id"] = [f"r{rnd}_{i:03d}" for i in range(len(S))]
    S["chunk"] = np.arange(len(S)) % chunks
    S[["item_id", "submission_id", "year", "form", "era", "chunk"]].to_parquet(OUT / f"round{rnd}_key.parquet")
    for c in range(chunks):
        with open(OUT / f"round{rnd}_items_chunk{c}.jsonl", "w") as f:
            for _, r in S[S.chunk == c].iterrows():
                f.write(json.dumps({"item_id": r.item_id, "title": r.title, "abstract": r.abstract}) + "\n")
    print(S.groupby(["form", "era"]).size().unstack(fill_value=0))


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
