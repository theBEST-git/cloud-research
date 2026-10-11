"""Outcome-blind features derived from the topics and keyword types.

Writes to output/:
- topic_year_panel.csv           one row per (level, topic, year): submissions, share of that year, change vs previous year
- paper_keyword_profile.csv.gz   one row per paper: how many of its keywords fall in each keyword type
- generic_keyword_breakdown.csv  what papers using broad labels (e.g. "deep learning") are about, by era and topic level

    python research/topics/derive_features.py
"""
from __future__ import annotations

import collections

import pandas as pd

from common import ERAS, LEVELS, OUTPUT, load_corpus, write_csv_gz

KEYWORD_TYPES = ["generic_field", "research_area", "specific_topic", "application_domain", "property",
                 "contribution_type", "unclear"]
BREAKDOWN_MIN_PAPERS = 300      # broad labels (non-specific types) used by at least this many papers are broken down


def topic_names() -> pd.DataFrame:
    path = OUTPUT / "topic_catalog.csv"
    cat = pd.read_csv(path if path.exists() else OUTPUT / "topic_catalog_auto.csv", keep_default_na=False)
    if "name" not in cat:
        cat["name"] = cat.keyword_signature
    return cat


def year_panel(assign: pd.DataFrame, names: pd.DataFrame) -> pd.DataFrame:
    totals = assign.year.value_counts()
    rows = []
    for level in LEVELS:
        counts = assign.groupby([level, "year"]).size().unstack(fill_value=0)
        for topic, row in counts.iterrows():
            prev = None
            for year, n in row.items():
                share = n / totals[year]
                rows.append({"level": level, "topic": topic, "year": year, "submissions": int(n),
                             "share_of_year": round(share, 6),
                             "share_ratio_vs_prev_year": round(share / prev, 4) if prev else None})
                prev = share
    panel = pd.DataFrame(rows)
    return panel.merge(names[["topic", "name"]], on="topic", how="left")


def keyword_profile(corpus: pd.DataFrame, types: dict[str, str]) -> pd.DataFrame:
    rows = []
    for sid, kws in zip(corpus.submission_id, corpus.keywords):
        c = collections.Counter(types.get(k, "rare_untyped") for k in kws)
        rows.append({"submission_id": sid, "n_keywords": len(kws),
                     **{f"n_{t}": c.get(t, 0) for t in KEYWORD_TYPES + ["rare_untyped"]}})
    return pd.DataFrame(rows)


def breakdown(corpus: pd.DataFrame, assign: pd.DataFrame, types: dict[str, str], names: pd.DataFrame) -> pd.DataFrame:
    frame = corpus[["submission_id", "keywords"]].merge(assign, on="submission_id")
    counts = collections.Counter(k for kws in frame.keywords for k in set(kws))
    broad = sorted((k for k, t in types.items() if t != "specific_topic" and counts[k] >= BREAKDOWN_MIN_PAPERS),
                   key=lambda k: (-counts[k], k))
    name = dict(zip(names.topic, names.name))
    rows = []
    for kw in broad:
        sub = frame[frame.keywords.map(lambda kws: kw in kws)]
        for era, (lo, hi) in {"all years": (2017, 2026), **ERAS}.items():
            e = sub[sub.year.between(lo, hi)]
            if len(e) < 30:
                continue
            for level in ("mid", "fine"):
                share = e[level].value_counts(normalize=True)
                for rank, (topic, s) in enumerate(share.items(), 1):
                    rows.append({"keyword": kw, "keyword_type": types[kw], "era": era, "papers": len(e), "level": level,
                                 "rank": rank, "topic": topic, "topic_name": name.get(topic, ""), "share": round(s, 4),
                                 "topics_for_80pct": int((share.cumsum() < 0.8).sum() + 1)})
    return pd.DataFrame(rows)


def main() -> None:
    corpus = load_corpus()
    assign = pd.read_csv(OUTPUT / "topic_assignments.csv.gz")
    names = topic_names()
    types = dict(pd.read_csv(OUTPUT / "keyword_types.csv", keep_default_na=False)[["keyword", "type"]].values)
    year_panel(assign, names).to_csv(OUTPUT / "topic_year_panel.csv", index=False)
    write_csv_gz(keyword_profile(corpus, types), OUTPUT / "paper_keyword_profile.csv.gz")
    b = breakdown(corpus, assign, types, names)
    b.to_csv(OUTPUT / "generic_keyword_breakdown.csv", index=False)
    top = b[(b.era == "all years") & (b.level == "mid") & (b["rank"] == 1)]
    for r in top.itertuples():
        print(f"{r.keyword!r:32s} ({r.keyword_type}, {r.papers} papers): {r.topics_for_80pct} middle topics cover 80%; "
              f"largest = {r.topic_name[:60]} ({r.share:.0%})")


if __name__ == "__main__":
    main()
