"""G2: does a title that states a finding (assertive verb, rule-based) go with more citations?

Pre-registered in docs/CITES_PREREG.md. Sample, outcome, controls and fixed effects come from the frozen
core (cites/core.py); nothing here changes them.

  1. Primary estimate: read from outputs/cites/primary.json (Holm p across the 8 primary tests) and
     re-computed with core.primary as a reproduction check.
  2. Robustness R1-R7: core.robustness. Verdict: core.verdict with the primary.json Holm p.
  3. Pre-specified secondary (prereg section 6):
       - G2: validity of the rule against the claims-pilot LLM title-strength labels (title_strength >= 2 =
         explicit claim) on pilot items that overlap this sample;
       - all questions: joint model with all 8 features; heterogeneity by LLM-topic papers.
  4. Diagnostics (not pre-registered):
       (a) artefact check: share of S2 venue records carrying an arXiv id by G2 status; primary re-run on
           papers whose record has an arXiv id (split-record undercount, outputs/cites/qc_split_records.jsonl);
       (b) confounding by other title features: + G1_name control, named titles excluded, + G6a_meme control;
       (c) the 15 most- and 15 least-cited assertive titles and the verbs the rule matches.

Writes outputs/cites/G2/results.json and outputs/cites/G2/fig.png.
Run: cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m cites.g2
"""
from __future__ import annotations

import json
import warnings
from collections import Counter

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from cites import core  # noqa: E402

warnings.filterwarnings("ignore")

F = "G2_assertive"
OUT = core.OUT / "G2"
PILOT = core.OUT.parent / "claims_pilot"
DIAG = "diagnostic (not pre-registered)"
SEC = "pre-specified secondary (prereg section 6; no multiplicity claim)"

# Claims-pilot label sets: annotator tag -> model family; round -> codebook version (from the pilot docs)
MODEL = {"C1": "Claude", "C2": "Claude", "G": "ChatGPT", "HK1": "Claude Haiku", "HK2": "Claude Haiku"}
CODEBOOK = {"r1": "v0", "r2": "v1.1", "r3": "v1.2", "gold_b1": "v1.3"}


# ----------------------------------------------------------------------------------------------- helpers
def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def wilson(k, n, z=1.96):
    if n == 0:
        return [None, None]
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [float(c - h), float(c + h)]


def first_match(t):
    m = core.ASSERT.search(t)
    return m.group(0).lower() if m else None


def era(y):
    return "2017-21" if y <= 2021 else "2022-25"


# ----------------------------------------------------------------------------------- secondary: validity
def load_pilot_labels() -> pd.DataFrame:
    rows = []
    for p in sorted((PILOT / "labels").glob("*.json*")):
        L = [json.loads(s) for s in open(p) if s.strip()] if p.suffix == ".jsonl" else json.load(open(p))
        tag = p.stem.split("_")[0]
        ann = tag.replace("v14", "")
        rnd = "gold_b1" if "gold_b1" in p.stem else p.stem.split("_")[1]
        cb = "v1.4" if tag.endswith("v14") else CODEBOOK[rnd]
        for r in L:
            rows.append({"item_id": r["item_id"], "title_strength": r.get("title_strength"), "annotator": ann,
                         "model": MODEL[ann], "round": rnd, "codebook": cb, "label_set": f"{ann} {rnd} {cb}"})
    return pd.DataFrame(rows)


