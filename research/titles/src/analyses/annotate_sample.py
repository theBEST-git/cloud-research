"""WP3a: stratified, blinded annotation samples and codebooks for measurement validation (PLAN.md §3).

    cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.annotate_sample

Builds, with a fixed seed (deterministic: re-running reproduces every file byte for byte):

- V1  1,200 titles stratified by year block (2017-19, 2020-22, 2023, 2024, 2025, 2026) x NAME detector output
      (positive by orthography all_caps / mixed_case / word / paren_acronym; negative split into phrase-colon
      compound and non-compound), plus 200 hard cases (two-token leads, LaTeX, dash compounds, genre leads).
- V2  400 slot-filled titles (2018+) stratified by slot x variant (LLM-favoured / neutral) x era (pre 2018-23 /
      post 2024-26), with an equal allocation across slot words inside each cell.
- V3  300 abstracts, 2024-26, stratified by year x fingerprint status (F0 / F24 only / F26-or-title-typography
      only / both).
- V5  the 100 MiniLM topic100 clusters (cache/topics.parquet), each with its 12 most central papers
      (title + first 300 characters of the abstract).

Outputs (outputs/validation/):
- batches/<task>_batchNN.jsonl   blinded items: an opaque item_id plus text only, globally shuffled per task.
- keys/<task>_key.csv            PRIVATE: item_id -> submission_id (or cluster), stratum, population and
                                 sample sizes, design weight, detector outputs. Annotators must not read keys/.
- codebooks/*.md                 V1 A/B, V2 A/B, V3 rubric, V5 instructions (exact JSONL output formats).
- labels/                        empty; annotators write <out_prefix>_pass<A|B>.jsonl here.
- sample_design.csv              stratum-level population and sample sizes (no item ids).
- annotate_manifest.json         seed, input/code/codebook hashes, batch list, label schemas, deviations.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

_SRC = Path(__file__).resolve().parents[1]
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

import features as F  # noqa: E402
from analyses import _core as C  # noqa: E402
from analyses.features_v2 import lexicon  # noqa: E402

SEED = 20261011
VAL = C.OUT / "validation"
BATCH_DIR = VAL / "batches"
KEY_DIR = VAL / "keys"
CODEBOOK_DIR = VAL / "codebooks"
LABEL_DIR = VAL / "labels"

N_V1_MAIN_PER_BLOCK = 200      # 100 NAME-positive + 100 NAME-negative per year block
N_V1_HARD_PER_TYPE = 50        # 4 hard-case types
N_V2 = 400
N_V3 = 300
N_V5_PAPERS = 12
SNIPPET_CHARS = 300
BATCH_SIZE = {"v1": 200, "v2": 200, "v3": 100, "v5": 50}
PASSES = {"v1": 2, "v2": 2, "v3": 1, "v5": 1}
ITEM_KEYS = {
    "v1": ["item_id", "title"],
    "v2": ["item_id", "title", "target_word", "target_occurrence", "sense", "swap_word"],
    "v3": ["item_id", "abstract"],
    "v5": ["item_id", "papers"],
}
BLOCKS = [("2017-19", (2017, 2018, 2019)), ("2020-22", (2020, 2021, 2022)), ("2023", (2023,)),
          ("2024", (2024,)), ("2025", (2025,)), ("2026", (2026,))]
ORTHO = ["all_caps", "mixed_case", "word", "paren_acronym"]
DICT_WORD_ZIPF = 3.5           # filler for genre-lead hard cases: single ordinary-English-word leads
# V2 substitution reference words: the first-listed word of each side in PLAN.md D3. An item whose target is an
# LLM-favoured word gets the neutral reference; an item whose target is a neutral word gets the LLM reference.
SWAP_REF = {"improve": {1: "improving", 0: "enhancing"},
            "reveal": {1: "understanding", 0: "unveiling"},
            "exploit": {1: "exploiting", 0: "leveraging"},
            "study_adj": {1: "systematic", 0: "comprehensive"}}
STUDY_NOUNS = r"(?:study|benchmark|evaluation|analysis|survey|investigation|review|assessment)"

DEVIATIONS = [
    "V5 shows the 12 most central papers per cluster (title + first 300 characters of the abstract), as the WP3a "
    "task specifies; PLAN.md §3 V5 says 20 central abstracts. Central = smallest squared Euclidean distance of the "
    "MiniLM abstract embedding to the cluster's label-mean centroid (outputs/topics/centroids.npz minilm_k100), over "
    "U papers of all years, skipping exact duplicate titles/abstracts (resubmissions).",
    "V1 hard cases, genre leads: U has only 22 compound titles whose lead is or contains a genre word "
    "(features_v2.lead_is_genre, which also fires on leads such as 'Orthogonal Drift Correction (ODC)'). All genre "
    "leads not already in the main sample are taken; the rest of the 50 are single-token leads that are ordinary "
    "English words (Title-case alphabetic, wordfreq zipf >= 3.5, e.g. 'Attention', 'Uncertainty', 'Echo'), the "
    "coined-name vs generic-word boundary.",
    "V1 main sample design: within each year block, 100 NAME-positive titles allocated as equally as possible "
    "across the four orthography classes (paren_acronym has only 1-22 titles per block, so all are taken and the "
    "remainder is redistributed), and 100 NAME-negative titles split 50 phrase-colon compound / 50 non-compound "
    "so that recall can be estimated where misses are plausible. Design weights N_h/n_h are in the key.",
    "V1 dash hard cases: 25 titles whose separator the detector found as a spaced dash, and 25 titles without a "
    "detected separator that contain an unspaced en/em dash or '--'/'---', or a dash with space on one side only "
    "(the v1 COLON regex misses e.g. ' --- ' and unspaced em dashes).",
    "V1/V2 items show the raw title (whitespace collapsed), not the NFKC title the detectors read, so annotators "
    "see what the authors typed (LaTeX kept).",
    "V1 codebook label set: lead_type adds 'none' for non-compound titles; casing has 4 classes, so the detector's "
    "'mixed' and 'other' both map to 'other'. Auxiliary fields 'lead' (verbatim) and 'note' support adjudication.",
    "V2 population: 2018+ (the D3 slot-model years), opener slots filled under EITHER opener rule: the primary "
    "opener after an optional NAME lead without the pre-V2 sense filter (slot_*_raw) or the opener after any "
    "compound lead (slot_*_al, API.md deviation 3). This covers both candidate primary definitions and the 8 "
    "sense-filtered titles. A title filling two slots is assigned by preferring the primary opener over the "
    "any-lead opener, then the order improve, reveal, exploit, study_adj. Within each slot x variant x era cell, items are allocated equally across slot words "
    "(capped at availability) so that per-word sense precision, the PLAN drop rule (< 0.85), is estimable.",
    "V2 swap test is symmetric: an LLM-favoured target gets the slot's reference neutral word (Improving / "
    "Understanding / Exploiting / systematic); a neutral target gets the reference LLM-favoured word (Enhancing / "
    "Unveiling / Leveraging / comprehensive). References are the first-listed words in PLAN.md D3. Annotators are "
    "not told which word of a pair is LLM-favoured.",
    "V3 strata: year (2024, 2025, 2026) x 4 fingerprint categories (F0; F24 only; F26 or title typography without "
    "F24; F24 and F26/typography), 25 per cell, finer than F0/F1 so that component-level convergence can be read. "
    "The rubric does not name the fingerprint words or typography, to avoid a mechanically induced correlation.",
    "V5 adds an auxiliary integer 'lm_papers' (how many of the 12 shown papers are centrally about language "
    "models) next to the required label and y/n flag, for comparison with the >50% regex-share cluster rule.",
]


# --------------------------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------------------------
def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def norm_key(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def alloc_equal(total: int, caps: dict) -> dict:
    """Water-filling: spread `total` units as equally as possible over strata, never above each cap.
    Ties go to the stratum with more spare capacity, then by name (deterministic)."""
    n = {k: 0 for k in caps}
    for _ in range(int(total)):
        open_ = [k for k in caps if n[k] < caps[k]]
        if not open_:
            break
        k = min(open_, key=lambda s: (n[s], -(caps[s] - n[s]), str(s)))
        n[k] += 1
    return n


class Drawer:
    """Seeded draws without replacement, unique by submission_id and by normalised text within one task."""

    def __init__(self, rng: np.random.Generator):
        self.rng = rng
        self.used_ids: set = set()
        self.used_keys: set = set()

    def available(self, cands: pd.DataFrame) -> pd.DataFrame:
        ok = ~cands.submission_id.isin(self.used_ids) & ~cands.nkey.isin(self.used_keys)
        return cands[ok].drop_duplicates("nkey")

    def draw(self, cands: pd.DataFrame, n: int) -> pd.DataFrame:
        c = cands.sort_values("submission_id", kind="mergesort").reset_index(drop=True)
        take = []
        for i in self.rng.permutation(len(c)):
            if len(take) >= n:
                break
            sid, key = c.submission_id.iat[i], c.nkey.iat[i]
            if sid in self.used_ids or key in self.used_keys:
                continue
            take.append(i)
            self.used_ids.add(sid)
            self.used_keys.add(key)
        return c.iloc[take].copy()

    def draw_alloc(self, strata: dict, total: int) -> tuple[pd.DataFrame, dict]:
        """Equal (water-filled) allocation of `total` over strata {name: candidates}; redistributes shortfalls."""
        out, got = [], {k: 0 for k in strata}
        remaining = total
        while remaining > 0:
            caps = {k: len(self.available(v)) for k, v in strata.items()}
            if sum(caps.values()) == 0:
                break
            a = alloc_equal(remaining, caps)
            drawn_now = 0
            for k in strata:  # fixed order -> deterministic
                if a[k] == 0:
                    continue
                d = self.draw(strata[k], a[k])
                d["stratum"] = k
                out.append(d)
                got[k] += len(d)
                drawn_now += len(d)
            remaining -= drawn_now
            if drawn_now == 0:
                break
        df = pd.concat(out, ignore_index=True) if out else pd.DataFrame()
        return df, got


def lead_end(title: str) -> int | None:
    """Character offset where the remainder starts after the first separator (features.COLON, math protected)."""
    t = title or ""
    prot = F.MATH.sub(lambda m: "M" * len(m.group(0)), t)
    m = F.COLON.search(prot)
    if not m or m.start() == 0 or not t[: m.start()].strip():
        return None
    return m.end()


def word_occurrences(title: str, word: str) -> list[re.Match]:
    return list(re.finditer(r"(?<![A-Za-z])" + re.escape(word) + r"(?![A-Za-z])", title, re.IGNORECASE))


def match_case(template: str, word: str) -> str:
    if len(template) > 1 and template.isupper():
        return word.upper()
    if template[:1].isupper():
        return word[:1].upper() + word[1:]
    return word.lower()


# --------------------------------------------------------------------------------------------
# V1: NAME / compound / orthography / casing
# --------------------------------------------------------------------------------------------
def sample_v1(df: pd.DataFrame, rng: np.random.Generator):
    from wordfreq import zipf_frequency
    d = df.copy()
    d["text"] = d.title.map(clean)
    d["nkey"] = d.text.map(norm_key)
    d["block"] = ""
    for b, ys in BLOCKS:
        d.loc[d.year.isin(ys), "block"] = b
    d["era"] = np.where(d.year >= 2024, "post", "pre")
    dr = Drawer(rng)
    parts, design = [], []

    # main: block x detector output
    for b, _ in BLOCKS:
        db = d[d.block.eq(b)]
        pos = {f"pos_{o}": db[db.name_primary & db.name_orthography.eq(o)] for o in ORTHO}
        neg = {"neg_phrase_colon": db[~db.name_primary & db.compound],
               "neg_noncompound": db[~db.compound]}
        for strata, tot in [(pos, N_V1_MAIN_PER_BLOCK // 2), (neg, N_V1_MAIN_PER_BLOCK // 2)]:
            s, got = dr.draw_alloc(strata, tot)
            s["component"] = "main"
            s["stratum"] = b + "|" + s.stratum
            parts.append(s)
            for k, v in strata.items():
                design.append(dict(task="v1", component="main", stratum=f"{b}|{k}", N_pop=len(v), n_sample=got[k]))

    # hard cases (drawn after the main sample, excluding its titles)
    d["sep"] = [(m.group(0).strip() if (m := F.COLON.search(F.strip_math(t).strip())) and m.start() > 0 else "")
                for t in d.title_nfkc]
    is_dash_sep = d.compound & C.rx_contains(d.sep, r"[-\u2013\u2014]")
    undet_dash = ~d.compound & C.rx_contains(
        d.title, r"\S(?:[\u2013\u2014]|-{2,})\S|\w\s[-\u2013\u2014]+\S|\S[-\u2013\u2014]+\s\w|\s-{3,}\s")
    latex = d.title.str.contains("$", regex=False) | d.title.str.contains("\\", regex=False)
    two = d.compound & d.lead_n_tokens.eq(2)
    single_alpha = d.compound & d.lead_n_tokens.eq(1) & C.rx_contains(d.lead_segment, r"^[A-Z][a-z]+$")
    zipf = pd.Series(0.0, index=d.index)
    zipf[single_alpha] = [zipf_frequency(w.lower(), "en") for w in d.lead_segment[single_alpha]]
    dict_word = single_alpha & zipf.ge(DICT_WORD_ZIPF) & ~d.lead_is_genre
    genre = d.compound & d.lead_is_genre

    hard_specs = [
        ("two_token_lead", {f"{'name' if nm else 'nonname'}_{e}": d[two & d.name_primary.eq(nm) & d.era.eq(e)]
                            for nm in (True, False) for e in ("pre", "post")}),
        ("latex", {f"latex_{e}": d[latex & d.era.eq(e)] for e in ("pre", "post")}),
        ("dash", {"dash_detected": d[is_dash_sep], "dash_undetected": d[undet_dash]}),
    ]
    for htype, strata in hard_specs:
        s, got = dr.draw_alloc(strata, N_V1_HARD_PER_TYPE)
        s["component"] = "hard"
        s["stratum"] = "hard|" + htype + "|" + s.stratum
        parts.append(s)
        for k, v in strata.items():
            design.append(dict(task="v1", component="hard", stratum=f"hard|{htype}|{k}", N_pop=len(v),
                               n_sample=got[k]))
    g = dr.draw(d[genre], N_V1_HARD_PER_TYPE)
    g["stratum"] = "hard|genre_lead|genre_word_lead"
    w = dr.draw(d[dict_word], N_V1_HARD_PER_TYPE - len(g))
    w["stratum"] = "hard|genre_lead|dict_word_lead"
    for s, k, pool in [(g, "genre_word_lead", d[genre]), (w, "dict_word_lead", d[dict_word])]:
        s["component"] = "hard"
        parts.append(s)
        design.append(dict(task="v1", component="hard", stratum=f"hard|genre_lead|{k}", N_pop=len(pool),
                           n_sample=len(s)))

    items = pd.concat(parts, ignore_index=True)
    des = pd.DataFrame(design)
    items = items.merge(des[["stratum", "N_pop", "n_sample"]].rename(columns={"N_pop": "N_stratum",
                                                                             "n_sample": "n_stratum"}),
                        on="stratum", how="left")
    items["weight"] = items.N_stratum / items.n_stratum
    items["payload"] = [{"title": t} for t in items.text]
    keep = ["submission_id", "year", "block", "component", "stratum", "N_stratum", "n_stratum", "weight",
            "name_primary", "name_strict", "name_loose", "compound", "name_orthography", "casing", "question",
            "lead_segment", "lead_raw", "lead_n_tokens", "lead_is_genre", "has_math", "payload"]
    return items[keep], des


# --------------------------------------------------------------------------------------------
# V2: slot senses and substitutability
# --------------------------------------------------------------------------------------------
def _v2_target(title: str, word: str, slot: str, pos: str) -> tuple[str, int]:
    """Locate the slot word as written in the displayed title; returns (target_word, occurrence 1-based)."""
    occ = word_occurrences(title, word)
    if not occ:
        raise ValueError(f"slot word {word!r} not found in {title!r}")
    if slot == "study_adj":
        m = re.search(r"(?<![A-Za-z])(" + re.escape(word) + r")\s+" + STUDY_NOUNS, title, re.IGNORECASE)
        start = m.start(1) if m else occ[0].start()
    elif pos == "after_lead":
        e = lead_end(title)
        start = next((o.start() for o in occ if e is not None and o.start() >= e), occ[0].start())
    else:
        start = occ[0].start()
    k = next(i for i, o in enumerate(occ) if o.start() == start)
    return occ[k].group(0), k + 1


def sample_v2(df: pd.DataFrame, rng: np.random.Generator):
    lx = lexicon()["slots"]
    w2 = {}
    for k, v in lx.items():
        for w_ in v["llm"]:
            w2[w_] = (k, 1)
        for w_ in v["neutral"]:
            w2[w_] = (k, 0)
    d = df[df.year >= 2018].copy()
    d["text"] = d.title.map(clean)
    d["nkey"] = d.text.map(norm_key)
    d["era"] = np.where(d.year >= 2024, "post", "pre")
    rows = []
    for r in d.itertuples(index=False):
        rec = None
        for k in ("improve", "reveal", "exploit"):  # primary opener (after optional NAME lead), no sense filter
            raw = getattr(r, f"slot_{k}_raw")
            if raw == raw:
                rec = (k, int(raw), r.opener_word, "primary",
                       "after_lead" if r.opener_pos == "post_name" else "start")
                break
        if rec is None:
            for k in ("improve", "reveal", "exploit"):  # opener after any compound lead
                al = getattr(r, f"slot_{k}_al")
                if al == al:
                    rec = (k, int(al), r.opener_word_al, "al_only", "after_lead" if r.compound else "start")
                    break
        if rec is None and r.slot_study_adj == r.slot_study_adj:
            rec = ("study_adj", int(r.slot_study_adj), r.slot_study_adj_word, "study_adj", "anywhere")
        if rec is None:
            continue
        slot, var, word, source, pos = rec
        assert w2[word] == (slot, var), (word, slot, var)
        target, occ = _v2_target(r.text, word, slot, pos)
        swap = match_case(target, SWAP_REF[slot][var])
        rows.append(dict(submission_id=r.submission_id, year=r.year, era=r.era, nkey=r.nkey, text=r.text,
                         slot=slot, variant=var, word=word, source=source, opener_rule_pos=pos,
                         target_word=target, target_occurrence=occ, swap_word=swap,
                         slot_sense_flag=r.slot_sense_flag, slot_word_in_abstract=r.slot_word_in_abstract))
    cand = pd.DataFrame(rows)
    cand["cell"] = cand.slot + "|" + np.where(cand.variant.eq(1), "llm", "neutral") + "|" + cand.era
    dr = Drawer(rng)
    cells = sorted(cand.cell.unique(), key=lambda c: (list(SWAP_REF).index(c.split("|")[0]), c))
    word_strata = {c: {f"{c}|{w_}": cand[cand.cell.eq(c) & cand.word.eq(w_)]
                       for w_ in sorted(cand[cand.cell.eq(c)].word.unique())} for c in cells}
    parts, got_all = [], {}
    remaining = N_V2
    while remaining > 0:  # cells water-filled to N_V2; words water-filled inside each cell; shortfalls re-spread
        caps = {c: len(dr.available(cand[cand.cell.eq(c)])) for c in cells}
        if sum(caps.values()) == 0:
            break
        a = alloc_equal(remaining, caps)
        drawn = 0
        for c in cells:
            if a[c] == 0:
                continue
            s, got = dr.draw_alloc(word_strata[c], a[c])
            parts.append(s)
            drawn += len(s)
            for k, v in got.items():
                got_all[k] = got_all.get(k, 0) + v
        remaining -= drawn
        if drawn == 0:
            break
    design = [dict(task="v2", component="main", stratum=k, N_pop=len(v), n_sample=got_all.get(k, 0))
              for c in cells for k, v in word_strata[c].items()]
    items = pd.concat(parts, ignore_index=True)
    des = pd.DataFrame(design)
    items = items.merge(des[["stratum", "N_pop", "n_sample"]].rename(columns={"N_pop": "N_stratum",
                                                                             "n_sample": "n_stratum"}),
                        on="stratum", how="left")
    items["weight"] = items.N_stratum / items.n_stratum
    items["component"] = "main"
    items["payload"] = [dict(title=t, target_word=tw, target_occurrence=int(o), sense=s_, swap_word=sw)
                        for t, tw, o, s_, sw in zip(items.text, items.target_word, items.target_occurrence,
                                                    items.slot, items.swap_word)]
    keep = ["submission_id", "year", "era", "component", "stratum", "N_stratum", "n_stratum", "weight", "slot",
            "variant", "word", "source", "opener_rule_pos", "target_word", "target_occurrence", "swap_word",
            "slot_sense_flag", "slot_word_in_abstract", "payload"]
    return items[keep], des


# --------------------------------------------------------------------------------------------
# V3: LLM-polish ratings of abstracts by fingerprint status
# --------------------------------------------------------------------------------------------
def f_status(d: pd.DataFrame) -> pd.Series:
    other = d.f26 | d.title_typo
    return pd.Series(np.select([~d.F_any, d.f24 & ~other, ~d.f24 & other],
                               ["F0", "F24_only", "F26typo_only"], "F24_and_F26typo"), index=d.index)


def sample_v3(df: pd.DataFrame, rng: np.random.Generator):
    d = df[df.year.isin(C.POST)].copy()
    d["text"] = d.abstract.map(clean)
    d["nkey"] = d.text.map(norm_key)
    d["fstat"] = f_status(d)
    dr = Drawer(rng)
    strata = {f"{y}|{f}": d[d.year.eq(y) & d.fstat.eq(f)]
              for y in C.POST for f in ["F0", "F24_only", "F26typo_only", "F24_and_F26typo"]}
    items, got = dr.draw_alloc(strata, N_V3)
    des = pd.DataFrame([dict(task="v3", component="main", stratum=k, N_pop=len(v), n_sample=got[k])
                        for k, v in strata.items()])
    items = items.merge(des[["stratum", "N_pop", "n_sample"]].rename(columns={"N_pop": "N_stratum",
                                                                             "n_sample": "n_stratum"}),
                        on="stratum", how="left")
    items["weight"] = items.N_stratum / items.n_stratum
    items["component"] = "main"
    items["payload"] = [{"abstract": t} for t in items.text]
    keep = ["submission_id", "year", "component", "stratum", "N_stratum", "n_stratum", "weight", "fstat", "F_any",
            "f24", "f24_n", "f26", "f26_words", "f26_typo", "title_typo", "payload"]
    return items[keep], des


# --------------------------------------------------------------------------------------------
# V5: topic100 cluster labels
# --------------------------------------------------------------------------------------------
def sample_v5(u: pd.DataFrame):
    tp = pd.read_parquet(C.CACHE / "topics.parquet")
    d = u.merge(tp[["submission_id", "topic100"]].rename(columns={"topic100": "topic100_cache"}),
                on="submission_id", how="left", validate="1:1")
    assert d.topic100_cache.notna().all() and (d.topic100_cache == d.topic100).all()
    E = C.load_embedding(d, "abstract", "all-MiniLM-L6-v2")
    cent = C.load_centroids("minilm_k100")
    lab = d.topic100_cache.astype(int).to_numpy()
    d["dist"] = ((E - cent[lab]) ** 2).sum(1)
    d = d.sort_values(["topic100_cache", "dist", "submission_id"], kind="mergesort")
    d["rank_all"] = d.groupby("topic100_cache").cumcount() + 1
    # sanity: the undeduplicated top-20 equal WP2's central_papers_k100.csv (minilm_k100)
    ref = pd.read_csv(C.TOPIC_DIR / "central_papers_k100.csv")
    ref = ref[ref.model.eq("minilm_k100")]
    mine = d[d.rank_all.le(20)][["submission_id", "topic100_cache", "rank_all"]]
    chk = ref.merge(mine, left_on=["submission_id", "cluster"], right_on=["submission_id", "topic100_cache"])
    agree_top20 = float((chk["rank"] == chk.rank_all).mean() * len(chk) / len(ref))
    d["t_clean"] = d.title.map(clean)
    d["a_clean"] = d.abstract.map(clean)
    d["tkey"] = d.t_clean.map(norm_key)
    d["akey"] = d.a_clean.str[:SNIPPET_CHARS].map(norm_key)
    clusters = []
    for k, g in d.groupby("topic100_cache", sort=True):
        g = g.drop_duplicates("tkey").drop_duplicates("akey").head(N_V5_PAPERS)
        papers = []
        for t, a in zip(g.t_clean, g.a_clean):
            snip = a[:SNIPPET_CHARS] + ("…" if len(a) > SNIPPET_CHARS else "")
            papers.append({"title": t, "abstract_snippet": snip})
        sub = d[d.topic100_cache.eq(k)]
        clusters.append(dict(cluster=int(k), n_cluster=len(sub), llm_regex_share=round(float(sub.llm_regex.mean()), 4),
                             llm_cluster=bool(sub.llm_cluster.iloc[0]),
                             paper_ids="|".join(g.submission_id), paper_ranks="|".join(map(str, g.rank_all)),
                             papers=papers))
    items = pd.DataFrame(clusters)
    assert len(items) == 100 and items.papers.map(len).eq(N_V5_PAPERS).all()
    items["component"] = "main"
    items["stratum"] = "cluster"
    items["payload"] = [{"papers": p} for p in items.papers]
    des = pd.DataFrame([dict(task="v5", component="main", stratum="all_clusters", N_pop=100, n_sample=100)])
    return items.drop(columns=["papers"]), des, agree_top20


# --------------------------------------------------------------------------------------------
# Blinding, shuffling, batching
# --------------------------------------------------------------------------------------------
def finalize(task: str, items: pd.DataFrame, rng: np.random.Generator, used_ids: set) -> tuple[pd.DataFrame, list]:
    n = len(items)
    ids = []
    while len(ids) < n:
        tok = f"{task}_{int(rng.integers(0, 16 ** 8)):08x}"
        if tok not in used_ids:
            used_ids.add(tok)
            ids.append(tok)
    items = items.copy()
    items["item_id"] = ids
    items = items.iloc[rng.permutation(n)].reset_index(drop=True)
    bs = BATCH_SIZE[task]
    items["batch"] = [f"{task}_batch{i // bs + 1:02d}" for i in range(n)]
    items["batch_pos"] = [i % bs + 1 for i in range(n)]
    batches = []
    for b, g in items.groupby("batch", sort=True):
        path = BATCH_DIR / f"{b}.jsonl"
        with path.open("w", encoding="utf-8") as fh:
            for iid, pl in zip(g.item_id, g.payload):
                rec = {"item_id": iid, **pl}
                assert list(rec) == ITEM_KEYS[task], (task, list(rec))
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        batches.append(dict(task=task.upper(), batch=b, batch_path=str(path), n_items=len(g)))
    key = items.drop(columns=["payload"])
    key.insert(0, "task", task.upper())
    front = ["item_id", "task", "batch", "batch_pos"]
    key = key[front + [c for c in key.columns if c not in front]]
    key.to_csv(KEY_DIR / f"{task}_key.csv", index=False)
    return key, batches


# --------------------------------------------------------------------------------------------
# Codebooks
# --------------------------------------------------------------------------------------------
V1_FORMAT = """\
Write a JSONL file (UTF-8): exactly one JSON object per input item, one object per line, in the same order as
the input file, with no other lines, headers or commentary. Every object has exactly these eight keys, in this
order, and every value is a string:

{"item_id": "<copied unchanged from the input>", "compound": "y|n", "lead": "<lead copied verbatim, or empty>", "lead_type": "coined_name|descriptive_phrase|genre_label|none", "lead_orthography": "all_caps|mixed_case|word|paren_acronym|na", "casing": "title_case|sentence_case|all_caps|other", "question": "y|n", "note": "<optional comment of at most 20 words, otherwise empty>"}

Constraints that every line must satisfy:
- compound = "n"  =>  lead = "", lead_type = "none", lead_orthography = "na".
- compound = "y"  =>  lead is non-empty and lead_type is coined_name, descriptive_phrase or genre_label.
- lead_type != "coined_name"  =>  lead_orthography = "na".
"""

V1_CODEBOOK_A = """\
# V1 title-form annotation: Codebook A (version 1.0)

## Task
You receive one batch file in JSONL format. Each line is an item of the form
`{"item_id": "...", "title": "..."}`. The title belongs to a machine-learning research paper and is shown
exactly as its authors typed it; LaTeX math such as `$\\ell_1$` may appear. For every item you record six
labels that describe the form of the title.

Judge only the title in front of you. Do not search for the paper, do not open any other file, and do not try
to infer anything about the paper beyond what its title says. Label every item; never skip one. When unsure,
choose the best-fitting label and explain briefly in `note`.

