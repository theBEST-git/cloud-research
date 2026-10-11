"""Audit D1-H1a: topic100-clustered Wald SEs ignore common year-level shocks (treatment varies only across 10 years).
Measure year-level overdispersion of the primary segmented logit: Pearson X2 of observed vs fitted yearly NAME counts
(fitted from the paper-level model incl. topic100 FE and controls) on 10 - 4 df, and the implied SE inflation."""
import sys, warnings
sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from scipy import stats
from analyses import d1_its as I
df = I.load()
out = {}
for lab, d in [("U", df), ("NA", df[df.NA == 1]), ("U excl 2026", df[df.year <= 2025])]:
    res = I.its_fit(d, "name_primary", 2024)
    dd = I._design(d, 2024).loc[res.model_rows]
    p = res.predict()
    g = pd.DataFrame({"year": dd.year.values, "y": dd.name_primary.values, "p": np.asarray(p), "v": np.asarray(p) * (1 - np.asarray(p))}).groupby("year").sum()
    X2 = float((((g.y - g.p) ** 2) / g.v).sum())
    dof = len(g) - 4
    phi = X2 / dof
    se = float(res.bse["post_t"]); b = float(res.params["post_t"])
    # year-level quasi-likelihood: inflate SE by sqrt(phi), t with dof
    se_q = se * np.sqrt(max(phi, 1))
    p_t = float(stats.t.sf(b / se_q, dof))
    out[lab] = dict(X2=X2, dof=dof, phi=phi, slopeOR=np.exp(b), se_cluster=se, se_inflated=se_q,
                    OR_lo_infl=np.exp(b - stats.t.ppf(.975, dof) * se_q), OR_hi_infl=np.exp(b + stats.t.ppf(.975, dof) * se_q),
                    p_one_sided_infl=p_t, p_one_sided_pipeline=float(stats.norm.sf(b / se)),
                    resid_pp_by_year=((g.y - g.p) / (g.v / g.p * 0 + dd.groupby("year").size()) * 100).round(2).to_dict())
for k, v in out.items():
    print(k, {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()})
pd.DataFrame(out).T.to_csv("/home/user/cloud-research/research/titles/outputs/audit/d1_code/its_yearshocks.csv")
