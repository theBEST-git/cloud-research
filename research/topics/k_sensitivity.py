"""Sensitivity of the middle level to its number of topics k (outcome-blind).

The middle level (k = 100) is the analysis level. Its k was a design choice, not tuned, so this script refits it
with k in K_VALUES using the same procedure as build_topics.py (spherical k-means on unit-length PCA(128)
SPECTER2 embeddings, best of 3 seeds x 20 initialisations, nearest-centroid assignment) and reports per k:
- quality: the metrics of evaluate_topics.py, plus stability (ARI against refits with other seeds)
- correspondence with the k = 100 topics: NMI, and how cleanly topics nest (for each topic of the finer solution,
  the share of its papers inside its main topic of the coarser one)
- label-free fashion measures that later analyses rely on:
  * effective number of topics per year (exp of the entropy of topic shares), divided by k
  * emerging topics: share in 2024-2026 at least 3x the share in 2017-2020; their count / k and the share of
    2024-2026 papers they hold
The k = 100 run with seeds (0, 1, 2) must reproduce the published middle topics exactly.
Writes output/k_sensitivity.json and output/k_sensitivity_assignments.csv.gz (middle topic per paper and k).

    python research/topics/k_sensitivity.py
"""
from __future__ import annotations

import collections
import json

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from sklearn.preprocessing import normalize

from assign_topics import project
from build_topics import N_INIT_MID, PCA_DIM, SEEDS
from common import OUTPUT, embedded_corpus, load_embeddings, write_csv_gz
from evaluate_topics import SYNONYMS, metrics

K_VALUES = (50, 75, 100, 150, 200)
REFIT_SEEDS = [(10, 11, 12), (20, 21, 22)]
EARLY, LATE, EMERGING_RATIO = (2017, 2020), (2024, 2026), 3.0


def fit_mid(z: np.ndarray, k: int, seeds: tuple[int, ...]) -> np.ndarray:
    km = min((KMeans(k, n_init=N_INIT_MID, random_state=s, max_iter=300).fit(z) for s in seeds), key=lambda f: f.inertia_)
    return (z @ normalize(km.cluster_centers_).T).argmax(axis=1)


def nesting(fine: np.ndarray, coarse: np.ndarray) -> float:
    """Paper-weighted share of each finer topic that falls inside its main coarser topic (1 = perfectly nested)."""
    table = pd.crosstab(fine, coarse).values
    return float(table.max(axis=1).sum() / table.sum())


def fashion(labels: np.ndarray, years: np.ndarray, k: int) -> dict:
    t = pd.crosstab(labels, years)
    shares = t / t.sum(axis=0)
    eff = {int(y): round(float(np.exp(-(shares[y][shares[y] > 0] * np.log(shares[y][shares[y] > 0])).sum()) / k), 3)
           for y in shares.columns}
    early = t.loc[:, EARLY[0]:EARLY[1]].sum(axis=1)
    late = t.loc[:, LATE[0]:LATE[1]].sum(axis=1)
    ratio = (late / late.sum()) / ((early + 0.5) / early.sum())
    emerging = ratio >= EMERGING_RATIO
    return {"effective_topics_over_k_by_year": eff,
            "emerging_topics_over_k": round(float(emerging.mean()), 3),
            "late_paper_share_in_emerging_topics": round(float(late[emerging].sum() / late.sum()), 3)}


def main() -> None:
    corpus = embedded_corpus()
    emb, ids = load_embeddings()
    if not ids.equals(corpus.submission_id):
        raise RuntimeError("Embedding cache does not match the current corpus; rerun embed_specter2.py")
    published = pd.read_csv(OUTPUT / "topic_assignments.csv.gz")
    if not published.submission_id.equals(corpus.submission_id):
        raise RuntimeError("Assignments are out of date; rerun build_topics.py")
    emb = emb.astype(np.float64)
    pca = PCA(PCA_DIM, svd_solver="full").fit(normalize(emb))
    z = project(emb, {"pca_mean": pca.mean_, "pca_components": pca.components_})
    kw_count = collections.Counter(w for kws in corpus.keywords for w in set(kws))
    pairs = [p for p in SYNONYMS if kw_count[p[0]] >= 30 and kw_count[p[1]] >= 30]
    years = corpus.year.values

    sols, report = {}, {"k_values": list(K_VALUES), "refit_seeds": REFIT_SEEDS, "emerging_rule":
                        f"share {LATE[0]}-{LATE[1]} >= {EMERGING_RATIO}x share {EARLY[0]}-{EARLY[1]}", "by_k": {}}
    for k in K_VALUES:
        sols[k] = fit_mid(z, k, SEEDS)
        refits = [fit_mid(z, k, s) for s in REFIT_SEEDS]
        aris = [adjusted_rand_score(sols[k], r) for r in refits]
        report["by_k"][k] = {**metrics(sols[k], corpus, pairs),
                             "stability_ari_mean": round(float(np.mean(aris)), 3),
                             "nmi_with_published_k100": round(float(normalized_mutual_info_score(published.mid, sols[k])), 3),
                             **fashion(sols[k], years, k)}
        print(k, json.dumps(report["by_k"][k]), flush=True)
    if adjusted_rand_score(published.mid, sols[100]) != 1.0:
        raise RuntimeError("k = 100 did not reproduce the published middle topics")
    for a, b in zip(K_VALUES, K_VALUES[1:]):
        report["by_k"][b][f"nests_in_k{a}"] = round(nesting(sols[b], sols[a]), 3)
    out = corpus[["submission_id", "year"]].copy()
    for k in K_VALUES:
        out[f"mid_k{k}"] = sols[k]
    write_csv_gz(out, OUTPUT / "k_sensitivity_assignments.csv.gz")
    (OUTPUT / "k_sensitivity.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
