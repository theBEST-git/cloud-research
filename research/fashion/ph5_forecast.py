"""PH5 forecast (final post hoc round, selection S6; outcome-free and exploratory): does a hot keyword or topic stay hot
over a project's lead time, and which signals visible when a new author keyword appears predict that it booms? No
acceptance outcome is read: compute(k) drops k's outcome columns and equals compute_free(). Everything describes
submission shares; none of it is causal.

Units, shares, growth (Part A)
  keyword  every normalised author keyword of the topic-layer corpus; share s_t = users_t / P_t, P_t = year-t papers
           listing >= 1 keyword (coverage share; the paper share P_t = N_t is a robustness variant)
  early    early-map topics (prospective map; the primary topic unit); share = papers_t / N_t
  k100     k100 topics (fitted on all years: the hindsight contrast); share = papers_t / N_t
  A unit is eligible in t with >= 10 users (papers) before t. g_t = log((c_t + .5) / P_t) - log((c_{t-1} + .5) /
  P_{t-1}); EB growth shrinks g_t to the year mean of eligible units with Poisson variance v = 1/(c_t + .5) +
  1/(c_{t-1} + .5) and the method-of-moments signal variance tau2_t = max(var(g) - mean(v), 0): g_eb = m_t + tau2_t
  (g - m_t) / (tau2_t + v). EB flags rank the score (g - m_t) / (tau2_t + v), which orders units exactly as g_eb when
  tau2_t > 0 and is its limit when tau2_t = 0 (no detectable signal that year). hot_t: growth >= the year's 80th
  percentile (numpy linear) among eligible units (the registered rule); terciles falling/flat/rising by average rank.
  Size band: earlier users 10-19, 20-49, 50+.
A1  P(hot_{t+h} | hot_t) against the base P(hot_{t+h}) of the same pairs (lift), P(hot_{t+h} | not hot_t), and
    P(s_{t+h} > s_t), P(s_{t+h} < s_t) given hot / not hot; h = 1 (origins 2018-2025) and 2 (2018-2024); by unit type,
    band, raw and EB growth. 999-draw unit bootstrap (all pairs of a resampled unit): percentile CI, p from inverting it.
    Declared tests: the lift at h = 1, all bands, for the three unit types; Holm over the three with raw growth
    (primary family) and, separately, with EB growth (secondary family). The lift describes what an author sees; its
    null (lift = 0) is not "no momentum": Poisson noise in the count c_t shared by g_t and g_{t+1} makes raw hotness
    anti-persistent without any latent mean reversion (calibrate() measures this with latent_growth_counts).
A2  transition probabilities t -> t + h between growth terciles, with an entry row (the unit's first eligible year) and
    an exit column (< 3 users at t + h); unit-bootstrap CIs; by band.
A3  Kaplan-Meier survival of hot spells (consecutive hot years; a spell still hot in 2026 is censored and known to
    last >= its length); Greenwood CIs.

Emerging keywords (Part B)
  Risk set: keywords whose first year with >= 5 users is t in 2019-2024 (fizzles included). Boom: s_{t+2} >= 2 s_t and
  users_{t+2} >= 10. Continuous target: log((users_{t+2} + .5) / P_{t+2}) - log((users_t + .5) / P_t), demeaned
  within cohort. Features at t from papers <= t (FEATURES): F1 log users_t; F2 momentum (log share t vs t - 1, counts
  + .5); F3 components of the year-t users linked by a shared author ID key, per user; F4 the largest component's
  share of users; F5 share of users with an author ID that has a discovery submission in t-2..t-1 (cohorts 2019-20 and
  2023-24 only: author-ID switch); F6 entropy (nats) of the users' 20 coarse areas; F7 mean pairwise cosine of the
  users' SPECTER2 vectors, centred on the mean of all year-t papers (not the all-years constant, which would carry
  later papers into a feature at t) and L2-normalised; F8 FM share; F9 measurement share (dataset_benchmark +
  evaluation); F10 share of users whose lower-cased title contains the keyword string (substring, so plurals count).
B1  AUC of each feature for boom (999-draw keyword bootstrap CI; the within-cohort AUC as a check), two-sided
    Mann-Whitney p, Holm over the ten; P(boom | pooled feature tercile) with Wilson CIs.
B2  rolling origin: test cohort t in 2021-2024 trained on cohorts <= t - 2. Features enter the models as z-scores
    within their own cohort (that cross-section is known at t; a feature that barely varies in early cohorts, such as
    FM share in 2019, is not extrapolated). Baseline logit on F1 + F2 (unpenalised) vs the L2 logit on F1-F10 without
    F5 (lambda from LAMBDAS by leave-one-cohort-out log loss, 5 folds when a single cohort trains); pooled AUC, PR-AUC
    (average precision), Brier, delta AUC (999 keyword bootstraps, percentile CI and p). OLS on the continuous target
    (baseline and full): out-of-time R2 (1 - SSE / SST of the pooled test rows) and Spearman, with bootstrap CIs.
B3  P(boom | >= 3 independent groups x >= 3 coarse areas) with counts and Wilson CIs.
B4  topic-years with >= 10 papers, origins 2019-2024, early map (primary) and k100 (hindsight contrast). Target: log
    share ratio t -> t + 2 (counts + .5), year-demeaned. Features at t, as within-year z-scores: past growth g_t, log
    share, FM, newcomer (map-specific), measurement and new-architecture shares, mean log team size. Ridge on the seven
    (lambda from RIDGE_LAMBDAS by leave-one-year-out CV, 5 folds when one year trains) vs momentum-only and size-only
    OLS; rolling origin as B2 (test 2021-2024, train <= t - 2). Out-of-time R2, Spearman, precision at the top quintile
    (share of the predicted top fifth of a test year that is in the realised top fifth), delta R2 of ridge over each
    baseline, 999 topic-cluster bootstraps; P(top-quintile growth | hot_t, within-year size tercile, within-year age
    tercile; age = years since the topic first had >= 10 papers, 0 if first now) with Wilson CIs, for the topic-years
    eligible for hot (>= 10 earlier papers).
Robustness: entry threshold 3 / 10; horizon 3 (cohorts <= 2023, test cohorts 2022-2023); paper share (P_t = N_t: it
changes shares, momentum and targets, but not the within-year ranks behind hot flags); keywords matching LLM_KEYWORDS
left out (A1 for keywords; B1, B2); B4 without papers in the LLM/VLM coarse areas LLM_AREAS. reproduction(): the
prototype persistence numbers from the registered hot flags.
calibrate(): sizes and planted-effect recovery of the declared tests on simulated panels (see its docstring).

    python research/fashion/ph5_forecast.py         # outcome-free run: output/ph5_forecast/*.csv, summary.json, figures
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import brentq
from scipy.special import expit

import panel
from common import OUTPUT, TOPICS, topic_layer
from ph5_common import POSTHOC_COLUMNS
from variables import load_authors
from variants import holm

YEARS = np.arange(2017, 2027)
MIN_EARLIER, HOT_PCT, EXIT_USERS = 10, 80, 3
BANDS = ["10-19", "20-49", "50+"]
ORIGINS = {1: (2018, 2025), 2: (2018, 2024)}
GROWTH = ["raw", "eb"]
STATES = ["exit", "falling", "flat", "rising"]
UNIT_TYPES = ["keyword", "early", "k100"]
COHORTS, ENTRY, HORIZON, BOOM_MIN = (2019, 2024), 5, 2, 10
F5_COHORTS = {2019, 2020, 2023, 2024}
FEATURES = {"F1": "log users", "F2": "momentum", "F3": "independent groups per user", "F4": "largest group share",
            "F5": "experienced adopters", "F6": "coarse-area entropy", "F7": "semantic coherence", "F8": "FM share",
            "F9": "measurement share", "F10": "keyword in title"}
BASE, FULL = ["F1", "F2"], [f for f in FEATURES if f != "F5"]
TOPIC_FEATURES = ["past_growth", "log_share", "fm", "newcomer", "measurement", "model", "log_team"]
TOPIC_MODELS = {"momentum": (["past_growth"], False), "size": (["log_share"], False), "ridge": (TOPIC_FEATURES, True)}
LLM_KEYWORDS = re.compile(r"llm|language model|gpt|chatgpt|foundation model|vlm|multimodal|agent|reasoning")
LLM_AREAS = {"c01", "c02", "c08", "c10", "c15"}
LAMBDAS = np.r_[0.0, np.logspace(-4, 1, 11)]
RIDGE_LAMBDAS = np.r_[0.0, np.logspace(-3, 2, 11)]
N_BOOT, SEED = 999, 20261017
OUT = OUTPUT / "ph5_forecast"


# ---------------------------------------------------------------- inputs

def paper_inputs() -> dict:
    """Outcome-free inputs in corpus (= panel frame) order: keyword sets, lower-case titles, coarse areas, author keys
    per paper (None without one), SPECTER2 vectors and their mean per year (mu, for centring within year t)."""
    tl = topic_layer()
    corpus = tl.embedded_corpus()
    emb, ids = tl.load_embeddings()
    ta = pd.read_csv(TOPICS / "topic_assignments.csv.gz")
    assert ids.equals(corpus.submission_id) and ta.submission_id.equals(corpus.submission_id)
    x, year = emb.astype(np.float32), corpus.year.to_numpy()
    a = load_authors(corpus.submission_id)
    row = pd.Series(np.arange(len(corpus)), index=corpus.submission_id)
    keys = a.groupby(a.submission_id.map(row).to_numpy()).key.apply(list).reindex(range(len(corpus)))
    return {"ids": corpus.submission_id.to_numpy(), "year": year,
            "mu": {int(y): x[year == y].mean(axis=0, dtype=np.float64) for y in YEARS},
            "keywords": [sorted(set(k)) for k in corpus.keywords], "title": corpus.title.fillna("").str.lower().to_numpy(),
            "coarse": ta.coarse.to_numpy(), "x": x, "keys": [v if isinstance(v, list) else None for v in keys]}


def keyword_uses(keywords: list[list[str]], years: np.ndarray) -> pd.DataFrame:
    paper = np.repeat(np.arange(len(keywords)), [len(k) for k in keywords])
    return pd.DataFrame({"paper": paper, "keyword": [w for ks in keywords for w in ks], "year": years[paper]})


def keyword_counts(uses: pd.DataFrame, pin: dict, share: str = "coverage",
                   drop_llm: bool = False) -> tuple[pd.DataFrame, pd.Series]:
    """Users per keyword and year (zeros included) and the share denominator per year."""
    u = uses[~uses.keyword.str.contains(LLM_KEYWORDS)] if drop_llm else uses
    counts = pd.crosstab(u.keyword, u.year).reindex(columns=YEARS, fill_value=0)
    has_kw = np.array([len(k) > 0 for k in pin["keywords"]])
    years = pd.Series(pin["year"][has_kw] if share == "coverage" else pin["year"])
    return counts, years.value_counts().reindex(YEARS)


# ---------------------------------------------------------------- Part A: persistence

def unit_years(counts: pd.DataFrame, denom: pd.Series) -> pd.DataFrame:
    """Unit x year grid (unit-major, RangeIndex) of the units ever eligible: count c, earlier count, share, growth g,
    Poisson variance v, eligibility, band, EB growth (tau2 per year) and per growth version hot / tercile flags."""
    c = counts.reindex(columns=YEARS, fill_value=0).to_numpy(float)
    earlier = np.cumsum(c, axis=1) - c
    keep = (earlier >= MIN_EARLIER).any(axis=1)
    c, earlier, units = c[keep], earlier[keep], counts.index[keep]
    P = denom.reindex(YEARS).to_numpy(float)
    ls = np.log((c + 0.5) / P)
    nan = np.full((len(c), 1), np.nan)
    d = pd.DataFrame({"unit": np.repeat(units.to_numpy(), len(YEARS)), "year": np.tile(YEARS, len(c)), "c": c.ravel(),
                      "earlier": earlier.ravel(), "share": (c / P).ravel(),
                      "g": np.hstack([nan, np.diff(ls, axis=1)]).ravel(),
                      "v": np.hstack([nan, 1 / (c[:, 1:] + 0.5) + 1 / (c[:, :-1] + 0.5)]).ravel()})
    d["eligible"] = (d.earlier >= MIN_EARLIER) & d.g.notna()
    d["band"] = pd.cut(d.earlier, [MIN_EARLIER, 20, 50, np.inf], right=False, labels=BANDS).astype(str)
    e = d[d.eligible]
    yr = e.year
    m = e.g.groupby(yr).transform("mean")
    tau2 = (e.g.groupby(yr).transform("var").fillna(0) - e.v.groupby(yr).transform("mean")).clip(lower=0)
    score = (e.g - m) / (tau2 + e.v)                    # g_eb - m = tau2 * score: same order, defined at tau2 = 0
    d["tau2"], d["g_eb"] = tau2, m + tau2 * score
    for kind, val in (("raw", e.g), ("eb", score)):
        val = val.round(10)
        thr = val.groupby(yr).transform(lambda s: np.percentile(s, HOT_PCT))
        d[f"hot_{kind}"] = (val >= thr).reindex(d.index, fill_value=False)
        terc = np.ceil(3 * val.groupby(yr).rank() / yr.map(yr.value_counts())).clip(1, 3)
        d[f"terc_{kind}"] = terc.reindex(d.index).fillna(0).astype(int)
    return d


def pairs(d: pd.DataFrame, kind: str, h: int) -> pd.DataFrame:
    """Origin unit-years (eligible, origin years ORIGINS[h]) joined to the same unit at t + h."""
    e = d[d.eligible]
    first = e.groupby("unit").year.transform("min")
    o = e[e.year.between(*ORIGINS[h])]
    t1 = d.loc[o.index + h]
    assert (t1.unit.to_numpy() == o.unit.to_numpy()).all() and (t1.year.to_numpy() == o.year.to_numpy() + h).all()
    return pd.DataFrame({"unit": o.unit.to_numpy(), "year": o.year.to_numpy(), "band": o.band.to_numpy(),
                         "entry": (o.year == first.loc[o.index]).to_numpy(),
                         "hot0": o[f"hot_{kind}"].to_numpy(float), "hot1": t1[f"hot_{kind}"].to_numpy(float),
                         "up": (t1.share.to_numpy() > o.share.to_numpy()).astype(float),
                         "down": (t1.share.to_numpy() < o.share.to_numpy()).astype(float),
                         "state0": o[f"terc_{kind}"].to_numpy(),
                         "state1": np.where(t1.c.to_numpy() < EXIT_USERS, 0, t1[f"terc_{kind}"].to_numpy())})


def a1_sums(q: pd.DataFrame) -> pd.DataFrame:
    h0, h1 = q.hot0.to_numpy(), q.hot1.to_numpy()
    s = pd.DataFrame({"n": 1.0, "h0": h0, "h1": h1, "h0h1": h0 * h1, "up0": q.up.to_numpy() * h0,
                      "upn": q.up.to_numpy() * (1 - h0), "dn0": q.down.to_numpy() * h0, "dnn": q.down.to_numpy() * (1 - h0)})
    return s.groupby(q.unit.to_numpy()).sum()


def a1_stats(s: np.ndarray) -> dict[str, np.ndarray]:
    n, h0, h1, h0h1, up0, upn, dn0, dnn = np.moveaxis(np.asarray(s, float), -1, 0)
    with np.errstate(divide="ignore", invalid="ignore"):
        hot, base = h0h1 / h0, h1 / n
        return {"p_hot_given_hot": hot, "p_hot_given_not": (h1 - h0h1) / (n - h0), "base": base, "lift": hot - base,
                "p_up_given_hot": up0 / h0, "p_up_given_not": upn / (n - h0), "up_diff": up0 / h0 - upn / (n - h0),
                "p_down_given_hot": dn0 / h0, "p_down_given_not": dnn / (n - h0), "down_diff": dn0 / h0 - dnn / (n - h0)}


def unit_weights(n_units: int, rng: np.random.Generator) -> np.ndarray:
    """Unit-bootstrap weights: how often each unit is drawn, N_BOOT draws."""
    return rng.multinomial(n_units, np.full(n_units, 1 / n_units), size=N_BOOT).astype(float)


def boot_summary(sums: pd.DataFrame, units: pd.Index, W: np.ndarray,
                 stat: Callable[[np.ndarray], dict]) -> tuple[dict, dict]:
    """Estimates from the unit sums, with percentile CIs from the weighted (bootstrap) sums W @ S."""
    S = sums.reindex(units, fill_value=0.0).to_numpy(float)
    est, bt = stat(S.sum(axis=0)), stat(W @ S)
    out = {}
    for name, v in est.items():
        b = bt[name][np.isfinite(bt[name])]
        out[name] = float(v)
        out[f"{name}_lo"], out[f"{name}_hi"] = np.percentile(b, [2.5, 97.5]) if len(b) else (np.nan, np.nan)
    return out, bt


def boot_p(b: np.ndarray) -> float:
    """Two-sided p from inverting the percentile interval at 0."""
    b = np.asarray(b)[np.isfinite(b)]
    return float(min(1.0, 2 * (1 + min((b <= 0).sum(), (b >= 0).sum())) / (len(b) + 1))) if len(b) else np.nan


def persistence(panels: dict[str, pd.DataFrame], seed: int = SEED) -> pd.DataFrame:
    rows = []
    for i, (utype, d) in enumerate(panels.items()):
        units = pd.Index(d.unit.unique())
        W = unit_weights(len(units), np.random.default_rng([seed, 1, i]))
        for kind in GROWTH:
            for h in (1, 2):
                q = pairs(d, kind, h)
                for band in ["all", *BANDS]:
                    qb = q if band == "all" else q[q.band == band]
                    if qb.hot0.sum() == 0 or qb.hot0.sum() == len(qb):
                        continue
                    est, bt = boot_summary(a1_sums(qb), units, W, a1_stats)
                    rows.append({"unit_type": utype, "growth": kind, "h": h, "band": band, "pairs": len(qb),
                                 "units": qb.unit.nunique(), "hot_pairs": int(qb.hot0.sum()), **est,
                                 "p_lift": boot_p(bt["lift"])})
    return pd.DataFrame(rows)


def a1_tests(a1: pd.DataFrame) -> pd.DataFrame:
    """The declared lift tests (h = 1, all bands); Holm over the three unit types within each growth version."""
    t = a1[(a1.h == 1) & (a1.band == "all")][["unit_type", "growth", "pairs", "hot_pairs", "p_hot_given_hot", "base",
                                              "lift", "lift_lo", "lift_hi", "p_lift"]].copy()
    t["family"] = t.growth.map({"raw": "primary (raw growth)", "eb": "secondary (EB growth)"})
    t["p_holm"] = t.groupby("growth").p_lift.transform(lambda p: holm(p.fillna(1.0)))
    return t.reset_index(drop=True)


def destination_shares(S: np.ndarray) -> dict[str, np.ndarray]:
    with np.errstate(divide="ignore", invalid="ignore"):
        return {s: S[..., j + 1] / S[..., 0] for j, s in enumerate(STATES)}


def transitions(panels: dict[str, pd.DataFrame], seed: int = SEED) -> pd.DataFrame:
    rows = []
    for i, (utype, d) in enumerate(panels.items()):
        units = pd.Index(d.unit.unique())
        W = unit_weights(len(units), np.random.default_rng([seed, 2, i]))
        for kind in GROWTH:
            for h in (1, 2):
                q = pairs(d, kind, h)
                for band in ["all", *BANDS]:
                    qb = q if band == "all" else q[q.band == band]
                    for origin in ["falling", "flat", "rising", "entry"]:
                        qo = qb[qb.entry] if origin == "entry" else qb[qb.state0 == STATES.index(origin)]
                        if qo.empty:
                            continue
                        s = pd.DataFrame({"n": 1.0, **{s: (qo.state1.to_numpy() == j).astype(float)
                                                       for j, s in enumerate(STATES)}}).groupby(qo.unit.to_numpy()).sum()
                        est, _ = boot_summary(s, units, W, destination_shares)
                        rows += [{"unit_type": utype, "growth": kind, "h": h, "band": band, "origin": origin,
                                  "destination": s_, "n": len(qo), "units": qo.unit.nunique(), "p": est[s_],
                                  "lo": est[f"{s_}_lo"], "hi": est[f"{s_}_hi"]} for s_ in STATES]
    return pd.DataFrame(rows)


def hot_spells(d: pd.DataFrame, kind: str) -> pd.DataFrame:
    """Maximal runs of consecutive hot years per unit (eligible years are contiguous); censored if still hot in 2026."""
    e = d[d.eligible]
    hot, unit = e[f"hot_{kind}"].to_numpy(bool), e.unit.to_numpy()
    new_unit = np.r_[True, unit[1:] != unit[:-1]]
    start = hot & (new_unit | ~np.r_[False, hot[:-1]])
    s = pd.DataFrame({"sid": np.cumsum(start)[hot], "unit": unit[hot], "year": e.year.to_numpy()[hot],
                      "band": e.band.to_numpy()[hot]}).groupby("sid")
    return pd.DataFrame({"unit": s.unit.first(), "start": s.year.min(), "length": s.size(), "band": s.band.first(),
                         "censored": s.year.max() == YEARS[-1]}).reset_index(drop=True)


def kaplan_meier(length: np.ndarray, censored: np.ndarray) -> pd.DataFrame:
    """S(d) = P(a spell lasts more than d years). A censored spell of length L is known to last >= L years, so it is at
    risk of ending after d years only for d <= L - 1. Greenwood SE, normal CI clipped to [0, 1]."""
    rows, s, gw = [], 1.0, 0.0
    for d in range(1, int(length.max(initial=0)) + 1):
        at_risk = int(((length >= d) & ~censored).sum() + ((length - 1 >= d) & censored).sum())
        events = int(((length == d) & ~censored).sum())
        if at_risk == 0:
            break
        s *= 1 - events / at_risk
        gw += events / (at_risk * (at_risk - events)) if at_risk > events else np.inf
        se = s * np.sqrt(gw) if np.isfinite(gw) else 0.0
        rows.append({"d": d, "at_risk": at_risk, "events": events, "S": s, "lo": max(0.0, s - 1.96 * se),
                     "hi": min(1.0, s + 1.96 * se)})
    return pd.DataFrame(rows)


def durations(panels: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame]:
    curves, summary = [], []
    for utype, d in panels.items():
        for kind in GROWTH:
            sp = hot_spells(d, kind)
            for band in ["all", *BANDS]:
                g = sp if band == "all" else sp[sp.band == band]
                if g.empty:
                    continue
                km = kaplan_meier(g.length.to_numpy(), g.censored.to_numpy())
                key = {"unit_type": utype, "growth": kind, "band": band}
                curves.append(km.assign(**key))
                below = km[km.S <= 0.5]
                summary.append({**key, "spells": len(g), "censored": int(g.censored.sum()),
                                "mean_observed_length": float(g.length.mean()),
                                "S1": float(km.S.iloc[0]) if len(km) else np.nan,
                                "S2": float(km.S.iloc[1]) if len(km) > 1 else np.nan,
                                "median_years": int(below.d.iloc[0]) if len(below) else np.nan})
    return pd.concat(curves, ignore_index=True), pd.DataFrame(summary)


# ---------------------------------------------------------------- Part B: emerging keywords

def risk_set(counts: pd.DataFrame, denom: pd.Series, entry: int = ENTRY, horizon: int = HORIZON) -> pd.DataFrame:
    """Keywords whose first year with >= entry users is a cohort t (<= 2026 - horizon); targets, F1 and F2."""
    c = counts.reindex(columns=YEARS, fill_value=0).to_numpy()
    reach = c >= entry
    first = YEARS[reach.argmax(axis=1)]
    sel = reach.any(axis=1) & (first >= COHORTS[0]) & (first <= min(COHORTS[1], YEARS[-1] - horizon))
    r = pd.DataFrame({"keyword": counts.index[sel], "cohort": first[sel]})
    c, ti = c[sel], r.cohort.to_numpy() - YEARS[0]
    rows, P = np.arange(len(r)), denom.reindex(YEARS).to_numpy(float)
    users, prev, fut = c[rows, ti], c[rows, ti - 1], c[rows, ti + horizon]
    r["users"], r["users_prev"], r["users_h"] = users, prev, fut
    r["boom"] = ((fut / P[ti + horizon] >= 2 * users / P[ti]) & (fut >= BOOM_MIN)).astype(int)
    r["target"] = np.log((fut + 0.5) / P[ti + horizon]) - np.log((users + 0.5) / P[ti])
    r["target"] -= r.groupby("cohort").target.transform("mean")
    r["F1"] = np.log(users)
    r["F2"] = np.log((users + 0.5) / P[ti]) - np.log((prev + 0.5) / P[ti - 1])
    return r


def components(keys: list[list[str] | None]) -> np.ndarray:
    """Component label per paper: papers sharing an author ID key are linked (a paper without keys stays alone)."""
    parent = list(range(len(keys)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    owner: dict[str, int] = {}
    for i, ks in enumerate(keys):
        for key in ks or []:
            parent[find(i)] = find(owner.setdefault(key, i))
    return np.unique([find(i) for i in range(len(keys))], return_inverse=True)[1]


def birth_features(r: pd.DataFrame, uses: pd.DataFrame, pin: dict, k: pd.DataFrame) -> pd.DataFrame:
    """F3-F10, n_groups and n_areas from each risk-set keyword's users in its cohort year."""
    born = uses.merge(r[["keyword", "cohort"]], left_on=["keyword", "year"], right_on=["keyword", "cohort"])
    by_year: dict[int, set] = {}
    for keys, y in zip(pin["keys"], pin["year"]):
        by_year.setdefault(int(y), set()).update(keys or [])
    fm, meas = k.fm.to_numpy(float), k.measurement.to_numpy(float)
    rows = []
    for kw, g in born.groupby("keyword", sort=False):
        idx, t = g.paper.to_numpy(), int(g.year.iat[0])
        n, keys = len(idx), [pin["keys"][i] for i in idx]
        sizes = np.bincount(components(keys))
        area = pd.Series(pin["coarse"][idx]).value_counts(normalize=True).to_numpy()
        xs = pin["x"][idx].astype(np.float64) - pin["mu"][t]
        s = (xs / np.linalg.norm(xs, axis=1, keepdims=True)).sum(axis=0)
        recent = by_year.get(t - 1, set()) | by_year.get(t - 2, set())
        rows.append({"keyword": kw, "n_groups": len(sizes), "n_areas": len(area), "F3": len(sizes) / n,
                     "F4": sizes.max() / n,
                     "F5": np.mean([bool(set(ks or []) & recent) for ks in keys]) if t in F5_COHORTS else np.nan,
                     "F6": float(-(area * np.log(area)).sum()), "F7": float((s @ s - n) / (n * (n - 1))),
                     "F8": fm[idx].mean(), "F9": meas[idx].mean(), "F10": np.mean([kw in pin["title"][i] for i in idx])})
    return r.merge(pd.DataFrame(rows), on="keyword", how="left", validate="1:1")


