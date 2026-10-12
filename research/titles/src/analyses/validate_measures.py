"""WP3b: measurement validation (PLAN.md section 3, V1-V6).

Reads the blind annotation passes (outputs/validation/labels/), the private item keys (outputs/validation/keys/),
the frozen features/topics, and writes outputs/validation/{VALIDATION.md, validation.json, slot_variants_dropped.json,
topic100_labels.csv, v*_*.csv, fig_*}.

V1  NAME / compound / orthography / casing detectors
    - Cohen's kappa between pass A (codebook A) and pass B (codebook B) for every label, item-bootstrap CIs.
    - Consensus = the label both passes gave. Disagreements are adjudicated by the PI's delegate from the title text
      alone, under a stated rule (ADJ_RULE_V1), and every adjudication is recorded (v1_adjudications.csv).
    - 150 agreed items drawn at random are spot-checked by the adjudicator (v1_spotcheck.csv) to estimate the
      consensus error.
    - Detector precision / recall / specificity per year block, design-weighted (Horvitz-Thompson ratio estimators
      with the sampling weights N_h/n_h of the main stratified sample; the 200 hard cases are reported separately
      because they are not a probability sample of a separate population). CIs: stratified bootstrap within
      sampling strata (2,000 reps).
    - Rogan-Gladen corrected yearly prevalence with block-specific Se/Sp.
    - The D1 ITS (segmented logit, topic100 FE, log authors, llm_topic, CRV1 by topic100) refitted by maximum
      likelihood under block-specific non-differential misclassification
          P(observed NAME = 1 | x) = (1 - Sp_b) + (Se_b + Sp_b - 1) * expit(x'beta),
      with validation-sample uncertainty propagated by refitting on 200 bootstrap draws of (Se_b, Sp_b).
V2  Slot sense precision and swap preservation per slot word; words with design-weighted sense precision < 0.85
    are listed in slot_variants_dropped.json (D3 reads it).
V3  LLM-polish ratings vs F24/F26 fingerprints (weak convergent validity only); fingerprint rates in 2021-22
    (pre-ChatGPT false-positive rates); manual inspection of 100 U+2011 / en-dash title hits.
V4  Name-masking leakage: lead strings surviving the R3 and R1 masks in NAME-paper abstracts (target 0%), and the
    masked-vs-unmasked AUC gap read from D1's T1_2_representations.csv.
V5  topic100 cluster labels table; annotator LM flag vs the regex-based LLM-cluster flag; MiniLM vs bge ARI/NMI;
    10 clusters checked manually.
V6  Papers per declared profile key and year, keys with > 40 papers in a year, alias sensitivity (trailing digits
    stripped), email-key vs profile-key eras.

Language: declared IDs are "declared profile keys", not people. Acceptance results are associational.

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.validate_measures
"""
from __future__ import annotations

import glob
import hashlib
import json
import re
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import expit
from sklearn.metrics import adjusted_rand_score, cohen_kappa_score, normalized_mutual_info_score

from analyses import _core as C

VAL = C.OUT / "validation"
LAB = VAL / "labels"
KEYS = VAL / "keys"
BAT = VAL / "batches"
SEED = 20261011
N_BOOT = 2000
N_BOOT_ITS = 200
BLOCKS = ["2017-19", "2020-22", "2023", "2024", "2025", "2026"]
V1_LABELS = ["compound", "lead_type", "lead_orthography", "casing", "question"]
T0 = time.time()


def log(msg: str):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def year_block(y: int) -> str:
    return "2017-19" if y <= 2019 else "2020-22" if y <= 2022 else str(int(y))


# =====================================================================================================
# Adjudications and manual checks (recorded by the PI's delegate, from the title / cluster text only)
# =====================================================================================================
ADJ_RULE_V1 = (
    "lead_type: a lead is coined_name when it is, or is headed by, a proper-noun-like label: an invented or blended "
    "word or acronym, a dictionary word used as the name of one specific artefact (including existing techniques), "
    "a phrase followed by its parenthesised acronym or its own symbol, or a non-literal noun phrase that the subtitle "
    "presents as the paper's artefact. A lead made of ordinary words in their ordinary or standard technical senses "
    "is descriptive_phrase even when it is the paper's method name ('method description' in codebook A, 'approach "
    "in ordinary language' in codebook B), as is a lead in which a pre-existing name or family abbreviation only "
    "modifies a generic head (codebook A: 'LoRA Fine-Tuning at Scale'). Metaphors, puns and allusions that the "
    "subtitle does not present as an artefact are slogans (descriptive_phrase). This matches 239 of the 255 agreed "
    "plain multi-word leads (both passes descriptive). orthography: the codebook's ordered rules applied to the name "
    "(an initial article is not part of the name). casing: tokens the authors treat as names (coined names, acronym "
    "expansions, established architecture names) are set aside; field and family terms are counted."
)

# item_id -> {label: adjudicated value, ..., 'why': reason}
ADJ_V1: dict[str, dict] = {
    "v1_1b5bde8f": dict(lead_type="coined_name", lead_orthography="mixed_case",
                        why="phrase followed by the metric's own symbol d_Eig, analogous to a parenthesised acronym"),
    "v1_abcb460a": dict(lead_type="descriptive_phrase", why="pre-existing name LoRA only modifies the generic head 'Recycle'"),
    "v1_64884465": dict(lead_type="descriptive_phrase", why="metaphor; the subtitle does not present it as an artefact"),
    "v1_28588c16": dict(lead_type="descriptive_phrase", why="literary allusion naming two things; slogan, not one artefact"),
    "v1_e1e7f9ff": dict(lead_type="descriptive_phrase", why="pun on the theme; subtitle frames a measurement study"),
    "v1_aa770aec": dict(casing="sentence_case", why="'Linear Concept Activation Vectors' expands the coined acronym; other content words lower case"),
    "v1_fdd8a67c": dict(lead_type="descriptive_phrase", why="catchy phrase; subtitle frames an analysis, not an artefact"),
    "v1_bafba3fc": dict(lead_type="coined_name", lead_orthography="word",
                        why="dictionary word used as the name of one specific technique; both codebooks count existing artefact names"),
    "v1_1719c904": dict(lead_type="descriptive_phrase", why="ordinary-word description of the approach"),
    "v1_2e72fe40": dict(lead_type="descriptive_phrase", why="eponymous adjective + generic noun; standard technical sense"),
    "v1_6ad48198": dict(lead_type="descriptive_phrase", why="model class described in ordinary technical words"),
    "v1_567f15aa": dict(lead_orthography="word", why="the name is 'Predictron'; the article is not part of its shape"),
    "v1_fad16cf4": dict(casing="sentence_case", why="paren-acronym name set aside; the remainder is lower case"),
    "v1_65da253b": dict(lead_type="descriptive_phrase", why="standard technical terms (successor representation, options)"),
    "v1_ccc84513": dict(lead_orthography="word", why="only the initial letter is a capital and there is no digit (rule 4)"),
    "v1_069559b0": dict(lead_type="descriptive_phrase", why="ordinary modifier + family abbreviation VAE"),
    "v1_801cbc3d": dict(lead_type="descriptive_phrase", why="the name APL only modifies the generic head 'Activations'"),
    "v1_507a0b20": dict(lead_type="descriptive_phrase", why="ordinary modifier + family abbreviation CNNs"),
    "v1_6e1822b9": dict(casing="title_case", why="6 of 8 content words capitalised (75%)"),
    "v1_a6abc8af": dict(lead_type="descriptive_phrase", casing="other",
                        why="ordinary technical words; as a non-name its capitals count: 3 of 5 content words capitalised"),
    "v1_cd4c8f70": dict(lead_type="coined_name", lead_orthography="mixed_case",
                        why="lead headed by the coined token Param-Delta (head, not modifier)"),
    "v1_4a763f5f": dict(casing="sentence_case", why="capitals only in the acronym expansion; rest lower case"),
    "v1_3a4963d6": dict(lead_type="coined_name", lead_orthography="mixed_case",
                        why="non-literal noun phrase the subtitle presents as the evaluation artefact (cf. agreed 'Balance Beam')"),
    "v1_13ed5042": dict(casing="other", why="2 of 6 content words capitalised; 'Semi-Supervised Learning' is a field term"),
    "v1_d0395f53": dict(lead_type="descriptive_phrase", why="ordinary technical words + family noun"),
    "v1_b9b8ae34": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_2172e006": dict(lead_orthography="word", why="one letter + '*': not all_caps (needs 2 letters), no inner capital, digit or LaTeX"),
    "v1_58883824": dict(casing="other", why="only 'Double' is judgeable after setting aside the first word and Q-learning"),
    "v1_8bee6fe0": dict(lead_type="descriptive_phrase", why="technical extension of sum-product networks in ordinary words"),
    "v1_31157597": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_0c71c510": dict(lead_type="descriptive_phrase", why="algorithm described in ordinary technical words"),
    "v1_c389bd3b": dict(casing="other", why="lead sentence case, subtitle title case; 2 of 4 non-name words capitalised"),
    "v1_998213c3": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_a06eccd6": dict(lead_type="descriptive_phrase", why="ordinary technical words (Schroedinger bridge variant)"),
    "v1_3835b33d": dict(lead_type="descriptive_phrase", why="ordinary words + generic 'Networks'"),
    "v1_fddb4575": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_8f31224d": dict(casing="sentence_case", why="paren-acronym name set aside; remainder lower case"),
    "v1_9c51549e": dict(lead_orthography="all_caps", why="rule 2 precedes rule 3: all letters capital, digit/caret ignored (as P$^2$-DPO in both passes)"),
    "v1_a9682827": dict(lead_type="coined_name", lead_orthography="mixed_case",
                        why="head ECE names one specific metric; 'Smooth' modifies it"),
    "v1_958fcc75": dict(lead_type="descriptive_phrase", why="ordinary modifier + family abbreviation DGN"),
    "v1_b19f19f0": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_c7d6bdd5": dict(lead_type="descriptive_phrase", why="ordinary technical words (herding is a technical term)"),
    "v1_8f127ed7": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_a58233c8": dict(lead_type="descriptive_phrase", why="eponymous modifier + family abbreviation PINNs"),
    "v1_e8859b79": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_6960bde2": dict(lead_type="descriptive_phrase", why="ordinary technical words (a setting/framework)"),
    "v1_0c68be39": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_53569758": dict(lead_type="coined_name", lead_orthography="mixed_case",
                        why="non-literal coinage the subtitle presents as a method (cf. agreed 'Balance Beam')"),
    "v1_9d84962c": dict(lead_type="descriptive_phrase", why="eponymous modifier + generic 'layers'"),
    "v1_bb735b58": dict(lead_type="descriptive_phrase", why="technical term (forcing) in ordinary words"),
    "v1_dd0f9f27": dict(casing="sentence_case", why="'Capsule Networks' is an established architecture name; rest lower case"),
    "v1_d730cb95": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_fd97bc80": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_b1c7cb4a": dict(lead_type="descriptive_phrase", why="ordinary technical words (switch gating)"),
    "v1_0140c3fe": dict(lead_type="descriptive_phrase", why="ordinary words + generic 'Networks'"),
    "v1_a53581ca": dict(lead_type="descriptive_phrase", why="ordinary words describing the framework"),
    "v1_622b8ffc": dict(lead_type="descriptive_phrase", why="ordinary technical words"),
    "v1_46c2c491": dict(lead_type="descriptive_phrase", why="pre-existing abbreviation CoT modifies the generic head 'Vectors'"),
}

# Spot check of 150 agreed V1 items (random, seed SPOT_SEED). Verdicts other than 'ok' are listed here;
# 'error' = consensus clearly wrong under the codebooks + ADJ_RULE_V1; 'borderline' = defensible either way.
SPOT_SEED = 20261012
SPOT_V1: dict[str, tuple[str, str, str]] = {
    "v1_0e20d3b8": ("borderline", "lead_type", "'Countdown Regression': near-literal method description, agreed coined"),
    "v1_2ee99b17": ("borderline", "lead_type", "'LayerMix Law': coined token as modifier of 'Law'; agreed coined"),
    "v1_7218153c": ("borderline", "casing", "3 of 4 content words capitalised: exactly at the 75% line"),
    "v1_ccdb692a": ("borderline", "casing", "'Federated Architecture Search' may be the acronym expansion (then sentence_case)"),
    "v1_fcc7035f": ("borderline", "casing", "'General AI Assistants' may be a name (then sentence_case)"),
}

ADJ_V2: dict[str, dict] = {
    "v2_9ba17f1e": dict(slot_sense="n", swap_preserves="n", why="first word of the method name 'Unleashing Mask' (technical term)"),
    "v2_01be19c2": dict(slot_sense="n", swap_preserves="n", why="'by leveraging cascaded meta-models' reads as the boosting ensemble technique"),
    "v2_cbb613bc": dict(swap_preserves="n", why="'Unveiling subtokenization options' reads as presenting options, not evaluating them"),
    "v2_5bcc2043": dict(slot_sense="n", swap_preserves="n", why="harnessing a harmful effect (client drift) = controlling it, not using it"),
    "v2_1e7b0518": dict(swap_preserves="n", why="'Unveiling self-supervised representations' reads as introducing new representations"),
    "v2_86f62605": dict(slot_sense="y", why="gerund verb: making client needs understood; not the noun-task use"),
    "v2_b4c7a6da": dict(swap_preserves="n", why="'Improving exogenous data' reads as improving data quality, a different claim"),
    "v2_64955c3b": dict(swap_preserves="n", why="'Exploiting reasoning capability' = using an existing capability, not eliciting it"),
    "v2_895b347a": dict(swap_preserves="y", why="unveiling a known paradox through likelihood peaks still describes explaining it"),
    "v2_e7bd59a1": dict(swap_preserves="n", why="'Unveiling concept shift' reads as detecting the shift, not explaining it"),
    "v2_bdb0e7e9": dict(swap_preserves="n", why="formal characterisation lost; 'unveiling linear convergence' = showing it occurs"),
    "v2_50d1ee09": dict(swap_preserves="n", why="populations of networks are not hidden; 'unveiling' loses the analysis"),
    "v2_c8628f83": dict(swap_preserves="n", why="uncovering = finding specific directions; understanding changes the task"),
    "v2_ac584476": dict(swap_preserves="n", why="'Unveiling attacks' reads as revealing new attacks"),
    "v2_31555f29": dict(swap_preserves="n", why="unveiling = showing behaviours emerge; understanding = explaining them"),
    "v2_10f2c65d": dict(swap_preserves="n", why="the DP-SGD perturbation is explicit; 'unveiling' it loses the analysis"),
    "v2_287889d8": dict(swap_preserves="n", why="'unveiling prediction matrix' is odd; characterising is an estimation step"),
    "v2_1573df23": dict(swap_preserves="n", why="unveiling a specific invariance vs understanding invariance in general"),
    "v2_6af9056c": dict(slot_sense="n", swap_preserves="n", why="harnessing mode collapse = taming a problem, not making use of it"),
    "v2_69e4ac38": dict(swap_preserves="n", why="'Exploiting reasoning capability' = using an existing capability, not eliciting it"),
}

# V3 manual inspection of 100 title typography hits (50 U+2011, 50 en dash without U+2011; seed TYPO_SEED).
TYPO_SEED = 20261013
TYPO_CLASS_DESC = {
    "nbh_compound": "U+2011 inside ordinary hyphenated words or compound modifiers (e.g. Source-Free, End-to-End)",
    "nbh_in_name": "U+2011 only inside a coined name",
    "en_eponym": "en dash between personal names (Kolmogorov-Arnold, Weisfeiler-Leman): standard typography",
    "en_relation": "en dash between parallel terms (Vision-Language, Teacher-Student, Actor-Critic): standard typography",
    "en_open_compound": "en dash joining an open compound to a modifier (Sliding Window-Based): Chicago-style",
    "en_nonstandard": "en dash where a hyphen is standard (Anchor-MoE, GraphIP-Bench, Land-Surface)",
}
TYPO_EN = {  # submission_id -> class for the 50 en-dash hits
    "H-AAaJ9v_lE": "en_eponym", "Odtr1rzQMq": "en_eponym", "q5zMyAUhGx": "en_eponym", "udfjje2xXb": "en_eponym",
    "0aTSKdkC2s": "en_relation", "0zJ9aU7Tds": "en_relation", "1d9r7OaqyO": "en_relation", "1ndthBqbyK": "en_relation",
    "3Oc8Pg7Kij": "en_relation", "3eOie5dkcN": "en_open_compound", "4LiX5ddGcU": "en_relation",
    "5Rs6MpXD7D": "en_eponym", "5k1vfgXgom": "en_nonstandard", "6RMeoRAfBk": "en_relation", "7QlJcWwd14": "en_relation",
    "8CnU2kchiw": "en_relation", "9235Gzvgiq": "en_relation", "9fHuFi4Qsu": "en_open_compound",
    "CfZLxT3zIZ": "en_relation", "ExobfZ35x1": "en_relation", "FKmSQWLcCF": "en_relation",
    "GVkUjsIIrl": "en_open_compound", "J5pqVzrwNo": "en_relation", "JdL67YDnSy": "en_relation",
    "LhwPy8NMoN": "en_relation", "MCeZ4k7J6M": "en_eponym", "RK6j9cwSK4": "en_relation", "RsDmCz23AJ": "en_relation",
    "TX3oGD99CJ": "en_relation", "U6ROetm5nW": "en_relation", "USEpVtH8qV": "en_relation", "WKUR7Wo01L": "en_relation",
    "Z8GPdfPLFa": "en_relation", "aIULmVHnl8": "en_relation", "aiM6bRd6bG": "en_open_compound",
    "dYO3XS9Wsm": "en_relation", "dwNXKkiP51": "en_eponym", "eNIXzyFTwJ": "en_relation", "eiTy6AYeQi": "en_relation",
    "fqOhwzfqya": "en_nonstandard", "hSjjVXWPS5": "en_open_compound", "jaDAFnRQFp": "en_relation",
    "kIxAQxUZHq": "en_open_compound", "mRjzWksbGR": "en_relation", "n9mXlqD2SJ": "en_relation",
    "q1TpQ6guwX": "en_relation", "uuMMdEfFXR": "en_relation", "xWOTN66DQm": "en_relation", "z3bntsNwG0": "en_relation",
    "zrKFIfjcRp": "en_nonstandard",
}
TYPO_NBH_IN_NAME = {"ypptmENxJn"}  # GUI-AIMA; all other sampled U+2011 hits are nbh_compound

