"""Rule-based title features: surface form, colon/branding structure, rhetorical templates, lexicons.

Every detector is a transparent regex or token rule so that it can be audited against a
hand-checked sample (see validate_features.py). Nothing here looks at outcomes.
"""
from __future__ import annotations

import re
import unicodedata

import numpy as np
import pandas as pd

# LaTeX math is common in ML titles (e.g. "S$^6$-DAMON"); strip it before splitting on colons.
MATH = re.compile(r"\$[^$]*\$")
WORD = re.compile(r"[A-Za-z][A-Za-z0-9'\-]*|[0-9]+(?:\.[0-9]+)?")
# "X: Y", "X:Y" (no space, but not ratios like 2:4 or N:M), fullwidth colon, or a spaced dash "X -- Y" / "X — Y".
COLON = re.compile(r"\s*[:：]\s+|(?<=[A-Za-z0-9)\]]{2})[:：](?=[A-Za-z])|\s+[-–—]{1,2}\s+")

FUNCTION_WORDS = {
    "a", "an", "the", "of", "for", "in", "on", "with", "to", "and", "or", "via", "by", "from", "at",
    "as", "is", "are", "be", "into", "through", "under", "over", "using", "towards", "toward",
    "without", "beyond", "across", "within", "between", "against", "about", "do", "does", "can",
    "not", "all", "you", "need", "when", "what", "how", "why", "which", "we", "it", "its", "that",
    "this", "your", "our", "vs", "versus", "than", "more", "less", "make", "makes",
}

QUESTION_OPENERS = {"how", "what", "why", "when", "where", "which", "who", "can", "could", "do", "does",
                    "did", "is", "are", "was", "were", "should", "will", "would", "has", "have"}

# Rhetorical templates (snowclones and stock openers). Patterns run on the lowercased title.
TEMPLATES: dict[str, str] = {
    "all_you_need": r"\b(?:is|are)\s+(?:not\s+)?(?:all|what|everything)\s+(?:you|we)\s+need\b|\ball\s+you\s+need\b",
    "towards": r"^(?:[^:]*:\s*)?towards?\b",
    "rethinking": r"^(?:[^:]*:\s*)?rethinking\b",
    "revisiting": r"^(?:[^:]*:\s*)?revisiting\b",
    "on_the": r"^on\s+the\b",
    "understanding": r"^(?:[^:]*:\s*)?understanding\b",
    "demystifying": r"^(?:[^:]*:\s*)?demystifying\b",
    "learning_to": r"^(?:[^:]*:\s*)?learning\s+to\b",
    "a_simple": r"^(?:[^:]*:\s*)?(?:a|an)\s+(?:simple|embarrassingly\s+simple|surprisingly\s+simple|minimalist)\b|\bsimple\s+(?:yet|but)\s+(?:effective|strong|powerful)\b",
    "empirical_study": r"\b(?:an?\s+)?(?:empirical|systematic|comprehensive|large-scale)\s+(?:study|investigation|analysis|evaluation)\b",
    "matters": r"\bmatters?\b(?=\s*(?:[:?!.]|$))",
    "when_meets": r"\bwhen\b.+\bmeets?\b|\bmeets\b",
    "less_is_more": r"\bless\s+is\s+more\b|\bmore\s+is\s+(?:less|more|better)\b",
    "devil_in": r"\bdevil\s+is\s+in\b|\bthe\s+devil\b",
    "lost_in": r"^(?:[^:]*:\s*)?lost\s+in\b",
    "tale_of": r"\ba\s+tale\s+of\b",
    "rule_them_all": r"\bto\s+rule\s+them\s+all\b",
    "do_really": r"^(?:do|does|can|are|is)\b.+\breally\b",
    "beyond": r"^(?:[^:]*:\s*)?beyond\b",
    "at_scale": r"\bat\s+scale\b",
    "free_lunch": r"\bfree\s+lunch\b",
    "is_secretly": r"\bis\s+secretly\b|\bsecretly\b",
    "worth_a_thousand": r"\bworth\s+(?:a\s+thousand|\d+x?\d*)\s+words\b|\bworth\s+a\b",
    "x_for_y_via_z": r"\bfor\b.+\bvia\b",
}
TEMPLATE_RE = {k: re.compile(v) for k, v in TEMPLATES.items()}

# Gerund/verb openers that frame the paper as an action ("Unlocking ...", "Harnessing ...").
ACTION_OPENERS = (
    "unlocking", "unleashing", "harnessing", "unveiling", "empowering", "boosting", "enhancing",
    "improving", "bridging", "navigating", "exploring", "leveraging", "scaling", "taming",
    "mitigating", "advancing", "accelerating", "uncovering", "elevating", "redefining", "reimagining",
    "delving", "decoding", "breaking", "pushing", "closing",
)


PLACEHOLDER_TITLES = {"", "title", "withdrawn", "withdraw", "na", "n/a", "xxx", "xxxx", "111", "placeholder", "null"}
# Typography that LLM output produces but keyboards rarely do: non-breaking hyphen, en dash joining letters.
LLM_TYPO = re.compile(r"\u2011|[A-Za-z]\u2013[A-Za-z]")


