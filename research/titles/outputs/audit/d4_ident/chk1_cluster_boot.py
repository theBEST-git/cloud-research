"""D4 identification audit, check 1: does H4b (L-union G_total < 1) and H4a TOST survive cluster-aware inference?

The D4 bootstrap resamples papers iid within year. Papers sharing a topic (topic100) or a last-position key share
acceptance shocks and style, so paper-iid CIs can be too narrow. Here: same year-standardised pooled gains for
2024-26, with (a) the original paper bootstrap (reproduction), (b) a topic100-cluster bootstrap (topics resampled
with all their 2024-26 papers), (c) a last-position-key cluster bootstrap (papers without a key are singletons).
Run: cd research/titles/src && OMP_NUM_THREADS=1 python -m analyses... (run as a file with PYTHONPATH=src)
"""
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import d4_stage_gains as S  # noqa: E402
from analyses import d4_exit_composition as E  # noqa: E402

B = 2000
rng = np.random.default_rng(7)
df = S.load_frame(min_year=2018, density=True)
df = df[df.year.isin(S.POST)].reset_index(drop=True)
lk = E.last_keys(set(df.submission_id))
df = df.merge(lk, on="submission_id", how="left", validate="1:1")
df["key_cl"] = df.key_last.fillna("solo_" + df.submission_id)

feats = {"NAME": "name_primary", "L_union": "L_union", "O_union": "O_union", "F24": "f24", "R24": "r24_any",
         "style_density": "xs_per100", "L_abstract": "L_abstract", "L_title": "L_title"}
stages = ["s0", "s1", "s2", "s3", "s1n", "s2n", "s0n"]
gdefs = {"total": ("s3", "s0"), "predec": ("s2", "s0"), "predec_crf": ("s2n", "s0n"), "dec": ("s3", "s2")}
years = list(S.POST)
w_year = np.array([(df.year == y).sum() for y in years], float)
w_year /= w_year.sum()

X = df[list(feats.values())].to_numpy(float)
St = df[stages].to_numpy(float)
F, K = X.shape[1], St.shape[1]
V = np.concatenate([St, (X[:, :, None] * St[:, None, :]).reshape(len(df), -1)], axis=1)  # n x (K + F*K)
Ycodes = np.array([years.index(y) for y in df.year])


def gains_from_cluster_sums(Csum, cl_year_codes, weights):
    """Csum: (G, 3 years, K+F*K) cluster x year sums; weights: (B, G). Returns dict gain -> (B, F)."""
    out = {}
    tot = np.einsum("bg,gyk->byk", weights, Csum)  # (B, Y, K+FK)
    N = tot[:, :, :K]
    Ssum = tot[:, :, K:].reshape(tot.shape[0], len(years), F, K)
    P = Ssum / N[:, :, None, :]
    Pp = np.einsum("y,byfk->bfk", w_year, P)
    for g, (a, b) in gdefs.items():
        out[g] = Pp[:, :, stages.index(a)] / Pp[:, :, stages.index(b)]
    return out


def run(cluster_col, label, stratify_year):
    if cluster_col is None:
        codes = np.arange(len(df))
    else:
        codes = pd.factorize(df[cluster_col])[0]
    G = codes.max() + 1
    Csum = np.zeros((G, len(years), V.shape[1]))
    np.add.at(Csum, (codes, Ycodes), V)
    res = []
    point = gains_from_cluster_sums(Csum, None, np.ones((1, G)))
    reps = {g: [] for g in gdefs}
    if stratify_year and cluster_col is None:
        # paper bootstrap stratified by year (original design)
        for _ in range(B // 200):
            W = np.zeros((200, G))
            for yi in range(len(years)):
                idx = np.where(Ycodes == yi)[0]
                draws = rng.integers(0, len(idx), size=(200, len(idx)))
                for b in range(200):
                    W[b] += np.bincount(idx[draws[b]], minlength=G)
            o = gains_from_cluster_sums(Csum, None, W)
            for g in gdefs:
                reps[g].append(o[g])
    else:
        for _ in range(B // 200):
            W = rng.multinomial(G, np.full(G, 1 / G), size=200).astype(float)
            o = gains_from_cluster_sums(Csum, None, W)
            for g in gdefs:
                reps[g].append(o[g])
    for g in gdefs:
        R = np.vstack(reps[g])
        for j, k in enumerate(feats):
            r = R[:, j]
            r = r[np.isfinite(r)]
            res.append(dict(boot=label, n_clusters=G, gain=g, feature=k, est=point[g][0, j],
                            lo95=np.quantile(r, .025), hi95=np.quantile(r, .975), lo90=np.quantile(r, .05),
                            hi90=np.quantile(r, .95), p_ge1=np.mean(r >= 1), se=np.std(r, ddof=1)))
    return res


rows = []
rows += run(None, "paper (year-stratified, original)", True)
rows += run("topic100", "topic100 cluster", False)
rows += run("key_cl", "last-position key cluster", False)
out = pd.DataFrame(rows)
out.to_csv("/home/user/cloud-research/research/titles/outputs/audit/d4_ident/chk1_cluster_boot.csv", index=False)
pd.set_option("display.width", 200)
show = out[out.gain.isin(["total", "predec", "predec_crf"])].copy()
print(show.round(4).to_string())
