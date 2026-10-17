"""PH5 teams (final post hoc round, selection S7): who to bring when entering a topic. Within topic x year, at a fixed
team size and a fixed number of authors with ICLR experience, is one co-author who has worked in the topic (an insider)
associated with higher acceptance, and do further insiders add little? Is that different in hot topics? Is a proven
outsider (an author with an earlier accepted ICLR paper, no insider) better or worse than an unproven insider (topic
history, no earlier acceptance)? Does it matter whether the insider is the last or the first author? Post hoc and
exploratory: every estimate is an association; Holm within the declared family ranks the evidence, nothing more.

Population: RQ3 decided papers (rq3, accepted) 2023-2026 with an author ID (history after the 2021-22 author-ID
switch); replication 2019-2020; 2021-2022 excluded.
Author types, per (paper, author ID); outcome-free; history = every discovery submission of the author in an earlier
year, any outcome (posthoc.author_rows): novice = none; crossover = some, none in the paper's k100 topic; insider = at
least one in the paper's k100 topic.
Paper features: n_ins (0, 1, 2, 3+); n_exp = n_cross + n_ins (0..3, 4+); team = distinct author IDs (1..7, 8+); first
and last author type (min / max source_list_position among the author IDs); mid_ins = insiders in neither position;
prior = the sum of the authors' earlier submissions; familiar = n_ins >= 1; proven = posthoc.established_authors (an
author ID with an accepted paper in an earlier year; earlier outcomes, gated); alphabetical = >= 3 listed authors whose
last names (declared_name_json) are in non-decreasing alphabetical order.
Models: LPM with k100 topic x year FE, CR1 by topic, t(G - 1). C = class + FM + has_earlier_version + log(1 + prior);
TS = team-size dummies (ref 1; ref 2 in T3); EXP = n_exp dummies (ref 0).
  T1   accepted ~ 1[n_ins = 1] + 1[n_ins >= 2] + TS + EXP + C
  T1h  T1 + each insider dummy x hot (hot itself is absorbed by the FE)
  T2   accepted ~ proven outsider + unproven insider + proven insider (ref: neither) + TS + EXP + C
  T2h  T2 + each cell x hot
  T3   team >= 2: accepted ~ first only + last only + both insiders + mid_ins + n_ins dummies + TS + EXP + C
Family (Holm over 6): H1 1 vs 0 insiders (T1); H2 concavity (1 vs 0) - (2+ vs 1) = 2 b1 - b2+ (T1); H3 (1 vs 0) in hot
minus other topics (T1h); H4 proven outsider - unproven insider (T2); H5 H4 in hot minus other topics (T2h); H6 last-
author insider - first-author insider (T3). Each with MDE80 = (z_.975 + z_.80) x the SD of the estimate over 200
within-topic-year permutations of acceptance (also at Holm's first step, alpha 0.05 / 6), 2.80 x its CR1 SE, and the
permutation p as a check.
Descriptive, separately for hot and other topics: adjusted P(accept | team size 2..8+, n_ins), P(accept | proven x
familiar) and P(accept | first x last author type), each from an LPM with group dummies | topic x year: adjusted P(g) =
mean acceptance of the heat level + b_g - sum_h w_h b_h (w = group shares), SE from the CR1 covariance of that contrast
(the heat level's mean is taken as fixed). Controls: B = class + FM + has_earlier_version (curves); TS + B (role grid);
TS + EXP + C (proven x familiar, as T2). The curves and the grid leave out log(1 + prior), which rises mechanically with
team size and with insiders and would absorb part of the gradients they describe. Additive type decomposition:
accepted ~ n_nov + n_cross + n_ins (each capped at 4) + class + FM + has_earlier_version | topic x year, next to the
log2 team-size slope on the same papers (PH2's gradient).
Robustness (H1-H6 re-estimated, raw p, no family): logit with topic x year dummies (log-odds; CR1 by topic; cells without
outcome variation dropped); keyword insider (an earlier submission of the author lists one of the paper's author keywords
typed research_area / specific_topic / property / application_domain; papers listing one); early-map insider; without
papers with a probable earlier version; T3 without alphabetical lists; the 2019-2020 replication. A variant whose fit
fails on the outcomes (e.g. logit separation) is reported with its error instead of stopping the run.
calibrate(): size and planted-effect recovery on simulated frames (see its docstring).
"""
from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
from scipy import stats

import panel
import ph5_common
import posthoc
from common import DATA, TOPICS, topic_layer
from ols import demean
from panel import CLASS_CONTROLS
from variants import holm

YEARS, REPLICATION = (2023, 2026), (2019, 2020)
TS_CAP, EXP_CAP, INS_CAP, TYPE_CAP, TEAM_LOG_CAP = 8, 4, 3, 4, 16
TOPICAL = ("research_area", "specific_topic", "property", "application_domain")
DEFINITIONS = ("k100", "early", "keyword")
TYPES = ["novice", "crossover", "insider"]
CELLS = ["neither", "unproven insider", "proven outsider", "proven insider"]       # code 2 x proven + familiar
SUFFIXES = {"jr", "sr", "ii", "iii", "iv"}
BASE = CLASS_CONTROLS + ["fm", "has_earlier_version"]
CONTROLS = BASE + ["log_prior"]
TS = [f"ts_{v}" for v in range(2, TS_CAP + 1)]
EXP = [f"exp_{v}" for v in range(1, EXP_CAP + 1)]
MODELS = {"T1": ["ins1", "ins2p"],
          "T1h": ["ins1", "ins2p", "ins1_x_hot", "ins2p_x_hot"],
          "T2": ["po", "ui", "pi"],
          "T2h": ["po", "ui", "pi", "po_x_hot", "ui_x_hot", "pi_x_hot"],
          "T3": ["f_only", "l_only", "both", "mid_ins", "nins_1", "nins_2", "nins_3p"]}
