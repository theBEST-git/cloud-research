"""WP0 core: universe and pools, periods, area crosswalk, LLM-topic flags, controls, loaders,
FE demeaning (alternating projections) with cluster-robust SEs, logit helpers, bootstraps,
centroid assignment and the paper figure style.

Build the shared tables once with
    cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses._core
which writes outputs/core/{universe.parquet, universe_counts.csv, area_crosswalk.csv, llm_clusters.json}.
Everything here is read-only on data/ and cache/. See analyses/API.md for the full contract.
"""
from __future__ import annotations

import json
import sys
import unicodedata
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Iterator, Sequence

import numpy as np
import pandas as pd

_SRC = Path(__file__).resolve().parents[1]
if str(_SRC) not in sys.path:  # allow `python path/to/_core.py` as well as `-m analyses._core`
    sys.path.insert(0, str(_SRC))

import features as F  # noqa: E402  (v1 detectors; never edited here)
from common import CACHE, DATA, OUT, STUDY, acceptance_population, load_submissions  # noqa: E402,F401

# --------------------------------------------------------------------------------------------
# Paths and constants
# --------------------------------------------------------------------------------------------
CORE = OUT / "core"
FEAT_DIR = OUT / "features"
TOPIC_DIR = OUT / "topics"
UNIVERSE_PATH = CORE / "universe.parquet"
FEATURES_PATH = FEAT_DIR / "features_v2.parquet"
TOPICS_BGE_PATH = TOPIC_DIR / "topics_bge.parquet"
CENTROIDS_PATH = TOPIC_DIR / "centroids.npz"
MASKED_EMB_PATH = TOPIC_DIR / "emb_masked_bge.npy"
MASKED_IDS_PATH = TOPIC_DIR / "emb_masked_bge_ids.npy"

YEARS = tuple(range(2017, 2027))
BREAK_YEAR = 2024
PRE = tuple(range(2017, 2024))          # 2017-2023
PRE_WD = tuple(range(2018, 2024))       # 2018-2023 (years with withdrawals)
POST = (2024, 2025, 2026)
POST_EXCL_2026 = (2024, 2025)
EARLY, LATE = (2022, 2023), (2025, 2026)  # D2 E and L windows

# Same regex as cache/title_features.parquet `llm_topic` (build_cache.title_table), on title + " " + abstract.
LLM_TOPIC_REGEX = (r"\b(?:LLMs?|large language models?|language models?|GPT-?\d|ChatGPT|instruction[- ]tun|"
                   r"in-context learning|chain-of-thought|RLHF)\b")
LLM_CLUSTER_THRESHOLD = 0.5  # topic100 cluster is an "LLM cluster" if > 50% of its U papers match the regex

CONTROLS_BASE = ["log_authors", "llm_topic"]
CONTROLS_EXP = ["max_prior_subs", "max_prior_accs", "share_new_authors", "last_prior_accs"]
EXP_MIN_YEAR = 2022  # author-experience covariates are interpretable from 2022 on

# --------------------------------------------------------------------------------------------
# primary_area crosswalk: 2024 labels -> 2025/26 labels (2025 and 2026 share one taxonomy)
# match_type: identical | renamed (same scope, new wording) | broadened (2025 label covers more) | judgement
# --------------------------------------------------------------------------------------------
AREA_CROSSWALK_2024 = {
    "representation learning for computer vision, audio, language, and other modalities":
        ("applications to computer vision, audio, language, and other modalities", "renamed"),
    "unsupervised, self-supervised, semi-supervised, and supervised representation learning":
        ("unsupervised, self-supervised, semi-supervised, and supervised representation learning", "identical"),
    "general machine learning (i.e., none of the above)":
        ("other topics in machine learning (i.e., none of the above)", "renamed"),
    "generative models": ("generative models", "identical"),
    "reinforcement learning": ("reinforcement learning", "identical"),
    "societal considerations including fairness, safety, privacy":
        ("alignment, fairness, safety, privacy, and societal considerations", "broadened"),
    "transfer learning, meta learning, and lifelong learning":
        ("transfer learning, meta learning, and lifelong learning", "identical"),
    "applications to physical sciences (physics, chemistry, biology, etc.)":
        ("applications to physical sciences (physics, chemistry, biology, etc.)", "identical"),
    "optimization": ("optimization", "identical"),
    "datasets and benchmarks": ("datasets and benchmarks", "identical"),
    "visualization or interpretation of learned representations":
        ("interpretability and explainable AI", "broadened"),
    "learning theory": ("learning theory", "identical"),
    "learning on graphs and other geometries & topologies":
        ("learning on graphs and other geometries & topologies", "identical"),
    "applications to robotics, autonomy, planning": ("applications to robotics, autonomy, planning", "identical"),
    "probabilistic methods (Bayesian methods, variational inference, sampling, UQ, etc.)":
        ("probabilistic methods (Bayesian methods, variational inference, sampling, UQ, etc.)", "identical"),
    "applications to neuroscience & cognitive science":
        ("applications to neuroscience & cognitive science", "identical"),
    "causal reasoning": ("causal reasoning", "identical"),
    "neurosymbolic & hybrid AI systems (physics-informed, logic & formal reasoning, etc.)":
        ("neurosymbolic & hybrid AI systems (physics-informed, logic & formal reasoning, etc.)", "identical"),
    "infrastructure, software libraries, hardware, etc.":
        ("infrastructure, software libraries, hardware, systems, etc.", "renamed"),
    # No 2025/26 counterpart. Metric learning and sparse coding are representation-learning topics;
    # kernel learning is the odd one out. 26 papers in 2024; documented judgement call.
    "metric learning, kernel learning, and sparse coding":
        ("unsupervised, self-supervised, semi-supervised, and supervised representation learning", "judgement"),
}
# Short labels for the harmonised taxonomy (21 areas; two exist from 2025 only).
AREA_SHORT = {
    "applications to computer vision, audio, language, and other modalities": "applications CV/audio/language",
    "foundation or frontier models, including LLMs": "foundation/frontier models",
    "generative models": "generative models",
    "alignment, fairness, safety, privacy, and societal considerations": "alignment/fairness/safety",
    "unsupervised, self-supervised, semi-supervised, and supervised representation learning": "representation learning",
    "datasets and benchmarks": "datasets & benchmarks",
    "reinforcement learning": "reinforcement learning",
    "other topics in machine learning (i.e., none of the above)": "other ML",
    "applications to physical sciences (physics, chemistry, biology, etc.)": "physical sciences",
    "interpretability and explainable AI": "interpretability",
    "optimization": "optimization",
    "learning on graphs and other geometries & topologies": "graphs & geometry",
    "transfer learning, meta learning, and lifelong learning": "transfer/meta/lifelong",
    "learning theory": "learning theory",
    "learning on time series and dynamical systems": "time series",
    "applications to robotics, autonomy, planning": "robotics/planning",
    "probabilistic methods (Bayesian methods, variational inference, sampling, UQ, etc.)": "probabilistic methods",
    "applications to neuroscience & cognitive science": "neuroscience/cognitive",
    "causal reasoning": "causal reasoning",
    "neurosymbolic & hybrid AI systems (physics-informed, logic & formal reasoning, etc.)": "neurosymbolic",
    "infrastructure, software libraries, hardware, systems, etc.": "infrastructure",
}


