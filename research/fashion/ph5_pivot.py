"""PH5 pivot (final post hoc round, selection S3): how far to jump. Within topic x year, how does acceptance vary with
the semantic distance between a paper and its authors' own earlier ICLR submissions: a monotone pivot penalty or an
inverted U, is the far-jump penalty different in hot topics, and is the same author accepted less often far from their
earlier work? Post hoc and exploratory: every estimate is an association within topic x year (and author); Holm within
the declared family ranks the evidence, nothing more.

Distance features (outcome-free; built on every discovery submission, any outcome):
  x_p         SPECTER2 vector (title [SEP] abstract), centred with output/specter2_centring_mean.npy, L2-normalised
  history     main era (papers 2023-2026): an author's submissions from 2021 on (profile IDs); replication era
              (2019-2020): from 2017 on (email IDs); 2021-2022 papers serve as history only
  P_a         author a's submissions in [first history year, t - 1], minus p's probable earlier version
              (earlier_versions.csv.gz) and minus every paper q with cos(x_p, x_q) >= 0.90; a is experienced iff P_a is
              not empty
  prior_cos   x_p . c_a, c_a = the normalised mean of P_a's vectors (higher = closer to the author's earlier work)
  F_max       max prior_cos over the experienced authors (primary); n_exp = their number; F_first / F_last = the first /
              last author's prior_cos (if experienced); F_team = cos to the normalised mean of the union of the P_a;
              F_nn = max cos to any paper of that union; n_prior_team = its size; F_max3 = F_max over authors with
              |P_a| >= 3; F_mean = mean prior_cos (calibration plant only)
  REF         frozen outcome-free reference points of each distance among all 2023-2026 submissions that have it (any
              outcome): spline knots (5/35/65/95th pct), contrast points p10 / p50 / p90, F_max quintile edges (display;
              the 20th pct is the calibration plant's threshold) and the prior_cos quintile edges of the author rows
Population: RQ3 decided papers 2023-2026 with n_exp >= 1 (replication: 2019-2020).
P1 (paper level, LPM): accepted ~ RCS(F_max) + RCS(F_max) x (hot - hot share) + class + FM + log2 team + n_exp dummies
   (ref. 1; 2, 3, 4+) + log(1 + n_prior_team) + has_earlier_version | k100 topic x year FE (hot is absorbed; centring it
   at the sample's hot share makes the main spline the population-average curve); CR1 by topic, t(G - 1). RCS =
   Harrell's restricted cubic spline (F and two nonlinear terms, linear beyond the outer knots). Adjusted curve of a
   group (all / hot / not hot) at f: the group's mean acceptance + sum_j b_j (B_j(f) - mean B_j in the group), controls
   at their means, 61 points over [p5, p95] with pointwise 95% CIs. Arg-max of the population curve over that grid
   with a 999-draw topic cluster bootstrap (percentile CI; shares of draws at either edge).
   Display: F_max quintile dummies (ref. Q3) instead of the spline, no interaction, centred at the quintile shares.
P2 (within author): one row per (paper, experienced author), weight 1 / (the paper's rows: n_exp); accepted ~ prior_cos
   + log1p(|P_a|) + class + FM + log2 team | author FE + topic x year FE (posthoc.wls_fe, singletons dropped
   iteratively); CR1 by topic, t(G - 1), with the author FE counted in the small-sample factor (author_fe); two-way
   (topic, author) SE for the slope as a check. Descriptive: prior_cos quintile dummies (ref. Q3) instead of prior_cos.
Declared tests (Holm over the four):
  E1  far-jump contrast: P1 population curve at the F_max p10 minus at p50
  E2  near contrast: p90 minus p50 (negative: close follow-ups do worse, an inverted U)
  E3  E1 in hot topics minus E1 in other topics (the spline x hot terms)
  E4  P2 slope per +0.1 cos
Secondary (BH over seven, descriptive): E1 among papers with / without an established author (an author ID with an
  earlier ICLR acceptance, posthoc.established_authors), among method / theory / measurement papers (each from one pooled
  model with group-specific regressors and group x topic x year FE), and with the first-author / last-author distance
  (own knots and contrast points). The no-acceptance minus established E1 is reported alongside (not in the family).
Robustness (E1-E4 re-estimated where defined; Holm within each variant, nothing counted): topic newcomer control (P1:
  paper newcomer; P2: the author is new to the topic, posthoc.author_rows); P2 with the team's experience (P1's n_exp
  dummies, log(1 + n_prior_team), has_earlier_version; within author and topic x year and given log2 team, prior_cos and
  n_exp correlate 0.12, so a planted n_exp effect moves E4); F_last, F_team or F_nn in place of F_max
  (P1 only); authors with >= 3 prior papers (P1: F_max3; P2: rows with |P_a| >= 3); team-size bands 2-4, 5-7, 8+;
  without papers with a probable earlier version; logit (P1 with topic x year dummies, logit.fe_logit; E1-E3 in log-odds
  via a reparametrised spline basis whose first coefficient is the contrast; E4 not estimated: author dummies are
  infeasible); s9_accepted on the S9 population; the 2019-2020 replication (same frozen reference points); early-map
  topic x year FE and early-map hot (CR1 by early topic).
Outcome-free (compute_free; also inside compute), all 2023-2026 submissions with n_exp >= 1, any outcome: F_max (and
  F_last) ~ hot | year FE + coarse-area FE, without and with controls (n_exp dummies, log2 team, log(1 + n_prior_team),
  class, FM), CR1 by topic; F_max by hot x year, n_exp, class, topic newcomer and team-size band; histograms; the
  correlations of the distance variants; the reference points recomputed against REF.
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
from common import DATA, OUTPUT, topic_layer
from logit import fe_logit
from ols import demean
from panel import CLASS_CONTROLS
from variables import load_authors
from variants import holm

ERAS = {"main": (2023, 2026), "replication": (2019, 2020)}
HISTORY_START = {**{y: 2017 for y in range(2019, 2021)}, **{y: 2021 for y in range(2023, 2027)}}
NEAR_DUP = 0.90
DIST = ["F_max", "F_first", "F_last", "F_team", "F_nn", "F_max3"]
KNOT_PCT, CONTRAST_PCT, QUINTILE_PCT = (5, 35, 65, 95), (10, 50, 90), (20, 40, 60, 80)
REF: dict[str, dict] = {   # frozen (outcome-free, 2023-2026 submissions; reference_points() recomputes them)
    "F_max": {"knots": (-0.0476, 0.2629, 0.4613, 0.7117), "p10": 0.0339, "p50": 0.366, "p90": 0.6508,
              "quintiles": (0.1431, 0.298, 0.4293, 0.5661)},
    "F_first": {"knots": (-0.0998, 0.2056, 0.4394, 0.7284), "p10": -0.0302, "p50": 0.3247, "p90": 0.6597},
    "F_last": {"knots": (-0.1335, 0.1543, 0.3624, 0.6507), "p10": -0.061, "p50": 0.2576, "p90": 0.5791},
    "F_team": {"knots": (-0.1196, 0.178, 0.3813, 0.6497), "p10": -0.0423, "p50": 0.2792, "p90": 0.5836},
    "F_nn": {"knots": (0.0273, 0.3297, 0.5027, 0.7192), "p10": 0.1139, "p50": 0.4191, "p90": 0.6632},
    "F_max3": {"knots": (-0.0829, 0.2345, 0.4307, 0.677), "p10": 0.0023, "p50": 0.3368, "p90": 0.619},
    "prior_cos": {"quintiles": (0.0351, 0.1872, 0.3303, 0.4883)},
}
SPLINE, SPLINE_X = ["s0", "s1", "s2"], ["sx0", "sx1", "sx2"]
NEXP = ["nexp_2", "nexp_3", "nexp_4p"]
TEAM_EXP = NEXP + ["log_prior_team", "has_earlier_version"]               # the team's experience (paper level)
CONTROLS = CLASS_CONTROLS + ["fm", "log2_team"] + TEAM_EXP
P2_CONTROLS = ["log_prior"] + CLASS_CONTROLS + ["fm", "log2_team"]
QUINTS = ["q1", "q2", "q4", "q5"]                                         # reference: the middle quintile
TEAM_BANDS = {"team_2_4": (2, 4), "team_5_7": (5, 7), "team_8plus": (8, 10_000)}
TESTS = {"E1": "far jump: P(accept) at F_max p10 minus p50", "E2": "near: P(accept) at F_max p90 minus p50",
         "E3": "far-jump contrast, hot minus other topics", "E4": "within-author slope per +0.1 cos"}
GRID_POINTS, BOOT, SEED, CHUNK = 61, 999, 20261017, 20_000
HIST_EDGES = np.round(np.arange(-0.6, 1.0001, 0.05), 2)
NOTE = "post hoc exploratory (PH5 pivot, selection S3); associations within topic x year, not causal effects"


# ---------------------------------------------------------------------------------------------------- features
def _rowdot(x: np.ndarray, r: np.ndarray, q: np.ndarray) -> np.ndarray:
    return np.concatenate([np.einsum("ij,ij->i", x[r[s:s + 100_000]], x[q[s:s + 100_000]])
                           for s in range(0, len(r), 100_000)]) if len(r) else np.zeros(0, np.float32)


def _centroid_cos(x: np.ndarray, t: pd.DataFrame, by: list[str]) -> pd.DataFrame:
    """Per group of t (rows: paper r, prior paper q, cos = x_r . x_q): size and x_r . normalised mean of the x_q."""
    g = t.groupby(by, sort=True)
    gi = g.ngroup().to_numpy()
    n = int(gi.max()) + 1
    M = sparse.csr_matrix((np.ones(len(t)), (gi, t.q.to_numpy())), shape=(n, len(x)))
    norm = np.concatenate([np.linalg.norm(M[s:s + CHUNK] @ x, axis=1) for s in range(0, n, CHUNK)])
    out = g.size().rename("n_prior").reset_index()
    out["prior_cos"] = np.bincount(gi, weights=t.cos.to_numpy(float), minlength=n) / norm
    return out


def distances(x: np.ndarray, year: np.ndarray, a: pd.DataFrame, earlier: np.ndarray) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Distance features from unit vectors x (papers x dims), paper years, author rows a (r = paper row, key, first,
    last) and each paper's probable earlier version row (-1 if none). Returns (paper level, indexed 0..n-1; author rows:
    r, key, n_prior, prior_cos)."""
    n = len(year)
    start = pd.Series(year).map(HISTORY_START).to_numpy()
    p = a[np.isfinite(start[a.r.to_numpy()])]
    t = p[["r", "key"]].merge(a[["key", "r"]].rename(columns={"r": "q"}), on="key")
    ty, qy = year[t.r.to_numpy()], year[t.q.to_numpy()]
    t = t[(qy < ty) & (qy >= start[t.r.to_numpy()])].reset_index(drop=True)
    R, Q = t.r.to_numpy(), t.q.to_numpy()
    t["cos"] = _rowdot(x, R, Q)
    excluded = (t.cos.to_numpy() >= NEAR_DUP) | (Q == earlier[R])
    n_excl = t[excluded].drop_duplicates(["r", "q"]).groupby("r").size()
    t = t[~excluded]
    ar = _centroid_cos(x, t, ["r", "key"]).merge(a[["r", "key", "first", "last"]], on=["r", "key"], how="left")
    team = t.drop_duplicates(["r", "q"])
    tc = _centroid_cos(x, team, ["r"]).set_index("r")
    g = ar.groupby("r").prior_cos
    f = pd.DataFrame(index=pd.RangeIndex(n))
    f["F_max"], f["F_mean"], f["n_exp"] = g.max(), g.mean(), g.size()
    f["F_first"] = ar[ar["first"].astype(bool)].groupby("r").prior_cos.max()
    f["F_last"] = ar[ar["last"].astype(bool)].groupby("r").prior_cos.max()
    f["F_team"], f["n_prior_team"] = tc.prior_cos, tc.n_prior
    f["F_nn"] = team.groupby("r").cos.max()
    big = ar[ar.n_prior >= 3].groupby("r").prior_cos
    f["F_max3"], f["n_exp3"] = big.max(), big.size()
    f["n_excluded"] = n_excl
    for c in ["n_exp", "n_prior_team", "n_exp3", "n_excluded"]:
        f[c] = f[c].fillna(0).astype(int)
    return f, ar[["r", "key", "n_prior", "prior_cos"]]