FAMILY = {"H1": ("T1", {"ins1": 1.0}, "one insider vs none"),
          "H2": ("T1", {"ins1": 2.0, "ins2p": -1.0}, "concavity: (1 vs 0) - (2+ vs 1)"),
          "H3": ("T1h", {"ins1_x_hot": 1.0}, "(1 vs 0) in hot minus other topics"),
          "H4": ("T2", {"po": 1.0, "ui": -1.0}, "proven outsider - unproven insider"),
          "H5": ("T2h", {"po_x_hot": 1.0, "ui_x_hot": -1.0}, "H4 in hot minus other topics"),
          "H6": ("T3", {"l_only": 1.0, "f_only": -1.0}, "last-author insider - first-author insider")}
DERIVED = {"T1": {"2+ vs 1 insiders": {"ins2p": 1.0, "ins1": -1.0}},
           "T1h": {"1 vs 0, other topics": {"ins1": 1.0}, "1 vs 0, hot topics": {"ins1": 1.0, "ins1_x_hot": 1.0},
                   "2+ vs 0, other topics": {"ins2p": 1.0}, "2+ vs 0, hot topics": {"ins2p": 1.0, "ins2p_x_hot": 1.0}},
           "T2": {"proven insider - unproven insider": {"pi": 1.0, "ui": -1.0},
                  "proven insider - proven outsider": {"pi": 1.0, "po": -1.0}},
           "T2h": {"PO - UI, other topics": {"po": 1.0, "ui": -1.0},
                   "PO - UI, hot topics": {"po": 1.0, "ui": -1.0, "po_x_hot": 1.0, "ui_x_hot": -1.0}},
           "T3": {"both - first only": {"both": 1.0, "f_only": -1.0}, "both - last only": {"both": 1.0, "l_only": -1.0}}}
PERMS, SEED, MIN_GROUP, PLANT = 200, 20261017, 30, 0.3
Z975, Z80, Z_HOLM = stats.norm.ppf(0.975), stats.norm.ppf(0.80), stats.norm.ppf(1 - 0.05 / 12)
NOTE = "post hoc exploratory (PH5 teams, selection S7); associations, not causal effects"


# ---------------------------------------------------------------------------------------------------- features
def read_authors() -> pd.DataFrame:
    """Every listed author of every submission: submission_id, key (NaN without an ID), position, name."""
    return pd.read_csv(DATA / "submission_authors.csv.gz", keep_default_na=False, na_values=[r"\N"],
                       usecols=["submission_id", "declared_id_key", "source_list_position", "declared_name_json"]).rename(
        columns={"declared_id_key": "key", "source_list_position": "position", "declared_name_json": "name"})


def topical_keywords() -> pd.DataFrame:
    """(submission_id, kw): the paper's author keywords typed research_area / specific_topic / property /
    application_domain (keyword_types.csv)."""
    kt = pd.read_csv(TOPICS / "keyword_types.csv", keep_default_na=False)
    vocab = set(kt[kt.type.isin(TOPICAL)].keyword)
    c = topic_layer().embedded_corpus()[["submission_id", "keywords"]]
    pairs = c.assign(kw=c.keywords.map(lambda x: sorted(set(x) & vocab))).explode("kw").dropna(subset=["kw"])
    return pairs[["submission_id", "kw"]].reset_index(drop=True)


def prior(at: pd.DataFrame, unit: str | None) -> np.ndarray:
    """Per author row: the author's submissions in earlier years (in the same unit, e.g. topic, if given)."""
    keys = ["key"] + ([unit] if unit else [])
    n = at.groupby(keys + ["year"]).size().rename("n").reset_index()
    n["prior"] = n.groupby(keys).n.cumsum() - n.n
    return at[keys + ["year"]].merge(n, on=keys + ["year"], how="left").prior.to_numpy(float)


def keyword_prior(at: pd.DataFrame, kw: pd.DataFrame) -> np.ndarray:
    """Per author row: 1 if the author has an earlier-year submission listing one of this paper's keywords (kw pairs),
    0 if not, NaN if the paper lists none (posthoc.keyword_incumbent, over every keyword of the paper)."""
    ak = at[["submission_id", "key", "year"]].merge(kw, on="submission_id")
    first = ak.groupby(["key", "kw"]).year.transform("min")
    hit = ak[first < ak.year].drop_duplicates(["submission_id", "key"]).assign(hit=1.0)
    out = at[["submission_id", "key"]].merge(hit[["submission_id", "key", "hit"]], on=["submission_id", "key"], how="left")
    return np.where(at.submission_id.isin(set(kw.submission_id)), out.hit.fillna(0.0).to_numpy(), np.nan)


def classify(prior_any: np.ndarray, prior_unit: np.ndarray) -> np.ndarray:
    """0 novice (no earlier submission), 1 crossover (none in the unit), 2 insider; NaN if the unit is undefined."""
    prior_any, prior_unit = np.asarray(prior_any, float), np.asarray(prior_unit, float)
    return np.where(prior_any == 0, 0.0, np.where(np.isnan(prior_unit), np.nan, np.where(prior_unit >= 1, 2.0, 1.0)))


