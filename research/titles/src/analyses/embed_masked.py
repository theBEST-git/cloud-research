"""WP2: bge-small-en-v1.5 (max_seq_length 512) embeddings of NAME-MASKED abstracts, universe 2018-2026 (D1 R3).

Masking = features_v2.mask_abstract (title lead + CamelCase/ALLCAPS tokens -> '[NAME]').
Long-running (about 1-2 CPU hours with 2 torch threads); resumable via per-chunk parts. Launch with

    cd research/titles/src && nohup env OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.embed_masked \
        > ../outputs/topics/embed_masked.log 2>&1 &

Outputs (outputs/topics/): emb_masked_bge.npy (float16, L2-normalised, rows aligned to emb_masked_bge_ids.npy),
emb_masked_bge_ids.npy, masked_abstracts.parquet (submission_id, year, masked text, hit counts), embed_masked.done.
"""
from __future__ import annotations

import hashlib
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

_SRC = Path(__file__).resolve().parents[1]
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

import features as F  # noqa: E402
from analyses._core import MASKED_EMB_PATH, MASKED_IDS_PATH, TOPIC_DIR, load_universe  # noqa: E402
from analyses.features_v2 import mask_abstract  # noqa: E402

MODEL = "BAAI/bge-small-en-v1.5"
MIN_YEAR = 2018
CHUNK = 1024
PARTS = TOPIC_DIR / "_emb_masked_parts"


def masked_table() -> pd.DataFrame:
    u = load_universe(["submission_id", "year", "title_nfkc", "abstract"])
    u = u[u.year >= MIN_YEAR].reset_index(drop=True)
    leads = [F.lead_segment(t)[0] for t in u.title_nfkc]
    m = [mask_abstract(a, l, return_counts=True) for a, l in zip(u.abstract, leads)]
    return pd.DataFrame({"submission_id": u.submission_id, "year": u.year, "lead": [l or "" for l in leads],
                         "masked": [x[0] for x in m], "n_lead_hits": [x[1] for x in m],
                         "n_token_hits": [x[2] for x in m]})


def main(threads: int = 2):
    import torch
    from sentence_transformers import SentenceTransformer
    torch.set_num_threads(threads)
    TOPIC_DIR.mkdir(parents=True, exist_ok=True)
    PARTS.mkdir(parents=True, exist_ok=True)
    mt_path = TOPIC_DIR / "masked_abstracts.parquet"
    mt = masked_table()
    digest = hashlib.sha256("\n".join(mt.masked).encode()).hexdigest()
    old = pd.read_parquet(mt_path) if mt_path.exists() else None
    if old is not None and not old.masked.equals(mt.masked):
        print("masked texts changed; clearing old parts", flush=True)
        for p in PARTS.glob("part_*.npy"):
            p.unlink()
    mt.to_parquet(mt_path, index=False)
    (TOPIC_DIR / "masked_abstracts.sha256").write_text(digest + "\n")
    print(f"{len(mt)} abstracts ({MIN_YEAR}-2026); masked-text sha256 {digest}", flush=True)
    print("mean lead hits", mt.n_lead_hits.mean().round(3), "mean token hits", mt.n_token_hits.mean().round(2), flush=True)

    model = SentenceTransformer(MODEL, device="cpu")
    model.max_seq_length = 512
    # Sort by length to cut padding; parts are stored in sorted order and un-permuted at the end.
    order = np.argsort(mt.masked.str.len().to_numpy(), kind="stable")
    texts = mt.masked.to_numpy()[order]
    n_chunks = int(np.ceil(len(texts) / CHUNK))
    t0 = time.time()
    for c in range(n_chunks):
        p = PARTS / f"part_{c:04d}.npy"
        if p.exists():
            continue
        batch = texts[c * CHUNK:(c + 1) * CHUNK].tolist()
        emb = model.encode(batch, batch_size=32, normalize_embeddings=True, convert_to_numpy=True,
                           show_progress_bar=False)
        np.save(p, emb.astype(np.float16))
        el = time.time() - t0
        print(f"chunk {c + 1}/{n_chunks} done, elapsed {el / 60:.1f} min", flush=True)
    E_sorted = np.concatenate([np.load(PARTS / f"part_{c:04d}.npy") for c in range(n_chunks)])
    E = np.empty_like(E_sorted)
    E[order] = E_sorted
    np.save(MASKED_EMB_PATH, E)
    np.save(MASKED_IDS_PATH, mt.submission_id.to_numpy(dtype=str))
    (TOPIC_DIR / "embed_masked.done").write_text(f"{len(E)} rows; model {MODEL}; max_seq_length 512; {digest}\n")
    print("saved", MASKED_EMB_PATH, E.shape, flush=True)


if __name__ == "__main__":
    main(*(int(x) for x in sys.argv[1:2]))
