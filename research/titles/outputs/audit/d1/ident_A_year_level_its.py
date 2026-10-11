"""Audit D1 / identification lens, check A: small-T inference for the H1a slope break.

The reported H1a p (Wald, SE clustered by topic100) treats 43k papers as independent within topic clusters, but the
regressor of interest (post x t) varies only across 10 annual cohorts. Common year shocks (cohort-level deviations from
the trend) are not in the SE. Here:
  A1  year-level segmented regression on the 10 annual logit shares (raw and covariate-adjusted year effects), OLS and
      inverse-variance WLS, df = 6;
  A2  wild cluster bootstrap (Webb weights, clusters = years, restricted under H0) for the paper-level LPM slope change;
  A3  leave-one-year-out slope-change OR on the adjusted year effects;
  A4  how much of the slope change is 2026 alone (fit 2017-2025 trend + extrapolate).
Run: cd research/titles/src && OMP_NUM_THREADS=1 /home/user/venv/bin/python ../outputs/audit/d1/ident_A_year_level_its.py
"""
import json
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import _core as C  # noqa: E402

warnings.filterwarnings("ignore")
OUT = Path(__file__).resolve().parent
df = C.load_analysis_frame(feature_cols=["name_primary"],
                           universe_cols=["submission_id", "year", "topic100", "log_authors", "llm_topic", "NA"])
df["name_primary"] = df.name_primary.astype(int)
df["llm_topic"] = df.llm_topic.astype(int)
res = {}

# ---------- A1: raw year shares ----------
g = df.groupby("year").name_primary.agg(["mean", "size"]).rename(columns={"mean": "s", "size": "n"})
g["lg"] = np.log(g.s / (1 - g.s))
g["var_lg"] = 1 / (g.n * g.s * (1 - g.s))


def seg_ols(yv, years, w=None, B=2024):
    t = np.asarray(years) - (B - 1)
    post = (np.asarray(years) >= B).astype(float)
    X = np.column_stack([np.ones_like(t), t, post, post * t]).astype(float)
    m = sm.WLS(yv, X, weights=w).fit() if w is not None else sm.OLS(yv, X).fit()
    b, se = m.params[3], m.bse[3]
    dfree = m.df_resid
    return {"slope_change_logit": float(b), "OR": float(np.exp(b)), "se": float(se), "t": float(b / se),
            "df": int(dfree), "p_one_sided_t": float(stats.t.sf(b / se, dfree)),
            "OR_lo95": float(np.exp(b - stats.t.ppf(.975, dfree) * se)),
            "OR_hi95": float(np.exp(b + stats.t.ppf(.975, dfree) * se)),
            "level_logit": float(m.params[2]), "pre_slope_OR": float(np.exp(m.params[1]))}


res["A1_raw_OLS"] = seg_ols(g.lg.to_numpy(), g.index.to_numpy())
res["A1_raw_WLS_invvar"] = seg_ols(g.lg.to_numpy(), g.index.to_numpy(), w=1 / g.var_lg.to_numpy())
res["year_table"] = g.reset_index().to_dict(orient="records")

# adjusted year effects: logit NAME ~ year dummies + controls + topic100 FE (clustered by topic100)
r = C.logit("name_primary ~ C(year) + log_authors + llm_topic + C(topic100)", df, cluster="topic100")
yrs = sorted(df.year.unique())
ye = np.array([0.0] + [r.params[f"C(year)[T.{y}]"] for y in yrs[1:]])
V = r.cov_params()
names = [f"C(year)[T.{y}]" for y in yrs[1:]]
Vy = np.zeros((10, 10))
Vy[1:, 1:] = V.loc[names, names].to_numpy()
res["A1_adj_yeareffects"] = ye.tolist()
res["A1_adj_OLS"] = seg_ols(ye, yrs)
# GLS-ish: WLS with the diagonal of the year-effect variance + baseline var (2017 reference ~ its own sampling var)
vdiag = np.diag(Vy).copy()
vdiag[0] = float(g.var_lg.loc[2017])
res["A1_adj_WLS"] = seg_ols(ye, yrs, w=1 / vdiag)
# NA pool raw
gn = df[df.NA == 1].groupby("year").name_primary.agg(["mean", "size"])
gn = gn[gn.index >= 2017]
res["A1_NA_raw_OLS"] = seg_ols(np.log(gn["mean"] / (1 - gn["mean"])).to_numpy(), gn.index.to_numpy())