def author_positions(ids: pd.Series) -> pd.DataFrame:
    """Author rows (submission_id, key) with first / last flags (by source list position among keyed authors)."""
    a = load_authors(ids)[["submission_id", "key"]]
    pos = pd.read_csv(DATA / "submission_authors.csv.gz", keep_default_na=False, na_values=[r"\N"],
                      usecols=["submission_id", "declared_id_key", "source_list_position"]).rename(
        columns={"declared_id_key": "key"}).dropna(subset=["key"])
    pos = pos.groupby(["submission_id", "key"]).source_list_position.min().rename("pos").reset_index()
    a = a.merge(pos, on=["submission_id", "key"], how="left")
    g = a.groupby("submission_id").pos
    return a.assign(first=a.pos == g.transform("min"), last=a.pos == g.transform("max"))


@lru_cache(maxsize=1)
def features() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Outcome-free features: (paper level in panel.frame('k100') row order; author rows with submission_id).
    Cached; do not mutate."""
    k = panel.frame("k100").reset_index(drop=True)
    emb, ids = topic_layer().load_embeddings()
    assert (ids.to_numpy() == k.submission_id.to_numpy()).all()
    x = emb.astype(np.float32) - np.load(OUTPUT / "specter2_centring_mean.npy").astype(np.float32)
    x /= np.linalg.norm(x, axis=1, keepdims=True)
    row = pd.Series(np.arange(len(k)), index=k.submission_id)
    a = author_positions(k.submission_id)
    a["r"] = a.submission_id.map(row).to_numpy()
    ev = pd.read_csv(OUTPUT / "earlier_versions.csv.gz")
    assert ev.submission_id.equals(k.submission_id)
    earlier = ev.probable_earlier_version.map(row).fillna(-1).astype(int).to_numpy()
    f, ar = distances(x, k.year.to_numpy(), a, earlier)
    f.insert(0, "submission_id", k.submission_id.to_numpy())
    early = panel.frame("early").reset_index(drop=True)
    assert early.submission_id.equals(k.submission_id)
    f["hot_early"], f["cell_early"] = early.hot.to_numpy(), early.cell.to_numpy()
    ar.insert(0, "submission_id", k.submission_id.to_numpy()[ar.r.to_numpy()])
    return f, ar.drop(columns="r")


def reference_points(f: pd.DataFrame, ar: pd.DataFrame, year: pd.Series) -> dict:
    """REF recomputed: percentiles of each distance among 2023-2026 submissions (any outcome)."""
    main = year.between(*ERAS["main"]).to_numpy()
    out = {}
    for v in DIST:
        s = f.loc[main, v].dropna().to_numpy()
        knots, (p10, p50, p90) = np.percentile(s, KNOT_PCT), np.percentile(s, CONTRAST_PCT)
        out[v] = {"knots": tuple(np.round(knots, 4)), "p10": round(p10, 4), "p50": round(p50, 4), "p90": round(p90, 4),
                  "papers": int(len(s))}
    out["F_max"]["quintiles"] = tuple(np.round(np.percentile(f.loc[main, "F_max"].dropna(), QUINTILE_PCT), 4))
    ay = year.to_numpy()[pd.Series(np.arange(len(f)), index=f.submission_id).reindex(ar.submission_id).to_numpy()]
    rows = ar.prior_cos[(ay >= ERAS["main"][0]) & (ay <= ERAS["main"][1])]
    out["prior_cos"] = {"quintiles": tuple(np.round(np.percentile(rows, QUINTILE_PCT), 4)), "author_rows": int(len(rows))}
    return out


def prepare(k: pd.DataFrame) -> pd.DataFrame:
    """k with the distance features, posthoc.add_columns and model columns; with outcomes, the author profile."""
    k = k.reset_index(drop=True)
    f, _ = features()
    assert (f.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    k = posthoc.add_columns(k.assign(**{c: f[c].to_numpy() for c in f.columns[1:]}))
    for c, lo, hi in [("nexp_2", 2, 2), ("nexp_3", 3, 3), ("nexp_4p", 4, 10_000)]:
        k[c] = k.n_exp.between(lo, hi).astype(float)
    k["log_prior_team"] = np.log1p(k.n_prior_team)
    k["team_band"] = np.select([k.team_size.between(*b) for b in TEAM_BANDS.values()], list(TEAM_BANDS), "1_or_none")
    if "accepted" in k:
        k["established"] = np.where(k.has_author_key, posthoc.established_authors(k).astype(float), np.nan)
    return k


def population(k: pd.DataFrame, era: str = "main", flag: str = "rq3", var: str = "F_max") -> pd.DataFrame:
    return k[k[flag].astype(bool) & k.year.between(*ERAS[era]) & k[var].notna()]


# ---------------------------------------------------------------------------------------------------- estimators
def rcs(x, knots) -> np.ndarray:
    """Harrell's restricted cubic spline basis: x and K - 2 nonlinear terms scaled by (t_K - t_1)^2 (linear beyond the
    outer knots)."""
    x, t = np.atleast_1d(np.asarray(x, float)), np.asarray(knots, float)
    K, cube = len(t), (lambda u: np.clip(u, 0, None) ** 3)
    a, b = t[K - 2], t[K - 1]
    cols = [x] + [(cube(x - t[j]) - cube(x - a) * (b - t[j]) / (b - a) + cube(x - b) * (a - t[j]) / (b - a))
                  / (b - t[0]) ** 2 for j in range(K - 2)]
    return np.column_stack(cols)


def design(d: pd.DataFrame, var: str = "F_max") -> pd.DataFrame:
    """Spline columns s0-s2 of d[var] (REF knots) and their interactions with hot centred at d's hot share."""
    d = d[d[var].notna() & d.hot.notna()].copy()
    B = rcs(d[var], REF[var]["knots"])
    hc = d.hot.to_numpy(float) - d.hot.mean()
    for j in range(3):
        d[SPLINE[j]], d[SPLINE_X[j]] = B[:, j], B[:, j] * hc
    return d


