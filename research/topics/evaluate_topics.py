"""Outcome-blind quality checks for the topic layer, against a word-count (TF-IDF/LSA) baseline.

Metrics, per level (broad / middle / fine):
- stability: adjusted Rand index between the final topics and a refit with different random seeds
- primary-area agreement: NMI with ICLR's author-chosen primary areas (2024-2026 only; an outside reference)
- keyword coherence: share of a topic's papers listing its most common specific keyword (size-weighted)
- synonym overlap: how much the topic distributions of near-synonymous keywords overlap (1 = identical)
- size rules: smallest topic and how many topics have >=30 papers in >=3 years

    python research/topics/evaluate_topics.py
"""
from __future__ import annotations

import collections
import json

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from sklearn.preprocessing import normalize

from common import LEVEL_SIZES, OUTPUT, embedded_corpus, load_embeddings
from build_topics import N_INIT, PCA_DIM

GENERIC = {"deep learning", "machine learning", "neural networks", "neural network", "deep neural networks",
           "deep neural network", "artificial intelligence"}
SYNONYMS = [("large language models", "language models"), ("large language models", "llm"),
            ("vision-language model", "vision-language models"), ("multimodal large language models", "vision-language model"),
            ("graph neural networks", "graph neural network"), ("diffusion models", "diffusion model"),
            ("offline reinforcement learning", "offline rl"), ("transformer", "transformers")]
BOILER = ("propose proposed proposes show shows shown demonstrate demonstrates method methods approach approaches results "
          "result paper work novel new existing experiments experimental performance state art sota outperforms outperform "
          "significantly significant extensive address based using use used problem problems framework").split()


def hierarchy(z: np.ndarray, seed_list: tuple[int, ...]) -> dict[str, np.ndarray]:
    km = min((KMeans(LEVEL_SIZES["fine"], n_init=N_INIT, random_state=s, max_iter=300).fit(z) for s in seed_list),
             key=lambda f: f.inertia_)
    c = normalize(km.cluster_centers_)
    out = {"fine": km.labels_}
    for lvl in ("mid", "coarse"):
        out[lvl] = AgglomerativeClustering(n_clusters=LEVEL_SIZES[lvl], linkage="ward").fit(c).labels_[km.labels_]
    return out


def tfidf_space(corpus: pd.DataFrame) -> np.ndarray:
    vec = TfidfVectorizer(stop_words=list(ENGLISH_STOP_WORDS.union(BOILER)), ngram_range=(1, 2), min_df=5, max_df=0.3,
                          sublinear_tf=True, max_features=120000, token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9\-]+\b")
    docs = corpus.title.fillna("") + ". " + corpus.title.fillna("") + ". " + corpus.abstract.fillna("")
    return normalize(TruncatedSVD(256, random_state=0, n_iter=7).fit_transform(vec.fit_transform(docs)))


def metrics(labels: np.ndarray, corpus: pd.DataFrame, pairs: list[tuple[str, str]]) -> dict:
    labels = pd.factorize(labels)[0]
    k = labels.max() + 1
    sizes = np.bincount(labels, minlength=k)
    years = pd.crosstab(labels, corpus.year.values)
    trackable = (years >= 30).sum(axis=1) >= 3
    area = corpus.primary_area.fillna("").ne("").values
    top_share = []
    for c in range(k):
        counts = collections.Counter(w for kws in corpus.keywords.values[labels == c] for w in set(kws) if w not in GENERIC)
        top_share.append(counts.most_common(1)[0][1] / sizes[c] if counts else 0.0)

    def dist(word):
        m = corpus.keywords.map(lambda kws: word in kws).values
        v = np.bincount(labels[m], minlength=k).astype(float)
        return v / v.sum()
    return {
        "topics": int(k), "smallest": int(sizes.min()), "largest": int(sizes.max()),
        "trackable_topics": int(trackable.sum()), "trackable_paper_share": round(float(sizes[trackable.values].sum() / len(labels)), 3),
        "nmi_primary_area_2024_2026": round(float(normalized_mutual_info_score(corpus.primary_area.values[area], labels[area])), 3),
        "keyword_coherence": round(float(np.dot(top_share, sizes) / sizes.sum()), 3),
        "synonym_overlap": round(float(np.mean([np.minimum(dist(a), dist(b)).sum() for a, b in pairs])), 3),
    }


def main() -> None:
    corpus = embedded_corpus()
    emb, _ = load_embeddings()
    kw_count = collections.Counter(w for kws in corpus.keywords for w in set(kws))
    pairs = [p for p in SYNONYMS if kw_count[p[0]] >= 30 and kw_count[p[1]] >= 30]
    final = pd.read_csv(OUTPUT / "topic_assignments.csv.gz")
    if not final.submission_id.equals(corpus.submission_id):
        raise RuntimeError("Assignments are out of date; rerun build_topics.py")

    z = normalize(PCA(PCA_DIM, svd_solver="full").fit_transform(normalize(emb)))
    refit = hierarchy(z, (10, 11, 12))
    lsa = tfidf_space(corpus)
    base = hierarchy(lsa, (0, 1, 2))
    base_refit = hierarchy(lsa, (10, 11, 12))
    report = {"synonym_pairs": pairs, "levels": {}}
    for lvl in ("coarse", "mid", "fine"):
        report["levels"][lvl] = {
            "specter2": {**metrics(final[lvl].values, corpus, pairs),
                         "stability_ari": round(float(adjusted_rand_score(final[lvl], refit[lvl])), 3)},
            "tfidf_baseline": {**metrics(base[lvl], corpus, pairs),
                               "stability_ari": round(float(adjusted_rand_score(base[lvl], base_refit[lvl])), 3)},
        }
    (OUTPUT / "quality_metrics.json").write_text(json.dumps(report, indent=2) + "\n")
    for lvl, r in report["levels"].items():
        for name, m in r.items():
            print(f"{lvl:6s} {name:15s} " + " | ".join(f"{k} {v}" for k, v in m.items()))


if __name__ == "__main__":
    main()
