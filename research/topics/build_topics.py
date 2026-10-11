"""Fit the nested topic layer from cached SPECTER2 embeddings.

The middle level (100 topics) is the analysis level, so it is fitted directly and the other levels
are built around it:
- middle: spherical k-means on unit-length PCA(128) embeddings, best of 3 seeds x 20 initialisations
- broad:  Ward merge of the 100 middle centroids into 20 groups (each middle topic has one parent)
- fine:   each middle topic split by k-means in proportion to its size (~200 in total); pieces under
          60 papers are folded into their nearest sibling, so fine topics stay analysable
Every paper goes to its nearest middle centroid, then to the nearest fine centroid inside that middle
topic; assign_topics.py applies the same rule to new papers. Codes are numbered by size.

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

PCA_DIM, SEEDS, N_INIT_MID, N_INIT_FINE, MIN_FINE, EXAMPLES = 128, (0, 1, 2), 20, 10, 60, 8


def allocate(sizes: np.ndarray, total: int) -> np.ndarray:
    """Split counts proportional to size (largest remainder), at least one per middle topic."""
    raw = sizes / sizes.sum() * total
    n = np.maximum(1, np.floor(raw)).astype(int)
    for i in np.argsort(-(raw - np.floor(raw)), kind="stable"):
        if n.sum() >= total:
            break
        n[i] += 1
    while n.sum() > total:
        n[np.argmax(n)] -= 1
    return n


def fit_hierarchy(z: np.ndarray, seeds: tuple[int, ...] = SEEDS) -> dict:
    k_mid = LEVEL_SIZES["mid"]
    km = min((KMeans(k_mid, n_init=N_INIT_MID, random_state=s, max_iter=300).fit(z) for s in seeds),
             key=lambda f: f.inertia_)
    mid_c = normalize(km.cluster_centers_)
    mid = (z @ mid_c.T).argmax(axis=1)
    if len(np.unique(mid)) != k_mid:
        raise RuntimeError("A middle topic became empty")
    coarse_of_mid = AgglomerativeClustering(n_clusters=LEVEL_SIZES["coarse"], linkage="ward").fit(mid_c).labels_
    splits = allocate(np.bincount(mid, minlength=k_mid), LEVEL_SIZES["fine"])
    fine = np.empty(len(z), dtype=int)
    fine_c, fine_parent = [], []
    for m in range(k_mid):
        idx = np.where(mid == m)[0]
        cc = mid_c[m:m + 1]
        if splits[m] > 1:
            cc = normalize(KMeans(splits[m], n_init=N_INIT_FINE, random_state=seeds[0], max_iter=300).fit(z[idx]).cluster_centers_)
        while True:                                   # fold the smallest piece into its siblings until all are big enough
            local = (z[idx] @ cc.T).argmax(axis=1)
            sizes = np.bincount(local, minlength=len(cc))
            j = int(np.argmin(sizes))
            if len(cc) == 1 or sizes[j] >= MIN_FINE:
                break
            cc = np.delete(cc, j, axis=0)
        fine[idx] = len(fine_c) + local
        fine_c.extend(cc)
        fine_parent.extend([m] * len(cc))
    return {"mid": mid, "coarse": coarse_of_mid[mid], "fine": fine, "mid_centroids": mid_c,
            "coarse_of_mid": coarse_of_mid, "fine_centroids": np.array(fine_c), "fine_parent": np.array(fine_parent)}


def keyword_signature(keyword_lists: pd.Series, global_counts: collections.Counter, n_total: int, k: int = 6) -> str:
    """Keywords most over-represented in a topic (lift-weighted share, at least 5 papers)."""
    counts = collections.Counter(w for kws in keyword_lists for w in set(kws))
    n = len(keyword_lists)
    score = {w: (v / n) * np.log((v / n) / (global_counts[w] / n_total)) for w, v in counts.items() if v >= 5}
    return " · ".join(w for w, _ in sorted(score.items(), key=lambda x: (-x[1], x[0]))[:k])


def codes(h: dict) -> dict:
    """Readable codes: broad by size; middle grouped under broad, then by size; fine grouped under middle."""
    mid_size = np.bincount(h["mid"])
    coarse_size = pd.Series(h["coarse"]).value_counts()
    coarse_code = {c: f"c{i + 1:02d}" for i, c in enumerate(coarse_size.index)}
    mid_order = sorted(range(len(mid_size)), key=lambda m: (coarse_code[h["coarse_of_mid"][m]], -mid_size[m], m))
    mid_code = {m: f"m{i + 1:03d}" for i, m in enumerate(mid_order)}
    fine_size = np.bincount(h["fine"])
    fine_order = sorted(range(len(fine_size)), key=lambda f: (mid_code[h["fine_parent"][f]], -fine_size[f], f))
    fine_code = {f: f"f{i + 1:03d}" for i, f in enumerate(fine_order)}
    return {"coarse": coarse_code, "mid": mid_code, "fine": fine_code, "mid_order": mid_order, "fine_order": fine_order}


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    corpus = embedded_corpus()
    emb, ids = load_embeddings()
    if not ids.equals(corpus.submission_id):
        raise RuntimeError("Embedding cache does not match the current corpus; rerun embed_specter2.py")
    from assign_topics import assign_projected, project
    emb = emb.astype(np.float64)
    pca = PCA(PCA_DIM, svd_solver="full").fit(normalize(emb))
    z = project(emb, {"pca_mean": pca.mean_, "pca_components": pca.components_})   # same formula as for new papers
    h = fit_hierarchy(z)
    c = codes(h)

    model = {"pca_mean": pca.mean_, "pca_components": pca.components_,       # float64 so reassignment is exact
             "mid_centroids": h["mid_centroids"][c["mid_order"]],
             "mid_codes": np.array([c["mid"][m] for m in c["mid_order"]]),
             "coarse_of_mid": np.array([c["coarse"][h["coarse_of_mid"][m]] for m in c["mid_order"]]),
             "fine_centroids": h["fine_centroids"][c["fine_order"]],
             "fine_codes": np.array([c["fine"][f] for f in c["fine_order"]]),
             "fine_parent": np.array([c["mid"][h["fine_parent"][f]] for f in c["fine_order"]])}
    np.savez_compressed(OUTPUT / "topic_model.npz", **model)
    assign = pd.concat([corpus[["submission_id", "year"]], assign_projected(z, model)], axis=1)
    expected = [c["fine"][f] for f in h["fine"]]
    if (assign.fine.values != np.array(expected)).any():
        raise RuntimeError("Saved model does not reproduce the fitted assignment")
    write_csv_gz(assign, OUTPUT / "topic_assignments.csv.gz")

    global_counts = collections.Counter(w for kws in corpus.keywords for w in set(kws))
    frame = corpus.assign(fine=assign.fine, mid=assign.mid, coarse=assign.coarse, sim=assign.mid_similarity)
    years = sorted(frame.year.unique())
    rows = []
    for level in ("coarse", "mid", "fine"):
        for code, g in frame.groupby(level):
            per_year = g.year.value_counts()
            rows.append({
                "level": level, "topic": code,
                "parent_mid": g.mid.iloc[0] if level == "fine" else "",
                "parent_coarse": g.coarse.iloc[0] if level != "coarse" else "",
                "papers": len(g), **{f"y{y}": int(per_year.get(y, 0)) for y in years},
                "mean_mid_similarity": round(float(g.sim.mean()), 4),
                "keyword_signature": keyword_signature(g.keywords, global_counts, len(frame)),
                "example_titles": " | ".join(g.sample(min(EXAMPLES, len(g)), random_state=0).title.str.slice(0, 120)),
            })
    catalog = pd.DataFrame(rows)
    catalog.to_csv(OUTPUT / "topic_catalog_auto.csv", index=False)
    for level in ("coarse", "mid", "fine"):
        cat = catalog[catalog.level == level]
        trackable = (cat[[f"y{y}" for y in years]] >= 30).sum(axis=1) >= 3
        print(f"{level:6s}: {len(cat)} topics | papers min {cat.papers.min()}, median {int(cat.papers.median())}, max {cat.papers.max()} | "
              f"{trackable.sum()} with >=30 papers in >=3 years ({cat.papers[trackable].sum() / len(frame):.0%} of papers)")
    print(json.dumps({"papers": len(frame), "pca_explained_variance": round(float(pca.explained_variance_ratio_.sum()), 3)}))


if __name__ == "__main__":
    main()
