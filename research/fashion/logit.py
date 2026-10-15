"""Logit with fixed-effect dummies and cluster-robust standard errors (numpy only; PREREGISTRATION.md D8).

fe_logit(y, X, dummies, cluster): maximum likelihood by Newton steps with step-halving. `dummies` are categorical
Series (e.g. topic, year) entered as full dummy sets with the first level of each dropped, plus an intercept. Groups
of the first dummy Series whose outcome never varies (all 0 or all 1) are dropped before fitting and reported, since
their coefficients diverge. Standard errors: CR1 sandwich by cluster, scaled G/(G-1)*(N-1)/(N-K) with K counting
every parameter, as statsmodels does with cov_type="cluster"; p-values from t(G-1). Average marginal effects of the
X columns are returned for reading (derivative for continuous columns, discrete 0->1 change for 0/1 columns).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def _design(X: pd.DataFrame, dummies: list[pd.Series]) -> tuple[np.ndarray, list[str]]:
    parts, names = [X.to_numpy(float), np.ones((len(X), 1))], list(X.columns) + ["_const"]
    for s in dummies:
        d = pd.get_dummies(s.astype(str), prefix=f"_{s.name}", drop_first=True).astype(float)
        parts.append(d.to_numpy())
        names += list(d.columns)
    return np.hstack(parts), names


def _loglik(Z: np.ndarray, y: np.ndarray, b: np.ndarray) -> float:
    eta = Z @ b
    return float(np.sum(y * eta - np.logaddexp(0.0, eta)))


def fe_logit(y: pd.Series, X: pd.DataFrame, dummies: list[pd.Series], cluster: pd.Series,
             tol: float = 1e-10, max_iter: int = 100) -> tuple[pd.DataFrame, dict]:
    keep = y.notna() & X.notna().all(axis=1) & cluster.notna()
    for s in dummies:
        keep &= s.notna()
    first = dummies[0][keep]
    rate = y[keep].groupby(first).mean()
    flat = set(rate[(rate == 0) | (rate == 1)].index)
    keep &= ~dummies[0].isin(flat)
    yv = y[keep].to_numpy(float)
    Xk = X[keep].reset_index(drop=True)
    Z, names = _design(Xk, [s[keep].reset_index(drop=True) for s in dummies])
    if np.linalg.matrix_rank(Z) < Z.shape[1]:
        raise ValueError("design matrix is rank deficient")
    b = np.zeros(Z.shape[1])
    ll = _loglik(Z, yv, b)
    for it in range(max_iter):
        p = 1.0 / (1.0 + np.exp(-(Z @ b)))
        grad = Z.T @ (yv - p)
        H = (Z * (p * (1 - p))[:, None]).T @ Z
        step = np.linalg.solve(H, grad)
        t = 1.0
        while True:
            nb = b + t * step
            nll = _loglik(Z, yv, nb)
            if nll >= ll - 1e-12 or t < 1e-8:
                break
            t /= 2
        b, ll_old, ll = nb, ll, nll
        if np.max(np.abs(t * step)) < tol or abs(ll - ll_old) < tol * (1 + abs(ll)):
            break
    else:
        raise RuntimeError("logit did not converge")
    p = 1.0 / (1.0 + np.exp(-(Z @ b)))
    H = (Z * (p * (1 - p))[:, None]).T @ Z
    Hinv = np.linalg.inv(H)
    _, cinv = np.unique(cluster[keep].to_numpy(), return_inverse=True)
    G, n, k = cinv.max() + 1, len(yv), Z.shape[1]
    scores = np.zeros((G, k))
    np.add.at(scores, cinv, Z * (yv - p)[:, None])
    vcov = (G / (G - 1)) * ((n - 1) / (n - k)) * Hinv @ (scores.T @ scores) @ Hinv
    se = np.sqrt(np.diag(vcov))
    tstat = b / se
    pval = 2 * stats.t.sf(np.abs(tstat), df=G - 1)
    nx = X.shape[1]
    ame = []
    for j, c in enumerate(X.columns):
        col = Xk[c].to_numpy(float)
        if set(np.unique(col)) <= {0.0, 1.0}:
            eta = Z @ b - Z[:, j] * b[j]
            ame.append(float(np.mean(1 / (1 + np.exp(-(eta + b[j]))) - 1 / (1 + np.exp(-eta)))))
        else:
            ame.append(float(np.mean(b[j] * p * (1 - p))))
    res = pd.DataFrame({"coef": b[:nx], "se": se[:nx], "t": tstat[:nx], "p": pval[:nx], "ame": ame, "n": n, "clusters": G},
                       index=X.columns)
    return res, {"dropped_groups": sorted(map(str, flat)), "iterations": it + 1, "loglik": ll, "params": k}
