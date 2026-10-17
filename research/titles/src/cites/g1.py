"""G1: coined method name ('NAME: subtitle') and citations among accepted ICLR papers 2017-2025.

Pre-registration: docs/CITES_PREREG.md. Frozen core: cites/core.py (not edited here).

What this module does
  1. Primary (pre-registered): reads the frozen estimate and Holm p for G1_name from outputs/cites/primary.json
     and re-computes it with core.primary as a reproduction check (the frozen numbers are the ones reported).
  2. Robustness R1-R7 (pre-registered): core.robustness.
  3. Verdict (pre-registered rule): core.verdict(frozen primary, robustness, frozen Holm p).
  4. Secondary (pre-registered, prereg section 6; no multiplicity claim):
       - name orthography: mixed case / ALL CAPS / word, each vs no-name, in one model (the 8 paren-acronym
         names get their own dummy so that the reference group is exactly 'no name');
       - joint model with all 8 primary features;
       - heterogeneity by LLM-topic papers.
  5. Diagnostics (NOT pre-registered; every block is labelled so in results.json):
       (a) S2 split-record artefact: match rate and arXiv-id share by G1 status; primary spec restricted to
           records with / without an arXiv id; primary spec with an arXiv-id indicator as control;
       (b) method-paper confound: abstract says 'we propose|we introduce|we present|this paper proposes';
       (c) team prior: R6 compared with the same-sample R5 (2022-25) estimate without the control;
       plus orthography pairwise contrasts and orthography-specific content-matched pairs.

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m cites.g1
Writes outputs/cites/G1/{results.json, fig.png, fig.pdf, fig.csv}.
"""
from __future__ import annotations

import json
import re
import warnings

import numpy as np
import pandas as pd
import pyfixest as pf

from analyses import _core as C
from cites import core

warnings.filterwarnings("ignore")

F = "G1_name"
DST = core.OUT / "G1"
DIAG = "diagnostic (not pre-registered)"
ORTHO = ["ortho_mixed_case", "ortho_all_caps", "ortho_word"]          # pre-specified classes
ORTHO_ALL = ORTHO + ["ortho_paren_acronym"]                           # + residual class (n = 8)
ORTHO_LABEL = {"ortho_mixed_case": "mixed case (e.g. LoRA)", "ortho_all_caps": "ALL CAPS (e.g. CRISP)",
               "ortho_word": "ordinary word (e.g. Chameleon)", "ortho_paren_acronym": "phrase (ACRONYM)"}
METHOD_RX = re.compile(r"\b(?:we propose|we introduce|we present|this paper proposes)\b", re.I)
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


def fmt(r: dict) -> str:
    if r.get("pct") is None:
        return "n/a"
    return f"{100 * r['pct']:+.1f}% [{100 * r['lo']:+.1f}, {100 * r['hi']:+.1f}]"


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


def secondary_orthography(df: pd.DataFrame) -> dict:
    """Pre-specified (prereg s6): each orthography class vs no-name in one model (reference = G1_name == 0)."""
    out = {}
    for o in ORTHO_ALL:
        others = [x for x in ORTHO_ALL if x != o]
        r = core._fit(df, "y", o, core.controls(F, others))
        r["n_with"] = int(df[o].sum())
        r["label"] = ORTHO_LABEL[o]
        r["prespecified"] = o in ORTHO
        out[o] = r
    out["note"] = ("One model, y ~ ortho_mixed_case + ortho_all_caps + ortho_word + ortho_paren_acronym + primary controls "
                   "| year^topic50, SE clustered by topic50; the four dummies partition G1_name, so each coefficient "
                   "compares that class with untitled-name papers. ortho_paren_acronym (n = 8) is a residual class "
                   "kept only to make the reference group exactly 'no name'; it is not interpreted.")
    return out


def secondary_joint(df: pd.DataFrame) -> dict:
    """Pre-specified (prereg s6, all questions): G1 coefficient in a joint model with all 8 primary features."""
    others = [f for f in core.FEATURES if f != F]
    r = core._fit(df, "y", F, core.controls(F, others))
    r["model"] = "y ~ all 8 primary features + primary controls | year^topic50"
    return r


