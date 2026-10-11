"""Audit D1 / identification, check B: does the R1 'content' model absorb the fashion trend through time-marker words?

The R1 content model is trained on pooled years y-3..y-1 WITHOUT year effects. Any word whose frequency trends within
the training window inherits the between-year rise in NAME (omitted-variable bias), and when the word keeps trending
in year y the model books part of the fashion's momentum as a 'content step'. Two decisive checks, same vectoriser,
same folds, same chosen C, same recalibration as d1_content_cf:
  orig    exact re-implementation (validation: must reproduce cf_rolling_steps.csv content steps)
  yearFE  add training-year dummies (scaled x10 so the L2 penalty on them is negligible); test and calibration rows
          carry the y-1 dummy, so content coefficients are identified only from within-year variation
  perm    within-year permutation of the NAME labels in the training window (yearly shares preserved): content has no
          within-year signal, so any content step is pure time-proxy extrapolation (null distribution of the artefact)
Same for the fixed window (train 2021-23 -> 2024-26) for orig and yearFE.
"""
import json
import sys
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import sparse
from scipy.special import expit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import d1_content_cf as CF  # noqa: E402

warnings.filterwarnings("ignore")
OUT = Path(__file__).resolve().parent
t0 = time.time()
df = CF.load_frame()
texts = CF.r1_texts(df)
yrs = df.year.to_numpy()
Y = df.name_primary.to_numpy()
meta_roll = json.loads((CF.SCORES / "R1__U__primary__rolling.json").read_text())
meta_fix = json.loads((CF.SCORES / "R1__U__primary__fixed.json").read_text())
N_PERM = int(sys.argv[1]) if len(sys.argv) > 1 else 3
SCALE = 10.0


def lr(Cv):
    return LogisticRegression(C=Cv, max_iter=5000, tol=1e-5)


def year_dummies(rows, train_years, as_year=None):
    """dummies for all training years except the last (calibration) year; as_year overrides the row year."""
    cols = list(train_years[:-1])
    yy = yrs[rows] if as_year is None else np.full(len(rows), as_year)
    M = np.column_stack([(yy == c).astype(np.float32) * SCALE for c in cols])
    return sparse.csr_matrix(M)


def run_window(tr, te, train_years, calib_year, Cv, spec, ytr):
    vec = TfidfVectorizer(min_df=5, max_df=0.5, ngram_range=(1, 2), sublinear_tf=True, max_features=50000,
                          dtype=np.float32)
    Xtr = vec.fit_transform(texts[tr])
    Xte = vec.transform(texts[te])
    if spec == "yearFE":
        Xtr = sparse.hstack([Xtr, year_dummies(tr, train_years)]).tocsr()
        Xte = sparse.hstack([Xte, year_dummies(te, train_years, as_year=calib_year)]).tocsr()
    folds = list(StratifiedKFold(5, shuffle=True, random_state=0).split(np.zeros(len(tr)), ytr))
    oof = np.zeros(len(tr))
    for a, b in folds:
        m = lr(Cv).fit(Xtr[a], ytr[a])
        oof[b] = m.decision_function(Xtr[b])
    m = lr(Cv).fit(Xtr, ytr)
    st = m.decision_function(Xte)
    cal = yrs[tr] == calib_year
    c = CF.shift_for(oof[cal], ytr[cal].mean())
    p_hat = {int(yv): float(expit(st[yrs[te] == yv] + c).mean()) for yv in np.unique(yrs[te])}
    obs = {int(yv): float(Y[te][yrs[te] == yv].mean()) for yv in np.unique(yrs[te])}
    return p_hat, obs, float(ytr[cal].mean()), m, vec


