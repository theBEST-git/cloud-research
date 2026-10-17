"""Match accepted ICLR submissions (discovery universe) to Semantic Scholar venue records by normalised
title (S2 year within [conf_year-2, conf_year]). Reports match rates; writes outputs/cites/matched.parquet.
Outcome columns are carried but not analysed here.
"""
from __future__ import annotations

import glob
import json
import re
import unicodedata

import pandas as pd

from analyses import _core as C

OUT = C.OUT / "cites"


def norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", t)


def load_s2():
    rows = []
    for f in sorted(glob.glob(str(C.CACHE / "s2" / "*.jsonl"))):
        rows += [json.loads(l) for l in open(f) if l.strip()]
    S = pd.DataFrame(rows).drop_duplicates("paperId")
    S["key"] = S.title.map(norm)
    S["arxiv"] = S.externalIds.map(lambda e: (e or {}).get("ArXiv"))
    S["dblp"] = S.externalIds.map(lambda e: (e or {}).get("DBLP"))
    return S


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    u = pd.read_parquet(C.UNIVERSE_PATH, columns=["submission_id", "year", "title", "ACC"])
    acc = u[u.ACC].copy()
    acc["key"] = acc.title.map(norm)
    S = load_s2()
    cand = acc.merge(S[["key", "paperId", "year", "citationCount", "influentialCitationCount", "arxiv", "dblp", "venue"]]
                     .rename(columns={"year": "s2_year"}), on="key", how="left")
    ok = cand.s2_year.isna() | ((cand.s2_year <= cand.year) & (cand.s2_year >= cand.year - 2))
    cand = cand[ok]
    # several S2 records for one title: keep the one with most citations, record how many
    cand["n_s2"] = cand.groupby("submission_id").paperId.transform("count")
    best = cand.sort_values("citationCount", ascending=False).drop_duplicates("submission_id")
    M = acc.merge(best[["submission_id", "paperId", "s2_year", "citationCount", "influentialCitationCount", "arxiv", "dblp", "venue", "n_s2"]],
                  on="submission_id", how="left")
    M["matched"] = M.paperId.notna()
    M.drop(columns=["key"]).to_parquet(OUT / "matched_venue.parquet")
    r = M.groupby("year").agg(accepted=("submission_id", "size"), matched=("matched", "sum"),
                              has_arxiv=("arxiv", lambda s: s.notna().sum()), multi=("n_s2", lambda s: (s > 1).sum()))
    r["rate"] = (r.matched / r.accepted).round(3)
    print(r)
    print("total", int(M.matched.sum()), "/", len(M))


if __name__ == "__main__":
    main()
