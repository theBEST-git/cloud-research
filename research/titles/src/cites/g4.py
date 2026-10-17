"""G4: LLM-favoured title words and citations among accepted ICLR papers 2017-2025.

Pre-registration: docs/CITES_PREREG.md. Frozen core: cites/core.py (not edited here).
Feature: G4_llm_words = r24_any = title contains a word from any of the 8 families
enhanc*, leverag*, unveil*, unleash*, harness*, empower*, elevat*, boost* (core.R24_WORDS).

What this module does
  1. Primary (pre-registered): reads the frozen estimate and Holm p for G4_llm_words from outputs/cites/primary.json
     and re-computes it with core.primary as a reproduction check (the frozen numbers are the ones reported).
  2. Robustness R1-R7 (pre-registered): core.robustness.
  3. Verdict (pre-registered rule): core.verdict(frozen primary, robustness, frozen Holm p).
  4. Secondary (pre-registered, prereg section 6; no multiplicity claim):
       - each word family separately: one model with all 8 family dummies + primary controls | year^topic50, so each
         coefficient compares titles with that family against titles with no LLM-favoured word;
       - pre-2023 vs 2023+: core._fit on each subset, plus a fully interacted pooled model for the difference;
       - (all questions) joint model with all 8 primary features;
       - (all questions) heterogeneity by LLM-topic papers.
  5. Diagnostics (NOT pre-registered; every block is labelled so in results.json):
       (a) S2 split-record artefact: arXiv-id share and S2 match rate by G4 status; primary spec within records with /
           without an arXiv id, with an arXiv-id indicator, and the interacted difference;
       (b) topic composition: share of G4 papers in llm_topic papers (raw and within year / year x topic50);
           primary spec + llm_topic indicator; concentration of G4 across topic50 clusters and FE cells;
       (c) word sense: G4 recoded without technical senses (gradient boosting, boosted trees, RL 'empowerment'),
           G4 without the boost / elevat families (the 'r24_noamb' variant used in D3), and the family model with
           boost* / empower* split by sense;
       (d) R1 calibration: placebo null of the R1 matched-pairs procedure (random non-G4 'treated' papers with the
           same per-year counts), placebo-adjusted R1 for G4 and for each family with n >= 20, where matched controls
           sit within their own year x topic50 cell, a pair-level adjustment, and tighter calipers;
       (e) team prior: R6 compared with the same-sample R5 (2022-25) estimate;
       (f) audit (2026-10-17): R1 mechanism from cites/audit_g3g4.py -- the placebo of (d) re-derived, the hubness
           mechanism (matched controls are embedding hubs, and hubs are cited more), residual decomposition,
           hub-penalised (CSLS-style) matching with its own null, pair-level hubness adjustment;
       (g) audit (2026-10-17): alternative explanations from cites/audit_g3g4.py -- preprint timing, code links,
           method / findings / benchmark paper type, llm_topic, F24 abstract style, tail and PPML superstar
           dependence (the R2 sign), retitling between arXiv v1 and camera-ready, the N24 neutral-synonym benchmark,
           and word families one at a time.

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m cites.g4
Writes outputs/cites/G4/{results.json, fig.png, fig.pdf, fig.csv}.
"""
from __future__ import annotations

import json
import re
import warnings

import numpy as np
import pandas as pd
import pyfixest as pf

from analyses import _core as C
from cites import audit_g3g4, core

warnings.filterwarnings("ignore")

F = "G4_llm_words"
DST = core.OUT / "G4"
DIAG = "diagnostic (not pre-registered)"
FAM = list(core.R24_WORDS)
FAM_LABEL = {"r24_enhanc": "enhanc*", "r24_leverag": "leverag*", "r24_unveil": "unveil*", "r24_unleash": "unleash*",
             "r24_harness": "harness*", "r24_empower": "empower*", "r24_elevat": "elevat*", "r24_boost": "boost*"}
MIN_N = 20  # families below this are reported but not interpreted (same threshold the prereg uses for G6 templates)
# Technical (non-stylistic) senses of two families: the boosting algorithm family and RL 'empowerment'.
TECH_SENSE = re.compile(r"gradient[- ]boost|\bboosted\b|post-gan boosting|co-boosting|multi-label boosting|"
                        r"optimization,? and boosting|\bempowerment\b", re.I)
ROB_LABEL = {
    "R1_matched_pairs": "R1 content-matched pairs",
    "R2_ppml_counts": "R2 PPML on counts (sign check)",
    "R3_influential": "R3 influential citations",
    "R4_drop_top1pct": "R4 drop top 1% per year",
    "R5_era_2017_21": "R5 2017-21 only",
    "R5_era_2022_25": "R5 2022-25 only",
    "R6_team_prior_2022_25": "R6 2022-25 + team prior",
    "R7_year_plus_topic100_fe": "R7 year + topic100 FE",
}


# --------------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------------
def lpm(r: dict) -> dict:
    """Re-express a core._fit result for a 0/1 outcome as a linear-probability difference (percentage points)."""
    return {"b_pp": 100 * r["b"], "lo_pp": 100 * (r["b"] - 1.96 * r["se"]), "hi_pp": 100 * (r["b"] + 1.96 * r["se"]),
            "se_pp": 100 * r["se"], "p": r["p"], "n": r["n"]}


def share_ci(x: pd.Series) -> dict:
    x = x.astype(float)
    p, n = float(x.mean()), int(len(x))
    se = np.sqrt(p * (1 - p) / n) if n else np.nan
    return {"share": p, "lo": p - 1.96 * se, "hi": p + 1.96 * se, "n": n}