def secondary_llm(df: pd.DataFrame) -> dict:
    """Pre-specified (prereg s6, all questions): heterogeneity by LLM-topic papers."""
    d = df.copy()
    d["llm"] = d.llm_topic.fillna(False).astype(int)
    d["G1_in_llm"] = d[F] * d.llm
    d["G1_in_nonllm"] = d[F] * (1 - d.llm)
    d["G1_x_llm"] = d[F] * d.llm
    llm = core._fit(d, "y", "G1_in_llm", core.controls(F, ["G1_in_nonllm", "llm"]))
    non = core._fit(d, "y", "G1_in_nonllm", core.controls(F, ["G1_in_llm", "llm"]))
    inter = core._fit(d, "y", "G1_x_llm", core.controls(F, [F, "llm"]))
    llm["n_with"] = int(d.G1_in_llm.sum())
    non["n_with"] = int(d.G1_in_nonllm.sum())
    return {"llm_topic_papers": llm, "non_llm_topic_papers": non,
            "difference_llm_minus_non": {"b": inter["b"], "se": inter["se"], "p": inter["p"],
                                          "ratio": float(np.exp(inter["b"])),
                                          "ratio_lo": float(np.exp(inter["b"] - 1.96 * inter["se"])),
                                          "ratio_hi": float(np.exp(inter["b"] + 1.96 * inter["se"]))},
            "n_llm_topic_papers": int(d.llm.sum()),
            "note": "One model with G1 split by llm_topic plus an llm_topic main effect; 'difference' is the "
                    "G1 x llm_topic interaction (ratio of the two citation multipliers)."}


