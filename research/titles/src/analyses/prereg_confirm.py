"""WP9 (PLAN.md section 4): pre-registration bundle for the held-out (~20%) confirmation split.

What this module does
---------------------
1. CT1-CT12 are implemented as PURE functions: each takes an analysis frame (discovery or held-out, built by the
   same code path) plus the frozen parameters `fz` (see `load_frozen`) and returns a result dict. They do no file
   I/O and use fixed seeds, so the held-out run is one call per test.
2. A discovery dry run applies every test to the discovery data and records the estimate the held-out run will be
   compared with (outputs/prereg/dryrun.json).
3. The bundle is frozen and hashed: code files, lexicons.json and the other frozen lexicons, the MiniLM k=100
   KMeans centroids and LLM-cluster list, the rolling R1 vectorisers and classifiers (refitted here with D1's
   CV-chosen C because D1 kept only scores), the DFL cell model, the fingerprint lists, the camera-ready audit
   state used by the gate and the machine-readable decision rules (frozen/rules.json).
   outputs/prereg/bundle.sha256 lists every file (sha256sum format); its own SHA-256 is the bundle hash recorded in
   prereg.md and dryrun.json.

Revision 2 (integration pass, before any held-out request)
---------------------------------------------------------
- The gate audit is WP4's frozen, complete audit (original + all 2,004 enlargement lines, SHA-256 checked against
  outputs/snapshot/results.json -> meta.audit_freeze): title gate = WP4 primary pairs (2023-26); abstract gate =
  WP4's 2024-26 v1-abstract pairs; flip tables via snapshot_final.flips (auditable = >= 10 v1-present per arm AND
  measurable through arXiv metadata). Revision 1 used the original audit + 1,261 enlargement lines.
- The gate uses WP4's multiplicity-controlled rule. Acceptance-margin ASSOCIATION claims (CT6 G_total, CT10) pass
  only if the marker is auditable, the editing-corrected 95% interval lies beyond the claim's boundary, and the
  one-sided identification p (z = (D_hat - D*)/sqrt(se_D^2 + se_D*^2), including the tipping point's sampling
  error) survives Holm at 0.025 across the run's auditable association claims (decide()). EQUIVALENCE claims
  (CT5, CT11) keep the editing-corrected interval rules (WP4 G1 construction for CT5).
- Required code changed after revision 1 (D3/D4 post-audit fixes), so the bundle hash changes; the previous hash
  and the reason are recorded in params.json -> revision and in prereg.md.

Revision 3 (second integration pass, before any held-out request)
-----------------------------------------------------------------
- Reading notes for CT1, CT2, CT4, CT6 and CT12 (audit_interpretation_notes): what a confirmed statistic would and
  would not show, given the direction audits. The decision rules are unchanged.
- Required code edited outside this module: d3_slots.py (D3's descriptive slot-word audit reads WP4's frozen
  enlargement sample instead of a 1,620-line pre-freeze pin, and fails loudly without the caches) and
  d4_bias_atlas.py (atlas prevalence ratios reuse the stage-gain bootstrap seed). No CT uses either change; the
  frozen parameters other than params.json -> revision and rules.json are byte-identical, and the dry run is re-run
  and compared statistic by statistic (stage `revise`).

Held-out handling (PLAN section 4)
----------------------------------
- `prepare_frame` rebuilds the analysis frame from raw submissions rows exactly as WP0/WP1 did for discovery:
  placeholder filter, pools/stages, harmonised area, features_v2.build, R1 mask text, topic100 = nearest frozen
  discovery MiniLM centroid, llm_topic = regex OR membership in a frozen discovery LLM cluster.
- Author history for CT3/CT12 is computed on the union of discovery and held-out keys (`panel_rows`).
- `run_heldout` verifies the bundle hashes, refuses to run twice (guard file) and runs each test once.

Stages (each well under 20 min with OMP_NUM_THREADS=2):
    cd research/titles/src
    python -m analyses.prereg_confirm freeze     # frozen parameters -> outputs/prereg/frozen/ (~5 min)
    python -m analyses.prereg_confirm check      # held-out pipeline check on a discovery sample (~1 min)
    python -m analyses.prereg_confirm dryrun     # CT1-CT12 on discovery -> dryrun.json (~8 min)
    python -m analyses.prereg_confirm bundle     # bundle.sha256 + prereg.md
    python -m analyses.prereg_confirm verify     # re-hash the bundle
    python -m analyses.prereg_confirm refreeze_final   # revision 2: re-freeze the audit gate on WP4's complete audit
    python -m analyses.prereg_confirm audit_refreeze   # closed in revision 2 (the enlargement is complete)
    python -m analyses.prereg_confirm revise           # revision 3: record the revision (params.json, rules.json); then
                                                       # dryrun -> bundle -> verify
    python -m analyses.prereg_confirm heldout <submissions.csv.gz> <submission_authors.csv.gz>   # ONCE
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import features_v2 as FV
from analyses import d1_its as D1
from analyses import d1_content_cf as CF
from analyses import d2_panel as P2
from analyses import d3_slots as D3
from analyses import d3_vintage as D3V
from analyses import d3_register as D3R
from analyses import d4_stage_gains as S4
from analyses import d4_bias_atlas as DBA
from analyses import snapshot_bounds as SB
from analyses import snapshot_final as SF   # WP4 final builders (frozen complete audit, channel rule, Holm gate)
from common import read_table

warnings.filterwarnings("ignore")

DATE = "2026-10-11"
STUDY = C.OUT.parent                      # research/titles
SRC = STUDY / "src"
OUTDIR = C.OUT / "prereg"
FROZEN = OUTDIR / "frozen"
REFREEZE = FROZEN / "audit_refreeze"
GUARD = OUTDIR / "heldout_started.json"
SEED = 20261011
B_PAPER = 2000
B_KEY = 1000
D2_SEED = 20260                           # D2 key-cluster bootstrap seed (reproduces D2's draws)
ALPHA = 0.05
HO_RATIO = 0.25                           # held-out / discovery size per year (PLAN section 4)
PRIMARY = ("CT1", "CT2", "CT3", "CT4", "CT5", "CT6")
SECONDARY = ("CT7", "CT8", "CT9", "CT10", "CT11", "CT12")
POST = (2024, 2025, 2026)
U_PRE = (2019, 2020, 2021, 2022, 2023)
E_WIN, L_WIN = P2.E_WIN, P2.L_WIN
TOST_MARGIN = (0.90, 1.11)
STAGE_COLS = ["s0", "s1", "s2", "s3", "s0n", "s1n", "s2n"]
GATE_SPEC_TITLE = "title_primary"         # WP4 primary: original 2023-26 + complete enlargement (revision 2)
GATE_SPEC_ABS = "abstract_2024_26"        # WP4 primary abstract audit: 2024-26 v1-abstract pairs (revision 2)
GATE_ALPHA1 = 0.025                       # one-sided level of the PLAN's 95% CI rule (WP4 gate)
WP4_RESULTS = C.OUT / "snapshot" / "results.json"
GATE_RULE = ("WP4 multiplicity-controlled gate (revision 2). Association claims (CT6 G_total, CT10): the marker must "
             "be auditable (>= 10 v1-present per arm and measurable through arXiv metadata), its editing-corrected "
             "95% interval (bootstrap replicate paired with an audit draw D ~ N(D_hat, se_D)) must lie beyond the "
             "claim's boundary, and its one-sided identification p, z = (D_hat - D*)/sqrt(se_D^2 + se_D*^2) with "
             "se_D the pseudo-flip SE and se_D* the bootstrap SE of the tipping point, must survive Holm at 0.025 "
             "across the run's auditable association claims. Equivalence claims (CT5, CT11): editing-corrected "
             "interval rules (CT5 = WP4 G1 TOST; CT11 = ACC-pair CIs widened by the largest editing bias inside "
             "the NAME audit CI).")
REVISION_1 = dict(
    revision=1, date=DATE,
    bundle_hash="f69fdb468702fe11e336b81476869531a71acb1d4f922b8bd1d479934bbac628",
    gate_audit="original audit + first 1,261 enlargement lines (965 pooled title pairs incl. 2022; 330 v1 abstracts of "
               "the original pairs); gate = point tipping point beyond the 95% audit CI (uncorrected)")
REVISION_2 = dict(
    revision=2, date=DATE,
    bundle_hash="853827a92e85ad56ee85376e8b90a881c4f4ca1e46a861e80ed21a04e883d922",
    previous_bundle_hash=REVISION_1["bundle_hash"],
    previous_audit=REVISION_1["gate_audit"],
    reason=("Post-audit corrections before any held-out data were requested or seen (no guard file, no "
            "heldout.json): (1) the D3 and D4 fixer passes changed required code hashed by revision 1 "
            "(d3_register.py, d3_slots.py, d3_vintage.py, d4_bias_atlas.py, d4_stage_gains.py; the frozen test "
            "definitions they supply are unchanged); (2) the WP4 enlargement finished (2,004 lines, 2,000 records) "
            "and the gate audit is re-frozen on WP4's complete audit; (3) the gate adopts WP4's "
            "multiplicity-controlled rule (identification p with the tipping point's sampling error, Holm at "
            "0.025, editing-corrected interval), because the revision-1 uncorrected rule admits acceptance "
            "associations that the Holm gate rejects. The R1 models, centroids, lexicons, slot inventory, DFL cells "
            "and every test statistic are unchanged (frozen files byte-identical)."))
REVISION = dict(
    revision=3, date=DATE, stage="second integration pass",
    previous_bundle_hash=REVISION_2["bundle_hash"], previous_revision=2,
    gate_audit="unchanged from revision 2 (WP4's complete audit, 2,004 enlargement lines; Holm gate)",
    reason=("Cross-direction consistency corrections before any held-out data were requested or seen (no guard "
            "file, no heldout.json): (1) reading notes for CT1, CT2, CT4, CT6 and CT12 state what a confirmed "
            "statistic would and would not show given the direction audits (CT1 and CT2 use paper-level inference "
            "that D1's audit demoted; CT4 leans on via/using and 'enhancing'; CT6 mostly re-detects the pre-2024 "
            "R24 penalty; CT12 mixes cohort with tenure); the decision rules are unchanged; (2) required code "
            "outside the tests changed: d3_slots.py reads WP4's frozen enlargement sample (2,004 lines, SHA-256 "
            "checked) for D3's descriptive slot-word audit instead of a 1,620-line pre-freeze pin and fails loudly "
            "without the audit caches; d4_bias_atlas.py makes atlas prevalence ratios reuse the stage-gain "
            "bootstrap seed. No CT uses either change. Frozen parameters other than params.json -> revision and "
            "rules.json are byte-identical, and the dry run was re-run with every statistic, CI, p-value and gate "
            "field unchanged."),
    history=[REVISION_1, REVISION_2])

_LOG: list[str] = []


def log(msg: str):
    print(msg, flush=True)
    _LOG.append(msg)


def flush_log(name: str):
    OUTDIR.mkdir(parents=True, exist_ok=True)
    with (OUTDIR / name).open("a") as fh:
        fh.write("\n".join(_LOG) + "\n")
    _LOG.clear()


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with Path(p).open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def clean(o):
    return S4._clean(o)


def write_json(obj, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(clean(obj), indent=1))


def boot_p(draws: np.ndarray, bad) -> float:
    """One-sided bootstrap p with the +1 correction: (1 + #{draws in the null region}) / (B + 1)."""
    d = np.asarray(draws, float)
    d = d[np.isfinite(d)]
    return float((1 + np.sum(bad(d))) / (len(d) + 1))


def q(a, lo=0.025, hi=0.975):
    a = np.asarray(a, float)
    a = a[np.isfinite(a)]
    return [float(np.quantile(a, lo)), float(np.quantile(a, hi))] if len(a) else [np.nan, np.nan]


def z_power(z_ho: float) -> dict:
    """Approximate power of a one-sided test whose held-out z is z_ho (normal; Holm worst case and alpha .05)."""
    return {"alpha_0.0083": float(stats.norm.cdf(z_ho - stats.norm.ppf(1 - ALPHA / 6))),
            "alpha_0.05": float(stats.norm.cdf(z_ho - stats.norm.ppf(1 - ALPHA)))}


def _ho_se(se: float) -> float:
    return float(se / np.sqrt(HO_RATIO))


# ================================================================================================
# 1. Analysis frames (discovery and held-out share one code path after the raw-table step)
# ================================================================================================
def finalize(df: pd.DataFrame) -> pd.DataFrame:
    """Integer flags and the derived columns every CT uses (same for discovery and held-out)."""
    df = df.copy()
    for c in df.columns:
        if pd.api.types.is_bool_dtype(df[c]):
            df[c] = df[c].astype(int)
    df["lnw"] = np.log(df.n_words.clip(lower=1))
    df["F_d1"] = ((df.f24_2 == 1) | (df.f26 == 1) | (df.title_typo == 1)).astype(int)   # D1 tool fingerprint
    df["O_union"] = df[["case_all_caps", "case_sentence_case", "question_opener"]].max(axis=1).astype(int)
    df["L_union"] = df[S4.BINARY_L].max(axis=1).astype(int)
    df["L_title"] = df[["title_typo", "r24_any", "r26_any"]].max(axis=1).astype(int)
    df["L_abstract"] = df[["f24", "f26", "abs_emdash"]].max(axis=1).astype(int)
    df["s0"] = 1
    df["s1"], df["s2"], df["s3"] = df.stage_s1, df.stage_s2, df.stage_s3
    nacc = 1 - df.ACC
    df["s0n"], df["s1n"], df["s2n"] = nacc, df.s1 * nacc, df.s2 * nacc
    return df.reset_index(drop=True)


def discovery_frame() -> pd.DataFrame:
    """Discovery U (43,482 rows) from the WP0/WP1 outputs, plus the D1 R1 mask text."""
    df = C.load_analysis_frame()
    p = CF.CACHE_DIR / "r1_text.parquet"
    t = pd.read_parquet(p) if p.exists() else None
    if t is not None and len(t) == len(df) and (t.submission_id.to_numpy() == df.submission_id.to_numpy()).all():
        df["r1_text"] = t.text.to_numpy(dtype=object)
    else:
        df["r1_text"] = [FV.mask_abstract_lower(a, l) for a, l in zip(df.abstract, df.lead_segment.fillna(""))]
    df["split"] = "discovery"
    return finalize(df)


def read_raw(path: str | Path) -> pd.DataFrame:
    """Raw export table with the README's reading convention."""
    return pd.read_csv(path, keep_default_na=False, na_values=[r"\N"], low_memory=False)


def embed_minilm(texts) -> np.ndarray:
    """all-MiniLM-L6-v2 abstract embeddings (L2-normalised), as in cache/emb_abstract_all-MiniLM-L6-v2.npy."""
    from sentence_transformers import SentenceTransformer
    m = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
    return m.encode(list(pd.Series(texts).fillna("").astype(str)), batch_size=64, normalize_embeddings=True,
                    convert_to_numpy=True, show_progress_bar=False).astype(np.float32)


def prepare_frame(s: pd.DataFrame, fz: dict, emb: np.ndarray | None = None,
                  split: str = "heldout") -> tuple[pd.DataFrame, pd.DataFrame]:
    """Held-out analysis frame from raw submissions rows (same schema as data/submissions.csv.gz).

    Mirrors _core.build_universe + features_v2.build, except that topic100 is the nearest FROZEN discovery MiniLM
    centroid and llm_cluster is membership in the FROZEN discovery LLM-cluster list (PLAN section 4).
    `emb` (rows aligned to `s`) may be passed; otherwise the abstracts are embedded with all-MiniLM-L6-v2.
    Returns (frame, per-year counts of rows / dropped placeholders / U)."""
    s = s.reset_index(drop=True).copy()
    s["year"] = s.year.astype(int)
    reason = pd.Series([C.placeholder_reason(t, a) for t, a in zip(s.title.fillna(""), s.abstract.fillna(""))],
                       index=s.index)
    in_u = reason.eq("")
    pf = C.pool_flags(s)
    counts = pd.DataFrame({"n_rows": s.groupby("year").size(), "n_dropped": (~in_u).groupby(s.year).sum(),
                           "n_U": in_u.groupby(s.year).sum()}).reset_index()
    u, pfu = s[in_u], pf[in_u]
    out = pd.DataFrame({
        "submission_id": u.submission_id.values,
        "year": u.year.values.astype(int),
        "emb_row": np.where(in_u.to_numpy())[0],
        "title": u.title.fillna("").values,
        "title_nfkc": u.title.fillna("").map(C.nfkc).values,
        "abstract": u.abstract.fillna("").values,
        "administrative_status": u.administrative_status.values,
        "decision": u.decision.values,
        "outcome_eligible": pd.to_numeric(u.outcome_eligible, errors="coerce").fillna(0).astype(int).values,
        "primary_area": u.primary_area.replace("", np.nan).values,
        "normalized_keywords_json": u.normalized_keywords_json.values,
        "declared_name_count": pd.to_numeric(u.declared_name_count, errors="coerce").fillna(0).astype(int).values,
    })
    out["area_h"] = C.harmonise_area(pd.Series(out.primary_area), pd.Series(out.year)).values
    out["area_short"] = out.area_h.map(C.AREA_SHORT)
    for c in pfu.columns:
        out[c] = pfu[c].values
    out = pd.concat([out, C.period_columns(out.year)], axis=1)
    out["log_authors"] = np.log(out.declared_name_count.clip(lower=1))
    E = np.asarray(emb, np.float32)[in_u.to_numpy()] if emb is not None else embed_minilm(out.abstract)
    out["topic100"] = C.assign_centroids(E, fz["centroids_minilm_k100"])
    out["llm_regex"] = C.llm_regex_flag(out.title, out.abstract).values
    out["llm_cluster"] = out.topic100.isin(fz["llm_clusters"])
    out["llm_topic"] = out.llm_regex | out.llm_cluster
    out["non_llm"] = ~out.llm_topic
    feats = FV.build(out[["submission_id", "year", "title", "title_nfkc", "abstract"]])
    feats = feats.drop(columns=[c for c in feats.columns if c in out.columns and c != "submission_id"])
    df = out.merge(feats, on="submission_id", how="left", validate="1:1")
    df["r1_text"] = [FV.mask_abstract_lower(a, l) for a, l in zip(df.abstract, df.lead_segment.fillna(""))]
    df["split"] = split
    return finalize(df), counts


def panel_rows(authors: pd.DataFrame, papers: pd.DataFrame) -> pd.DataFrame:
    """D2 declared-profile-key panel (2021-26, one row per key x paper, first/last list-position flags from the
    full declared list) for the given papers. For the held-out run `authors` and `papers` are the UNION of
    discovery and held-out rows (author history on the union of keys, PLAN section 4)."""
    a = authors[["submission_id", "year", "source_list_position", "native_id", "native_id_kind",
                 "declared_id_key"]]
    a = a[a.submission_id.isin(set(papers.submission_id))].copy()
    pmax = a.groupby("submission_id").source_list_position.transform("max")
    a["is_first"] = a.source_list_position.eq(0)
    a["is_last"] = a.source_list_position.eq(pmax)
    a["list_len"] = pmax + 1
    return P2.make_panel(a, "profile", P2.PANEL_YEARS)


# ================================================================================================
# 2. Frozen rolling R1 models (D1 content counterfactual; CT2)
# ================================================================================================
def r1_fold_scores(texts, win: dict) -> np.ndarray:
    """(5 x n) decision scores of the five frozen fold models of one rolling window. The TF-IDF transform is
    rebuilt from the frozen vocabulary and idf (sublinear tf, l2 norm), i.e. TfidfVectorizer.transform."""
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.preprocessing import normalize
    vocab = {t: i for i, t in enumerate(win["terms"].tolist())}
    X = CountVectorizer(vocabulary=vocab, ngram_range=(1, 2), dtype=np.float64).transform(list(texts)).tocsr()
    X.data = 1.0 + np.log(X.data)
    X = normalize(X.multiply(np.asarray(win["idf"], float)[None, :]).tocsr(), norm="l2")
    return np.asarray(X @ np.asarray(win["coef"], float).T).T + np.asarray(win["intercept"], float)[:, None]


def freeze_r1(disc: pd.DataFrame) -> dict:
    """Refit D1's rolling R1 models (train y-3..y-1, test y = 2019..2026) at D1's CV-chosen C with D1's folds,
    save vocabulary/idf/fold coefficients, the intercept shift and the calibration-year OOF scores, and check the
    test-row fold scores against D1's stored scores (D1 saved scores only, not models)."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.model_selection import StratifiedKFold
    meta_d1 = json.loads((CF.SCORES / "R1__U__primary__rolling.json").read_text())
    S = pd.read_parquet(CF.SCORES / "R1__U__primary__rolling.parquet")
    texts = disc.r1_text.to_numpy(dtype=object)
    yrs = disc.year.to_numpy()
    y = disc.name_primary.to_numpy().astype(int)
    out = {}
    for w in CF.windows("rolling"):
        t0 = time.time()
        yt = w["test"][0]
        tr = np.where(np.isin(yrs, w["train"]))[0]
        te = np.where(yrs == yt)[0]
        Cv = float(meta_d1["windows"][w["name"]]["C"])
        vec = TfidfVectorizer(min_df=5, max_df=0.5, ngram_range=(1, 2), sublinear_tf=True, max_features=50000,
                              dtype=np.float32)
        Xtr = vec.fit_transform(texts[tr])
        ytr = y[tr]
        folds = list(StratifiedKFold(CF.N_FOLDS, shuffle=True, random_state=0).split(np.zeros(len(tr)), ytr))
        oof = np.zeros(len(tr))
        coefs, icpts = [], []
        for trf, vaf in folds:
            m = CF._lr(Cv, "R1").fit(Xtr[trf], ytr[trf])
            oof[vaf] = m.decision_function(Xtr[vaf])
            coefs.append(m.coef_.ravel().astype(np.float64))
            icpts.append(float(m.intercept_[0]))
        cal = yrs[tr] == w["calib"]
        shift = CF.shift_for(oof[cal], ytr[cal].mean())
        terms = np.array(sorted(vec.vocabulary_, key=vec.vocabulary_.get), dtype=str)
        win = dict(terms=terms, idf=vec.idf_.astype(np.float64), coef=np.vstack(coefs),
                   intercept=np.array(icpts), oof_calib=oof[cal], y_calib=ytr[cal].astype(np.int8))
        sk = r1_fold_scores(texts[te], win)
        st = S[(S.window == w["name"]) & (S.role == "test")].set_index("row").loc[te]
        d1k = st[CF.FOLD_COLS].to_numpy(float).T
        st_cal = S[(S.window == w["name"]) & (S.role == "calib")]
        oof_d1 = st_cal.set_index("row").loc[tr[cal], "score"].to_numpy(float)
        np.savez_compressed(FROZEN / f"r1_rolling_{yt}.npz", **win)
        out[yt] = dict(window=w["name"], train_years=list(w["train"]), calib_year=int(w["calib"]), C=Cv,
                       shift=float(shift), obs_calib=float(ytr[cal].mean()), n_train=int(len(tr)),
                       n_calib=int(cal.sum()), n_features=int(len(terms)),
                       max_abs_diff_test_scores_vs_d1=float(np.max(np.abs(sk - d1k))),
                       max_abs_diff_oof_calib_vs_d1=float(np.max(np.abs(oof[cal] - oof_d1))),
                       seconds=round(time.time() - t0, 1))
        log(f"  R1 {w['name']}: C={Cv} n_tr={len(tr)} shift={shift:.4f} |score-D1|max="
            f"{out[yt]['max_abs_diff_test_scores_vs_d1']:.2e} |oof-D1|max={out[yt]['max_abs_diff_oof_calib_vs_d1']:.2e}"
            f" {time.time() - t0:.0f}s")
    return out


def freeze_dfl() -> dict:
    """D1-H1d DFL cell model (team-size bins x share-new-author bins (2-year lookback) x llm_topic): the 2023
    reference composition and the discovery cell NAME rates. Frozen for completeness (PLAN section 4 lists the
    DFL propensity models); no confirmatory test uses it."""
    from analyses import d1_decompose as DC
    d = DC.load()
    d = d[d.year.isin((2023,) + POST)]
    d = d[~d[["sizeb", "newb", "llm_topic"]].astype(str).isin(["NA", "nan"]).any(axis=1)]
    tab = d.groupby(["year", "cell"]).agg(n=("name_primary", "size"), name_rate=("name_primary", "mean")).reset_index()
    tab["share"] = tab.n / tab.groupby("year").n.transform("sum")
    tab.to_csv(FROZEN / "dfl_cells.csv", index=False)
    return dict(file="frozen/dfl_cells.csv", size_bins=[lab for *_, lab in DC.SIZE_BINS],
                newcomer_bins=["0", "(0,.5]", "(.5,1]"], newcomer_lookback_years=DC.LOOKBACK,
                cell="size_bin|newcomer_bin|llm_topic", reference_year=2023, n_cells=int(tab.cell.nunique()))


def _complete_jsonl(path: Path, n_lines: int | None = None) -> tuple[pd.DataFrame, int, str]:
    """Complete lines (newline-terminated) of an append-only jsonl file, optionally the first n; returns the
    records, the number of lines used and the SHA-256 of exactly those bytes."""
    if not path.exists():
        return pd.DataFrame(), 0, ""
    raw = path.read_bytes().splitlines(keepends=True)
    raw = [ln for ln in raw if ln.endswith(b"\n")]
    if n_lines is not None:
        raw = raw[:n_lines]
    recs = []
    for ln in raw:
        try:
            recs.append(json.loads(ln))
        except ValueError:
            continue
    return pd.DataFrame(recs), len(raw), hashlib.sha256(b"".join(raw)).hexdigest()


def wp4_audit_freeze() -> tuple[int, str]:
    """(n_lines_used, sha256) of WP4's frozen enlargement sample (outputs/snapshot/results.json meta.audit_freeze)."""
    m = json.loads(WP4_RESULTS.read_text())["meta"]["audit_freeze"]["enlargement"]
    return int(m["n_lines_used"]), str(m["sha256_of_lines_used"])


def freeze_audit(dest: Path, enlarge_n: int | None = None) -> dict:
    """Camera-ready audit flips for the gate, built exactly as WP4's final analysis (snapshot_final): title flips on
    the original audit (sensitivity) and on WP4's primary audit (original 2023-26 + the complete, frozen enlargement),
    abstract flips on WP4's 2024-26 v1-abstract pairs (original + enlargement v1 abstracts). Auditability follows
    WP4's rule (>= 10 v1-present titles per arm AND measurable through arXiv metadata). Asserts that the enlargement
    bytes match WP4's freeze hash and that the flip tables reproduce WP4's canonical outputs."""
    dest.mkdir(parents=True, exist_ok=True)
    n_wp4, h_wp4 = wp4_audit_freeze()
    enlarge_n = n_wp4 if enlarge_n is None else enlarge_n
    U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
    orig_raw, n_orig, h_orig = SF.read_frozen(SB.ORIG_PATH)
    enl_raw, n_enl, h_enl = SF.read_frozen(SB.ENLARGE_PATH, enlarge_n)
    v1a_raw, n_v1a, h_v1a = SF.read_frozen(SB.V1ABS_PATH)
    assert enlarge_n != n_wp4 or h_enl == h_wp4, "enlargement bytes differ from WP4's frozen audit"
    orig, enl, v1a = SF.clean(orig_raw), SF.clean(enl_raw), SF.clean(v1a_raw)
    Po_all = SF.pairs(orig, U, "original")
    Pe = SF.pairs(enl, U, "enlarge")
    Po = Po_all[Po_all.year >= 2023].reset_index(drop=True)
    P = pd.concat([Po, Pe], ignore_index=True)
    f0, b0 = SF.flips(Po_all, SF.KEYS_T, "title_original")
    f1, b1 = SF.flips(P, SF.KEYS_T, GATE_SPEC_TITLE)
    o2 = orig.drop(columns=["v1_title", "v1_date"]).merge(
        v1a[["submission_id", "v1_title", "v1_date", "v1_summary"]], on="submission_id", how="inner")
    Pa_o = SF.pairs(o2, U, "v1abs", v1_abstract=True)
    Pa_e = SF.pairs(enl, U, "enlarge", v1_abstract=True)
    Pa_all = pd.concat([Pa_o[Pa_o.year >= 2023], Pa_e], ignore_index=True)
    Pa = Pa_all[Pa_all.year.isin(POST)].reset_index(drop=True)
    fa, ba = SF.flips(Pa, SF.KEYS_A, GATE_SPEC_ABS)
    # reproduction of WP4's canonical tables (same pairs, same code, same seeds)
    repro = {}
    wf = C.OUT / "snapshot" / "T4_2_flip_matrices.csv"
    wa = C.OUT / "snapshot" / "abstract_audit.csv"
    if enlarge_n == n_wp4 and wf.exists() and wa.exists():
        for mine, path, spec in [(f1, wf, "primary"), (fa, wa, "abs_2024_26")]:
            ref = pd.read_csv(path)
            ref = ref[ref.spec == spec].set_index("feature")
            mi = mine.set_index("feature").loc[ref.index]
            dev = float(np.nanmax(np.abs(mi[["did", "did_lo", "did_hi"]].to_numpy(float) -
                                         ref[["did", "did_lo", "did_hi"]].to_numpy(float))))
            aud = bool((mi.auditable.astype(bool) == ref.auditable.astype(bool)).all())
            repro[spec] = dict(max_abs_diff=dev, auditable_identical=aud, n_features=int(len(ref)))
            assert dev < 1e-12 and aud, f"audit flips do not reproduce WP4 ({spec})"
    flips = pd.concat([f0, f1, fa], ignore_index=True)
    flips.to_csv(dest / "audit_flips.csv", index=False)
    np.savez_compressed(dest / "audit_did_boot.npz", title_original=b0, **{GATE_SPEC_TITLE: b1, GATE_SPEC_ABS: ba})
    state = dict(
        frozen_on=time.strftime("%Y-%m-%d %H:%M:%S"),
        source="WP4 final audit (snapshot_final builders); revision 2",
        original=dict(path=str(SB.ORIG_PATH.relative_to(STUDY)), n_lines=n_orig, sha256=h_orig,
                      n_pairs=int(len(Po_all)), pairs_by_decision=Po_all.decision.value_counts().to_dict(),
                      n_pairs_2023_26=int(len(Po))),
        enlargement=dict(path=str(SB.ENLARGE_PATH.relative_to(STUDY)), n_lines_used=n_enl,
                         sha256_of_lines_used=h_enl, wp4_freeze=dict(n_lines_used=n_wp4, sha256=h_wp4),
                         matches_wp4=bool(n_enl == n_wp4 and h_enl == h_wp4),
                         n_records=int(len(enl)), n_pairs=int(len(Pe)),
                         note="complete enlargement (2,000 sampled papers; errored lines superseded by retries)"),
        pooled=dict(n_pairs=int(len(P)), pairs_by_decision=P.decision.value_counts().to_dict(),
                    years="2023-26 (WP4 primary)"),
        v1_abstracts=dict(path=str(SB.V1ABS_PATH.relative_to(STUDY)), n_lines=n_v1a, sha256=h_v1a,
                          n_pairs=int(len(Pa)), pairs_by_decision=Pa.decision.value_counts().to_dict(),
                          years="2024-26 (WP4 primary abstract audit: original + enlargement v1 abstracts)"),
        specs={"title_original": "original 616-paper audit, usable pre-decision pairs (2022-26; sensitivity)",
               GATE_SPEC_TITLE: "WP4 primary: original 2023-26 + complete enlargement (gate spec for title features)",
               GATE_SPEC_ABS: "WP4 primary abstract audit, 2024-26 pairs (gate spec for abstract markers)"},
        auditable_rule=">= 10 v1-present titles (abstracts) in BOTH arms AND measurable through arXiv metadata "
                       "(arXiv titles never ALL-CAPS or U+2011/U+2013-typographic; arXiv abstracts never carry the "
                       "em dash)",
        reproduces_wp4=repro,
        ci="primary net-flip DiD 95% CI: Wald with the pseudo-flip variance floor (WP4); bootstrap B = 2,000 "
           "stratified by year x decision for the combined (editing-corrected) intervals")
    write_json(state, dest / "audit_state.json")
    nm = f1.set_index("feature").loc["NAME"]
    log(f"  audit frozen -> {dest.relative_to(STUDY)}: original {len(Po_all)} pairs, primary {len(P)} "
        f"(enlargement lines {n_enl}, matches WP4 {state['enlargement']['matches_wp4']}), abstract {len(Pa)}; "
        f"NAME DiD {100 * nm.did:+.2f} pp [{100 * nm.did_lo:.2f}, {100 * nm.did_hi:.2f}]; repro {repro}")
    return state


def audit_params(state: dict) -> dict:
    return dict(state=state, gate_spec_title=GATE_SPEC_TITLE, gate_spec_abstract=GATE_SPEC_ABS,
                gate_rule=GATE_RULE, holm_alpha_one_sided=GATE_ALPHA1,
                refreeze_rule="closed in revision 2: the enlargement is complete and frozen in the bundle")


def freeze(disc: pd.DataFrame) -> dict:
    """Write every frozen parameter to outputs/prereg/frozen/."""
    t0 = time.time()
    FROZEN.mkdir(parents=True, exist_ok=True)
    A = Path(FV.__file__).parent
    copies = {"lexicons.json": A / "lexicons.json", "d4_lexicon.json": A / "d4_lexicon.json",
              "slot_inventory.json": C.OUT / "d3_register" / "slot_inventory.json",
              "slot_variants_dropped.json": C.OUT / "validation" / "slot_variants_dropped.json",
              "llm_clusters.json": C.CORE / "llm_clusters.json",
              "area_crosswalk.csv": C.CORE / "area_crosswalk.csv"}
    src_hash = {}
    for nm, p in copies.items():
        shutil.copyfile(p, FROZEN / nm)
        src_hash[nm] = dict(source=str(p.relative_to(STUDY)), sha256=sha256_file(p))
    # KMeans centroids (MiniLM k = 100): saved as a plain .npy so the bytes are deterministic
    cen = C.load_centroids("minilm_k100").astype(np.float32)
    np.save(FROZEN / "centroids_minilm_k100.npy", cen)
    Ecache = C.load_embedding(disc, "abstract", "all-MiniLM-L6-v2")
    agree = float((C.assign_centroids(Ecache, cen) == disc.topic100.to_numpy()).mean())
    log(f"  centroids: nearest-centroid topic100 reproduces the discovery labels for {100 * agree:.2f}% of U")
    # fingerprint lists (extract of lexicons.json, for reading)
    lx = FV.lexicon()
    fp = dict(source="lexicons.json (v2.0, frozen)", RARE21=lx["fingerprints"]["RARE21"],
              F26_words=lx["fingerprints"]["F26_words"], typography_raw=lx["fingerprints"]["typography_raw"],
              R24=lx["register"]["R24"], R26=lx["register"]["R26"],
              F24="abstract has >= 1 RARE21 word", F24_2="abstract has >= 2 distinct RARE21 words (D1 variant)",
              F26="abstract has >= 1 F26 word, or U+2011 / letter-en dash-letter compound in title or abstract",
              F_D1="f24_2 OR f26 OR title_typo (D1 tool fingerprint, CT9)",
              F_D3="f24 OR f26 OR title_typo (D3)")
    write_json(fp, FROZEN / "fingerprints.json")
    log("  fitting rolling R1 models ...")
    r1 = freeze_r1(disc)
    log("  DFL cells ...")
    dfl = freeze_dfl()
    log("  audit ...")
    audit = freeze_audit(FROZEN)
    reg = json.loads((C.OUT / "d3_register" / "register_results.json").read_text())
    obs = disc.groupby("year").name_primary.mean()
    params = dict(
        date=DATE,
        plan=dict(path="docs/PLAN.md", sha256=sha256_file(STUDY / "docs" / "PLAN.md"), section="4"),
        copied_files=src_hash,
        discovery=dict(n_U=int(len(disc)), n_by_year=disc.groupby("year").size().to_dict(),
                       name_primary_share_by_year={int(k): float(v) for k, v in obs.items()}),
        heldout_ratio_assumed=HO_RATIO,
        seeds=dict(main=SEED, d2_key_bootstrap=D2_SEED, d4_stage=S4.SEED, d4_kobak=S4.SEED + 1, d1_f0=3,
                   snapshot=SB.SEED),
        n_boot=dict(paper=B_PAPER, key=B_KEY),
        topics=dict(centroids="frozen/centroids_minilm_k100.npy (MiniLM label means; outputs/topics/centroids.npz "
                              "minilm_k100)", assignment="nearest centroid (Euclidean) of the all-MiniLM-L6-v2 "
                                                         "L2-normalised abstract embedding",
                    discovery_label_reproduction=agree,
                    llm_clusters=json.loads((FROZEN / "llm_clusters.json").read_text())["topic100_minilm_llm_clusters"]),
        d1=dict(its=dict(outcome="name_primary", break_year=2024, fe="topic100", controls=["log_authors", "llm_topic"],
                         cluster="topic100", years=[2017, 2026]),
                r1_windows={int(k): v for k, v in r1.items()},
                r1_spec="name-masked abstract TF-IDF (features_v2.mask_abstract_lower), 1-2-grams, min_df 5, "
                        "max_df 0.5, 50k features, sublinear tf; L2 logit, C from D1's 5-fold CV; prediction = mean "
                        "over the 5 fold models of expit(s_k + c), c solved on the fold models' OOF scores of y-1",
                pre_years=list(U_PRE), post_years=list(POST), tool_F="f24_2 | f26 | title_typo",
                dfl=dfl),
        d2=dict(E=list(E_WIN), L=list(L_WIN), panel_years=list(P2.PANEL_YEARS), key_kind="profile",
                stayer="any-role presence: >= 1 E paper (discovery ∪ held-out) and >= 1 L paper in the L set",
                L_set="held-out papers only (dry run: discovery)", weights="paper (each last/first row weight 1)"),
        d3=dict(large_areas=reg["large_areas"], large_area_rule=reg["large_area_rule"],
                slot_inventory="frozen/slot_inventory.json", stacked_formula=D3.STACKED, slot_years_from=2018,
                opener_rule="primary (PLAN: after an optional NAME lead)", vintage_controls=D3V.CTRL,
                vintage_years=[2025, 2026]),
        d4=dict(years=[2018, 2026], pooled_years=list(POST), pooling="year-standardised (weights = s0 size)",
                tost_margin=list(TOST_MARGIN), kobak_marker="f24", kobak_baseline="cons", kobak_years=[2021, 2026],
                its_pools=["ACC", "REJ", "WD"], equivalence_margin_logOR=0.1),
        audit=audit_params(audit), revision=REVISION,
        versions=dict(python=sys.version.split()[0], numpy=np.__version__, pandas=pd.__version__,
                      sklearn=__import__("sklearn").__version__, statsmodels=__import__("statsmodels").__version__),
    )
    write_json(params, FROZEN / "params.json")
    write_json(rules_doc(), FROZEN / "rules.json")
    log(f"freeze done ({time.time() - t0:.0f}s)")
    return params


def load_frozen(path: Path = FROZEN, prefer_refreeze: bool = True) -> dict:
    params = json.loads((path / "params.json").read_text())
    fz = dict(params=params)
    fz["centroids_minilm_k100"] = np.load(path / "centroids_minilm_k100.npy")
    fz["llm_clusters"] = params["topics"]["llm_clusters"]
    fz["slot_inventory"] = json.loads((path / "slot_inventory.json").read_text())["inventory"]
    fz["large_areas"] = params["d3"]["large_areas"]
    fz["r1"] = {}
    for k, meta in params["d1"]["r1_windows"].items():
        z = np.load(path / f"r1_rolling_{k}.npz", allow_pickle=False)
        fz["r1"][int(k)] = dict({n: z[n] for n in z.files}, **meta)
    apath = REFREEZE if prefer_refreeze and (REFREEZE / "audit_flips.csv").exists() else path
    fz["audit_source"] = str(apath.relative_to(STUDY))
    fz["audit_flips"] = pd.read_csv(apath / "audit_flips.csv")
    z = np.load(apath / "audit_did_boot.npz")
    fz["audit_did_boot"] = {n: z[n] for n in z.files}
    return fz


def audit_spec(fz: dict, spec: str) -> tuple[pd.DataFrame, np.ndarray]:
    f = fz["audit_flips"]
    return f[f.spec == spec].reset_index(drop=True), fz["audit_did_boot"][spec]


# ================================================================================================
# 3. Confirmatory tests (pure functions: frame + frozen parameters -> result dict)
# ================================================================================================
def _result(cid, estimate, ci, ci_level, p, min_effect_met, ci_rule_met, contradicted, gate=None, power=None,
            details=None, n=None, scale=""):
    return dict(id=cid, family="primary" if cid in PRIMARY else "secondary", estimate=estimate, ci=ci,
                ci_level=ci_level, scale=scale, p_one_sided=p, min_effect_met=bool(min_effect_met),
                ci_rule_met=bool(ci_rule_met), contradicted=bool(contradicted),
                gate=gate or dict(applies=False, passes=None, rule="none (diachronic or camera-ready-free)"),
                projected_heldout_power=power or {}, n=n, details=details or {})


def ct1_break(df: pd.DataFrame, fz: dict) -> dict:
    """CT1 (D1-H1a): 2024 slope change in NAME, segmented logit on U 2017-26 (D1 specification)."""
    d = df[df.year.between(2017, 2026)]
    res = D1.its_fit(d, "name_primary", B=2024, fe="topic100", controls=("log_authors", "llm_topic"),
                     cluster="topic100")
    t = C.or_table(res, ["post_t", "tc", "post"])
    r = t.loc["post_t"]
    z = float(r.coef / r.se)
    se_ho = _ho_se(r.se)
    power = {}
    for a in (ALPHA / 6, ALPHA):
        thr = max(np.log(1.10), stats.norm.ppf(1 - a) * se_ho)
        power[f"P(confirm) at alpha {a:.4f}"] = float(stats.norm.cdf((r.coef - thr) / se_ho))
    power["z_heldout_projected"] = float(r.coef / se_ho)
    return _result("CT1", float(r.OR), [float(r.OR_lo), float(r.OR_hi)], 0.95, float(stats.norm.sf(z)),
                   r.OR >= 1.10, True, r.OR_hi < 1, power=power, n=int(res.nobs), scale="OR per year",
                   details=dict(log_or=float(r.coef), se=float(r.se), z=z, pre_slope_OR=float(t.loc["tc", "OR"]),
                                level_OR=float(t.loc["post", "OR"]), n_clusters=int(d.topic100.nunique())))


def ct2_acceleration(df: pd.DataFrame, fz: dict, n_boot: int = B_PAPER, seed: int = SEED + 2) -> dict:
    """CT2 (D1-H1c): acceleration of content-unexplained drift with the frozen rolling R1 models."""
    yrs = df.year.to_numpy()
    texts = df.r1_text.to_numpy(dtype=object)
    yv = df.name_primary.to_numpy(float)
    rows, per = [], {}
    for yt in sorted(fz["r1"]):
        m = yrs == yt
        if not m.any():
            continue
        win = fz["r1"][yt]
        Sk = r1_fold_scores(texts[m], win)
        c = float(win["shift"])
        ph = CF.ens_prob(Sk, c)
        per[yt] = dict(Sk=Sk, y=yv[m], oof=np.asarray(win["oof_calib"], float),
                       ycal=np.asarray(win["y_calib"], float), c=c)
        rows.append(dict(year=int(yt), n=int(m.sum()), obs=float(yv[m].mean()), p_hat=float(ph.mean()),
                         obs_calib=float(win["obs_calib"]), shift=c))
    P = pd.DataFrame(rows)
    P["step"] = P.obs - P.obs_calib
    P["content_step"] = P.p_hat - P.obs_calib
    P["unexplained"] = P.obs - P.p_hat
    st = CF.rolling_stats(P, pre=U_PRE, post=POST)
    rng = np.random.default_rng(seed)
    dr = {yt: dict(obs=[], phat=[], anc=[]) for yt in per}
    for start in range(0, n_boot, 250):
        b = min(250, n_boot - start)
        for yt, d in per.items():
            nc, nt = len(d["oof"]), len(d["y"])
            Wc = rng.multinomial(nc, np.full(nc, 1 / nc), size=b).astype(float)
            tgt = (Wc @ d["ycal"]) / Wc.sum(1)
            cb = CF.shift_batch(d["oof"], Wc, tgt, d["c"])
            Wt = rng.multinomial(nt, np.full(nt, 1 / nt), size=b).astype(float)
            Pt = CF.ens_prob(d["Sk"], cb)
            ws = Wt.sum(1)
            dr[yt]["obs"].append((Wt @ d["y"]) / ws)
            dr[yt]["phat"].append((Wt * Pt).sum(1) / ws)
            dr[yt]["anc"].append(tgt)
    dr = {yt: {k: np.concatenate(v) for k, v in d.items()} for yt, d in dr.items()}
    pre = [y for y in U_PRE if y in dr]
    post = [y for y in POST if y in dr]
    u = {yt: d["obs"] - d["phat"] for yt, d in dr.items()}
    up, uq = np.mean([u[y] for y in pre], 0), np.mean([u[y] for y in post], 0)
    diff = uq - up
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio_b = uq / up
        share_b = np.sum([dr[y]["phat"] - dr[y]["anc"] for y in post], 0) / \
            np.sum([dr[y]["obs"] - dr[y]["anc"] for y in post], 0)
    diff_ci, share_ci, ratio_ci = q(diff), q(share_b), q(ratio_b)
    ratio = st["ratio"] if st["u_pre"] > 0 else (np.inf if st["diff"] > 0 else np.nan)
    sd = float(np.std(diff, ddof=1))
    sd_sh = float(np.std(share_b[np.isfinite(share_b)], ddof=1))
    power = dict(z_heldout_projected=float(st["diff"] / _ho_se(sd)), **z_power(st["diff"] / _ho_se(sd)),
                 P_share_upper95_below_0p60=float(stats.norm.cdf((0.60 - st["content_share_post_steps"])
                                                                 / _ho_se(sd_sh) - 1.96)))
    ci_rule = bool(diff_ci[0] > 0 and share_ci[1] < 0.60)
    return _result("CT2", 100 * st["diff"], [100 * diff_ci[0], 100 * diff_ci[1]], 0.95,
                   boot_p(diff, lambda d: d <= 0), ratio >= 1.5, ci_rule, diff_ci[1] < 0, power=power,
                   n=int(P.n.sum()), scale="pp/yr (mean u 2024-26 minus mean u 2019-23)",
                   details=dict(u_pre_pp=100 * st["u_pre"], u_post_pp=100 * st["u_post"], ratio=ratio,
                                ratio_ci=ratio_ci, content_share_post_steps=st["content_share_post_steps"],
                                content_share_ci=share_ci, diff_se_pp=100 * sd,
                                per_year=P.round(6).to_dict(orient="records"),
                                bootstrap="held-out papers resampled within year; discovery calibration-year "
                                          "papers resampled independently and the shift re-solved"))


def d2_rho(papers: pd.DataFrame, prof: pd.DataFrame, l_split: str | None = None, n_boot: int = B_KEY,
           seed: int = D2_SEED) -> dict:
    """Within-stayer shares rho = (P_SL - P_SE)/(P_L - P_E) for the last and first list positions with a joint
    key-cluster bootstrap (D2 engine). E = 2022-23 papers of `papers` (union); L = 2025-26 papers, restricted to
    split == l_split when given (held-out run: 'heldout'). Stayers: keys with any-role rows in both sets."""
    pp = papers[["submission_id", "year", "name_primary"] + (["split"] if "split" in papers else [])]
    e_ids = set(pp.loc[pp.year.isin(E_WIN), "submission_id"])
    lm = pp.year.isin(L_WIN)
    if l_split is not None:
        lm &= pp.split.eq(l_split)
    l_ids = set(pp.loc[lm, "submission_id"])
    idx = pd.Index(sorted(prof.key.unique()))
    pr = prof.assign(key_code=idx.get_indexer(prof.key))
    pr = pr[pr.submission_id.isin(e_ids | l_ids)]
    K = len(idx)
    inE = set(pr.loc[pr.submission_id.isin(e_ids), "key_code"])
    inL = set(pr.loc[pr.submission_id.isin(l_ids), "key_code"])
    g = pd.DataFrame(index=np.arange(K))
    g["S"] = g.index.isin(inE & inL)
    g["X"] = g.index.isin(inE) & ~g.S
    g["N"] = g.index.isin(inL) & ~g.S
    g["R"] = False
    specs = []
    for part, flag in [("last", "is_last"), ("first", "is_first")]:
        r = pr[pr[flag]].merge(pp[["submission_id", "name_primary"]], on="submission_id", how="inner")
        r = r.dropna(subset=["name_primary"])
        r["period"] = np.where(r.submission_id.isin(e_ids), "E", "L")
        r["w"] = 1.0
        specs.append(P2.Spec(name=part, rows=r, weight="w", outcomes=["name_primary"], groups=g))
    res = P2.run_specs(specs, K, n_boot=n_boot, seed=seed, chunk=50)
    out = {}
    for part in ("last", "first"):
        pt = res[part]["point"]["name_primary"]
        bt = res[part]["boot"]["name_primary"] if n_boot else {}
        out[part] = dict(point={k: float(v[0]) for k, v in pt.items() if k in (
            "rho", "delta", "delta_S", "P_E", "P_L", "P_SE", "P_SL", "s_E", "s_L")},
            rho_boot=bt.get("rho"), counts=res[part]["counts"])
    out["n_stayer_keys"] = int(g.S.sum())
    out["n_keys_E"], out["n_keys_L"] = len(inE), len(inL)
    out["n_papers_E"], out["n_papers_L"] = len(e_ids), len(l_ids)
    return out


def ct3_communal(papers: pd.DataFrame, prof: pd.DataFrame, fz: dict, l_split: str | None = None,
                 n_boot: int = B_KEY, rho: dict | None = None) -> dict:
    """CT3 (D2-H2a): last-list-position within-stayer share, lower 95% bound > 0.5."""
    rho = rho or d2_rho(papers, prof, l_split, n_boot)
    est = rho["last"]["point"]["rho"]
    b = rho["last"]["rho_boot"]
    ci = q(b)
    sd = float(np.nanstd(b, ddof=1))
    zp = (est - 0.5) / _ho_se(sd)
    return _result("CT3", est, ci, 0.95, boot_p(b, lambda d: d <= 0.5), est > 0.5, ci[0] > 0.5, ci[1] < 0.5,
                   power=dict(z_heldout_projected=float(zp), **z_power(zp),
                              note="E side is the discovery-held-out union, so the held-out SE is smaller than "
                                   "2 x the discovery SE; this projection is conservative"),
                   n=rho["n_stayer_keys"], scale="rho_last",
                   details=dict(point=rho["last"]["point"], counts=rho["last"]["counts"],
                                n_keys_E=rho["n_keys_E"], n_keys_L=rho["n_keys_L"], n_papers_E=rho["n_papers_E"],
                                n_papers_L=rho["n_papers_L"], boot_sd=sd))


def ct12_role_gradient(papers: pd.DataFrame, prof: pd.DataFrame, fz: dict, l_split: str | None = None,
                       n_boot: int = B_KEY, rho: dict | None = None) -> dict:
    """CT12 (D2-H2b): first-position minus last-position within-stayer share < 0 (joint key bootstrap)."""
    rho = rho or d2_rho(papers, prof, l_split, n_boot)
    est = rho["first"]["point"]["rho"] - rho["last"]["point"]["rho"]
    b = rho["first"]["rho_boot"] - rho["last"]["rho_boot"]
    ci = q(b)
    sd = float(np.nanstd(b, ddof=1))
    zp = -est / _ho_se(sd)
    return _result("CT12", est, ci, 0.95, boot_p(b, lambda d: d >= 0), est < 0, ci[1] < 0, ci[0] > 0,
                   power=dict(z_heldout_projected=float(zp), **z_power(zp)), n=rho["n_stayer_keys"],
                   scale="rho_first - rho_last",
                   details=dict(rho_first=rho["first"]["point"]["rho"], rho_first_ci=q(rho["first"]["rho_boot"]),
                                rho_last=rho["last"]["point"]["rho"], first_point=rho["first"]["point"],
                                first_counts=rho["first"]["counts"], boot_sd=sd))


def ct4_slots(df: pd.DataFrame, fz: dict) -> dict:
    """CT4 (D3-H3a): stacked slot + control logit, post x LLM-slot interaction (D3 STACKED, 2018+)."""
    P = D3.slot_panel(df, fz["slot_inventory"], rule="primary", sense=True, controls=True, years_from=2018)
    res = C.logit(D3.STACKED, P, cluster="topic100")
    r = C.or_table(res, ["post:llm_slot"]).iloc[0]
    z = float(r.coef / r.se)
    se_ho = _ho_se(r.se)
    power = {f"P(confirm) at alpha {a:.4f}": float(stats.norm.cdf(
        (r.coef - max(np.log(1.5), stats.norm.ppf(1 - a) * se_ho)) / se_ho)) for a in (ALPHA / 6, ALPHA)}
    power["z_heldout_projected"] = float(r.coef / se_ho)
    sl = P[P.llm_slot == 1]
    return _result("CT4", float(r.OR), [float(r.OR_lo), float(r.OR_hi)], 0.95, float(stats.norm.sf(z)),
                   r.OR >= 1.5, True, r.OR_hi < 1, power=power, n=int(res.nobs), scale="OR (slot minus control)",
                   details=dict(log_or=float(r.coef), se=float(r.se), z=z, n_slot_titles=int(len(sl)),
                                n_control_titles=int((P.llm_slot == 0).sum()),
                                slot_share_pre=float(sl.loc[sl.post == 0, "y"].mean()),
                                slot_share_post=float(sl.loc[sl.post == 1, "y"].mean())))


def _d4(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df.year >= 2018) & (df.pool != "OTHER")].reset_index(drop=True)