def paper_level(at: pd.DataFrame, names: tuple[str, ...]) -> pd.DataFrame:
    """Per paper (index submission_id) from author rows with position, prior_any and type_<name> columns."""
    at = at.sort_values(["submission_id", "position"], kind="stable").reset_index(drop=True)
    g = at.groupby("submission_id", sort=False)
    rank, size = g.cumcount().to_numpy(), g.position.transform("size").to_numpy()
    first, last = rank == 0, rank == size - 1
    sid = at.submission_id.to_numpy()
    f = pd.DataFrame({"team": g.size(), "n_exp": (at.prior_any > 0).groupby(sid, sort=False).sum(),
                      "prior": g.prior_any.sum()})
    for name in names:
        t = at[f"type_{name}"]
        ins = (t == 2).astype(float).where(t.notna())
        f[f"n_ins_{name}"] = ins.groupby(sid).sum(min_count=1).where(t.notna().groupby(sid).all())
        f[f"first_{name}"] = pd.Series(t.to_numpy()[first], index=sid[first])
        f[f"last_{name}"] = pd.Series(t.to_numpy()[last], index=sid[last])
        f[f"mid_ins_{name}"] = ins.where(~first & ~last, 0.0).groupby(sid).sum(min_count=1).where(f[f"n_ins_{name}"].notna())
    return f


def surname(raw: str) -> str:
    try:
        s = json.loads(raw)
    except (ValueError, TypeError):
        s = raw
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    toks = [t for t in (re.sub(r"[^a-z]", "", w) for w in s.split()) if t and t not in SUFFIXES]
    return toks[-1] if toks else ""


def alphabetical(rows: pd.DataFrame) -> pd.Series:
    """Per paper: at least 3 listed authors whose last names are in non-decreasing alphabetical order."""
    r = rows.sort_values(["submission_id", "position"], kind="stable").assign(sur=lambda x: x.name.map(surname))
    prev = r.groupby("submission_id").sur.shift()
    ok = (prev.isna() | (r.sur >= prev)) & (r.sur != "")
    g = ok.groupby(r.submission_id)
    return g.all() & (g.size() >= 3)


@lru_cache(maxsize=1)
def paper_features() -> pd.DataFrame:
    """Outcome-free paper features in panel.frame('k100') row order (index submission_id): team, n_exp, prior, and per
    insider definition (k100, early, keyword) n_ins_, first_, last_ (0 novice, 1 crossover, 2 insider), mid_ins_;
    alphabetical; has_keyword (lists a topical typed keyword). Papers without an author ID have NaN team."""
    k = panel.frame("k100")
    rows = read_authors()
    rows = rows[rows.submission_id.isin(set(k.submission_id))]
    at = rows.dropna(subset=["key"]).groupby(["submission_id", "key"]).position.min().reset_index()
    at = at.merge(k[["submission_id", "year", "topic", "topic_early"]], on="submission_id")
    kw = topical_keywords()
    at["prior_any"] = prior(at, None)
    at["type_k100"] = classify(at.prior_any, prior(at, "topic"))
    at["type_early"] = classify(at.prior_any, prior(at, "topic_early"))
    at["type_keyword"] = classify(at.prior_any, keyword_prior(at, kw))
    f = paper_level(at, DEFINITIONS).reindex(k.submission_id)
    f["alphabetical"] = alphabetical(rows).reindex(k.submission_id).fillna(False).astype(bool).to_numpy()
    f["has_keyword"] = k.submission_id.isin(set(kw.submission_id)).to_numpy()
    return f


def design(d: pd.DataFrame, name: str = "k100") -> pd.DataFrame:
    """d with the insider definition `name` as n_ins / n_cross / first_type / last_type / mid_ins and all model columns."""
    d = d.assign(n_ins=d[f"n_ins_{name}"], first_type=d[f"first_{name}"], last_type=d[f"last_{name}"],
                 mid_ins=d[f"mid_ins_{name}"])
    assert d.n_ins.notna().all() and d.team.notna().all(), f"insider definition {name} undefined for some papers"
    d["n_cross"] = d.n_exp - d.n_ins
    fam, pr = d.n_ins >= 1, d.proven == 1
    fi, la = d.first_type == 2, d.last_type == 2
    X = {"ins1": d.n_ins == 1, "ins2p": d.n_ins >= 2, "nins_1": d.n_ins == 1, "nins_2": d.n_ins == 2,
         "nins_3p": d.n_ins >= 3, "po": pr & ~fam, "ui": ~pr & fam, "pi": pr & fam,
         "f_only": fi & ~la, "l_only": la & ~fi, "both": fi & la}
    X = pd.DataFrame(X).astype(float)
    for c in ["ins1", "ins2p", "po", "ui", "pi"]:
        X[f"{c}_x_hot"] = X[c] * d.hot
    ts, ex = d.team.clip(upper=TS_CAP), d.n_exp.clip(upper=EXP_CAP)
    for v in range(2, TS_CAP + 1):
        X[f"ts_{v}"] = (ts == v).astype(float)
    for v in range(1, EXP_CAP + 1):
        X[f"exp_{v}"] = (ex == v).astype(float)
    return pd.concat([d.drop(columns=[c for c in X.columns if c in d]), X], axis=1)


def population(k: pd.DataFrame, years: tuple[int, int] = YEARS) -> pd.DataFrame:
    """Decided papers with an author ID and a heat flag in `years`, with features, proven and the k100 design."""
    k = k.reset_index(drop=True)
    f = paper_features().reindex(k.submission_id)
    d = k.assign(proven=posthoc.established_authors(k).astype(float), **{c: f[c].to_numpy() for c in f.columns})
    d = d[d.rq3.astype(bool) & d.has_author_key & d.year.between(*years) & d.hot.notna()].copy()
    d["log_prior"] = np.log1p(d.prior)
    return design(d, "k100")