def with_n(r: dict, d: pd.DataFrame, col: str) -> dict:
    r = dict(r)
    r["n_with"] = int(d[col].sum())
    return r


def ratio(r: dict) -> dict:
    """Interaction coefficient as a ratio of two citation multipliers."""
    return {"b": r["b"], "se": r["se"], "p": r["p"], "ratio": float(np.exp(r["b"])),
            "ratio_lo": float(np.exp(r["b"] - 1.96 * r["se"])), "ratio_hi": float(np.exp(r["b"] + 1.96 * r["se"])),
            "n": r["n"]}


def fmt(r: dict) -> str:
    if r.get("pct") is None:
        return "n/a"
    return f"{100 * r['pct']:+.1f}% [{100 * r['lo']:+.1f}, {100 * r['hi']:+.1f}]"


def fit_interacted(d: pd.DataFrame, group: str, fe: str = "year^topic50") -> dict:
    """b(G4 in group=1) - b(G4 in group=0) from one pooled model in which the controls are interacted with `group`.
    When `group` is constant within FE cells (era) this reproduces the two split-sample point estimates exactly."""
    dd = d.copy()
    dd["G4_x_grp"] = dd[F] * dd[group]
    ctrl = core.controls(F)
    for c in ctrl:
        dd[f"{c}_g"] = dd[c] * dd[group]
    return core._fit(dd, "y", "G4_x_grp", ctrl + [F] + [f"{c}_g" for c in ctrl], fe=fe)


# --------------------------------------------------------------------------------------------
# pre-registered parts
# --------------------------------------------------------------------------------------------
def primary_block(df: pd.DataFrame) -> dict:
    frozen = json.load(open(core.OUT / "primary.json"))
    prim = frozen["primary"][F]
    rep = core.primary(df, F)
    diff = {k: abs(prim[k] - rep[k]) for k in ["b", "se", "p", "pct", "lo", "hi"]}
    ok = diff["b"] < 1e-8 and diff["se"] < 1e-8 and prim["n"] == rep["n"] and prim["n_with"] == rep["n_with"]
    return {"frozen": prim, "reproduced": rep, "max_abs_diff": max(diff.values()), "reproduction_ok": bool(ok),
            "n_papers_frame": int(len(df)), "n_papers_frozen": int(frozen["n_papers"])}


def secondary_families(df: pd.DataFrame) -> dict:
    """Pre-specified (prereg s6, G4): each word family separately. One model with all 8 family dummies; the reference
    group is exactly 'no LLM-favoured word' (G4 == 0). 11 titles contain two families and load on both dummies."""
    d = df.copy()
    for w in FAM:
        d[w] = d[w].fillna(False).astype(int)
    out = {}
    for w in FAM:
        others = [x for x in FAM if x != w]
        r = core._fit(d, "y", w, core.controls(F, others))
        r["n_with"] = int(d[w].sum())
        r["n_with_2023plus"] = int(d.loc[d.year >= 2023, w].sum())
        r["label"] = FAM_LABEL[w]
        r["interpretable"] = r["n_with"] >= MIN_N
        out[w] = r
    out["n_titles_two_families"] = int((d[FAM].sum(axis=1) >= 2).sum())
    out["holm_across_8_families"] = {"label": DIAG + " - descriptive only; the prereg makes no multiplicity claim here",
                                     **core.holm({w: out[w]["p"] for w in FAM})}
    out["note"] = (f"One model: y ~ 8 family dummies + primary controls | year^topic50, SE clustered by topic50. "
                   f"Families with n < {MIN_N} are reported but not interpreted.")
    return out


def secondary_era(df: pd.DataFrame) -> dict:
    """Pre-specified (prereg s6, G4): pre-2023 vs 2023+ (core._fit on subsets) and their difference."""
    d = df.copy()
    pre, post = d[d.year <= 2022], d[d.year >= 2023]
    r_pre = with_n(core._fit(pre, "y", F, core.controls(F)), pre, F)
    r_post = with_n(core._fit(post, "y", F, core.controls(F)), post, F)
    d["post2023"] = (d.year >= 2023).astype(int)
    inter = ratio(fit_interacted(d, "post2023"))
    inter["check_b_post_minus_b_pre"] = r_post["b"] - r_pre["b"]
    inter["model"] = ("pooled, G4 x post2023 with all controls interacted with post2023; year^topic50 FE are nested in "
                      "era, so the point estimate equals the split-sample difference; SE clustered by topic50")
    return {"pre_2023": r_pre, "from_2023": r_post, "difference_2023plus_minus_pre": inter}


def secondary_joint(df: pd.DataFrame) -> dict:
    """Pre-specified (prereg s6, all questions): G4 coefficient in a joint model with all 8 primary features."""
    others = [f for f in core.FEATURES if f != F]
    r = core._fit(df, "y", F, core.controls(F, others))
    r["model"] = "y ~ all 8 primary features + primary controls | year^topic50"
    return r


