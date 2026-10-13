"""Twin feasibility, step 2: stratified labelling sample (decisions and titles are never exported).

Strata: masked-cosine band (5) x era (2018-23, 2024, 2025, 2026); 16 clean candidate pairs per
stratum (all if fewer). Controls: the ICLR 2023 flow-matching trio (3 known positives) and 16 random
same-year, same-topic100 non-candidate pairs (expected negatives). Items are shuffled, A/B order is
randomised, and only name-masked abstracts are shown. Writes outputs/twins_feas/pilot_items.jsonl
(labeller view) and pilot_key.parquet (stratum, weights, controls).
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from analyses import _core as C

OUT = C.OUT / "twins_feas"
BANDS = [0.86, 0.88, 0.90, 0.92, 0.94, 1.01]
PER = 16
CHUNKS = 8
TRIO = ["Flow Matching for Generative Modeling",
        "Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow",
        "Building Normalizing Flows with Stochastic Interpolants"]


def era(y):
    return "2018-23" if y <= 2023 else str(y)


def main():
    rng = np.random.default_rng(20261013)
    df = C.load_analysis_frame(feature_cols=["name_primary"],
                               universe_cols=["submission_id", "year", "title", "topic100", "pool"]).reset_index(drop=True)
    M = pd.read_parquet(C.TOPIC_DIR / "masked_abstracts.parquet")[["submission_id", "masked"]]
    masked = dict(zip(M.submission_id, M.masked))
    P = pd.read_parquet(OUT / "candidates.parquet")
    P["clean2"] = (P.key_ov == 0) & (P.name_ov == 0) & ~P.title_dup & ~P.dr_or_other  # same-cycle pairs cannot be resubmission links
    c = P[P.clean2 & P.cos_masked.notna()].copy()
    c["band"] = pd.cut(c.cos_masked, BANDS, right=False).astype(str)
    c["era"] = c.year.map(era)
    pop = c.groupby(["band", "era"]).size().rename("N_stratum")
    picks = []
    for (b, e), g in c.groupby(["band", "era"]):
        k = min(PER, len(g))
        picks.append(g.sample(k, random_state=int(rng.integers(1e9))))
    S = pd.concat(picks)
    S = S.merge(pop, left_on=["band", "era"], right_index=True)
    S["kind"] = "candidate"
    # known positives
    ix = [int(df.index[(df.title == t) & (df.year == 2023)][0]) for t in TRIO]
    trio = pd.DataFrame([(2023, min(a, b), max(a, b)) for k, a in enumerate(ix) for b in ix[k + 1:]], columns=["year", "i", "j"])
    trio["kind"] = "known_positive"
    # random same-topic negatives (not in candidate set)
    cand = set(zip(P.i, P.j))
    neg = []
    while len(neg) < 16:
        y = int(rng.choice(range(2019, 2027)))
        idx = np.where(df.year.to_numpy() == y)[0]
        a = int(rng.choice(idx))
        same = idx[(df.topic100.to_numpy()[idx] == df.topic100[a]) & (idx != a)]
        if len(same) == 0:
            continue
        b = int(rng.choice(same))
        p = (min(a, b), max(a, b))
        if p not in cand and df.submission_id[a] in masked and df.submission_id[b] in masked:
            neg.append((y, *p))
    neg = pd.DataFrame(neg, columns=["year", "i", "j"])
    neg["kind"] = "random_same_topic"
    K = pd.concat([S, trio, neg], ignore_index=True)
    sid = df.submission_id.to_numpy()
    K["sid_i"], K["sid_j"] = sid[K.i], sid[K.j]
    K = K.sample(frac=1, random_state=7).reset_index(drop=True)
    K["item_id"] = [f"p{n:03d}" for n in range(len(K))]
    K["swap"] = rng.random(len(K)) < 0.5
    K["chunk"] = np.arange(len(K)) % CHUNKS
    K.drop(columns=[c for c in ["clean", "clean2"] if c in K.columns]).to_parquet(OUT / "pilot_key.parquet")
    for ch in range(CHUNKS):
        with open(OUT / f"pilot_items_chunk{ch}.jsonl", "w") as f:
            for _, r in K[K.chunk == ch].iterrows():
                a, b = (r.sid_j, r.sid_i) if r.swap else (r.sid_i, r.sid_j)
                f.write(json.dumps({"item_id": r.item_id, "abstract_A": masked[a], "abstract_B": masked[b]}) + "\n")
    print(K.kind.value_counts().to_dict())
    print(K[K.kind == "candidate"].groupby(["band", "era"]).size().unstack(fill_value=0))
    print(pop.unstack(fill_value=0))


if __name__ == "__main__":
    main()