def agreement(rule, llm, w=None):
    """Binary agreement between the rule (G2) and an LLM label (title_strength >= 2). Optional weights."""
    rule = np.asarray(rule).astype(int)
    llm = np.asarray(llm).astype(int)
    w = np.ones(len(rule)) if w is None else np.asarray(w, float)
    W = w.sum()
    p11 = w[(rule == 1) & (llm == 1)].sum() / W
    p10 = w[(rule == 1) & (llm == 0)].sum() / W
    p01 = w[(rule == 0) & (llm == 1)].sum() / W
    p00 = w[(rule == 0) & (llm == 0)].sum() / W
    po = p11 + p00
    pr, pl = p11 + p10, p11 + p01
    pe = pr * pl + (1 - pr) * (1 - pl)
    div = lambda a, b: float(a / b) if b > 0 else None
    out = {"n": int(len(rule)),
           "counts": {"rule1_llm1": int(((rule == 1) & (llm == 1)).sum()), "rule1_llm0": int(((rule == 1) & (llm == 0)).sum()),
                      "rule0_llm1": int(((rule == 0) & (llm == 1)).sum()), "rule0_llm0": int(((rule == 0) & (llm == 0)).sum())},
           "agreement": float(po), "kappa": div(po - pe, 1 - pe),
           "sensitivity": div(p11, p11 + p01), "specificity": div(p00, p00 + p10),
           "ppv": div(p11, p11 + p10), "npv": div(p00, p00 + p01),
           "prev_rule": float(pr), "prev_llm": float(pl)}
    if w is None or np.allclose(w, 1):
        c = out["counts"]
        out["agreement_ci"] = wilson(c["rule1_llm1"] + c["rule0_llm0"], out["n"])
        out["ppv_ci"] = wilson(c["rule1_llm1"], c["rule1_llm1"] + c["rule1_llm0"])
        out["npv_ci"] = wilson(c["rule0_llm0"], c["rule0_llm0"] + c["rule0_llm1"])
    return out


def form_of(d):
    """Pilot sampling strata (claims/sample_pilot.py precedence: question > assertive > NAME-colon > other)."""
    return np.select([d.G3_question == 1, d.G2_assertive == 1, d.G1_name == 1], ["question", "assertive", "name_colon"], "other")


def validity(df):
    keys = pd.concat([pd.read_parquet(PILOT / f"{k}.parquet")[["item_id", "submission_id", "form"]]
                      for k in ["round1_key", "round2_key", "round3_key", "gold_key"]], ignore_index=True)
    titles = {}
    for p in sorted(PILOT.glob("round*_items_chunk*.jsonl")) + [PILOT / "gold_b1_items.jsonl"]:
        for s in open(p):
            r = json.loads(s)
            titles[r["item_id"]] = r["title"]
    lab = load_pilot_labels()
    lab = lab[lab.title_strength.notna()].copy()
    lab["llm_explicit"] = (lab.title_strength >= 2).astype(int)
    d = df[["submission_id", "title", "year", "cites", F, "G1_name", "G3_question"]].copy()
    d["form_sample"] = form_of(d)
    ov = keys.merge(d, on="submission_id", how="inner")
    ov["pilot_round"] = ov.item_id.str.split("_").str[0]
    ov["labelled"] = ov.item_id.isin(set(lab.item_id))
    ov["title_same_as_pilot"] = [titles.get(i) == t if i in titles else None for i, t in zip(ov.item_id, ov.title)]
    res = {"label": SEC,
           "definition": "LLM explicit claim = title_strength >= 2 (codebook step 3); rule = G2_assertive (core.ASSERT verb, not a question)",
           "pilot_items_keyed": int(len(keys)), "pilot_items_labelled": int(lab.item_id.nunique()),
           "overlap_keyed": int(len(ov)), "overlap_labelled": int(ov.labelled.sum()),
           "overlap_keyed_by_round": ov.pilot_round.value_counts().to_dict(),
           "overlap_labelled_by_round": ov[ov.labelled].pilot_round.value_counts().to_dict(),
           "overlap_labelled_by_rule": ov[ov.labelled][F].value_counts().to_dict(),
           "pilot_form_equals_rule_strata": bool((ov.form == ov.form_sample).all()),
           "titles_identical_to_pilot_text": int(ov[ov.labelled].title_same_as_pilot.sum()),
           "note_sampling": "pilot items were drawn from all ICLR submissions 2017-2026 (incl. rejected), stratified by title form with "
                            "assertive titles oversampled (~40%); overlap = accepted, 2017-2025, S2-matched items only"}
    m = lab.merge(ov[ov.labelled][["item_id", "submission_id", "title", "year", "cites", F, "form_sample"]], on="item_id", how="inner")
    per = {}
    for ls, g in m.groupby("label_set", sort=True):
        per[ls] = {"model": g.model.iloc[0], "codebook": g.codebook.iloc[0], **agreement(g[F], g.llm_explicit)}
    res["per_label_set"] = per
    res["pooled_all_labels"] = agreement(m[F], m.llm_explicit)
    res["pooled_all_labels"]["note"] = "label-level (item x label set); items with more label sets count more than once"
    # item-level consensus: median title_strength across every label set for that item
    it = m.groupby("item_id").agg(title=("title", "first"), year=("year", "first"), cites=("cites", "first"), rule=(F, "first"),
                                  form=("form_sample", "first"), med_ts=("title_strength", "median"), n_sets=("label_set", "nunique"),
                                  share_explicit=("llm_explicit", "mean"),
                                  labels=("title_strength", lambda s: [int(x) for x in s])).reset_index()
    it["consensus_explicit"] = (it.med_ts >= 2).astype(int)
    res["consensus_item_level"] = agreement(it.rule, it.consensus_explicit)
    res["consensus_item_level"]["rule"] = "explicit if the median title_strength across all label sets on the item is >= 2"
    res["consensus_item_level"]["n_label_sets_per_item"] = it.n_sets.value_counts().sort_index().to_dict()
    res["consensus_item_level"]["mean_title_strength_by_rule"] = it.groupby("rule").med_ts.mean().to_dict()
    res["consensus_item_level"]["distribution_by_rule"] = {int(k): g.med_ts.value_counts().sort_index().to_dict() for k, g in it.groupby("rule")}
    # consensus restricted to the ChatGPT labels (the claims main-study primary annotator) and to Claude C1
    for tag in ["G", "C1"]:
        g = m[m.annotator == tag].groupby("item_id").agg(rule=(F, "first"), ts=("title_strength", "median")).reset_index()
        res[f"{tag}_item_level"] = agreement(g.rule, (g.ts >= 2).astype(int))
    # diagnostic: reweight item-level consensus agreement to this sample's mix of pilot strata
    N = pd.Series(form_of(df)).value_counts()
    n = it.form.value_counts()
    w = it.form.map(lambda s: N[s] / n[s])
    rw = agreement(it.rule, it.consensus_explicit, w=w)
    rw.update({"label": DIAG, "how": "items weighted by N_stratum(sample) / n_stratum(labelled overlap), strata = pilot title forms",
               "sample_strata_N": N.to_dict(), "overlap_strata_n": n.to_dict(), "ci95_stratified_bootstrap": reweighted_ci(it, N)})
    res["consensus_reweighted_to_sample"] = rw
    dis = it[it.rule != it.consensus_explicit].sort_values(["rule", "med_ts"], ascending=[False, True])
    res["disagreements"] = [{"item_id": r.item_id, "title": r.title, "year": int(r.year), "rule": int(r.rule), "median_ts": float(r.med_ts),
                             "labels": r.labels, "matched_verb": first_match(r.title)} for r in dis.itertuples()]
    return res, it


