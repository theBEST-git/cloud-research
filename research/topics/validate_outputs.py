"""Check the topic-layer outputs for completeness and internal consistency.

    python research/topics/validate_outputs.py
"""
from __future__ import annotations

import collections
import json
import re

import numpy as np
import pandas as pd

from common import CACHE, HERE, LEVEL_SIZES, OUTPUT, embedded_corpus, load_corpus

OUTCOME_COLUMNS = ["decision", "outcome_eligible", "administrative_status", "review_count", "distinct_reviewers",
                   "base_decision", "decision_evidence"]
KEYWORD_TYPES = {"generic_field", "research_area", "specific_topic", "application_domain", "property",
                 "contribution_type", "unclear"}


def check(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)
    print("ok  ", message)


def main() -> None:
    corpus = embedded_corpus()
    a = pd.read_csv(OUTPUT / "topic_assignments.csv.gz")
    cat = pd.read_csv(OUTPUT / "topic_catalog.csv", keep_default_na=False)

    check(a.submission_id.is_unique and a.submission_id.equals(corpus.submission_id),
          f"every paper with a real abstract has exactly one topic ({len(a)} papers)")
    for level, k in LEVEL_SIZES.items():
        n = a[level].nunique()
        right_count = n == k if level != "fine" else 0.9 * k <= n <= k      # small fine pieces are folded into siblings
        check(right_count and set(a[level]) == set(cat[cat.level == level].topic), f"{n} {level} topics, all described in the catalog")
    check(cat[cat.level == "fine"].papers.min() >= 60, "every fine topic has at least 60 papers")
    stab = pd.read_csv(OUTPUT / "paper_topic_stability.csv.gz")
    check(stab.submission_id.equals(a.submission_id) and stab.drop(columns="submission_id").stack().between(0, 1).all(),
          "per-paper stability covers every paper and lies in [0, 1]")
    check((a.groupby("fine").mid.nunique() == 1).all() and (a.groupby("mid").coarse.nunique() == 1).all(),
          "levels nest: each fine topic sits in one middle topic, each middle topic in one broad topic")
    named = cat.name.str.strip().ne("")
    check(named.all() and not cat.duplicated(["level", "name"]).any(), "every topic has a name, unique within its level")
    sizes = cat.set_index("topic").papers
    check(all((a[level].value_counts() == sizes[a[level].value_counts().index]).all() for level in LEVEL_SIZES),
          "catalog paper counts match the assignments")

    if (CACHE / "specter2.npy").exists():
        from assign_topics import assign
        again = assign(np.load(CACHE / "specter2.npy"))
        check((again.fine.values == a.fine.values).all(), "saved topic model reproduces every assignment")

    kt = pd.read_csv(OUTPUT / "keyword_types.csv", keep_default_na=False)
    counts = collections.Counter(k for kws in load_corpus().keywords for k in set(kws))
    expected = {k for k, v in counts.items() if v >= 20}
    check(set(kt.keyword) == expected and kt.keyword.is_unique, f"all {len(expected)} keywords used by >=20 papers are typed once")
    check(set(kt.type) <= KEYWORD_TYPES, "keyword types come from the codebook")

    b = pd.read_csv(OUTPUT / "generic_keyword_breakdown.csv", keep_default_na=False)
    sums = b.groupby(["keyword", "era", "level"]).share.sum()
    check(((sums - 1).abs() < 0.01).all(), "each keyword's topic shares sum to 1 per era and level")

    panel = pd.read_csv(OUTPUT / "topic_year_panel.csv")
    check((panel.groupby(["level", "year"]).share_of_year.sum().sub(1).abs() < 1e-3).all(), "topic shares sum to 1 within each year")

    pattern = re.compile(r"\b(" + "|".join(OUTCOME_COLUMNS) + r")\b")
    leaks = [p.name for p in HERE.glob("*.py") if p.name != "validate_outputs.py" and pattern.search(p.read_text())]
    check(not leaks, "no topic-layer script mentions an outcome or review column" + (f": {leaks}" if leaks else ""))
    print(json.dumps({"validation": "passed", "papers": len(a)}))


if __name__ == "__main__":
    main()