def secondary_llm(df: pd.DataFrame) -> dict:
    """Pre-specified (prereg s6, all questions): heterogeneity by LLM-topic papers."""
    d = df.copy()
    d["llm"] = d.llm_topic.fillna(False).astype(int)
    d["G4_in_llm"] = d[F] * d.llm
    d["G4_in_nonllm"] = d[F] * (1 - d.llm)
    llm = core._fit(d, "y", "G4_in_llm", core.controls(F, ["G4_in_nonllm", "llm"]))
    non = core._fit(d, "y", "G4_in_nonllm", core.controls(F, ["G4_in_llm", "llm"]))
    inter = core._fit(d, "y", "G4_in_llm", core.controls(F, [F, "llm"]))  # G4 x llm interaction given G4 main effect
    llm["n_with"] = int(d.G4_in_llm.sum())
    non["n_with"] = int(d.G4_in_nonllm.sum())
    return {"llm_topic_papers": llm, "non_llm_topic_papers": non, "difference_llm_minus_non": ratio(inter),
            "n_llm_topic_papers": int(d.llm.sum()),
            "note": "One model with G4 split by llm_topic plus an llm_topic main effect; 'difference' is the "
                    "G4 x llm_topic interaction (ratio of the two citation multipliers)."}


# --------------------------------------------------------------------------------------------
# diagnostics (not pre-registered)
# --------------------------------------------------------------------------------------------
def diag_split_records(df: pd.DataFrame) -> dict:
    """(a) S2 split-record artefact. A venue record without an arXiv id can miss citations that S2 credits to a
    separate arXiv record (qc_split_records.jsonl). G4 papers have fewer arXiv ids, which would bias G4 downwards."""
    out = {"label": DIAG}
    d = df.copy()
    d["has_arxiv"] = d.arxiv.notna().astype(int)
    out["arxiv_share"] = {"G4": share_ci(d.loc[d[F] == 1, "has_arxiv"]), "not_G4": share_ci(d.loc[d[F] == 0, "has_arxiv"])}
    m = pf.feols("has_arxiv ~ G4_llm_words | year", data=d, vcov={"CRV1": "topic50"})
    t = m.tidy().loc[F]
    b, se = float(t["Estimate"]), float(t["Std. Error"])
    out["arxiv_share_diff_year_fe_pp"] = {"b_pp": 100 * b, "lo_pp": 100 * (b - 1.96 * se), "hi_pp": 100 * (b + 1.96 * se),
                                          "p": float(t["Pr(>|t|)"]), "n": int(m._N)}
    out["arxiv_share_diff_primary_controls_pp"] = lpm(core._fit(d, "has_arxiv", F, core.controls(F)))
    out["arxiv_share_by_year"] = (d.groupby(["year", F]).has_arxiv.mean().unstack().rename(columns={0: "not_G4", 1: "G4"})
                                  .round(4).reset_index().to_dict(orient="records"))
    out["arxiv_share_coef_on_y"] = core._fit(d, "y", "has_arxiv", core.controls(F, [F]))

    # S2 match rate among all accepted papers 2017-2025 (matched_venue.parquet is read only)
    M = pd.read_parquet(core.OUT / "matched_venue.parquet", columns=["submission_id", "year", "matched"])
    M = M[M.year.between(*core.YEARS)]
    M = M.merge(C.load_features(["r24_any"]), on="submission_id", how="left", validate="1:1")
    out["accepted_2017_25"] = int(len(M))
    out["accepted_missing_G4_feature"] = int(M.r24_any.isna().sum())
    M = M[M.r24_any.notna()].copy()
    M["G4"] = M.r24_any.astype(bool).astype(int)
    M["matched_i"] = M.matched.astype(int)
    out["match_rate"] = {"G4": share_ci(M.loc[M.G4 == 1, "matched_i"]), "not_G4": share_ci(M.loc[M.G4 == 0, "matched_i"])}
    m = pf.feols("matched_i ~ G4 | year", data=M, vcov="hetero")
    t = m.tidy().loc["G4"]
    b, se = float(t["Estimate"]), float(t["Std. Error"])
    out["match_rate_diff_year_fe_pp"] = {"b_pp": 100 * b, "lo_pp": 100 * (b - 1.96 * se), "hi_pp": 100 * (b + 1.96 * se),
                                         "p": float(t["Pr(>|t|)"]), "n": int(m._N)}

    # QC sample of split records (venue record without arXiv id; S2 title-match lookup)
    q = pd.read_json(core.OUT / "qc_split_records.jsonl", lines=True)
    q = q.merge(d[["submission_id", F]], left_on="sid", right_on="submission_id", how="left")
    q["split"] = q.match_pid.notna() & (q.match_pid != q.venue_pid)
    out["qc_split_sample"] = {
        "n_checked": int(len(q)), "n_split": int(q.split.sum()),
        "split_by_G4": {str(k): {"n": int(len(g)), "split": int(g.split.sum())}
                        for k, g in q.groupby(q[F].fillna(-1).astype(int))},
        "note": "Random sample of matched records without an arXiv id (qc_split.py; the run has finished, its log ends "
                "'DONE' at 30 records); too small for a G4 comparison.",
    }

    # primary spec within arXiv / non-arXiv records, with an arXiv indicator, and the interacted difference
    a1, a0 = d[d.has_arxiv == 1], d[d.has_arxiv == 0]
    out["primary_spec_arxiv_only"] = with_n(core._fit(a1, "y", F, core.controls(F)), a1, F)
    out["primary_spec_no_arxiv_only"] = with_n(core._fit(a0, "y", F, core.controls(F)), a0, F)
    out["primary_spec_plus_arxiv_control"] = core._fit(d, "y", F, core.controls(F, ["has_arxiv"]))
    d["no_arxiv"] = 1 - d.has_arxiv
    inter = ratio(fit_interacted(d, "no_arxiv", fe="year^topic50^has_arxiv"))
    inter["model"] = "G4 x no-arXiv interaction; controls and year^topic50 FE interacted with has_arxiv (as in G1)"
    out["difference_no_arxiv_minus_arxiv"] = inter
    return out


