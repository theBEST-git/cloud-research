"""Hindsight-bias check for the middle topic level (outcome-blind, label-free).

The published topics are fitted on all papers at once, and 69% of papers are from 2024-2026, so the topic map
reflects the field as it is now. That can exaggerate how topics "rise" (today's topics get early seeds) and hide
topics that faded (absorbed into today's topics). This script compares five maps, each with k = 100 and the
same fitting procedure as build_topics.py, every paper assigned to its nearest centroid:

- pooled:   the published middle topics (all years, every paper weighted equally)
- balanced: all years, every year weighted equally (no dominance of recent years)
- early:    fitted on 2017-2020 papers only (no hindsight: only the past is used to define topics)
- middle:   fitted on 2021-2023 papers only
- late:     fitted on 2024-2026 papers only (full hindsight)

Per map: emerging topics (2024-26 share >= 3x the 2017-20 share) and declining topics (<= 1/3x), their number
and the share of papers in them; effective number of topics per year / k; mean similarity of papers to their
topic centroid by year; NMI with the pooled map. The early and late maps bracket the pooled map: if the pooled
map shows far fewer declines than the early map, it hides faded topics. A plain seed refit of the pooled map
gives the baseline for how much any refit differs.

Writes output/hindsight_check.json and output/hindsight_assignments.csv.gz (topic per paper for each map).

    python research/topics/hindsight_check.py
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from sklearn.preprocessing import normalize

from assign_topics import project
from build_topics import N_INIT_MID, PCA_DIM, SEEDS
from common import ERAS, OUTPUT, embedded_corpus, load_embeddings, write_csv_gz

K = 100
REFIT_SEEDS = (10, 11, 12)
RATIO = 3.0
EARLY, LATE = ERAS["2017-2020"], ERAS["2024-2026"]


def fit_centroids(z: np.ndarray, seeds: tuple[int, ...], weight: np.ndarray | None = None) -> np.ndarray:
    km = min((KMeans(K, n_init=N_INIT_MID, random_state=s, max_iter=300).fit(z, sample_weight=weight) for s in seeds),
             key=lambda f: f.inertia_)
    return normalize(km.cluster_centers_)


def describe(labels: np.ndarray, sim: np.ndarray, years: np.ndarray, pooled: np.ndarray) -> dict:
    t = pd.crosstab(labels, years)
    early = t.loc[:, EARLY[0]:EARLY[1]].sum(axis=1)
    late = t.loc[:, LATE[0]:LATE[1]].sum(axis=1)
    ratio = ((late + 0.5) / late.sum()) / ((early + 0.5) / early.sum())
    emerging, declining = ratio >= RATIO, ratio <= 1 / RATIO
    shares = t / t.sum(axis=0)
    eff = {int(y): round(float(np.exp(-(shares[y][shares[y] > 0] * np.log(shares[y][shares[y] > 0])).sum()) / K), 3)
           for y in shares.columns}
    fit = pd.Series(sim).groupby(years).mean()
    return {"topics_used": int(len(t)),
            "nmi_with_pooled": round(float(normalized_mutual_info_score(pooled, labels)), 3),
            "ari_with_pooled": round(float(adjusted_rand_score(pooled, labels)), 3),
            "emerging_topics": int(emerging.sum()),
            "late_paper_share_in_emerging": round(float(late[emerging].sum() / late.sum()), 3),
            "declining_topics": int(declining.sum()),
            "early_paper_share_in_declining": round(float(early[declining].sum() / early.sum()), 3),
            "effective_topics_over_k_by_year": eff,
            "mean_similarity_to_centroid_by_year": {int(y): round(float(v), 4) for y, v in fit.items()}}


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
    years = corpus.year.values
    pooled = pd.factorize(published.mid)[0]

    counts = pd.Series(years).value_counts()
    weight = 1.0 / pd.Series(years).map(counts).values
    in_era = {name: (years >= lo) & (years <= hi) for name, (lo, hi) in
              {"early": EARLY, "middle": ERAS["2021-2023"], "late": LATE}.items()}
    centroids = {"pooled": fit_centroids(z, SEEDS),
                 "seed_refit": fit_centroids(z, REFIT_SEEDS),
                 "balanced": fit_centroids(z, SEEDS, weight),
                 **{name: fit_centroids(z[mask], SEEDS) for name, mask in in_era.items()}}

    report = {"k": K, "ratio_rule": f"emerging: 2024-26 share >= {RATIO}x 2017-20 share; declining: <= 1/{RATIO}x",
              "papers_by_era": {n: int(m.sum()) for n, m in in_era.items()}, "maps": {}}
    out = corpus[["submission_id", "year"]].copy()
    for name, c in centroids.items():
        s = z @ c.T
        labels = s.argmax(axis=1)
        if name == "pooled" and adjusted_rand_score(pooled, labels) != 1.0:
            raise RuntimeError("Refitting the pooled map did not reproduce the published middle topics")
        report["maps"][name] = describe(labels, s.max(axis=1), years, pooled)
        out[f"mid_{name}"] = labels
        print(name, json.dumps({k: v for k, v in report["maps"][name].items() if "by_year" not in k}), flush=True)
    write_csv_gz(out, OUTPUT / "hindsight_assignments.csv.gz")
    (OUTPUT / "hindsight_check.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