# --------------------------------------------------------------------------------------------
# diagnostics (not pre-registered)
# --------------------------------------------------------------------------------------------
def diag_split_records(df: pd.DataFrame) -> dict:
    """(a) S2 split-record artefact. A venue record without an arXiv id may miss citations that S2 credits to a
    separate arXiv record (qc_split_records.jsonl). If that happens more often for one G1 group, the primary
    estimate is biased. Checks: match rate, arXiv-id share, multi-record share by G1; primary spec within
    records with / without an arXiv id; primary spec + arXiv-id indicator."""
    out = {"label": DIAG}
    # match rate among all accepted papers 2017-2025 (matched_venue.parquet is read only)
    M = pd.read_parquet(core.OUT / "matched_venue.parquet", columns=["submission_id", "year", "matched", "arxiv"])
    M = M[M.year.between(*core.YEARS)]
    nm = C.load_features(["name_primary"])
    M = M.merge(nm, on="submission_id", how="left", validate="1:1")
    out["accepted_2017_25"] = int(len(M))
    out["accepted_missing_G1_feature"] = int(M.name_primary.isna().sum())
    M = M[M.name_primary.notna()].copy()
    M["G1"] = M.name_primary.astype(bool).astype(int)
    M["matched_i"] = M.matched.astype(int)
    out["match_rate"] = {"named": share_ci(M.loc[M.G1 == 1, "matched_i"]), "not_named": share_ci(M.loc[M.G1 == 0, "matched_i"])}
    m = pf.feols("matched_i ~ G1 | year", data=M, vcov="hetero")
    t = m.tidy().loc["G1"]
    b, se = float(t["Estimate"]), float(t["Std. Error"])
    out["match_rate_diff_year_fe_pp"] = {"b_pp": 100 * b, "lo_pp": 100 * (b - 1.96 * se), "hi_pp": 100 * (b + 1.96 * se),
                                         "p": float(t["Pr(>|t|)"]), "n": int(m._N)}
    out["match_rate_by_year"] = (M.groupby(["year", "G1"]).matched_i.mean().unstack().rename(columns={0: "not_named", 1: "named"})
                                 .round(4).reset_index().to_dict(orient="records"))

    # arXiv-id share among matched records in the analysis frame
    d = df.copy()
    d["has_arxiv"] = d.arxiv.notna().astype(int)
    d["multi_s2"] = (d.n_s2.fillna(1) > 1).astype(int)
    out["arxiv_share"] = {"named": share_ci(d.loc[d[F] == 1, "has_arxiv"]), "not_named": share_ci(d.loc[d[F] == 0, "has_arxiv"])}
    out["arxiv_share_diff_primary_controls_pp"] = lpm(core._fit(d, "has_arxiv", F, core.controls(F)))
    out["multi_record_share"] = {"named": share_ci(d.loc[d[F] == 1, "multi_s2"]), "not_named": share_ci(d.loc[d[F] == 0, "multi_s2"])}
    out["arxiv_share_by_year"] = (d.groupby(["year", F]).has_arxiv.mean().unstack().rename(columns={0: "not_named", 1: "named"})
                                  .round(4).reset_index().to_dict(orient="records"))

    # QC sample of split records (venue record without arXiv id; S2 title-match lookup)
    q = pd.read_json(core.OUT / "qc_split_records.jsonl", lines=True)
    q = q.merge(d[["submission_id", F]], left_on="sid", right_on="submission_id", how="left")
    q["split"] = (q.match_pid.notna() & (q.match_pid != q.venue_pid))
    out["qc_split_sample"] = {
        "n_checked": int(len(q)), "n_split": int(q.split.sum()),
        "split_by_G1": {str(k): {"n": int(len(g)), "split": int(g.split.sum())} for k, g in q.groupby(q[F].fillna(-1).astype(int))},
        "split_cites_venue_vs_other": [[float(a), float(b)] for a, b in q.loc[q.split, ["venue_cites", "match_cites"]].to_numpy()],
        "note": "Random sample of matched records without an arXiv id (qc_split.py); too small for a G1 comparison, "
                "shown only to size the artefact.",
    }

    # primary spec within arXiv / non-arXiv records, and with an arXiv indicator
    out["primary_spec_arxiv_only"] = with_n(core._fit(d[d.has_arxiv == 1], "y", F, core.controls(F)), d[d.has_arxiv == 1], F)
    out["primary_spec_no_arxiv_only"] = with_n(core._fit(d[d.has_arxiv == 0], "y", F, core.controls(F)), d[d.has_arxiv == 0], F)
    out["primary_spec_plus_arxiv_control"] = core._fit(d, "y", F, core.controls(F, ["has_arxiv"]))
    # difference between the two subsets in one pooled model. has_arxiv shifts y by about 1 log point and its share
    # varies across year x topic cells, so controls and FE are interacted with has_arxiv (a shared-FE interaction
    # model is misspecified here and was not used).
    dd = d.copy()
    dd["G1_x_noarxiv"] = dd[F] * (1 - dd.has_arxiv)
    ctrl = core.controls(F)
    for c in ctrl:
        dd[f"{c}_na"] = dd[c] * (1 - dd.has_arxiv)
    inter = core._fit(dd, "y", "G1_x_noarxiv", ctrl + [F] + [f"{c}_na" for c in ctrl], fe="year^topic50^has_arxiv")
    out["difference_no_arxiv_minus_arxiv"] = {"b": inter["b"], "se": inter["se"], "p": inter["p"],
                                               "ratio": float(np.exp(inter["b"])),
                                               "ratio_lo": float(np.exp(inter["b"] - 1.96 * inter["se"])),
                                               "ratio_hi": float(np.exp(inter["b"] + 1.96 * inter["se"])),
                                               "model": "G1 x no-arXiv interaction; controls and year^topic50 FE interacted with has_arxiv"}
    out["match_rate_trimming_bounds"] = lee_bounds(df, M)
    return out


def lee_bounds(df: pd.DataFrame, M: pd.DataFrame, seed: int = 0) -> dict:
    """Named titles match an S2 venue record less often. Trimming bound (Lee-style, per year): drop from the
    better-matched group the share of papers equal to the excess match rate, from the bottom of y (lower bound
    of the G1 difference) or the top (upper bound), then re-fit the primary spec. Ties broken at random."""
    rng = np.random.default_rng(seed)
    d = df.reset_index(drop=True).copy()
    d["_u"] = rng.random(len(d))
    rate = M.groupby(["year", "G1"]).matched_i.mean().unstack()
    drop_lo, drop_hi, trims = [], [], {}
    for y, r in rate.iterrows():
        r0, r1 = r[0], r[1]
        grp, share = (0, (r0 - r1) / r0) if r0 > r1 else (1, (r1 - r0) / r1)
        trims[int(y)] = {"group_trimmed": "not_named" if grp == 0 else "named", "share": float(share)}
        idx = d.index[(d.year == y) & (d[F] == grp)]
        k = int(round(share * len(idx)))
        if k == 0:
            continue
        s = d.loc[idx].sort_values(["y", "_u"])
        low, high = list(s.index[:k]), list(s.index[-k:])
        # trimming the bottom of the non-named group raises its mean -> lower bound; for the named group the reverse
        if grp == 0:
            drop_lo += low
            drop_hi += high
        else:
            drop_lo += high
            drop_hi += low
    lo = core._fit(d.drop(index=drop_lo), "y", F, core.controls(F))
    hi = core._fit(d.drop(index=drop_hi), "y", F, core.controls(F))
    return {"lower": lo, "upper": hi, "n_trimmed_lower": len(drop_lo), "n_trimmed_upper": len(drop_hi), "trim_by_year": trims,
            "note": "Bounds treat the excess unmatched named papers as missing at the extremes of the outcome distribution."}