def contrast(var: str, at: str, prefix: str = "s") -> dict[str, float]:
    """Weights of the spline coefficients for curve(REF[var][at]) - curve(REF[var]['p50'])."""
    ref = REF[var]
    c = rcs(ref[at], ref["knots"])[0] - rcs(ref["p50"], ref["knots"])[0]
    return {f"{prefix}{j}": float(v) for j, v in enumerate(c)}


def _partial(d: pd.DataFrame, y: str, xs: list[str], absorb: str):
    """Complete cases, regressors with within-group variation, and the demeaned y and X."""
    d = d.dropna(subset=[y, *xs, absorb])
    g = pd.factorize(d[absorb])[0]
    yd, Xd = demean(d[y].to_numpy(float), g), demean(d[xs].to_numpy(float), g)
    keep = Xd.std(axis=0) > 1e-12
    return d, [x for x, k_ in zip(xs, keep) if k_], Xd[:, keep], yd


@dataclass
class Fit:
    beta: pd.Series
    V: pd.DataFrame
    G: int
    n: int

    def lincom(self, w: dict[str, float]) -> dict:
        """Estimate, CR1 SE, t(G - 1) p and 95% CI of sum w_j b_j; NaN if a term was dropped (no variation)."""
        if not set(w) <= set(self.beta.index):
            return {"coef": np.nan, "se": np.nan, "p": np.nan, "ci95_lo": np.nan, "ci95_hi": np.nan, "n": self.n,
                    "clusters": self.G, "note": "not identified: " + ";".join(sorted(set(w) - set(self.beta.index)))}
        c = pd.Series(w).reindex(self.beta.index).fillna(0.0).to_numpy()
        est, se = float(c @ self.beta.to_numpy()), float(np.sqrt(c @ self.V.to_numpy() @ c))
        q = stats.t.ppf(0.975, self.G - 1)
        return {"coef": est, "se": se, "p": float(2 * stats.t.sf(abs(est / se), self.G - 1)) if se > 0 else np.nan,
                "ci95_lo": est - q * se, "ci95_hi": est + q * se, "n": self.n, "clusters": self.G}