def diag_topic(df: pd.DataFrame) -> dict:
    """(b) Topic composition. G4 papers are disproportionately LLM-topic papers and from 2024-25."""
    out = {"label": DIAG}
    d = df.copy()
    d["llm"] = d.llm_topic.fillna(False).astype(int)
    out["llm_topic_share"] = {"G4": share_ci(d.loc[d[F] == 1, "llm"]), "not_G4": share_ci(d.loc[d[F] == 0, "llm"])}
    for fe, key in [("year", "llm_share_diff_year_fe_pp"), ("year^topic50", "llm_share_diff_year_x_topic50_fe_pp")]:
        m = pf.feols(f"llm ~ {F} | {fe}", data=d, vcov={"CRV1": "topic50"})
        t = m.tidy().loc[F]
        b, se = float(t["Estimate"]), float(t["Std. Error"])
        out[key] = {"b_pp": 100 * b, "lo_pp": 100 * (b - 1.96 * se), "hi_pp": 100 * (b + 1.96 * se),
                    "p": float(t["Pr(>|t|)"]), "n": int(m._N)}
    # G4 rate per 1,000 titles, by era and llm_topic
    d["era"] = np.where(d.year >= 2023, "2023-25", "2017-22")
    rate = d.groupby(["era", "llm"])[F].agg(["sum", "count"]).reset_index()
    rate["per_1000"] = 1000 * rate["sum"] / rate["count"]
    out["G4_per_1000_by_era_llm"] = rate.rename(columns={"sum": "n_G4", "count": "n"}).to_dict(orient="records")
    out["G4_by_year"] = d.groupby("year")[F].agg(["sum", "count"]).rename(columns={"sum": "n_G4", "count": "n"}) \
        .reset_index().to_dict(orient="records")
    # primary spec + llm_topic indicator (llm_topic varies within year x topic50 cells)
    out["primary_spec_plus_llm_topic_control"] = core._fit(d, "y", F, core.controls(F, ["llm"]))
    cellvar = d.groupby("yt").llm.transform("nunique") > 1
    out["G4_papers_in_cells_where_llm_topic_varies"] = int(d.loc[cellvar, F].sum())
    # identification: G4 papers in year x topic50 cells that also contain non-G4 papers
    cell = d.groupby("yt")[F].agg(["sum", "count"])
    informative = cell[(cell["sum"] > 0) & (cell["sum"] < cell["count"])]
    out["fe_cells"] = {"n_cells": int(len(cell)), "cells_with_G4": int((cell["sum"] > 0).sum()),
                       "G4_papers_in_cells_with_variation": int(informative["sum"].sum()),
                       "largest_cell_share_of_G4": float(cell["sum"].max() / d[F].sum())}
    # concentration across topic50 clusters
    t = d.groupby("topic50").agg(n=(F, "size"), n_G4=(F, "sum"), llm_share=("llm", "mean"))
    t["share_of_G4"] = t.n_G4 / t.n_G4.sum()
    t["share_of_papers"] = t.n / t.n.sum()
    top = t.sort_values("n_G4", ascending=False).head(5)
    out["top5_topic50_by_G4"] = top.reset_index().to_dict(orient="records")
    out["top5_topic50_share_of_G4"] = float(top.share_of_G4.sum())
    out["top5_topic50_share_of_papers"] = float(top.share_of_papers.sum())
    out["top5_topic50_example_titles"] = {int(k): d.loc[(d.topic50 == k) & (d[F] == 1), "title"].head(3).tolist()
                                          for k in top.index}
    return out


def diag_word_sense(df: pd.DataFrame) -> dict:
    """(c) Word sense. Some matches are technical terms, not stylistic choices: the boosting algorithm family
    (gradient boosting, boosted trees) and 'empowerment' in RL. Recode those to G4 = 0 unless another family matches;
    separately drop the boost / elevat families altogether (the 'r24_noamb' variant used in D3)."""
    out = {"label": DIAG, "tech_sense_regex": TECH_SENSE.pattern}
    d = df.copy()
    X = d[FAM].fillna(False).astype(bool)
    tech = d.title.map(lambda t: bool(TECH_SENSE.search(t)))
    style_fam = X.copy()
    style_fam["r24_boost"] = X.r24_boost & ~tech
    style_fam["r24_empower"] = X.r24_empower & ~tech
    d["G4_style_sense"] = style_fam.any(axis=1).astype(int)
    d["G4_noamb"] = X.drop(columns=["r24_boost", "r24_elevat"]).any(axis=1).astype(int)
    recoded = d[(d[F] == 1) & (d.G4_style_sense == 0)]
    out["recoded_to_0"] = recoded[["year", "title"]].sort_values("year").to_dict(orient="records")
    out["n_recoded"] = int(len(recoded))
    out["G4_style_sense"] = with_n(core._fit(d, "y", "G4_style_sense", core.controls(F)), d, "G4_style_sense")
    out["G4_without_boost_elevat"] = with_n(core._fit(d, "y", "G4_noamb", core.controls(F)), d, "G4_noamb")
    # 2023+ (where 88% of G4 titles are) with the style-sense coding
    p = d[d.year >= 2023]
    out["G4_style_sense_2023plus"] = with_n(core._fit(p, "y", "G4_style_sense", core.controls(F)), p, "G4_style_sense")
    # family model with boost* and empower* split into technical vs stylistic sense (reference = no LLM word)
    for w in FAM:
        d[w] = X[w].astype(int)
    d["boost_tech"] = (X.r24_boost & tech).astype(int)
    d["boost_style"] = (X.r24_boost & ~tech).astype(int)
    d["empower_tech"] = (X.r24_empower & tech).astype(int)
    d["empower_style"] = (X.r24_empower & ~tech).astype(int)
    cols = [w for w in FAM if w not in ("r24_boost", "r24_empower")] + ["boost_tech", "boost_style", "empower_tech", "empower_style"]
    split = {}
    for c in ["boost_tech", "boost_style", "empower_tech", "empower_style"]:
        r = core._fit(d, "y", c, core.controls(F, [x for x in cols if x != c]))
        r["n_with"] = int(d[c].sum())
        split[c] = r
    out["family_model_boost_empower_split_by_sense"] = split
    return out


