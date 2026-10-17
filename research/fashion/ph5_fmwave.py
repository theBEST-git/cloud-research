"""PH5 fmwave (final post hoc round, selection S2): riding the foundation-model wave. Within topic x year, how does the
acceptance premium of foundation-model (FM) papers change with the topic's FM adoption in the previous year, does the
curve differ by author track record, and does naming the FM up front add anything? Post hoc and exploratory: every
estimate is an association within topic x year; Holm within each declared family ranks the evidence, nothing more.

Variables (outcome-free, built on every discovery submission):
  fm          the paper builds on a foundation model (LLM label)
  adoption    the k100 topic's FM share in t - 1 (panel fm_adoption); ladopt = logit(clip(adoption, 0.02, 0.98));
              l = ladopt - c, c = mean ladopt of the primary population's FM papers; bins 0-5, 5-15, 15-30, 30-50, >= 50%
  framed      the title or the first abstract sentence (SENTENCE_END) matches FRAMING (frozen, case-insensitive)
  first_time  no author ID with an earlier discovery submission (descriptive only)
  established some author ID had an accepted ICLR paper in an earlier year (posthoc.established_authors; gated)
  no_acc      the paper has an author ID and no established author
Population: RQ3 decided papers 2023-2026 with a prior-year adoption.
Models: LPM, topic x year FE absorbed, CR1 SE by k100 topic with t(G - 1); two-way (topic, early-map topic) SE as a
check. Controls X = class (ref. method) + log2 team size + newcomer + has_earlier_version.
  F1 bins     accepted ~ sum_b fm x 1[bin b] + X                                          (descriptive)
  F1 linear   accepted ~ fm + fm x l + X; crossing a* = expit(c - b_fm / b_fm_l) with a 999-draw topic cluster
              bootstrap (percentile CI; 'not reached in range' unless a* and both CI ends lie in [2%, 98%])
  F1 spline   accepted ~ fm + fm x ladopt + fm x RCS(ladopt; knots at the 10/50/90th pct among FM papers) + X (figure)
  F2 profile  papers with an author ID: accepted ~ fm + fm x l + fm x no_acc + fm x l x no_acc + no_acc + no_acc x l + X
  F3 framing  FM papers only: accepted ~ framed + framed x l + X
  P0          code-link share (github.com, not /anonymous) of accepted minus rejected abstracts by year; a paper-weighted
              mean over 2023-2026 above 3 pp labels F3 'possibly contaminated by camera-ready edits'
Declared tests, Holm within each family:
  F-A  A1 slope of the FM premium per logit unit of adoption (b_fm_l); A2 FM premium in the >= 50% bin
  F-B  B1 no_acc minus established FM premium at 10% adoption; B2 no_acc minus established slope
  F-C  C1 framing premium among FM papers at l = 0; C2 its slope in ladopt
The FM premium (fm) is common to all years, so A1 compares adoption levels both across topics within a year and across
years; a calendar trend in the FM premium would load on it. The fm x year variant identifies the slopes within year.
Robustness (declared tests re-estimated, same centre c): 2024-2026; fm x year and framed x year dummies (A and C;
centred at the FM / framed FM papers' year mix); era-specific curves 2019-23 vs 2024-26; early-map adoption with
early-map topic x year FE (CR1 by early topic, two-way with k100 topic); fm x coarse-area dummies (A; centred at the FM
papers' area mix); topics with >= 30 papers in t - 1; the second-pass FM label (fm and adoption rebuilt); logit with
topic x year dummies (log-odds); s9_accepted on the S9 population; without the primary area 'foundation or
frontier models' (2025-26).
Outcome-free (compute_free; also inside compute): FM share by adoption bin and year (all submissions 2019-2026), and who
brings FMs into low-adoption topics: fm ~ first_time x bin + newcomer x bin + class + log2 team | topic x year, all
submissions 2023-2026 with an author ID (first_time is nested in newcomer: its terms compare first-time with returning
topic newcomers, the newcomer terms compare returning newcomers with topic incumbents).
"""
from __future__ import annotations

import json
import re
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
from common import TOPICS, topic_layer
from logit import fe_logit
from ols import demean
from panel import CLASS_CONTROLS
from variables import load_authors
from variants import holm

YEARS = (2023, 2026)
ERAS = {"2019-2023": (2019, 2023), "2024-2026": (2024, 2026)}
CLIP = (0.02, 0.98)
EDGES = np.array([0.05, 0.15, 0.30, 0.50])
BINS = ["0-5%", "5-15%", "15-30%", "30-50%", ">=50%"]
FM_BINS = [f"fm_b{j}" for j in range(len(BINS))]
CONTROLS = CLASS_CONTROLS + ["log2_team", "newcomer", "has_earlier_version"]
FRAMING = re.compile(r"\b(LLMs?|large language models?|language models?|foundation models?|VLMs?|vision[- ]language "
                     r"models?|MLLMs?|multimodal (large )?language models?|GPT[- ]?\w*|ChatGPT|LLaMA\w*)\b", re.I)
SENTENCE_END = re.compile(r"(?<=[.!?])(?<!\be\.g\.)(?<!\bi\.e\.)(?<!\bal\.)(?<!\bvs\.)(?<!\bcf\.)\s+(?=[A-Z0-9(\[])")
CODE_LINK = re.compile(r"github\.com(?!/anonymous)", re.I)
FM_AREA = "foundation or frontier models"
CONTAMINATION = 0.03
REF_ADOPTION = 0.10
MIN_PAPERS_PREV = 30
MIN_SHARE_CELL = 30                                                       # figure: bin x year cells drawn
BOOT, SEED = 999, 20261017
GRID = np.linspace(logit(CLIP[0]), logit(CLIP[1]), 61)
NOTE = "post hoc exploratory (PH5 fmwave, selection S2); associations within topic x year, not causal effects"


