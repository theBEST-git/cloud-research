"""G5: title length and title informativeness vs citations among accepted ICLR papers 2017-2025.

Pre-registration: docs/CITES_PREREG.md. Frozen core: cites/core.py (not edited here).
Features (core.load):
  G5a_length5     = n_words / 5   (per +5 words); primary controls add G1_name (core.EXTRA_CONTROLS)
  G5b_informative = cosine(bge title emb, bge abstract emb), z-scored within year (per SD);
                    primary controls add G1_name and G5a_length5

What this module does
  1. Primary (pre-registered): reads the frozen estimates and Holm p from outputs/cites/primary.json and re-computes
     them with core.primary as a reproduction check (the frozen numbers are the ones reported).
  2. Robustness R1-R7 (pre-registered): core.robustness for each feature.
  3. Verdict (pre-registered rule): core.verdict(frozen primary, robustness, frozen Holm p).
  4. Secondary (pre-registered, prereg section 6; no multiplicity claim):
       - G5a length bins (<=6, 7-9, 10-12, 13-15, >=16 words) as dummies vs 10-12, controls core.controls('G5a_length5');
       - (all questions) joint model with all 8 primary features, for G5a and G5b;
       - (all questions) heterogeneity by LLM-topic papers, for G5a and G5b.
  5. Diagnostics (NOT pre-registered; every block is labelled so in results.json):
       (a) what G5b measures: within non-named (G1_name == 0) and within named titles; the named-minus-non-named
           difference; a name-masked variant (title vs name-masked abstract); lexical overlap and topic-keyword
           controls;
       (b) alternative informativeness measure: all-MiniLM-L6-v2 title-abstract cosine (z within year) in place of
           bge, primary spec + the full core.robustness battery, and a horse-race model with both;
       (c) S2 split-record / matching artefact: arXiv-id share and S2 match rate by within-year tercile (G5b and G5a);
           primary spec within arXiv / non-arXiv records, with an arXiv indicator, and the interacted difference;
       (d) R1 scale: reimplemented R1 pairing, the feature contrast inside the pairs, the primary estimate re-expressed
           at that contrast, and a pair-difference regression that adjusts for the other covariates;
       (e) shape of G5b: within-year quintile dummies vs the middle quintile; the bottom tail; trimming |z| > 3;
       (f) team prior: pre-registered R6 compared with R5 on the same 2022-25 sample.
       (g) adversarial audit (cites/audit_g5g6.py, added 2026-10-17): R1 calibration for continuous features (feature
           permuted within year; null of the R1 statistic and of the pair-difference slopes in (d)); alternative
           explanations (preprint timing, code links, paper type, tail, camera-ready retitling via WP4 v1 titles,
           combined); richer / non-bge content controls; the S2 split-record mechanism on WP4 audit pairs.

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m cites.g5
Writes outputs/cites/G5/{results.json, fig.png, fig.pdf, fig.csv}.
"""
from __future__ import annotations

import json
import warnings

import numpy as np
import pandas as pd
import pyfixest as pf
import statsmodels.api as sm
from scipy import stats
from sklearn.feature_extraction.text import CountVectorizer

from analyses import _core as C
from cites import core

warnings.filterwarnings("ignore")

FA, FB = "G5a_length5", "G5b_informative"
FEATS = [FA, FB]
DST = core.OUT / "G5"
DIAG = "diagnostic (not pre-registered)"
BINS = [(0, 6, "le6", "<=6 words"), (7, 9, "7_9", "7-9 words"), (10, 12, "10_12", "10-12 words (reference)"),
        (13, 15, "13_15", "13-15 words"), (16, 999, "ge16", ">=16 words")]
TOKEN_RX = r"(?u)\b[a-zA-Z][a-zA-Z0-9\-]{2,}\b"
N_TOPIC_KW = 30
ROB_LABEL = {
    "R1_matched_pairs": "R1 matched pairs (top vs bottom third)",
    "R2_ppml_counts": "R2 PPML on counts (sign check)",
    "R3_influential": "R3 influential citations",
    "R4_drop_top1pct": "R4 drop top 1% per year",
    "R5_era_2017_21": "R5 2017-21 only",
    "R5_era_2022_25": "R5 2022-25 only",
    "R6_team_prior_2022_25": "R6 2022-25 + team prior",
    "R7_year_plus_topic100_fe": "R7 year + topic100 FE",
}
UNIT = {FA: "per +5 words", FB: "per +1 SD (within year)"}


# --------------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------------
def share_ci(x: pd.Series) -> dict:
    x = x.astype(float)
    p, n = float(x.mean()), int(len(x))
    se = np.sqrt(p * (1 - p) / n) if n else np.nan
    return {"share": p, "lo": p - 1.96 * se, "hi": p + 1.96 * se, "n": n}


def lpm(r: dict) -> dict:
    """core._fit result for a 0/1 outcome as a linear-probability difference (percentage points per unit)."""
    return {"b_pp": 100 * r["b"], "lo_pp": 100 * (r["b"] - 1.96 * r["se"]), "hi_pp": 100 * (r["b"] + 1.96 * r["se"]),
            "se_pp": 100 * r["se"], "p": r["p"], "n": r["n"]}


def ratio(r: dict) -> dict:
    """Interaction coefficient as a ratio of two citation multipliers (per unit of the feature)."""
    return {"b": r["b"], "se": r["se"], "p": r["p"], "ratio": float(np.exp(r["b"])),
            "ratio_lo": float(np.exp(r["b"] - 1.96 * r["se"])), "ratio_hi": float(np.exp(r["b"] + 1.96 * r["se"])),
            "n": r["n"]}


def pct_from_b(b: float, se: float | None = None) -> dict:
    out = {"pct": float(np.exp(b) - 1)}
    if se is not None:
        out.update({"lo": float(np.exp(b - 1.96 * se) - 1), "hi": float(np.exp(b + 1.96 * se) - 1)})
    return out


def fmt(r: dict) -> str:
    if r.get("pct") is None:
        return "n/a"
    return f"{100 * r['pct']:+.1f}% [{100 * r['lo']:+.1f}, {100 * r['hi']:+.1f}]"


def zyear(df: pd.DataFrame, col: str) -> pd.Series:
    return df.groupby("year")[col].transform(lambda s: (s - s.mean()) / s.std())


def tercile(df: pd.DataFrame, col: str) -> pd.Series:
    """Within-year terciles with the same cut-offs as core.matched_pairs (pct rank >= 2/3 top, <= 1/3 bottom)."""
    q = df.groupby("year")[col].transform(lambda s: s.rank(pct=True))
    return pd.Series(np.where(q >= 2 / 3, "top", np.where(q <= 1 / 3, "bottom", "middle")), index=df.index)