def fit(d: pd.DataFrame, y: str, xs: list[str], absorb: str = "cell", cluster: str = "topic") -> Fit:
    """OLS with one absorbed FE and CR1 SE by cluster (same estimator and small-sample factor as ols.fe_ols)."""
    d, xs, Xd, yd = _partial(d, y, xs, absorb)
    inv = np.linalg.pinv(Xd.T @ Xd)
    beta = inv @ Xd.T @ yd
    e = yd - Xd @ beta
    n, k = Xd.shape
    cg = pd.factorize(d[cluster])[0]
    G = int(cg.max()) + 1
    S = np.zeros((G, k))
    np.add.at(S, cg, Xd * e[:, None])
    V = (G / (G - 1)) * ((n - 1) / (n - k)) * inv @ (S.T @ S) @ inv
    return Fit(pd.Series(beta, xs), pd.DataFrame(V, xs, xs), G, n)


def boot_betas(d: pd.DataFrame, y: str, xs: list[str], rng: np.random.Generator, draws: int = BOOT,
               absorb: str = "cell", cluster: str = "topic") -> tuple[list[str], np.ndarray]:
    """Topic cluster bootstrap of the FE-OLS coefficients. Cells nest in topics, so a resampled topic keeps its
    demeaned rows and each draw solves a weighted sum of per-topic cross products."""
    d, xs, Xd, yd = _partial(d, y, xs, absorb)
    cg = pd.factorize(d[cluster])[0]
    G = int(cg.max()) + 1
    A, b = np.zeros((G, len(xs), len(xs))), np.zeros((G, len(xs)))
    np.add.at(A, cg, Xd[:, :, None] * Xd[:, None, :])
    np.add.at(b, cg, Xd * yd[:, None])
    w = rng.multinomial(G, np.full(G, 1 / G), size=draws).astype(float)
    return xs, np.linalg.solve(np.einsum("bg,gij->bij", w, A), np.einsum("bg,gi->bi", w, b)[:, :, None])[:, :, 0]


def p1(d: pd.DataFrame, var: str = "F_max", y: str = "accepted", extra: tuple[str, ...] = ()) -> tuple[dict, Fit]:
    """E1-E3 from the P1 spline model on d (already through design(d, var))."""
    f = fit(d, y, SPLINE + SPLINE_X + CONTROLS + list(extra))
    return {"E1": f.lincom(contrast(var, "p10")), "E2": f.lincom(contrast(var, "p90")),
            "E3": f.lincom(contrast(var, "p10", "sx"))}, f


def author_sample(d: pd.DataFrame, ar: pd.DataFrame, y: str = "accepted", min_prior: int = 1) -> pd.DataFrame:
    """P2 rows: the experienced authors of d's papers (|P_a| >= min_prior); each paper weighs 1 in total."""
    at = ar[ar.n_prior >= min_prior].merge(d[["submission_id", y, "cell", "topic", *CLASS_CONTROLS, "fm", "log2_team",
                                              *TEAM_EXP]], on="submission_id")
    at["w"] = 1.0 / at.groupby("submission_id").key.transform("size")
    at["log_prior"] = np.log1p(at.n_prior)
    edges = REF["prior_cos"]["quintiles"]
    qi = np.searchsorted(edges, at.prior_cos.to_numpy(), side="right")
    for j, c in zip([0, 1, 3, 4], QUINTS):
        at[c] = (qi == j).astype(float)
    return at


def author_fe(at: pd.DataFrame, y: str, xs: list[str], cluster2: str | None = None) -> pd.DataFrame:
    """posthoc.wls_fe with author and topic x year FE and CR1 SE by topic, whose small-sample factor also counts the
    absorbed author FE (not nested in topics, as reghdfe counts them): SE x sqrt((n - k) / (n - k - (A - 1))), p from
    t(G - 1) again. Uncorrected, E4 rejected 10 of 120 simulated null frames at 0.05 (SD of the estimates 1.08-1.27 x
    the mean SE); corrected, 2 of 60. The two-way SE (the author FE nest in its author clusters) is left as
    posthoc.wls_fe computes it."""
    r = posthoc.wls_fe(at, y, xs, ["key", "cell"], "w", "topic", cluster2)
    n, k = int(r.rows.iloc[0]), len(r)
    A = posthoc.drop_singletons(at.dropna(subset=[y, *xs]), ["key", "cell"]).key.nunique()
    r["se"] *= np.sqrt((n - k) / (n - k - (A - 1)))
    r["p"] = 2 * stats.t.sf(np.abs(r.coef / r.se), r.dof)
    return r


def p2(at: pd.DataFrame, y: str = "accepted", extra: tuple[str, ...] = ()) -> dict:
    """E4: the within-author slope per +0.1 cos (CR1 by topic; two-way topic x author SE and p alongside)."""
    x = author_fe(at, y, ["prior_cos"] + P2_CONTROLS + list(extra), "key").loc["prior_cos"]
    coef, se, sew = 0.1 * x.coef, 0.1 * x.se, 0.1 * x.se_twoway
    q = stats.t.ppf(0.975, x.dof)
    return {"coef": coef, "se": se, "p": x.p, "ci95_lo": coef - q * se, "ci95_hi": coef + q * se, "n": int(x.rows),
            "clusters": int(x.clusters), "papers": int(x.papers), "se_twoway": sew,
            "p_twoway": float(2 * stats.t.sf(abs(coef / sew), x.dof))}


def declared(pop: pd.DataFrame, ar: pd.DataFrame, y: str = "accepted") -> tuple[pd.DataFrame, Fit, pd.DataFrame]:
    """E1-E4 with Holm over the four; also the P1 fit and its design."""
    d = design(pop)
    res, f = p1(d, y=y)
    res["E4"] = p2(author_sample(pop, ar, y), y)
    rows = pd.DataFrame([{"family": "declared", "test": t, "label": lab, **res[t]} for t, lab in TESTS.items()])
    rows["p_holm"] = holm(rows.p.fillna(1.0)).to_numpy()
    return rows, f, d


def pooled_e1(pop: pd.DataFrame, groups: dict[str, np.ndarray], var: str = "F_max") -> tuple[dict, Fit]:
    """E1 within each (disjoint) group from one model: every P1 regressor interacted with the group, group x topic x year
    FE (point estimates equal separate fits; one CR1 covariance by topic)."""
    cols, parts = SPLINE + SPLINE_X + CONTROLS, []
    for name, mask in groups.items():
        g = design(pop[mask], var).dropna(subset=cols)
        parts.append(g.assign(gcell=g.cell + "|" + name, **{f"{c}@{name}": g[c] for c in cols}))
    p = pd.concat(parts, ignore_index=True)
    xs = [f"{c}@{n}" for n in groups for c in cols]
    p[xs] = p[xs].fillna(0.0)
    f = fit(p, "accepted", xs, absorb="gcell")
    return {n: f.lincom({f"{c}@{n}": w for c, w in contrast(var, "p10").items()}) for n in groups}, f


