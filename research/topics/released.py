"""Outcome-free reader for the released former-confirmation submissions (data_confirmation/, released 2026-10-18).

The release (data_confirmation/README.md) is a JSONL package whose submission records also carry outcome and review
fields. load_free() keeps only the content columns in FREE from each record as it is read, so no outcome value leaves
this module; the same text filter as load_corpus() marks the papers that can receive a topic. Author lists are not in
the release.
"""
from __future__ import annotations

import gzip
import json

import pandas as pd

from common import MIN_ABSTRACT_WORDS, ROOT

RELEASE = ROOT / "data_confirmation" / "released_data"
FREE = ["submission_id", "family_id", "year", "title", "abstract", "keywords", "primary_area", "split",
        "analysis_allowed", "released_from_confirmation"]


def load_free() -> pd.DataFrame:
    rows = []
    for path in sorted(RELEASE.glob("submissions-*.jsonl.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            rows += [{c: rec.get(c) for c in FREE} for rec in map(json.loads, stream)]
    s = pd.DataFrame(rows, columns=FREE).sort_values(["year", "submission_id"], kind="stable").reset_index(drop=True)
    s["has_text"] = s.abstract.fillna("").str.split().str.len() >= MIN_ABSTRACT_WORDS
    return s


def embedded_released() -> pd.DataFrame:
    """Released papers that receive a topic, in the row order of cache/specter2_released.npy."""
    s = load_free()
    return s[s.has_text].reset_index(drop=True)
