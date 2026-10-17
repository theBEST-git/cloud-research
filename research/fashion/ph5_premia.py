"""PH5 premia (final post hoc round, selection S5): do topic acceptance advantages last? How large is the true
(noise-corrected) spread of topic acceptance premia within a year, how persistent is it, how much of an extreme past
premium survives (winner's curse), do submissions flow towards high-premium topics, and who bears the cost of an
unexpected submission surge? Post hoc and exploratory: every estimate is an association; Holm within each declared
family ranks the evidence, nothing more.

Population: RQ3 decided papers 2018-2026 (rq3, accepted).
Units (outcome-free memberships, panel.frame('k100') row order):
  early     early-map topics (fitted on 2017-2020 papers only): the primary, prospective unit
  k100      k100 topics (fitted on all years): the hindsight comparison
  keywords  the 68 PH4 author keywords (posthoc.ph4_members; a paper can be in several)
  areas     the 20 coarse areas (parent of the k100 topic, posthoc.add_columns)
  robustness units: seed_refit (the k100 procedure refitted with other seeds: the noise ceiling for differences
  between maps) and primary_area (the ICLR primary area string, 2024-2026)
Cell (u, t): g = acceptance of u's papers in year t minus that of all other papers of year t; v = p_t(1 - p_t)(1/n1 +
1/n0), p_t = the year's acceptance rate (not the per-cell shrunk rates of posthoc.gap_summary: those correlate with g
and inflated the null DL tau^2 by about 7 pp^2 in 30 simulated null frames). Eligible: n1 >= 15 decided papers; a
year enters (a) and (b) with >= 5 eligible units.
(a) spread       tau_t^2 = DerSimonian-Laird moment estimate (Q_t - (m_t - 1)) / C_t across the eligible units of year
                 t; tau^2 = max(0, sum_t m_t tau_t^2 / sum_t m_t), m_t = eligible units (truncated once, after pooling;
                 truncating each year first biases tau upwards under the null: that version and per-year REML are
                 reported as checks). Signal share = tau^2 / (tau^2 + median v). p(tau > 0) = (1 + #{tau_perm >= tau})
                 / 201 over 200 within-year permutations of acceptance; 95% CI: 999 unit bootstraps (percentile).
                 Reliability rel(n) = tau^2 / (tau^2 + p(1 - p)/n), p = population rate; n* = p(1 - p)/tau^2.
(b) persistence  per year pair (t, t + h), both years in (a), units eligible in both: w = 1/sqrt((v_t + tau^2)(v_t+h +
                 tau^2)), W = sum w, C = W - sum w^2 / W; signal covariance sum w (x - xbar_w)(y - ybar_w) / C (binomial
                 noise is independent across years: no correction needed); signal variances (sum w (x - xbar_w)^2 -
                 sum w v + sum w^2 v / W) / C (tau^2 on the same units, same weights); pooled over the pairs weighted by
                 overlapping units; rho_h = cov / sqrt(var_t var_t+h), h = 1..4, clipped to [-1, 1], undefined unless
                 both variances > 0. p(rho_1 = 0): two-sided z of the pooled covariance with its unit-bootstrap SD;
                 CI: unit-bootstrap percentile. Window version: one pair, W1 = 2018-2022 and W2 = 2024-2026 premia.
                 Window premium: paper-weighted mean of the unit's yearly gaps in the window, variance sum (n_t/n)^2 v_t;
                 window units: >= 50 submissions (any status; outcome-free) and >= 15 decided papers in each window.
(c) winner's curse  window premia centred (1/v-weighted mean); tau_W^2 = DL across window units; EB = tau_W1^2 /
                 (tau_W1^2 + v) x centred W1 premium. Ranked by raw W1 and by EB: retention R = mean W2 / mean W1 of the
                 top and bottom decile (quintile for areas), and mean W2 / mean EB for the EB ranking; unit-bootstrap
                 CIs (centring, tau_W1^2 and selection redone per draw). Shrinkage b = WLS slope of W2 on W1 (weights
                 1/(v_W2 + tau_W2^2)), HC3 SE, t(m - 2) (HC1 rejected 7-13% at 0.05 in 300 null frames, areas worst;
                 HC3 5-7%).
(d) flows        (early map; k100 as a check) unit-years t = 2019-2025 with an eligible cell: dshare = log share_t+1 -
                 log share_t (all submissions, counts + .5) ~ EB premium_t per 10 pp (pooled tau^2, shrunk to the
                 year's random-effects mean) + log growth t - 1 -> t + log prior growth (t - 2 -> t - 1, as
                 topic_maturity) + log share_t | year FE; CR1 by unit. The t - 1 -> t growth is added to the spec's
                 controls: a surge in t that lowers the premium in t and then reverts makes a flow association that is
                 not a response to the premium (k100 surge plant, 150 frames: 37% rejections at 0.05 without it, 7%
                 with it). Undefined (NaN; p = 1 in Holm) when tau^2 = 0, as the EB premium is then constant
                 within year. Erosion (t = 2018-2025, eligible in t and t + 1): g_t+1 ~ g_t + inflow + g_t x inflow |
                 year FE; g_t centred within year (1/v), inflow = dshare demeaned within year; CR1 by unit. Both are
                 unweighted (unit-years count equally; weighting the flow by submissions or the erosion by 1/(v_t+1 +
                 tau^2) rejected more often in simulated null frames). With the share series fixed at their real values,
                 the flow-slope test still rejected 6-8% at 0.05 (250 frames under each of the null, persistent,
                 transient and surge plants; CR2 or a wild cluster bootstrap did not fix it) and the erosion interaction
                 4-5% (early) and 6-10% (k100): their p are approximate.
(e) surge        (k100) outcome-free first stage on topic_year_maturity, 2019-2026: log(papers + .5) ~ log(papers_t-1 +
                 .5) + log prior_growth | year FE (OLS); s = residual / its SD. LPM on decided papers 2019-2026 with an
                 author ID: accepted ~ s x incumbent + s x newcomer + newcomer + class + FM + log2 team | topic FE + year
                 FE; CR1 by topic, t(G - 1). Reading (Holm p < 0.05): competition if beta_inc < 0; dilution if beta_new
                 < 0 and beta_inc not significant; proportional allocation if neither; otherwise other. Descriptive:
                 s x maturity tercile (+ tercile dummies).
Families (Holm): per unit type {tau > 0, rho_1, b} (early map primary); {flow slope, erosion interaction} (early map);
{beta_inc, beta_new, beta_new - beta_inc}.
Robustness ((a)-(c) re-estimated; no family): composition-adjusted premia (residuals of accepted ~ class + FM + log2
team | year FE; gap = mean residual in u minus outside, as posthoc.residual_gaps, with the year's residual variance in
place of p_t(1 - p_t)); minimum cell 30; the S9 population (s9_accepted); without 2021-2022; primary_area units
2024-2026 (spread only); the seed_refit map (|k100 - seed_refit| is the noise ceiling for |early - k100|).
calibrate(): sizes and planted-effect recovery on simulated frames (see its docstring).
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
from scipy import sparse, stats
from scipy.special import expit, logit

import panel
import ph5_common
import posthoc
from common import OUTPUT, TOPICS, topic_layer
from ols import demean, fe_ols
from panel import CLASS_CONTROLS
from variants import holm

YEARS = np.arange(2018, 2027)                       # population years (columns of the cell arrays)
ALL_YEARS = np.arange(2017, 2027)                   # submission counts (shares, prior growth)
W1, W2 = (2018, 2022), (2024, 2026)
MIN_CELL, MIN_UNITS, MIN_WINDOW_SUBS = 15, 5, 50
LAGS = (1, 2, 3, 4)
UNIT_TYPES = ("early", "k100", "keywords", "areas")
TAIL = {"areas": 0.2}                               # retention tails: quintiles for the 20 areas, deciles otherwise
SURGE_YEARS = (2019, 2026)
CONTROLS = CLASS_CONTROLS + ["fm", "log2_team"]
TERCILES = ["young", "middle", "mature"]
N_GRID = np.array([10, 15, 20, 30, 50, 75, 100, 150, 200, 300, 500, 1000, 2000])
PERMS, BOOT, SEED = 200, 999, 20261017
NOTE = "post hoc exploratory (PH5 premia, selection S5); associations, not causal effects"


# ---------------------------------------------------------------------------------------------------- units and cells
def onehot(labels: pd.Series) -> tuple[list[str], sparse.csr_matrix]:
    codes, names = pd.factorize(labels, sort=True)
    rows = np.flatnonzero(codes >= 0)
    M = sparse.csr_matrix((np.ones(len(rows)), (rows, codes[rows])), shape=(len(codes), len(names)))
    return [str(x) for x in names], M


@lru_cache(maxsize=1)
def unit_sets() -> dict[str, tuple[list[str], sparse.csr_matrix]]:
    """Paper x unit memberships of every unit type, in panel.frame('k100') row order (cached). Reads no outcome."""
    k = panel.frame("k100").reset_index(drop=True)
    cat = pd.read_csv(TOPICS / "topic_catalog.csv", keep_default_na=False).set_index("topic").name
    a = posthoc.add_columns(k.copy())
    hs = pd.read_csv(TOPICS / "hindsight_assignments.csv.gz", usecols=["submission_id", "mid_seed_refit"])
    corpus = topic_layer().embedded_corpus()
    assert hs.submission_id.equals(k.submission_id)
    assert (corpus.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    pa = corpus.primary_area.fillna("").to_numpy()
    kw, K = posthoc.ph4_members(k)["K"]
    return {"early": onehot(k.topic_early),
            "k100": onehot(k.topic + " " + k.topic.map(cat)),
            "keywords": (kw, sparse.csr_matrix(K, dtype=float)),
            "areas": onehot(a.area + " " + a.area_name),
            "seed_refit": onehot("seed_" + hs.mid_seed_refit.astype(str)),
            "primary_area": onehot(pd.Series(np.where((k.year >= 2024).to_numpy() & (pa != ""), pa, None)))}


def year_matrix(yi: np.ndarray, n_years: int) -> np.ndarray:
    Y = np.zeros((len(yi), n_years))
    Y[np.arange(len(yi)), yi] = 1.0
    return Y


@lru_cache(maxsize=1)
def submissions() -> tuple[np.ndarray, dict[str, np.ndarray]]:
    """All submissions per year (ALL_YEARS) and per unit x year for every unit type (cached). Reads no outcome."""
    k = panel.frame("k100")
    Y = year_matrix(k.year.to_numpy() - ALL_YEARS[0], len(ALL_YEARS))
    return Y.sum(0), {name: M.T @ Y for name, (_, M) in unit_sets().items()}


@dataclass
class Sample:
    rows: np.ndarray           # positions in k
    y: np.ndarray              # outcome per row
    yi: np.ndarray             # year index into YEARS
    rate: float                # acceptance rate of the population (reliability, n*)
    residual: bool = False     # continuous outcome (composition-adjusted gaps)


def sample(k: pd.DataFrame, flag: str = "rq3", outcome: str = "accepted", years: tuple[int, int] = (2018, 2026),
           drop: tuple[int, ...] = ()) -> Sample:
    keep = (k[flag].astype(bool) & k.year.between(*years) & ~k.year.isin(drop)).to_numpy()
    rows = np.flatnonzero(keep)
    y = k[outcome].to_numpy(float)[rows]
    return Sample(rows, y, k.year.to_numpy()[rows] - YEARS[0], float(y.mean()))


def adjusted(k: pd.DataFrame, s: Sample) -> Sample:
    """Composition-adjusted outcome: accepted minus the fit of class + FM + log2 team (year FE absorbed)."""
    d = posthoc.add_columns(k.iloc[s.rows].copy()).reset_index(drop=True)
    X = d[CONTROLS].astype(float)
    r = fe_ols(pd.Series(s.y), X, d.year, d.submission_id)
    return Sample(s.rows, s.y - X.to_numpy() @ r.coef.to_numpy(), s.yi, s.rate, residual=True)


def cells(MT: sparse.csr_matrix, Y: np.ndarray, y: np.ndarray, residual: bool = False) -> dict[str, np.ndarray]:
    """Per unit (rows) and year (columns): papers n (n0 outside), gap g (unit minus all other papers of the year) and
    its null variance v = s2_t (1/n + 1/n0), s2_t = the year's p_t (1 - p_t) (or residual variance)."""
    Yy = Y * y[:, None]
    n1, k1 = MT @ Y, MT @ Yy
    N, K = Y.sum(0), Yy.sum(0)
    n0, k0 = N - n1, K - k1
    with np.errstate(divide="ignore", invalid="ignore"):
        s2 = ((Yy * y[:, None]).sum(0) - K ** 2 / N) / (N - 1) if residual else K / N * (1 - K / N)
        return {"n": n1, "n0": n0, "g": k1 / n1 - k0 / n0, "v": s2 * (1 / n1 + 1 / n0)}


