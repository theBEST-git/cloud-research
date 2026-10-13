"""Least squares with absorbed fixed effects and cluster-robust standard errors (numpy only).

fe_ols(y, X, absorb, cluster): one set of fixed effects is absorbed by demeaning within `absorb` groups (other
fixed effects, e.g. year dummies, go into X and are demeaned too, which is exact by Frisch-Waugh-Lovell).
Standard errors are CR1 cluster-robust; p-values use a t distribution with G - 1 degrees of freedom. Absorbed
fixed effects nested in clusters are not counted in the small-sample correction (as in Stata's areg/reghdfe).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def demean(values: np.ndarray, groups: np.ndarray) -> np.ndarray:
    codes, inv = np.unique(groups, return_inverse=True)
    sums = np.zeros((len(codes),) + values.shape[1:])
    np.add.at(sums, inv, values)
    counts = np.bincount(inv, minlength=len(codes)).reshape((-1,) + (1,) * (values.ndim - 1))
    return values - (sums / counts)[inv]


def fe_ols(y: pd.Series, X: pd.DataFrame, absorb: pd.Series, cluster: pd.Series) -> pd.DataFrame:
    keep = y.notna() & X.notna().all(axis=1) & absorb.notna() & cluster.notna()
    yv, Xv = y[keep].to_numpy(float), X[keep].to_numpy(float)
    g, c = absorb[keep].to_numpy(), cluster[keep].to_numpy()
    yd, Xd = demean(yv, g), demean(Xv, g)
    varying = Xd.std(axis=0) > 1e-12
    if not varying.all():
        raise ValueError(f"no within-group variation in {list(X.columns[~varying])}")
    xtx_inv = np.linalg.pinv(Xd.T @ Xd)
    beta = xtx_inv @ Xd.T @ yd
    resid = yd - Xd @ beta
    _, cinv = np.unique(c, return_inverse=True)
    G, n, k = cinv.max() + 1, len(yd), Xd.shape[1]
    scores = np.zeros((G, k))
    np.add.at(scores, cinv, Xd * resid[:, None])
    meat = scores.T @ scores
    vcov = (G / (G - 1)) * ((n - 1) / (n - k)) * xtx_inv @ meat @ xtx_inv
    se = np.sqrt(np.diag(vcov))
    t = beta / se
    p = 2 * stats.t.sf(np.abs(t), df=G - 1)
    return pd.DataFrame({"coef": beta, "se": se, "t": t, "p": p, "n": n, "clusters": G}, index=X.columns)
