"""WP4: camera-ready snapshot bounds (PLAN D4 "Decision-stage bound", V7, section 4 Gate).

The exported titles of ACCEPTED papers may be camera-ready versions (edited after the decision); rejected,
withdrawn and desk-rejected papers keep submission-stage text. The arXiv audit compares each audited paper's
arXiv version 1 (posted BEFORE the ICLR decision date, `arxiv_audit.DECISION_DATE`) with the stored title.
The rejected papers' v1-vs-stored differences measure everything that is not camera-ready editing (arXiv vs
OpenReview wording, rebuttal-period edits); the accepted-minus-rejected difference ("net-flip DiD") is the
camera-ready excess that can bias any acceptance association of a title feature.

Inputs (read-only): cache/arxiv_audit.jsonl (original title-route audit, 616 papers), and, when present,
cache/arxiv_audit_route.jsonl (V7 route re-query), cache/arxiv_audit_v1abs.jsonl (arXiv v1 abstracts of the
original pre-decision pairs), cache/arxiv_audit_enlarge.jsonl (background enlargement, partial) - all written by
analyses/audit_v2.py; outputs/core/universe.parquet and outputs/features/features_v2.parquet.

Definitions
- Usable pair: found on arXiv, v1 title present, v1 date < decision date of the conference year.
- Features are computed with features_v2.build on the v1 title and on the stored title (identical code path;
  the stored-title features reproduce features_v2.parquet exactly). Abstract features in the abstract audit use
  the arXiv v1 abstract vs the stored abstract ('---' is normalised to an em dash in both).
- Flip matrix per feature and decision: stay0, adds (0->1), drops (1->0), stay1; feature-present v1
  denominators; drop rate = drops / v1-present; add rate = adds / v1-absent; net flip = (adds - drops) / n.
- Net-flip DiD D = net(accepted) - net(rejected). PRIMARY 95% CI: Wald with a pseudo-flip variance floor
  (one pseudo-add and one pseudo-drop per arm; plain Wald SEs collapse to 0 when an arm has no flips, which
  would make any tipping point look "identified"). Plain Wald and a 2,000-replicate bootstrap stratified by
  year x decision are reported alongside.
- Auditable (pre-stated): v1-present count >= 10 in BOTH accepted and rejected pairs of the primary sample.
  D4's interim rule (>= 10 accepted v1-present and >= 10 accepted stored-present) is reported for comparison.
- Acceptance associations come from the universe, 2024-26 pooled (year-standardised to s0 sizes, as in D4) and
  per year: stage sets s0 = U, s2 = reviewed (stage_s2), s3 = accepted; G_dec = P3/P2, G_total = P3/P0;
  accepted share a_k of s_k. A camera-ready net addition D shifts P3 by D and P_k by a_k D, so the
  submission-stage gain is G(D) = (P3 - D)/(P_k - a_k D). Tipping points: D*_dec = (P3 - P2)/(1 - a2),
  D*_total = (P3 - P0)/(1 - a0); D*_dec equals the accepted-minus-rest risk difference.
  Identified (PLAN gate) iff auditable and the tipping point lies beyond the audit CI on the side that would
  move G to 1 (G >= 1: D* > upper CI; G < 1: D* < lower CI).
  Editing-corrected G with a combined CI: universe bootstrap replicate b (stratified by year) paired with an
  independent audit bootstrap replicate b.
- Differential findability: logit of found (and of usable pair) on year FE, accepted, log title words and NAME
  (2023-26 audit sample). IPW specs weight usable pairs by 1/p_hat(usable | x) and optionally by population
  design weights N_pop(year, decision)/n_sampled(year, decision).
- V7 route validation: route A = original title route; route B = first-author surname + distinctive abstract
  words (audit_v2.py). Compared on the same random subsample: found rates (McNemar), arXiv-id agreement, usable
  pairs, and title stability (v1 vs stored retitling; latest arXiv title vs stored).

Outputs (outputs/snapshot/): audit_pairs.csv, found_rates.csv, findability_models.csv, retitling.csv,
T4_2_flip_matrices.csv, T4_2_flip_multiclass.csv, T4_2_tipping_points.csv, T4_2_tipping_by_year.csv,
T4_2_identification_by_spec.csv, abstract_audit.csv, gate.csv, route_validation.csv, route_pairs.csv,
results.json, figures fig_S*.{pdf,png,csv}, snapshot_bounds.log.

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.snapshot_bounds [--enlarge-n N]
      (the reported run used --enlarge-n 254: the first 254 records of the still-growing enlargement cache)
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import features_v2 as FV

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import arxiv_audit as A  # noqa: E402

OUTDIR = C.OUT / "snapshot"
ORIG_PATH = C.CACHE / "arxiv_audit.jsonl"
ROUTE_PATH = C.CACHE / "arxiv_audit_route.jsonl"
V1ABS_PATH = C.CACHE / "arxiv_audit_v1abs.jsonl"
ENLARGE_PATH = C.CACHE / "arxiv_audit_enlarge.jsonl"
DEC = A.DECISION_DATE
POST = (2024, 2025, 2026)
AUDIT_YEARS = (2023, 2024, 2025, 2026)
N_BOOT = 2000
SEED = 4404
MIN_V1 = 10
Z = 1.959963984540054

# key, label, family, column in the derived feature frame
TITLE_FEATS = [
    ("NAME", "NAME (primary)", "M", "name_primary"),
    ("NAME_strict", "NAME strict", "M", "name_strict"),
    ("NAME_loose", "NAME loose", "M", "name_loose"),
    ("compound", "Compound", "M", "name_compound"),
    ("phrase_colon", "Phrase colon", "M", "phrase_colon"),
    ("title_case", "Title Case", "M", "case_title_case"),
    ("mixed_case_name", "Mixed-case name", "M", "ortho_mixed_case"),
    ("allcaps_name", "ALL-CAPS name", "ortho", "ortho_all_caps"),
    ("word_name", "Word name", "ortho", "ortho_word"),
    ("paren_acronym_name", "(ACR) name", "ortho", "ortho_paren_acronym"),
    ("sentence_case", "Sentence case", "O", "case_sentence_case"),
    ("all_caps_title", "ALL-CAPS title", "O", "case_all_caps"),
    ("mixed_casing", "Mixed casing", "casing", "case_mixed"),
    ("question_opener", "Question opener", "O", "question_opener"),
    ("O_union", "O-union", "O", "O_union"),
    ("slot_llm", "LLM slot word", "L", "slot_llm_any"),
    ("slot_filled", "Any slot filled", "L", "slot_filled_any"),
    ("R24", "R24 word", "L", "r24_any"),
    ("R26", "R26 word", "L", "r26_any"),
    ("title_typo", "Title typography", "L", "title_typo"),
    ("L_title", "L-title union", "L", "L_title"),
    ("using", "'using'", "ctrl", "mk_using"),
    ("via", "'via'", "ctrl", "mk_via"),
    ("llm_abbrev_only", "LLM abbrev-only", "M", "llm_t_abbrev_only"),
]
ABS_FEATS = [
    ("F24", "F24 (RARE21 >= 1)", "L_abs", "f24"),
    ("F24_2", "RARE21 >= 2", "L_abs", "f24_2"),
    ("F26_words", "F26 words", "L_abs", "f26_words"),
    ("abs_emdash", "Abstract em dash", "L_abs", "abs_emdash"),
    ("L_abstract", "L-abstract union", "L_abs", "L_abstract"),
    ("L_abs_words", "F24 or F26 words", "L_abs", "L_abs_words"),
]
MULTI = [("casing", "casing"), ("name_orthography", "ortho_class"), ("slot_state", "slot_state"),
         ("via_using", "via_using")]
FEAT_LABEL = {k: lab for k, lab, _, _ in TITLE_FEATS + ABS_FEATS}
FEAT_FAMILY = {k: fam for k, _, fam, _ in TITLE_FEATS + ABS_FEATS}
FEAT_COL = {k: c for k, _, _, c in TITLE_FEATS + ABS_FEATS}

_LOG = []


def log(msg: str):
    print(msg, flush=True)
    _LOG.append(msg)


# ------------------------------------------------------------------------------------------------
# small statistics helpers
# ------------------------------------------------------------------------------------------------
def wilson(k: float, n: float, z: float = Z) -> tuple[float, float]:
    if n <= 0:
        return (np.nan, np.nan)
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, c - h), min(1.0, c + h))


def newcombe(k1, n1, k2, n2) -> tuple[float, float, float]:
    """p1 - p2 with the Newcombe hybrid-score (MOVER-Wilson) 95% CI."""
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    d = p1 - p2
    return d, d - np.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2), d + np.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)


def read_jsonl(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    rows = []
    for line in path.open():
        try:
            rows.append(json.loads(line))
        except ValueError:
            continue
    return pd.DataFrame(rows)


def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    return o


# ------------------------------------------------------------------------------------------------
# features
# ------------------------------------------------------------------------------------------------
def derive(fr: pd.DataFrame) -> pd.DataFrame:
    fr = fr.copy()
    sl = fr[["slot_improve", "slot_reveal", "slot_exploit", "slot_study_adj"]]
    fr["slot_llm_any"] = (sl == 1).any(axis=1)
    fr["slot_neutral_any"] = (sl == 0).any(axis=1)
    fr["slot_filled_any"] = sl.notna().any(axis=1)
    fr["slot_state"] = np.where(fr.slot_llm_any, "llm", np.where(fr.slot_neutral_any, "neutral", "none"))
    via, using = fr.mk_via.astype(bool), fr.mk_using.astype(bool)
    fr["via_using"] = np.select([via & using, via, using], ["both", "via", "using"], "neither")
    fr["ortho_class"] = fr.name_orthography.fillna("").replace("", "none")
    fr["O_union"] = fr[["case_all_caps", "case_sentence_case", "question_opener"]].astype(bool).any(axis=1)
    fr["L_title"] = fr[["title_typo", "r24_any", "r26_any"]].astype(bool).any(axis=1)
    fr["L_abstract"] = fr[["f24", "f26", "abs_emdash"]].astype(bool).any(axis=1)
    # arXiv-measurable abstract markers: arXiv abstracts carry dashes as TeX '--' or '-', never U+2014/U+2011,
    # so typography cannot be audited through arXiv; the word markers can
    fr["L_abs_words"] = fr[["f24", "f26_words"]].astype(bool).any(axis=1)
    return fr


def _emdash_norm(s: pd.Series) -> pd.Series:
    return s.fillna("").str.replace("---", "—", regex=False)


def build_pairs(rec: pd.DataFrame, U: pd.DataFrame, source: str, v1_abstract: bool = False) -> pd.DataFrame:
    """Usable pairs with v1/stored features for every TITLE/ABS/MULTI feature."""
    if rec.empty:
        return pd.DataFrame()
    r = rec.copy()
    r["usable"] = r.found.astype(bool) & r.v1_title.notna() & r.v1_date.notna() & \
        (r.v1_date.astype(str) < r.year.map(DEC).astype(str))
    if v1_abstract:
        r["usable"] &= r.v1_summary.notna()
    p = r[r.usable].merge(U[["submission_id", "year", "title", "title_nfkc", "abstract"]],
                          on=["submission_id", "year"], how="inner", validate="1:1").reset_index(drop=True)
    if p.empty:
        return pd.DataFrame()
    if "or_title" in p and not (p.or_title == p.title).all():
        log(f"  [warn] {source}: {(p.or_title != p.title).sum()} audit titles differ from universe titles")
    cols = ["submission_id", "year", "title", "title_nfkc", "abstract"]
    st_in = p[cols].copy()
    v1_in = p[["submission_id", "year", "abstract"]].copy()
    v1_in["title"] = p.v1_title.astype(str).map(lambda t: " ".join(t.split()))
    v1_in["title_nfkc"] = v1_in.title.map(C.nfkc)
    if v1_abstract:
        st_in["abstract"] = _emdash_norm(st_in.abstract)
        v1_in["abstract"] = _emdash_norm(p.v1_summary)
    st = derive(FV.build(st_in[cols]))
    v1 = derive(FV.build(v1_in[cols]))
    out = p[["submission_id", "year", "decision", "v1_title", "v1_date", "arxiv_id"]].copy()
    out["or_title"] = p.title
    out["source"] = source
    out["acc"] = out.decision.eq("accepted").astype(int)
    for k, _, _, c in TITLE_FEATS + ABS_FEATS:
        out[f"{k}_or"] = st[c].astype(int).to_numpy()
        out[f"{k}_v1"] = v1[c].astype(int).to_numpy()
    for k, c in MULTI:
        out[f"{k}_or"] = st[c].astype(str).to_numpy()
        out[f"{k}_v1"] = v1[c].astype(str).to_numpy()
    if v1_abstract:
        out["abs_jacc"] = [A.jaccard(a, b) for a, b in zip(v1_in.abstract, st_in.abstract)]
    out["n_words_or"] = st.n_words.to_numpy()
    out["n_words_v1"] = v1.n_words.to_numpy()
    ws = lambda t: " ".join(str(t).split())  # noqa: E731
    out["changed_norm"] = (out.v1_title.map(A.norm_title) != out.or_title.map(A.norm_title)).astype(int)
    out["changed_raw"] = (out.v1_title.map(ws) != out.or_title.map(ws)).astype(int)
    out["case_punct_only"] = ((out.changed_raw == 1) & (out.changed_norm == 0)).astype(int)
    out["title_jacc"] = [A.jaccard(a, b) for a, b in zip(out.v1_title, out.or_title)]
    out["changed_major"] = (out.title_jacc < 0.5).astype(int)
    return out


# ------------------------------------------------------------------------------------------------
# flip tables
# ------------------------------------------------------------------------------------------------
def boot_matrix(P: pd.DataFrame, n_boot: int = N_BOOT, seed: int = SEED) -> np.ndarray:
    strata = P.year.astype(str) + "_" + P.decision
    return np.vstack(list(C.boot_weights(len(P), n_boot, strata=strata.to_numpy(), seed=seed))).astype(np.float64)


def _arm_stats(v1, orr, w):
    net = (orr - v1).astype(float)
    sw = w.sum()
    mu = float((w * net).sum() / sw)
    neff = sw ** 2 / (w ** 2).sum()
    var_raw = float((w * (net - mu) ** 2).sum() / sw) / max(neff - 1, 1)
    pa = float((w * ((v1 == 0) & (orr == 1))).sum() / sw)
    pdr = float((w * ((v1 == 1) & (orr == 0))).sum() / sw)
    Ns = neff + 2
    pa_s, pd_s = (pa * neff + 1) / Ns, (pdr * neff + 1) / Ns
    var_adj = (pa_s + pd_s - (pa_s - pd_s) ** 2) / Ns
    return mu, var_raw, max(var_adj, var_raw), neff


def flip_table(P: pd.DataFrame, keys: list[str], label: str, w: np.ndarray | None = None,
               Wb: np.ndarray | None = None) -> tuple[pd.DataFrame, np.ndarray]:
    """Per-feature flip matrix and net-flip DiD. Returns (table, bootstrap DiD matrix B x F)."""
    w = np.ones(len(P)) if w is None else np.asarray(w, float)
    acc = P.acc.to_numpy() == 1
    V1 = P[[f"{k}_v1" for k in keys]].to_numpy(int)
    OR = P[[f"{k}_or" for k in keys]].to_numpy(int)
    NET = (OR - V1).astype(float)
    if Wb is None:
        Wb = boot_matrix(P)
    did_b = np.zeros((Wb.shape[0], len(keys)))
    for m, sgn in [(acc, 1.0), (~acc, -1.0)]:
        Ww = Wb[:, m] * w[m]
        did_b += sgn * (Ww @ NET[m]) / Ww.sum(1, keepdims=True)
    rows = []
    for j, k in enumerate(keys):
        r = dict(spec=label, feature=k, label=FEAT_LABEL.get(k, k), family=FEAT_FAMILY.get(k, ""))
        var_raw_tot, var_adj_tot = 0.0, 0.0
        for g, m in [("acc", acc), ("rej", ~acc)]:
            v1, orr, ww = V1[m, j], OR[m, j], w[m]
            n = int(m.sum())
            r[f"n_{g}"] = n
            r[f"v1_present_{g}"] = int(v1.sum())
            r[f"or_present_{g}"] = int(orr.sum())
            r[f"stay0_{g}"] = int(((v1 == 0) & (orr == 0)).sum())
            r[f"adds_{g}"] = int(((v1 == 0) & (orr == 1)).sum())
            r[f"drops_{g}"] = int(((v1 == 1) & (orr == 0)).sum())
            r[f"stay1_{g}"] = int(((v1 == 1) & (orr == 1)).sum())
            nv1, nab = r[f"v1_present_{g}"], n - r[f"v1_present_{g}"]
            r[f"drop_rate_{g}"] = r[f"drops_{g}"] / nv1 if nv1 else np.nan
            r[f"drop_rate_lo_{g}"], r[f"drop_rate_hi_{g}"] = wilson(r[f"drops_{g}"], nv1)
            r[f"add_rate_{g}"] = r[f"adds_{g}"] / nab if nab else np.nan
            r[f"add_rate_lo_{g}"], r[f"add_rate_hi_{g}"] = wilson(r[f"adds_{g}"], nab)
            r[f"prev_v1_{g}"] = float((ww * v1).sum() / ww.sum())
            r[f"prev_or_{g}"] = float((ww * orr).sum() / ww.sum())
            mu, vr, va, neff = _arm_stats(v1, orr, ww)
            r[f"net_{g}"], r[f"net_se_{g}"], r[f"neff_{g}"] = mu, np.sqrt(vr), neff
            var_raw_tot += vr
            var_adj_tot += va
        r["did"] = r["net_acc"] - r["net_rej"]
        r["did_se_wald"] = float(np.sqrt(var_raw_tot))
        r["did_se"] = float(np.sqrt(var_adj_tot))
        r["did_lo"], r["did_hi"] = r["did"] - Z * r["did_se"], r["did"] + Z * r["did_se"]
        r["did_lo_wald"], r["did_hi_wald"] = r["did"] - Z * r["did_se_wald"], r["did"] + Z * r["did_se_wald"]
        r["did_lo_boot"], r["did_hi_boot"] = (float(np.quantile(did_b[:, j], .025)),
                                              float(np.quantile(did_b[:, j], .975)))
        r["mde80"] = 2.8 * r["did_se"]
        r["auditable"] = bool(min(r["v1_present_acc"], r["v1_present_rej"]) >= MIN_V1)
        r["auditable_d4rule"] = bool(r["v1_present_acc"] >= MIN_V1 and r["or_present_acc"] >= MIN_V1)
        rows.append(r)
    return pd.DataFrame(rows), did_b


def multiclass_table(P: pd.DataFrame, label: str) -> pd.DataFrame:
    rows = []
    for k, _ in MULTI:
        for dec, g in P.groupby("decision"):
            ct = pd.crosstab(g[f"{k}_v1"], g[f"{k}_or"])
            for a in ct.index:
                for b in ct.columns:
                    if ct.loc[a, b]:
                        rows.append(dict(spec=label, feature=k, decision=dec, v1_class=a, stored_class=b,
                                         n=int(ct.loc[a, b]), changed=bool(a != b)))
    return pd.DataFrame(rows)


# ------------------------------------------------------------------------------------------------
# universe prevalences (stage sets) with bootstrap
# ------------------------------------------------------------------------------------------------
def universe_frame() -> pd.DataFrame:
    fcols = sorted(set(["name_primary", "name_strict", "name_loose", "name_compound", "phrase_colon",
                        "case_title_case", "case_sentence_case", "case_all_caps", "case_mixed",
                        "ortho_mixed_case", "ortho_all_caps", "ortho_word", "ortho_paren_acronym",
                        "question_opener", "slot_improve", "slot_reveal", "slot_exploit", "slot_study_adj",
                        "r24_any", "r26_any", "title_typo", "mk_using", "mk_via", "llm_t_abbrev_only", "f24",
                        "f24_2", "f26_words", "f26", "abs_emdash", "name_orthography", "n_words"]))
    df = C.load_analysis_frame(feature_cols=fcols,
                               universe_cols=["submission_id", "year", "pool", "ACC", "REJ", "stage_s1",
                                              "stage_s2", "stage_s3", "wd_post"])
    df = derive(df)
    df = df[(df.year >= 2023) & df.pool.ne("OTHER")].reset_index(drop=True)
    return df


def stage_prevalences(df: pd.DataFrame, keys: list[str], n_boot: int = N_BOOT, seed: int = SEED) -> dict:
    """Per year y: (S (B+1, F, 4), N (B+1, 4)) for stage sets [s0, s2, s3, rej]; row 0 = point estimate."""
    X = df[[FEAT_COL[k] for k in keys]].astype(float).to_numpy()
    Sg = np.column_stack([np.ones(len(df)), df.stage_s2.astype(float), df.ACC.astype(float),
                          df.REJ.astype(float)])
    F, K = X.shape[1], Sg.shape[1]
    out = {}
    for y in sorted(df.year.unique()):
        m = (df.year == y).to_numpy()
        V = np.concatenate([Sg[m], (X[m][:, :, None] * Sg[m][:, None, :]).reshape(int(m.sum()), -1)], axis=1)
        parts = [V.sum(0)[None]]
        if n_boot:
            parts += [Wb.astype(np.float64) @ V for Wb in C.boot_weights(int(m.sum()), n_boot, seed=seed + int(y))]
        Aa = np.vstack(parts)
        out[int(y)] = (Aa[:, K:].reshape(-1, F, K), Aa[:, :K])
    return out


def pooled(sums: dict, years) -> tuple[np.ndarray, np.ndarray]:
    """Year-standardised (weights = s0 sizes) prevalences (B+1, F, 4) and stage accepted shares (B+1, 4)."""
    years = [y for y in years if y in sums]
    w = np.array([sums[y][1][0, 0] for y in years], float)
    w = w / w.sum()
    P = sum(wi * sums[y][0] / sums[y][1][:, None, :] for wi, y in zip(w, years))
    a = sum(wi * sums[y][1][:, 2:3] / sums[y][1] for wi, y in zip(w, years))  # accepted share of each set
    return P, a


def tipping_table(P: np.ndarray, a: np.ndarray, keys: list[str], flips: pd.DataFrame, did_b: np.ndarray,
                  period: str) -> pd.DataFrame:
    """P: (B+1, F, 4) [s0, s2, s3, rej]; a: (B+1, 4) accepted share per set. flips indexed by feature."""
    fl = flips.set_index("feature")
    nb = min(P.shape[0] - 1, did_b.shape[0])
    rows = []
    for j, k in enumerate(keys):
        P0, P2, P3, Pr = P[0, j]
        a0, a2 = a[0, 0], a[0, 1]
        f = fl.loc[k]
        D, Dlo, Dhi = f.did, f.did_lo, f.did_hi

        def G(x, Pk, ak, p3=P3):
            den = Pk - ak * x
            return (p3 - x) / den if den > 0 else np.nan
        r = dict(period=period, feature=k, label=FEAT_LABEL.get(k, k), family=FEAT_FAMILY.get(k, ""),
                 auditable=bool(f.auditable), P_s0=P0, P_s2=P2, P_s3=P3, P_rej=Pr, acc_share_s0=a0, acc_share_s2=a2,
                 did_pp=100 * D, did_lo_pp=100 * Dlo, did_hi_pp=100 * Dhi, did_lo_boot_pp=100 * f.did_lo_boot,
                 did_hi_boot_pp=100 * f.did_hi_boot, did_lo_wald_pp=100 * f.did_lo_wald,
                 did_hi_wald_pp=100 * f.did_hi_wald)
        b = P[1:nb + 1, j]
        ab = a[1:nb + 1]
        # a net camera-ready addition cannot exceed the accepted prevalence nor fall below P3 - 1:
        # clip the audit values to the feasible range before mapping them to submission-stage gains
        Dlo_c, Dhi_c = max(Dlo, P3 - 1), min(Dhi, P3)
        r["did_feasible_lo_pp"], r["did_feasible_hi_pp"] = 100 * Dlo_c, 100 * Dhi_c
        # acceptance-population risk difference (accepted vs rejected): erased by a net addition D = P3 - P_rej
        r["rd_acc_rej_pp"] = 100 * (P3 - Pr)
        r["rd_acc_rej_identified"] = bool(f.auditable) and bool((P3 - Pr) > Dhi if P3 >= Pr else (P3 - Pr) < Dlo)
        for name, Pk_idx, a_idx in [("dec", 1, 1), ("total", 0, 0)]:
            Pk, ak = P[0, j, Pk_idx], a[0, a_idx]
            Gobs = P3 / Pk if Pk > 0 else np.nan
            tip = (P3 - Pk) / (1 - ak)
            with np.errstate(invalid="ignore", divide="ignore"):
                Gb = b[:, 2] / b[:, Pk_idx]
            # G is decreasing in D on the feasible range (P_k >= a_k P3), so the interval is [G(Dhi), G(Dlo)]
            lo, hi = G(Dhi_c, Pk, ak), G(Dlo_c, Pk, ak)
            # combined: universe replicate b paired with an independent audit draw b. Primary: D_b ~ Normal(D, se)
            # with the pseudo-flip SE (consistent with the primary CI; the bootstrap DiD is degenerate when an
            # arm has no flips); variant: the stratified audit bootstrap replicate b.
            rng = np.random.default_rng(SEED + 31 * j + (0 if name == "dec" else 1))

            def gcomb(Draw):
                Dc = np.clip(Draw, b[:, 2] - 1, b[:, 2])
                den = b[:, Pk_idx] - ab[:, a_idx] * Dc
                with np.errstate(invalid="ignore", divide="ignore"):
                    return np.where(den > 0, (b[:, 2] - Dc) / np.where(den > 0, den, 1), np.nan)
            Gc = gcomb(rng.normal(D, f.did_se, nb))
            Gcb = gcomb(did_b[:nb, j])
            if Gobs >= 1:
                ident = bool(tip > Dhi)
                ident_boot, ident_wald = bool(tip > f.did_hi_boot), bool(tip > f.did_hi_wald)
            else:
                ident = bool(tip < Dlo)
                ident_boot, ident_wald = bool(tip < f.did_lo_boot), bool(tip < f.did_lo_wald)
            r.update({
                f"G_{name}_obs": Gobs, f"G_{name}_lo95": float(np.nanquantile(Gb, .025)),
                f"G_{name}_hi95": float(np.nanquantile(Gb, .975)), f"G_{name}_lo90": float(np.nanquantile(Gb, .05)),
                f"G_{name}_hi90": float(np.nanquantile(Gb, .95)),
                f"tip_{name}_pp": 100 * tip,
                f"G_{name}_sel_point": G(D, Pk, ak), f"G_{name}_audit_lo": lo, f"G_{name}_audit_hi": hi,
                f"G_{name}_corr_lo95": float(np.nanquantile(Gc, .025)), f"G_{name}_corr_hi95": float(np.nanquantile(Gc, .975)),
                f"G_{name}_corr_lo90": float(np.nanquantile(Gc, .05)), f"G_{name}_corr_hi90": float(np.nanquantile(Gc, .95)),
                f"G_{name}_corrboot_lo90": float(np.nanquantile(Gcb, .05)),
                f"G_{name}_corrboot_hi90": float(np.nanquantile(Gcb, .95)),
                f"G_{name}_identified": ident and bool(f.auditable),
                f"G_{name}_identified_boot": ident_boot and bool(f.auditable),
                f"G_{name}_identified_wald": ident_wald and bool(f.auditable),
                f"tip_{name}_margin_pp": 100 * ((tip - Dhi) if Gobs >= 1 else (Dlo - tip)),
            })
            # audit-size multiplier needed for the 95% CI to clear the tipping point if the true DiD were 0
            # (requires the tipping point on the side the observed G implies; SE scales with 1/sqrt(n))
            same_side = (tip > 0) if Gobs >= 1 else (tip < 0)
            r[f"n_factor_{name}_if_D0"] = float((Z * f.did_se / abs(tip)) ** 2) if same_side and tip != 0 else np.nan
            r[f"G_{name}_obs_ci_excl1"] = bool(r[f"G_{name}_lo95"] > 1 or r[f"G_{name}_hi95"] < 1)
            r[f"G_{name}_corr_ci_excl1"] = bool(r[f"G_{name}_corr_lo95"] > 1 or r[f"G_{name}_corr_hi95"] < 1)
            r[f"claim_{name}_passes_gate"] = bool(r[f"G_{name}_identified"] and r[f"G_{name}_obs_ci_excl1"])
        rows.append(r)
    return pd.DataFrame(rows)


# ------------------------------------------------------------------------------------------------
# findability
# ------------------------------------------------------------------------------------------------
def audit_frame(rec: pd.DataFrame, fv: pd.DataFrame) -> pd.DataFrame:
    d = rec.copy()
    d["found"] = d.found.astype(bool)
    d["usable"] = d.found & d.v1_title.notna() & d.v1_date.notna() & \
        (d.v1_date.astype(str) < d.year.map(DEC).astype(str))
    d = d.merge(fv[["submission_id", "n_words", "name_primary"]], on="submission_id", how="left")
    d["acc"] = d.decision.eq("accepted").astype(int)
    d["log_nw"] = np.log(d.n_words.clip(lower=1))
    d["NAME"] = d.name_primary.astype(float)
    d["found_i"] = d.found.astype(int)
    d["usable_i"] = d.usable.astype(int)
    return d


def found_rate_table(d: pd.DataFrame, source: str) -> pd.DataFrame:
    rows = []
    groups = [((y, dec), g) for (y, dec), g in d.groupby(["year", "decision"])]
    groups += [(("all", dec), g) for dec, g in d.groupby("decision")]
    groups += [(("2024-26", dec), g) for dec, g in d[d.year.isin(POST)].groupby("decision")]
    for (y, dec), g in groups:
        n, kf, ku = len(g), int(g.found.sum()), int(g.usable.sum())
        flo, fhi = wilson(kf, n)
        ulo, uhi = wilson(ku, n)
        plo, phi = wilson(ku, kf)
        rows.append(dict(source=source, year=y, decision=dec, n=n, found=kf, found_rate=kf / n, found_lo=flo,
                         found_hi=fhi, usable=ku, usable_rate=ku / n, usable_lo=ulo, usable_hi=uhi,
                         pre_share_found=ku / kf if kf else np.nan, pre_share_lo=plo, pre_share_hi=phi))
    return pd.DataFrame(rows)


def findability_models(d: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    dd = d[d.year.isin(AUDIT_YEARS)].copy()
    tabs, fits = [], {}
    for y in ["found_i", "usable_i"]:
        for form in [f"{y} ~ C(year) + acc", f"{y} ~ C(year) + acc + log_nw + NAME"]:
            res = C.logit(form, dd)
            t = C.or_table(res).reset_index().rename(columns={"index": "term"})
            t["outcome"], t["formula"] = y, form
            tabs.append(t)
            fits[form] = res
    # pre-decision given found
    res = C.logit("usable_i ~ C(year) + acc + log_nw + NAME", dd[dd.found])
    t = C.or_table(res).reset_index().rename(columns={"index": "term"})
    t["outcome"], t["formula"] = "usable_given_found", "usable_i ~ C(year) + acc + log_nw + NAME | found"
    tabs.append(t)
    return pd.concat(tabs, ignore_index=True), fits


def ipw_weights(d: pd.DataFrame, pairs: pd.DataFrame, fit, pop: bool, U: pd.DataFrame) -> tuple[pd.DataFrame, np.ndarray]:
    """Weights for usable pairs (2023-26): 1/p_hat(usable|x) [x design weight N_pop/n_sampled]."""
    dd = d[d.year.isin(AUDIT_YEARS)].copy()
    b = fit.params
    xb = b["Intercept"] + b["acc"] * dd.acc + b["log_nw"] * dd.log_nw + b["NAME"] * dd.NAME
    for y in AUDIT_YEARS:
        xb = xb + b.get(f"C(year)[T.{y}]", 0.0) * dd.year.eq(y)
    dd["p_usable"] = 1 / (1 + np.exp(-xb))
    assert abs(dd.p_usable.mean() - dd.usable_i.mean()) < 1e-6, "IPW fitted mean does not match"
    p = pairs[pairs.year.isin(AUDIT_YEARS)].merge(dd[["submission_id", "p_usable"]], on="submission_id",
                                                   how="left", validate="1:1").reset_index(drop=True)
    w = 1.0 / p.p_usable.to_numpy()
    if pop:
        npop = {}
        for y in AUDIT_YEARS:
            npop[(y, "accepted")] = int((U.year.eq(y) & U.ACC).sum())
            npop[(y, "rejected")] = int((U.year.eq(y) & U.REJ).sum())
        ns = dd.groupby(["year", "decision"]).size()
        w = w * np.array([npop[(y, dec)] / ns[(y, dec)] for y, dec in zip(p.year, p.decision)])
    for dec in ["accepted", "rejected"]:
        m = p.decision.eq(dec).to_numpy()
        w[m] = w[m] / w[m].mean()
    return p.drop(columns="p_usable"), w


# ------------------------------------------------------------------------------------------------
# retitling
# ------------------------------------------------------------------------------------------------
def retitling_table(P: pd.DataFrame, Wb: np.ndarray, label: str) -> tuple[pd.DataFrame, dict]:
    rows = []
    meas = ["changed_norm", "changed_raw", "case_punct_only", "changed_major"]
    groups = [(str(y), P.year.eq(y)) for y in sorted(P.year.unique())] + \
        [("all", P.year.notna()), ("2024-26", P.year.isin(POST)), ("2022-23", P.year.isin((2022, 2023)))]
    acc = P.acc.to_numpy() == 1
    for gname, gm in groups:
        gm = gm.to_numpy()
        for mcol in meas:
            x = P[mcol].to_numpy(float)
            ka, na = x[gm & acc].sum(), (gm & acc).sum()
            kr, nr = x[gm & ~acc].sum(), (gm & ~acc).sum()
            if na == 0 or nr == 0:
                continue
            d, lo, hi = newcombe(ka, na, kr, nr)
            rows.append(dict(spec=label, years=gname, measure=mcol, n_acc=int(na), k_acc=int(ka), rate_acc=ka / na,
                             rate_acc_lo=wilson(ka, na)[0], rate_acc_hi=wilson(ka, na)[1], n_rej=int(nr),
                             k_rej=int(kr), rate_rej=kr / nr, rate_rej_lo=wilson(kr, nr)[0],
                             rate_rej_hi=wilson(kr, nr)[1], diff=d, diff_lo=lo, diff_hi=hi))
    tab = pd.DataFrame(rows)
    # logit with year FE, and DiD over periods: (acc - rej) in 2024-26 minus (acc - rej) in 2022-23
    extra = {}
    res = C.logit("changed_norm ~ acc + C(year)", P)
    ot = C.or_table(res, ["acc"]).iloc[0]
    extra["logit_acc_OR"] = dict(OR=ot.OR, lo=ot.OR_lo, hi=ot.OR_hi, p=ot.p, n=int(ot.nobs))
    x = P.changed_norm.to_numpy(float)
    post = P.year.isin(POST).to_numpy()

    def did_period(W):
        out = []
        for per in [post, ~post]:
            ma, mr = per & acc, per & ~acc
            out.append((W[:, ma] @ x[ma]) / W[:, ma].sum(1) - (W[:, mr] @ x[mr]) / W[:, mr].sum(1))
        return out[0] - out[1]
    pt = did_period(np.ones((1, len(P))))[0]
    bs = did_period(Wb)
    extra["did_period_post_minus_pre"] = dict(est=float(pt), lo=float(np.quantile(bs, .025)),
                                              hi=float(np.quantile(bs, .975)),
                                              note="(acc-rej retitle rate) 2024-26 minus 2022-23")
    m_all = (P.acc == 1)
    da = (P.n_words_or - P.n_words_v1)
    extra["mean_dwords"] = dict(acc=float(da[m_all].mean()), rej=float(da[~m_all].mean()))
    return tab, extra


# ------------------------------------------------------------------------------------------------
# V7 route validation
# ------------------------------------------------------------------------------------------------
def route_validation(orig: pd.DataFrame, U: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    r = read_jsonl(ROUTE_PATH)
    if r.empty:
        return pd.DataFrame(), pd.DataFrame(), {"n": 0}
    r = r[r.error.isna()] if "error" in r else r
    r = r.drop_duplicates("submission_id", keep="last").reset_index(drop=True)
    o = orig.set_index("submission_id")
    r["A_found"] = r.submission_id.map(o.found).astype(bool)
    r["A_v1_title"] = r.submission_id.map(o.v1_title)
    r["A_v1_date"] = r.submission_id.map(o.v1_date)
    r["A_latest_title"] = r.submission_id.map(o.latest_title)
    dd = r.year.map(DEC).astype(str)
    r["B_found"] = r.found.astype(bool)
    r["B_found_strict"] = r.B_found & r.tier.isin(["A", "B"])
    r["A_usable"] = r.A_found & r.A_v1_date.notna() & (r.A_v1_date.astype(str) < dd)
    r["B_usable"] = r.B_found & r.v1_date.notna() & (r.v1_date.astype(str) < dd) & r.v1_title.notna()
    r["union_found"] = r.A_found | r.B_found
    r["union_usable"] = r.A_usable | r.B_usable
    nt = lambda s: s.map(lambda t: A.norm_title(t) if isinstance(t, str) else None)  # noqa: E731
    r["A_changed"] = np.where(r.A_usable, (nt(r.A_v1_title) != nt(r.or_title)).astype(float), np.nan)
    r["B_changed"] = np.where(r.B_usable, (nt(r.v1_title) != nt(r.or_title)).astype(float), np.nan)
    r["B_changed_strict"] = np.where(r.B_usable & r.B_found_strict, r.B_changed, np.nan)
    r["A_latest_diff"] = np.where(r.A_found, (nt(r.A_latest_title) != nt(r.or_title)).astype(float), np.nan)
    r["B_latest_diff"] = np.where(r.B_found, (nt(r.latest_title) != nt(r.or_title)).astype(float), np.nan)
    r["B_only"] = r.B_found & ~r.A_found
    r["A_only"] = r.A_found & ~r.B_found
    r["acc"] = r.decision.eq("accepted").astype(int)
    rows = []
    for dec, g in list(r.groupby("decision")) + [("all", r)]:
        n = len(g)
        row = dict(decision=dec, n=n)
        for col in ["A_found", "B_found", "B_found_strict", "union_found", "A_usable", "B_usable", "union_usable"]:
            k = int(g[col].sum())
            lo, hi = wilson(k, n)
            row.update({col: k, f"{col}_rate": k / n, f"{col}_lo": lo, f"{col}_hi": hi})
        b, c = int((g.A_found & ~g.B_found).sum()), int((~g.A_found & g.B_found).sum())
        row.update(both=int((g.A_found & g.B_found).sum()), A_only=b, B_only=c,
                   neither=int((~g.A_found & ~g.B_found).sum()),
                   mcnemar_p=float(stats.binomtest(min(b, c), b + c, 0.5).pvalue) if b + c else 1.0)
        both = g[g.A_found & g.B_found]
        row["same_id_both"] = int((both.arxiv_id == both.orig_arxiv_id).sum())
        row["same_id_rate"] = row["same_id_both"] / len(both) if len(both) else np.nan
        row["diff_id_tiers"] = json.dumps(both[both.arxiv_id != both.orig_arxiv_id].tier.value_counts().to_dict())
        row["tier_counts"] = json.dumps(g[g.B_found].tier.value_counts().to_dict())
        for col in ["A_changed", "B_changed", "B_changed_strict", "A_latest_diff", "B_latest_diff"]:
            x = g[col].dropna()
            row[f"{col}_n"], row[f"{col}_k"] = len(x), int(x.sum())
            row[f"{col}_rate"] = x.mean() if len(x) else np.nan
            row[f"{col}_lo"], row[f"{col}_hi"] = wilson(x.sum(), len(x))
        x = g[g.B_only].B_changed.dropna()
        row["Bonly_changed_n"], row["Bonly_changed_k"] = len(x), int(x.sum())
        x = g[g.A_found & g.B_usable].B_changed.dropna()
        row["Bfound_by_A_changed_rate"] = x.mean() if len(x) else np.nan
        rows.append(row)
    tab = pd.DataFrame(rows)
    # gap in found rates (acc - rej) by route, and its difference (paired bootstrap by paper, strata = decision)
    rng = np.random.default_rng(SEED + 7)
    acc = r.acc.to_numpy() == 1
    FA, FB = r.A_found.to_numpy(float), r.B_found.to_numpy(float)
    idx_a, idx_r = np.where(acc)[0], np.where(~acc)[0]

    def gaps(ia, ir):
        ga = FA[ia].mean() - FA[ir].mean()
        gb = FB[ia].mean() - FB[ir].mean()
        return ga, gb, gb - ga
    est = gaps(idx_a, idx_r)
    bs = np.array([gaps(rng.choice(idx_a, len(idx_a)), rng.choice(idx_r, len(idx_r))) for _ in range(N_BOOT)])
    lo, hi = np.quantile(bs, .025, axis=0), np.quantile(bs, .975, axis=0)
    summary = dict(n=int(len(r)), n_acc=int(acc.sum()), n_rej=int((~acc).sum()),
                   gap_A=dict(est=est[0], lo=lo[0], hi=hi[0]), gap_B=dict(est=est[1], lo=lo[1], hi=hi[1]),
                   gap_B_minus_A=dict(est=est[2], lo=lo[2], hi=hi[2]))
    # retitle-rate difference between routes on the same papers (usable by both): paired
    both_u = r[r.A_usable & r.B_usable & (r.arxiv_id == r.orig_arxiv_id)]
    summary["n_usable_both_same_id"] = int(len(both_u))
    summary["changed_A_vs_B_same_papers"] = dict(A=float(both_u.A_changed.mean()) if len(both_u) else None,
                                                  B=float(both_u.B_changed.mean()) if len(both_u) else None)
    return tab, r, summary


# ------------------------------------------------------------------------------------------------
# figures
# ------------------------------------------------------------------------------------------------
def fig_findability(fr: pd.DataFrame, rt: pd.DataFrame):
    import matplotlib.pyplot as plt  # noqa: F401
    fig, axes = C.new_fig("double", 2.5, ncols=2)
    f = fr[(fr.source == "original") & fr.year.isin(AUDIT_YEARS)].copy()
    f["year"] = f.year.astype(int)
    plot_rows = []
    for i, (dec, lab) in enumerate([("accepted", "Accepted"), ("rejected", "Rejected")]):
        g = f[f.decision == dec].sort_values("year")
        off = -0.06 if i == 0 else 0.06
        ax = axes[0]
        ax.errorbar(g.year + off, g.found_rate, yerr=[g.found_rate - g.found_lo, g.found_hi - g.found_rate],
                    color=C.color(i), marker="o", ms=5, lw=2, capsize=0, elinewidth=1.0, label=f"{lab}: found")
        ax.plot(g.year + off, g.usable_rate, color=C.color(i), marker="s", ms=5, lw=1.2, ls="--",
                label=f"{lab}: usable pre-decision pair")
        for _, rr in g.iterrows():
            plot_rows.append(dict(panel="a", series=f"{dec}_found", year=rr.year, value=rr.found_rate,
                                  lo=rr.found_lo, hi=rr.found_hi, n=rr.n))
            plot_rows.append(dict(panel="a", series=f"{dec}_usable", year=rr.year, value=rr.usable_rate,
                                  lo=rr.usable_lo, hi=rr.usable_hi, n=rr.n))
        h = rt[(rt.spec == "primary") & (rt.measure == "changed_norm") & rt.years.isin([str(y) for y in AUDIT_YEARS])]
        h = h.assign(year=h.years.astype(int)).sort_values("year")
        col = "acc" if dec == "accepted" else "rej"
        ax = axes[1]
        ax.errorbar(h.year + off, h[f"rate_{col}"], yerr=[h[f"rate_{col}"] - h[f"rate_{col}_lo"],
                                                        h[f"rate_{col}_hi"] - h[f"rate_{col}"]],
                    color=C.color(i), marker="o", ms=5, lw=2, capsize=0, elinewidth=1.0, label=lab)
        for _, rr in h.iterrows():
            plot_rows.append(dict(panel="b", series=f"{dec}_retitled", year=rr.year, value=rr[f"rate_{col}"],
                                  lo=rr[f"rate_{col}_lo"], hi=rr[f"rate_{col}_hi"], n=rr[f"n_{col}"]))
    axes[0].set_ylim(0, 1.02)
    axes[0].set_ylabel("Share of audited papers")
    axes[0].set_title("a  arXiv findability (title route)", loc="left")
    axes[1].set_ylim(0, None)
    axes[1].set_ylabel("Share of usable pairs retitled")
    axes[1].set_title("b  v1 title differs from stored title", loc="left")
    for ax in axes:
        ax.set_xticks(list(AUDIT_YEARS))
        ax.set_xlabel("ICLR year")
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=4, fontsize=7, bbox_to_anchor=(0.5, 0.0))
    fig.tight_layout(rect=(0, 0.09, 1, 1))
    C.save_fig(fig, "fig_S1_findability_retitling", OUTDIR, data=pd.DataFrame(plot_rows))


def fig_tipping(tp: pd.DataFrame):
    keys = [k for k, *_ in TITLE_FEATS if k in set(tp.feature)] + [k for k, *_ in ABS_FEATS if k in set(tp.feature)]
    t = tp.set_index("feature").loc[keys].reset_index()
    n = len(t)
    fig, axes = C.new_fig("double", 0.17 * n + 1.2, ncols=2, sharey=True)
    ypos = np.arange(n)[::-1]
    ax = axes[0]
    for yv, (_, r) in zip(ypos, t.iterrows()):
        c = C.color(0) if r.auditable else C.GREY
        ax.plot([r.did_lo_pp, r.did_hi_pp], [yv, yv], color=c, lw=1.8, solid_capstyle="butt")
        ax.plot([r.did_pp], [yv], "o", color=c, ms=5)
        ax.plot([r.tip_dec_pp], [yv], "D", color=C.color(1), ms=5, mec="white", mew=0.5)
    ax.axvline(0, color=C.GREY, lw=0.8, ls="--", zorder=0)
    ax.set_yticks(ypos, [("" if r.auditable else "† ") + r.label for _, r in t.iterrows()])
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("Percentage points")
    ax.set_title("a  Audit net-flip DiD (95% CI) vs tipping point", loc="left")
    ax.plot([], [], color=C.color(0), lw=1.8, marker="o", ms=5, label="Net-flip DiD (95% CI), auditable")
    ax.plot([], [], color=C.GREY, lw=1.8, marker="o", ms=5, label="Net-flip DiD (95% CI), † unauditable")
    ax.plot([], [], "D", color=C.color(1), ms=5, label="Tipping point D* (G_dec = 1)")
    lim = np.nanmax(np.abs(np.r_[t.did_lo_pp, t.did_hi_pp, t.tip_dec_pp])) * 1.08
    ax.set_xlim(-lim, lim)
    ax = axes[1]
    for yv, (_, r) in zip(ypos, t.iterrows()):
        c = C.color(0) if r.auditable else C.GREY
        if np.isfinite(r.G_dec_audit_lo) and np.isfinite(r.G_dec_audit_hi):
            ax.plot([r.G_dec_audit_lo, r.G_dec_audit_hi], [yv, yv], color=c, lw=1.8, solid_capstyle="butt")
        ax.plot([r.G_dec_obs], [yv], "o", color=C.TEXT, ms=4.5)
    ax.axvline(1, color=C.GREY, lw=0.8, ls="--", zorder=0)
    ax.set_xlim(0, 2.5)
    ax.set_xlabel("G_dec = P(f | accepted) / P(f | reviewed)")
    ax.set_title("b  Observed G_dec and audit-implied interval", loc="left")
    ax.plot([], [], "o", color=C.TEXT, ms=4.5, label="Observed G_dec (stored titles)")
    ax.plot([], [], color=C.GREY, lw=1.8, label="Submission-stage G_dec over the audit CI")
    ax.grid(axis="y", visible=False)
    h0, l0 = axes[0].get_legend_handles_labels()
    h1, l1 = axes[1].get_legend_handles_labels()
    fig.legend(h0 + h1, l0 + l1, loc="lower center", ncol=3, fontsize=7, bbox_to_anchor=(0.5, 0.0))
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    C.save_fig(fig, "fig_S2_tipping_points", OUTDIR,
               data=t[["feature", "label", "auditable", "did_pp", "did_lo_pp", "did_hi_pp", "tip_dec_pp",
                       "G_dec_obs", "G_dec_audit_lo", "G_dec_audit_hi", "G_dec_identified"]])


def fig_route(rv: pd.DataFrame):
    if rv.empty:
        return
    fig, axes = C.new_fig("double", 2.3, ncols=2)
    rows = []
    g = rv[rv.decision.isin(["accepted", "rejected"])].set_index("decision")
    routes = [("A_found", "Title route (A)"), ("B_found", "Surname + abstract (B)"), ("union_found", "A or B")]
    for i, dec in enumerate(["accepted", "rejected"]):
        if dec not in g.index:
            continue
        r = g.loc[dec]
        xs = np.arange(len(routes)) + (-0.1 if i == 0 else 0.1)
        v = [r[f"{c}_rate"] for c, _ in routes]
        lo = [r[f"{c}_rate"] - r[f"{c}_lo"] for c, _ in routes]
        hi = [r[f"{c}_hi"] - r[f"{c}_rate"] for c, _ in routes]
        axes[0].errorbar(xs, v, yerr=[lo, hi], color=C.color(i), marker="o", ms=5, lw=0, elinewidth=1.4,
                         label=dec.capitalize() + f" (n = {int(r.n)})")
        for (c, lab), x_, vv in zip(routes, xs, v):
            rows.append(dict(panel="a", decision=dec, measure=c, value=vv, lo=r[f"{c}_lo"], hi=r[f"{c}_hi"], n=r.n))
        ms = [("A_changed", "v1 vs stored (A)"), ("B_changed", "v1 vs stored (B)"),
              ("A_latest_diff", "latest vs stored (A)"), ("B_latest_diff", "latest vs stored (B)")]
        xs2 = np.arange(len(ms)) + (-0.1 if i == 0 else 0.1)
        v2 = [r[f"{c}_rate"] for c, _ in ms]
        lo2 = [r[f"{c}_rate"] - r[f"{c}_lo"] for c, _ in ms]
        hi2 = [r[f"{c}_hi"] - r[f"{c}_rate"] for c, _ in ms]
        axes[1].errorbar(xs2, v2, yerr=[lo2, hi2], color=C.color(i), marker="o", ms=5, lw=0, elinewidth=1.4,
                         label=dec.capitalize())
        for (c, lab), vv in zip(ms, v2):
            rows.append(dict(panel="b", decision=dec, measure=c, value=vv, lo=r[f"{c}_lo"], hi=r[f"{c}_hi"],
                             n=r[f"{c}_n"]))
    axes[0].set_xticks(range(len(routes)), [lab for _, lab in routes])
    axes[0].set_ylim(0, 1.02)
    axes[0].set_ylabel("Found on arXiv")
    axes[0].set_title("a  Found rate by retrieval route", loc="left")
    axes[1].set_xticks(range(4), ["v1\nroute A", "v1\nroute B", "latest\nroute A", "latest\nroute B"])
    axes[1].set_xlabel("arXiv title compared with the stored title")
    axes[1].set_ylim(0, None)
    axes[1].set_ylabel("Share with a different title")
    axes[1].set_title("b  Title stability by route", loc="left")
    for ax in axes:
        ax.grid(axis="x", visible=False)
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=2, fontsize=7, bbox_to_anchor=(0.5, 0.0))
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    C.save_fig(fig, "fig_S3_route_validation", OUTDIR, data=pd.DataFrame(rows))


def fig_flip_rates(fl: pd.DataFrame):
    """Drop rate given v1-present, accepted vs rejected, for auditable features (feature-present denominators)."""
    t = fl[(fl.spec == "primary")].copy()
    t = t[t.feature.isin([k for k, *_ in TITLE_FEATS])]
    t = t.iloc[::-1].reset_index(drop=True)
    n = len(t)
    fig, ax = C.new_fig("single", 0.17 * n + 0.8)
    ypos = np.arange(n)
    rows = []
    for i, (dec, g) in enumerate([("accepted", "acc"), ("rejected", "rej")]):
        off = 0.15 if i == 0 else -0.15
        for yv, (_, r) in zip(ypos, t.iterrows()):
            if not np.isfinite(r[f"drop_rate_{g}"]):
                continue
            ax.plot([r[f"drop_rate_lo_{g}"], r[f"drop_rate_hi_{g}"]], [yv + off] * 2, color=C.color(i), lw=1.4)
            ax.plot([r[f"drop_rate_{g}"]], [yv + off], "o", color=C.color(i), ms=4.5)
            rows.append(dict(feature=r.feature, decision=dec, drop_rate=r[f"drop_rate_{g}"],
                             lo=r[f"drop_rate_lo_{g}"], hi=r[f"drop_rate_hi_{g}"], v1_present=r[f"v1_present_{g}"],
                             drops=r[f"drops_{g}"]))
        ax.plot([], [], "o-", color=C.color(i), ms=4.5, lw=1.4, label=dec.capitalize())
    ax.set_yticks(ypos, [f"{r.label} ({r.v1_present_acc}/{r.v1_present_rej})" for _, r in t.iterrows()])
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", visible=False)
    ax.set_xlim(0, 1)
    ax.set_xlabel("Drop rate: P(absent in stored | present in v1)")
    ax.set_title("Feature drops by decision (v1-present n: acc/rej)", loc="left", fontsize=8.5)
    ax.legend(loc="lower right", fontsize=7)
    fig.tight_layout()
    C.save_fig(fig, "fig_S4_drop_rates", OUTDIR, data=pd.DataFrame(rows))



# ------------------------------------------------------------------------------------------------
# hypotheses / verdicts for results.json
# ------------------------------------------------------------------------------------------------
def _fmt(x, d=2):
    return "nan" if x is None or not np.isfinite(x) else f"{x:.{d}f}"


def _v7b_verdict(g, bo_n: int) -> str:
    a, b = g.loc["all", "A_changed_rate"], g.loc["all", "B_changed_rate"]
    if bo_n < 5:
        return "not_testable"
    bonly = g.loc["all", "Bonly_changed_k"] / bo_n
    if abs(b - a) >= 0.05:
        return "not_supported"
    return "supported" if bonly - a <= 0.20 else "partially_supported"


def compose_results(core: dict, tp, flips, fm, fr, rt, rt_extra, idt, rv, rv_sum, gate, tpa, fla, P) -> dict:
    T = tp.set_index("feature")
    Fl = flips.set_index("feature")
    hyps, rob = [], []
    nm, nf = T.loc["NAME"], Fl.loc["NAME"]
    hyps.append(dict(
        id="SB1", statement="PLAN D4 decision-stage bound: the NAME acceptance association (G_dec, 2024-26) is not "
        "identified by the current audit, because its tipping point (pilot ~1.8 pp) lies inside the audit 95% CI of "
        "the net-flip DiD (pilot +2.1 pp, se 2.4).",
        verdict="supported" if not nm.G_dec_identified else "not_supported",
        estimate=(f"net-flip DiD {_fmt(100 * nf.did)} pp, 95% CI [{_fmt(100 * nf.did_lo)}, {_fmt(100 * nf.did_hi)}] "
                  f"(pseudo-flip Wald; plain Wald se {_fmt(100 * nf.did_se_wald)} pp, bootstrap "
                  f"[{_fmt(100 * nf.did_lo_boot)}, {_fmt(100 * nf.did_hi_boot)}]); tipping point D*_dec "
                  f"{_fmt(nm.tip_dec_pp)} pp; observed G_dec {_fmt(nm.G_dec_obs, 3)} [{_fmt(nm.G_dec_lo95, 3)}, "
                  f"{_fmt(nm.G_dec_hi95, 3)}]; audit-implied submission-stage G_dec [{_fmt(nm.G_dec_audit_lo, 3)}, "
                  f"{_fmt(nm.G_dec_audit_hi, 3)}]; n = {int(nf.n_acc)} accepted / {int(nf.n_rej)} rejected pairs "
                  f"(v1-present {int(nf.v1_present_acc)}/{int(nf.v1_present_rej)})"),
        notes="Tipping point regenerated at 2.9 pp (pilot 1.8 pp); the conclusion (not identified) is unchanged "
              "under plain Wald, bootstrap, 2024-26-only, IPW and union-route audits (T4_2_identification_by_spec.csv)."))
    n_pass = int(sum(bool(T.loc[k].claim_dec_passes_gate) for k in T.index))
    n_aud = int(T.auditable.sum())
    hyps.append(dict(
        id="SB2", statement="Gate (PLAN section 4): at least one title feature's acceptance association (G_dec != 1, "
        "2024-26) survives the camera-ready audit (auditable, tipping point beyond the audit CI, observed G_dec CI "
        "excludes 1).",
        verdict="supported" if n_pass > 0 else "not_supported",
        estimate=f"{n_pass} of {len(T)} title features pass ({n_aud} auditable); identified under any spec: "
                 f"{sorted(set(idt[idt.G_dec_identified].feature)) or 'none'}",
        notes="Acceptance-margin claims about title features therefore cannot enter the headline; diachronic and "
              "NA-pool results do not depend on the audit."))
    rare = ["using", "R24", "R26", "slot_llm", "title_typo"]
    hyps.append(dict(
        id="SB3", statement="V7: rare lexical title features ('using', R24, R26, LLM slot words, title typography) "
        "are unauditable (fewer than 10 v1-present titles in an arm).",
        verdict="supported" if all(not Fl.loc[k].auditable for k in rare) else "partially_supported",
        estimate="; ".join(f"{k}: v1-present {int(Fl.loc[k].v1_present_acc)} acc / {int(Fl.loc[k].v1_present_rej)} rej"
                           for k in rare),
        notes="The PLAN example ('using' in only 4 accepted v1 titles) is regenerated with the v2 detector."))
    fa = fm[(fm.term == "acc") & (fm.formula == "found_i ~ C(year) + acc + log_nw + NAME")]
    fa = fa[fa.get("sample", pd.Series("original", index=fa.index)).fillna("original") == "original"].iloc[0]
    fn = fm[(fm.term == "NAME") & (fm.formula == "found_i ~ C(year) + acc + log_nw + NAME")].iloc[0]
    fu = fm[(fm.term == "acc") & (fm.formula == "usable_i ~ C(year) + acc + log_nw + NAME")].iloc[0]
    fpre = fm[(fm.term == "acc") & (fm.outcome == "usable_given_found")].iloc[0]
    fra = fr[(fr.source == "original") & (fr.year.astype(str) == "all")].set_index("decision")
    ipw = idt[(idt.spec == "ipw_find_pop") & (idt.feature == "NAME")].iloc[0]
    hyps.append(dict(
        id="SB4", statement="Differential findability: accepted papers are found on arXiv more often than rejected "
        "papers; reweighting usable pairs by 1/P(usable | year, decision, title length, NAME) leaves the NAME bound "
        "unchanged.",
        verdict="supported" if (fa.OR_lo > 1 and not bool(ipw.G_dec_identified)) else "partially_supported",
        estimate=(f"found {_fmt(100 * fra.loc['accepted', 'found_rate'], 1)}% vs "
                  f"{_fmt(100 * fra.loc['rejected', 'found_rate'], 1)}%; logit OR(accepted) {_fmt(fa.OR)} "
                  f"[{_fmt(fa.OR_lo)}, {_fmt(fa.OR_hi)}], OR(NAME) {_fmt(fn.OR)} [{_fmt(fn.OR_lo)}, {_fmt(fn.OR_hi)}]; "
                  f"usable pair OR(accepted) {_fmt(fu.OR)} [{_fmt(fu.OR_lo)}, {_fmt(fu.OR_hi)}]; pre-decision v1 given "
                  f"found OR(accepted) {_fmt(fpre.OR)} [{_fmt(fpre.OR_lo)}, {_fmt(fpre.OR_hi)}]; IPW x population "
                  f"NAME DiD {_fmt(ipw.did_pp)} pp [{_fmt(ipw.did_lo_pp)}, {_fmt(ipw.did_hi_pp)}]"),
        notes="Findability differs by decision, not by NAME or title length; v1 timing given found does not differ."))
    r_all = rt[(rt.spec == "primary") & (rt.years == "all") & (rt.measure == "changed_norm")].iloc[0]
    r_post = rt[(rt.spec == "primary") & (rt.years == "2024-26") & (rt.measure == "changed_norm")].iloc[0]
    hyps.append(dict(
        id="SB5", statement="Camera-ready retitling: accepted papers' stored titles differ from the pre-decision "
        "arXiv v1 more often than rejected papers' (descriptive; no pre-registered threshold).",
        verdict="supported" if r_all.diff_lo > 0 else "not_supported",
        estimate=(f"retitled (word-level) {_fmt(100 * r_all.rate_acc, 1)}% acc (n={int(r_all.n_acc)}) vs "
                  f"{_fmt(100 * r_all.rate_rej, 1)}% rej (n={int(r_all.n_rej)}): diff {_fmt(100 * r_all["diff"], 1)} pp "
                  f"[{_fmt(100 * r_all.diff_lo, 1)}, {_fmt(100 * r_all.diff_hi, 1)}]; 2024-26 "
                  f"{_fmt(100 * r_post["diff"], 1)} pp [{_fmt(100 * r_post.diff_lo, 1)}, {_fmt(100 * r_post.diff_hi, 1)}]; "
                  f"logit OR(acc | year FE) {_fmt(rt_extra['logit_acc_OR']['OR'])} "
                  f"[{_fmt(rt_extra['logit_acc_OR']['lo'])}, {_fmt(rt_extra['logit_acc_OR']['hi'])}]"),
        notes="Rejected papers retitle too (arXiv vs OpenReview wording, rebuttal edits); only the excess is "
              "camera-ready editing."))
    if not rv.empty:
        g = rv.set_index("decision")
        hyps.append(dict(
            id="V7a", statement="Route validation (findability): a title-free route (first-author surname + "
            "distinctive abstract words) finds papers at a similar rate, so the accepted-rejected findability gap is "
            "not an artefact of title search.",
            verdict="supported" if (rv_sum["gap_B"]["lo"] > 0 and rv_sum["gap_B_minus_A"]["lo"] < 0 <
                                    rv_sum["gap_B_minus_A"]["hi"]) else "partially_supported",
            estimate=(f"partial n = {rv_sum['n']} of 300 (acc {rv_sum['n_acc']}, rej {rv_sum['n_rej']}); found A/B: "
                      f"acc {_fmt(g.loc['accepted', 'A_found_rate'], 3)}/{_fmt(g.loc['accepted', 'B_found_rate'], 3)}, "
                      f"rej {_fmt(g.loc['rejected', 'A_found_rate'], 3)}/{_fmt(g.loc['rejected', 'B_found_rate'], 3)}; "
                      f"gap A {_fmt(rv_sum['gap_A']['est'], 3)}, gap B {_fmt(rv_sum['gap_B']['est'], 3)}, B - A "
                      f"{_fmt(rv_sum['gap_B_minus_A']['est'], 3)} [{_fmt(rv_sum['gap_B_minus_A']['lo'], 3)}, "
                      f"{_fmt(rv_sum['gap_B_minus_A']['hi'], 3)}]; arXiv-id agreement when both found "
                      f"{_fmt(g.loc['all', 'same_id_rate'], 3)}"),
            notes="Paired on the same random subsample of the original audit; McNemar p per decision in "
                  "route_validation.csv."))
        bo_n = int(g.loc["all", "Bonly_changed_n"])
        hyps.append(dict(
            id="V7b", statement="Route validation (title stability): the title route does not select on title "
            "stability; retitling among route-B pairs matches route-A pairs, and adding papers only route B finds "
            "leaves the flip DiDs unchanged.",
            verdict=_v7b_verdict(g, bo_n),
            estimate=(f"retitled v1 vs stored: route A {_fmt(g.loc['all', 'A_changed_rate'], 3)} "
                      f"(n={int(g.loc['all', 'A_changed_n'])}), route B {_fmt(g.loc['all', 'B_changed_rate'], 3)} "
                      f"(n={int(g.loc['all', 'B_changed_n'])}); B-only usable pairs {bo_n} "
                      f"({int(g.loc['all', 'Bonly_changed_k'])} retitled); latest arXiv title differs from stored: A "
                      f"{_fmt(g.loc['all', 'A_latest_diff_rate'], 3)}, B {_fmt(g.loc['all', 'B_latest_diff_rate'], 3)}"),
            notes="Verdict rule (descriptive, set after the pilot design): supported if route-level retitling rates "
                  "differ by < 5 pp and papers found only by route B are not retitled > 20 pp more often than route-A "
                  "pairs; partially supported if only the first holds; not testable if fewer than 5 B-only pairs. "
                  "See the union_route spec for the effect on the flip DiDs."))
    gt = gate.set_index("claim")
    k1 = "H4a NAME G_total within [0.90, 1.11] (2024-26 pooled)"
    k2 = "H4a NAME G_dec within [0.90, 1.11] (2024-26 pooled)"
    hyps.append(dict(
        id="G1", statement="Gate for D4-H4a: NAME neutrality (pooled 2024-26 G_total inside [0.90, 1.11]) survives "
        "camera-ready uncertainty (editing-corrected 90% CI combining universe bootstrap and audit).",
        verdict=("supported" if bool(gt.loc[k1, "passes"]) else
                 "partially_supported" if any(bool(gt.loc[c, "passes"]) for c in gt.index
                                              if c.startswith("H4a NAME G_total") and "enlarged" in c)
                 else "not_supported"),
        estimate=(f"G_total observed {_fmt(gt.loc[k1, 'observed'], 3)} 90% CI {gt.loc[k1, 'obs_ci90']}; audit-implied "
                  f"{gt.loc[k1, 'audit_interval']}; corrected 90% CI {gt.loc[k1, 'corrected_ci90']}. G_dec: observed "
                  f"{_fmt(gt.loc[k2, 'observed'], 3)}, corrected 90% CI {gt.loc[k2, 'corrected_ci90']} "
                  f"({'inside' if bool(gt.loc[k2, 'passes']) else 'outside'} the margins)"),
        notes="G_total is more sensitive to editing than G_dec because accepted papers are a smaller share of s0 "
              "(a0) than of s2 (a2). Enlarged-audit gate: " + "; ".join(
                  f"{c.split('(')[1].rstrip(')')}: corrected 90% CI {gt.loc[c, 'corrected_ci90']}, passes="
                  f"{bool(gt.loc[c, 'passes'])}" for c in gt.index if c.startswith("H4a NAME G_total") and "enlarged" in c)))
    lt = gate[gate.feature.isin(["L_title"])].iloc[0]
    hyps.append(dict(
        id="G2", statement="Gate for D4-H4b: depletion of title LLM markers (L-title G_total < 1, 2024-26) "
        "survives the audit.",
        verdict="supported" if bool(lt.passes) else "not_supported",
        estimate=f"G_total {_fmt(lt.observed, 3)}, 90% CI {lt.obs_ci90}; audit-implied {lt.audit_interval}; corrected "
                 f"90% CI {lt.corrected_ci90}; L-title auditable={bool(Fl.loc['L_title'].auditable)}",
        notes="G_desk x G_exit uses submission-stage text and needs no audit (D4)."))
    if len(tpa):
        Ta = tpa.set_index("feature")
        Fa = fla.set_index("feature")
        la = Ta.loc["L_abs_words"]
        hyps.append(dict(
            id="G3", statement="Abstract audit (extension): the accepted/all depletion of arXiv-measurable abstract "
            "LLM markers (F24 or F26 words; G_total < 1, 2024-26) survives the camera-ready audit. Em dash and other "
            "typography are unauditable through arXiv (TeX dashes).",
            verdict="supported" if bool(la.G_total_identified) else "not_supported",
            estimate="; ".join(
                f"{k}: DiD {_fmt(100 * Fa.loc[k].did)} pp [{_fmt(100 * Fa.loc[k].did_lo)}, {_fmt(100 * Fa.loc[k].did_hi)}],"
                f" tip_total {_fmt(Ta.loc[k].tip_total_pp)} pp, G_total {_fmt(Ta.loc[k].G_total_obs, 3)}, identified="
                f"{bool(Ta.loc[k].G_total_identified)}" for k in Ta.index),
            notes=f"arXiv v1 abstract vs stored abstract; n = {int(Fa.iloc[0].n_acc)} acc / {int(Fa.iloc[0].n_rej)} rej."))
        f24 = Fa.loc["F24"]
        if f24.did_lo > 0:
            v4 = "supported"
        elif f24.did_hi < 0:
            v4 = "falsified"
        elif f24.did >= 0:
            v4 = "partially_supported"
        else:
            v4 = "not_supported"
        hyps.append(dict(
            id="G4", statement="D4-H4c direction assumption: camera-ready polishing does not lower accepted papers' "
            "abstract LLM-marker (RARE21/F24) rates relative to rejected papers (net-flip DiD >= 0), so the "
            "accepted-only understatement of the Kobak bound is conservative.",
            verdict=v4,
            estimate=(f"F24 net flips: accepted {_fmt(100 * f24.net_acc)} pp ({int(f24.adds_acc)} adds / "
                      f"{int(f24.drops_acc)} drops, v1-present {int(f24.v1_present_acc)}), rejected "
                      f"{_fmt(100 * f24.net_rej)} pp ({int(f24.adds_rej)} / {int(f24.drops_rej)}, v1-present "
                      f"{int(f24.v1_present_rej)}); DiD {_fmt(100 * f24.did)} pp [{_fmt(100 * f24.did_lo)}, "
                      f"{_fmt(100 * f24.did_hi)}]"),
            notes="supported = CI above 0; partially = point >= 0, CI includes 0; not_supported = point < 0, CI "
                  "includes 0; falsified = CI below 0. Pairs from all audit years (2022-26)."))
    for sname in sorted(set(idt.spec)):
        t = idt[(idt.spec == sname) & (idt.feature == "NAME")].iloc[0]
        rob.append(dict(check=f"NAME bound under audit spec '{sname}'",
                        result=f"DiD {_fmt(t.did_pp)} pp [{_fmt(t.did_lo_pp)}, {_fmt(t.did_hi_pp)}], tip "
                               f"{_fmt(t.tip_dec_pp)} pp, identified={bool(t.G_dec_identified)}, n={int(t.n_acc)}/"
                               f"{int(t.n_rej)}"))
    rob.append(dict(check="CI type for the net-flip DiD (NAME)",
                    result=f"pseudo-flip Wald [{_fmt(100 * nf.did_lo)}, {_fmt(100 * nf.did_hi)}]; plain Wald "
                           f"[{_fmt(100 * nf.did_lo_wald)}, {_fmt(100 * nf.did_hi_wald)}]; bootstrap "
                           f"[{_fmt(100 * nf.did_lo_boot)}, {_fmt(100 * nf.did_hi_boot)}]; identified under any: "
                           f"{bool(nm.G_dec_identified or nm.G_dec_identified_wald or nm.G_dec_identified_boot)}"))
    rob.append(dict(check="Auditability rule (D4 interim rule vs this module)",
                    result=f"this rule: {sorted(Fl[Fl.auditable].index)}; D4 rule: {sorted(Fl[Fl.auditable_d4rule].index)}"))
    core["hypotheses"] = hyps
    core["robustness"] = rob
    return core

# ------------------------------------------------------------------------------------------------
def main(enlarge_n: int | None = None):
    """enlarge_n: use only the first N lines of the (append-only) enlargement cache, for a reproducible freeze."""
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
    fv = C.load_features(["submission_id", "n_words", "name_primary"])
    orig = read_jsonl(ORIG_PATH)
    log(f"original audit: {len(orig)} records; by year x decision {orig.groupby(['year', 'decision']).size().to_dict()}")

    # ---------------- findability
    d = audit_frame(orig, fv)
    fr = found_rate_table(d, "original")
    fm, fits = findability_models(d)
    log("found rates (original):\n" + fr[fr.year.isin(["all", "2024-26"])][
        ["year", "decision", "n", "found_rate", "found_lo", "found_hi", "usable_rate", "pre_share_found"]].round(3)
        .to_string())
    log("findability logits (2023-26):\n" + fm[fm.term.isin(["acc", "log_nw", "NAME"])][
        ["outcome", "formula", "term", "OR", "OR_lo", "OR_hi", "p", "nobs"]].round(4).to_string())

    # ---------------- pairs
    P = build_pairs(orig, U, "original")
    log(f"usable pre-decision pairs: {len(P)} ({P.decision.value_counts().to_dict()}); by year "
        f"{P.groupby(['year', 'decision']).size().to_dict()}")
    keys_t = [k for k, *_ in TITLE_FEATS]
    Wb = boot_matrix(P)

    # ---------------- retitling
    rt, rt_extra = retitling_table(P, Wb, "primary")
    log("retitling (primary):\n" + rt[rt.years.isin(["all", "2024-26", "2022-23"])][
        ["years", "measure", "n_acc", "rate_acc", "n_rej", "rate_rej", "diff", "diff_lo", "diff_hi"]].round(3)
        .to_string())
    log(f"retitling extras: {json.dumps(jsonable(rt_extra))}")

    # ---------------- flip tables (specs)
    flips, did_b = flip_table(P, keys_t, "primary", Wb=Wb)
    specs = {"primary": (flips, did_b)}
    Ppost = P[P.year.isin(POST)].reset_index(drop=True)
    specs["post_2024_26"] = flip_table(Ppost, keys_t, "post_2024_26")
    fit_u = fits["usable_i ~ C(year) + acc + log_nw + NAME"]
    Pi, wi = ipw_weights(d, P, fit_u, pop=False, U=U)
    specs["ipw_find"] = flip_table(Pi, keys_t, "ipw_find", w=wi)
    Pp, wp = ipw_weights(d, P, fit_u, pop=True, U=U)
    specs["ipw_find_pop"] = flip_table(Pp, keys_t, "ipw_find_pop", w=wp)
    multi = [multiclass_table(P, "primary")]

    # enlarged audit (partial)
    enl = read_jsonl(ENLARGE_PATH)
    if enlarge_n is not None and not enl.empty:
        enl = enl.head(enlarge_n)
    enl_info = {"n_records": 0, "enlarge_n_cap": enlarge_n}
    if not enl.empty:
        enl = enl[enl.error.isna()] if "error" in enl else enl
        enl = enl.drop_duplicates("submission_id", keep="last")
        de = audit_frame(enl, fv)
        fre = found_rate_table(de, "enlarge")
        fr = pd.concat([fr, fre, found_rate_table(pd.concat([d, de], ignore_index=True), "original+enlarge")],
                       ignore_index=True)
        Pe = build_pairs(enl, U, "enlarge")
        enl_info = dict(n_records=int(len(enl)), enlarge_n_cap=enlarge_n, n_found=int(de.found.sum()), n_usable=int(len(Pe)),
                        by_cell=enl.groupby(["year", "decision"]).size().to_dict())
        if len(Pe):
            Pall = pd.concat([P, Pe], ignore_index=True)
            specs["enlarged"] = flip_table(Pall, keys_t, "enlarged")
            enl_info["n_pairs_pooled"] = int(len(Pall))
            rt_e, _ = retitling_table(Pall, boot_matrix(Pall), "enlarged")
            rt = pd.concat([rt, rt_e], ignore_index=True)
            multi.append(multiclass_table(Pall, "enlarged"))
            fm_e, fits_e = findability_models(pd.concat([d, de], ignore_index=True))
            fm_e["sample"] = "original+enlarge"
            fm["sample"] = "original"
            fm = pd.concat([fm, fm_e], ignore_index=True)
    log(f"enlargement: {json.dumps(jsonable(enl_info))}")

    # ---------------- V7 route validation
    rv, rpairs, rv_sum = route_validation(orig, U)
    if not rv.empty:
        log("route validation:\n" + rv[["decision", "n", "A_found_rate", "B_found_rate", "B_found_strict_rate",
                                        "union_found_rate", "A_only", "B_only", "mcnemar_p", "same_id_rate",
                                        "A_changed_rate", "B_changed_rate", "A_latest_diff_rate",
                                        "B_latest_diff_rate"]].round(3).to_string())
        log(f"route summary: {json.dumps(jsonable(rv_sum))}")
        # union-route pairs: original usable pairs + route-B-only usable pairs from the subsample
        bo = rpairs[rpairs.B_only & rpairs.B_usable].copy()
        if len(bo):
            bo_rec = bo[["submission_id", "year", "decision", "or_title", "arxiv_id", "v1_title", "v1_date"]].copy()
            bo_rec["found"] = True
            Pb = build_pairs(bo_rec, U, "route_B_only")
            Pu = pd.concat([P, Pb], ignore_index=True)
            specs["union_route"] = flip_table(Pu, keys_t, "union_route")
            rv_sum["n_B_only_pairs_added"] = int(len(Pb))
            rv_sum["B_only_pairs_changed_rate"] = float(Pb.changed_norm.mean()) if len(Pb) else None

    # ---------------- universe stage prevalences and tipping points
    df = universe_frame()
    keys_all = keys_t + [k for k, *_ in ABS_FEATS]
    sums = stage_prevalences(df, keys_all)
    Ppool, apool = pooled(sums, POST)
    Pt = Ppool[:, :len(keys_t)]
    tp = tipping_table(Pt, apool, keys_t, flips, did_b, "2024-26")
    log("tipping points (2024-26 pooled, primary audit):\n" + tp[
        ["feature", "auditable", "G_dec_obs", "G_dec_lo95", "G_dec_hi95", "did_pp", "did_lo_pp", "did_hi_pp",
         "tip_dec_pp", "G_dec_audit_lo", "G_dec_audit_hi", "G_dec_identified", "claim_dec_passes_gate",
         "G_total_obs", "tip_total_pp", "G_total_identified"]].round(3).to_string())

    # identification across specs
    id_rows = []
    for sname, (ftab, db) in specs.items():
        tps = tipping_table(Pt, apool, keys_t, ftab, db, "2024-26")
        tps["spec"] = sname
        tps["n_acc"] = ftab.set_index("feature").loc[tps.feature, "n_acc"].to_numpy()
        tps["n_rej"] = ftab.set_index("feature").loc[tps.feature, "n_rej"].to_numpy()
        id_rows.append(tps)
    idt = pd.concat(id_rows, ignore_index=True)

    # per-year tipping (year-specific audit DiD)
    by_year = []
    for y in AUDIT_YEARS:
        Py_ = P[P.year == y].reset_index(drop=True)
        if Py_.acc.nunique() < 2:
            continue
        fy, dby = flip_table(Py_, keys_t, f"year_{y}")
        Pyy, ayy = pooled(sums, (y,))
        t_y = tipping_table(Pyy[:, :len(keys_t)], ayy, keys_t, fy, dby, str(y))
        t_y["n_acc"], t_y["n_rej"] = int(Py_.acc.sum()), int((Py_.acc == 0).sum())
        by_year.append(t_y)
    tpy = pd.concat(by_year, ignore_index=True)

    # ---------------- abstract audit (arXiv v1 abstracts)
    v1a = read_jsonl(V1ABS_PATH)
    abs_info = {"n_records": 0}
    tpa = pd.DataFrame()
    fla = pd.DataFrame()
    if not v1a.empty:
        v1a = v1a[v1a.error.isna()] if "error" in v1a else v1a
        v1a = v1a.drop_duplicates("submission_id", keep="last")
        o2 = orig.drop(columns=["v1_title", "v1_date"]).merge(
            v1a[["submission_id", "v1_title", "v1_date", "v1_summary"]], on="submission_id", how="inner")
        Pa = build_pairs(o2, U, "v1abs", v1_abstract=True)
        abs_info = dict(n_records=int(len(v1a)), n_pairs=int(len(Pa)),
                        by_decision=Pa.decision.value_counts().to_dict() if len(Pa) else {})
        if len(Pa) and Pa.acc.nunique() == 2:
            keys_a = [k for k, *_ in ABS_FEATS]
            fla, dba = flip_table(Pa, keys_a, "v1_abstract")
            Pa_t = Ppool[:, len(keys_t):]
            tpa = tipping_table(Pa_t, apool, keys_a, fla, dba, "2024-26")
            # consistency: v1 titles fetched again equal the original audit's v1 titles
            chk = Pa.merge(orig[["submission_id", "v1_title"]], on="submission_id", suffixes=("", "_orig"))
            abs_info["v1_title_consistent"] = float((chk.v1_title.map(A.norm_title) ==
                                                     chk.v1_title_orig.map(A.norm_title)).mean())
            abs_info["abstract_jaccard_v1_vs_stored"] = Pa.groupby("decision").abs_jacc.mean().to_dict()
            log("abstract audit flips:\n" + fla[["feature", "n_acc", "v1_present_acc", "adds_acc", "drops_acc",
                                                 "n_rej", "v1_present_rej", "adds_rej", "drops_rej", "did",
                                                 "did_lo", "did_hi", "auditable"]].round(4).to_string())
            log("abstract tipping:\n" + tpa[["feature", "G_dec_obs", "tip_dec_pp", "did_pp", "did_lo_pp",
                                             "did_hi_pp", "G_dec_identified", "G_total_obs", "tip_total_pp",
                                             "G_total_identified"]].round(3).to_string())
    log(f"abstract audit: {json.dumps(jsonable(abs_info))}")

    # ---------------- gate (PLAN section 4) for D4 acceptance-margin claims
    tpi = tp.set_index("feature")
    gate = []
    nm = tpi.loc["NAME"]
    gate.append(dict(claim="H4a NAME G_total within [0.90, 1.11] (2024-26 pooled)", feature="NAME",
                     observed=nm.G_total_obs, obs_ci90=f"[{nm.G_total_lo90:.3f}, {nm.G_total_hi90:.3f}]",
                     audit_interval=f"[{nm.G_total_audit_lo:.3f}, {nm.G_total_audit_hi:.3f}]",
                     corrected_ci90=f"[{nm.G_total_corr_lo90:.3f}, {nm.G_total_corr_hi90:.3f}]",
                     passes=bool(0.90 <= nm.G_total_corr_lo90 and nm.G_total_corr_hi90 <= 1.11),
                     rule="editing-corrected 90% CI (universe x audit bootstrap) inside the TOST margins"))
    gate.append(dict(claim="H4a NAME G_dec within [0.90, 1.11] (2024-26 pooled)", feature="NAME",
                     observed=nm.G_dec_obs, obs_ci90=f"[{nm.G_dec_lo90:.3f}, {nm.G_dec_hi90:.3f}]",
                     audit_interval=f"[{nm.G_dec_audit_lo:.3f}, {nm.G_dec_audit_hi:.3f}]",
                     corrected_ci90=f"[{nm.G_dec_corr_lo90:.3f}, {nm.G_dec_corr_hi90:.3f}]",
                     passes=bool(0.90 <= nm.G_dec_corr_lo90 and nm.G_dec_corr_hi90 <= 1.11),
                     rule="editing-corrected 90% CI inside the TOST margins"))
    for k in keys_t:
        r = tpi.loc[k]
        gate.append(dict(claim=f"acceptance association of {k} (G_dec != 1)", feature=k, observed=r.G_dec_obs,
                         obs_ci90=f"[{r.G_dec_lo90:.3f}, {r.G_dec_hi90:.3f}]",
                         audit_interval=f"[{r.G_dec_audit_lo:.3f}, {r.G_dec_audit_hi:.3f}]",
                         corrected_ci90=f"[{r.G_dec_corr_lo90:.3f}, {r.G_dec_corr_hi90:.3f}]",
                         passes=bool(r.claim_dec_passes_gate),
                         rule="auditable, tipping point beyond audit 95% CI, and observed G_dec 95% CI excludes 1"))
    if len(tpa):
        tpai = tpa.set_index("feature")
        for k in tpai.index:
            r = tpai.loc[k]
            gate.append(dict(claim=f"H4b/abstract: {k} G_total < 1 (2024-26)", feature=k, observed=r.G_total_obs,
                             obs_ci90=f"[{r.G_total_lo90:.3f}, {r.G_total_hi90:.3f}]",
                             audit_interval=f"[{r.G_total_audit_lo:.3f}, {r.G_total_audit_hi:.3f}]",
                             corrected_ci90=f"[{r.G_total_corr_lo90:.3f}, {r.G_total_corr_hi90:.3f}]",
                             passes=bool(r.G_total_identified and r.G_total_corr_hi95 < 1),
                             rule="abstract audit: auditable, tipping beyond CI, corrected 95% CI below 1"))
    r = tpi.loc["L_title"]
    gate.append(dict(claim="H4b L-title G_total < 1 (2024-26)", feature="L_title", observed=r.G_total_obs,
                     obs_ci90=f"[{r.G_total_lo90:.3f}, {r.G_total_hi90:.3f}]",
                     audit_interval=f"[{r.G_total_audit_lo:.3f}, {r.G_total_audit_hi:.3f}]",
                     corrected_ci90=f"[{r.G_total_corr_lo90:.3f}, {r.G_total_corr_hi90:.3f}]",
                     passes=bool(r.G_total_identified and r.G_total_corr_hi95 < 1),
                     rule="auditable, tipping beyond CI, corrected 95% CI below 1"))
    if "enlarged" in set(idt.spec):
        ne = idt[(idt.spec == "enlarged") & (idt.feature == "NAME")].iloc[0]
        ntag = f"enlarged audit, partial, n = {int(ne.n_acc)}/{int(ne.n_rej)} pairs"
        for nm_, col in [("G_total", "total"), ("G_dec", "dec")]:
            gate.append(dict(claim=f"H4a NAME {nm_} within [0.90, 1.11] (2024-26 pooled; {ntag})", feature="NAME",
                             observed=ne[f"G_{col}_obs"],
                             obs_ci90=f"[{ne[f'G_{col}_lo90']:.3f}, {ne[f'G_{col}_hi90']:.3f}]",
                             audit_interval=f"[{ne[f'G_{col}_audit_lo']:.3f}, {ne[f'G_{col}_audit_hi']:.3f}]",
                             corrected_ci90=f"[{ne[f'G_{col}_corr_lo90']:.3f}, {ne[f'G_{col}_corr_hi90']:.3f}]",
                             passes=bool(0.90 <= ne[f"G_{col}_corr_lo90"] and ne[f"G_{col}_corr_hi90"] <= 1.11),
                             rule="as above, with the pooled original + enlargement audit"))
        n_id = int(idt[(idt.spec == "enlarged")].G_dec_identified.sum())
        gate.append(dict(claim=f"acceptance associations identified ({ntag})", feature="all", observed=np.nan,
                         obs_ci90="", audit_interval="", corrected_ci90="", passes=bool(n_id > 0),
                         rule=f"{n_id} of {len(keys_t)} title features identified"))
    gate = pd.DataFrame(gate)
    log("gate:\n" + gate[["claim", "observed", "audit_interval", "corrected_ci90", "passes"]].to_string())

    # ---------------- write tables
    fl_all = pd.concat([s[0] for s in specs.values()], ignore_index=True)
    P.drop(columns=[]).to_csv(OUTDIR / "audit_pairs.csv", index=False)
    fr.to_csv(OUTDIR / "found_rates.csv", index=False)
    fm.to_csv(OUTDIR / "findability_models.csv", index=False)
    rt.to_csv(OUTDIR / "retitling.csv", index=False)
    fl_all.to_csv(OUTDIR / "T4_2_flip_matrices.csv", index=False)
    pd.concat(multi, ignore_index=True).to_csv(OUTDIR / "T4_2_flip_multiclass.csv", index=False)
    tp.to_csv(OUTDIR / "T4_2_tipping_points.csv", index=False)
    tpy.to_csv(OUTDIR / "T4_2_tipping_by_year.csv", index=False)
    idt.to_csv(OUTDIR / "T4_2_identification_by_spec.csv", index=False)
    gate.to_csv(OUTDIR / "gate.csv", index=False)
    if len(fla):
        pd.concat([fla, tpa.add_prefix("tp_")], axis=1).to_csv(OUTDIR / "abstract_audit.csv", index=False)
    if not rv.empty:
        rv.to_csv(OUTDIR / "route_validation.csv", index=False)
        keep = ["submission_id", "year", "decision", "route", "surname_b", "A_found", "B_found", "B_found_strict",
                "tier", "abstract_jaccard", "same_id", "A_usable", "B_usable", "A_changed", "B_changed",
                "A_latest_diff", "B_latest_diff", "orig_arxiv_id", "arxiv_id", "hit_query"]
        rpairs[[c for c in keep if c in rpairs]].to_csv(OUTDIR / "route_pairs.csv", index=False)

    # ---------------- figures
    fig_findability(fr, rt)
    tp_fig = pd.concat([tp, tpa], ignore_index=True) if len(tpa) else tp
    fig_tipping(tp_fig)
    fig_route(rv)
    fig_flip_rates(fl_all)

    # ---------------- results.json
    def frow(tab, k):
        r = tab.set_index("feature").loc[k]
        return {c: r[c] for c in r.index if not isinstance(r[c], str) or c in ("label", "family")}
    res = dict(
        meta=dict(script="analyses/snapshot_bounds.py", n_boot=N_BOOT, seed=SEED, min_v1_present=MIN_V1,
                  decision_dates=DEC, runtime_s=round(time.time() - t0, 1),
                  sources=dict(original=str(ORIG_PATH), route=str(ROUTE_PATH), v1abs=str(V1ABS_PATH),
                               enlarge=str(ENLARGE_PATH)),
                  n_original=int(len(orig)), n_pairs_primary=int(len(P)),
                  n_pairs_by_decision=P.decision.value_counts().to_dict(), enlargement=enl_info,
                  abstract_audit=abs_info),
        findability=dict(
            rates=fr[fr.source == "original"].to_dict(orient="records"),
            models=fm[fm.term.isin(["acc", "log_nw", "NAME"])].to_dict(orient="records")),
        retitling=dict(table=rt[rt.spec == "primary"].to_dict(orient="records"), extra=rt_extra),
        flips={s: v[0].to_dict(orient="records") for s, v in specs.items()},
        tipping_2024_26={k: frow(tp, k) for k in keys_t},
        tipping_by_year=tpy.to_dict(orient="records"),
        identification_by_spec=idt[["spec", "feature", "auditable", "did_pp", "did_lo_pp", "did_hi_pp",
                                    "tip_dec_pp", "G_dec_identified", "G_total_identified", "n_acc", "n_rej"]]
        .to_dict(orient="records"),
        abstract_audit=dict(flips=fla.to_dict(orient="records") if len(fla) else [],
                            tipping=tpa.to_dict(orient="records") if len(tpa) else []),
        route_validation=dict(table=rv.to_dict(orient="records") if not rv.empty else [], summary=rv_sum),
        gate=gate.to_dict(orient="records"),
    )
    res = compose_results(res, tp=tp, flips=flips, fm=fm, fr=fr, rt=rt, rt_extra=rt_extra, idt=idt, rv=rv,
                          rv_sum=rv_sum, gate=gate, tpa=tpa, fla=fla, P=P)
    (OUTDIR / "results.json").write_text(json.dumps(jsonable(res), indent=1))
    log(f"done in {time.time() - t0:.0f}s")
    (OUTDIR / "snapshot_bounds.log").write_text("\n".join(_LOG) + "\n")
    return res


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="WP4 snapshot bounds")
    ap.add_argument("--enlarge-n", type=int, default=None,
                    help="use only the first N lines of cache/arxiv_audit_enlarge.jsonl (default: all)")
    main(ap.parse_args().enlarge_n)