def diag_method_paper(df: pd.DataFrame) -> dict:
    """(b) Method-paper confound: abstracts that announce a proposed method."""
    d = df.copy()
    d["method_abs"] = [int(METHOD_RX.search(a or "") is not None) for a in d.abstract]
    out = {"label": DIAG, "regex": METHOD_RX.pattern}
    out["share_method_abstract"] = {"named": share_ci(d.loc[d[F] == 1, "method_abs"]),
                                    "not_named": share_ci(d.loc[d[F] == 0, "method_abs"])}
    out["method_share_diff_primary_controls_pp"] = lpm(core._fit(d, "method_abs", F, core.controls(F)))
    out["primary_spec_plus_method_control"] = core._fit(d, "y", F, core.controls(F, ["method_abs"]))
    out["method_indicator_coef"] = core._fit(d, "y", "method_abs", core.controls(F, [F]))
    out["primary_spec_method_abstracts_only"] = with_n(core._fit(d[d.method_abs == 1], "y", F, core.controls(F)),
                                                       d[d.method_abs == 1], F)
    out["primary_spec_non_method_abstracts_only"] = with_n(core._fit(d[d.method_abs == 0], "y", F, core.controls(F)),
                                                           d[d.method_abs == 0], F)
    d["G1_x_method"] = d[F] * d.method_abs
    inter = core._fit(d, "y", "G1_x_method", core.controls(F, [F, "method_abs"]))
    out["difference_method_minus_non_method"] = {"b": inter["b"], "se": inter["se"], "p": inter["p"],
                                                 "ratio": float(np.exp(inter["b"])),
                                                 "ratio_lo": float(np.exp(inter["b"] - 1.96 * inter["se"])),
                                                 "ratio_hi": float(np.exp(inter["b"] + 1.96 * inter["se"]))}
    return out


def _pairs(df: pd.DataFrame, caliper: float = 0.80):
    """Same pairing as core.matched_pairs (binary feature), returning the pairs themselves."""
    d = df.reset_index(drop=True)
    tr, co = d[F] == 1, d[F] == 0
    Em, found = C.load_masked_embedding(d)
    Ea = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    E = np.where(found[:, None], Em, Ea)
    E = E / np.linalg.norm(E, axis=1, keepdims=True)
    rows = []
    for y in sorted(d.year.unique()):
        ti = np.where(tr & (d.year == y))[0]
        ci = np.where(co & (d.year == y))[0]
        S = E[ti] @ E[ci].T
        j = S.argmax(1)
        s = S[np.arange(len(ti)), j]
        ok = s >= caliper
        rows.append(pd.DataFrame({"t": ti[ok], "c": ci[j[ok]], "cos": s[ok], "year": y}))
    return d, pd.concat(rows, ignore_index=True), E


