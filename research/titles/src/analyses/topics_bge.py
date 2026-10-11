"""WP2 topics: KMeans k50/k100 refit on bge-small (512-token) abstract embeddings of universe U, plus frozen
centroids for held-out assignment, MiniLM-vs-bge stability (ARI/NMI), the bge LLM-cluster flag, and the
20 most central papers per topic100 cluster (input for the V5 cluster labels).

    cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.topics_bge

Outputs (outputs/topics/): topics_bge.parquet, centroids.npz, topic_stability.csv, llm_cluster_agreement.csv,
central_papers_k100.csv, llm_clusters_bge.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

_SRC = Path(__file__).resolve().parents[1]
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from analyses._core import (CACHE, CENTROIDS_PATH, LLM_CLUSTER_THRESHOLD, TOPIC_DIR, TOPICS_BGE_PATH,  # noqa: E402
                            assign_centroids, llm_clusters, load_universe)

N_INIT = 4
SEED = 0


def label_means(E: np.ndarray, labels: np.ndarray, k: int) -> np.ndarray:
    C = np.zeros((k, E.shape[1]), dtype=np.float64)
    np.add.at(C, labels, E)
    return (C / np.bincount(labels, minlength=k)[:, None]).astype(np.float32)


def central(E: np.ndarray, labels: np.ndarray, C: np.ndarray, ids: np.ndarray, n: int = 20) -> pd.DataFrame:
    d = ((E - C[labels]) ** 2).sum(1)
    df = pd.DataFrame({"submission_id": ids, "cluster": labels, "dist": d})
    df = df.sort_values(["cluster", "dist"]).groupby("cluster").head(n)
    df["rank"] = df.groupby("cluster").cumcount() + 1
    return df


def main():
    from sklearn.cluster import KMeans
    from sklearn.metrics import adjusted_rand_score, cohen_kappa_score, normalized_mutual_info_score
    TOPIC_DIR.mkdir(parents=True, exist_ok=True)
    u = load_universe(["submission_id", "year", "emb_row", "title", "topic50", "topic100", "llm_regex",
                       "llm_cluster", "llm_topic"])
    Eb = np.load(CACHE / "emb_abstract_bge-small-en-v1.5.npy", mmap_mode="r")
    Xb = np.asarray(Eb[u.emb_row.to_numpy()], dtype=np.float32)
    out = pd.DataFrame({"submission_id": u.submission_id})
    cents = {}
    for k in (50, 100):
        km = KMeans(n_clusters=k, n_init=N_INIT, random_state=SEED).fit(Xb)
        out[f"topic{k}_bge"] = km.labels_
        cents[f"bge_k{k}"] = km.cluster_centers_.astype(np.float32)
        print(f"bge k={k}: inertia {km.inertia_:.1f}, iters {km.n_iter_}", flush=True)

    # MiniLM centroids = per-label means over the rows the cache KMeans was fitted on (all 43,516 rows).
    tp = pd.read_parquet(CACHE / "topics.parquet")
    ids_all = np.load(CACHE / "embedding_ids.npy", allow_pickle=True)
    assert (tp.submission_id.to_numpy() == ids_all).all()
    Em = np.load(CACHE / "emb_abstract_all-MiniLM-L6-v2.npy").astype(np.float32)
    repro = {}
    for k in (50, 100):
        C = label_means(Em, tp[f"topic{k}"].to_numpy(), k)
        cents[f"minilm_k{k}"] = C
        repro[k] = float((assign_centroids(Em, C) == tp[f"topic{k}"].to_numpy()).mean())
        print(f"MiniLM k={k}: nearest-centroid reproduces cache labels for {repro[k]:.4%} of rows", flush=True)
    np.savez(CENTROIDS_PATH, **cents,
             note=np.array("bge_k*: sklearn KMeans(n_init=4, random_state=0) cluster_centers_ fitted on universe U "
                           "bge-small abstract embeddings (float16 cache -> float32). minilm_k*: per-label means of "
                           "MiniLM abstract embeddings for cache/topics.parquet labels (fit on all 43,516 rows). "
                           "Assign with analyses._core.assign_centroids (Euclidean)."))

    # Stability (V5)
    rows = []
    for k in (50, 100):
        a, b = u[f"topic{k}"].to_numpy(), out[f"topic{k}_bge"].to_numpy()
        rows.append(dict(k=k, comparison="MiniLM vs bge (U)", ari=adjusted_rand_score(a, b),
                         nmi=normalized_mutual_info_score(a, b)))
        for y0, y1 in [(2017, 2023), (2024, 2026)]:
            m = u.year.between(y0, y1).to_numpy()
            rows.append(dict(k=k, comparison=f"MiniLM vs bge ({y0}-{y1})", ari=adjusted_rand_score(a[m], b[m]),
                             nmi=normalized_mutual_info_score(a[m], b[m])))
    a50, a100 = out.topic50_bge.to_numpy(), out.topic100_bge.to_numpy()
    rows.append(dict(k="50 vs 100", comparison="bge k50 vs bge k100", ari=adjusted_rand_score(a50, a100),
                     nmi=normalized_mutual_info_score(a50, a100)))
    rows.append(dict(k="50 vs 100", comparison="MiniLM k50 vs MiniLM k100",
                     ari=adjusted_rand_score(u.topic50, u.topic100), nmi=normalized_mutual_info_score(u.topic50, u.topic100)))
    stab = pd.DataFrame(rows)
    stab.to_csv(TOPIC_DIR / "topic_stability.csv", index=False)
    print(stab.round(3).to_string(), flush=True)

    # bge LLM-cluster flag (same rule as MiniLM: > 50% regex-LLM papers, U all years)
    clus = llm_clusters(out.topic100_bge, u.llm_regex)
    clus50 = llm_clusters(out.topic50_bge, u.llm_regex)
    out["llm_cluster_bge"] = out.topic100_bge.isin(clus)
    out["llm_topic_bge"] = u.llm_regex.to_numpy() | out.llm_cluster_bge.to_numpy()
    share = u.llm_regex.groupby(out.topic100_bge.to_numpy()).mean()
    (TOPIC_DIR / "llm_clusters_bge.json").write_text(json.dumps({
        "threshold": LLM_CLUSTER_THRESHOLD, "topic100_bge_llm_clusters": clus, "topic50_bge_llm_clusters": clus50,
        "topic100_bge_regex_share": {int(i): round(float(v), 4) for i, v in share.sort_values(ascending=False).items()},
    }, indent=1))
    ag = []
    pairs = [("llm_cluster (MiniLM)", u.llm_cluster), ("llm_cluster_bge", out.llm_cluster_bge),
             ("llm_regex", u.llm_regex), ("llm_topic (MiniLM union)", u.llm_topic), ("llm_topic_bge (union)", out.llm_topic_bge)]
    for i, (na, xa) in enumerate(pairs):
        for nb, xb in pairs[i + 1:]:
            xa_, xb_ = np.asarray(xa, bool), np.asarray(xb, bool)
            ag.append(dict(a=na, b=nb, share_a=xa_.mean(), share_b=xb_.mean(), agree=(xa_ == xb_).mean(),
                           kappa=cohen_kappa_score(xa_, xb_)))
    ag = pd.DataFrame(ag)
    by_year = pd.DataFrame({"year": u.year, "llm_regex": u.llm_regex, "llm_cluster": u.llm_cluster,
                            "llm_cluster_bge": out.llm_cluster_bge, "llm_topic": u.llm_topic,
                            "llm_topic_bge": out.llm_topic_bge}).groupby("year").mean()
    ag.to_csv(TOPIC_DIR / "llm_cluster_agreement.csv", index=False)
    by_year.to_csv(TOPIC_DIR / "llm_flags_by_year.csv")
    print(ag.round(3).to_string())
    print(by_year.round(3).to_string())
    print("bge LLM clusters:", clus)

    # Central papers per topic100 cluster (for V5 cluster labelling)
    cm = central(Em[u.emb_row.to_numpy()], u.topic100.to_numpy(), cents["minilm_k100"], u.submission_id.to_numpy())
    cm["model"] = "minilm_k100"
    cb = central(Xb, out.topic100_bge.to_numpy(), cents["bge_k100"], u.submission_id.to_numpy())
    cb["model"] = "bge_k100"
    pd.concat([cm, cb]).to_csv(TOPIC_DIR / "central_papers_k100.csv", index=False)

    out.to_parquet(TOPICS_BGE_PATH, index=False)
    print("topics_bge", out.shape, flush=True)


if __name__ == "__main__":
    main()