def ctrl_wo(feature: str, drop: list[str], extra=()) -> list[str]:
    return [c for c in core.controls(feature, extra) if c not in drop]


def fit_interacted(d: pd.DataFrame, feature: str, group: str, fe: str) -> dict:
    """b(feature | group=1) - b(feature | group=0) from one pooled model; controls interacted with `group` and FE given
    by `fe` (pass a FE interacted with `group` to reproduce the split-sample estimates exactly)."""
    dd = d.copy()
    dd["F_x_grp"] = dd[feature] * dd[group]
    ctrl = [c for c in core.controls(feature) if c != group]
    for c in ctrl:
        dd[f"{c}_g"] = dd[c] * dd[group]
    return core._fit(dd, "y", "F_x_grp", ctrl + [feature] + [f"{c}_g" for c in ctrl], fe=fe)


def wald(fml: str, d: pd.DataFrame, terms: list[str]) -> dict:
    """Joint cluster-robust Wald test that all `terms` are 0 (chi2 and F with G-1 denominator df)."""
    m = pf.feols(fml, data=d, vcov={"CRV1": "topic50"})
    names = list(m._coefnames)
    idx = [names.index(t) for t in terms]
    b = np.asarray(m.coef())[idx]
    V = np.asarray(m._vcov)[np.ix_(idx, idx)]
    chi2 = float(b @ np.linalg.solve(V, b))
    k, G = len(terms), int(d.topic50.nunique())
    return {"chi2": chi2, "df": k, "p_chi2": float(stats.chi2.sf(chi2, k)),
            "F": chi2 / k, "df_denom": G - 1, "p_F": float(stats.f.sf(chi2 / k, k, G - 1))}


# --------------------------------------------------------------------------------------------
# pre-registered parts
# --------------------------------------------------------------------------------------------
def primary_block(df: pd.DataFrame, F: str) -> dict:
    frozen = json.load(open(core.OUT / "primary.json"))
    prim = frozen["primary"][F]
    rep = core.primary(df, F)
    diff = {k: abs(prim[k] - rep[k]) for k in ["b", "se", "p", "pct", "lo", "hi"]}
    ok = diff["b"] < 1e-8 and diff["se"] < 1e-8 and prim["n"] == rep["n"]
    return {"frozen": prim, "reproduced": rep, "max_abs_diff": max(diff.values()), "reproduction_ok": bool(ok),
            "n_papers_frame": int(len(df)), "n_papers_frozen": int(frozen["n_papers"]),
            "controls": core.controls(F), "fe": "year^topic50", "vcov": "CRV1 topic50", "unit": UNIT[F]}


def verdict_inputs(prim: dict, rob: dict, p_holm: float) -> dict:
    return {"p_holm": p_holm,
            "R1_sign_same": (rob["R1_matched_pairs"]["pct"] > 0) == (prim["pct"] > 0),
            "R2_sign_same": (rob["R2_ppml_counts"]["pct"] > 0) == (prim["pct"] > 0),
            "ci_within_10pct": bool(prim["lo"] > -0.10 and prim["hi"] < 0.10)}


def secondary_length_bins(df: pd.DataFrame, prim_a: dict) -> dict:
    """Pre-specified (prereg s6, G5a): length bins as dummies vs 10-12 words, controls core.controls('G5a_length5').
    One model with 4 dummies; each coefficient compares that bin with 10-12-word titles."""
    d = df.copy()
    for lo, hi, key, _ in BINS:
        d[f"len_{key}"] = d.n_words.between(lo, hi).astype(int)
    dums = [f"len_{k}" for _, _, k, _ in BINS if k != "10_12"]
    ctrl = core.controls(FA)
    out = {"reference": "10-12 words", "controls": ctrl, "model": "y ~ 4 bin dummies + core.controls('G5a_length5') "
           "| year^topic50, SE clustered by topic50 (the linear G5a term is replaced by the bins)"}
    ref_mean = float(d.loc[d.len_10_12 == 1, "n_words"].mean())
    for lo, hi, key, lab in BINS:
        col = f"len_{key}"
        sub = d[d[col] == 1]
        row = {"label": lab, "n_in_bin": int(len(sub)), "n_named": int(sub.G1_name.sum()), "mean_words": float(sub.n_words.mean()),
               "raw_mean_y": float(sub.y.mean()), "raw_median_cites": float(sub.cites.median())}
        if key != "10_12":
            r = core._fit(d, "y", col, ctrl + [x for x in dums if x != col])
            row.update(r)
            # what the pre-registered linear term implies for this bin's mean length vs the reference bin
            row["linear_implied_pct"] = float(np.exp(prim_a["b"] * (row["mean_words"] - ref_mean) / 5.0) - 1)
        out[key] = row
    fml = f"y ~ {' + '.join(dums)} + {' + '.join(ctrl)} | year^topic50"
    out["joint_wald_all_bins_zero"] = wald(fml, d, dums)
    return out


def secondary_joint(df: pd.DataFrame, F: str) -> dict:
    """Pre-specified (prereg s6, all questions): coefficient in a joint model with all 8 primary features."""
    ctrl = core.controls(F)
    others = [f for f in core.FEATURES if f != F and f not in ctrl]
    r = core._fit(df, "y", F, core.controls(F, others))
    r["model"] = "y ~ all 8 primary features + base controls | year^topic50"
    return r


def secondary_llm(df: pd.DataFrame, F: str) -> dict:
    """Pre-specified (prereg s6, all questions): heterogeneity by LLM-topic papers (continuous feature split by group)."""
    d = df.copy()
    d["llm"] = d.llm_topic.fillna(False).astype(int)
    d["F_in_llm"] = d[F] * d.llm
    d["F_in_nonllm"] = d[F] * (1 - d.llm)
    llm = core._fit(d, "y", "F_in_llm", core.controls(F, ["F_in_nonllm", "llm"]))
    non = core._fit(d, "y", "F_in_nonllm", core.controls(F, ["F_in_llm", "llm"]))
    inter = core._fit(d, "y", "F_in_llm", core.controls(F, [F, "llm"]))
    return {"llm_topic_papers": llm, "non_llm_topic_papers": non, "difference_llm_minus_non": ratio(inter),
            "n_llm_topic_papers": int(d.llm.sum()),
            "note": "One model with the feature split by llm_topic plus an llm_topic main effect; 'difference' is the "
                    "feature x llm_topic interaction, as a ratio of the two per-unit citation multipliers."}