def _pooled_stage_prev(df: pd.DataFrame, col: str, n_boot: int, seed: int = S4.SEED) -> dict:
    sums = S4.stage_sums(_d4(df), [col], STAGE_COLS, n_boot=n_boot, seed=seed)
    P = S4.pooled_prev(sums, POST, "std")[:, 0, :]
    ix = {s: i for i, s in enumerate(STAGE_COLS)}
    with np.errstate(divide="ignore", invalid="ignore"):
        return dict(total=P[:, ix["s3"]] / P[:, ix["s0"]], predec=P[:, ix["s2"]] / P[:, ix["s0"]],
                    dec=P[:, ix["s3"]] / P[:, ix["s2"]], predec_crf=P[:, ix["s2n"]] / P[:, ix["s0n"]],
                    desk=P[:, ix["s1"]] / P[:, ix["s0"]], exit=P[:, ix["s2"]] / P[:, ix["s1"]],
                    prev={s: float(P[0, i]) for s, i in ix.items()})


def _gate_tipping(df: pd.DataFrame, fz: dict, spec: str, keys_audit: list[str], n_boot: int) -> pd.DataFrame:
    """WP4 tipping/editing-corrected table for audit `spec` with stage prevalences from `df` (2023+, 2024-26
    pooled). Uses snapshot_bounds.tipping_table unchanged."""
    flips, did_b = audit_spec(fz, spec)
    keys = list(flips.feature)
    assert keys == keys_audit, "audit flip order differs from the snapshot feature list"
    u = SB.derive(df[(df.year >= 2023) & (df.pool != "OTHER")].reset_index(drop=True))
    u["L_title_words"] = u.r24_any.astype(bool) | u.r26_any.astype(bool)          # WP4 audited L-title
    u["O_union_arxiv"] = u.case_sentence_case.astype(bool) | u.question_opener.astype(bool)
    sums = SB.stage_prevalences(u, keys, n_boot=n_boot, seed=SB.SEED)
    Pp, ap = SB.pooled(sums, POST)
    # snapshot_final.tipping = snapshot_bounds.tipping_table + identification p-values (tipping-point SE)
    return SF.tipping(Pp, ap, keys, flips, did_b, "2024-26").set_index("feature")