# ---------- A2: wild cluster bootstrap by year (LPM, topic100 FE, controls) ----------
d = df.copy()
d["tc"] = d.year - 2023
d["post"] = (d.year >= 2024).astype(int)
d["post_t"] = d.post * d.tc
fe = C.demean(d[["name_primary", "tc", "post", "post_t", "log_authors", "llm_topic"]].to_numpy(float),
              [d.topic100.to_numpy()])
yv, X = fe[:, 0], fe[:, 1:]
beta = np.linalg.lstsq(X, yv, rcond=None)[0]
cl = d.year.to_numpy()
G = np.unique(cl)


def cr1_t(X, yv, beta, cl, j):
    e = yv - X @ beta
    XtX_inv = np.linalg.inv(X.T @ X)
    meat = np.zeros((X.shape[1], X.shape[1]))
    for gg in G:
        m = cl == gg
        s = X[m].T @ e[m]
        meat += np.outer(s, s)
    n, k = X.shape
    adj = (len(G) / (len(G) - 1)) * ((n - 1) / (n - k))
    Vc = adj * XtX_inv @ meat @ XtX_inv
    return beta[j] / np.sqrt(Vc[j, j]), np.sqrt(Vc[j, j])


j = 2  # post_t
t_obs, se_year = cr1_t(X, yv, beta, cl, j)
# restricted model (post_t = 0)
Xr = np.delete(X, j, axis=1)
br = np.linalg.lstsq(Xr, yv, rcond=None)[0]
fit_r = Xr @ br
er = yv - fit_r
rng = np.random.default_rng(0)
webb = np.array([-np.sqrt(1.5), -1, -np.sqrt(.5), np.sqrt(.5), 1, np.sqrt(1.5)])
idx = {gg: cl == gg for gg in G}
B = 1999
tb = np.empty(B)
XtX_inv = np.linalg.inv(X.T @ X)
for b in range(B):
    w = rng.choice(webb, len(G))
    ystar = fit_r.copy()
    for gi, gg in enumerate(G):
        ystar[idx[gg]] += w[gi] * er[idx[gg]]
    bb = XtX_inv @ (X.T @ ystar)
    tb[b] = cr1_t(X, ystar, bb, cl, j)[0]
res["A2_wild_cluster_year"] = {
    "lpm_slope_change_pp": float(100 * beta[j]), "se_cluster_year_pp": float(100 * se_year), "t_cluster_year": float(t_obs),
    "p_one_sided_wcb_webb": float((np.sum(tb >= t_obs) + 1) / (B + 1)),
    "p_two_sided_wcb_webb": float((np.sum(np.abs(tb) >= abs(t_obs)) + 1) / (B + 1)), "B": B, "G": int(len(G))}

# ---------- A3: leave-one-year-out on adjusted year effects ----------
loo = {}
for k, y in enumerate(yrs):
    m = np.array(yrs) != y
    yy = ye[m] - (ye[m][0] if y == 2017 else 0)  # reference shift irrelevant for slope terms
    loo[int(y)] = seg_ols(yy, np.array(yrs)[m])
res["A3_leave_one_year_out_adj_OLS"] = {k: {kk: v[kk] for kk in ("OR", "OR_lo95", "OR_hi95", "p_one_sided_t")}
                                        for k, v in loo.items()}

# ---------- A4: 2017-2025 linear logit trend, extrapolated 2026 ----------
m = np.array(yrs) <= 2025
t = np.array(yrs)[m] - 2023
Xl = sm.add_constant(t.astype(float))
ml = sm.OLS(ye[m], Xl).fit()
pred26 = ml.params[0] + ml.params[1] * 3
se_pred = np.sqrt(np.array([1, 3.]) @ ml.cov_params() @ np.array([1, 3.]) + ml.mse_resid)
res["A4_2026_vs_linear_2017_25"] = {"resid_logit": float(ye[-1] - pred26), "pred_se_incl_year_shock": float(se_pred),
                                    "t": float((ye[-1] - pred26) / se_pred), "df": int(ml.df_resid),
                                    "p_one_sided": float(stats.t.sf((ye[-1] - pred26) / se_pred, ml.df_resid)),
                                    "year_shock_sd_logit_2017_25": float(np.sqrt(ml.mse_resid))}
(OUT / "ident_A_year_level_its.json").write_text(json.dumps(res, indent=1, default=float))
print(json.dumps({k: v for k, v in res.items() if k not in ("year_table", "A1_adj_yeareffects")}, indent=1, default=float))
print(g.round(4).to_string())
print("adj year effects", np.round(ye, 3))
