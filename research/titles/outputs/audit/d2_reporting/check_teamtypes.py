"""Audit check: per-team-type NAME change under the rolling / fixed / lag-1 definitions, with a simple
paper bootstrap CI (clustered on last-position key, as in D2-12), and the all-prior ratio under each definition.
Also: H2c(i) one-sided p against the *predicted* boundary (ratio >= 0.5)."""
import numpy as np
import pandas as pd
from scipy import stats

D = "/home/user/cloud-research/research/titles/outputs/d2_carriers/"
P = pd.read_parquet(D + "panel_papers.parquet")
R = pd.read_parquet(D + "panel_rows.parquet")
last_key = R[R.is_last].set_index("submission_id").key
P["clu"] = P.submission_id.map(last_key).fillna(P.submission_id)

rng = np.random.default_rng(7)


def contrast(df, E, L, col):
    d = df[df.year.isin(E + L) & df[col].notna()].copy()
    d["L"] = d.year.isin(L)
    out = {}
    pop = d[d.L].name_primary.mean() - d[~d.L].name_primary.mean()
    for t in ["all_prior", "mixed", "all_new"]:
        a = d[d[col] == t]
        out[t] = (a[~a.L].name_primary.mean(), a[a.L].name_primary.mean(), len(a[~a.L]), len(a[a.L]))
    return pop, out


def boot(df, E, L, col, B=500):
    d = df[df.year.isin(E + L) & df[col].notna()].copy()
    d["L"] = d.year.isin(L)
    cl = d.clu.astype("category").cat.codes.to_numpy()
    ncl = cl.max() + 1
    y = d.name_primary.to_numpy(float)
    isL = d.L.to_numpy()
    ap = (d[col] == "all_prior").to_numpy()
    res = []
    for _ in range(B):
        w = np.bincount(rng.integers(0, ncl, ncl), minlength=ncl)[cl].astype(float)
        pop = (w * y * isL).sum() / (w * isL).sum() - (w * y * ~isL).sum() / (w * ~isL).sum()
        a1 = (w * y * isL * ap).sum() / (w * isL * ap).sum()
        a0 = (w * y * ~isL * ap).sum() / (w * ~isL * ap).sum()
        res.append((a1 - a0, (a1 - a0) / pop))
    res = np.array(res)
    return np.quantile(res, [.025, .975], axis=0)


for col, E, L in [("team_roll", [2022, 2023], [2025, 2026]), ("team_fixed", [2023], [2025, 2026]),
                  ("team_lag1", [2022, 2023], [2025, 2026]), ("team_fixed", [2023], [2026])]:
    pop, out = contrast(P, E, L, col)
    ap = out["all_prior"]
    ci = boot(P, E, L, col)
    print(f"{col} E={E} L={L}: pop {pop:.4f}; all_prior {ap[0]:.3f}->{ap[1]:.3f} (n {ap[2]}->{ap[3]}) "
          f"change {ap[1]-ap[0]:+.4f} CI [{ci[0,0]:+.4f},{ci[1,0]:+.4f}]  ratio {(ap[1]-ap[0])/pop:.3f} "
          f"CI [{ci[0,1]:.3f},{ci[1,1]:.3f}]")
    for t in ["mixed", "all_new"]:
        o = out[t]
        print(f"     {t}: {o[0]:.3f}->{o[1]:.3f} (n {o[2]}->{o[3]}) change {o[1]-o[0]:+.4f}")

# H2c(i): p-value against the predicted boundary ratio >= 0.5
fe = pd.read_csv(D + "T2_2_author_fe.csv").iloc[0]
z = (fe.change_EtoL_at_share_new0 - 0.5 * fe.pop_change) / fe.se_change
print("H2c(i) z vs 0.5x boundary:", round(z, 3), "one-sided p(ratio >= 0.5):", stats.norm.cdf(z))
z3 = (fe.change_EtoL_at_share_new0 - 0.3 * fe.pop_change) / fe.se_change
print("H2c(i) z vs 0.3x falsification point:", round(z3, 3), "p(ratio <= 0.3):", stats.norm.sf(z3))