# ----------------------------------------------------------------- diagnostic: why R1 and primary differ
def _pairs(d, caliper=0.80, same_cell=False):
    """Re-implementation of core.matched_pairs' pairing (same embedding, same-year nearest control, cosine >=
    caliper, with replacement) that also returns the pair indices. same_cell=True restricts controls to the same
    year x topic50 cell. Validated against core.matched_pairs in main()."""
    d = d.reset_index(drop=True)
    tr, co = d[F] == 1, d[F] == 0
    Em, found = core.C.load_masked_embedding(d)
    Ea = core.C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea)
    E = E / np.linalg.norm(E, axis=1, keepdims=True)
    T, K, S_ = [], [], []
    groups = ["year", "topic50"] if same_cell else ["year"]
    for _, g in d.groupby(groups, sort=True):
        gi = g.index.to_numpy()
        ti = gi[tr.loc[gi].to_numpy()]
        ci = gi[co.loc[gi].to_numpy()]
        if len(ti) == 0 or len(ci) == 0:
            continue
        S = E[ti] @ E[ci].T
        j = S.argmax(1)
        s = S[np.arange(len(ti)), j]
        ok = s >= caliper
        T += list(ti[ok]); K += list(ci[j[ok]]); S_ += list(s[ok])
    return d, np.array(T, int), np.array(K, int), np.array(S_)