# --------------------------------------------------------------------------------------------
# diagnostics (not pre-registered)
# --------------------------------------------------------------------------------------------
def masked_informativeness(df: pd.DataFrame) -> pd.Series:
    """cosine(bge title, bge name-masked abstract), z within year. The masked abstract replaces the title's lead
    segment and CamelCase / ALLCAPS tokens with '[NAME]'; 2017 has no masked embedding and keeps the unmasked one
    (as core.matched_pairs does)."""
    Et = C.load_embedding(df, "title", "bge-small-en-v1.5")
    Et /= np.linalg.norm(Et, axis=1, keepdims=True)
    Em, found = C.load_masked_embedding(df)
    Ea = C.load_embedding(df, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea).astype(np.float32)
    E /= np.linalg.norm(E, axis=1, keepdims=True)
    return pd.Series((Et * E).sum(1), index=df.index), found


def keyword_measures(df: pd.DataFrame) -> pd.DataFrame:
    """Lexical overlap (share of title content words that occur in the abstract) and topic-keyword share (share of
    title content words among the top-30 c-TF-IDF abstract words of the paper's topic50 cluster)."""
    cv = CountVectorizer(stop_words="english", token_pattern=TOKEN_RX, lowercase=True, min_df=5)
    X = cv.fit_transform(df.abstract.fillna(""))
    vocab = np.array(cv.get_feature_names_out())
    an = cv.build_analyzer()
    # c-TF-IDF per topic50
    topics = df.topic50.to_numpy()
    tops = np.unique(topics)
    tf = np.vstack([np.asarray(X[topics == t].sum(0)).ravel() for t in tops]).astype(float)
    A = tf.sum(1).mean()
    idf = np.log1p(A / np.maximum(tf.sum(0), 1))
    ctfidf = (tf / tf.sum(1, keepdims=True)) * idf
    kw = {t: set(vocab[np.argsort(-ctfidf[i])[:N_TOPIC_KW]]) for i, t in enumerate(tops)}
    lex, tkw, ntok = [], [], []
    for title, abst, t in zip(df.title, df.abstract.fillna(""), topics):
        tt = an(title)
        ntok.append(len(tt))
        if not tt:
            lex.append(np.nan)
            tkw.append(np.nan)
            continue
        aset = set(an(abst))
        lex.append(np.mean([w in aset for w in tt]))
        tkw.append(np.mean([w in kw[t] for w in tt]))
    out = pd.DataFrame({"lex_overlap": lex, "topic_kw_share": tkw, "n_content_tokens": ntok}, index=df.index)
    out.attrs["example_keywords"] = {int(t): sorted(kw[t])[:12] for t in tops[:5]}
    return out


def diag_what_g5b_measures(df: pd.DataFrame) -> dict:
    """(a) Is G5b just 'non-name title' or 'title contains topic keywords'?"""
    out = {"label": DIAG}
    d = df.copy()
    # descriptives
    out["mean_G5b"] = {"named": float(d.loc[d.G1_name == 1, FB].mean()), "not_named": float(d.loc[d.G1_name == 0, FB].mean())}
    m = core._fit(d, FB, "G1_name", [c for c in core.controls(FB) if c != "G1_name"])
    out["G5b_named_minus_not_primary_controls_sd"] = {"b": m["b"], "lo": m["b"] - 1.96 * m["se"],
                                                      "hi": m["b"] + 1.96 * m["se"], "p": m["p"]}
    # within subsets
    for key, sub in [("within_not_named", d[d.G1_name == 0]), ("within_named", d[d.G1_name == 1])]:
        r = core._fit(sub, "y", FB, ctrl_wo(FB, ["G1_name"]))
        r["n_group"] = int(len(sub))
        out[key] = r
    out["difference_named_minus_not"] = ratio(fit_interacted(d, FB, "G1_name", fe="year^topic50^G1_name"))
    out["difference_named_minus_not"]["model"] = ("G5b x G1_name; controls and year^topic50 FE interacted with G1_name "
                                                  "(reproduces the two within-group estimates)")
    out["difference_named_minus_not_shared_fe"] = ratio(fit_interacted(d, FB, "G1_name", fe="year^topic50"))

    # name-masked variant
    raw, found = masked_informativeness(d)
    d["cos_masked"] = raw
    d["G5b_masked"] = zyear(d, "cos_masked")
    out["masked"] = {
        "n_with_masked_embedding": int(found.sum()), "n_2017_unmasked": int((~found).sum()),
        "corr_with_G5b": float(np.corrcoef(d.G5b_masked, d[FB])[0, 1]),
        "corr_with_G5b_named": float(np.corrcoef(d.loc[d.G1_name == 1, "G5b_masked"], d.loc[d.G1_name == 1, FB])[0, 1]),
        "corr_with_G5b_not_named": float(np.corrcoef(d.loc[d.G1_name == 0, "G5b_masked"], d.loc[d.G1_name == 0, FB])[0, 1]),
        "mean_named": float(d.loc[d.G1_name == 1, "G5b_masked"].mean()),
        "mean_not_named": float(d.loc[d.G1_name == 0, "G5b_masked"].mean()),
        "primary_spec": core._fit(d, "y", "G5b_masked", core.controls(FB)),
        "within_not_named": core._fit(d[d.G1_name == 0], "y", "G5b_masked", ctrl_wo(FB, ["G1_name"])),
        "within_named": core._fit(d[d.G1_name == 1], "y", "G5b_masked", ctrl_wo(FB, ["G1_name"])),
    }
    # keyword measures
    K = keyword_measures(d)
    d = d.join(K)
    ok = d.lex_overlap.notna()
    out["keywords"] = {
        "definition": {"lex_overlap": "share of title content words (sklearn English stop words removed, >=3 chars) "
                                      "that also occur in the abstract",
                       "topic_kw_share": f"share of title content words among the top {N_TOPIC_KW} c-TF-IDF abstract "
                                         "words of the paper's topic50 cluster (cluster keywords include the paper's own "
                                         "abstract)"},
        "n_missing_no_content_tokens": int((~ok).sum()),
        "mean": {"lex_overlap": float(d.lex_overlap.mean()), "topic_kw_share": float(d.topic_kw_share.mean())},
        "corr_with_G5b": {"lex_overlap": float(d.loc[ok, ["lex_overlap", FB]].corr().iloc[0, 1]),
                          "topic_kw_share": float(d.loc[ok, ["topic_kw_share", FB]].corr().iloc[0, 1])},
        "example_topic_keywords": K.attrs["example_keywords"],
    }
    dk = d[ok].copy()
    dk["lex_z"] = zyear(dk, "lex_overlap")
    dk["tkw_z"] = zyear(dk, "topic_kw_share")
    out["keywords"]["G5b_same_sample_no_keyword_controls"] = core._fit(dk, "y", FB, core.controls(FB))
    out["keywords"]["G5b_plus_lex_overlap"] = core._fit(dk, "y", FB, core.controls(FB, ["lex_z"]))
    out["keywords"]["G5b_plus_topic_kw_share"] = core._fit(dk, "y", FB, core.controls(FB, ["tkw_z"]))
    out["keywords"]["G5b_plus_both"] = core._fit(dk, "y", FB, core.controls(FB, ["lex_z", "tkw_z"]))
    out["keywords"]["lex_overlap_coef_given_G5b"] = core._fit(dk, "y", "lex_z", core.controls(FB, [FB, "tkw_z"]))
    out["keywords"]["topic_kw_coef_given_G5b"] = core._fit(dk, "y", "tkw_z", core.controls(FB, [FB, "lex_z"]))
    out["keywords"]["lex_overlap_alone_primary_controls"] = core._fit(dk, "y", "lex_z", core.controls(FB))
    out["keywords"]["topic_kw_alone_primary_controls"] = core._fit(dk, "y", "tkw_z", core.controls(FB))

    # topic centrality: is 'uses the cluster's keywords' a content (abstract) property or a title property?
    Ea = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    Et = C.load_embedding(d, "title", "bge-small-en-v1.5")
    Ea /= np.linalg.norm(Ea, axis=1, keepdims=True)
    Et /= np.linalg.norm(Et, axis=1, keepdims=True)
    cent = pd.DataFrame(Ea).groupby(d.topic50.to_numpy()).mean()
    Cm = np.array(cent.loc[d.topic50.to_numpy()].to_numpy(), dtype=np.float32, copy=True)
    Cm /= np.linalg.norm(Cm, axis=1, keepdims=True)
    d["abs_central"] = (Ea * Cm).sum(1)
    d["title_central"] = (Et * Cm).sum(1)
    d["abs_central_z"] = zyear(d, "abs_central")
    d["title_central_z"] = zyear(d, "title_central")
    dk = dk.join(d[["abs_central_z", "title_central_z"]])
    out["centrality"] = {
        "definition": "cosine of the bge abstract (abs_central) or bge title (title_central) embedding to the mean bge "
                      "abstract embedding of the paper's topic50 cluster (in-sample, own paper included), z within year",
        "corr": {"G5b_abs_central": float(np.corrcoef(d[FB], d.abs_central_z)[0, 1]),
                 "G5b_title_central": float(np.corrcoef(d[FB], d.title_central_z)[0, 1]),
                 "topic_kw_abs_central": float(dk[["tkw_z", "abs_central_z"]].corr().iloc[0, 1]),
                 "topic_kw_title_central": float(dk[["tkw_z", "title_central_z"]].corr().iloc[0, 1])},
        "abs_central_alone_primary_controls": core._fit(d, "y", "abs_central_z", core.controls(FB)),
        "title_central_alone_primary_controls": core._fit(d, "y", "title_central_z", core.controls(FB)),
        "G5b_plus_abs_central": core._fit(d, "y", FB, core.controls(FB, ["abs_central_z"])),
        "G5b_plus_title_central": core._fit(d, "y", FB, core.controls(FB, ["title_central_z"])),
        "G5b_plus_abs_and_title_central": core._fit(d, "y", FB, core.controls(FB, ["abs_central_z", "title_central_z"])),
        "topic_kw_plus_abs_central": core._fit(dk, "y", "tkw_z", core.controls(FB, [FB, "abs_central_z"])),
        "G5b_plus_topic_kw_and_abs_central": core._fit(dk, "y", FB, core.controls(FB, ["tkw_z", "abs_central_z"])),
        "title_central_given_abs_central": core._fit(d, "y", "title_central_z", core.controls(FB, ["abs_central_z"])),
    }
    return out


