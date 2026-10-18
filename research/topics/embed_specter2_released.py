"""SPECTER2 vectors for the released former-confirmation papers, with the model, revisions, input format
(title [SEP] abstract), pooling and length limit of embed_specter2.py. Outcome-free (released.embedded_released).

    cache/specter2_released.npy       (released papers with text, row order of released.embedded_released())
    cache/specter2_released_ids.csv

Resumable in chunks like embed_specter2_clean.py (one long CPU process grows its memory with every batch shape), so
run it until it says "done":

    until python research/topics/embed_specter2_released.py --chunks 3 | grep -q '^done'; do :; done
"""
from __future__ import annotations

import argparse
import time

import numpy as np

CHUNK = 500


def main() -> None:
    from common import CACHE
    from embed_specter2 import embed, load_model, paper_texts
    from released import embedded_released
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunks", type=int, default=3, help="chunks to embed in this call")
    max_chunks = ap.parse_args().chunks
    corpus = embedded_released()
    chunks = CACHE / "specter2_released_chunks"
    chunks.mkdir(exist_ok=True)
    todo = [s for s in range(0, len(corpus), CHUNK) if not (chunks / f"chunk_{s:06d}.npy").exists()]
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
    print(f"done {len(corpus)} papers", flush=True)


if __name__ == "__main__":
    main()
