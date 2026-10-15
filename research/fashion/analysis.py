"""Estimation and verdicts for RQ2 and RQ3 (PREREGISTRATION.md "Decision rule", D4, D7-D12).

estimate(): one linear probability model (fe_ols) or logit (fe_logit) for an outcome, a tested regressor and
controls, with either topic FE + year dummies ("topic+year") or one absorbed topic x year FE ("cell", singleton cells
dropped), SE clustered by topic. Controls without within-FE variation are dropped and logged; if the tested regressor
has none, the estimate is missing (D4), and a missing estimate counts as the wrong sign (D9).
decide(): the RQ1 decision rule unchanged (Holm within the family, >= 75% of counted variants with the predicted sign,
both hindsight variants), plus the D12 labels (equivalent to null / inconclusive / significant in the opposite
direction), TOST p-values and the fragile flag.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy import stats

from logit import fe_logit
from ols import demean, fe_ols
from variants import HINDSIGHT_VARIANTS, ROBUST_SHARE, holm

ALPHA = 0.05


@dataclass(frozen=True)
class Spec:
    hid: str
    y: str
    x: str
    sign: int
    sesoi: float
    fe: str                                   # "topic+year" or "cell"
    years: tuple[int, int]
    controls: tuple[str, ...] = ()
    gated: bool = False
    note: str = ""
    extra: dict = field(default_factory=dict, compare=False, hash=False)


def _missing(n: int = 0, clusters: int = 0, why: str = "") -> dict:
    return {"coef": np.nan, "se": np.nan, "p": np.nan, "dof": np.nan, "n": n, "clusters": clusters,
            "ci95_lo": np.nan, "ci95_hi": np.nan, "ci90_lo": np.nan, "ci90_hi": np.nan, "dropped_controls": "", "note": why}


def _design(df: pd.DataFrame, y: str, x: str, controls, fe: str, years, estimator: str = "ols"):
    """The estimation sample and design of a registered model: (d, X, absorb, dropped), or a missing-estimate dict.
    X's first column is the tested regressor; for OLS with topic + year FE it includes the year dummies."""
    d = df if years is None else df[(df.year >= years[0]) & (df.year <= years[1])]
    d = d.dropna(subset=[y, x, *controls])
    if fe == "cell":
        size = d.groupby("cell").cell.transform("size")
        d = d[size > 1]                                                   # singleton topic-year cells (D4)
    if len(d) < 10 or d[y].nunique() < 2 or d[x].nunique() < 2:
        return _missing(len(d), d.topic.nunique() if len(d) else 0, "no variation")
    d = d.reset_index(drop=True)
    X = d[[x, *controls]].astype(float)
    if fe == "topic+year" and estimator == "ols":
        X = pd.concat([X, pd.get_dummies(d.year, prefix="y", drop_first=True).astype(float)], axis=1)
    absorb = d.cell if fe == "cell" else d.topic
    if estimator == "logit":
        absorb = d.topic.astype(str) + ":" + d.year.astype(str) if fe == "cell" else d.topic
    within = demean(X.to_numpy(float), pd.factorize(absorb)[0]).std(axis=0) > 1e-12
    if estimator == "logit":                                               # logit: variation across rows is enough
        within = X.to_numpy(float).std(axis=0) > 1e-12
    if not within[0]:
        return _missing(len(d), d.topic.nunique(), "tested regressor has no within-FE variation")
    dropped = [c for c, ok in zip(X.columns, within) if not ok]
    return d, X.loc[:, within], absorb, dropped