def diag_minilm(df: pd.DataFrame, prim_b: dict) -> dict:
    """(b) Alternative informativeness measure: all-MiniLM-L6-v2 title-abstract cosine, z within year."""
    out = {"label": DIAG}
    d = df.copy()
    Et = C.load_embedding(d, "title", "all-MiniLM-L6-v2")
    Ea = C.load_embedding(d, "abstract", "all-MiniLM-L6-v2")
    Et /= np.linalg.norm(Et, axis=1, keepdims=True)
    Ea /= np.linalg.norm(Ea, axis=1, keepdims=True)
    d["cos_minilm"] = (Et * Ea).sum(1)
    d["G5b_minilm"] = zyear(d, "cos_minilm")
    within = d.groupby("year").apply(lambda g: g[[FB, "G5b_minilm"]].corr().iloc[0, 1])
    t_bge, t_ml = tercile(d, FB), tercile(d, "G5b_minilm")
    out["agreement"] = {"pearson": float(np.corrcoef(d[FB], d.G5b_minilm)[0, 1]),
                        "spearman": float(stats.spearmanr(d[FB], d.G5b_minilm).statistic),
                        "pearson_within_year_min": float(within.min()), "pearson_within_year_max": float(within.max()),
                        "tercile_agreement": float((t_bge == t_ml).mean()),
                        "top_bge_in_bottom_minilm": float(((t_bge == "top") & (t_ml == "bottom")).sum() / (t_bge == "top").sum())}
    out["primary_spec"] = core._fit(d, "y", "G5b_minilm", core.controls(FB))
    # full pre-registered robustness battery on the alternative measure (column swapped so core.controls applies)
    dd = df.copy()
    dd[FB] = d.G5b_minilm
    rob = core.robustness(dd, FB)
    out["robustness"] = rob
    out["rule_signs"] = {"R1_sign_same": (rob["R1_matched_pairs"]["pct"] > 0) == (out["primary_spec"]["pct"] > 0),
                         "R2_sign_same": (rob["R2_ppml_counts"]["pct"] > 0) == (out["primary_spec"]["pct"] > 0),
                         "note": "Holm is not applied: the alternative measure is not in the pre-registered family."}
    # horse race
    out["horse_race_bge_given_minilm"] = core._fit(d, "y", FB, core.controls(FB, ["G5b_minilm"]))
    out["horse_race_minilm_given_bge"] = core._fit(d, "y", "G5b_minilm", core.controls(FB, [FB]))
    out["within_not_named"] = core._fit(d[d.G1_name == 0], "y", "G5b_minilm", ctrl_wo(FB, ["G1_name"]))
    out["within_named"] = core._fit(d[d.G1_name == 1], "y", "G5b_minilm", ctrl_wo(FB, ["G1_name"]))
    out["corr_with_G5a_length"] = {"bge": float(np.corrcoef(d[FB], d[FA])[0, 1]),
                                   "minilm": float(np.corrcoef(d.G5b_minilm, d[FA])[0, 1])}
    out["R1_scale"] = pair_scale(dd, FB, out["primary_spec"], rob["R1_matched_pairs"])
    out["mean_named"] = float(d.loc[d.G1_name == 1, "G5b_minilm"].mean())
    out["mean_not_named"] = float(d.loc[d.G1_name == 0, "G5b_minilm"].mean())
    return out


