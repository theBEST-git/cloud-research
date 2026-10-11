"""Camera-ready audit: how often do titles change between a pre-decision arXiv version and the stored title?

The exported metadata is a post-decision snapshot, so accepted papers may carry camera-ready titles.
For a stratified sample of accepted and rejected submissions we locate the paper on arXiv
(public export API, rate-limited to one request per ~3 s), take version 1 when it predates the
ICLR decision date, and compare its title to the stored OpenReview title. The accepted-minus-
rejected difference in change rates bounds the camera-ready contribution to title features.

Only arXiv identifiers, version dates and version-1 titles are cached (cache/arxiv_audit.jsonl).
"""
from __future__ import annotations

import argparse
import json
import re
import ssl
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
import pandas as pd

from common import CACHE, load_submissions, read_table

API = "https://export.arxiv.org/api/query?"
NS = {"a": "http://www.w3.org/2005/Atom"}
# Notification dates of ICLR decisions (conference year -> date); v1 must predate these.
DECISION_DATE = {2022: "2022-01-24", 2023: "2023-01-21", 2024: "2024-01-16", 2025: "2025-01-22", 2026: "2026-01-26"}
STOP = set("a an the of for in on with to and or via by from at as is are be into using towards toward we our do does can".split())
_last_call = [0.0]


def _ctx():
    ca = Path("/root/.ccr/ca-bundle.crt")
    return ssl.create_default_context(cafile=str(ca)) if ca.exists() else ssl.create_default_context()


CTX = _ctx()


def query(params: dict) -> list[dict]:
    wait = 3.2 - (time.time() - _last_call[0])
    if wait > 0:
        time.sleep(wait)
    url = API + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60, context=CTX) as r:
                body = r.read()
            break
        except Exception:  # transient network/proxy errors: back off and retry
            time.sleep(5 * 2 ** attempt)
    else:
        _last_call[0] = time.time()
        return []
    _last_call[0] = time.time()
    root = ET.fromstring(body)
    out = []
    for e in root.findall("a:entry", NS):
        out.append({
            "id": e.findtext("a:id", default="", namespaces=NS).rsplit("/abs/", 1)[-1],
            "title": " ".join(e.findtext("a:title", default="", namespaces=NS).split()),
            "summary": " ".join(e.findtext("a:summary", default="", namespaces=NS).split()),
            "published": e.findtext("a:published", default="", namespaces=NS),
            "updated": e.findtext("a:updated", default="", namespaces=NS),
            "authors": [a.findtext("a:name", default="", namespaces=NS) for a in e.findall("a:author", NS)],
        })
    return out


def words(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP and len(w) > 2]


def jaccard(a: str, b: str) -> float:
    x, y = set(words(a)), set(words(b))
    return len(x & y) / max(1, len(x | y))


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def surname(name_json: str | None) -> str:
    try:
        name = json.loads(name_json) if name_json else ""
    except ValueError:
        name = ""
    parts = re.findall(r"[A-Za-z\-']+", name or "")
    return parts[-1] if parts else ""


def find(row) -> dict | None:
    """Search by title words, then by first-author surname plus title words; accept on text overlap."""
    tw = words(row.title)[:8]
    attempts = []
    if tw:
        attempts.append(" AND ".join(f"ti:{w}" for w in tw[:6]))
    if row.first_surname and tw:
        attempts.append(f"au:{row.first_surname} AND " + " AND ".join(f"ti:{w}" for w in tw[:3]))
    if row.first_surname:
        aw = sorted(set(words(row.abstract)), key=lambda w: (-len(w), w))[:3]
        if aw:
            attempts.append(f"au:{row.first_surname} AND " + " AND ".join(f"abs:{w}" for w in aw))
    for q in attempts:
        best, best_score = None, 0.0
        for c in query({"search_query": q, "max_results": 10}):
            score = max(jaccard(c["summary"], row.abstract), 0.0)
            tscore = jaccard(c["title"], row.title)
            surname_ok = bool(row.first_surname) and any(row.first_surname.lower() in a.lower() for a in c["authors"])
            ok = score >= 0.45 or (tscore >= 0.6 and surname_ok)
            if ok and score + tscore > best_score:
                best, best_score = c, score + tscore
        if best:
            best["abstract_jaccard"] = jaccard(best["summary"], row.abstract)
            return best
    return None


def sample(n_per_cell: int, seed: int, years=tuple(DECISION_DATE)) -> pd.DataFrame:
    s = load_submissions()
    a = read_table("submission_authors")
    first = a[a.source_list_position.eq(0)].set_index("submission_id").declared_name_json
    s = s[s.year.isin(years) & s.administrative_status.eq("ordinary_submission") & s.decision.isin(["accepted", "rejected"])]
    s = s.assign(first_surname=s.submission_id.map(first).map(surname))
    parts = [g.sample(min(n_per_cell, len(g)), random_state=seed) for _, g in s.groupby(["year", "decision"])]
    return pd.concat(parts)[["submission_id", "year", "decision", "title", "abstract", "first_surname"]]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--n-per-cell", type=int, default=120)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--years", type=int, nargs="+", default=list(DECISION_DATE))
    args = ap.parse_args()
    out = CACHE / "arxiv_audit.jsonl"
    done = set()
    if out.exists():
        done = {json.loads(l)["submission_id"] for l in out.open()}
    todo = sample(args.n_per_cell, args.seed, tuple(args.years))
    todo = todo[~todo.submission_id.isin(done)]
    print(f"{len(done)} cached, {len(todo)} to query", flush=True)
    with out.open("a") as f:
        for i, row in enumerate(todo.itertuples(index=False)):
            rec = {"submission_id": row.submission_id, "year": int(row.year), "decision": row.decision,
                   "or_title": row.title, "found": False}
            hit = find(row)
            if hit:
                base = hit["id"].split("v")[0] if re.search(r"v\d+$", hit["id"]) else hit["id"]
                v1 = query({"id_list": base + "v1"})
                rec.update(found=True, arxiv_id=base, latest_title=hit["title"], abstract_jaccard=hit["abstract_jaccard"],
                           v1_title=v1[0]["title"] if v1 else None, v1_date=v1[0]["published"][:10] if v1 else None)
            f.write(json.dumps(rec) + "\n")
            f.flush()
            if i % 25 == 0:
                print(i, flush=True)


if __name__ == "__main__":
    main()
