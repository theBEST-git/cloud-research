"""Train and evaluate the contribution classifiers (outcome-blind: title, abstract, embeddings, annotation labels).

Labels come from annotation/contribution_types (2,000 training papers + 300 pilot gold papers):
- primary_class (6): method, theory, empirical, dataset_benchmark, evaluation, other
- architecture (yes/no): the primary fine type is `model` (a new architecture)
- secondary_class (7): none, or the secondary fine type grouped like the primary class
- foundation_model (yes/no)
Fine types inside "other" (problem, system, application, perspective, survey, recipe) have too few examples
to learn; they come from annotators for papers routed to them.

Features: SPECTER2 embedding (centred, unit length) and/or TF-IDF of title + abstract (word 1-3 grams, top 100k; IDF
fitted on all papers, which is unsupervised). Model: logistic regression per label.
Selection: feature set x regularisation x class weighting chosen by 5-fold CV (seed 0); the chosen setting is then
re-evaluated on fresh 5-fold splits (seed 1), which are the numbers reported.

    python research/topics/contribution_classifier.py
"""
from __future__ import annotations

import itertools
import json
import pickle

import numpy as np
import pandas as pd
import scipy.sparse as sp
from joblib import Parallel, delayed
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, log_loss, precision_recall_fscore_support
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import normalize

from common import CACHE, ERAS, HERE, OUTPUT, embedded_corpus, load_embeddings

ANN = HERE / "annotation" / "contribution_types"
CLASS_OF = {"model": "method", "system": "other", "problem": "other", "application": "other", "recipe": "other",
            "perspective": "other", "survey_position": "other"}
LABELS = {  # label: (selection metric, class weights tried)
    "primary_class": ("macro_f1", (None, "balanced")),
    "architecture": ("macro_f1", (None, "balanced")),
    "secondary_class": ("macro_f1", (None, "balanced")),
    "foundation_model": ("macro_f1", (None,)),
}
FEATURES, CS = ("tfidf", "embedding", "both"), (4.0, 16.0, 64.0)


def to_class(t: str) -> str:
    return "none" if t == "none" else CLASS_OF.get(t, t)


def load_labels() -> pd.DataFrame:
    cols = ["submission_id", "year", "stratum", "fine", "secondary", "foundation_model"]
    t = pd.read_csv(ANN / "training" / "training_labels.csv").rename(columns={"primary_type": "fine", "secondary_type": "secondary"})
    p = pd.read_csv(ANN / "pilot_gold.csv").merge(pd.read_csv(ANN / "pilot_gold_facets.csv")[["submission_id", "gold_foundation_model"]],
                                                  on="submission_id")
    p = p.rename(columns={"gold_primary": "fine", "gold_secondary": "secondary", "gold_foundation_model": "foundation_model"})
    lab = pd.concat([t[cols].assign(source="training"), p[cols].assign(source="pilot")], ignore_index=True)
    if not lab.submission_id.is_unique:
        raise RuntimeError("A paper appears in both the training and the pilot labels")
    lab["primary_class"] = lab.fine.map(to_class)
    lab["architecture"] = np.where(lab.fine == "model", "yes", "no")
    lab["secondary_class"] = lab.secondary.map(to_class)
    return lab


def features(corpus: pd.DataFrame, emb: np.ndarray):
    text = (corpus.title.fillna("") + ". " + corpus.abstract.fillna("")).str.lower()
    vec = TfidfVectorizer(ngram_range=(1, 3), min_df=3, max_df=0.5, sublinear_tf=True, max_features=100000,
                          token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9\-]+\b")
    tfidf = vec.fit_transform(text).tocsr()
    e = normalize(emb - emb.mean(axis=0))
    return vec, {"tfidf": tfidf, "embedding": sp.csr_matrix(e), "both": sp.hstack([tfidf, sp.csr_matrix(e)]).tocsr()}


def _fold(X, y, tr, te, C, weight):
    return te, LogisticRegression(C=C, class_weight=weight, max_iter=5000).fit(X[tr], y[tr]).predict_proba(X[te])


