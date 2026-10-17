"""QC: for matched papers whose S2 venue record has no arXiv id, ask S2's title-match endpoint whether a
different record (e.g. a separate arXiv record) exists. Appends one JSON line per paper to
outputs/cites/qc_split_records.jsonl. Download-only; no title-citation analysis.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

import pandas as pd

from analyses import _core as C

OUT = C.OUT / "cites"


def main(n=30):
    M = pd.read_parquet(OUT / "matched_venue.parquet")
    s = M[M.matched & M.arxiv.isna() & (M.year <= 2025)].sample(n, random_state=1)
    dst = OUT / "qc_split_records.jsonl"
    done = set()
    if dst.exists():
        done = {json.loads(l)["sid"] for l in open(dst)}
    for r in s.itertuples():
        if r.submission_id in done:
            continue
        url = "https://api.semanticscholar.org/graph/v1/paper/search/match?" + urllib.parse.urlencode(
            {"query": r.title, "fields": "paperId,title,year,citationCount,externalIds"})
        d = None
        for k in range(8):
            try:
                with urllib.request.urlopen(url, timeout=40) as f:
                    d = json.load(f)
                break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    d = {"data": []}
                    break
                time.sleep(min(120, 5 * 2 ** k))
        top = ((d or {}).get("data") or [{}])[0]
        rec = {"sid": r.submission_id, "venue_pid": r.paperId, "venue_cites": r.citationCount, "match_pid": top.get("paperId"),
               "match_cites": top.get("citationCount"), "match_arxiv": (top.get("externalIds") or {}).get("ArXiv")}
        with open(dst, "a") as f:
            f.write(json.dumps(rec) + "\n")
        print(rec, flush=True)
        time.sleep(3)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
