"""Second encoder with 512-token context (robustness for abstract-level measures)."""
from __future__ import annotations

import sys

import numpy as np

from common import CACHE, load_submissions


def main(model_name="BAAI/bge-small-en-v1.5", threads=2):
    import torch
    from sentence_transformers import SentenceTransformer
    torch.set_num_threads(threads)
    s = load_submissions()
    model = SentenceTransformer(model_name, device="cpu")
    model.max_seq_length = 512
    tag = model_name.split("/")[-1]
    for field in ("title", "abstract"):
        out = CACHE / f"emb_{field}_{tag}.npy"
        if out.exists():
            continue
        emb = model.encode(s[field].fillna("").astype(str).tolist(), batch_size=32,
                           normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False)
        np.save(out, emb.astype(np.float16))
        print("saved", out, emb.shape, flush=True)


if __name__ == "__main__":
    main(*(sys.argv[1:2] or []))
