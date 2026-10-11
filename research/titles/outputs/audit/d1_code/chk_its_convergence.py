"""Audit D1-H1a: does every segmented logit in the break scan converge with Newton (not the BFGS fallback),
and is the sup-LR ranking (2023 vs 2024) robust to the fitting method / FE handling?
Also: LR of level+slope vs linear compared with an LPM-based F-ish check.
Run: cd research/titles/src && OMP_NUM_THREADS=1 /home/user/venv/bin/python ../outputs/audit/d1_code/chk_its_convergence.py
"""
import sys, warnings
sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
import statsmodels.api as sm, patsy
from analyses import d1_its as I
from analyses import _core as CORE

df = I.load()
print("n", len(df))

def fit_raw(d, f, method):
    y, X = patsy.dmatrices(f, d, return_type="dataframe")
    m = sm.Logit(y.iloc[:, 0], X)
    r = m.fit(disp=0, method=method, maxiter=5000)
    return r

rows = []
d0 = I._design(df, 2024)
f_lin = "name_primary ~ tc + log_authors + llm_topic + C(topic100)"
r_lin_n = fit_raw(d0, f_lin, "newton")
r_lin_c = CORE.logit(f_lin, d0, cluster="topic100")
print("linear: newton llf", r_lin_n.llf, "conv", r_lin_n.mle_retvals.get("converged"), "| C.logit llf", r_lin_c.llf,
      "method", r_lin_c.mle_settings.get("optimizer"))
for B in range(2019, 2026):
    for level in (True, False):
        d = I._design(df, B)
        rhs = "tc + " + ("post + " if level else "") + "post_t + log_authors + llm_topic + C(topic100)"
        f = "name_primary ~ " + rhs
        rn = fit_raw(d, f, "newton")
        rc = I.its_fit(df, "name_primary", B, level=level)
        rows.append(dict(B=B, level=level, llf_newton=rn.llf, conv_newton=rn.mle_retvals.get("converged"),
                         llf_pipeline=rc.llf, opt_pipeline=rc.mle_settings.get("optimizer"),
                         LR_newton=2 * (rn.llf - r_lin_n.llf), LR_pipeline=2 * (rc.llf - r_lin_c.llf),
                         slopeOR=float(np.exp(rc.params["post_t"]))))
R = pd.DataFrame(rows)
pd.set_option("display.width", 200)
print(R.round(4).to_string())
R.to_csv("/home/user/cloud-research/research/titles/outputs/audit/d1_code/its_convergence.csv", index=False)