def harmonise_area(area: pd.Series, year: pd.Series) -> pd.Series:
    """Map primary_area to the 2025/26 taxonomy. Missing ('' or NaN, i.e. pre-2024) stays NaN."""
    a = area.replace("", np.nan)
    m24 = year.eq(2024) & a.notna()
    out = a.copy()
    out[m24] = a[m24].map(lambda x: AREA_CROSSWALK_2024.get(x, (x, "unmapped"))[0])
    return out


def area_crosswalk_table(s: pd.DataFrame | None = None) -> pd.DataFrame:
    """Crosswalk rows (2024 labels -> harmonised; 2025/26 labels -> themselves) with paper counts."""
    if s is None:
        s = load_submissions()
    a = s.primary_area.replace("", np.nan)
    rows = []
    n24 = a[s.year.eq(2024)].value_counts()
    n25 = a[s.year.eq(2025)].value_counts()
    n26 = a[s.year.eq(2026)].value_counts()
    for lab24, (lab, kind) in AREA_CROSSWALK_2024.items():
        rows.append(dict(source_year="2024", source_label=lab24, harmonised_label=lab, match_type=kind,
                         n_source=int(n24.get(lab24, 0))))
    for lab in sorted(set(n25.index) | set(n26.index)):
        rows.append(dict(source_year="2025-2026", source_label=lab, harmonised_label=lab, match_type="identical",
                         n_source=int(n25.get(lab, 0) + n26.get(lab, 0))))
    t = pd.DataFrame(rows)
    t["harmonised_short"] = t.harmonised_label.map(AREA_SHORT)
    unmapped = set(n24.index) - set(AREA_CROSSWALK_2024)
    if unmapped:
        warnings.warn(f"2024 area labels missing from crosswalk: {unmapped}")
    t["exists_2024"] = t.harmonised_label.isin({v[0] for v in AREA_CROSSWALK_2024.values()})
    return t


# --------------------------------------------------------------------------------------------
# Universe, pools, periods
# --------------------------------------------------------------------------------------------
def nfkc(text: str | None) -> str:
    return unicodedata.normalize("NFKC", text or "").strip()


def pool_flags(s: pd.DataFrame) -> pd.DataFrame:
    """Pool and stage indicators for submission rows (any subset of submissions.csv columns + year)."""
    acc_pop = acceptance_population(s)
    adm, dec = s.administrative_status, s.decision
    out = pd.DataFrame(index=s.index)
    out["in_acc_pop"] = acc_pop
    out["ACC"] = acc_pop & dec.eq("accepted")
    out["REJ"] = acc_pop & dec.eq("rejected")
    out["WD"] = adm.eq("withdrawn")
    out["DR"] = adm.eq("desk_rejected")
    out["NA"] = out.REJ | out.WD | out.DR
    # PLAN §0: the 349 post-decision withdrawals in 2026 (decision 'rejected') are flagged wd_post.
    out["wd_post"] = out.WD & dec.eq("rejected") & s.year.eq(2026)
    # Descriptive: any withdrawn row carrying an accept/reject decision (all years; 642 rows incl. 2026's 349).
    out["wd_decided"] = out.WD & dec.isin(["accepted", "rejected"])
    # README: 27 accepted rows that are withdrawn (14) or desk-rejected (13); excluded from ACC/REJ automatically.
    out["inconsistent"] = adm.isin(["withdrawn", "desk_rejected"]) & dec.eq("accepted")
    out["pool"] = np.select([out.ACC, out.REJ, out.WD, out.DR], ["ACC", "REJ", "WD", "DR"], "OTHER")
    # D4 stages: s0 = U; s1 = not desk-rejected; s2 = s1 and not withdrawn before decision
    # (wd_post rows stay in s2 as rejected); s3 = accepted.
    out["stage_s1"] = ~out.DR
    out["stage_s2"] = out.stage_s1 & (~out.WD | out.wd_post)
    out["stage_s3"] = out.ACC
    return out


