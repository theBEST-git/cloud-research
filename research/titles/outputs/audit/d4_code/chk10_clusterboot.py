"""Topic100-cluster (and last-key-cluster) bootstrap of the pooled 2024-26 year-standardised L-union / NAME G_total,
vs the paper bootstrap used in d4_stage_gains."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d4_stage_gains as S
from analyses import d4_exit_composition as E
df = S.load_frame(density=False)
df = df[df.year.isin(S.POST)].reset_index(drop=True)
lk = E.last_keys(set(df.submission_id))
df = df.merge(lk, on="submission_id", how="left", validate="1:1")
df["key_cl"] = df.key_last.fillna("solo_" + df.submission_id)
feats = ["L_union", "name_primary", "O_union", "r24_any"]
X = df[feats].to_numpy(float); St = df[["s0", "s3", "s2"]].to_numpy(float)
yrs = df.year.to_numpy()
w_y = np.array([(yrs == y).sum() for y in S.POST], float); w_y /= w_y.sum()
def gains(W):  # W: (b, n)
    out = []
    P = {}
    for y in S.POST:
        m = yrs == y
        Wy = W[:, m]
        N = Wy @ St[m]                      # (b, 3)
        Sx = np.einsum("bn,nf,ns->bfs", Wy, X[m], St[m])
        P[y] = Sx / N[:, None, :]
    Pp = sum(wi * P[y] for wi, y in zip(w_y, S.POST))
    return Pp[:, :, 1] / Pp[:, :, 0], Pp[:, :, 2] / Pp[:, :, 0]   # total, predec
B = 1000
for lab, kw in [("paper (by year)", dict(strata=yrs)), ("topic100 cluster", dict(clusters=df.topic100.to_numpy())),
                ("last-key cluster", dict(clusters=df.key_cl.to_numpy()))]:
    tot, pre = [], []
    for W in C.boot_weights(len(df), B, seed=7, **kw):
        t, p = gains(W.astype(float)); tot.append(t); pre.append(p)
    tot, pre = np.vstack(tot), np.vstack(pre)
    t0, p0 = gains(np.ones((1, len(df))))
    for j, f in enumerate(feats):
        print(f"{lab:18s} {f:12s} total {t0[0, j]:.4f} [{np.quantile(tot[:, j], .025):.4f}, {np.quantile(tot[:, j], .975):.4f}] p(G>=1)={np.mean(tot[:, j] >= 1):.3f} | predec {p0[0, j]:.4f} [{np.quantile(pre[:, j], .025):.4f}, {np.quantile(pre[:, j], .975):.4f}]")