rows = []
rng = np.random.default_rng(12345)
for spec in ["orig", "yearFE"] + [f"perm{k}" for k in range(N_PERM)]:
    for yv in range(2019, 2027):
        w = meta_roll["windows"][f"roll{yv}"]
        tyrs = tuple(range(yv - 3, yv))
        tr = np.where(np.isin(yrs, tyrs))[0]
        te = np.where(yrs == yv)[0]
        ytr = Y[tr].copy()
        if spec.startswith("perm"):
            for ty in tyrs:
                m_ = yrs[tr] == ty
                ytr[m_] = rng.permutation(ytr[m_])
        p_hat, obs, obs_cal, model, vec = run_window(tr, te, tyrs, yv - 1, w["C"], "yearFE" if spec == "yearFE" else "orig", ytr)
        rows.append(dict(design="rolling", spec=spec, year=yv, C=w["C"], obs=obs[yv], p_hat=p_hat[yv], obs_calib=obs_cal))
        print(f"{spec} roll{yv}: step={100*(obs[yv]-obs_cal):.2f} content={100*(p_hat[yv]-obs_cal):.2f} "
              f"u={100*(obs[yv]-p_hat[yv]):.2f}  {time.time()-t0:.0f}s", flush=True)
        if spec == "yearFE" and yv == 2026:
            yc = model.coef_.ravel()[-2:] / SCALE
            print("   year coefs (2023, 2024 vs 2025):", np.round(yc, 3), flush=True)
for spec in ["orig", "yearFE"]:
    tyrs = (2021, 2022, 2023)
    tr = np.where(np.isin(yrs, tyrs))[0]
    te = np.where(np.isin(yrs, (2024, 2025, 2026)))[0]
    p_hat, obs, obs_cal, model, vec = run_window(tr, te, tyrs, 2023, meta_fix["windows"]["fixed"]["C"], spec, Y[tr].copy())
    for yv in (2024, 2025, 2026):
        rows.append(dict(design="fixed", spec=spec, year=yv, C=meta_fix["windows"]["fixed"]["C"], obs=obs[yv],
                         p_hat=p_hat[yv], obs_calib=obs_cal))
    print(f"fixed {spec}: share2026={(p_hat[2026]-obs_cal)/(obs[2026]-obs_cal):.3f} {time.time()-t0:.0f}s", flush=True)
    if spec == "orig":
        # which top features trend in time? correlation of feature frequency with year within window
        pass

R = pd.DataFrame(rows)
R["step"] = R.obs - R.obs_calib
R["content_step"] = R.p_hat - R.obs_calib
R["u"] = R.obs - R.p_hat
R.to_csv(OUT / "ident_B_time_proxy_steps.csv", index=False)

summ = {}
pre, post = list(range(2019, 2024)), [2024, 2025, 2026]
for spec, g in R[R.design == "rolling"].groupby("spec"):
    g = g.set_index("year")
    summ[spec] = {"content_share_post_steps": float(g.loc[post, "content_step"].sum() / g.loc[post, "step"].sum()),
                  "content_step_pre_mean_pp": float(100 * g.loc[pre, "content_step"].mean()),
                  "content_step_post_mean_pp": float(100 * g.loc[post, "content_step"].mean()),
                  "u_pre_pp": float(100 * g.loc[pre, "u"].mean()), "u_post_pp": float(100 * g.loc[post, "u"].mean()),
                  "diff_pp": float(100 * (g.loc[post, "u"].mean() - g.loc[pre, "u"].mean())),
                  "ratio": float(g.loc[post, "u"].mean() / g.loc[pre, "u"].mean()),
                  "content_steps_pp": {int(k): round(100 * v, 2) for k, v in g.content_step.items()}}
for spec, g in R[R.design == "fixed"].groupby("spec"):
    g = g.set_index("year")
    summ[f"fixed|{spec}"] = {f"share_{y}": float(g.loc[y, "content_step"] / g.loc[y, "step"]) for y in (2024, 2025, 2026)}
# validation vs the published steps
pub = pd.read_csv(CF.OUTDIR / "cf_rolling_steps.csv")
pub = pub[(pub.rep == "R1") & (pub["pop"] == "U") & (pub.outcome == "primary")].set_index("year")
o = R[(R.design == "rolling") & (R.spec == "orig")].set_index("year")
summ["validation_max_abs_diff_content_step_pp"] = float(100 * (o.content_step - pub.content_step).abs().max())
perm = R[(R.design == "rolling") & R.spec.str.startswith("perm")]
summ["perm_mean_content_step_pp_by_year"] = (100 * perm.groupby("year").content_step.mean()).round(2).to_dict()
(OUT / "ident_B_time_proxy.json").write_text(json.dumps(summ, indent=1))
print(json.dumps(summ, indent=1))
print(f"done {time.time()-t0:.0f}s")