def ct5_neutrality(df: pd.DataFrame, fz: dict, n_boot: int = B_PAPER) -> dict:
    """CT5 (D4-H4a): pooled 2024-26 NAME G_total TOST within [0.90, 1.11]; gated by the editing-corrected CI."""
    g = _pooled_stage_prev(df, "name_primary", n_boot)
    G = g["total"]
    lo90, hi90 = q(G[1:], 0.05, 0.95)
    lo95, hi95 = q(G[1:])
    p = max(boot_p(G[1:], lambda d: d <= TOST_MARGIN[0]), boot_p(G[1:], lambda d: d >= TOST_MARGIN[1]))
    tp = _gate_tipping(df, fz, GATE_SPEC_TITLE, SF.KEYS_T, n_boot).loc["NAME"]
    passes = bool(TOST_MARGIN[0] <= tp.G_total_corr_lo90 and tp.G_total_corr_hi90 <= TOST_MARGIN[1])
    gate = dict(applies=True, kind="equivalence", passes=passes, audit_spec=GATE_SPEC_TITLE,
                audit_source=fz["audit_source"],
                rule="editing-corrected 90% CI of G_total (held-out bootstrap x audit net-flip DiD draws, WP4 G1 "
                     "construction) inside [0.90, 1.11]",
                corrected_ci90=[float(tp.G_total_corr_lo90), float(tp.G_total_corr_hi90)],
                audit_interval=[float(tp.G_total_audit_lo), float(tp.G_total_audit_hi)],
                tipping_total_pp=float(tp.tip_total_pp), audit_did_pp=float(tp.did_pp),
                audit_did_ci_pp=[float(tp.did_lo_pp), float(tp.did_hi_pp)], auditable=bool(tp.auditable))
    sd = float(np.std(G[1:], ddof=1))
    se_ho = _ho_se(sd)
    pw = float(max(0.0, stats.norm.cdf((TOST_MARGIN[1] - G[0]) / se_ho - 1.645)
                   + stats.norm.cdf((G[0] - TOST_MARGIN[0]) / se_ho - 1.645) - 1))
    inside = bool(TOST_MARGIN[0] <= lo90 and hi90 <= TOST_MARGIN[1])
    return _result("CT5", float(G[0]), [lo90, hi90], 0.90, p, inside, inside,
                   (lo90 > TOST_MARGIN[1]) or (hi90 < TOST_MARGIN[0]), gate=gate,
                   power={"P(90% CI inside margin), approx": pw, "heldout_se_projected": se_ho},
                   n=int(_d4(df).year.isin(POST).sum()), scale="G_total (accepted/all)",
                   details=dict(ci95=[lo95, hi95], G_desk=float(g["desk"][0]), G_exit=float(g["exit"][0]),
                                G_dec=float(g["dec"][0]), prevalence_by_stage=g["prev"], boot_sd=sd))