def diag_content_granularity(df: pd.DataFrame, rob: dict) -> dict:
    """Why is R1 (content-matched pairs) smaller than the primary? Two candidate reasons: (i) R1 matches content
    more finely than 20 PCs + year x topic50 cells; (ii) R1 does not adjust for team size / abstract length.
    (i): primary spec with 50 / 100 PCs (unmasked and name-masked embedding); R1 at tighter calipers.
    (ii): R1 pairs with the within-pair difference regressed on within-pair differences in the two controls."""
    import statsmodels.api as sm
    out = {"label": DIAG}
    d, P, Em = _pairs(df)
    dy = d.y.to_numpy()[P.t] - d.y.to_numpy()[P.c]
    out["pairs_reimplementation_check"] = {"n_pairs": int(len(P)), "pct": float(np.exp(dy.mean()) - 1),
                                           "core_R1_n_pairs": rob["R1_matched_pairs"]["n_pairs"],
                                           "core_R1_pct": rob["R1_matched_pairs"]["pct"]}
    X = pd.DataFrame({"d_log_authors": d.log_authors.to_numpy()[P.t] - d.log_authors.to_numpy()[P.c],
                      "d_log_abs_words": d.log_abs_words.to_numpy()[P.t] - d.log_abs_words.to_numpy()[P.c]})
    out["pair_control_differences_mean"] = X.mean().to_dict()
    m = sm.OLS(dy, sm.add_constant(X)).fit(cov_type="cluster", cov_kwds={"groups": P.c.to_numpy()})
    a, se = float(m.params["const"]), float(m.bse["const"])
    out["R1_pairs_adjusted_team_size_abs_length"] = {"pct": float(np.exp(a) - 1), "lo": float(np.exp(a - 1.96 * se) - 1),
                                                     "hi": float(np.exp(a + 1.96 * se) - 1), "p": float(m.pvalues["const"]),
                                                     "n_pairs": int(len(P)),
                                                     "coef_d_log_authors": float(m.params["d_log_authors"]),
                                                     "note": "intercept of d_y ~ 1 + d_log_authors + d_log_abs_words; SE clustered by control paper (pairs share controls)"}
    from sklearn.decomposition import PCA
    Ea = C.load_embedding(d, "abstract", "bge-small-en-v1.5")
    Ea = Ea / np.linalg.norm(Ea, axis=1, keepdims=True)
    pcs = {"unmasked": PCA(n_components=100, svd_solver="full").fit_transform(Ea),
           "name_masked": PCA(n_components=100, svd_solver="full").fit_transform(Em)}
    base = ["log_authors", "log_abs_words"]
    res = {}
    for emb, Z in pcs.items():
        for k in (20, 50, 100):
            dk = d.copy()
            cols = [f"zz{i}" for i in range(k)]
            dk[cols] = Z[:, :k]
            r = core._fit(dk, "y", F, base + cols)
            res[f"{emb}_{k}pcs"] = r
    out["primary_spec_more_pcs"] = res
    out["R1_caliper"] = {f"{c:.2f}": core.matched_pairs(df, F, caliper=c) for c in (0.85, 0.90)}
    return out


def diag_team_prior(df: pd.DataFrame, rob: dict) -> dict:
    """(c) Team prior: R6 (pre-registered) against R5 2022-25 (same sample, no team-prior control)."""
    d = df[df.year >= 2022]
    r5, r6 = rob["R5_era_2022_25"], rob["R6_team_prior_2022_25"]
    return {"label": DIAG + " - comparison of two pre-registered checks",
            "R5_2022_25_no_team_prior": r5, "R6_2022_25_with_team_prior": r6,
            "change_in_b": r6["b"] - r5["b"], "share_of_b_removed": float(1 - r6["b"] / r5["b"]) if r5["b"] else None,
            "mean_log1p_prior_accs": {"named": float(d.loc[d[F] == 1, "lprior_acc"].mean()),
                                      "not_named": float(d.loc[d[F] == 0, "lprior_acc"].mean())},
            "team_prior_coef": core._fit(d, "y", "lprior_acc", core.controls(F, [F])),
            "n_2022_25": int(len(d))}


def diag_orthography(df: pd.DataFrame) -> dict:
    """Orthography follow-ups: pairwise contrasts (reference = mixed case) and content-matched pairs per class."""
    out = {"label": DIAG}
    pw = {}
    # coefficient on X with G1_name in the model = X minus the omitted named class (mixed case)
    for o in ["ortho_all_caps", "ortho_word"]:
        others = [x for x in ["ortho_all_caps", "ortho_word", "ortho_paren_acronym"] if x != o]
        pw[f"{o}_minus_mixed_case"] = core._fit(df, "y", o, core.controls(F, [F] + others))
    pw["ortho_word_minus_all_caps"] = core._fit(df, "y", "ortho_word", core.controls(F, [F, "ortho_mixed_case", "ortho_paren_acronym"]))
    for k, r in pw.items():
        r["ratio"] = float(np.exp(r["b"]))
    out["pairwise_ratio_of_multipliers"] = pw
    mp = {}
    for o in ORTHO:
        sub = df[(df[o] == 1) | (df[F] == 0)]
        mp[o] = core.matched_pairs(sub, F)
    out["matched_pairs_vs_no_name"] = mp
    return out