def _boot_mean(x, n_boot=2000, seed=0):
    rng = np.random.default_rng(seed)
    b = [rng.choice(x, len(x)).mean() for _ in range(n_boot)]
    m, lo, hi = x.mean(), *np.percentile(b, [2.5, 97.5])
    return {"n_pairs": int(len(x)), "pct": float(np.exp(m) - 1), "lo": float(np.exp(lo) - 1), "hi": float(np.exp(hi) - 1)}


def r1_vs_primary(df):
    out = {"label": DIAG, "question": "R1 (content-matched pairs) has the opposite sign to the primary estimate; which content "
                                      "or covariate differences account for the gap?"}
    # matched pairs: caliper and era sensitivity (core.matched_pairs itself)
    out["R1_caliper_0.85"] = core.matched_pairs(df, F, caliper=0.85)
    out["R1_caliper_0.90"] = core.matched_pairs(df, F, caliper=0.90)
    out["R1_era_2017_21"] = core.matched_pairs(df[df.year <= 2021], F)
    out["R1_era_2022_25"] = core.matched_pairs(df[df.year >= 2022], F)
    out["R1_arxiv_id_only"] = core.matched_pairs(df[df.arxiv.notna()], F)
    # pair-level detail from the re-implementation
    d, T, K, S = _pairs(df)
    dy = d.y.to_numpy()[T] - d.y.to_numpy()[K]
    out["reimplementation_check"] = {"n_pairs": int(len(T)), "pct": float(np.exp(dy.mean()) - 1)}
    out["pair_balance"] = {"mean_cosine": float(S.mean()), "share_same_topic50": float((d.topic50.to_numpy()[T] == d.topic50.to_numpy()[K]).mean()),
                           "mean_diff_log_authors": float((d.log_authors.to_numpy()[T] - d.log_authors.to_numpy()[K]).mean()),
                           "mean_diff_log_abs_words": float((d.log_abs_words.to_numpy()[T] - d.log_abs_words.to_numpy()[K]).mean()),
                           "n_distinct_controls": int(len(set(K)))}
    # regression-adjusted matched estimate: pair diff in y on pair diffs in the primary's non-embedding controls
    X = np.column_stack([np.ones(len(T)), d.log_authors.to_numpy()[T] - d.log_authors.to_numpy()[K],
                         d.log_abs_words.to_numpy()[T] - d.log_abs_words.to_numpy()[K]])
    rng = np.random.default_rng(0)
    beta = np.linalg.lstsq(X, dy, rcond=None)[0]
    bs = []
    for _ in range(2000):
        i = rng.integers(0, len(dy), len(dy))
        bs.append(np.linalg.lstsq(X[i], dy[i], rcond=None)[0][0])
    lo, hi = np.percentile(bs, [2.5, 97.5])
    out["R1_regression_adjusted"] = {"pct": float(np.exp(beta[0]) - 1), "lo": float(np.exp(lo) - 1), "hi": float(np.exp(hi) - 1),
                                     "n_pairs": int(len(T)), "adjusted_for": ["log_authors", "log_abs_words"]}
    # matched within the same year x topic50 cell
    d2, T2, K2, _ = _pairs(df, same_cell=True)
    out["R1_same_year_topic50_cell"] = _boot_mean(d2.y.to_numpy()[T2] - d2.y.to_numpy()[K2])
    # primary regression with more (or fewer) abstract-embedding PCs: content-control dose-response
    from sklearn.decomposition import PCA
    Ea = core.C.load_embedding(df, "abstract", "bge-small-en-v1.5")
    Ea = Ea / np.linalg.norm(Ea, axis=1, keepdims=True)
    P = PCA(n_components=200, random_state=0).fit_transform(Ea)
    dd = df.copy()
    for k in range(200):
        dd[f"xpc{k}"] = P[:, k]
    base = ["log_authors", "log_abs_words"]
    dose = {}
    for k in [0, 5, 10, 20, 50, 100, 200]:
        dose[str(k)] = core._fit(dd, "y", F, base + [f"xpc{j}" for j in range(k)])
    out["primary_by_n_abstract_pcs"] = dose
    out["primary_by_n_abstract_pcs_note"] = "PCA(200) on the normalised bge abstract embedding (random_state=0), first k components; " \
                                            "k=20 is the pre-registered control set up to PCA numerics"
    out["primary_full_384d_embedding"] = core._fit(dd.assign(**{f"e{j}": Ea[:, j] for j in range(Ea.shape[1])}), "y", F,
                                                   base + [f"e{j}" for j in range(Ea.shape[1])])
    return out