def secondary(pop: pd.DataFrame) -> pd.DataFrame:
    """The seven BH-adjusted descriptive E1s and the no-acceptance minus established difference."""
    prof, fp = pooled_e1(pop, {"established": (pop.established == 1).to_numpy(),
                               "no_acceptance": (pop.established == 0).to_numpy()})
    cls, _ = pooled_e1(pop, {"method": (pop.primary_class == "method").to_numpy(),
                             "theory": (pop.primary_class == "theory").to_numpy(),
                             "measurement": (pop.measurement == 1).to_numpy()})
    rows = [{"set": "profile", "group": g, **r} for g, r in prof.items()]
    rows += [{"set": "class", "group": g, **r} for g, r in cls.items()]
    for v, name in [("F_first", "first author"), ("F_last", "last author")]:
        rows.append({"set": "author position", "group": name, **p1(design(pop[pop[v].notna()], v), v)[0]["E1"]})
    out = pd.DataFrame(rows)
    out["q_bh"] = ph5_common.bh(out.p).to_numpy()
    diff = {f"{c}@no_acceptance": w for c, w in contrast("F_max", "p10").items()}
    diff.update({f"{c}@established": -w for c, w in contrast("F_max", "p10").items()})
    extra = pd.DataFrame([{"set": "profile difference (not in BH family)", "group": "no_acceptance minus established",
                           **fp.lincom(diff)}])
    return pd.concat([out, extra], ignore_index=True)


# ---------------------------------------------------------------------------------------------------- curves
def grid(var: str = "F_max") -> np.ndarray:
    kn = REF[var]["knots"]
    return np.linspace(kn[0], kn[-1], GRID_POINTS)


def curves(f: Fit, d: pd.DataFrame, y: str = "accepted") -> pd.DataFrame:
    """Adjusted P(accept) over the grid for all papers, hot and not hot (see the module docstring)."""
    g, s = grid(), d.hot.mean()
    Bg = rcs(g, REF["F_max"]["knots"])
    rows = []
    for name, mask, wx in [("all", np.ones(len(d), bool), 0.0), ("hot", (d.hot == 1).to_numpy(), 1 - s),
                           ("not hot", (d.hot == 0).to_numpy(), -s)]:
        level, Bbar = d[y][mask].mean(), d.loc[mask, SPLINE].mean().to_numpy()
        for x, b in zip(g, Bg):
            w = {**{SPLINE[j]: b[j] - Bbar[j] for j in range(3)}, **{SPLINE_X[j]: wx * (b[j] - Bbar[j]) for j in range(3)}}
            r = f.lincom(w)
            rows.append({"group": name, "F_max": x, "p_accept": level + r["coef"], "ci95_lo": level + r["ci95_lo"],
                         "ci95_hi": level + r["ci95_hi"], "level": level, "papers": int(mask.sum())})
    return pd.DataFrame(rows)


def argmax(f: Fit, d: pd.DataFrame, rng: np.random.Generator, y: str = "accepted") -> dict:
    """Arg-max of the adjusted curves over the grid, with topic cluster bootstrap percentile CIs."""
    g, s = grid(), d.hot.mean()
    Bg = rcs(g, REF["F_max"]["knots"])
    xs, B = boot_betas(d, y, SPLINE + SPLINE_X + CONTROLS, rng)
    bs, bx = B[:, [xs.index(c) for c in SPLINE]], B[:, [xs.index(c) for c in SPLINE_X]]
    out = {}
    for name, mask, wx in [("all", d.hot.notna(), 0.0), ("hot", d.hot == 1, 1 - s), ("not hot", d.hot == 0, -s)]:
        point = g[int(np.argmax(Bg @ (f.beta[SPLINE].to_numpy() + wx * f.beta[SPLINE_X].to_numpy())))]
        draws = g[np.argmax((bs + wx * bx) @ Bg.T, axis=1)]
        out[name] = {"argmax": float(point), "ci95": [float(v) for v in np.quantile(draws, [0.025, 0.975])],
                     "share_draws_lower_edge": float((draws == g[0]).mean()),
                     "share_draws_upper_edge": float((draws == g[-1]).mean()),
                     "share_of_group_at_or_below": float((d.F_max[mask] <= point).mean())}
    return {**out, "grid": [float(g[0]), float(g[-1]), GRID_POINTS], "draws": BOOT}


def quintile_rows(d: pd.DataFrame, at: pd.DataFrame, y: str = "accepted") -> pd.DataFrame:
    """Display: P1 with F_max quintile dummies (centred at the quintile shares, plus the mean acceptance) and P2 with
    prior_cos quintile dummies (differences from Q3)."""
    qi = np.searchsorted(REF["F_max"]["quintiles"], d.F_max.to_numpy(), side="right")
    dq = d.assign(**{c: (qi == j).astype(float) for j, c in zip([0, 1, 3, 4], QUINTS)}, qi=qi)
    f = fit(dq, y, QUINTS + CONTROLS)
    share = np.bincount(qi, minlength=5) / len(qi)
    wbar = {c: share[j] for j, c in zip([0, 1, 3, 4], QUINTS)}
    level, rows = dq[y].mean(), []
    for j in range(5):
        w = {c: (1.0 if c == f"q{j + 1}" else 0.0) - wbar[c] for c in QUINTS}
        r = f.lincom(w)
        rows.append({"model": "P1 F_max quintiles (adjusted P(accept))", "quintile": f"Q{j + 1}",
                     "position": float(dq.F_max[qi == j].median()), "papers": int((qi == j).sum()),
                     "coef": level + r["coef"], "ci95_lo": level + r["ci95_lo"], "ci95_hi": level + r["ci95_hi"],
                     "se": r["se"], "p": np.nan})
    r = author_fe(at, y, QUINTS + P2_CONTROLS)
    pq = np.searchsorted(REF["prior_cos"]["quintiles"], at.prior_cos.to_numpy(), side="right")
    for j in range(5):
        c = f"q{j + 1}"
        x = r.loc[c] if c in r.index else pd.Series({"coef": 0.0, "se": 0.0, "p": np.nan, "dof": 1})
        q = stats.t.ppf(0.975, x.dof) if c in r.index else 0.0
        rows.append({"model": "P2 within-author prior_cos quintiles (difference from Q3; papers = author rows)",
                     "quintile": f"Q{j + 1}",
                     "position": float(at.prior_cos[pq == j].median()), "papers": int((pq == j).sum()),
                     "coef": x.coef, "ci95_lo": x.coef - q * x.se, "ci95_hi": x.coef + q * x.se, "se": x.se, "p": x.p})
    return pd.DataFrame(rows)