def estimate(df: pd.DataFrame, y: str, x: str, controls: tuple[str, ...] | list[str] = (), fe: str = "topic+year",
             years: tuple[int, int] | None = None, estimator: str = "ols", describe: bool = False) -> dict:
    """describe=True adds the sample means of y and x. Only the frozen real run asks for them: in a dry-run they would
    be means of real columns (e.g. a product of two real regressors), which can reveal a hypothesis relationship."""
    des = _design(df, y, x, controls, fe, years, estimator)
    if isinstance(des, dict):
        return des
    d, X, absorb, dropped = des
    if estimator == "logit":
        if fe != "topic+year":
            raise ValueError("the logit variant is defined for topic + year fixed effects only (D8)")
        try:
            r, info = fe_logit(d[y].astype(float), X, [d.topic.rename("topic"), d.year.rename("year")], d.topic)
        except (ValueError, RuntimeError, np.linalg.LinAlgError) as e:
            return _missing(len(d), d.topic.nunique(), f"logit failed: {e}")
        row = r.loc[x]
        extra = {"ame": float(row.ame), "dropped_topics": ";".join(info["dropped_groups"])}
    else:
        codes = pd.Series(pd.factorize(absorb)[0])                       # integer group codes: same result, faster
        row = fe_ols(d[y].astype(float), X, codes, pd.Series(pd.factorize(d.topic)[0])).loc[x]
        extra = {}
    dof = int(row.clusters) - 1
    q95, q90 = stats.t.ppf(0.975, dof), stats.t.ppf(0.95, dof)
    out = {"coef": float(row.coef), "se": float(row.se), "p": float(row.p), "dof": dof, "n": int(row.n),
           "clusters": int(row.clusters), "ci95_lo": float(row.coef - q95 * row.se), "ci95_hi": float(row.coef + q95 * row.se),
           "ci90_lo": float(row.coef - q90 * row.se), "ci90_hi": float(row.coef + q90 * row.se),
           "dropped_controls": ";".join(c for c in dropped if not c.startswith("y_")), "note": "", **extra}
    if describe:
        out["outcome_mean"], out["regressor_mean"] = float(d[y].mean()), float(d[x].mean())
    if fe == "cell":
        out["cells"] = int(d.cell.nunique())
    return out


def _partial(d: pd.DataFrame, y: str, X: pd.DataFrame, absorb: pd.Series):
    """FE-demeaned design, OLS fit and residuals, exactly as fe_ols computes them."""
    codes = pd.factorize(absorb)[0]
    Xd = demean(X.to_numpy(float), codes)
    yd = demean(d[y].to_numpy(float), codes)
    xtx_inv = np.linalg.pinv(Xd.T @ Xd)
    beta = xtx_inv @ Xd.T @ yd
    return Xd, yd, xtx_inv, beta, yd - Xd @ beta


def _cluster_variance(Xd: np.ndarray, e: np.ndarray, q: np.ndarray, groups) -> tuple[float, int]:
    """CR1 variance of q'beta for one clustering: G/(G-1)*(n-1)/(n-k) * sum_g (q's_g)^2."""
    codes = pd.factorize(pd.Series(groups))[0]
    G, (n, k) = codes.max() + 1, Xd.shape
    S = np.zeros((G, k))
    np.add.at(S, codes, Xd * e[:, None])
    return float((G / (G - 1)) * ((n - 1) / (n - k)) * np.sum((S @ q) ** 2)), int(G)


BOOT_DRAWS, BOOT_SEED = 9999, 20261015