# V5: 10 clusters checked manually (the 5 where the annotator flag and the regex rule disagree + 5 random others)
V5_SEED = 20261014
V5_CHECK: dict[str, tuple[str, str, str]] = {  # item_id -> (label verdict, about_lms verdict, note)
    "v5_078423cd": ("too narrow", "borderline", "about half the shown papers are general multimodal learning without LMs; my count 6-7"),
    "v5_c467982e": ("accurate", "agree", "my count 8-9 LM papers"),
    "v5_02b78603": ("accurate", "borderline", "older sentence/word-embedding papers are not LM papers; my count about 7"),
    "v5_95a5e01f": ("accurate", "agree", "VLA/VLM robotics; my count 10-11"),
    "v5_890a86a0": ("accurate", "borderline", "half LLM post-training quantization, half general DNN quantization; my count 6-7"),
    "v5_1dd822b6": ("accurate", "agree", "my count 4-5"),
    "v5_7230e728": ("accurate", "agree", "no LM papers"),
    "v5_864b163b": ("accurate", "agree", "protein LMs are not natural-language LMs under the codebook; 2 LLM papers"),
    "v5_90099684": ("accurate", "agree", "no LM papers"),
    "v5_c0081b66": ("slightly off", "agree", "'robust' is over-specific; 'image classification and visual representations' fits better"),
}