def histogram(d: pd.DataFrame, var: str = "F_max") -> pd.DataFrame:
    rows = []
    for name, mask in [("hot", d.hot == 1), ("not hot", d.hot == 0)]:
        n, _ = np.histogram(d.loc[mask, var].clip(HIST_EDGES[0], HIST_EDGES[-1] - 1e-9), HIST_EDGES)
        rows += [{"group": name, "bin_lo": lo, "bin_hi": hi, "papers": int(c)}
                 for lo, hi, c in zip(HIST_EDGES[:-1], HIST_EDGES[1:], n)]
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------------- robustness
def logit_rows(d: pd.DataFrame, var: str = "F_max") -> list[dict]:
    """E1-E3 in log-odds: logit with topic x year dummies (flat cells dropped), CR1 by topic. The spline basis is
    reparametrised (B T^-1, first row of T = the contrast) so that the first coefficient is the contrast."""
    rows, ref = [], REF[var]
    d = d.reset_index(drop=True)
    for at, tests in [("p10", ("E1", "E3")), ("p90", ("E2",))]:
        T = np.eye(3)
        T[0] = rcs(ref[at], ref["knots"])[0] - rcs(ref["p50"], ref["knots"])[0]
        Ti = np.linalg.inv(T)
        Z = np.hstack([d[SPLINE].to_numpy() @ Ti, d[SPLINE_X].to_numpy() @ Ti])
        X = pd.concat([pd.DataFrame(Z, columns=["z0", "z1", "z2", "zx0", "zx1", "zx2"]), d[CONTROLS].astype(float)], axis=1)
        X = X.loc[:, X.std() > 0]
        try:
            r, info = fe_logit(d.accepted.astype(float), X, [d.cell.rename("cell")], d.topic)
        except (ValueError, RuntimeError, np.linalg.LinAlgError) as e:
            rows += [{"test": t, "coef": np.nan, "note": f"logit failed: {e}"} for t in tests]
            continue
        for t, term in zip(tests, ["z0", "zx0"]):
            x, q = r.loc[term], stats.t.ppf(0.975, r.loc[term, "clusters"] - 1)
            rows.append({"test": t, "coef": x.coef, "se": x.se, "p": x.p, "ci95_lo": x.coef - q * x.se,
                         "ci95_hi": x.coef + q * x.se, "n": int(x.n), "clusters": int(x.clusters),
                         "note": f"log-odds; {len(info['dropped_groups'])} flat cells dropped"})
    return rows


def robustness(k: pd.DataFrame, ar: pd.DataFrame) -> pd.DataFrame:
    pop = population(k)
    new = posthoc.author_rows(k)[["submission_id", "key", "author_new"]]
    early = pop.assign(cell=pop.cell_early, topic=pop.topic_early, hot=pop.hot_early)

    def both(p: pd.DataFrame, y: str = "accepted", extra1=(), extra2=(), at: pd.DataFrame | None = None) -> dict:
        res = p1(design(p), y=y, extra=extra1)[0]
        res["E4"] = p2(author_sample(p, ar, y) if at is None else at, y, extra2)
        return res

    out = {"newcomer_control": both(pop, extra1=("newcomer",), extra2=("author_new",),
                                    at=author_sample(pop, ar).merge(new, on=["submission_id", "key"], how="left")),
           "team_experience_control": {"E4": p2(author_sample(pop, ar), extra=tuple(TEAM_EXP))},
           "authors_ge3_prior": {**p1(design(population(k, var="F_max3"), "F_max3"), "F_max3")[0],
                                 "E4": p2(author_sample(pop, ar, min_prior=3))},
           "no_earlier_version": both(pop[pop.has_earlier_version == 0]),
           "s9": both(population(k, flag="s9"), y="s9_accepted"),
           "replication_2019_2020": both(population(k, era="replication")),
           "early_map": both(early)}
    for v in ["F_last", "F_team", "F_nn"]:
        out[f"{v}_as_primary"] = p1(design(population(k, var=v), v), v)[0]
    for name in TEAM_BANDS:
        out[name] = both(pop[pop.team_band == name])
    rows = [{"variant": v, "test": t, **r} for v, res in out.items() for t, r in res.items()]
    rows += [{"variant": "logit", **r} for r in sorted(logit_rows(design(pop)), key=lambda r: r["test"])]
    res = pd.DataFrame(rows)
    for _, g in res.groupby("variant"):
        res.loc[g.index, "p_holm"] = holm(g.p.fillna(1.0)).to_numpy()
    return res


# ---------------------------------------------------------------------------------------------------- outcome-free
def describe(v: pd.Series) -> dict:
    ref = REF["F_max"]
    return {"papers": int(v.notna().sum()), "mean": float(v.mean()), "median": float(v.median()),
            "share_far_below_p10": float((v < ref["p10"]).mean()), "share_near_above_p90": float((v > ref["p90"]).mean())}


def free_part(k: pd.DataFrame) -> dict:
    """Outcome-free: F_max by destination heat (year + coarse-area FE), by n_exp, class, newcomer and team band."""
    d = k[k.year.between(*ERAS["main"]) & k.F_max.notna()].assign(w=1.0)
    ctr = NEXP + ["log2_team", "log_prior_team"] + CLASS_CONTROLS + ["fm"]
    heat = []
    for v in ["F_max", "F_last"]:
        for label, xs in [("hot | year + area FE", ["hot"]), ("hot + controls | year + area FE", ["hot"] + ctr)]:
            r = posthoc.wls_fe(d[d[v].notna()], v, xs, ["year", "area"], "w", "topic").loc["hot"]
            q = stats.t.ppf(0.975, r.dof)
            heat.append({"distance": v, "model": label, "coef": r.coef, "se": r.se, "p": r.p,
                         "ci95_lo": r.coef - q * r.se, "ci95_hi": r.coef + q * r.se, "papers": int(r.rows),
                         "clusters": int(r.clusters)})
    by_year = pd.DataFrame([{"year": y, "hot": h, **describe(g.F_max)} for (y, h), g in d.groupby(["year", "hot"])])
    nexp = np.where(d.n_exp >= 4, "4+", d.n_exp.astype(str))
    groups = [("n_exp", nexp), ("class", d.primary_class.to_numpy()), ("topic newcomer", d.newcomer.to_numpy()),
              ("team band", d.team_band.to_numpy()), ("hot", d.hot.to_numpy())]
    by_group = pd.DataFrame([{"by": name, "group": str(g), **describe(d.F_max[lab == g])}
                             for name, lab in groups for g in sorted(pd.unique(lab), key=str)])
    f, ar = features()
    ref = reference_points(f, ar, k.year)
    drift = max(abs(np.array(ref[v][key]) - np.array(REF[v][key])).max() for v in REF for key in REF[v])
    corr = d[DIST + ["newcomer", "log2_team", "n_exp"]].corr().round(4)
    summary = {"papers_2023_2026_with_history": int(len(d)),
               "papers_2019_2020_with_history": int((k.year.between(*ERAS["replication"]) & k.F_max.notna()).sum()),
               "author_rows_2023_2026": ref["prior_cos"]["author_rows"],
               "papers_with_an_excluded_prior_paper": int((d.n_excluded > 0).sum()),
               "mean_F_max_newcomer_vs_incumbent": {str(g): float(v) for g, v in d.groupby("newcomer").F_max.mean().items()},
               "correlations": {c: corr[c].to_dict() for c in corr.columns}, "reference_points_recomputed": ref,
               "max_abs_drift_from_REF": float(drift), "note": "outcome-free (any outcome); embeddings, authors, topics"}
    return {"free_heat": pd.DataFrame(heat), "free_by_heat_year": by_year, "free_by_group": by_group,
            "free_hist": histogram(d), "free_summary": summary}