def ct6_depletion(df: pd.DataFrame, fz: dict, n_boot: int = B_PAPER) -> dict:
    """CT6 (D4-H4b): L-union pooled 2024-26 G_total < 1 and G_desk x G_exit < 1 (both, one-sided)."""
    g = _pooled_stage_prev(df, "L_union", n_boot)
    Gt, Gp = g["total"], g["predec"]
    p_t, p_p = boot_p(Gt[1:], lambda d: d >= 1), boot_p(Gp[1:], lambda d: d >= 1)
    ci_t, ci_p = q(Gt[1:]), q(Gp[1:])
    # gate: L-union is not auditable (its abstract em dash and title typography cannot be measured on arXiv v1);
    # the auditable sub-unions are reported for information only
    info = {}
    try:
        tt = _gate_tipping(df, fz, GATE_SPEC_TITLE, SF.KEYS_T, n_boot)
        ta = _gate_tipping(df, fz, GATE_SPEC_ABS, SF.KEYS_A, n_boot)
        for nm, r in [("L_title", tt.loc["L_title"]), ("L_title_words (R24|R26)", tt.loc["L_title_words"]),
                      ("L_abstract", ta.loc["L_abstract"]), ("L_abs_words (F24|F26 words)", ta.loc["L_abs_words"])]:
            info[nm] = dict(auditable=bool(r.auditable), G_total=float(r.G_total_obs), tip_total_pp=float(r.tip_total_pp),
                            audit_did_ci_pp=[float(r.did_lo_pp), float(r.did_hi_pp)],
                            identified_uncorrected=bool(r.G_total_identified),
                            p_ident_total=float(r.p_ident_total),
                            corrected_ci95=[float(r.G_total_corr_lo95), float(r.G_total_corr_hi95)])
    except Exception as e:  # noqa: BLE001
        info["error"] = str(e)[:200]
    gate = dict(applies=True, kind="association", passes=False, component="G_total", auditable=False,
                corrected_ci_beyond=None, p_ident=None,
                rule="L-union G_total is an acceptance-margin association: confirmation needs the L-union to be "
                     "auditable (>= 10 v1-present pairs in both arms and measurable through arXiv), its "
                     "editing-corrected 95% interval below 1, and its identification p to survive Holm at 0.025 "
                     "across the run's auditable association claims (WP4 gate). The L-union contains title "
                     "typography and the abstract em dash, which arXiv metadata cannot carry (0 of ~3,600 arXiv "
                     "titles typographic; 0 of 1,709 v1 abstracts with an em dash), so the L-union is unauditable "
                     "and this gate cannot pass (fixed before held-out access). The auditable proxies (R24|R26 "
                     "title words, F24|F26 abstract words) are reported for information only.",
                auditable_subunions_info=info)
    sd_t, sd_p = float(np.std(Gt[1:], ddof=1)), float(np.std(Gp[1:], ddof=1))
    zt, zp = (1 - Gt[0]) / _ho_se(sd_t), (1 - Gp[0]) / _ho_se(sd_p)
    pw = {k: z_power(zt)[k] * z_power(zp)[k] for k in z_power(0)}
    return _result("CT6", dict(G_total=float(Gt[0]), G_desk_x_exit=float(Gp[0])),
                   dict(G_total=ci_t, G_desk_x_exit=ci_p), 0.95, max(p_t, p_p), bool(Gt[0] < 1 and Gp[0] < 1),
                   True, bool(ci_t[0] > 1 or ci_p[0] > 1), gate=gate,
                   power=dict(z_heldout_projected=dict(G_total=float(zt), G_desk_x_exit=float(zp)), **pw),
                   n=int(_d4(df).year.isin(POST).sum()), scale="gains (L-union)",
                   details=dict(p_G_total=p_t, p_G_desk_x_exit=p_p,
                                G_desk_x_exit_camera_ready_free=float(g["predec_crf"][0]),
                                G_desk_x_exit_camera_ready_free_ci=q(g["predec_crf"][1:]),
                                G_dec=float(g["dec"][0]), prevalence_by_stage=g["prev"],
                                audit_free_component_one_sided_p=p_p))


def ct7_vintage(df: pd.DataFrame, fz: dict) -> dict:
    """CT7 (D3-H3c): OR(F24 -> R24 in title) / OR(F26 -> R24 in title) > 1 in 2025-26."""
    d = df[df.year.isin([2025, 2026])].copy()
    r = D3V.fit(d, "r24_any", "f24", "f26", "CT7")
    se_ho = _ho_se(r["se_log_ratio"])
    zp = r["log_ratio"] / se_ho
    return _result("CT7", float(r["ratio"]), [float(r["ratio_lo"]), float(r["ratio_hi"])], 0.95, float(r["p_one"]),
                   r["ratio"] > 1, True, r["ratio_hi"] < 1, power=dict(z_heldout_projected=float(zp), **z_power(zp)),
                   n=int(r["nobs"]), scale="OR ratio",
                   details={k: r[k] for k in ("OR_a", "OR_a_lo", "OR_a_hi", "OR_b", "OR_b_lo", "OR_b_hi", "log_ratio",
                                              "se_log_ratio", "n_y", "n_xa", "n_xb")})


def ct8_turnover(df: pd.DataFrame, fz: dict) -> dict:
    """CT8 (D3-H3b): 2026 vs 2025 within-area R24 down and R26 up (two one-sided tests, frozen large areas)."""
    d = df[df.year.isin([2025, 2026])]
    R = D3R.rates(d, "area_h", ["r24_any", "r26_any"])
    big = [a for a in fz["large_areas"] if ((R.area == a) & (R.year == 2025)).any() and
           ((R.area == a) & (R.year == 2026)).any()]
    comp = {}
    for fam, direction in [("r24_any", "down"), ("r26_any", "up")]:
        pc = D3R.poisson_cells(R, fam, (2025, 2026), areas=big)
        rr, lo, hi = pc["RR_2026_vs_2025"], pc["RR_2026_vs_2025_lo"], pc["RR_2026_vs_2025_hi"]
        b, se = np.log(rr), (np.log(hi) - np.log(lo)) / (2 * 1.959963984540054)
        p = stats.norm.cdf(b / se) if direction == "down" else stats.norm.sf(b / se)
        at = D3R.area_tests(R, big, fam)
        comp[fam] = dict(RR=float(rr), RR_ci=[float(lo), float(hi)], p_one=float(p), dispersion=pc["dispersion"],
                         log_rr=float(b), se=float(se), direction=direction,
                         n_areas_predicted_direction=int(at[direction].sum()), n_areas=int(len(at)),
                         rate_2025_per_1k=float(1000 * at.k_2025.sum() / at.n_2025.sum()),
                         rate_2026_per_1k=float(1000 * at.k_2026.sum() / at.n_2026.sum()))
    a, b_ = comp["r24_any"], comp["r26_any"]
    zs = (-a["log_rr"] / _ho_se(a["se"]), b_["log_rr"] / _ho_se(b_["se"]))
    pw = {k: z_power(zs[0])[k] * z_power(zs[1])[k] for k in z_power(0)}
    return _result("CT8", dict(RR_R24=a["RR"], RR_R26=b_["RR"]), dict(RR_R24=a["RR_ci"], RR_R26=b_["RR_ci"]), 0.95,
                   max(a["p_one"], b_["p_one"]), a["RR"] < 1 and b_["RR"] > 1, True,
                   a["RR_ci"][0] > 1 or b_["RR_ci"][1] < 1,
                   power=dict(z_heldout_projected=dict(R24=float(zs[0]), R26=float(zs[1])), **pw),
                   n=int(d.area_h.isin(big).sum()), scale="rate ratio 2026/2025",
                   details=dict(components=comp, n_large_areas_used=len(big)))


def ct9_tool(df: pd.DataFrame, fz: dict, n_boot: int = B_PAPER, seed: int = 3) -> dict:
    """CT9 (D1-H1e(i)): F=0 NAME rise / total rise, 2023 -> 2026 (F = f24_2 | f26 | title_typo), lower bound > 0.70.
    Draws replicate D1's f0_rise (one generator over target years 2024, 2025, 2026)."""
    rng = np.random.default_rng(seed)
    out = {}
    a = df[df.year == 2023]
    ya, fa = a.name_primary.to_numpy(float), a.F_d1.to_numpy() == 0
    for t in POST:
        bdf = df[df.year == t]
        yb, fb = bdf.name_primary.to_numpy(float), bdf.F_d1.to_numpy() == 0

        def stat(wa, wb):
            all_ = (wb @ yb) / wb.sum(-1) - (wa @ ya) / wa.sum(-1)
            f0 = (wb[..., fb] @ yb[fb]) / wb[..., fb].sum(-1) - (wa[..., fa] @ ya[fa]) / wa[..., fa].sum(-1)
            return all_, f0
        all_, f0 = stat(np.ones(len(ya)), np.ones(len(yb)))
        bs = []
        for start in range(0, n_boot, 500):
            k = min(500, n_boot - start)
            wa = rng.multinomial(len(ya), np.full(len(ya), 1 / len(ya)), size=k).astype(float)
            wb = rng.multinomial(len(yb), np.full(len(yb), 1 / len(yb)), size=k).astype(float)
            r = stat(wa, wb)
            bs.append(r[1] / r[0])
        out[t] = dict(ratio=float(f0 / all_), rise_all_pp=float(100 * all_), rise_F0_pp=float(100 * f0),
                      share_F=float(1 - fb.mean()), draws=np.concatenate(bs))
    o = out[2026]
    ci = q(o["draws"])
    sd = float(np.std(o["draws"], ddof=1))
    zp = (o["ratio"] - 0.70) / _ho_se(sd)
    return _result("CT9", o["ratio"], ci, 0.95, boot_p(o["draws"], lambda d: d <= 0.70), o["ratio"] > 0.70,
                   ci[0] > 0.70, ci[1] < 0.70, power=dict(z_heldout_projected=float(zp), **z_power(zp)),
                   n=int(((df.year == 2023) | (df.year == 2026)).sum()), scale="F=0 rise / total rise (2023->2026)",
                   details=dict(rise_all_pp=o["rise_all_pp"], rise_F0_pp=o["rise_F0_pp"], share_F_2026=o["share_F"],
                                share_F_2023=float(1 - fa.mean()),
                                by_target={int(t): dict(ratio=v["ratio"], ci=q(v["draws"])) for t, v in out.items()}))


