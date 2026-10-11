"""Fit the nested topic layer from cached SPECTER2 embeddings.

Embeddings -> unit length -> PCA(128) -> unit length -> k-means (200 fine topics, best of 3 seeds x 5 inits)
-> Ward merge of the fine centroids into 100 middle and 20 broad topics, so the levels nest exactly.
Topic codes are numbered by size so they are readable and stable across identical runs.

    python research/topics/build_topics.py
"""
from __future__ import annotations

import collections
import json

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize

from common import LEVEL_SIZES, OUTPUT, embedded_corpus, load_embeddings, write_csv_gz

PCA_DIM, SEEDS, N_INIT, EXAMPLES = 128, (0, 1, 2), 5, 8


def project(emb: np.ndarray, mean: np.ndarray, components: np.ndarray) -> np.ndarray:
    return normalize((normalize(emb) - mean) @ components.T)


def keyword_signature(keyword_lists: pd.Series, global_counts: collections.Counter, n_total: int, k: int = 6) -> str:
    """Keywords most over-represented in a topic (lift-weighted share, at least 5 papers)."""
    counts = collections.Counter(w for kws in keyword_lists for w in set(kws))
    n = len(keyword_lists)
    score = {w: (v / n) * np.log((v / n) / (global_counts[w] / n_total)) for w, v in counts.items() if v >= 5}
    return " · ".join(w for w, _ in sorted(score.items(), key=lambda x: (-x[1], x[0]))[:k])


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    corpus = embedded_corpus()
    emb, ids = load_embeddings()
    if not ids.equals(corpus.submission_id):
        raise RuntimeError("Embedding cache does not match the current corpus; rerun embed_specter2.py")

    pca = PCA(PCA_DIM, svd_solver="full").fit(normalize(emb))
    z = project(emb, pca.mean_, pca.components_)
    km = min((KMeans(LEVEL_SIZES["fine"], n_init=N_INIT, random_state=s, max_iter=300).fit(z) for s in SEEDS),
             key=lambda f: f.inertia_)
    centroids = normalize(km.cluster_centers_)
    # Final step of spherical k-means: nearest unit centroid. assign_topics.py uses the same rule for new papers.
    raw_fine = (z @ centroids.T).argmax(axis=1)
    if len(np.unique(raw_fine)) != LEVEL_SIZES["fine"]:
        raise RuntimeError("A fine topic became empty after reassignment")
    merged = {lvl: AgglomerativeClustering(n_clusters=LEVEL_SIZES[lvl], linkage="ward").fit(centroids).labels_
              for lvl in ("mid", "coarse")}
    # Both cuts come from the same Ward merge sequence, so every middle topic sits inside one broad topic.
    if (pd.DataFrame(merged).groupby("mid").coarse.nunique() > 1).any():
        raise RuntimeError("Middle topics do not nest inside broad topics")

    # Readable codes: broad topics by size; middle and fine topics grouped under their parent, then by size.
    size = pd.Series(raw_fine).value_counts()
    coarse_size = pd.Series(merged["coarse"][raw_fine]).value_counts()
    coarse_code = {c: f"c{i + 1:02d}" for i, c in enumerate(coarse_size.index)}
    mid_size = pd.Series(merged["mid"][raw_fine]).value_counts()
    mid_order = sorted(mid_size.index, key=lambda m: (coarse_code[merged["coarse"][np.argmax(merged["mid"] == m)]], -mid_size[m], m))
    mid_code = {m: f"m{i + 1:03d}" for i, m in enumerate(mid_order)}
    fine_order = sorted(size.index, key=lambda f: (mid_code[merged["mid"][f]], -size[f], f))
    fine_code = {f: f"f{i + 1:03d}" for i, f in enumerate(fine_order)}

    sims = z @ centroids.T
    own = sims[np.arange(len(z)), raw_fine]
    sims[np.arange(len(z)), raw_fine] = -np.inf
    assign = pd.DataFrame({
        "submission_id": corpus.submission_id, "year": corpus.year,
        "fine": [fine_code[f] for f in raw_fine],
        "mid": [mid_code[merged["mid"][f]] for f in raw_fine],
        "coarse": [coarse_code[merged["coarse"][f]] for f in raw_fine],
        "fine_similarity": own.round(4), "fine_margin": (own - sims.max(axis=1)).round(4),
    })
    write_csv_gz(assign, OUTPUT / "topic_assignments.csv.gz")

    # Model needed to place new (e.g. held-out confirmation) papers into the same topics.
    order = [f for f in sorted(fine_code, key=fine_code.get)]
    np.savez_compressed(OUTPUT / "topic_model.npz", pca_mean=pca.mean_.astype(np.float32),
                        pca_components=pca.components_.astype(np.float32),
                        fine_centroids=centroids[order].astype(np.float32),
                        fine_codes=np.array([fine_code[f] for f in order]),
                        mid_codes=np.array([mid_code[merged["mid"][f]] for f in order]),
                        coarse_codes=np.array([coarse_code[merged["coarse"][f]] for f in order]))

    global_counts = collections.Counter(w for kws in corpus.keywords for w in set(kws))
    rows, frame = [], corpus.assign(fine=assign.fine, mid=assign.mid, coarse=assign.coarse, sim=assign.fine_similarity)
    years = sorted(frame.year.unique())
    for level in ("coarse", "mid", "fine"):
        for code, g in frame.groupby(level):
            per_year = g.year.value_counts()
            rows.append({
                "level": level, "topic": code,
                "parent_mid": g.mid.iloc[0] if level == "fine" else "",
                "parent_coarse": g.coarse.iloc[0] if level != "coarse" else "",
                "papers": len(g), **{f"y{y}": int(per_year.get(y, 0)) for y in years},
                "mean_fine_similarity": round(float(g.sim.mean()), 4),
                "keyword_signature": keyword_signature(g.keywords, global_counts, len(frame)),
                "example_titles": " | ".join(g.sample(min(EXAMPLES, len(g)), random_state=0).title.str.slice(0, 120)),
            })
    catalog = pd.DataFrame(rows)
    catalog.to_csv(OUTPUT / "topic_catalog_auto.csv", index=False)
    for level in ("coarse", "mid", "fine"):
        c = catalog[catalog.level == level]
        yt = c[[f"y{y}" for y in years]]
        trackable = (yt >= 30).sum(axis=1) >= 3
        print(f"{level:6s}: {len(c)} topics | papers min {c.papers.min()}, median {int(c.papers.median())}, max {c.papers.max()} | "
              f"{trackable.sum()} with >=30 papers in >=3 years ({c.papers[trackable].sum() / len(frame):.0%} of papers)")
    print(json.dumps({"papers": len(frame), "pca_explained_variance": round(float(pca.explained_variance_ratio_.sum()), 3)}))


if __name__ == "__main__":
    main()
