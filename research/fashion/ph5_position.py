"""PH5 position (final post hoc round, selection S4): where to stand inside a topic. Within k100 topic x year, how does
acceptance depend on a paper's novelty relative to earlier ICLR work and on independent same-year near-duplicates
(twins); does the novelty curve differ for topic newcomers and in mature topics; how does it look within the same
author; and do near-duplicates share fate? Post hoc and exploratory: every estimate is an association; Holm within
each declared family ranks the evidence, nothing more.

Features (outcome-free, all 43,480 discovery submissions; SPECTER2 centred by output/specter2_centring_mean.npy and
L2-normalised):
  nov          1 - mean of the K = 10 largest cosines with all papers of earlier years, the paper's own chain of
               probable earlier versions (output/earlier_versions.csv.gz) excluded. Variants: K = 5 / 20; the prior 3
               years only; fixed reference (5,000 random earlier papers, mean over 5 draws; all earlier papers when
               there are fewer, i.e. 2018-2021)
  pct          percentile rank (rank - 0.5) / n of nov within the k100 topic x year cell (all submissions); quintiles
               Q1 (least novel) to Q5 cut at 0.2, 0.4, ...; terciles low / mid / high cut at 1/3 and 2/3
  twins        same-year pairs with cos >= 0.70 (0.65 / 0.75 sensitivities). Independent: no shared declared_id_key,
               no shared normalised author name (declared name lower-cased, whitespace collapsed), and neither is in
               the other's earlier-version chain; sibling: shares an author. any_twin = >= 1 independent twin;
               sibling_twin = >= 1 sibling twin; dose = log1p(independent twins per 1,000 same-year submissions)
  precedents   earlier papers with cos >= 0.70 (chain excluded); prior_density = log1p(1,000 x precedents / earlier
               papers)
  first_time   no author ID with an earlier discovery submission (outcome-free part only)
Population: RQ3 decided papers 2019-2026 (Q5: its 2023-2026 papers). LPM with k100 topic x year FE absorbed, CR1 SE by
topic, t(G - 1). Controls X = class (ref. method) + fm + log2 team + newcomer + sibling_twin.
  Q0  accepted ~ q1 + q2 + q4 + q5 (ref. Q3) + any_twin + X
  Q1  Q0 + ter_low + ter_high + any_twin x mid + any_twin x high (interaction ref. low: P3 is one coefficient)
  Q2  Q0 + any_twin x hot
  Q3  Q0 + q_j x newcomer
  Q4  Q0 + q_j x middle + q_j x mature (posthoc.add_columns maturity tercile of the population; ref. young)
  Q5  one row per (paper, author ID), weight 1 / the paper's author IDs: accepted ~ nov10 (= pct x 10) + any_twin + X
      | author + topic x year FE (as posthoc.wls_fe); CR1 by topic and two-way topic x author SE, both counting the
      absorbed author FE in the small-sample factor (authors are not nested in topics)
Family 1 (Holm over 8): P1a q5 and P1b q1 (Q0); P2 any_twin (Q0); P3 any_twin x high (Q1); P4 any_twin x hot (Q2); P5
  q5 x newcomer (Q3); P6 q5 x mature (Q4); P7 nov10 (Q5). P3-P7 also get a p-value calibrated on NULLS (200) simulated
  nulls on the same papers (accepted ~ Bernoulli(the paper's topic x year acceptance rate)): p_cal = (1 + #{|t_null| >=
  |t|}) / (NULLS + 1). Each test enters Holm with p_used = the largest of its CR1 p, p_cal (P3-P7) and, for P7, the
  two-way p (an author's residuals can span topics, which topic clusters miss).
Secondary (no Holm): Lind-Mehlum inverted-U test (quadratic in pct; slopes at the observed minimum and maximum; p = the
  larger one-sided t(G - 1) p-value); adjusted P(accept | tercile, any_twin, hot) (difference from (mid, no twin) of
  the same hot stratum, as hot is constant within topic x year, plus that group's raw rate; BH over the 10); the surface
  quintile x any_twin vs (Q3, no twin) (BH over the 9); risk view: Q0 on the S9 population with s9_accepted and with
  withdrawn_after_review (BH over the 10; 'polarising' = raises both with q < 0.05); novelty curves by newcomer /
  incumbent (Q3) and maturity tercile (Q4).
Family 3, dyadic (Holm over the 3 bins): independent same-year pairs of decided papers 2018-2026 with cos in [0.60,
  0.70), [0.70, 0.80) and >= 0.80. r = accepted - the leave-one-out mean of the topic x year cell (single-paper cells
  dropped); rho_b = mean r_i r_j / var(r); rho_0 the same on 100,000 random same-cell pairs with cos < 0.30 and no shared
  author (fixed seed); statistic rho_b - rho_0 with a two-sided p from 1,000 within-cell permutations of accepted (r
  recomputed each time; deviations from the permutation mean, since the LOO residual makes same-cell pairs negatively
  correlated by construction; stat_excess = stat minus that mean). Also P(both accepted) and P(exactly one) minus their
  expectation under independence given the cell rates, with permutation bands. Variant (total shared fate, topic level
  included): year means, rho_0 on random same-year pairs, within-year permutations.
Robustness (Family 1 re-estimated, Holm within variant on CR1 p; P7: the larger of CR1 and two-way p): tau 0.65 /
  0.75; K = 5 / 20; prior 3 years; fixed reference; class x year percentile; prior_density control; early map (early
  topic x year FE and clusters, early hot, maturity tercile and newcomer, percentile within the early cell); without
  papers with an earlier version; logit with topic x year dummies (P1a-P6, log-odds, flat cells dropped); twin dose in
  place of any_twin (P2 only).
Outcome-free (compute_free; also inside compute): any_twin share by year x hot / FM / class / newcomer; herding LPM
  any_twin ~ first_time + newcomer + class + fm + log2 team | topic x year (submissions 2019-2026 with an author ID, CR1
  by topic; first_time is nested in newcomer); descriptive checks; titles of 20 random independent pairs per bin
  (compute_free only, the reading check).
calibrate(): sizes and planted-effect recovery on simulated frames (see its docstring).
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import sparse, stats
from scipy.sparse.csgraph import connected_components
from scipy.special import expit, logit

import panel
import ph5_common
import posthoc
from common import DATA, OUTPUT, ROOT, topic_layer
from logit import fe_logit
from ols import demean
from panel import CLASS_CONTROLS
from variables import load_authors
from variants import holm

K_MAIN, K_ALT = 10, (5, 20)
TAU, TAU_ALT, PAIR_MIN = 0.70, (0.65, 0.75), 0.60
FIXED_REF, FIXED_DRAWS, PRIOR_WINDOW = 5000, 5, 3
YEARS, AUTHOR_YEARS, DYAD_YEARS = (2019, 2026), (2023, 2026), (2018, 2026)
BINS = [(0.60, 0.70), (0.70, 0.80), (0.80, np.inf)]
BIN_NAMES = ["0.60-0.70", "0.70-0.80", ">=0.80"]
BASE_PAIRS, BASE_COS = 100_000, 0.30
PERMS, NULLS, SEED = 1000, 200, 20261017
Q_TERMS = ["q1", "q2", "q4", "q5"]                          # novelty quintile dummies, reference Q3
TERCILES = ["low", "mid", "high"]
MATURITY = ["young", "middle", "mature"]
CONTROLS = CLASS_CONTROLS + ["fm", "log2_team", "newcomer", "sibling_twin"]
NOTE = "post hoc exploratory (PH5 position, selection S4); associations within topic x year, not causal effects"


@lru_cache(maxsize=1)
def embeddings() -> np.ndarray:
    """Centred, L2-normalised SPECTER2 vectors in panel.frame('k100') row order (float32)."""
    ids = pd.read_csv(ROOT / "research" / "topics" / "cache" / "specter2_ids.csv").submission_id
    assert (ids.to_numpy() == panel.frame("k100").submission_id.to_numpy()).all()
    X = np.load(ROOT / "research" / "topics" / "cache" / "specter2.npy").astype(np.float32)
    X -= np.load(OUTPUT / "specter2_centring_mean.npy").astype(np.float32)
    return X / np.linalg.norm(X, axis=1, keepdims=True)


def earlier_chains(ids: pd.Series) -> list[np.ndarray]:
    """Per paper: row positions of its chain of probable earlier versions (earlier version, its earlier version, ...)."""
    ev = pd.read_csv(OUTPUT / "earlier_versions.csv.gz", usecols=["submission_id", "probable_earlier_version"])
    assert ev.submission_id.equals(ids.reset_index(drop=True))
    pos = {s: i for i, s in enumerate(ids)}
    link = dict(zip(ev.submission_id, ev.probable_earlier_version))
    chains = []
    for s in ids:
        out, e = [], link.get(s)
        while isinstance(e, str) and e in pos and pos[e] not in out:
            out.append(pos[e])
            e = link.get(e)
        chains.append(np.array(out, int))
    return chains


def topk_mean(S: np.ndarray, k: int) -> np.ndarray:
    return np.partition(S, -k, axis=1)[:, -k:].mean(axis=1)


def novelty(X: np.ndarray, years: np.ndarray, chains: list[np.ndarray], chunk: int = 2000) -> pd.DataFrame:
    """Per paper, against every paper of earlier years (its own earlier-version chain excluded): nov_k = 1 - mean of the
    k largest cosines (k = 5, 10, 20); the same against the prior 3 years only, and against FIXED_REF random earlier
    papers (mean over FIXED_DRAWS draws; all earlier papers when there are fewer); precedents = earlier papers with
    cos >= TAU and prior_papers = the size of the earlier corpus. NaN for the first year."""
    n = len(years)
    out = {c: np.full(n, np.nan) for c in ["nov", "nov_k5", "nov_k20", "nov_prior3", "nov_fixed", "precedents",
                                           "prior_papers"]}
    rng = np.random.default_rng(SEED)
    for y in np.unique(years):
        R, Q = np.flatnonzero(years < y), np.flatnonzero(years == y)
        if len(R) < max(K_ALT):
            continue
        recent = years[R] >= y - PRIOR_WINDOW
        draws = ([rng.choice(len(R), FIXED_REF, replace=False) for _ in range(FIXED_DRAWS)] if len(R) > FIXED_REF
                 else [np.arange(len(R))])
        XR = X[R].T
        for s in range(0, len(Q), chunk):
            q = Q[s:s + chunk]
            S = X[q] @ XR
            for a, i in enumerate(q):
                c = chains[i][years[chains[i]] < y]
                S[a, np.searchsorted(R, c)] = -2.0
            top = -np.sort(-np.partition(S, -max(K_ALT), axis=1)[:, -max(K_ALT):], axis=1)
            out["nov"][q] = 1 - top[:, :K_MAIN].mean(1)
            for k in K_ALT:
                out[f"nov_k{k}"][q] = 1 - top[:, :k].mean(1)
            out["nov_prior3"][q] = 1 - topk_mean(S[:, recent], K_MAIN)
            out["nov_fixed"][q] = 1 - np.mean([topk_mean(S[:, d], K_MAIN) for d in draws], axis=0)
            out["precedents"][q] = (S >= TAU).sum(1)
        out["prior_papers"][Q] = len(R)
    return pd.DataFrame(out)


def same_year_pairs(X: np.ndarray, years: np.ndarray, chunk: int = 2000) -> pd.DataFrame:
    """Every same-year pair (i < j, row positions) with cosine >= PAIR_MIN."""
    parts = []
    for y in np.unique(years):
        Q = np.flatnonzero(years == y)
        XQ = X[Q].T
        for s in range(0, len(Q), chunk):
            S = X[Q[s:s + chunk]] @ XQ
            a, b = np.nonzero(S >= PAIR_MIN)
            keep = b > a + s
            a, b = a[keep], b[keep]
            parts.append(pd.DataFrame({"i": Q[a + s], "j": Q[b], "cos": S[a, b]}))
    return pd.concat(parts, ignore_index=True)


def normalise_name(v: str) -> str | None:
    try:
        s = json.loads(v)
    except (TypeError, ValueError):
        return None
    s = " ".join(s.lower().split()) if isinstance(s, str) else ""
    return s or None


def author_matrix(ids: pd.Series) -> sparse.csr_matrix:
    """Papers x author tokens (declared_id_key, and the normalised declared name: lower case, whitespace collapsed)."""
    a = pd.read_csv(DATA / "submission_authors.csv.gz", keep_default_na=False, na_values=[r"\N"],
                    usecols=["submission_id", "declared_name_json", "declared_id_key"])
    pos = pd.Series(np.arange(len(ids)), index=ids.to_numpy())
    a = a[a.submission_id.isin(pos.index)]
    tok = pd.concat([pd.DataFrame({"row": pos[a.submission_id].to_numpy(), "tok": "k:" + a.declared_id_key}),
                     pd.DataFrame({"row": pos[a.submission_id].to_numpy(),
                                   "tok": "n:" + a.declared_name_json.map(normalise_name)})]).dropna().drop_duplicates()
    codes, _ = pd.factorize(tok.tok)
    return sparse.csr_matrix((np.ones(len(tok)), (tok.row.to_numpy(), codes)), shape=(len(ids), codes.max() + 1))


@lru_cache(maxsize=1)
def authors() -> sparse.csr_matrix:
    return author_matrix(panel.frame("k100").submission_id)


def classify_pairs(p: pd.DataFrame, A: sparse.csr_matrix, chains: list[np.ndarray]) -> pd.DataFrame:
    """sibling: the two papers share an author ID or normalised name; earlier: one is in the other's earlier-version
    chain; independent: neither."""
    shared = np.asarray(A[p.i.to_numpy()].multiply(A[p.j.to_numpy()]).sum(axis=1)).ravel() > 0
    n = A.shape[0]
    links = {i * n + int(e) for i, c in enumerate(chains) for e in c}
    links |= {int(e) * n + i for i, c in enumerate(chains) for e in c}
    earlier = np.isin(p.i.to_numpy() * n + p.j.to_numpy(), list(links)) if links else np.zeros(len(p), bool)
    return p.assign(sibling=shared, earlier=earlier, independent=~shared & ~earlier)


def cell_pct(x: pd.Series, groups: list[pd.Series]) -> np.ndarray:
    """Percentile rank (average rank - 0.5) / n within groups, in (0, 1); NaN where x is NaN."""
    g = x.groupby([s.to_numpy() for s in groups])
    return ((g.rank(method="average") - 0.5) / g.transform("count")).to_numpy()


def tag(t: float) -> str:
    return f"{round(t * 100):03d}"


@lru_cache(maxsize=1)
def build() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Outcome-free paper features (panel.frame('k100') row order) and same-year pairs (cached; do not mutate)."""
    k = panel.frame("k100").reset_index(drop=True)
    years = k.year.to_numpy()
    X = embeddings()
    chains = earlier_chains(k.submission_id)
    f = novelty(X, years, chains)
    f.insert(0, "submission_id", k.submission_id.to_numpy())
    f["prior_density"] = np.log1p(1000 * f.precedents / f.prior_papers)
    p = classify_pairs(same_year_pairs(X, years), authors(), chains)
    n = len(k)
    for t in (TAU, *TAU_ALT):
        ind, sib = p[(p.cos >= t) & p.independent], p[(p.cos >= t) & p.sibling]
        f[f"twins_{tag(t)}"] = np.bincount(ind.i, minlength=n) + np.bincount(ind.j, minlength=n)
        f[f"sibling_{tag(t)}"] = ((np.bincount(sib.i, minlength=n) + np.bincount(sib.j, minlength=n)) > 0).astype(float)
    f["dose"] = np.log1p(1000 * f[f"twins_{tag(TAU)}"] / k.groupby("year").year.transform("size").to_numpy())
    for c in ["nov", "nov_k5", "nov_k20", "nov_prior3", "nov_fixed"]:
        f["pct" + c[3:]] = cell_pct(f[c], [k.topic, k.year])
    f["pct_class"] = cell_pct(f.nov, [k.primary_class, k.year])
    f["pct_early"] = cell_pct(f.nov, [k.topic_early, k.year])
    a = load_authors(k.submission_id)[["submission_id", "key"]].merge(k[["submission_id", "year"]], on="submission_id")
    a["seen"] = a.key.map(a.groupby("key").year.min()) < a.year
    seen = a.groupby("submission_id").seen.any().reindex(k.submission_id).fillna(False).to_numpy(float)
    f["first_time"] = np.where(k.has_author_key, 1.0 - seen, np.nan)
    return f, p