# ---------------------------------------------------------------------------------------------------- estimators
@dataclass
class Fit:
    beta: pd.Series
    vcov: pd.DataFrame
    G: int
    n: int
    A: np.ndarray | None = None          # LPM: beta = A @ yd (rows: kept regressors)
    yd: np.ndarray | None = None         # LPM: the outcome demeaned within the absorbed groups
    groups: np.ndarray | None = None     # LPM: absorbed-group codes of the rows

    def weights(self, w: dict[str, float]) -> np.ndarray | None:
        return None if not set(w) <= set(self.beta.index) else np.array([w.get(c, 0.0) for c in self.beta.index])

    def contrast(self, w: dict[str, float]) -> dict:
        c = self.weights(w)
        out = {"estimate": np.nan, "se": np.nan, "p": np.nan, "ci95_lo": np.nan, "ci95_hi": np.nan, "n": self.n,
               "clusters": self.G}
        if c is None:
            return out
        est, se = float(c @ self.beta.to_numpy()), float(np.sqrt(max(c @ self.vcov.to_numpy() @ c, 0.0)))
        q = stats.t.ppf(0.975, self.G - 1)
        out.update(estimate=est, se=se, ci95_lo=est - q * se, ci95_hi=est + q * se,
                   p=float(2 * stats.t.sf(abs(est / se), self.G - 1)) if se > 0 else np.nan)
        return out


def independent(Xd: np.ndarray) -> np.ndarray:
    """Columns to keep, in order: drops columns without within-group variation, then later columns that are linear
    combinations of earlier ones (e.g. an empty dummy level in a subsample)."""
    keep = Xd.std(axis=0) > 1e-12
    if np.linalg.matrix_rank(Xd[:, keep]) == keep.sum():
        return keep
    kept: list[int] = []
    for j in np.flatnonzero(keep):
        if np.linalg.matrix_rank(Xd[:, kept + [j]]) == len(kept) + 1:
            kept.append(j)
    return np.isin(np.arange(Xd.shape[1]), kept)


def cr1(u: np.ndarray, bread: np.ndarray, clusters: np.ndarray, k: int) -> tuple[np.ndarray, int]:
    """CR1 sandwich from per-row scores u, scaled G/(G-1) (n-1)/(n-k) as ols.fe_ols."""
    c = pd.factorize(clusters)[0]
    G, n = int(c.max() + 1), len(u)
    S = np.zeros((G, u.shape[1]))
    np.add.at(S, c, u)
    return (G / (G - 1)) * ((n - 1) / (n - k)) * bread @ (S.T @ S) @ bread, G


def lpm(d: pd.DataFrame, y: str, xs: list[str], absorb: str = "cell", cluster: str = "topic") -> Fit:
    """OLS with `absorb` FE (demeaning) and CR1 SE by `cluster` (as ols.fe_ols), keeping A for permutations."""
    s = d.dropna(subset=[y, *xs])
    g = pd.factorize(s[absorb])[0]
    yd, Xd = demean(s[y].to_numpy(float), g), demean(s[xs].to_numpy(float), g)
    keep = independent(Xd)
    xs, Xd = [x for x, kk in zip(xs, keep) if kk], Xd[:, keep]
    bread = np.linalg.inv(Xd.T @ Xd)
    A = bread @ Xd.T
    beta = A @ yd
    V, G = cr1(Xd * (yd - Xd @ beta)[:, None], bread, s[cluster].to_numpy(), Xd.shape[1])
    return Fit(pd.Series(beta, xs), pd.DataFrame(V, xs, xs), G, len(yd), A, yd, g)


