"""WP4 / V7: retrieval-route validation of the arXiv camera-ready audit, plus a background enlargement.

Why: the original audit (`src/arxiv_audit.py`, cache/arxiv_audit.jsonl) finds papers mainly by TITLE words. A
title route can only find a paper whose arXiv title still resembles the stored OpenReview title, so it may
under-find retitled papers and understate retitling (and feature flips). V7 re-queries a random subsample by a
route that never uses the title.

Phase 1 ("route", always first)
    Sample: a random subsample of the original audit rows, up to 150 accepted + 150 rejected (seed ROUTE_SEED),
    drawn without regard to whether the title route found them.
    Route B query ("surname_abs"): first-author surname (list position 0, ASCII-transliterated) AND the 3 most
    distinctive abstract words (lowest document frequency among all exported ICLR abstracts, then Zipf; alphabetic, >= 5 letters, LaTeX removed, and
    excluding every word that occurs in the stored title, so the route is title-free). If no candidate is
    accepted, a second query uses the surname and the next 2 distinctive words. Papers without a usable surname get an
    abstract-only query (4 words) and are flagged.
    Acceptance (title never used; see candidate_tier): A abstract Jaccard >= 0.45; B surname among arXiv authors
    and Jaccard >= 0.30; C surname match, Jaccard >= 0.15, v1 year in [year-2, year+1], >= 3-word query.
    All candidates (id, Jaccard, surname match, v1 date, tier) are stored so stricter rules can be re-applied.
    Version 1 is re-used from the original audit when route B lands on the same arXiv id; otherwise queried.
    Output: cache/arxiv_audit_route.jsonl (one JSON record per paper, resumable).

Phase 1b ("v1abs", always): for every original-audit paper whose arXiv v1 predates the ICLR decision, fetch the
    v1 record again (id_list=<id>v1) and cache its abstract (public arXiv metadata), so abstract-level LLM markers
    (RARE21/F24, F26, em dash) can be audited like title features. Output: cache/arxiv_audit_v1abs.jsonl.

Phase 2 ("enlarge", optional, --enlarge N_PER_CELL)
    A fresh stratified random sample of not-yet-audited papers (acceptance population, years 2023-26 x
    {accepted, rejected}, up to N_PER_CELL per cell, seed ENLARGE_SEED), queried with the ORIGINAL procedure
    (`arxiv_audit.find`, title route, same surname helper) so it can be pooled with the original audit. Queue
    order is randomly interleaved across cells so a partial run stays balanced. Output:
    cache/arxiv_audit_enlarge.jsonl (same record format as cache/arxiv_audit.jsonl, plus `phase` and the v1
    abstract `v1_summary`).

Rate limit: every request goes through one shared clock (>= 3.2 s between requests, as `arxiv_audit.query`).
Only one instance may run at a time (lock file). Network errors are recorded (`error`) instead of being read
as "not found"; errored rows are retried on the next run.

Run (background):
    cd research/titles/src && nohup env OMP_NUM_THREADS=1 /home/user/venv/bin/python -m analyses.audit_v2 \
        --enlarge 250 > ../outputs/snapshot/audit_v2.log 2>&1 &
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import arxiv_audit as A  # noqa: E402
from common import CACHE, load_submissions, read_table  # noqa: E402

ROUTE_PATH = CACHE / "arxiv_audit_route.jsonl"
ENLARGE_PATH = CACHE / "arxiv_audit_enlarge.jsonl"
V1ABS_PATH = CACHE / "arxiv_audit_v1abs.jsonl"
ORIG_PATH = CACHE / "arxiv_audit.jsonl"
LOCK = CACHE / ".audit_v2.lock"
ROUTE_SEED = 20261011
ENLARGE_SEED = 11
ROUTE_N_PER_DECISION = 150
ENLARGE_YEARS = (2023, 2024, 2025, 2026)
MIN_GAP_S = 3.2
JACC_ACCEPT = 0.45
JACC_ACCEPT_WITH_SURNAME = 0.30

_SUFFIX = {"jr", "sr", "ii", "iii", "iv", "phd", "md"}


# ------------------------------------------------------------------------------------------------
# helpers
# ------------------------------------------------------------------------------------------------
def surname_ascii(name_json: str | None) -> str:
    """Last name token, transliterated to ASCII (the original helper splits 'Mueller'-type names at accents)."""
    try:
        name = json.loads(name_json) if name_json else ""
    except (ValueError, TypeError):
        name = ""
    if not isinstance(name, str):
        return ""
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    parts = [p for p in re.findall(r"[A-Za-z][A-Za-z'\-]*", name) if p.lower().strip(".") not in _SUFFIX]
    if not parts:
        return ""
    last = parts[-1]
    if "-" in last:  # hyphenated surname: query the longest piece
        last = max(last.split("-"), key=len)
    last = last.replace("'", "")
    return last if len(last) >= 2 else ""


def _clean_abstract(text: str) -> str:
    text = re.sub(r"\$[^$]*\$", " ", text or "")
    text = re.sub(r"\\[A-Za-z]+", " ", text)
    return text


_DF: dict | None = None


def corpus_df() -> dict:
    """Document frequency of abstract words across all exported submissions (ICLR-specific rarity)."""
    global _DF
    if _DF is None:
        from collections import Counter
        cnt = Counter()
        for a in load_submissions().abstract.fillna(""):
            cnt.update(set(re.findall(r"\b[a-z]{5,}\b", _clean_abstract(a).lower())))
        _DF = dict(cnt)
    return _DF


def distinctive_words(abstract: str, title: str, k: int = 6) -> list[str]:
    """Abstract words ranked by rarity in the ICLR corpus (document frequency over all exported abstracts, then
    general-English Zipf frequency), excluding every word that occurs in the stored title."""
    from wordfreq import zipf_frequency
    df = corpus_df()
    title_w = set(re.findall(r"[a-z]+", (title or "").lower()))
    ws = set(w for w in re.findall(r"\b[a-z]{5,}\b", _clean_abstract(abstract).lower()))
    ws = [w for w in ws if w not in title_w and w not in A.STOP]
    ws.sort(key=lambda w: (df.get(w, 0), zipf_frequency(w, "en"), w))
    return ws[:k]


def query_checked(params: dict) -> tuple[list[dict], str | None]:
    """arxiv_audit.query with the same parser and shared rate-limit clock, but errors are reported."""
    wait = MIN_GAP_S - (time.time() - A._last_call[0])
    if wait > 0:
        time.sleep(wait)
    url = A.API + urllib.parse.urlencode(params)
    err = None
    body = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60, context=A.CTX) as r:
                body = r.read()
            err = None
            break
        except Exception as e:  # transient network/proxy errors: back off and retry
            err = f"{type(e).__name__}: {e}"[:200]
            A._last_call[0] = time.time()
            time.sleep(5 * 2 ** attempt)
    A._last_call[0] = time.time()
    if body is None:
        return [], err
    try:
        root = ET.fromstring(body)
    except ET.ParseError as e:
        return [], f"ParseError: {e}"[:200]
    out = []
    for e in root.findall("a:entry", A.NS):
        out.append({
            "id": e.findtext("a:id", default="", namespaces=A.NS).rsplit("/abs/", 1)[-1],
            "title": " ".join(e.findtext("a:title", default="", namespaces=A.NS).split()),
            "summary": " ".join(e.findtext("a:summary", default="", namespaces=A.NS).split()),
            "published": e.findtext("a:published", default="", namespaces=A.NS),
            "authors": [a.findtext("a:name", default="", namespaces=A.NS) for a in e.findall("a:author", A.NS)],
        })
    return out, None


def base_id(arxiv_id: str) -> str:
    return re.sub(r"v\d+$", "", arxiv_id or "")


def _acquire_lock():
    if LOCK.exists():
        try:
            pid = int(LOCK.read_text().strip())
            os.kill(pid, 0)
            raise SystemExit(f"another audit_v2 run is active (pid {pid}); refusing to start (rate limit)")
        except (ValueError, ProcessLookupError, PermissionError):
            pass
    LOCK.write_text(str(os.getpid()))


def _release_lock():
    try:
        if LOCK.exists() and LOCK.read_text().strip() == str(os.getpid()):
            LOCK.unlink()
    except OSError:
        pass


def _done_ids(path: Path) -> set[str]:
    """Ids already written without a network error (errored rows are retried)."""
    if not path.exists():
        return set()
    out = set()
    for line in path.open():
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if not r.get("error"):
            out.add(r["submission_id"])
    return out


def first_author_names() -> pd.Series:
    a = read_table("submission_authors")
    return a[a.source_list_position.eq(0)].set_index("submission_id").declared_name_json


# ------------------------------------------------------------------------------------------------
# Phase 1: route validation
# ------------------------------------------------------------------------------------------------
def read_jsonl(path: Path) -> pd.DataFrame:
    """Read a JSONL cache with the json module (pd.read_json parses arXiv ids such as 2309.02390 as floats)."""
    return pd.DataFrame([json.loads(l) for l in path.open() if l.strip()]) if path.exists() else pd.DataFrame()


def route_sample() -> pd.DataFrame:
    orig = read_jsonl(ORIG_PATH)
    rng = np.random.default_rng(ROUTE_SEED)
    parts = []
    for dec in ["accepted", "rejected"]:
        g = orig[orig.decision.eq(dec)].sort_values("submission_id")
        take = rng.choice(len(g), size=min(ROUTE_N_PER_DECISION, len(g)), replace=False)
        parts.append(g.iloc[np.sort(take)])
    smp = pd.concat(parts).reset_index(drop=True)
    s = load_submissions()[["submission_id", "title", "abstract"]]
    smp = smp.merge(s, on="submission_id", how="left", validate="1:1")
    names = first_author_names()
    smp["first_name_json"] = smp.submission_id.map(names)
    smp["surname_b"] = smp.first_name_json.map(surname_ascii)
    smp["surname_orig"] = smp.first_name_json.map(A.surname)
    # random processing order (a partial run is then a random subsample of the route sample)
    smp = smp.iloc[rng.permutation(len(smp))].reset_index(drop=True)
    return smp


def candidate_tier(c: dict, abstract: str, surname: str, year: int, n_words: int) -> tuple[str | None, float, bool]:
    """Title-free acceptance tiers (best first):
    A: abstract Jaccard >= 0.45;
    B: first-author surname among arXiv authors and Jaccard >= 0.30;
    C: surname match, Jaccard >= 0.15, arXiv v1 year within [year-2, year+1], and the hit came from a query with
       >= 3 distinctive abstract words (abstracts are often rewritten between arXiv and OpenReview).
    The strict rule (A or B) is re-applied offline as a sensitivity check."""
    jac = A.jaccard(c["summary"], abstract)
    sn_ok = bool(surname) and any(surname.lower() in
                                  unicodedata.normalize("NFKD", a).encode("ascii", "ignore").decode().lower()
                                  for a in c["authors"])
    pub_year = int(c["published"][:4]) if c.get("published", "")[:4].isdigit() else None
    if jac >= JACC_ACCEPT:
        return "A", jac, sn_ok
    if sn_ok and jac >= JACC_ACCEPT_WITH_SURNAME:
        return "B", jac, sn_ok
    if sn_ok and jac >= 0.15 and n_words >= 3 and pub_year is not None and year - 2 <= pub_year <= year + 1:
        return "C", jac, sn_ok
    return None, jac, sn_ok


def route_b(row) -> dict:
    words = distinctive_words(row.abstract, row.title, k=6)
    sn = row.surname_b
    queries = []
    if sn and len(words) >= 3:
        queries.append((f"au:{sn} AND " + " AND ".join(f"abs:{w}" for w in words[:3]), 3))
        if len(words) >= 5:  # fallback: fewer, different words (recall if the arXiv abstract was rewritten)
            queries.append((f"au:{sn} AND " + " AND ".join(f"abs:{w}" for w in words[3:5]), 2))
    elif len(words) >= 4:
        queries.append((" AND ".join(f"abs:{w}" for w in words[:4]), 4))
    rec = {"route": "surname_abs" if sn else "abs_only", "surname_b": sn, "words": words[:6], "queries": [],
           "found": False, "error": None}
    for q, nw in queries:
        cands, err = query_checked({"search_query": q, "max_results": 10})
        qrec = {"q": q, "n_cand": len(cands), "error": err, "cands": []}
        rec["queries"].append(qrec)
        if err:
            rec["error"] = err
            return rec
        best, best_key = None, None
        for c in cands:
            tier, jac, sn_ok = candidate_tier(c, row.abstract, sn, int(row.year), nw)
            qrec["cands"].append({"id": base_id(c["id"]), "jac": round(jac, 4), "sn_ok": sn_ok,
                                  "pub": c.get("published", "")[:10], "tier": tier})
            if tier is None:
                continue
            key = ("ABC".index(tier), -jac)
            if best_key is None or key < best_key:
                best, best_key = (c, tier, jac, sn_ok), key
        if best is not None:
            c, tier, jac, sn_ok = best
            rec.update(found=True, arxiv_id=base_id(c["id"]), latest_title=c["title"], abstract_jaccard=jac,
                       surname_ok=sn_ok, tier=tier, hit_query=len(rec["queries"]),
                       pub_date=c.get("published", "")[:10])
            return rec
    return rec


def run_route(limit: int | None = None):
    smp = route_sample()
    done = _done_ids(ROUTE_PATH)
    todo = smp[~smp.submission_id.isin(done)]
    if limit:
        todo = todo.head(limit)
    print(f"[route] sample {len(smp)} ({smp.decision.value_counts().to_dict()}); {len(done)} done; "
          f"{len(todo)} to query", flush=True)
    with ROUTE_PATH.open("a") as f:
        for i, row in enumerate(todo.itertuples(index=False)):
            rec = {"submission_id": row.submission_id, "year": int(row.year), "decision": row.decision,
                   "or_title": row.or_title, "orig_found": bool(row.found),
                   "orig_arxiv_id": base_id(row.arxiv_id) if isinstance(row.arxiv_id, str) else None,
                   "surname_orig": row.surname_orig, "phase": "route", "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
            rec.update(route_b(row))
            if rec["found"] and not rec.get("error"):
                if rec["orig_arxiv_id"] and rec["arxiv_id"] == rec["orig_arxiv_id"] and isinstance(row.v1_title, str):
                    rec.update(v1_title=row.v1_title, v1_date=row.v1_date, v1_source="reused_orig")
                else:
                    v1, err = query_checked({"id_list": rec["arxiv_id"] + "v1"})
                    if err:
                        rec["error"] = err
                    rec.update(v1_title=v1[0]["title"] if v1 else None,
                               v1_date=v1[0]["published"][:10] if v1 else None, v1_source="queried")
            rec["same_id"] = bool(rec["found"] and rec.get("arxiv_id") == rec["orig_arxiv_id"])
            f.write(json.dumps(rec) + "\n")
            f.flush()
            if i % 25 == 0:
                print(f"[route] {i}/{len(todo)} {time.strftime('%H:%M:%S')}", flush=True)
    print("[route] finished", flush=True)


# ------------------------------------------------------------------------------------------------
# Phase 1b: v1 abstracts of the original audit's pre-decision pairs
# ------------------------------------------------------------------------------------------------
def run_v1abs(limit: int | None = None):
    orig = read_jsonl(ORIG_PATH)
    orig = orig[orig.found.astype(bool) & orig.v1_date.notna()].copy()
    orig = orig[orig.v1_date.astype(str) < orig.year.map(A.DECISION_DATE)]
    orig = orig.sort_values("submission_id")
    orig = orig.iloc[np.random.default_rng(ROUTE_SEED + 1).permutation(len(orig))]
    done = _done_ids(V1ABS_PATH)
    todo = orig[~orig.submission_id.isin(done)]
    if limit:
        todo = todo.head(limit)
    print(f"[v1abs] {len(orig)} pre-decision pairs; {len(done)} done; {len(todo)} to query", flush=True)
    with V1ABS_PATH.open("a") as f:
        for i, row in enumerate(todo.itertuples(index=False)):
            v1, err = query_checked({"id_list": str(row.arxiv_id) + "v1"})
            rec = {"submission_id": row.submission_id, "year": int(row.year), "decision": row.decision,
                   "arxiv_id": row.arxiv_id, "error": err, "phase": "v1abs",
                   "v1_title": v1[0]["title"] if v1 else None, "v1_date": v1[0]["published"][:10] if v1 else None,
                   "v1_summary": v1[0]["summary"] if v1 else None, "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
            f.write(json.dumps(rec) + "\n")
            f.flush()
            if i % 25 == 0:
                print(f"[v1abs] {i}/{len(todo)} {time.strftime('%H:%M:%S')}", flush=True)
    print("[v1abs] finished", flush=True)


# ------------------------------------------------------------------------------------------------
# Phase 2: enlargement (original title route, fresh sample)
# ------------------------------------------------------------------------------------------------
def enlarge_sample(n_per_cell: int) -> pd.DataFrame:
    s = load_submissions()
    s = s[s.year.isin(ENLARGE_YEARS) & A_acceptance(s)]
    audited = set(read_jsonl(ORIG_PATH).submission_id)
    s = s[~s.submission_id.isin(audited)].sort_values("submission_id")
    rng = np.random.default_rng(ENLARGE_SEED)
    parts = []
    for (y, d), g in s.groupby(["year", "decision"]):
        take = rng.choice(len(g), size=min(n_per_cell, len(g)), replace=False)
        parts.append(g.iloc[np.sort(take)])
    smp = pd.concat(parts)
    names = first_author_names()
    smp = smp.assign(first_surname=smp.submission_id.map(names).map(A.surname))
    smp = smp.iloc[rng.permutation(len(smp))].reset_index(drop=True)
    return smp[["submission_id", "year", "decision", "title", "abstract", "first_surname"]]


def A_acceptance(s: pd.DataFrame) -> pd.Series:
    """Same frame as arxiv_audit.sample: ordinary submissions decided accepted/rejected."""
    return s.administrative_status.eq("ordinary_submission") & s.decision.isin(["accepted", "rejected"])


def _find_checked(row) -> tuple[dict | None, str | None]:
    """arxiv_audit.find (same attempts and acceptance rule) with error reporting."""
    tw = A.words(row.title)[:8]
    attempts = []
    if tw:
        attempts.append(" AND ".join(f"ti:{w}" for w in tw[:6]))
    if row.first_surname and tw:
        attempts.append(f"au:{row.first_surname} AND " + " AND ".join(f"ti:{w}" for w in tw[:3]))
    if row.first_surname:
        aw = sorted(set(A.words(row.abstract)), key=lambda w: (-len(w), w))[:3]
        if aw:
            attempts.append(f"au:{row.first_surname} AND " + " AND ".join(f"abs:{w}" for w in aw))
    for i, q in enumerate(attempts):
        cands, err = query_checked({"search_query": q, "max_results": 10})
        if err:
            return None, err
        best, best_score = None, 0.0
        for c in cands:
            score = max(A.jaccard(c["summary"], row.abstract), 0.0)
            tscore = A.jaccard(c["title"], row.title)
            surname_ok = bool(row.first_surname) and any(row.first_surname.lower() in a.lower() for a in c["authors"])
            ok = score >= 0.45 or (tscore >= 0.6 and surname_ok)
            if ok and score + tscore > best_score:
                best, best_score = c, score + tscore
        if best:
            best["abstract_jaccard"] = A.jaccard(best["summary"], row.abstract)
            best["attempt"] = i
            return best, None
    return None, None


def run_enlarge(n_per_cell: int, limit: int | None = None):
    smp = enlarge_sample(n_per_cell)
    done = _done_ids(ENLARGE_PATH)
    todo = smp[~smp.submission_id.isin(done)]
    if limit:
        todo = todo.head(limit)
    print(f"[enlarge] sample {len(smp)}; {len(done)} done; {len(todo)} to query", flush=True)
    with ENLARGE_PATH.open("a") as f:
        for i, row in enumerate(todo.itertuples(index=False)):
            rec = {"submission_id": row.submission_id, "year": int(row.year), "decision": row.decision,
                   "or_title": row.title, "found": False, "phase": "enlarge",
                   "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
            hit, err = _find_checked(row)
            if err:
                rec["error"] = err
            if hit:
                b = base_id(hit["id"])
                v1, err = query_checked({"id_list": b + "v1"})
                if err:
                    rec["error"] = err
                rec.update(found=True, arxiv_id=b, latest_title=hit["title"], abstract_jaccard=hit["abstract_jaccard"],
                           find_attempt=hit["attempt"],
                           v1_title=v1[0]["title"] if v1 else None, v1_date=v1[0]["published"][:10] if v1 else None,
                           v1_summary=v1[0]["summary"] if v1 else None)
            f.write(json.dumps(rec) + "\n")
            f.flush()
            if i % 25 == 0:
                print(f"[enlarge] {i}/{len(todo)} {time.strftime('%H:%M:%S')}", flush=True)
    print("[enlarge] finished", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--enlarge", type=int, default=0, help="phase 2: papers per year x decision cell (0 = skip)")
    ap.add_argument("--limit", type=int, default=None, help="process at most this many papers per phase (testing)")
    ap.add_argument("--skip-route", action="store_true")
    args = ap.parse_args()
    _acquire_lock()
    try:
        if not args.skip_route:
            run_route(args.limit)
            run_v1abs(args.limit)
        if args.enlarge:
            run_enlarge(args.enlarge, args.limit)
    finally:
        _release_lock()


if __name__ == "__main__":
    main()
