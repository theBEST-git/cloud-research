"""PH5 kwtiming (final post hoc round, selection S1): when to enter a trend keyword. For papers that list an author
keyword of the trend vocabulary, compared with papers of the same k100 topic and year, how does acceptance vary with
the keyword's prospective lifecycle state (age since onset x within-year momentum), with arriving early in the paper's
own coarse area while the keyword is globally old, and with the team's track record? Post hoc and exploratory: every
estimate is an association within the stated fixed effects; Holm within each declared family ranks the evidence only.

Keyword frame (outcome-free; every discovery submission, any outcome):
  V           author keywords typed research_area / specific_topic (buzzwords.TYPES; 759 keywords)
  uses        one row per (paper, distinct keyword of V)
  onset o_k   first year (data start 2017) in which the cumulative number of papers listing k reaches 10;
              eligible in t iff t >= o_k + 1 (= keyword_year.eligible, asserted)
  age bin     a = t - o_k: young 1-2, middle 3-4, old >= 5; keywords with o_k <= 2018 are left-censored and coded old
  momentum    keyword_year.growth (share t-1 / share t-2, +0.5) cut into within-year terciles among eligible keywords:
              percentile rank pr = (average rank - 0.5) / n; falling pr < 1/3, flat < 2/3, rising otherwise (ties share
              a tercile)
  state       age bin x momentum (9 cells); Emerging = young x rising, Mainstream (reference) = old x flat, Cooling =
              old x falling, Fizzling = young x falling, Resurgent = old x rising
  weights     w = 1 / (the paper's number of eligible keywords in the sample): each paper weighs 1
  local arrival (Model C): the 129 keywords with >= 100 listing papers 2017-2026; area = coarse topic (20);
              A = first year the cumulative number of the keyword's users inside the area reaches 3; locally_early = 1
              if t <= A + 1 or the area never reaches 3 users by 2026 (then the true A is after t), 0 if t >= A + 2,
              i.e. locally_early = [fewer than 3 users in the area up to t - 2] (prospective); rows with global age
              bin middle / old ('globally late'; censored keywords included). The 129-keyword set is chosen with
              hindsight (later popularity); within keyword x year it only selects the sample
  profiles    first_time: no author ID with an earlier discovery submission (outcome-free); established: an author
              had an accepted ICLR paper in an earlier year (posthoc.established_authors; gated); no_acc = 1 -
              established among papers with an author ID; profile3: first-time / returning, never accepted /
              established. Profile models use the ID-consistent years 2019-20 and 2023-26 (2022 added as a check)
Gated models: RQ3 decided papers 2019-2026, outcome accepted, LPM, weights w, k100 topic x year FE absorbed.
Controls X: class (ref. method) + fm + log2 team (cap 16) + newcomer + log(1 + number of V keywords listed).
SE two-way clustered by keyword and k100 topic (Cameron-Gelbach-Miller V_kw + V_topic - V_kw&topic, CR1 factors,
eigenvalues clipped at 0), t with min(G) - 1 df.
  A   accepted ~ 8 state dummies + X | topic x year; adjusted P(state) = effect + the Mainstream (weighted) mean;
      omnibus Wald F (8 df) with p calibrated on 200 null frames (ph5_common.fake_outcomes seeds 0-199, decided set
      and acceptance both simulated): p = (1 + #F_null >= F) / 201
  B   ID-consistent years: A + state x no_acc + no_acc; descriptive EB table of adjusted P(state, profile3) (27 cell
      dummies, ref. Mainstream x established, each cell shrunk to its state's mean, method-of-moments tau^2)
  C   globally late rows of the 129 keywords: accepted ~ locally_early + X | keyword x year + topic x year
      (alternating projections), weight 1 / (the paper's number of such rows); descriptive: global age 3-4 vs >= 5
      x local stage (raw rates and within-age effects) and importer split (domain insider = topic incumbent,
      keyword incumbent = an author listed the keyword in an earlier year) with MDE80
  D   r = accepted - leave-one-out mean of the topic x year cell; per keyword with >= 30 decided young-stage uses,
      premium = mean r (variance s^2 / n_k, s^2 the pooled within-keyword variance of r); DerSimonian-Laird tau, EB
      posterior means, tau null from 50 within-cell permutations; survivorship gap: mean premium of keywords with
      >= 100 papers vs all (descriptive)
  risk  Model A on the S9 population with s9_accepted and with withdrawn_after_review (nominal p)
Declared tests: family A (Holm over 3) A1 Emerging - Mainstream, A2 Cooling - Mainstream, A3 mean over momentum
terciles of (young - old); family B (Holm over 2) D_E, D_C = the no_acc minus established difference of
(Emerging - Mainstream), (Cooling - Mainstream); family C beta(locally_early). Each is reported with its analytic and
simulated MDE80 ((t.975 + t.80) x SE, or x the SD of the estimate over the 200 null frames), its rejection rate at
0.05 in those frames and, as a size check that is not counted, p_null_frames = (1 + #|t_null| >= |t|) / 201.
Robustness (reported, not counted): censored keywords dropped, 2-year momentum (share t-1 / share t-3; from 2020),
2022-2026, early-map topic x year FE, keyword FE + topic x year FE with momentum only, unweighted, weighted FE logit
(A1-A3, log-odds), no earlier version; Model B with 2022; Model C with arrival threshold 5, censored keywords dropped,
and ICLR primary_area 2025-2026 (see primary_areas).
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import expit, logit

import panel
import ph5_common
import posthoc
from buzzwords import TYPES
from common import OUTPUT, TOPICS, topic_layer
from panel import CLASS_CONTROLS
from variables import load_authors
from variants import holm

YEARS = tuple(range(2019, 2027))
PROFILE_YEARS = (2019, 2020, 2023, 2024, 2025, 2026)
ONSET_USERS, CENSOR_YEAR, BIG_PAPERS, ARRIVAL, ARRIVAL_ALT = 10, 2018, 100, 3, 5
PA_FROM = 2025                                    # the 2025-2026 primary-area taxonomy (2024's differs)
AGES, MOMS = ["young", "middle", "old"], ["falling", "flat", "rising"]
STATES = [f"{a}_{m}" for a in AGES for m in MOMS]
REF = "old_flat"
NAMED = {"young_rising": "Emerging", "old_flat": "Mainstream", "old_falling": "Cooling", "young_falling": "Fizzling",
         "old_rising": "Resurgent"}
DUMMIES = [f"st_{s}" for s in STATES if s != REF]
CONTROLS = CLASS_CONTROLS + ["fm", "log2_team", "newcomer", "log_nv"]
PROFILES = ["first_time", "returning_no_acceptance", "established"]
IMPORTERS = ["domain_and_keyword_insider", "domain_insider_only", "keyword_incumbent_only", "neither"]
PREMIUM_MIN, PERMS, N_REF, SEED = 30, 50, 200, 20261017
NOTE = "post hoc exploratory (PH5 kwtiming, selection S1); associations within the stated fixed effects, not causal"
A_TESTS = {"A1": {"st_young_rising": 1.0}, "A2": {"st_old_falling": 1.0},
           "A3": {"st_young_falling": 1 / 3, "st_old_falling": -1 / 3, "st_young_flat": 1 / 3,
                  "st_young_rising": 1 / 3, "st_old_rising": -1 / 3}}
B_TESTS = {"D_E": {"st_young_rising_na": 1.0}, "D_C": {"st_old_falling_na": 1.0}}
TESTS = [("A", "A1", "Emerging (young x rising) minus Mainstream (old x flat)"),
         ("A", "A2", "Cooling (old x falling) minus Mainstream"),
         ("A", "A3", "age gradient: mean over momentum terciles of (young - old)"),
         ("B", "D_E", "Emerging - Mainstream: no earlier acceptance minus established"),
         ("B", "D_C", "Cooling - Mainstream: no earlier acceptance minus established"),
         ("C", "C1", "locally early (globally late keyword) | keyword x year + topic x year")]


# ---------------------------------------------------------------------------------------------------- estimators
@dataclass
class Fit:
    beta: pd.Series
    V: pd.DataFrame                                 # two-way (clipped) covariance, or one-way with one cluster
    G: int                                          # min clusters; t reference with G - 1 df
    rows: int
    papers: int

    def lincom(self, w: dict[str, float]) -> dict:
        """Estimate, SE, t(G - 1) p, 95% CI and analytic MDE80 of sum w_j b_j; NaN if a term is not identified."""
        out = {"rows": self.rows, "papers": self.papers, "dof": self.G - 1}
        if not set(w) <= set(self.beta.index):
            return {"coef": np.nan, "se": np.nan, "p": np.nan, "ci95_lo": np.nan, "ci95_hi": np.nan, "mde80": np.nan,
                    **out, "note": "not identified: " + ";".join(sorted(set(w) - set(self.beta.index)))}
        c = pd.Series(w).reindex(self.beta.index).fillna(0.0).to_numpy()
        est, se = float(c @ self.beta.to_numpy()), float(np.sqrt(max(c @ self.V.to_numpy() @ c, 0.0)))
        q = stats.t.ppf(0.975, self.G - 1)
        p = float(2 * stats.t.sf(abs(est / se), self.G - 1)) if se > 0 else np.nan
        return {"coef": est, "se": se, "p": p, "ci95_lo": est - q * se, "ci95_hi": est + q * se,
                "mde80": (q + stats.t.ppf(0.80, self.G - 1)) * se, **out}

    def wald(self, cols: list[str]) -> dict:
        """Joint test that the coefficients in cols are zero: F = b' V^+ b / q, nominal p from F(q, G - 1)."""
        cols = [c for c in cols if c in self.beta.index]
        b, V = self.beta[cols].to_numpy(), self.V.loc[cols, cols].to_numpy()
        F = float(b @ np.linalg.pinv(V) @ b / len(cols))
        return {"F": F, "df1": len(cols), "df2": self.G - 1, "p_nominal": float(stats.f.sf(F, len(cols), self.G - 1))}