# =====================================================================================================
# Helpers
# =====================================================================================================
def read_jsonl(paths) -> pd.DataFrame:
    rows = []
    for p in sorted(paths):
        with open(p, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    return pd.DataFrame(rows)


def kappa_ci(a, b, n_boot=1000, seed=0, labels=None):
    a, b = np.asarray(a), np.asarray(b)
    k = cohen_kappa_score(a, b, labels=labels)
    rng = np.random.default_rng(seed)
    ks = []
    for _ in range(n_boot):
        i = rng.integers(0, len(a), len(a))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            v = cohen_kappa_score(a[i], b[i], labels=labels)
        if np.isfinite(v):
            ks.append(v)
    lo, hi = np.percentile(ks, [2.5, 97.5]) if ks else (np.nan, np.nan)
    return float(k), float(lo), float(hi), float(np.mean(a == b))


def wilson(k, n, z=1.96):
    if n == 0:
        return np.nan, np.nan
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return float(c - h), float(c + h)


def clopper_pearson(k, n, a=0.05):
    lo = stats.beta.ppf(a / 2, k, n - k + 1) if k > 0 else 0.0
    hi = stats.beta.ppf(1 - a / 2, k + 1, n - k) if k < n else 1.0
    return float(lo), float(hi)


def strat_boot_counts(strata: np.ndarray, B: int, rng) -> np.ndarray:
    """B x n matrix of resampling counts: items are resampled with replacement within each stratum."""
    n = len(strata)
    Cm = np.zeros((B, n), dtype=np.float64)
    s = pd.Series(strata)
    for _, idx in s.groupby(s).groups.items():
        idx = np.asarray(list(idx))
        k = len(idx)
        Cm[:, idx] = rng.multinomial(k, np.full(k, 1.0 / k), size=B)
    return Cm


def pct(x, d=1):
    return "n/a" if x is None or not np.isfinite(x) else f"{100 * x:.{d}f}"


def fmt_ci(e, lo, hi, d=1, scale=100):
    if e is None or not np.isfinite(e):
        return "n/a"
    return f"{scale * e:.{d}f} [{scale * lo:.{d}f}, {scale * hi:.{d}f}]"


def md_table(df: pd.DataFrame, floatfmt: str = "{:.3f}") -> str:
    cols = list(df.columns)
    out = ["| " + " | ".join(map(str, cols)) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for r in df.astype(object).to_dict(orient="records"):
        vals = []
        for c in cols:
            v = r[c]
            if isinstance(v, (float, np.floating)):
                vals.append("" if not np.isfinite(v) else floatfmt.format(v))
            else:
                vals.append(str(v))
        out.append("| " + " | ".join(vals) + " |")
    return "\n".join(out)


def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, pd.DataFrame):
        return jsonable(o.to_dict(orient="records"))
    return o


# =====================================================================================================
# V1
# =====================================================================================================
def load_v1() -> pd.DataFrame:
    key = pd.read_csv(KEYS / "v1_key.csv", keep_default_na=False, na_values=[""])
    bat = read_jsonl(BAT.glob("v1_batch*.jsonl"))
    A = read_jsonl(LAB.glob("v1_batch*_A.jsonl"))
    B = read_jsonl(LAB.glob("v1_batch*_B.jsonl"))
    for X, nm in [(A, "A"), (B, "B")]:
        assert X.item_id.is_unique and len(X) == len(key), f"pass {nm}: {len(X)} rows"
    A = A.rename(columns={c: c + "_A" for c in A.columns if c != "item_id"})
    B = B.rename(columns={c: c + "_B" for c in B.columns if c != "item_id"})
    m = key.merge(bat, on="item_id").merge(A, on="item_id").merge(B, on="item_id")
    assert len(m) == len(key) == 1400
    for c in ["lead_A", "lead_B", "note_A", "note_B"]:
        m[c] = m[c].fillna("")
    # consensus
    for c in V1_LABELS:
        m[c + "_cons"] = np.where(m[c + "_A"] == m[c + "_B"], m[c + "_A"], None)
    m["lead_cons"] = np.where(m.lead_A.str.strip() == m.lead_B.str.strip(), m.lead_A.str.strip(), None)
    m["adjudicated"] = False
    m["adj_why"] = ""
    for iid, d in ADJ_V1.items():
        i = m.index[m.item_id == iid]
        assert len(i) == 1, iid
        i = i[0]
        for lab, v in d.items():
            if lab == "why":
                continue
            m.at[i, lab + "_cons"] = v
        if d.get("lead_type", m.at[i, "lead_type_cons"]) != "coined_name":
            m.at[i, "lead_orthography_cons"] = "na"
        m.at[i, "adjudicated"] = True
        m.at[i, "adj_why"] = d["why"]
    missing = [c for c in V1_LABELS if m[c + "_cons"].isna().any()]
    assert not missing, f"unadjudicated disagreements in {missing}: " + \
        str(m.loc[m[[c + '_cons' for c in missing]].isna().any(axis=1), 'item_id'].tolist())
    # every adjudication must concern an actual disagreement
    dis_ids = set(m.item_id[(m[[c + "_A" for c in V1_LABELS]].to_numpy() !=
                             m[[c + "_B" for c in V1_LABELS]].to_numpy()).any(axis=1)])
    assert set(ADJ_V1) == dis_ids, (set(ADJ_V1) - dis_ids, dis_ids - set(ADJ_V1))
    # constructs
    m["t_name"] = (m.lead_type_cons == "coined_name").astype(int)
    m["t_compound"] = (m.compound_cons == "y").astype(int)
    m["t_name_single"] = ((m.t_name == 1) & (m.lead_cons.fillna("").str.strip().str.split().str.len() == 1)).astype(int)
    m["t_name_union"] = ((m.lead_type_A == "coined_name") | (m.lead_type_B == "coined_name")).astype(int)
    m["t_name_inter"] = ((m.lead_type_A == "coined_name") & (m.lead_type_B == "coined_name")).astype(int)
    m["t_question"] = (m.question_cons == "y").astype(int)
    # detectors (key holds the frozen features_v2 values)
    for c in ["name_primary", "name_strict", "name_loose", "compound", "question"]:
        m["d_" + c] = m[c].astype(str).str.lower().map({"true": 1, "false": 0}).astype(int)
    m["d_casing"] = m.casing.map({"title_case": "title_case", "sentence_case": "sentence_case",
                                  "all_caps": "all_caps", "mixed": "other", "other": "other"})
    m["d_orth"] = m.name_orthography.fillna("")
    return m


def v1_kappas(m: pd.DataFrame) -> pd.DataFrame:
    rows = []
    specs = [("compound", None), ("lead_type", None), ("lead_orthography", None), ("casing", None), ("question", None)]
    for lab, _ in specs:
        for comp, sub in [("all", m), ("main", m[m.component == "main"]), ("hard", m[m.component == "hard"])]:
            k, lo, hi, agr = kappa_ci(sub[lab + "_A"], sub[lab + "_B"], seed=SEED)
            rows.append(dict(label=lab, items=comp, n=len(sub), kappa=k, lo=lo, hi=hi, raw_agreement=agr,
                             n_disagree=int((sub[lab + "_A"] != sub[lab + "_B"]).sum())))
    # binary coined_name, orthography among items both coded as names, lead string among both-compound
    a = (m.lead_type_A == "coined_name").astype(int)
    b = (m.lead_type_B == "coined_name").astype(int)
    k, lo, hi, agr = kappa_ci(a, b, seed=SEED)
    rows.append(dict(label="coined_name (binary)", items="all", n=len(m), kappa=k, lo=lo, hi=hi, raw_agreement=agr,
                     n_disagree=int((a != b).sum())))
    for blk in BLOCKS:
        s = m[(m.component == "main") & (m.block == blk)]
        a = (s.lead_type_A == "coined_name").astype(int)
        b = (s.lead_type_B == "coined_name").astype(int)
        k, lo, hi, agr = kappa_ci(a, b, seed=SEED)
        rows.append(dict(label="coined_name (binary)", items=f"main {blk}", n=len(s), kappa=k, lo=lo, hi=hi,
                         raw_agreement=agr, n_disagree=int((a != b).sum())))
    s = m[(m.lead_type_A == "coined_name") & (m.lead_type_B == "coined_name")]
    k, lo, hi, agr = kappa_ci(s.lead_orthography_A, s.lead_orthography_B, seed=SEED)
    rows.append(dict(label="lead_orthography | both coined", items="all", n=len(s), kappa=k, lo=lo, hi=hi,
                     raw_agreement=agr, n_disagree=int((s.lead_orthography_A != s.lead_orthography_B).sum())))
    s = m[(m.compound_A == "y") & (m.compound_B == "y")]
    same = (s.lead_A.str.strip() == s.lead_B.str.strip())
    rows.append(dict(label="lead string | both compound", items="all", n=len(s), kappa=np.nan, lo=np.nan, hi=np.nan,
                     raw_agreement=float(same.mean()), n_disagree=int((~same).sum())))
    return pd.DataFrame(rows)


def v1_spotcheck(m: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    agree = (m[[c + "_A" for c in V1_LABELS]].to_numpy() == m[[c + "_B" for c in V1_LABELS]].to_numpy()).all(axis=1)
    ag = m[agree].sort_values("item_id")
    rng = np.random.default_rng(SPOT_SEED)
    idx = rng.choice(len(ag), 150, replace=False)
    s = ag.iloc[np.sort(idx)].copy()
    assert set(SPOT_V1) <= set(s.item_id), set(SPOT_V1) - set(s.item_id)
    s["verdict"] = [SPOT_V1.get(i, ("ok", "", ""))[0] for i in s.item_id]
    s["label_in_question"] = [SPOT_V1.get(i, ("ok", "", ""))[1] for i in s.item_id]
    s["note"] = [SPOT_V1.get(i, ("ok", "", ""))[2] for i in s.item_id]
    out = s[["item_id", "block", "component", "title", "compound_cons", "lead_cons", "lead_type_cons",
             "lead_orthography_cons", "casing_cons", "question_cons", "verdict", "label_in_question", "note"]]
    n_err = int((s.verdict == "error").sum())
    n_bl = int((s.verdict == "borderline").sum())
    lo, hi = clopper_pearson(n_err, 150)
    lo2, hi2 = clopper_pearson(n_err + n_bl, 150)
    summ = dict(n_checked=150, n_error=n_err, n_borderline=n_bl, error_rate=n_err / 150, error_ci=[lo, hi],
                error_or_borderline_rate=(n_err + n_bl) / 150, error_or_borderline_ci=[lo2, hi2],
                n_borderline_lead_type=int(((s.verdict == "borderline") & (s.label_in_question == "lead_type")).sum()),
                n_borderline_casing=int(((s.verdict == "borderline") & (s.label_in_question == "casing")).sum()))
    return out, summ


BIN_SPECS = [  # (detector, truth construct, label)
    ("d_name_primary", "t_name", "NAME primary (name_colon) vs consensus coined name"),
    ("d_name_strict", "t_name", "NAME strict vs consensus coined name"),
    ("d_name_strict", "t_name_single", "NAME strict vs consensus single-token coined name"),
    ("d_name_loose", "t_name", "NAME loose vs consensus coined name"),
    ("d_compound", "t_name", "NAME compound vs consensus coined name"),
    ("d_compound", "t_compound", "compound vs consensus compound"),
    ("d_question", "t_question", "question vs consensus question"),
    ("d_name_primary", "t_name_union", "NAME primary vs coined by either pass (lenient)"),
    ("d_name_primary", "t_name_inter", "NAME primary vs coined by both passes (strict)"),
]


def v1_binary_metrics(main: pd.DataFrame, Cm: np.ndarray) -> pd.DataFrame:
    """Design-weighted precision/recall/specificity/NPV and prevalences per block and pooled, with stratified
    bootstrap percentile CIs (Cm: B x n resampling counts over the main sample)."""
    w = main.weight.to_numpy(float)
    rows = []
    for det, tru, lab in BIN_SPECS:
        d = main[det].to_numpy(int)
        t = main[tru].to_numpy(int)
        for blk in BLOCKS + ["all"]:
            bm = np.ones(len(main), bool) if blk == "all" else (main.block == blk).to_numpy()
            ind = {"tp": bm & (d == 1) & (t == 1), "fp": bm & (d == 1) & (t == 0),
                   "fn": bm & (d == 0) & (t == 1), "tn": bm & (d == 0) & (t == 0)}
            V = np.column_stack([w * ind[k] for k in ["tp", "fp", "fn", "tn"]])
            est = V.sum(axis=0)
            bt = Cm @ V
            def met(T):
                tp, fp, fn, tn = (T[..., i] for i in range(4))
                with np.errstate(invalid="ignore", divide="ignore"):
                    return dict(precision=tp / (tp + fp), recall=tp / (tp + fn), specificity=tn / (tn + fp),
                                npv=tn / (tn + fn), prev_true=(tp + fn) / (tp + fp + fn + tn),
                                prev_det=(tp + fp) / (tp + fp + fn + tn),
                                accuracy=(tp + tn) / (tp + fp + fn + tn))
            e = met(est)
            b = met(bt)
            r = dict(detector=det.replace("d_", ""), truth=tru, spec=lab, block=blk, n_items=int(bm.sum()),
                     n_det_pos=int((bm & (d == 1)).sum()), n_truth_pos=int((bm & (t == 1)).sum()),
                     n_fp=int(ind["fp"].sum()), n_fn=int(ind["fn"].sum()))
            for k in e:
                r[k] = float(e[k])
                lo, hi = np.nanpercentile(b[k], [2.5, 97.5])
                r[k + "_lo"], r[k + "_hi"] = float(lo), float(hi)
            rows.append(r)
    return pd.DataFrame(rows)


def v1_multiclass(main: pd.DataFrame, det: str, tru: str, classes: list[str], subset: np.ndarray | None,
                  Cm: np.ndarray) -> pd.DataFrame:
    w = main.weight.to_numpy(float)
    sub = np.ones(len(main), bool) if subset is None else subset
    d = main[det].to_numpy()
    t = main[tru].to_numpy()
    rows = []
    for blk in BLOCKS + ["all"]:
        bm = sub & (np.ones(len(main), bool) if blk == "all" else (main.block == blk).to_numpy())
        if bm.sum() == 0:
            continue
        acc_v = w * (bm & (d == t))
        tot_v = w * bm
        r = dict(block=blk, cls="(accuracy)", n_items=int(bm.sum()))
        e = acc_v.sum() / tot_v.sum()
        bt = (Cm @ acc_v) / (Cm @ tot_v)
        r["est"], r["lo"], r["hi"] = float(e), *map(float, np.nanpercentile(bt, [2.5, 97.5]))
        rows.append(r)
        for c in classes:
            tp = w * (bm & (d == c) & (t == c))
            dp = w * (bm & (d == c))
            tpos = w * (bm & (t == c))
            for nm, den in [("precision", dp), ("recall", tpos)]:
                r = dict(block=blk, cls=f"{c} {nm}", n_items=int((den > 0).sum()))
                if den.sum() == 0:
                    r["est"] = r["lo"] = r["hi"] = np.nan
                else:
                    with np.errstate(invalid="ignore", divide="ignore"):
                        bt = (Cm @ tp) / (Cm @ den)
                    r["est"] = float(tp.sum() / den.sum())
                    r["lo"], r["hi"] = map(float, np.nanpercentile(bt, [2.5, 97.5]))
                rows.append(r)
    return pd.DataFrame(rows)


_K = {"tp": lambda d, t: d * t, "fp": lambda d, t: d * (1 - t), "fn": lambda d, t: (1 - d) * t,
      "tn": lambda d, t: (1 - d) * (1 - t)}


def ps_totals(main: pd.DataFrame, hardT: pd.DataFrame, popN: dict, det: str, tru: str, Cm: np.ndarray,
              Ch: np.ndarray) -> dict:
    """Post-stratified (dual-frame) population totals of TP/FP/FN/TN per block.

    Each main sampling stratum (block x detector stratum) is split into a two-token-lead cell T (compound title,
    lead of exactly 2 whitespace tokens) and the rest O, with known population counts popN[(block, h, T)].
    O cells are estimated from the main items in them. T cells are estimated per era (pre <= 2023, post) and
    detector side (NAME-positive / negative) from the pooled main + hard two-token items, which are random draws
    from those cells (the WP3a hard strata two_token_lead|{name,nonname}_{pre,post}). Row 0 is the point estimate
    (all counts 1); rows 1.. are bootstrap replicates (Cm, Ch: resampling counts within strata)."""
    Cm1 = np.vstack([np.ones((1, len(main))), Cm])
    Ch1 = np.vstack([np.ones((1, len(hardT))), Ch])
    R = Cm1.shape[0]
    dm, tm = main[det].to_numpy(int), main[tru].to_numpy(int)
    dh, th = hardT[det].to_numpy(int), hardT[tru].to_numpy(int)
    Tm = main["T"].to_numpy(bool)
    Tmean = {}
    for era in ("pre", "post"):
        for pn in (0, 1):
            im = (Tm & (main.era == era).to_numpy() & (main.d_name_primary == pn).to_numpy()).astype(float)
            ih = ((hardT.era == era).to_numpy() & (hardT.d_name_primary == pn).to_numpy()).astype(float)
            D = Cm1 @ im + Ch1 @ ih
            for k, f in _K.items():
                with np.errstate(invalid="ignore", divide="ignore"):
                    Tmean[(era, pn, k)] = (Cm1 @ (im * f(dm, tm)) + Ch1 @ (ih * f(dh, th))) / D
    out = {k: np.zeros((R, len(BLOCKS))) for k in _K}
    for j, b in enumerate(BLOCKS):
        era = "post" if b in ("2024", "2025", "2026") else "pre"
        for h in sorted(main.loc[main.block == b, "h"].unique()):
            pn = 1 if h.startswith("pos") else 0
            NO, NT = popN.get((b, h, False), 0), popN.get((b, h, True), 0)
            io = ((main.block == b) & (main.h == h) & ~main["T"]).to_numpy().astype(float)
            ia = ((main.block == b) & (main.h == h)).to_numpy().astype(float)
            D, Da = Cm1 @ io, Cm1 @ ia
            for k, f in _K.items():
                with np.errstate(invalid="ignore", divide="ignore"):
                    mo = (Cm1 @ (io * f(dm, tm))) / D
                    ma = (Cm1 @ (ia * f(dm, tm))) / Da
                mo = np.where(D > 0, mo, ma)  # replicate drew only T items from this stratum: use stratum mean
                out[k][:, j] += NO * mo + (NT * Tmean[(era, pn, k)] if NT else 0.0)
    return out


def metrics_from_totals(T: dict) -> dict:
    tp, fp, fn, tn = (T[k] for k in ["tp", "fp", "fn", "tn"])
    with np.errstate(invalid="ignore", divide="ignore"):
        return dict(precision=tp / (tp + fp), recall=tp / (tp + fn), specificity=tn / (tn + fp), npv=tn / (tn + fn),
                    prev_true=(tp + fn) / (tp + fp + fn + tn), prev_det=(tp + fp) / (tp + fp + fn + tn),
                    accuracy=(tp + tn) / (tp + fp + fn + tn))


def ps_sesp(T: dict) -> pd.DataFrame:
    """Rows = point (row 0) + replicates; columns (block, Se/Sp)."""
    out = {}
    with np.errstate(invalid="ignore", divide="ignore"):
        for j, b in enumerate(BLOCKS):
            out[(b, "Se")] = T["tp"][:, j] / (T["tp"][:, j] + T["fn"][:, j])
            out[(b, "Sp")] = T["tn"][:, j] / (T["tn"][:, j] + T["fp"][:, j])
    return pd.DataFrame(out)


def se_sp(main: pd.DataFrame, det: str, tru: str, counts: np.ndarray) -> pd.DataFrame:
    """Se/Sp per block for a vector (or B x n matrix) of resampling counts."""
    w = main.weight.to_numpy(float)
    d = main[det].to_numpy(int)
    t = main[tru].to_numpy(int)
    out = {}
    cnt = np.atleast_2d(counts)
    for blk in BLOCKS:
        bm = (main.block == blk).to_numpy()
        tp = cnt @ (w * (bm & (d == 1) & (t == 1)))
        fn = cnt @ (w * (bm & (d == 0) & (t == 1)))
        tn = cnt @ (w * (bm & (d == 0) & (t == 0)))
        fp = cnt @ (w * (bm & (d == 1) & (t == 0)))
        with np.errstate(invalid="ignore", divide="ignore"):
            out[(blk, "Se")] = tp / (tp + fn)
            out[(blk, "Sp")] = tn / (tn + fp)
    return pd.DataFrame(out)


def rogan_gladen(p_obs: pd.Series, sesp: pd.DataFrame) -> pd.DataFrame:
    """p_obs indexed by year; sesp: rows = draws, columns (block, Se/Sp)."""
    out = {}
    for y, p in p_obs.items():
        b = year_block(y)
        se, sp = sesp[(b, "Se")].to_numpy(), sesp[(b, "Sp")].to_numpy()
        with np.errstate(invalid="ignore", divide="ignore"):
            out[y] = np.clip((p + sp - 1) / (se + sp - 1), 0, 1)
    return pd.DataFrame(out)


# ---------------------------------------------------------------- misclassification-corrected ITS
def its_design(df: pd.DataFrame) -> tuple[np.ndarray, list[str]]:
    tc = (df.year - 2023).to_numpy(float)
    post = (df.year >= 2024).to_numpy(float)
    cols = [np.ones(len(df)), tc, post, post * tc, df.log_authors.to_numpy(float), df.llm_topic.to_numpy(float)]
    names = ["Intercept", "tc", "post", "post_t", "log_authors", "llm_topic"]
    topics = np.sort(df.topic100.unique())
    for k in topics[1:]:
        cols.append((df.topic100.to_numpy() == k).astype(float))
        names.append(f"topic100[{k}]")
    return np.column_stack(cols), names


def fit_misclass_logit(X, y, a, b, beta0=None, maxiter=200, tol=1e-10):
    """ML for P(y=1|x) = a + b * expit(x'beta) (a = 1 - Sp, b = Se + Sp - 1, per row). Fisher scoring with step
    halving; returns beta and the per-row derivative pieces needed for the sandwich."""
    n, k = X.shape
    beta = np.zeros(k) if beta0 is None else beta0.copy()
    if beta0 is None:
        beta[0] = np.log(max(y.mean(), 1e-3) / (1 - max(y.mean(), 1e-3)))

    def ll_parts(bt):
        eta = X @ bt
        p = expit(eta)
        q = np.clip(a + b * p, 1e-12, 1 - 1e-12)
        ll = np.sum(y * np.log(q) + (1 - y) * np.log1p(-q))
        return eta, p, q, ll

    eta, p, q, ll = ll_parts(beta)
    for it in range(maxiter):
        dq = b * p * (1 - p)
        g = (y - q) / (q * (1 - q)) * dq
        W = dq * dq / (q * (1 - q))
        score = X.T @ g
        info = X.T @ (X * W[:, None])
        step = np.linalg.solve(info + 1e-10 * np.eye(k), score)
        t = 1.0
        while True:
            nb = beta + t * step
            _, p2, q2, ll2 = ll_parts(nb)
            if ll2 >= ll - 1e-9 or t < 1e-6:
                break
            t /= 2
        beta = nb
        conv = abs(ll2 - ll) < tol * (1 + abs(ll)) and np.max(np.abs(t * step)) < 1e-7
        eta, p, q, ll = ll_parts(beta)
        if conv:
            break
    return beta, ll, it + 1


def misclass_vcov(X, y, a, b, beta, clusters):
    """Cluster-robust sandwich (observed Hessian bread, CRV1 small-sample factor as statsmodels' Logit)."""
    eta = X @ beta
    p = expit(eta)
    q = np.clip(a + b * p, 1e-12, 1 - 1e-12)
    dq = b * p * (1 - p)
    d2q = b * p * (1 - p) * (1 - 2 * p)
    r = y / q - (1 - y) / (1 - q)
    g = r * dq
    h = -(y / q ** 2 + (1 - y) / (1 - q) ** 2) * dq ** 2 + r * d2q
    H = X.T @ (X * h[:, None])
    try:
        Hinv = np.linalg.inv(-H)
        if np.any(np.linalg.eigvalsh(-H) <= 0):
            raise np.linalg.LinAlgError
    except np.linalg.LinAlgError:
        W = dq * dq / (q * (1 - q))
        Hinv = np.linalg.inv(X.T @ (X * W[:, None]))
    S = X * g[:, None]
    codes = pd.factorize(clusters)[0]
    G = codes.max() + 1
    Sg = np.zeros((G, X.shape[1]))
    np.add.at(Sg, codes, S)
    meat = Sg.T @ Sg
    n, k = X.shape
    fac = G / (G - 1) * (n - 1) / (n - k)
    return fac * Hinv @ meat @ Hinv


def its_corrected(df: pd.DataFrame, outcome: str, sesp_point: pd.Series, sesp_draws: pd.DataFrame | None):
    """Uncorrected and misclassification-corrected segmented logit (D1 specification)."""
    X, names = its_design(df)
    y = df[outcome].to_numpy(float)
    blk = df.year.map(year_block).to_numpy()
    j = names.index("post_t")
    clusters = df.topic100.to_numpy()
    # uncorrected (a = 0, b = 1)
    b0, ll0, it0 = fit_misclass_logit(X, y, np.zeros(len(y)), np.ones(len(y)))
    V0 = misclass_vcov(X, y, np.zeros(len(y)), np.ones(len(y)), b0, clusters)
    out = dict(uncorrected=dict(delta=float(b0[j]), se=float(np.sqrt(V0[j, j])), iters=it0,
                                pre_slope=float(b0[names.index("tc")]), level=float(b0[names.index("post")])))

    def ab(sesp):
        se = np.array([sesp[(x, "Se")] for x in blk], float)
        sp = np.array([sesp[(x, "Sp")] for x in blk], float)
        return 1 - sp, se + sp - 1
    a, b = ab(sesp_point)
    b1, ll1, it1 = fit_misclass_logit(X, y, a, b, beta0=b0)
    V1 = misclass_vcov(X, y, a, b, b1, clusters)
    out["corrected"] = dict(delta=float(b1[j]), se=float(np.sqrt(V1[j, j])), iters=it1,
                            pre_slope=float(b1[names.index("tc")]), level=float(b1[names.index("post")]))
    if sesp_draws is not None:
        ds, ses = [], []
        for i in range(len(sesp_draws)):
            a_, b_ = ab(sesp_draws.iloc[i])
            if not (np.all(np.isfinite(a_)) and np.all(np.isfinite(b_))) or np.any(b_ <= 0.05):
                continue
            bi, _, _ = fit_misclass_logit(X, y, a_, b_, beta0=b1, maxiter=60)
            ds.append(bi[j])
        ds = np.array(ds)
        out["corrected"]["boot_draws"] = int(len(ds))
        out["corrected"]["boot_delta_sd"] = float(ds.std(ddof=1))
        # total variance = sampling variance (sandwich) + validation-sample variance (between draws)
        tot = np.sqrt(V1[j, j] + ds.var(ddof=1))
        out["corrected"]["se_total"] = float(tot)
        out["corrected"]["boot_delta_pct"] = [float(x) for x in np.percentile(ds, [2.5, 50, 97.5])]
        out["corrected"]["share_draws_within10pct_OR"] = float(np.mean(np.abs(np.exp(ds - b0[j]) - 1) <= 0.10))
    for key in ["uncorrected", "corrected"]:
        r = out[key]
        se = r.get("se_total", r["se"])
        r["OR"] = float(np.exp(r["delta"]))
        r["OR_lo"], r["OR_hi"] = float(np.exp(r["delta"] - 1.96 * se)), float(np.exp(r["delta"] + 1.96 * se))
        r["z"] = r["delta"] / se
    out["OR_ratio"] = out["corrected"]["OR"] / out["uncorrected"]["OR"]
    out["logOR_rel_change"] = (out["corrected"]["delta"] - out["uncorrected"]["delta"]) / out["uncorrected"]["delta"]
    out["within_10pct_OR"] = bool(abs(out["OR_ratio"] - 1) <= 0.10)
    out["within_10pct_logOR"] = bool(abs(out["logOR_rel_change"]) <= 0.10)
    return out


def fp_fn_categories(m: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Rule-based categories of NAME-detector errors (main + hard items) for the report."""
    fp = m[(m.d_name_primary == 1) & (m.t_name == 0)].copy()
    fn = m[(m.d_name_primary == 0) & (m.t_name == 1)].copy()

    def fp_cat(r):
        lead = (r.lead_raw if isinstance(r.lead_raw, str) else "") or ""
        if r.compound_cons == "n":
            return "separator misread (spaced hyphen inside a word)"
        if lead.rstrip().endswith(")"):
            return "parenthesis read as an acronym"
        if len(lead.split()) == 1:
            return "one-word descriptive lead"
        if r.title.upper() == r.title:
            return "all-caps title"
        return "two-token descriptive lead with a hyphenated or capitalised modifier"

    def fn_cat(r):
        lead = (r.lead_cons or "") if isinstance(r.lead_cons, str) else ""
        toks = lead.split()
        if r.d_compound == 0:
            return "separator not detected"
        if toks and re.sub(r"[^a-z]", "", toks[0].lower()) in {"the", "a", "an", "can"}:
            return "lead starts with an article or function word"
        if len(toks) == 2 and (sum(c.isupper() for c in toks[1]) >= 2 or any(c.isdigit() for c in toks[1])) and \
                not re.search(r"[A-Z]", toks[0][1:]):
            return "ordinary first word + coined token"
        if len(toks) >= 3:
            return "lead of 3+ tokens headed by a name"
        return "two ordinary words used as a name"
    fp["category"] = [fp_cat(r) for r in fp.itertuples()]
    fn["category"] = [fn_cat(r) for r in fn.itertuples()]
    return fp, fn


def v1_analysis(frame: pd.DataFrame) -> dict:
    m = load_v1()
    log(f"V1: {len(m)} items, {int(m.adjudicated.sum())} adjudicated")
    kap = v1_kappas(m)
    kap.to_csv(VAL / "v1_kappa.csv", index=False)
    # adjudication record
    rec = []
    for _, r in m[m.adjudicated].iterrows():
        for lab in V1_LABELS:
            if r[lab + "_A"] != r[lab + "_B"]:
                rec.append(dict(item_id=r.item_id, block=r.block, component=r.component, title=r.title,
                                label=lab, pass_A=r[lab + "_A"], pass_B=r[lab + "_B"], adjudicated=r[lab + "_cons"],
                                why=r.adj_why, note_A=r.note_A, note_B=r.note_B,
                                detector_name_primary=int(r.d_name_primary)))
    adj = pd.DataFrame(rec)
    adj.to_csv(VAL / "v1_adjudications.csv", index=False)
    spot, spot_s = v1_spotcheck(m)
    spot.to_csv(VAL / "v1_spotcheck.csv", index=False)
    m.drop(columns=["note_A", "note_B"]).to_csv(VAL / "v1_consensus.csv", index=False)

    # ---------------------------------------------------------------- estimation frames
    m["era"] = np.where(m.year >= 2024, "post", "pre")
    m["T"] = (m.d_compound == 1) & (m.lead_n_tokens == 2)
    main = m[m.component == "main"].reset_index(drop=True)
    main["h"] = main.stratum.str.split("|").str[1]
    hardT = m[(m.component == "hard") & m.stratum.str.contains("two_token_lead")].reset_index(drop=True)
    assert hardT["T"].all()
    pop = frame[["year", "name_primary", "name_compound", "name_orthography", "lead_n_tokens"]].copy()
    pop["block"] = pop.year.map(year_block)
    pop["h"] = np.where(pop.name_primary == 1, "pos_" + pop.name_orthography.astype(str),
                        np.where(pop.name_compound == 1, "neg_phrase_colon", "neg_noncompound"))
    pop["T"] = (pop.name_compound == 1) & (pop.lead_n_tokens == 2)
    popN = pop.groupby(["block", "h", "T"]).size().to_dict()
    chk = pop.groupby(["block", "h"]).size()
    kst = main.groupby(["block", "h"]).N_stratum.first()
    assert (chk.reindex(kst.index) == kst).all(), "population strata do not reproduce the sampling frame"
    rng = np.random.default_rng(SEED)
    Cm = strat_boot_counts(main.stratum.to_numpy(), N_BOOT, rng)
    Ch = strat_boot_counts(hardT.stratum.to_numpy(), N_BOOT, rng)

    # ---------------------------------------------------------------- binary detectors: PS (primary) and HT
    ht = v1_binary_metrics(main, Cm)
    ht["estimator"] = "HT (main only)"
    rows = []
    ps_store = {}
    for det, tru, lab in BIN_SPECS:
        T = ps_totals(main, hardT, popN, det, tru, Cm, Ch)
        ps_store[(det, tru)] = T
        Tall = {k: np.column_stack([v, v.sum(axis=1)]) for k, v in T.items()}
        met = metrics_from_totals(Tall)
        for j, blk in enumerate(BLOCKS + ["all"]):
            bm = np.ones(len(main), bool) if blk == "all" else (main.block == blk).to_numpy()
            hb = np.zeros(len(hardT), bool) if blk == "all" else (hardT.block == blk).to_numpy()
            d_ = main[det].to_numpy(int)
            t_ = main[tru].to_numpy(int)
            r = dict(detector=det.replace("d_", ""), truth=tru, spec=lab, block=blk, estimator="PS (main + hard)",
                     n_items=int(bm.sum()), n_det_pos=int((bm & (d_ == 1)).sum()),
                     n_truth_pos=int((bm & (t_ == 1)).sum()), n_fp=int((bm & (d_ == 1) & (t_ == 0)).sum()),
                     n_fn=int((bm & (d_ == 0) & (t_ == 1)).sum()))
            for k, arr in met.items():
                r[k] = float(arr[0, j])
                lo, hi = np.nanpercentile(arr[1:, j], [2.5, 97.5])
                r[k + "_lo"], r[k + "_hi"] = float(lo), float(hi)
            rows.append(r)
    binm = pd.concat([pd.DataFrame(rows), ht], ignore_index=True)
    binm.to_csv(VAL / "v1_detector_metrics.csv", index=False)
    # T-cell estimates (share coined among two-token leads)
    tcell = []
    for era in ("pre", "post"):
        for pn in (1, 0):
            im = main[main["T"] & (main.era == era) & (main.d_name_primary == pn)]
            ih = hardT[(hardT.era == era) & (hardT.d_name_primary == pn)]
            n_ = len(im) + len(ih)
            k_ = int(im.t_name.sum() + ih.t_name.sum())
            lo, hi = wilson(k_, n_)
            tcell.append(dict(era=era, detector_NAME=pn, N_population=int(pop[pop["T"] & (pop.year >= 2024 if era == "post"
                                                                                           else pop.year < 2024) &
                                                                                (pop.name_primary == pn)].shape[0]),
                              n_main=len(im), n_hard=len(ih), coined=k_, share_coined=k_ / n_, lo=lo, hi=hi))
    tcell = pd.DataFrame(tcell)
    tcell.to_csv(VAL / "v1_two_token_cells.csv", index=False)

    # orthography and casing (main sample, HT)
    orth_sub = ((main.d_name_primary == 1) & (main.t_name == 1)).to_numpy()
    orth = v1_multiclass(main, "d_orth", "lead_orthography_cons", ["all_caps", "mixed_case", "word", "paren_acronym"],
                         orth_sub, Cm)
    orth.to_csv(VAL / "v1_orthography_metrics.csv", index=False)
    cas = v1_multiclass(main, "d_casing", "casing_cons", ["title_case", "sentence_case", "all_caps", "other"], None, Cm)
    cas.to_csv(VAL / "v1_casing_metrics.csv", index=False)
    conf_orth = pd.crosstab(main.loc[orth_sub, "d_orth"], main.loc[orth_sub, "lead_orthography_cons"])
    conf_cas = pd.crosstab(main.d_casing, main.casing_cons)

    hard = m[m.component == "hard"]
    hrows = []
    for st, g in hard.groupby("stratum"):
        hrows.append(dict(stratum=st, n=len(g), det_name=int(g.d_name_primary.sum()), cons_name=int(g.t_name.sum()),
                          agree_name=float((g.d_name_primary == g.t_name).mean()),
                          det_compound=int(g.d_compound.sum()), cons_compound=int(g.t_compound.sum()),
                          agree_compound=float((g.d_compound == g.t_compound).mean())))
    hardt = pd.DataFrame(hrows)
    hardt.to_csv(VAL / "v1_hard_cases.csv", index=False)
    fp, fn = fp_fn_categories(m)
    fp[["item_id", "block", "component", "title", "lead_cons", "lead_type_cons", "category"]].to_csv(
        VAL / "v1_name_false_positives.csv", index=False)
    fn[["item_id", "block", "component", "title", "lead_cons", "compound_cons", "d_compound", "category"]].to_csv(
        VAL / "v1_name_false_negatives.csv", index=False)

    # ---------------------------------------------------------------- Rogan-Gladen (PS Se/Sp; HT as a check)
    rg_specs = [("name_primary", "d_name_primary", "t_name"), ("name_strict", "d_name_strict", "t_name_single"),
                ("name_loose", "d_name_loose", "t_name"), ("name_compound", "d_compound", "t_compound"),
                ("name_primary|lenient", "d_name_primary", "t_name_union"),
                ("name_primary|strict", "d_name_primary", "t_name_inter")]
    rg_rows = []
    sesp_store = {}
    for nm, det, tru in rg_specs:
        col = nm.split("|")[0]
        p_obs = frame.groupby("year")[col].mean()
        T = ps_store.get((det, tru)) or ps_totals(main, hardT, popN, det, tru, Cm, Ch)
        S = ps_sesp(T)
        sp_point, sp_draws = S.iloc[0], S.iloc[1:].reset_index(drop=True)
        ht_point = se_sp(main, det, tru, np.ones(len(main))).iloc[0]
        sesp_store[nm] = (sp_point, sp_draws, ht_point)
        rg_p = rogan_gladen(p_obs, sp_point.to_frame().T).iloc[0]
        rg_b = rogan_gladen(p_obs, sp_draws)
        rg_ht = rogan_gladen(p_obs, ht_point.to_frame().T).iloc[0]
        for y in p_obs.index:
            blk = year_block(y)
            lo, hi = np.nanpercentile(rg_b[y], [2.5, 97.5])
            j = BLOCKS.index(blk)
            ppv = T["tp"][0, j] / (T["tp"][0, j] + T["fp"][0, j])
            npv = T["tn"][0, j] / (T["tn"][0, j] + T["fn"][0, j])
            rg_rows.append(dict(detector=nm, year=int(y), block=blk, n_papers=int((frame.year == y).sum()),
                                p_obs=float(p_obs[y]), Se=float(sp_point[(blk, "Se")]), Sp=float(sp_point[(blk, "Sp")]),
                                p_rg=float(rg_p[y]), p_rg_lo=float(lo), p_rg_hi=float(hi),
                                p_ppv_npv=float(p_obs[y] * ppv + (1 - p_obs[y]) * (1 - npv)),
                                Se_HT=float(ht_point[(blk, "Se")]), Sp_HT=float(ht_point[(blk, "Sp")]),
                                p_rg_HT=float(rg_ht[y])))
    rg = pd.DataFrame(rg_rows)
    rg.to_csv(VAL / "v1_rogan_gladen.csv", index=False)

    def seg_slope(p):
        yrs = np.array(sorted(p.index))
        tc = yrs - 2023
        post = (yrs >= 2024).astype(float)
        Xa = np.column_stack([np.ones(len(yrs)), tc, post, post * tc])
        pc = np.clip(p.loc[yrs].to_numpy(), 1e-4, 1 - 1e-4)
        lp = np.log(pc / (1 - pc))
        wts = frame.groupby("year").size().loc[yrs].to_numpy(float)
        bt = np.linalg.lstsq(Xa * np.sqrt(wts)[:, None], lp * np.sqrt(wts), rcond=None)[0]
        return float(bt[3])
    prim = rg[rg.detector == "name_primary"].set_index("year")
    agg = dict(uncorrected_slope_change=seg_slope(prim.p_obs), corrected_slope_change=seg_slope(prim.p_rg),
               corrected_slope_change_HT=seg_slope(prim.p_rg_HT))
    agg["OR_ratio"] = float(np.exp(agg["corrected_slope_change"] - agg["uncorrected_slope_change"]))

    # ---------------------------------------------------------------- ITS with block-specific misclassification
    its = {}
    boot_sel = np.random.default_rng(SEED + 7)
    for nm in ["name_primary", "name_loose", "name_strict", "name_compound", "name_primary|lenient",
               "name_primary|strict"]:
        col = nm.split("|")[0]
        sp_point, sp_draws, ht_point = sesp_store[nm]
        nb = N_BOOT_ITS if nm == "name_primary" else (N_BOOT_ITS // 2 if nm in ("name_loose", "name_primary|lenient",
                                                                              "name_primary|strict") else 0)
        log(f"V1: corrected ITS {nm} ({nb} bootstrap draws)")
        draws = sp_draws.iloc[boot_sel.choice(len(sp_draws), nb, replace=False)] if nb else None
        its[nm] = its_corrected(frame, col, sp_point, draws)
        if nm == "name_primary":
            its[nm]["HT_check"] = its_corrected(frame, col, ht_point, None)["corrected"]
    d1 = json.loads((C.OUT / "d1_break" / "its_results.json").read_text())["H1a"]["primary"]
    its["d1_reference_slope_change_OR"] = d1["slope_change_OR"]

    # ---------------------------------------------------------------- precision drift (primary, PS)
    met = metrics_from_totals(ps_store[("d_name_primary", "t_name")])
    precs = met["precision"]  # rows: point + replicates; columns: blocks
    rec_ = met["recall"]
    pt = precs[0]
    rep = precs[1:]
    drift = float(pt.max() - pt.min())
    drift_b = rep.max(axis=1) - rep.min(axis=1)
    Tp = ps_store[("d_name_primary", "t_name")]
    pooled = Tp["tp"][0].sum() / (Tp["tp"][0].sum() + Tp["fp"][0].sum())
    null = rep - pt[None, :] + pooled  # sampling noise around a common precision
    null_range = null.max(axis=1) - null.min(axis=1)
    pre_post = rep[:, 3:].mean(axis=1) - rep[:, :3].mean(axis=1)
    rec_drift = rec_[1:].max(axis=1) - rec_[1:].min(axis=1)
    drift_s = dict(precision_by_block={b: float(v) for b, v in zip(BLOCKS, pt)},
                   precision_range=drift, precision_range_ci=list(map(float, np.percentile(drift_b, [2.5, 97.5]))),
                   precision_range_null_p=float(np.mean(null_range >= drift)),
                   precision_range_null_median=float(np.median(null_range)),
                   precision_post_minus_pre=float(pt[3:].mean() - pt[:3].mean()),
                   precision_post_minus_pre_ci=list(map(float, np.percentile(pre_post, [2.5, 97.5]))),
                   recall_by_block={b: float(v) for b, v in zip(BLOCKS, rec_[0])},
                   recall_range=float(rec_[0].max() - rec_[0].min()),
                   recall_range_ci=list(map(float, np.percentile(rec_drift, [2.5, 97.5]))),
                   pass_lt_5pp=bool(drift < 0.05))
    return dict(m=m, main=main, kappa=kap, adj=adj, spot=spot, spot_summary=spot_s, binm=binm, orth=orth, cas=cas,
                conf_orth=conf_orth, conf_cas=conf_cas, hard=hardt, fp=fp, fn=fn, rg=rg, its=its, agg=agg,
                drift=drift_s, tcell=tcell)


# =====================================================================================================
# V2
# =====================================================================================================
def v2_analysis() -> dict:
    key = pd.read_csv(KEYS / "v2_key.csv", keep_default_na=False, na_values=[""])
    bat = read_jsonl(BAT.glob("v2_batch*.jsonl"))
    A = read_jsonl(LAB.glob("v2_batch*_A.jsonl"))
    B = read_jsonl(LAB.glob("v2_batch*_B.jsonl"))
    assert len(A) == len(B) == len(key) == 400 and A.item_id.is_unique and B.item_id.is_unique
    m = key.merge(bat[["item_id", "title"]], on="item_id").merge(A, on="item_id").merge(
        B, on="item_id", suffixes=("_A", "_B"))
    kap = {}
    for c in ["slot_sense", "swap_preserves"]:
        k, lo, hi, agr = kappa_ci(m[c + "_A"], m[c + "_B"], seed=SEED)
        kap[c] = dict(kappa=k, lo=lo, hi=hi, raw_agreement=agr, n_disagree=int((m[c + "_A"] != m[c + "_B"]).sum()))
    for c in ["slot_sense", "swap_preserves"]:
        m[c] = np.where(m[c + "_A"] == m[c + "_B"], m[c + "_A"], None)
    m["adj_why"] = ""
    dis = set(m.item_id[(m.slot_sense_A != m.slot_sense_B) | (m.swap_preserves_A != m.swap_preserves_B)])
    assert set(ADJ_V2) == dis, (set(ADJ_V2) - dis, dis - set(ADJ_V2))
    rec = []
    for iid, d in ADJ_V2.items():
        i = m.index[m.item_id == iid][0]
        for lab in ["slot_sense", "swap_preserves"]:
            if m.at[i, lab + "_A"] != m.at[i, lab + "_B"]:
                assert lab in d, (iid, lab)
            if lab in d:
                m.at[i, lab] = d[lab]
        m.at[i, "adj_why"] = d["why"]
        for lab in ["slot_sense", "swap_preserves"]:
            if m.at[i, lab + "_A"] != m.at[i, lab + "_B"]:
                rec.append(dict(item_id=iid, title=m.at[i, "title"], target=m.at[i, "target_word"],
                                slot=m.at[i, "slot"], swap_word=m.at[i, "swap_word"], label=lab,
                                pass_A=m.at[i, lab + "_A"], pass_B=m.at[i, lab + "_B"], adjudicated=m.at[i, lab],
                                why=d["why"], note_A=m.at[i, "note_A"], note_B=m.at[i, "note_B"]))
    assert m.slot_sense.notna().all() and m.swap_preserves.notna().all()
    pd.DataFrame(rec).to_csv(VAL / "v2_adjudications.csv", index=False)
    m["sense"] = (m.slot_sense == "y").astype(int)
    m["swap"] = (m.swap_preserves == "y").astype(int)
    m["filtered_pre_v2"] = m.slot_sense_flag.notna() & (m.slot_sense_flag.astype(str) != "")
    m.drop(columns=["note_A", "note_B"]).to_csv(VAL / "v2_consensus.csv", index=False)

    def wmean(g, col):
        return float(np.average(g[col], weights=g.weight))

    rows = []
    for (slot, var, word), g in m.groupby(["slot", "variant", "word"]):
        k = int(g.sense.sum())
        n = len(g)
        lo, hi = wilson(k, n)
        gp = g[~g.filtered_pre_v2]
        r = dict(slot=slot, variant="llm" if var == 1 else "neutral", word=word, n=n, n_sense_y=k,
                 precision_w=wmean(g, "sense"), precision_unw=k / n, wilson_lo=lo, wilson_hi=hi,
                 precision_pre=float(g[g.era == "pre"].sense.mean()) if (g.era == "pre").any() else np.nan,
                 n_pre=int((g.era == "pre").sum()),
                 precision_post=float(g[g.era == "post"].sense.mean()) if (g.era == "post").any() else np.nan,
                 n_post=int((g.era == "post").sum()),
                 n_after_prefilter=len(gp),
                 precision_after_prefilter_w=wmean(gp, "sense") if len(gp) else np.nan,
                 swap_preserves_w=wmean(g, "swap"),
                 swap_preserves_given_sense=float(g[g.sense == 1].swap.mean()) if k else np.nan,
                 N_population=int(g.groupby("stratum").N_stratum.first().sum()))
        r["drop"] = bool(r["precision_w"] < 0.85)
        r["drop_if_unweighted_rule"] = bool(r["precision_unw"] < 0.85)
        r["borderline"] = bool(not r["drop"] and (
            r["precision_unw"] < 0.85 or (r["n_pre"] >= 3 and r["precision_pre"] < 0.85) or
            (r["n_post"] >= 3 and r["precision_post"] < 0.85)))
        rows.append(r)
    words = pd.DataFrame(rows).sort_values(["slot", "variant", "word"]).reset_index(drop=True)
    words.to_csv(VAL / "v2_word_metrics.csv", index=False)
    # slot x side x era
    srows = []
    for (slot, var, era), g in m.groupby(["slot", "variant", "era"]):
        srows.append(dict(slot=slot, variant="llm" if var == 1 else "neutral", era=era, n=len(g),
                          precision_w=wmean(g, "sense"), swap_w=wmean(g, "swap"),
                          precision_w_after_drops=wmean(g[~g.word.isin(words[words["drop"]].word)], "sense")
                          if (~g.word.isin(words[words["drop"]].word)).any() else np.nan))
    slots = pd.DataFrame(srows)
    slots.to_csv(VAL / "v2_slot_metrics.csv", index=False)
    by_source = m.groupby("source").agg(n=("sense", "size"), sense=("sense", "mean"), swap=("swap", "mean")).reset_index()
    dropped = words[words["drop"]]
    payload = dict(
        rule="PLAN.md section 3 V2: slot words (variants) whose V2 sense precision is below 0.85 are dropped before "
             "the slot inventory is frozen. Precision = design-weighted share (weights N/n over era strata) of "
             "sampled titles whose consensus slot_sense is 'y', on the population sampled by WP3a (2018+, slot "
             "filled under either opener rule, before the pre-V2 heuristic sense filter).",
        generated_by="analyses/validate_measures.py",
        lexicons_sha256=hashlib.sha256((C._SRC / "analyses" / "lexicons.json").read_bytes()).hexdigest(),
        dropped=[dict(slot=r.slot, word=r.word, variant=r.variant, precision_w=r.precision_w, n=r.n,
                      n_sense_y=r.n_sense_y, wilson_lo=r.wilson_lo, wilson_hi=r.wilson_hi,
                      precision_after_prefilter_w=r.precision_after_prefilter_w, swap_preserves_w=r.swap_preserves_w)
                 for r in dropped.itertuples()],
        dropped_words={s: sorted(dropped[dropped.slot == s].word.tolist()) for s in sorted(words.slot.unique())},
        kept_words={s: sorted(words[(words.slot == s) & ~words["drop"]].word.tolist()) for s in sorted(words.slot.unique())},
        borderline_kept=[dict(slot=r.slot, word=r.word, precision_w=r.precision_w, precision_unw=r.precision_unw,
                              n=r.n, precision_pre=r.precision_pre, n_pre=r.n_pre, precision_post=r.precision_post,
                              n_post=r.n_post) for r in words[words["borderline"]].itertuples()],
        sensitivity_unweighted_rule=dict(
            rule="drop if the unweighted share of sampled titles in the slot sense is below 0.85",
            dropped_words={s: sorted(words[(words.slot == s) & words.drop_if_unweighted_rule].word.tolist())
                           for s in sorted(words.slot.unique())}),
        notes=[
            "Dropping a word removes it from both the LLM-favoured and the neutral side of its slot (titles whose "
            "opener is that word become 'slot not filled').",
            "'decoding' fails even after the pre-V2 sense filter (see precision_after_prefilter_w), so the heuristic "
            "filter is not sufficient.",
            "borderline_kept lists kept words whose unweighted precision, or precision in one era (n >= 3), is below "
            "0.85; D3 should run leave-one-variant-out on them. Era-specific sense failures sit mostly in the pre "
            "era on the LLM-favoured side, which raises the pre-2024 LLM share and so biases the slot break toward "
            "zero.",
        ])
    (VAL / "slot_variants_dropped.json").write_text(json.dumps(jsonable(payload), indent=1))
    return dict(m=m, kappa=kap, words=words, slots=slots, by_source=by_source, payload=payload,
                adj=pd.DataFrame(rec))


# =====================================================================================================
# V3
# =====================================================================================================
def v3_analysis(feat: pd.DataFrame) -> dict:
    key = pd.read_csv(KEYS / "v3_key.csv", keep_default_na=False, na_values=[""])
    L = read_jsonl(LAB.glob("v3_batch*_A.jsonl"))
    assert len(L) == 300 and L.item_id.is_unique
    m = key.merge(L, on="item_id")
    for c in ["F_any", "f24", "f26", "f26_words", "f26_typo", "title_typo"]:
        m[c] = m[c].astype(str).str.lower().map({"true": 1, "false": 0}).astype(int)
    m.to_csv(VAL / "v3_ratings.csv", index=False)
    rng = np.random.default_rng(SEED)
    corr = []
    for c in ["F_any", "f24", "f24_n", "f26", "f26_words", "f26_typo", "title_typo"]:
        rho = stats.spearmanr(m[c], m.rating).statistic
        bs = []
        for _ in range(2000):
            i = rng.integers(0, len(m), len(m))
            bs.append(stats.spearmanr(m[c].to_numpy()[i], m.rating.to_numpy()[i]).statistic)
        lo, hi = np.nanpercentile(bs, [2.5, 97.5])
        auc = np.nan
        if m[c].nunique() == 2:
            pos, neg = m.rating[m[c] == 1], m.rating[m[c] == 0]
            auc = stats.mannwhitneyu(pos, neg).statistic / (len(pos) * len(neg))
        corr.append(dict(fingerprint=c, spearman=float(rho), lo=float(lo), hi=float(hi), auc=float(auc),
                         mean_rating_pos=float(m.rating[m[c] >= 1].mean()), mean_rating_neg=float(m.rating[m[c] == 0].mean())))
    corr = pd.DataFrame(corr)
    within = []
    for y, g in m.groupby("year"):
        within.append(dict(year=int(y), spearman_F_any=float(stats.spearmanr(g.F_any, g.rating).statistic),
                           spearman_f24=float(stats.spearmanr(g.f24, g.rating).statistic),
                           spearman_f26=float(stats.spearmanr(g.f26, g.rating).statistic)))
    within = pd.DataFrame(within)
    strat = m.groupby(["year", "fstat"]).rating.agg(["mean", "count"]).reset_index()
    rating_dist = m.groupby("fstat").rating.value_counts().unstack(fill_value=0)
    # design-weighted (population) correlation of rating with F_any within 2024-26
    cv = np.cov(np.vstack([m.F_any.to_numpy(float), m.rating.to_numpy(float)]), aweights=m.weight.to_numpy(float))
    wcorr = float(cv[0, 1] / np.sqrt(cv[0, 0] * cv[1, 1]))
    # F0 trend (undetected-use signal)
    f0 = m[m.fstat == "F0"]
    f0_trend = stats.spearmanr(f0.year, f0.rating)

    # specificity: fingerprint rates in 2021-22 (pre-ChatGPT) vs 2024-26
    flags = ["f24", "f24_2", "f26_words", "abs_nbhyphen", "abs_endash_compound", "f26_typo", "f26", "title_typo",
             "title_nbhyphen", "title_endash_compound", "F_any"]
    fr = feat.groupby("year")[flags].mean().reset_index()
    fr.insert(1, "n", feat.groupby("year").size().to_numpy())
    fr.to_csv(VAL / "v3_fingerprint_rates_by_year.csv", index=False)
    pre = feat[feat.year.isin([2021, 2022])]
    post = feat[feat.year.isin([2024, 2025, 2026])]
    fpr = []
    for f in flags:
        k = int(pre[f].sum())
        n = len(pre)
        lo, hi = clopper_pearson(k, n)
        fpr.append(dict(flag=f, n_2021_22=n, hits_2021_22=k, fpr=k / n, fpr_lo=lo, fpr_hi=hi,
                        rate_2024=float(feat[feat.year == 2024][f].mean()), rate_2025=float(feat[feat.year == 2025][f].mean()),
                        rate_2026=float(feat[feat.year == 2026][f].mean()),
                        excess_share_2024_26=float(1 - (k / n) / post[f].mean()) if post[f].mean() > 0 else np.nan))
    fpr = pd.DataFrame(fpr)
    fpr.to_csv(VAL / "v3_fpr_2021_22.csv", index=False)
    # words driving pre-2023 F24 hits
    w24 = pre.loc[pre.f24, "f24_words"].str.split("|").explode().value_counts().head(10)
    w26 = pre.loc[pre.f26_words, "f26_words_list"].str.split("|").explode().value_counts().head(10) \
        if "f26_words_list" in pre else pd.Series(dtype=int)

    # manual typography inspection
    h = feat[feat.title_nbhyphen | feat.title_endash_compound]
    rng2 = np.random.default_rng(TYPO_SEED)
    nb = h[h.title_nbhyphen]
    en = h[h.title_endash_compound & ~h.title_nbhyphen]
    s = pd.concat([nb.iloc[np.sort(rng2.choice(len(nb), min(50, len(nb)), replace=False))],
                   en.iloc[np.sort(rng2.choice(len(en), min(50, len(en)), replace=False))]])
    assert set(s.submission_id[~s.title_nbhyphen]) == set(TYPO_EN), "typography sample changed"
    s = s[["submission_id", "year", "title", "title_nbhyphen", "title_endash_compound"]].copy()
    s["cls"] = [("nbh_in_name" if sid in TYPO_NBH_IN_NAME else "nbh_compound") if nbh else TYPO_EN[sid]
                for sid, nbh in zip(s.submission_id, s.title_nbhyphen)]
    s["also_ascii_hyphen"] = s.title.map(lambda t: bool(re.search(r"[A-Za-z]-[A-Za-z]", t)))
    s["latex_or_pdf_artefact"] = False
    s.to_csv(VAL / "v3_typography_inspection.csv", index=False)
    typo_counts = s.cls.value_counts().to_dict()
    # all title hits: year profile and ASCII '--' persistence (rules out a blanket export conversion)
    uni = C.load_universe(["submission_id", "year", "title", "abstract"])
    yr = uni.groupby("year").agg(
        n=("title", "size"),
        title_endash_letters=("title", lambda s_: int(s_.map(lambda x: bool(re.search("[A-Za-z]–[A-Za-z]", x or ""))).sum())),
        title_u2011=("title", lambda s_: int(s_.map(lambda x: "‑" in (x or "")).sum())),
        title_ascii_dd_letters=("title", lambda s_: int(s_.map(lambda x: bool(re.search("[A-Za-z]--[A-Za-z]", x or ""))).sum())),
        abstract_ascii_dd_letters=("abstract", lambda s_: int(s_.map(lambda x: bool(re.search("[A-Za-z]--[A-Za-z]", x or ""))).sum())),
        abstract_endash_letters=("abstract", lambda s_: int(s_.map(lambda x: bool(re.search("[A-Za-z]–[A-Za-z]", x or ""))).sum())),
        abstract_u2011=("abstract", lambda s_: int(s_.map(lambda x: "‑" in (x or "")).sum())),
    ).reset_index()
    yr.to_csv(VAL / "v3_dash_codepoints_by_year.csv", index=False)
    pre26 = feat[(feat.year < 2026) & (feat.title_nbhyphen | feat.title_endash_compound)][["submission_id", "year", "title"]]
    return dict(m=m, corr=corr, within=within, strat=strat, rating_dist=rating_dist, wcorr=wcorr,
                f0_trend=dict(rho=float(f0_trend.statistic), p=float(f0_trend.pvalue)), fpr=fpr, fr=fr,
                w24=w24, w26=w26, typo=s, typo_counts=typo_counts, dash_years=yr, pre26=pre26,
                n_title_hits=int(len(h)), n_nbh=int(len(nb)), n_en=int(len(en)))


# =====================================================================================================
# V4
# =====================================================================================================
def v4_analysis(feat: pd.DataFrame) -> dict:
    from analyses import features_v2 as FV2
    ma = pd.read_parquet(C.TOPIC_DIR / "masked_abstracts.parquet", columns=["submission_id", "masked"])
    u = C.load_universe(["submission_id", "year", "abstract"])
    d = feat[["submission_id", "name_primary", "lead_raw", "lead_survives_mask", "lead_in_abstract"]].merge(
        u, on="submission_id").merge(ma, on="submission_id", how="left")
    nm = d[d.name_primary].copy()
    n2017 = int((nm.year == 2017).sum())
    nm = nm[nm.year >= 2018]
    nm["r3_survive"] = [FV2.lead_survives(mk, ld) for mk, ld in zip(nm.masked, nm.lead_raw)]
    nm["r1_text"] = [FV2.mask_abstract_lower(a, ld) for a, ld in zip(nm.abstract, nm.lead_raw)]
    nm["r1_survive"] = [FV2.lead_survives(mk, ld) for mk, ld in zip(nm.r1_text, nm.lead_raw)]

    def core(ld):
        return re.sub(r"[^a-z0-9]", "", (ld or "").lower())
    nm["lead_core"] = nm.lead_raw.map(core)
    nm["too_short_for_check"] = nm.lead_core.str.len() < 2
    # stricter: alphanumeric core of the lead as a substring of the alphanumeric masked text (no word boundary)
    def tok_sub(c, text):
        if len(c) < 3:
            return False
        return any(c in re.sub(r"[^a-z0-9]", "", t) for t in (text or "").lower().split())
    nm["r3_substring"] = [tok_sub(c, mk) for c, mk in zip(nm.lead_core, nm.masked)]
    nm["r1_substring"] = [tok_sub(c, mk) for c, mk in zip(nm.lead_core, nm.r1_text)]
    ex_r1 = nm[nm.r1_survive][["submission_id", "year", "lead_raw"]].head(30)

    def first_tok(c, text):
        for t in (text or "").lower().split():
            a = re.sub(r"[^a-z0-9]", "", t)
            if len(c) >= 3 and c in a:
                return t
        return ""
    sub = nm[nm.r3_substring].copy()
    sub["token"] = [first_tok(c, mk) for c, mk in zip(sub.lead_core, sub.masked)]
    def tcore(t):
        return re.sub(r"[^a-z0-9]", "", re.sub(r"\\[a-z]+", "", t))
    sub["tok_core"] = sub.token.map(tcore)

    def sub_cat(c, t, raw):
        if re.search(r"https?:|www\.|\.(com|io|org|ai|net)|github", raw):
            return "URL or handle containing the lead"
        if t == c or t in (c + "s", c + "es"):
            return "variant spelling of the lead (LaTeX, markdown, Unicode hyphen; or its plural)"
        if t.startswith(c):
            return "lead letters + suffix (mostly ordinary words: flow-based, stitching, divergence)"
        return "lead letters inside a longer word (coincidental: space, complex)"
    sub["category"] = [sub_cat(c, t, r) for c, t, r in zip(sub.lead_core, sub.tok_core, sub.token)]
    sub[["submission_id", "year", "lead_raw", "token", "category"]].to_csv(VAL / "v4_r3_substring_hits.csv", index=False)
    # the same classification for the R1 text
    sub1 = nm[nm.r1_substring].copy()
    sub1["token"] = [first_tok(c, mk) for c, mk in zip(sub1.lead_core, sub1.r1_text)]
    sub1["cat"] = [sub_cat(c, tcore(t), t) for c, t in zip(sub1.lead_core, sub1.token)]
    n_var3 = int(sub.category.str.startswith("variant").sum() + sub.category.str.startswith("URL").sum())
    n_var1 = int(sub1.cat.str.startswith("variant").sum() + sub1.cat.str.startswith("URL").sum())
    ex_sub = nm[nm.r3_substring][["submission_id", "year", "lead_raw"]]
    # substring hits are mostly ordinary-word leads whose letters recur inside other words; keep examples
    reps = pd.read_csv(C.OUT / "d1_break" / "T1_2_representations.csv")
    auc = reps.pivot_table(index="rep", columns="design", values="auc_mean")
    gap = {}
    for a_, b_ in [("R1u", "R1"), ("R4", "R3")]:
        if a_ in auc.index and b_ in auc.index:
            gap[f"{a_}-{b_}"] = {k: float(auc.loc[a_, k] - auc.loc[b_, k]) for k in auc.columns}
    feats_top = C.OUT / "d1_break" / "v4_top200_R1_features.csv"
    top = pd.read_csv(feats_top) if feats_top.exists() else None
    # name fragments among top-200 R1 features: any feature token equal to a NAME lead core (>= 3 chars)
    frag = []
    if top is not None:
        leads = set(c for c in nm.lead_core if len(c) >= 3)
        for f in top.feature:
            for tok in str(f).split():
                if tok.lower() in leads:
                    frag.append(dict(feature=f, token=tok))
    res = dict(n_name_2018_26=int(len(nm)), n_name_2017_not_masked=n2017,
               r3_survive=int(nm.r3_survive.sum()), r3_survive_share=float(nm.r3_survive.mean()),
               r3_survive_features_v2=int(nm.lead_survives_mask.sum()),
               r1_survive=int(nm.r1_survive.sum()), r1_survive_share=float(nm.r1_survive.mean()),
               too_short_for_check=int(nm.too_short_for_check.sum()),
               r3_substring=int(nm.r3_substring.sum()), r1_substring=int(nm.r1_substring.sum()),
               lead_in_abstract_share=float(nm.lead_in_abstract.mean()),
               auc_gap=gap, auc_table=auc.reset_index().to_dict(orient="records"),
               top200_name_fragments=frag,
               r3_substring_categories=sub.category.value_counts().to_dict(),
               r3_variant_or_url_leaks=n_var3, r3_variant_or_url_share=n_var3 / len(nm),
               r1_variant_or_url_leaks=n_var1, r1_variant_or_url_share=n_var1 / len(nm))
    nm[["submission_id", "year", "lead_raw", "r3_survive", "r1_survive", "r3_substring", "r1_substring",
        "too_short_for_check"]].to_csv(VAL / "v4_mask_checks.csv", index=False)
    return dict(res=res, ex_r1=ex_r1, ex_sub=ex_sub, sub=sub)


# =====================================================================================================
# V5
# =====================================================================================================
def v5_analysis() -> dict:
    key = pd.read_csv(KEYS / "v5_key.csv", keep_default_na=False, na_values=[""])
    L = read_jsonl(LAB.glob("v5_batch*_A.jsonl"))
    bat = read_jsonl(BAT.glob("v5_batch*.jsonl"))
    assert len(L) == 100 and L.item_id.is_unique
    m = key.merge(L, on="item_id").merge(bat, on="item_id")
    m["llm_cluster"] = m.llm_cluster.astype(str).str.lower().map({"true": 1, "false": 0}).astype(int)
    m["about_lms_y"] = (m.about_lms == "y").astype(int)
    assert ((m.lm_papers >= 7) == (m.about_lms_y == 1)).all()
    u = C.load_universe(["submission_id", "title", "llm_regex", "topic100", "year"])
    reg = dict(zip(u.submission_id, u.llm_regex))
    title_of = dict(zip(u.submission_id, u.title))
    m["regex_in_shown"] = [sum(bool(reg.get(s, False)) for s in ids.split("|")) for ids in m.paper_ids]
    m["central_titles"] = [" || ".join(title_of.get(s, "") for s in ids.split("|")[:3]) for ids in m.paper_ids]
    yrs = dict(zip(u.submission_id, u.year))
    m["shown_median_year"] = [float(np.median([yrs[s] for s in ids.split("|")])) for ids in m.paper_ids]
    # share of U papers by year per cluster (to explain disagreements: recent composition vs all-years regex share)
    rec = u[u.year >= 2024].groupby("topic100").llm_regex.mean()
    m["llm_regex_share_2024_26"] = m.cluster.map(rec)
    m["manual_label_verdict"] = m.item_id.map(lambda i: V5_CHECK.get(i, ("", "", ""))[0])
    m["manual_lm_verdict"] = m.item_id.map(lambda i: V5_CHECK.get(i, ("", "", ""))[1])
    m["manual_note"] = m.item_id.map(lambda i: V5_CHECK.get(i, ("", "", ""))[2])
    # the 10 checked clusters = 5 disagreements + 5 random agreements (seed V5_SEED)
    dis = m[m.llm_cluster != m.about_lms_y]
    rest = m[m.llm_cluster == m.about_lms_y].sort_values("item_id")
    pick = rest.iloc[np.sort(np.random.default_rng(V5_SEED).choice(len(rest), 5, replace=False))]
    assert set(dis.item_id) | set(pick.item_id) == set(V5_CHECK), "V5 manual-check sample changed"
    out = m[["cluster", "label", "about_lms", "lm_papers", "n_cluster", "llm_regex_share", "llm_regex_share_2024_26",
             "llm_cluster", "regex_in_shown", "shown_median_year", "manual_label_verdict", "manual_lm_verdict",
             "manual_note", "central_titles", "item_id"]].rename(columns={"cluster": "topic100",
                                                                         "llm_cluster": "llm_cluster_regex_rule"})
    out = out.sort_values("topic100")
    out.to_csv(VAL / "topic100_labels.csv", index=False)
    k, lo, hi, agr = kappa_ci(m.llm_cluster, m.about_lms_y, seed=SEED)
    conf = pd.crosstab(m.llm_cluster.map({1: "regex rule: LLM cluster", 0: "regex rule: not"}),
                       m.about_lms.map({"y": "annotator: about LMs", "n": "annotator: not"}))
    rho = stats.spearmanr(m.llm_regex_share, m.lm_papers)
    rho2 = stats.spearmanr(m.regex_in_shown, m.lm_papers)
    paper_level = dict(mean_abs_diff=float((m.regex_in_shown - m.lm_papers).abs().mean()),
                       mean_regex_minus_annot=float((m.regex_in_shown - m.lm_papers).mean()))
    # ARI / NMI MiniLM vs bge on U
    t = C.load_universe(["submission_id", "topic50", "topic100"]).merge(C.load_topics_bge(), on="submission_id")
    ari = dict(k50=dict(ari=float(adjusted_rand_score(t.topic50, t.topic50_bge)),
                        nmi=float(normalized_mutual_info_score(t.topic50, t.topic50_bge))),
               k100=dict(ari=float(adjusted_rand_score(t.topic100, t.topic100_bge)),
                         nmi=float(normalized_mutual_info_score(t.topic100, t.topic100_bge))))
    # flag-level agreement (paper level) between MiniLM and bge LLM flags, recomputed
    uu = C.load_universe(["submission_id", "llm_cluster", "llm_topic"]).merge(C.load_topics_bge(), on="submission_id")
    flag_k = dict(cluster_flag=float(cohen_kappa_score(uu.llm_cluster, uu.llm_cluster_bge)),
                  union_flag=float(cohen_kappa_score(uu.llm_topic, uu.llm_topic_bge)))
    return dict(m=m, out=out, kappa=dict(kappa=k, lo=lo, hi=hi, raw_agreement=agr), conf=conf,
                spearman_share=dict(rho=float(rho.statistic), p=float(rho.pvalue)),
                spearman_shown=dict(rho=float(rho2.statistic), p=float(rho2.pvalue)), paper_level=paper_level,
                ari=ari, flag_k=flag_k, dis=dis)


# =====================================================================================================
# V6
# =====================================================================================================
def v6_analysis() -> dict:
    from common import read_table
    u = C.load_universe(["submission_id", "year", "share_new_authors", "max_prior_subs", "exp_valid"])
    a = read_table("submission_authors")[["submission_id", "year", "source_list_position", "native_id",
                                          "native_id_kind", "declared_id_key"]]
    a = a[a.submission_id.isin(set(u.submission_id))].copy()
    a["has_key"] = a.declared_id_key.notna() & (a.declared_id_key.astype(str) != "\\N")
    kind_year = pd.crosstab(a.year, a.native_id_kind)
    kind_share = kind_year.div(kind_year.sum(axis=1), axis=0)
    k = a[a.has_key]
    ky = k.groupby(["declared_id_key", "year", "native_id_kind"]).submission_id.nunique().rename("papers").reset_index()
    dist = ky.groupby(["year", "native_id_kind"]).papers.agg(
        n_keys="size", mean="mean", median="median", p90=lambda x: x.quantile(0.9), p99=lambda x: x.quantile(0.99),
        max="max", share_single=lambda x: (x == 1).mean(), over_40=lambda x: int((x > 40).sum())).reset_index()
    dist.to_csv(VAL / "v6_papers_per_key.csv", index=False)
    over = ky[ky.papers > 40].copy()
    nid = k.drop_duplicates("declared_id_key").set_index("declared_id_key").native_id
    over["key_prefix"] = over.declared_id_key.astype(str).str[:15]
    # non-person IDs (kind 'other') are shown; profile IDs are not printed
    over["native_id_if_not_profile"] = np.where(over.native_id_kind == "profile", "",
                                                over.declared_id_key.map(nid).fillna("").astype(str))
    over = over.sort_values(["year", "papers"], ascending=[True, False])
    over[["key_prefix", "year", "native_id_kind", "papers", "native_id_if_not_profile"]].to_csv(
        VAL / "v6_keys_over40.csv", index=False)
    # share of U papers (by year) that carry at least one >40 key
    flagged = set(zip(over.declared_id_key, over.year))
    k_fl = k[[ (kk, yy) in flagged for kk, yy in zip(k.declared_id_key, k.year)]]
    papers_touched = k_fl.groupby("year").submission_id.nunique()

    # alias sensitivity: profile keys with trailing digits stripped (~Jane_Doe1, ~Jane_Doe2 -> ~Jane_Doe)
    p = k[k.native_id_kind == "profile"].copy()
    p["alias"] = p.native_id.astype(str).str.replace(r"\d+$", "", regex=True)
    al = p.groupby("year").agg(profile_keys=("declared_id_key", "nunique"), aliases=("alias", "nunique")).reset_index()
    al["keys_per_alias"] = al.profile_keys / al.aliases
    pay = p.groupby(["alias", "year"]).submission_id.nunique().rename("papers").reset_index()
    al["alias_over_40"] = al.year.map(pay[pay.papers > 40].groupby("year").size()).fillna(0).astype(int)
    al["key_over_40"] = al.year.map(ky[(ky.native_id_kind == "profile") & (ky.papers > 40)].groupby("year").size()
                                    ).fillna(0).astype(int)
    al["alias_max_papers"] = al.year.map(pay.groupby("year").papers.max())
    ex_multi = p.groupby("alias").declared_id_key.nunique()
    al_summary = dict(profile_keys_all=int(p.declared_id_key.nunique()), aliases_all=int(p.alias.nunique()),
                      aliases_merging_2plus_keys=int((ex_multi >= 2).sum()),
                      share_profile_rows_in_merged_aliases=float(p.alias.map(ex_multi).ge(2).mean()))

    # effect of alias collapse on the paper-level experience covariates (exp_valid years 2022+)
    def covariates(df, keycol):
        ky_ = df.groupby([keycol, "year"]).submission_id.nunique().rename("n").reset_index().sort_values([keycol, "year"])
        ky_["prior_subs"] = ky_.groupby(keycol).n.cumsum() - ky_.n
        d_ = df.merge(ky_[[keycol, "year", "prior_subs"]], on=[keycol, "year"])
        d_["new"] = (d_.prior_subs == 0).astype(float)
        g = d_.groupby("submission_id")
        return pd.DataFrame({"max_prior_subs": g.prior_subs.max(), "share_new_authors": g.new.mean()})
    base = k[["submission_id", "year", "declared_id_key", "native_id", "native_id_kind"]].copy()
    base["alias"] = np.where(base.native_id_kind == "profile",
                             base.native_id.astype(str).str.replace(r"\d+$", "", regex=True),
                             base.declared_id_key.astype(str))
    ex = covariates(base, "declared_id_key")
    ali = covariates(base, "alias")
    cmp_ = ex.join(ali, lsuffix="_exact", rsuffix="_alias").reset_index().merge(u[["submission_id", "year"]],
                                                                               on="submission_id")
    cmp_ = cmp_[cmp_.year >= 2022]
    eff = dict(n_papers=int(len(cmp_)),
               corr_max_prior_subs=float(np.corrcoef(np.log1p(cmp_.max_prior_subs_exact), np.log1p(cmp_.max_prior_subs_alias))[0, 1]),
               corr_share_new=float(np.corrcoef(cmp_.share_new_authors_exact, cmp_.share_new_authors_alias)[0, 1]),
               share_papers_share_new_changed=float((cmp_.share_new_authors_exact != cmp_.share_new_authors_alias).mean()),
               mean_share_new_exact=float(cmp_.share_new_authors_exact.mean()),
               mean_share_new_alias=float(cmp_.share_new_authors_alias.mean()),
               share_papers_maxprior_changed=float((cmp_.max_prior_subs_exact != cmp_.max_prior_subs_alias).mean()))
    by_year_eff = cmp_.groupby("year").apply(lambda g: pd.Series(dict(
        mean_share_new_exact=g.share_new_authors_exact.mean(), mean_share_new_alias=g.share_new_authors_alias.mean(),
        share_changed=(g.share_new_authors_exact != g.share_new_authors_alias).mean())), include_groups=False).reset_index()
    al.to_csv(VAL / "v6_alias_sensitivity.csv", index=False)
    by_year_eff.to_csv(VAL / "v6_alias_covariate_effect.csv", index=False)
    # email vs profile era: share of new keys per year (exact keys) and positions with a usable key
    era = u.groupby("year").agg(n=("submission_id", "size"), mean_share_new=("share_new_authors", "mean"),
                                mean_max_prior_subs=("max_prior_subs", "mean")).reset_index()
    pos = a.groupby("year").agg(positions=("has_key", "size"), with_key=("has_key", "mean")).reset_index()
    era = era.merge(pos, on="year")
    era = era.merge(kind_share.reset_index(), on="year", how="left")
    era.to_csv(VAL / "v6_email_profile_eras.csv", index=False)
    return dict(dist=dist, over=over, papers_touched=papers_touched, al=al, al_summary=al_summary, eff=eff,
                by_year_eff=by_year_eff, era=era, kind_share=kind_share)


# =====================================================================================================
# Figures
# =====================================================================================================
def figures(v1: dict):
    import matplotlib.pyplot as plt
    C.set_style()
    # (1) precision / recall of the primary NAME detector by year block
    b = v1["binm"]
    pm = b[(b.detector == "name_primary") & (b.truth == "t_name") & (b.block.isin(BLOCKS)) &
           (b.estimator == "PS (main + hard)")].copy()
    fig, ax = C.new_fig("single", height=2.4)
    x = np.arange(len(BLOCKS))
    for i, (met, nm) in enumerate([("precision", "Precision"), ("recall", "Recall")]):
        off = -0.08 if i == 0 else 0.08
        ax.errorbar(x + off, pm[met], yerr=[pm[met] - pm[met + "_lo"], pm[met + "_hi"] - pm[met]], color=C.color(i),
                    marker="o", ms=5, lw=2, capsize=0, elinewidth=1.2, label=nm)
    ax.set_xticks(x, [b.replace("-", "–") for b in BLOCKS])
    ax.tick_params(axis="x", labelsize=7.5)
    ax.set_ylim(0.88, 1.005)
    ax.set_ylabel("Share (population-weighted)")
    ax.set_xlabel("Year block")
    ax.legend(loc="lower right", ncol=2)
    data = pm[["block", "precision", "precision_lo", "precision_hi", "recall", "recall_lo", "recall_hi", "n_items"]]
    C.save_fig(fig, "fig_v1_name_detector_precision_recall", VAL, data=data)
    # (2) observed vs Rogan-Gladen corrected NAME share by year
    rg = v1["rg"][v1["rg"].detector == "name_primary"]
    fig, ax = C.new_fig("single", height=2.4)
    ax.plot(rg.year, 100 * rg.p_obs, color=C.color(0), marker="o", ms=5, lw=2, label="Detector (observed)")
    ax.fill_between(rg.year, 100 * rg.p_rg_lo, 100 * rg.p_rg_hi, color=C.color(1), alpha=0.18, lw=0)
    ax.plot(rg.year, 100 * rg.p_rg, color=C.color(1), marker="s", ms=5, lw=2, label="Rogan-Gladen corrected")
    ax.set_ylabel("NAME titles (% of submissions)")
    ax.set_xticks(rg.year, [str(y)[2:] if y not in (2017, 2026) else str(y) for y in rg.year])
    ax.legend(loc="upper left")
    C.save_fig(fig, "fig_v1_name_share_corrected", VAL,
               data=rg[["year", "n_papers", "p_obs", "Se", "Sp", "p_rg", "p_rg_lo", "p_rg_hi", "p_ppv_npv"]])
    plt.close("all")


# =====================================================================================================
# Report
# =====================================================================================================
def write_report(v1, v2, v3, v4, v5, v6) -> tuple[str, dict]:
    L = []
    A = L.append
    its = v1["its"]["name_primary"]
    kap = v1["kappa"]
    bm = v1["binm"]

    def met_row(det, tru, blk, est="PS (main + hard)"):
        r = bm[(bm.detector == det) & (bm.truth == tru) & (bm.block == blk) & (bm.estimator == est)].iloc[0]
        return r

    A("# Measurement validation (WP3b, PLAN.md section 3, V1-V6)")
    A("")
    A("Produced by `src/analyses/validate_measures.py`. All numbers are regenerated from the blind annotation passes in "
      "`outputs/validation/labels/` and the frozen features (`features_v2.parquet`, lexicons v2.0). Annotation passes A and B are LLM annotators "
      "(different models and codebooks), blind to year, outcome and detector output. "
      "\"Consensus\" means the label both passes gave. Where they differed, the PI's delegate adjudicated from the "
      "title (or cluster) text alone; every adjudication is recorded in a CSV. Declared author IDs are \"declared "
      "profile keys\", not people.")
    A("")
    # ------------------------------------------------------------------ summary
    pr = met_row("name_primary", "t_name", "all")
    A("## Summary")
    A("")
    kap_main = kap[kap["items"] == "all"].set_index("label")
    A(f"- **V1 agreement.** Passes A and B agree almost perfectly.")
    A(f"  - compound κ = {kap_main.loc['compound','kappa']:.3f}, question κ = {kap_main.loc['question','kappa']:.3f}.")
    A(f"  - lead type κ = {kap_main.loc['lead_type','kappa']:.3f} (coined-name binary "
      f"{kap_main.loc['coined_name (binary)','kappa']:.3f}), orthography κ = {kap_main.loc['lead_orthography','kappa']:.3f}, "
      f"casing κ = {kap_main.loc['casing','kappa']:.3f}.")
    core_k = kap_main.loc[["compound", "lead_type", "lead_orthography", "casing", "question"], "kappa"]
    A(f"  - {'All five labels clear' if (core_k >= 0.80).all() else 'Not all labels clear'} the 0.80 target "
      f"(lowest {core_k.min():.3f}; lowest lower CI bound {kap_main.loc[core_k.index, 'lo'].min():.3f}). "
      f"{int(v1['m'].adjudicated.sum())} of 1,400 items needed adjudication. "
      f"The spot check found {v1['spot_summary']['n_error']} clear errors among 150 agreed items "
      f"(95% CI 0–{100*v1['spot_summary']['error_ci'][1]:.1f}%) and {v1['spot_summary']['n_borderline']} borderline calls.")
    A(f"- **V1 NAME detector (primary), against the adjudicated consensus.** Population estimates over all years "
      f"(post-stratified: main sample plus the two-token-lead hard cells):")
    A(f"  - precision {fmt_ci(pr.precision, pr.precision_lo, pr.precision_hi)}%;")
    A(f"  - recall {fmt_ci(pr.recall, pr.recall_lo, pr.recall_hi)}%;")
    A(f"  - specificity {fmt_ci(pr.specificity, pr.specificity_lo, pr.specificity_hi)}%.")
    d = v1["drift"]
    pb = d["precision_by_block"]
    A(f"  - Precision by block runs from {100*min(pb.values()):.1f}% ({min(pb, key=pb.get)}) to "
      f"{100*max(pb.values()):.1f}% ({max(pb, key=pb.get)}): a range of {100*d['precision_range']:.1f} pp.")
    A(f"  - Pass criterion < 5 pp: **{'met' if d['pass_lt_5pp'] else 'not met'}** on the point estimate. "
      f"Six noisy block estimates spread by {100*d['precision_range_null_median']:.1f} pp (median) even with no drift; "
      f"p = {d['precision_range_null_p']:.2f} for a range this large.")
    A(f"  - Post (2024–26) minus pre block mean: {100*d['precision_post_minus_pre']:+.1f} pp "
      f"[{100*d['precision_post_minus_pre_ci'][0]:+.1f}, {100*d['precision_post_minus_pre_ci'][1]:+.1f}].")
    A(f"- **V1 corrected ITS.** The block-specific misclassification-corrected slope-change OR is "
      f"{its['corrected']['OR']:.3f} [{its['corrected']['OR_lo']:.3f}, {its['corrected']['OR_hi']:.3f}], against "
      f"{its['uncorrected']['OR']:.3f} [{its['uncorrected']['OR_lo']:.3f}, {its['uncorrected']['OR_hi']:.3f}] uncorrected.")
    A(f"  - OR ratio {its['OR_ratio']:.3f}: within 10% on the OR scale, **{'yes' if its['within_10pct_OR'] else 'no'}**. "
      f"On the log-OR scale the change is {100*its['logOR_rel_change']:+.1f}% "
      f"({'within' if its['within_10pct_logOR'] else 'outside'} 10%).")
    dr = v2["payload"]["dropped"]
    A(f"- **V2 slots.** Words to drop (sense precision < 0.85): "
      + ", ".join(f"{x['slot']}/{x['word']} ({x['precision_w']:.2f}, n={x['n']})" for x in dr) + ". "
      f"Written to `slot_variants_dropped.json`.")
    c3 = v3["corr"].set_index("fingerprint")
    A(f"- **V3.** LLM-polish ratings correlate weakly with the fingerprints: Spearman ρ = {c3.loc['F_any','spearman']:.2f} for F, "
      f"{c3.loc['f24','spearman']:.2f} for F24 and {c3.loc['f26','spearman']:.2f} for F26. This is weak convergent validity only.")
    fp = v3["fpr"].set_index("flag")
    A(f"  - False-positive rates in 2021–22: F24 {pct(fp.loc['f24','fpr'])}%, F26 {pct(fp.loc['f26','fpr'])}%, "
      f"F {pct(fp.loc['F_any','fpr'])}%, title typography {pct(fp.loc['title_typo','fpr'],2)}%.")
    A(f"  - No LaTeX or PDF artefacts among the 100 inspected typography titles.")
    r4 = v4["res"]
    A(f"- **V4.** The lead string (whole word) survives the R3 mask in {r4['r3_survive']} of {r4['n_name_2018_26']:,} NAME "
      f"abstracts ({'meets' if r4['r3_survive'] == 0 else 'misses'} the 0% target) and the R1 mask in {r4['r1_survive']}.")
    A(f"  - Variant spellings of the name do survive: LaTeX-wrapped, markdown, other Unicode hyphens, project URLs. "
      f"That is {r4['r3_variant_or_url_leaks']} abstracts ({100*r4['r3_variant_or_url_share']:.2f}%) under R3 and "
      f"{r4['r1_variant_or_url_leaks']} ({100*r4['r1_variant_or_url_share']:.2f}%) under R1.")
    A(f"- **V5.** The annotator's LM flag agrees with the regex LLM-cluster rule at κ = {v5['kappa']['kappa']:.2f}; "
      f"all {len(v5['dis'])} disagreements are clusters the annotator calls LM but whose all-years regex share sits just below 0.5. "
      f"MiniLM vs bge topic100 ARI = {v5['ari']['k100']['ari']:.3f} (NMI {v5['ari']['k100']['nmi']:.3f}).")
    o = v6["over"]
    A(f"- **V6.** {len(o)} exact key-years exceed 40 papers (max {int(v6['dist']['max'].max())}); "
      f"{int(v6['al'].alias_over_40.sum())} alias-years do once trailing digits are stripped. Collapsing trailing digits changes "
      f"{100*v6['eff']['share_papers_share_new_changed']:.1f}% of 2022+ papers' new-key share "
      f"(mean {v6['eff']['mean_share_new_exact']:.3f} → {v6['eff']['mean_share_new_alias']:.3f}).")
    A("")

    # ------------------------------------------------------------------ V1
    A("## V1. NAME, compound, orthography and casing detectors")
    A("")
    A("### Sample and agreement")
    A("- **Sample:**")
    A("  - 1,200 main items: 6 year blocks × (100 NAME-positive, spread over the 4 orthography classes; 50 phrase-colon "
      "compounds; 50 non-compound). Design weights are N_h/n_h.")
    A("  - 200 hard cases: two-token leads, LaTeX, dash compounds, genre and dictionary-word leads.")
    A("  - Population estimates combine the main sample with the two-token-lead hard strata by post-stratification (below). "
      "The other hard strata are diagnostics only.")
    A("- **Cohen's κ, pass A vs pass B** (item-bootstrap 95% CI):")
    A("")
    kt = kap.copy()
    kt["κ [95% CI]"] = [("" if not np.isfinite(k) else f"{k:.3f} [{lo:.3f}, {hi:.3f}]") for k, lo, hi in zip(kt.kappa, kt.lo, kt.hi)]
    kt["agreement"] = kt.raw_agreement.map(lambda v: f"{100*v:.1f}%")
    A(md_table(kt[["label", "items", "n", "κ [95% CI]", "agreement", "n_disagree"]]))
    A("")
    A("- Compound, lead string and question agree on every item. The disagreements concentrate on whether a multi-word "
      "lead is a coined name or a descriptive phrase.")
    A("- **Adjudication.**")
    A(f"  - {int(v1['m'].adjudicated.sum())} items, {len(v1['adj'])} label decisions; see `v1_adjudications.csv`.")
    A(f"  - Rule: {ADJ_RULE_V1}")
    na = v1["adj"]
    lt = na[na.label == "lead_type"]
    A(f"  - Lead type: {len(lt)} disputes, resolved as coined_name in {int((lt.adjudicated=='coined_name').sum())} and "
      f"descriptive_phrase in {int((lt.adjudicated=='descriptive_phrase').sum())}.")
    A(f"  - Pass A had called coined_name in {int((lt.pass_A=='coined_name').sum())} of these, pass B in {int((lt.pass_B=='coined_name').sum())}.")
    A("  - Because this boundary is the main source of disagreement, every detector metric is also reported against a lenient "
      "construct (coined in either pass) and a strict one (coined in both).")
    s = v1["spot_summary"]
    A(f"- **Spot check of agreed items.**")
    A(f"  - 150 random agreed items were checked: {s['n_error']} clear errors and {s['n_borderline']} borderline "
      f"({s['n_borderline_lead_type']} lead type, {s['n_borderline_casing']} casing).")
    A(f"  - Estimated consensus error ≤ {100*s['error_ci'][1]:.1f}% (95% upper bound); "
      f"{100*s['error_or_borderline_rate']:.1f}% if borderline calls are counted as errors.")
    A("  - The checker is the adjudicator, so this is not an independent audit. Details in `v1_spotcheck.csv`.")
    A("")
    A("### Detector accuracy against the consensus")
    A("- **Estimator (primary): post-stratified, main sample plus hard cases.**")
    A("  - Each main sampling stratum is split into the cell of two-token leads and the rest, using known population counts.")
    A("  - The rest is estimated from the main items.")
    A("  - Two-token cells are estimated per era and detector side from the pooled main and hard two-token items, which are "
      "random draws from exactly those cells.")
    A("- **Why:** the main sample, allocated by orthography, contains almost no two-token NAME leads in 2024–26 (none in 2026), "
      "yet the consensus calls most of them descriptive (table below). The main-only Horvitz–Thompson (HT) estimator is "
      "unbiased but misses this cell by chance, and its bootstrap CI cannot show it.")
    A("- CIs: stratified bootstrap of both samples (2,000 reps). Values are percentages. Items, FP and FN are unweighted counts in "
      "the main sample.")
    A("")
    A("Two-token lead cells (compound title, lead of exactly 2 tokens; main + hard items):")
    A("")
    tcl = v1["tcell"].copy()
    tcl["share coined [Wilson 95%]"] = [f"{p_:.2f} [{l_:.2f}, {h_:.2f}]" for p_, l_, h_ in zip(tcl.share_coined, tcl.lo, tcl.hi)]
    tcl["detector"] = tcl.detector_NAME.map({1: "NAME", 0: "not NAME"})
    A(md_table(tcl[["era", "detector", "N_population", "n_main", "n_hard", "coined", "share coined [Wilson 95%]"]]))
    A("")
    rows = []
    for det, tru, lab in BIN_SPECS:
        for blk in BLOCKS + ["all"]:
            r = met_row(det.replace("d_", ""), tru, blk)
            rows.append({"detector vs construct": lab if blk == BLOCKS[0] else "", "block": blk,
                         "precision": fmt_ci(r.precision, r.precision_lo, r.precision_hi),
                         "recall": fmt_ci(r.recall, r.recall_lo, r.recall_hi),
                         "specificity": fmt_ci(r.specificity, r.specificity_lo, r.specificity_hi),
                         "items": r.n_items, "FP": r.n_fp, "FN": r.n_fn})
    A(md_table(pd.DataFrame(rows)))
    A("")
    A("Main-only HT estimates for the primary detector, for comparison:")
    A("")
    rows = []
    for blk in BLOCKS + ["all"]:
        r = met_row("name_primary", "t_name", blk, "HT (main only)")
        rows.append({"block": blk, "precision (HT)": fmt_ci(r.precision, r.precision_lo, r.precision_hi),
                     "recall (HT)": fmt_ci(r.recall, r.recall_lo, r.recall_hi),
                     "specificity (HT)": fmt_ci(r.specificity, r.specificity_lo, r.specificity_hi)})
    A(md_table(pd.DataFrame(rows)))
    A("")
    A(f"- **Precision drift (primary, PS).**")
    A(f"  - By block: " + ", ".join(f"{b} {100*v:.1f}" for b, v in d["precision_by_block"].items()) + ".")
    A(f"  - Range {100*d['precision_range']:.1f} pp (bootstrap 95% CI {100*d['precision_range_ci'][0]:.1f}–{100*d['precision_range_ci'][1]:.1f}).")
    A(f"  - Under a common precision, sampling noise alone gives a median range of {100*d['precision_range_null_median']:.1f} pp; "
      f"p = {d['precision_range_null_p']:.2f} for a range at least this large.")
    A(f"  - Post (2024–26) minus pre (2017–23) block mean: {100*d['precision_post_minus_pre']:+.1f} pp "
      f"[{100*d['precision_post_minus_pre_ci'][0]:+.1f}, {100*d['precision_post_minus_pre_ci'][1]:+.1f}].")
    A(f"  - Recall by block: " + ", ".join(f"{b} {100*v:.1f}" for b, v in d["recall_by_block"].items()) +
      f"; range {100*d['recall_range']:.1f} pp.")
    fpn = v1["fp"]
    fnn = v1["fn"]
    A(f"- **Error patterns of the primary detector** (all 1,400 items, main and hard; rule-based categories; full lists in "
      "`v1_name_false_positives.csv` and `v1_name_false_negatives.csv`):")
    for nm_, df_, lc in [("False positives", fpn, "lead_raw"), ("False negatives", fnn, "lead_cons")]:
        A(f"  - {nm_} ({len(df_)}):")
        for cat, g in df_.groupby("category"):
            ex = "; ".join(f"'{x}'" for x in g[lc].fillna("").head(4))
            A(f"    - {cat}: {len(g)} (e.g. {ex}).")
    A("")
    A("**Hard cases** (unweighted; the two-token strata enter the PS estimator; the others are diagnostics only):")
    A("")
    A(md_table(v1["hard"], "{:.2f}"))
    A("")
    A("**Orthography** (items where the detector and the consensus both say NAME; design-weighted, %):")
    A("")
    o = v1["orth"].copy()
    o["value"] = [fmt_ci(e, l, h) for e, l, h in zip(o.est, o.lo, o.hi)]
    ot = o.pivot_table(index="cls", columns="block", values="value", aggfunc="first")[BLOCKS + ["all"]]
    A(md_table(ot.reset_index()))
    A("")
    A("Confusion matrix (rows: detector, columns: consensus; unweighted counts):")
    A("")
    A(md_table(v1["conf_orth"].reset_index().rename(columns={"d_orth": "detector"})))
    A("")
    A("**Casing** (all main items; the detector's 'mixed' and 'other' both map to 'other'; design-weighted, %):")
    A("")
    o = v1["cas"].copy()
    o["value"] = [fmt_ci(e, l, h) for e, l, h in zip(o.est, o.lo, o.hi)]
    ot = o.pivot_table(index="cls", columns="block", values="value", aggfunc="first")[BLOCKS + ["all"]]
    A(md_table(ot.reset_index()))
    A("")
    A("Confusion matrix (rows: detector, columns: consensus; unweighted counts):")
    A("")
    A(md_table(v1["conf_cas"].reset_index().rename(columns={"d_casing": "detector"})))
    A("")
    A("### Rogan–Gladen corrected yearly prevalence")
    A("- **Formula:** p_RG = (p_obs + Sp_b − 1)/(Se_b + Sp_b − 1), with block-specific Se/Sp from the PS estimator.")
    A("- **CI:** validation-sample uncertainty only.")
    A("- **Checks:** \"PPV/NPV\" is the calibration estimator p_obs·PPV + (1 − p_obs)(1 − NPV). \"RG (HT)\" uses main-only Se/Sp.")
    A("")
    rg = v1["rg"]
    rows = []
    for det in ["name_primary", "name_strict", "name_loose", "name_compound"]:
        g = rg[rg.detector == det]
        for _, r in g.iterrows():
            rows.append({"detector": det if r.year == 2017 else "", "year": int(r.year), "observed %": f"{100*r.p_obs:.1f}",
                         "Se": f"{r.Se:.3f}", "Sp": f"{r.Sp:.3f}",
                         "RG-corrected % [95% CI]": f"{100*r.p_rg:.1f} [{100*r.p_rg_lo:.1f}, {100*r.p_rg_hi:.1f}]",
                         "PPV/NPV %": f"{100*r.p_ppv_npv:.1f}", "RG (HT) %": f"{100*r.p_rg_HT:.1f}"})
    A(md_table(pd.DataFrame(rows)))
    A("")
    g = rg[rg.detector == "name_primary"].set_index("year")
    A(f"- **Corrected 2023 → 2026 rise (primary):** {100*g.p_rg[2023]:.1f}% → {100*g.p_rg[2026]:.1f}% "
      f"(+{100*(g.p_rg[2026]-g.p_rg[2023]):.1f} pp), against {100*g.p_obs[2023]:.1f}% → {100*g.p_obs[2026]:.1f}% observed "
      f"(+{100*(g.p_obs[2026]-g.p_obs[2023]):.1f} pp).")
    for nm in ["name_primary|lenient", "name_primary|strict"]:
        gg = rg[rg.detector == nm].set_index("year")
        A(f"  - Against the {nm.split('|')[1]} construct: {100*gg.p_rg[2023]:.1f}% → {100*gg.p_rg[2026]:.1f}% "
          f"(+{100*(gg.p_rg[2026]-gg.p_rg[2023]):.1f} pp).")
    A("")
    A("### D1 ITS with block-specific misclassification")
    A("- **Model:**")
    A("  - D1 specification: U 2017–26, `name_primary ~ tc + post + post×tc + log_authors + llm_topic + topic100 FE`, CRV1 by topic100.")
    A("  - Fitted by maximum likelihood with P(observed = 1 | x) = (1 − Sp_b) + (Se_b + Sp_b − 1)·expit(x′β), Se/Sp by year block.")
    A(f"  - Uncertainty: the corrected CI adds the between-draw variance from refitting on {its['corrected'].get('boot_draws','?')} "
      "stratified-bootstrap draws of (Se_b, Sp_b) to the sandwich variance.")
    A(f"- **Reproduction check:** the in-house uncorrected fit gives OR {its['uncorrected']['OR']:.4f}; the D1 file "
      f"(`its_results.json`) gives {v1['its']['d1_reference_slope_change_OR']:.4f}.")
    A("")
    rows = []
    for nm, r in v1["its"].items():
        if not isinstance(r, dict):
            continue
        rows.append({"outcome (construct)": nm, "Se/Sp draws": r["corrected"].get("boot_draws", 0),
                     "uncorrected OR [95% CI]":
                     f"{r['uncorrected']['OR']:.3f} [{r['uncorrected']['OR_lo']:.3f}, {r['uncorrected']['OR_hi']:.3f}]",
                     "corrected OR [95% CI]": f"{r['corrected']['OR']:.3f} [{r['corrected']['OR_lo']:.3f}, {r['corrected']['OR_hi']:.3f}]",
                     "OR ratio": f"{r['OR_ratio']:.3f}", "log-OR change": f"{100*r['logOR_rel_change']:+.1f}%",
                     "within 10% (OR)": "yes" if r["within_10pct_OR"] else "no",
                     "within 10% (log OR)": "yes" if r["within_10pct_logOR"] else "no"})
    A(md_table(pd.DataFrame(rows)))
    A("")
    htc = its.get("HT_check")
    if htc:
        A(f"- **Main-only (HT) Se/Sp check:** corrected OR {np.exp(htc['delta']):.3f} "
          f"(sandwich CI {np.exp(htc['delta']-1.96*htc['se']):.3f}–{np.exp(htc['delta']+1.96*htc['se']):.3f}).")
    lo_ = v1["its"].get("name_loose")
    if lo_:
        ov_ = lo_["corrected"]["OR_lo"] <= its["corrected"]["OR_hi"] and its["corrected"]["OR_lo"] <= lo_["corrected"]["OR_hi"]
        A(f"- **Cross-detector consistency:** the loose detector, corrected against the same NAME construct, gives "
          f"{lo_['corrected']['OR']:.3f} [{lo_['corrected']['OR_lo']:.3f}, {lo_['corrected']['OR_hi']:.3f}].")
        A(f"  - Uncorrected, loose gives {lo_['uncorrected']['OR']:.3f}.")
        A("  - If misclassification is non-differential within blocks, both detectors should recover the same latent slope change.")
        A(f"  - The two corrected CIs {'overlap' if ov_ else 'do not overlap'}.")
    if "boot_delta_pct" in its["corrected"]:
        A(f"- **Bootstrap draws:** {100*its['corrected']['share_draws_within10pct_OR']:.0f}% of corrected ORs lie within 10% of the uncorrected OR. "
          f"Draw quantiles of the corrected OR: {np.exp(its['corrected']['boot_delta_pct'][0]):.3f} / {np.exp(its['corrected']['boot_delta_pct'][1]):.3f} / "
          f"{np.exp(its['corrected']['boot_delta_pct'][2]):.3f}.")
    ag = v1["agg"]
    A(f"- **Aggregate cross-check:** WLS on the logit of 10 yearly shares gives a slope change of {ag['uncorrected_slope_change']:.3f} "
      f"(observed) and {ag['corrected_slope_change']:.3f} (RG-corrected); OR ratio {ag['OR_ratio']:.3f}.")
    A("- **Reading:**")
    A("  - The correction assumes misclassification is non-differential within a block (independent of topic, team size and "
      "llm_topic) and that the consensus is the truth.")
    A("  - The \"within 10%\" criterion is pre-registered on the OR scale. Because the OR is close to 1, the log-OR change is the "
      "more demanding comparison and is reported next to it.")
    A("")
    A("Figures: `fig_v1_name_detector_precision_recall.{pdf,png,csv}`, `fig_v1_name_share_corrected.{pdf,png,csv}`.")
    A("")

    # ------------------------------------------------------------------ V2
    A("## V2. Slot sense and swap preservation")
    k2 = v2["kappa"]
    A("- **Sample:** 400 slot-filled titles, 2018+, stratified by slot × variant × era × word.")
    A(f"- **Agreement:** slot_sense κ = {k2['slot_sense']['kappa']:.3f} [{k2['slot_sense']['lo']:.3f}, {k2['slot_sense']['hi']:.3f}] "
      f"({k2['slot_sense']['n_disagree']} disagreements); swap_preserves κ = {k2['swap_preserves']['kappa']:.3f} "
      f"[{k2['swap_preserves']['lo']:.3f}, {k2['swap_preserves']['hi']:.3f}] ({k2['swap_preserves']['n_disagree']} disagreements).")
    A("  - The swap test is the more subjective judgement, as expected.")
    A(f"  - {len(ADJ_V2)} items were adjudicated (`v2_adjudications.csv`). Rule: swap preserves meaning when the new title "
      "describes the same kind of contribution about the same object, ignoring tone. 'Unveiling X' fails when X is not hidden or "
      "when it implies discovering rather than analysing X.")
    A("")
    A("**Per word.** Columns:")
    A("- \"weighted\": design-weighted sense precision over eras (weights N/n); this is the drop rule, < 0.85.")
    A("- \"k/n [Wilson]\": unweighted sampled share with its Wilson 95% CI.")
    A("")
    w = v2["words"].copy()
    w["weighted"] = w.precision_w.map(lambda v: f"{v:.2f}")
    w["k/n [Wilson]"] = [f"{k}/{n} [{lo:.2f}, {hi:.2f}]" for k, n, lo, hi in zip(w.n_sense_y, w.n, w.wilson_lo, w.wilson_hi)]
    w["after pre-V2 filter"] = w.precision_after_prefilter_w.map(lambda v: "" if not np.isfinite(v) else f"{v:.2f}")
    w["swap preserves"] = w.swap_preserves_w.map(lambda v: f"{v:.2f}")
    w["pre / post"] = [f"{'' if not np.isfinite(a) else f'{a:.2f}'} (n={na_}) / {'' if not np.isfinite(b) else f'{b:.2f}'} (n={nb_})"
                       for a, na_, b, nb_ in zip(w.precision_pre, w.n_pre, w.precision_post, w.n_post)]
    w["DROP"] = [("**drop**" if d_ else ("borderline" if b_ else "")) for d_, b_ in zip(w["drop"], w["borderline"])]
    A(md_table(w[["slot", "variant", "word", "weighted", "k/n [Wilson]", "after pre-V2 filter", "pre / post",
                  "swap preserves", "N_population", "DROP"]]))
    A("")
    A("**Per slot side and era** (design-weighted):")
    A("")
    A(md_table(v2["slots"], "{:.2f}"))
    A("")
    A("**By opener rule of the sampled title:**")
    A("")
    A(md_table(v2["by_source"], "{:.2f}"))
    A("")
    bl = v2["payload"]["borderline_kept"]
    A("- **Notes:**")
    A("  - 'enabling' (exploit, neutral side) is never used in the exploit sense: it means making something possible.")
    A("  - 'unlocking' mostly means enabling a capability.")
    A("  - 'decoding' is mostly the technical operation, even after the pre-V2 filter.")
    if bl:
        A("  - **Borderline (kept):** unweighted or single-era precision is below 0.85. " + "; ".join(
            f"{x['slot']}/{x['word']}: weighted {x['precision_w']:.2f}, unweighted {x['precision_unw']:.2f}, "
            f"pre {x['precision_pre']:.2f} (n={x['n_pre']}), post {x['precision_post']:.2f} (n={x['n_post']})" for x in bl) + ".")
        A("    - In each case the sense failures sit in the pre era, on the LLM-favoured side. That inflates the pre-2024 "
          "LLM share and biases the slot break toward zero. D3 should run leave-one-variant-out on these words.")
    su = v2["payload"]["sensitivity_unweighted_rule"]["dropped_words"]
    A("  - **Unweighted-rule sensitivity:** the drop set would be " + "; ".join(f"{k}: {', '.join(v)}" for k, v in su.items() if v) + ".")
    sl = v2["slots"]
    rv = sl[(sl.slot == "reveal")]
    A(f"  - **Swap preservation:** the reveal slot is the weakest (LLM side {rv[rv.variant=='llm'].swap_w.mean():.2f}, neutral side "
      f"{rv[rv.variant=='neutral'].swap_w.mean():.2f}, weighted mean over eras). Swapping 'Unveiling' for 'Understanding' "
      "often changes the claim (discovering vs explaining), so reveal-slot shifts are partly shifts in what is claimed, not only in wording.")
    bs = v2["by_source"].set_index("source")
    A(f"  - **Opener rule:** titles that fill a slot only under the any-lead rule (`_al`) have lower sense precision "
      f"({bs.loc['al_only','sense']:.2f}, n={int(bs.loc['al_only','n'])}) than titles filled under the primary rule "
      f"({bs.loc['primary','sense']:.2f}, n={int(bs.loc['primary','n'])}). This supports the primary opener rule in D3.")
    A("")

    # ------------------------------------------------------------------ V3
    A("## V3. Fingerprints and register")
    A("### Convergent validity (weak; not ground truth)")
    A("- **Design:** one LLM rater, blind to the fingerprint words, rated 300 abstracts from 2024–26 (25 per year × fingerprint stratum) "
      "on a 1–5 scale of how likely the abstract is LLM-written or LLM-polished.")
    A("- **Circularity caveat:** the rubric does not name the RARE21 words, but an LLM rater is likely to know them. "
      "Part of the F24 correlation may therefore be mechanical.")
    A("")
    ct = v3["corr"].copy()
    ct["Spearman ρ [95% CI]"] = [f"{r:.2f} [{lo:.2f}, {hi:.2f}]" for r, lo, hi in zip(ct.spearman, ct.lo, ct.hi)]
    A(md_table(ct[["fingerprint", "Spearman ρ [95% CI]", "auc", "mean_rating_pos", "mean_rating_neg"]], "{:.2f}"))
    A("")
    A("Mean rating by year × fingerprint stratum:")
    A("")
    st = v3["strat"].pivot(index="year", columns="fstat", values="mean").reset_index()
    A(md_table(st, "{:.2f}"))
    A("")
    A(f"- **Within-year Spearman ρ (F vs rating):** "
      + ", ".join(f"{int(r.year)}: {r.spearman_F_any:.2f}" for r in v3["within"].itertuples()) + ".")
    A(f"  - Design-weighted Pearson r(F, rating) over 2024–26 = {v3['wcorr']:.2f}.")
    A(f"- **Ratings of unfingerprinted (F = 0) abstracts rise with year** (Spearman ρ = {v3['f0_trend']['rho']:.2f}, "
      f"p = {v3['f0_trend']['p']:.3f}).")
    A("  - This is consistent with undetected LLM use growing among unflagged papers (fingerprint recall decays), or with "
      "general register drift. Either way it supports the plan's position that recall is unknown and tool estimates are bounds.")
    A("")
    A("### Specificity: fingerprint rates in 2021–22 (pre-ChatGPT, so every hit is a false positive)")
    A("")
    fpt = v3["fpr"].copy()
    fpt["FPR % [95% CI]"] = [f"{100*f:.2f} [{100*lo:.2f}, {100*hi:.2f}]" for f, lo, hi in zip(fpt.fpr, fpt.fpr_lo, fpt.fpr_hi)]
    for c in ["rate_2024", "rate_2025", "rate_2026"]:
        fpt[c] = fpt[c].map(lambda v: f"{100*v:.2f}")
    fpt["excess share 2024–26"] = fpt.excess_share_2024_26.map(lambda v: "" if not np.isfinite(v) else f"{v:.2f}")
    A(md_table(fpt[["flag", "hits_2021_22", "FPR % [95% CI]", "rate_2024", "rate_2025", "rate_2026", "excess share 2024–26"]]))
    A("")
    A("- **Columns:**")
    A("  - rate_YYYY: share of U papers flagged in that year.")
    A("  - Excess share: 1 − FPR / (2024–26 rate), the share of 2024–26 hits above the pre-LLM baseline.")
    A(f"- **Most frequent RARE21 words in 2021–22 hits:** " + ", ".join(f"{k} ({v})" for k, v in v3["w24"].items()) + ".")
    A("")
    A("### Manual inspection of title typography hits")
    tc = v3["typo_counts"]
    A(f"- **Sample:** 50 of the {v3['n_nbh']} U+2011 titles and 50 of the {v3['n_en']} letter–en dash–letter titles without U+2011, "
      f"drawn at random. All {v3['n_title_hits']} hits are in `v3_typography_inspection.csv` as sampled.")
    A("")
    rows = [{"class": k, "n": tc.get(k, 0), "description": v} for k, v in TYPO_CLASS_DESC.items()]
    A(md_table(pd.DataFrame(rows)))
    A("")
    ts = v3["typo"]
    A(f"- **Result:** none of the 100 shows a LaTeX or PDF conversion artefact. There is no math, line-break hyphenation, "
      f"soft hyphen or ligature damage, and no hit sits inside a LaTeX span.")
    A(f"- **U+2011 hits:**")
    A(f"  - Every one is an ordinary hyphenated compound (Source‑Free, End‑to‑End). LaTeX and PDF text extraction do not "
      "produce U+2011 for a typed hyphen.")
    A(f"  - {int(ts[ts.title_nbhyphen].also_ascii_hyphen.sum())} of 50 also contain an ASCII hyphen elsewhere in the same "
      "title, which points to pasted fragments rather than a whole-title conversion.")
    A("  - U+2011 is absent from every title before 2026.")
    A("- **En-dash hits:**")
    A(f"  - {tc.get('en_eponym',0)} of 50 join personal names (Kolmogorov–Arnold). This is standard typography, typical of "
      "LaTeX `--` pasted from a PDF, and the kind of hit that also occurs before 2024. These are false positives for an LLM marker.")
    A(f"  - {tc.get('en_relation',0)} join parallel terms (Vision–Language). This is standard style, compatible with LaTeX, "
      "careful human typing or LLM output.")
    A(f"  - {tc.get('en_open_compound',0)} are Chicago-style open-compound modifiers and {tc.get('en_nonstandard',0)} are nonstandard.")
    A("- **No export-level conversion:** ASCII `--` between letters persists in 2026 titles and abstracts (table below), "
      "so the 2026 spike is not a blanket `--` → en dash conversion by the export.")
    A("")
    A(md_table(v3["dash_years"]))
    A("")
    A("Title hits before 2026 (all of them):")
    A("")
    A(md_table(v3["pre26"]))
    A("")
    A("- **Implication:** the en-dash part of the typography marker carries a non-LLM component (eponym pairs, standard relation dashes). "
      "The U+2011 part has no pre-2026 baseline at all.")
    A("")

    # ------------------------------------------------------------------ V4
    A("## V4. Name-masking leakage")
    A(f"- **R3 mask** (bge input; lead + CamelCase/ALLCAPS tokens → [NAME]):")
    A(f"  - The lead survives (case-insensitive, whole word) in **{r4['r3_survive']} of {r4['n_name_2018_26']:,}** NAME abstracts "
      f"from 2018–26 ({100*r4['r3_survive_share']:.2f}%). The features_v2 column gives {r4['r3_survive_features_v2']}.")
    A(f"  - Target 0%: **{'met' if r4['r3_survive']==0 else 'not met'}**.")
    A(f"- **R1 mask** (TF-IDF input; lead dropped, lowercase tokens kept): the lead survives in {r4['r1_survive']} "
      f"({100*r4['r1_survive_share']:.2f}%).")
    if len(v4["ex_r1"]):
        A("  - Examples: " + ", ".join(f"'{x}'" for x in v4['ex_r1'].lead_raw.head(8)) + ".")
        A("  - As D1 found, these are leads whose lowercase letter run survives in a URL or with a digit suffix (e.g. 'resgrad1' → 'resgrad').")
    A(f"- **Unchecked leads:** {r4['too_short_for_check']} leads have fewer than 2 alphanumeric characters (e.g. 'Q*') and "
      "cannot be checked by string match.")
    A(f"- **Stricter substring test** (lead core of ≥ 3 characters anywhere in the alphanumeric masked text, no word boundary): "
      f"{r4['r3_substring']} hits for R3 and {r4['r1_substring']} for R1.")
    sb = v4["sub"]
    for cat, g in sb.groupby("category"):
        ex = "; ".join(f"{l} → {t}" for l, t in zip(g.lead_raw.head(4), g.token.head(4)))
        A(f"  - {cat}: {len(g)} (e.g. {ex}).")
    A(f"  - **Leak (variant spellings).** The 'variant spelling' and 'URL' categories are real leaks: the name survives in a variant spelling the "
      f"whole-word lead pattern does not match. Such variants are LaTeX-wrapped (`$q$-neurons`), markdown-emphasised, "
      f"use a different Unicode hyphen, or sit inside a project URL.")
    A(f"    - R3: about {r4['r3_variant_or_url_leaks']} NAME abstracts ({100*r4['r3_variant_or_url_share']:.2f}%).")
    A(f"    - R1: about {r4['r1_variant_or_url_leaks']} ({100*r4['r1_variant_or_url_share']:.2f}%).")
    A("    - The counts are approximate in both directions. LaTeX-symbol spellings (`$\\pi$-light`, `$\\xi$-learning`) escape the "
      "string test, while a few hits mention a base name the lead builds on ('adam' for 'Adam$^+$').")
    A("    - The pre-registered whole-word test (0%) is therefore met, but the masks are not leak-free.")
    A("    - The leak is small, but D1 R3 should note it. Masking URLs and matching on a normalised form (LaTeX and markdown "
      "stripped, hyphens unified) would close most of it.")
    A("  - **Not leaks:** the 'lead letters' categories are ordinary words that share the lead's letters. The full list is `v4_r3_substring_hits.csv`.")
    A(f"- **Masked-vs-unmasked AUC gap** (from D1 `T1_2_representations.csv`): "
      + "; ".join(f"{k}: " + ", ".join(f"{d_} {v:+.3f}" for d_, v in vv.items()) for k, vv in r4["auc_gap"].items()) + ".")
    A(f"- **Name fragments among the top-200 R1 features:** {len(r4['top200_name_fragments'])}"
      + (" (" + ", ".join(sorted(set(x['token'] for x in r4['top200_name_fragments']))) + ")" if r4['top200_name_fragments'] else "") + ".")
    A("  - This is a token match against NAME lead strings. Matches are ordinary words that are also used as names, not leaked identifiers.")
    A(f"- **Not masked:** {r4['n_name_2017_not_masked']} NAME papers from 2017 are outside the masked set (R3 covers 2018–26).")
    A("")

    # ------------------------------------------------------------------ V5
    A("## V5. Topics")
    A("- **Labels:** one LLM pass labelled all 100 MiniLM topic100 clusters from their 12 most central papers. "
      "The table is `topic100_labels.csv`.")
    A(f"- **Annotator LM flag vs the regex LLM-cluster rule** (> 50% of the cluster's U papers match the LLM regex): "
      f"κ = {v5['kappa']['kappa']:.3f} [{v5['kappa']['lo']:.3f}, {v5['kappa']['hi']:.3f}], raw agreement {100*v5['kappa']['raw_agreement']:.0f}%.")
    A("")
    A(md_table(v5["conf"].reset_index().rename(columns={"llm_cluster": ""})))
    A("")
    dd = v5["dis"]
    A(f"- **All {len(dd)} disagreements go the same way:** the annotator says 'about LMs', the rule says no.")
    A("  - These clusters' all-years regex shares are "
      + ", ".join(f"{s_:.2f}" for s_ in dd.llm_regex_share) + ".")
    A("  - Their 2024–26 regex shares are " + ", ".join(f"{s_:.2f}" for s_ in dd.llm_regex_share_2024_26) + ".")
    A("  - The central papers shown skew recent, so the annotator sees the clusters' current, LLM-heavier composition. The two "
      "flags measure the same thing at different time windows.")
    A(f"- **Rank agreement:** Spearman ρ(regex share, annotator LM count) = {v5['spearman_share']['rho']:.2f}. "
      f"Paper by paper on the same 12 shown papers, ρ(regex hits, annotator count) = {v5['spearman_shown']['rho']:.2f}. "
      f"The regex count exceeds the annotator's count by {v5['paper_level']['mean_regex_minus_annot']:+.2f} papers per cluster on average.")
    A("- **Manual check of 10 clusters** (the 5 disagreements and 5 random agreements; `topic100_labels.csv`, manual_* columns):")
    mm = v5["out"][v5["out"].manual_label_verdict != ""]
    A("")
    A(md_table(mm[["topic100", "label", "about_lms", "lm_papers", "llm_regex_share", "manual_label_verdict",
                   "manual_lm_verdict", "manual_note"]], "{:.2f}"))
    A("")
    A(f"- **Topic stability, MiniLM vs bge (recomputed on U):**")
    A(f"  - k=100: ARI {v5['ari']['k100']['ari']:.3f}, NMI {v5['ari']['k100']['nmi']:.3f}.")
    A(f"  - k=50: ARI {v5['ari']['k50']['ari']:.3f}, NMI {v5['ari']['k50']['nmi']:.3f}.")
    A(f"  - Paper-level LLM flags: cluster flag κ = {v5['flag_k']['cluster_flag']:.3f}, union flag (llm_topic) κ = {v5['flag_k']['union_flag']:.3f}.")
    A("  - Partitions agree only moderately, but the LLM flag that enters the models is stable across encoders.")
    A("")

    # ------------------------------------------------------------------ V6
    A("## V6. Author keys")
    A("Keys are exact declared-ID keys (SHA-256 of the declared ID). They are declared profile keys, not people.")
    A("")
    dist = v6["dist"].copy()
    A(md_table(dist, "{:.2f}"))
    A("")
    ov = v6["over"]
    A(f"- **Key-years with more than 40 papers:** {len(ov)} in total, listed in `v6_keys_over40.csv` (key prefix only; "
      "profile IDs are not printed).")
    for kind, g in ov.groupby("native_id_kind"):
        A(f"  - {kind}: {len(g)} key-years, years {sorted(g.year.unique().tolist())}, papers per key-year {int(g.papers.min())}–{int(g.papers.max())}.")
    oth = ov[ov.native_id_kind != "profile"]
    if len(oth):
        A("  - Non-profile IDs among them (not people): " + ", ".join(sorted(set(oth.native_id_if_not_profile.astype(str)))) + ".")
    if len(ov):
        A(f"  - U papers touched by a flagged key-year, by year: {v6['papers_touched'].to_dict()}.")
    mx = v6["dist"].groupby("year")["max"].max()
    A(f"  - The largest exact key-year count is {int(mx.max())} papers ({int(mx.idxmax())}).")
    alv = v6["al"]
    A(f"  - After the alias collapse below, {int(alv.alias_over_40.sum())} alias-years exceed 40 "
      f"(max {int(alv.alias_max_papers.max())}). These are homonym merges, not plausible single authors.")
    A("")
    A("**Alias sensitivity** (profile IDs with trailing digits removed; this merges homonymous profiles and duplicate profiles "
      "of one person, so it over-links and is an upper bound on missed linkage):")
    A("")
    A(md_table(v6["al"], "{:.3f}"))
    A("")
    s6 = v6["al_summary"]
    e6 = v6["eff"]
    A(f"- **Merging:** over 2021–26, {s6['profile_keys_all']:,} profile keys collapse to {s6['aliases_all']:,} aliases.")
    A(f"  - {s6['aliases_merging_2plus_keys']:,} aliases merge two or more keys; they hold {100*s6['share_profile_rows_in_merged_aliases']:.1f}% of profile author rows.")
    A(f"- **Effect on 2022+ paper covariates** ({e6['n_papers']:,} papers):")
    A(f"  - r(log max_prior_subs) exact vs alias = {e6['corr_max_prior_subs']:.3f}; max_prior_subs changes for {100*e6['share_papers_maxprior_changed']:.1f}% of papers.")
    A(f"  - r(share_new_authors) = {e6['corr_share_new']:.3f}; share_new_authors changes for {100*e6['share_papers_share_new_changed']:.1f}% of papers, "
      f"with mean {e6['mean_share_new_exact']:.3f} → {e6['mean_share_new_alias']:.3f}.")
    A("")
    A("**Email-key vs profile-key eras** (positions by ID kind; mean paper-level new-key share from exact keys):")
    A("")
    A(md_table(v6["era"], "{:.3f}"))
    A("")
    A("- **2021 break:** ID kind switches from email to profile, so 2021 keys have no history. The new-key share jumps "
      "in 2021 and is not comparable across the switch, which is why the experience covariates are used from 2022 on (`exp_valid`).")
    A("")

    # ------------------------------------------------------------------ deviations
    A("## Deviations from PLAN.md section 3 and notes")
    devs = [
        "Annotation passes are LLM subagents (as planned). V3 and V5 have one pass each (as planned); V1 and V2 have two.",
        "V1 consensus error: the 150 spot checks were done by the adjudicator (PI's delegate), not an independent reviewer.",
        "V1 precision/recall use the main stratified sample with design weights; the 200 hard cases are reported "
        "separately (they overlap the main strata, so pooling would double-count).",
        "V1 ITS correction uses year-BLOCK-specific Se/Sp (2017-19, 2020-22, 2023, 2024, 2025, 2026), because the "
        "validation sample was stratified by block; the plan says 'year-specific'.",
        "V1 'within 10%' is evaluated on the OR scale as pre-registered; the log-OR change is reported alongside.",
        "V2 drop rule applied to the design-weighted sense precision of each slot word over the population sampled by "
        "WP3a (2018+, either opener rule, before the heuristic pre-V2 filter); post-filter precision is also reported.",
        "V3: 2021-22 used as the pre-ChatGPT specificity window (ICLR 2023 submissions closed in September 2022, before "
        "ChatGPT's release, so 2023 could also serve).",
        "V5 used 12 central papers per cluster (WP3a deviation); 'LLM topic' agreement compares the annotator's flag "
        "with the MiniLM >50% regex cluster rule (llm_cluster), not with llm_topic (which is paper-level).",
        "V6 key-year flags print key prefixes only; profile IDs are not printed.",
    ]
    for x in devs:
        A(f"- {x}")
    A("")
    A("## Files")
    for f in sorted(VAL.glob("*")):
        if f.is_file() and f.suffix in (".csv", ".json", ".md", ".png", ".pdf"):
            A(f"- `{f.name}`")
    return "\n".join(L) + "\n", {}


def main():
    VAL.mkdir(parents=True, exist_ok=True)
    feat_cols = ["name_primary", "name_strict", "name_loose", "name_compound", "name_orthography", "lead_n_tokens",
                 "f24", "f24_2", "f24_words", "f26_words",
                 "f26_words_list", "abs_nbhyphen", "abs_endash_compound", "f26_typo", "f26", "title_typo",
                 "title_nbhyphen", "title_endash_compound", "F_any", "lead_raw", "lead_survives_mask", "lead_in_abstract"]
    frame = C.load_analysis_frame(feature_cols=feat_cols,
                                  universe_cols=["submission_id", "year", "title", "topic100", "log_authors", "llm_topic"])
    for c in ["name_primary", "name_strict", "name_loose", "name_compound", "llm_topic"]:
        frame[c] = frame[c].astype(int)
    feat = frame.copy()
    for c in ["f24", "f24_2", "f26_words", "abs_nbhyphen", "abs_endash_compound", "f26_typo", "f26", "title_typo",
              "title_nbhyphen", "title_endash_compound", "F_any", "lead_survives_mask", "lead_in_abstract"]:
        feat[c] = feat[c].astype(bool)
    feat["name_primary"] = feat.name_primary.astype(bool)
    log("loaded frame")
    v1 = v1_analysis(frame)
    log("V1 done")
    v2 = v2_analysis()
    log("V2 done")
    v3 = v3_analysis(feat)
    log("V3 done")
    v4 = v4_analysis(feat)
    log("V4 done")
    v5 = v5_analysis()
    log("V5 done")
    v6 = v6_analysis()
    log("V6 done")
    figures(v1)
    report, _ = write_report(v1, v2, v3, v4, v5, v6)
    (VAL / "VALIDATION.md").write_text(report)
    # machine-readable summary
    bm = v1["binm"]
    out = dict(
        generated_by="analyses/validate_measures.py", seed=SEED,
        V1=dict(kappa=v1["kappa"], n_adjudicated_items=int(v1["m"].adjudicated.sum()),
                n_adjudicated_labels=int(len(v1["adj"])), adjudication_rule=ADJ_RULE_V1,
                spotcheck=v1["spot_summary"], detector_metrics=bm, rogan_gladen=v1["rg"],
                its_corrected=v1["its"], its_aggregate_check=v1["agg"], precision_drift=v1["drift"],
                orthography=v1["orth"], casing=v1["cas"], hard_cases=v1["hard"]),
        V2=dict(kappa=v2["kappa"], words=v2["words"], slots=v2["slots"], dropped=v2["payload"]["dropped_words"],
                borderline_kept=v2["payload"]["borderline_kept"]),
        V3=dict(correlations=v3["corr"], within_year=v3["within"], weighted_r=v3["wcorr"], f0_trend=v3["f0_trend"],
                fpr_2021_22=v3["fpr"], typography_inspection_counts=v3["typo_counts"],
                n_title_typo_hits=v3["n_title_hits"], latex_or_pdf_artefacts_found=0),
        V4=v4["res"],
        V5=dict(kappa_annotator_vs_regex_cluster=v5["kappa"], spearman_share=v5["spearman_share"],
                spearman_shown=v5["spearman_shown"], paper_level=v5["paper_level"], ari=v5["ari"],
                llm_flag_kappa_minilm_vs_bge=v5["flag_k"], n_disagreements=int(len(v5["dis"])),
                manual_checks={k: dict(label=v[0], about_lms=v[1], note=v[2]) for k, v in V5_CHECK.items()}),
        V6=dict(papers_per_key=v6["dist"], keys_over40=int(len(v6["over"])),
                keys_over40_by_kind=v6["over"].groupby("native_id_kind").size().to_dict(),
                alias=v6["al"], alias_summary=v6["al_summary"], alias_covariate_effect=v6["eff"]),
    )
    (VAL / "validation.json").write_text(json.dumps(jsonable(out), indent=1))
    log("wrote VALIDATION.md and validation.json")


if __name__ == "__main__":
    main()