@lru_cache(maxsize=1)
def author_keys() -> pd.DataFrame:
    return load_authors(panel.frame("k100").submission_id)[["submission_id", "key"]]


@lru_cache(maxsize=1)
def early_columns() -> pd.DataFrame:
    """The early map's (2017-2020 fit) cell, hot, maturity and newcomer, in panel.frame('k100') row order."""
    e = panel.frame("early").reset_index(drop=True)
    assert (e.submission_id.to_numpy() == panel.frame("k100").submission_id.to_numpy()).all()
    return pd.DataFrame({"cell_early": e.cell, "hot_early": e.hot, "maturity_early": e.maturity,
                         "newcomer_early": e.newcomer})


# ---------------------------------------------------------------------------------------------------- analysis frame
def prepare(k: pd.DataFrame) -> pd.DataFrame:
    """k (panel.frame('k100') rows, with or without outcomes) with the features and the early-map columns."""
    k = k.reset_index(drop=True)
    f, _ = build()
    assert (f.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    e = early_columns()
    return k.assign(**{c: f[c].to_numpy() for c in f.columns[1:]}, **{c: e[c].to_numpy() for c in e.columns})


def population(k: pd.DataFrame, years: tuple[int, int] = YEARS, flag: str = "rq3") -> pd.DataFrame:
    return posthoc.add_columns(k[k[flag].astype(bool) & k.year.between(*years)].copy())


def design(d: pd.DataFrame, pct: str = "pct", tau: float = TAU) -> pd.DataFrame:
    """Model variables: novelty percentile, quintile (ref. Q3) and tercile dummies, twin indicators, interactions."""
    x = d[pct].to_numpy(float)
    nan = np.isnan(x)
    quint = np.where(nan, np.nan, np.clip(np.floor(x * 5), 0, 4) + 1)
    ter = np.where(nan, np.nan, np.clip(np.floor(x * 3), 0, 2))
    cols = {"nov_pct": x, "nov_pct2": x ** 2, "nov10": 10 * x, "quintile": quint,
            "tercile": pd.Series(ter, index=d.index).map(dict(enumerate(TERCILES))),
            "any_twin": (d[f"twins_{tag(tau)}"] >= 1).astype(float), "sibling_twin": d[f"sibling_{tag(tau)}"]}
    for j in range(1, 6):
        cols[f"q{j}"] = np.where(nan, np.nan, quint == j)
    for j, t in enumerate(TERCILES):
        cols[f"ter_{t}"] = np.where(nan, np.nan, ter == j)
    d = d.assign(**cols)
    extra = {"twin_mid": d.any_twin * d.ter_mid, "twin_high": d.any_twin * d.ter_high, "twin_hot": d.any_twin * d.hot}
    for q in Q_TERMS:
        extra[f"{q}_new"] = d[q] * d.newcomer
        for m in MATURITY[1:]:
            extra[f"{q}_{m}"] = d[q] * (d.maturity_tercile == m)
    return d.assign(**extra)


# ---------------------------------------------------------------------------------------------------- estimators
class Fit:
    """LPM with one absorbed fixed effect (same estimator and CR1 factor as ols.fe_ols), t(G - 1) inference."""

    def __init__(self, d: pd.DataFrame, y: str, xs: list[str], absorb: str = "cell", cluster: str = "topic"):
        d, self.xs, Xd, yd = partial(d, y, xs, absorb)
        inv = np.linalg.pinv(Xd.T @ Xd)
        beta = inv @ Xd.T @ yd
        e = yd - Xd @ beta
        n, k = Xd.shape
        cg = pd.factorize(d[cluster])[0]
        G = cg.max() + 1
        S = sparse.csr_matrix((np.ones(n), (cg, np.arange(n))), shape=(G, n)) @ (Xd * e[:, None])
        V = (G / (G - 1)) * ((n - 1) / (n - k)) * inv @ (S.T @ S) @ inv
        self.beta, self.V, self.G, self.n = pd.Series(beta, self.xs), pd.DataFrame(V, self.xs, self.xs), int(G), n

    def lincom(self, w: dict[str, float]) -> dict:
        """Estimate, CR1 SE, t(G - 1) p and 95% CI of sum w_j b_j; NaN if a term was not identified."""
        if not set(w) <= set(self.xs):
            return {"coef": np.nan, "se": np.nan, "p": np.nan, "ci95_lo": np.nan, "ci95_hi": np.nan, "n": self.n,
                    "clusters": self.G, "note": "not identified: " + ";".join(sorted(set(w) - set(self.xs)))}
        c = pd.Series(w).reindex(self.xs).fillna(0.0).to_numpy()
        est, se = float(c @ self.beta.to_numpy()), float(np.sqrt(c @ self.V.to_numpy() @ c))
        q = stats.t.ppf(0.975, self.G - 1)
        return {"coef": est, "se": se, "p": float(2 * stats.t.sf(abs(est / se), self.G - 1)), "ci95_lo": est - q * se,
                "ci95_hi": est + q * se, "n": self.n, "clusters": self.G}


def partial(d: pd.DataFrame, y: str, xs: list[str], absorb: str):
    """Complete cases, regressors with within-group variation, and the demeaned X and y."""
    d = d.dropna(subset=[y, *xs])
    g = pd.factorize(d[absorb])[0]
    Xd, yd = demean(d[xs].to_numpy(float), g), demean(d[y].to_numpy(float), g)
    keep = Xd.std(axis=0) > 1e-12
    return d, [x for x, k_ in zip(xs, keep) if k_], Xd[:, keep], yd


def null_t(d: pd.DataFrame, xs: list[str], term: str, Y: np.ndarray, absorb: str = "cell",
           cluster: str = "topic") -> np.ndarray:
    """t statistic of `term` (CR1, as Fit) for every column of simulated outcomes Y (rows aligned with d)."""
    keep = d[xs].notna().all(axis=1).to_numpy()
    dd, names, Xd, _ = partial(d[keep].assign(_y=0.0), "_y", xs, absorb)
    g = pd.factorize(dd[absorb])[0]
    Yd = demean(Y[keep], g)
    inv = np.linalg.pinv(Xd.T @ Xd)
    B = inv @ (Xd.T @ Yd)
    E = Yd - Xd @ B
    j = names.index(term)
    u = Xd @ inv[:, j]
    n, k = Xd.shape
    cg = pd.factorize(dd[cluster])[0]
    G = cg.max() + 1
    S = sparse.csr_matrix((np.ones(n), (cg, np.arange(n))), shape=(G, n)) @ (u[:, None] * E)
    return B[j] / np.sqrt((G / (G - 1)) * ((n - 1) / (n - k)) * (S ** 2).sum(axis=0))


MODELS = {"Q0": [], "Q1": ["ter_low", "ter_high", "twin_mid", "twin_high"], "Q2": ["twin_hot"],
          "Q3": [f"{q}_new" for q in Q_TERMS], "Q4": [f"{q}_{m}" for m in MATURITY[1:] for q in Q_TERMS]}
TESTS = [("P1a", "Q0", "q5", "novelty Q5 minus Q3"),
         ("P1b", "Q0", "q1", "novelty Q1 minus Q3"),
         ("P2", "Q0", "any_twin", "any independent same-year twin"),
         ("P3", "Q1", "twin_high", "twin association, high minus low novelty tercile"),
         ("P4", "Q2", "twin_hot", "twin association, hot minus other topics"),
         ("P5", "Q3", "q5_new", "(Q5 - Q3), newcomer minus incumbent papers"),
         ("P6", "Q4", "q5_mature", "(Q5 - Q3), mature minus young topics"),
         ("P7", "Q5", "nov10", "within-author slope per 10 novelty percentile points (2023-2026)")]
CALIBRATED = ("P3", "P4", "P5", "P6", "P7")


def xs(model: str, extra: tuple[str, ...] = (), twin: str = "any_twin") -> list[str]:
    return Q_TERMS + [twin] + MODELS[model] + list(extra) + CONTROLS


def author_fe(d: pd.DataFrame, y: str = "accepted", absorb: str = "cell", cluster: str = "topic",
              extra: tuple[str, ...] = (), null: np.ndarray | None = None) -> tuple[dict, np.ndarray]:
    """Q5: one row per (paper, author ID) of d's 2023-2026 papers, weights 1 / the paper's author IDs, author + topic x
    year FE absorbed jointly (posthoc.twfe, singletons dropped as posthoc.wls_fe; same WLS estimate). CR1 SE by topic and
    two-way topic x author SE for the novelty slope, both with the absorbed author FE counted in the small-sample factor
    (n - 1) / (n - k - (authors - 1)) since authors are not nested in topics (as reghdfe). With posthoc.wls_fe's factor
    the CR1 t had SD 1.14 over 200 simulated null outcomes of one frame; with this one 0.98 there, and 1.03 (5.8%
    rejection at 0.05; two-way 5.0%) over 120 simulated null frames. null: paper-level outcome draws (rows of d x draws)
    whose slope t statistics (CR1) are returned alongside."""
    sub = d.assign(_row=np.arange(len(d)))[d.year.between(*AUTHOR_YEARS).to_numpy()]
    a = author_keys().merge(sub, on="submission_id")
    a["w"] = 1.0 / a.groupby("submission_id").key.transform("size")
    names = ["nov10", "any_twin", *extra, *CONTROLS]
    a = posthoc.drop_singletons(a.dropna(subset=[y, *names]), [absorb, "key"]).reset_index(drop=True)
    w = a.w.to_numpy(float)
    Y = a[[y]].to_numpy(float) if null is None else np.column_stack([a[y].to_numpy(float), null[a._row.to_numpy()]])
    first, rest = posthoc.twfe(Y[:, 0], np.column_stack([Y[:, 1:], a[names].to_numpy(float)]),
                               [a[absorb].to_numpy(), a.key.to_numpy()], w)
    Yd, Xd = np.column_stack([first, rest[:, :Y.shape[1] - 1]]), rest[:, Y.shape[1] - 1:]
    Xd = Xd[:, Xd.std(axis=0) > 1e-12]
    inv = np.linalg.pinv(Xd.T @ (Xd * w[:, None]))
    B = inv @ (Xd * w[:, None]).T @ Yd
    u = (Xd * w[:, None]) @ inv[:, 0]
    E = u[:, None] * (Yd - Xd @ B)
    n, k = Xd.shape
    scale = (n - 1) / (n - k - (a.key.nunique() - 1))

    def var(groups: np.ndarray) -> tuple[np.ndarray, int]:
        cg = pd.factorize(groups)[0]
        G = cg.max() + 1
        S = sparse.csr_matrix((np.ones(n), (cg, np.arange(n))), shape=(G, n)) @ E
        return G / (G - 1) * scale * (S ** 2).sum(axis=0), int(G)

    V, G = var(a[cluster].to_numpy())
    Va, _ = var(a.key.to_numpy())
    V2 = V + Va - var(a[cluster].astype(str).to_numpy() + "|" + a.key.astype(str).to_numpy())[0]
    V2 = np.where(V2 > 0, V2, np.maximum(V, Va))
    b, se, se2 = B[0, 0], float(np.sqrt(V[0])), float(np.sqrt(V2[0]))
    q = stats.t.ppf(0.975, G - 1)
    return ({"coef": b, "se": se, "p": float(2 * stats.t.sf(abs(b / se), G - 1)), "ci95_lo": b - q * se,
             "ci95_hi": b + q * se, "n": n, "clusters": G, "papers": int(a.submission_id.nunique()),
             "authors": int(a.key.nunique()), "se_twoway": se2, "p_twoway": float(2 * stats.t.sf(abs(b / se2), G - 1))},
            B[0, 1:] / np.sqrt(V[1:]))


def declared(d: pd.DataFrame, y: str = "accepted", absorb: str = "cell", cluster: str = "topic",
             extra: tuple[str, ...] = ()) -> tuple[pd.DataFrame, dict[str, Fit]]:
    """Family 1 (P1a-P7) on a designed population; Holm over the rows (p_used: see family())."""
    fits = {m: Fit(d, y, xs(m, extra), absorb, cluster) for m in MODELS}
    rows = [{"test": t, "model": m, "term": term, "label": lab, **fits[m].lincom({term: 1})}
            for t, m, term, lab in TESTS if m in fits]
    t, m, term, lab = TESTS[-1]
    rows.append({"test": t, "model": m, "term": term, "label": lab, **author_fe(d, y, absorb, cluster, extra)[0]})
    return family(pd.DataFrame(rows)), fits


def family(rows: pd.DataFrame) -> pd.DataFrame:
    """Holm over the family on p_used = the largest available of the CR1 p, the two-way p (P7) and the calibrated p
    (P3-P7, when present); NaN p (a term not identified) enters as 1."""
    extra = [c for c in ("p_twoway", "p_calibrated") if c in rows]
    rows["p_used"] = rows[["p", *extra]].max(axis=1, skipna=True).where(rows.p.notna())
    rows["p_holm"] = holm(rows.p_used.fillna(1.0)).to_numpy()
    return rows


def calibrated_p(d: pd.DataFrame, tests: pd.DataFrame, rng: np.random.Generator, draws: int = NULLS) -> pd.DataFrame:
    """P3-P7: p = (1 + #{|t_null| >= |t|}) / (draws + 1), t_null from `draws` simulated nulls on the same papers:
    accepted ~ Bernoulli(the paper's topic x year acceptance rate), so nothing but the cell predicts acceptance."""
    rate = d.groupby("cell").accepted.transform("mean").to_numpy(float)
    Y = (rng.random((len(d), draws)) < rate[:, None]).astype(float)
    tests = tests.copy()
    for t, m, term, _ in TESTS:
        if t in CALIBRATED:
            i = tests.index[tests.test == t][0]
            tn = author_fe(d, null=Y)[1] if m == "Q5" else null_t(d, xs(m), term, Y)
            obs = abs(tests.at[i, "coef"] / tests.at[i, "se"])
            tests.at[i, "p_calibrated"] = float((1 + (np.abs(tn) >= obs).sum()) / (draws + 1))
            tests.at[i, "null_t_sd"] = float(np.std(tn))
    return family(tests)


# ---------------------------------------------------------------------------------------------------- secondary
def lind_mehlum(d: pd.DataFrame, y: str = "accepted") -> dict:
    """accepted ~ nov_pct + nov_pct^2 + any_twin + controls | topic x year. Inverted U: slope > 0 at the lowest and < 0
    at the highest observed percentile; p = max of the two one-sided t(G - 1) p-values (Lind & Mehlum 2010)."""
    terms = ["nov_pct", "nov_pct2", "any_twin"] + CONTROLS
    f = Fit(d, y, terms)
    x = d.dropna(subset=[y, *terms]).nov_pct
    lo, hi = float(x.min()), float(x.max())
    sl, sh = f.lincom({"nov_pct": 1, "nov_pct2": 2 * lo}), f.lincom({"nov_pct": 1, "nov_pct2": 2 * hi})
    p = max(stats.t.sf(sl["coef"] / sl["se"], f.G - 1), stats.t.cdf(sh["coef"] / sh["se"], f.G - 1))
    b1, b2 = f.beta["nov_pct"], f.beta["nov_pct2"]
    g = np.array([-1 / (2 * b2), b1 / (2 * b2 ** 2)])
    V = f.V.loc[["nov_pct", "nov_pct2"], ["nov_pct", "nov_pct2"]].to_numpy()
    return {"b_linear": float(b1), "b_quadratic": float(b2), "quadratic_p": f.lincom({"nov_pct2": 1})["p"],
            "slope_at_min": sl["coef"], "slope_at_min_se": sl["se"], "slope_at_max": sh["coef"], "slope_at_max_se": sh["se"],
            "range": [lo, hi], "turning_point": float(-b1 / (2 * b2)), "turning_point_se": float(np.sqrt(g @ V @ g)),
            "p_inverted_u": float(p), "n": f.n, "clusters": f.G}


def cell_table(d: pd.DataFrame, groups: dict[str, pd.Series], refs: list[str], y: str = "accepted") -> pd.DataFrame:
    """accepted ~ group dummies (the refs omitted) + controls | topic x year: one row per group with its raw rate and
    adjusted difference from its reference; BH q over the non-reference groups."""
    d = d.assign(**{g: m.astype(float) for g, m in groups.items()})
    f = Fit(d, y, [g for g in groups if g not in refs] + CONTROLS)
    rows = []
    for g, m in groups.items():
        r = {"coef": 0.0, "se": 0.0, "p": np.nan, "ci95_lo": 0.0, "ci95_hi": 0.0} if g in refs else f.lincom({g: 1})
        rows.append({"group": g, "papers": int(m.sum()), "raw_rate": float(d.loc[m.astype(bool), y].mean()), **r})
    out = pd.DataFrame(rows)
    out["q_bh"] = ph5_common.bh(out.p)
    return out


def adjusted_table(d: pd.DataFrame) -> pd.DataFrame:
    """P(accept | novelty tercile, any_twin, hot): adjusted difference from (mid tercile, no twin) of the same hot
    stratum (hot is constant within topic x year, so levels across strata are not compared), plus that reference's
    raw rate as the adjusted level."""
    groups = {f"{t}|{w}|{h}": (d.tercile == t) & (d.any_twin == w) & (d.hot == h)
              for h in (0, 1) for t in TERCILES for w in (0, 1)}
    out = cell_table(d, groups, [f"mid|0|{h}" for h in (0, 1)])
    out[["tercile", "any_twin", "hot"]] = out.group.str.split("|", expand=True)
    ref = out[(out.tercile == "mid") & (out.any_twin == "0")].set_index("hot").raw_rate
    out["adjusted_rate"] = out.hot.map(ref) + out.coef
    return out


def surface(d: pd.DataFrame) -> pd.DataFrame:
    """Adjusted pp by novelty quintile x any_twin, reference Q3 without a twin (the heatmap)."""
    groups = {f"Q{j}|{w}": (d.quintile == j) & (d.any_twin == w) for w in (0, 1) for j in range(1, 6)}
    out = cell_table(d, groups, ["Q3|0"])
    out[["quintile", "any_twin"]] = out.group.str.split("|", expand=True)
    return out


def curves(fits: dict[str, Fit]) -> pd.DataFrame:
    """Novelty curves (Qj minus Q3 of the same group) for incumbent / newcomer papers (Q3) and topic maturity (Q4)."""
    rows = []
    for model, groups in [("Q3", {"incumbent": "", "newcomer": "_new"}), ("Q4", {m: f"_{m}" for m in MATURITY})]:
        for group, suffix in groups.items():
            for j in range(1, 6):
                w = {} if j == 3 else {f"q{j}": 1.0, **({f"q{j}{suffix}": 1.0} if suffix and group != "young" else {})}
                r = fits[model].lincom(w) if w else {"coef": 0.0, "se": 0.0, "ci95_lo": 0.0, "ci95_hi": 0.0, "p": np.nan}
                rows.append({"model": model, "group": group, "quintile": j, **r})
    return pd.DataFrame(rows)


def risk(k: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Q0 on the S9 population with s9_accepted and withdrawn_after_review; BH over the 10 cells; a novelty quintile or
    any_twin is 'polarising' if it raises both (both coefficients > 0 with BH q < 0.05)."""
    d = design(population(k, flag="s9"))
    rows = []
    for y in ("s9_accepted", "withdrawn_after_review"):
        f = Fit(d, y, xs("Q0"))
        rows += [{"outcome": y, "term": t, **f.lincom({t: 1})} for t in Q_TERMS + ["any_twin"]]
    out = pd.DataFrame(rows)
    out["q_bh"] = ph5_common.bh(out.p)
    w = out.pivot(index="term", columns="outcome", values=["coef", "q_bh"])
    pol = ((w["coef"] > 0) & (w["q_bh"] < 0.05)).all(axis=1)
    return out, {"papers": int(len(d)), "polarising": sorted(pol[pol].index)}


# ---------------------------------------------------------------------------------------------------- dyadic
def loo_resid(a: np.ndarray, codes: np.ndarray) -> np.ndarray:
    """a minus the leave-one-out mean of its group (NaN in single-paper groups); a is papers x draws."""
    n = np.bincount(codes).astype(float)
    M = sparse.csr_matrix((np.ones(len(codes)), (codes, np.arange(len(codes)))), shape=(len(n), len(codes)))
    with np.errstate(divide="ignore", invalid="ignore"):
        r = a - ((M @ a)[codes] - a) / (n[codes] - 1)[:, None]
    r[n[codes] < 2] = np.nan
    return r


def permute_within(a: np.ndarray, codes: np.ndarray, rng: np.random.Generator, draws: int) -> np.ndarray:
    """papers x draws matrix of a permuted within groups."""
    order = np.argsort(codes, kind="stable")
    sc = codes[order]
    out = np.empty((len(a), draws))
    for b in range(draws):
        out[order, b] = a[order[np.lexsort((rng.random(len(a)), sc))]]
    return out


def baseline_pairs(group: np.ndarray, rows: np.ndarray, rng: np.random.Generator, n_pairs: int = BASE_PAIRS,
                   batch: int = 50_000) -> tuple[np.ndarray, np.ndarray]:
    """n_pairs random same-group pairs (positions into rows; uniform over pairs, with replacement) with cos < BASE_COS
    and no shared author."""
    X, A = embeddings(), authors()
    sizes = np.bincount(group)
    w = sizes * (sizes - 1.0)
    order = np.argsort(group, kind="stable")
    start = np.concatenate([[0], np.cumsum(sizes)[:-1]])
    I, J, got = [], [], 0
    while got < n_pairs:
        c = rng.choice(len(sizes), batch, p=w / w.sum())
        u = rng.integers(0, sizes[c])
        v = rng.integers(0, sizes[c] - 1)
        i, j = order[start[c] + u], order[start[c] + v + (v >= u)]
        cos = np.einsum("ij,ij->i", X[rows[i]], X[rows[j]])
        shared = np.asarray(A[rows[i]].multiply(A[rows[j]]).sum(axis=1)).ravel() > 0
        ok = (cos < BASE_COS) & ~shared
        I.append(i[ok])
        J.append(j[ok])
        got += int(ok.sum())
    return np.concatenate(I)[:n_pairs], np.concatenate(J)[:n_pairs]


def dyad_stats(R: np.ndarray, a: np.ndarray, pc: np.ndarray, sets: list[tuple[np.ndarray, np.ndarray]]) -> np.ndarray:
    """Per pair set (last = baseline) and draw (columns of R, a): rho = mean r_i r_j / var(r), P(both accepted) minus
    its expectation and P(exactly one) minus its expectation under independence given the group rates pc."""
    v = np.nanvar(R, axis=0)
    out = []
    for i, j in sets:
        both = (a[i] * a[j]).mean(axis=0) - (pc[i] * pc[j]).mean()
        one = (a[i] + a[j] - 2 * a[i] * a[j]).mean(axis=0) - (pc[i] + pc[j] - 2 * pc[i] * pc[j]).mean()
        out.append(np.stack([(R[i] * R[j]).mean(axis=0) / v, both, one]))
    return np.stack(out)                                         # sets x 3 x draws


def dyadic(k: pd.DataFrame, perms: int = PERMS, seed: int = SEED, variants: tuple[str, ...] = ("cell", "year")
           ) -> pd.DataFrame:
    """Family 3: independent same-year pairs of decided papers (2018-2026) by similarity bin. r = accepted minus the
    leave-one-out mean of the paper's topic x year cell (variant: year); rho_b = mean r_i r_j / var(r); statistic
    rho_b - rho_0 (rho_0: BASE_PAIRS random pairs of the same cell (year variant: the same year) with cos < BASE_COS and
    no shared author); two-sided p, around the permutation mean, from `perms` permutations of accepted within cells
    (years), recomputing r; stat_excess = stat minus its permutation mean (0 under the null; the LOO residual makes
    same-cell pairs mechanically negatively correlated, so stat itself is not); Holm over the three bins (cell variant).
    The year variant measures total shared fate, topic-level included: its baseline is same-year, not same-cell, since
    same-cell pairs would carry the between-cell variance of acceptance that within-year permutations remove."""
    _, p = build()
    sel = (k.rq3.astype(bool) & k.year.between(*DYAD_YEARS)).to_numpy()
    rows = np.flatnonzero(sel)
    pos = np.full(len(k), -1)
    pos[rows] = np.arange(len(rows))
    a = k.accepted.to_numpy(float)[rows]
    pp = p[p.independent.to_numpy() & (pos[p.i] >= 0) & (pos[p.j] >= 0)]
    rng = np.random.default_rng(seed)
    out = []
    for variant in variants:
        codes = pd.factorize((k.cell if variant == "cell" else k.year).to_numpy()[rows])[0]
        bi, bj = baseline_pairs(codes, rows, rng)
        ok = np.bincount(codes)[codes] > 1
        pc = (np.bincount(codes, weights=a) / np.bincount(codes))[codes]
        sets = []
        for lo, hi in BINS:
            m = (pp.cos.to_numpy() >= lo) & (pp.cos.to_numpy() < hi)
            i, j = pos[pp.i.to_numpy()[m]], pos[pp.j.to_numpy()[m]]
            keep = ok[i] & ok[j]
            sets.append((i[keep], j[keep]))
        keep = ok[bi] & ok[bj]
        sets.append((bi[keep], bj[keep]))
        obs = dyad_stats(loo_resid(a[:, None], codes), a[:, None], pc, sets)[..., 0]
        null = np.concatenate([dyad_stats(loo_resid(P, codes), P, pc, sets)
                               for P in (permute_within(a, codes, rng, min(50, perms - s)) for s in range(0, perms, 50))],
                              axis=-1)
        stat, nstat = obs[:-1, 0] - obs[-1, 0], null[:-1, 0] - null[-1, 0]
        for b, name in enumerate(BIN_NAMES):
            row = {"variant": variant, "bin": name, "pairs": len(sets[b][0]), "baseline_pairs": len(sets[-1][0]),
                   "rho": obs[b, 0], "rho_0": obs[-1, 0], "stat": stat[b], "stat_excess": stat[b] - nstat[b].mean(),
                   "perms": perms}
            for key, o, nl in [("stat", stat[b], nstat[b]), ("both_excess", obs[b, 1], null[b, 1]),
                               ("one_excess", obs[b, 2], null[b, 2])]:
                c = nl.mean()
                row.update({f"{key}_null_mean": c, f"{key}_null_lo": np.quantile(nl, 0.025),
                            f"{key}_null_hi": np.quantile(nl, 0.975),
                            f"{key}_p": float((1 + (np.abs(nl - c) >= abs(o - c) - 1e-12).sum()) / (len(nl) + 1))})
            i, j = sets[b]
            row.update({"both_rate": float((a[i] * a[j]).mean()), "both_expected": float((pc[i] * pc[j]).mean()),
                        "both_excess": obs[b, 1], "one_rate": float((a[i] + a[j] - 2 * a[i] * a[j]).mean()),
                        "one_expected": float((pc[i] + pc[j] - 2 * pc[i] * pc[j]).mean()), "one_excess": obs[b, 2],
                        "rho_null_lo": np.quantile(null[b, 0], 0.025), "rho_null_hi": np.quantile(null[b, 0], 0.975)})
            out.append(row)
    res = pd.DataFrame(out)
    cellv = res.variant == "cell"
    res.loc[cellv, "p_holm"] = holm(res.loc[cellv, "stat_p"]).to_numpy()
    return res


# ---------------------------------------------------------------------------------------------------- robustness
def early_frame(d: pd.DataFrame) -> pd.DataFrame:
    """The population on the early map (fitted on 2017-2020 papers): early topic x year cells and clusters, early-map
    hot, maturity tercile and newcomer."""
    return d.assign(topic=d.topic_early, cell=d.cell_early, hot=d.hot_early, newcomer=d.newcomer_early,
                    maturity_tercile=pd.qcut(d.maturity_early, 3, labels=MATURITY).astype(str))


def logit_rows(d: pd.DataFrame) -> list[dict]:
    """P1a-P6 as logits with topic x year dummies (logit.fe_logit; flat cells dropped), CR1 by topic, log-odds."""
    rows, fits = [], {}
    for t, m, term, lab in TESTS[:-1]:
        if m not in fits:
            dd = d.dropna(subset=["accepted", *xs(m)]).reset_index(drop=True)
            X = dd[xs(m)].astype(float)
            try:
                fits[m] = fe_logit(dd.accepted.astype(float), X.loc[:, X.std() > 0], [dd.cell.rename("cell")], dd.topic)
            except (ValueError, RuntimeError, np.linalg.LinAlgError) as e:
                fits[m] = e
        if isinstance(fits[m], Exception):
            rows.append({"variant": "logit", "test": t, "model": m, "term": term, "label": lab, "coef": np.nan,
                         "note": f"logit failed: {fits[m]}"})
            continue
        r, info = fits[m]
        x, q = r.loc[term], stats.t.ppf(0.975, r.loc[term, "clusters"] - 1)
        rows.append({"variant": "logit", "test": t, "model": m, "term": term, "label": lab, "coef": x.coef, "se": x.se,
                     "p": x.p, "ci95_lo": x.coef - q * x.se, "ci95_hi": x.coef + q * x.se, "n": int(x.n),
                     "clusters": int(x.clusters), "ame": x.ame,
                     "note": f"log-odds; {len(info['dropped_groups'])} flat cells dropped"})
    return rows


def robustness(d: pd.DataFrame) -> pd.DataFrame:
    """Family 1 re-estimated under each declared variant (Holm within variant on p_used: CR1 p, P7 the larger of
    CR1 and two-way p; no calibrated p)."""
    base = design(d)
    runs = {f"tau_{tag(t)}": (design(d, tau=t), {}) for t in TAU_ALT}
    runs |= {name: (design(d, pct=pct), {}) for name, pct in
             [("k5", "pct_k5"), ("k20", "pct_k20"), ("prior_3_years", "pct_prior3"), ("fixed_reference", "pct_fixed"),
              ("class_year_percentile", "pct_class")]}
    runs["prior_density_control"] = (base, {"extra": ("prior_density",)})
    runs["early_map"] = (design(early_frame(d), pct="pct_early"), {})
    runs["no_earlier_version"] = (base[base.has_earlier_version == 0], {})
    parts = [declared(v, **kw)[0].assign(variant=name) for name, (v, kw) in runs.items()]
    parts.append(pd.DataFrame(logit_rows(base)))
    f = Fit(base, "accepted", xs("Q0", twin="dose"))
    parts.append(pd.DataFrame([{"variant": "twin_dose", "test": "P2", "model": "Q0", "term": "dose",
                                "label": "log1p(independent twins per 1,000 same-year papers)", **f.lincom({"dose": 1})}]))
    res = pd.concat(parts, ignore_index=True)
    res["p_used"] = res.p_used.fillna(res.p)
    for _, g in res.groupby("variant"):
        res.loc[g.index, "p_holm"] = holm(g.p_used.fillna(1.0)).to_numpy()
    return res


# ---------------------------------------------------------------------------------------------------- outcome-free
def free_part(k: pd.DataFrame) -> dict:
    """Outcome-free, all discovery submissions 2019-2026 (any outcome): twin shares by year and group, the herding LPM
    (any_twin ~ first_time + newcomer + class + FM + log2 team | topic x year, papers with an author ID, CR1 by topic;
    first_time is nested in newcomer, so it compares first-time with returning topic newcomers), descriptive checks."""
    d = design(posthoc.add_columns(k[k.year.between(*YEARS)].copy()))
    d["precedent"] = (d.precedents >= 1).astype(float)
    groups = {"all": pd.Series("all", d.index), "hot": d.hot.map({0.0: "other", 1.0: "hot"}),
              "fm": d.fm.map({0.0: "not FM", 1.0: "FM"}), "class": d.primary_class,
              "newcomer": d.newcomer.map({0.0: "incumbent", 1.0: "newcomer"})}
    share = pd.concat([d.groupby([g.rename("group"), d.year]).agg(
        papers=("any_twin", "size"), any_twin=("any_twin", "mean"), sibling_twin=("sibling_twin", "mean"),
        twins=("twins_070", "mean"), precedent=("precedent", "mean")).reset_index().assign(dimension=name)
        for name, g in groups.items()], ignore_index=True)
    h = d[d.has_author_key]
    f = Fit(h, "any_twin", ["first_time", "newcomer"] + CLASS_CONTROLS + ["fm", "log2_team"])
    herding = pd.DataFrame([{"term": t, **f.lincom({t: 1}), "mean": float(h[t].mean())} for t in f.xs])
    _, p = build()
    py = k.year.to_numpy()[p.i.to_numpy()]
    pairs = p[(py >= DYAD_YEARS[0]) & (py <= DYAD_YEARS[1])]
    summary = {
        "papers": int(len(d)), "any_twin_share": float(d.any_twin.mean()), "sibling_twin_share": float(d.sibling_twin.mean()),
        "any_twin_by_year": d.groupby("year").any_twin.mean().round(4).to_dict(),
        "spearman_novelty_twins_by_year": {int(y): float(stats.spearmanr(g.nov, g.twins_070).statistic)
                                           for y, g in d.groupby("year")},
        "tercile_x_twin_counts": {t: {str(w): int(n) for w, n in g.groupby("any_twin").size().items()}
                                  for t, g in d.groupby("tercile")},
        "precedent_x_twin_shares": {f"precedent={int(a)},twin={int(b)}": float(v) for (a, b), v in
                                    d.groupby(["precedent", "any_twin"]).size().div(len(d)).items()},
        "independent_pairs_2018_2026": {n_: int(((pairs.cos >= lo) & (pairs.cos < hi) & pairs.independent).sum())
                                        for n_, (lo, hi) in zip(BIN_NAMES, BINS)},
        "sibling_pairs_2018_2026": {n_: int(((pairs.cos >= lo) & (pairs.cos < hi) & pairs.sibling).sum())
                                    for n_, (lo, hi) in zip(BIN_NAMES, BINS)},
        "note": "outcome-free (any outcome): embeddings, topics, labels and authors only"}
    return {"free_twin_share": share, "free_herding": herding, "free_summary": summary}


def pair_titles(n: int = 20, seed: int = SEED) -> pd.DataFrame:
    """The reading check: titles of n random independent pairs per similarity bin, 2018-2026."""
    k = panel.frame("k100").reset_index(drop=True)
    corpus = topic_layer().embedded_corpus()
    assert (corpus.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    title = corpus.title.to_numpy()
    _, p = build()
    p = p[p.independent & (k.year.to_numpy()[p.i.to_numpy()] >= DYAD_YEARS[0])]
    rng = np.random.default_rng(seed)
    out = []
    for name, (lo, hi) in zip(BIN_NAMES, BINS):
        s = p[(p.cos >= lo) & (p.cos < hi)]
        s = s.iloc[rng.choice(len(s), min(n, len(s)), replace=False)]
        out.append(pd.DataFrame({"bin": name, "year": k.year.to_numpy()[s.i], "cos": s.cos.round(3).to_numpy(),
                                 "same_cell": k.cell.to_numpy()[s.i] == k.cell.to_numpy()[s.j],
                                 "title_i": title[s.i], "title_j": title[s.j]}))
    return pd.concat(out, ignore_index=True)


def compute_free() -> dict:
    """Outcome-free parts on the real discovery data (no outcome column is loaded), plus the reading-check pairs."""
    return {**free_part(prepare(panel.frame("k100"))), "free_pair_titles": pair_titles()}


# ---------------------------------------------------------------------------------------------------- compute
def compute(k: pd.DataFrame, perms: int = PERMS, nulls: int = NULLS) -> dict:
    k = prepare(k)
    pop = population(k)
    d = design(pop)
    tests, fits = declared(d)
    tests = calibrated_p(d, tests, np.random.default_rng(SEED), nulls)
    risk_cells, risk_summary = risk(k)
    dy = dyadic(k, perms)
    counts = d.groupby(["quintile", "any_twin"]).size()
    summary = {
        "population": "RQ3 decided papers 2019-2026 (P7: 2023-2026 author rows)", "papers": int(len(d)),
        "papers_by_year": d.groupby("year").size().to_dict(), "acceptance_rate": float(d.accepted.mean()),
        "any_twin_share": float(d.any_twin.mean()), "sibling_twin_share": float(d.sibling_twin.mean()),
        "quintile_x_twin_papers": {f"Q{int(q)}|{int(w)}": int(n) for (q, w), n in counts.items()},
        "family1": tests[["test", "coef", "ci95_lo", "ci95_hi", "p", "p_twoway", "p_calibrated", "p_used", "p_holm"]
                         ].to_dict("records"),
        "family3": dy[dy.variant == "cell"][["bin", "pairs", "rho", "rho_0", "stat", "stat_excess", "stat_null_lo",
                                             "stat_null_hi", "stat_p", "p_holm"]].to_dict("records"),
        "lind_mehlum": lind_mehlum(d), "risk": risk_summary, "calibration_nulls": nulls, "permutations": perms,
        "note": NOTE}
    return {"tests": tests, "curves": curves(fits), "surface": surface(d), "adjusted_table": adjusted_table(d),
            "risk": risk_cells, "dyadic": dy, "robustness": robustness(pop), **free_part(k), "summary": summary}


# ---------------------------------------------------------------------------------------------------- calibration
BASE_RATES = dict(zip(range(2017, 2027), np.linspace(0.45, 0.32, 10)))   # mirrors ph5_common.fake_outcomes
SHOCK_SD = np.sqrt(0.5)


def feature(k: pd.DataFrame, col: str) -> np.ndarray:
    f, _ = build()
    return f.set_index("submission_id")[col].reindex(k.submission_id).to_numpy(float)


def inverted_u(k: pd.DataFrame) -> np.ndarray:
    """-0.3 log-odds in novelty quintiles Q1 and Q5."""
    q = np.clip(np.floor(feature(k, "pct") * 5), 0, 4)
    return -0.3 * ((q == 0) | (q == 4))


def twin_hot(k: pd.DataFrame) -> np.ndarray:
    """-0.3 log-odds for papers with an independent twin in hot topics."""
    return -0.3 * (feature(k, f"twins_{tag(TAU)}") >= 1) * np.nan_to_num(k.hot.to_numpy(float))


def shared_shock(seed: int):
    """A common N(0, 0.5) (variance) log-odds shock per connected group of independent pairs with cos >= 0.80."""
    f, p = build()
    s = p[p.independent & (p.cos >= BINS[-1][0])]
    n = len(f)
    g = sparse.csr_matrix((np.ones(len(s)), (s.i, s.j)), shape=(n, n))
    _, lab = connected_components(g, directed=False)
    member = np.bincount(np.concatenate([s.i, s.j]), minlength=n) > 0
    shock = pd.Series(np.where(member, np.random.default_rng(seed).normal(0, SHOCK_SD, n)[lab], 0.0), f.submission_id)
    return lambda k: shock.reindex(k.submission_id).to_numpy()


def true_prob(k: pd.DataFrame, plant) -> np.ndarray:
    eta = logit(k.year.map(BASE_RATES).fillna(0.4).to_numpy(float))
    return expit(eta if plant is None else eta + plant(k))


def calibrate(n_null: int = 200, n_planted: int = 50, seed: int = 0, perms: int = 200) -> dict:
    """Declared tests on simulated frames (ph5_common.simulated_frame): null, inverted U, twin penalty in hot topics, and
    a shared shock for pairs at >= 0.80. Family 1: rejection at 0.05 (raw and Holm), mean estimate, mean target (the
    same model fitted to the true probabilities on the same sample), bias and CI coverage of the target; Lind-Mehlum
    rejection; Family 3 (cell variant, `perms` permutations): rejection (raw, Holm) and the mean statistic per bin. The
    shared shocks are redrawn for every frame."""
    plants = {"null": lambda s: None, "inverted_u": lambda s: inverted_u, "twin_hot": lambda s: twin_hot,
              "shared_shock": shared_shock}
    rows, lm, dy = [], [], []
    for j, (name, make) in enumerate(plants.items()):
        for i in range(n_null if name == "null" else n_planted):
            s = seed + 10_000 * j + i
            plant = make(s)
            k = prepare(ph5_common.simulated_frame(s, plant))
            d = design(population(k))
            res, _ = declared(d)
            tgt, _ = declared(d.assign(accepted=true_prob(d, plant)))
            rows += [{"plant": name, "frame": s, **r, "target": t} for r, t in zip(res.to_dict("records"), tgt.coef)]
            lm.append({"plant": name, "frame": s, **lind_mehlum(d)})
            dy += [{"plant": name, "frame": s, **r} for r in dyadic(k, perms, s, ("cell",)).to_dict("records")]
    r = pd.DataFrame(rows)
    r["reject"], r["reject_holm"] = r.p < 0.05, r.p_holm < 0.05
    r["reject_twoway"] = (r.p_twoway < 0.05).where(r.p_twoway.notna())
    r["covered"] = (r.ci95_lo <= r.target) & (r.target <= r.ci95_hi)
    per_test = r.groupby(["plant", "test"]).agg(
        frames=("p", "size"), reject=("reject", "mean"), reject_holm=("reject_holm", "mean"),
        reject_twoway=("reject_twoway", "mean"), mean_coef=("coef", "mean"), mean_target=("target", "mean"),
        coverage=("covered", "mean")).reset_index()
    per_test["bias"] = per_test.mean_coef - per_test.mean_target
    fam = r.groupby(["plant", "frame"]).reject_holm.any().groupby("plant").mean()
    lm = pd.DataFrame(lm).assign(reject=lambda x: x.p_inverted_u < 0.05)
    dy = pd.DataFrame(dy).assign(reject=lambda x: x.stat_p < 0.05, reject_holm=lambda x: x.p_holm < 0.05)
    return {"per_test": per_test.to_dict("records"), "family1_any_holm_rejection": fam.to_dict(),
            "lind_mehlum": lm.groupby("plant").agg(frames=("reject", "size"), reject=("reject", "mean"),
                                                   mean_b_quadratic=("b_quadratic", "mean")).reset_index().to_dict("records"),
            "family3": dy.groupby(["plant", "bin"]).agg(frames=("reject", "size"), reject=("reject", "mean"),
                                                        reject_holm=("reject_holm", "mean"), mean_rho=("rho", "mean"),
                                                        mean_stat=("stat", "mean")).reset_index().to_dict("records"),
            "family3_any_holm_rejection": dy.groupby(["plant", "frame"]).reject_holm.any().groupby("plant").mean().to_dict(),
            "n_null": n_null, "n_planted": n_planted, "seed": seed, "perms": perms}


# ---------------------------------------------------------------------------------------------------- figures
def plot(out_dir: Path) -> None:
    import figures
    plt = figures.plt
    out_dir = Path(out_dir)

    s = pd.read_csv(out_dir / "surface.csv")
    s["quintile"] = s.quintile.str[1:].astype(int)
    M, N, Q = (s.pivot(index="any_twin", columns="quintile", values=v) for v in ("coef", "papers", "q_bh"))
    fig, ax = plt.subplots(figsize=(5.6, 2.3), constrained_layout=True)
    lim = max(float(np.nanmax(np.abs(M.to_numpy()))) * 100, 1.0)
    im = ax.imshow(M.to_numpy() * 100, cmap=figures.DIVERGING, vmin=-lim, vmax=lim, aspect="auto")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            star = "*" if Q.iat[i, j] < 0.05 else ""
            ax.text(j, i, f"{M.iat[i, j] * 100:+.1f}{star}\nn={N.iat[i, j]:,}", ha="center", va="center", fontsize=6.8,
                    color=figures.INK)
    ax.set_xticks(range(5), ["Q1\nleast novel", "Q2", "Q3", "Q4", "Q5\nmost novel"])
    ax.set_yticks([0, 1], ["no twin", "independent twin"])
    ax.grid(False)
    fig.colorbar(im, ax=ax, shrink=0.8, label="pp vs Q3, no twin")
    ax.set_title("Acceptance by novelty quintile (within topic x year) and concurrent twins; * BH q < 0.05\n"
                 "post hoc, exploratory; decided papers 2019-2026", loc="left", fontsize=7.5)
    _save(fig, out_dir, "PH5_position_surface")

    c = pd.read_csv(out_dir / "curves.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 2.8), sharey=True, constrained_layout=True)
    for ax, model, groups, title in [(axes[0], "Q3", ["incumbent", "newcomer"], "Topic incumbents vs newcomers"),
                                     (axes[1], "Q4", MATURITY, "By topic maturity tercile")]:
        ax.axhline(0, color=figures.INK2, lw=0.7)
        for g_i, (g, colour) in enumerate(zip(groups, figures.SERIES)):
            r = c[(c.model == model) & (c.group == g)]
            x = r.quintile + (g_i - (len(groups) - 1) / 2) * 0.12
            ax.errorbar(x, r.coef * 100, yerr=[(r.coef - r.ci95_lo) * 100, (r.ci95_hi - r.coef) * 100], fmt="o-",
                        ms=3.5, lw=1.2, color=colour, label=g, capsize=0)
        ax.set_xticks(range(1, 6), ["Q1", "Q2", "Q3", "Q4", "Q5"])
        ax.set_xlabel("novelty quintile within topic x year (Q5 most novel)")
        ax.set_title(title + " (post hoc, exploratory)", loc="left")
        ax.legend(fontsize=6.8)
    axes[0].set_ylabel("pp vs Q3 of the same group (95% CI)")
    _save(fig, out_dir, "PH5_position_curves")

    dy = pd.read_csv(out_dir / "dyadic.csv")
    fig, ax = plt.subplots(figsize=(5.2, 2.8), constrained_layout=True)
    ax.axhline(0, color=figures.INK2, lw=0.7)
    for v_i, (variant, colour) in enumerate(zip(["cell", "year"], figures.SERIES)):
        r = dy[dy.variant == variant].reset_index(drop=True)
        x = np.arange(len(r)) + (v_i - 0.5) * 0.22
        ax.vlines(x, r.stat_null_lo, r.stat_null_hi, color=figures.MUTED, lw=4, alpha=0.5,
                  label="permutation 95% band" if v_i == 0 else None)
        ax.scatter(x, r.stat, color=colour, s=24, zorder=3, label=f"r vs {variant} mean")
    pairs = dy[dy.variant == "cell"].pairs.to_numpy()
    ax.set_xticks(range(len(BIN_NAMES)), [f"cos {b}\n{n:,} pairs" for b, n in zip(BIN_NAMES, pairs)])
    ax.set_ylabel("rho_b - rho_0 (outcome correlation)")
    ax.set_title("Do independent near-duplicates share fate? (post hoc, exploratory)", loc="left")
    ax.legend(fontsize=6.5)
    _save(fig, out_dir, "PH5_position_dyadic")

    share = pd.read_csv(out_dir / "free_twin_share.csv")
    fig, ax = plt.subplots(figsize=(5.0, 2.8), constrained_layout=True)
    for (dim, g), colour in zip([("all", "all"), ("hot", "hot"), ("hot", "other")], [figures.INK2] + figures.SERIES[:2]):
        r = share[(share.dimension == dim) & (share.group == g)]
        ax.plot(r.year, r.any_twin * 100, marker="o", ms=3, color=colour, label="all topics" if g == "all" else
                f"{g} topics")
    ax.set_ylabel("papers with an independent twin (%)")
    ax.set_title(f"Concurrent near-duplicates (cos >= {TAU:.2f}), all submissions (outcome-free)", loc="left")
    ax.legend(fontsize=6.8)
    _save(fig, out_dir, "PH5_position_twin_share")


def _save(fig, out_dir: Path, name: str) -> None:
    import figures
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out_dir / f"{name}.png", dpi=220, bbox_inches="tight")
    figures.plt.close(fig)
