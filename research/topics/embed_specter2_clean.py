"""Robustness input for PH5: SPECTER2 vectors with post-decision markers removed from the abstract.

Camera-ready abstracts of accepted papers often add a de-anonymised code link or a "code is available" sentence
(output/posthoc/ph5_fmwave/code_links.csv). This script removes URLs and code/data-availability sentences from every
abstract, re-embeds only the papers whose text changed (same model, revisions, input format and pooling as
embed_specter2.py), and writes a full matrix in the original row order:

    cache/specter2_clean.npy          (all papers; unchanged rows copied from specter2.npy)
    cache/specter2_clean_changed.csv  (submission_id of the re-embedded papers)
    cache/specter2_clean_meta.json    (counts, and a reproduction check: REPRO unchanged papers re-embedded by the same
                                       code and compared with specter2.npy)

Outcome-free: it reads only titles and abstracts. Resumable like embed_specter2.py: the papers are embedded in
length-sorted chunks under cache/specter2_clean_chunks/, and each call embeds at most --chunks of them and exits (one
long CPU process grows its memory with every new batch shape until it is killed), so run it until it says "done":

    until python research/topics/embed_specter2_clean.py --chunks 2 | grep -q '^done'; do :; done
"""
from __future__ import annotations

import argparse
import json
import re
import time

import numpy as np
import pandas as pd

URL = re.compile(r"(?:\\(?:href|url)\{[^}]*\}(?:\{[^}]*\})?|https?://\S+|www\.\S+|\S*github\.com\S*|\S+\.github\.io\S*"
                 r"|\S*4open\.science\S*)", re.I)
AVAILABLE = re.compile(r"\b(?:code|codes|data|models?|datasets?|implementations?|checkpoints?|weights|project page|website|demo"
                       r"|repository|source code)\b[^.]{0,60}?\b(?:is|are|will be|has been|have been|can be|shall be)\s+"
                       r"(?:made\s+)?(?:publicly\s+|freely\s+|openly\s+)?(?:available|released|open[- ]sourced|accessible|found)", re.I)
POINTER = re.compile(r"\b(?:code|codes|available|availability|release|released|github|project|page|webpage|website|demo|repo"
                     r"|repository|implementation|visit|url|link|homepage|open[- ]sourced?|found|accessed|hosted)\b", re.I)
LONG = 30   # a URL sentence whose remainder has more words and no POINTER word is content: only the URL goes
CHUNK, REPRO = 500, 64


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def clean(abstract: str) -> str:
    """Drop every availability sentence (present or future tense, so submitted versions lose theirs too) and every
    sentence that points to a URL (its remainder mentions code, a page, a release ..., or is at most LONG words), then
    remove any remaining URL; collapse whitespace."""
    kept = []
    for s in re.split(r"(?<=[.!?])\s+", abstract):
        rest = URL.sub(" ", s)
        if AVAILABLE.search(s) or (rest != s and (POINTER.search(rest) or len(rest.split()) <= LONG)):
            continue
        kept.append(s)
    return squash(URL.sub("", " ".join(kept)))


def main() -> None:
    from common import CACHE, embedded_corpus
    from embed_specter2 import embed, load_model, paper_texts
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunks", type=int, default=2, help="chunks to embed in this call")
    max_chunks = ap.parse_args().chunks
    corpus = embedded_corpus()
    ids = pd.read_csv(CACHE / "specter2_ids.csv").submission_id
    assert ids.equals(corpus.submission_id), "embedding rows and corpus are not aligned"
    original = corpus.abstract.fillna("")
    cleaned = original.map(clean)
    changed = np.flatnonzero(cleaned.to_numpy() != original.map(squash).to_numpy())   # whitespace alone is no change
    unchanged = np.setdiff1d(np.arange(len(corpus)), changed)
    repro = np.random.default_rng(20261017).choice(unchanged, REPRO, replace=False)
    rows = np.concatenate([changed, repro])          # the reproduction rows are embedded from their (unchanged) text
    chunks = CACHE / "specter2_clean_chunks"
    chunks.mkdir(exist_ok=True)
    todo = [s for s in range(0, len(rows), CHUNK) if not (chunks / f"chunk_{s:06d}.npy").exists()]
    if todo:
        tok, model = load_model()
        texts = paper_texts(corpus.assign(abstract=cleaned).iloc[rows], tok.sep_token)
        order = np.argsort([len(t) for t in texts], kind="stable")
        for start in todo[:max_chunks]:
            idx, t0 = order[start:start + CHUNK], time.time()
            np.save(chunks / f"chunk_{start:06d}.npy", embed(tok, model, [texts[i] for i in idx]))
            np.save(chunks / f"idx_{start:06d}.npy", idx)
            print(f"papers {start}-{start + len(idx)} of {len(rows)} embedded in {time.time() - t0:.0f}s", flush=True)
        if len(todo) > max_chunks:
            return
    idx = np.concatenate([np.load(p) for p in sorted(chunks.glob("idx_*.npy"))])
    vec = np.vstack([np.load(p) for p in sorted(chunks.glob("chunk_*.npy"))])
    assert len(idx) == len(rows) and len(np.unique(idx)) == len(rows), "chunks do not cover the papers"
    new = np.zeros((len(rows), vec.shape[1]), dtype=np.float32)
    new[idx] = vec
    base = np.load(CACHE / "specter2.npy")
    a, b = new[len(changed):], base[repro]
    cos = (a * b).sum(1) / np.linalg.norm(a, axis=1) / np.linalg.norm(b, axis=1)
    out = base.copy()
    out[changed] = new[:len(changed)]
    np.save(CACHE / "specter2_clean.npy", out)
    corpus.iloc[changed][["submission_id"]].to_csv(CACHE / "specter2_clean_changed.csv", index=False)
    meta = {"papers": int(len(corpus)), "changed": int(len(changed)),
            "changed_by_year": {int(y): int(n) for y, n in corpus.iloc[changed].year.value_counts().sort_index().items()},
            "reproduction_papers": REPRO, "reproduction_min_cos": float(cos.min()),
            "reproduction_mean_cos": float(cos.mean())}
    (CACHE / "specter2_clean_meta.json").write_text(json.dumps(meta, indent=1))
    print("done", json.dumps(meta), flush=True)


if __name__ == "__main__":
    main()
