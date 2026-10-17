"""Shared, pre-registered analysis core for the title -> citation study (docs/CITES_PREREG.md).

Every G-analysis MUST call `primary()` for its pre-registered estimate and `robustness()` for the
pre-specified checks; no analysis may change the outcome, sample, controls or fixed effects.

Sample: accepted ICLR papers 2017-2025 (discovery universe) matched to a Semantic Scholar venue record.
Outcome: y = log(1 + citationCount); PPML on raw counts as robustness.
Primary model: y ~ feature + log_authors + log_abs_words + 20 abstract-embedding PCs | year^topic50,
SEs clustered by topic50. Effects are reported as % difference = exp(b) - 1.
"""
from __future__ import annotations

import json
import re

import numpy as np
import pandas as pd
import pyfixest as pf
from sklearn.decomposition import PCA

from analyses import _core as C

OUT = C.OUT / "cites"
YEARS = (2017, 2025)
N_PCS = 20
ASSERT = re.compile(r"\b(is|are|was|were|can|cannot|can't|could|will|does|do|did|doesn't|don't|isn't|aren't|improves?|outperforms?|beats?|solves?|enables?|matters?|helps?|hurts?|needs?|makes?|yields?|leads?|works?|fails?|suffices?|reveals?|shows?|proves?|guarantees?|achieves?|boosts?|surpasses?)\b", re.I)
MEME = ["tpl_all_you_need", "tpl_is_secretly", "tpl_free_lunch", "tpl_less_is_more", "tpl_lost_in", "tpl_devil_in", "tpl_tale_of",
        "tpl_rule_them_all", "tpl_worth_a_thousand", "tpl_matters", "tpl_do_really", "tpl_when_meets"]
TENTATIVE = ["tpl_towards", "tpl_rethinking", "tpl_revisiting", "tpl_understanding", "tpl_on_the", "tpl_demystifying"]
R24_WORDS = ["r24_enhanc", "r24_leverag", "r24_unveil", "r24_unleash", "r24_harness", "r24_empower", "r24_elevat", "r24_boost"]

# Pre-registered primary family (Holm over these 8)
FEATURES = {
    "G1_name": "Coined method name ('NAME: subtitle')",
    "G2_assertive": "Title states a finding (assertive verb, not a question; rule-based)",
    "G3_question": "Question title",
    "G4_llm_words": "LLM-favoured title words (enhancing, leveraging, unveiling, ...)",
    "G5a_length5": "Title length (per +5 words)",
    "G5b_informative": "Title informativeness (title-abstract similarity, per SD within year)",
    "G6a_meme": "Meme template (All You Need, Is Secretly, Matters, When X Meets Y, ...)",
    "G6b_tentative": "Tentative framing (Towards, Rethinking, Revisiting, Understanding, On the, Demystifying)",
}
BINARY = ["G1_name", "G2_assertive", "G3_question", "G4_llm_words", "G6a_meme", "G6b_tentative"]
EXTRA_CONTROLS = {"G5a_length5": ["G1_name"], "G5b_informative": ["G1_name", "G5a_length5"]}


def load(permute_outcome: bool = False, seed: int = 0) -> pd.DataFrame:
    """Analysis frame with features, controls, PCs and outcome. permute_outcome shuffles citations within year (dry run)."""
    M = pd.read_parquet(OUT / "matched_venue.parquet")
    M = M[M.matched & M.year.between(*YEARS)][["submission_id", "citationCount", "influentialCitationCount", "arxiv", "n_s2"]]
    df = C.load_analysis_frame(universe_cols=["submission_id", "year", "title", "abstract", "emb_row", "topic50", "topic100",
                                              "log_authors", "max_prior_accs", "exp_valid", "llm_topic"]).reset_index(drop=True)
    df = df.merge(M, on="submission_id", how="inner").reset_index(drop=True)
    b = lambda c: df[c].fillna(False).astype(bool)
    df["G1_name"] = b("name_primary").astype(int)
    df["G3_question"] = b("question").astype(int)
    df["G2_assertive"] = (df.title.map(lambda t: bool(ASSERT.search(t))) & ~b("question")).astype(int)
    df["G4_llm_words"] = b("r24_any").astype(int)
    df["G5a_length5"] = df.n_words / 5.0
    df["G6a_meme"] = df[MEME].fillna(False).astype(bool).any(axis=1).astype(int)
    df["G6b_tentative"] = df[TENTATIVE].fillna(False).astype(bool).any(axis=1).astype(int)
    Et = C.load_embedding(df, "title", "bge-small-en-v1.5")
    Ea = C.load_embedding(df, "abstract", "bge-small-en-v1.5")
    Et /= np.linalg.norm(Et, axis=1, keepdims=True)
    Ea /= np.linalg.norm(Ea, axis=1, keepdims=True)
    sim = (Et * Ea).sum(1)
    df["title_abs_cos"] = sim
    df["G5b_informative"] = df.groupby("year").title_abs_cos.transform(lambda s: (s - s.mean()) / s.std())
    pcs = PCA(n_components=N_PCS, random_state=0).fit_transform(Ea)
    for k in range(N_PCS):
        df[f"pc{k}"] = pcs[:, k]
    df["log_abs_words"] = np.log(df.abstract.str.split().str.len().clip(lower=1))
    df["lprior_acc"] = np.log1p(df.max_prior_accs.fillna(0))
    df["cites"] = df.citationCount.fillna(0).astype(float)
    df["infl"] = df.influentialCitationCount.fillna(0).astype(float)
    if permute_outcome:
        rng = np.random.default_rng(seed)
        for col in ["cites", "infl"]:
            df[col] = df.groupby("year")[col].transform(lambda s: rng.permutation(s.to_numpy()))
    df["y"] = np.log1p(df.cites)
    df["y_infl"] = np.log1p(df.infl)
    df["yt"] = df.year.astype(str) + "_" + df.topic50.astype(str)
    df["topic50"] = df.topic50.astype(int)
    return df