def diag_arxiv(df: pd.DataFrame) -> dict:
    """(c) S2 split-record / matching artefact. Venue records without an arXiv id can miss citations credited to a
    separate arXiv record (qc_split_records.jsonl). If that share differed by tercile it would bias the estimates."""
    out = {"label": DIAG}
    d = df.copy()
    d["has_arxiv"] = d.arxiv.notna().astype(int)
    out["arxiv_share_overall"] = float(d.has_arxiv.mean())
    for F in FEATS:
        t = tercile(d, F)
        blk = {"by_tercile": {k: share_ci(d.loc[t == k, "has_arxiv"]) for k in ["bottom", "middle", "top"]},
               "arxiv_on_feature_primary_controls_pp": lpm(core._fit(d, "has_arxiv", F, core.controls(F)))}
        blk["top_minus_bottom_pp"] = 100 * (blk["by_tercile"]["top"]["share"] - blk["by_tercile"]["bottom"]["share"])
        a1, a0 = d[d.has_arxiv == 1], d[d.has_arxiv == 0]
        blk["primary_spec_arxiv_only"] = core._fit(a1, "y", F, core.controls(F))
        blk["primary_spec_no_arxiv_only"] = core._fit(a0, "y", F, core.controls(F))
        blk["primary_spec_plus_arxiv_control"] = core._fit(d, "y", F, core.controls(F, ["has_arxiv"]))
        others = [f for f in core.FEATURES if f != F and f not in core.controls(F)]
        blk["joint_model_plus_arxiv_control"] = core._fit(d, "y", F, core.controls(F, others + ["has_arxiv"]))
        blk["has_arxiv_coef_on_y"] = core._fit(d, "y", "has_arxiv", core.controls(F, [F]))
        d["no_arxiv"] = 1 - d.has_arxiv
        inter = ratio(fit_interacted(d, F, "no_arxiv", fe="year^topic50^has_arxiv"))
        inter["model"] = "feature x no-arXiv; controls and year^topic50 FE interacted with arXiv status (as in G1/G4)"
        blk["difference_no_arxiv_minus_arxiv"] = inter
        out[F] = blk

    # S2 match rate by tercile, all accepted papers 2017-25 (unmatched ones are not in the analysis frame)
    M = pd.read_parquet(core.OUT / "matched_venue.parquet", columns=["submission_id", "year", "matched"])
    M = M[M.year.between(*core.YEARS)]
    U = C.load_universe(["submission_id", "emb_row"])
    Fw = C.load_features(["n_words"])
    M = M.merge(U, on="submission_id", how="left", validate="1:1").merge(Fw, on="submission_id", how="left", validate="1:1")
    out["accepted_2017_25"] = int(len(M))
    out["accepted_missing_emb_or_length"] = int((M.emb_row.isna() | M.n_words.isna()).sum())
    M = M[M.emb_row.notna() & M.n_words.notna()].reset_index(drop=True)
    M["emb_row"] = M.emb_row.astype(int)
    Et = C.load_embedding(M, "title", "bge-small-en-v1.5")
    Ea = C.load_embedding(M, "abstract", "bge-small-en-v1.5")
    Et /= np.linalg.norm(Et, axis=1, keepdims=True)
    Ea /= np.linalg.norm(Ea, axis=1, keepdims=True)
    M["G5b_all"] = (Et * Ea).sum(1)
    M["G5a_all"] = M.n_words / 5.0
    M["matched_i"] = M.matched.astype(int)
    mr = {}
    for col, key in [("G5b_all", FB), ("G5a_all", FA)]:
        t = tercile(M, col)
        mr[key] = {k: share_ci(M.loc[t == k, "matched_i"]) for k in ["bottom", "middle", "top"]}
        M["z"] = zyear(M, col)
        m = pf.feols("matched_i ~ z | year", data=M, vcov="hetero")
        tt = m.tidy().loc["z"]
        b, se = float(tt["Estimate"]), float(tt["Std. Error"])
        mr[key]["match_on_z_year_fe_pp_per_sd"] = {"b_pp": 100 * b, "lo_pp": 100 * (b - 1.96 * se),
                                                   "hi_pp": 100 * (b + 1.96 * se), "p": float(tt["Pr(>|t|)"])}
    out["match_rate_by_tercile"] = mr
    out["match_rate_note"] = "terciles within year over all accepted papers 2017-25 (bge cosine / word count)"
    return out


def r1_pairs(df: pd.DataFrame, feature: str, caliper: float = 0.80):
    """Reimplementation of core.matched_pairs pairing for continuous features; returns frame and pair indices."""
    d = df.reset_index(drop=True)
    q = d.groupby("year")[feature].transform(lambda s: s.rank(pct=True))
    tr, co = q >= 2 / 3, q <= 1 / 3
    Em, found = C.load_masked_embedding(d)
    Ea = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea)
    E = E / np.linalg.norm(E, axis=1, keepdims=True)
    T, Cc = [], []
    for y in sorted(d.year.unique()):
        ti = np.where(tr & (d.year == y))[0]
        ci = np.where(co & (d.year == y))[0]
        if len(ti) == 0 or len(ci) == 0:
            continue
        S = E[ti] @ E[ci].T
        j = S.argmax(1)
        ok = S[np.arange(len(ti)), j] >= caliper
        T += list(ti[ok])
        Cc += list(ci[j[ok]])
    return d, np.array(T), np.array(Cc)


def pair_scale(df: pd.DataFrame, F: str, prim: dict, r1: dict) -> dict:
    """R1 pairs for feature column F: reproduction of core R1, feature contrast in the pairs, the primary estimate at
    that contrast, and pair-difference regressions adjusting for the covariates R1 leaves unmatched."""
    d, T, Cc = r1_pairs(df, F)
    d["has_arxiv"] = d.arxiv.notna().astype(int)
    y = d.y.to_numpy()
    dy = y[T] - y[Cc]
    blk = {"n_pairs": int(len(T)), "reimplemented_pct": float(np.exp(dy.mean()) - 1),
           "core_R1_pct": r1["pct"], "core_R1_n_pairs": r1["n_pairs"]}
    blk["reproduces_core_R1"] = bool(blk["n_pairs"] == blk["core_R1_n_pairs"]
                                     and abs(blk["reimplemented_pct"] - blk["core_R1_pct"]) < 1e-10)
    dx = d[F].to_numpy()[T] - d[F].to_numpy()[Cc]
    blk["mean_feature_contrast_in_pairs"] = float(dx.mean())
    blk["primary_at_pair_contrast"] = pct_from_b(prim["b"] * dx.mean(), prim["se"] * dx.mean())
    covs = ["log_authors", "log_abs_words"] + list(core.EXTRA_CONTROLS.get(F, []))
    diff = lambda c: d[c].to_numpy()[T] - d[c].to_numpy()[Cc]
    blk["mean_cov_diff_in_pairs"] = {c: float(diff(c).mean()) for c in covs + ["has_arxiv"]}
    for tag, cv in [("", covs), ("_plus_arxiv", covs + ["has_arxiv"])]:
        Z = pd.DataFrame({f"d_{c}": diff(c) for c in cv})
        # (i) intercept = within-pair difference at zero covariate differences (SE clustered by the control paper)
        m1 = sm.OLS(dy, sm.add_constant(Z)).fit(cov_type="cluster", cov_kwds={"groups": Cc})
        blk[f"adjusted_pair_difference{tag}"] = {**pct_from_b(m1.params["const"], m1.bse["const"]),
                                                 "p": float(m1.pvalues["const"]), "covariates": cv}
        # (ii) pair-difference model, no intercept: per-unit slope on the feature, comparable to the primary
        Z2 = Z.copy()
        Z2.insert(0, "d_feature", dx)
        m2 = sm.OLS(dy, Z2).fit(cov_type="cluster", cov_kwds={"groups": Cc})
        blk[f"pair_difference_slope_per_unit{tag}"] = {**pct_from_b(m2.params["d_feature"], m2.bse["d_feature"]),
                                                       "p": float(m2.pvalues["d_feature"]), "unit": UNIT[F],
                                                       "covariates": cv}
    return blk


