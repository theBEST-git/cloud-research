"""Encode titles and abstracts with a sentence-transformer; cache as float16 .npy aligned to submissions order."""
from __future__ import annotations

import argparse
import os
from pathlib import Path

import numpy as np

from common import CACHE, load_submissions


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    ap.add_argument("--fields", nargs="+", default=["title", "abstract"])
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--batch", type=int, default=128)
    args = ap.parse_args()
    import torch
    from sentence_transformers import SentenceTransformer
    torch.set_num_threads(args.threads)
    s = load_submissions()
    model = SentenceTransformer(args.model, device="cpu")
    tag = args.model.split("/")[-1]
    CACHE.mkdir(parents=True, exist_ok=True)
    np.save(CACHE / "embedding_ids.npy", s["submission_id"].to_numpy(dtype=str))
    for field in args.fields:
        out = CACHE / f"emb_{field}_{tag}.npy"
        if out.exists():
            print("exists", out)
            continue
        texts = s[field].fillna("").astype(str).tolist()
        emb = model.encode(texts, batch_size=args.batch, show_progress_bar=False,
                           normalize_embeddings=True, convert_to_numpy=True)
        np.save(out, emb.astype(np.float16))
        print("saved", out, emb.shape, flush=True)


if __name__ == "__main__":
    main()