def _emb(d: pd.DataFrame) -> np.ndarray:
    """Same embedding as core.matched_pairs: name-masked abstract (unmasked where no masked text, e.g. 2017)."""
    Em, found = C.load_masked_embedding(d)
    Ea = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea)
    return E / np.linalg.norm(E, axis=1, keepdims=True)


def _nn_pairs(E: np.ndarray, years: np.ndarray, tr: np.ndarray, co: np.ndarray, caliper: float = 0.80):
    """Nearest same-year control for each treated row, as in core.matched_pairs (with replacement, cosine >= caliper)."""
    T, Cc = [], []
    for y in np.unique(years):
        ti = np.where(tr & (years == y))[0]
        ci = np.where(co & (years == y))[0]
        if len(ti) == 0 or len(ci) == 0:
            continue
        S = E[ti] @ E[ci].T
        j = S.argmax(1)
        ok = S[np.arange(len(ti)), j] >= caliper
        T.append(ti[ok])
        Cc.append(ci[j[ok]])
    return np.concatenate(T), np.concatenate(Cc)


def _placebo(d: pd.DataFrame, E: np.ndarray, treat: np.ndarray, n_rep: int, seed: int = 0) -> dict:
    """Null distribution of the R1 statistic: draw pseudo-treated papers at random from the non-G4 pool with the same
    per-year counts as the real treated group, match them to the remaining non-G4 papers with the R1 procedure, and
    record the mean within-pair log difference. Under no association this should centre on 0."""
    years, yv = d.year.to_numpy(), d.y.to_numpy()
    pool0 = (d[F] == 0).to_numpy()
    counts = pd.Series(years[treat]).value_counts()
    rng = np.random.default_rng(seed)
    stats = []
    for _ in range(n_rep):
        tr = np.zeros(len(d), bool)
        for y, k in counts.items():
            idx = np.where(pool0 & (years == y))[0]
            tr[rng.choice(idx, int(k), replace=False)] = True
        t, c = _nn_pairs(E, years, tr, pool0 & ~tr)
        stats.append(float((yv[t] - yv[c]).mean()))
    return {"n_rep": n_rep, "mean_log_diff": float(np.mean(stats)), "sd_log_diff": float(np.std(stats, ddof=1)),
            "pct_at_mean": float(np.exp(np.mean(stats)) - 1),
            "q2.5_q97.5_pct": [float(np.exp(q) - 1) for q in np.percentile(stats, [2.5, 97.5])], "_stats": stats}