def diag_r1_scale(df: pd.DataFrame, prims: dict, robs: dict) -> dict:
    """(d) R1 compares top with bottom within-year terciles, not a 1-unit change. Put R1 and the primary on one scale,
    and adjust the within-pair difference for the covariates R1 leaves unmatched (team size, abstract length, G1, G5a,
    and, as a further variant, arXiv-id status)."""
    out = {"label": DIAG,
           "audit_note": "The R1 pairing is shifted downward when there is no association (see g_audit.r1_null). The "
                         "no-intercept 'pair_difference_slope_per_unit' absorbs that shift and is biased toward a negative "
                         "slope (null means: g_audit.r1_null.<feature>.null.slope_no_intercept_null_mean_pct); use the "
                         "null-corrected or with-intercept slopes in g_audit.r1_null instead."}
    for F in FEATS:
        out[F] = pair_scale(df, F, prims[F], robs[F]["R1_matched_pairs"])
    return out


def diag_audit(df: pd.DataFrame, robs: dict, minilm_r1: dict) -> dict:
    """(g) Adversarial-audit diagnostics (cites/audit_g5g6.py)."""
    from cites import audit_g5g6 as AU
    out = {"label": AU.LABEL}
    cov = lambda F: ["log_authors", "log_abs_words"] + list(core.EXTRA_CONTROLS.get(F, []))
    dd = df.copy()
    dd[FB] = AU.minilm_informativeness(df)
    out["r1_null"] = {FA: AU.r1_null_continuous(df, FA, cov(FA), robs[FA]["R1_matched_pairs"], unit=UNIT[FA]),
                      FB: AU.r1_null_continuous(df, FB, cov(FB), robs[FB]["R1_matched_pairs"], unit=UNIT[FB]),
                      "G5b_minilm": AU.r1_null_continuous(dd, FB, cov(FB), minilm_r1, unit=UNIT[FB] + " (MiniLM measure)")}
    out["r1_null"]["G5b_minilm"]["feature"] = "G5b_minilm"
    v1 = AU.v1_frame(df)
    out["alt_explanations"] = {F: AU.alt_explanations(df, F, False, v1) for F in FEATS}
    out["content_controls"] = AU.content_controls(df, FEATS)
    out["split_record_mechanism"] = AU.split_record_mechanism(df)
    return out


def diag_shape(df: pd.DataFrame) -> dict:
    """(e) Shape of G5b: within-year quintile dummies vs the middle quintile; bottom tail; trimming."""
    out = {"label": DIAG}
    d = df.copy()
    q = d.groupby("year")[FB].transform(lambda s: s.rank(pct=True))
    d["q5"] = np.minimum((q * 5).apply(np.ceil).astype(int), 5)
    for k in [1, 2, 4, 5]:
        d[f"q_{k}"] = (d.q5 == k).astype(int)
    dums = ["q_1", "q_2", "q_4", "q_5"]
    for k in [1, 2, 3, 4, 5]:
        row = {"n_in_bin": int((d.q5 == k).sum()), "mean_cos": float(d.loc[d.q5 == k, "title_abs_cos"].mean()),
               "mean_G5b": float(d.loc[d.q5 == k, FB].mean())}
        if k != 3:
            row.update(core._fit(d, "y", f"q_{k}", core.controls(FB, [x for x in dums if x != f"q_{k}"])))
        out[f"Q{k}"] = row
    out["reference"] = "Q3 (middle fifth within year)"
    fml = f"y ~ {' + '.join(dums)} + {' + '.join(core.controls(FB))} | year^topic50"
    out["joint_wald_all_quintiles_zero"] = wald(fml, d, dums)
    low = d.nsmallest(8, FB)[["year", "title", "title_abs_cos", FB]]
    out["lowest_8_titles"] = low.round(3).to_dict(orient="records")
    out["n_abs_z_gt_3"] = int((d[FB].abs() > 3).sum())
    out["trim_abs_z_gt_3"] = core._fit(d[d[FB].abs() <= 3], "y", FB, core.controls(FB))
    return out


def diag_team_prior(df: pd.DataFrame, robs: dict) -> dict:
    """(f) Team prior: R6 (pre-registered) against R5 2022-25 (same sample, no team-prior control)."""
    d = df[df.year >= 2022]
    out = {"label": DIAG + " - comparison of two pre-registered checks", "n_2022_25": int(len(d))}
    for F in FEATS:
        r5, r6 = robs[F]["R5_era_2022_25"], robs[F]["R6_team_prior_2022_25"]
        out[F] = {"R5_2022_25_no_team_prior": r5, "R6_2022_25_with_team_prior": r6, "change_in_b": r6["b"] - r5["b"],
                  "corr_feature_lprior_acc": float(np.corrcoef(d[F], d.lprior_acc)[0, 1])}
    return out


