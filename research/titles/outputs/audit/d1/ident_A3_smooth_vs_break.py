"""Audit D1 / identification, check A (part 3): is a *dated* 2024 break distinguishable from a smooth acceleration?
Compare, on adjusted logit year effects with full sampling covariance (GLS, tau2 fixed at the REML value of the
segmented-2024 model and also tau2 = 0): segmented break at B in 2020..2025 vs a quadratic logit trend (same #params).
Also: does the 2024-break term survive once a quadratic trend is allowed?
"""
import json, sys, warnings
from pathlib import Path
import numpy as np
from scipy import stats
sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import _core as C
warnings.filterwarnings("ignore")
OUT = Path(__file__).resolve().parent
df = C.load_analysis_frame(feature_cols=["name_primary"], universe_cols=["submission_id", "year", "topic100", "log_authors", "llm_topic", "NA"])
for c in ["name_primary", "llm_topic", "NA"]:
    df[c] = df[c].astype(int)
YRS = np.arange(2017, 2027)
out = {}
for pop, d in [("U", df), ("NA", df[df.NA == 1])]:
    r = C.logit("name_primary ~ 0 + C(year) + log_authors + llm_topic + C(topic100)", d, cluster="topic100")
    names = [f"C(year)[{y}]" for y in YRS]
    y = r.params[names].to_numpy(); V = r.cov_params().loc[names, names].to_numpy()
    t = (YRS - 2023).astype(float)
    def gls(X, tau2):
        S = V + tau2 * np.eye(10); Si = np.linalg.inv(S)
        Vb = np.linalg.inv(X.T @ Si @ X); b = Vb @ X.T @ Si @ y; e = y - X @ b
        return b, Vb, float(e @ Si @ e)
    res = {}
    for tau in (0.0, 0.0441):
        rows = {}
        for B in range(2020, 2026):
            tb = YRS - (B - 1); post = (YRS >= B).astype(float)
            X = np.column_stack([np.ones(10), tb, post, post * tb])
            b, Vb, q = gls(X, tau ** 2)
            rows[f"seg{B}"] = {"Q": q, "slope_change": float(b[3]), "z": float(b[3] / np.sqrt(Vb[3, 3]))}
        Xq = np.column_stack([np.ones(10), t, t ** 2])
        b, Vb, q = gls(Xq, tau ** 2); rows["quadratic(3p)"] = {"Q": q, "quad": float(b[2]), "z": float(b[2] / np.sqrt(Vb[2, 2]))}
        Xk = np.column_stack([np.ones(10), t, np.maximum(t, 0)])
        b, Vb, q = gls(Xk, tau ** 2); rows["kink2024(3p)"] = {"Q": q, "kink": float(b[2]), "z": float(b[2] / np.sqrt(Vb[2, 2]))}
        Xqb = np.column_stack([np.ones(10), t, t ** 2, (YRS >= 2024) * t])
        b, Vb, q = gls(Xqb, tau ** 2); rows["quadratic + post*t"] = {"Q": q, "post_t": float(b[3]), "z_post_t": float(b[3] / np.sqrt(Vb[3, 3])), "quad": float(b[2]), "z_quad": float(b[2] / np.sqrt(Vb[2, 2]))}
        Xl = np.column_stack([np.ones(10), t])
        b, Vb, q = gls(Xl, tau ** 2); rows["linear(2p)"] = {"Q": q}
        res[f"tau={tau}"] = rows
    out[pop] = res
    for k, rows in res.items():
        print(pop, k)
        for m, v in rows.items():
            print("   ", m, {kk: round(vv, 3) for kk, vv in v.items()})
(OUT / "ident_A3_smooth_vs_break.json").write_text(json.dumps(out, indent=1))