def logit(d: pd.DataFrame, y: str, xs: list[str], absorb: str = "cell", cluster: str = "topic",
          tol: float = 1e-10, max_iter: int = 100) -> Fit:
    """Logit with a full set of `absorb` dummies, by Newton steps with the dummies concentrated out (exact: the Schur
    complement of the Hessian is the weighted within design). Groups without outcome variation are dropped. CR1 SE
    by `cluster` with k counting every parameter (as logit.fe_logit)."""
    s = d.dropna(subset=[y, *xs])
    rate = s.groupby(absorb)[y].transform("mean")
    s = s[(rate > 0) & (rate < 1)]
    g = pd.factorize(s[absorb])[0]
    m = int(g.max() + 1)
    keep = independent(demean(s[xs].to_numpy(float), g))
    xs = [x for x, kk in zip(xs, keep) if kk]
    X, yv = s[xs].to_numpy(float), s[y].to_numpy(float)
    b, a = np.zeros(len(xs)), np.log(np.bincount(g, yv) / (np.bincount(g) - np.bincount(g, yv)))

    def loglik(b_: np.ndarray, a_: np.ndarray) -> float:
        eta = X @ b_ + a_[g]
        return float(np.sum(yv * eta - np.logaddexp(0.0, eta)))

    def within(w: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        W = np.bincount(g, w, minlength=m)
        means = np.vstack([np.bincount(g, w * X[:, j], minlength=m) for j in range(X.shape[1])]).T / W[:, None]
        return X - means[g], W

    ll = loglik(b, a)
    for _ in range(max_iter):
        p = 1 / (1 + np.exp(-(X @ b + a[g])))
        w, r = p * (1 - p), yv - p
        Xt, W = within(w)
        db = np.linalg.solve(Xt.T @ (Xt * w[:, None]), Xt.T @ r)
        da = (np.bincount(g, r, minlength=m) - np.bincount(g, w * (X @ db), minlength=m)) / W
        t = 1.0
        while True:
            nll = loglik(b + t * db, a + t * da)
            if nll >= ll - 1e-12 or t < 1e-8:
                break
            t /= 2
        b, a, ll_old, ll = b + t * db, a + t * da, ll, nll
        if max(np.abs(t * db).max(initial=0), np.abs(t * da).max()) < tol or abs(ll - ll_old) < tol * (1 + abs(ll)):
            break
    else:
        raise RuntimeError("logit did not converge")
    p = 1 / (1 + np.exp(-(X @ b + a[g])))
    Xt, _ = within(p * (1 - p))
    bread = np.linalg.inv(Xt.T @ (Xt * (p * (1 - p))[:, None]))
    V, G = cr1(Xt * (yv - p)[:, None], bread, s[cluster].to_numpy(), len(xs) + m)
    return Fit(pd.Series(b, xs), pd.DataFrame(V, xs, xs), G, len(yv))


def fit_models(d: pd.DataFrame, y: str = "accepted", est: Callable[..., Fit] = lpm,
               only: list[str] | None = None) -> dict[str, Fit]:
    out = {}
    for m, focal in MODELS.items():
        if only is not None and m not in only:
            continue
        s, ts = (d[d.team >= 2], TS[1:]) if m == "T3" else (d, TS)
        out[m] = est(s, y, focal + ts + EXP + CONTROLS)
    return out


def family_table(fits: dict[str, Fit], adjust: bool = True) -> pd.DataFrame:
    rows = [{"test": h, "model": m, "label": lab, **fits[m].contrast(w)} for h, (m, w, lab) in FAMILY.items() if m in fits]
    r = pd.DataFrame(rows)
    r["mde80_se"] = (Z975 + Z80) * r.se
    if adjust:
        r["p_holm"] = holm(r.p.fillna(1.0)).to_numpy()
    return r


def estimates_table(fits: dict[str, Fit]) -> pd.DataFrame:
    rows = []
    for m, f in fits.items():
        rows += [{"model": m, "term": x, **f.contrast({x: 1.0})} for x in MODELS[m]]
        rows += [{"model": m, "term": lab, **f.contrast(w)} for lab, w in DERIVED.get(m, {}).items()]
    return pd.DataFrame(rows)


def within_permutation(groups: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Row indices permuted at random within groups."""
    base = np.argsort(groups, kind="stable")
    perm = np.empty(len(groups), int)
    perm[base] = np.lexsort((rng.random(len(groups)), groups))
    return perm


def permutation_mde(fits: dict[str, Fit], perms: int, rng: np.random.Generator) -> pd.DataFrame:
    """Per family test: SD of the LPM estimate over within-topic-year permutations of acceptance, MDE80 and perm p."""
    rows = []
    for h, (m, w, _) in FAMILY.items():
        f = fits[m]
        c = f.weights(w)
        if c is None:
            rows.append({"test": h})
            continue
        a = c @ f.A
        obs = float(a @ f.yd)
        draws = np.array([a @ f.yd[within_permutation(f.groups, rng)] for _ in range(perms)])
        sd = float(draws.std(ddof=1))
        rows.append({"test": h, "perm_sd": sd, "perm_p": float((1 + (np.abs(draws) >= abs(obs)).sum()) / (1 + perms)),
                     "mde80": (Z975 + Z80) * sd, "mde80_holm": (Z_HOLM + Z80) * sd})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------------- descriptive
def adjusted(d: pd.DataFrame, label: pd.Series, extra: list[str], y: str = "accepted") -> pd.DataFrame:
    """Adjusted acceptance by group (label aligned with d): LPM y ~ group dummies (ref: largest group) + extra |
    topic x year; adjusted P(g) = mean y + b_g - sum_h w_h b_h over the estimable groups (w = their shares)."""
    s = d.assign(_g=label).dropna(subset=[y, "_g", *extra])
    counts = s._g.value_counts()
    ref = counts.index[0]
    names = {lev: f"_g{i}" for i, lev in enumerate(counts.index) if lev != ref}
    s = s.assign(**{c: (s._g == lev).astype(float) for lev, c in names.items()})
    f = lpm(s, y, list(names.values()) + extra)
    ok = [ref] + [lev for lev, c in names.items() if c in f.beta.index]
    w = counts.loc[ok] / counts.loc[ok].sum()
    ybar = float(s[s._g.isin(ok)][y].mean())
    raw = s.groupby("_g")[y].mean()
    rows = []
    for lev in sorted(counts.index):
        r = {"group": lev, "papers": int(counts.loc[lev]), "raw_rate": float(raw.loc[lev])}
        if lev in ok:
            c = {names[h]: -float(w.loc[h]) for h in ok if h != ref}
            if lev != ref:
                c[names[lev]] += 1.0
            e = f.contrast(c) if c else {"estimate": 0.0, "se": 0.0, "ci95_lo": 0.0, "ci95_hi": 0.0}
            r.update(adjusted=ybar + e["estimate"], se=e["se"], ci95_lo=ybar + e["ci95_lo"], ci95_hi=ybar + e["ci95_hi"])
        rows.append(r)
    return pd.DataFrame(rows)


def curves(d: pd.DataFrame) -> pd.DataFrame:
    out = []
    for hot in (0.0, 1.0):
        s = d[(d.hot == hot) & (d.team >= 2)]
        a = adjusted(s, s.team.clip(upper=TS_CAP).astype(int) * 10 + s.n_ins.clip(upper=INS_CAP).astype(int), BASE)
        out.append(a.assign(hot=hot, team=a.group // 10, n_ins=a.group % 10))
    return pd.concat(out, ignore_index=True).drop(columns="group")


def proven_familiar(d: pd.DataFrame) -> pd.DataFrame:
    out = []
    for hot in (0.0, 1.0):
        s = d[d.hot == hot]
        a = adjusted(s, (2 * s.proven + (s.n_ins >= 1)).astype(int), TS + EXP + CONTROLS)
        out.append(a.assign(hot=hot, cell=a.group.map(dict(enumerate(CELLS)))))
    return pd.concat(out, ignore_index=True)


def role_grid(d: pd.DataFrame) -> pd.DataFrame:
    out = []
    for hot in (0.0, 1.0):
        s = d[(d.hot == hot) & (d.team >= 2)]
        a = adjusted(s, (3 * s.first_type + s.last_type).astype(int), TS[1:] + BASE)
        out.append(a.assign(hot=hot, first=a.group.map(lambda v: TYPES[v // 3]), last=a.group.map(lambda v: TYPES[v % 3])))
    return pd.concat(out, ignore_index=True)


def decomposition(d: pd.DataFrame) -> pd.DataFrame:
    s = d.assign(n_nov_c=(d.team - d.n_exp).clip(upper=TYPE_CAP), n_cross_c=d.n_cross.clip(upper=TYPE_CAP),
                 n_ins_c=d.n_ins.clip(upper=TYPE_CAP), log2_team=np.log2(d.team.clip(1, TEAM_LOG_CAP)))
    f = lpm(s, "accepted", ["n_nov_c", "n_cross_c", "n_ins_c"] + BASE)
    terms = {"per novice": {"n_nov_c": 1.0}, "per crossover": {"n_cross_c": 1.0}, "per insider": {"n_ins_c": 1.0},
             "insider - crossover": {"n_ins_c": 1.0, "n_cross_c": -1.0},
             "crossover - novice": {"n_cross_c": 1.0, "n_nov_c": -1.0}}
    rows = [{"model": "additive types", "term": t, **f.contrast(w)} for t, w in terms.items()]
    g = lpm(s, "accepted", ["log2_team"] + BASE)
    return pd.DataFrame(rows + [{"model": "PH2 gradient, same papers", "term": "per doubling of team size",
                                 **g.contrast({"log2_team": 1.0})}])


# ---------------------------------------------------------------------------------------------------- analysis
def robustness(k: pd.DataFrame, d: pd.DataFrame) -> pd.DataFrame:
    variants = [("logit (log-odds)", d, "k100", logit, None),
                ("keyword insider", d[d.has_keyword], "keyword", lpm, None),
                ("early-map insider", d, "early", lpm, None),
                ("without earlier versions", d[d.has_earlier_version == 0], "k100", lpm, None),
                ("T3 without alphabetical lists", d[~d.alphabetical.astype(bool)], "k100", lpm, ["T3"]),
                ("2019-2020 replication", population(k, REPLICATION), "k100", lpm, None)]
    rows = []
    for name, s, defn, est, only in variants:
        try:                                    # outcome-dependent failures (e.g. logit separation) must not stop the run
            tab = family_table(fit_models(design(s, defn), "accepted", est, only), adjust=False)
        except (RuntimeError, np.linalg.LinAlgError) as e:
            rows.append({"variant": name, "error": repr(e)})
            continue
        rows += [{"variant": name, **r} for r in tab.to_dict("records")]
    return pd.DataFrame(rows)


def counts(d: pd.DataFrame) -> dict:
    t2 = 2 * d.proven + (d.n_ins >= 1)
    multi = d[d.team >= 2]
    return {"papers": int(len(d)), "topics": int(d.topic.nunique()), "hot_share": float(d.hot.mean()),
            "papers_by_n_ins": d.n_ins.clip(upper=INS_CAP).astype(int).value_counts().sort_index().to_dict(),
            "papers_by_n_exp": d.n_exp.clip(upper=EXP_CAP).astype(int).value_counts().sort_index().to_dict(),
            "papers_by_proven_familiar": {CELLS[int(c)]: int(n) for c, n in t2.value_counts().sort_index().items()},
            "papers_by_role_t3": {"first only": int(multi.f_only.sum()), "last only": int(multi.l_only.sum()),
                                  "both": int(multi.both.sum())},
            "alphabetical_share_t3": float(multi.alphabetical.mean())}


def compute(k: pd.DataFrame, perms: int = PERMS) -> dict:
    k = k.reset_index(drop=True)
    d = population(k)
    fits = fit_models(d)
    fam = family_table(fits).merge(permutation_mde(fits, perms, np.random.default_rng(SEED)), on="test", how="left")
    rep = population(k, REPLICATION)
    summary = {"population": {**counts(d), "years": list(YEARS), "acceptance_rate": float(d.accepted.mean())},
               "replication_population": {**counts(rep), "years": list(REPLICATION)},
               "family": fam[["test", "label", "estimate", "se", "p", "p_holm", "mde80", "perm_p"]].to_dict("records"),
               "permutations": perms, "note": NOTE}
    return {"family": fam, "estimates": estimates_table(fits), "robustness": robustness(k, d), "curves": curves(d),
            "proven_familiar": proven_familiar(d), "role_grid": role_grid(d), "decomposition": decomposition(d),
            "summary": summary}


def compute_free() -> dict:
    """Outcome-free descriptives (any submission status) of the features, 2023-2026 and 2019-2020."""
    k = panel.frame("k100").reset_index(drop=True)
    f = paper_features().reindex(k.submission_id)
    d = k.assign(**{c: f[c].to_numpy() for c in f.columns})
    d = d[d.has_author_key & d.team.notna()]
    out, summary = {}, {}
    for label, years in [("main", YEARS), ("replication", REPLICATION)]:
        e = d[d.year.between(*years) & d.hot.notna()]
        ins = e.n_ins_k100.clip(upper=INS_CAP).astype(int)
        multi = e[e.team >= 2]
        fam = {n: (e[f"n_ins_{n}"] >= 1)[e[f"n_ins_{n}"].notna()] for n in DEFINITIONS}
        summary[label] = {
            "years": list(years), "papers": int(len(e)), "team_median": float(e.team.median()),
            "papers_by_n_ins": ins.value_counts().sort_index().to_dict(),
            "familiar_share_by_year": (e.n_ins_k100 >= 1).groupby(e.year).mean().round(4).to_dict(),
            "mean_n_exp_by_year": e.n_exp.groupby(e.year).mean().round(3).to_dict(),
            "familiar_equals_frame_incumbent": float(((e.n_ins_k100 >= 1).astype(float) == e.incumbent).mean()),
            "familiar_share": {n: float(v.mean()) for n, v in fam.items()},
            "agreement_with_k100_familiar": {n: float((fam[n] == fam["k100"].reindex(fam[n].index)).mean())
                                             for n in ("early", "keyword")},
            "has_keyword_share": float(e.has_keyword.mean()),
            "alphabetical_share_by_team": multi.alphabetical.groupby(multi.team.clip(upper=6)).mean().round(4).to_dict(),
            "n_ins_levels_present_at_every_team_size_2_8": bool(
                (pd.crosstab(e.team.clip(upper=TS_CAP), ins).loc[3:] > 0).all().all())}
        out[f"free_team_by_insiders_{label}"] = (pd.crosstab([e.hot, e.team.clip(upper=TS_CAP).astype(int)], ins)
                                                 .rename(columns=lambda c: f"n_ins_{c}").reset_index())
        grid = pd.crosstab([multi.hot, multi.first_k100.astype(int).map(dict(enumerate(TYPES)))],
                           multi.last_k100.astype(int).map(dict(enumerate(TYPES))))
        out[f"free_role_grid_{label}"] = grid.rename(columns=lambda c: f"last_{c}").reset_index().rename(
            columns={"first_k100": "first"})
    out["summary"] = summary
    return out


# ---------------------------------------------------------------------------------------------------- calibration
def plant_threshold(k: pd.DataFrame) -> np.ndarray:
    """+PLANT log-odds if the paper has at least one k100 insider, nothing more (H1, H2)."""
    return PLANT * (paper_features().reindex(k.submission_id).n_ins_k100.fillna(0).to_numpy() >= 1)


def plant_last(k: pd.DataFrame) -> np.ndarray:
    """+PLANT log-odds if the last author is a k100 insider (H6)."""
    return PLANT * (paper_features().reindex(k.submission_id).last_k100.to_numpy() == 2)


PLANTS: dict[str, Callable[[pd.DataFrame], np.ndarray] | None] = {"null": None, "threshold": plant_threshold,
                                                                  "last_author": plant_last}


def true_prob(k: pd.DataFrame, plant: Callable[[pd.DataFrame], np.ndarray] | None) -> np.ndarray:
    """The simulated acceptance probability of ph5_common.fake_outcomes (year base rate, plus the plant)."""
    base = dict(zip(range(2017, 2027), np.linspace(0.45, 0.32, 10)))
    b = k.year.map(base).fillna(0.4).to_numpy(float)
    eta = np.log(b / (1 - b)) + (0.0 if plant is None else np.asarray(plant(k), float))
    return 1 / (1 + np.exp(-eta))


def calibrate(n_null: int = 200, n_planted: int = 50, seed: int = 0) -> dict:
    """Run the family on simulated frames: null (acceptance by year only), a threshold plant (+0.3 log-odds with at
    least one insider) and a last-author-insider plant (+0.3 log-odds). Per plant and test: rejection at 0.05 (raw and
    Holm over the six), mean and SD of the estimate, the target (the same LPM contrast computed on the true
    probabilities of the same frame, i.e. the estimator's expectation), bias, 95% CI coverage of the target; per plant,
    the share of frames with any Holm rejection; MDE80 = (z_.975 + z_.80) x the null SD of each estimate."""
    rows = []
    for j, (name, plant) in enumerate(PLANTS.items()):
        for i in range(n_null if plant is None else n_planted):
            s = seed + 10_000 * j + i
            k = ph5_common.simulated_frame(s, plant)
            d = population(k.assign(p_true=true_prob(k, plant)))
            fam = family_table(fit_models(d))
            tgt = family_table(fit_models(d, "p_true"), adjust=False).set_index("test").estimate
            rows += [{"plant": name, "frame": s, **r, "target": tgt[r["test"]]} for r in fam.to_dict("records")]
    r = pd.DataFrame(rows)
    r["reject"], r["reject_holm"] = r.p < 0.05, r.p_holm < 0.05
    r["covered"] = (r.ci95_lo <= r.target) & (r.target <= r.ci95_hi)
    per = (r.groupby(["plant", "test"], sort=False)
           .agg(frames=("frame", "size"), reject=("reject", "mean"), reject_holm=("reject_holm", "mean"),
                mean_estimate=("estimate", "mean"), sd_estimate=("estimate", "std"), mean_se=("se", "mean"),
                mean_target=("target", "mean"), coverage=("covered", "mean"))
           .reset_index())
    per["bias"] = per.mean_estimate - per.mean_target
    null_sd = per[per.plant == "null"].set_index("test").sd_estimate
    per["mde80_null_sd"] = per.test.map((Z975 + Z80) * null_sd)
    fam_any = r.groupby(["plant", "frame"]).reject_holm.any().groupby("plant").mean()
    return {"per_test": per.to_dict("records"), "family_any_holm_rejection": fam_any.round(4).to_dict(),
            "n_null": n_null, "n_planted": n_planted, "seed": seed, "plant_log_odds": PLANT}


# ---------------------------------------------------------------------------------------------------- figures
def _save(fig, out_dir: Path, name: str) -> None:
    import figures
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out_dir / f"{name}.png", dpi=220, bbox_inches="tight")
    figures.plt.close(fig)


def plot(out_dir: Path) -> None:
    import figures
    plt = figures.plt
    out_dir = Path(out_dir)
    heat = {0.0: "other topics", 1.0: "hot topics"}

    cur = pd.read_csv(out_dir / "curves.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.0), sharey=True, constrained_layout=True)
    for ax, (h, title) in zip(axes, heat.items()):
        for i in range(INS_CAP + 1):
            c = cur[(cur.hot == h) & (cur.n_ins == i) & (cur.papers >= MIN_GROUP)].sort_values("team")
            x = c.team + (i - 1.5) * 0.08
            ax.errorbar(x, c.adjusted * 100, yerr=[(c.adjusted - c.ci95_lo) * 100, (c.ci95_hi - c.adjusted) * 100],
                        fmt="-o", ms=3.5, lw=1.4, elinewidth=0.7, color=figures.SERIES[i],
                        label=f"{i}{'+' if i == INS_CAP else ''} insider{'s' if i != 1 else ''}")
        ax.set_xticks(range(2, TS_CAP + 1), [str(v) for v in range(2, TS_CAP)] + [f"{TS_CAP}+"])
        ax.set_xlabel("team size (author IDs)")
        ax.set_title(title, loc="left")
    axes[0].set_ylabel("adjusted acceptance, % (95% CI)")
    axes[1].legend(loc="center left", bbox_to_anchor=(1.01, 0.5))
    fig.suptitle(f"Acceptance by team size and topic insiders, within topic-year (groups with >= {MIN_GROUP} papers; "
                 "post hoc, exploratory)", x=0.01, ha="left", fontsize=8.5)
    _save(fig, out_dir, "teams_curves")

    pf = pd.read_csv(out_dir / "proven_familiar.csv")
    fig, ax = plt.subplots(figsize=(6.2, 2.9), constrained_layout=True)
    x = np.arange(len(CELLS))
    for j, (h, title) in enumerate(heat.items()):
        c = pf[pf.hot == h].set_index("cell").reindex(CELLS)
        xx = x + (j - 0.5) * 0.36
        ax.bar(xx, c.adjusted * 100, width=0.34, color=figures.SERIES[j], label=title, edgecolor=figures.SURFACE, lw=1)
        ax.errorbar(xx, c.adjusted * 100, yerr=[(c.adjusted - c.ci95_lo) * 100, (c.ci95_hi - c.adjusted) * 100],
                    fmt="none", ecolor=figures.INK2, elinewidth=0.8, capsize=2)
        for xi, n in zip(xx, c.papers):
            ax.annotate(f"n={int(n)}" if np.isfinite(n) else "", (xi, 0), xytext=(0, 2), textcoords="offset points",
                        ha="center", fontsize=6, color=figures.SURFACE)
    ax.set_xticks(x, CELLS)
    ax.set_ylabel("adjusted acceptance, % (95% CI)")
    ax.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0))
    ax.set_title("Proven (earlier ICLR acceptance) x familiar (topic insider), same team size and experience\n"
                 "post hoc, exploratory", loc="left")
    _save(fig, out_dir, "teams_proven_familiar")

    rg = pd.read_csv(out_dir / "role_grid.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.1), constrained_layout=True)
    lo, hi = np.nanmin(rg.adjusted) * 100, np.nanmax(rg.adjusted) * 100
    cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list("ramp", figures.BLUE_RAMP)
    for ax, (h, title) in zip(axes, heat.items()):
        g = rg[rg.hot == h]
        piv = g.pivot(index="first", columns="last", values="adjusted").reindex(index=TYPES, columns=TYPES) * 100
        n = g.pivot(index="first", columns="last", values="papers").reindex(index=TYPES, columns=TYPES)
        im = ax.imshow(np.ma.masked_invalid(piv.to_numpy()), cmap=cmap, vmin=lo, vmax=hi)
        for i in range(3):
            for jj in range(3):
                v, nn = piv.iat[i, jj], n.iat[i, jj]
                dark = np.isfinite(v) and (v - lo) / max(hi - lo, 1e-9) > 0.55
                ax.text(jj, i, "–" if not np.isfinite(v) else f"{v:.1f}%\nn={int(nn)}", ha="center", va="center",
                        fontsize=6.8, color=figures.SURFACE if dark else figures.INK)
        ax.set_xticks(range(3), TYPES)
        ax.set_yticks(range(3), TYPES)
        ax.set_xlabel("last author")
        ax.set_ylabel("first author")
        ax.set_title(title, loc="left")
        ax.grid(False)
        for sp in ax.spines.values():
            sp.set_visible(False)
    fig.colorbar(im, ax=axes, shrink=0.8, label="adjusted acceptance, %")
    fig.suptitle("Acceptance by first and last author type (teams of 2+; post hoc, exploratory)", x=0.01, ha="left",
                 fontsize=8.5)
    _save(fig, out_dir, "teams_role_grid")

    fam = pd.read_csv(out_dir / "family.csv")
    fig, ax = plt.subplots(figsize=(6.6, 2.6), constrained_layout=True)
    y = np.arange(len(fam))[::-1]
    ax.axvline(0, color=figures.INK2, lw=0.7)
    ax.hlines(y, fam.ci95_lo * 100, fam.ci95_hi * 100, color=figures.SERIES[0], lw=1.6)
    ax.scatter(fam.estimate * 100, y, s=24, color=figures.SERIES[0], edgecolor=figures.SURFACE, linewidth=1, zorder=3)
    for sign in (-1, 1):
        ax.scatter(sign * fam.mde80 * 100, y, marker="|", s=60, color=figures.MUTED)
    ax.set_yticks(y, [f"{t} {lab}  (Holm p={p:.2f})" for t, lab, p in zip(fam.test, fam.label, fam.p_holm)], fontsize=6.8)
    ax.set_xlabel("percentage points (95% CI); grey ticks: +/- MDE80 from within topic-year permutations")
    ax.set_title("Declared family H1-H6 (LPM, topic-year FE, CR1 by topic; post hoc, exploratory)", loc="left")
    _save(fig, out_dir, "teams_family")