# --------------------------------------------------------------------------------------------
# figure
# --------------------------------------------------------------------------------------------
def figure(prims: dict, robs: dict) -> dict:
    import matplotlib.pyplot as plt  # noqa: F401
    keys = ["primary"] + list(ROB_LABEL)
    labels = ["Primary"] + [ROB_LABEL[k] for k in ROB_LABEL]
    fig, axes = C.new_fig(width=7.0, height=3.5, ncols=2, sharey=True, gridspec_kw={"wspace": 0.08})
    ypos = np.arange(len(keys))[::-1]
    rows = []
    titles = {FA: "Title length, per +5 words", FB: "Title informativeness, per +1 SD"}
    for ax, F in zip(axes, FEATS):
        rs = [prims[F]] + [robs[F][k] for k in ROB_LABEL]
        est = np.array([100 * r["pct"] for r in rs])
        lo = np.array([100 * r["lo"] for r in rs])
        hi = np.array([100 * r["hi"] for r in rs])
        ax.axvspan(-10, 10, color=C.GRID, alpha=0.55, lw=0, zorder=0)
        ax.axvline(0, color=C.TEXT2, lw=0.8, zorder=1)
        for yv, e, l_, h, k in zip(ypos, est, lo, hi, keys):
            c = C.COLORS[0] if k == "primary" else C.TEXT2
            ax.plot([l_, h], [yv, yv], color=c, lw=2.0, solid_capstyle="round", zorder=2)
            if k == "R1_matched_pairs":  # different contrast (top vs bottom tercile): open marker
                ax.plot([e], [yv], "o", color=C.BG, mec=c, mew=1.5, ms=6, zorder=3)
            else:
                ax.plot([e], [yv], "o", color=c, ms=7 if k == "primary" else 5.5, mec=C.BG, mew=1.2, zorder=3)
            rows.append({"feature": F, "row": k, "pct": e, "lo": l_, "hi": h})
        f_ = lambda v: f"{v:+.1f}"
        ax.annotate(f"{f_(est[0])}%  [{f_(lo[0])}, {f_(hi[0])}]", (est[0], ypos[0]), xytext=(0, 9),
                    textcoords="offset points", ha="center", va="bottom", fontsize=7.5, color=C.TEXT, fontweight="bold")
        xmin, xmax = min(lo.min(), -10) - 4, max(hi.max(), 10) + 4
        ax.set_xlim(xmin, xmax)
        step = 10 if xmax - xmin <= 60 else 20
        ticks = [t for t in np.arange(-100, 201, step) if xmin <= t <= xmax]
        ax.set_xticks(ticks)
        ax.set_xticklabels([f"{t:+.0f}%" if t else "0" for t in ticks])
        ax.set_title(titles[F], loc="left", fontsize=9, pad=14)
        ax.spines["left"].set_visible(False)
        ax.grid(axis="y", visible=False)
        ax.tick_params(axis="y", length=0)
        ax.text(0, -0.95, "±10%", ha="center", va="top", fontsize=6.5, color=C.TEXT2)
    axes[0].set_yticks(ypos, labels)
    for t in axes[0].get_yticklabels():
        t.set_fontweight("bold" if t.get_text() == "Primary" else "normal")
    axes[0].set_ylim(-1.3, ypos[0] + 0.9)
    fig.supxlabel("Difference in citations, accepted ICLR papers 2017-25 (95% CI)", fontsize=8.5, y=-0.02)
    return C.save_fig(fig, "fig", DST, data=pd.DataFrame(rows))