def diag_r1_calibration(df: pd.DataFrame, rob: dict, n_rep: int = 200) -> dict:
    """(d) R1 calibration and per-family matched pairs. R1 is far more negative than the primary. Checks:
    (i) placebo null of the R1 procedure (pseudo-treated non-G4 papers, same per-year counts) for G4 and for each
        family with n >= MIN_N; placebo-adjusted R1 = observed mean log diff - placebo mean, with a placebo p-value;
    (ii) where the matched controls sit relative to their own year x topic50 cell;
    (iii) pair-level adjustment for within-pair differences in log team size, log abstract words and arXiv id;
    (iv) tighter calipers."""
    import statsmodels.api as sm
    out = {"label": DIAG}
    d = df.reset_index(drop=True).copy()
    d["has_arxiv"] = d.arxiv.notna().astype(int)
    E = _emb(d)
    years, yv = d.year.to_numpy(), d.y.to_numpy()
    X = d[FAM].fillna(False).astype(bool)
    pool0 = (d[F] == 0).to_numpy()
    groups = {"G4_llm_words": (d[F] == 1).to_numpy()}
    groups.update({w: X[w].to_numpy() for w in FAM if X[w].sum() >= MIN_N})
    for g, tr in groups.items():
        t, c = _nn_pairs(E, years, tr, pool0)
        obs = float((yv[t] - yv[c]).mean())
        pl = _placebo(d, E, tr, n_rep, seed=0)
        stats = np.array(pl.pop("_stats"))
        adj = obs - pl["mean_log_diff"]
        se = float(pl["sd_log_diff"] * np.sqrt(1 + 1 / n_rep))
        p_lo = (1 + (stats <= obs).sum()) / (n_rep + 1)
        p_hi = (1 + (stats >= obs).sum()) / (n_rep + 1)
        out[g] = {"n_pairs": int(len(t)), "observed_pct": float(np.exp(obs) - 1), "placebo": pl,
                  "placebo_p_two_sided": float(min(1.0, 2 * min(p_lo, p_hi))),
                  "placebo_adjusted_pct": float(np.exp(adj) - 1),
                  "placebo_adjusted_lo": float(np.exp(adj - 1.96 * se) - 1),
                  "placebo_adjusted_hi": float(np.exp(adj + 1.96 * se) - 1),
                  "note": "adjusted = exp(observed mean log diff - placebo mean) - 1; approximate CI uses the placebo SD "
                          "of the R1 statistic (its sampling SD for this group size and year mix) as the SE"}
        if g != "G4_llm_words":
            out[g]["core_matched_pairs"] = core.matched_pairs(d[X[g] | (d[F] == 0)], F)  # same pairs via core
    t, c = _nn_pairs(E, years, groups["G4_llm_words"], pool0)
    out["reimplementation_check"] = {"n_pairs": int(len(t)), "pct": float(np.exp((yv[t] - yv[c]).mean()) - 1),
                                     "core_R1_n_pairs": rob["R1_matched_pairs"]["n_pairs"],
                                     "core_R1_pct": rob["R1_matched_pairs"]["pct"]}
    cm = d[d[F] == 0].groupby("yt").y.mean()
    yt = d.yt.to_numpy()
    out["controls_y_minus_own_cell_nonG4_mean"] = float(np.nanmean(yv[c] - cm.reindex(yt[c]).to_numpy()))
    out["treated_y_minus_own_cell_nonG4_mean"] = float(np.nanmean(yv[t] - cm.reindex(yt[t]).to_numpy()))
    out["share_pairs_same_topic50"] = float((d.topic50.to_numpy()[t] == d.topic50.to_numpy()[c]).mean())
    out["n_unique_controls"] = int(len(np.unique(c)))
    dy = yv[t] - yv[c]
    Z = pd.DataFrame({k: d[k].to_numpy(float)[t] - d[k].to_numpy(float)[c] for k in ["log_authors", "log_abs_words", "has_arxiv"]})
    out["pair_control_differences_mean"] = Z.mean().to_dict()
    m = sm.OLS(dy, sm.add_constant(Z)).fit(cov_type="cluster", cov_kwds={"groups": c})
    a, se = float(m.params["const"]), float(m.bse["const"])
    out["R1_pairs_adjusted"] = {"pct": float(np.exp(a) - 1), "lo": float(np.exp(a - 1.96 * se) - 1),
                                "hi": float(np.exp(a + 1.96 * se) - 1), "p": float(m.pvalues["const"]),
                                "coef_d_has_arxiv": float(m.params["has_arxiv"]),
                                "note": "intercept of d_y ~ 1 + d_log_authors + d_log_abs_words + d_has_arxiv; SE clustered by control"}
    out["R1_caliper"] = {f"{cal:.2f}": core.matched_pairs(df, F, caliper=cal) for cal in (0.85, 0.90)}
    return out


def diag_team_prior(df: pd.DataFrame, rob: dict) -> dict:
    """(e) Team prior: R6 (pre-registered) against R5 2022-25 (same sample, no team-prior control)."""
    d = df[df.year >= 2022]
    r5, r6 = rob["R5_era_2022_25"], rob["R6_team_prior_2022_25"]
    return {"label": DIAG + " - comparison of two pre-registered checks",
            "R5_2022_25_no_team_prior": r5, "R6_2022_25_with_team_prior": r6, "change_in_b": r6["b"] - r5["b"],
            "mean_log1p_prior_accs": {"G4": float(d.loc[d[F] == 1, "lprior_acc"].mean()),
                                      "not_G4": float(d.loc[d[F] == 0, "lprior_acc"].mean())},
            "n_2022_25": int(len(d)), "n_G4_2022_25": int(d[F].sum())}


# --------------------------------------------------------------------------------------------
# figure
# --------------------------------------------------------------------------------------------
def figure(prim: dict, rob: dict, r1cal: dict) -> dict:
    adj = {"pct": r1cal["placebo_adjusted_pct"], "lo": r1cal["placebo_adjusted_lo"], "hi": r1cal["placebo_adjusted_hi"]}
    rows = [("Primary", prim, C.COLORS[0], "main")]
    for k in ROB_LABEL:
        rows.append((ROB_LABEL[k], rob[k], C.TEXT2, "rob"))
        if k == "R1_matched_pairs":
            rows.append(("   R1 placebo-adjusted (diagnostic)", adj, C.GREY, "diag"))
    lab = [r[0] for r in rows]
    est = np.array([100 * r[1]["pct"] for r in rows])
    lo = np.array([100 * r[1]["lo"] for r in rows])
    hi = np.array([100 * r[1]["hi"] for r in rows])
    fig, ax = C.new_fig(width=6.2, height=3.5)
    ypos = np.arange(len(rows))[::-1]
    ax.axvspan(-10, 10, color=C.GRID, alpha=0.55, lw=0, zorder=0)
    ax.axvline(0, color=C.TEXT2, lw=0.8, zorder=1)
    for yv, e, l_, h, (_, _, c, kind) in zip(ypos, est, lo, hi, rows):
        ax.plot([l_, h], [yv, yv], color=c, lw=1.4 if kind == "diag" else 2.0, solid_capstyle="round", zorder=2)
        if kind == "diag":
            ax.plot([e], [yv], "o", mfc=C.BG, mec=c, ms=5.5, mew=1.4, zorder=3)
        else:
            ax.plot([e], [yv], "o", color=c, ms=7 if kind == "main" else 5.5, mec=C.BG, mew=1.2, zorder=3)
    ax.set_yticks(ypos, lab)
    for t, (_, _, c, kind) in zip(ax.get_yticklabels(), rows):
        t.set_fontweight("bold" if kind == "main" else "normal")
        if kind == "diag":
            t.set_color(C.TEXT2)
            t.set_fontstyle("italic")
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", visible=False)
    xmin = min(lo.min(), -10) - 4
    xmax = max(hi.max(), 10) + 4
    ax.set_xlim(xmin, xmax)
    f_ = lambda v: f"{v:+.1f}" if abs(v) < 1 else f"{v:+.0f}"
    for yv, e, l_, h, (_, _, _, kind) in zip(ypos, est, lo, hi, rows):
        ax.text(xmax + 3, yv, f"{f_(e)}%  [{f_(l_)}, {f_(h)}]", ha="left", va="center", fontsize=7.5,
                color=C.TEXT if kind == "main" else C.TEXT2, fontweight="bold" if kind == "main" else "normal", clip_on=False)
    ax.text(10.8, ypos[0] + 0.7, "±10%", ha="left", va="center", fontsize=7, color=C.TEXT2)
    ax.set_ylim(-0.6, ypos[0] + 1.1)
    ticks = [t for t in np.arange(-40, 101, 20) if xmin <= t <= xmax]
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{t:+.0f}%" if t else "0" for t in ticks])
    ax.set_xlabel("Difference in citations, titles with vs without LLM-favoured words (95% CI)")
    ax.set_title("LLM-favoured title words, accepted ICLR papers 2017-25", loc="left", fontsize=9, pad=8)
    ax.spines["left"].set_visible(False)
    data = pd.DataFrame({"row": lab, "pct": est, "lo": lo, "hi": hi})
    return C.save_fig(fig, "fig", DST, data=data)