def auc_draws(x: np.ndarray, y: np.ndarray, idx: np.ndarray) -> np.ndarray:
    """AUC (ties count 1/2) of x for y in each row of resampling indices idx (B x n)."""
    yb = y[idx]
    rk = stats.rankdata(x[idx], axis=1)
    n1 = yb.sum(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return ((rk * yb).sum(axis=1) - n1 * (n1 + 1) / 2) / (n1 * (idx.shape[1] - n1))


def auc(x: np.ndarray, y: np.ndarray) -> float:
    return float(auc_draws(np.asarray(x, float), np.asarray(y, int), np.arange(len(x))[None])[0])


def roc_points(y: np.ndarray, score: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """True and false positive counts and precision at each distinct threshold, highest score first."""
    order = np.argsort(-score, kind="mergesort")
    y, score = np.asarray(y, float)[order], np.asarray(score, float)[order]
    last = np.r_[np.diff(score) != 0, True]
    tp = np.cumsum(y)[last]
    fp = np.arange(1, len(y) + 1)[last] - tp
    return tp, fp, tp / (tp + fp)


def average_precision(y: np.ndarray, score: np.ndarray) -> float:
    """PR-AUC as the step sum of precision over recall increments (sklearn's average precision)."""
    tp, _, prec = roc_points(y, score)
    return float(np.sum(np.diff(np.r_[0.0, tp / tp[-1]]) * prec))


def stratified_auc(x: np.ndarray, y: np.ndarray, strata: np.ndarray) -> float:
    """AUC over boom / non-boom pairs of the same stratum (cohort) only."""
    num = den = 0.0
    for s in np.unique(strata):
        m = strata == s
        n1 = y[m].sum()
        n0 = m.sum() - n1
        if n1 and n0:
            num += auc(x[m], y[m]) * n1 * n0
            den += n1 * n0
    return num / den if den else np.nan


def wilson(k: float, n: float, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return np.nan, np.nan
    p, den = k / n, 1 + z ** 2 / n
    mid, half = (p + z ** 2 / (2 * n)) / den, z * np.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / den
    return max(0.0, mid - half), min(1.0, mid + half)


def tercile(x: np.ndarray) -> np.ndarray:
    """1-3 by average rank, so tied values share a tercile."""
    return np.ceil(3 * stats.rankdata(x) / len(x)).clip(1, 3).astype(int)


def screen(r: pd.DataFrame, seed: int = SEED) -> tuple[pd.DataFrame, pd.DataFrame]:
    """B1: AUC (bootstrap CI), within-cohort AUC, Mann-Whitney p and Holm per feature; P(boom | tercile)."""
    rng = np.random.default_rng([seed, 3])
    rows, terc = [], []
    for f, label in FEATURES.items():
        d = r[r[f].notna()]
        x, y = d[f].to_numpy(float), d.boom.to_numpy(int)
        bt = auc_draws(x, y, rng.integers(0, len(x), (N_BOOT, len(x))))
        bt = bt[np.isfinite(bt)]
        ok = 0 < y.sum() < len(y)
        rows.append({"feature": f, "label": label, "keywords": len(d), "booms": int(y.sum()),
                     "auc": auc(x, y) if ok else np.nan, "auc_lo": np.percentile(bt, 2.5) if len(bt) else np.nan,
                     "auc_hi": np.percentile(bt, 97.5) if len(bt) else np.nan,
                     "auc_within_cohort": stratified_auc(x, y, d.cohort.to_numpy()),
                     "p_mann_whitney": stats.mannwhitneyu(x[y == 1], x[y == 0]).pvalue if ok else np.nan,
                     "mean_boom": x[y == 1].mean() if y.sum() else np.nan, "mean_other": x[y == 0].mean()})
        t = tercile(x)
        for j in np.unique(t):                          # a tercile is empty when ties straddle its cut
            m = t == j
            lo, hi = wilson(y[m].sum(), m.sum())
            terc.append({"feature": f, "label": label, "tercile": j, "keywords": int(m.sum()), "booms": int(y[m].sum()),
                         "p_boom": y[m].mean(), "lo": lo, "hi": hi, "x_min": x[m].min(), "x_max": x[m].max()})
    out = pd.DataFrame(rows)
    out["p_holm"] = holm(out.p_mann_whitney.fillna(1.0))
    return out, pd.DataFrame(terc)


def fit_logit(X: np.ndarray, y: np.ndarray, lam: float, iters: int = 100) -> np.ndarray:
    """Intercept and slopes minimising mean log loss + lam / 2 * |slopes|^2 (Newton steps, halved until the objective
    falls; stops after `iters` steps, e.g. under separation with lam = 0)."""
    Xa = np.column_stack([np.ones(len(X)), X])
    pen = np.r_[0.0, np.full(X.shape[1], lam)]

    def objective(b):
        z = Xa @ b
        return np.mean(np.logaddexp(0, z) - y * z) + 0.5 * pen @ b ** 2

    b, f = np.zeros(Xa.shape[1]), objective(np.zeros(Xa.shape[1]))
    for _ in range(iters):
        p = expit(Xa @ b)
        grad = Xa.T @ (p - y) / len(y) + pen * b
        hess = (Xa * (p * (1 - p))[:, None]).T @ Xa / len(y) + np.diag(pen)
        step = np.linalg.lstsq(hess, grad, rcond=None)[0]
        for _ in range(30):
            if objective(b - step) <= f:
                break
            step = step / 2
        b, f_new = b - step, objective(b - step)
        if abs(f - f_new) < 1e-12 or np.abs(step).max() < 1e-9:
            break
        f = f_new
    return b


def fit_ridge(X: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
    """Intercept and slopes minimising mean squared error + lam * |slopes|^2 (lam = 0: OLS)."""
    mx, my = X.mean(axis=0), y.mean()
    Xc = X - mx
    A = np.vstack([Xc / np.sqrt(len(y)), np.sqrt(lam) * np.eye(X.shape[1])])
    b = np.linalg.lstsq(A, np.r_[(y - my) / np.sqrt(len(y)), np.zeros(X.shape[1])], rcond=None)[0]
    return np.r_[my - mx @ b, b]


MODELS = {"logit": (fit_logit, expit, LAMBDAS,
                    lambda y, p: -np.mean(y * np.log(np.clip(p, 1e-9, 1)) + (1 - y) * np.log(np.clip(1 - p, 1e-9, 1)))),
          "linear": (fit_ridge, lambda z: z, RIDGE_LAMBDAS, lambda y, p: np.mean((y - p) ** 2))}


def choose_lambda(X: np.ndarray, y: np.ndarray, groups: np.ndarray, kind: str, seed: int) -> float:
    """Lambda with the smallest held-out loss: leave one group (cohort / year) out, or 5 folds if one group trains."""
    fit, link, grid, loss = MODELS[kind]
    if len(np.unique(groups)) < 2:
        groups = np.random.default_rng(seed).permutation(len(y)) % 5
    cv = []
    for lam in grid:
        tot = 0.0
        for g in np.unique(groups):
            m = groups == g
            b = fit(X[~m], y[~m], lam)
            tot += loss(y[m], link(b[0] + X[m] @ b[1:])) * m.sum()
        cv.append(tot)
    return float(grid[int(np.argmin(cv))])


def oot_predict(d: pd.DataFrame, time: str, feats: list[str], target: str, kind: str, penalised: bool,
                horizon: int, tests: list[int], seed: int = SEED) -> tuple[pd.Series, dict]:
    """Rolling origin: for each test period t, fit on periods <= t - horizon and predict t. Features are standardised
    within each period (that period's cross-section, known at t), so a feature that barely varies in early training
    periods (FM share before 2020) is not extrapolated. Returns the predictions and the lambda used per test period."""
    fit, link, _, _ = MODELS[kind]
    z = d[feats].groupby(d[time].to_numpy()).transform(lambda s: (s - s.mean()) / s.std(ddof=0) if s.std(ddof=0) > 0
                                                       else s * 0.0)
    pred, lams = pd.Series(np.nan, index=d.index), {}
    for t in tests:
        tr, te = d[time] <= t - horizon, d[time] == t
        if not tr.any() or not te.any():
            continue
        Xtr, Xte, ytr = z[tr].to_numpy(float), z[te].to_numpy(float), d.loc[tr, target].to_numpy(float)
        lam = choose_lambda(Xtr, ytr, d.loc[tr, time].to_numpy(), kind, seed + t) if penalised else 0.0
        b = fit(Xtr, ytr, lam)
        pred[te], lams[int(t)] = link(b[0] + Xte @ b[1:]), lam
    return pred, lams


def r2_draws(y: np.ndarray, p: np.ndarray, idx: np.ndarray) -> np.ndarray:
    yb, pb = y[idx], p[idx]
    return 1 - ((yb - pb) ** 2).sum(axis=1) / ((yb - yb.mean(axis=1, keepdims=True)) ** 2).sum(axis=1)


def spearman_draws(y: np.ndarray, p: np.ndarray, idx: np.ndarray) -> np.ndarray:
    a, b = stats.rankdata(y[idx], axis=1), stats.rankdata(p[idx], axis=1)
    a, b = a - a.mean(axis=1, keepdims=True), b - b.mean(axis=1, keepdims=True)
    return (a * b).sum(axis=1) / np.sqrt((a ** 2).sum(axis=1) * (b ** 2).sum(axis=1))


def metric(name: str, model: str, est: float, draws: np.ndarray | None = None, test: bool = False, **extra) -> dict:
    ok = draws[np.isfinite(draws)] if draws is not None else np.array([])
    lo, hi = np.percentile(ok, [2.5, 97.5]) if len(ok) else (np.nan, np.nan)
    return {"metric": name, "model": model, "estimate": float(est), "lo": lo, "hi": hi,
            "p": boot_p(draws) if test else np.nan, **extra}


def forecast(r: pd.DataFrame, horizon: int = HORIZON, seed: int = SEED) -> tuple[pd.DataFrame, pd.DataFrame]:
    """B2: rolling-origin boom and growth forecasts; pooled out-of-time metrics with keyword-bootstrap CIs."""
    tests = [int(t) for t in sorted(r.cohort.unique()) if t - horizon >= COHORTS[0]]
    d = r.copy()
    d["p_base"], _ = oot_predict(d, "cohort", BASE, "boom", "logit", False, horizon, tests, seed)
    d["p_full"], lam = oot_predict(d, "cohort", FULL, "boom", "logit", True, horizon, tests, seed)
    d["y_base"], _ = oot_predict(d, "cohort", BASE, "target", "linear", False, horizon, tests, seed)
    d["y_full"], _ = oot_predict(d, "cohort", FULL, "target", "linear", False, horizon, tests, seed)
    te = d[d.cohort.isin(tests)].reset_index(drop=True)
    y, t = te.boom.to_numpy(int), te.target.to_numpy(float)
    idx = np.random.default_rng([seed, 4]).integers(0, len(te), (N_BOOT, len(te)))
    pb, pf, yb, yf = (te[c].to_numpy(float) for c in ("p_base", "p_full", "y_base", "y_full"))
    ab, af = auc_draws(pb, y, idx), auc_draws(pf, y, idx)
    rb, rf = r2_draws(t, yb, idx), r2_draws(t, yf, idx)
    r2b, r2f = (float(r2_draws(t, v, np.arange(len(t))[None])[0]) for v in (yb, yf))
    extra = {"test_keywords": len(te), "test_booms": int(y.sum()), "test_cohorts": ",".join(map(str, tests)),
             "lambda_full_by_cohort": str(lam)}
    rows = [metric("AUC", "baseline logit (F1+F2)", auc(pb, y), ab, **extra),
            metric("AUC", "full L2 logit", auc(pf, y), af, **extra),
            metric("delta AUC", "full - baseline", auc(pf, y) - auc(pb, y), af - ab, test=True, **extra),
            metric("PR-AUC", "baseline logit (F1+F2)", average_precision(y, pb), **extra),
            metric("PR-AUC", "full L2 logit", average_precision(y, pf), **extra),
            metric("PR-AUC", "base rate", y.mean(), **extra),
            metric("Brier", "baseline logit (F1+F2)", np.mean((pb - y) ** 2), **extra),
            metric("Brier", "full L2 logit", np.mean((pf - y) ** 2), **extra),
            metric("R2", "baseline OLS (F1+F2)", r2b, rb, **extra),
            metric("R2", "full OLS", r2f, rf, **extra),
            metric("delta R2", "full - baseline", r2f - r2b, rf - rb, test=True, **extra),
            metric("Spearman", "baseline OLS (F1+F2)", stats.spearmanr(t, yb).statistic, spearman_draws(t, yb, idx),
                   test=True, **extra),
            metric("Spearman", "full OLS", stats.spearmanr(t, yf).statistic, spearman_draws(t, yf, idx), test=True,
                   **extra)]
    return pd.DataFrame(rows), te[["keyword", "cohort", "users", "boom", "target", "p_base", "p_full", "y_base", "y_full"]]


def merton_table(r: pd.DataFrame) -> pd.DataFrame:
    """B3: P(boom | >= 3 independent groups x >= 3 coarse areas)."""
    rows = []
    for groups in (False, True):
        for areas in (False, True):
            m = ((r.n_groups >= 3) == groups) & ((r.n_areas >= 3) == areas)
            lo, hi = wilson(r.boom[m].sum(), m.sum())
            rows.append({"groups_ge3": groups, "areas_ge3": areas, "keywords": int(m.sum()),
                         "booms": int(r.boom[m].sum()), "p_boom": r.boom[m].mean() if m.any() else np.nan,
                         "lo": lo, "hi": hi})
    return pd.DataFrame(rows)


def keyword_risk(uses: pd.DataFrame, pin: dict, k: pd.DataFrame, entry: int = ENTRY, horizon: int = HORIZON,
                 share: str = "coverage", drop_llm: bool = False) -> pd.DataFrame:
    counts, denom = keyword_counts(uses, pin, share, drop_llm)
    return birth_features(risk_set(counts, denom, entry, horizon), uses, pin, k)


# ---------------------------------------------------------------- B4: topics

def topic_rows(f: pd.DataFrame, keep: np.ndarray | None = None) -> pd.DataFrame:
    """B4 topic-years (>= 10 papers in t, origins 2019-2024): features at t, year-demeaned target, age."""
    f = f if keep is None else f[keep]
    N = f.groupby("year").size().reindex(YEARS).to_numpy(float)
    agg = f.groupby(["topic", "year"]).agg(fm=("fm", "mean"), newcomer=("newcomer", "mean"),
                                           measurement=("measurement", "mean"), model=("model", "mean"),
                                           log_team=("log_team", "mean"))
    topics = np.sort(f.topic.unique())
    n = pd.crosstab(f.topic, f.year).reindex(index=topics, columns=YEARS, fill_value=0).to_numpy(float)
    ls = np.log((n + 0.5) / N)
    nan = np.full((len(topics), 1), np.nan)
    ten = n >= 10
    first10 = np.where(ten.any(axis=1), YEARS[ten.argmax(axis=1)], 9999)
    d = pd.DataFrame({"topic": np.repeat(topics, len(YEARS)), "year": np.tile(YEARS, len(topics)), "n": n.ravel(),
                      "past_growth": np.hstack([nan, np.diff(ls, axis=1)]).ravel(),
                      "log_share": np.log((n + 0.5) / N).ravel(),
                      "target": np.hstack([ls[:, 2:] - ls[:, :-2], nan, nan]).ravel(),
                      "age": (np.tile(YEARS, len(topics)) - np.repeat(first10, len(YEARS))).astype(float)})
    d = d.merge(agg.reset_index(), on=["topic", "year"], how="left")
    d = d[(d.n >= 10) & d.year.between(*COHORTS)].reset_index(drop=True)
    d["target"] -= d.groupby("year").target.transform("mean")
    return d


def topic_forecast(d: pd.DataFrame, seed: int = SEED) -> tuple[pd.DataFrame, pd.DataFrame]:
    """B4 rolling-origin forecasts and pooled out-of-time metrics with topic-cluster bootstrap CIs."""
    tests = [t for t in range(COHORTS[0] + HORIZON, COHORTS[1] + 1)]
    d = d.copy()
    for name, (feats, pen) in TOPIC_MODELS.items():
        d[f"pred_{name}"], _ = oot_predict(d, "year", feats, "target", "linear", pen, HORIZON, tests, seed)
    te = d[d.year.isin(tests)].reset_index(drop=True)
    y = te.target.to_numpy()
    real_top = (te.target >= te.groupby("year").target.transform(lambda s: np.percentile(s, 80))).to_numpy()
    codes = pd.factorize(te.topic)[0]
    members = [np.flatnonzero(codes == g) for g in range(codes.max() + 1)]
    rng = np.random.default_rng([seed, 5])
    draws = [np.concatenate([members[j] for j in rng.integers(0, len(members), len(members))]) for _ in range(N_BOOT)]
    rows, r2s, r2 = [], {}, {}
    for name in TOPIC_MODELS:
        p = te[f"pred_{name}"].to_numpy()
        top = (p >= te.groupby("year")[f"pred_{name}"].transform(lambda s: np.percentile(s, 80))).to_numpy()
        r2s[name] = np.array([1 - ((y[i] - p[i]) ** 2).sum() / ((y[i] - y[i].mean()) ** 2).sum() for i in draws])
        rho = np.array([stats.spearmanr(y[i], p[i]).statistic for i in draws])
        prec = np.array([real_top[i][top[i]].mean() if top[i].any() else np.nan for i in draws])
        r2[name] = 1 - ((y - p) ** 2).sum() / ((y - y.mean()) ** 2).sum()
        extra = {"test_rows": len(te), "test_topics": len(members)}
        rows += [metric("R2", name, r2[name], r2s[name], **extra),
                 metric("Spearman", name, stats.spearmanr(y, p).statistic, rho, test=True, **extra),
                 metric("precision@top quintile", name, real_top[top].mean(), prec, **extra)]
        te[f"top_{name}"] = top
    rows += [metric("delta R2", f"ridge - {b}", r2["ridge"] - r2[b], r2s["ridge"] - r2s[b], test=True,
                    test_rows=len(te), test_topics=len(members)) for b in ("momentum", "size")]
    te["real_top"] = real_top
    return pd.DataFrame(rows), te


def topic_conditional(d: pd.DataFrame, panel_rows: pd.DataFrame) -> pd.DataFrame:
    """P(top-quintile growth t -> t+2 | hot_t, size tercile, age tercile); topic-years not yet eligible for hot dropped."""
    h = panel_rows[panel_rows.eligible][["unit", "year", "hot_raw"]].rename(columns={"unit": "topic"})
    d = d.merge(h, on=["topic", "year"], how="inner")
    d["top"] = d.target >= d.groupby("year").target.transform(lambda s: np.percentile(s, 80))
    for c, name in (("log_share", "size"), ("age", "age")):
        d[name] = d.groupby("year")[c].transform(lambda s: tercile(s.to_numpy())).map({1: "low", 2: "mid", 3: "high"})
    d["hot"] = d.hot_raw.map({True: "hot", False: "not hot"})
    rows = []
    for by in (["hot"], ["size"], ["age"], ["hot", "size"], ["hot", "age"], ["hot", "size", "age"]):
        for key, g in d.groupby(by):
            lo, hi = wilson(g.top.sum(), len(g))
            rows.append({"hot": "all", "size": "all", "age": "all", **dict(zip(by, key)), "topic_years": len(g),
                         "top_quintile": int(g.top.sum()), "p": g.top.mean(), "lo": lo, "hi": hi})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- assembly

def prepare(k: pd.DataFrame) -> dict:
    """Every outcome-free input the analyses share: paper inputs, keyword uses, unit panels, risk set, topic rows."""
    k = k.reset_index(drop=True)
    pin = paper_inputs()
    assert (k.submission_id.to_numpy() == pin["ids"]).all()
    frames = {"k100": k, "early": panel.frame("early").reset_index(drop=True)}
    assert (frames["early"].submission_id.to_numpy() == pin["ids"]).all()
    uses = keyword_uses(pin["keywords"], pin["year"])
    counts, denom = keyword_counts(uses, pin)
    N = k.groupby("year").size()
    panels = {"keyword": unit_years(counts, denom),
              **{m: unit_years(pd.crosstab(f.topic, f.year), N) for m, f in (("early", frames["early"]), ("k100", k))}}
    return {"k": k, "pin": pin, "frames": frames, "uses": uses, "panels": panels,
            "risk": birth_features(risk_set(counts, denom), uses, pin, k),
            "topics": {m: topic_rows(f) for m, f in frames.items()}}


def robustness(p: dict) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    k, pin, uses = p["k"], p["pin"], p["uses"]
    ra = []
    for name, share, drop in (("main", "coverage", False), ("paper_share", "paper", False),
                              ("no_llm_family", "coverage", True)):
        d = p["panels"]["keyword"] if name == "main" else unit_years(*keyword_counts(uses, pin, share, drop))
        a1 = persistence({"keyword": d})
        ra.append(a1[a1.h == 1].assign(variant=name))
    rb = []
    variants = {"main": {}, "entry3": {"entry": 3}, "entry10": {"entry": 10}, "horizon3": {"horizon": 3},
                "paper_share": {"share": "paper"}, "no_llm_family": {"drop_llm": True}}
    for name, kw in variants.items():
        r = p["risk"] if name == "main" else keyword_risk(uses, pin, k, **kw)
        b1, _ = screen(r)
        b2, _ = forecast(r, kw.get("horizon", HORIZON))
        info = {"variant": name, "keywords": len(r), "booms": int(r.boom.sum())}
        rb += [{**info, "block": "B1", "name": x.feature, "estimate": x.auc, "lo": x.auc_lo, "hi": x.auc_hi,
                "p": x.p_mann_whitney, "p_holm": x.p_holm} for x in b1.itertuples()]
        rb += [{**info, "block": "B2", "name": f"{x.metric}: {x.model}", "estimate": x.estimate, "lo": x.lo, "hi": x.hi,
                "p": x.p} for x in b2.itertuples() if x.metric in ("AUC", "delta AUC", "R2", "delta R2")]
    r4 = []
    for m, f in p["frames"].items():
        for name, keep in (("all papers", None), ("without LLM/VLM areas", ~np.isin(p["pin"]["coarse"], list(LLM_AREAS)))):
            rows = p["topics"][m] if keep is None else topic_rows(f, keep)
            met, _ = topic_forecast(rows)
            r4.append(met.assign(map=m, variant=name, rows=len(rows)))
    return pd.concat(ra, ignore_index=True), pd.DataFrame(rb), pd.concat(r4, ignore_index=True)


def reproduction(p: dict) -> pd.DataFrame:
    """The prototype persistence numbers re-derived from the registered hot flags: keyword_year.csv.gz (typed keywords,
    prior growth, origins 2019-2025; flags as registered, and re-ranked within the size subset) and the panel hot flags
    of the topic maps (origins 2019-2024), each -> next year."""
    rows = []
    kw = pd.read_csv(OUTPUT / "keyword_year.csv.gz")
    for thr in (10, 20, 50):
        for flags in ("registered", "re-ranked in subset"):
            s = kw[kw.eligible & (kw.earlier_users >= thr)].copy()
            if flags != "registered":
                s["hot"] = s.growth >= s.groupby("year").growth.transform(lambda g: np.percentile(g, HOT_PCT))
            j = s.merge(s[["keyword", "year", "hot"]].assign(year=s.year - 1).rename(columns={"hot": "hot1"}),
                        on=["keyword", "year"])
            rows.append({"unit": "registered keywords", "subset": f">={thr} earlier users", "flags": flags,
                         "pairs": len(j), "p_hot_given_hot": j[j.hot].hot1.mean(),
                         "p_hot_given_not": j[~j.hot].hot1.mean(), "base": j.hot1.mean()})
    for m, f in p["frames"].items():
        ty = f.groupby(["topic", "year"]).hot.first().reset_index()
        j = ty.merge(ty.assign(year=ty.year - 1).rename(columns={"hot": "hot1"}), on=["topic", "year"])
        j = j[j.year.between(2019, 2024) & j.hot.notna() & j.hot1.notna()]
        rows.append({"unit": f"registered {m} topics", "subset": "all", "flags": "registered", "pairs": len(j),
                     "p_hot_given_hot": j[j.hot == 1].hot1.mean(), "p_hot_given_not": j[j.hot == 0].hot1.mean(),
                     "base": j.hot1.mean()})
    return pd.DataFrame(rows)


def compute_free(k: pd.DataFrame | None = None) -> dict:
    """Every PH5 forecast estimate (no outcome is needed or read)."""
    p = prepare(panel.frame("k100") if k is None else k)
    panels, r = p["panels"], p["risk"]
    a1 = persistence(panels)
    tests = a1_tests(a1)
    km, spells = durations(panels)
    b1, terc = screen(r)
    b2, preds = forecast(r)
    b4 = {m: topic_forecast(rows) for m, rows in p["topics"].items()}
    ra, rb, r4 = robustness(p)
    out = {"a1_persistence": a1, "a1_tests": tests, "a2_transitions": transitions(panels), "a3_km": km,
           "a3_spells": spells, "b_risk_set": r, "b1_screen": b1, "b1_terciles": terc, "b2_models": b2,
           "b2_predictions": preds, "b3_table": merton_table(r),
           "b4_models": pd.concat([b4[m][0].assign(map=m) for m in b4], ignore_index=True),
           "b4_predictions": pd.concat([b4[m][1].assign(map=m) for m in b4], ignore_index=True),
           "b4_conditional": pd.concat([topic_conditional(p["topics"][m], panels[m]).assign(map=m) for m in b4],
                                       ignore_index=True),
           "robust_a": ra, "robust_b": rb, "robust_b4": r4, "reproduction": reproduction(p)}
    elig = {u: d[d.eligible] for u, d in panels.items()}
    out["sizes"] = {"eligible_units_by_year": {u: {int(y): int(n) for y, n in e.groupby("year").size().items()}
                                               for u, e in elig.items()},
                    "eb_signal_variance_by_year": {u: {int(y): round(float(v), 5)
                                                       for y, v in e.groupby("year").tau2.first().items()}
                                                   for u, e in elig.items()},
                    "risk_set_by_cohort": {int(c): int(n) for c, n in r.groupby("cohort").size().items()},
                    "booms_by_cohort": {int(c): int(n) for c, n in r.groupby("cohort").boom.sum().items()},
                    "b4_topic_years": {m: len(rows) for m, rows in p["topics"].items()}}
    prim = tests.set_index(["growth", "unit_type"])
    out["headline"] = {
        "a1_lift_h1": {f"{g}:{u}": {"p_hot_given_hot": round(x.p_hot_given_hot, 4), "base": round(x.base, 4),
                                    "lift": round(x.lift, 4), "ci": [round(x.lift_lo, 4), round(x.lift_hi, 4)],
                                    "p_holm": round(x.p_holm, 4)} for (g, u), x in prim.iterrows()},
        "b1_auc": {x.feature: [round(x.auc, 3), round(x.auc_lo, 3), round(x.auc_hi, 3), round(x.p_holm, 4)]
                   for x in b1.itertuples()},
        "b2": {f"{x.metric}: {x.model}": [round(x.estimate, 4), round(x.lo, 4), round(x.hi, 4)] for x in b2.itertuples()},
        "b4": {f"{m}: {x.metric}: {x.model}": [round(x.estimate, 3), round(x.lo, 3), round(x.hi, 3)]
               for m in b4 for x in b4[m][0].itertuples()},
        "note": "outcome-free; exploratory descriptions and forecasts of submission shares, not causal effects"}
    return out


def compute(k: pd.DataFrame) -> dict:
    """The contract entry point: k's outcome columns are dropped, so the result equals compute_free(k)."""
    return compute_free(k.drop(columns=[c for c in POSTHOC_COLUMNS if c in k.columns]))


# ---------------------------------------------------------------- calibration

def with_hot(d: pd.DataFrame, hot: np.ndarray) -> pd.DataFrame:
    return d.assign(hot_raw=hot, hot_eb=hot)


def permuted_hot(d: pd.DataFrame, rng: np.random.Generator) -> np.ndarray:
    """Each year's hot flags shuffled across that year's eligible units (hotness independent over time)."""
    hot = d.hot_raw.to_numpy(bool).copy()
    for idx in d.index[d.eligible].groupby(d.year[d.eligible]).values():
        hot[idx] = rng.permutation(hot[idx])
    return hot


def ar1_hot(d: pd.DataFrame, rho: float, rng: np.random.Generator) -> np.ndarray:
    """Latent z_t = rho z_{t-1} + sqrt(1 - rho^2) e over a unit's eligible years (N(0, 1) at entry); hot = top 20% of z
    among the year's eligible units."""
    elig = d.eligible.to_numpy().reshape(-1, len(YEARS))
    z = np.zeros(elig.shape)
    for j in range(len(YEARS)):
        e = rng.standard_normal(len(z))
        z[:, j] = e if j == 0 else np.where(elig[:, j - 1], rho * z[:, j - 1] + np.sqrt(1 - rho ** 2) * e, e)
    thr = [np.percentile(z[elig[:, j], j], HOT_PCT) if elig[:, j].any() else np.inf for j in range(len(YEARS))]
    return (elig & (z >= np.array(thr))).ravel()


def latent_growth_counts(d: pd.DataFrame, denom: pd.Series, phi: float, rng: np.random.Generator) -> pd.DataFrame:
    """Counts c ~ Poisson(P_t exp(x_t)): x starts at the unit's mean log share and grows by a stationary AR(1)
    g_t = phi g_{t-1} + sqrt(1 - phi^2) e_t, e ~ N(0, sigma^2), sigma^2 = mean over years of the unit type's tau2.
    phi = 0 is a random walk (no momentum); phi > 0 is latent momentum, observed through Poisson noise."""
    grid = d.c.to_numpy().reshape(-1, len(YEARS))
    P = denom.reindex(YEARS).to_numpy(float)
    e = np.sqrt(d.groupby("year").tau2.first().mean()) * rng.standard_normal((len(grid), len(YEARS) - 1))
    g = np.zeros(grid.shape)
    g[:, 1] = e[:, 0]
    for j in range(2, len(YEARS)):
        g[:, j] = phi * g[:, j - 1] + np.sqrt(1 - phi ** 2) * e[:, j - 1]
    x = np.log((grid / P).mean(axis=1, keepdims=True) + 1e-9) + np.cumsum(g, axis=1)
    return pd.DataFrame(rng.poisson(P * np.exp(x)), index=d.unit.unique(), columns=YEARS)


def planted_score(r: pd.DataFrame) -> np.ndarray:
    return sum((r[f] - r[f].mean()) / r[f].std() for f in ("F3", "F6")).to_numpy()


def plant_boom(r: pd.DataFrame, beta: float, rng: np.random.Generator) -> tuple[pd.DataFrame, dict]:
    """Latent y = beta (z_F3 + z_F6) + logistic noise; boom = y + a_c > 0 with a_c matching the real cohort boom rate
    in expectation; continuous target = y demeaned within cohort. Returns the frame and each feature's true AUC."""
    s, cohort = planted_score(r), r.cohort.to_numpy()
    a = np.zeros(len(r))
    for c in np.unique(cohort):
        m = cohort == c
        a[m] = brentq(lambda v: expit(beta * s[m] + v).mean() - r.boom[m].mean(), -30, 30)
    y = beta * s + rng.logistic(size=len(r))
    out = r.assign(boom=(y + a > 0).astype(int), target=y)
    out["target"] -= out.groupby("cohort").target.transform("mean")
    p = expit(beta * s + a)
    w = p[:, None] * (1 - p)[None, :]
    np.fill_diagonal(w, 0)
    truth = {}
    for f in FEATURES:
        x = r[f].to_numpy(float)
        ok = np.isfinite(x)
        k = (x[ok][:, None] > x[ok][None, :]) + 0.5 * (x[ok][:, None] == x[ok][None, :])
        truth[f] = float((w[np.ix_(ok, ok)] * k).sum() / w[np.ix_(ok, ok)].sum())
    return out, truth


def calibrate(n_null: int = 40, n_planted: int = 20, seed: int = 0, rho: float = 0.25, phi: float = 0.5,
              beta: float = 0.6, r2: float = 0.15) -> dict:
    """Sizes and planted-effect recovery of the declared tests. No acceptance outcome enters this module, so
    simulated_frame() would leave every result unchanged; the simulations replace the forecast targets instead, on the
    real (outcome-free) panels, risk set and topic-years.

    A1  null: each year's hot flags shuffled across that year's eligible units; planted: AR(1) latent growth with
        rho (true lift = P(Z1 > c, Z2 > c) / 0.2 - 0.2, c = Phi^-1(0.8)). Per unit type: rejection rate of the bootstrap
        lift test at 0.05, Holm family-wise rate, bias, CI coverage and Holm power. Through the whole counts -> growth
        -> hot pipeline (latent_growth_counts, Poisson noise): with no momentum (random walk, n_null draws) the mean
        raw and EB lifts and how often the declared tests reject with a negative / positive lift, and with latent
        momentum phi (n_planted draws) the mean lifts and the Holm power for a positive lift. The declared null is
        lift = 0, not "no momentum": Poisson noise in the shared count c_t makes raw hotness anti-persistent.
    B1/B2  null: boom and continuous target permuted within cohort; planted: plant_boom(beta) on F3 and F6.
    B4  early map; null: target permuted within year; planted: target = sqrt(r2) z_FM + sqrt(1 - r2) e, z_FM the
        within-year standardised FM share.
    """
    p = prepare(panel.frame("k100"))
    rng = np.random.default_rng(seed)
    c = stats.norm.ppf(HOT_PCT / 100)
    true_lift = (1 - 2 * stats.norm.cdf(c) + stats.multivariate_normal([0, 0], [[1, rho], [rho, 1]]).cdf([c, c])) \
        / (1 - HOT_PCT / 100) - (1 - HOT_PCT / 100)

    def a1(sim: dict, i: int) -> pd.DataFrame:
        return a1_tests(persistence(sim, seed=seed + i)).query("growth == 'raw'").set_index("unit_type")

    res_null = [a1({u: with_hot(d, permuted_hot(d, rng)) for u, d in p["panels"].items()}, i) for i in range(n_null)]
    res_plant = [a1({u: with_hot(d, ar1_hot(d, rho, rng)) for u, d in p["panels"].items()}, i) for i in range(n_planted)]
    _, kw_denom = keyword_counts(p["uses"], p["pin"])
    den = {"keyword": kw_denom, "early": p["k"].groupby("year").size(), "k100": p["k"].groupby("year").size()}

    def pipeline(phi_: float, i: int) -> pd.DataFrame:
        sims = {u: unit_years(latent_growth_counts(d, den[u], phi_, rng), den[u]) for u, d in p["panels"].items()}
        return a1_tests(persistence(sims, seed=seed + i)).set_index(["unit_type", "growth"])

    walk, mom = [pipeline(0.0, i) for i in range(n_null)], [pipeline(phi, i) for i in range(n_planted)]

    def rate(res: list[pd.DataFrame], key: tuple, sign: int) -> float:
        return float(np.mean([(x.p_holm[key] < 0.05) & (np.sign(x.lift[key]) == sign) for x in res]))

    out = {"settings": {"n_null": n_null, "n_planted": n_planted, "seed": seed, "rho": rho, "phi": phi, "beta": beta,
                        "r2": r2, "bootstrap_draws": N_BOOT},
           "a1": {u: {"null_rejection_0.05": float(np.mean([x.p_lift[u] < 0.05 for x in res_null])),
                      "null_mean_lift": float(np.mean([x.lift[u] for x in res_null])),
                      "planted_true_lift": float(true_lift),
                      "planted_mean_lift": float(np.mean([x.lift[u] for x in res_plant])),
                      "planted_coverage": float(np.mean([x.lift_lo[u] <= true_lift <= x.lift_hi[u] for x in res_plant])),
                      "planted_power_holm": float(np.mean([x.p_holm[u] < 0.05 for x in res_plant])),
                      **{f"{name}_{g}": v for g in GROWTH for name, v in (
                          ("random_walk_lift", float(np.mean([x.lift[(u, g)] for x in walk]))),
                          ("random_walk_holm_reject_negative", rate(walk, (u, g), -1)),
                          ("random_walk_holm_reject_positive", rate(walk, (u, g), 1)),
                          ("momentum_lift", float(np.mean([x.lift[(u, g)] for x in mom]))),
                          ("momentum_holm_power_positive", rate(mom, (u, g), 1)))}} for u in UNIT_TYPES},
           "a1_familywise_null_holm": float(np.mean([(x.p_holm < 0.05).any() for x in res_null]))}

    r = p["risk"]
    perm = lambda df, col: df.groupby(col)[["boom", "target"]].transform(  # noqa: E731
        lambda s: s.to_numpy()[rng.permutation(len(s))])
    nb1, nb2, pb1, pb2, truths = [], [], [], [], []
    for i in range(n_null):
        sim = r.assign(**perm(r, "cohort"))
        nb1.append(screen(sim, seed + i)[0].set_index("feature"))
        nb2.append(forecast(sim, seed=seed + i)[0].set_index(["metric", "model"]))
    for i in range(n_planted):
        sim, truth = plant_boom(r, beta, rng)
        pb1.append(screen(sim, seed + i)[0].set_index("feature"))
        pb2.append(forecast(sim, seed=seed + i)[0].set_index(["metric", "model"]))
        truths.append(truth)
    truth, signal = pd.DataFrame(truths).mean(), beta ** 2 * np.var(planted_score(r))
    dauc = ("delta AUC", "full - baseline")
    out["b1"] = {f: {"null_rejection_0.05": float(np.mean([x.p_mann_whitney[f] < 0.05 for x in nb1])),
                     "null_mean_auc": float(np.mean([x.auc[f] for x in nb1])),
                     "planted_true_auc": float(truth[f]), "planted_mean_auc": float(np.mean([x.auc[f] for x in pb1])),
                     "planted_coverage": float(np.mean([x.auc_lo[f] <= t[f] <= x.auc_hi[f] for x, t in zip(pb1, truths)])),
                     "planted_power_holm": float(np.mean([x.p_holm[f] < 0.05 for x in pb1]))} for f in FEATURES}
    out["b1_familywise_null_holm"] = float(np.mean([(x.p_holm < 0.05).any() for x in nb1]))
    out["b2"] = {"null_delta_auc_rejection_0.05": float(np.mean([x.p[dauc] < 0.05 for x in nb2])),
                 "null_mean_auc_full": float(np.mean([x.estimate[("AUC", "full L2 logit")] for x in nb2])),
                 "null_mean_r2_full": float(np.mean([x.estimate[("R2", "full OLS")] for x in nb2])),
                 "null_spearman_full_rejection_0.05": float(np.mean([x.p[("Spearman", "full OLS")] < 0.05 for x in nb2])),
                 "planted_mean_delta_auc": float(np.mean([x.estimate[dauc] for x in pb2])),
                 "planted_power_delta_auc": float(np.mean([(x.p[dauc] < 0.05) & (x.estimate[dauc] > 0) for x in pb2])),
                 "planted_mean_auc_full": float(np.mean([x.estimate[("AUC", "full L2 logit")] for x in pb2])),
                 "planted_mean_r2_full": float(np.mean([x.estimate[("R2", "full OLS")] for x in pb2])),
                 "planted_oracle_r2": float(signal / (signal + np.pi ** 2 / 3))}

    d = p["topics"]["early"]
    zfm = d.groupby("year").fm.transform(lambda s: (s - s.mean()) / s.std(ddof=0)).to_numpy()
    n4, p4 = [], []
    for i in range(n_null):
        sim = d.assign(target=d.groupby("year").target.transform(lambda s: s.to_numpy()[rng.permutation(len(s))]))
        n4.append(topic_forecast(sim, seed + i)[0].set_index(["metric", "model"]))
    for i in range(n_planted):
        y = np.sqrt(r2) * zfm + np.sqrt(1 - r2) * rng.standard_normal(len(d))
        sim = d.assign(target=y - pd.Series(y).groupby(d.year.to_numpy()).transform("mean").to_numpy())
        p4.append(topic_forecast(sim, seed + i)[0].set_index(["metric", "model"]))
    out["b4"] = {m: {"null_mean_r2": float(np.mean([x.estimate[("R2", m)] for x in n4])),
                     "null_spearman_rejection_0.05": float(np.mean([x.p[("Spearman", m)] < 0.05 for x in n4])),
                     "null_mean_precision": float(np.mean([x.estimate[("precision@top quintile", m)] for x in n4])),
                     "planted_mean_r2": float(np.mean([x.estimate[("R2", m)] for x in p4])),
                     "planted_spearman_power": float(np.mean([x.p[("Spearman", m)] < 0.05 for x in p4]))}
                 for m in TOPIC_MODELS}
    out["b4"]["planted_true_r2"] = r2
    return out


# ---------------------------------------------------------------- figures

def _save(fig, out_dir: Path, name: str) -> None:
    import matplotlib.pyplot as plt
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out_dir / f"{name}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot(out_dir: Path) -> None:
    """Figures from the saved CSVs only: persistence, transitions, hot-spell survival, feature AUCs, ROC, B3, B4."""
    import matplotlib.pyplot as plt
    import figures
    from matplotlib.colors import LinearSegmentedColormap
    out_dir = Path(out_dir)
    read = lambda name: pd.read_csv(out_dir / f"{name}.csv")  # noqa: E731
    names = {"keyword": "author keywords", "early": "early-map topics", "k100": "k100 topics (hindsight)"}
    colours = {"raw": figures.SERIES[0], "eb": figures.SERIES[1]}

    a1 = read("a1_persistence")
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.6), sharey=True, constrained_layout=True)
    for ax, u in zip(axes, UNIT_TYPES):
        g = a1[(a1.unit_type == u) & (a1.h == 1)]
        bands = [b for b in ["all", *BANDS] if b in set(g.band)]
        for j, kind in enumerate(GROWTH):
            x = g[g.growth == kind].set_index("band").reindex(bands)
            pos = np.arange(len(bands)) + (j - 0.5) * 0.36
            ax.bar(pos, x.p_hot_given_hot, 0.32, color=colours[kind], label=f"{kind} growth" if u == "keyword" else None)
            ax.errorbar(pos, x.p_hot_given_hot, yerr=[x.p_hot_given_hot - x.p_hot_given_hot_lo,
                                                      x.p_hot_given_hot_hi - x.p_hot_given_hot], fmt="none",
                        ecolor=figures.INK2, lw=0.8)
            ax.hlines(x.base, pos - 0.16, pos + 0.16, color=figures.INK, lw=1.6,
                      label="base P(hot)" if u == "keyword" and j else None)
        ax.set_xticks(np.arange(len(bands)), [b if b == "all" else f"{b} users" for b in bands], fontsize=6.5)
        ax.set_title(names[u], loc="left")
    axes[0].set_ylabel("P(hot next year | hot now)")
    axes[0].legend(loc="upper left", fontsize=6.5)
    fig.suptitle("A1: does hotness persist one year? Bars with 95% unit-bootstrap CI; black tick = base rate", fontsize=8)
    _save(fig, out_dir, "forecast_persistence")

    a2 = read("a2_transitions")
    ramp = LinearSegmentedColormap.from_list("ramp", [figures.SURFACE, *figures.BLUE_RAMP])
    fig, axes = plt.subplots(3, 2, figsize=(5.6, 6.6), constrained_layout=True)
    for i, u in enumerate(UNIT_TYPES):
        for j, h in enumerate((1, 2)):
            ax = axes[i, j]
            g = a2[(a2.unit_type == u) & (a2.h == h) & (a2.growth == "raw") & (a2.band == "all")]
            m = g.pivot(index="origin", columns="destination", values="p").reindex(
                index=["falling", "flat", "rising", "entry"], columns=STATES)
            ax.imshow(m.to_numpy(), cmap=ramp, vmin=0, vmax=0.6)
            for (a, b), v in np.ndenumerate(m.to_numpy()):
                if np.isfinite(v):
                    ax.text(b, a, f"{v:.2f}", ha="center", va="center", fontsize=6.5,
                            color="white" if v > 0.4 else figures.INK)
            ax.set_xticks(range(4), STATES, fontsize=6.5)
            ax.set_yticks(range(4), m.index, fontsize=6.5)
            ax.grid(False)
            ax.set_title(f"{names[u]}: t -> t+{h}", loc="left", fontsize=7.5)
    fig.suptitle("A2: growth-tercile transitions (raw growth; rows: state at t, columns: state at t+h)", fontsize=8)
    _save(fig, out_dir, "forecast_transitions")

    km = read("a3_km")
    fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.5), sharey=True, constrained_layout=True)
    for ax, kind in zip(axes, GROWTH):
        for i, u in enumerate(UNIT_TYPES):
            g = km[(km.unit_type == u) & (km.growth == kind) & (km.band == "all")]
            d = np.r_[0, g.d]
            ax.step(d, np.r_[1, g.S], where="post", color=figures.SERIES[i], label=names[u])
            ax.fill_between(d, np.r_[1, g.lo], np.r_[1, g.hi], step="post", color=figures.SERIES[i], alpha=0.15, lw=0)
        ax.set_xlabel("years hot")
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
        ax.set_title(f"{kind} growth", loc="left")
    axes[0].set_ylabel("P(spell lasts longer)")
    axes[0].legend(fontsize=6.5)
    fig.suptitle("A3: Kaplan-Meier survival of hot spells (95% Greenwood CI)", fontsize=8)
    _save(fig, out_dir, "forecast_hot_spells")

    b1 = read("b1_screen")
    fig, ax = plt.subplots(figsize=(4.6, 3.0), constrained_layout=True)
    y = np.arange(len(b1))[::-1]
    ax.errorbar(b1.auc, y, xerr=[b1.auc - b1.auc_lo, b1.auc_hi - b1.auc], fmt="none", ecolor=figures.SERIES[0], lw=1)
    sig = b1.p_holm < 0.05
    ax.plot(b1.auc[sig], y[sig], "o", color=figures.SERIES[0], ms=5, label="Holm p < 0.05")
    ax.plot(b1.auc[~sig], y[~sig], "o", mfc=figures.SURFACE, mec=figures.SERIES[0], ms=5, label="not significant")
    ax.plot(b1.auc_within_cohort, y, "|", color=figures.INK2, ms=7, label="within-cohort AUC")
    ax.axvline(0.5, color=figures.INK2, lw=0.7)
    ax.set_yticks(y, [f"{f} {lab}" for f, lab in zip(b1.feature, b1.label)], fontsize=6.5)
    ax.set_xlabel("AUC for boom (95% keyword-bootstrap CI)")
    ax.legend(fontsize=6, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
    ax.set_title(f"B1: signals at birth ({int(b1.keywords.max())} new keywords, {int(b1.booms.max())} booms)", loc="left")
    _save(fig, out_dir, "forecast_feature_auc")

    pr, b2 = read("b2_predictions"), read("b2_models")
    fig, ax = plt.subplots(figsize=(3.2, 3.0), constrained_layout=True)
    for i, (col, lab) in enumerate((("p_base", "baseline logit (F1+F2)"), ("p_full", "full L2 logit"))):
        tp, fp, _ = roc_points(pr.boom.to_numpy(), pr[col].to_numpy())
        fpr, tpr = np.r_[0, fp / fp[-1]], np.r_[0, tp / tp[-1]]
        a = b2[(b2.metric == "AUC") & (b2.model == lab)].estimate.iloc[0]
        ax.plot(fpr, tpr, color=figures.SERIES[i], label=f"{lab}, AUC {a:.2f}")
    ax.plot([0, 1], [0, 1], color=figures.MUTED, lw=0.7, ls="--")
    ax.set_xlabel("false positive rate")
    ax.set_ylabel("true positive rate")
    ax.legend(fontsize=6, loc="lower right")
    ax.set_title("B2: out-of-time ROC, cohorts 2021-2024", loc="left")
    _save(fig, out_dir, "forecast_roc")

    b3 = read("b3_table")
    fig, ax = plt.subplots(figsize=(3.2, 2.6), constrained_layout=True)
    m, n = (b3.pivot(index="groups_ge3", columns="areas_ge3", values=v).reindex(index=[True, False], columns=[False, True])
            for v in ("p_boom", "keywords"))
    ax.imshow(m.to_numpy(float), cmap=ramp, vmin=0, vmax=max(0.2, np.nanmax(m.to_numpy(float))))
    for (a, b), v in np.ndenumerate(m.to_numpy(float)):
        ax.text(b, a, f"{v:.1%}\nn={int(n.iat[a, b])}" if np.isfinite(v) else f"n={int(n.iat[a, b])}", ha="center",
                va="center", fontsize=7, color=figures.INK)
    ax.set_xticks([0, 1], ["< 3 areas", ">= 3 areas"])
    ax.set_yticks([0, 1], [">= 3 groups", "< 3 groups"])
    ax.grid(False)
    ax.set_title("B3: P(boom) by independent groups x areas", loc="left")
    _save(fig, out_dir, "forecast_b3")

    pr4, m4 = read("b4_predictions"), read("b4_models")
    fig, axes = plt.subplots(2, 3, figsize=(7.0, 4.4), sharey="row", constrained_layout=True)
    for row, mp in zip(axes, ("early", "k100")):
        g = pr4[pr4["map"] == mp]
        for i, (ax, model) in enumerate(zip(row, TOPIC_MODELS)):
            r2 = m4[(m4["map"] == mp) & (m4.metric == "R2") & (m4.model == model)].estimate.iloc[0]
            ax.scatter(g[f"pred_{model}"], g.target, s=6, color=figures.SERIES[i], alpha=0.6, lw=0)
            ax.axhline(0, color=figures.MUTED, lw=0.6)
            ax.set_title(f"{names[mp]}: {model}, R2 {r2:.2f}", loc="left", fontsize=7)
        row[0].set_ylabel("realised")
    for ax in axes[1]:
        ax.set_xlabel("predicted (year-demeaned)")
    fig.suptitle("B4: topic log share ratio t -> t+2, out of time (test origins 2021-2024)", fontsize=8)
    _save(fig, out_dir, "forecast_topics")


def main() -> None:
    import posthoc
    posthoc.write_outputs(compute_free(), OUT)
    plot(OUT)
    print((OUT / "summary.json").read_text())


if __name__ == "__main__":
    main()