def _sums(codes: np.ndarray, M: np.ndarray) -> np.ndarray:
    G = codes.max() + 1
    return np.column_stack([np.bincount(codes, weights=M[:, j], minlength=G) for j in range(M.shape[1])])


def _twoway(scores: np.ndarray, bread: np.ndarray, d: pd.DataFrame, clusters: tuple[str, ...], scale: float):
    """CR1 covariance by one cluster, or two-way (Cameron-Gelbach-Miller, eigenvalues clipped at 0)."""
    def cr1(groups: np.ndarray) -> tuple[np.ndarray, int]:
        cg = pd.factorize(groups)[0]
        G = int(cg.max() + 1)
        S = _sums(cg, scores)
        return (G / (G - 1)) * scale * bread @ (S.T @ S) @ bread, G

    V, G = cr1(d[clusters[0]].to_numpy())
    if len(clusters) == 2:
        V2, G2 = cr1(d[clusters[1]].to_numpy())
        V12, _ = cr1(d[clusters[0]].astype(str).to_numpy() + "|" + d[clusters[1]].astype(str).to_numpy())
        lam, Q = np.linalg.eigh(V + V2 - V12)
        V, G = (Q * np.clip(lam, 0, None)) @ Q.T, min(G, G2)
    return V, G


def fit(d: pd.DataFrame, y: str, xs: list[str], fes: tuple[str, ...] = ("cell",), w: str = "w",
        clusters: tuple[str, ...] = ("keyword", "topic")) -> Fit:
    """posthoc.wls_fe (same singleton dropping, weighted alternating projections, CR1 factor) returning the full
    one- or two-way covariance matrix."""
    d = posthoc.drop_singletons(d.dropna(subset=[y, *xs, w]), list(fes)).reset_index(drop=True)
    wv = d[w].to_numpy(float)
    yd, Xd = posthoc.twfe(d[y].to_numpy(float), d[xs].to_numpy(float), [d[f].to_numpy() for f in fes], wv)
    keep = Xd.std(axis=0) > 1e-12
    xs, Xd = [x for x, k_ in zip(xs, keep) if k_], Xd[:, keep]
    Xw = Xd * wv[:, None]
    bread = np.linalg.pinv(Xd.T @ Xw)
    beta = bread @ Xw.T @ yd
    n, k = Xd.shape
    V, G = _twoway(Xw * (yd - Xd @ beta)[:, None], bread, d, clusters, (n - 1) / (n - k))
    papers = int(d.i.nunique()) if "i" in d else n
    return Fit(pd.Series(beta, xs), pd.DataFrame(V, xs, xs), G, n, papers)


def fe_logit_w(d: pd.DataFrame, y: str, xs: list[str], fe: str = "cell", w: str = "w",
               clusters: tuple[str, ...] = ("keyword", "topic"), tol: float = 1e-10, max_iter: int = 100) -> Fit:
    """Weighted logit with one set of group intercepts (Newton steps, Schur complement on the diagonal intercept
    block, step-halving). Groups whose weighted outcome is all 0 or all 1 are dropped. Sandwich from the partialled
    scores (x_i - weighted group mean) * w_i (y_i - p_i), CR1 factor G / (G - 1), one- or two-way; log-odds."""
    d = d.dropna(subset=[y, *xs, w]).reset_index(drop=True)
    c = pd.factorize(d[fe])[0]
    yv, wv = d[y].to_numpy(float), d[w].to_numpy(float)
    rate = np.bincount(c, wv * yv) / np.bincount(c, wv)
    d = d[((rate > 0) & (rate < 1))[c]].reset_index(drop=True)
    c = pd.factorize(d[fe])[0]
    yv, wv, X = d[y].to_numpy(float), d[w].to_numpy(float), d[xs].to_numpy(float)
    G = c.max() + 1
    rate = np.bincount(c, wv * yv, G) / np.bincount(c, wv, G)
    b, a = np.zeros(X.shape[1]), logit(rate)

    def loglik(b_, a_):
        eta = X @ b_ + a_[c]
        return float(np.sum(wv * (yv * eta - np.logaddexp(0.0, eta))))

    ll = loglik(b, a)
    for _ in range(max_iter):
        p = expit(X @ b + a[c])
        r, W = wv * (yv - p), wv * p * (1 - p)
        haa, hxa = np.bincount(c, W, G), _sums(c, X * W[:, None]).T
        S = X.T @ (X * W[:, None]) - (hxa / haa) @ hxa.T
        ga = np.bincount(c, r, G)
        db = np.linalg.solve(S, X.T @ r - hxa @ (ga / haa))
        da = (ga - hxa.T @ db) / haa
        t = 1.0
        while (new := loglik(b + t * db, a + t * da)) < ll - 1e-12 and t > 1e-8:
            t /= 2
        b, a, ll_old, ll = b + t * db, a + t * da, ll, new
        if max(np.abs(t * db).max(), np.abs(t * da).max()) < tol or abs(ll - ll_old) < tol * (1 + abs(ll)):
            break
    p = expit(X @ b + a[c])
    W = wv * p * (1 - p)
    haa, hxa = np.bincount(c, W, G), _sums(c, X * W[:, None]).T
    bread = np.linalg.inv(X.T @ (X * W[:, None]) - (hxa / haa) @ hxa.T)
    scores = (X - (hxa / haa).T[c]) * (wv * (yv - p))[:, None]
    V, Gc = _twoway(scores, bread, d, clusters, 1.0)
    return Fit(pd.Series(b, xs), pd.DataFrame(V, xs, xs), Gc, len(d), int(d.i.nunique()) if "i" in d else len(d))


def dersimonian_laird(y: np.ndarray, v: np.ndarray) -> dict:
    """Random-effects summary: DL tau^2, its mean mu, Q, I^2 and EB posterior means / SDs (mu treated as known)."""
    w = 1 / v
    mu_fe = np.sum(w * y) / w.sum()
    Q = float(np.sum(w * (y - mu_fe) ** 2))
    K = len(y)
    tau2 = max(0.0, (Q - (K - 1)) / (w.sum() - np.sum(w ** 2) / w.sum()))
    ws = 1 / (v + tau2)
    mu = float(np.sum(ws * y) / ws.sum())
    B = tau2 / (tau2 + v)
    return {"tau2": tau2, "tau": float(np.sqrt(tau2)), "mu": mu, "Q": Q, "K": K,
            "I2": max(0.0, (Q - (K - 1)) / Q) if Q > 0 else 0.0, "post_mean": mu + B * (y - mu),
            "post_sd": np.sqrt(B * v)}


