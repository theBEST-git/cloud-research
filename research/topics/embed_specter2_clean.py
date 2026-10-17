"""Robustness input for PH5: SPECTER2 vectors with post-decision markers removed from the abstract.

Camera-ready abstracts of accepted papers often add a de-anonymised code link or a "code is available" sentence
(output/posthoc/ph5_fmwave/code_links.csv). This script removes URLs and code/data-availability sentences from every
abstract, re-embeds only the papers whose text changed (same model, revisions, input format and pooling as
embed_specter2.py), and writes a full matrix in the original row order:

    cache/specter2_clean.npy          (all papers; unchanged rows copied from specter2.npy)
    cache/specter2_clean_changed.csv  (submission_id of the re-embedded papers)

Outcome-free: it reads only titles and abstracts.

    python research/topics/embed_specter2_clean.py
"""
from __future__ import annotations

import re
import time

import numpy as np
import pandas as pd

URL = re.compile(r"(?:https?://\S+|www\.\S+|\S*github\.com\S*|\S+\.github\.io\S*)", re.I)
AVAILABLE = re.compile(r"(?:code|data|models?|datasets?|implementation|checkpoints?|project page|demo)[^.]{0,60}"
                       r"(?:is|are) (?:publicly )?(?:available|released|open[- ]sourced)", re.I)


def clean(abstract: str) -> str:
    """Drop every sentence that states availability, then any remaining URL; collapse whitespace."""
    sentences = re.split(r"(?<=[.!?])\s+", abstract)
    kept = [s for s in sentences if not AVAILABLE.search(s)]
    return re.sub(r"\s+", " ", URL.sub("", " ".join(kept))).strip()


def main() -> None:
    from common import CACHE, embedded_corpus
    from embed_specter2 import embed, load_model, paper_texts
    corpus = embedded_corpus()
    ids = pd.read_csv(CACHE / "specter2_ids.csv").submission_id
    assert ids.equals(corpus.submission_id), "embedding rows and corpus are not aligned"
    cleaned = corpus.abstract.fillna("").map(clean)
    changed = np.flatnonzero(cleaned.to_numpy() != corpus.abstract.fillna("").to_numpy())
    tok, model = load_model()
    texts = paper_texts(corpus.assign(abstract=cleaned).iloc[changed], tok.sep_token)
    order = np.argsort([len(t) for t in texts], kind="stable")
    t0 = time.time()
    vec = embed(tok, model, [texts[i] for i in order])
    out = np.load(CACHE / "specter2.npy").copy()
    out[changed[order]] = vec
    np.save(CACHE / "specter2_clean.npy", out)
    corpus.iloc[changed][["submission_id"]].to_csv(CACHE / "specter2_clean_changed.csv", index=False)
    print(f"re-embedded {len(changed)} papers in {time.time() - t0:.0f}s -> {CACHE / 'specter2_clean.npy'}", flush=True)


if __name__ == "__main__":
    main()
