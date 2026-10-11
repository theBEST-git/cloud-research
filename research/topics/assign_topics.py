"""Place papers into the frozen topics (also used by build_topics.py for the discovery split).

Rule: nearest middle centroid, then the nearest fine centroid inside that middle topic; the broad topic
is the middle topic's parent. Nothing is refitted, so held-out papers (e.g. the confirmation split) get
topics comparable with the discovery papers.

    python research/topics/assign_topics.py --input new_papers.csv --output new_assignments.csv
    (input columns: submission_id, title, abstract)
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from common import MIN_ABSTRACT_WORDS, OUTPUT


def project(embeddings: np.ndarray, model) -> np.ndarray:
    x = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    z = (x - model["pca_mean"]) @ model["pca_components"].T
    return z / np.linalg.norm(z, axis=1, keepdims=True)


def assign_projected(z: np.ndarray, model) -> pd.DataFrame:
    rows = np.arange(len(z))
    ms = z @ model["mid_centroids"].T
    mi = ms.argmax(axis=1)
    own = ms[rows, mi].copy()
    ms[rows, mi] = -np.inf
    mid_codes = model["mid_codes"][mi]
    fs = z @ model["fine_centroids"].T
    fs[model["fine_parent"][None, :] != mid_codes[:, None]] = -np.inf     # only fine topics inside the chosen middle topic
    fi = fs.argmax(axis=1)
    return pd.DataFrame({"fine": model["fine_codes"][fi], "mid": mid_codes, "coarse": model["coarse_of_mid"][mi],
                         "mid_similarity": own.round(4), "mid_margin": (own - ms.max(axis=1)).round(4),
                         "fine_similarity": fs[rows, fi].round(4)})


def assign(embeddings: np.ndarray, model_path=OUTPUT / "topic_model.npz") -> pd.DataFrame:
    model = np.load(model_path)
    return assign_projected(project(embeddings.astype(np.float64), model), model)


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
