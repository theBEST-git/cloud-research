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


def estimate(df: pd.DataFrame, y: str, x: str, controls: tuple[str, ...] | list[str] = (), fe: str = "topic+year",
             years: tuple[int, int] | None = None, estimator: str = "ols") -> dict:
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
    within = demean(X.to_numpy(float), absorb.to_numpy()).std(axis=0) > 1e-12
    if estimator == "logit":                                               # logit: variation across rows is enough
        within = X.to_numpy(float).std(axis=0) > 1e-12
    if not within[0]:
        return _missing(len(d), d.topic.nunique(), "tested regressor has no within-FE variation")
    dropped = [c for c, ok in zip(X.columns, within) if not ok]
    X = X.loc[:, within]
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
        row = fe_ols(d[y].astype(float), X, absorb, d.topic).loc[x]
        extra = {}
    dof = int(row.clusters) - 1
    q95, q90 = stats.t.ppf(0.975, dof), stats.t.ppf(0.95, dof)
    out = {"coef": float(row.coef), "se": float(row.se), "p": float(row.p), "dof": dof, "n": int(row.n),
           "clusters": int(row.clusters), "ci95_lo": float(row.coef - q95 * row.se), "ci95_hi": float(row.coef + q95 * row.se),
           "ci90_lo": float(row.coef - q90 * row.se), "ci90_hi": float(row.coef + q90 * row.se),
           "dropped_controls": ";".join(c for c in dropped if not c.startswith("y_")), "note": "",
           "outcome_mean": float(d[y].mean()), "regressor_mean": float(d[x].mean()), **extra}
    if fe == "cell":
        out["cells"] = int(d.cell.nunique())
    return out


def fit(df: pd.DataFrame, spec: Spec, estimator: str = "ols", extra_controls: tuple[str, ...] = (),
        x: str | None = None, years: tuple[int, int] | None = None) -> dict:
    return estimate(df, spec.y, x or spec.x, tuple(spec.controls) + tuple(extra_controls), spec.fe,
                    years or spec.years, estimator)


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
