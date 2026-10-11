"""Build shared analysis tables: title features, abstract-embedding topic clusters, resubmission pairs.

Outputs (cache/, gitignored):
  title_features.parquet   one row per submission: outcomes, rule-based title features, author covariates
  topics.parquet           KMeans topic ids (k=50, k=100) on abstract embeddings
  resubmissions.parquet    candidate (earlier, later) pairs sharing a declared-ID key with similar abstracts
"""
from __future__ import annotations

import argparse
import collections

import numpy as np
import pandas as pd

import features as F
from common import CACHE, acceptance_population, load_submissions, read_table

ENC = "all-MiniLM-L6-v2"


def load_emb(field: str, enc: str = ENC) -> np.ndarray:
    return np.load(CACHE / f"emb_{field}_{enc}.npy").astype(np.float32)


def outcome_columns(s: pd.DataFrame) -> pd.DataFrame:
    pop = acceptance_population(s)
    return pd.DataFrame({
        "in_acceptance_population": pop.astype(int),
        "accepted": np.where(pop, s.decision.eq("accepted").astype(float), np.nan),
        "withdrawn": s.administrative_status.eq("withdrawn").astype(int),
        "desk_rejected": s.administrative_status.eq("desk_rejected").astype(int),
        # Success over all submissions: withdrawal and desk rejection count as failures.
        "accepted_any": (s.decision.eq("accepted") & s.administrative_status.eq("ordinary_submission")).astype(int),
    }, index=s.index)


def title_table(s: pd.DataFrame) -> pd.DataFrame:
    f = F.build(s)
    f["placeholder"] = [F.is_placeholder(t, a) for t, a in zip(s.title.fillna(""), s.abstract.fillna(""))]
    keep = ["submission_id", "year", "administrative_status", "decision", "primary_area", "declared_name_count", "review_count"]
    t = pd.concat([s[keep].reset_index(drop=True), outcome_columns(s).reset_index(drop=True),
                   f.drop(columns=["submission_id", "year"]).reset_index(drop=True)], axis=1)
    t["abstract_words"] = s.abstract.fillna("").str.split().str.len().values
    llm_topic = s.title.fillna("") + " " + s.abstract.fillna("")
    t["llm_topic"] = llm_topic.str.contains(
        r"\b(?:LLMs?|large language models?|language models?|GPT-?\d|ChatGPT|instruction[- ]tun|in-context learning|chain-of-thought|RLHF)\b",
        case=False, regex=True).values
    af = pd.read_parquet(CACHE / "author_features.parquet").drop(columns="year")
    return t.merge(af, on="submission_id", how="left")


def topics(s: pd.DataFrame) -> pd.DataFrame:
    from sklearn.cluster import KMeans
    X = load_emb("abstract")
    out = pd.DataFrame({"submission_id": s.submission_id.values})
    for k in (50, 100):
        km = KMeans(n_clusters=k, n_init=4, random_state=0).fit(X)
        out[f"topic{k}"] = km.labels_
    return out


def resubmissions(s: pd.DataFrame, min_cos: float = 0.80, max_gap: int = 2) -> pd.DataFrame:
    """Pairs (earlier i, later j), j.year - i.year in 1..max_gap, sharing >= 1 declared-ID key.

    Similarity is the cosine of abstract embeddings (MiniLM); title similarity is reported separately
    so that title changes do not drive matching. Each earlier submission keeps its best later match.
    """
    a = read_table("submission_authors")
    a = a[a.declared_id_key.notna()][["submission_id", "declared_id_key"]]
    pos = {sid: i for i, sid in enumerate(s.submission_id)}
    year = s.year.to_numpy()
    by_key = a.groupby("declared_id_key").submission_id.apply(list)
    pairs = set()
    for sids in by_key:
        if len(sids) < 2 or len(sids) > 400:
            continue
        idx = [pos[x] for x in sids]
        for i in idx:
            for j in idx:
                if 1 <= year[j] - year[i] <= max_gap:
                    pairs.add((i, j))
    if not pairs:
        return pd.DataFrame()
    P = np.array(sorted(pairs))
    A, T = load_emb("abstract"), load_emb("title")
    acos = np.einsum("ij,ij->i", A[P[:, 0]], A[P[:, 1]])
    tcos = np.einsum("ij,ij->i", T[P[:, 0]], T[P[:, 1]])
    keys = a.groupby("submission_id").declared_id_key.apply(set)
    df = pd.DataFrame({"i": P[:, 0], "j": P[:, 1], "abstract_cos": acos, "title_cos": tcos})
    df = df[df.abstract_cos >= min_cos].copy()
    df["shared_keys"] = [len(keys.get(s.submission_id.iat[i], set()) & keys.get(s.submission_id.iat[j], set()))
                         for i, j in zip(df.i, df.j)]
    df = df.sort_values("abstract_cos", ascending=False).drop_duplicates("i").drop_duplicates("j")
    cols = ["submission_id", "year", "title", "administrative_status", "decision"]
    left = s.iloc[df.i.values][cols].add_prefix("prev_").reset_index(drop=True)
    right = s.iloc[df.j.values][cols].add_prefix("next_").reset_index(drop=True)
    return pd.concat([left, right, df[["abstract_cos", "title_cos", "shared_keys"]].reset_index(drop=True)], axis=1)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", nargs="*", default=["titles", "topics", "resub"])
    args = ap.parse_args()
    s = load_submissions()
    if "titles" in args.only:
        t = title_table(s)
        t.to_parquet(CACHE / "title_features.parquet", index=False)
        print("title_features", t.shape)
    if "topics" in args.only:
        tp = topics(s)
        tp.to_parquet(CACHE / "topics.parquet", index=False)
        print("topics", tp.shape)
    if "resub" in args.only:
        r = resubmissions(s)
        r.to_parquet(CACHE / "resubmissions.parquet", index=False)
        print("resubmissions", r.shape)
        print(pd.crosstab(r.prev_year, r.prev_decision))
        print(r.title_cos.describe())


if __name__ == "__main__":
    main()
