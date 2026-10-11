"""Outcome-blind quality checks for the topic layer, against a word-count (TF-IDF/LSA) baseline.

Both spaces use the same fitting procedure (build_topics.fit_hierarchy). Metrics per level:
- stability: adjusted Rand index between the final topics and refits with other random seeds
- primary-area agreement: NMI with ICLR's author-chosen primary areas (2024-2026; an outside reference)
- keyword coherence: share of a topic's papers listing its most common specific keyword (size-weighted)
- synonym overlap: overlap of the topic distributions of near-synonymous keywords (1 = identical)
- size rules: smallest topic, and topics with >=30 papers in >=3 years
Also writes per-topic and per-paper stability (how consistently papers stay together across refits).

    python research/topics/evaluate_topics.py
"""
from __future__ import annotations

import collections
import json

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from sklearn.preprocessing import normalize

from assign_topics import project
from build_topics import PCA_DIM, fit_hierarchy
from common import OUTPUT, embedded_corpus, load_embeddings, write_csv_gz

LEVELS = ("coarse", "mid", "fine")
REFIT_SEEDS = [(10, 11, 12), (20, 21, 22), (30, 31, 32)]
GENERIC = {"deep learning", "machine learning", "neural networks", "neural network", "deep neural networks",
           "deep neural network", "artificial intelligence"}
SYNONYMS = [("large language models", "language models"), ("large language models", "llm"),
            ("vision-language model", "vision-language models"), ("multimodal large language models", "vision-language model"),
            ("graph neural networks", "graph neural network"), ("diffusion models", "diffusion model"),
            ("offline reinforcement learning", "offline rl"), ("transformer", "transformers")]
BOILER = ("propose proposed proposes show shows shown demonstrate demonstrates method methods approach approaches results "
          "result paper work novel new existing experiments experimental performance state art sota outperforms outperform "
          "significantly significant extensive address based using use used problem problems framework").split()


def tfidf_space(corpus: pd.DataFrame) -> np.ndarray:
    vec = TfidfVectorizer(stop_words=list(ENGLISH_STOP_WORDS.union(BOILER)), ngram_range=(1, 2), min_df=5, max_df=0.3,
                          sublinear_tf=True, max_features=120000, token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9\-]+\b")
    docs = corpus.title.fillna("") + ". " + corpus.title.fillna("") + ". " + corpus.abstract.fillna("")
    return normalize(TruncatedSVD(256, random_state=0, n_iter=7).fit_transform(vec.fit_transform(docs)))


def metrics(labels, corpus: pd.DataFrame, pairs) -> dict:
    labels = pd.factorize(np.asarray(labels))[0]
    k = labels.max() + 1
    sizes = np.bincount(labels, minlength=k)
    years = pd.crosstab(labels, corpus.year.values)
    trackable = ((years >= 30).sum(axis=1) >= 3).values
    area = corpus.primary_area.fillna("").ne("").values
    top_share = []
    for c in range(k):
        counts = collections.Counter(w for kws in corpus.keywords.values[labels == c] for w in set(kws) if w not in GENERIC)
        top_share.append(counts.most_common(1)[0][1] / sizes[c] if counts else 0.0)

    def dist(word):
        m = corpus.keywords.map(lambda kws: word in kws).values
        v = np.bincount(labels[m], minlength=k).astype(float)
        return v / v.sum()
    return {"topics": int(k), "smallest": int(sizes.min()), "largest": int(sizes.max()),
            "trackable_topics": int(trackable.sum()), "trackable_paper_share": round(float(sizes[trackable].sum() / len(labels)), 3),
            "nmi_primary_area_2024_2026": round(float(normalized_mutual_info_score(corpus.primary_area.values[area], labels[area])), 3),
            "keyword_coherence": round(float(np.dot(top_share, sizes) / sizes.sum()), 3),
            "synonym_overlap": round(float(np.mean([np.minimum(dist(a), dist(b)).sum() for a, b in pairs])), 3)}


def matched(final: np.ndarray, refit: np.ndarray):
    """For each final topic: best-matching refit cluster (Jaccard) and whether each paper stayed in it."""
    f_codes, f = np.unique(final, return_inverse=True)
    _, r = np.unique(refit, return_inverse=True)
    inter = np.zeros((f.max() + 1, r.max() + 1))
    np.add.at(inter, (f, r), 1)
    union = inter.sum(1, keepdims=True) + inter.sum(0, keepdims=True) - inter
    jac = inter / union
    best = jac.argmax(axis=1)
    return dict(zip(f_codes, jac.max(axis=1))), (r == best[f])


def main() -> None:
    corpus = embedded_corpus()
    emb, _ = load_embeddings()
    kw_count = collections.Counter(w for kws in corpus.keywords for w in set(kws))
    pairs = [p for p in SYNONYMS if kw_count[p[0]] >= 30 and kw_count[p[1]] >= 30]
    final = pd.read_csv(OUTPUT / "topic_assignments.csv.gz")
    if not final.submission_id.equals(corpus.submission_id):
        raise RuntimeError("Assignments are out of date; rerun build_topics.py")

    emb = emb.astype(np.float64)
    pca = PCA(PCA_DIM, svd_solver="full").fit(normalize(emb))
    z = project(emb, {"pca_mean": pca.mean_, "pca_components": pca.components_})
    refits = [fit_hierarchy(z, seeds) for seeds in REFIT_SEEDS]
    lsa = tfidf_space(corpus)
    base, base_refit = fit_hierarchy(lsa), fit_hierarchy(lsa, REFIT_SEEDS[0])

    report = {"synonym_pairs": pairs, "refit_seeds": REFIT_SEEDS, "levels": {}}
    topic_rows, paper = [], {"submission_id": corpus.submission_id}
    for lvl in LEVELS:
        aris, jac_runs, stay_runs = [], [], []
        for h in refits:
            aris.append(adjusted_rand_score(final[lvl], h[lvl]))
            jac, stay = matched(final[lvl].values, h[lvl])
            jac_runs.append(jac)
            stay_runs.append(stay)
        paper[f"{lvl}_stability"] = np.mean(stay_runs, axis=0).round(3)
        for t in sorted(jac_runs[0]):
            topic_rows.append({"level": lvl, "topic": t, "stability_jaccard": round(float(np.mean([j[t] for j in jac_runs])), 3)})
        report["levels"][lvl] = {
            "specter2": {**metrics(final[lvl], corpus, pairs), "stability_ari_mean": round(float(np.mean(aris)), 3),
                         "stability_ari_range": [round(float(min(aris)), 3), round(float(max(aris)), 3)]},
            "tfidf_baseline": {**metrics(base[lvl], corpus, pairs),
                               "stability_ari_mean": round(float(adjusted_rand_score(base[lvl], base_refit[lvl])), 3)},
        }
    pd.DataFrame(topic_rows).to_csv(OUTPUT / "topic_stability.csv", index=False)
    write_csv_gz(pd.DataFrame(paper), OUTPUT / "paper_topic_stability.csv.gz")
    (OUTPUT / "quality_metrics.json").write_text(json.dumps(report, indent=2) + "\n")
    for lvl, r in report["levels"].items():
        for name, m in r.items():
            print(f"{lvl:6s} {name:15s} " + " | ".join(f"{k} {v}" for k, v in m.items()))


if __name__ == "__main__":
    main()