def ct10_kobak(df: pd.DataFrame, fz: dict, n_boot: int = B_PAPER, seed: int = S4.SEED + 1) -> dict:
    """CT10 (D4-H4c): Kobak-style F24 bound, accepted-only / all submissions, mean over 2024-26 < 0.90."""
    d = _d4(df)
    d = d[d.year >= 2021]
    sums = S4.stage_sums(d, ["f24"], ["s0", "s3"], n_boot=n_boot, seed=seed)
    Pd = {y: sums[y][0] / sums[y][1][:, None, :] for y in sums}
    Bd = {Y: DBA.kobak_from_prev(Pd, Y, "cons")[:, 0, :] for Y in POST}
    mb = np.mean([Bd[Y] for Y in POST], axis=0)
    ratio = mb[:, 1] / mb[:, 0]
    ci = q(ratio[1:])
    b0, b3 = float(mb[0, 0]), float(mb[0, 1])
    a0_all = np.mean([sums[Y][1][:, 1] / sums[Y][1][:, 0] for Y in POST], axis=0)   # (B+1,)
    a0 = float(a0_all[0])
    dstar_all = (mb[:, 1] - 0.9 * mb[:, 0]) / (1 - 0.9 * a0_all)
    dstar = float(dstar_all[0])
    se_dstar = float(np.nanstd(dstar_all[1:], ddof=1))
    fa, _ = audit_spec(fz, GATE_SPEC_ABS)
    f24 = fa.set_index("feature").loc["F24"]
    D, se_D = float(f24.did), float(f24.did_se)
    # identification (WP4): H0 'true net camera-ready change D <= D*' (editing large enough to explain ratio < 0.90)
    z_id = (D - dstar) / np.sqrt(se_D ** 2 + se_dstar ** 2)
    p_id = float(stats.norm.sf(z_id))
    # editing-corrected ratio: bootstrap replicate b paired with an audit draw D_b ~ N(D_hat, se_D) (fixed seed)
    rng_g = np.random.default_rng(SEED + 10)
    Db = rng_g.normal(D, se_D, len(mb) - 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        rc = (mb[1:, 1] - Db) / (mb[1:, 0] - a0_all[1:] * Db)
    rc_hi = float(np.nanquantile(rc, 0.975))
    gate = dict(applies=True, kind="association", passes=None, audit_spec=GATE_SPEC_ABS,
                audit_source=fz["audit_source"],
                rule="tipping point D* = (b_acc - 0.9 b_all)/(1 - 0.9 a0) (net camera-ready change in accepted F24 "
                     "prevalence, 2024-26, that would lift the ratio to 0.90). WP4 gate: passes if the F24 abstract "
                     "audit is auditable, the editing-corrected ratio's upper 95% bound (bootstrap replicate paired "
                     "with an audit draw) is < 0.90, and the identification p, z = (D_hat - D*)/sqrt(se_D^2 + "
                     "se_D*^2), survives Holm at one-sided 0.025 across the run's auditable association claims",
                tipping_pp=100 * dstar, tipping_se_pp=100 * se_dstar, audit_did_pp=100 * D, audit_did_se_pp=100 * se_D,
                audit_did_ci_pp=[100 * float(f24.did_lo), 100 * float(f24.did_hi)], auditable=bool(f24.auditable),
                z_ident=float(z_id), p_ident=p_id, corrected_ratio_hi95=rc_hi,
                corrected_ci_beyond=bool(rc_hi < 0.90),
                passes_uncorrected_rule=bool(f24.auditable and dstar < 0 and f24.did_lo > dstar),
                accepted_share_s0=a0)
    sd = float(np.std(ratio[1:], ddof=1))
    zp = (0.90 - ratio[0]) / _ho_se(sd)
    return _result("CT10", float(ratio[0]), ci, 0.95, boot_p(ratio[1:], lambda x: x >= 0.90), ratio[0] < 0.90, True,
                   ci[0] > 0.90, gate=gate, power=dict(z_heldout_projected=float(zp), **z_power(zp)),
                   n=int(len(d)), scale="bound ratio accepted/all",
                   details=dict(bound_all_pp=100 * b0, bound_acc_pp=100 * b3,
                                by_year={int(Y): dict(all_pp=100 * float(Bd[Y][0, 0]), acc_pp=100 * float(Bd[Y][0, 1]),
                                                      ratio=float(Bd[Y][0, 1] / Bd[Y][0, 0])) for Y in POST}))


def ct11_invariance(df: pd.DataFrame, fz: dict) -> dict:
    """CT11 (D4-H4a(iii)): pool-specific (ACC, REJ, WD) 2024 slope-change log ORs equivalent within +/-0.1."""
    d = _d4(df)
    rows, test = S4.its_pools(d, "name_primary", pools=("ACC", "REJ", "WD"), years=tuple(range(2018, 2027)),
                              label="CT11")
    pairs = test["pairs"]
    p = max(pr["tost_p"] for pr in pairs)
    equiv = all(pr["equivalent_0p1"] for pr in pairs)
    contra = any(pr["lo90"] > 0.1 or pr["hi90"] < -0.1 for pr in pairs)
    fl, _ = audit_spec(fz, GATE_SPEC_TITLE)
    nm = fl.set_index("feature").loc["NAME"]
    pacc = float(d.loc[d.ACC.eq(1) & d.year.isin(POST), "name_primary"].mean())
    bmax = float((nm.did_hi - nm.did_lo) / (2 * pacc * (1 - pacc)))
    widened = [dict(a=pr["a"], b=pr["b"], lo90=pr["lo90"] - bmax, hi90=pr["hi90"] + bmax) for pr in pairs
               if "ACC" in (pr["a"], pr["b"])]
    passes = all(w["lo90"] > -0.1 and w["hi90"] < 0.1 for w in widened)
    gate = dict(applies=True, kind="equivalence", passes=bool(passes), audit_spec=GATE_SPEC_TITLE,
                audit_source=fz["audit_source"],
                rule="ACC-pool pairs (camera-ready titles): widen each pairwise 90% CI by b_max = (D_hi - D_lo) / "
                     "(2 p(1-p)), the largest slope-change bias that post-year editing inside the NAME audit's 95% "
                     "net-flip CI [D_lo, D_hi] could create (p = ACC NAME share 2024-26); passes if every widened "
                     "ACC-pair CI lies inside (-0.1, 0.1). The REJ-WD pair is audit-free.",
                b_max_logOR=bmax, acc_name_share_post=pacc,
                audit_did_ci_pp=[100 * float(nm.did_lo), 100 * float(nm.did_hi)], widened_acc_pairs=widened)
    ses = [pr["se"] for pr in pairs]
    pw_pairs = [float(max(0.0, 2 * stats.norm.cdf((0.1 - abs(pr["dlogOR"])) / _ho_se(pr["se"]) - 1.645) - 1))
                for pr in pairs]
    return _result("CT11", {f"{pr['a']}-{pr['b']}": pr["dlogOR"] for pr in pairs},
                   {f"{pr['a']}-{pr['b']}": [pr["lo90"], pr["hi90"]] for pr in pairs}, 0.90, float(p), equiv, equiv,
                   contra, gate=gate,
                   power={"P(pair equivalent), approx, per pair": pw_pairs, "heldout_se_projected": [_ho_se(s) for s in ses]},
                   n=int(sum(r["nobs"] for r in rows)), scale="difference in slope-change log OR",
                   details=dict(pools={r["pool"]: dict(OR=r["slope_change_OR"], ci=[r["slope_change_OR_lo"],
                                                                                     r["slope_change_OR_hi"]],
                                                       nobs=r["nobs"]) for r in rows},
                                wald_equality_p=test["p"], pairs=pairs))


# ================================================================================================
# 4. Decision layer
# ================================================================================================
def holm(p: dict) -> dict:
    keys = sorted(p, key=lambda k: p[k])
    m, run, out = len(keys), 0.0, {}
    for i, k in enumerate(keys):
        run = max(run, min(1.0, (m - i) * p[k]))
        out[k] = run
    return out


def bh(p: dict) -> dict:
    keys = sorted(p, key=lambda k: p[k])
    m = len(keys)
    out, run = {}, 1.0
    for i in range(m - 1, -1, -1):
        k = keys[i]
        run = min(run, p[k] * m / (i + 1))
        out[k] = min(1.0, run)
    return out


def decide(res: dict) -> dict:
    """Holm over CT1-CT6, BH over CT7-CT12, then the PLAN verdicts with the audit gate."""
    padj = {**holm({k: res[k]["p_one_sided"] for k in PRIMARY if k in res}),
            **bh({k: res[k]["p_one_sided"] for k in SECONDARY if k in res})}
    # WP4 multiplicity-controlled gate for acceptance-margin ASSOCIATION claims (revision 2): Holm over the run's
    # auditable association claims of the identification p-values, one-sided alpha 0.025
    assoc = {k: r["gate"] for k, r in res.items() if r["gate"].get("kind") == "association"}
    fam = {k: float(g["p_ident"]) for k, g in assoc.items() if g.get("auditable") and g.get("p_ident") is not None}
    gadj = holm(fam) if fam else {}
    for k, g in assoc.items():
        g["holm_family"] = sorted(fam)
        g["p_ident_holm"] = gadj.get(k)
        g["passes"] = bool(g.get("auditable") and g.get("corrected_ci_beyond") and
                           gadj.get(k, 1.0) < GATE_ALPHA1)
    for k, r in res.items():
        r["p_adjusted"] = padj.get(k)
        r["adjustment"] = "Holm (CT1-CT6)" if k in PRIMARY else "BH (CT7-CT12)"
        reasons = []
        if not (r["p_adjusted"] is not None and r["p_adjusted"] < ALPHA):
            reasons.append("adjusted p >= .05")
        if not r["min_effect_met"]:
            reasons.append("point estimate not beyond the minimal effect")
        if not r["ci_rule_met"]:
            reasons.append("CI rule not met")
        g = r["gate"]
        gate_ok = (not g.get("applies")) or bool(g.get("passes"))
        if not gate_ok:
            reasons.append("audit gate not passed")
        if not reasons:
            v = "confirmed"
        elif r["contradicted"]:
            v = "contradicted"
        else:
            v = "not confirmed"
        r["verdict"] = v
        r["verdict_reasons"] = reasons
        r["statistical_part_met"] = bool(not [x for x in reasons if x != "audit gate not passed"])
    return res


def run_all(df: pd.DataFrame, papers: pd.DataFrame, prof: pd.DataFrame, fz: dict, l_split: str | None = None,
            n_boot: int = B_PAPER, n_key: int = B_KEY) -> dict:
    out = {}
    t0 = time.time()

    def go(cid, f, *a, **kw):
        t = time.time()
        out[cid] = f(*a, **kw)
        out[cid]["seconds"] = round(time.time() - t, 1)
        r = out[cid]
        log(f"  {cid}: est={json.dumps(clean(r['estimate']))} ci={json.dumps(clean(r['ci']))} "
            f"p1={r['p_one_sided']:.4g} ({r['seconds']}s)")
    go("CT1", ct1_break, df, fz)
    go("CT2", ct2_acceleration, df, fz, n_boot)
    rho = d2_rho(papers, prof, l_split, n_key)
    go("CT3", ct3_communal, papers, prof, fz, l_split, n_key, rho=rho)
    go("CT4", ct4_slots, df, fz)
    go("CT5", ct5_neutrality, df, fz, n_boot)
    go("CT6", ct6_depletion, df, fz, n_boot)
    go("CT7", ct7_vintage, df, fz)
    go("CT8", ct8_turnover, df, fz)
    go("CT9", ct9_tool, df, fz, n_boot)
    go("CT10", ct10_kobak, df, fz, n_boot)
    go("CT11", ct11_invariance, df, fz)
    go("CT12", ct12_role_gradient, papers, prof, fz, l_split, n_key, rho=rho)
    log(f"  all tests {time.time() - t0:.0f}s")
    return decide(out)


# ================================================================================================
# 5. Rules (single source for rules.json and prereg.md)
# ================================================================================================
TESTS = {
    "CT1": dict(
        title="D1 break (H1a)", data="held-out U, 2017-2026",
        statistic="Segmented logit NAME ~ (t-2023) + post + post x (t-2023) + log(#authors) + llm_topic + topic100 FE, "
                  "SEs clustered by topic100 (d1_its.its_fit). Parameter: slope change delta = post x (t-2023), "
                  "reported as OR per year.",
        p="one-sided Wald z of delta <= 0", confirm="Holm-adjusted p < .05 and OR >= 1.10",
        contradict="upper 95% CI bound of the OR < 1", gate="none (diachronic)"),
    "CT2": dict(
        title="D1 acceleration of unexplained drift (H1c)", data="held-out U, 2019-2026",
        statistic="Each held-out year y is scored by the frozen rolling R1 models (trained on discovery y-3..y-1; "
                  "five fold models; prediction = mean_k expit(s_k + c_y)); the frozen shift c_y makes the "
                  "discovery cross-fitted predictions of y-1 match discovery obs_{y-1}. u_y = obs_y - p_hat_y. "
                  "D = mean(u_2024-26) - mean(u_2019-23); ratio = mean(u_post)/mean(u_pre); content share of the "
                  "2024-26 steps = sum(p_hat_y - obs^disc_{y-1}) / sum(obs_y - obs^disc_{y-1}).",
        p="bootstrap (B = 2,000): held-out papers resampled within year, discovery calibration-year papers "
          "resampled independently and c_y re-solved; p = (1 + #{D_b <= 0})/(B + 1)",
        confirm="Holm-adjusted p < .05, lower 95% bound of D > 0, ratio >= 1.5, and upper 95% bound of the content "
                "share < 0.60",
        contradict="upper 95% bound of D < 0", gate="none (diachronic)"),
    "CT3": dict(
        title="D2 communal change at the last list position (H2a)",
        data="declared profile keys, panel 2021-26; E = 2022-23 papers of discovery ∪ held-out; L = 2025-26 "
             "held-out papers",
        statistic="Stayers: keys with >= 1 E paper and >= 1 held-out L paper (any list position). rho_last = "
                  "(P_SL - P_SE)/(P_L - P_E) on last-list-position rows (weight 1 per row); P_E over all E rows, "
                  "P_L over all held-out L rows.",
        p="key-cluster bootstrap (B = 1,000, multinomial key counts, seed 20260); p = (1 + #{rho_b <= 0.5})/(B + 1)",
        confirm="Holm-adjusted p < .05 and lower 95% bound > 0.5", contradict="upper 95% bound < 0.5",
        gate="none (diachronic within-key change)"),
    "CT4": dict(
        title="D3 meaning-fixed slot break (H3a)",
        data="held-out titles 2018-2026 that fill an LLM slot (frozen V2 inventory, PLAN opener rule) or a control "
             "pair",
        statistic="Stacked logit y ~ C(slot) + C(slot):(t-2023) + post + post x LLM-slot + llm_topic, SEs clustered by "
                  "topic100 (d3_slots.STACKED). Parameter: post x LLM-slot, as OR.",
        p="one-sided Wald z of the interaction <= 0", confirm="Holm-adjusted p < .05 and OR >= 1.5",
        contradict="upper 95% CI bound of the OR < 1", gate="none (diachronic)"),
    "CT5": dict(
        title="D4 neutral filter for NAME (H4a)", data="held-out 2018-2026 without OTHER rows; stages s0-s3",
        statistic="Pooled 2024-26 NAME G_total = P(NAME | accepted)/P(NAME | U), year-standardised (weights = the "
                  "year's s0 size).",
        p="paper bootstrap stratified by year (B = 2,000); TOST p = max{(1 + #{G_b <= 0.90})/(B + 1), "
          "(1 + #{G_b >= 1.11})/(B + 1)}",
        confirm="Holm-adjusted p < .05, 90% percentile CI inside [0.90, 1.11], and the gate",
        contradict="90% CI entirely outside [0.90, 1.11]",
        gate="acceptance-margin: the editing-corrected 90% CI (held-out bootstrap paired with draws of the audit "
             "net-flip DiD, WP4 G1 construction, frozen title audit) must lie inside [0.90, 1.11]"),
    "CT6": dict(
        title="D4 depletion of LLM markers (H4b)", data="as CT5",
        statistic="L-union (title typography, R24, R26, F24, F26, abstract em dash): pooled 2024-26 G_total and "
                  "G_desk x G_exit = P(f | s2)/P(f | s0).",
        p="bootstrap as CT5; p = max of (1 + #{G_b >= 1})/(B + 1) over the two gains",
        confirm="Holm-adjusted p < .05 (both gains < 1) and the gate for G_total",
        contradict="lower 95% bound of either gain > 1",
        gate="acceptance-margin association (G_total), WP4 Holm gate: L-union must be auditable (count and arXiv "
             "channel), its editing-corrected 95% interval below 1 and its identification p must survive Holm at "
             "0.025. "
             "It is not auditable (title typography and the abstract em dash cannot be carried by arXiv metadata), "
             "so CT6 cannot reach 'confirmed'; G_desk x G_exit is reported as the audit-free component"),
    "CT7": dict(
        title="D3 vintage alignment (H3c)", data="held-out U, 2025-2026",
        statistic="Logit R24-in-title ~ F24 + F26 + C(year) + C(topic100) + log(#authors) + llm_topic + log(title "
                  "words); topic100 cells without outcome variation dropped; SEs clustered by topic100. Statistic: "
                  "OR(F24)/OR(F26).",
        p="one-sided Wald z of log ratio <= 0", confirm="BH-adjusted p < .05 and ratio > 1",
        contradict="upper 95% CI bound < 1", gate="none (submission-population association, not acceptance)"),
    "CT8": dict(
        title="D3 register turnover (H3b)", data="held-out 2025 and 2026 titles in the 16 frozen large areas",
        statistic="Quasi-Poisson counts of titles with R24 (and R26) by area x year, area FE, log(#titles) offset, "
                  "Pearson dispersion: RR 2026/2025 for R24 and for R26.",
        p="two one-sided Wald tests on log RR (R24 down, R26 up); p = max of the two (intersection-union)",
        confirm="BH-adjusted p < .05, RR_R24 < 1 and RR_R26 > 1",
        contradict="R24 lower 95% bound > 1 or R26 upper 95% bound < 1", gate="none (diachronic)"),
    "CT9": dict(
        title="D1 tool bound (H1e(i))", data="held-out U, 2023 and 2026",
        statistic="F = f24_2 OR f26 OR title_typo. ratio = (NAME_2026 - NAME_2023 among F = 0) / (NAME_2026 - "
                  "NAME_2023 among all).",
        p="bootstrap within year (B = 2,000); p = (1 + #{ratio_b <= 0.70})/(B + 1)",
        confirm="BH-adjusted p < .05 and lower 95% bound > 0.70", contradict="upper 95% bound < 0.70",
        gate="none (diachronic)"),
    "CT10": dict(
        title="D4 published-only understatement of LLM use (H4c)", data="held-out 2021-2026 without OTHER rows",
        statistic="Kobak-style bound per year Y in 2024-26 = P(F24 | set, Y) - baseline, baseline = max(linear "
                  "2021-23 trend extrapolated to Y, max(P_2022, P_2023)), set in {accepted, all}; pooled = mean over "
                  "the three years; ratio = accepted/all. The held-out split supplies its own baseline years.",
        p="paper bootstrap stratified by year (B = 2,000); p = (1 + #{ratio_b >= 0.90})/(B + 1)",
        confirm="BH-adjusted p < .05, ratio < 0.90, and the gate", contradict="lower 95% bound > 0.90",
        gate="acceptance-margin association, WP4 Holm gate: tipping point D* = (b_acc - 0.9 b_all)/(1 - 0.9 a0) "
             "(net camera-ready change of the accepted F24 prevalence that would lift the ratio to 0.90); passes if "
             "the F24 abstract audit (2024-26 v1-abstract pairs) is auditable, the editing-corrected ratio's upper "
             "95% bound is < 0.90, and the identification p (z = (D_hat - D*)/sqrt(se_D^2 + se_D*^2)) survives "
             "Holm at one-sided 0.025 across the run's auditable association claims"),
    "CT11": dict(
        title="D4 pool invariance of the break (H4a(iii))", data="held-out 2018-2026, ACC, REJ and WD pools",
        statistic="CT1 logit fitted separately per pool; joint cluster-robust covariance from influence functions "
                  "summed by topic100 (d4_stage_gains.its_pools). Statistic: the three pairwise differences in "
                  "slope-change log OR.",
        p="TOST at +/-0.1 per pair (normal); p = max over the three pairs",
        confirm="BH-adjusted p < .05, every pairwise 90% CI inside (-0.1, 0.1), and the gate",
        contradict="any pairwise 90% CI entirely outside [-0.1, 0.1]",
        gate="acceptance-margin for the ACC pairs: widen their 90% CIs by b_max = (D_hi - D_lo)/(2 p (1 - p)) from "
             "the frozen NAME title audit and the held-out ACC NAME share p (2024-26); widened CIs must stay inside "
             "(-0.1, 0.1). The REJ-WD pair is audit-free"),
    "CT12": dict(
        title="D2 role gradient (H2b)", data="as CT3",
        statistic="rho_first - rho_last (first-list-position minus last-list-position within-stayer share), same "
                  "stayers and windows as CT3.",
        p="joint key-cluster bootstrap (the CT3 draws); p = (1 + #{diff_b >= 0})/(B + 1)",
        confirm="BH-adjusted p < .05 and upper 95% bound < 0", contradict="lower 95% bound > 0",
        gate="none (diachronic within-key change)"),
}

VERDICTS = dict(
    confirmed="adjusted p < .05, the point estimate beyond the stated minimal effect, the test's CI rule met and, "
              "for acceptance-margin tests, the audit gate passed",
    contradicted="the CI excludes the predicted region on the opposite side (test-specific rule)",
    not_confirmed="otherwise; when only the gate fails the result is reported as 'not confirmed (gate)'")


def rules_doc() -> dict:
    return dict(date=DATE, plan_section="PLAN.md section 4", alpha=ALPHA,
                multiplicity=dict(primary=dict(tests=list(PRIMARY), method="Holm", family_wise_alpha=ALPHA),
                                  secondary=dict(tests=list(SECONDARY), method="Benjamini-Hochberg", q=ALPHA)),
                sidedness="all tests one-sided in the predicted direction", verdicts=VERDICTS, tests=TESTS,
                gate=("No acceptance-margin result is called confirmed unless the audit rules out camera-ready editing "
                      "large enough to produce it (PLAN: tipping point beyond the audit CI). Gated: CT5, CT6 "
                      "(G_total), CT10, CT11 (ACC pairs). Diachronic and camera-ready-free tests are not gated. "
                      + GATE_RULE),
                gate_alpha_one_sided=GATE_ALPHA1, revision=REVISION,
                heldout_runs_allowed=1)


# ================================================================================================
# 6. Bundle, dry run, held-out run
# ================================================================================================
CODE_TOP = ["common.py", "features.py", "arxiv_audit.py", "author_features.py", "build_cache.py"]
INPUT_FILES = ["../../data/submissions.csv.gz", "../../data/submission_authors.csv.gz", "../../data/manifest.json",
               "outputs/core/universe.parquet", "outputs/features/features_v2.parquet",
               "outputs/features/lexicon_hash.txt", "outputs/d1_break/cache/r1_text.parquet",
               "outputs/d1_break/scores/R1__U__primary__rolling.json", "outputs/d3_register/register_results.json",
               "docs/PLAN.md"]


def bundle_files() -> dict:
    code = sorted((SRC / "analyses").glob("*.py")) + [SRC / f for f in CODE_TOP]
    code += sorted((SRC / "analyses").glob("*.json"))
    frozen = sorted(p for p in FROZEN.rglob("*") if p.is_file() and REFREEZE not in p.parents)
    inputs = [(STUDY / f).resolve() for f in INPUT_FILES]
    return dict(code=code, frozen=frozen, inputs=inputs)


def _rel(p: Path) -> str:
    import os
    return os.path.relpath(p, STUDY)


def write_bundle() -> str:
    files = bundle_files()
    lines = []
    for grp in ("code", "frozen", "inputs"):
        for p in files[grp]:
            lines.append(f"{sha256_file(p)}  {_rel(p)}")
    text = "\n".join(lines) + "\n"
    (OUTDIR / "bundle.sha256").write_text(text)
    h = hashlib.sha256(text.encode()).hexdigest()
    log(f"bundle.sha256: {len(lines)} files; bundle hash {h}")
    return h


def required_code() -> set[str]:
    """Code the tests execute: every loaded module file under src/ (prereg_confirm imports the D1-D4 and snapshot
    modules at top level) plus the lexicon JSONs. Other hashed code files are informational at verification."""
    import os
    req = {"src/analyses/lexicons.json", "src/analyses/d4_lexicon.json", "src/analyses/__init__.py"}
    for m in list(sys.modules.values()):
        f = getattr(m, "__file__", None)
        if f and Path(f).resolve().is_relative_to(SRC.resolve()):
            req.add(os.path.relpath(Path(f).resolve(), STUDY))
    return req


def verify_bundle(strict: bool = False) -> dict:
    """Re-hash every file in bundle.sha256 (paths relative to research/titles). Frozen parameters and the code the
    tests execute must match; other code files and the reference inputs only produce warnings (strict: all)."""
    text = (OUTDIR / "bundle.sha256").read_text()
    req = required_code()
    bad, warn = [], []
    for ln in text.splitlines():
        h, rel = ln.split("  ", 1)
        p = (STUDY / rel).resolve()
        ok = p.exists() and sha256_file(p) == h
        if not ok:
            must = strict or rel.startswith("outputs/prereg/frozen") or rel in req
            (bad if must else warn).append(rel)
    out = dict(bundle_hash=hashlib.sha256(text.encode()).hexdigest(), n_files=len(text.splitlines()),
               n_required_code=len(req), mismatched_required=bad, mismatched_other=warn, ok=not bad)
    log(f"verify: {out}")
    return out


def discovery_inputs(disc: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    papers = disc[["submission_id", "year", "name_primary", "split"]]
    prof = panel_rows(read_table("submission_authors"), papers)
    return papers, prof


# reference values reported by the work packages (for the dry-run reproduction check)
WP_REFERENCE = {
    "CT1": ("D1 RESULTS (H1a): slope-change OR 1.098 [1.044, 1.154], one-sided p = 1.3e-4", 1.098),
    "CT2": ("D1 results.json (H1c, current): u 1.51 -> 2.87 pp/yr, difference +1.353 pp, conditional CI [0.56, 2.15] "
            "(calibration and test roles share one weight vector per year); ratio 1.894; content share 0.574 "
            "[0.531, 0.621]. (The WP brief's +1.17 / 1.85 / 0.620 came from an earlier D1 iteration.)", 1.353),
    "CT3": ("D2 RESULTS (H2a): rho_last 0.995 [0.943, 1.050]", 0.995),
    "CT4": ("D3 RESULTS (H3a): stacked slot/control OR 2.55 [1.53, 4.25], p1 = 0.0002", 2.55),
    "CT5": ("D4 RESULTS (H4a): NAME G_total 1.021, 90% CI [1.001, 1.041]; WP4 G1 editing-corrected 90% CI "
            "[0.949, 1.031] (complete audit)", 1.021),
    "CT6": ("D4 RESULTS (H4b): L-union G_total 0.975 [0.951, 1.001]; G_desk x G_exit 0.981 [0.972, 0.992]",
            0.975),
    "CT7": ("D3 RESULTS (H3c): ratio 1.46 [1.17, 1.83], p1 = 0.0005", 1.46),
    "CT8": ("D3 RESULTS (H3b): RR 2026/2025 R24 0.744, R26 1.945 (2023-26 spec); 2025-26 spec 0.744 [0.642, 0.862], "
            "1.944 [1.672, 2.261]", 0.744),
    "CT9": ("D1 RESULTS (H1e): F=0 rise / total rise 2026 0.98 [0.96, 1.00]", 0.98),
    "CT10": ("D4 kobak_bounds.csv: F24 cons 2024-26 mean ratio 0.717 [0.495, 0.888], P(ratio >= 0.9) = 0.0175",
             0.717),
    "CT11": ("D4 RESULTS (H4a): ACC 1.053, REJ 1.119, WD 1.107; Wald equality p = 0.51; no pair TOST-equivalent",
             None),
    "CT12": ("D2 RESULTS (H2b): rho_first - rho_last = -0.470 [-0.602, -0.359]", -0.470),
}


def check_prepare(fz: dict, disc: pd.DataFrame, n_per_year: int = 300, n_embed: int = 120) -> dict:
    """Validate the held-out pipeline: run prepare_frame on a stratified sample of RAW discovery rows (cached MiniLM
    embeddings) and compare every column the tests use with the discovery frame; re-embed a few abstracts to check
    the embedding step; check the universe filter on all raw rows."""
    t0 = time.time()
    s = read_table("submissions")
    rng = np.random.default_rng(SEED)
    idx = np.sort(np.concatenate([rng.choice(np.where(s.year.to_numpy() == y)[0],
                                             min(n_per_year, int((s.year == y).sum())), replace=False)
                                  for y in sorted(s.year.unique())]))
    Ec = np.load(C.CACHE / "emb_abstract_all-MiniLM-L6-v2.npy", mmap_mode="r")
    sub = s.iloc[idx].reset_index(drop=True)
    ho, counts = prepare_frame(sub, fz, emb=np.asarray(Ec[idx], np.float32), split="check")
    cols = ["year", "name_primary", "name_strict", "name_loose", "name_compound", "f24", "f24_2", "f26", "f26_words",
            "title_typo", "F_d1", "F_any", "r24_any", "r26_any", "abs_emdash", "L_union", "O_union", "opener_word",
            "slot_improve", "slot_improve_raw", "slot_reveal", "slot_reveal_raw", "slot_exploit", "slot_exploit_raw",
            "slot_study_adj", "slot_study_adj_word", "slot_word_in_abstract", "ctrl_towards", "ctrl_novel", "ctrl_via",
            "n_words", "case_all_caps", "case_sentence_case", "question_opener", "mk_via", "mk_using",
            "name_orthography", "topic100", "llm_regex", "llm_cluster", "llm_topic", "ACC", "REJ", "WD", "DR", "NA",
            "wd_post", "pool", "stage_s1", "stage_s2", "stage_s3", "area_h", "log_authors", "r1_text", "lead_segment"]
    m = ho.merge(disc[["submission_id"] + cols], on="submission_id", suffixes=("_ho", "_d"), how="inner")
    mism = {}
    for c in cols:
        a, b = m[f"{c}_ho"], m[f"{c}_d"]
        if pd.api.types.is_numeric_dtype(a) and pd.api.types.is_numeric_dtype(b):
            eq = np.isclose(a.astype(float).fillna(-999).to_numpy(), b.astype(float).fillna(-999).to_numpy())
        else:
            eq = a.astype(object).where(a.notna(), "<NA>").astype(str).to_numpy() == \
                b.astype(object).where(b.notna(), "<NA>").astype(str).to_numpy()
        mism[c] = int((~eq).sum())
    # universe filter on all raw discovery rows
    reason = pd.Series([C.placeholder_reason(t, a) for t, a in zip(s.title.fillna(""), s.abstract.fillna(""))])
    n_u = int(reason.eq("").sum())
    # embedding step
    from sentence_transformers import SentenceTransformer  # noqa: F401
    j = rng.choice(len(sub), n_embed, replace=False)
    E_new = embed_minilm(sub.abstract.iloc[j])
    E_old = np.asarray(Ec[idx[j]], np.float32)
    cos = (E_new * E_old).sum(1) / (np.linalg.norm(E_new, axis=1) * np.linalg.norm(E_old, axis=1))
    t_new = C.assign_centroids(E_new, fz["centroids_minilm_k100"])
    t_old = C.assign_centroids(E_old, fz["centroids_minilm_k100"])
    out = dict(n_sample_raw=int(len(sub)), n_sample_U=int(len(ho)), n_matched=int(len(m)),
               mismatches_by_column=mism, total_mismatches=int(sum(mism.values())),
               universe_filter_all_raw_rows=dict(n_raw=int(len(s)), n_U=n_u, expected=43482, ok=n_u == 43482),
               embedding_check=dict(n=int(n_embed), cos_min=float(cos.min()), cos_median=float(np.median(cos)),
                                    topic100_agreement=float((t_new == t_old).mean())),
               seconds=round(time.time() - t0, 1))
    log(f"check: {json.dumps(clean(out))}")
    write_json(out, OUTDIR / "pipeline_check.json")
    return out


def dryrun(fz: dict, disc: pd.DataFrame) -> dict:
    t0 = time.time()
    papers, prof = discovery_inputs(disc)
    d2p = pd.read_parquet(C.OUT / "d2_carriers" / "panel_rows.parquet", columns=["submission_id", "key"])
    log(f"  D2 panel rows rebuilt: {len(prof)} (D2 file {len(d2p)}), keys {prof.key.nunique()} "
        f"(D2 {d2p.key.nunique()})")
    res = run_all(disc, papers, prof, fz, l_split=None)
    for k, r in res.items():
        ref, val = WP_REFERENCE[k]
        est = r["estimate"]
        if isinstance(est, dict):
            est = list(est.values())[0]
        r["wp_reference"] = dict(text=ref, value=val,
                                 abs_diff=(abs(float(est) - val) if val is not None else None))
    out = dict(
        date=DATE, mode="discovery dry run (every CT applied to the discovery split)", plan="docs/PLAN.md section 4",
        n_discovery_U=int(len(disc)), audit_source=fz["audit_source"],
        note=("Verdicts below are 'as if' the discovery data were the held-out data. They show which decision rules "
              "the discovery estimates already meet; they are not confirmations. Projected held-out power assumes "
              "the discovery estimate is the truth and a held-out SE of 2 x the discovery SE (held-out ~ 1/4 of "
              "discovery per year)."),
        results=res,
        summary=[dict(id=k, title=TESTS[k]["title"], family=r["family"], estimate=r["estimate"], ci=r["ci"],
                      ci_level=r["ci_level"], p_one_sided=r["p_one_sided"], p_adjusted=r["p_adjusted"],
                      gate_applies=r["gate"]["applies"], gate_passes=r["gate"].get("passes"),
                      verdict_as_if=r["verdict"], reasons=r["verdict_reasons"]) for k, r in res.items()],
        runtime_s=round(time.time() - t0, 1))
    return out


def run_heldout(sub_path: str, auth_path: str, force: bool = False) -> dict:
    """The confirmatory run. Verifies the bundle, refuses a second run, writes outputs/prereg/heldout.json."""
    if GUARD.exists() and not force:
        raise SystemExit(f"held-out run already started ({GUARD}); each test runs once (PLAN section 4)")
    if (OUTDIR / "heldout.json").exists():
        raise SystemExit("heldout.json exists: the confirmatory run is complete and cannot be repeated")
    v = verify_bundle()
    if not v["ok"]:
        raise SystemExit(f"bundle verification failed: {v['mismatched_required']}")
    attempts = json.loads(GUARD.read_text())["attempts"] if GUARD.exists() else []
    attempts.append(dict(started=time.strftime("%Y-%m-%d %H:%M:%S"), bundle_hash=v["bundle_hash"], forced=force,
                         submissions=str(sub_path), authors=str(auth_path),
                         submissions_sha256=sha256_file(Path(sub_path)), authors_sha256=sha256_file(Path(auth_path))))
    write_json(dict(attempts=attempts), GUARD)
    fz = load_frozen()
    s_ho, a_ho = read_raw(sub_path), read_raw(auth_path)
    df_ho, counts = prepare_frame(s_ho, fz, split="heldout")
    disc = discovery_frame()
    keep = ["submission_id", "year", "name_primary", "split"]
    papers = pd.concat([disc[keep], df_ho[keep]], ignore_index=True)
    assert not papers.submission_id.duplicated().any(), "held-out ids overlap discovery ids"
    prof = panel_rows(pd.concat([read_table("submission_authors"), a_ho], ignore_index=True), papers)
    res = run_all(df_ho, papers, prof, fz, l_split="heldout")
    alt = {}
    if fz["audit_source"] != str(FROZEN.relative_to(STUDY)):  # refrozen audit used: also report the bundle-time one
        fzb = load_frozen(prefer_refreeze=False)
        for cid, f in [("CT5", ct5_neutrality), ("CT6", ct6_depletion), ("CT10", ct10_kobak), ("CT11", ct11_invariance)]:
            alt[cid] = f(df_ho, fzb)["gate"]
    out = dict(date_run=time.strftime("%Y-%m-%d"), bundle_hash=v["bundle_hash"], audit_source=fz["audit_source"],
               heldout_counts=counts.to_dict(orient="records"), results=res,
               gates_with_bundle_time_audit=alt or "not applicable (bundle-time audit used)")
    write_json(out, OUTDIR / "heldout.json")
    return out


# ================================================================================================
# 7. prereg.md
# ================================================================================================
def _fmt(x, d=3):
    if x is None:
        return "n/a"
    if isinstance(x, dict):
        return "; ".join(f"{k} {_fmt(v, d)}" for k, v in x.items())
    if isinstance(x, (list, tuple)):
        return "[" + ", ".join(_fmt(v, d) for v in x) + "]"
    try:
        xf = float(x)
    except (TypeError, ValueError):
        return str(x)
    if not np.isfinite(xf):
        return "inf" if xf > 0 else "n/a"
    if abs(xf) < 1e-3 and xf != 0:
        return f"{xf:.1e}"
    return f"{xf:.{d}f}"


def _fmtp(x) -> str:
    return "n/a" if x is None else f"{float(x):.4g}"


def write_prereg(bundle_hash: str, dry: dict, params: dict, check: dict | None):
    R = dry["results"]
    au = params["audit"]["state"]
    L = []
    A = L.append
    A("# Pre-registration: held-out confirmation of the ICLR title study (WP9)")
    A("")
    A(f"- **Date:** {DATE}")
    A(f"- **Plan:** `docs/PLAN.md` section 4 (sha256 `{params['plan']['sha256'][:16]}...`)")
    A(f"- **Bundle hash:** `{bundle_hash}` (SHA-256 of `outputs/prereg/bundle.sha256`)")
    rv = params.get("revision") or REVISION
    A(f"- **Revision {rv['revision']}** ({rv.get('stage', 'integration pass')}, {rv['date']}). Supersedes bundle "
      f"hash `{rv['previous_bundle_hash']}` (revision {rv.get('previous_revision', rv['revision'] - 1)}). Why: "
      f"{rv['reason']} Details in section 9.")
    A("- **Status:** frozen before any request for held-out data. The held-out (confirmation) split has not been "
      "seen; only discovery rows (`discovery_allowed = 1`) were used.")
    A("- **Code:** `src/analyses/prereg_confirm.py` (CT1–CT12 as pure functions, discovery dry run, bundle). "
      "The repository is not committed by this work package (no git commands are run here); the code is frozen "
      "by content hash instead, as for `features.py` in WP1.")
    A("")
    A("## 1. Held-out data handling")
    A("")
    A("1. The held-out submissions and author tables are read with the README convention "
      "(`keep_default_na=False`, `na_values=['\\N']`).")
    A("2. `prepare_frame` applies the discovery universe rules (placeholder titles, abstracts under 20 words, empty "
      "titles), builds pools and stages with `_core.pool_flags`, harmonises areas, and computes all title and "
      "abstract features with the frozen `features_v2.build` and `lexicons.json`.")
    A("3. Topics: each held-out abstract is embedded with all-MiniLM-L6-v2 (L2-normalised) and assigned to the "
      f"nearest frozen discovery centroid (k = 100). The centroids reproduce "
      f"{100 * params['topics']['discovery_label_reproduction']:.2f}% of the discovery labels. `llm_topic` = LLM "
      "regex OR membership in one of the 20 frozen discovery LLM clusters.")
    A("4. Author history (CT3, CT12) is built on the union of discovery and held-out declared profile keys.")
    A("   Expected held-out sizes (PLAN): about a quarter of discovery per year, e.g. 2023 ≈ 970, 2024 ≈ 1,440, "
      "2025 ≈ 2,240, 2026 ≈ 3,850 papers.")
    A("5. `run_heldout` verifies every hash in `bundle.sha256`, writes a guard file and refuses a second run. "
      "Each test runs once.")
    if check:
        A(f"6. Pipeline check on {check['n_sample_U']} raw discovery rows run through `prepare_frame`: "
          f"{check['total_mismatches']} mismatches over {len(check['mismatches_by_column'])} columns against the "
          f"discovery frame. The universe filter on all raw rows gives {check['universe_filter_all_raw_rows']['n_U']:,} "
          f"(expected 43,482). Re-embedding {check['embedding_check']['n']} abstracts: median cosine "
          f"{check['embedding_check']['cos_median']:.4f} to the cached embeddings, topic agreement "
          f"{100 * check['embedding_check']['topic100_agreement']:.1f}%.")
    A("")
    A("## 2. Frozen bundle")
    A("")
    A("`outputs/prereg/bundle.sha256` lists every file in `sha256sum` format, with paths relative to "
      "`research/titles`. It has three groups:")
    A("")
    A("- **Code:** all of `src/analyses/*.py` and `*.json`, plus `src/{common,features,arxiv_audit,author_features,"
      "build_cache}.py`.")
    A("- **Frozen parameters (`outputs/prereg/frozen/`):**")
    A("  - `lexicons.json`, `d4_lexicon.json`, `slot_inventory.json` (V2-frozen slots) and "
      "`slot_variants_dropped.json`.")
    A("  - `fingerprints.json` (RARE21, F26 words, typography, R24/R26).")
    A("  - `centroids_minilm_k100.npy`, `llm_clusters.json` and `area_crosswalk.csv`.")
    A("  - `r1_rolling_<year>.npz`: rolling R1 vocabularies, idf, five fold models and calibration-year OOF scores.")
    A("  - `dfl_cells.csv` (DFL cell model), `audit_flips.csv`, `audit_did_boot.npz` and `audit_state.json`.")
    A("  - `params.json` and `rules.json` (the machine-readable rules of section 4).")
    A("- **Inputs (reference):** the discovery data files, `universe.parquet`, `features_v2.parquet`, the D1 R1 "
      "text cache and `PLAN.md`.")
    A("")
    w = params["d1"]["r1_windows"]
    early = max(v["max_abs_diff_test_scores_vs_d1"] for k, v in w.items() if int(k) <= 2023)
    late = max(v["max_abs_diff_test_scores_vs_d1"] for k, v in w.items() if int(k) >= 2024)
    A("The R1 models were refitted here, because D1 saved scores only. Each refit uses D1's CV-chosen C and D1's "
      "folds. Test-row fold scores match D1's stored scores:")
    A(f"- Windows 2019–23: within {early:.1e} logit units.")
    A(f"- Windows 2024–26: within {late:.1e} logit units, which is within the lbfgs stopping tolerance.")
    A("- The per-year unexplained increments u_y equal D1's to about 1e-5. The CT2 dry-run point estimate "
      f"(+{dry['results']['CT2']['estimate']:.3f} pp) equals D1's current `results.json` (+1.353 pp).")
    A("")
    A("Two consistency checks also pass:")
    A("- The D2 key panel rebuilt from the raw author table matches D2's `panel_rows.parquet` (rows and keys).")
    A("- Every other dry-run estimate reproduces the corresponding work package (`dryrun.json`, `wp_reference`).")
    A("")
    A("## 3. Inference, multiplicity and verdicts")
    A("")
    A("- All tests are one-sided in the predicted direction.")
    A("- **Primary family (CT1–CT6):** Holm, family-wise α = 0.05.")
    A("- **Secondary family (CT7–CT12):** Benjamini–Hochberg, q = 0.05.")
    A("- Bootstrap p-values use the +1 correction, (1 + #null)/(B + 1). Paper bootstraps use B = 2,000, stratified "
      "by year; the key-cluster bootstrap uses B = 1,000. All seeds are fixed in `params.json`.")
    A(f"- **Confirmed:** {VERDICTS['confirmed']}.")
    A(f"- **Contradicted:** {VERDICTS['contradicted']}.")
    A(f"- **Not confirmed:** {VERDICTS['not_confirmed']}.")
    A("")
    A("## 4. Tests")
    A("")
    for k, t in TESTS.items():
        r = R[k]
        A(f"### {k}: {t['title']} ({'primary' if k in PRIMARY else 'secondary'})")
        A("")
        A(f"- **Data:** {t['data']}.")
        A(f"- **Statistic:** {t['statistic']}")
        A(f"- **p-value:** {t['p']}.")
        A(f"- **Confirm if:** {t['confirm']}.")
        A(f"- **Contradicted if:** {t['contradict']}.")
        A(f"- **Gate:** {t['gate']}.")
        A(f"- **Discovery dry run:** {_fmt(r['estimate'])}, {int(100 * r['ci_level'])}% CI {_fmt(r['ci'])}; "
          f"one-sided p = {_fmtp(r['p_one_sided'])}.")
        pw = {kk: v for kk, v in r["projected_heldout_power"].items() if not isinstance(v, str)}
        if pw:
            A(f"- **Projected held-out power (approximate):** {_fmt(pw, 2)}.")
        A("")
    A("## 5. Audit gate")
    A("")
    A("The PLAN gate says that no acceptance-margin result is called confirmed unless the audit tipping point "
      "exceeds the audit's CI. Diachronic and camera-ready-free tests (CT1–CT4, CT7–CT9, CT12) are not gated. "
      "The gated tests, with their operational rules fixed now:")
    A("")
    for k in ("CT5", "CT6", "CT10", "CT11"):
        A(f"- **{k}:** {TESTS[k]['gate']}.")
    A("")
    A(f"**Gate rule (adopted in revision 2; unchanged since).** {GATE_RULE}")
    A("")
    A("**Audit state frozen in the bundle** (WP4's final audit; `frozen/audit_state.json`).")
    A(f"- Original audit: {au['original']['n_pairs']} usable pairs (2022–26; sensitivity spec), "
      f"{au['original'].get('n_pairs_2023_26', 'n/a')} of them in 2023–26.")
    A(f"- Enlargement: the complete file, {au['enlargement']['n_lines_used']} lines ({au['enlargement']['n_records']} "
      f"records without a network error; SHA-256 `{au['enlargement']['sha256_of_lines_used'][:16]}...`, identical to "
      f"WP4's freeze: {au['enlargement'].get('matches_wp4')}), of which {au['enlargement']['n_pairs']} are usable "
      f"pairs.")
    A(f"- Title gate audit (WP4 primary, 2023–26): {au['pooled']['n_pairs']} pairs "
      f"({au['pooled']['pairs_by_decision']}).")
    A(f"- Abstract gate audit (WP4 primary, 2024–26 v1-abstract pairs): {au['v1_abstracts']['n_pairs']} pairs "
      f"({au['v1_abstracts']['pairs_by_decision']}).")
    rp = au.get("reproduces_wp4") or {}
    if rp:
        A("- The frozen flip tables reproduce WP4's canonical `T4_2_flip_matrices.csv` (primary) and "
          "`abstract_audit.csv` (abs_2024_26) exactly: max |difference| "
          + ", ".join(f"{k} {v['max_abs_diff']:.1e}" for k, v in rp.items()) + "; auditability identical.")
    A("")
    A("**Refreeze rule: closed.** Revision 1 allowed one `audit_refreeze` before held-out access because the "
      "background enlargement was still running. The enlargement is now complete and frozen in the bundle "
      "itself, so `audit_refreeze` refuses to run.")
    A("")
    A("## 6. Discovery dry run")
    A("")
    A("Each test applied to the discovery split. The verdicts are **as if** discovery were the held-out data; "
      "they show which decision rules the discovery estimates already meet. Adjusted p-values use the same "
      "families.")
    A("")
    A("| Test | Estimate | CI | p (one-sided) | p adjusted | Gate | Verdict as if | Reasons |")
    A("|---|---|---|---|---|---|---|---|")
    for s in dry["summary"]:
        gate = "n/a" if not s["gate_applies"] else ("pass" if s["gate_passes"] else "fail")
        A(f"| {s['id']} | {_fmt(s['estimate'])} | {_fmt(s['ci'])} ({int(100 * s['ci_level'])}%) | "
          f"{_fmtp(s['p_one_sided'])} | {_fmtp(s['p_adjusted'])} | {gate} | {s['verdict_as_if']} | "
          f"{'; '.join(s['reasons']) or '-'} |")
    A("")
    A("**What the dry run implies for the held-out run.** These points were fixed before held-out access and are "
      "not grounds for changing any rule:")
    A("")
    notes = dryrun_notes(R)
    for n in notes:
        A(f"- {n}")
    A("")
    A("## 7. Clarifications and deviations from PLAN section 4")
    A("")
    for i, d in enumerate(DEVIATIONS, 1):
        A(f"{i}. {d}")
    A("")
    A("## 8. Running the confirmation")
    A("")
    A("```bash")
    A("cd research/titles/src")
    A("OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.prereg_confirm verify")
    A("OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.prereg_confirm heldout "
      "<heldout_submissions.csv.gz> <heldout_submission_authors.csv.gz>")
    A("```")
    A("")
    A("The run writes `outputs/prereg/heldout.json`, with the same fields as `dryrun.json`.")
    A("")
    A("The guard file `heldout_started.json` logs every attempt. A run that crashes before writing "
      "`heldout.json` is a technical failure, not a result; it may be restarted with `--force`, and the restart "
      "is logged. Once `heldout.json` exists, the run cannot be repeated.")
    A("")
    A("## 9. Revision history")
    A("")
    hist = rv.get("history") or []
    for h in hist:
        if h["revision"] == 1:
            A(f"- **Revision 1** ({h['date']}, bundle hash `{h['bundle_hash']}`): gate audit = {h['gate_audit']}.")
        else:
            A(f"- **Revision {h['revision']}** ({h['date']}, bundle hash `{h['bundle_hash']}`): {h['reason']}")
    if not hist:   # revision-2 record (before the history field existed)
        A(f"- **Revision 1** (2026-10-11, bundle hash `{rv['previous_bundle_hash']}`): gate audit = "
          f"{rv.get('previous_audit')}.")
    A(f"- **Revision {rv['revision']}** (this file, bundle hash `{bundle_hash}`): {rv['reason']}")
    A("- What changed in the dry run: revision 2 changed only the gate fields of CT5, CT6, CT10 and CT11 (new audit, "
      "new rule); revision 3 changed nothing in `dryrun.json` except the bundle hash (re-run and compared). Every "
      "test statistic, p-value and CI of CT1–CT12 is computed by the same frozen functions on the same discovery "
      "data. Superseded bundle files are not kept in `outputs/prereg/`; the integration pass's pre-change copies are "
      "in `outputs/audit/integration/pre_fix_backup/` (pass1: revision 1; pass2: revision 2).")
    (OUTDIR / "prereg.md").write_text("\n".join(L) + "\n")


def dryrun_notes(R: dict) -> list[str]:
    n = []
    r1 = R["CT1"]
    n.append(f"CT1: the discovery OR ({r1['estimate']:.3f}) is below the pre-registered minimal effect of 1.10. "
             f"Even with the discovery value as the true effect, the projected held-out z is about "
             f"{r1['projected_heldout_power']['z_heldout_projected']:.1f}, not the ≈ 6 stated in the PLAN (that "
             "figure came from the pilot's 1.28, which was for compound titles). CT1 will most likely end as 'not "
             "confirmed'.")
    r2 = R["CT2"]
    n.append(f"CT2: in discovery, the upper bound of the content share is {r2['details']['content_share_ci'][1]:.3f} "
             f"(point {r2['details']['content_share_post_steps']:.3f}), so the '< 0.60' condition already fails. "
             f"The acceleration itself is +{r2['estimate']:.2f} pp/yr [{r2['ci'][0]:.2f}, {r2['ci'][1]:.2f}], ratio "
             f"{r2['details']['ratio']:.2f}. This CI is wider than D1's conditional CI [0.56, 2.15] because the "
             "held-out design resamples the discovery calibration years and the test years independently. In the "
             "held-out data they really are independent, so obs_{y-1} no longer telescopes out of the year-to-year "
             f"steps. Projected held-out z ≈ {r2['projected_heldout_power']['z_heldout_projected']:.1f}, so CT2 is "
             "underpowered.")
    r6 = R["CT6"]
    n.append("CT6: the L-union is unauditable (arXiv cannot carry title typography or the em dash), so CT6 cannot be "
             "'confirmed' under the gate. The audit-free "
             f"G_desk x G_exit = {r6['estimate']['G_desk_x_exit']:.3f} (one-sided p "
             f"{r6['details']['p_G_desk_x_exit']:.4f}) will be reported as such.")
    r11 = R["CT11"]
    n.append("CT11: no discovery pair is equivalent within ±0.1 (90% CIs "
             f"{_fmt(r11['ci'])}). The held-out CIs are about twice as wide, so CT11 is expected to be 'not "
             f"confirmed'. Its ACC-pair gate also fails in discovery (b_max = {r11['gate']['b_max_logOR']:.3f}).")
    r5 = R["CT5"]
    n.append(f"CT5: discovery G_total {r5['estimate']:.3f}, 90% CI {_fmt(r5['ci'])}. The editing-corrected 90% CI "
             f"{_fmt(r5['gate']['corrected_ci90'])} {'passes' if r5['gate']['passes'] else 'fails'} the gate.")
    r10 = R["CT10"]
    g10 = r10["gate"]
    n.append(f"CT10: discovery ratio {r10['estimate']:.3f} {_fmt(r10['ci'])}. Tipping point "
             f"{g10['tipping_pp']:.2f} pp (se {g10['tipping_se_pp']:.2f}) against the F24 abstract-audit DiD "
             f"{g10['audit_did_pp']:+.2f} pp {_fmt(g10['audit_did_ci_pp'], 2)}: identification p "
             f"{g10['p_ident']:.4f} (Holm {_fmtp(g10.get('p_ident_holm'))}, family {g10.get('holm_family')}); "
             f"editing-corrected upper 95% bound of the ratio {g10['corrected_ratio_hi95']:.3f}. The gate "
             f"{'passes' if g10['passes'] else 'fails'} (the revision-1 uncorrected rule would "
             f"{'pass' if g10['passes_uncorrected_rule'] else 'fail'}). The held-out split's own 2021–23 baseline "
             "years are small, so the CI will be wide.")
    n.extend(audit_interpretation_notes(R))
    pw = {k: power_05(r) for k, r in R.items()}
    low = [f"{k} ({v:.2f})" for k, v in pw.items() if v is not None and v < 0.5]
    if low:
        n.append("Approximate projected probability of meeting the statistical rule at α = .05 (unadjusted) is "
                 "below 0.5 for: " + ", ".join(low) + ". For these tests, a 'not confirmed' held-out result is weak "
                 "evidence against the discovery finding.")
    return n


def audit_interpretation_notes(R: dict | None = None) -> list[str]:
    """Revisions 2-3: what the direction audits imply for READING a held-out confirmation. The decision rules are
    unchanged; these notes only state which substantive claims a confirmed statistic would and would not carry.
    Revision 2 added CT3, CT7, CT8 and CT9; revision 3 added CT1, CT2, CT4, CT6 and CT12."""
    n = []
    try:
        d1 = json.loads((C.OUT / "d1_break" / "results.json").read_text())
        a = d1["H1a"]
        n.append(f"CT1 (reading): CT1's p-value uses paper-level SEs clustered by topic100 (dry run "
                 f"{a['p_one_sided_paper_level']:.1e}). D1's audit showed that these ignore year shocks: the "
                 f"year-level REML p in discovery is {a['p_one_sided_year_level']:.3f} (Holm "
                 f"{a['holm_adjusted_p']:.3f}). A confirmed CT1 (which needs OR >= 1.10) should be reported with the "
                 "year-level test beside it, and on its own it would not establish a dated 2024 break.")
        c = d1["H1c"]
        ci2 = (R or {}).get("CT2", {}).get("ci")
        n.append("CT2 (reading): the held-out bootstrap resamples papers within year, so it holds year shocks fixed; "
                 "a confirmed CT2 would not establish year-level acceleration. D1's two-stage year-level CI in "
                 f"discovery is [{100 * c['year_level_two_stage']['diff_ci'][0]:.2f}, "
                 f"{100 * c['year_level_two_stage']['diff_ci'][1]:.2f}] pp (Holm {c['holm_adjusted_p']:.3f})"
                 + (f"; the dry-run CI [{ci2[0]:.2f}, {ci2[1]:.2f}] is similar in width but contains no year-shock "
                    "variance." if ci2 else "."))
    except (OSError, KeyError, ValueError, TypeError):
        pass
    try:
        r3 = json.loads((C.OUT / "d3_register" / "results.json").read_text())
        e = next(h for h in r3["hypotheses"] if h["id"] == "H3a")["estimates"]
        rob = pd.read_csv(C.OUT / "d3_register" / "slot_robustness.csv")
        nv = rob[rob["label"].str.startswith("controls without via/using") & (rob["model"] == "stacked_interaction")]
        nv = nv.iloc[0]
        le = e["leave_out_enhancing"]["slots_post"]
        other = [int(x["break_year"]) for x in e["control_break_scan"]
                 if int(x["break_year"]) != 2024 and x["p_two"] < 0.05]
        n.append("CT4 (reading): a confirmation confirms the stacked slot-minus-control statistic on the "
                 "pre-registered 2024 specification. The control contrast leans on via/using (without it the stacked "
                 f"contrast is {nv['OR']:.2f} [{nv['OR_lo']:.2f}, {nv['OR_hi']:.2f}]); OR >= 2 for the slots rests on "
                 f"the in-sample word 'enhancing' (without it {le['OR']:.2f} [{le['OR_lo']:.2f}, {le['OR_hi']:.2f}]); "
                 f"the pooled controls shift at the other candidate break years ({', '.join(map(str, other))}); and "
                 "the break is not sharply dated against 2023.")
    except (OSError, KeyError, ValueError, StopIteration, IndexError):
        pass
    try:
        r4 = json.loads((C.OUT / "d4_filter" / "results.json").read_text())["hypotheses"]["H4b"]["estimates"]
        n.append("CT6 (reading): an L-union G < 1, including the audit-free G_desk x G_exit, would mainly re-detect "
                 "the pre-2024 R24 genre penalty (D4: R24 total "
                 f"{r4['components']['R24']['total']['est']:.3f} in 2024-26 against "
                 f"{r4['components_pre_2018_23']['R24']['total']['est']:.3f} in 2018-23; L-union without R24 "
                 f"{r4['L_noR24']['total']['est']:.3f}). LLM-specific selection would need the L-union without R24 or "
                 "the post/pre ratio, which CT6 does not test.")
    except (OSError, KeyError, ValueError, TypeError):
        pass
    try:
        r2 = json.loads((C.OUT / "d2_carriers" / "results.json").read_text())
        h = next(x for x in r2["hypotheses"] if x["id"] == "H2b")["estimate"]
        w = h["entrant_minus_stayer_L_first_within_lastkey_size_topic"]
        sy = h["symmetric_lookback_prior_first_ratio"]
        n.append("CT12 (reading): a confirmation confirms the D2-group contrast rho_first - rho_last, which mixes "
                 "cohort with tenure (D2 stayer keys have >= 3 years of presence): within the same last-position key "
                 f"the entrant-first premium is {100 * w['est']:.1f} pp [{100 * w['lo']:.1f}, {100 * w['hi']:.1f}], and "
                 "with a symmetric 2-year lookback prior first keys changed "
                 f"{sy['ratio_prior']:.2f} [{sy['ratio_prior_lo']:.2f}, {sy['ratio_prior_hi']:.2f}] times the "
                 "first-position population. It is not a role effect: list position is a partition label.")
    except (OSError, KeyError, ValueError, StopIteration):
        pass
    try:
        r2 = json.loads((C.OUT / "d2_carriers" / "results.json").read_text())
        son = r2["shared_outcome_null"]["main"]["last"]
        n.append("CT3 (reading): the D2 audit found that a purely generational world with the observed "
                 f"co-authorship gives rho_last of {son['null_Nfirst']['est']:.2f}-{son['null_NRfirst']['est']:.2f}, "
                 "above the 0.5 threshold, so a confirmed CT3 would confirm the statistic, not communal change (H2a "
                 "is 'not identified' in discovery).")
    except (OSError, KeyError, ValueError):
        pass
    try:
        r3 = json.loads((C.OUT / "d3_register" / "results.json").read_text())
        H = {h["id"]: h for h in r3["hypotheses"]}
        c = H["H3c"]["estimates"]["co_primary_shared_lemma_free"]
        nb = H["H3b"]["estimates"]["neutral_synonym_benchmark"]["all|R24_vs_N24_ratio_of_RR"]
        n.append(f"CT7 (reading): without the lemmas shared by RARE21 and R24 the discovery ratio is {c['ratio']:.2f} "
                 f"[{c['ratio_ci'][0]:.2f}, {c['ratio_ci'][1]:.2f}] with OR(F24) {c['OR_a']:.2f}; the contrast is "
                 "carried by F26 papers avoiding R24, so a confirmed CT7 would not by itself establish title-abstract "
                 "vintage alignment.")
        n.append(f"CT8 (reading): neutral synonyms (improv*, utili[sz]*, exploit*) fell like R24 in discovery (R24 "
                 f"relative to them {nb['ratio']:.2f} [{nb['lo']:.2f}, {nb['hi']:.2f}]) and R26 was chosen after the "
                 "pilot saw it rise, so a confirmed CT8 would show a 2026 shift in these word families, not a register "
                 "turnover.")
    except (OSError, KeyError, ValueError, StopIteration):
        pass
    try:
        r1 = json.loads((C.OUT / "d1_break" / "results.json").read_text())
        pc = r1["H1e"]["positive_control_D3"]["H3d_slot_uplift_F_d1"]
        ok = bool(r1["H1e"]["positive_control_D3"].get("validates_F_d1_bound", pc["OR_slot_ci"][0] > 1))
        n.append(f"CT9 (reading): the D3 positive control with this fingerprint is "
                 f"{'significant' if ok else 'not significant'} (slot OR "
                 f"{pc['OR_slot']:.2f} [{pc['OR_slot_ci'][0]:.2f}, {pc['OR_slot_ci'][1]:.2f}]) and criterion (i) has "
                 "little power by construction, so a confirmed CT9 would not bound the tool share"
                 + (" on its own." if ok else "."))
    except (OSError, KeyError, ValueError):
        pass
    return n


def power_05(r: dict) -> float | None:
    """One comparable projected-power number per test (alpha .05, unadjusted; see projected_heldout_power)."""
    p = r["projected_heldout_power"]
    for k in ("P(confirm) at alpha 0.0500", "P(90% CI inside margin), approx", "alpha_0.05"):
        if isinstance(p.get(k), float):
            return p[k]
    v = p.get("P(pair equivalent), approx, per pair")
    return float(np.prod(v)) if isinstance(v, list) else None


DEVIATIONS = [
    "Code commit: no git commands are run in this work package, so the code is frozen by content hashes "
    "(bundle.sha256) rather than by a commit id. The commit itself is left to the orchestrator.",
    "R1 vectoriser and classifiers: D1 saved scores, not models. The rolling R1 models were refitted with D1's "
    "CV-chosen C and D1's StratifiedKFold folds (seed 0). Their test-row fold scores reproduce D1's stored scores "
    "(see params.json, `max_abs_diff_test_scores_vs_d1`).",
    "CT2 inference: the PLAN asks for a paper bootstrap stratified by year. Held-out papers are resampled within "
    "year. Because the recalibration targets discovery obs_{y-1}, the discovery calibration-year papers are also "
    "resampled, independently, and the shift is re-solved each replicate. The content-share condition uses the "
    "share of the summed 2024–26 steps, as in D1.",
    "CT3/CT12: stayer status uses any-role presence (D2-2). The E side uses the discovery ∪ held-out union "
    "(PLAN: 'an E-period paper (union)'); P_E and P_SE are computed over union E rows. L outcomes are held-out "
    "only. rho uses the pilot/D2 definition (P_SL − P_SE)/(P_L − P_E) (D2-1).",
    "CT5/CT6 pooling: 2024–26 is year-standardised to s0 sizes (D4). G_desk × G_exit uses the PLAN stages "
    "(accepted papers are inside s0–s2). The camera-ready-free variant (accepted papers removed) is reported as "
    "a pre-specified robustness check.",
    "Gate operationalisation (revision 2): CT5 uses the editing-corrected TOST (the WP4 G1 construction). CT6's "
    "G_total gate cannot pass, because the L-union is unauditable (arXiv channel). CT10 uses an explicit tipping "
    "point for the 0.90 ratio against the F24 abstract audit, with WP4's identification p (tipping-point SE "
    "included), an editing-corrected interval and Holm at 0.025 across the run's auditable association claims. "
    "CT11 widens the ACC-pair CIs by the largest slope bias that editing within the NAME audit CI could create. "
    "The gate audit is WP4's frozen complete audit (title: 2023–26 primary pairs; abstracts: 2024–26 pairs). "
    "Revision 1 used the original audit + 1,261 enlargement lines and an uncorrected rule.",
    "CT8 statistic: the PLAN says 'R24 down and R26 up (two one-sided tests)'. Here this is the within-area "
    "quasi-Poisson rate ratio 2026/2025 (D3 H3b model, area FE and offset) on the 16 frozen large areas, with "
    "an intersection-union p. Area sign counts are descriptive only, because the held-out areas are about a "
    "quarter of discovery size.",
    "CT9 estimand: 2023→2026, with F = f24_2 ∪ f26 ∪ title_typo, the D1 primary fingerprint.",
    "CT10: the Kobak bound uses F24 (any RARE21 word) with the conservative baseline. 'Pooled 2024–26' is the "
    "mean of the three yearly bounds (D4). The held-out split supplies its own 2021–23 baseline.",
    "CT11: 'equivalent within ±0.1' means that all three pairwise 90% CIs lie inside (−0.1, 0.1). The CT11 "
    "p-value is the largest pairwise TOST p.",
    "Expected z: the PLAN's 'expected z ≈ 6' for CT1 came from the pilot's 1.28/yr, which was for compound "
    "titles. The dry run gives the discovery-based projection.",
    "The DFL cell model is frozen, as the PLAN requires, but no CT uses it, because there is no confirmatory "
    "test of H1d.",
    "Fixed seeds reproduce the work packages' bootstrap draws wherever the inputs coincide: D4 stage gains, the "
    "D4 Kobak bound, the D2 key bootstrap and D1's f0_rise.",
]


# ================================================================================================
def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    OUTDIR.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    log(f"=== prereg_confirm {stage} {time.strftime('%Y-%m-%d %H:%M:%S')} ===")
    if stage in ("freeze", "all"):
        disc = discovery_frame()
        freeze(disc)
    if stage in ("check", "all"):
        check_prepare(load_frozen(), discovery_frame())
    if stage in ("dryrun", "all"):
        fz = load_frozen()
        dry = dryrun(fz, discovery_frame())
        write_json(dry, OUTDIR / "dryrun.json")
        log(json.dumps(clean(dry["summary"]), indent=1)[:6000])
    if stage in ("bundle", "all"):
        h = write_bundle()
        dry = json.loads((OUTDIR / "dryrun.json").read_text())
        dry["bundle_hash"] = h
        dry["bundle_note"] = ("bundle hash = SHA-256 of outputs/prereg/bundle.sha256; dryrun.json and prereg.md are "
                              "written after it and are not inside the bundle")
        (OUTDIR / "dryrun.json").write_text(json.dumps(dry, indent=1))
        params = json.loads((FROZEN / "params.json").read_text())
        chk = json.loads((OUTDIR / "pipeline_check.json").read_text()) if (OUTDIR / "pipeline_check.json").exists() \
            else None
        write_prereg(h, dry, params, chk)
        log("prereg.md written")
    if stage == "verify":
        verify_bundle()
    if stage == "refreeze_final":
        # revision 2 (integration pass): re-freeze the gate audit on WP4's complete audit and record the revision;
        # every other frozen file (R1 models, centroids, lexicons, slot inventory, DFL cells) is left byte-identical
        if GUARD.exists() or (OUTDIR / "heldout.json").exists():
            raise SystemExit("held-out run already started; the bundle can no longer be revised")
        st = freeze_audit(FROZEN)
        params = json.loads((FROZEN / "params.json").read_text())
        params["audit_revision_1"] = params.get("audit_revision_1", params["audit"])
        params["audit"] = audit_params(st)
        params["revision"] = REVISION
        write_json(params, FROZEN / "params.json")
        write_json(rules_doc(), FROZEN / "rules.json")
        log(f"refreeze_final: audit re-frozen on WP4's complete audit; revision {REVISION['revision']}")
    if stage == "revise":
        # revision 3 (second integration pass): record the revision; every frozen file other than params.json and
        # rules.json stays byte-identical. Follow with dryrun (compared against the previous dryrun.json), bundle and
        # verify.
        if GUARD.exists() or (OUTDIR / "heldout.json").exists():
            raise SystemExit("held-out run already started; the bundle can no longer be revised")
        params = json.loads((FROZEN / "params.json").read_text())
        params["revision"] = REVISION
        write_json(params, FROZEN / "params.json")
        write_json(rules_doc(), FROZEN / "rules.json")
        log(f"revise: revision {REVISION['revision']} recorded (supersedes {REVISION['previous_bundle_hash'][:16]}...)")
    if stage == "audit_refreeze":
        if GUARD.exists():
            raise SystemExit("held-out run already started; the audit can no longer be refrozen")
        raise SystemExit("closed in revision 2: the enlargement is complete and frozen in the bundle "
                         "(see prereg.md section 5)")
        st = freeze_audit(REFREEZE)
        lines = [f"{sha256_file(p)}  {_rel(p)}" for p in sorted(REFREEZE.glob("*")) if p.is_file()]
        (OUTDIR / "audit_refreeze.sha256").write_text("\n".join(lines) + "\n")
        log(f"audit refrozen: {json.dumps(clean(st))[:500]}")
    if stage == "heldout":
        run_heldout(sys.argv[2], sys.argv[3], force="--force" in sys.argv)
    log(f"=== done {stage} ({time.time() - t0:.0f}s) ===")
    flush_log("prereg_confirm.log")


if __name__ == "__main__":
    main()