def reweighted_ci(it, N, n_boot=2000, seed=0):
    """Stratified bootstrap for the sample-reweighted consensus agreement (strata = pilot title forms)."""
    rng = np.random.default_rng(seed)
    keys = ["agreement", "kappa", "sensitivity", "specificity", "ppv", "npv", "prev_llm"]
    acc = {k: [] for k in keys}
    groups = {s: g for s, g in it.groupby("form")}
    for _ in range(n_boot):
        b = pd.concat([g.iloc[rng.integers(0, len(g), len(g))] for g in groups.values()])
        w = b.form.map(lambda s: N[s] / len(groups[s]))
        a = agreement(b.rule, b.consensus_explicit, w=w)
        for k in keys:
            if a[k] is not None:
                acc[k].append(a[k])
    return {k: [float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))] for k, v in acc.items()}


# ------------------------------------------------------------------------------------------------ main
def fmt(r):
    return f"{r['pct'] * 100:+.1f}% [{r['lo'] * 100:+.1f}, {r['hi'] * 100:+.1f}]"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = core.load()
    pj = json.load(open(core.OUT / "primary.json"))["primary"][F]
    p_holm = pj["p_holm"]
    ctrl = core.controls(F)

    # 1. primary + reproduction check
    prim = core.primary(df, F)
    repro = {"b_json": pj["b"], "b_recomputed": prim["b"], "abs_diff_b": abs(pj["b"] - prim["b"]),
             "se_json": pj["se"], "se_recomputed": prim["se"], "n_json": pj["n"], "n_recomputed": prim["n"],
             "n_with_json": pj["n_with"], "n_with_recomputed": prim["n_with"],
             "reproduced": bool(abs(pj["b"] - prim["b"]) < 1e-8 and abs(pj["se"] - prim["se"]) < 1e-8 and pj["n"] == prim["n"])}
    print("primary (json):", fmt(pj), "p", pj["p"], "Holm", p_holm, "| reproduced:", repro["reproduced"])

    # 2. robustness + verdict
    rob = core.robustness(df, F)
    ver = core.verdict(pj, rob, p_holm)
    for k, r in rob.items():
        print(f"  {k:28s}", fmt(r) if "pct" in r else r, f"n_pairs={r.get('n_pairs')}" if "n_pairs" in r else f"p={r.get('p'):.4f} n={r.get('n')}")
    print("verdict:", ver)

    # 3. pre-specified secondary
    sec = {}
    sec["validity_vs_llm_title_strength"], items = validity(df)
    v = sec["validity_vs_llm_title_strength"]
    print("validity: overlap labelled", v["overlap_labelled"], "consensus", {k: v["consensus_item_level"][k] for k in ["agreement", "kappa", "ppv", "npv"]})
    others = [f for f in core.FEATURES if f != F]
    sec["joint_model_all8"] = {"label": SEC, **core._fit(df, "y", F, ctrl + others), "other_features": others}
    llm = df.llm_topic.fillna(False).astype(bool)
    het = {"label": SEC}
    for nm, sub in [("llm_topic", df[llm]), ("non_llm_topic", df[~llm])]:
        het[nm] = {**core._fit(sub, "y", F, ctrl), "n_with": int(sub[F].sum())}
    dx = df.assign(G2_x_llm=df[F] * llm.astype(int), llm_topic_i=llm.astype(int))
    het["interaction_ratio"] = core._fit(dx, "y", "G2_x_llm", ctrl + [F, "llm_topic_i"])
    het["interaction_ratio"]["note"] = "pct = ratio of the G2 citation ratio in LLM-topic vs other papers, minus 1"
    sec["heterogeneity_llm_topic"] = het

    # 4. diagnostics
    diag = {"label": DIAG}
    d = df.assign(has_arxiv=df.arxiv.notna().astype(int), multi_s2=(df.n_s2 > 1).astype(int), era=df.year.map(era))
    # (a) artefact check
    share = d.groupby(F).has_arxiv.agg(["mean", "sum", "size"]).rename(columns={"mean": "share", "sum": "n_arxiv", "size": "n"})
    share_era = d.groupby(["era", F]).has_arxiv.mean().unstack()
    lpm = core._fit(d, "has_arxiv", F, ctrl)
    qc = [json.loads(s) for s in open(core.OUT / "qc_split_records.jsonl")]
    qc_split = [r for r in qc if r["match_pid"] and r["match_pid"] != r["venue_pid"]]
    qc_more = [r for r in qc_split if (r["match_cites"] or 0) > (r["venue_cites"] or 0)]
    qc_in = d[d.submission_id.isin({r["sid"] for r in qc})]
    art = {"label": DIAG,
           "why": "S2 venue records without an arXiv id can miss citations that accrue to a separate arXiv record "
                  f"(QC snapshot: {len(qc_split)} of {len(qc)} checked no-arXiv venue records have a separate S2 record, "
                  f"{len(qc_more)} of them with more citations)",
           "arxiv_share_by_G2": {int(k): {kk: float(vv) for kk, vv in r.items()} for k, r in share.iterrows()},
           "arxiv_share_by_era_and_G2": {e: {int(k): float(x) for k, x in r.items()} for e, r in share_era.iterrows()},
           "arxiv_share_diff_adjusted_pp": {"b": lpm["b"] * 100, "lo": (lpm["b"] - 1.96 * lpm["se"]) * 100,
                                            "hi": (lpm["b"] + 1.96 * lpm["se"]) * 100, "p": lpm["p"],
                                            "model": "linear probability, primary controls and FE"},
           "multi_s2_records_by_G2": d.groupby(F).multi_s2.sum().to_dict(),
           "qc_split_records": {"n_checked": len(qc), "n_split": len(qc_split),
                                "split": [{"sid": r["sid"], "venue_cites": r["venue_cites"], "other_record_cites": r["match_cites"]} for r in qc_split],
                                "qc_papers_in_sample": int(len(qc_in)), "qc_papers_in_sample_assertive": int(qc_in[F].sum())},
           "rerun_arxiv_id_only": {**core._fit(d[d.has_arxiv == 1], "y", F, ctrl), "n_with": int(d[(d.has_arxiv == 1)][F].sum())},
           "rerun_no_arxiv_id_only": {**core._fit(d[d.has_arxiv == 0], "y", F, ctrl), "n_with": int(d[(d.has_arxiv == 0)][F].sum())},
           "rerun_has_arxiv_control": core._fit(d, "y", F, ctrl + ["has_arxiv"])}
    diag["a_artefact_arxiv"] = art
    # (b) overlap with other title features
    ovl = {"label": DIAG,
           "crosstab_G1_G2": pd.crosstab(d.G1_name, d[F]).to_dict(),
           "crosstab_G6a_G2": pd.crosstab(d.G6a_meme, d[F]).to_dict(),
           "share_named_among_assertive": float(d.loc[d[F] == 1, "G1_name"].mean()),
           "share_named_among_other": float(d.loc[d[F] == 0, "G1_name"].mean()),
           "plus_G1_name_control": core._fit(d, "y", F, ctrl + ["G1_name"]),
           "non_named_titles_only": {**core._fit(d[d.G1_name == 0], "y", F, ctrl), "n_with": int(d[d.G1_name == 0][F].sum())},
           "plus_G6a_meme_control": core._fit(d, "y", F, ctrl + ["G6a_meme"]),
           "plus_G1_and_G6a_controls": core._fit(d, "y", F, ctrl + ["G1_name", "G6a_meme"]),
           "meme_titles_excluded": {**core._fit(d[d.G6a_meme == 0], "y", F, ctrl), "n_with": int(d[d.G6a_meme == 0][F].sum())}}
    diag["b_overlap_other_features"] = ovl
    # (c) what the rule captures
    d["cite_pctile_in_year"] = d.groupby("year").cites.rank(pct=True)
    d["verb"] = d.title.map(first_match)
    A = d[d[F] == 1].copy()
    cons = items.set_index("title").med_ts.to_dict()
    row = lambda r: {"title": r.title, "year": int(r.year), "cites": int(r.cites), "pctile_in_year": round(float(r.cite_pctile_in_year), 3),
                     "matched_verb": r.verb, "named": int(r.G1_name), "venue_record_has_arxiv_id": int(r.has_arxiv),
                     "llm_median_ts": cons.get(r.title)}
    top = A.sort_values(["cite_pctile_in_year", "cites"], ascending=[False, False]).head(15)
    bot = A.sort_values(["cite_pctile_in_year", "cites", "year"], ascending=[True, True, True]).head(15)
    verbs = Counter(A.verb)
    all_matches = d.title.map(lambda t: {m.lower() for m in core.ASSERT.findall(t)})
    guar_only = (d[F] == 1) & all_matches.map(lambda s: len(s) > 0 and s <= {"guarantee", "guarantees"})
    art["zero_citation_share_by_G2_and_era"] = {e: {int(k): float(x) for k, x in r.items()}
                                                for e, r in d.assign(zero=(d.cites == 0).astype(int)).groupby(["era", F]).zero.mean().unstack().iterrows()}
    art["zero_citation_share_by_arxiv_status"] = d.assign(zero=(d.cites == 0).astype(int)).groupby("has_arxiv").zero.mean().to_dict()
    rule_precision = {"label": DIAG, "n_guarantee_only_matches": int(guar_only.sum()),
                      "rerun_guarantee_only_titles_excluded": {**core._fit(d[~guar_only], "y", F, ctrl), "n_with": int(d[~guar_only][F].sum())},
                      "note": "titles whose only rule match is 'guarantee(s)' (mostly the noun phrase 'with ... Guarantees') dropped from the sample"}
    diag["c_titles"] = {"label": DIAG, "ranking": "within-year citation percentile among all papers in the sample (age-adjusted); raw count shown",
                        "top15": [row(r) for r in top.itertuples()], "bottom15": [row(r) for r in bot.itertuples()],
                        "matched_verb_counts": dict(verbs.most_common()),
                        "share_copula_or_modal": float(A.verb.isin(["is", "are", "was", "were", "can", "cannot", "can't", "could", "will",
                                                                     "does", "do", "did", "doesn't", "don't", "isn't", "aren't"]).mean()),
                        "assertive_by_year": A.year.value_counts().sort_index().to_dict(),
                        "share_by_year": d.groupby("year")[F].mean().to_dict(), "rule_precision": rule_precision}
    # (d) why R1 and the primary differ
    diag["d_r1_vs_primary"] = r1_vs_primary(df)
    chk = diag["d_r1_vs_primary"]["reimplementation_check"]
    assert chk["n_pairs"] == rob["R1_matched_pairs"]["n_pairs"] and abs(chk["pct"] - rob["R1_matched_pairs"]["pct"]) < 1e-9, chk

    res = {"feature": F, "label": core.FEATURES[F], "n_papers": int(len(df)), "n_with": int(df[F].sum()),
           "primary": {**pj, "source": "outputs/cites/primary.json (Holm across the 8 primary tests)"},
           "reproduction_check": repro, "robustness": rob, "verdict": ver,
           "verdict_rule": "more/fewer citations: Holm p < 0.05 and same sign in R1 and R2; no meaningful difference: 95% CI within +/-10%; else inconclusive",
           "secondary": sec, "diagnostics": diag}
    json.dump(_clean(res), open(OUT / "results.json", "w"), indent=1, ensure_ascii=False)
    figure(res)
    print("wrote", OUT / "results.json", OUT / "fig.png")


