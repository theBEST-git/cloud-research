"""Probable earlier versions (resubmissions) of each paper (outcome-blind; PREREGISTRATION.md R1, S4).

For every paper in year t, its nearest earlier-year paper by cosine of mean-centred SPECTER2 embeddings, plus title token Jaccard, shared
author keys, and any earlier paper with the same normalised title. With --tau (calibrated by blind judges, R1),
`probable_earlier_version` = the exact-title match if there is one, else the nearest neighbour if its cosine >= tau.

Writes output/earlier_versions.csv.gz and output/checks/resubmissions.json (cosine percentiles for the τ bins).

    python research/fashion/resubmissions.py [--tau 0.95]
"""
from __future__ import annotations

import argparse
import json
import re

import numpy as np
import pandas as pd

from common import OUTPUT, topic_layer, write_csv_gz
from variables import load_authors

BLOCK = 2000
TAU_BINS = [(0.80, 0.85), (0.85, 0.90), (0.90, 0.95), (0.95, 1.01)]   # centred cosine; fixed before judging (D15)


def norm_title(t: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", str(t).lower()).split())


def nearest_earlier(x: np.ndarray, years: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Index and cosine of each paper's nearest neighbour among papers from strictly earlier years (-1 if none)."""
    nn, cos = np.full(len(x), -1), np.full(len(x), np.nan)
    order = np.argsort(years, kind="stable")
    for y in np.unique(years):
        q = np.where(years == y)[0]
        db = order[: np.searchsorted(years[order], y)]           # all papers from earlier years
        if not len(db):
            continue
        for s in range(0, len(q), BLOCK):
            qi = q[s:s + BLOCK]
            sims = x[qi] @ x[db].T
            j = sims.argmax(axis=1)
            nn[qi], cos[qi] = db[j], sims[np.arange(len(qi)), j]
    return nn, cos


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--tau", type=float)
    a = p.parse_args()
    tl = topic_layer()
    corpus = tl.embedded_corpus()
    emb, ids = tl.load_embeddings()
    assert ids.equals(corpus.submission_id)
    x = emb.astype(np.float32)
    x -= x.mean(axis=0)                                            # centring removes SPECTER2's anisotropy (D15)
    x /= np.linalg.norm(x, axis=1, keepdims=True)
    years = corpus.year.to_numpy()
    nn, cos = nearest_earlier(x, years)

    sid = corpus.submission_id.to_numpy()
    titles = corpus.title.map(norm_title).to_numpy()
    tokens = [set(t.split()) for t in titles]
    authors = load_authors(corpus.submission_id).groupby("submission_id").key.apply(set)
    keys = [authors.get(s, set()) for s in sid]
    first_by_title: dict[str, list[tuple[int, int]]] = {}
    for i, (t, y) in enumerate(zip(titles, years)):
        first_by_title.setdefault(t, []).append((y, i))
    exact = []
    for i, (t, y) in enumerate(zip(titles, years)):
        earlier = [(yy, j) for yy, j in first_by_title[t] if yy < y]
        exact.append(sid[max(earlier)[1]] if earlier and t else None)    # most recent earlier exact-title paper
    has = nn >= 0
    out = pd.DataFrame({"submission_id": sid, "year": years,
                        "nn_id": np.where(has, sid[np.maximum(nn, 0)], None),
                        "nn_year": np.where(has, years[np.maximum(nn, 0)], np.nan),
                        "nn_cos": np.round(cos, 5)})
    out["nn_title_jaccard"] = [round(len(tokens[i] & tokens[j]) / max(len(tokens[i] | tokens[j]), 1), 4) if j >= 0 else np.nan
                               for i, j in enumerate(nn)]
    out["nn_shared_keys"] = [len(keys[i] & keys[j]) if j >= 0 else np.nan for i, j in enumerate(nn)]
    out["exact_title_id"] = exact
    if a.tau is not None:
        out["probable_earlier_version"] = [e if e is not None else (n if c >= a.tau else None)
                                           for e, n, c in zip(out.exact_title_id, out.nn_id, out.nn_cos)]
    write_csv_gz(out, OUTPUT / "earlier_versions.csv.gz")
    v = out.nn_cos.dropna()
    checks = {"papers_with_earlier_year": int(has.sum()),
              "nn_cos_percentiles": {str(q): round(float(np.percentile(v, q)), 4) for q in (50, 75, 85, 90, 95, 98, 99, 99.5)},
              "pairs_per_tau_bin": {f"[{lo},{hi})": int(((v >= lo) & (v < hi)).sum()) for lo, hi in TAU_BINS},
              "exact_title_matches": int(out.exact_title_id.notna().sum()), "tau": a.tau}
    prof = out[(out.year >= 2021) & (out.nn_year >= 2021)]      # profile-ID years: shared keys are comparable (D15)
    checks["shared_author_share_per_tau_bin_2021_on"] = {
        f"[{lo},{hi})": round(float((prof[(prof.nn_cos >= lo) & (prof.nn_cos < hi)].nn_shared_keys > 0).mean()), 4)
        for lo, hi in TAU_BINS}
    if a.tau is not None:
        f = out.probable_earlier_version.notna()
        checks["flagged"] = int(f.sum())
        checks["flagged_by_year"] = out[f].groupby("year").size().to_dict()
        checks["flagged_share_with_shared_author_key"] = round(float((out[f].nn_shared_keys > 0).mean()), 4)
    (OUTPUT / "checks").mkdir(parents=True, exist_ok=True)
    (OUTPUT / "checks" / "resubmissions.json").write_text(json.dumps(checks, indent=2, default=int) + "\n")
    print(json.dumps(checks, indent=1, default=int))


if __name__ == "__main__":
    main()