def cv_proba(X, y, C, weight, seed):
    classes = np.unique(y)
    proba = np.zeros((len(y), len(classes)))
    folds = StratifiedKFold(5, shuffle=True, random_state=seed).split(X, y)
    for te, p in Parallel(n_jobs=4)(delayed(_fold)(X, y, tr, te, C, weight) for tr, te in folds):
        proba[te] = p
    return classes, proba


def ece(conf, correct, bins=10):
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(conf, edges) - 1, 0, bins - 1)
    return float(sum(abs(correct[idx == b].mean() - conf[idx == b].mean()) * (idx == b).mean() for b in range(bins) if (idx == b).any()))


def report(y, classes, proba, lab):
    pred = classes[proba.argmax(axis=1)]
    conf = proba.max(axis=1)
    correct = pred == y
    rnd = (lab.stratum == "random").values
    p, r, f, n = precision_recall_fscore_support(y, pred, labels=classes, zero_division=0)
    order = np.argsort(-conf)
    keep = {f"top_{q}pct": round(float(correct[order[: int(len(y) * q / 100)]].mean()), 3) for q in (90, 80)}
    return {
        "accuracy": round(float(accuracy_score(y, pred)), 3),
        "accuracy_random_papers": round(float(correct[rnd].mean()), 3),
        "macro_f1": round(float(f1_score(y, pred, average="macro")), 3),
        "log_loss": round(float(log_loss(y, proba, labels=classes)), 3),
        "calibration_error": round(ece(conf, correct.astype(float)), 3),
        "accuracy_on_most_confident": keep,
        "accuracy_by_era": {era: round(float(correct[lab.year.between(lo, hi).values].mean()), 3) for era, (lo, hi) in ERAS.items()},
        "per_class": {c: {"precision": round(float(pp), 3), "recall": round(float(rr), 3), "f1": round(float(ff), 3), "n": int(nn)}
                      for c, pp, rr, ff, nn in zip(classes, p, r, f, n)},
        "confusion": {"labels": classes.tolist(), "matrix": confusion_matrix(y, pred, labels=classes).tolist()},
    }


def main() -> None:
    corpus = embedded_corpus()
    emb, ids = load_embeddings()
    if not ids.equals(corpus.submission_id):
        raise RuntimeError("Embedding cache does not match the corpus")
    lab = load_labels()
    row = pd.Series(np.arange(len(corpus)), index=corpus.submission_id)
    missing = set(lab.submission_id) - set(row.index)
    if missing:
        raise RuntimeError(f"{len(missing)} labelled papers have no embedding")
    rows = row[lab.submission_id].values
    vec, feats = features(corpus, emb.astype(np.float64))
    results, final = {"labelled_papers": len(lab), "labels": {}}, {}
    for label, (metric, weights) in LABELS.items():
        y = lab[label].values
        scores = []
        for fs, C, w in itertools.product(FEATURES, CS, weights):
            classes, proba = cv_proba(feats[fs][rows], y, C, w, seed=0)
            pred = classes[proba.argmax(axis=1)]
            scores.append((f1_score(y, pred, average="macro"), accuracy_score(y, pred), fs, C, w))
            print(f"{label:16s} {fs:9s} C={C:<4} weight={str(w):8s} macro-F1 {scores[-1][0]:.3f} accuracy {scores[-1][1]:.3f}", flush=True)
        best = max(scores, key=lambda s: (s[0], s[1]))
        classes, proba = cv_proba(feats[best[2]][rows], y, best[3], best[4], seed=1)
        results["labels"][label] = {"features": best[2], "C": best[3], "class_weight": best[4], "selected_by": metric,
                                    "cv_seed1": report(y, classes, proba, lab)}
        final[label] = (best[2], LogisticRegression(C=best[3], class_weight=best[4], max_iter=5000).fit(feats[best[2]][rows], y))
        print(json.dumps({label: results["labels"][label]["cv_seed1"]}, indent=1)[:1500], flush=True)
    (OUTPUT / "contribution_classifier_metrics.json").write_text(json.dumps(results, indent=2) + "\n")
    with open(CACHE / "contribution_models.pkl", "wb") as f:
        pickle.dump({"vectorizer": vec, "models": final, "embedding_mean": emb.astype(np.float64).mean(axis=0)}, f)


if __name__ == "__main__":
    main()