def ladopt(a) -> np.ndarray:
    return logit(np.clip(np.asarray(a, float), *CLIP))


def prior_share(topic: pd.Series, year: pd.Series, x: pd.Series) -> np.ndarray:
    """Per paper: the mean of x over its topic's papers in t - 1 (NaN if the topic had none), as panel.fm_adoption."""
    m = pd.DataFrame({"topic": topic.to_numpy(), "year": year.to_numpy(), "x": x.to_numpy(float)})
    prev = m.groupby(["topic", "year"]).x.mean()
    return prev.reindex(pd.MultiIndex.from_arrays([m.topic, m.year - 1])).to_numpy()


def first_sentence(text: str) -> str:
    return SENTENCE_END.split(text.strip(), maxsplit=1)[0]


@lru_cache(maxsize=1)
def features() -> pd.DataFrame:
    """Outcome-free paper features in panel.frame('k100') row order (cached; do not mutate)."""
    k = panel.frame("k100").reset_index(drop=True)
    corpus = topic_layer().embedded_corpus()
    assert (corpus.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    f = pd.DataFrame({"submission_id": k.submission_id})
    titles, abstracts = corpus.title.fillna(""), corpus.abstract.fillna("")
    f["framed"] = [float(bool(FRAMING.search(t) or FRAMING.search(first_sentence(a)))) for t, a in zip(titles, abstracts)]
    f["code_link"] = abstracts.str.contains(CODE_LINK).astype(float).to_numpy()
    f["fm_primary_area"] = corpus.primary_area.fillna("").str.startswith(FM_AREA).to_numpy()
    a = load_authors(k.submission_id)[["submission_id", "key"]].merge(k[["submission_id", "year"]], on="submission_id")
    a["seen"] = a.key.map(a.groupby("key").year.min()) < a.year
    seen = a.groupby("submission_id").seen.any().reindex(k.submission_id).fillna(False).to_numpy(float)
    f["first_time"] = np.where(k.has_author_key, 1.0 - seen, np.nan)
    lab = pd.read_csv(TOPICS / "paper_contributions.csv.gz",
                      usecols=["submission_id", "foundation_model", "second_pass_foundation_model"])
    assert lab.submission_id.equals(k.submission_id)
    f["fm2"] = (lab.second_pass_foundation_model.fillna(lab.foundation_model) == "yes").astype(float).to_numpy()
    f["adoption2"] = prior_share(k.topic, k.year, f.fm2)
    early = panel.frame("early").reset_index(drop=True)
    assert early.submission_id.equals(k.submission_id)
    f["adoption_early"], f["cell_early"] = early.fm_adoption.to_numpy(), early.cell.to_numpy()
    return f


def prepare(k: pd.DataFrame) -> pd.DataFrame:
    """k with the features, area and log2 team (posthoc.add_columns) and, if k has outcomes, the author profile."""
    k = k.reset_index(drop=True)
    f = features()
    assert (f.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    k = posthoc.add_columns(k.assign(adoption=k.fm_adoption, **{c: f[c].to_numpy() for c in f.columns[1:]}))
    if "accepted" in k:
        est = posthoc.established_authors(k)
        k["established"] = est.astype(float)
        k["no_acc"] = np.where(k.has_author_key, 1.0 - est, np.nan)
    return k


def population(k: pd.DataFrame, years: tuple[int, int] = YEARS, flag: str = "rq3") -> pd.DataFrame:
    return k[k[flag].astype(bool) & k.year.between(*years) & k.adoption.notna()]


def rcs(x, t) -> np.ndarray:
    """Harrell's restricted cubic spline term for three knots t (linear beyond them), scaled by (t3 - t1)^2."""
    x, (t1, t2, t3) = np.asarray(x, float), t
    p = lambda u: np.clip(u, 0, None) ** 3                                     # noqa: E731
    return (p(x - t1) - p(x - t2) * (t3 - t1) / (t3 - t2) + p(x - t3) * (t2 - t1) / (t3 - t2)) / (t3 - t1) ** 2


def design(d: pd.DataFrame, centre: float, knots=None) -> pd.DataFrame:
    """Regressors built from d.fm, d.adoption, d.no_acc, d.framed and d.first_time (rows without adoption dropped)."""
    d = d[d.adoption.notna()].copy()
    d["ladopt"] = ladopt(d.adoption)
    d["l"] = d.ladopt - centre
    d["bin"] = np.searchsorted(EDGES, d.adoption.to_numpy(), side="right")
    fm = d.fm.to_numpy(float)
    d["fm_l"] = fm * d.l
    for j in range(len(BINS)):
        b = (d.bin == j).to_numpy(float)
        d[f"fm_b{j}"], d[f"framed_b{j}"] = fm * b, d.framed * b
    d["framed_l"] = d.framed * d.l
    if "no_acc" in d:
        na = d.no_acc.to_numpy(float)
        d["fm_na"], d["fm_l_na"], d["na_l"] = fm * na, fm * d.l * na, na * d.l
        for j in range(len(BINS)):
            d[f"fm_b{j}_est"], d[f"fm_b{j}_na"] = d[f"fm_b{j}"] * (1 - na), d[f"fm_b{j}"] * na
    ft = d.first_time.to_numpy(float)
    d["ft_l"] = ft * d.l
    for j in range(len(BINS)):
        d[f"fm_b{j}_ft"], d[f"fm_b{j}_ret"] = d[f"fm_b{j}"] * ft, d[f"fm_b{j}"] * (1 - ft)
    if knots is not None:
        d["fm_s1"], d["fm_s2"] = fm * d.ladopt, fm * rcs(d.ladopt, knots)
    return d


def _partial(d: pd.DataFrame, y: str, xs: list[str], absorb: str):
    """Complete cases, regressors with within-group variation, and the demeaned y and X."""
    d = d.dropna(subset=[y, *xs])
    g = pd.factorize(d[absorb])[0]
    yd, Xd = demean(d[y].to_numpy(float), g), demean(d[xs].to_numpy(float), g)
    keep = Xd.std(axis=0) > 1e-12                       # e.g. no earlier versions in a small subset: control drops out
    return d, [x for x, k_ in zip(xs, keep) if k_], Xd[:, keep], yd


@dataclass
class Fit:
    beta: pd.Series
    V: pd.DataFrame
    G: int
    n: int
    V2: pd.DataFrame | None = None                      # one-way by the second cluster
    Vt: pd.DataFrame | None = None                      # two-way (Cameron-Gelbach-Miller)
    G2: int = 0                                         # min(G, G2): the two-way t reference has G2 - 1 df

    def lincom(self, w: dict[str, float]) -> dict:
        """Estimate, CR1 SE, t(G - 1) p and 95% CI of sum w_j b_j; NaN if a term has no within-cell variation."""
        if not set(w) <= set(self.beta.index):
            return {"coef": np.nan, "se": np.nan, "p": np.nan, "ci95_lo": np.nan, "ci95_hi": np.nan, "n": self.n,
                    "clusters": self.G, "note": "term not identified: " + ";".join(sorted(set(w) - set(self.beta.index)))}
        c = pd.Series(w).reindex(self.beta.index).fillna(0.0).to_numpy()
        est, se = float(c @ self.beta.to_numpy()), float(np.sqrt(c @ self.V.to_numpy() @ c))
        q = stats.t.ppf(0.975, self.G - 1)
        out = {"coef": est, "se": se, "p": float(2 * stats.t.sf(abs(est / se), self.G - 1)), "ci95_lo": est - q * se,
               "ci95_hi": est + q * se, "n": self.n, "clusters": self.G}
        if self.Vt is not None:
            v = float(c @ self.Vt.to_numpy() @ c)
            v = v if v > 0 else max(se ** 2, float(c @ self.V2.to_numpy() @ c))
            out["se_twoway"] = float(np.sqrt(v))
            out["p_twoway"] = float(2 * stats.t.sf(abs(est) / np.sqrt(v), self.G2 - 1))
        return out


def fit(d: pd.DataFrame, y: str, xs: list[str], absorb: str = "cell", cluster: str = "topic",
        cluster2: str | None = None) -> Fit:
    """OLS with one absorbed FE (same estimator and CR1 factor as ols.fe_ols); optional two-way clustered vcov."""
    d, xs, Xd, yd = _partial(d, y, xs, absorb)
    inv = np.linalg.pinv(Xd.T @ Xd)
    beta = inv @ Xd.T @ yd
    e = yd - Xd @ beta
    n, k = Xd.shape

    def cr1(groups: np.ndarray) -> tuple[np.ndarray, int]:
        cg = pd.factorize(groups)[0]
        G = cg.max() + 1
        S = np.zeros((G, k))
        np.add.at(S, cg, Xd * e[:, None])
        return (G / (G - 1)) * ((n - 1) / (n - k)) * inv @ (S.T @ S) @ inv, int(G)

    V, G = cr1(d[cluster].to_numpy())
    out = Fit(pd.Series(beta, xs), pd.DataFrame(V, xs, xs), G, n)
    if cluster2:
        V2, G2 = cr1(d[cluster2].to_numpy())
        V12, _ = cr1(d[cluster].astype(str).to_numpy() + "|" + d[cluster2].astype(str).to_numpy())
        out.V2, out.Vt, out.G2 = pd.DataFrame(V2, xs, xs), pd.DataFrame(V + V2 - V12, xs, xs), min(G, G2)
    return out


def boot_betas(d: pd.DataFrame, y: str, xs: list[str], rng: np.random.Generator, draws: int = BOOT,
               absorb: str = "cell", cluster: str = "topic") -> tuple[list[str], np.ndarray]:
    """Cluster (topic) bootstrap of the FE-OLS coefficients. Cells nest in topics, so a resampled topic keeps its
    demeaned rows and each draw is a weighted sum of per-topic cross products (pseudo-inverse: a control absent from
    a draw gets 0 and leaves the other coefficients as if it were dropped)."""
    d, xs, Xd, yd = _partial(d, y, xs, absorb)
    cg = pd.factorize(d[cluster])[0]
    G = cg.max() + 1
    A = np.zeros((G, len(xs), len(xs)))
    b = np.zeros((G, len(xs)))
    np.add.at(A, cg, Xd[:, :, None] * Xd[:, None, :])
    np.add.at(b, cg, Xd * yd[:, None])
    w = rng.multinomial(G, np.full(G, 1 / G), size=draws).astype(float)
    return xs, (np.linalg.pinv(np.einsum("bg,gij->bij", w, A), hermitian=True)
                @ np.einsum("bg,gi->bi", w, b)[:, :, None])[:, :, 0]


def crossing(f: Fit, d: pd.DataFrame, centre: float, rng: np.random.Generator, y: str = "accepted") -> dict:
    """Adoption a* where the linear-in-logit FM premium is zero, with a percentile topic-bootstrap CI. Draws beyond
    the clip range are open ends: a CI end at 0 or 1 means the interval leaves [2%, 98%] on that side."""
    lo, hi = logit(CLIP[0]), logit(CLIP[1])
    point = centre - f.beta["fm"] / f.beta["fm_l"]
    xs, B = boot_betas(d, y, ["fm", "fm_l"] + CONTROLS, rng, BOOT)
    draws = centre - B[:, xs.index("fm")] / B[:, xs.index("fm_l")]
    draws = np.where(draws > hi, np.inf, np.where(draws < lo, -np.inf, draws))
    ci = np.quantile(draws, [0.025, 0.975], method="inverted_cdf")
    reached = bool(lo <= point <= hi and np.isfinite(ci).all())
    return {"a_star": float(expit(point)), "a_star_ci_lo": float(expit(ci[0])), "a_star_ci_hi": float(expit(ci[1])),
            "status": "crossing in range" if reached else "not reached in range",
            "range": list(CLIP), "share_draws_in_range": float(np.isfinite(draws).mean()),
            "share_draws_slope_negative": float((B[:, xs.index("fm_l")] < 0).mean()), "draws": len(draws)}


TESTS = [("F-A", "A1", "slope of the FM premium per logit unit of prior adoption"),
         ("F-A", "A2", "FM premium in topics with >= 50% prior adoption"),
         ("F-B", "B1", "no-acceptance minus established FM premium at 10% prior adoption"),
         ("F-B", "B2", "no-acceptance minus established slope per logit unit"),
         ("F-C", "C1", "framing premium among FM papers at the centre adoption"),
         ("F-C", "C2", "slope of the framing premium per logit unit")]


def declared(d: pd.DataFrame, centre: float, y: str = "accepted", absorb: str = "cell", cluster: str = "topic",
             cluster2: str | None = "topic_early", families: str = "ABC", extra: dict[str, list[str]] | None = None
             ) -> tuple[pd.DataFrame, dict[str, Fit]]:
    """The six declared tests (or the families asked for) with Holm within each family; d already has design().
    extra: additional regressors for the F1 ('A') or F3 ('C') models (robustness variants)."""
    kw, extra = {"absorb": absorb, "cluster": cluster, "cluster2": cluster2}, extra or {}
    fits, res = {}, {}
    if "A" in families:
        fits["F1_bins"] = fit(d, y, FM_BINS + extra.get("A", []) + CONTROLS, **kw)
        fits["F1_linear"] = fit(d, y, ["fm", "fm_l"] + extra.get("A", []) + CONTROLS, **kw)
        res["A1"], res["A2"] = fits["F1_linear"].lincom({"fm_l": 1}), fits["F1_bins"].lincom({"fm_b4": 1})
    if "B" in families:
        fits["F2"] = fit(d[d.has_author_key], y, ["fm", "fm_l", "fm_na", "fm_l_na", "no_acc", "na_l"] + CONTROLS, **kw)
        res["B1"] = fits["F2"].lincom({"fm_na": 1, "fm_l_na": float(ladopt(REF_ADOPTION)) - centre})
        res["B2"] = fits["F2"].lincom({"fm_l_na": 1})
    if "C" in families:
        fits["F3"] = fit(d[d.fm == 1], y, ["framed", "framed_l"] + extra.get("C", []) + CONTROLS, **kw)
        res["C1"], res["C2"] = fits["F3"].lincom({"framed": 1}), fits["F3"].lincom({"framed_l": 1})
    rows = pd.DataFrame([{"family": fam, "test": t, "label": lab, **res[t]} for fam, t, lab in TESTS if t in res])
    for fam, g in rows.groupby("family"):
        rows.loc[g.index, "p_holm"] = holm(g.p.fillna(1.0)).to_numpy()
    return rows, fits


def curve(f: Fit, terms: dict[str, Callable[[np.ndarray], np.ndarray]], model: str) -> list[dict]:
    """Pointwise premium sum_j b_j h_j(ladopt) over GRID with a 95% CI."""
    rows = []
    for x in GRID:
        r = f.lincom({t: float(h(np.array([x]))[0]) for t, h in terms.items()})
        rows.append({"model": model, "ladopt": x, "adoption": float(expit(x)), "coef": r["coef"], "se": r["se"],
                     "ci95_lo": r["ci95_lo"], "ci95_hi": r["ci95_hi"]})
    return rows


def bin_rows(f: Fit, d: pd.DataFrame, model: str, terms: list[str], member: pd.Series) -> list[dict]:
    """One row per adoption bin: coefficient of terms[j], the bin's position (median ladopt of member papers)."""
    rows = []
    for j, t in enumerate(terms):
        inb = d.bin == j
        pos = d.ladopt[inb & (member == 1)]
        rows.append({"model": model, "bin": BINS[j], "position": float(pos.median()) if len(pos) else np.nan,
                     "papers": int(inb.sum()), "member_papers": int((inb & (member == 1)).sum()), **f.lincom({t: 1})})
    return rows


def fm_share(k: pd.DataFrame) -> pd.DataFrame:
    """Outcome-free: FM share by prior-adoption bin and year, all submissions 2019-2026."""
    d = k[k.adoption.notna() & k.year.between(2019, 2026)]
    b = np.searchsorted(EDGES, d.adoption.to_numpy(), side="right")
    g = d.assign(bin=[BINS[j] for j in b]).groupby(["year", "bin"], sort=False).fm.agg(["size", "sum", "mean"])
    g = g.rename(columns={"size": "papers", "sum": "fm_papers", "mean": "fm_share"}).reset_index()
    return g.sort_values(["year", "bin"], key=lambda s: s.map(BINS.index) if s.name == "bin" else s, ignore_index=True)


def fm_entry(k: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Outcome-free: who brings FMs into low-adoption topics (LPM of fm | topic x year, CR1 by topic), and raw shares."""
    d = design(k[k.year.between(*YEARS) & k.has_author_key & k.adoption.notna()], centre=0.0)
    for j in range(len(BINS)):
        b = (d.bin == j).to_numpy(float)
        d[f"ft_b{j}"], d[f"nc_b{j}"] = d.first_time * b, d.newcomer * b
    terms = [f"{p}_b{j}" for p in ("ft", "nc") for j in range(len(BINS))]
    f = fit(d, "fm", terms + CLASS_CONTROLS + ["log2_team"])
    rows = [{"term": {"ft": "first_time (vs returning topic newcomer)", "nc": "topic newcomer (vs incumbent)"}[t[:2]],
             "bin": BINS[int(t[-1])], **f.lincom({t: 1})} for t in terms]
    prof = np.where(d.first_time == 1, "first_time", np.where(d.newcomer == 1, "returning_newcomer", "incumbent"))
    raw = (d.assign(profile=prof).groupby(["profile", "bin"]).fm.agg(["size", "mean"])
           .rename(columns={"size": "papers", "mean": "fm_share"}).reset_index())
    raw["bin"] = [BINS[j] for j in raw.bin]
    return pd.DataFrame(rows), raw


def free_part(k: pd.DataFrame) -> dict:
    entry, raw = fm_entry(k)
    share = fm_share(k)
    s = share[share.year.between(*YEARS)].groupby("bin").fm_papers.sum()
    return {"free_fm_share": share, "free_entry": entry, "free_entry_raw": raw,
            "free_summary": {"fm_papers_by_bin_2023_2026_all_submissions": {b: int(s.get(b, 0)) for b in BINS},
                             "note": "outcome-free (any outcome); FM labels, topics, authors only"}}


def compute_free() -> dict:
    """Outcome-free parts on the real discovery data (no outcome column is loaded)."""
    return free_part(prepare(panel.frame("k100")))


def code_links(k: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """P0: share of abstracts with a non-anonymous GitHub link, accepted minus rejected decided papers, by year."""
    d = k[k.rq3 & k.year.between(2019, 2026)]
    g = d.groupby(["year", "accepted"]).code_link.agg(["mean", "size"]).unstack("accepted")
    t = pd.DataFrame({"year": g.index, "share_accepted": g[("mean", 1.0)].to_numpy(),
                      "share_rejected": g[("mean", 0.0)].to_numpy(), "accepted_papers": g[("size", 1.0)].to_numpy(),
                      "rejected_papers": g[("size", 0.0)].to_numpy()})
    t["difference"] = t.share_accepted - t.share_rejected
    r = t[t.year.between(*YEARS)]
    pooled = float(np.average(r.difference, weights=r.accepted_papers + r.rejected_papers))
    return t, {"difference_2023_2026": pooled, "threshold": CONTAMINATION,
               "F3_label": "possibly contaminated by camera-ready edits" if pooled > CONTAMINATION else "no flag"}


def logit_rows(d: pd.DataFrame, d10: pd.DataFrame) -> list[dict]:
    """Logit variant of the declared tests: topic x year dummies (fe_logit; flat cells dropped), CR1 by topic, log-odds.
    d10 is d with l centred at logit(0.10), so B1 is the fm_na coefficient (B2 and the rest do not move)."""
    models = [("F-A", d, ["fm", "fm_l"], {"A1": "fm_l"}), ("F-A", d, FM_BINS, {"A2": "fm_b4"}),
              ("F-B", d10[d10.has_author_key], ["fm", "fm_l", "fm_na", "fm_l_na", "no_acc", "na_l"],
               {"B1": "fm_na", "B2": "fm_l_na"}),
              ("F-C", d[d.fm == 1], ["framed", "framed_l"], {"C1": "framed", "C2": "framed_l"})]
    rows = []
    for fam, dm, xs, tests in models:
        dd = dm.dropna(subset=["accepted", *xs, *CONTROLS]).reset_index(drop=True)
        X = dd[xs + CONTROLS].astype(float)
        X = X.loc[:, X.std() > 0]
        try:
            r, info = fe_logit(dd.accepted.astype(float), X, [dd.cell.rename("cell")], dd.topic)
        except (ValueError, RuntimeError, np.linalg.LinAlgError) as e:
            rows += [{"variant": "logit", "family": fam, "test": t, "coef": np.nan, "note": f"logit failed: {e}"}
                     for t in tests]
            continue
        for test, term in tests.items():
            x, q = r.loc[term], stats.t.ppf(0.975, r.loc[term, "clusters"] - 1)
            rows.append({"variant": "logit", "family": fam, "test": test, "coef": x.coef, "se": x.se, "p": x.p,
                         "ci95_lo": x.coef - q * x.se, "ci95_hi": x.coef + q * x.se, "n": int(x.n),
                         "clusters": int(x.clusters), "ame": x.ame,
                         "note": f"log-odds; {len(info['dropped_groups'])} flat cells dropped"})
    return rows


def centred_terms(d: pd.DataFrame, by: str, mult: str, at: pd.Series) -> tuple[pd.DataFrame, list[str]]:
    """d[mult] x (1[d[by] == v] - share of v among the rows `at`) for every level v of `by` but the first, so the other
    coefficients of the model stay at the `at` rows' mix of `by`."""
    levels = sorted(d[by].dropna().unique())[1:]
    cols = {f"{mult}_{by}_{v}": d[mult] * ((d[by] == v) - (d[by][at] == v).mean()) for v in levels}
    return d.assign(**cols), list(cols)


def year_terms(d: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, list[str]]]:
    """fm x year (F1) and framed x year (F3) dummies, centred at the FM and the framed FM papers' year mix: the slopes
    are then identified within year, and A2, C1 stay at the average year composition."""
    d, a = centred_terms(d, "year", "fm", d.fm == 1)
    d, c = centred_terms(d, "year", "framed", (d.fm == 1) & (d.framed == 1))
    return d, {"A": a, "C": c}


def robustness(k: pd.DataFrame, centre: float) -> pd.DataFrame:
    d = population(k)
    base = design(d, centre)
    da, area = centred_terms(base, "area", "fm", base.fm == 1)
    dy, year = year_terms(base)
    early = d.assign(adoption=d.adoption_early, cell=d.cell_early)
    variants = {"years_2024_2026": (design(population(k, (2024, 2026)), centre), {}),
                "fm_x_year": (dy, {"families": "AC", "extra": year}),
                "early_map": (design(early, centre), {"cluster": "topic_early", "cluster2": "topic"}),
                "fm_x_area": (da, {"families": "A", "extra": {"A": area}}),
                "papers_prev_ge30": (design(d[d.papers_prev >= MIN_PAPERS_PREV], centre), {}),
                "second_pass_fm": (design(d.assign(fm=d.fm2, adoption=d.adoption2), centre), {}),
                "s9": (design(population(k, YEARS, "s9"), centre), {"y": "s9_accepted"}),
                "without_fm_primary_area": (design(d[~d.fm_primary_area], centre), {})}
    parts = [declared(v, centre, **kw)[0].assign(variant=name) for name, (v, kw) in variants.items()]
    logit_ = pd.DataFrame(logit_rows(base, design(d, float(ladopt(REF_ADOPTION)))))
    res = pd.concat(parts + [logit_], ignore_index=True)
    for _, g in res.groupby(["variant", "family"]):
        res.loc[g.index, "p_holm"] = holm(g.p.fillna(1.0)).to_numpy()
    return res


def eras(k: pd.DataFrame, centre: float) -> pd.DataFrame:
    """2019-2026 with era-specific curves: fm, fm x l and fm x bin interacted with the era."""
    d = design(population(k, (2019, 2026)), centre)
    late = (d.year >= ERAS["2024-2026"][0]).to_numpy(float)
    cols = {}
    for e, w in [("early", 1 - late), ("late", late)]:
        for t in ["fm", "fm_l"] + FM_BINS:
            cols[f"{t}_{e}"] = d[t] * w
    d = d.assign(**cols)
    lin = fit(d, "accepted", [f"{t}_{e}" for e in ("early", "late") for t in ("fm", "fm_l")] + CONTROLS,
              cluster2="topic_early")
    bins = fit(d, "accepted", [f"{t}_{e}" for e in ("early", "late") for t in FM_BINS] + CONTROLS, cluster2="topic_early")
    rows = []
    for e, era in zip(("early", "late"), ERAS):
        rows.append({"era": era, "test": "A1", **lin.lincom({f"fm_l_{e}": 1})})
        rows.append({"era": era, "test": "A2", **bins.lincom({f"fm_b4_{e}": 1})})
        rows.append({"era": era, "test": "premium at centre", **lin.lincom({f"fm_{e}": 1})})
    rows.append({"era": "late minus early", "test": "A1", **lin.lincom({"fm_l_late": 1, "fm_l_early": -1})})
    fm = d[d.fm == 1]
    for era, (a, b) in ERAS.items():
        n = fm[fm.year.between(a, b)].bin.value_counts().reindex(range(len(BINS)), fill_value=0)
        rows.append({"era": era, "test": "FM papers by bin", "note": "; ".join(f"{BINS[j]}: {n[j]}" for j in n.index)})
    return pd.DataFrame(rows)


def compute(k: pd.DataFrame, boot_seed: int = SEED) -> dict:
    k = prepare(k)
    pop = population(k)
    centre = float(ladopt(pop.adoption[pop.fm == 1]).mean())
    knots = np.percentile(ladopt(pop.adoption[pop.fm == 1]), [10, 50, 90])
    assert np.all(np.diff(knots) > 0), "spline knots coincide"
    d = design(pop, centre, knots)
    tests, fits = declared(d, centre)
    spline = fit(d, "accepted", ["fm", "fm_s1", "fm_s2"] + CONTROLS)
    keyed = d[d.has_author_key]
    pbins = fit(keyed, "accepted", [f"fm_b{j}_{p}" for p in ("est", "na") for j in range(len(BINS))]
                + ["no_acc", "na_l"] + CONTROLS)
    ftbins = fit(keyed, "accepted", [f"fm_b{j}_{p}" for p in ("ret", "ft") for j in range(len(BINS))]
                 + ["first_time", "ft_l"] + CONTROLS)
    fm = d[d.fm == 1]
    fbins = fit(fm, "accepted", [f"framed_b{j}" for j in range(len(BINS))] + CONTROLS)
    one, lin = (lambda x: np.ones_like(x)), (lambda x: x - centre)
    curves = (curve(spline, {"fm": one, "fm_s1": lambda x: x, "fm_s2": lambda x: rcs(x, knots)}, "F1 spline")
              + curve(fits["F1_linear"], {"fm": one, "fm_l": lin}, "F1 linear")
              + curve(fits["F2"], {"fm": one, "fm_l": lin}, "F2 established")
              + curve(fits["F2"], {"fm": one, "fm_l": lin, "fm_na": one, "fm_l_na": lin}, "F2 no acceptance")
              + curve(fits["F3"], {"framed": one, "framed_l": lin}, "F3 framing"))
    terms = lambda p: [f"{p}{j}" if p.endswith("_b") else f"fm_b{j}_{p}" for j in range(len(BINS))]    # noqa: E731
    bins = (bin_rows(fits["F1_bins"], d, "F1", FM_BINS, d.fm)
            + bin_rows(pbins, keyed, "F2 established", terms("est"), keyed.fm * (1 - keyed.no_acc))
            + bin_rows(pbins, keyed, "F2 no acceptance", terms("na"), keyed.fm * keyed.no_acc)
            + bin_rows(ftbins, keyed, "first time (descriptive)", terms("ft"), keyed.fm * keyed.first_time)
            + bin_rows(fbins, fm, "F3 framing", terms("framed_b"), fm.framed))
    p0, p0_summary = code_links(k)
    tests["note"] = np.where(tests.family == "F-C", p0_summary["F3_label"], "")
    star = crossing(fits["F1_linear"], d, centre, np.random.default_rng(boot_seed))
    groups = {"FM papers": d.fm == 1, "FM, no acceptance": (d.fm == 1) & (d.no_acc == 1),
              "FM, established": (d.fm == 1) & (d.no_acc == 0), "FM, first time": (d.fm == 1) & (d.first_time == 1),
              "FM, framed": (d.fm == 1) & (d.framed == 1), "non-FM papers": d.fm == 0}
    counts = {name: {BINS[j]: int((m & (d.bin == j)).sum()) for j in range(len(BINS))} for name, m in groups.items()}
    summary = {"population": "RQ3 decided papers 2023-2026 with a prior-year adoption", "papers": int(len(d)),
               "fm_papers": int(d.fm.sum()), "papers_with_author_id": int(d.has_author_key.sum()),
               "no_acceptance_share": float(keyed.no_acc.mean()), "framed_share_of_fm": float(fm.framed.mean()),
               "centre_ladopt": centre, "centre_adoption": float(expit(centre)), "spline_knots_ladopt": knots.tolist(),
               "counts_by_bin": counts, "a_star": star, "P0_code_links": p0_summary,
               "premium_at": {f"{a:.0%}": fits["F1_linear"].lincom({"fm": 1, "fm_l": float(ladopt(a)) - centre})
                              for a in (0.02, 0.10, 0.25, 0.50, 0.75, 0.90)}, "note": NOTE}
    return {"tests": tests, "bins": pd.DataFrame(bins), "curves": pd.DataFrame(curves), "code_links": p0,
            "robustness": robustness(k, centre), "eras": eras(k, centre), **free_part(k), "summary": summary}


# ---------------------------------------------------------------------------------------------------- calibration
BASE_RATES = dict(zip(range(2017, 2027), np.linspace(0.45, 0.32, 10)))   # mirrors ph5_common.fake_outcomes
PLANTS: dict[str, Callable[[pd.DataFrame], np.ndarray] | None] = {
    "null": None,
    "fading": lambda k: 0.35 * (1 - np.nan_to_num(k.fm_adoption.to_numpy(float))) * k.fm.to_numpy(float),
    "constant": lambda k: 0.2 * k.fm.to_numpy(float),
    # calendar decline of the FM premium unrelated to adoption (+0.4 log-odds in 2023 to 0 in 2026): a confound for A1
    "calendar": lambda k: 0.4 * k.fm.to_numpy(float) * np.clip((2026 - k.year.to_numpy(float)) / 3, 0, 1)}


def true_prob(k: pd.DataFrame, plant: Callable[[pd.DataFrame], np.ndarray] | None) -> np.ndarray:
    eta = logit(k.year.map(BASE_RATES).fillna(0.4).to_numpy(float))
    return expit(eta if plant is None else eta + plant(k))


def calibrate(n_null: int = 200, n_planted: int = 50, seed: int = 0) -> dict:
    """Run the declared tests on simulated frames (null; fading, constant and calendar FM premium). Per plant and test:
    rejection rate at 0.05 (raw, Holm and two-way), mean estimate, mean target (the same LPM fitted to the true
    probabilities on the same sample), bias and 95% CI coverage of the target; per family the any-Holm-rejection rate;
    a* status shares and coverage (an open CI end is reported as 0 or 1). Families A and C are also run with the fm x
    year terms (tests suffixed ' fm_x_year')."""
    rows, stars = [], []
    for j, (name, plant) in enumerate(PLANTS.items()):
        for i in range(n_null if plant is None else n_planted):
            s = seed + 10_000 * j + i
            k = prepare(ph5_common.simulated_frame(s, plant))
            pop = population(k)
            centre = float(ladopt(pop.adoption[pop.fm == 1]).mean())
            d = design(pop, centre)
            dy, year = year_terms(d)
            for suffix, dd, kw in [("", d, {}), (" fm_x_year", dy, {"families": "AC", "extra": year})]:
                res, fits = declared(dd, centre, **kw)
                target, tfits = declared(dd.assign(accepted=true_prob(dd, plant)), centre, cluster2=None, **kw)
                rows += [{"plant": name, "frame": s, **r, "family": r["family"] + suffix, "test": r["test"] + suffix,
                          "target": t} for r, t in zip(res.to_dict("records"), target.coef)]
                if suffix:
                    continue
                st = crossing(fits["F1_linear"], d, centre, np.random.default_rng(s))
                ts = float(expit(centre - tfits["F1_linear"].beta["fm"] / tfits["F1_linear"].beta["fm_l"]))
                tc = 1.0 if ts > CLIP[1] else 0.0 if ts < CLIP[0] else ts             # open ends, as the draws
                stars.append({"plant": name, "status": st["status"], "a_star": st["a_star"], "target": ts,
                              "covered": bool(st["a_star_ci_lo"] <= tc <= st["a_star_ci_hi"])})
    r = pd.DataFrame(rows)
    r["reject"], r["reject_holm"], r["reject_twoway"] = r.p < 0.05, r.p_holm < 0.05, r.p_twoway < 0.05
    r["covered"] = (r.ci95_lo <= r.target) & (r.target <= r.ci95_hi)
    per_test = (r.groupby(["plant", "test"]).agg(frames=("p", "size"), reject=("reject", "mean"),
                                                 reject_holm=("reject_holm", "mean"),
                                                 reject_twoway=("reject_twoway", "mean"), mean_coef=("coef", "mean"),
                                                 mean_target=("target", "mean"), coverage=("covered", "mean"))
                .reset_index())
    per_test["bias"] = per_test.mean_coef - per_test.mean_target
    fam = r.groupby(["plant", "family", "frame"]).reject_holm.any().groupby(["plant", "family"]).mean()
    st = pd.DataFrame(stars)
    st["in_range"] = st.status == "crossing in range"
    star = st.groupby("plant").agg(frames=("status", "size"), in_range=("in_range", "mean"),
                                   median_a_star=("a_star", "median"), target=("target", "median"),
                                   coverage=("covered", "mean")).reset_index()
    return {"per_test": per_test.to_dict("records"),
            "family_any_holm_rejection": [{"plant": p, "family": f, "rate": float(v)} for (p, f), v in fam.items()],
            "a_star": star.to_dict("records"), "n_null": n_null, "n_planted": n_planted, "seed": seed}


# ---------------------------------------------------------------------------------------------------- figures
def plot(out_dir: Path) -> None:
    import figures
    plt = figures.plt
    out_dir = Path(out_dir)
    curves, bins = pd.read_csv(out_dir / "curves.csv"), pd.read_csv(out_dir / "bins.csv")
    summary = json.loads((out_dir / "summary.json").read_text())["summary"]
    ticks = [0.02, 0.05, 0.15, 0.3, 0.5, 0.75, 0.9, 0.98]

    def panel_(ax, model: str, bin_model: str, colour: str, title: str) -> list:
        c = curves[curves.model == model]
        ax.axhline(0, color=figures.INK2, lw=0.7)
        band = ax.fill_between(c.ladopt, c.ci95_lo * 100, c.ci95_hi * 100, color=colour, alpha=0.16, lw=0)
        (line,) = ax.plot(c.ladopt, c.coef * 100, color=colour, lw=1.6)
        b = bins[(bins.model == bin_model) & bins.position.notna()]
        dots = ax.errorbar(b.position, b.coef * 100, yerr=[(b.coef - b.ci95_lo) * 100, (b.ci95_hi - b.coef) * 100],
                           fmt="o", ms=4, color=figures.SERIES[1], mec=figures.SURFACE, lw=1, capsize=0, zorder=3)
        ax.set_xticks(logit(ticks), [f"{t:.0%}" for t in ticks], fontsize=6.8)
        ax.set_xlabel("topic's FM share in the previous year (logit scale)")
        ax.set_title(title, loc="left")
        return [(line, band), dots]

    fig, ax = plt.subplots(figsize=(5.2, 3.3), constrained_layout=True)
    handles = panel_(ax, "F1 spline", "F1", figures.SERIES[0],
                     "FM acceptance premium vs prior FM adoption, within topic x year")
    lin = curves[curves.model == "F1 linear"]
    handles += ax.plot(lin.ladopt, lin.coef * 100, color=figures.MUTED, lw=1.0, ls=(0, (3, 2)))
    star = summary["a_star"]
    if star["status"] == "crossing in range":
        ax.axvline(logit(star["a_star"]), color=figures.MUTED, lw=0.6)
        figures.end_label(ax, logit(star["a_star"]), ax.get_ylim()[1] * 0.9, f"a* = {star['a_star']:.0%}")
    ax.set_ylabel("FM premium (pp, 95% CI)")
    ax.legend(handles, ["restricted cubic spline (95% band)", "adoption bins (95% CI)", "linear in logit"], loc="best")
    fig.suptitle("PH5 fmwave (post hoc, exploratory; decided papers 2023-2026)", x=0.01, ha="left", fontsize=7)
    _save(fig, out_dir, "PH5_fmwave_premium")

    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.0), sharey=True, constrained_layout=True)
    for ax, (model, title), colour in zip(axes, [("F2 established", "Established teams (earlier ICLR acceptance)"),
                                                 ("F2 no acceptance", "Teams with no earlier ICLR acceptance")],
                                          figures.SERIES[:3:2]):
        handles = panel_(ax, model, model, colour, title)
        ax.legend(handles, ["linear in logit (95% band)", "adoption bins (95% CI)"], loc="lower left")
    axes[0].set_ylabel("FM premium (pp, 95% CI)")
    fig.suptitle("FM premium by author profile (line: linear in logit with 95% band; dots: adoption bins)", x=0.01,
                 ha="left", fontsize=7.5)
    _save(fig, out_dir, "PH5_fmwave_profiles")

    fig, ax = plt.subplots(figsize=(5.2, 3.1), constrained_layout=True)
    flag = summary["P0_code_links"]["F3_label"]
    handles = panel_(ax, "F3 framing", "F3 framing", figures.SERIES[2],
                     "Among FM papers: FM/LLM named in title or first sentence")
    ax.legend(handles, ["linear in logit (95% band)", "adoption bins (95% CI)"], loc="lower right")
    ax.set_ylabel("framing premium (pp, 95% CI)")
    if flag != "no flag":
        ax.text(0.01, 0.02, flag, transform=ax.transAxes, fontsize=6.5, color=figures.INK2)
    _save(fig, out_dir, "PH5_fmwave_framing")

    share, entry = pd.read_csv(out_dir / "free_fm_share.csv"), pd.read_csv(out_dir / "free_entry.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.0), constrained_layout=True, gridspec_kw={"width_ratios": [1.2, 1]})
    ax = axes[0]
    share = share[(share.year >= 2020) & (share.papers >= MIN_SHARE_CELL)]
    for j, b in enumerate(BINS):
        g = share[share.bin == b]
        ax.plot(g.year, g.fm_share * 100, color=figures.SERIES[j], marker="o", ms=3, label=f"prior adoption {b}")
    ax.set_ylabel("FM papers (% of submissions)")
    ax.set_title(f"FM share by prior-adoption bin (all submissions;\ncells with >= {MIN_SHARE_CELL} papers)", loc="left")
    ax.legend(fontsize=6.5)
    ax = axes[1]
    x = np.arange(len(BINS))
    for i, (term, colour) in enumerate(zip(entry.term.unique(), figures.SERIES[:3:2])):
        g = entry[entry.term == term]
        ax.errorbar(x + (i - 0.5) * 0.18, g.coef * 100, yerr=[(g.coef - g.ci95_lo) * 100, (g.ci95_hi - g.coef) * 100],
                    fmt="o", ms=4, color=colour, lw=1, label=term)
    ax.axhline(0, color=figures.INK2, lw=0.7)
    ax.set_xticks(x, BINS, fontsize=6.8)
    ax.set_xlabel("topic's FM share in the previous year")
    ax.set_ylabel("difference in FM share (pp, 95% CI)")
    ax.set_title("Who brings FMs in (2023-2026, within topic x year)", loc="left")
    ax.legend(fontsize=6.3, loc="lower left")
    _save(fig, out_dir, "PH5_fmwave_fm_share")


def _save(fig, out_dir: Path, name: str) -> None:
    import figures
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out_dir / f"{name}.png", dpi=220, bbox_inches="tight")
    figures.plt.close(fig)
