"""Embed every paper's "title [SEP] abstract" with SPECTER2 (base + proximity adapter, CLS vector).

A CPU-only run takes about 2 hours for the discovery split. Work is saved in 2,000-paper chunks,
so an interrupted run resumes where it stopped. Model revisions are pinned for reproducibility.

    python research/topics/embed_specter2.py
"""
from __future__ import annotations

import json
import time

import numpy as np
import pandas as pd
import torch
from adapters import AutoAdapterModel
from transformers import AutoTokenizer

from common import CACHE, embedded_corpus

BASE, BASE_SHA = "allenai/specter2_base", "3447645e1def9117997203454fa4495937bfbd83"
ADAPTER, ADAPTER_SHA = "allenai/specter2", "2081559630a80fc5851d8f798a05ba81e9468089"
CHUNK, BATCH, MAX_LENGTH = 2000, 32, 512


def load_model():
    tok = AutoTokenizer.from_pretrained(BASE, revision=BASE_SHA)
    model = AutoAdapterModel.from_pretrained(BASE, revision=BASE_SHA)
    # adapters passes `version` to the Hub download as the revision
    model.load_adapter(ADAPTER, source="hf", load_as="specter2", set_active=True, version=ADAPTER_SHA)
    model.set_active_adapters("specter2")
    assert "specter2" in str(model.active_adapters), model.active_adapters
    return tok, model.eval()


def paper_texts(frame: pd.DataFrame, sep: str) -> list[str]:
    return (frame.title.fillna("") + sep + frame.abstract.fillna("")).tolist()


def embed(tok, model, texts: list[str]) -> np.ndarray:
    vectors = []
    with torch.inference_mode():
        for b in range(0, len(texts), BATCH):
            enc = tok(texts[b:b + BATCH], padding=True, truncation=True, max_length=MAX_LENGTH,
                      return_tensors="pt", return_token_type_ids=False)
            vectors.append(model(**enc).last_hidden_state[:, 0, :].numpy())
    return np.vstack(vectors) if vectors else np.zeros((0, 768), dtype=np.float32)


def main() -> None:
    chunks = CACHE / "specter2_chunks"
    chunks.mkdir(parents=True, exist_ok=True)
    corpus = embedded_corpus()
    tok, model = load_model()
    texts = paper_texts(corpus, tok.sep_token)
    order = np.argsort([len(t) for t in texts], kind="stable")    # length-sorted batches waste less padding
    for start in range(0, len(order), CHUNK):
        path = chunks / f"chunk_{start:06d}.npy"
        if path.exists():
            continue
        idx, t0 = order[start:start + CHUNK], time.time()
        np.save(path, embed(tok, model, [texts[i] for i in idx]))
        np.save(chunks / f"idx_{start:06d}.npy", idx)
        print(f"papers {start}-{start + len(idx)} embedded in {time.time() - t0:.0f}s", flush=True)
    assemble(corpus)


def assemble(corpus: pd.DataFrame) -> None:
    chunks = CACHE / "specter2_chunks"
    idx = np.concatenate([np.load(p) for p in sorted(chunks.glob("idx_*.npy"))])
    vec = np.vstack([np.load(p) for p in sorted(chunks.glob("chunk_*.npy"))])
    if len(idx) != len(corpus) or len(np.unique(idx)) != len(corpus):
        raise RuntimeError(f"Embedding chunks cover {len(np.unique(idx))} of {len(corpus)} papers")
    out = np.zeros((len(corpus), vec.shape[1]), dtype=np.float32)
    out[idx] = vec
    np.save(CACHE / "specter2.npy", out)
    corpus[["submission_id"]].to_csv(CACHE / "specter2_ids.csv", index=False)
    (CACHE / "specter2_meta.json").write_text(json.dumps({
        "base": BASE, "base_revision": BASE_SHA, "adapter": ADAPTER, "adapter_revision": ADAPTER_SHA,
        "pooling": "CLS", "input": "title [SEP] abstract", "max_length": MAX_LENGTH,
        "papers": len(corpus), "dim": int(out.shape[1]), "torch": torch.__version__}, indent=2) + "\n")
    print(f"assembled {out.shape} -> {CACHE / 'specter2.npy'}", flush=True)


if __name__ == "__main__":
    main()
