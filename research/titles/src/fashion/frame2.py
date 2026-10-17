"""Look-ahead-free topic heat (adds columns to outputs/fashion/frame.parquet -> frame2.parquet).

The fixed topic100 clusters were fitted on all years, so a topic that only became big later is visible as a
cluster from the start (survivorship). Here every heat measure for a paper of year t uses only papers of t-1, t-2:

- Rolling topics: KMeans(k=50) fitted on the name-masked bge embeddings of years t-2..t-1 only; papers of t-2, t-1
  and t are assigned to these centroids. r_share1 / r_share2 = topic share in t-1 / t-2, r_mom = log growth,
  r_size_pct = percentile of r_share1 among the 50 topics, stage_roll = same rule as stage_ex_ante.
- Cluster-free neighbourhood ("sub-field") heat, threshold cos >= 0.80 (median ~45 neighbours per prior year):
  loc1 / loc2 = neighbours per 1,000 submissions in t-1 / t-2, loc_mom = log((c1+1)/N1) - log((c2+1)/N2),
  stage_loc = same rule on (loc1 percentile, loc_mom tercile).
- nn_prev = cosine to the single closest paper of t-1..t-2 (closest predecessor; high = near-duplicate idea).
- loc_cur = same-year neighbours per 1,000 (concurrent competition, ex post), loc_next = neighbours in t+1 per
  1,000 (did the area keep growing after you? ex post, descriptive only).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

from analyses import _core as C
from fashion.frame import _norm

OUT = C.OUT / "fashion"
TAU = 0.80
K = 50


def stage(size_pct, mom_t):
    big, small = size_pct >= 2 / 3, size_pct < 1 / 3
    rising, falling = mom_t >= 2 / 3, mom_t < 1 / 3
    s = np.select([small & rising, ~big & rising, big & rising, big & ~rising & ~falling, falling],
                  ["emerging", "growing", "hot_rising", "mature", "declining"], "steady").astype(object)
    s[np.isnan(mom_t)] = None
    return s


def count_close(Q, R, tau=TAU, block=2000):
    out = np.zeros(len(Q), np.int32)
    mx = np.full(len(Q), np.nan, np.float32)
    if len(R) == 0:
        return out, mx
    for s in range(0, len(Q), block):
        S = Q[s:s + block] @ R.T
        out[s:s + block] = (S >= tau).sum(1)
        mx[s:s + block] = S.max(1)
    return out, mx


def main():
    f = pd.read_parquet(OUT / "frame.parquet")
    Em, found = C.load_masked_embedding(f)
    Ea = C.load_embedding(f, "abstract", "bge-small-en-v1.5")
    E = _norm(np.where(found[:, None], Em, Ea))
    yr = f.year.to_numpy()
    N = pd.Series(yr).value_counts().to_dict()
    n = len(f)
    cols = {c: np.full(n, np.nan) for c in ["r_share1", "r_share2", "r_mom", "r_size_pct", "loc1", "loc2", "loc_mom",
                                             "nn_prev", "loc_cur", "loc_next"]}
    r_topic = np.full(n, -1)
    for t in sorted(N):
        qi = np.where(yr == t)[0]
        p1, p2, nx = np.where(yr == t - 1)[0], np.where(yr == t - 2)[0], np.where(yr == t + 1)[0]
        c1, m1 = count_close(E[qi], E[p1])
        c2, m2 = count_close(E[qi], E[p2])
        cc, _ = count_close(E[qi], E[qi])
        if len(p1):
            cols["loc1"][qi] = 1000 * c1 / N[t - 1]
            cols["nn_prev"][qi] = np.fmax(m1, m2) if len(p2) else m1
        if len(p2):
            cols["loc2"][qi] = 1000 * c2 / N[t - 2]
            cols["loc_mom"][qi] = np.log((c1 + 1) / N[t - 1]) - np.log((c2 + 1) / N[t - 2])
        cols["loc_cur"][qi] = 1000 * (cc - 1) / N[t]
        if len(nx):
            cn, _ = count_close(E[qi], E[nx])
            cols["loc_next"][qi] = 1000 * cn / N[t + 1]
        if len(p1) and len(p2):
            fit = np.concatenate([p2, p1])
            km = KMeans(K, n_init=3, random_state=0).fit(E[fit])
            lab = {i: l for i, l in zip(fit, km.labels_)}
            lt = C.assign_centroids(E[qi], km.cluster_centers_)
            r_topic[qi] = lt
            s1 = np.bincount([lab[i] for i in p1], minlength=K) / len(p1)
            s2 = np.bincount([lab[i] for i in p2], minlength=K) / len(p2)
            cols["r_share1"][qi], cols["r_share2"][qi] = s1[lt], s2[lt]
            cols["r_mom"][qi] = np.log((s1[lt] + 1e-4) / (s2[lt] + 1e-4))
            cols["r_size_pct"][qi] = pd.Series(s1).rank(pct=True).to_numpy()[lt]
        print(t, len(qi), flush=True)
    for c, v in cols.items():
        f[c] = v
    f["r_topic"] = np.where(r_topic >= 0, f.year.astype(str) + "_" + pd.Series(r_topic).astype(str), None)
    rk = lambda c: f.groupby("year")[c].transform(lambda s: s.rank(pct=True)).to_numpy()
    f["stage_roll"] = stage(f.r_size_pct.to_numpy(), rk("r_mom"))
    f["stage_loc"] = stage(rk("loc1"), rk("loc_mom"))
    f.to_parquet(OUT / "frame2.parquet")
    print(f.stage_roll.value_counts(dropna=False), f.stage_loc.value_counts(dropna=False))
    print(f[["loc1", "loc2", "loc_mom", "nn_prev", "loc_cur", "loc_next", "r_mom"]].describe().T)


if __name__ == "__main__":
    main()