def eligible(c: dict[str, np.ndarray], min_cell: int) -> np.ndarray:
    return (c["n"] >= min_cell) & (c["n0"] >= 2) & np.isfinite(c["v"]) & (c["v"] > 0)


# ---------------------------------------------------------------------------------------------------- estimators
def dl(g: np.ndarray, v: np.ndarray, ok: np.ndarray, F: np.ndarray, noise: bool = True) -> tuple[np.ndarray, np.ndarray]:
    """DerSimonian-Laird moment estimate (Q - (m - 1)) / C of tau^2 per year (column), NOT truncated at 0, for each row
    of unit frequency weights F (draws x units), and the number of units m (NaN below MIN_UNITS). noise=False: the
    noise-free analogue sum w (g - gbar_w)^2 / C (calibration target)."""
    w = np.where(ok, 1 / np.where(ok, v, 1.0), 0.0)
    x = np.where(ok, g, 0.0)
    m, sw, sw2, swx, swx2 = (F @ a for a in (ok.astype(float), w, w ** 2, w * x, w * x ** 2))
    with np.errstate(divide="ignore", invalid="ignore"):
        q = swx2 - swx ** 2 / sw
        t2 = ((q - (m - 1)) if noise else q) / (sw - sw2 / sw)
    return np.where(m >= MIN_UNITS, t2, np.nan), m


def pooled(t2: np.ndarray, m: np.ndarray) -> np.ndarray:
    """Unit-count-weighted mean of the yearly tau^2 (last axis); callers truncate at 0."""
    ok = np.isfinite(t2)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(ok, t2 * m, 0.0).sum(-1) / np.where(ok, m, 0.0).sum(-1)


def reml(g: np.ndarray, v: np.ndarray, tol: float = 1e-14, max_iter: int = 2000) -> float:
    """REML tau^2 by the fixed point tau^2 = sum w^2 ((g - mu)^2 - v) / sum w^2 + 1 / sum w, w = 1/(v + tau^2)."""
    t2 = max(0.0, float(np.var(g, ddof=1) - np.mean(v)))
    for _ in range(max_iter):
        w = 1 / (v + t2)
        mu = (w * g).sum() / w.sum()
        new = max(0.0, float((w ** 2 * ((g - mu) ** 2 - v)).sum() / (w ** 2).sum() + 1 / w.sum()))
        if abs(new - t2) < tol:
            return new
        t2 = new
    return t2


def cross(g: np.ndarray, v: np.ndarray, ok: np.ndarray, tau2: np.ndarray, pairs: list[tuple[int, int]],
          F: np.ndarray, noise: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray, np.ndarray, int]:
    """Signal covariance and signal variances of columns a and b over the units eligible in both, pooled over the
    pairs (a, b) weighted by overlapping units, per row of F: (cov, var_a, var_b, pairs used). noise: the variances
    removed from var_a and var_b (default v; zeros give the noise-free target)."""
    noise = v if noise is None else noise
    B = F.shape[0]
    num, da, db, mm, used = np.zeros(B), np.zeros(B), np.zeros(B), np.zeros(B), 0
    for a, b in pairs:
        both = ok[:, a] & ok[:, b]
        if not (np.isfinite(tau2[a]) and np.isfinite(tau2[b])) or both.sum() < MIN_UNITS:
            continue
        w = np.zeros(len(both))
        w[both] = 1 / np.sqrt((v[both, a] + tau2[a]) * (v[both, b] + tau2[b]))
        x, y = np.where(both, g[:, a], 0.0), np.where(both, g[:, b], 0.0)
        nx, ny = np.where(both, noise[:, a], 0.0), np.where(both, noise[:, b], 0.0)
        fw = F * w
        W, W2 = fw.sum(1), fw @ w
        m = F @ both.astype(float)
        with np.errstate(divide="ignore", invalid="ignore"):
            C = W - W2 / W
            sx, sy = fw @ x, fw @ y
            cov = (fw @ (x * y) - sx * sy / W) / C
            va = (fw @ x ** 2 - sx ** 2 / W - fw @ nx + (fw * w) @ nx / W) / C
            vb = (fw @ y ** 2 - sy ** 2 / W - fw @ ny + (fw * w) @ ny / W) / C
        live = (m >= 2) & np.isfinite(cov)
        num += np.where(live, m * cov, 0.0)
        da += np.where(live, m * va, 0.0)
        db += np.where(live, m * vb, 0.0)
        mm += np.where(live, m, 0.0)
        used += 1
    with np.errstate(divide="ignore", invalid="ignore"):
        return num / mm, da / mm, db / mm, used


