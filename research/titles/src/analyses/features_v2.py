"""WP1 features v2: extends features.py (imported, never edited) with NAME variants, orthography and casing
dummies, LLM title slots and control pairs, register families R24/R26, abstract fingerprints F24/F26,
typography, LLM-mention abbreviation features, the frozen D2 style-marker set, and name-masking of abstracts.

All word lists live in analyses/lexicons.json (frozen; SHA-256 in outputs/features/lexicon_hash.txt).

    cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.features_v2

writes outputs/features/features_v2.parquet (one row per universe paper, keyed by submission_id).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

_SRC = Path(__file__).resolve().parents[1]
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

import features as F  # noqa: E402

LEXICON_PATH = Path(__file__).with_name("lexicons.json")
FEATURES_PY = _SRC / "features.py"


@lru_cache(maxsize=1)
def lexicon() -> dict:
    return json.loads(LEXICON_PATH.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


GENRE = set(lexicon()["genre_leads"]) | set(F.GENERIC_LEADS)
SENTINEL = ""  # private-use placeholder while masking (cannot match [A-Za-z0-9])
_TOKEN = re.compile(r"(?<![A-Za-z0-9])[A-Za-z0-9]+(?:[-'‐‑][A-Za-z0-9]+)*")
_PIECE_SPLIT = re.compile(r"[-'‐‑]")
_LOWER_UPPER = re.compile(r"[a-z][A-Z]")
_WORD = re.compile(r"[A-Za-z]+(?:-[A-Za-z]+)*")
GERUND_STOP = {"string", "strings", "thing", "things", "nothing", "something", "everything", "anything", "king",
               "spring", "during", "bring", "sing", "ring", "wing", "sling", "swing", "ping", "ming", "ling",
               "ceiling", "evening", "morning", "sibling", "siblings"}


# --------------------------------------------------------------------------------------------
# Name masking (D1 R1/R3; V4)
# --------------------------------------------------------------------------------------------
def _core_word(tok: str) -> str:
    return re.sub(r"[^A-Za-z]", "", tok).lower()


def lead_patterns(lead: str | None) -> list[re.Pattern]:
    """Case-insensitive regexes for a title lead (math-tolerant, hyphen-optional, optional 's / s)."""
    if not lead:
        return []
    lead = lead.strip().strip("\"'`“”‘’")
    pieces = [lead]
    m = F.PAREN_ACRONYM.search(lead)
    if m:
        pieces += [m.group(1), lead[: m.start()].strip()]
    pats = []
    for p in pieces:
        if len(re.sub(r"[^A-Za-z0-9]", "", p)) < 2:
            continue
        parts = []
        for tok in p.split():
            e = re.escape(tok)
            e = e.replace("MATH", r"(?:MATH|\$[^$]*\$)")
            e = e.replace(r"\-", r"[\s\-‐‑]?")
            parts.append(e)
        rx = r"(?<![A-Za-z0-9])" + r"[\s\-‐‑]+".join(parts) + r"(?:'?s)?(?![A-Za-z0-9])"
        pats.append(re.compile(rx, re.IGNORECASE))
    return pats


def _namey(tok: str, min_len: int) -> bool:
    for p in _PIECE_SPLIT.split(tok):
        if len(p) >= min_len and (sum(c.isupper() for c in p) >= 2 or _LOWER_UPPER.search(p)):
            return True
    return False


def mask_abstract(abstract: str, lead: str | None, token: str | None = None, min_len: int | None = None,
                  return_counts: bool = False):
    """R3 name mask: replace the title lead string and every CamelCase/ALLCAPS token (piece >= 3 chars)
    by `token` ('[NAME]'). With return_counts=True returns (masked, n_lead_hits, n_token_hits)."""
    cfg = lexicon()["name_mask"]
    token = cfg["token"] if token is None else token
    min_len = cfg["min_len"] if min_len is None else min_len
    s = abstract or ""
    n_lead = 0
    for rx in lead_patterns(lead):
        s, k = rx.subn(SENTINEL, s)
        n_lead += k
    n_tok = 0

    def rep(m):
        nonlocal n_tok
        if _namey(m.group(0), min_len):
            n_tok += 1
            return SENTINEL
        return m.group(0)

    s = _TOKEN.sub(rep, s).replace(SENTINEL, token)
    return (s, n_lead, n_tok) if return_counts else s


def mask_abstract_lower(abstract: str, lead: str | None) -> str:
    """R1 name mask (pilot rule, stricter lead removal): drop the title lead string (case-insensitive) and keep
    only originally all-lowercase word tokens [A-Za-z][A-Za-z-]+ (drops coined names, acronyms, capitals)."""
    s = abstract or ""
    for rx in lead_patterns(lead):
        s = rx.sub(" ", s)
    return " ".join(t for t in re.findall(r"[A-Za-z][A-Za-z\-]+", s) if t == t.lower())


def raw_lead(title: str) -> str | None:
    """The compound lead exactly as written (LaTeX kept), located like features.lead_segment."""
    t = (title or "").strip()
    prot = F.MATH.sub(lambda m: "M" * len(m.group(0)), t)  # same length, so positions map back
    m = F.COLON.search(prot)
    if not m or m.start() == 0:
        return None
    return t[: m.start()].strip()


def lead_survives(masked: str, lead_raw: str | None) -> bool:
    """V4 check: does the raw lead string (LaTeX kept, case-insensitive, whole word) occur in the masked text?"""
    if not lead_raw:
        return False
    core = lead_raw.strip().strip("\"'`\u201c\u201d\u2018\u2019").lower()
    if len(re.sub(r"[^a-z0-9]", "", core)) < 2:
        return False
    return re.search(r"(?<![a-z0-9])" + re.escape(core) + r"(?![a-z0-9])", (masked or "").lower()) is not None


# --------------------------------------------------------------------------------------------
# Title-level helpers
# --------------------------------------------------------------------------------------------
def name_variants(lead: str | None, name_colon: bool) -> dict:
    if lead is None:
        return dict(name_strict=False, name_loose=False, lead_n_tokens=0, lead_is_genre=False)
    toks = lead.strip().strip("\"'`").split()
    cores = [_core_word(t) for t in toks]
    is_genre = lead.strip().lower() in GENRE or any(c in GENRE for c in cores)
    strict = bool(name_colon) and len(toks) == 1 and not is_genre
    loose = (1 <= len(toks) <= 2 and cores[0] not in F.FUNCTION_WORDS and not is_genre
             and not all(c in F.FUNCTION_WORDS for c in cores))
    return dict(name_strict=strict, name_loose=loose, lead_n_tokens=len(toks), lead_is_genre=is_genre)


def first_word(text: str) -> str:
    w = _WORD.findall(F.strip_math(text or ""))
    return w[0].lower() if w else ""


def opener(title_nfkc: str, lead: str | None, rest: str, name_colon: bool) -> tuple[str, str, str]:
    """(opener after optional NAME lead, position 'start'|'post_name', opener after any compound lead)."""
    if lead is not None and name_colon:
        op, pos = first_word(rest), "post_name"
    else:
        op, pos = first_word(title_nfkc), "start"
    op_al = first_word(rest) if lead is not None else first_word(title_nfkc)
    return op, pos, op_al


def _slot_maps():
    lx = lexicon()["slots"]
    word2slot = {}
    for k, v in lx.items():
        if v["position"] != "opener":
            continue
        for w in v["llm"]:
            word2slot[w] = (k, 1)
        for w in v["neutral"]:
            word2slot[w] = (k, 0)
    return word2slot


# --------------------------------------------------------------------------------------------
# Builder
# --------------------------------------------------------------------------------------------
def _contains(s: pd.Series, rx: str, flags=0) -> pd.Series:
    """Python-re search (pandas 3 pyarrow strings would use RE2 in .str.contains)."""
    r = re.compile(rx, flags)
    return pd.Series([r.search(x) is not None for x in s], index=s.index, dtype=bool)


def _extract(s: pd.Series, rx: str, flags=0) -> pd.Series:
    r = re.compile(rx, flags)
    out = []
    for x in s:
        m = r.search(x)
        out.append(m.group(1) if m else np.nan)
    return pd.Series(out, index=s.index, dtype=object)


def build(u: pd.DataFrame) -> pd.DataFrame:
    """Features for universe rows u (needs submission_id, year, title, title_nfkc, abstract)."""
    lx = lexicon()
    title_raw = u.title.fillna("")
    t = u.title_nfkc.fillna("")
    a_raw = u.abstract.fillna("")
    a_low = a_raw.map(lambda x: F.unicodedata.normalize("NFKC", x).lower())
    tl = t.map(lambda x: F.strip_math(x).lower())  # lower-cased, math-stripped NFKC title

    # v1 features (title_features applies NFKC itself) + lead/rest
    v1 = pd.DataFrame([F.title_features(x) for x in t], index=u.index)
    lr = [F.lead_segment(x) for x in t]
    lead = pd.Series([l for l, _ in lr], index=u.index, dtype=object)
    rest = pd.Series([r for _, r in lr], index=u.index, dtype=object)

    out = pd.DataFrame({"submission_id": u.submission_id.values, "year": u.year.values}, index=u.index)
    v1 = v1.drop(columns=["llm_typography"])  # v1 computes it after NFKC, which erases U+2011; replaced below
    out = pd.concat([out, v1], axis=1)

    # NAME variants
    nv = pd.DataFrame([name_variants(l, nc) for l, nc in zip(lead, out.name_colon)], index=u.index)
    out = pd.concat([out, nv], axis=1)
    out["name_primary"] = out.name_colon
    out["name_compound"] = out.compound
    for o in ["all_caps", "mixed_case", "word", "paren_acronym"]:
        out[f"ortho_{o}"] = out.name_orthography.eq(o)
    for c in ["title_case", "sentence_case", "all_caps", "mixed", "other"]:
        out[f"case_{c}"] = out.casing.eq(c)

    # Openers and LLM slots
    ops = [opener(x, l, r, nc) for x, l, r, nc in zip(t, lead, rest, out.name_colon)]
    out["opener_word"] = [o[0] for o in ops]
    out["opener_pos"] = [o[1] for o in ops]
    out["opener_word_al"] = [o[2] for o in ops]
    out["opener_gerund"] = out.opener_word.str.len().gt(4) & out.opener_word.str.endswith("ing") \
        & ~out.opener_word.isin(GERUND_STOP)
    w2s = _slot_maps()
    sense = lx["slot_sense_exclusions_preV2"]
    stems = lx["slot_word_stems"]
    # opener text used for the sense filters: title from the opener on (after an optional NAME lead)
    op_text = pd.Series(np.where(out.opener_pos.eq("post_name"), rest.fillna("").map(str), t), index=u.index)
    op_text = op_text.map(lambda x: F.strip_math(x).lower().strip())
    sense_hit = pd.Series("", index=u.index)
    for nm, rx in sense.items():
        hit = _contains(op_text, rx)
        if nm == "boosting_algorithm":
            hit = hit | _contains(tl, rx)
        sense_hit = sense_hit.where(~hit | sense_hit.ne(""), nm)
    out["slot_word"] = ""
    out["slot_name"] = ""
    sense_rule = {"improve": ("boosting", ["boosting_algorithm"]),
                  "reveal": ("decoding", ["decoding_lm", "decoding_neural"])}
    for k in ["improve", "reveal", "exploit"]:
        raw = out.opener_word.map(lambda w: w2s[w][1] if w in w2s and w2s[w][0] == k else np.nan).astype(float)
        out[f"slot_{k}_raw"] = raw
        excl = pd.Series(False, index=u.index)
        if k in sense_rule:
            word, names = sense_rule[k]
            excl = raw.notna() & out.opener_word.eq(word) & sense_hit.isin(names)
        out[f"slot_{k}"] = raw.where(~excl)
        al = out.opener_word_al.map(lambda w: w2s[w][1] if w in w2s and w2s[w][0] == k else np.nan).astype(float)
        out[f"slot_{k}_al"] = al
        filled = raw.notna()
        out.loc[filled, "slot_word"] = out.opener_word[filled]
        out.loc[filled, "slot_name"] = k
    out["slot_sense_flag"] = np.where(out.slot_word.isin(["boosting", "decoding"]), sense_hit, "")
    sa = lx["slots"]["study_adj"]
    m = _extract(tl, sa["regex"])
    out["slot_study_adj_raw"] = np.where(m.isna(), np.nan, m.eq("comprehensive").astype(float))
    out["slot_study_adj"] = out.slot_study_adj_raw
    out["slot_study_adj_word"] = m.fillna("")
    # does the abstract contain the same lemma as the slot word? (robustness: title-specific choice)
    def lemma_in_abs(word, ab):
        if not word:
            return np.nan
        return bool(re.search(r"\b" + stems[word], ab))
    out["slot_word_in_abstract"] = pd.Series([lemma_in_abs(w, ab) for w, ab in zip(out.slot_word, a_low)],
                                             index=u.index, dtype=float)
    out["slot_study_adj_word_in_abstract"] = pd.Series(
        [lemma_in_abs(w, ab) for w, ab in zip(out.slot_study_adj_word, a_low)], index=u.index, dtype=float)
    out["slot_any_filled"] = out[["slot_improve", "slot_reveal", "slot_exploit", "slot_study_adj"]].notna().any(axis=1)

    # Control pairs (first occurrence anywhere in the title)
    for k, v in lx["control_pairs"].items():
        w = _extract(tl, r"\b(%s|%s)\b" % (re.escape(v["variant"]), re.escape(v["reference"])))
        out[f"ctrl_{k}"] = np.where(w.isna(), np.nan, w.eq(v["variant"]).astype(float))

    # Register families (title)
    for fam, d in lx["register"].items():
        cols = []
        for nm, rx in d.items():
            c = f"{fam.lower()}_{nm.replace('-', '_')}"
            out[c] = _contains(tl, rx)
            cols.append(c)
        out[f"{fam.lower()}_n"] = out[cols].sum(axis=1).astype(int)
        out[f"{fam.lower()}_any"] = out[f"{fam.lower()}_n"].gt(0)

    out = out.copy()
    # Abstract fingerprints
    fp = lx["fingerprints"]
    R = pd.DataFrame({w: _contains(a_low, rx) for w, rx in fp["RARE21"].items()}, index=u.index)
    out["f24_n"] = R.sum(axis=1).astype(int)
    out["f24"] = out.f24_n.ge(1)
    out["f24_2"] = out.f24_n.ge(2)
    out["f24_words"] = R.apply(lambda r: "|".join(R.columns[r.values]), axis=1)
    W26 = pd.DataFrame({w: _contains(a_low, rx) for w, rx in fp["F26_words"].items()}, index=u.index)
    out["f26_words_n"] = W26.sum(axis=1).astype(int)
    out["f26_words"] = out.f26_words_n.ge(1)
    out["f26_words_list"] = W26.apply(lambda r: "|".join(W26.columns[r.values]), axis=1)
    typo = fp["typography_raw"]
    out["title_nbhyphen"] = _contains(title_raw, typo["nb_hyphen"])
    out["title_endash_compound"] = _contains(title_raw, typo["endash_compound"])
    out["title_emdash"] = _contains(title_raw, typo["emdash"])
    out["abs_nbhyphen"] = _contains(a_raw, typo["nb_hyphen"])
    out["abs_endash_compound"] = _contains(a_raw, typo["endash_compound"])
    out["abs_emdash"] = _contains(a_raw, typo["emdash"])
    out["abs_emdash_n"] = a_raw.map(lambda x: x.count(typo["emdash"])).astype(int)
    # title typography = v1 LLM_TYPO (U+2011 or letter-en dash-letter) applied to the RAW title
    out["title_typo"] = _contains(title_raw, F.LLM_TYPO.pattern)
    out["llm_typography_v1"] = [bool(F.LLM_TYPO.search(x)) for x in t]  # v1 behaviour (NFKC) for reference
    out["f26_typo"] = out.title_nbhyphen | out.title_endash_compound | out.abs_nbhyphen | out.abs_endash_compound
    out["f26"] = out.f26_words | out.f26_typo
    out["F_any"] = out.f24 | out.f26 | out.title_typo

    out = out.copy()
    # LLM mentions in title / abstract (abbreviation vs spelled out)
    lm = lx["llm_mention"]
    for nm, src_raw, src_low in [("t", t, tl), ("a", a_raw, a_low)]:
        ab = _contains(src_raw, lm["abbrev_case_sensitive"])
        sp = _contains(src_low, lm["spelled_case_insensitive"])
        nmd = _contains(src_raw, lm["named_case_sensitive"])
        out[f"llm_{nm}_abbrev"] = ab
        out[f"llm_{nm}_spelled"] = sp
        out[f"llm_{nm}_named"] = nmd
        out[f"llm_{nm}_abbrev_only"] = ab & ~sp
        out[f"llm_{nm}_any"] = ab | sp | nmd

    # D2 style markers
    mk = lx["d2_style_markers"]["markers"]
    mcols = {}
    for nm, (kind, spec) in mk.items():
        if kind == "col":
            if "==" in spec:
                col, val = spec.split("==")
                mcols[f"mk_{nm}"] = out[col].eq(val)
            else:
                mcols[f"mk_{nm}"] = out[spec].astype(bool)
        elif kind == "re":
            mcols[f"mk_{nm}"] = _contains(tl, spec)
        elif kind == "tpl":
            mcols[f"mk_{nm}"] = out[spec].astype(bool)
        else:
            raise ValueError(kind)

    # Name-mask diagnostics (V4): is the lead in the abstract, and does it survive the R3 mask?
    masked = [mask_abstract(ab, l, return_counts=True) for ab, l in zip(a_raw, lead)]
    mcols["lead_in_abstract"] = pd.Series([n > 0 for _, n, _ in masked], index=u.index)
    mcols["mask_lead_hits"] = pd.Series([n for _, n, _ in masked], index=u.index)
    mcols["mask_token_hits"] = pd.Series([k for _, _, k in masked], index=u.index)
    rl = [raw_lead(x) for x in t]
    mcols["lead_raw"] = pd.Series([x or "" for x in rl], index=u.index)
    mcols["lead_survives_mask"] = pd.Series([lead_survives(mtxt, l) for (mtxt, _, _), l in zip(masked, rl)],
                                            index=u.index)
    out = pd.concat([out, pd.DataFrame(mcols, index=u.index)], axis=1)

    # Bool columns as bool; drop pandas index
    for c in out.columns:
        if out[c].dtype == object and out[c].map(lambda v: isinstance(v, (bool, np.bool_))).all():
            out[c] = out[c].astype(bool)
    return out.reset_index(drop=True)


def write_hashes(path: Path):
    lines = [
        f"{sha256(LEXICON_PATH)}  analyses/lexicons.json",
        f"{sha256(FEATURES_PY)}  features.py (v1, version-locked by content hash; no git commit available)",
        f"{sha256(Path(__file__))}  analyses/features_v2.py",
    ]
    path.write_text("\n".join(lines) + "\n")
    return lines


def main():
    sys.path.insert(0, str(_SRC))
    from analyses._core import FEAT_DIR, FEATURES_PATH, load_universe
    FEAT_DIR.mkdir(parents=True, exist_ok=True)
    u = load_universe(["submission_id", "year", "title", "title_nfkc", "abstract"])
    f = build(u)
    assert f.submission_id.is_unique and len(f) == len(u)
    f.to_parquet(FEATURES_PATH, index=False)
    for ln in write_hashes(FEAT_DIR / "lexicon_hash.txt"):
        print(ln)
    print("features_v2", f.shape)
    cols = ["name_primary", "name_strict", "name_loose", "name_compound", "f24", "f26", "F_any", "title_typo",
            "r24_any", "r26_any"]
    print(f.groupby("year")[cols].mean().round(3).to_string())


if __name__ == "__main__":
    main()