## Labels

### 1. `compound` (y / n)
A title is compound when a separator splits it into an opening part (the lead) and a remainder (the subtitle).
Separators are:
- a colon, `:` or fullwidth `：` ("Lead: Remainder");
- a dash used as a break between two parts of the title. This is normally a hyphen, en dash, em dash or a run
  of hyphens with spaces on both sides ("Lead - Remainder", "Lead — Remainder", "Lead -- Remainder"). An en or em
  dash, or a run of hyphens, without spaces also counts when it clearly breaks the title into lead and remainder
  ("Lead—Remainder").

Not separators:
- hyphens or dashes inside a word or a compound term ("Pre-training", "Kolmogorov–Arnold Networks",
  "Vision–Language Models", "state-of-the-art", "High- and Low-Resource");
- colons inside numbers, ratios or mathematics ("1:1", "2:4 sparsity", `$f: X \\to Y$`);
- question marks, exclamation marks, full stops, semicolons, commas, brackets and quotation marks.

If there are several separators, the lead is the text before the first one. A title that begins with a
separator is not compound.

### 2. `lead` (verbatim text)
If compound = y, copy the lead exactly as written: every character before the first separator, without the
separator and without surrounding spaces. If compound = n, write an empty string.

### 3. `lead_type`
- `coined_name`: the lead is a name, i.e. a label that identifies one particular artefact (a model, method,
  algorithm, architecture, system, agent, dataset, benchmark, library or framework) and works like a proper noun
  or a brand. It is usually invented by the authors, but names of existing artefacts also count. A name can be
  an ordinary English word used as a name ("Heron"), can carry a version number or size ("KoalaLM 2"), and can
  be a descriptive phrase followed by its acronym in parentheses ("Contrastive Patch Alignment (CPA)").