# --------------------------------------------------------------------------------------------
def main():
    DST.mkdir(parents=True, exist_ok=True)
    df = core.load()
    P, prims, robs, verdicts, vin = {}, {}, {}, {}, {}
    for F in FEATS:
        P[F] = primary_block(df, F)
        prims[F] = P[F]["frozen"]
        robs[F] = core.robustness(df, F)
        verdicts[F] = core.verdict(prims[F], robs[F], prims[F]["p_holm"])
        vin[F] = verdict_inputs(prims[F], robs[F], prims[F]["p_holm"])
    res = {
        "question": "G5: among accepted ICLR papers 2017-2025, do papers with longer titles (G5a, per +5 words) or more "
                    "informative titles (G5b, title-abstract bge cosine, per SD within year) receive more or fewer "
                    "Semantic Scholar citations than papers with similar content?",
        "outcome": "y = log(1 + Semantic Scholar citationCount, retrieved 2026-10-17); % difference = exp(b) - 1",
        "features": {F: {"label": core.FEATURES[F], "unit": UNIT[F], "primary": P[F], "robustness": robs[F],
                         "verdict": verdicts[F], "verdict_inputs": vin[F]} for F in FEATS},
        "secondary_prespecified": {
            "G5a_length_bins": secondary_length_bins(df, prims[FA]),
            "joint_model_8_features": {F: secondary_joint(df, F) for F in FEATS},
            "llm_topic_heterogeneity": {F: secondary_llm(df, F) for F in FEATS},
        },
        "diagnostics_not_preregistered": {
            "label": DIAG,
            "a_what_G5b_measures": diag_what_g5b_measures(df),
            "b_minilm_alternative": diag_minilm(df, prims[FB]),
            "c_arxiv_and_match_rate": diag_arxiv(df),
            "d_R1_scale": diag_r1_scale(df, prims, robs),
            "e_G5b_shape": diag_shape(df),
            "f_team_prior": diag_team_prior(df, robs),
        },
    }
    D_ = res["diagnostics_not_preregistered"]
    D_["g_audit"] = diag_audit(df, robs, D_["b_minilm_alternative"]["robustness"]["R1_matched_pairs"])
    res["figure"] = {k: str(v) for k, v in figure(prims, robs).items()}
    json.dump(res, open(DST / "results.json", "w"), indent=1, default=float)

    # console summary
    for F in FEATS:
        p = prims[F]
        print(f"== {F}: reproduction ok {P[F]['reproduction_ok']} max|diff| {P[F]['max_abs_diff']:.2e}")
        print(f"primary {fmt(p)}  p {p['p']:.3g} holm {p['p_holm']:.3g} n {p['n']}")
        for k in ROB_LABEL:
            r = robs[F][k]
            extra = f"n_pairs {r['n_pairs']}" if "n_pairs" in r else f"p {r['p']:.3g} n {r['n']}"
            print(f"  {k:26s} {fmt(r)}  {extra}")
        print("verdict:", verdicts[F], vin[F])
    S = res["secondary_prespecified"]
    B = S["G5a_length_bins"]
    for _, _, k, lab in BINS:
        r = B[k]
        print(f"  bin {lab:24s} n {r['n_in_bin']:5d} named {r['n_named']:4d} mean {r['mean_words']:.1f}",
              (fmt(r) + f" p {r['p']:.3g} linear-implied {100 * r['linear_implied_pct']:+.1f}%") if "pct" in r else "")
    print("  bins wald", B["joint_wald_all_bins_zero"])
    for F in FEATS:
        J = S["joint_model_8_features"][F]
        L = S["llm_topic_heterogeneity"][F]
        print(F, "joint", fmt(J), f"p {J['p']:.3g}", "| llm", fmt(L["llm_topic_papers"]), "non", fmt(L["non_llm_topic_papers"]),
              "ratio", {k: round(v, 3) for k, v in L["difference_llm_minus_non"].items()})
    D = res["diagnostics_not_preregistered"]
    A = D["a_what_G5b_measures"]
    print("(a) mean G5b", A["mean_G5b"], "named-not sd", {k: round(v, 3) for k, v in A["G5b_named_minus_not_primary_controls_sd"].items()})
    print("    within not named", fmt(A["within_not_named"]), A["within_not_named"]["n"], "| named", fmt(A["within_named"]),
          A["within_named"]["n"], "| diff", {k: round(v, 3) for k, v in A["difference_named_minus_not"].items() if isinstance(v, float)},
          "| shared fe", {k: round(v, 3) for k, v in A["difference_named_minus_not_shared_fe"].items()})
    Mk = A["masked"]
    print("    masked corr", round(Mk["corr_with_G5b"], 3), round(Mk["corr_with_G5b_named"], 3), round(Mk["corr_with_G5b_not_named"], 3),
          "means", round(Mk["mean_named"], 3), round(Mk["mean_not_named"], 3), "| primary", fmt(Mk["primary_spec"]),
          "| not named", fmt(Mk["within_not_named"]), "| named", fmt(Mk["within_named"]))
    Kw = A["keywords"]
    print("    kw", Kw["mean"], Kw["corr_with_G5b"], "missing", Kw["n_missing_no_content_tokens"])
    for k in ["G5b_same_sample_no_keyword_controls", "G5b_plus_lex_overlap", "G5b_plus_topic_kw_share", "G5b_plus_both",
              "lex_overlap_coef_given_G5b", "topic_kw_coef_given_G5b", "lex_overlap_alone_primary_controls",
              "topic_kw_alone_primary_controls"]:
        print(f"      {k:40s} {fmt(Kw[k])} p {Kw[k]['p']:.3g}")
    Ce = A["centrality"]
    print("    centrality corr", {k: round(v, 3) for k, v in Ce["corr"].items()})
    for k, r in Ce.items():
        if isinstance(r, dict) and "pct" in r:
            print(f"      {k:40s} {fmt(r)} p {r['p']:.3g}")
    Mi = D["b_minilm_alternative"]
    print("(b) agreement", {k: round(v, 3) for k, v in Mi["agreement"].items()}, "| primary", fmt(Mi["primary_spec"]),
          f"p {Mi['primary_spec']['p']:.3g}")
    for k in ROB_LABEL:
        r = Mi["robustness"][k]
        print(f"      {k:26s} {fmt(r)}")
    print("    horse race bge|minilm", fmt(Mi["horse_race_bge_given_minilm"]), "minilm|bge", fmt(Mi["horse_race_minilm_given_bge"]),
          "| not named", fmt(Mi["within_not_named"]), "| named", fmt(Mi["within_named"]))
    Ax = D["c_arxiv_and_match_rate"]
    for F in FEATS:
        b = Ax[F]
        print(f"(c) {F} arxiv by tercile", {k: round(v["share"], 4) for k, v in b["by_tercile"].items()},
              "top-bottom pp", round(b["top_minus_bottom_pp"], 2), "lpm", {k: round(v, 3) for k, v in b["arxiv_on_feature_primary_controls_pp"].items()})
        print("    arxiv only", fmt(b["primary_spec_arxiv_only"]), b["primary_spec_arxiv_only"]["n"], "| no arxiv",
              fmt(b["primary_spec_no_arxiv_only"]), b["primary_spec_no_arxiv_only"]["n"], "| +ctrl", fmt(b["primary_spec_plus_arxiv_control"]),
              "| diff", {k: round(v, 3) for k, v in b["difference_no_arxiv_minus_arxiv"].items() if isinstance(v, float)})
        print("    joint+arxiv ctrl", fmt(b["joint_model_plus_arxiv_control"]), f"p {b['joint_model_plus_arxiv_control']['p']:.3g}",
              "| arxiv coef on y", fmt(b["has_arxiv_coef_on_y"]))
        mr = Ax["match_rate_by_tercile"][F]
        print("    match rate", {k: round(mr[k]["share"], 4) for k in ["bottom", "middle", "top"]},
              {k: round(v, 3) for k, v in mr["match_on_z_year_fe_pp_per_sd"].items()})
    R = D["d_R1_scale"]
    print("    minilm corr with length", {k: round(v, 3) for k, v in Mi["corr_with_G5a_length"].items()})
    for F, b in [(FA, R[FA]), (FB, R[FB]), ("G5b_minilm", Mi["R1_scale"])]:
        print(f"(d) {F} pairs {b['n_pairs']} reproduces {b['reproduces_core_R1']} contrast {b['mean_feature_contrast_in_pairs']:.3f}",
              "primary@contrast", fmt(b["primary_at_pair_contrast"]), "| adj diff", fmt(b["adjusted_pair_difference"]),
              "| slope/unit", fmt(b["pair_difference_slope_per_unit"]), "| +arxiv adj", fmt(b["adjusted_pair_difference_plus_arxiv"]),
              "slope", fmt(b["pair_difference_slope_per_unit_plus_arxiv"]),
              "| covdiff", {k: round(v, 3) for k, v in b["mean_cov_diff_in_pairs"].items()})
    Sh = D["e_G5b_shape"]
    for k in [1, 2, 3, 4, 5]:
        r = Sh[f"Q{k}"]
        print(f"(e) Q{k} n {r['n_in_bin']} cos {r['mean_cos']:.3f}", fmt(r) if "pct" in r else "ref")
    print("    wald", Sh["joint_wald_all_quintiles_zero"], "trim", fmt(Sh["trim_abs_z_gt_3"]), Sh["n_abs_z_gt_3"])
    for r in Sh["lowest_8_titles"]:
        print("     ", r)
    TP = D["f_team_prior"]
    for F in FEATS:
        print(f"(f) {F} R5", fmt(TP[F]["R5_2022_25_no_team_prior"]), "R6", fmt(TP[F]["R6_2022_25_with_team_prior"]),
              "dB", round(TP[F]["change_in_b"], 4), "corr", round(TP[F]["corr_feature_lprior_acc"], 3))
    from cites import audit_g5g6 as AU
    G = D["g_audit"]
    for k, r in G["r1_null"].items():
        print("(g)", AU.r1_lines(r), "| hub: treated", round(r["treated_y_minus_own_cell_mean"], 3), "controls",
              round(r["controls_y_minus_own_cell_mean"], 3), "| null hub", {k: round(v, 3) for k, v in r["null_hub"].items()})
        print("     reverse", {k: v for k, v in r["reverse_direction"].items()}, "| symmetric",
              {k: v for k, v in r["symmetric_average"].items() if k != "note"})
    for F in FEATS:
        print("(g)", F)
        for line in AU.summary_lines(G["alt_explanations"][F]):
            print("     ", line)
        cc = G["content_controls"][F]
        print("      content:", {k: fmt(v) for k, v in cc.items()})
    print("(g) split records", {k: v for k, v in G["split_record_mechanism"].items() if k not in ("label", "by_length_tercile")})


if __name__ == "__main__":
    main()