def ratio(cov: np.ndarray, va: np.ndarray, vb: np.ndarray) -> np.ndarray:
    """Signal correlation, clipped to [-1, 1]; undefined (NaN) unless both signal variances exceed 1e-10."""
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where((va > 1e-10) & (vb > 1e-10), np.clip(cov / np.sqrt(np.abs(va * vb)), -1, 1), np.nan)


def permute_within(y: np.ndarray, groups: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """y shuffled at random within each group (the within-year permutation null)."""
    out = np.empty_like(y)
    out[np.argsort(groups, kind="stable")] = y[np.lexsort((rng.random(len(y)), groups))]
    return out


def counts(idx: np.ndarray, n: int) -> np.ndarray:
    """Frequency weights (draws x units) from bootstrap index draws."""
    B = idx.shape[0]
    return np.bincount((idx + n * np.arange(B)[:, None]).ravel(), minlength=B * n).reshape(B, n).astype(float)


def pct(draws: np.ndarray) -> tuple[float, float]:
    d = np.asarray(draws, float)
    d = d[np.isfinite(d)]
    return (float(np.quantile(d, 0.025)), float(np.quantile(d, 0.975))) if len(d) else (np.nan, np.nan)


def window_premia(c: dict[str, np.ndarray], years: tuple[int, int]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Paper-weighted mean of each unit's yearly gaps in the window, its variance and the unit's papers."""
    cols = (YEARS >= years[0]) & (YEARS <= years[1])
    n, g, v = c["n"][:, cols], c["g"][:, cols], c["v"][:, cols]
    has = (n > 0) & np.isfinite(g) & np.isfinite(v)
    w = np.where(has, n, 0.0)
    N = w.sum(1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return (w * np.where(has, g, 0.0)).sum(1) / N, (w ** 2 * np.where(has, v, 0.0)).sum(1) / N ** 2, N


def wls_hc3(x: np.ndarray, y: np.ndarray, w: np.ndarray) -> tuple[float, float, float, int]:
    """Slope of the WLS of y on (1, x) with an HC3 SE (scores divided by 1 - leverage) and p from t(n - 2)."""
    X = np.column_stack([np.ones_like(x), x])
    A = np.linalg.inv(X.T @ (X * w[:, None]))
    beta = A @ X.T @ (w * y)
    h = w * np.einsum("ij,jk,ik->i", X, A, X)
    sc = X * (w * (y - X @ beta) / (1 - h))[:, None]
    n = len(y)
    se = float(np.sqrt((A @ sc.T @ sc @ A)[1, 1]))
    return float(beta[1]), se, float(2 * stats.t.sf(abs(beta[1] / se), n - 2)), n - 2


def slope_draws(x: np.ndarray, y: np.ndarray, w: np.ndarray, F: np.ndarray) -> np.ndarray:
    fw = F * w
    S, sx, sy = fw.sum(1), fw @ x, fw @ y
    with np.errstate(divide="ignore", invalid="ignore"):
        return (fw @ (x * y) - sx * sy / S) / (fw @ (x * x) - sx ** 2 / S)


def select(score: np.ndarray, tie: np.ndarray, q: float, top: bool) -> np.ndarray:
    """Positions of the top (or bottom) share q of units by score, ties broken by tie; at least one."""
    order = np.lexsort((tie, score))
    j = max(1, int(np.ceil(q * len(score))))
    return order[-j:] if top else order[:j]


def winners(x: np.ndarray, vx: np.ndarray, y: np.ndarray, vy: np.ndarray, q: float, rng: np.random.Generator,
            boot: int, truth: tuple[np.ndarray, np.ndarray] | None = None) -> tuple[dict, list[dict], dict]:
    """(c) and the window version of (b) for window premia x (W1) and y (W2) of the same units: shrinkage b, window
    persistence, retention by raw and EB ranking (with targets from the true window premia if given)."""
    U = len(x)
    one = np.ones((1, U))
    tx = max(float(dl(x[:, None], vx[:, None], np.ones((U, 1), bool), one)[0][0, 0]), 0.0)
    ty = max(float(dl(y[:, None], vy[:, None], np.ones((U, 1), bool), one)[0][0, 0]), 0.0)
    xc, yc = x - (x / vx).sum() / (1 / vx).sum(), y - (y / vy).sum() / (1 / vy).sum()
    eb = tx / (tx + vx) * xc
    omega = 1 / (vy + ty)
    b, se, p, dof = wls_hc3(x, y, omega)
    idx = rng.integers(0, U, (boot, U))
    F = counts(idx, U)
    G2, V2, ok2 = np.column_stack([x, y]), np.column_stack([vx, vy]), np.ones((U, 2), bool)
    cov, va, vb, _ = cross(G2, V2, ok2, np.array([tx, ty]), [(0, 1)], one)
    rho_b = ratio(*cross(G2, V2, ok2, np.array([tx, ty]), [(0, 1)], F)[:3])
    qt = stats.t.ppf(0.975, dof)
    shrink = {"units": U, "tau_w1_pp": np.sqrt(tx) * 100, "tau_w2_pp": np.sqrt(ty) * 100, "b": b, "b_se": se,
              "b_p": p, "b_ci95_lo": b - qt * se, "b_ci95_hi": b + qt * se,
              **dict(zip(["b_boot_lo", "b_boot_hi"], pct(slope_draws(x, y, omega, F)))),
              "rho_w": float(ratio(cov, va, vb)[0]), **dict(zip(["rho_w_ci95_lo", "rho_w_ci95_hi"], pct(rho_b)))}
    if truth is not None:
        xs, ys = truth
        shrink["b_target"] = float(slope_draws(x, ys, omega, one)[0])
        shrink["rho_w_target"] = float(ratio(*cross(np.column_stack([xs, ys]), V2, ok2, np.array([tx, ty]), [(0, 1)],
                                                     one, noise=np.zeros_like(V2))[:3])[0])
        ysc = ys - (ys / vy).sum() / (1 / vy).sum()
    # bootstrap: centring, tau_W1^2 and the selection are redone in each draw
    cxb = (F @ (x / vx)) / (F @ (1 / vx))
    cyb = (F @ (y / vy)) / (F @ (1 / vy))
    txb = np.maximum(dl(x[:, None], vx[:, None], np.ones((U, 1), bool), F)[0][:, 0], 0.0)
    rows, sel = [], {}
    for ranking in ("raw", "eb"):
        for side in ("top", "bottom"):
            s = select(eb if ranking == "eb" else xc, xc, q, side == "top")
            sel[(ranking, side)] = s
            draws, draws_eb = np.empty(boot), np.empty(boot)
            for j in range(boot):
                ids = idx[j]
                xj, yj = x[ids] - cxb[j], y[ids] - cyb[j]
                ebj = txb[j] / (txb[j] + vx[ids]) * xj
                sj = select(ebj if ranking == "eb" else xj, xj, q, side == "top")
                draws[j] = yj[sj].mean() / xj[sj].mean()
                with np.errstate(divide="ignore", invalid="ignore"):
                    draws_eb[j] = yj[sj].mean() / ebj[sj].mean() if ranking == "eb" else np.nan
            r = {"ranking": ranking, "side": side, "share": q, "units_selected": len(s), "mean_w1_pp": xc[s].mean() * 100,
                 "mean_w2_pp": yc[s].mean() * 100, "mean_eb_pp": eb[s].mean() * 100, "R": yc[s].mean() / xc[s].mean(),
                 **dict(zip(["R_ci95_lo", "R_ci95_hi"], pct(draws)))}
            if ranking == "eb":
                with np.errstate(divide="ignore", invalid="ignore"):
                    r["R_vs_eb"] = yc[s].mean() / eb[s].mean()
                r["R_vs_eb_ci95_lo"], r["R_vs_eb_ci95_hi"] = pct(draws_eb)
            if truth is not None:
                r["R_target"] = ysc[s].mean() / xc[s].mean()
            rows.append(r)
    table = {"w1": xc, "w2": yc, "v1": vx, "v2": vy, "eb1": eb,
             **{f"{t}_{r}": np.isin(np.arange(U), s) for (r, t), s in sel.items()}}
    return shrink, rows, table


# ---------------------------------------------------------------------------------------------------- (a)-(c) per unit type
def analyse(units: tuple[list[str], sparse.csr_matrix], s: Sample, subs: np.ndarray, rng: np.random.Generator,
            min_cell: int = MIN_CELL, perms: int = PERMS, boot: int = BOOT, tail: float = 0.1, full: bool = True,
            p_true: np.ndarray | None = None) -> dict:
    """Spread, persistence and winner's curse for one unit type on one sample (targets from p_true if given)."""
    names, M = units
    MT = M[s.rows].T.tocsr()
    Y = year_matrix(s.yi, len(YEARS))
    c = cells(MT, Y, s.y, s.residual)
    ok_all = eligible(c, min_cell)
    used = np.flatnonzero(ok_all.any(1))
    g, v, ok = c["g"][used], c["v"][used], ok_all[used]
    U = len(used)
    one = np.ones((1, U))
    t2y, my = (a[0] for a in dl(g, v, ok, one))
    tau2 = max(float(pooled(t2y, my)), 0.0)
    tau2_w = np.where(np.isfinite(t2y), tau2, np.nan)            # persistence weights: pooled tau^2, years in (a)
    idx = rng.integers(0, U, (boot, U))
    F = counts(idx, U)
    t2b = np.maximum(pooled(*dl(g, v, ok, F)), 0.0)
    t2p = np.empty(perms)
    for i in range(perms):
        cp = cells(MT, Y, permute_within(s.y, s.yi, rng), s.residual)
        t2p[i] = max(pooled(*dl(cp["g"][used], cp["v"][used], ok, one))[0], 0.0)
    rel = lambda t2, n: t2 / (t2 + s.rate * (1 - s.rate) / n)  # noqa: E731
    nstar = lambda t2: s.rate * (1 - s.rate) / t2 if t2 > 0 else np.inf  # noqa: E731
    spread = {"units": U, "cells": int(ok.sum()), "years": int(np.isfinite(t2y).sum()), "rate": s.rate,
              "tau_pp": np.sqrt(tau2) * 100, **dict(zip(["tau_ci95_lo", "tau_ci95_hi"], np.sqrt(pct(t2b)) * 100)),
              "tau_dl_yearly_pp": np.sqrt(pooled(np.maximum(t2y, 0.0), my)) * 100,
              "tau_reml_yearly_pp": np.sqrt(pooled(np.array([reml(g[ok[:, t], t], v[ok[:, t], t]) if np.isfinite(t2y[t])
                                                             else np.nan for t in range(len(YEARS))]), my)) * 100,
              "median_v": float(np.median(v[ok])), "signal_share": tau2 / (tau2 + float(np.median(v[ok]))),
              "p_perm": float((1 + (t2p >= tau2 - 1e-14).sum()) / (1 + perms)),
              "perm_tau_q50_pp": np.sqrt(np.quantile(t2p, 0.5)) * 100,
              "perm_tau_q95_pp": np.sqrt(np.quantile(t2p, 0.95)) * 100,
              "n_star": nstar(tau2), **dict(zip(["n_star_ci95_lo", "n_star_ci95_hi"],
                                                 [nstar(t) for t in pct(t2b)[::-1]]))}
    by_year = [{"year": int(YEARS[t]), "units": int(my[t]), "tau2_moment_pp2": t2y[t] * 1e4,
                "tau_pp": np.sqrt(max(t2y[t], 0.0)) * 100 if np.isfinite(t2y[t]) else np.nan,
                "tau_reml_pp": np.sqrt(reml(g[ok[:, t], t], v[ok[:, t], t])) * 100 if np.isfinite(t2y[t]) else np.nan}
               for t in range(len(YEARS)) if my[t] > 0]
    reliability = [{"papers": int(n), "rel": rel(tau2, n), **dict(zip(["rel_ci95_lo", "rel_ci95_hi"],
                                                                       pct(rel(t2b, n))))} for n in N_GRID]
    out = {"c": c, "ok": ok_all, "tau2": tau2, "spread": spread, "by_year": by_year,
           "reliability": reliability, "names": names}
    ct = None
    if p_true is not None:
        ct = cells(MT, Y, p_true)
        spread["tau_target_pp"] = np.sqrt(max(float(pooled(*(a[0] for a in dl(ct["g"][used], v, ok, one,
                                                                                 noise=False)))), 0.0)) * 100
        out["truth"] = ct
    if not full:
        return out
    pers = []
    for h in LAGS:
        pairs = [(t, t + h) for t in range(len(YEARS) - h)]
        cov, va, vb, npairs = cross(g, v, ok, tau2_w, pairs, one)
        covb, vab, vbb, _ = cross(g, v, ok, tau2_w, pairs, F)
        sd = np.nanstd(covb, ddof=1)
        r = {"lag": str(h), "pairs": npairs, "cov_pp2": cov[0] * 1e4, "rho": float(ratio(cov, va, vb)[0]),
             **dict(zip(["rho_ci95_lo", "rho_ci95_hi"], pct(ratio(covb, vab, vbb)))),
             "rho_defined_share": float(np.isfinite(ratio(covb, vab, vbb)).mean()),
             "rho_clipped_share": float((np.abs(ratio(covb, vab, vbb)) == 1).mean()),
             "p_cov": float(2 * stats.norm.sf(abs(cov[0] / sd))) if sd > 0 else np.nan}
        if ct is not None:
            r["rho_target"] = float(ratio(*cross(ct["g"][used], v, ok, tau2_w, pairs, one, noise=np.zeros_like(v))[:3])[0])
        pers.append(r)
    x, vx, nx = window_premia(c, W1)
    y, vy, ny = window_premia(c, W2)
    sw = lambda w: subs[:, (ALL_YEARS >= w[0]) & (ALL_YEARS <= w[1])].sum(1)  # noqa: E731
    sub1, sub2 = sw(W1), sw(W2)
    E = np.flatnonzero((sub1 >= MIN_WINDOW_SUBS) & (sub2 >= MIN_WINDOW_SUBS) & (nx >= min_cell) & (ny >= min_cell)
                       & np.isfinite(vx) & np.isfinite(vy) & (vx > 0) & (vy > 0))
    truth = None if ct is None else (window_premia(ct, W1)[0][E], window_premia(ct, W2)[0][E])
    shrink, retention, table = winners(x[E], vx[E], y[E], vy[E], tail, rng, boot, truth)
    pers.append({"lag": "W1->W2", "pairs": 1, "cov_pp2": np.nan, "rho": shrink["rho_w"],
                 "rho_ci95_lo": shrink["rho_w_ci95_lo"], "rho_ci95_hi": shrink["rho_w_ci95_hi"],
                 **({"rho_target": shrink["rho_w_target"]} if ct is not None else {})})
    windows = pd.DataFrame({"unit": np.array(names)[E], "subs_w1": sub1[E], "subs_w2": sub2[E], "papers_w1": nx[E],
                            "papers_w2": ny[E], **table})
    return {**out, "persistence": pers, "shrinkage": shrink, "retention": retention, "windows": windows}


# ---------------------------------------------------------------------------------------------------- (d) flows, (e) surge
@dataclass
class Fit:
    beta: pd.Series
    V: pd.DataFrame
    G: int
    n: int

    def term(self, weights: dict[str, float]) -> dict:
        """Linear combination of coefficients: coef, se, p and 95% CI with t(G - 1); NaN if a term was dropped."""
        dof = self.G - 1
        if not set(weights) <= set(self.beta.index):
            return {"coef": np.nan, "se": np.nan, "p": np.nan, "ci95_lo": np.nan, "ci95_hi": np.nan, "dof": dof}
        a = pd.Series(weights).reindex(self.beta.index).fillna(0.0).to_numpy()
        coef, se = float(a @ self.beta.to_numpy()), float(np.sqrt(a @ self.V.to_numpy() @ a))
        q = stats.t.ppf(0.975, dof)
        return {"coef": coef, "se": se, "p": float(2 * stats.t.sf(abs(coef / se), dof)) if se > 0 else np.nan,
                "ci95_lo": coef - q * se, "ci95_hi": coef + q * se, "dof": dof}


def fit_fe(d: pd.DataFrame, y: str, xs: list[str], fes: list[str], cluster: str, w: str | None = None) -> Fit:
    """posthoc.wls_fe with the full CR1 covariance: WLS with absorbed fixed effects (posthoc.twfe), clusters `cluster`."""
    d = posthoc.drop_singletons(d.dropna(subset=[y, *xs]), fes).reset_index(drop=True)
    wv = np.ones(len(d)) if w is None else d[w].to_numpy(float)
    yd, Xd = posthoc.twfe(d[y].to_numpy(float), d[xs].to_numpy(float), [d[f].to_numpy() for f in fes], wv)
    keep = Xd.std(axis=0) > 1e-12
    xs, Xd = [x for x, kept in zip(xs, keep) if kept], Xd[:, keep]
    A = np.linalg.pinv(Xd.T @ (Xd * wv[:, None]))
    beta = A @ (Xd * wv[:, None]).T @ yd
    cg = pd.factorize(d[cluster])[0]
    G, (n, kx) = int(cg.max() + 1), Xd.shape
    S = np.zeros((G, kx))
    np.add.at(S, cg, Xd * (wv * (yd - Xd @ beta))[:, None])
    V = G / (G - 1) * (n - 1) / (n - kx) * A @ S.T @ S @ A
    return Fit(pd.Series(beta, xs), pd.DataFrame(V, xs, xs), G, n)


FLOW_X = ["eb10", "growth", "prior_growth", "lshare"]


def flow_panel(a: dict, subs: np.ndarray, totals: np.ndarray) -> pd.DataFrame:
    """Unit-years t = 2018-2025 with an eligible cell: share change t -> t + 1, growth t - 1 -> t, prior growth
    t - 2 -> t - 1, EB premium, next year's gap."""
    c, ok, tau2 = a["c"], a["ok"], a["tau2"]
    lshare = np.log((subs + 0.5) / totals)
    frames = []
    for j, t in enumerate(YEARS[:-1]):
        u, jj = np.flatnonzero(ok[:, j]), t - ALL_YEARS[0]
        if not len(u):
            continue
        g, v = c["g"][u, j], c["v"][u, j]
        wre = 1 / (v + tau2)
        mu = (wre * g).sum() / wre.sum()
        f = pd.DataFrame({"unit": u, "year": t, "papers": subs[u, jj], "lshare": lshare[u, jj],
                          "dshare": lshare[u, jj + 1] - lshare[u, jj], "growth": lshare[u, jj] - lshare[u, jj - 1],
                          "prior_growth": lshare[u, jj - 1] - lshare[u, jj - 2] if jj >= 2 else np.nan,
                          "g": g, "gc": g - (g / v).sum() / (1 / v).sum(), "eb10": (mu + tau2 / (tau2 + v) * (g - mu)) * 10,
                          "next_ok": ok[u, j + 1], "g_next": c["g"][u, j + 1]})
        if "truth" in a:
            f["g_next_true"] = a["truth"]["g"][u, j + 1]
        frames.append(f)
    return pd.concat(frames, ignore_index=True)


def flows(a: dict, subs: np.ndarray, totals: np.ndarray, unit_type: str) -> list[dict]:
    """(d): flow slope (dshare on the EB premium) and the erosion interaction for one unit type."""
    p = flow_panel(a, subs, totals)
    f = fit_fe(p, "dshare", FLOW_X, ["year"], "unit")
    e = p[p.next_ok].copy()
    e["inflow"] = e.dshare - e.groupby("year").dshare.transform("mean")
    e["gc_x_inflow"] = e.gc * e.inflow
    xs = ["gc", "inflow", "gc_x_inflow"]
    fe = fit_fe(e, "g_next", xs, ["year"], "unit")
    rows = [{"unit_type": unit_type, "model": "flow", "term": "eb10", "rows": f.n, "units": f.G, **f.term({"eb10": 1})}]
    for x in FLOW_X[1:]:
        rows.append({"unit_type": unit_type, "model": "flow", "term": x, "rows": f.n, "units": f.G, **f.term({x: 1})})
    for x in xs:
        rows.append({"unit_type": unit_type, "model": "erosion", "term": x, "rows": fe.n, "units": fe.G, **fe.term({x: 1})})
    if "g_next_true" in e:                  # calibration: shares are fixed data, so the flow target is 0
        rows[0]["target"] = 0.0
        rows[-1]["target"] = fit_fe(e, "g_next_true", xs, ["year"], "unit").term({"gc_x_inflow": 1})["coef"]
    return rows


@lru_cache(maxsize=1)
def first_stage() -> tuple[pd.DataFrame, dict]:
    """Outcome-free surge first stage (k100, 2019-2026): standardised residual s of log papers on last year's log
    papers and log prior growth, year FE (OLS; CR1 by topic for the reported SEs)."""
    m = pd.read_csv(OUTPUT / "topic_year_maturity.csv.gz")
    m = m[m["map"] == "k100"].assign(topic=lambda x: x.topic.astype(str))
    prev = m[["topic", "year", "papers"]].assign(year=m.year + 1).rename(columns={"papers": "papers_prev"})
    d = m.merge(prev, on=["topic", "year"], how="left", validate="1:1")
    d = d[d.year.between(*SURGE_YEARS)].reset_index(drop=True)
    d["log_papers"], d["log_prev"] = np.log(d.papers + 0.5), np.log(d.papers_prev + 0.5)
    d["log_prior_growth"] = np.log(d.prior_growth)
    xs = ["log_prev", "log_prior_growth"]
    r = fe_ols(d.log_papers, d[xs], d.year, d.topic)
    yd = demean(d.log_papers.to_numpy(float), d.year.to_numpy())
    e = yd - demean(d[xs].to_numpy(float), d.year.to_numpy()) @ r.coef.to_numpy()
    d["resid"], d["s"] = e, e / e.std(ddof=1)
    info = {"topic_years": int(len(d)), "residual_sd": float(e.std(ddof=1)), "within_r2": float(1 - (e ** 2).sum() /
            (yd ** 2).sum()), **{f"{x}_{c}": float(r.loc[x, c]) for x in xs for c in ("coef", "se")},
            "largest_surges": d.nlargest(5, "s")[["topic", "year", "papers", "papers_prev", "s"]].round(3).to_dict("records")}
    return d[["topic", "year", "papers", "papers_prev", "prior_growth", "resid", "s"]], info


def surge_frame(k: pd.DataFrame) -> pd.DataFrame:
    keep = k.rq3.astype(bool) & k.year.between(*SURGE_YEARS) & k.has_author_key & (k.team_size >= 1)
    d = posthoc.add_columns(k[keep].copy())
    d = d.merge(first_stage()[0][["topic", "year", "s"]], on=["topic", "year"], how="left", validate="m:1")
    d = d[d.s.notna() & d.newcomer.notna()].copy()
    d["s_inc"], d["s_new"] = d.s * d.incumbent, d.s * d.newcomer
    for t in TERCILES:
        d[f"s_{t}"] = d.s * (d.maturity_tercile == t)
        d[f"mt_{t}"] = (d.maturity_tercile == t).astype(float)
    return d


SURGE_TESTS = {"beta_inc": {"s_inc": 1}, "beta_new": {"s_new": 1}, "beta_new - beta_inc": {"s_new": 1, "s_inc": -1}}


def read_surge(inc: tuple[bool, float], new: tuple[bool, float]) -> str:
    """Declared reading from (Holm-significant, coefficient) of beta_inc and beta_new."""
    return ("competition" if inc[0] and inc[1] < 0 else
            "dilution" if not inc[0] and new[0] and new[1] < 0 else
            "proportional allocation" if not inc[0] and not new[0] else "other")


def surge(k: pd.DataFrame, descriptive: bool = True) -> tuple[list[dict], str]:
    """(e): the declared LPM (pp per SD of surge) with the reading rule, and s x maturity tercile (descriptive)."""
    d = surge_frame(k)
    xs = ["s_inc", "s_new", "newcomer"] + CONTROLS
    f = fit_fe(d, "accepted", xs, ["topic", "year"], "topic")
    tf = fit_fe(d, "p_true", xs, ["topic", "year"], "topic") if "p_true" in d else None
    rows = []
    for name, wts in SURGE_TESTS.items():
        r = {"model": "declared", "term": name, "rows": f.n, "topics": f.G, **scale(f.term(wts), 100)}
        if tf is not None:
            r["target"] = tf.term(wts)["coef"] * 100
        rows.append(r)
    ps = pd.Series([r["p"] for r in rows]).fillna(1.0)
    for r, ph in zip(rows, holm(ps)):
        r["p_holm"] = float(ph)
    reading = read_surge(*((r["p_holm"] < 0.05, r["coef"]) for r in rows[:2]))
    if descriptive:
        xm = [f"s_{t}" for t in TERCILES] + ["mt_middle", "mt_mature", "newcomer"] + CONTROLS
        fm = fit_fe(d, "accepted", xm, ["topic", "year"], "topic")
        rows += [{"model": "maturity tercile (descriptive)", "term": f"s x {t}", "rows": fm.n, "topics": fm.G,
                  "papers_in_tercile": int((d.maturity_tercile == t).sum()), **scale(fm.term({f"s_{t}": 1}), 100)}
                 for t in TERCILES]
    return rows, reading


def scale(r: dict, f: float) -> dict:
    return {key: (val * f if key in ("coef", "se", "ci95_lo", "ci95_hi") else val) for key, val in r.items()}


# ---------------------------------------------------------------------------------------------------- assembly
def primary(k: pd.DataFrame, perms: int = PERMS, boot: int = BOOT, descriptive: bool = True) -> dict:
    """The declared analyses (a)-(e) on the main sample; with a p_true column in k, also their targets."""
    sets, (totals, subs) = unit_sets(), submissions()
    s = sample(k)
    p_true = k.p_true.to_numpy(float)[s.rows] if "p_true" in k else None
    main = {ut: analyse(sets[ut], s, subs[ut], np.random.default_rng([SEED, j]), perms=perms, boot=boot,
                        tail=TAIL.get(ut, 0.1), p_true=p_true) for j, ut in enumerate(UNIT_TYPES)}
    flow_rows = flows(main["early"], subs["early"], totals, "early") + flows(main["k100"], subs["k100"], totals, "k100")
    surge_rows, reading = surge(k, descriptive)
    return {"sample": s, "main": main, "flows": flow_rows, "surge": surge_rows, "reading": reading}


def estimates(res: dict) -> pd.DataFrame:
    """Declared tests (family set, Holm within family) and the other estimates checked in calibration."""
    rows = []
    for ut in UNIT_TYPES:
        a = res["main"][ut]
        sp, sh, p1 = a["spread"], a["shrinkage"], a["persistence"][0]
        rows += [{"family": f"F-{ut}", "unit_type": ut, "test": "tau > 0 (pp)", "estimate": sp["tau_pp"],
                  "ci95_lo": sp["tau_ci95_lo"], "ci95_hi": sp["tau_ci95_hi"], "p": sp["p_perm"],
                  "target": sp.get("tau_target_pp")},
                 {"family": f"F-{ut}", "unit_type": ut, "test": "rho_1", "estimate": p1["rho"], "ci95_lo": p1["rho_ci95_lo"],
                  "ci95_hi": p1["rho_ci95_hi"], "p": p1["p_cov"], "target": p1.get("rho_target")},
                 {"family": f"F-{ut}", "unit_type": ut, "test": "b", "estimate": sh["b"], "ci95_lo": sh["b_ci95_lo"],
                  "ci95_hi": sh["b_ci95_hi"], "p": sh["b_p"], "target": sh.get("b_target")}]
        rows += [{"family": "", "unit_type": ut, "test": f"rho_{r['lag']}", "estimate": r["rho"], "ci95_lo": r["rho_ci95_lo"],
                  "ci95_hi": r["rho_ci95_hi"], "p": r.get("p_cov", np.nan), "target": r.get("rho_target")}
                 for r in a["persistence"][1:]]
        rows += [{"family": "", "unit_type": ut, "test": f"R {r['side']} {r['ranking']}", "estimate": r["R"],
                  "ci95_lo": r["R_ci95_lo"], "ci95_hi": r["R_ci95_hi"], "p": np.nan, "target": r.get("R_target")}
                 for r in a["retention"]]
    for r in res["flows"]:
        if r["term"] in ("eb10", "gc_x_inflow"):
            rows.append({"family": "F-flows" if r["unit_type"] == "early" else "", "unit_type": r["unit_type"],
                         "test": "flow slope (per 10 pp)" if r["term"] == "eb10" else "erosion interaction",
                         "estimate": r["coef"],
                         "ci95_lo": r["ci95_lo"], "ci95_hi": r["ci95_hi"], "p": r["p"], "target": r.get("target")})
    rows += [{"family": "F-surge", "unit_type": "k100", "test": r["term"] + " (pp per SD)", "estimate": r["coef"],
              "ci95_lo": r["ci95_lo"], "ci95_hi": r["ci95_hi"], "p": r["p"], "target": r.get("target")}
             for r in res["surge"] if r["model"] == "declared"]
    t = pd.DataFrame(rows)
    t["target"] = t.target.astype(float)
    for fam, g in t[t.family != ""].groupby("family"):
        t.loc[g.index, "p_holm"] = holm(g.p.fillna(1.0)).to_numpy()
    return t


def robust_row(variant: str, unit_type: str, a: dict) -> dict:
    sp = a["spread"]
    r = {"variant": variant, "unit_type": unit_type, **{x: sp[x] for x in ("units", "cells", "tau_pp", "tau_ci95_lo",
         "tau_ci95_hi", "tau_dl_yearly_pp", "tau_reml_yearly_pp", "signal_share", "p_perm", "n_star")}}
    if "persistence" in a:
        p1, sh = a["persistence"][0], a["shrinkage"]
        r.update({"rho_1": p1["rho"], "rho_1_ci95_lo": p1["rho_ci95_lo"], "rho_1_ci95_hi": p1["rho_ci95_hi"],
                  "rho_1_p": p1["p_cov"], "window_units": sh["units"], "b": sh["b"], "b_ci95_lo": sh["b_ci95_lo"],
                  "b_ci95_hi": sh["b_ci95_hi"], "b_p": sh["b_p"], "rho_w": sh["rho_w"]})
    return r


def robustness(k: pd.DataFrame, res: dict) -> tuple[pd.DataFrame, dict]:
    sets, (_, subs) = unit_sets(), submissions()
    base = res["sample"]
    rows = [robust_row("main", ut, res["main"][ut]) for ut in UNIT_TYPES]
    variants = {"composition_adjusted": (adjusted(k, base), MIN_CELL), "min_cell_30": (base, 30),
                "s9": (sample(k, "s9", "s9_accepted"), MIN_CELL), "without_2021_22": (sample(k, drop=(2021, 2022)), MIN_CELL)}
    for i, (name, (s, mc)) in enumerate(variants.items()):
        for j, ut in enumerate(UNIT_TYPES):
            a = analyse(sets[ut], s, subs[ut], np.random.default_rng([SEED, 10 + i, j]), min_cell=mc,
                        tail=TAIL.get(ut, 0.1))
            rows.append(robust_row(name, ut, a))
    rows.append(robust_row("seed_refit_map", "seed_refit",
                           analyse(sets["seed_refit"], base, subs["seed_refit"], np.random.default_rng([SEED, 20]))))
    rows.append(robust_row("primary_area_2024_26", "primary_area",
                           analyse(sets["primary_area"], sample(k, years=(2024, 2026)), subs["primary_area"],
                                   np.random.default_rng([SEED, 21]), full=False)))
    t = pd.DataFrame(rows)
    get = lambda v, u, x: float(t[(t.variant == v) & (t.unit_type == u)][x].iloc[0])  # noqa: E731
    noise = {x: {"early_minus_k100": get("main", "early", x) - get("main", "k100", x),
                 "k100_minus_seed_refit": get("main", "k100", x) - get("seed_refit_map", "seed_refit", x)}
             for x in ("tau_pp", "rho_1", "b")}
    for d in noise.values():
        d["map_difference_exceeds_refit_noise"] = bool(abs(d["early_minus_k100"]) > abs(d["k100_minus_seed_refit"]))
    return t, noise


def compute_free() -> dict:
    """Outcome-free parts: the surge first stage and the unit counts per window (all submissions)."""
    fs, info = first_stage()
    totals, subs = submissions()
    rows = []
    for name, (names, _) in unit_sets().items():
        S = subs[name]
        sw = lambda w: S[:, (ALL_YEARS >= w[0]) & (ALL_YEARS <= w[1])].sum(1)  # noqa: E731
        rows.append({"unit_type": name, "units": len(names), "units_ge50_both_windows":
                     int(((sw(W1) >= MIN_WINDOW_SUBS) & (sw(W2) >= MIN_WINDOW_SUBS)).sum()),
                     **{f"units_ge{MIN_CELL}_subs_{y}": int((S[:, y - ALL_YEARS[0]] >= MIN_CELL).sum()) for y in YEARS}})
    return {"free_surge_first_stage": fs, "free_units": pd.DataFrame(rows),
            "free_summary": {"first_stage": info, "submissions_by_year": dict(zip(ALL_YEARS.tolist(), totals.tolist()))}}


def compute(k: pd.DataFrame) -> dict:
    k = k.reset_index(drop=True)
    assert (k.submission_id.to_numpy() == panel.frame("k100").submission_id.to_numpy()).all()
    res = primary(k)
    tests = estimates(res)
    rob, noise = robustness(k, res)
    main = res["main"]
    tag = lambda rows, ut: [{"unit_type": ut, **r} for r in rows]  # noqa: E731
    cells_ = []
    for ut in UNIT_TYPES:
        c, names = main[ut]["c"], np.array(main[ut]["names"])
        u, t = np.nonzero(c["n"] > 0)
        cells_.append(pd.DataFrame({"unit_type": ut, "unit": names[u], "year": YEARS[t], "papers": c["n"][u, t],
                                    "gap": c["g"][u, t], "var": c["v"][u, t], "eligible": main[ut]["ok"][u, t]}))
    head = {ut: {"tau_pp": main[ut]["spread"]["tau_pp"], "tau_ci95": [main[ut]["spread"]["tau_ci95_lo"],
                                                                      main[ut]["spread"]["tau_ci95_hi"]],
                 "p_perm": main[ut]["spread"]["p_perm"], "signal_share": main[ut]["spread"]["signal_share"],
                 "n_star": main[ut]["spread"]["n_star"], "rho_1": main[ut]["persistence"][0]["rho"],
                 "rho_w": main[ut]["shrinkage"]["rho_w"], "b": main[ut]["shrinkage"]["b"],
                 "window_units": main[ut]["shrinkage"]["units"],
                 "retention": {f"{r['side']} {r['ranking']}": r["R"] for r in main[ut]["retention"]}}
            for ut in UNIT_TYPES}
    summary = {"population": "RQ3 decided papers 2018-2026", "papers": int(len(res["sample"].rows)),
               "acceptance_rate": res["sample"].rate, "windows": {"W1": list(W1), "W2": list(W2)},
               "min_cell": MIN_CELL, "min_units_per_year": MIN_UNITS, "permutations": PERMS, "bootstraps": BOOT,
               "headline": head, "surge_reading": res["reading"], "map_noise": noise,
               "tests": tests[tests.family != ""][["family", "test", "estimate", "p", "p_holm"]].to_dict("records"),
               "note": NOTE}
    return {"tests": tests,
            "spread": pd.DataFrame([{"unit_type": ut, **main[ut]["spread"]} for ut in UNIT_TYPES]),
            "spread_by_year": pd.DataFrame(sum((tag(main[ut]["by_year"], ut) for ut in UNIT_TYPES), [])),
            "persistence": pd.DataFrame(sum((tag(main[ut]["persistence"], ut) for ut in UNIT_TYPES), [])),
            "shrinkage": pd.DataFrame([{"unit_type": ut, **main[ut]["shrinkage"]} for ut in UNIT_TYPES]),
            "retention": pd.DataFrame(sum((tag(main[ut]["retention"], ut) for ut in UNIT_TYPES), [])),
            "windows": pd.concat([main[ut]["windows"].assign(unit_type=ut) for ut in UNIT_TYPES], ignore_index=True),
            "reliability": pd.DataFrame(sum((tag(main[ut]["reliability"], ut) for ut in UNIT_TYPES), [])),
            "cells": pd.concat(cells_, ignore_index=True), "flows": pd.DataFrame(res["flows"]),
            "surge": pd.DataFrame(res["surge"]), "robustness": rob, **compute_free(), "summary": summary}


# ---------------------------------------------------------------------------------------------------- calibration
BASE_RATES = dict(zip(range(2017, 2027), np.linspace(0.45, 0.32, 10)))   # mirrors ph5_common.fake_outcomes
PLANT_SD, AR_RHO, SURGE_PENALTY = 0.25, 0.5, -0.15


def persistent(seed: int) -> Callable[[pd.DataFrame], np.ndarray]:
    """Early-map topic log-odds ~ N(0, PLANT_SD^2), constant over years."""
    def plant(k: pd.DataFrame) -> np.ndarray:
        topics = np.sort(k.topic_early.unique())
        a = np.random.default_rng([seed, 1]).normal(0, PLANT_SD, len(topics))
        return k.topic_early.map(dict(zip(topics, a))).to_numpy(float)
    return plant


def ar1(seed: int, rho: float = AR_RHO) -> Callable[[pd.DataFrame], np.ndarray]:
    """Early-map topic log-odds following a stationary AR(1) over years (sd PLANT_SD, autocorrelation rho; rho = 0
    gives independent yearly premia: a real spread without persistence, the null of rho_1 and b)."""
    def plant(k: pd.DataFrame) -> np.ndarray:
        topics = np.sort(k.topic_early.unique())
        rng = np.random.default_rng([seed, 2])
        a = np.zeros((len(topics), len(ALL_YEARS)))
        a[:, 0] = rng.normal(0, PLANT_SD, len(topics))
        for j in range(1, len(ALL_YEARS)):
            a[:, j] = rho * a[:, j - 1] + np.sqrt(1 - rho ** 2) * rng.normal(0, PLANT_SD, len(topics))
        return a[np.searchsorted(topics, k.topic_early.to_numpy()), k.year.to_numpy() - ALL_YEARS[0]]
    return plant


def transient(seed: int) -> Callable[[pd.DataFrame], np.ndarray]:
    return ar1(seed, 0.0)


def surge_plant(seed: int) -> Callable[[pd.DataFrame], np.ndarray]:
    """SURGE_PENALTY log-odds per SD of the k100 surge s, for topic newcomers only."""
    def plant(k: pd.DataFrame) -> np.ndarray:
        s = first_stage()[0].set_index(["topic", "year"]).s
        sv = s.reindex(pd.MultiIndex.from_arrays([k.topic, k.year])).fillna(0.0).to_numpy()
        return SURGE_PENALTY * sv * k.newcomer.fillna(0.0).to_numpy(float)
    return plant


PLANTS: dict[str, Callable[[int], Callable[[pd.DataFrame], np.ndarray]] | None] = {
    "null": None, "persistent": persistent, "ar1": ar1, "transient": transient, "surge_newcomers": surge_plant}


def true_prob(k: pd.DataFrame, plant: Callable[[pd.DataFrame], np.ndarray] | None) -> np.ndarray:
    eta = logit(k.year.map(BASE_RATES).fillna(0.4).to_numpy(float))
    return expit(eta if plant is None else eta + plant(k))


def calibrate(n_null: int = 200, n_planted: int = 50, seed: int = 0) -> dict:
    """Run the declared analyses on simulated frames: null (acceptance by year only), a persistent early-map topic
    effect, an AR(1) early-map topic effect, independent yearly early-map topic effects (transient: a spread without
    persistence, the null of rho_1 and b) and a surge penalty for newcomers. Per plant, unit type and estimate:
    rejection rate at 0.05 (raw and Holm within the declared family; an undefined estimate does not reject), mean
    estimate, mean target (the same estimator's noise-free value from the true probabilities on the same sample, e.g.
    tau of the true premia, b of the true W2 premia on the observed W1 premia), bias, 95% CI coverage of the target
    (frames with a defined estimate) and the share of frames with a defined estimate; per family, the share of frames
    with any Holm rejection; per plant, the shares of the surge readings."""
    rows, readings = [], []
    for j, (name, make) in enumerate(PLANTS.items()):
        for i in range(n_null if make is None else n_planted):
            s = seed + 10_000 * j + i
            plant = None if make is None else make(s)
            k = ph5_common.simulated_frame(s, plant)
            res = primary(k.assign(p_true=true_prob(k, plant)), descriptive=False)
            rows += [{"plant": name, "frame": s, **r} for r in estimates(res).to_dict("records")]
            readings.append({"plant": name, "reading": res["reading"]})
    r = pd.DataFrame(rows)
    r["reject"] = r.p < 0.05
    r["reject_holm"] = r.p_holm < 0.05
    r["defined"] = np.isfinite(r.estimate)
    r["covered"] = np.where(r.target.notna() & r.defined, (r.ci95_lo <= r.target) & (r.target <= r.ci95_hi), np.nan)
    per = (r.groupby(["plant", "unit_type", "test"], sort=False)
           .agg(frames=("frame", "size"), defined=("defined", "mean"), reject=("reject", "mean"),
                reject_holm=("reject_holm", "mean"), mean_estimate=("estimate", "mean"),
                median_estimate=("estimate", "median"), mean_target=("target", "mean"), coverage=("covered", "mean"))
           .reset_index())
    per["bias"] = per.mean_estimate - per.mean_target
    fam = (r[r.family != ""].groupby(["plant", "family", "frame"]).reject_holm.any()
           .groupby(["plant", "family"]).mean())
    return {"per_test": per.to_dict("records"),
            "family_any_holm_rejection": [{"plant": p, "family": f, "rate": float(v)} for (p, f), v in fam.items()],
            "surge_readings": pd.crosstab(pd.DataFrame(readings).plant, pd.DataFrame(readings).reading,
                                          normalize="index").round(4).to_dict("index"),
            "n_null": n_null, "n_planted": n_planted, "seed": seed,
            "plants": {"persistent_sd": PLANT_SD, "ar1_rho": AR_RHO, "surge_newcomer_log_odds_per_sd": SURGE_PENALTY}}


# ---------------------------------------------------------------------------------------------------- figures
LABELS = {"early": "early map (prospective)", "k100": "k100 (hindsight)", "keywords": "author keywords",
          "areas": "coarse areas"}


def plot(out_dir: Path) -> None:
    import figures
    plt = figures.plt
    out_dir = Path(out_dir)
    summary = json.loads((out_dir / "summary.json").read_text())["summary"]
    rate = summary["acceptance_rate"]
    spread = pd.read_csv(out_dir / "spread.csv").set_index("unit_type")
    cells_ = pd.read_csv(out_dir / "cells.csv")

    fig, axes = plt.subplots(2, 2, figsize=(7.4, 5.4), sharey=True, constrained_layout=True)
    for ax, ut in zip(axes.flat, UNIT_TYPES):
        c, sp = cells_[(cells_.unit_type == ut) & cells_.eligible], spread.loc[ut]
        n = np.geomspace(MIN_CELL, max(c.papers.max(), MIN_CELL * 2), 100)
        se = np.sqrt(rate * (1 - rate) / n)
        tau, tq = sp.tau_pp / 100, sp.perm_tau_q95_pp / 100
        ax.fill_between(n, -1.96 * np.sqrt(se ** 2 + tau ** 2) * 100, 1.96 * np.sqrt(se ** 2 + tau ** 2) * 100,
                        color=figures.SERIES[0], alpha=0.14, lw=0, label=f"noise + tau ({sp.tau_pp:.1f} pp)")
        for sgn in (-1, 1):
            ax.plot(n, sgn * 1.96 * se * 100, color=figures.INK2, lw=0.8, ls=(0, (3, 2)),
                    label="binomial noise only" if sgn == 1 else None)
            ax.plot(n, sgn * 1.96 * np.sqrt(se ** 2 + tq ** 2) * 100, color=figures.MUTED, lw=0.7,
                    label="permutation null, 95th pct tau" if sgn == 1 else None)
        ax.scatter(c.papers, c.gap * 100, s=6, color=figures.SERIES[0], alpha=0.55, lw=0)
        ax.axhline(0, color=figures.INK2, lw=0.6)
        ax.set_xscale("log")
        ax.set_title(f"{LABELS[ut]}: tau {sp.tau_pp:.1f} pp [{sp.tau_ci95_lo:.1f}, {sp.tau_ci95_hi:.1f}], "
                     f"p_perm {sp.p_perm:.3f}", loc="left", fontsize=7.2)
        ax.set_xlabel("decided papers in the unit-year")
    axes[0, 0].set_ylabel("premium vs other papers of the year (pp)")
    axes[1, 0].set_ylabel("premium vs other papers of the year (pp)")
    axes[0, 0].legend(fontsize=6.3, loc="upper right")
    fig.suptitle("PH5 premia: funnel of unit-year acceptance premia (95% bands; post hoc, exploratory)", x=0.01,
                 ha="left", fontsize=7.5)
    _save(fig, out_dir, "PH5_premia_funnel")

    pers = pd.read_csv(out_dir / "persistence.csv", dtype={"lag": str})
    fig, ax = plt.subplots(figsize=(5.4, 3.2), constrained_layout=True)
    lags = [str(h) for h in LAGS] + ["W1->W2"]
    for i, ut in enumerate(UNIT_TYPES):
        p = pers[pers.unit_type == ut].set_index("lag").reindex(lags)
        x = np.arange(len(lags)) + (i - 1.5) * 0.12
        err = np.clip([p.rho - p.rho_ci95_lo, p.rho_ci95_hi - p.rho], 0, None)   # a percentile CI may miss rho
        ax.errorbar(x, p.rho, yerr=err, fmt="o-" if i < 3 else "o:", ms=3.5,
                    color=figures.SERIES[i], lw=1, capsize=0, label=LABELS[ut])
    ax.axhline(0, color=figures.INK2, lw=0.6)
    ax.axhline(1, color=figures.MUTED, lw=0.6, ls=(0, (3, 2)))
    ax.set_xticks(np.arange(len(lags)), [f"lag {h}" for h in LAGS] + ["2018-22 -> 2024-26"])
    ax.set_ylabel("signal correlation rho (95% CI)")
    ax.set_title("Persistence of the noise-free premium across years", loc="left")
    ax.legend(fontsize=6.5)
    _save(fig, out_dir, "PH5_premia_persistence")

    win, ret = pd.read_csv(out_dir / "windows.csv"), pd.read_csv(out_dir / "retention.csv")
    shr, rel = pd.read_csv(out_dir / "shrinkage.csv").set_index("unit_type"), pd.read_csv(out_dir / "reliability.csv")
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 2.9), constrained_layout=True, gridspec_kw={"width_ratios": [1, 1.25, 1]})
    ax, w = axes[0], win[win.unit_type == "early"]
    ax.scatter(w.w1 * 100, w.w2 * 100, s=8 + 40 * np.sqrt(w.papers_w2 / w.papers_w2.max()), color=figures.SERIES[0],
               alpha=0.6, lw=0)
    lim = np.array([w.w1.min(), w.w1.max()]) * 100
    ax.plot(lim, lim, color=figures.MUTED, lw=0.7, ls=(0, (3, 2)), label="no shrinkage")
    ax.plot(lim, shr.loc["early", "b"] * lim, color=figures.SERIES[1], lw=1.4, label=f"b = {shr.loc['early', 'b']:.2f}")
    ax.set_xlabel("2018-2022 premium (pp)")
    ax.set_ylabel("2024-2026 premium (pp)")
    ax.set_title("Early-map topics", loc="left")
    ax.legend(fontsize=6.5)
    ax = axes[1]
    groups = [(ut, rk, tl) for ut in UNIT_TYPES for rk in ("raw", "eb") for tl in ("top", "bottom")]
    for i, (ut, rk, tl) in enumerate(groups):
        r = ret[(ret.unit_type == ut) & (ret.ranking == rk) & (ret.side == tl)].iloc[0]
        ax.barh(-i, r.R, color=figures.SERIES[UNIT_TYPES.index(ut)], alpha=0.85 if rk == "eb" else 0.45, height=0.8)
        ax.plot([r.R_ci95_lo, r.R_ci95_hi], [-i, -i], color=figures.INK2, lw=0.8)
    ax.set_yticks(-np.arange(len(groups)), [f"{ut} {rk} {tl}" for ut, rk, tl in groups], fontsize=5.6)
    ax.axvline(0, color=figures.INK2, lw=0.6)
    ax.axvline(1, color=figures.MUTED, lw=0.6, ls=(0, (3, 2)))
    ax.set_xlabel("retention R = W2 / W1 premium (95% CI)")
    ax.set_title("Extreme tails: share of the edge kept", loc="left")
    ax = axes[2]
    for i, ut in enumerate(UNIT_TYPES):
        r = rel[rel.unit_type == ut]
        ax.plot(r.papers, r.rel, color=figures.SERIES[i], lw=1.2, label=LABELS[ut])
        ax.fill_between(r.papers, r.rel_ci95_lo, r.rel_ci95_hi, color=figures.SERIES[i], alpha=0.1, lw=0)
    ax.axhline(0.5, color=figures.MUTED, lw=0.6, ls=(0, (3, 2)))
    ax.set_xscale("log")
    ax.set_ylim(0, 1)
    ax.set_xlabel("decided papers in one year")
    ax.set_ylabel("reliability of a year's premium")
    ax.set_title("How big must a topic be?", loc="left")
    ax.legend(fontsize=6)
    fig.suptitle("PH5 premia: winner's curse and usable shrinkage (post hoc, exploratory)", x=0.01, ha="left",
                 fontsize=7.5)
    _save(fig, out_dir, "PH5_premia_winners")

    sg = pd.read_csv(out_dir / "surge.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8), constrained_layout=True, gridspec_kw={"width_ratios": [1.3, 1]})
    ax = axes[0]
    y = np.arange(len(sg))[::-1]
    ax.errorbar(sg.coef, y, xerr=[sg.coef - sg.ci95_lo, sg.ci95_hi - sg.coef], fmt="o", ms=4, color=figures.SERIES[0],
                lw=1, capsize=0)
    ax.axvline(0, color=figures.INK2, lw=0.6)
    ax.set_yticks(y, sg.term, fontsize=6.8)
    ax.set_xlabel("acceptance, pp per SD of unexpected surge (95% CI)")
    ax.set_title("Surge and acceptance within topic (topic + year FE)", loc="left")
    ax = axes[1]
    dec = sg[sg.model == "declared"].set_index("term")
    state = lambda t: 0 if dec.loc[t, "p_holm"] >= 0.05 else 1 if dec.loc[t, "coef"] < 0 else 2  # noqa: E731
    seen = (state("beta_inc"), state("beta_new"))                           # (row, column): ~0, < 0, > 0
    grid = [["proportional\nallocation", "dilution", "other"], ["competition"] * 3, ["other"] * 3]
    for i in range(3):
        for j in range(3):
            colour = figures.SERIES[1] if (i, j) == seen else figures.NEUTRAL
            ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor=colour, edgecolor=figures.SURFACE, lw=2))
            ax.text(j + 0.5, i + 0.5, grid[i][j], ha="center", va="center", fontsize=6.3)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xticks([0.5, 1.5, 2.5], ["new ~ 0", "new < 0", "new > 0"])
    ax.set_yticks([0.5, 1.5, 2.5], ["inc ~ 0", "inc < 0", "inc > 0"])
    ax.grid(False)
    ax.set_title(f"Declared reading (Holm 0.05): {summary['surge_reading']}", loc="left")
    fig.suptitle("PH5 premia: who bears a submission surge? (k100, decided papers 2019-2026; post hoc)", x=0.01,
                 ha="left", fontsize=7.5)
    _save(fig, out_dir, "PH5_premia_surge")


def _save(fig, out_dir: Path, name: str) -> None:
    import figures
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out_dir / f"{name}.png", dpi=220, bbox_inches="tight")
    figures.plt.close(fig)
