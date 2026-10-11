"""Audit D1 / identification, check A (part 2): random-effects meta-regression of the segmented break on annual
year effects, using the full sampling covariance of the covariate-adjusted year effects plus a year-shock variance tau^2
(REML). This is the minimum-distance analogue of the paper-level ITS that also admits cohort-level shocks.
Also: the same on the LPM scale (pp), and on the NA pool.
"""
import json
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import optimize, stats

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import _core as C  # noqa: E402

warnings.filterwarnings("ignore")
OUT = Path(__file__).resolve().parent
df = C.load_analysis_frame(feature_cols=["name_primary"],
                           universe_cols=["submission_id", "year", "topic100", "log_authors", "llm_topic", "NA"])
for c in ["name_primary", "llm_topic", "NA"]:
    df[c] = df[c].astype(int)
YRS = np.arange(2017, 2027)


def design(B=2024):
    t = YRS - (B - 1)
    post = (YRS >= B).astype(float)
    return np.column_stack([np.ones(10), t, post, post * t]).astype(float)


def reml(y, V, X):
    """REML for y ~ N(X b, V + tau2 I). Returns tau2, b, cov(b)."""
    def negll(lt):
        tau2 = np.exp(lt)
        S = V + tau2 * np.eye(len(y))
        Si = np.linalg.inv(S)
        XtSiX = X.T @ Si @ X
        b = np.linalg.solve(XtSiX, X.T @ Si @ y)
        r = y - X @ b
        return 0.5 * (np.linalg.slogdet(S)[1] + np.linalg.slogdet(XtSiX)[1] + r @ Si @ r)
    opt = optimize.minimize_scalar(negll, bounds=(-20, 2), method="bounded")
    tau2 = float(np.exp(opt.x))
    S = V + tau2 * np.eye(len(y))
    Si = np.linalg.inv(S)
    Vb = np.linalg.inv(X.T @ Si @ X)
    b = Vb @ X.T @ Si @ y
    # fixed-effect (tau2 = 0) for comparison
    Si0 = np.linalg.inv(V)
    Vb0 = np.linalg.inv(X.T @ Si0 @ X)
    b0 = Vb0 @ X.T @ Si0 @ y
    return tau2, b, Vb, b0, Vb0


def summarise(y, V, label, scale="logit"):
    X = design()
    tau2, b, Vb, b0, Vb0 = reml(y, V, X)
    dfree = 6
    se, se0 = np.sqrt(Vb[3, 3]), np.sqrt(Vb0[3, 3])
    out = {"label": label, "scale": scale, "tau_year_shock": float(np.sqrt(tau2)),
           "slope_change_RE": float(b[3]), "se_RE": float(se), "t_RE": float(b[3] / se),
           "p_one_sided_RE_t6": float(stats.t.sf(b[3] / se, dfree)),
           "p_one_sided_RE_z": float(stats.norm.sf(b[3] / se)),
           "slope_change_FE_tau0": float(b0[3]), "se_FE_tau0": float(se0), "z_FE_tau0": float(b0[3] / se0)}
    if scale == "logit":
        out["OR_RE"] = float(np.exp(b[3]))
        out["OR_RE_lo95_t6"] = float(np.exp(b[3] - stats.t.ppf(.975, dfree) * se))
        out["OR_RE_hi95_t6"] = float(np.exp(b[3] + stats.t.ppf(.975, dfree) * se))
        out["OR_FE_tau0"] = float(np.exp(b0[3]))
    else:
        out["pp_RE_lo95_t6"] = float(100 * (b[3] - stats.t.ppf(.975, dfree) * se))
        out["pp_RE_hi95_t6"] = float(100 * (b[3] + stats.t.ppf(.975, dfree) * se))
    return out


res = {}
for pop, d in [("U", df), ("NA", df[df.NA == 1])]:
    # logit, adjusted (controls + topic100 FE), full year intercepts
    r = C.logit("name_primary ~ 0 + C(year) + log_authors + llm_topic + C(topic100)", d, cluster="topic100")
    names = [f"C(year)[{y}]" for y in YRS]
    y = r.params[names].to_numpy()
    V = r.cov_params().loc[names, names].to_numpy()
    res[f"{pop}|logit_adj"] = summarise(y, V, f"{pop}: adjusted logit year effects (controls + topic100 FE)")
    # logit raw (no covariates): independent binomial sampling variance
    g = d.groupby("year").name_primary.agg(["mean", "size"]).reindex(YRS)
    yr = np.log(g["mean"] / (1 - g["mean"])).to_numpy()
    Vr = np.diag(1 / (g["size"] * g["mean"] * (1 - g["mean"])).to_numpy())
    res[f"{pop}|logit_raw"] = summarise(yr, Vr, f"{pop}: raw logit shares")
    # LPM adjusted (pp scale)
    dd = d.copy()
    yd = pd.get_dummies(dd.year).astype(float)
    yd.columns = [f"y{c}" for c in yd.columns]
    dd = pd.concat([dd, yd], axis=1)
    fr = C.feols(dd, "name_primary", list(yd.columns[1:]) + ["log_authors", "llm_topic"], fe=["topic100"],
                 cluster="topic100")
    ylpm = np.array([0.0] + [fr.params[c] for c in yd.columns[1:]])
    Vl = np.zeros((10, 10))
    Vl[1:, 1:] = fr.vcov.loc[list(yd.columns[1:]), list(yd.columns[1:])].to_numpy()
    # reference-year (2017) sampling variance enters every contrast: add it as a common component
    s17 = d.loc[d.year == 2017, "name_primary"].mean()
    Vl[0, 0] = s17 * (1 - s17) / (d.year == 2017).sum()
    res[f"{pop}|lpm_adj"] = summarise(ylpm, Vl, f"{pop}: adjusted LPM year effects (pp)", scale="pp")
for k, v in res.items():
    print(k, {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()})
(OUT / "ident_A2_re_metareg.json").write_text(json.dumps(res, indent=1))