# --------------------------------------------------------------------------------------------
# figure
# --------------------------------------------------------------------------------------------
def figure(prim: dict, rob: dict) -> dict:
    import matplotlib.pyplot as plt
    rows = [("Primary", prim, C.COLORS[0])] + [(ROB_LABEL[k], rob[k], C.TEXT2) for k in ROB_LABEL]
    lab = [r[0] for r in rows]
    est = np.array([100 * r[1]["pct"] for r in rows])
    lo = np.array([100 * r[1]["lo"] for r in rows])
    hi = np.array([100 * r[1]["hi"] for r in rows])
    fig, ax = C.new_fig(width=6.2, height=3.3)
    ypos = np.arange(len(rows))[::-1]
    ax.axvline(0, color=C.TEXT2, lw=0.8, zorder=1)
    for yv, e, l_, h, (_, _, c) in zip(ypos, est, lo, hi, rows):
        ax.plot([l_, h], [yv, yv], color=c, lw=2.0, solid_capstyle="round", zorder=2)
        ax.plot([e], [yv], "o", color=c, ms=7 if c == C.COLORS[0] else 5.5, mec=C.BG, mew=1.2, zorder=3)
    ax.set_yticks(ypos, lab)
    for t, (_, _, c) in zip(ax.get_yticklabels(), rows):
        t.set_fontweight("bold" if c == C.COLORS[0] else "normal")
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", visible=False)
    xmax = max(hi.max(), 0) + 8
    xmin = min(lo.min(), 0) - 4
    ax.set_xlim(xmin, xmax + 22)
    f_ = lambda v: f"{v:+.1f}" if abs(v) < 1 else f"{v:+.0f}"
    for yv, e, l_, h in zip(ypos, est, lo, hi):
        ax.text(xmax + 21, yv, f"{f_(e)}%  [{f_(l_)}, {f_(h)}]", ha="right", va="center", fontsize=7.5, color=C.TEXT2)
    ax.set_xticks([t for t in ax.get_xticks() if xmin <= t <= xmax])
    ax.set_xticklabels([f"{t:+.0f}%" if t else "0" for t in ax.get_xticks()])
    ax.set_xlabel("Difference in citations, named vs other titles (95% CI)")
    ax.set_title("'NAME: subtitle' titles, accepted ICLR papers 2017-25", loc="left", fontsize=9, pad=8)
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
        "question": "G1: among accepted ICLR papers 2017-2025, do papers whose titles lead with a coined method name "
                    "('NAME: subtitle') receive more or fewer Semantic Scholar citations than papers with similar content?",
        "feature": F, "label": core.FEATURES[F],
        "outcome": "y = log(1 + Semantic Scholar citationCount, retrieved 2026-10-17); % difference = exp(b) - 1",
        "primary": P,
        "robustness": rob,
        "verdict": verdict,
        "verdict_inputs": {"p_holm": p_holm, "R1_sign_same": (rob["R1_matched_pairs"]["pct"] > 0) == (prim["pct"] > 0),
                           "R2_sign_same": (rob["R2_ppml_counts"]["pct"] > 0) == (prim["pct"] > 0)},
        "secondary_prespecified": {
            "orthography_vs_no_name": secondary_orthography(df),
            "joint_model_8_features": secondary_joint(df),
            "llm_topic_heterogeneity": secondary_llm(df),
        },
        "diagnostics_not_preregistered": {
            "label": DIAG,
            "a_s2_split_records": diag_split_records(df),
            "b_method_paper_confound": diag_method_paper(df),
            "c_team_prior": diag_team_prior(df, rob),
            "orthography_followups": diag_orthography(df),
            "content_granularity": diag_content_granularity(df, rob),
        },
    }
    res["figure"] = {k: str(v) for k, v in figure(prim, rob).items()}
    json.dump(res, open(DST / "results.json", "w"), indent=1, default=float)

    # console summary
    print(f"reproduction ok: {P['reproduction_ok']}  max|diff| {P['max_abs_diff']:.2e}")
    print(f"primary {fmt(prim)}  holm p {p_holm:.2e}  n {prim['n']}  n_with {prim['n_with']}")
    for k in ROB_LABEL:
        r = rob[k]
        extra = f"n_pairs {r['n_pairs']}" if "n_pairs" in r else f"p {r['p']:.2e} n {r['n']}"
        print(f"  {k:26s} {fmt(r)}  {extra}")
    print("verdict:", verdict)
    so = res["secondary_prespecified"]["orthography_vs_no_name"]
    for o in ORTHO_ALL:
        print(f"  {o:20s} {fmt(so[o])}  p {so[o]['p']:.2e}  n_with {so[o]['n_with']}")
    j = res["secondary_prespecified"]["joint_model_8_features"]
    print(f"joint 8: {fmt(j)} p {j['p']:.2e}")
    L = res["secondary_prespecified"]["llm_topic_heterogeneity"]
    print(f"llm {fmt(L['llm_topic_papers'])}  non-llm {fmt(L['non_llm_topic_papers'])}  diff p {L['difference_llm_minus_non']['p']:.3f}")
    A = res["diagnostics_not_preregistered"]["a_s2_split_records"]
    print("match rate", {k: round(v["share"], 4) for k, v in A["match_rate"].items()}, A["match_rate_diff_year_fe_pp"])
    print("arxiv share", {k: round(v["share"], 4) for k, v in A["arxiv_share"].items()}, A["arxiv_share_diff_primary_controls_pp"])
    print("arxiv only", fmt(A["primary_spec_arxiv_only"]), "no arxiv", fmt(A["primary_spec_no_arxiv_only"]),
          "+ctrl", fmt(A["primary_spec_plus_arxiv_control"]), "diff p", round(A["difference_no_arxiv_minus_arxiv"]["p"], 3))
    print("qc", A["qc_split_sample"])
    B = res["diagnostics_not_preregistered"]["b_method_paper_confound"]
    print("method share", {k: round(v["share"], 4) for k, v in B["share_method_abstract"].items()},
          "+ctrl", fmt(B["primary_spec_plus_method_control"]), "method coef", fmt(B["method_indicator_coef"]),
          "within method", fmt(B["primary_spec_method_abstracts_only"]), "within non", fmt(B["primary_spec_non_method_abstracts_only"]))
    T = res["diagnostics_not_preregistered"]["c_team_prior"]
    print("R5 22-25", fmt(T["R5_2022_25_no_team_prior"]), "R6", fmt(T["R6_2022_25_with_team_prior"]), "share removed", T["share_of_b_removed"])
    O = res["diagnostics_not_preregistered"]["orthography_followups"]
    for k, r in O["pairwise_ratio_of_multipliers"].items():
        print(f"  {k:32s} ratio {r['ratio']:.3f}  p {r['p']:.3f}")
    for k, r in O["matched_pairs_vs_no_name"].items():
        print(f"  MP {k:20s} {fmt(r)} n_pairs {r.get('n_pairs')}")
    print("arxiv diff (interacted)", A["difference_no_arxiv_minus_arxiv"])
    lb = A["match_rate_trimming_bounds"]
    print("trim bounds", fmt(lb["lower"]), fmt(lb["upper"]), lb["n_trimmed_lower"], lb["n_trimmed_upper"])
    print("method x G1", B["difference_method_minus_non_method"])
    G = res["diagnostics_not_preregistered"]["content_granularity"]
    print("pairs check", G["pairs_reimplementation_check"], G["pair_control_differences_mean"])
    print("R1 adjusted", fmt(G["R1_pairs_adjusted_team_size_abs_length"]), G["R1_pairs_adjusted_team_size_abs_length"]["p"])
    for k, r in G["primary_spec_more_pcs"].items():
        print(f"  {k:22s} {fmt(r)}  p {r['p']:.2e}")
    for k, r in G["R1_caliper"].items():
        print(f"  caliper {k} {fmt(r)} n_pairs {r['n_pairs']}")


if __name__ == "__main__":
    main()
