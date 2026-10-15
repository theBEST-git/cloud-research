"""Buzzword use: listing a fast-growing keyword the paper's content does not fit (outcome-blind; PREREGISTRATION.md D5).

For each research_area / specific_topic keyword and year t, using only papers from years before t:
- eligible:  the keyword has >= 10 earlier users
- centroid:  normalised sum of the earlier users' (L2-normalised, raw) SPECTER2 vectors
- threshold: 10th percentile of the earlier users' leave-one-out cosines to the centroid of the others
- atypical:  a year-t user whose cosine to the centroid is below the threshold
- growth:    ((c[t-1] + 0.5) / N[t-1]) / ((c[t-2] + 0.5) / N[t-2]); hot = growth >= 80th percentile of eligible keywords
A paper is a *buzzword* user if it lists a hot keyword and uses it atypically. Years 2019-2026.

Writes output/keyword_year.csv.gz, output/keyword_uses.csv.gz, output/paper_buzzword.csv.gz,
output/checks/buzzwords.json and output/checks/buzzword_examples.md.

    python research/fashion/buzzwords.py
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from common import OUTPUT, TOPICS, topic_layer, write_csv_gz

TYPES = {"research_area", "specific_topic"}
MIN_EARLIER, PCT_ATYPICAL, PCT_HOT, YEARS = 10, 10, 80, (2019, 2026)


def build(keywords: pd.Series, years: np.ndarray, x: np.ndarray, vocab: set[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """keyword-year table and per-use table. keywords: list per paper; x: L2-normalised vectors (paper order)."""
    uses = [(i, k) for i, kws in enumerate(keywords) for k in set(kws) if k in vocab]
    u = pd.DataFrame(uses, columns=["paper", "keyword"])
    u["year"] = years[u.paper.to_numpy()]
    n_year = pd.Series(years).value_counts()
    kw_rows, use_rows = [], []
    for k, g in u.groupby("keyword"):
        idx, yr = g.paper.to_numpy(), g.year.to_numpy()
        counts = pd.Series(yr).value_counts()
        for t in range(YEARS[0], YEARS[1] + 1):
            prior = idx[yr < t]
            c1, c2 = counts.get(t - 1, 0), counts.get(t - 2, 0)
            growth = ((c1 + 0.5) / n_year.get(t - 1, 1)) / ((c2 + 0.5) / n_year.get(t - 2, 1))
            row = {"keyword": k, "year": t, "earlier_users": len(prior), "users": int(counts.get(t, 0)),
                   "growth": growth, "eligible": len(prior) >= MIN_EARLIER, "threshold": np.nan}
            if row["eligible"]:
                xp = x[prior]
                s = xp.sum(axis=0)
                ss = float(s @ s)
                dots = xp @ s
                loo = (dots - 1.0) / np.sqrt(np.maximum(ss - 2.0 * dots + 1.0, 1e-12))
                row["threshold"] = float(np.percentile(loo, PCT_ATYPICAL))
                cur = idx[yr == t]
                if len(cur):
                    cos = (x[cur] @ s) / np.sqrt(ss)
                    use_rows.append(pd.DataFrame({"paper": cur, "keyword": k, "year": t, "cos": cos,
                                                  "threshold": row["threshold"]}))
            kw_rows.append(row)
    kw = pd.DataFrame(kw_rows)
    kw["growth"] = kw.growth.round(10)          # logically tied growths become bit-identical (no 1-ulp tie splits)
    kw["hot"] = False
    for t, g in kw[kw.eligible].groupby("year"):
        kw.loc[g.index, "hot"] = g.growth >= np.percentile(g.growth, PCT_HOT)
    uses = pd.concat(use_rows, ignore_index=True) if use_rows else pd.DataFrame(columns=["paper", "keyword", "year", "cos", "threshold"])
    uses["atypical"] = uses.cos < uses.threshold
    uses = uses.merge(kw[["keyword", "year", "hot"]], on=["keyword", "year"], how="left")
    return kw, uses


def per_paper(uses: pd.DataFrame, n: int, years: np.ndarray) -> pd.DataFrame:
    g = uses.groupby("paper")
    out = pd.DataFrame({"n_eligible_keywords": g.size(), "lists_hot": g.hot.any(),
                        "buzzword": g.apply(lambda d: bool((d.hot & d.atypical).any()), include_groups=False)})
    out = out.reindex(range(n))
    in_years = (years >= YEARS[0]) & (years <= YEARS[1])
    out["n_eligible_keywords"] = out.n_eligible_keywords.fillna(0).astype(int)
    for c in ["lists_hot", "buzzword"]:
        out[c] = out[c].astype("boolean").fillna(False).astype(float)
        out.loc[~in_years, c] = np.nan
    out.loc[~in_years, "n_eligible_keywords"] = 0
    return out


def main() -> None:
    tl = topic_layer()
    corpus = tl.embedded_corpus()
    emb, ids = tl.load_embeddings()
    assert ids.equals(corpus.submission_id)
    x = emb.astype(np.float64)
    x /= np.linalg.norm(x, axis=1, keepdims=True)
    years = corpus.year.to_numpy()
    kt = pd.read_csv(TOPICS / "keyword_types.csv", keep_default_na=False)
    vocab = set(kt[kt.type.isin(TYPES)].keyword)
    kw, uses = build(corpus.keywords, years, x, vocab)
    paper = per_paper(uses, len(corpus), years)
    sid = corpus.submission_id.to_numpy()
    uses_out = uses.assign(submission_id=sid[uses.paper.to_numpy()]).drop(columns="paper")
    paper_out = paper.assign(submission_id=sid, year=years)[["submission_id", "year", "n_eligible_keywords", "lists_hot", "buzzword"]]
    write_csv_gz(kw.round(6), OUTPUT / "keyword_year.csv.gz")
    write_csv_gz(uses_out.round(6), OUTPUT / "keyword_uses.csv.gz")
    write_csv_gz(paper_out, OUTPUT / "paper_buzzword.csv.gz")

    hot_uses, cold_uses = uses[uses.hot], uses[~uses.hot]
    flags = uses[uses.hot & uses.atypical]
    in_y = paper_out.year.between(*YEARS)
    checks = {
        "vocabulary": len(vocab),
        "eligible_keywords_by_year": kw[kw.eligible].groupby("year").size().to_dict(),
        "hot_keywords_by_year": kw[kw.hot].groupby("year").size().to_dict(),
        "top_hot_keywords_by_year": {int(t): g.sort_values("growth", ascending=False).keyword.head(12).tolist()
                                     for t, g in kw[kw.hot].groupby("year")},
        "atypical_rate_hot_uses": round(float(hot_uses.atypical.mean()), 4),
        "atypical_rate_other_eligible_uses": round(float(cold_uses.atypical.mean()), 4),
        "atypical_rate_by_year": uses.groupby("year").atypical.mean().round(4).to_dict(),
        "paper_share_listing_hot_keyword_by_year": paper_out[in_y].groupby("year").lists_hot.mean().round(4).to_dict(),
        "buzzword_rate_by_year": paper_out[in_y].groupby("year").buzzword.mean().round(4).to_dict(),
        "flagged_uses": int(len(flags)),
        "flag_concentration_top10_keywords": flags.keyword.value_counts().head(10).to_dict(),
        "share_of_flags_on_top_keyword": round(float(flags.keyword.value_counts(normalize=True).iloc[0]), 4) if len(flags) else None,
    }
    (OUTPUT / "checks").mkdir(parents=True, exist_ok=True)
    (OUTPUT / "checks" / "buzzwords.json").write_text(json.dumps(checks, indent=2, default=int) + "\n")
    rng = np.random.default_rng(5)
    lines = ["# Buzzword examples (for reading only)\n"]
    titles = corpus.title.to_numpy()
    for t in range(YEARS[0], YEARS[1] + 1):
        f, ty = flags[flags.year == t], hot_uses[(hot_uses.year == t) & ~hot_uses.atypical]
        lines.append(f"\n## {t}\n\nFlagged (hot keyword, atypical use):\n")
        for _, r in f.sample(min(10, len(f)), random_state=int(rng.integers(1e9))).iterrows():
            lines.append(f"- `{r.keyword}` (cos {r.cos:.3f} < {r.threshold:.3f}): {titles[r.paper]}")
        lines.append("\nTypical use of a hot keyword:\n")
        for _, r in ty.sample(min(10, len(ty)), random_state=int(rng.integers(1e9))).iterrows():
            lines.append(f"- `{r.keyword}` (cos {r.cos:.3f}): {titles[r.paper]}")
    (OUTPUT / "checks" / "buzzword_examples.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({k: v for k, v in checks.items() if k != "top_hot_keywords_by_year"}, indent=1, default=int))


if __name__ == "__main__":
    main()