def period_columns(year: pd.Series) -> pd.DataFrame:
    return pd.DataFrame({
        "post": (year >= BREAK_YEAR).astype(int),
        "t": (year - 2023).astype(int),
        "period": np.where(year >= BREAK_YEAR, "post", "pre"),
    }, index=year.index)


def year_mask(year: pd.Series, which: str) -> pd.Series:
    """Boolean mask for named year sets: all, pre, pre_wd, post, post_excl2026, no2019, 2018plus, early, late."""
    sets = {
        "all": YEARS, "pre": PRE, "pre_wd": PRE_WD, "post": POST, "post_excl2026": POST_EXCL_2026,
        "no2019": tuple(y for y in YEARS if y != 2019), "2018plus": tuple(range(2018, 2027)),
        "excl2026": tuple(range(2017, 2026)), "early": EARLY, "late": LATE,
    }
    if which not in sets:
        raise KeyError(f"unknown year set {which!r}; choose from {sorted(sets)}")
    return year.isin(sets[which])


def rx_contains(s: pd.Series, pattern: str, flags: int = 0) -> pd.Series:
    """Python-`re` search on a string Series. Use this instead of Series.str.contains: pandas 3 string columns
    are pyarrow-backed and .str.contains/.str.extract then use RE2, whose semantics differ (no look-behind,
    no \\u escapes, ASCII \\b)."""
    import re
    rx = re.compile(pattern, flags)
    return pd.Series([rx.search(x) is not None for x in s.fillna("").astype(str)], index=s.index, dtype=bool)


def rx_extract(s: pd.Series, pattern: str, group: int = 1, flags: int = 0) -> pd.Series:
    """First match of `group` (Python re); NaN where no match."""
    import re
    rx = re.compile(pattern, flags)
    out = []
    for x in s.fillna("").astype(str):
        m = rx.search(x)
        out.append(m.group(group) if m else np.nan)
    return pd.Series(out, index=s.index, dtype=object)


def rx_count(s: pd.Series, pattern: str, flags: int = 0) -> pd.Series:
    import re
    rx = re.compile(pattern, flags)
    return pd.Series([len(rx.findall(x)) for x in s.fillna("").astype(str)], index=s.index, dtype=int)


def llm_regex_flag(title: pd.Series, abstract: pd.Series) -> pd.Series:
    import re
    return rx_contains(title.fillna("") + " " + abstract.fillna(""), LLM_TOPIC_REGEX, re.IGNORECASE)


def llm_clusters(topic: pd.Series, llm_regex: pd.Series, threshold: float = LLM_CLUSTER_THRESHOLD) -> list[int]:
    """Topic ids whose share of regex-LLM papers exceeds `threshold` (computed on the rows given)."""
    share = llm_regex.astype(float).groupby(topic).mean()
    return sorted(int(k) for k in share.index[share > threshold])


def placeholder_reason(title: str, abstract: str) -> str:
    t = (title or "").strip()
    if nfkc(t) == "":
        return "empty_title"
    if t.lower() in F.PLACEHOLDER_TITLES:
        return "placeholder_title"
    if len((abstract or "").split()) < 20:
        return "short_abstract"
    return ""


