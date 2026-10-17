"""Adversarial-audit diagnostics for G3 (question titles) and G4 (LLM-favoured title words), added 2026-10-17.

Everything here is DIAGNOSTIC (NOT PRE-REGISTERED). Nothing changes the pre-registered primary estimate, sample,
outcome, controls, fixed effects or verdict. Unless stated otherwise each re-fit uses core._fit with the primary
controls (core.controls), year^topic50 FE and SEs clustered by topic50.

r1_calibration(df, F)  -- why R1 (core.matched_pairs) sits below the primary
  placebo    Null of the R1 procedure: pseudo-treated papers drawn at random from the papers without the feature, with
             the same per-year counts as the real treated group, matched with the R1 rule to the remaining papers
             without the feature. Placebo-adjusted R1 = exp(observed mean log diff - placebo mean) - 1 (same method as
             g4.py diagnostic (d)).
  hubness    Mechanism. k-occurrence = how often a paper is the nearest same-year neighbour (R1 embedding) of another
             paper; local density = mean cosine to its 10 nearest same-year neighbours (z-scored). Both are regressed
             on y with the primary controls and FE. Matched controls are compared with treated papers and with all
             papers on k-occurrence.
  residual   Where treated papers and their matched controls sit relative to the primary model's content prediction
             (model fitted on papers without the feature, FE = year x topic50 cell, predicted for everyone).
  csls       Hub-penalised matching: control chosen by argmax(2 cos - density_c) (CSLS-style, k = 10), same caliper on
             the raw cosine, with its own placebo null.
  pair_adj   R1 with a pair-level adjustment for the within-pair difference in log(1 + k-occurrence).
  primary_plus_hubness  Primary spec + log(1 + k-occurrence) or + local density (does the primary miss this?).

alt_explanations(df, F)  -- can something other than the title explain the primary point estimate?
  timing     Preprint exposure time (months from first arXiv posting to the conference; arXiv-id records only;
             lead-month FE bins). Uses audit_g1g2.add_columns (read only).
  code       Abstract announces code or a URL (promotion / reuse).
  paper_type Method and findings abstract indicators (crude regexes from audit_g1g2), and a benchmark / dataset paper
             indicator (title contains 'bench', or the abstract says we introduce / present / release ... a benchmark /
             dataset / testbed).
  topic      + llm_topic indicator.
  llm_style  + F24 abstract fingerprint (2024-style LLM words in the abstract; a proxy for LLM-assisted writing).
  tail       Within-year citation percentile outcome; drop the top 5% per year; drop zero-citation records; PPML (R2)
             after dropping the k most-cited feature papers (one-sided, shows how many papers the R2 sign rests on)
             and after dropping the top 1% per year (symmetric).
  retitling  WP4 audit pairs (outputs/snapshot/audit_pairs.csv, read only): feature status on the arXiv v1 title
             (posted before the decision) vs the camera-ready title, for accepted 2023-25 papers.
  G4 only    neutral-synonym benchmark N24 = improv*|utili[sz]*|exploit* (as in D3); word families estimated one at a
             time against all other papers (sensitivity for the one-model family secondary).
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd
import pyfixest as pf

from analyses import _core as C
from cites import audit_g1g2, core

LABEL = "diagnostic (not pre-registered; added by the adversarial audit)"
BENCH_T = re.compile(r"bench", re.I)
BENCH_A = re.compile(r"\b(?:we|this paper|this work)\s+(?:introduce|present|propose|release|build|construct|create|curate|"
                     r"develop|contribute)s?\b[^.]{0,120}\b(?:benchmark|dataset|testbed|test suite|evaluation suite)s?\b", re.I)
N24_RX = re.compile(r"\b(improv\w*|utili[sz]\w*|exploit\w*)", re.I)
R24_RX = re.compile(r"\b(enhanc|leverag|unveil|unleash|harness|empower|elevat|boost)\w*", re.I)  # reproduces r24_any exactly
AUDIT_PAIRS = core.OUT.parent / "snapshot" / "audit_pairs.csv"


# --------------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------------
def _nw(r: dict, d: pd.DataFrame, col: str) -> dict:
    r = dict(r)
    r["n_with"] = int(d[col].sum())
    return r


def _by(d: pd.DataFrame, F: str, col: str) -> dict:
    return {"with_feature": float(d.loc[d[F] == 1, col].mean()), "without_feature": float(d.loc[d[F] == 0, col].mean())}


def _pp(r: dict) -> dict:
    return {"b_pp": 100 * r["b"], "lo_pp": 100 * (r["b"] - 1.96 * r["se"]), "hi_pp": 100 * (r["b"] + 1.96 * r["se"]),
            "p": r["p"], "n": r["n"]}


def _boot(x: np.ndarray, n_boot: int = 2000, seed: int = 0) -> dict:
    rng = np.random.default_rng(seed)
    b = [rng.choice(x, len(x)).mean() for _ in range(n_boot)]
    lo, hi = np.percentile(b, [2.5, 97.5])
    return {"pct": float(np.exp(x.mean()) - 1), "lo": float(np.exp(lo) - 1), "hi": float(np.exp(hi) - 1), "n_pairs": int(len(x))}


def _embedding(d: pd.DataFrame) -> np.ndarray:
    """Same embedding as core.matched_pairs (name-masked abstract; unmasked where no masked text, i.e. 2017)."""
    Em, found = C.load_masked_embedding(d)
    Ea = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea)
    return E / np.linalg.norm(E, axis=1, keepdims=True)


def _hubness(E: np.ndarray, years: np.ndarray, k: int = 10):
    """k-occurrence (times a paper is the nearest same-year neighbour of another paper) and local density (mean cosine to
    its k nearest same-year neighbours)."""
    kocc, dens = np.zeros(len(E)), np.zeros(len(E))
    for y in np.unique(years):
        ii = np.where(years == y)[0]
        S = E[ii] @ E[ii].T
        np.fill_diagonal(S, -9.0)
        np.add.at(kocc, ii[S.argmax(1)], 1)
        dens[ii] = np.sort(S, axis=1)[:, -k:].mean(1)
    return kocc, dens


def _pairs(E, years, tr, co, caliper=0.80, penalty=None):
    """core.matched_pairs pairing (nearest same-year control, with replacement, cosine >= caliper). With `penalty`
    (per-row local density) the control maximises 2*cos - penalty (CSLS-style); the caliper is applied to the raw cosine."""
    T, K = [], []
    for y in np.unique(years):
        ti = np.where(tr & (years == y))[0]
        ci = np.where(co & (years == y))[0]
        if len(ti) == 0 or len(ci) == 0:
            continue
        S = E[ti] @ E[ci].T
        j = (S if penalty is None else 2 * S - penalty[ci][None, :]).argmax(1)
        ok = S[np.arange(len(ti)), j] >= caliper
        T.append(ti[ok])
        K.append(ci[j[ok]])
    return np.concatenate(T), np.concatenate(K)


def _placebo(E, years, yv, tr, pool0, n_rep, seed, penalty=None) -> np.ndarray:
    counts = pd.Series(years[tr]).value_counts()
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(n_rep):
        ptr = np.zeros(len(years), bool)
        for y, k in counts.items():
            idx = np.where(pool0 & (years == y))[0]
            ptr[rng.choice(idx, int(k), replace=False)] = True
        a, b = _pairs(E, years, ptr, pool0 & ~ptr, penalty=penalty)
        out.append(float((yv[a] - yv[b]).mean()))
    return np.array(out)


def _calibrate(obs: float, st: np.ndarray) -> dict:
    n = len(st)
    adj = obs - st.mean()
    se = float(st.std(ddof=1) * np.sqrt(1 + 1 / n))
    p_lo, p_hi = (1 + (st <= obs).sum()) / (n + 1), (1 + (st >= obs).sum()) / (n + 1)
    return {"observed_pct": float(np.exp(obs) - 1), "null_n_rep": n, "null_mean_pct": float(np.exp(st.mean()) - 1),
            "null_sd_log": float(st.std(ddof=1)), "null_q2.5_q97.5_pct": [float(np.exp(q) - 1) for q in np.percentile(st, [2.5, 97.5])],
            "placebo_p_two_sided": float(min(1.0, 2 * min(p_lo, p_hi))),
            "adjusted_pct": float(np.exp(adj) - 1), "adjusted_lo": float(np.exp(adj - 1.96 * se) - 1),
            "adjusted_hi": float(np.exp(adj + 1.96 * se) - 1)}


# --------------------------------------------------------------------------------------------
# R1 calibration and mechanism
# --------------------------------------------------------------------------------------------
def r1_calibration(df: pd.DataFrame, F: str, n_rep: int = 200, seed: int = 0) -> dict:
    d = df.reset_index(drop=True).copy()
    E = _embedding(d)
    years, yv = d.year.to_numpy(), d.y.to_numpy()
    kocc, dens = _hubness(E, years)
    d["lkocc"] = np.log1p(kocc)
    d["dens10_z"] = (dens - dens.mean()) / dens.std()
    tr = (d[F] == 1).to_numpy()
    pool0 = ~tr
    out = {"label": LABEL, "feature": F}

    t, c = _pairs(E, years, tr, pool0)
    obs = float((yv[t] - yv[c]).mean())
    out["reimplementation_check"] = {"n_pairs": int(len(t)), "pct": float(np.exp(obs) - 1)}

    # (i) random placebo (same procedure as g4.py diagnostic (d))
    st = _placebo(E, years, yv, tr, pool0, n_rep, seed)
    out["placebo"] = {**_calibrate(obs, st), "seed": seed,
                      "note": "pseudo-treated = random papers without the feature, same per-year counts; adjusted CI uses "
                              "the placebo SD of the R1 statistic as its SE"}

    # (ii) mechanism: hubness of matched controls, and hubness / density vs citations
    lk = d.lkocc.to_numpy()
    out["hubness"] = {
        "mean_log1p_kocc": {"treated": float(lk[t].mean()), "matched_controls": float(lk[c].mean()), "all_papers": float(lk.mean())},
        "mean_kocc": {"treated": float(kocc[t].mean()), "matched_controls": float(kocc[c].mean()), "all_papers": float(kocc.mean())},
        "mean_density10_z": {"treated": float(d.dens10_z.to_numpy()[t].mean()), "matched_controls": float(d.dens10_z.to_numpy()[c].mean())},
        "y_on_log1p_kocc_primary_controls": core._fit(d, "y", "lkocc", core.controls(F)),
        "y_on_density10_z_primary_controls": core._fit(d, "y", "dens10_z", core.controls(F)),
        "y_on_log1p_kocc_plus_density": core._fit(d, "y", "lkocc", core.controls(F, ["dens10_z"])),
        "mean_log1p_kocc_feature_vs_rest": _by(d, F, "lkocc"),
        "note": "k-occurrence counts how often a paper is the nearest same-year neighbour (R1 embedding) of another paper "
                "(all papers); density = mean cosine to the 10 nearest same-year neighbours, z-scored. Coefficients are "
                "per unit of log(1 + k-occurrence) and per SD of density, with the primary controls and FE."}

    # (iii) residual decomposition relative to the primary model's content prediction (fitted without treated papers)
    m = pf.feols(f"y ~ {' + '.join(core.controls(F))} | yt", data=d[d[F] == 0], vcov={"CRV1": "topic50"})
    res = yv - np.asarray(m.predict(newdata=d), dtype=float)
    out["residual_decomposition"] = {
        "treated_mean_residual_log": float(np.nanmean(res[t])), "matched_controls_mean_residual_log": float(np.nanmean(res[c])),
        "R1_on_residuals_pct": float(np.exp(np.nanmean(res[t] - res[c])) - 1),
        "R1_minus_control_excess_pct": float(np.exp(obs + np.nanmean(res[c])) - 1),
        "note": "residual = y - prediction of y ~ primary controls | year x topic50 cell, fitted on papers without the "
                "feature. A positive control residual means the matched controls are cited more than their content "
                "predicts; R1_minus_control_excess removes that excess from R1 for this treated group's own pairs."}

    # (iv) hub-penalised (CSLS-style) matching with its own placebo
    t2, c2 = _pairs(E, years, tr, pool0, penalty=dens)
    obs2 = float((yv[t2] - yv[c2]).mean())
    st2 = _placebo(E, years, yv, tr, pool0, n_rep, seed + 1, penalty=dens)
    out["csls_matching"] = {**_boot(yv[t2] - yv[c2]), "calibration": _calibrate(obs2, st2),
                            "matched_controls_mean_log1p_kocc": float(lk[c2].mean()),
                            "note": "control = argmax(2 cos - density_c); caliper 0.80 on the raw cosine"}

    # (v) pair-level adjustment for the hubness difference
    dy = yv[t] - yv[c]
    X = np.column_stack([np.ones(len(t)), lk[t] - lk[c]])
    beta = np.linalg.lstsq(X, dy, rcond=None)[0]
    rng = np.random.default_rng(seed)
    bs = []
    for _ in range(2000):
        i = rng.integers(0, len(dy), len(dy))
        bs.append(np.linalg.lstsq(X[i], dy[i], rcond=None)[0][0])
    lo, hi = np.percentile(bs, [2.5, 97.5])
    out["R1_pair_adjusted_for_hubness"] = {"pct": float(np.exp(beta[0]) - 1), "lo": float(np.exp(lo) - 1), "hi": float(np.exp(hi) - 1),
                                           "slope_on_d_log1p_kocc": float(beta[1]), "mean_d_log1p_kocc": float(X[:, 1].mean()),
                                           "n_pairs": int(len(t))}

    # (vi) does the primary miss hubness / density? (treated papers are compared with typical, not hub, papers there)
    out["primary_plus_log1p_kocc"] = core._fit(d, "y", F, core.controls(F, ["lkocc"]))
    out["primary_plus_density10"] = core._fit(d, "y", F, core.controls(F, ["dens10_z"]))
    return out


# --------------------------------------------------------------------------------------------
# alternative explanations
# --------------------------------------------------------------------------------------------
def _v1_status(F: str, t: pd.Series) -> pd.Series:
    t = t.fillna("")
    if F == "G3_question":
        return t.str.contains("?", regex=False).astype(int)
    if F == "G4_llm_words":
        return t.map(lambda s: R24_RX.search(s) is not None).astype(int)
    raise ValueError(F)


def alt_explanations(df: pd.DataFrame, F: str) -> dict:
    d = audit_g1g2.add_columns(df).reset_index(drop=True)
    Cc = core.controls(F)
    ab = d.abstract.fillna("")
    d["bench"] = (d.title.str.contains(BENCH_T) | ab.map(lambda a: BENCH_A.search(a) is not None)).astype(int)
    d["llm"] = d.llm_topic.fillna(False).astype(bool).astype(int)
    d["f24_abs"] = d.f24.fillna(False).astype(bool).astype(int)
    out = {"label": LABEL, "feature": F}

    a = d[d.arxiv_month_idx.notna()]
    out["timing"] = {"label": LABEL, "mean_lead_months": _by(a, F, "lead_months"),
                     "lead_months_diff_primary_controls": core._fit(a, "lead_months", F, Cc),
                     "arxiv_only_primary_spec": _nw(core._fit(a, "y", F, Cc), a, F),
                     "arxiv_only_plus_lead_bin_fe": _nw(core._fit(a, "y", F, Cc, fe="year^topic50 + lead_bin"), a, F)}
    out["code"] = {"label": LABEL, "share": _by(d, F, "code_link"), "plus_code_control": core._fit(d, "y", F, Cc + ["code_link"])}
    out["paper_type"] = {
        "label": LABEL, "bench_title_regex": BENCH_T.pattern, "bench_abstract_regex": BENCH_A.pattern,
        "share_method": _by(d, F, "method_abs"), "share_finding": _by(d, F, "finding_abs"), "share_benchmark": _by(d, F, "bench"),
        "benchmark_share_diff_primary_controls_pp": _pp(core._fit(d, "bench", F, Cc)),
        "benchmark_indicator_coef": core._fit(d, "y", "bench", Cc + [F]),
        "plus_benchmark_control": core._fit(d, "y", F, Cc + ["bench"]),
        "benchmark_papers_excluded": _nw(core._fit(d[d.bench == 0], "y", F, Cc), d[d.bench == 0], F),
        "plus_method_finding_benchmark_controls": core._fit(d, "y", F, Cc + ["method_abs", "finding_abs", "bench"]),
        "within_finding_abstracts": _nw(core._fit(d[d.finding_abs == 1], "y", F, Cc), d[d.finding_abs == 1], F),
        "within_non_finding_abstracts": _nw(core._fit(d[d.finding_abs == 0], "y", F, Cc), d[d.finding_abs == 0], F)}
    out["topic"] = {"label": LABEL, "share_llm_topic": _by(d, F, "llm"), "plus_llm_topic_control": core._fit(d, "y", F, Cc + ["llm"])}
    out["llm_style"] = {"label": LABEL, "share_f24_abstract": _by(d, F, "f24_abs"),
                        "plus_f24_abstract_control": core._fit(d, "y", F, Cc + ["f24_abs"])}

    tail = {"label": LABEL}
    r = core._fit(d, "cite_pctile", F, Cc)
    tail["cite_percentile_outcome_pp"] = {"b_pp": r["b"], "lo_pp": r["b"] - 1.96 * r["se"], "hi_pp": r["b"] + 1.96 * r["se"],
                                          "p": r["p"], "n": r["n"]}
    cap5 = d.groupby("year").cites.transform(lambda s: s.quantile(0.95))
    tail["drop_top5pct_per_year"] = _nw(core._fit(d[d.cites <= cap5], "y", F, Cc), d[d.cites <= cap5], F)
    tail["drop_zero_citation_records"] = _nw(core._fit(d[d.cites > 0], "y", F, Cc), d[d.cites > 0], F)
    top = d[d[F] == 1].sort_values("cites", ascending=False)
    tail["most_cited_feature_papers"] = [{"year": int(x.year), "cites": int(x.cites), "title": x.title} for x in top.head(5).itertuples()]
    tail["ppml_drop_k_most_cited_feature_papers"] = {
        str(k): core._fit(d.drop(index=top.index[:k]), "cites", F, Cc, poisson=True) for k in (0, 1, 2, 3)}
    cap1 = d.groupby("year").cites.transform(lambda s: s.quantile(0.99))
    tail["ppml_drop_top1pct_per_year"] = core._fit(d[d.cites <= cap1], "cites", F, Cc, poisson=True)
    tail["note"] = ("Dropping only the most-cited feature papers is one-sided (biased against the feature by construction); "
                    "it shows how many papers the R2 sign rests on. Dropping the top 1% per year is symmetric.")
    out["tail"] = tail

    A = pd.read_csv(AUDIT_PAIRS)
    A = A[A.decision == "accepted"]
    m = d.merge(A[["submission_id", "v1_title", "or_title"]], on="submission_id", how="inner")
    m["F_v1"] = _v1_status(F, m.v1_title).to_numpy()
    out["retitling"] = {
        "label": LABEL, "source": "outputs/snapshot/audit_pairs.csv (accepted, arXiv v1 posted before the decision)",
        "n_papers": int(len(m)), "years": sorted(int(y) for y in m.year.unique()),
        "camera_ready_rule_reproduces_feature": float((_v1_status(F, m.or_title) == m[F]).mean()),
        "n_with_camera_ready": int(m[F].sum()), "n_with_v1": int(m.F_v1.sum()),
        "added_at_camera_ready": int(((m[F] == 1) & (m.F_v1 == 0)).sum()),
        "removed_at_camera_ready": int(((m[F] == 0) & (m.F_v1 == 1)).sum()),
        "added_titles": m.loc[(m[F] == 1) & (m.F_v1 == 0), ["v1_title", "title"]].to_dict(orient="records"),
        "note": "too few feature papers in the audited subsample for an estimate; counts only"}

    if F == "G4_llm_words":
        d["n24"] = d.title.map(lambda s: N24_RX.search(s) is not None).astype(int)
        d["improve_frame"] = ((d.n24 == 1) | (d[F] == 1)).astype(int)
        post = d[d.year >= 2023]
        fr = d[d.improve_frame == 1]
        out["neutral_synonyms_N24"] = {
            "label": LABEL, "regex": N24_RX.pattern, "n": int(d.n24.sum()), "n_2023plus": int(post.n24.sum()),
            "N24_primary_spec": _nw(core._fit(d, "y", "n24", Cc), d, "n24"),
            "N24_primary_spec_2023plus": _nw(core._fit(post, "y", "n24", Cc), post, "n24"),
            "G4_primary_spec_2023plus": _nw(core._fit(post, "y", F, Cc), post, F),
            "G4_vs_N24_within_improvement_framed_titles": {**_nw(core._fit(fr, "y", F, Cc), fr, F), "n_titles": int(len(fr))},
            "G4_plus_N24_control": core._fit(d, "y", F, Cc + ["n24"]),
            "note": "N24 is the D3 neutral-synonym benchmark. If 'improvement-framed' titles in general go with fewer "
                    "citations, the G4 point estimate is not specific to LLM-favoured vocabulary."}
        X = d[core.R24_WORDS].fillna(False).astype(int)
        sep = {}
        for w in core.R24_WORDS:
            if X[w].sum() >= 20:
                dd = d.assign(**{w: X[w]})
                sep[w] = _nw(core._fit(dd, "y", w, Cc), dd, w)
        out["families_one_at_a_time_vs_all_other_papers"] = {
            "label": LABEL, **sep,
            "note": "each family with n >= 20 in its own model against all other papers (including other-family G4 "
                    "papers); sensitivity for the pre-specified one-model family secondary"}
    return out


def summary_lines(cal: dict, alt: dict) -> list[str]:
    f = lambda r: f"{100 * r['pct']:+.1f}% [{100 * r['lo']:+.1f}, {100 * r['hi']:+.1f}]"
    P, H, R, S = cal["placebo"], cal["hubness"], cal["residual_decomposition"], cal["csls_matching"]
    L = [f"R1 obs {100 * P['observed_pct']:+.1f}%  null mean {100 * P['null_mean_pct']:+.1f}%  adj {100 * P['adjusted_pct']:+.1f}% "
         f"[{100 * P['adjusted_lo']:+.1f}, {100 * P['adjusted_hi']:+.1f}] p {P['placebo_p_two_sided']:.3f}",
         f"hubness log1p kocc treated/controls/all {H['mean_log1p_kocc']}  y~lkocc {f(H['y_on_log1p_kocc_primary_controls'])}  "
         f"y~dens {f(H['y_on_density10_z_primary_controls'])}",
         f"residuals treated {R['treated_mean_residual_log']:+.3f} controls {R['matched_controls_mean_residual_log']:+.3f} "
         f"R1-excess {100 * R['R1_minus_control_excess_pct']:+.1f}%",
         f"CSLS {f(S)} null {100 * S['calibration']['null_mean_pct']:+.1f}% adj {100 * S['calibration']['adjusted_pct']:+.1f}% "
         f"[{100 * S['calibration']['adjusted_lo']:+.1f}, {100 * S['calibration']['adjusted_hi']:+.1f}]",
         f"pair-adj hubness {f(cal['R1_pair_adjusted_for_hubness'])}  primary+lkocc {f(cal['primary_plus_log1p_kocc'])}  "
         f"primary+dens {f(cal['primary_plus_density10'])}"]
    T, Pt, Tl = alt["timing"], alt["paper_type"], alt["tail"]
    L += [f"timing lead {T['mean_lead_months']} arxiv {f(T['arxiv_only_primary_spec'])} +leadFE {f(T['arxiv_only_plus_lead_bin_fe'])}",
          f"code {alt['code']['share']} +code {f(alt['code']['plus_code_control'])}",
          f"bench {Pt['share_benchmark']} +bench {f(Pt['plus_benchmark_control'])} excl {f(Pt['benchmark_papers_excluded'])} "
          f"({Pt['benchmark_papers_excluded']['n_with']})  +method/finding/bench {f(Pt['plus_method_finding_benchmark_controls'])}",
          f"finding {Pt['share_finding']} within finding {f(Pt['within_finding_abstracts'])} non {f(Pt['within_non_finding_abstracts'])}",
          f"+llm {f(alt['topic']['plus_llm_topic_control'])}  f24 {alt['llm_style']['share_f24_abstract']} +f24 "
          f"{f(alt['llm_style']['plus_f24_abstract_control'])}",
          f"pctile {Tl['cite_percentile_outcome_pp']}  drop top5 {f(Tl['drop_top5pct_per_year'])}  drop zero {f(Tl['drop_zero_citation_records'])}",
          "PPML drop k: " + "  ".join(f"{k}: {f(v)}" for k, v in Tl["ppml_drop_k_most_cited_feature_papers"].items())
          + f"  drop top1%/yr {f(Tl['ppml_drop_top1pct_per_year'])}",
          f"retitling {({k: v for k, v in alt['retitling'].items() if k not in ('added_titles', 'note', 'source', 'label')})}"]
    if "neutral_synonyms_N24" in alt:
        N = alt["neutral_synonyms_N24"]
        L.append(f"N24 n {N['n']} {f(N['N24_primary_spec'])}  2023+ {f(N['N24_primary_spec_2023plus'])}  G4 2023+ "
                 f"{f(N['G4_primary_spec_2023plus'])}  G4 vs N24 {f(N['G4_vs_N24_within_improvement_framed_titles'])}  "
                 f"G4+N24 {f(N['G4_plus_N24_control'])}")
        for w, r in alt["families_one_at_a_time_vs_all_other_papers"].items():
            if isinstance(r, dict):
                L.append(f"  family alone {w} {r['n_with']} {f(r)} p {r['p']:.3f}")
    return L
