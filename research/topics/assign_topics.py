"""Place new papers (for example the held-out confirmation split) into the frozen topics.

Input: a CSV with submission_id, title, abstract. Nothing is refitted: papers are embedded with the
same pinned SPECTER2 model and assigned to the nearest saved fine topic, whose parents give the
middle and broad topics.

    python research/topics/assign_topics.py --input new_papers.csv --output new_assignments.csv
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from common import MIN_ABSTRACT_WORDS, OUTPUT


def assign(embeddings: np.ndarray, model_path=OUTPUT / "topic_model.npz") -> pd.DataFrame:
    m = np.load(model_path)
    z = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    z = (z - m["pca_mean"]) @ m["pca_components"].T
    z /= np.linalg.norm(z, axis=1, keepdims=True)
    sims = z @ m["fine_centroids"].T
    best = sims.argmax(axis=1)
    own = sims[np.arange(len(z)), best]
    sims[np.arange(len(z)), best] = -np.inf
    return pd.DataFrame({"fine": m["fine_codes"][best], "mid": m["mid_codes"][best], "coarse": m["coarse_codes"][best],
                         "fine_similarity": own.round(4), "fine_margin": (own - sims.max(axis=1)).round(4)})


def main() -> None:
    from embed_specter2 import embed, load_model, paper_texts
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    papers = pd.read_csv(a.input, keep_default_na=False, na_values=[r"\N"])
    papers = papers[papers.abstract.fillna("").str.split().str.len() >= MIN_ABSTRACT_WORDS].reset_index(drop=True)
    tok, model = load_model()
    out = pd.concat([papers[["submission_id"]], assign(embed(tok, model, paper_texts(papers, tok.sep_token)))], axis=1)
    out.to_csv(a.output, index=False)
    print(f"assigned {len(out)} papers -> {a.output}")


if __name__ == "__main__":
    main()