def wild_cluster_bootstrap_p(df: pd.DataFrame, y: str, x: str, controls=(), fe: str = "topic+year", years=None,
                             draws: int = BOOT_DRAWS, seed: int = BOOT_SEED, weights: np.ndarray | None = None) -> dict:
    """D16 remedy: wild cluster restricted bootstrap p-value for the tested regressor (Rademacher weights by topic,
    null beta_x = 0 imposed, controls and fixed effects kept), comparing |t*| with the observed CR1 |t|.

    Vectorised: with the restricted fit yhat and residual u, y*_b = yhat + u * w_b[g], so beta*_b = beta_r + sum_g
    w_bg M_g and the cluster scores of the tested coefficient are q's*_bg = q'P_g + w_bg q'R_g - (H_g q)'beta*_b."""
    des = _design(df, y, x, controls, fe, years)
    if isinstance(des, dict):
        return {"p": np.nan, "t": np.nan, "draws": 0}
    d, X, absorb, _ = des
    Xd, yd, xtx_inv, beta, e = _partial(d, y, X, absorb)
    q = xtx_inv[0]
    cl = pd.factorize(d.topic)[0]
    G, (n, k) = cl.max() + 1, Xd.shape
    c = (G / (G - 1)) * ((n - 1) / (n - k))
    v, _ = _cluster_variance(Xd, e, q, d.topic)
    t_obs = beta[0] / np.sqrt(v)
    C = Xd[:, 1:]
    yhat = C @ np.linalg.lstsq(C, yd, rcond=None)[0] if C.shape[1] else np.zeros(n)
    u = yd - yhat
    A = xtx_inv @ Xd.T
    M, P, R, QH = (np.zeros((G, k)) for _ in range(4))
    np.add.at(M, cl, (A * u).T)
    np.add.at(P, cl, Xd * yhat[:, None])
    np.add.at(R, cl, Xd * u[:, None])
    np.add.at(QH, cl, Xd * (Xd @ q)[:, None])
    W = weights if weights is not None else np.random.default_rng(seed).choice([-1.0, 1.0], size=(draws, G))
    betas = A @ yhat + W @ M
    z = (P @ q)[None, :] + W * (R @ q)[None, :] - betas @ QH.T
    t_star = betas[:, 0] / np.sqrt(c * np.sum(z ** 2, axis=1))
    return {"p": float(np.mean(np.abs(t_star) >= abs(t_obs))), "t": float(t_obs), "draws": int(len(W)),
            "t_star": t_star if weights is not None else None}


def estimate_twoway(df: pd.DataFrame, y: str, x: str, controls=(), fe: str = "topic+year", years=None,
                    cluster2: str = "topic_early") -> dict:
    """S11: the registered OLS model with two-way clustered SE (topic and cluster2; Cameron-Gelbach-Miller, each
    component with its own CR1 factor; the larger one-way variance if the two-way variance is not positive), p-value and
    CIs from t(min(G1, G2) - 1)."""
    des = _design(df, y, x, controls, fe, years)
    if isinstance(des, dict):
        return des
    d, X, absorb, dropped = des
    Xd, yd, xtx_inv, beta, e = _partial(d, y, X, absorb)
    q = xtx_inv[0]
    v1, g1 = _cluster_variance(Xd, e, q, d.topic)
    v2, g2 = _cluster_variance(Xd, e, q, d[cluster2])
    v12, _ = _cluster_variance(Xd, e, q, d.topic.astype(str) + "|" + d[cluster2].astype(str))
    v = v1 + v2 - v12
    if v <= 0:
        v = max(v1, v2)
    se, dof = float(np.sqrt(v)), min(g1, g2) - 1
    coef = float(beta[0])
    q95, q90 = stats.t.ppf(0.975, dof), stats.t.ppf(0.95, dof)
    return {"coef": coef, "se": se, "p": float(2 * stats.t.sf(abs(coef / se), dof)), "dof": dof, "n": int(len(d)),
            "clusters": g1, "clusters2": g2, "ci95_lo": coef - q95 * se, "ci95_hi": coef + q95 * se,
            "ci90_lo": coef - q90 * se, "ci90_hi": coef + q90 * se, "dropped_controls": "", "note": f"two-way: topic, {cluster2}"}


def apply_bootstrap(est: dict, df: pd.DataFrame, spec: "Spec") -> dict:
    """Registered remedy (D16): replace the main-specification p-value by the wild cluster bootstrap p-value."""
    b = wild_cluster_bootstrap_p(df, spec.y, spec.x, spec.controls, spec.fe, spec.years)
    return {**est, "p_cr1": est["p"], "p": b["p"],
            "p_method": f"wild cluster restricted bootstrap (Rademacher by topic, {b['draws']} draws)"}


def fit(df: pd.DataFrame, spec: Spec, estimator: str = "ols", extra_controls: tuple[str, ...] = (),
        x: str | None = None, years: tuple[int, int] | None = None, describe: bool = False) -> dict:
    return estimate(df, spec.y, x or spec.x, tuple(spec.controls) + tuple(extra_controls), spec.fe,
                    years or spec.years, estimator, describe)


