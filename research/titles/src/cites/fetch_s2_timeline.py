"""Citation timelines (citing-paper year counts) from Semantic Scholar for accepted, matched ICLR papers 2019-2023.

Purpose: compare cohorts at the SAME citation age (e.g. citations received by the end of year t+1), so that the
hot-area citation premium of old cohorts can be measured on the window that recent cohorts have.
The /citations endpoint returns at most 10,000 rows; papers above that are flagged `truncated` (their early-year
counts are lower bounds). Resumable. Writes cache/s2/timeline.jsonl:
{"paperId", "year" (conference year), "citationCount", "by_year": {citing_year: n}, "n_rows", "truncated"}.
Run: cd research/titles/src && nohup /home/user/venv/bin/python -m cites.fetch_s2_timeline > ../cache/s2/timeline.log 2>&1 &
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DST = ROOT / "cache" / "s2" / "timeline.jsonl"
BASE = "https://api.semanticscholar.org/graph/v1/paper/{}/citations?fields=year&limit=1000&offset={}"


def get(url, tries=12):
    for k in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (400, 404):
                return None
            wait = min(300, 5 * 2 ** k)
            print("HTTP", e.code, "wait", wait, flush=True)
            time.sleep(wait)
        except Exception as e:
            print("ERR", repr(e)[:120], flush=True)
            time.sleep(15)
    raise RuntimeError("giving up: " + url)


def main():
    m = pd.read_parquet(ROOT / "outputs" / "cites" / "matched_venue.parquet")
    m = m[m.matched & m.year.between(2019, 2023)]
    # random order (seed 0), 2019-21 first: any prefix of the fetch is a random sample of the oldest cohorts
    m = m.sample(frac=1, random_state=0)
    m = pd.concat([m[m.year <= 2021], m[m.year >= 2022]])
    done = set()
    if DST.exists():
        done = {json.loads(l)["paperId"] for l in open(DST) if l.strip()}
    todo = m[~m.paperId.isin(done)]
    print("todo", len(todo), "done", len(done), flush=True)
    with open(DST, "a") as f:
        for i, (pid, yr, cc) in enumerate(zip(todo.paperId, todo.year, todo.citationCount)):
            cnt, off, n, trunc = Counter(), 0, 0, False
            while True:
                d = get(BASE.format(pid, off))
                time.sleep(1.2)
                if d is None:
                    break
                for c in d.get("data", []):
                    cnt[str((c.get("citingPaper") or {}).get("year"))] += 1
                    n += 1
                nxt = d.get("next")
                if nxt is None:
                    break
                if nxt >= 9000:
                    trunc = True
                    break
                off = nxt
            f.write(json.dumps({"paperId": pid, "year": int(yr), "citationCount": float(cc), "by_year": cnt,
                                "n_rows": n, "truncated": trunc}) + "\n")
            f.flush()
            if i % 100 == 0:
                print(i, "/", len(todo), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
