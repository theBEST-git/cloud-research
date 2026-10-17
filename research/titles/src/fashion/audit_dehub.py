"""Audit: neighbourhood density on de-hubbed (centred) embeddings.

bge embeddings are anisotropic, so raw cos >= 0.80 counts partly measure how generic/central an abstract is (hub1 =
mean cos to all t-1 papers has corr 0.75 with size_p). For each year t, subtract the mean embedding of t-1..t-2
(look-ahead free), renormalise query and reference vectors, and count neighbours above a per-year threshold chosen
so that the mean t-1 count equals the raw cos >= 0.80 mean count. Same threshold for t-2. Discovery data only.
Writes outputs/fashion/explore/audit/loc_dehub.parquet (c1_c, c2_c, nn_c = max centred cos to t-1..t-2).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from analyses import _core as C
from fashion.frame import _norm

OUT = C.OUT / "fashion" / "explore" / "audit"


def main():
    f = pd.read_parquet(C.OUT / "fashion" / "frame2.parquet")[["submission_id", "year", "emb_row"]]
    v = pd.read_parquet(OUT / "loc_variants.parquet")[["submission_id", "c1_80"]]
    f = f.merge(v, on="submission_id", how="left")
    Em, found = C.load_masked_embedding(f)
    Ea = C.load_embedding(f, "abstract", "bge-small-en-v1.5")
    E = _norm(np.where(found[:, None], Em, Ea))
    yr = f.year.to_numpy()
    n = len(f)
    c1c, c2c, nnc = np.full(n, np.nan), np.full(n, np.nan), np.full(n, np.nan)
    rng = np.random.default_rng(0)
    for t in range(2019, 2027):
        qi, p1, p2 = np.where(yr == t)[0], np.where(yr == t - 1)[0], np.where(yr == t - 2)[0]
        mu = E[np.concatenate([p1, p2])].mean(0)
        Q, R1, R2 = _norm(E[qi] - mu), _norm(E[p1] - mu), _norm(E[p2] - mu)
        # calibrate threshold on a subsample: mean count of t-1 neighbours = raw mean c1_80
        target = np.nanmean(f.c1_80.to_numpy()[qi])
        sub = rng.choice(len(qi), min(2000, len(qi)), replace=False)
        S = Q[sub] @ R1.T
        k = int(round(target * len(sub)))
        tau = np.partition(S.ravel(), -k)[-k]
        a1, a2, mx = np.zeros(len(qi)), np.zeros(len(qi)), np.full(len(qi), -1.0)
        for s in range(0, len(qi), 2000):
            S1 = Q[s:s + 2000] @ R1.T
            S2 = Q[s:s + 2000] @ R2.T
            a1[s:s + 2000] = (S1 >= tau).sum(1)
            a2[s:s + 2000] = (S2 >= tau).sum(1)
            mx[s:s + 2000] = np.maximum(S1.max(1), S2.max(1))
        c1c[qi], c2c[qi], nnc[qi] = a1, a2, mx
        r = np.corrcoef(a1, f.c1_80.to_numpy()[qi])[0, 1]
        print(t, f"tau_c={tau:.3f}", f"corr(c1_c, c1_80)={r:.3f}", flush=True)
    out = pd.DataFrame({"submission_id": f.submission_id, "year": yr, "c1_c": c1c, "c2_c": c2c, "nn_c": nnc})
    out[out.year >= 2019].to_parquet(OUT / "loc_dehub.parquet")


if __name__ == "__main__":
    main()