def build_universe() -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Return (universe rows, per-year counts table, llm-cluster metadata)."""
    s = load_submissions()
    s["emb_row"] = np.arange(len(s))
    ids = np.load(CACHE / "embedding_ids.npy", allow_pickle=True)
    assert (ids == s.submission_id.to_numpy()).all(), "embedding_ids.npy is not aligned to submissions order"
    reason = pd.Series([placeholder_reason(t, a) for t, a in zip(s.title.fillna(""), s.abstract.fillna(""))],
                       index=s.index)
    # Cross-check with features.is_placeholder (the plan's definition).
    isph = pd.Series([F.is_placeholder(t, a) for t, a in zip(s.title.fillna(""), s.abstract.fillna(""))], index=s.index)
    assert (isph | reason.eq("empty_title")).eq(reason.ne("")).all()
    in_u = reason.eq("")

    pf = pool_flags(s)
    counts = pd.DataFrame({
        "n_rows": s.groupby("year").size(),
        "drop_empty_title": reason.eq("empty_title").groupby(s.year).sum(),
        "drop_placeholder_title": reason.eq("placeholder_title").groupby(s.year).sum(),
        "drop_short_abstract": reason.eq("short_abstract").groupby(s.year).sum(),
    })
    counts["n_dropped"] = counts[["drop_empty_title", "drop_placeholder_title", "drop_short_abstract"]].sum(axis=1)
    counts["n_U"] = in_u.groupby(s.year).sum()
    for p in ["ACC", "REJ", "WD", "DR", "NA", "wd_post", "wd_decided", "inconsistent"]:
        counts[f"n_{p}"] = (pf[p] & in_u).groupby(s.year).sum()
    counts["n_OTHER"] = (pf.pool.eq("OTHER") & in_u).groupby(s.year).sum()
    counts.loc["total"] = counts.sum()
    counts = counts.astype(int)

    u = s[in_u].copy()
    pfu = pf[in_u]
    out = pd.DataFrame({
        "submission_id": u.submission_id.values,
        "year": u.year.values.astype(int),
        "emb_row": u.emb_row.values.astype(int),
        "title": u.title.fillna("").values,
        "title_nfkc": u.title.fillna("").map(nfkc).values,
        "abstract": u.abstract.fillna("").values,
        "administrative_status": u.administrative_status.values,
        "decision": u.decision.values,
        "outcome_eligible": u.outcome_eligible.values.astype(int),
        "primary_area": u.primary_area.replace("", np.nan).values,
        "normalized_keywords_json": u.normalized_keywords_json.values,
        "declared_name_count": u.declared_name_count.values.astype(int),
        "review_count": u.review_count.values,
    })
    out["area_h"] = harmonise_area(pd.Series(out.primary_area), pd.Series(out.year)).values
    out["area_short"] = out.area_h.map(AREA_SHORT)
    for c in pfu.columns:
        out[c] = pfu[c].values
    out = pd.concat([out, period_columns(out.year)], axis=1)
    out["log_authors"] = np.log(out.declared_name_count.clip(lower=1))

    # Topics (MiniLM KMeans from cache; fitted on all 43,516 rows) and LLM flags.
    tp = pd.read_parquet(CACHE / "topics.parquet")
    out = out.merge(tp, on="submission_id", how="left", validate="1:1")
    out["llm_regex"] = llm_regex_flag(out.title, out.abstract).values
    tf = pd.read_parquet(CACHE / "title_features.parquet", columns=["submission_id", "llm_topic"])
    chk = out[["submission_id", "llm_regex"]].merge(tf, on="submission_id")
    assert (chk.llm_regex == chk.llm_topic).all(), "llm regex differs from cache/title_features.llm_topic"
    clus100 = llm_clusters(out.topic100, out.llm_regex)
    clus50 = llm_clusters(out.topic50, out.llm_regex)
    out["llm_cluster"] = out.topic100.isin(clus100)
    out["llm_topic"] = out.llm_regex | out.llm_cluster
    out["non_llm"] = ~out.llm_topic

    # Author covariates (exact declared-ID keys; see author_features.py).
    af = pd.read_parquet(CACHE / "author_features.parquet").drop(columns="year")
    out = out.merge(af, on="submission_id", how="left", validate="1:1")
    for c in ["max_prior_subs", "max_prior_accs", "last_prior_accs", "last_prior_subs", "first_prior_subs",
              "sum_prior_accs"]:
        out[f"l{c}"] = np.log1p(out[c])
    out["exp_valid"] = out.year >= EXP_MIN_YEAR

    share = out.groupby("topic100").llm_regex.mean()
    meta = {
        "threshold": LLM_CLUSTER_THRESHOLD,
        "regex": LLM_TOPIC_REGEX,
        "computed_on": "universe U, all years 2017-2026",
        "topic100_minilm_llm_clusters": clus100,
        "topic100_regex_share": {int(k): round(float(v), 4) for k, v in share.sort_values(ascending=False).items()},
        "topic50_minilm_llm_clusters": clus50,
    }
    return out, counts, meta


# --------------------------------------------------------------------------------------------
# Loaders for downstream scripts
# --------------------------------------------------------------------------------------------
def load_universe(columns: Sequence[str] | None = None) -> pd.DataFrame:
    return pd.read_parquet(UNIVERSE_PATH, columns=list(columns) if columns else None)


def load_features(columns: Sequence[str] | None = None) -> pd.DataFrame:
    cols = list(columns) if columns else None
    if cols is not None and "submission_id" not in cols:
        cols = ["submission_id"] + cols
    return pd.read_parquet(FEATURES_PATH, columns=cols)


def load_topics_bge() -> pd.DataFrame:
    return pd.read_parquet(TOPICS_BGE_PATH)


def load_analysis_frame(feature_cols: Sequence[str] | None = None, universe_cols: Sequence[str] | None = None,
                        with_bge_topics: bool = False) -> pd.DataFrame:
    """Universe (all or selected columns) merged 1:1 with features_v2 (all or selected) and optionally bge topics."""
    u = load_universe(universe_cols)
    if "submission_id" not in u.columns:
        raise ValueError("universe_cols must include submission_id")
    f = load_features(feature_cols)
    f = f.drop(columns=[c for c in f.columns if c in u.columns and c != "submission_id"])
    df = u.merge(f, on="submission_id", how="left", validate="1:1")
    if with_bge_topics:
        df = df.merge(load_topics_bge(), on="submission_id", how="left", validate="1:1")
    return df


def load_embedding(df: pd.DataFrame, field: str = "abstract", model: str = "bge-small-en-v1.5") -> np.ndarray:
    """float32 cache embedding rows aligned to df (uses df.emb_row). model: bge-small-en-v1.5 | all-MiniLM-L6-v2."""
    E = np.load(CACHE / f"emb_{field}_{model}.npy", mmap_mode="r")
    return np.asarray(E[df.emb_row.to_numpy()], dtype=np.float32)


def load_masked_embedding(df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """Name-masked bge abstract embeddings aligned to df; returns (E, found) with zero rows where not embedded."""
    E = np.load(MASKED_EMB_PATH, mmap_mode="r")
    ids = np.load(MASKED_IDS_PATH, allow_pickle=True)
    pos = pd.Series(np.arange(len(ids)), index=ids)
    p = pos.reindex(df.submission_id.to_numpy())
    found = p.notna().to_numpy()
    out = np.zeros((len(df), E.shape[1]), dtype=np.float32)
    out[found] = E[p[found].astype(int).to_numpy()]
    return out, found


def controls(df: pd.DataFrame, experience: bool = False, log_counts: bool = True) -> list[str]:
    """Control column names per PLAN §0 (title length is never a control in trend models).

    experience=True adds author experience (only valid for year >= 2022; raises if earlier years present).
    log_counts=True uses log1p versions of the count covariates (columns l<name>).
    """
    cols = list(CONTROLS_BASE)
    if experience:
        if (df.year < EXP_MIN_YEAR).any():
            raise ValueError("author-experience controls are defined for 2022+ only (PLAN §0)")
        exp = [("l" + c) if (log_counts and c != "share_new_authors") else c for c in CONTROLS_EXP]
        cols += exp
    return cols


# --------------------------------------------------------------------------------------------
# Fixed-effects LPM: alternating-projection demeaning, cluster-robust SEs
# --------------------------------------------------------------------------------------------
try:  # thin optional wrapper; the in-house implementation below is always available
    import pyfixest as _pf  # type: ignore
    HAS_PYFIXEST = True
except Exception:  # pragma: no cover
    _pf = None
    HAS_PYFIXEST = False


def _codes(a) -> np.ndarray:
    return pd.factorize(pd.Series(np.asarray(a)), use_na_sentinel=False)[0]


def demean(X: np.ndarray, fe: Sequence[np.ndarray], weights: np.ndarray | None = None, tol: float = 1e-10,
           maxiter: int = 10_000) -> np.ndarray:
    """Within-transform columns of X for one or more FE dimensions by alternating projections.

    fe: list of 1-D arrays of group labels (any dtype). Exact in one sweep for a single FE.
    weights: optional analytic weights (weighted group means).
    """
    from scipy import sparse
    X = np.asarray(X, dtype=float)
    one_d = X.ndim == 1
    X = X.reshape(len(X), -1).copy()
    if not fe:
        return X.ravel() if one_d else X
    n = X.shape[0]
    w = np.ones(n) if weights is None else np.asarray(weights, dtype=float)
    codes = [_codes(c) for c in fe]
    mats, cnts = [], []
    for c in codes:
        G = int(c.max()) + 1
        mats.append(sparse.csr_matrix((w, (np.arange(n), c)), shape=(n, G)).T.tocsr())
        cnts.append(np.bincount(c, weights=w, minlength=G))
    for it in range(maxiter):
        prev = X.copy() if len(codes) > 1 else None
        for c, M, cnt in zip(codes, mats, cnts):
            X -= (M @ X / cnt[:, None])[c]
        if prev is None or np.max(np.abs(X - prev)) < tol:
            break
    else:
        warnings.warn(f"demean: no convergence after {maxiter} sweeps")
    return X.ravel() if one_d else X


@dataclass
class FEResult:
    params: pd.Series
    se: pd.Series
    vcov: pd.DataFrame
    nobs: int
    df_resid: int
    vcov_type: str
    n_clusters: int | None = None
    fe: list = field(default_factory=list)
    r2_within: float = np.nan

    @property
    def tstat(self) -> pd.Series:
        return self.params / self.se

    @property
    def pvalue(self) -> pd.Series:
        from scipy import stats
        return pd.Series(2 * stats.t.sf(np.abs(self.tstat), self.df_resid), index=self.params.index)

    def conf_int(self, level: float = 0.95) -> pd.DataFrame:
        from scipy import stats
        q = stats.t.ppf(0.5 + level / 2, self.df_resid)
        return pd.DataFrame({"lo": self.params - q * self.se, "hi": self.params + q * self.se})

    def summary(self, level: float = 0.95) -> pd.DataFrame:
        ci = self.conf_int(level)
        return pd.DataFrame({"coef": self.params, "se": self.se, "t": self.tstat, "p": self.pvalue,
                             "lo": ci.lo, "hi": ci.hi}).assign(nobs=self.nobs, n_clusters=self.n_clusters,
                                                                vcov=self.vcov_type)


def feols(data: pd.DataFrame, y: str, x: Sequence[str], fe: Sequence[str] | None = None,
          cluster: str | None = None, weights: str | None = None, vcov: str | None = None,
          tol: float = 1e-10) -> FEResult:
    """OLS/LPM of y on numeric columns x, absorbing FE columns `fe` (labels; interact beforehand, e.g. via
    fe_interact), with CRV1 cluster-robust (default when `cluster` given), HC1 ('hetero') or 'iid' SEs.

    Small-sample correction follows fixest/pyfixest defaults: (N-1)/(N-K) * G/(G-1), where K counts the
    slopes plus FE levels not nested in the cluster variable; p-values use t(G-1) (cluster) or t(N-K).
    Rows with missing values in any used column are dropped.
    """
    fe = list(fe or [])
    x = list(x)
    used = [y] + x + fe + ([cluster] if cluster else []) + ([weights] if weights else [])
    d = data[list(dict.fromkeys(used))].dropna()
    n = len(d)
    w = d[weights].to_numpy(float) if weights else None
    Y = d[y].to_numpy(float)
    X = d[x].to_numpy(float) if x else np.empty((n, 0))
    names = list(x)
    if not fe:
        X = np.column_stack([np.ones(n), X])
        names = ["Intercept"] + names
        Yd, Xd = Y, X
    else:
        Z = demean(np.column_stack([Y, X]), [d[f].to_numpy() for f in fe], weights=w, tol=tol)
        Yd, Xd = Z[:, 0], Z[:, 1:]
    ww = np.ones(n) if w is None else w
    XtWX = Xd.T @ (Xd * ww[:, None])
    XtWX_inv = np.linalg.pinv(XtWX)
    beta = XtWX_inv @ (Xd.T @ (ww * Yd))
    e = Yd - Xd @ beta
    k = Xd.shape[1]
    # FE degrees of freedom (levels minus redundancies), excluding FE nested in clusters
    k_fe = 0
    if fe:
        cl = d[cluster].to_numpy() if cluster else None
        for j, f in enumerate(fe):
            lv = d[f].nunique()
            nested = cl is not None and (d.groupby(f)[cluster].nunique() <= 1).all()
            if not nested:
                k_fe += lv - (1 if j > 0 else 0)
    K = k + k_fe
    vtype = vcov or ("CRV1" if cluster else "iid")
    if vtype == "CRV1":
        if not cluster:
            raise ValueError("CRV1 requires cluster")
        g = _codes(d[cluster].to_numpy())
        G = int(g.max()) + 1
        S = Xd * (ww * e)[:, None]
        Sg = np.zeros((G, k))
        np.add.at(Sg, g, S)
        meat = Sg.T @ Sg
        adj = (n - 1) / (n - K) * G / (G - 1)
        V = adj * XtWX_inv @ meat @ XtWX_inv
        dfr = G - 1
        ncl = G
    elif vtype in ("hetero", "HC1"):
        S = Xd * (ww * e)[:, None]
        V = (n - 1) / (n - K) * XtWX_inv @ (S.T @ S) @ XtWX_inv
        dfr, ncl = n - K, None
    elif vtype == "iid":
        s2 = float((ww * e ** 2).sum() / (n - K))
        V = s2 * XtWX_inv
        dfr, ncl = n - K, None
    else:
        raise ValueError(f"unknown vcov {vtype}")
    se = np.sqrt(np.clip(np.diag(V), 0, None))
    tss = float((ww * (Yd - (np.average(Yd, weights=ww) if not fe else 0.0)) ** 2).sum())
    r2w = 1 - float((ww * e ** 2).sum()) / tss if tss > 0 else np.nan
    return FEResult(params=pd.Series(beta, index=names), se=pd.Series(se, index=names),
                    vcov=pd.DataFrame(V, index=names, columns=names), nobs=n, df_resid=dfr, vcov_type=vtype,
                    n_clusters=ncl, fe=fe, r2_within=r2w)


def fe_interact(*cols: pd.Series) -> pd.Series:
    """Label for an interacted FE (e.g. topic100 x year) as a single categorical column."""
    out = cols[0].astype(str)
    for c in cols[1:]:
        out = out + "|" + c.astype(str)
    return out


def pf_feols(fml: str, data: pd.DataFrame, vcov=None, **kw):
    """Thin pyfixest wrapper: pf_feols('y ~ x | topic100^year', df, vcov={'CRV1': 'topic100'})."""
    if not HAS_PYFIXEST:
        raise ImportError("pyfixest not installed; use feols()")
    return _pf.feols(fml, data=data, vcov=vcov, **kw)


# --------------------------------------------------------------------------------------------
# Logit helpers (statsmodels)
# --------------------------------------------------------------------------------------------
def logit(formula: str, data: pd.DataFrame, cluster: str | None = None, maxiter: int = 300,
          method: str = "newton", freq_weights: str | None = None):
    """Patsy-formula logit with cluster-robust SEs (statsmodels CRV, small-sample corrected).

    Rows with missing values in formula variables or the cluster column are dropped consistently.
    Falls back to BFGS when Newton fails (e.g. near-separation). Returns a statsmodels results object
    with `.model_rows` (index of rows used).
    """
    import patsy
    import statsmodels.api as sm
    d = data if cluster is None else data[data[cluster].notna()]
    yv, X = patsy.dmatrices(formula, d, return_type="dataframe", NA_action="drop")
    y = yv.iloc[:, 0]
    kw = {}
    if cluster is not None:
        kw = dict(cov_type="cluster", cov_kwds={"groups": _codes(d.loc[X.index, cluster].to_numpy())})
    if freq_weights is not None:
        mod = sm.GLM(y, X, family=sm.families.Binomial(), freq_weights=d.loc[X.index, freq_weights])
        res = mod.fit(maxiter=maxiter, **kw)
    else:
        mod = sm.Logit(y, X)
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                res = mod.fit(disp=0, maxiter=maxiter, method=method, **kw)
            if not res.mle_retvals.get("converged", True):
                raise RuntimeError("no convergence")
        except Exception:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                res = mod.fit(disp=0, maxiter=max(maxiter, 2000), method="bfgs", **kw)
    res.model_rows = X.index
    return res


def or_table(res, terms: Iterable[str] | None = None, level: float = 0.95) -> pd.DataFrame:
    """Tidy coefficient table with odds ratios and Wald CIs for selected terms (default: all but Intercept)."""
    ci = res.conf_int(alpha=1 - level)
    ci.columns = ["lo", "hi"]
    t = pd.DataFrame({"coef": res.params, "se": res.bse, "z": res.tvalues, "p": res.pvalues, "lo": ci.lo,
                      "hi": ci.hi})
    if terms is None:
        terms = [i for i in t.index if i != "Intercept"]
    t = t.loc[list(terms)]
    t["OR"], t["OR_lo"], t["OR_hi"] = np.exp(t.coef), np.exp(t.lo), np.exp(t.hi)
    t["nobs"] = int(res.nobs)
    return t


# --------------------------------------------------------------------------------------------
# Bootstraps
# --------------------------------------------------------------------------------------------
def _units(n: int, strata=None, clusters=None):
    unit = np.arange(n) if clusters is None else _codes(clusters)
    U = int(unit.max()) + 1
    if strata is None:
        ustr = np.zeros(U, dtype=int)
    else:
        sc = _codes(strata)
        ustr = np.full(U, -1)
        ustr[unit] = sc  # last write wins; check consistency below
        if clusters is not None and (ustr[unit] != sc).any():
            warnings.warn("clusters span several strata; each cluster is assigned to one stratum")
    return unit, U, ustr


def boot_weights(n: int, n_boot: int, strata=None, clusters=None, seed: int = 0,
                 chunk: int = 200) -> Iterator[np.ndarray]:
    """Yield (b x n) float32 frequency-weight matrices for a (stratified) paper or cluster bootstrap.

    Each replicate draws, within each stratum, as many units (rows or clusters) as the stratum holds,
    with replacement. Row weight = number of times its unit was drawn. Use with boot_means().
    """
    rng = np.random.default_rng(seed)
    unit, U, ustr = _units(n, strata, clusters)
    groups = [np.where(ustr == s)[0] for s in np.unique(ustr)]
    done = 0
    while done < n_boot:
        b = min(chunk, n_boot - done)
        Wu = np.zeros((b, U), dtype=np.float32)
        for members in groups:
            m = len(members)
            Wu[:, members] = rng.multinomial(m, np.full(m, 1.0 / m), size=b)
        yield Wu[:, unit]
        done += b


def boot_means(values: np.ndarray, n_boot: int = 2000, strata=None, clusters=None, seed: int = 0,
               chunk: int = 200) -> np.ndarray:
    """Bootstrap distribution (n_boot x k) of column means of `values` (n x k; NaN = missing)."""
    V = np.asarray(values, dtype=float)
    V = V.reshape(len(V), -1)
    M = ~np.isnan(V)
    V0 = np.where(M, V, 0.0)
    out = []
    for W in boot_weights(len(V), n_boot, strata, clusters, seed, chunk):
        out.append((W @ V0) / np.maximum(W @ M, 1e-12))
    return np.vstack(out)


def boot_indices(n: int, strata=None, clusters=None, rng: np.random.Generator | None = None) -> np.ndarray:
    """One bootstrap draw of row indices (stratified paper bootstrap, or cluster bootstrap within strata)."""
    rng = rng or np.random.default_rng()
    if clusters is None:
        if strata is None:
            return rng.integers(0, n, n)
        sc = _codes(strata)
        idx = []
        for s in np.unique(sc):
            rows = np.where(sc == s)[0]
            idx.append(rows[rng.integers(0, len(rows), len(rows))])
        return np.concatenate(idx)
    unit, U, ustr = _units(n, strata, clusters)
    order = np.argsort(unit, kind="stable")
    sizes = np.bincount(unit, minlength=U)
    starts = np.concatenate([[0], np.cumsum(sizes)[:-1]])
    drawn = []
    for s in np.unique(ustr):
        members = np.where(ustr == s)[0]
        drawn.append(members[rng.integers(0, len(members), len(members))])
    drawn = np.concatenate(drawn)
    lens = sizes[drawn]
    offs = np.repeat(starts[drawn] - np.concatenate([[0], np.cumsum(lens)[:-1]]), lens)
    return order[np.arange(lens.sum()) + offs]


def bootstrap(data: pd.DataFrame, stat: Callable[[pd.DataFrame], float | np.ndarray], n_boot: int = 1000,
              strata: str | None = None, cluster: str | None = None, seed: int = 0) -> np.ndarray:
    """Generic bootstrap: stat(resampled DataFrame) for n_boot draws; returns (n_boot,) or (n_boot, k)."""
    rng = np.random.default_rng(seed)
    st = data[strata].to_numpy() if strata else None
    cl = data[cluster].to_numpy() if cluster else None
    out = [np.asarray(stat(data.iloc[boot_indices(len(data), st, cl, rng)]), dtype=float)
           for _ in range(n_boot)]
    return np.array(out)


def percentile_ci(samples: np.ndarray, level: float = 0.95) -> tuple[np.ndarray, np.ndarray]:
    a = (1 - level) / 2
    return np.nanquantile(samples, a, axis=0), np.nanquantile(samples, 1 - a, axis=0)


def boot_summary(est, samples: np.ndarray, level: float = 0.95) -> pd.DataFrame:
    lo, hi = percentile_ci(samples, level)
    est = np.atleast_1d(np.asarray(est, dtype=float))
    return pd.DataFrame({"est": est, "se": np.atleast_1d(np.nanstd(samples, axis=0, ddof=1)),
                         "lo": np.atleast_1d(lo), "hi": np.atleast_1d(hi),
                         "p_le0": np.atleast_1d(np.nanmean(np.asarray(samples) <= 0, axis=0))})


# --------------------------------------------------------------------------------------------
# Centroid assignment (held-out topics from frozen discovery centroids)
# --------------------------------------------------------------------------------------------
def assign_centroids(E: np.ndarray, C: np.ndarray, chunk: int = 20000) -> np.ndarray:
    """Nearest centroid (Euclidean, as in KMeans) for rows of E."""
    E = np.asarray(E, dtype=np.float32)
    C = np.asarray(C, dtype=np.float32)
    cn = (C ** 2).sum(1)
    out = np.empty(len(E), dtype=int)
    for i in range(0, len(E), chunk):
        out[i:i + chunk] = np.argmin(cn[None, :] - 2 * E[i:i + chunk] @ C.T, axis=1)
    return out


def load_centroids(name: str) -> np.ndarray:
    """name in outputs/topics/centroids.npz: bge_k50, bge_k100, minilm_k50, minilm_k100."""
    return np.load(CENTROIDS_PATH)[name]


# --------------------------------------------------------------------------------------------
# Figures (paper style)
# --------------------------------------------------------------------------------------------
BG = "#ffffff"
TEXT = "#0b0b0b"
TEXT2 = "#52514e"
GRID = "#e6e5e1"
GREY = "#8a8984"  # controls / reference series
COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
COLOR_NAMES = ["blue", "orange", "aqua", "yellow", "magenta", "green", "violet", "red"]
DIVERGING = ("#2a78d6", "#f0efec", "#e34948")
SINGLE_W, DOUBLE_W = 3.4, 7.0


def color(i: int) -> str:
    """i-th categorical colour in the fixed order; never cycles."""
    if i >= len(COLORS):
        raise IndexError("more than 8 categorical series: aggregate or facet instead of cycling colours")
    return COLORS[i]


def set_style():
    import logging
    import matplotlib as mpl
    logging.getLogger("fontTools").setLevel(logging.WARNING)
    from matplotlib import font_manager
    fams = {f.name for f in font_manager.fontManager.ttflist}
    sans = [f for f in ["Inter", "DejaVu Sans", "Arial", "Helvetica"] if f in fams] or ["sans-serif"]
    mpl.rcParams.update({
        "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG, "savefig.edgecolor": BG,
        "font.family": "sans-serif", "font.sans-serif": sans, "font.size": 8.5,
        "axes.titlesize": 9, "axes.labelsize": 8.5, "xtick.labelsize": 8, "ytick.labelsize": 8,
        "legend.fontsize": 8, "legend.frameon": False,
        "text.color": TEXT, "axes.labelcolor": TEXT, "axes.titlecolor": TEXT, "axes.edgecolor": TEXT2,
        "xtick.color": TEXT2, "ytick.color": TEXT2, "xtick.labelcolor": TEXT, "ytick.labelcolor": TEXT,
        "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": 0.6,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
        "lines.linewidth": 2.0, "lines.markersize": 5.0, "patch.linewidth": 0,
        "axes.prop_cycle": mpl.cycler(color=COLORS),
        "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.dpi": 300, "savefig.bbox": "tight",
        "figure.dpi": 100,
    })


def new_fig(width: str | float = "single", height: float | None = None, nrows: int = 1, ncols: int = 1, **kw):
    """Figure at single (3.4in) or double (7in) column width with the paper style applied."""
    import matplotlib.pyplot as plt
    set_style()
    w = {"single": SINGLE_W, "double": DOUBLE_W}.get(width, width)
    h = height if height is not None else w * (0.68 if w <= SINGLE_W else 0.42)
    return plt.subplots(nrows, ncols, figsize=(w, h), **kw)


def label_end(ax, x, y, text: str, color_: str, dx: float = 0.15, dy: float = 0.0, **kw):
    """Direct label at the end of a series (x, y = last point)."""
    ax.annotate(text, (x, y), xytext=(x + dx, y + dy), textcoords="data", color=color_, va="center",
                ha="left", fontsize=kw.pop("fontsize", 8), annotation_clip=False, **kw)


def forest(ax, labels: Sequence[str], est, lo, hi, ref: float | None = 1.0, log: bool = True,
           colors: Sequence[str] | str | None = None, marker: str = "o"):
    """Horizontal forest plot (top-to-bottom in label order)."""
    est, lo, hi = map(lambda a: np.asarray(a, dtype=float), (est, lo, hi))
    ypos = np.arange(len(labels))[::-1]
    cols = [colors] * len(labels) if isinstance(colors, str) or colors is None else list(colors)
    cols = [c or COLORS[0] for c in cols]
    for yv, e, l_, h, c in zip(ypos, est, lo, hi, cols):
        ax.plot([l_, h], [yv, yv], color=c, lw=1.6, solid_capstyle="butt")
        ax.plot([e], [yv], marker=marker, color=c, ms=5.5, lw=0)
    if ref is not None:
        ax.axvline(ref, color=GREY, lw=0.8, ls="--", zorder=0)
    if log:
        ax.set_xscale("log")
    ax.set_yticks(ypos, labels)
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)
    return ax


def diverging_cmap(name: str = "blue_grey_red"):
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list(name, list(DIVERGING))


def save_fig(fig, name: str, folder: str | Path, data: pd.DataFrame | dict | None = None, close: bool = True) -> dict:
    """Write <folder>/<name>.pdf, .png (300 dpi) and .csv (plotted data). Relative folders live under outputs/."""
    import matplotlib.pyplot as plt
    folder = Path(folder)
    if not folder.is_absolute():
        folder = OUT / folder
    folder.mkdir(parents=True, exist_ok=True)
    paths = {}
    for ext in ("pdf", "png"):
        p = folder / f"{name}.{ext}"
        fig.savefig(p, dpi=300, facecolor=BG)
        paths[ext] = p
    if data is None:
        warnings.warn(f"save_fig({name}): no plotted data given; CSV not written")
    elif isinstance(data, dict):
        for k, v in data.items():
            p = folder / f"{name}__{k}.csv"
            pd.DataFrame(v).to_csv(p, index=False)
            paths[f"csv_{k}"] = p
    else:
        p = folder / f"{name}.csv"
        pd.DataFrame(data).to_csv(p, index=False)
        paths["csv"] = p
    if close:
        plt.close(fig)
    return paths


# --------------------------------------------------------------------------------------------
def main():
    CORE.mkdir(parents=True, exist_ok=True)
    u, counts, meta = build_universe()
    u.to_parquet(UNIVERSE_PATH, index=False)
    counts.to_csv(CORE / "universe_counts.csv")
    cw = area_crosswalk_table()
    cw.to_csv(CORE / "area_crosswalk.csv", index=False)
    (CORE / "llm_clusters.json").write_text(json.dumps(meta, indent=1))
    print("universe", u.shape)
    print(counts.to_string())
    print("llm clusters (topic100, MiniLM):", meta["topic100_minilm_llm_clusters"])
    print(u.groupby("year")[["llm_regex", "llm_cluster", "llm_topic"]].mean().round(3).to_string())
    print(cw[["source_year", "match_type"]].value_counts().to_string())


if __name__ == "__main__":
    main()