def is_placeholder(title: str, abstract: str | None = None) -> bool:
    t = (title or "").strip().lower()
    return t in PLACEHOLDER_TITLES or (abstract is not None and len((abstract or "").split()) < 20)


def name_orthography(lead: str) -> str:
    """Orthographic class of a coined lead: all_caps (CRISP), mixed_case (LoRA), paren_acronym, or word (Chameleon)."""
    if PAREN_ACRONYM.search(lead):
        return "paren_acronym"
    letters = [c for c in lead if c.isalpha()]
    if len(letters) >= 2 and all(c.isupper() for c in letters):
        return "all_caps"
    if any(c.isupper() for c in lead[1:]) or any(c.isdigit() for c in lead):
        return "mixed_case"
    return "word"


def casing_style(title: str) -> str:
    letters = [c for c in strip_math(title) if c.isalpha()]
    if len(letters) >= 12 and sum(c.isupper() for c in letters) / len(letters) > 0.8:
        return "all_caps"
    share = is_title_case(title)
    if share != share:  # NaN: too few content words
        return "other"
    return "title_case" if share >= 0.75 else "sentence_case" if share <= 0.25 else "mixed"


def strip_math(title: str) -> str:
    return MATH.sub("MATH", title)


def tokens(title: str) -> list[str]:
    return WORD.findall(strip_math(title))


def lead_segment(title: str) -> tuple[str | None, str]:
    """Split a compound title at the first colon / spaced dash. Returns (lead, rest) or (None, title)."""
    t = strip_math(title).strip()
    m = COLON.search(t)
    if not m or m.start() == 0:
        return None, title
    return t[: m.start()].strip(), t[m.end():].strip()


GENERIC_LEADS = {"position", "survey", "review", "note", "erratum", "tutorial", "commentary", "perspective"}
PAREN_ACRONYM = re.compile(r"\(([A-Za-z0-9'\-+.]{2,})\)\s*$")


def is_coined_name(segment: str) -> bool:
    """Lead segment that names an artifact rather than describing it.

    True for a single token ('LoRA', 'GPT-4V', 'Qronos', 'Chameleon'), a two-token coined name
    ('LLaVA 1.5'), or a phrase ending in a parenthetical acronym ('Trusted Aggregation (TAG)').
    Generic genre labels ('Position:', 'Survey:') are excluded. Audited in validate_features.py.
    """
    seg = segment.strip().strip("\"'`")
    if PAREN_ACRONYM.search(seg):
        return True
    parts = seg.split()
    if not seg or len(parts) > 2:
        return False
    if len(parts) == 1:
        word = re.sub(r"[^A-Za-z]", "", parts[0]).lower()
        return word not in FUNCTION_WORDS and word not in GENERIC_LEADS
    if not re.fullmatch(r"[A-Za-z0-9.\-+]+", parts[1]):
        return False
    core = parts[0]
    if core.lower() in FUNCTION_WORDS:
        return False
    upper = sum(c.isupper() for c in core)
    has_inner_upper = any(c.isupper() for c in core[1:])
    has_digit = any(c.isdigit() for c in core)
    # Two tokens: "LLaVA 1.5" counts; descriptive pairs such as "Stable Diffusion" do not.
    return has_inner_upper or has_digit or upper >= 2


def is_title_case(title: str) -> float:
    words = [w for w in tokens(title) if w.isalpha() and w.lower() not in FUNCTION_WORDS]
    if len(words) < 2:
        return np.nan
    return float(np.mean([w[0].isupper() for w in words[1:]]))


def title_features(title: str) -> dict:
    t = unicodedata.normalize("NFKC", title or "").strip()
    low = t.lower()
    toks = tokens(t)
    lead, rest = lead_segment(t)
    coined = lead is not None and is_coined_name(lead)
    first = toks[0].lower() if toks else ""
    feats = {
        "n_chars": len(t),
        "n_words": len(toks),
        "compound": lead is not None,
        "name_colon": coined,
        "phrase_colon": lead is not None and not coined,
        "lead_segment": lead if lead is not None else "",
        "name_orthography": name_orthography(lead) if coined else "",
        "casing": casing_style(t),
        "llm_typography": bool(LLM_TYPO.search(t)),
        "question": "?" in t,
        "question_opener": first in QUESTION_OPENERS and "?" in t,
        "first_word": first,
        "action_opener": (rest.split()[0].lower() if rest.split() else "") in ACTION_OPENERS
        or first in ACTION_OPENERS,
        "has_math": "$" in t,
        "has_digit": any(ch.isdigit() for ch in strip_math(t)),
        "title_case_share": is_title_case(t),
        "exclamation": "!" in t,
        "quoted": bool(re.search(r"[\"“”‘’]|''|``", t)),
        "mentions_llm": bool(re.search(r"\bllms?\b|large language models?|\blanguage models?\b|\bgpt[- ]?\d|\bchatgpt\b", low)),
    }
    for name, rx in TEMPLATE_RE.items():
        feats[f"tpl_{name}"] = bool(rx.search(low))
    return feats


def build(s: pd.DataFrame) -> pd.DataFrame:
    rows = [title_features(t) for t in s["title"].fillna("")]
    f = pd.DataFrame(rows, index=s.index)
    f.insert(0, "submission_id", s["submission_id"].values)
    f.insert(1, "year", s["year"].values)
    return f