# --------------------------------------------------------------------------------------------
def main():
    DST.mkdir(parents=True, exist_ok=True)
    df = core.load()
    P = primary_block(df)
    prim, p_holm = P["frozen"], P["frozen"]["p_holm"]
    rob = core.robustness(df, F)
    verdict = core.verdict(prim, rob, p_holm)
    res = {
        "question": "G4: among accepted ICLR papers 2017-2025, do papers whose titles use LLM-favoured words (enhancing, "
                    "leveraging, unveiling, unleashing, harnessing, empowering, elevating, boosting) receive more or "
                    "fewer Semantic Scholar citations than papers with similar content?",
        "feature": F, "label": core.FEATURES[F],
        "outcome": "y = log(1 + Semantic Scholar citationCount, retrieved 2026-10-17); % difference = exp(b) - 1",
        "primary": P,
        "robustness": rob,
        "verdict": verdict,
        "verdict_inputs": {"p_holm": p_holm,
                           "R1_sign_same": (rob["R1_matched_pairs"]["pct"] > 0) == (prim["pct"] > 0),
                           "R2_sign_same": (rob["R2_ppml_counts"]["pct"] > 0) == (prim["pct"] > 0),
                           "ci_within_10pct": bool(prim["lo"] > -0.10 and prim["hi"] < 0.10)},
        "secondary_prespecified": {
            "word_families": secondary_families(df),
            "era_pre2023_vs_2023plus": secondary_era(df),
            "joint_model_8_features": secondary_joint(df),
            "llm_topic_heterogeneity": secondary_llm(df),
        },
        "diagnostics_not_preregistered": {
            "label": DIAG,
            "a_s2_split_records": diag_split_records(df),
            "b_topic_composition": diag_topic(df),
            "c_word_sense": diag_word_sense(df),
            "d_r1_calibration_and_family_pairs": diag_r1_calibration(df, rob),
            "e_team_prior": diag_team_prior(df, rob),
            "f_audit_r1_mechanism": audit_g3g4.r1_calibration(df, F),
            "g_audit_alt_explanations": audit_g3g4.alt_explanations(df, F),
        },
        "audit": {"date": "2026-10-17", "label": "adversarial audit; changes are diagnostic only (not pre-registered)",
                  "changes": ["added diagnostics_not_preregistered.f_audit_r1_mechanism and g_audit_alt_explanations "
                              "(cites/audit_g3g4.py)",
                              "qc_split_sample note: the QC run has finished (30 records); counts unchanged"]},
    }
    rc = res["diagnostics_not_preregistered"]["f_audit_r1_mechanism"]["reimplementation_check"]
    assert rc["n_pairs"] == rob["R1_matched_pairs"]["n_pairs"] and abs(rc["pct"] - rob["R1_matched_pairs"]["pct"]) < 1e-9, rc
    res["figure"] = {k: str(v) for k, v in figure(prim, rob, res["diagnostics_not_preregistered"]
                                                  ["d_r1_calibration_and_family_pairs"]["G4_llm_words"]).items()}
    json.dump(res, open(DST / "results.json", "w"), indent=1, default=float)

    # console summary
    print(f"reproduction ok: {P['reproduction_ok']}  max|diff| {P['max_abs_diff']:.2e}")
    print(f"primary {fmt(prim)}  p {prim['p']:.3g} holm p {p_holm:.3g}  n {prim['n']}  n_with {prim['n_with']}")
    for k in ROB_LABEL:
        r = rob[k]
        extra = f"n_pairs {r['n_pairs']}" if "n_pairs" in r else f"p {r['p']:.3g} n {r['n']}"
        print(f"  {k:26s} {fmt(r)}  {extra}")
    print("verdict:", verdict, res["verdict_inputs"])
    S = res["secondary_prespecified"]
    for w in FAM:
        r = S["word_families"][w]
        print(f"  {w:12s} n {r['n_with']:4d} {fmt(r)}  p {r['p']:.3g}")
    E = S["era_pre2023_vs_2023plus"]
    print("pre-2023", fmt(E["pre_2023"]), E["pre_2023"]["n_with"], "| 2023+", fmt(E["from_2023"]), E["from_2023"]["n_with"],
          "| diff", {k: round(v, 4) for k, v in E["difference_2023plus_minus_pre"].items() if isinstance(v, float)})
    print("joint 8:", fmt(S["joint_model_8_features"]), f"p {S['joint_model_8_features']['p']:.3g}")
    L = S["llm_topic_heterogeneity"]
    print("llm", fmt(L["llm_topic_papers"]), L["llm_topic_papers"]["n_with"], "non-llm", fmt(L["non_llm_topic_papers"]),
          L["non_llm_topic_papers"]["n_with"], "diff", {k: round(v, 3) for k, v in L["difference_llm_minus_non"].items()})
    D = res["diagnostics_not_preregistered"]
    A = D["a_s2_split_records"]
    print("arxiv share", {k: round(v["share"], 4) for k, v in A["arxiv_share"].items()},
          "yearFE", {k: round(v, 3) for k, v in A["arxiv_share_diff_year_fe_pp"].items()},
          "primary ctrl", {k: round(v, 3) for k, v in A["arxiv_share_diff_primary_controls_pp"].items()})
    print("match rate", {k: round(v["share"], 4) for k, v in A["match_rate"].items()}, A["match_rate_diff_year_fe_pp"])
    print("arxiv only", fmt(A["primary_spec_arxiv_only"]), A["primary_spec_arxiv_only"]["n"], A["primary_spec_arxiv_only"]["n_with"],
          "| no arxiv", fmt(A["primary_spec_no_arxiv_only"]), A["primary_spec_no_arxiv_only"]["n"], A["primary_spec_no_arxiv_only"]["n_with"],
          "| +ctrl", fmt(A["primary_spec_plus_arxiv_control"]),
          "| diff", {k: round(v, 3) for k, v in A["difference_no_arxiv_minus_arxiv"].items() if isinstance(v, float)})
    print("arxiv coef on y", fmt(A["arxiv_share_coef_on_y"]), "qc", A["qc_split_sample"])
    T = D["b_topic_composition"]
    print("llm share", {k: round(v["share"], 4) for k, v in T["llm_topic_share"].items()},
          "yearFE", {k: round(v, 3) for k, v in T["llm_share_diff_year_fe_pp"].items()},
          "cellFE", {k: round(v, 3) for k, v in T["llm_share_diff_year_x_topic50_fe_pp"].items()})
    print("rates", T["G4_per_1000_by_era_llm"])
    print("+llm ctrl", fmt(T["primary_spec_plus_llm_topic_control"]), "fe cells", T["fe_cells"],
          "G4 in llm-varying cells", T["G4_papers_in_cells_where_llm_topic_varies"])
    print("top5", T["top5_topic50_share_of_G4"], T["top5_topic50_share_of_papers"])
    for r in T["top5_topic50_by_G4"]:
        print("   ", r, T["top5_topic50_example_titles"][int(r["topic50"])])
    W = D["c_word_sense"]
    print("recoded", W["n_recoded"], "style", fmt(W["G4_style_sense"]), W["G4_style_sense"]["n_with"],
          "noamb", fmt(W["G4_without_boost_elevat"]), W["G4_without_boost_elevat"]["n_with"],
          "style 2023+", fmt(W["G4_style_sense_2023plus"]), W["G4_style_sense_2023plus"]["n_with"])
    for k, r in W["family_model_boost_empower_split_by_sense"].items():
        print("  sense", k, r["n_with"], fmt(r), f"p {r['p']:.3g}")
    R = D["d_r1_calibration_and_family_pairs"]
    for g in ["G4_llm_words"] + FAM:
        if g in R:
            r = R[g]
            print(f"  R1 {g:12s} pairs {r['n_pairs']:4d} obs {100 * r['observed_pct']:+.1f}% placebo "
                  f"{100 * r['placebo']['pct_at_mean']:+.1f}% (sd {r['placebo']['sd_log_diff']:.3f}, 95% {r['placebo']['q2.5_q97.5_pct']}) "
                  f"adj {100 * r['placebo_adjusted_pct']:+.1f}% [{100 * r['placebo_adjusted_lo']:+.1f}, {100 * r['placebo_adjusted_hi']:+.1f}] "
                  f"p {r['placebo_p_two_sided']:.3f}" + (f" core {fmt(r['core_matched_pairs'])}" if "core_matched_pairs" in r else ""))
    print("reimpl", R["reimplementation_check"], "ctrl vs cell", round(R["controls_y_minus_own_cell_nonG4_mean"], 3),
          "treated vs cell", round(R["treated_y_minus_own_cell_nonG4_mean"], 3), "same topic", round(R["share_pairs_same_topic50"], 3),
          "unique ctrl", R["n_unique_controls"])
    print("pair diffs", R["pair_control_differences_mean"], "adjusted", fmt(R["R1_pairs_adjusted"]), round(R["R1_pairs_adjusted"]["p"], 4))
    for k, r in R["R1_caliper"].items():
        print("  caliper", k, fmt(r), r.get("n_pairs"))
    TP = D["e_team_prior"]
    print("R5", fmt(TP["R5_2022_25_no_team_prior"]), "R6", fmt(TP["R6_2022_25_with_team_prior"]), "dB", round(TP["change_in_b"], 4),
          TP["mean_log1p_prior_accs"])
    print("AUDIT (diagnostic, not pre-registered):")
    for line in audit_g3g4.summary_lines(D["f_audit_r1_mechanism"], D["g_audit_alt_explanations"]):
        print("  ", line)


if __name__ == "__main__":
    main()
