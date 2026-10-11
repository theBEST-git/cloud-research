"""WP4 fixer check: recompute key final numbers with plain pandas from outputs/snapshot/audit_pairs.csv and the
tipping table (independent of snapshot_bounds.flip_table / tipping_table)."""
import numpy as np, pandas as pd
from scipy import stats
O = "/home/user/cloud-research/research/titles/outputs/snapshot/"
P = pd.read_csv(O + "audit_pairs.csv")
tp = pd.read_csv(O + "T4_2_tipping_points.csv").set_index("feature")
print("pairs", P.decision.value_counts().to_dict(), "years", sorted(P.year.unique()))
for k in ["NAME", "O_union_arxiv", "sentence_case", "compound"]:
    a, r = P[P.acc == 1], P[P.acc == 0]
    na, nr = a[f"{k}_or"] - a[f"{k}_v1"], r[f"{k}_or"] - r[f"{k}_v1"]
    did = na.mean() - nr.mean()
    se_w = np.sqrt(na.var(ddof=1) / len(na) + nr.var(ddof=1) / len(nr))
    print(f"{k}: DiD {100*did:+.3f} pp (plain Wald se {100*se_w:.3f}); table {tp.loc[k, 'did_pp']:+.3f}; "
          f"adds/drops acc {((a[f'{k}_v1']==0)&(a[f'{k}_or']==1)).sum()}/{((a[f'{k}_v1']==1)&(a[f'{k}_or']==0)).sum()} "
          f"rej {((r[f'{k}_v1']==0)&(r[f'{k}_or']==1)).sum()}/{((r[f'{k}_v1']==1)&(r[f'{k}_or']==0)).sum()}")
# tipping point and G at D-hat
nm = tp.loc["NAME"]
tip = (nm.P_s3 - nm.P_s2) / (1 - nm.acc_share_s2)
D = nm.did_pp / 100
print(f"NAME tip {100*tip:.3f} (table {nm.tip_dec_pp:.3f}); G(D) {(nm.P_s3 - D)/(nm.P_s2 - nm.acc_share_s2*D):.4f} "
      f"(table {nm.G_dec_sel_point:.4f}); excess share {( nm.G_dec_obs - (nm.P_s3 - D)/(nm.P_s2 - nm.acc_share_s2*D))/(nm.G_dec_obs-1):.3f}")
# Holm across auditable features
aud = tp[tp.auditable].sort_values("p_ident_dec")
m = len(aud)
adj = np.maximum.accumulate(np.minimum(1, (m - np.arange(m)) * aud.p_ident_dec.to_numpy()))
print("Holm check max abs diff", float(np.max(np.abs(adj - aud.p_holm_dec.to_numpy()))), "m", m)
# O-union identification p by hand
r = tp.loc["O_union_arxiv"]
se = (r.did_hi_pp - r.did_lo_pp) / (2 * 1.959964)
z = -(r.tip_dec_pp - r.did_pp) / np.hypot(se, r.tip_dec_se_pp)
print(f"O_union_arxiv p {stats.norm.sf(z):.4f} (table {r.p_ident_dec:.4f}); draw-based {r.p_ident_draw_dec:.4f}")
# retitling by timing
for lab, q in [("in review", P[P.v1_in_review == 1]), ("before deadline", P[P.v1_in_review == 0])]:
    print(lab, q.groupby("decision").changed_norm.agg(["mean", "size"]).round(4).to_dict())