def tost_p(coef: float, se: float, dof: float, bound: float) -> float:
    if not np.isfinite(coef) or not np.isfinite(se):
        return np.nan
    lower = stats.t.sf((coef + bound) / se, dof)                       # H0: beta <= -bound
    upper = stats.t.cdf((coef - bound) / se, dof)                      # H0: beta >= +bound
    return float(max(lower, upper))


def decide(specs: list[Spec], main: dict[str, dict], counted: dict[str, dict[str, dict]],
           supplementary: dict[str, dict[str, dict]] | None = None) -> dict[str, dict]:
    """main[hid] = estimate; counted[hid][variant] = estimate; supplementary[hid][s_variant] = estimate."""
    family = [s.hid for s in specs]
    p = pd.Series({h: main[h]["p"] for h in family}, dtype=float)
    p_holm = holm(p.fillna(1.0))
    out = {}
    for s in specs:
        m = main[s.hid]
        rob = counted.get(s.hid, {})
        signs = {v: (np.sign(r["coef"]) == s.sign) if np.isfinite(r["coef"]) else False for v, r in rob.items()}
        share = float(np.mean(list(signs.values()))) if signs else np.nan
        hind = all(signs.get(v, False) for v in HINDSIGHT_VARIANTS)
        right = bool(np.isfinite(m["coef"]) and np.sign(m["coef"]) == s.sign)
        sig = bool(p_holm[s.hid] < ALPHA)
        supported = right and sig and share >= ROBUST_SHARE and hind
        within = bool(np.isfinite(m["coef"]) and -s.sesoi < m["ci90_lo"] and m["ci90_hi"] < s.sesoi)
        if supported:
            verdict = "supported"
        elif sig and np.isfinite(m["coef"]) and not right:
            verdict = "significant in the opposite direction"
        elif within:
            verdict = "equivalent to null"
        else:
            verdict = "inconclusive"
        fragile_by = [f"{k}" for k, r in (supplementary or {}).get(s.hid, {}).items()
                      if np.isfinite(r.get("coef", np.nan)) and r["p"] < ALPHA and np.sign(r["coef"]) == -s.sign]
        out[s.hid] = {
            "outcome": s.y, "regressor": s.x, "predicted_sign": s.sign, "sesoi": s.sesoi,
            "coef": m["coef"], "se": m["se"], "ci95": [m["ci95_lo"], m["ci95_hi"]], "ci90": [m["ci90_lo"], m["ci90_hi"]],
            "p": m["p"], "p_holm": float(p_holm[s.hid]), "n": m["n"], "clusters": m["clusters"],
            "p_method": m.get("p_method", "CR1, t(G-1)"), "p_cr1": m.get("p_cr1", m["p"]),
            "robustness_same_sign": share, "robustness_variants": len(rob),
            "variants_wrong_sign": sorted(v for v, ok in signs.items() if not ok),
            "hindsight_variants_same_sign": hind,
            "tost_p": tost_p(m["coef"], m["se"], m["dof"], s.sesoi),
            "verdict": verdict, "fragile": bool(supported and fragile_by), "fragile_by": fragile_by,
        }
    return out


def misclassification_rates(ours: pd.Series, ref: pd.Series, positive: set[str]) -> tuple[float, float, int]:
    """(false positive rate alpha0, false negative rate alpha1, n) of our class indicator against a reference."""
    o, r = ours.isin(positive), ref.isin(positive)
    a0 = float((o & ~r).sum() / max((~r).sum(), 1))
    a1 = float((~o & r).sum() / max(r.sum(), 1))
    return a0, a1, int(len(r))


def corrected(est: dict, a0: float, a1: float) -> dict:
    """S8: under non-differential misclassification, the LPM slope on the observed label is (1 - a0 - a1) times the
    slope on the true class; divide coefficient, SE and CI by that factor (rates treated as known)."""
    k = 1.0 - a0 - a1
    out = dict(est)
    for c in ["coef", "se", "ci95_lo", "ci95_hi", "ci90_lo", "ci90_hi"]:
        out[c] = est[c] / k
    out["note"] = f"divided by 1 - a0 - a1 = {k:.4f} (a0 {a0:.4f}, a1 {a1:.4f})"
    return out