def compute_free() -> dict:
    """Outcome-free parts on the real discovery data (no outcome column is loaded)."""
    return free_part(prepare(panel.frame("k100")))


# ---------------------------------------------------------------------------------------------------- compute
def compute(k: pd.DataFrame, boot_seed: int = SEED) -> dict:
    k = prepare(k)
    _, ar = features()
    pop = population(k)
    tests, f, d = declared(pop, ar)
    at = author_sample(pop, ar)
    summary = {"population": "RQ3 decided papers 2023-2026 with >= 1 experienced author", "papers": int(len(d)),
               "hot_papers": int(d.hot.sum()), "hot_share": float(d.hot.mean()),
               "n_exp": {str(c): int(v) for c, v in d.n_exp.clip(upper=4).value_counts().sort_index().items()},
               "acceptance_rate": float(d.accepted.mean()), "established_share": float(d.established.mean()),
               "P2_author_rows_before_singletons": int(len(at)), "P2_authors_before_singletons": int(at.key.nunique()),
               "reference_points": REF, "argmax": argmax(f, d, np.random.default_rng(boot_seed)), "note": NOTE}
    return {"tests": tests, "secondary": secondary(pop), "curves": curves(f, d), "quintiles": quintile_rows(d, at),
            "robustness": robustness(k, ar), "hist": histogram(d), **free_part(k), "summary": summary}


# ---------------------------------------------------------------------------------------------------- calibration
BASE_RATES = dict(zip(range(2017, 2027), np.linspace(0.45, 0.32, 10)))   # mirrors ph5_common.fake_outcomes
FAR_SHIFT, WITHIN_SLOPE = -0.5, 1.0


def _feature(k: pd.DataFrame, col: str) -> np.ndarray:
    f, _ = features()
    return f.set_index("submission_id")[col].reindex(k.submission_id).to_numpy(float)


PLANTS: dict[str, Callable[[pd.DataFrame], np.ndarray] | None] = {
    "null": None,
    "far": lambda k: FAR_SHIFT * (_feature(k, "F_max") < REF["F_max"]["quintiles"][0]),
    "within": lambda k: WITHIN_SLOPE * np.nan_to_num(_feature(k, "F_mean"))}


def true_prob(k: pd.DataFrame, plant: Callable[[pd.DataFrame], np.ndarray] | None) -> np.ndarray:
    eta = logit(k.year.map(BASE_RATES).fillna(0.4).to_numpy(float))
    return expit(eta if plant is None else eta + plant(k))


def calibrate(n_null: int = 200, n_planted: int = 50, seed: int = 0) -> dict:
    """Run the declared tests on simulated frames: null; 'far' (-0.5 log-odds for F_max below its frozen 20th pct);
    'within' (+1 log-odds per unit of the paper's mean prior_cos, i.e. +0.1 per 0.1 cos). Per plant and test: rejection
    rate at 0.05 (raw, Holm, and two-way for E4), mean estimate, mean target (the same model fitted to the true
    probabilities on the same sample), bias and 95% CI coverage of the target (also two-way for E4), the SD of the
    errors (estimate - target; the sample, hence the target, changes between frames) and the mean SE; the any-Holm
    rejection rate of the family; under the null, the secondary tests' raw
    rejection and any-BH rates."""
    rows, sec = [], []
    _, ar = features()
    for j, (name, plant) in enumerate(PLANTS.items()):
        for i in range(n_null if plant is None else n_planted):
            s = seed + 10_000 * j + i
            k = prepare(ph5_common.simulated_frame(s, plant))
            pop = population(k)
            res, _, _ = declared(pop, ar)
            truth = pop.assign(accepted=np.where(pop.accepted.notna(), true_prob(pop, plant), np.nan))
            target, _, _ = declared(truth, ar)
            rows += [{"plant": name, "frame": s, **r, "target": t} for r, t in zip(res.to_dict("records"), target.coef)]
            if plant is None:
                sec += [{"frame": s, **r} for r in secondary(pop).to_dict("records")]
    r = pd.DataFrame(rows)
    r["reject"], r["reject_holm"], r["reject_twoway"] = r.p < 0.05, r.p_holm < 0.05, r.p_twoway < 0.05
    r["covered"] = (r.ci95_lo <= r.target) & (r.target <= r.ci95_hi)
    half = stats.t.ppf(0.975, r.clusters - 1) * r.se_twoway
    r["covered_twoway"] = np.where(r.se_twoway.notna(), (r.coef - r.target).abs() <= half, np.nan)
    r["error"] = r.coef - r.target
    per_test = (r.groupby(["plant", "test"]).agg(frames=("p", "size"), reject=("reject", "mean"),
                                                 reject_holm=("reject_holm", "mean"),
                                                 reject_twoway=("reject_twoway", "mean"), mean_coef=("coef", "mean"),
                                                 mean_target=("target", "mean"), coverage=("covered", "mean"),
                                                 coverage_twoway=("covered_twoway", "mean"),
                                                 mean_se=("se", "mean"), sd_error=("error", "std"))
                .reset_index())
    per_test["bias"] = per_test.mean_coef - per_test.mean_target
    per_test.loc[per_test.test != "E4", ["reject_twoway", "coverage_twoway"]] = np.nan
    fam = r.groupby(["plant", "frame"]).reject_holm.any().groupby("plant").mean()
    out = {"per_test": per_test.to_dict("records"), "family_any_holm_rejection": fam.to_dict(),
           "n_null": n_null, "n_planted": n_planted, "seed": seed}
    if sec:
        s_ = pd.DataFrame(sec)
        fam_s = s_[s_.q_bh.notna()]
        out["secondary_null"] = {"per_test_rejection": s_.assign(rej=s_.p < 0.05).groupby(["set", "group"]).rej.mean()
                                 .reset_index().to_dict("records"),
                                 "any_bh_flag": float((fam_s.q_bh < 0.05).groupby(fam_s.frame).any().mean())}
    return out


