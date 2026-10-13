"""Twin feasibility, step 1: same-cycle candidate pairs of near-identical submissions.

Candidates = same-year pairs that are within each other's top-3 neighbours on name-masked bge
abstracts (union over directions, so not only mutual nearest neighbours) with cosine >= 0.86,
plus top-3 pairs on the unmasked MiniLM abstract encoder (second view). Exclusions (flagged, not
dropped): shared declared author key, shared fuzzy author name (initial + surname), linked
ICLR->ICLR resubmission, near-identical titles (title cosine >= 0.95, dual-submission suspects).
Outcomes (decisions) are NOT read here.

Run: cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m twins.candidates
Writes outputs/twins_feas/candidates.parquet and candidates_counts.csv.
"""
from __future__ import annotations

import json
import re
import unicodedata

import numpy as np
import pandas as pd

from analyses import _core as C

OUT = C.OUT / "twins_feas"
K = 3
FLOOR = 0.86


def _norm(E):
    n = np.linalg.norm(E, axis=1, keepdims=True)
    n[n == 0] = 1
    return (E / n).astype(np.float32)


def topk_pairs(E, years, ok, k=K, floor=FLOOR):
    rows = []
    for y in sorted(set(years)):
        idx = np.where((years == y) & ok)[0]
        X = E[idx]
        for st in range(0, len(idx), 2000):
            S = X[st:st + 2000] @ X.T
            for r in range(S.shape[0]):
                S[r, st + r] = -1
            part = np.argpartition(-S, k, axis=1)[:, :k]
            for r in range(S.shape[0]):
                for c in part[r]:
                    s = S[r, c]
                    if s >= floor:
                        a, b = idx[st + r], idx[c]
                        rows.append((y, min(a, b), max(a, b), float(s)))
    P = pd.DataFrame(rows, columns=["year", "i", "j", "cos"])
    return P.groupby(["year", "i", "j"], as_index=False).cos.max()


def normname(s):
    try:
        s = json.loads(s)
    except Exception:
        pass
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    toks = re.sub(r"[^a-z ]", " ", s).split()
    return (toks[0][0] + " " + toks[-1]) if len(toks) >= 2 else ""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = C.load_analysis_frame(feature_cols=["name_primary"],
                               universe_cols=["submission_id", "year", "emb_row", "topic100", "area_h", "pool"]).reset_index(drop=True)
    years = df.year.to_numpy()
    Em, found = C.load_masked_embedding(df)
    Em = _norm(Em)
    Ea = _norm(C.load_embedding(df, "abstract", "all-MiniLM-L6-v2"))
    Eb = _norm(C.load_embedding(df, "abstract", "bge-small-en-v1.5"))
    Et = _norm(C.load_embedding(df, "title", "bge-small-en-v1.5"))

    Pm = topk_pairs(Em, years, found).rename(columns={"cos": "cos_masked"})
    Pa = topk_pairs(Ea, years, np.ones(len(df), bool), floor=0.80).rename(columns={"cos": "cos_minilm_topk"})
    P = Pm.merge(Pa, on=["year", "i", "j"], how="outer")
    P["src_masked"] = P.cos_masked.notna()
    P["src_minilm"] = P.cos_minilm_topk.notna()
    i, j = P.i.to_numpy(), P.j.to_numpy()
    P["cos_masked"] = np.where(found[i] & found[j], (Em[i] * Em[j]).sum(1), np.nan)
    P["cos_minilm"] = (Ea[i] * Ea[j]).sum(1)
    P["cos_bge_abs"] = (Eb[i] * Eb[j]).sum(1)
    P["cos_title"] = (Et[i] * Et[j]).sum(1)
    # mutual-NN flag and rank on masked
    P["mutual_masked"] = False
    for y in sorted(set(years)):
        idx = np.where((years == y) & found)[0]
        X = Em[idx]
        nn = np.empty(len(idx), int)
        for st in range(0, len(idx), 2000):
            S = X[st:st + 2000] @ X.T
            for r in range(S.shape[0]):
                S[r, st + r] = -1
            nn[st:st + 2000] = S.argmax(1)
        g = idx[nn]
        mut = set((min(a, b), max(a, b)) for a, b in zip(idx, g) if g[np.searchsorted(idx, b)] == a)
        m = P.year == y
        P.loc[m, "mutual_masked"] = [(a, b) in mut for a, b in zip(P.loc[m, "i"], P.loc[m, "j"])]

    sid = df.submission_id.to_numpy()
    P["sid_i"], P["sid_j"] = sid[i], sid[j]
    A = pd.read_csv(C.DATA / "submission_authors.csv.gz", usecols=["submission_id", "declared_name_json", "declared_id_key"])
    A["nm"] = A.declared_name_json.map(normname)
    keys = A.groupby("submission_id").declared_id_key.apply(lambda x: set(x.dropna()))
    names = A.groupby("submission_id").nm.apply(lambda x: set(v for v in x if v))
    P["key_ov"] = [len(keys.get(a, set()) & keys.get(b, set())) for a, b in zip(P.sid_i, P.sid_j)]
    P["name_ov"] = [len(names.get(a, set()) & names.get(b, set())) for a, b in zip(P.sid_i, P.sid_j)]
    R = pd.read_parquet(C.CACHE / "resubmissions.parquet")
    rs = set(R.prev_submission_id) | set(R.next_submission_id)
    P["resub"] = P.sid_i.isin(rs) | P.sid_j.isin(rs)
    P["title_dup"] = P.cos_title >= 0.95
    P["same_topic100"] = df.topic100.to_numpy()[i] == df.topic100.to_numpy()[j]
    ah = df.area_h.to_numpy()
    P["same_area"] = [np.nan if (pd.isna(ah[a]) or pd.isna(ah[b])) else float(ah[a] == ah[b]) for a, b in zip(i, j)]
    pool = df.pool.to_numpy()
    P["dr_or_other"] = np.isin(pool[i], ["DR", "OTHER"]) | np.isin(pool[j], ["DR", "OTHER"])  # admin filter only
    P["clean"] = (P.key_ov == 0) & (P.name_ov == 0) & ~P.resub & ~P.title_dup & ~P.dr_or_other
    P = P.drop(columns=["cos_minilm_topk"])
    P.to_parquet(OUT / "candidates.parquet")

    bands = [0.86, 0.88, 0.90, 0.92, 0.94, 1.01]
    c = P[P.clean & P.cos_masked.notna()].copy()
    c["band"] = pd.cut(c.cos_masked, bands, right=False)
    tab = c.groupby(["band", "year"], observed=False).size().unstack(fill_value=0)
    tab["total"] = tab.sum(1)
    tab.to_csv(OUT / "candidates_counts.csv")
    print("all candidate pairs", len(P), "| masked-source", P.src_masked.sum(), "| minilm-only", (~P.src_masked).sum())
    print("excluded: key", (P.key_ov > 0).sum(), "name", (P.name_ov > 0).sum(), "resub", P.resub.sum(),
          "title_dup", P.title_dup.sum(), "DR/OTHER", P.dr_or_other.sum(), "| clean", P.clean.sum())
    print(tab)
    print("clean & masked>=0.90: mutual share", round(c[c.cos_masked >= 0.90].mutual_masked.mean(), 3))
    print("clean minilm-only pairs (masked < 0.86 or missing):", int((P.clean & ~P.src_masked).sum()))


if __name__ == "__main__":
    main()
