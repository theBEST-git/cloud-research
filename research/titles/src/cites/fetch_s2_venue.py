"""Fetch Semantic Scholar records for the ICLR venue (bulk search, all years), with backoff.

Only downloads; no analysis. Writes cache/s2/iclr_venue_<year>.jsonl (one S2 record per line).
Run: cd research/titles/src && nohup /home/user/venv/bin/python -m cites.fetch_s2_venue > ../cache/s2/fetch_venue.log 2>&1 &
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "cache" / "s2"
BASE = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FIELDS = "paperId,title,year,venue,citationCount,influentialCitationCount,externalIds,publicationDate"
VENUES = ["International Conference on Learning Representations", "ICLR"]


def get(url, tries=10):
    for k in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            wait = min(300, 5 * 2 ** k)
            print("HTTP", e.code, "wait", wait, flush=True)
            time.sleep(wait)
        except Exception as e:  # network hiccup
            print("ERR", repr(e)[:120], flush=True)
            time.sleep(10)
    raise RuntimeError("giving up: " + url)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for year in range(2016, 2027):
        dst = OUT / f"iclr_venue_{year}.jsonl"
        if dst.exists() and dst.stat().st_size > 0:
            print("skip", year, flush=True)
            continue
        rows, seen = [], set()
        for venue in VENUES:
            token = None
            while True:
                q = {"query": "*", "venue": venue, "year": str(year), "fields": FIELDS}
                if token:
                    q["token"] = token
                d = get(BASE + "?" + urllib.parse.urlencode(q))
                for r in d.get("data", []):
                    if r["paperId"] not in seen:
                        seen.add(r["paperId"])
                        rows.append(r)
                token = d.get("token")
                print(year, venue[:10], "total", d.get("total"), "have", len(rows), flush=True)
                time.sleep(3)
                if not token:
                    break
        with open(dst, "w") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")
        print("wrote", year, len(rows), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