def controls(feature: str, extra=()):
    base = ["log_authors", "log_abs_words"] + [f"pc{k}" for k in range(N_PCS)]
    return base + EXTRA_CONTROLS.get(feature, []) + list(extra)


def _fit(df, y, feature, ctrl, fe="year^topic50", poisson=False):
    fml = f"{y} ~ {feature} + {' + '.join(ctrl)} | {fe}"
    m = (pf.fepois if poisson else pf.feols)(fml, data=df, vcov={"CRV1": "topic50"})
    t = m.tidy().loc[feature]
    b, se, p = float(t["Estimate"]), float(t["Std. Error"]), float(t["Pr(>|t|)"])
    return {"b": b, "se": se, "p": p, "pct": float(np.exp(b) - 1), "lo": float(np.exp(b - 1.96 * se) - 1),
            "hi": float(np.exp(b + 1.96 * se) - 1), "n": int(m._N)}


def primary(df, feature):
    """Pre-registered primary estimate."""
    r = _fit(df, "y", feature, controls(feature))
    if feature in BINARY:
        r["n_with"] = int(df[feature].sum())
    return r


def matched_pairs(df, feature, caliper=0.80, n_boot=2000, seed=0):
    """Content-matched pairs: each treated paper (feature=1, or top tercile for continuous features) is paired
    with its nearest same-year control (feature=0 / bottom tercile) on the name-masked abstract embedding
    (unmasked for 2017), cosine >= caliper, with replacement. Returns mean within-pair difference in y."""
    d = df.reset_index(drop=True)
    if feature in BINARY:
        tr, co = d[feature] == 1, d[feature] == 0
    else:
        q = d.groupby("year")[feature].transform(lambda s: s.rank(pct=True))
        tr, co = q >= 2 / 3, q <= 1 / 3
    Em, found = C.load_masked_embedding(d)
    Ea = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea)
    E = E / np.linalg.norm(E, axis=1, keepdims=True)
    diffs = []
    for y in sorted(d.year.unique()):
        ti = np.where(tr & (d.year == y))[0]
        ci = np.where(co & (d.year == y))[0]
        if len(ti) == 0 or len(ci) == 0:
            continue
        S = E[ti] @ E[ci].T
        j = S.argmax(1)
        ok = S[np.arange(len(ti)), j] >= caliper
        diffs += list(d.y.to_numpy()[ti[ok]] - d.y.to_numpy()[ci[j[ok]]])
    diffs = np.array(diffs)
    if len(diffs) == 0:
        return {"n_pairs": 0}
    rng = np.random.default_rng(seed)
    boots = [rng.choice(diffs, len(diffs)).mean() for _ in range(n_boot)]
    m, lo, hi = diffs.mean(), *np.percentile(boots, [2.5, 97.5])
    return {"n_pairs": int(len(diffs)), "pct": float(np.exp(m) - 1), "lo": float(np.exp(lo) - 1), "hi": float(np.exp(hi) - 1)}


def robustness(df, feature):
    """Pre-specified robustness checks (R1-R6)."""
    out = {}
    out["R1_matched_pairs"] = matched_pairs(df, feature)
    out["R2_ppml_counts"] = _fit(df, "cites", feature, controls(feature), poisson=True)
    out["R3_influential"] = _fit(df, "y_infl", feature, controls(feature))
    cap = df.groupby("year").cites.transform(lambda s: s.quantile(0.99))
    out["R4_drop_top1pct"] = _fit(df[df.cites <= cap], "y", feature, controls(feature))
    out["R5_era_2017_21"] = _fit(df[df.year <= 2021], "y", feature, controls(feature))
    out["R5_era_2022_25"] = _fit(df[df.year >= 2022], "y", feature, controls(feature))
    out["R6_team_prior_2022_25"] = _fit(df[df.year >= 2022], "y", feature, controls(feature, ["lprior_acc"]))
    out["R7_year_plus_topic100_fe"] = _fit(df, "y", feature, controls(feature), fe="year + topic100")
    return out


def holm(pvals: dict) -> dict:
    keys = sorted(pvals, key=pvals.get)
    m, adj, run = len(keys), {}, 0.0
    for i, k in enumerate(keys):
        run = max(run, min(1.0, (m - i) * pvals[k]))
        adj[k] = run
    return adj


def verdict(prim, rob, p_holm):
    """Pre-registered decision rule."""
    pos = prim["pct"] > 0
    same = lambda r: r.get("pct") is not None and (r["pct"] > 0) == pos
    if p_holm < 0.05 and same(rob["R1_matched_pairs"]) and same(rob["R2_ppml_counts"]):
        return "more citations" if pos else "fewer citations"
    if prim["lo"] > -0.10 and prim["hi"] < 0.10:
        return "no meaningful difference (within +/-10%)"
    return "inconclusive"


def save(obj, name):
    OUT.mkdir(parents=True, exist_ok=True)
    json.dump(obj, open(OUT / name, "w"), indent=1, default=float)