# --------------------------------------------------------------------------------------------- figure
def figure(res):
    rob, dg, sec = res["robustness"], res["diagnostics"], res["secondary"]
    dr = dg["d_r1_vs_primary"]
    pcs = dr["primary_by_n_abstract_pcs"]
    groups = [
        ("Pre-registered", [
            ("Primary (20 abstract PCs, year × topic50 FE)", res["primary"], "primary"),
            ("R1 content-matched pairs", rob["R1_matched_pairs"], "rob"),
            ("R2 PPML, raw counts", rob["R2_ppml_counts"], "rob"),
            ("R3 influential citations", rob["R3_influential"], "rob"),
            ("R4 drop top 1% per year", rob["R4_drop_top1pct"], "rob"),
            ("R5 2017–21", rob["R5_era_2017_21"], "rob"),
            ("R5 2022–25", rob["R5_era_2022_25"], "rob"),
            ("R6 + team prior acceptances, 2022–25", rob["R6_team_prior_2022_25"], "rob"),
            ("R7 year + topic100 FE", rob["R7_year_plus_topic100_fe"], "rob")]),
        ("Diagnostic: richer content controls", [
            ("Primary with 0 abstract PCs", pcs["0"], "diag"),
            ("Primary with 50 PCs", pcs["50"], "diag"),
            ("Primary with 200 PCs", pcs["200"], "diag"),
            ("Primary with full 384-d embedding", dr["primary_full_384d_embedding"], "diag"),
            ("Matched pairs within year × topic50", dr["R1_same_year_topic50_cell"], "diag")]),
        ("Secondary (joint model) and other diagnostics", [
            ("Joint model, all 8 features (secondary)", sec["joint_model_all8"], "diag"),
            ("Records with an arXiv id only", dg["a_artefact_arxiv"]["rerun_arxiv_id_only"], "diag"),
            ("+ named-title (G1) control", dg["b_overlap_other_features"]["plus_G1_name_control"], "diag"),
            ("Meme-template titles excluded", dg["b_overlap_other_features"]["meme_titles_excluded"], "diag")]),
    ]
    BLUE, INK, INK2, MUTED, GRID = "#2a78d6", "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})
    fig, ax = plt.subplots(figsize=(8.2, 7.4), facecolor="white")
    ax.set_facecolor("white")
    allrows = [r for _, g in groups for r in g]
    xmax = max(r[1]["hi"] for r in allrows) * 100
    xmin = min(min(r[1]["lo"] for r in allrows) * 100, -10)
    y, ticks, labels, kinds, heads = 0.0, [], [], [], []
    for gi, (head, rows) in enumerate(groups):
        if gi:
            y += 0.6
        heads.append((head, y))
        y += 0.9
        for name, e, kind in rows:
            col = BLUE if kind == "primary" else (INK2 if kind == "rob" else MUTED)
            ax.plot([e["lo"] * 100, e["hi"] * 100], [y, y], color=col, lw=2, solid_capstyle="round", zorder=2)
            ax.scatter([e["pct"] * 100], [y], s=44 if kind == "primary" else 30, color=col if kind != "diag" else "white",
                       edgecolor=col, linewidth=1.6, zorder=3)
            ax.text(xmax + 5, y, f"{e['pct'] * 100:+.0f}%  [{e['lo'] * 100:+.0f}, {e['hi'] * 100:+.0f}]", va="center", ha="left",
                    fontsize=8, color=INK if kind == "primary" else INK2)
            ticks.append(y); labels.append(name); kinds.append(kind)
            y += 1
    for head, yy in heads:
        ax.text(-0.02, yy, head, transform=ax.get_yaxis_transform(), fontsize=8, color=INK, fontweight="bold", ha="right", va="center")
    ax.axvline(0, color=INK2, lw=0.9, zorder=1)
    ax.set_yticks(ticks)
    ax.set_yticklabels(labels, fontsize=8.3)
    for t, k in zip(ax.get_yticklabels(), kinds):
        t.set_color(INK if k == "primary" else (INK2 if k == "rob" else MUTED))
        if k == "primary":
            t.set_fontweight("bold")
    ax.set_ylim(y - 0.4, -0.6)
    ax.set_xlim(xmin - 3, xmax + 2)
    ax.set_xlabel("% difference in citations, assertive vs other titles (95% CI)", color=INK2)
    ax.grid(axis="x", color=GRID, lw=0.6, zorder=0)
    for s_ in ["top", "right", "left"]:
        ax.spines[s_].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", colors=INK2)
    ax.set_title(f"G2 · Titles that state a finding: {res['n_with']} of {res['n_papers']:,} accepted ICLR papers, 2017–2025",
                 loc="left", fontsize=10, color=INK, pad=20, x=-0.62)
    ax.text(-0.62, 1.012, f"Holm p = {res['primary']['p_holm']:.3f}; R1 has the opposite sign · pre-registered verdict: {res['verdict']}",
            transform=ax.transAxes, fontsize=8, color=INK2, ha="left", va="bottom")
    fig.tight_layout()
    fig.savefig(OUT / "fig.png", dpi=200, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
