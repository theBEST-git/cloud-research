"""SPECTER2 vectors for the released former-confirmation papers, with the model, revisions, input format
(title [SEP] abstract), pooling and length limit of embed_specter2.py. Outcome-free (released.embedded_released).

    cache/specter2_released.npy       (released papers with text, row order of released.embedded_released())
    cache/specter2_released_ids.csv
    cache/specter2_released_meta.json (model, revisions, sha256 of the two files, reproduction check)

Resumable in chunks like embed_specter2_clean.py (one long CPU process grows its memory with every batch shape), so
run it until it says "done":

    until python research/topics/embed_specter2_released.py --chunks 3 | grep -q '^done'; do :; done
    python research/topics/embed_specter2_released.py --meta      (the check and meta for an existing cache only)

Provenance (as embed_specter2_clean.py's meta): after assembly, REPRO = 64 random discovery papers (seed REPRO_SEED)
are re-embedded through this code path (load_model, paper_texts, embed in this environment) and compared with
cache/specter2.npy, and REPRO_RELEASED = 32 random released papers with cache/specter2_released.npy; the meta is written
only if every cosine is >= MIN_COS (the two caches are then one embedding space). Run with ICLR_CORPUS unset.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time

import numpy as np
import pandas as pd

CHUNK = 500
REPRO, REPRO_RELEASED, REPRO_SEED, MIN_COS = 64, 32, 20261018, 0.9999


def sha256(path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cosines(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a * b).sum(1) / np.linalg.norm(a, axis=1) / np.linalg.norm(b, axis=1)


def write_meta(tok=None, model=None) -> dict:
    """Re-embed the reproduction papers, require min cosine >= MIN_COS against both caches, write the meta."""
    import torch
    from common import CACHE, CORPUS, embedded_corpus
    from embed_specter2 import ADAPTER, ADAPTER_SHA, BASE, BASE_SHA, MAX_LENGTH, embed, load_model, paper_texts
    from released import embedded_released
    if CORPUS != "discovery":
        raise SystemExit("run with ICLR_CORPUS unset (the reproduction papers are discovery papers)")
    if tok is None:
        tok, model = load_model()
    disc, rel = embedded_corpus(), embedded_released()
    if not pd.read_csv(CACHE / "specter2_ids.csv").submission_id.equals(disc.submission_id) or \
            not pd.read_csv(CACHE / "specter2_released_ids.csv").submission_id.equals(rel.submission_id):
        raise SystemExit("an embedding id list does not match its corpus")
    rng = np.random.default_rng(REPRO_SEED)
    rows_d = np.sort(rng.choice(len(disc), REPRO, replace=False))
    rows_r = np.sort(rng.choice(len(rel), REPRO_RELEASED, replace=False))
    released = np.load(CACHE / "specter2_released.npy")
    cd = cosines(embed(tok, model, paper_texts(disc.iloc[rows_d], tok.sep_token)), np.load(CACHE / "specter2.npy")[rows_d])
    cr = cosines(embed(tok, model, paper_texts(rel.iloc[rows_r], tok.sep_token)), released[rows_r])
    meta = {"base": BASE, "base_revision": BASE_SHA, "adapter": ADAPTER, "adapter_revision": ADAPTER_SHA,
            "pooling": "CLS", "input": "title [SEP] abstract", "max_length": MAX_LENGTH, "papers": int(len(rel)),
            "dim": int(released.shape[1]), "torch": torch.__version__,
            "sha256": {"specter2_released.npy": sha256(CACHE / "specter2_released.npy"),
                       "specter2_released_ids.csv": sha256(CACHE / "specter2_released_ids.csv"),
                       "specter2.npy": sha256(CACHE / "specter2.npy")},
            "reproduction_seed": REPRO_SEED, "min_cos_required": MIN_COS,
            "reproduction_discovery_papers": REPRO, "reproduction_discovery_min_cos": float(cd.min()),
            "reproduction_discovery_mean_cos": float(cd.mean()),
            "reproduction_released_papers": REPRO_RELEASED, "reproduction_released_min_cos": float(cr.min()),
            "reproduction_released_mean_cos": float(cr.mean())}
    if min(cd.min(), cr.min()) < MIN_COS:
        raise SystemExit(f"reproduction failed (min cosine {min(cd.min(), cr.min()):.6f} < {MIN_COS}): "
                         + json.dumps(meta))
    (CACHE / "specter2_released_meta.json").write_text(json.dumps(meta, indent=1) + "\n")
    return meta


def main() -> None:
    from common import CACHE
    from embed_specter2 import embed, load_model, paper_texts
    from released import embedded_released
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunks", type=int, default=3, help="chunks to embed in this call")
    ap.add_argument("--meta", action="store_true", help="only the reproduction check and meta of an existing cache")
    a = ap.parse_args()
    if a.meta:
        print("meta", json.dumps(write_meta()), flush=True)
        return
    max_chunks = a.chunks
    corpus = embedded_released()
    chunks = CACHE / "specter2_released_chunks"
    chunks.mkdir(exist_ok=True)
    todo = [s for s in range(0, len(corpus), CHUNK) if not (chunks / f"chunk_{s:06d}.npy").exists()]
    tok = model = None
    if todo:
        tok, model = load_model()
        texts = paper_texts(corpus, tok.sep_token)
        order = np.argsort([len(t) for t in texts], kind="stable")
        for start in todo[:max_chunks]:
            idx, t0 = order[start:start + CHUNK], time.time()
            np.save(chunks / f"chunk_{start:06d}.npy", embed(tok, model, [texts[i] for i in idx]))
            np.save(chunks / f"idx_{start:06d}.npy", idx)
            print(f"papers {start}-{start + len(idx)} of {len(corpus)} embedded in {time.time() - t0:.0f}s", flush=True)
        if len(todo) > max_chunks:
            return
    idx = np.concatenate([np.load(p) for p in sorted(chunks.glob("idx_*.npy"))])
    vec = np.vstack([np.load(p) for p in sorted(chunks.glob("chunk_*.npy"))])
    assert len(idx) == len(corpus) and len(np.unique(idx)) == len(corpus), "chunks do not cover the papers"
    out = np.zeros((len(corpus), vec.shape[1]), dtype=np.float32)
    out[idx] = vec
    np.save(CACHE / "specter2_released.npy", out)
    corpus[["submission_id"]].to_csv(CACHE / "specter2_released_ids.csv", index=False)
    write_meta(tok, model)
    print(f"done {len(corpus)} papers", flush=True)


if __name__ == "__main__":
    main()