# ---------------------------------------------------------------------------------------------------- features
def terciles(g: pd.Series, year: pd.Series) -> pd.Series:
    """Within-year momentum tercile from percentile ranks (average ranks, so ties share a tercile); NaN stays NaN."""
    pr = (g.groupby(year).rank(method="average") - 0.5) / g.groupby(year).transform("count")
    lab = np.select([pr < 1 / 3, pr < 2 / 3], ["falling", "flat"], "rising")
    return pd.Series(lab, g.index).where(g.notna())


def keyword_states(u: pd.DataFrame, n_year: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Per keyword: onset, total papers, censored, big. Per eligible keyword-year 2019-2026: age bin, momentum
    terciles (1-year from keyword_year.growth, 2-year recomputed) and states."""
    cnt = u.groupby(["keyword", "year"]).size().unstack(fill_value=0).reindex(columns=range(2017, 2027), fill_value=0)
    reached = cnt.cumsum(axis=1) >= ONSET_USERS
    kw = pd.DataFrame({"onset": reached.idxmax(axis=1).where(reached.any(axis=1)), "papers": cnt.sum(axis=1)})
    kw["censored"], kw["big"] = kw.onset <= CENSOR_YEAR, kw.papers >= BIG_PAPERS
    share = ((cnt + 0.5) / n_year.reindex(cnt.columns).to_numpy()).stack()
    ky = pd.read_csv(OUTPUT / "keyword_year.csv.gz", usecols=["keyword", "year", "growth", "eligible"])
    ky = ky.join(kw.onset, on="keyword")
    assert (ky.eligible == (ky.year >= ky.onset + 1)).all(), "onset rule disagrees with keyword_year.eligible"
    ky = ky[ky.eligible].reset_index(drop=True)
    at = lambda lag: share.reindex(pd.MultiIndex.from_arrays([ky.keyword, ky.year - lag])).to_numpy()  # noqa: E731
    assert np.allclose(at(1) / at(2), ky.growth, rtol=1e-5, atol=1e-6), "recomputed growth disagrees with keyword_year"
    ky["growth2"] = (at(1) / at(3)).round(10)                 # NaN in 2019 (no 2016 data)
    ky["age"] = ky.year - ky.onset
    ky["censored"] = ky.onset <= CENSOR_YEAR
    ky["agebin"] = np.select([ky.censored, ky.age <= 2, ky.age <= 4], ["old", "young", "middle"], "old")
    ky["mom"], ky["mom2"] = terciles(ky.growth, ky.year), terciles(ky.growth2, ky.year)
    ky["state"] = ky.agebin + "_" + ky.mom
    ky["state2"] = (ky.agebin + "_" + ky.mom2).where(ky.mom2.notna())
    return kw, ky


def arrivals(u: pd.DataFrame, col: str, threshold: int) -> pd.Series:
    """First year in which the cumulative number of a keyword's users inside area `col` reaches threshold."""
    c = u.dropna(subset=[col]).groupby(["keyword", col, "year"]).size().rename("n").reset_index()
    c = c.sort_values(["keyword", col, "year"])
    c["cum"] = c.groupby(["keyword", col]).n.cumsum()
    return c[c.cum >= threshold].groupby(["keyword", col]).year.min()


def locally_early(u: pd.DataFrame, col: str, threshold: int) -> np.ndarray:
    """1 if t <= A + 1 or the area never reaches the threshold (true A after 2026 >= t), 0 if t >= A + 2; NaN for
    keywords outside the big set or rows without an area."""
    A = arrivals(u[u.big], col, threshold).reindex(pd.MultiIndex.from_arrays([u.keyword, u[col]])).to_numpy(float)
    le = np.where(np.isnan(A), 1.0, (u.year.to_numpy() <= A + 1).astype(float))
    return np.where(u.big.to_numpy() & u[col].notna().to_numpy(), le, np.nan)


def primary_areas(corpus: pd.DataFrame, fine: np.ndarray, years: np.ndarray) -> np.ndarray:
    """ICLR primary area: the author's own choice from 2025 (one taxonomy in 2025-2026), and for earlier papers the
    modal 2025-2026 primary area of the paper's fine topic (ties: alphabetical), so arrival years are not truncated
    at the first year with primary areas."""
    pa = corpus.primary_area.replace("", np.nan).to_numpy(object)
    own = (years >= PA_FROM) & pd.notna(pa)
    modal = pd.Series(pa[own]).groupby(fine[own]).agg(lambda s: s.value_counts().sort_index().idxmax())
    return np.where(years >= PA_FROM, pa, pd.Series(fine).map(modal).to_numpy(object))


def keyword_incumbent_rows(u: pd.DataFrame, ids: pd.Series) -> np.ndarray:
    """Per use row: 1 if an author ID of the paper listed the keyword in an earlier year (posthoc.keyword_incumbent,
    vectorised over keywords), 0 if not, NaN without an author ID. Outcome-free."""
    a = load_authors(ids)[["submission_id", "key"]]
    a["i"] = a.submission_id.map(pd.Series(np.arange(len(ids)), index=ids.to_numpy()))
    au = u[["i", "keyword", "year"]].assign(row=np.arange(len(u))).merge(a[["i", "key"]], on="i")
    au["inc"] = au.groupby(["key", "keyword"]).year.transform("min") < au.year
    return au.groupby("row").inc.any().reindex(range(len(u))).to_numpy(float)


@lru_cache(maxsize=1)
def features() -> dict[str, pd.DataFrame]:
    """Outcome-free keyword uses, keyword table and paper features in panel.frame('k100') order (cached; read only)."""
    k = panel.frame("k100").reset_index(drop=True)
    corpus = topic_layer().embedded_corpus()
    assert (corpus.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    ta = pd.read_csv(TOPICS / "topic_assignments.csv.gz", usecols=["submission_id", "fine", "coarse"])
    assert ta.submission_id.equals(k.submission_id)
    kt = pd.read_csv(TOPICS / "keyword_types.csv", keep_default_na=False)
    vocab = set(kt[kt.type.isin(TYPES)].keyword)
    years = k.year.to_numpy()
    u = pd.DataFrame([(i, kw) for i, kws in enumerate(corpus.keywords) for kw in sorted(set(kws) & vocab)],
                     columns=["i", "keyword"])
    u["year"] = years[u.i]
    u["area"] = ta.coarse.to_numpy()[u.i]
    u["pa_area"] = primary_areas(corpus, ta.fine.to_numpy(), years)[u.i]
    kw, ky = keyword_states(u, pd.Series(years).value_counts())
    u = u.merge(ky[["keyword", "year", "agebin", "mom", "state", "state2"]], on=["keyword", "year"], how="left")
    u = u.join(kw[["onset", "censored", "big"]], on="keyword")
    u["eligible"] = u.state.notna()
    u["global_late"] = u.agebin.isin(["middle", "old"])
    for name, col, thr in [("le3", "area", ARRIVAL), ("le5", "area", ARRIVAL_ALT), ("le_pa", "pa_area", ARRIVAL)]:
        u[name] = locally_early(u, col, thr)
    u["kw_inc"] = keyword_incumbent_rows(u, k.submission_id)

    a = load_authors(k.submission_id)[["submission_id", "key"]].merge(k[["submission_id", "year"]], on="submission_id")
    a["seen"] = a.key.map(a.groupby("key").year.min()) < a.year
    seen = a.groupby("submission_id").seen.any().reindex(k.submission_id).fillna(False).to_numpy(float)
    el = u[u.eligible]
    n_el = el.groupby("i").size()
    late = u[u.global_late & (u.le3 == 1)]
    papers = pd.DataFrame({"submission_id": k.submission_id,
                           "n_v": u.groupby("i").size().reindex(range(len(k)), fill_value=0).to_numpy(),
                           "n_eligible": n_el.reindex(range(len(k)), fill_value=0).to_numpy(),
                           "first_time": np.where(k.has_author_key, 1.0 - seen, np.nan)})
    for flag, s in [("all_emerging", "young_rising"), ("all_cooling", "old_falling")]:
        hit = (el.state == s).groupby(el.i).sum()
        papers[flag] = (hit == n_el).reindex(range(len(k)), fill_value=False).to_numpy(float)
    papers["has_local_early"] = np.isin(np.arange(len(k)), late.i.unique()).astype(float)
    return {"uses": u, "keywords": kw, "keyword_years": ky, "papers": papers}


def prepare(k: pd.DataFrame) -> pd.DataFrame:
    """k (panel order) with log2 team (posthoc.add_columns), the paper features and, if k has outcomes, profiles."""
    k = posthoc.add_columns(k.reset_index(drop=True).copy())
    f = features()["papers"]
    assert (f.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    k["log_nv"], k["first_time"] = np.log1p(f.n_v.to_numpy()), f.first_time.to_numpy()
    k["cell_early"] = k.topic_early.astype(str) + ":" + k.year.astype(str)
    if "accepted" in k:
        est = posthoc.established_authors(k)
        k["no_acc"] = np.where(k.has_author_key, 1.0 - est, np.nan)
        k["profile3"] = np.select([k.first_time == 1, k.no_acc == 1, k.no_acc == 0], PROFILES, "")
    return k


PAPER_COLS = ["submission_id", "topic", "cell", "topic_early", "cell_early", "fm", "log2_team", "newcomer", "incumbent",
              "has_author_key", "has_earlier_version", "log_nv", "first_time", *CLASS_CONTROLS, "rq3", "accepted", "s9",
              "s9_accepted", "withdrawn_after_review", "no_acc", "profile3"]


def stack(k: pd.DataFrame, papers: np.ndarray, rows: Callable[[pd.DataFrame], pd.Series] | None = None,
          state: str = "state") -> pd.DataFrame:
    """Eligible use rows of the papers flagged in `papers` (bool, panel order) joined with the paper columns, state
    dummies and w = 1 / (the paper's rows left after `rows`)."""
    u = features()["uses"]
    r = u[u.eligible & papers[u.i.to_numpy()] & u[state].notna()]
    r = r.join(k[[c for c in PAPER_COLS if c in k]], on="i")
    r = r[rows(r).to_numpy(bool)] if rows is not None else r
    r = r.assign(w=1.0 / r.groupby("i").i.transform("size"))
    return r.assign(**{f"st_{s}": (r[state] == s).astype(float) for s in STATES if s != REF})


def decided(k: pd.DataFrame, years=YEARS, pop: str = "rq3") -> np.ndarray:
    return (k[pop].astype(bool) & k.year.isin(years)).to_numpy()


def stack_c(k: pd.DataFrame, le: str = "le3", years=YEARS, rows=None) -> pd.DataFrame:
    """Model C rows: globally late uses of the big keywords with a local stage; w = 1 / (the paper's such rows)."""
    u = features()["uses"]
    r = u[u.big & u.global_late & u[le].notna() & decided(k, years)[u.i.to_numpy()]]
    r = r.join(k[[c for c in PAPER_COLS if c in k]], on="i")
    r = r[rows(r).to_numpy(bool)] if rows is not None else r
    return r.assign(w=1.0 / r.groupby("i").i.transform("size"), locally_early=r[le],
                    kwyear=r.keyword + ":" + r.year.astype(str))


# ---------------------------------------------------------------------------------------------------- models
def model_a(k: pd.DataFrame, years=YEARS, pop: str = "rq3", y: str = "accepted", **kw) -> tuple[Fit, pd.DataFrame]:
    opts = {o: kw.pop(o) for o in ("fes", "clusters") if o in kw}
    r = stack(k, decided(k, years, pop), **kw)
    return fit(r, y, DUMMIES + CONTROLS, **opts), r


def model_b(k: pd.DataFrame, years=PROFILE_YEARS) -> tuple[Fit, pd.DataFrame]:
    r = stack(k, decided(k, years) & k.no_acc.notna().to_numpy())
    r = r.assign(**{f"{x}_na": r[x] * r.no_acc for x in DUMMIES})
    return fit(r, "accepted", DUMMIES + [f"{x}_na" for x in DUMMIES] + ["no_acc"] + CONTROLS), r


def model_c(k: pd.DataFrame, le: str = "le3", years=YEARS, rows=None) -> tuple[Fit, pd.DataFrame]:
    r = stack_c(k, le, years, rows)
    return fit(r, "accepted", ["locally_early"] + CONTROLS, fes=("kwyear", "cell")), r


def declared(k: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, tuple[Fit, pd.DataFrame]], dict]:
    """The six declared tests (Holm within families A and B), the fitted models with their rows, and the omnibus F
    (nominal p) on a prepared frame."""
    m = {"A": model_a(k), "B": model_b(k), "C": model_c(k)}
    res = {t: m["A"][0].lincom(c) for t, c in A_TESTS.items()} | {t: m["B"][0].lincom(c) for t, c in B_TESTS.items()}
    res["C1"] = m["C"][0].lincom({"locally_early": 1.0})
    rows = pd.DataFrame([{"family": fam, "test": t, "label": lab, **res[t]} for fam, t, lab in TESTS])
    for _, g in rows.groupby("family"):
        rows.loc[g.index, "p_holm"] = holm(g.p.fillna(1.0)).to_numpy()
    return rows, m, m["A"][0].wald(DUMMIES)


def reference(k: pd.DataFrame, n_ref: int = N_REF) -> pd.DataFrame:
    """Omnibus F and the six declared estimates (coef, nominal p, t) on null frames: the decided set and acceptance
    from ph5_common.fake_outcomes(k, seed), seeds 0..n_ref-1; profiles stay those of k."""
    out = []
    for s in range(n_ref):
        o = ph5_common.fake_outcomes(k, s)
        kk = k.assign(rq3=o.rq3.to_numpy(), accepted=o.accepted.to_numpy())
        fits = {"A": model_a(kk)[0], "B": model_b(kk)[0], "C": model_c(kk)[0]}
        row = {"seed": s, **fits["A"].wald(DUMMIES)}
        for t, c in {**A_TESTS, **B_TESTS, "C1": {"locally_early": 1.0}}.items():
            e = fits["B" if t in B_TESTS else "C" if t == "C1" else "A"].lincom(c)
            row[f"{t}_coef"], row[f"{t}_p"] = e["coef"], e["p"]
            row[f"{t}_t"] = e["coef"] / e["se"] if e["se"] > 0 else np.nan
        out.append(row)
    return pd.DataFrame(out)


def wmean(y: pd.Series, w: pd.Series) -> float:
    ok = y.notna()
    return float(np.average(y[ok], weights=w[ok])) if ok.any() else np.nan


def state_rows(f: Fit, r: pd.DataFrame, model: str, y: str = "accepted", na: bool = False) -> list[dict]:
    """One row per state: effect vs Mainstream (Model B: + the state x no_acc term when na), adjusted P = effect +
    the weighted Mainstream mean of the rows, counts."""
    if model.startswith("B"):
        r = r[r.no_acc == float(na)]
    base = wmean(r[y][r.state == REF], r.w[r.state == REF])
    out = []
    for s in STATES:
        a, m = s.split("_")
        terms = {} if s == REF else {f"st_{s}": 1.0, **({f"st_{s}_na": 1.0} if na else {})}
        e = f.lincom(terms) if terms else {"coef": 0.0, "se": 0.0, "p": np.nan, "ci95_lo": 0.0, "ci95_hi": 0.0}
        g = r[r.state == s]
        out.append({"model": model, "state": s, "age": a, "momentum": m, "name": NAMED.get(s, ""),
                    **{c: e.get(c, np.nan) for c in ("coef", "se", "p", "ci95_lo", "ci95_hi")},
                    "adjusted_rate": e["coef"] + base, "raw_rate": wmean(g[y], g.w), "uses": int(len(g)),
                    "weighted_papers": float(g.w.sum()), "keywords": int(g.keyword.nunique())})
    return out


def mom_shrink(m: pd.Series, se: pd.Series, group: pd.Series) -> tuple[pd.Series, pd.Series, float]:
    """Group means of m, EB shrinkage tau^2 / (tau^2 + se^2) and the method-of-moments between-cell variance (cells
    independent): tau^2 = max(0, [sum (m - mean_g)^2 - sum (J_g - 1) / J_g se^2] / sum (J_g - 1))."""
    ok = m.notna() & se.notna()
    mean = m[ok].groupby(group[ok]).transform("mean").reindex(m.index)
    J = m[ok].groupby(group[ok]).transform("size")
    num = float(((m - mean)[ok] ** 2).sum() - ((J - 1) / J * se[ok] ** 2).sum())
    tau2 = max(0.0, num / float(ok.sum() - group[ok].nunique()))
    return mean, tau2 / (tau2 + se ** 2), tau2


def profile_cells(k: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Adjusted P(accept | state, profile3) (27 cells, ref. Mainstream x established) shrunk to each state's mean."""
    r = stack(k, decided(k, PROFILE_YEARS) & (k.profile3 != "").to_numpy())
    cell = r.state + "|" + r.profile3
    ref = f"{REF}|established"
    names = [f"{s}|{p}" for s in STATES for p in PROFILES]
    r = r.assign(**{f"c_{c}": (cell == c).astype(float) for c in names if c != ref})
    f = fit(r, "accepted", [f"c_{c}" for c in names if c != ref] + CONTROLS)
    base = wmean(r.accepted[cell == ref], r.w[cell == ref])
    rows = []
    for c in names:
        s, p = c.split("|")
        e = f.lincom({f"c_{c}": 1.0}) if c != ref else {"coef": 0.0, "se": 0.0}
        g = r[cell == c]
        rows.append({"state": s, "name": NAMED.get(s, ""), "profile": p, "uses": int(len(g)), "papers": int(g.i.nunique()),
                     "weighted_papers": float(g.w.sum()), "raw_rate": wmean(g.accepted, g.w),
                     "adjusted_rate": e["coef"] + base if len(g) else np.nan, "se": e["se"] if len(g) else np.nan})
    t = pd.DataFrame(rows)
    t["state_mean"], t["shrinkage"], tau2 = mom_shrink(t.adjusted_rate, t.se, t.state)
    t.loc[(t.state == REF) & (t.profile == "established"), "shrinkage"] = 1.0
    t["shrunk_rate"] = t.state_mean + t.shrinkage * (t.adjusted_rate - t.state_mean)
    return t, {"tau_between_profile_cells": float(np.sqrt(tau2)), "reference_cell_rate": base,
               "note": "descriptive; cells treated as independent in the method of moments; the reference cell has "
                       "SE 0 and is not shrunk"}


def local_early(k: pd.DataFrame, fc: Fit, rc: pd.DataFrame) -> pd.DataFrame:
    """Model C and its descriptives: by global age, the 2 x 2 grid, importer split, robustness."""
    main = fc.lincom({"locally_early": 1.0})
    rows = [{"block": "C main", "label": "locally early", **main,
             "uses_early": int((rc.locally_early == 1).sum()), "uses_late": int((rc.locally_early == 0).sum())}]
    r = rc.assign(le_mid=rc.locally_early * (rc.agebin == "middle"), le_old=rc.locally_early * (rc.agebin == "old"))
    f = fit(r, "accepted", ["le_mid", "le_old"] + CONTROLS, fes=("kwyear", "cell"))
    rows += [{"block": "C by global age", "label": lab, **f.lincom({t: 1.0})}
             for t, lab in [("le_mid", "global age 3-4"), ("le_old", "global age >= 5 (incl. censored)")]]
    for a, lab in [("middle", "global age 3-4"), ("old", "global age >= 5 (incl. censored)")]:
        for le, stage in [(1.0, "locally early"), (0.0, "locally late")]:
            g = rc[(rc.agebin == a) & (rc.locally_early == le)]
            rows.append({"block": "C grid", "label": f"{lab} | {stage}", "rate": wmean(g.accepted, g.w),
                         "rows": int(len(g)), "papers": int(g.i.nunique()), "weighted_papers": float(g.w.sum())})
    r = rc.dropna(subset=["incumbent", "kw_inc"])
    grp = np.select([(r.incumbent == 1) & (r.kw_inc == 1), r.incumbent == 1, r.kw_inc == 1], IMPORTERS[:3], IMPORTERS[3])
    r = r.assign(**{f"g_{g}": (grp == g).astype(float) for g in IMPORTERS},
                 **{f"le_{g}": r.locally_early * (grp == g) for g in IMPORTERS})
    ctr = [c for c in CONTROLS if c != "newcomer"]                            # newcomer = 1 - domain insider
    f = fit(r, "accepted", [f"le_{g}" for g in IMPORTERS] + [f"g_{g}" for g in IMPORTERS[:3]] + ctr,
            fes=("kwyear", "cell"))
    for g in IMPORTERS:
        rows.append({"block": "C importer", "label": g, **f.lincom({f"le_{g}": 1.0}),
                     "uses_early": int(((grp == g) & (r.locally_early == 1)).sum()),
                     "uses_late": int(((grp == g) & (r.locally_early == 0)).sum())})
    rows.append({"block": "C importer", "label": "domain_insider_only minus keyword_incumbent_only",
                 **f.lincom({"le_domain_insider_only": 1.0, "le_keyword_incumbent_only": -1.0})})
    for name, kw in [("arrival threshold 5", {"le": "le5"}), ("censored keywords dropped", {"rows": lambda x: ~x.censored}),
                     ("ICLR primary area, 2025-2026", {"le": "le_pa", "years": (2025, 2026)})]:
        f, rr = model_c(k, **kw)
        rows.append({"block": "C robustness", "label": name, **f.lincom({"locally_early": 1.0}),
                     "uses_early": int((rr.locally_early == 1).sum()), "uses_late": int((rr.locally_early == 0).sum())})
    return pd.DataFrame(rows)


def pooled_dl(g: pd.DataFrame) -> dict:
    """DerSimonian-Laird over per-keyword (size, mean, var) rows with v_k = pooled within-keyword variance / n_k (a
    keyword's own variance of a binary outcome moves with its mean and would bias mu and tau)."""
    s2 = float(((g["size"] - 1) * g["var"]).sum() / (g["size"] - 1).sum())
    return dersimonian_laird(g["mean"].to_numpy(), s2 / g["size"].to_numpy(float)) | {"pooled_var": s2}


def within_cell_permutation(y: np.ndarray, codes: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """y shuffled within the groups given by codes (cell sizes and sums preserved)."""
    order, out = np.argsort(codes, kind="stable"), np.empty_like(y)
    out[order] = y[np.lexsort((rng.random(len(y)), codes))]
    return out


def keyword_premia(k: pd.DataFrame, rng: np.random.Generator, perms: int = PERMS) -> tuple[pd.DataFrame, dict]:
    """Model D: per-keyword early-entry premium (young-stage uses), DL tau, EB means, permutation tau null."""
    d = k[decided(k)]
    y = d.accepted.to_numpy(float)
    codes = pd.factorize(d.cell)[0]
    s, n = np.bincount(codes, y)[codes], np.bincount(codes)[codes]
    u = features()["uses"]
    young = u[u.eligible & (u.agebin == "young") & decided(k)[u.i.to_numpy()]]
    j = pd.Series(np.arange(len(d)), index=d.index)[young.i].to_numpy()

    def premia(yv: np.ndarray) -> pd.DataFrame:
        r = np.where(n > 1, yv - (s - yv) / np.maximum(n - 1, 1), np.nan)[j]
        ok = np.isfinite(r)
        return pd.Series(r[ok]).groupby(young.keyword.to_numpy()[ok]).agg(["size", "mean", "var"])

    obs = premia(y)
    obs = obs[obs["size"] >= PREMIUM_MIN]
    dl = pooled_dl(obs)
    null = np.array([pooled_dl(premia(within_cell_permutation(y, codes, rng)).reindex(obs.index))["tau"]
                     for _ in range(perms)])
    kw = features()["keywords"]
    t = pd.DataFrame({"keyword": obs.index, "young_uses": obs["size"].to_numpy(), "premium": obs["mean"].to_numpy(),
                      "se": np.sqrt(dl["pooled_var"] / obs["size"].to_numpy()), "posterior_mean": dl["post_mean"],
                      "posterior_sd": dl["post_sd"]})
    t = t.join(kw[["onset", "papers", "big"]], on="keyword")
    t = t.sort_values(["posterior_mean", "premium"], ignore_index=True)
    big = t.big.astype(bool)
    summary = {"keywords": dl["K"], "tau": dl["tau"], "mu": dl["mu"], "Q": dl["Q"], "I2": dl["I2"],
               "pooled_sd_r": float(np.sqrt(dl["pooled_var"])),
               "share_posterior_positive": float((t.posterior_mean > 0).mean()), "tau_null_mean": float(null.mean()),
               "tau_null_p95": float(np.quantile(null, 0.95)), "tau_p_permutation": float((1 + (null >= dl["tau"]).sum())
                                                                                     / (1 + len(null))),
               "permutations": perms,
               "survivorship": {"mean_premium_keywords_with_100_papers": float(t.premium[big].mean()),
                                "mean_premium_all": float(t.premium.mean()),
                                "mean_premium_other": float(t.premium[~big].mean()),
                                "keywords_with_100_papers": int(big.sum()),
                                "note": "hindsight: the 100-paper status is known only later; descriptive"}}
    return t, summary


def robustness(k: pd.DataFrame) -> pd.DataFrame:
    """A1-A3 (and the momentum-only keyword-FE model, Model B with 2022) under each declared variant; nominal p."""
    rows = []
    variants = {"censored keywords dropped": {"rows": lambda r: ~r.censored},
                "2-year momentum (2020-2026)": {"state": "state2"},
                "2022-2026": {"years": range(2022, 2027)},
                "early-map topic x year FE": {"fes": ("cell_early",), "clusters": ("keyword", "topic_early")},
                "no earlier version": {"rows": lambda r: r.has_earlier_version == 0}}
    for name, kw in variants.items():
        f, _ = model_a(k, **kw)
        rows += [{"variant": name, "test": t, **f.lincom(c)} for t, c in A_TESTS.items()]
    r = stack(k, decided(k)).assign(w1=1.0)
    f = fit(r, "accepted", DUMMIES + CONTROLS, w="w1")
    rows += [{"variant": "unweighted rows", "test": t, **f.lincom(c)} for t, c in A_TESTS.items()]
    f = fe_logit_w(r, "accepted", DUMMIES + CONTROLS)
    rows += [{"variant": "weighted FE logit (log-odds)", "test": t, **f.lincom(c)} for t, c in A_TESTS.items()]
    r = r.assign(m_falling=(r.mom == "falling").astype(float), m_rising=(r.mom == "rising").astype(float))
    f = fit(r, "accepted", ["m_rising", "m_falling"] + CONTROLS, fes=("keyword", "cell"))
    rows += [{"variant": "keyword FE + topic x year FE, momentum only", "test": t, **f.lincom({c: 1.0})}
             for t, c in [("rising - flat", "m_rising"), ("falling - flat", "m_falling")]]
    f, _ = model_b(k, (2019, 2020, 2022, 2023, 2024, 2025, 2026))
    rows += [{"variant": "Model B with 2022", "test": t, **f.lincom(c)} for t, c in B_TESTS.items()]
    return pd.DataFrame(rows)


def off_trend(k: pd.DataFrame) -> dict:
    """Descriptive: decided papers 2019-2026 with no eligible keyword vs with one (raw and within topic x year)."""
    d = k[decided(k)].assign(off=(features()["papers"].n_eligible.to_numpy()[decided(k)] == 0).astype(float))
    d = d.assign(i=np.arange(len(d)), w=1.0)
    f = fit(d, "accepted", ["off"] + CONTROLS, clusters=("topic",))
    return {"papers_off_trend": int(d.off.sum()), "papers_on_trend": int((d.off == 0).sum()),
            "rate_off_trend": float(d.accepted[d.off == 1].mean()), "rate_on_trend": float(d.accepted[d.off == 0].mean()),
            "within_topic_year_difference": f.lincom({"off": 1.0})}


# ---------------------------------------------------------------------------------------------------- outcome-free
def free_part(k: pd.DataFrame) -> dict:
    """State shares by year, P(state | first-time team), diffusion lags of the big keywords (no outcome)."""
    u, kw = features()["uses"], features()["keywords"]
    r = stack(k, k.year.isin(YEARS).to_numpy())
    g = r.groupby(["year", "state"]).agg(uses=("w", "size"), weighted_papers=("w", "sum")).reset_index()
    g["share_weighted"] = g.weighted_papers / g.groupby("year").weighted_papers.transform("sum")
    g["share_uses"] = g.uses / g.groupby("year").uses.transform("sum")
    g["name"] = g.state.map(NAMED).fillna("")
    shares = g
    p = stack(k, (k.year.isin(PROFILE_YEARS) & k.first_time.notna()).to_numpy())
    lpm = []
    for s in STATES:
        f = fit(p.assign(y=(p.state == s).astype(float)), "y", ["first_time"])
        raw = {lab: wmean((p.state == s).astype(float)[p.first_time == v], p.w[p.first_time == v])
               for lab, v in [("share_first_time", 1.0), ("share_returning", 0.0)]}
        lpm.append({"state": s, "name": NAMED.get(s, ""), **raw, **f.lincom({"first_time": 1.0})})
    lpm = pd.DataFrame(lpm)
    lpm["q_bh"] = ph5_common.bh(lpm.p)
    big = u[u.big]
    arr = arrivals(big, "area", ARRIVAL).rename("arrival").reset_index()
    arr = arr.join(kw[["onset", "censored"]], on="keyword")
    arr["lag"] = arr.arrival - arr.onset
    cat = pd.read_csv(TOPICS / "topic_catalog.csv", keep_default_na=False)
    names = cat[cat.level == "coarse"].set_index("topic").name
    unc = arr[~arr.censored]
    areas = pd.DataFrame({"keywords_arrived": arr.groupby("area").size(),
                          "median_lag_all": arr.groupby("area").lag.median(),
                          "median_lag_uncensored_onset": unc.groupby("area").lag.median(),
                          "keywords_arrived_uncensored_onset": unc.groupby("area").size()}).reset_index()
    areas["area_name"] = areas.area.map(names)
    areas["share_of_big_keywords_arrived"] = areas.keywords_arrived / int(kw.big.sum())
    areas = areas.sort_values("median_lag_uncensored_onset", ignore_index=True)
    c = u[u.big & u.global_late & u.year.isin(YEARS)]
    mixed = c.groupby(["keyword", "year"]).le3.agg(["min", "max"])
    mixed = int(((mixed["min"] == 0) & (mixed["max"] == 1)).sum())
    counts = r.groupby("state").agg(uses=("w", "size"), papers=("i", "nunique"), keywords=("keyword", "nunique"))
    summary = {"vocabulary": int(len(kw)), "keywords_with_onset": int(kw.onset.notna().sum()),
               "censored_keywords": int(kw.censored.sum()), "big_keywords": int(kw.big.sum()),
               "eligible_uses_2019_2026": int(len(r)), "papers_with_eligible_keyword_2019_2026": int(r.i.nunique()),
               "uses_by_state": counts.reset_index().to_dict("records"),
               "model_c_rows_any_outcome": {"rows": int(len(c)), "locally_early": int((c.le3 == 1).sum()),
                                            "mixed_keyword_year_cells": mixed},
               "median_lag_uncensored_onset": float(unc.lag.median()),
               "note": "outcome-free (any outcome): keywords, topics, author IDs only"}
    return {"free_state_shares": shares, "free_profile_states": lpm, "free_diffusion_lags": arr,
            "free_area_lags": areas, "free_summary": summary}


def compute_free() -> dict:
    """Outcome-free parts on the real discovery data (no outcome column is loaded)."""
    return free_part(prepare(panel.frame("k100")))


# ---------------------------------------------------------------------------------------------------- gated run
def compute(k: pd.DataFrame, n_ref: int = N_REF) -> dict:
    k = prepare(k)
    tests, fits, omni = declared(k)
    (fa, ra), (fb, rb), (fc, rc) = fits["A"], fits["B"], fits["C"]
    ref = reference(k, n_ref)
    omni["p_calibrated"] = float((1 + (ref.F >= omni["F"]).sum()) / (1 + len(ref)))
    omni.update({"null_F_median": float(ref.F.median()), "null_F_95pct": float(ref.F.quantile(0.95)),
                 "null_frames": int(len(ref)), "nominal_size_in_null_frames": float((ref.p_nominal < 0.05).mean())})
    for t, dof, tstat in zip(tests.test, tests.dof, tests.coef / tests.se):
        mult = stats.t.ppf(0.975, dof) + stats.t.ppf(0.80, dof)
        tests.loc[tests.test == t, "mde80_sim"] = mult * float(ref[f"{t}_coef"].std(ddof=1))
        tests.loc[tests.test == t, "size_in_null_frames"] = float((ref[f"{t}_p"] < 0.05).mean())
        tests.loc[tests.test == t, "p_null_frames"] = float((1 + (ref[f"{t}_t"].abs() >= abs(tstat)).sum())
                                                            / (1 + len(ref)))
    states = state_rows(fa, ra, "A") + state_rows(fb, rb, "B established") + state_rows(fb, rb, "B no acceptance", na=True)
    for y in ("s9_accepted", "withdrawn_after_review"):
        f, r = model_a(k, pop="s9", y=y)
        states += state_rows(f, r, f"risk {y}", y=y)
        for t, c in A_TESTS.items():
            tests = pd.concat([tests, pd.DataFrame([{"family": "risk (nominal)", "test": f"{t} {y}", **f.lincom(c)}])],
                              ignore_index=True)
    cells, cells_summary = profile_cells(k)
    premia, premia_summary = keyword_premia(k, np.random.default_rng(SEED), PERMS)
    summary = {"population": "RQ3 decided papers with an eligible trend keyword, 2019-2026 (Model B and profile cells: "
                             "2019-20 and 2023-26)", "papers_model_a": fa.papers, "rows_model_a": fa.rows,
               "papers_model_b": fb.papers, "papers_model_c": fc.papers, "rows_model_c": fc.rows,
               "no_acceptance_share_model_b": float(np.average(rb.no_acc, weights=rb.w)),
               "omnibus": omni, "mainstream_rate": wmean(ra.accepted[ra.state == REF], ra.w[ra.state == REF]),
               "profile_cells": cells_summary, "model_d": premia_summary, "off_trend": off_trend(k), "note": NOTE}
    return {"tests": tests, "state_effects": pd.DataFrame(states), "profile_cells": cells,
            "local_early": local_early(k, fc, rc), "keyword_premia": premia, "robustness": robustness(k),
            "reference_null": ref, **free_part(k), "summary": summary}


# ---------------------------------------------------------------------------------------------------- calibration
BASE_RATES = dict(zip(range(2017, 2027), np.linspace(0.45, 0.32, 10)))     # mirrors ph5_common.fake_outcomes
PLANT = 0.3


def _paper_flag(k: pd.DataFrame, col: str) -> np.ndarray:
    f = features()["papers"]
    assert (f.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    return f[col].to_numpy(float)


PLANTS: dict[str, Callable[[pd.DataFrame], np.ndarray] | None] = {
    "null": None,
    "timing": lambda k: PLANT * (_paper_flag(k, "all_emerging") - _paper_flag(k, "all_cooling")),
    "local": lambda k: PLANT * _paper_flag(k, "has_local_early")}


def true_prob(k: pd.DataFrame, plant: Callable[[pd.DataFrame], np.ndarray] | None) -> np.ndarray:
    eta = logit(k.year.map(BASE_RATES).fillna(0.4).to_numpy(float))
    return expit(eta if plant is None else eta + plant(k))


def calibrate(n_null: int = 200, n_planted: int = 50, seed: int = 0) -> dict:
    """Declared tests on simulated frames: null, 'timing' (+0.3 log-odds if all of a paper's eligible keywords are
    Emerging, -0.3 if all are Cooling) and 'local' (+0.3 with a locally-early Model C row). Per plant and test:
    rejection at 0.05 (raw, Holm), mean estimate, target (the same estimator on the true probabilities, same rows),
    bias, SD and 95% CI coverage; per family the any-Holm rejection; omnibus size: nominal F and calibrated against
    the other null frames (leave-one-out), power of the calibrated omnibus in planted frames."""
    rows, omni = [], []
    for j, (name, plant) in enumerate(PLANTS.items()):
        for i in range(n_null if plant is None else n_planted):
            s = seed + 10_000 * j + i
            k = prepare(ph5_common.simulated_frame(s, plant))
            res, _, om = declared(k)
            target, _, _ = declared(k.assign(accepted=np.where(k.rq3, true_prob(k, plant), np.nan)))
            rows += [{"plant": name, "frame": s, **r, "target": t} for r, t in zip(res.to_dict("records"), target.coef)]
            omni.append({"plant": name, "frame": s, "F": om["F"], "p_nominal": om["p_nominal"]})
    r = pd.DataFrame(rows)
    r["reject"], r["reject_holm"] = r.p < 0.05, r.p_holm < 0.05
    r["covered"] = (r.ci95_lo <= r.target) & (r.target <= r.ci95_hi)
    per_test = (r.groupby(["plant", "test"], sort=False)
                .agg(frames=("p", "size"), reject=("reject", "mean"), reject_holm=("reject_holm", "mean"),
                     mean_coef=("coef", "mean"), sd_coef=("coef", "std"), mean_se=("se", "mean"),
                     mean_target=("target", "mean"), coverage=("covered", "mean"), mean_mde80=("mde80", "mean"))
                .reset_index())
    per_test["bias"] = per_test.mean_coef - per_test.mean_target
    fam = r.groupby(["plant", "family", "frame"]).reject_holm.any().groupby(["plant", "family"]).mean()
    o = pd.DataFrame(omni)
    nullF = o.F[o.plant == "null"].to_numpy()
    o["p_calibrated"] = [(1 + (nullF >= F).sum() - (pl == "null")) / (len(nullF) + (pl != "null"))
                         for F, pl in zip(o.F, o.plant)]
    o["reject_nominal"], o["reject_calibrated"] = o.p_nominal < 0.05, o.p_calibrated < 0.05
    om = o.groupby("plant", sort=False).agg(frames=("F", "size"), reject_nominal=("reject_nominal", "mean"),
                                            reject_calibrated=("reject_calibrated", "mean"),
                                            median_F=("F", "median")).reset_index()
    return {"per_test": per_test.to_dict("records"),
            "family_any_holm_rejection": [{"plant": p, "family": f, "rate": float(v)} for (p, f), v in fam.items()],
            "omnibus": om.to_dict("records"), "n_null": n_null, "n_planted": n_planted, "seed": seed,
            "plant_log_odds": PLANT}


# ---------------------------------------------------------------------------------------------------- figures
def _save(fig, out_dir: Path, name: str) -> None:
    import figures
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out_dir / f"{name}.png", dpi=220, bbox_inches="tight")
    figures.plt.close(fig)


def _heatmap(ax, g: pd.DataFrame, lim: float, title: str):
    import figures
    g = g.set_index("state")
    Z = np.array([[g.coef[f"{a}_{m}"] * 100 for m in MOMS] for a in AGES])
    im = ax.imshow(Z, cmap=figures.DIVERGING, vmin=-lim, vmax=lim, aspect="auto")
    ax.grid(False)
    for i, a in enumerate(AGES):
        for j, m in enumerate(MOMS):
            x = g.loc[f"{a}_{m}"]
            name = f"{x['name']}\n" if isinstance(x["name"], str) and x["name"] else ""
            ci = f"[{x.ci95_lo * 100:+.1f}, {x.ci95_hi * 100:+.1f}]"
            body = "reference" if f"{a}_{m}" == REF else f"{x.coef * 100:+.1f} pp\n{ci}"
            ax.text(j, i, f"{name}{body}\nn={int(x.uses):,}", ha="center", va="center", fontsize=6.3, color=figures.INK)
    ax.set_xticks(range(3), ["falling", "flat", "rising"])
    ax.set_yticks(range(3), ["young (1-2 y)", "middle (3-4 y)", "old (>= 5 y)"])
    ax.set_xlabel("momentum (within-year tercile of growth)")
    ax.set_title(title, loc="left")
    for s in ax.spines.values():
        s.set_visible(False)
    return im


def plot(out_dir: Path) -> None:
    import figures
    from matplotlib.colors import LinearSegmentedColormap
    plt = figures.plt
    out_dir = Path(out_dir)
    st = pd.read_csv(out_dir / "state_effects.csv", keep_default_na=False, na_values=[""])
    summary = json.loads((out_dir / "summary.json").read_text())["summary"]

    a = st[st.model == "A"]
    lim = float(np.nanmax(np.abs(a.coef))) * 100 or 1.0
    fig, ax = plt.subplots(figsize=(5.0, 3.6), constrained_layout=True)
    im = _heatmap(ax, a, lim, "Acceptance vs Mainstream keywords, same topic x year (pp, 95% CI)")
    fig.colorbar(im, ax=ax, shrink=0.7, label="pp vs Mainstream")
    om = summary["omnibus"]
    fig.suptitle(f"PH5 kwtiming (post hoc, exploratory). Omnibus F = {om['F']:.2f}, calibrated p = "
                 f"{om['p_calibrated']:.3f}; n = keyword uses", x=0.01, ha="left", fontsize=7)
    _save(fig, out_dir, "PH5_kwtiming_states")

    b = st[st.model.str.startswith("B")]
    lim = float(np.nanmax(np.abs(b.coef))) * 100 or 1.0
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.5), constrained_layout=True)
    for ax, (model, title) in zip(axes, [("B no acceptance", "Teams with no earlier ICLR acceptance"),
                                         ("B established", "Established teams")]):
        im = _heatmap(ax, b[b.model == model], lim, title)
    axes[1].set_yticks([])
    fig.colorbar(im, ax=axes, shrink=0.7, label="pp vs Mainstream (same profile)")
    fig.suptitle("Lifecycle-state effects by track record (2019-20, 2023-26; post hoc, exploratory)", x=0.01, ha="left",
                 fontsize=7.5)
    _save(fig, out_dir, "PH5_kwtiming_profiles")

    le = pd.read_csv(out_dir / "local_early.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.2), constrained_layout=True, gridspec_kw={"width_ratios": [1.6, 1]})
    ax = axes[0]
    g = le[le.block.isin(["C main", "C by global age", "C importer", "C robustness"]) & le.coef.notna()]
    y = np.arange(len(g))[::-1]
    colour = np.where(g.block == "C main", figures.SERIES[0], figures.MUTED)
    ax.axvline(0, color=figures.INK2, lw=0.7)
    ax.hlines(y, g.ci95_lo * 100, g.ci95_hi * 100, color=colour, lw=1.6)
    ax.scatter(g.coef * 100, y, s=22, c=colour, edgecolor=figures.SURFACE, linewidth=1, zorder=3)
    ax.set_yticks(y, [f"{bl[2:]}: {lab}".replace("main: ", "").replace("_", " ") for bl, lab in zip(g.block, g.label)],
                  fontsize=6.3)
    ax.set_xlabel("locally early minus locally late, pp (95% CI)")
    ax.set_title("Globally late keyword, early in the paper's own area\n(same keyword x year, same topic x year)", loc="left")
    ax = axes[1]
    grid = le[le.block == "C grid"]
    Z = grid.rate.to_numpy().reshape(2, 2) * 100
    ramp = LinearSegmentedColormap.from_list("light", figures.BLUE_RAMP[:3])
    ax.imshow(Z, cmap=ramp, vmin=np.nanmin(Z), vmax=np.nanmax(Z), aspect="auto")
    ax.grid(False)
    for i in range(2):
        for j in range(2):
            x = grid.iloc[2 * i + j]
            ax.text(j, i, f"{Z[i, j]:.1f}%\nn={int(x.rows):,}", ha="center", va="center", fontsize=7, color=figures.INK)
    ax.set_xticks(range(2), ["locally early", "locally late"])
    ax.set_yticks(range(2), ["global age 3-4", "global age >= 5"])
    ax.set_title("Raw acceptance (weighted)", loc="left")
    for s in ax.spines.values():
        s.set_visible(False)
    fig.suptitle("PH5 kwtiming Model C (post hoc, exploratory)", x=0.01, ha="left", fontsize=7.5)
    _save(fig, out_dir, "PH5_kwtiming_local")

    kp = pd.read_csv(out_dir / "keyword_premia.csv").sort_values(["posterior_mean", "premium"])
    md = summary["model_d"]
    fig, ax = plt.subplots(figsize=(5.4, max(3.0, 0.085 * len(kp) + 1.0)), constrained_layout=True)
    y = np.arange(len(kp))
    ax.axvspan((md["mu"] - 1.96 * md["tau"]) * 100, (md["mu"] + 1.96 * md["tau"]) * 100, color=figures.GRID, lw=0,
               label="mu +- 1.96 tau")
    ax.axvline(0, color=figures.INK2, lw=0.7)
    ax.scatter(kp.premium * 100, y, s=8, facecolor="none", edgecolor=figures.MUTED, linewidth=0.6, label="raw premium")
    ax.hlines(y, (kp.posterior_mean - 1.96 * kp.posterior_sd) * 100, (kp.posterior_mean + 1.96 * kp.posterior_sd) * 100,
              color=figures.SERIES[0], lw=0.9)
    ax.scatter(kp.posterior_mean * 100, y, s=10, color=figures.SERIES[0], zorder=3, label="EB posterior (95%)")
    ax.set_yticks(y, kp.keyword, fontsize=4.6)
    ax.set_xlabel("young-stage uses: acceptance minus leave-one-out topic x year mean (pp)")
    ax.set_title(f"Early-entry premium by keyword: tau = {md['tau'] * 100:.1f} pp (permutation null mean "
                 f"{md['tau_null_mean'] * 100:.1f}, p = {md['tau_p_permutation']:.2f}); {md['keywords']} keywords",
                 loc="left", fontsize=7)
    ax.legend(loc="lower right", fontsize=6.3)
    _save(fig, out_dir, "PH5_kwtiming_premia")

    sh, pr = pd.read_csv(out_dir / "free_state_shares.csv"), pd.read_csv(out_dir / "free_profile_states.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.0), constrained_layout=True)
    ax = axes[0]
    for j, (s, name) in enumerate(NAMED.items()):
        g = sh[sh.state == s]
        ax.plot(g.year, g.share_weighted * 100, color=figures.SERIES[j], marker="o", ms=3, label=name)
    ax.set_ylabel("share of eligible keyword uses (%, paper-weighted)")
    ax.set_title("Lifecycle state of listed trend keywords, all submissions\n(named states; 4 others not drawn)", loc="left")
    ax.legend(fontsize=6.3)
    ax = axes[1]
    y = np.arange(len(pr))[::-1]
    ax.axvline(0, color=figures.INK2, lw=0.7)
    ax.hlines(y, pr.ci95_lo * 100, pr.ci95_hi * 100, color=figures.SERIES[0], lw=1.4)
    ax.scatter(pr.coef * 100, y, s=18, color=figures.SERIES[0], edgecolor=figures.SURFACE, linewidth=1, zorder=3)
    ax.set_yticks(y, [f"{s} ({n})" if isinstance(n, str) and n else s for s, n in zip(pr.state, pr.name.fillna(""))],
                  fontsize=6.5)
    ax.set_xlabel("first-time minus returning teams, pp (95% CI)")
    ax.set_title("Which states do first-time teams enter?\n(share of uses, same topic x year; 2019-20, 2023-26)", loc="left")
    _save(fig, out_dir, "PH5_kwtiming_free")