# ---------------------------------------------------------------------------------------------------- figures
def plot(out_dir: Path) -> None:
    import figures
    plt = figures.plt
    out_dir = Path(out_dir)
    curves_, hist = pd.read_csv(out_dir / "curves.csv"), pd.read_csv(out_dir / "hist.csv")
    quint, tests = pd.read_csv(out_dir / "quintiles.csv"), pd.read_csv(out_dir / "tests.csv").set_index("test")
    summary = json.loads((out_dir / "summary.json").read_text())["summary"]
    ref = summary["reference_points"]["F_max"]
    colours = {"hot": figures.SERIES[1], "not hot": figures.SERIES[0]}

    fig, (ax, axh) = plt.subplots(2, 1, figsize=(5.6, 4.6), sharex=True, constrained_layout=True,
                                  gridspec_kw={"height_ratios": [3, 1.1]})
    for g in ["not hot", "hot"]:
        c = curves_[curves_.group == g]
        ax.fill_between(c.F_max, c.ci95_lo * 100, c.ci95_hi * 100, color=colours[g], alpha=0.15, lw=0)
        ax.plot(c.F_max, c.p_accept * 100, color=colours[g], lw=1.6, label=f"{g} topics ({c.papers.iloc[0]:,} papers)")
    a = curves_[curves_.group == "all"]
    ax.plot(a.F_max, a.p_accept * 100, color=figures.MUTED, lw=0.9, ls=(0, (3, 2)), label="all papers")
    q = quint[quint.model.str.startswith("P1")]
    ax.errorbar(q.position, q.coef * 100, yerr=[(q.coef - q.ci95_lo) * 100, (q.ci95_hi - q.coef) * 100], fmt="o", ms=3.5,
                color=figures.INK2, mec=figures.SURFACE, lw=0.9, label="F_max quintiles (all papers)")
    for key in ("p10", "p50", "p90"):
        for axis in (ax, axh):
            axis.axvline(ref[key], color=figures.MUTED, lw=0.6)
        ax.annotate(key, (ref[key], 1), xycoords=("data", "axes fraction"), xytext=(2, -8), textcoords="offset points",
                    fontsize=6.5, color=figures.INK2)
    e = tests.loc[["E1", "E2", "E3"]]
    ax.set_title("Acceptance vs closeness to the authors' own earlier work, within topic x year\n"
                 + "; ".join(f"{t} {r.coef * 100:+.1f} pp (Holm p {r.p_holm:.2f})" for t, r in e.iterrows()), loc="left")
    ax.set_ylabel("adjusted P(accept), % (95% CI)")
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=6.5)
    width = hist.bin_hi.iloc[0] - hist.bin_lo.iloc[0]
    bottom = np.zeros(hist.bin_lo.nunique())
    for g in ["not hot", "hot"]:
        h = hist[hist.group == g]
        axh.bar(h.bin_lo + width / 2, h.papers, width=width * 0.95, bottom=bottom, color=colours[g], alpha=0.7, lw=0)
        bottom = bottom + h.papers.to_numpy()
    axh.set_ylabel("papers")
    axh.set_xlabel("F_max (cos to the centroid of the closest author's earlier submissions)")
    used = hist[hist.papers > 0]
    axh.set_xlim(used.bin_lo.min(), used.bin_hi.max())
    fig.suptitle("PH5 pivot (post hoc, exploratory; decided papers 2023-2026 with an experienced author)", x=0.01,
                 ha="left", fontsize=7)
    _save(fig, out_dir, "PH5_pivot_curve")

    fig, ax = plt.subplots(figsize=(4.8, 2.9), constrained_layout=True)
    q = quint[quint.model.str.startswith("P2")]
    ax.axhline(0, color=figures.INK2, lw=0.7)
    ax.errorbar(q.position, q.coef * 100, yerr=[(q.coef - q.ci95_lo) * 100, (q.ci95_hi - q.coef) * 100], fmt="o", ms=4,
                color=figures.SERIES[0], mec=figures.SURFACE, lw=1)
    for _, r in q.iterrows():
        ax.annotate(r.quintile, (r.position, r.coef * 100), xytext=(4, 4), textcoords="offset points", fontsize=6.5,
                    color=figures.INK2)
    e4 = tests.loc["E4"]
    ax.set_title(f"Same author, papers closer to vs farther from their earlier work\nslope E4 {e4.coef * 100:+.2f} pp "
                 f"per +0.1 cos (CR1 p {e4.p:.2f}; two-way p {e4.p_twoway:.2f})", loc="left")
    ax.set_xlabel("prior_cos (author's distance; quintile medians)")
    ax.set_ylabel("acceptance vs Q3, pp (95% CI)")
    _save(fig, out_dir, "PH5_pivot_within_author")

    by_year, heat = pd.read_csv(out_dir / "free_by_heat_year.csv"), pd.read_csv(out_dir / "free_heat.csv")
    fhist = pd.read_csv(out_dir / "free_hist.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.1), constrained_layout=True, gridspec_kw={"width_ratios": [1.4, 1]})
    ax = axes[0]
    for g, hv in [("not hot", 0.0), ("hot", 1.0)]:
        h = fhist[fhist.group == g]
        ax.step(h.bin_lo, h.papers / h.papers.sum() * 100, where="post", color=colours[g], label=f"{g} topics")
        c = by_year[by_year.hot == hv]
        axes[1].plot(c.year, c["median"], marker="o", ms=3, color=colours[g], label=f"{g} topics")
    ax.set_xlabel("F_max")
    ax.set_ylabel("% of submissions")
    ax.legend(fontsize=6.5)
    r = heat[(heat.distance == "F_max") & (heat.model == "hot + controls | year + area FE")].iloc[0]
    ax.set_title(f"Do hot topics draw farther jumps? Hot minus other topics,\nyear + area FE + controls: "
                 f"{r.coef:+.3f} cos (95% CI {r.ci95_lo:+.3f} to {r.ci95_hi:+.3f})", loc="left")
    axes[1].set_xticks(sorted(by_year.year.unique()))
    axes[1].set_xlabel("year")
    axes[1].set_ylabel("median F_max")
    axes[1].set_title("Median F_max by destination heat", loc="left")
    fig.suptitle("PH5 pivot, outcome-free (2023-2026 submissions with an experienced author, any outcome)", x=0.01,
                 ha="left", fontsize=7)
    _save(fig, out_dir, "PH5_pivot_heat")


def _save(fig, out_dir: Path, name: str) -> None:
    import figures
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out_dir / f"{name}.png", dpi=220, bbox_inches="tight")
    figures.plt.close(fig)