- `descriptive_phrase`: the lead tells what the paper is about in ordinary words: a topic, task, setting,
  method description, claim, slogan or question ("Rethinking Warmup", "Graph Neural Networks", "Less Is More",
  "When Do Transformers Fail?"). Generic abbreviations that name a whole field or family of methods (RL, GNNs,
  LLMs, NLP, AI) are descriptive, not names. A phrase that merely uses a name as a modifier ("BERT-based
  Ranking", "LoRA Fine-Tuning at Scale") is descriptive.
- `genre_label`: the lead only says what kind of paper this is, not its subject: "Position", "Survey",
  "A Survey", "Review", "Tutorial", "Perspective", "Opinion", "Case Study", "Technical Report", "Erratum",
  "Note". If the lead also states the subject ("A Survey of Graph Neural Networks"), it is a descriptive_phrase.
- `none`: the title is not compound.

### 4. `lead_orthography` (only when lead_type = coined_name, otherwise "na")
Classify the written shape of the name. Apply the first rule that fits:
1. `paren_acronym`: the lead is a phrase ending in an acronym in parentheses: "Contrastive Patch Alignment (CPA)".
2. `all_caps`: every letter of the name is a capital letter (at least two letters; digits, hyphens and spaces
   are ignored): "PRISM", "GPT-4", "SAM 2", "U-NET".
3. `mixed_case`: not all capitals, and the name has a capital letter after its first character, or contains a
   digit, or contains LaTeX math: "KoalaLM 2", "LoRA", "word2vec", "AlphaFold", "Llama 2", "GPT-4o".
4. `word`: everything else, i.e. written like an ordinary word, with at most its first letter capitalised and no
   digits: "Heron", "Prometheus", "Diffuser".

### 5. `casing` (the whole title)
Consider the content words of the whole title (nouns, verbs, adjectives, adverbs). Ignore the very first word
of the title, short function words (a, an, the, of, for, in, on, at, by, with, to, and, or, via, from, as, is,
are, ...), and tokens that are always capitalised (acronyms, coined names, proper nouns and adjectives such as
"Bayesian" or "Markov").
- `title_case`: almost all of these words (about three quarters or more) start with a capital letter:
  "Learning Sparse Features From Noisy Labels".
- `sentence_case`: almost none of them (about a quarter or fewer) start with a capital letter:
  "Learning sparse features from noisy labels". A capital letter right after the separator does not change
  this. Titles written entirely in lower case also count as sentence_case.
- `all_caps`: the whole title is written in capital letters: "LEARNING SPARSE FEATURES FROM NOISY LABELS".
- `other`: the capitalisation is inconsistent (roughly between a quarter and three quarters of these words
  capitalised), or there are fewer than two such words to judge.

### 6. `question` (y / n)
`y` if the title, or any part of it, is a direct question, which normally carries a question mark
("Can Small Models Plan?", "PRISM: Do Sparse Models Share Features?"). Indirect question phrases without a
question mark ("How Transformers Learn Syntax", "What Makes Pretraining Work") are `n`.

## Worked examples (invented titles, not from your batch)
- "PRISM: Probing Representations in Sparse Models": compound y, lead "PRISM", coined_name, all_caps,
  title_case, question n.
- "KoalaLM 2: Efficient Pretraining at Small Scale": compound y, lead "KoalaLM 2", coined_name, mixed_case,
  title_case, question n.
- "Heron: a lightweight planner for household robots": compound y, lead "Heron", coined_name, word,
  sentence_case, question n.
- "Contrastive Patch Alignment (CPA): Learning Dense Features without Labels": compound y, coined_name,
  paren_acronym, title_case, question n.
- "Rethinking Warmup: Why Learning-Rate Schedules Matter": compound y, descriptive_phrase, na, title_case,
  question n.
- "Survey: Graph Learning under Distribution Shift": compound y, genre_label, na, title_case, question n.
- "Can Small Models Plan?": compound n, lead "", none, na, title_case, question y.
- "Learning 2:4 Sparse Masks for Fast Inference": compound n (ratio colon), none, na, title_case, question n.

## Output format (exact)
""" + V1_FORMAT + """
Example output lines (for the invented examples above; your item_ids come from the batch file):
{"item_id": "example-1", "compound": "y", "lead": "PRISM", "lead_type": "coined_name", "lead_orthography": "all_caps", "casing": "title_case", "question": "n", "note": ""}
{"item_id": "example-2", "compound": "y", "lead": "Rethinking Warmup", "lead_type": "descriptive_phrase", "lead_orthography": "na", "casing": "title_case", "question": "n", "note": ""}
{"item_id": "example-3", "compound": "n", "lead": "", "lead_type": "none", "lead_orthography": "na", "casing": "title_case", "question": "y", "note": ""}
"""

V1_CODEBOOK_B = """\
# V1 title-form annotation: Codebook B (version 1.0)

## What you are doing
You are coding the surface form of research-paper titles from machine learning. The batch file has one JSON
object per line, `{"item_id": "...", "title": "..."}`, with the title exactly as submitted (it may contain
LaTeX between dollar signs). Answer the six questions below for every title, in order. Base every answer on
the title string alone: no web searches, no other files, no guesses about the paper's year, venue or fate.
Code every line. If a case is borderline, pick the closest answer and say why in `note`.

## Q1. Is the title split in two? → `compound`
Look for a separator that divides the title into an opening part (call it the lead) and a remainder.
Only two kinds of mark count:
- a colon (ASCII `:` or the fullwidth `：`);
- a dash acting as a break between two parts: a hyphen, en dash, em dash or several hyphens, typically with a
  space on each side ("Otter — Streaming Speech Recognition"). An unspaced en/em dash or run of hyphens counts
  only if it plainly acts as that break ("Otter—Streaming Speech Recognition").
These do not count: hyphens and dashes that join words or names ("Self-Supervised", "Navier–Stokes",
"Image–Text Retrieval", "Pre- and Post-Training"); colons in ratios, clock times or formulas ("N:M",
`$g:\\mathbb{R}\\to\\mathbb{R}$`); and every other punctuation mark (?, !, ., ;, commas, brackets, quotes).
Several separators: only the first matters. A separator as the very first character: answer "n".
Answer "y" or "n".

## Q2. What exactly is the lead? → `lead`
When Q1 = "y", copy the characters that precede the first separator, character for character, trimmed of
spaces and without the separator. When Q1 = "n", leave it empty ("").

## Q3. What kind of lead is it? → `lead_type`
Work through these checks in order and stop at the first "yes":
(a) Q1 = "n"? → `none`.
(b) Does the lead do nothing but announce the type of paper (for example "Position", "Overview", "Primer",
    "Short Paper", "Lessons Learned", "Survey", "Erratum")? → `genre_label`. A type word plus subject matter
    ("Review of Diffusion Samplers") is not a genre label.
(c) Is the lead the name of one specific thing (a particular model, method, algorithm, architecture, dataset,
    benchmark, environment, toolkit or system) used the way a proper noun is used? Examples of the shape:
    "MAPLE-3D", "fastSeg", "Otter", "ViT-Giga", "Gated Linear Attention (GLA)". → `coined_name`. It does not
    matter whether the name is new or already known, whether it is a dictionary word ("Otter"), or whether it
    carries a version or size tag. A label for a whole field or family (DL, LMs, LLMs, RL, CV, GNN) is not the
    name of one specific thing. Nor is a phrase in which a name is just one modifier ("CLIP-Guided Editing",
    "Transformer Variants for Speech").
(d) Otherwise the lead describes, in ordinary language, a topic, approach, finding, claim or question
    ("Scaling Laws for Routing", "Sparse Attention Revisited", "Beyond Accuracy") → `descriptive_phrase`.

## Q4. How is the name written? → `lead_orthography`
Only when Q3 = `coined_name`; otherwise write "na". Take the first description that matches:
- `paren_acronym`: a phrase that ends with an acronym in brackets, e.g. "Gated Linear Attention (GLA)".
- `all_caps`: all letters in the name are upper case (two or more letters; ignore digits, spaces and
  punctuation), e.g. "MAPLE-3D", "DQN", "VQ-VAE".
- `mixed_case`: a letter after the first one is upper case, or the name includes a digit or a math expression,
  e.g. "fastSeg", "ViT-Giga", "MuZero", "T5", "Phi-3".
- `word`: plain word shape, where only the initial letter may be a capital and there are no digits, e.g.
  "Otter", "Hyena", "Mamba".

## Q5. Which capitalisation pattern does the whole title follow? → `casing`
Set aside the first word, the small function words (articles, prepositions, conjunctions, forms of "be": a,
the, of, for, on, in, with, and, or, to, via, by, from, is, are, ...), and any word that would be capitalised
anyway (acronyms, names, adjectives formed from names such as "Gaussian"). Among the words left:
- most of them (≈ 75% or more) begin with a capital → `title_case`;
- few of them (≈ 25% or less) begin with a capital → `sentence_case` (an all-lower-case title also goes here; a
  capital right after the separator is allowed);
- the entire title is in capitals → `all_caps`;
- anything in between, or fewer than two words left to judge → `other`.

## Q6. Is it a question? → `question`
"y" when the title contains a direct question, usually closed by "?" ("Are Sparse Experts Lazy?",
"Sparse Attention Revisited: When Does Locality Help?"). Clauses that start with how/why/what but are not
asked as questions and have no "?" ("Why Warmup Works") → "n".

## Examples (made up for this codebook)
- "MAPLE-3D: Multi-View Alignment for Point-Cloud Learning" → y, "MAPLE-3D", coined_name, all_caps, title_case, n
- "fastSeg: real-time segmentation on microcontrollers" → y, "fastSeg", coined_name, mixed_case, sentence_case, n
- "Otter — Streaming Speech Recognition with Bounded Memory" → y, "Otter", coined_name, word, title_case, n
- "Position: Benchmarks Should Report Variance" → y, "Position", genre_label, na, title_case, n
- "Sparse Attention Revisited: When Does Locality Help?" → y, "Sparse Attention Revisited", descriptive_phrase,
  na, title_case, y
- "LLMs: A Field Guide to Their Failure Modes" → y, "LLMs", descriptive_phrase, na, title_case, n
- "Navier–Stokes Surrogates with Spectral Operators" → n, "", none, na, title_case, n

## Output format (exact)
""" + V1_FORMAT + """
Example output lines (made-up items):
{"item_id": "example-1", "compound": "y", "lead": "fastSeg", "lead_type": "coined_name", "lead_orthography": "mixed_case", "casing": "sentence_case", "question": "n", "note": ""}
{"item_id": "example-2", "compound": "y", "lead": "Position", "lead_type": "genre_label", "lead_orthography": "na", "casing": "title_case", "question": "n", "note": ""}
{"item_id": "example-3", "compound": "n", "lead": "", "lead_type": "none", "lead_orthography": "na", "casing": "title_case", "question": "n", "note": "en dash joins two names"}
"""

V2_FORMAT = """\
Write a JSONL file (UTF-8): exactly one JSON object per input item, one per line, in the input order, with no
other lines or commentary. Every object has exactly these four keys, in this order, and string values:

{"item_id": "<copied unchanged from the input>", "slot_sense": "y|n", "swap_preserves": "y|n", "note": "<optional comment of at most 20 words, otherwise empty>"}

Answer both questions for every item, even when slot_sense is "n".
"""

V2_CODEBOOK_A = """\
# V2 title-word annotation: Codebook A (version 1.0)

## Task
Each line of the batch file is one item:
`{"item_id": "...", "title": "...", "target_word": "...", "target_occurrence": 1, "sense": "...", "swap_word": "..."}`

- `title`: a machine-learning paper title, as written by its authors.
- `target_word`: the word under study, exactly as it appears in the title. `target_occurrence` says which
  occurrence of that word is meant, counting whole-word matches from the start of the title and ignoring case
  (almost always 1).
- `sense`: the meaning to test (one of improve, reveal, exploit, study_adj; defined below).
- `swap_word`: an alternative word for the substitution test in question (b).

Use only the title. Do not look up the paper and do not open any other file. Label every item.

## (a) `slot_sense`: is the target word used in the given sense? (y / n)
Answer "y" if, in this title, the target word carries the meaning below; "n" if it carries another meaning
(for example it is part of a technical term, names a specific algorithm or operation, or is used literally).

- `improve`: the word says that the paper makes something better: it raises the performance, quality,
  robustness, efficiency, capability or reach of a model, method, system or person ("Improving sample
  efficiency of ...", "Enhancing robustness of ...", "Boosting reasoning in small models", "Empowering robots
  with ...", "Advancing molecular generation with ..."). Not this sense: the word is the name of a technique
  (e.g. boosting as the ensemble-learning method that the paper is about) or has a literal physical or temporal
  meaning.
- `reveal`: the word presents the paper as bringing something to light or making it understood, i.e. analysing,
  investigating, exposing or explaining how or why something works, behaves or fails ("Understanding the
  generalization of ...", "Uncovering hidden biases in ...", "Demystifying contrastive learning",
  "Characterizing the loss landscape of ..."); methods whose purpose is to explain a model's behaviour also
  count. Not this sense: the word names a technical operation, such as generating text from a model (decoding
  algorithms) or reading out signals or stimuli from recordings, or is a noun naming a task ("Language
  Understanding with ...").
- `exploit`: the word says that the paper makes use of, draws on, takes advantage of or puts to work something
  (a resource, model, signal, structure or property), including releasing its untapped potential, in order to
  achieve a goal ("Leveraging unlabeled data for ...", "Exploiting sparsity in ...", "Harnessing pretrained
  diffusion models for ...", "Utilizing auxiliary tasks to ...", "Unlocking the potential of ... for ...").
  Not this sense: the word mainly means something else, such as making something possible, or is used
  literally.
- `study_adj`: the adjective describes the scope, breadth or thoroughness of the study, benchmark, evaluation,
  analysis, survey, review or assessment that the paper itself presents ("A Comprehensive Study of ...",
  "A Systematic Evaluation of ...", "An Extensive Analysis of ...", "A Large-Scale Benchmark for ...").
  Not this sense: the adjective belongs to another term or describes something other than the paper's own
  study.

## (b) `swap_preserves`: does the substitution keep the meaning? (y / n)
Replace the indicated occurrence of the target word with `swap_word` (already in matching capitalisation),
leaving every other word unchanged. Would a researcher in the field read the new title as saying essentially
the same thing about what the paper does? Ignore differences in tone, emphasis, excitement or style:
"Unveiling" may sound more dramatic than "Understanding", but if both titles say the paper explains the same
thing, answer "y". Answer "n" if the new title says the paper does something different, becomes ungrammatical
or nonsensical, or breaks a technical term.

## Examples (invented)
- title "Enhancing Robustness of Vision Transformers via Patch Dropout", target "Enhancing", sense improve,
  swap "Improving" → slot_sense y, swap_preserves y.
- title "Boosting with Soft Margins: A Statistical View", target "Boosting", sense improve, swap "Improving" →
  slot_sense n (the ensemble method), swap_preserves n.
- title "Decoding Strategies for Faithful Summarization", target "Decoding", sense reveal, swap
  "Understanding" → slot_sense n (text generation), swap_preserves n.
- title "Understanding Overfitting in Adversarial Training", target "Understanding", sense reveal, swap
  "Unveiling" → slot_sense y, swap_preserves y.
- title "A Systematic Study of Data Augmentation for Speech", target "Systematic", sense study_adj, swap
  "Comprehensive" → slot_sense y, swap_preserves y.

## Output format (exact)
""" + V2_FORMAT + """
Example output line:
{"item_id": "example-1", "slot_sense": "y", "swap_preserves": "y", "note": ""}
"""

V2_CODEBOOK_B = """\
# V2 title-word annotation: Codebook B (version 1.0)

## Overview
You will make two yes/no judgements about one word in each research-paper title. Every input line looks like
`{"item_id": "...", "title": "...", "target_word": "...", "target_occurrence": 1, "sense": "...", "swap_word": "..."}`.
The word to judge is `target_word`; if it occurs more than once, `target_occurrence` tells you which one
(1 = first occurrence, case ignored). `sense` names the meaning you must check and `swap_word` is the
replacement for the second judgement. Rely on the title text only (no searching, no other files), and give
both judgements for every line.

## Judgement 1, `slot_sense`: does the word mean what `sense` says?
"y" when the word, as used in this title, has the meaning described for its `sense`; "n" otherwise.

- improve: "to make better or stronger". The paper raises how well, how robustly, how efficiently or how
  widely something (a model, algorithm, system, agent or user) performs. Typical: "Improving Calibration under
  Shift", "Elevating Small-Model Reasoning", "Advancing Protein Design with Equivariant Priors", "Empowering
  Agents with Memory". Answer "n" when the word is the proper name of a learning technique the paper studies
  (the boosting family of ensemble methods, for instance) or is meant physically or in time.
- reveal: "to bring to light or to make understood". The paper sets out to find out, analyse, expose or
  explain why or how something happens, including producing explanations of a model's behaviour. Typical:
  "Analyzing Attention Sinks", "Unraveling the Dynamics of Grokking", "Investigating Label Noise in Medical
  Imaging", "Explaining Classifier Decisions with Counterfactuals". Answer "n" when the word is a technical
  operation, as in generating output tokens from a sequence model or decoding signals from neural or other
  recordings, or when it is a noun naming a task ("Scene Understanding Benchmarks ...").
- exploit: "to make use of". The paper draws on, takes advantage of, or puts to work something it already has
  (data, a pretrained model, a structural property, a signal), including tapping its latent potential. Typical:
  "Harnessing Weak Labels for Segmentation", "Utilizing Symmetry for Sample-Efficient Control", "Unleashing
  Pretrained Encoders for Retrieval". Answer "n" when the word chiefly means something other than using, for
  example making something possible, or is meant literally.
- study_adj: an adjective that rates how broad or thorough the paper's own study, benchmark, evaluation,
  analysis, survey, review or assessment is. Typical: "An Extensive Evaluation of Optimizers", "A Comprehensive
  Benchmark for Tabular Learning". Answer "n" when the adjective is part of some other term or qualifies
  something other than the paper's own study.

## Judgement 2, `swap_preserves`: does `swap_word` say the same thing?
Mentally rewrite the title with the indicated occurrence of the target word replaced by `swap_word`
(capitalisation already matched) and nothing else changed. "y" if the rewritten title makes essentially the
same claim about what the paper contributes; differences of flavour, register or hype do not matter
("Harnessing" vs "Exploiting" can both mean "making use of"). "n" if the contribution described changes, the
title stops making sense or becomes ungrammatical, or a fixed technical term is broken.

## Examples (made up)
- "Leveraging Synthetic Captions for Zero-Shot Retrieval", target "Leveraging", sense exploit, swap
  "Exploiting" → slot_sense y, swap_preserves y.
- "Exploiting Label Hierarchies for Few-Shot Classification", target "Exploiting", sense exploit, swap
  "Leveraging" → slot_sense y, swap_preserves y.
- "Decoding Visual Stimuli from fMRI with Diffusion Priors", target "Decoding", sense reveal, swap
  "Understanding" → slot_sense n (reading out signals), swap_preserves n.
- "Advancing Fronts in Level-Set Segmentation", target "Advancing", sense improve, swap "Improving" →
  slot_sense n (literal motion), swap_preserves n.

## Output format (exact)
""" + V2_FORMAT + """
Example output line:
{"item_id": "example-1", "slot_sense": "n", "swap_preserves": "n", "note": "technical term: neural decoding"}
"""

V3_RUBRIC = """\
# V3 abstract style rating: rubric (version 1.0, one pass)

## Task
Each line of the batch file is `{"item_id": "...", "abstract": "..."}`: the abstract of a machine-learning
research paper. For each abstract, rate from 1 to 5 how likely it is that the text was written or substantially
polished by a large language model (LLM) such as a chat assistant. Judge the prose only; do not search for the
paper, do not open any other file, and do not try to guess the paper's year or venue. Rate every item.

## Scale
- 1: almost certainly human-written, with no LLM polishing.
- 2: probably human-written.
- 3: cannot tell; signals are absent or point both ways.
- 4: probably LLM-written or LLM-polished.
- 5: almost certainly LLM-written or heavily LLM-polished.

## How to judge
Machine-learning abstracts are formulaic by tradition ("We propose X, a novel method that ... Experiments on
... show ..."). That template alone is not evidence of LLM use. Weigh the prose as a whole and do not let the
presence of any single word or punctuation mark decide the rating.

Cues that tend to raise the rating (several together matter more than any one):
- an elevated, promotional or ornate register out of step with the technical content; stacked evaluative
  adjectives and adverbs;
- generic framing sentences that could open almost any paper, and broad closing claims of impact or of
  "paving the way" with little that is specific to this work;
- uniformly smooth, evenly paced sentences of similar length and shape; neat parallel lists (often of three);
  paired constructions such as "not only ... but also";
- high-level summaries that restate the contribution several times in different words instead of adding
  concrete detail.

Cues that tend to lower the rating:
- idiosyncratic or non-native phrasing, small grammatical slips, typos or awkward but natural constructions;
- terse, dense technical writing with specific details (numbers, named datasets, precise mechanisms);
- uneven rhythm, informal asides, field jargon used naturally and economically.

## Output format (exact)
Write a JSONL file (UTF-8): exactly one JSON object per input item, one per line, in the input order, with no
other lines or commentary. Every object has exactly these three keys, in this order:

{"item_id": "<copied unchanged from the input>", "rating": <integer 1-5>, "cues": "<the main cues behind the rating, at most 15 words>"}

Example output line:
{"item_id": "example-1", "rating": 2, "cues": "terse technical detail, specific numbers, slightly awkward phrasing"}
"""

V5_INSTRUCTIONS = """\
# V5 topic-cluster labelling: instructions (version 1.0, one pass)

## Task
Papers from a machine-learning venue were grouped automatically into 100 clusters by the similarity of their
abstracts. Each line of the batch file describes one cluster:
`{"item_id": "...", "papers": [{"title": "...", "abstract_snippet": "..."}, ... 12 entries ...]}`.
The 12 papers are the most typical members of the cluster (closest to its centre), most typical first; each
`abstract_snippet` is the first 300 characters of that paper's abstract ("…" marks the cut). Use only what is
shown: no searching, no other files.

For each cluster give:
1. `label`: a short, specific, human-readable name for the shared research topic, at most 6 words
   (e.g. "Offline reinforcement learning", "Graph neural network expressivity", "Diffusion models for image
   editing"). Name the topic itself; do not write "Papers about ..." or list several unrelated topics. If the
   cluster is mixed, name what most of the shown papers share.
2. `about_lms`: "y" if the cluster is about language models, i.e. more than half of the 12 shown papers are
   centrally about building, training, evaluating, analysing, aligning, prompting or applying neural language
   models (large language models, BERT-style encoders, earlier neural language models, multimodal or
   vision-language models that read or generate text, and agents built on language models); "n" otherwise.
   A paper that mentions a language model only in passing, or uses one as a minor component, does not count.
3. `lm_papers`: the number of the 12 shown papers (an integer from 0 to 12) that are centrally about language
   models in the sense of point 2.

## Output format (exact)
Write a JSONL file (UTF-8): exactly one JSON object per cluster, one per line, in the input order, with no other
lines or commentary. Every object has exactly these four keys, in this order:

{"item_id": "<copied unchanged from the input>", "label": "<at most 6 words>", "about_lms": "y|n", "lm_papers": <integer 0-12>}

Consistency: about_lms = "y" exactly when lm_papers >= 7.

Example output line:
{"item_id": "example-1", "label": "Instruction tuning of language models", "about_lms": "y", "lm_papers": 11}
"""

CODEBOOKS = {
    "v1_codebook_A.md": V1_CODEBOOK_A,
    "v1_codebook_B.md": V1_CODEBOOK_B,
    "v2_codebook_A.md": V2_CODEBOOK_A,
    "v2_codebook_B.md": V2_CODEBOOK_B,
    "v3_rubric.md": V3_RUBRIC,
    "v5_instructions.md": V5_INSTRUCTIONS,
}

LABEL_SCHEMAS = {
    "V1": {"keys": ["item_id", "compound", "lead", "lead_type", "lead_orthography", "casing", "question", "note"],
           "values": {"compound": ["y", "n"], "lead_type": ["coined_name", "descriptive_phrase", "genre_label", "none"],
                      "lead_orthography": ["all_caps", "mixed_case", "word", "paren_acronym", "na"],
                      "casing": ["title_case", "sentence_case", "all_caps", "other"], "question": ["y", "n"]}},
    "V2": {"keys": ["item_id", "slot_sense", "swap_preserves", "note"],
           "values": {"slot_sense": ["y", "n"], "swap_preserves": ["y", "n"]}},
    "V3": {"keys": ["item_id", "rating", "cues"], "values": {"rating": [1, 2, 3, 4, 5]}},
    "V5": {"keys": ["item_id", "label", "about_lms", "lm_papers"],
           "values": {"about_lms": ["y", "n"], "lm_papers": list(range(13))}},
}


def write_codebooks() -> dict:
    out = {}
    for name, text in CODEBOOKS.items():
        p = CODEBOOK_DIR / name
        p.write_text(text, encoding="utf-8")
        out[name] = dict(path=str(p), sha256=sha256_file(p))
    return out


# --------------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------------
def main():
    for p in (BATCH_DIR, KEY_DIR, CODEBOOK_DIR, LABEL_DIR):
        p.mkdir(parents=True, exist_ok=True)
    for old in list(BATCH_DIR.glob("*.jsonl")):  # stale batches from an earlier run
        old.unlink()
    ss = np.random.SeedSequence(SEED)
    r_v1, r_v2, r_v3, r_fin = [np.random.default_rng(s) for s in ss.spawn(4)]

    fcols = ["name_primary", "name_strict", "name_loose", "compound", "name_orthography", "casing", "question",
             "lead_segment", "lead_raw", "lead_n_tokens", "lead_is_genre", "has_math",
             "slot_improve_raw", "slot_reveal_raw", "slot_exploit_raw", "slot_improve_al", "slot_reveal_al",
             "slot_exploit_al", "slot_study_adj", "slot_study_adj_word", "opener_word", "opener_pos",
             "opener_word_al", "slot_sense_flag", "slot_word_in_abstract",
             "F_any", "f24", "f24_n", "f26", "f26_words", "f26_typo", "title_typo"]
    ucols = ["submission_id", "year", "emb_row", "title", "title_nfkc", "abstract", "topic100", "llm_regex",
             "llm_cluster"]
    df = C.load_analysis_frame(feature_cols=fcols, universe_cols=ucols)
    df = df.sort_values("submission_id", kind="mergesort").reset_index(drop=True)
    print(f"analysis frame {df.shape}", flush=True)

    v1, d1 = sample_v1(df, r_v1)
    v2, d2 = sample_v2(df, r_v2)
    v3, d3 = sample_v3(df, r_v3)
    v5, d5, agree = sample_v5(df.sort_values(["year", "submission_id"]).reset_index(drop=True))
    assert len(v1) == 1400 and len(v2) == N_V2 and len(v3) == N_V3 and len(v5) == 100, \
        (len(v1), len(v2), len(v3), len(v5))
    assert v1.submission_id.is_unique and v2.submission_id.is_unique and v3.submission_id.is_unique

    used_ids: set = set()
    batches, keys = [], {}
    for task, items in [("v1", v1), ("v2", v2), ("v3", v3), ("v5", v5)]:
        key, b = finalize(task, items, r_fin, used_ids)
        keys[task] = key
        batches += b
    (KEY_DIR / "README_PRIVATE.txt").write_text(
        "PRIVATE. These key files map opaque item_ids to submission_ids, strata, design weights and detector "
        "outputs. Annotators (and annotation agents) must not read this folder.\n", encoding="utf-8")

    design = pd.concat([d1, d2, d3, d5], ignore_index=True)
    design.to_csv(VAL / "sample_design.csv", index=False)
    cb = write_codebooks()
    cbA = {"V1": cb["v1_codebook_A.md"]["path"], "V2": cb["v2_codebook_A.md"]["path"],
           "V3": cb["v3_rubric.md"]["path"], "V5": cb["v5_instructions.md"]["path"]}
    cbB = {"V1": cb["v1_codebook_B.md"]["path"], "V2": cb["v2_codebook_B.md"]["path"]}
    batch_list = []
    for b in batches:
        t = b["task"]
        rec = dict(task=t, batch_path=b["batch_path"], n_items=b["n_items"], codebook_A=cbA[t],
                   passes=PASSES[t.lower()], out_prefix=str(LABEL_DIR / b["batch"]))
        if t in cbB:
            rec["codebook_B"] = cbB[t]
        batch_list.append(rec)

    inputs = {str(p): sha256_file(p) for p in (C.UNIVERSE_PATH, C.FEATURES_PATH, C.CACHE / "topics.parquet",
                                               C.CENTROIDS_PATH, C.FEAT_DIR / "lexicon_hash.txt")}
    manifest = dict(
        script=str(Path(__file__)), script_sha256=sha256_file(Path(__file__)), seed=SEED,
        inputs_sha256=inputs, counts={t.upper(): int(len(k)) for t, k in keys.items()},
        batch_files={b["batch"]: sha256_file(Path(b["batch_path"])) for b in batches},
        codebooks=cb, label_file_convention="<out_prefix>_passA.jsonl (codebook_A) and <out_prefix>_passB.jsonl "
        "(codebook_B); single-pass tasks write <out_prefix>_passA.jsonl",
        label_schemas=LABEL_SCHEMAS, batches=batch_list, v5_top20_rank_agreement_with_wp2=agree,
        blinding="batch items contain only item_id and text fields (V1 title; V2 title, target word, occurrence, "
                 "sense, swap word; V3 abstract; V5 12 central titles + 300-char abstract snippets); item order "
                 "and batch membership are random; keys/ is private",
        deviations=DEVIATIONS)
    (VAL / "annotate_manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")

    # console summary
    print("\nV1 strata (main):")
    m = keys["v1"][keys["v1"].component.eq("main")]
    print(pd.crosstab(m.block, m.stratum.str.split("|").str[1]).to_string())
    h = keys["v1"][keys["v1"].component.eq("hard")]
    print("\nV1 hard:", h.stratum.value_counts().sort_index().to_dict())
    print("\nV2 cells:")
    k2 = keys["v2"]
    print(pd.crosstab([k2.slot, k2.variant], k2.era).to_string())
    print("V2 words:", k2.word.value_counts().to_dict())
    print("V2 source:", k2.source.value_counts().to_dict(), "| target_occurrence>1:",
          int((k2.target_occurrence > 1).sum()))
    print("\nV3:", keys["v3"].stratum.value_counts().sort_index().to_dict())
    print("\nV5 clusters:", len(keys["v5"]), "| WP2 top-20 rank agreement:", round(agree, 4))
    print("\nbatches:")
    for b in batch_list:
        print(" ", b["task"], Path(b["batch_path"]).name, b["n_items"], "passes", b["passes"])
    return batch_list


if __name__ == "__main__":
    main()
