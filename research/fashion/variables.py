"""RQ2/RQ3 paper-level variables for every topic map (outcome-blind; PREREGISTRATION.md D1-D4, D9, S1, S3-S5).

Per paper and map:
- incumbent:     at least one author (exact declared_id_key) has a submission in the same topic in an earlier year
- newcomer:      1 - incumbent
- incumbent_w2:  same, but only years t-1 and t-2 count (S3)
- incumbent_s4:  same as incumbent, ignoring the paper's own chain of probable earlier versions (S4; needs earlier_versions)
- hot:           the topic's prior_growth is at or above the 80th percentile of the map's topics in year t (D3)
Per paper: team_size (distinct author keys), has_author_key.
Maps: the seven in common.topic_maps() plus `fine` (S5). Every variable uses only papers from years before t.

Writes output/paper_variables.csv.gz (long: one row per paper and map) and output/checks/variables.json.

    python research/fashion/variables.py
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from common import DATA, OUTPUT, TOPICS, topic_maps, write_csv_gz
from topic_maturity import maturity

HOT_PERCENTILE = 80
CHECKS = OUTPUT / "checks"


def load_authors(ids: pd.Series) -> pd.DataFrame:
    """Author rows (submission_id, key, kind) for the given papers; rows without a key are dropped (D2)."""
    a = pd.read_csv(DATA / "submission_authors.csv.gz", keep_default_na=False, na_values=[r"\N"],
                    usecols=["submission_id", "declared_id_key", "native_id_kind"])
    a = a[a.declared_id_key.notna() & a.submission_id.isin(set(ids))]
    return a.rename(columns={"declared_id_key": "key", "native_id_kind": "kind"}).drop_duplicates(["submission_id", "key"])


def incumbency(authors: pd.DataFrame, topic: pd.Series, year: pd.Series, ids: pd.Series,
               earlier: pd.Series | None = None) -> pd.DataFrame:
    """incumbent, incumbent_w2 and incumbent_s4 for each paper (index = submission_id).

    topic/year/ids are aligned per paper. earlier maps submission_id -> probable earlier version id (S4) or is None.
    """
    papers = pd.DataFrame({"submission_id": ids.values, "topic": topic.values, "year": year.values})
    at = authors[["submission_id", "key"]].merge(papers, on="submission_id")
    # papers per (author, topic, year), and how many of them came before year t
    cnt = at.groupby(["key", "topic", "year"]).size().rename("n").reset_index().sort_values(["key", "topic", "year"])
    cnt["n_prior"] = cnt.groupby(["key", "topic"]).n.cumsum() - cnt.n
    at = at.merge(cnt[["key", "topic", "year", "n_prior"]], on=["key", "topic", "year"])
    present = set(zip(cnt.key, cnt.topic, cnt.year))
    at["w2"] = [(k, t, y - 1) in present or (k, t, y - 2) in present for k, t, y in zip(at.key, at.topic, at.year)]
    at["adjust"] = 0
    if earlier is not None and len(earlier):
        # the paper's own chain of earlier versions (earlier version, its earlier version, ...), same topic, earlier year
        ev = earlier.dropna().to_dict()
        rows = []
        for sid in ev:
            e, seen = ev[sid], set()
            while e is not None and e not in seen:
                rows.append((sid, e))
                seen.add(e)
                e = ev.get(e)
        pairs = pd.DataFrame(rows, columns=["submission_id", "earlier"])
        p_topic = papers.set_index("submission_id").topic
        p_year = papers.set_index("submission_id").year
        pairs = pairs[pairs.submission_id.isin(p_topic.index) & pairs.earlier.isin(p_topic.index)]
        pairs = pairs[(p_topic.loc[pairs.earlier].values == p_topic.loc[pairs.submission_id].values)
                      & (p_year.loc[pairs.earlier].values < p_year.loc[pairs.submission_id].values)]
        on_earlier = authors[["submission_id", "key"]].rename(columns={"submission_id": "earlier"})
        hit = pairs.merge(on_earlier, on="earlier").groupby(["submission_id", "key"]).size().rename("hit").reset_index()
        at = at.merge(hit, on=["submission_id", "key"], how="left")
        at["adjust"] = at.hit.fillna(0).astype(int)
    g = at.assign(inc=at.n_prior >= 1, inc_s4=(at.n_prior - at.adjust) >= 1).groupby("submission_id")
    out = pd.DataFrame({"incumbent": g.inc.any(), "incumbent_w2": g.w2.any(), "incumbent_s4": g.inc_s4.any()})
    return out.astype(float)


def hot_flags(mat: pd.DataFrame) -> pd.DataFrame:
    """hot per (topic, year): prior_growth >= 80th percentile (numpy linear) of that year's topics; NaN before 2019."""
    out = []
    for y, g in mat.groupby("year"):
        g = g[["topic", "year", "prior_growth"]].copy()
        if g.prior_growth.notna().all():
            g["hot"] = (g.prior_growth >= np.percentile(g.prior_growth, HOT_PERCENTILE)).astype(float)
        else:
            g["hot"] = np.nan
        out.append(g)
    return pd.concat(out, ignore_index=True)


def main() -> None:
    CHECKS.mkdir(parents=True, exist_ok=True)
    maps = topic_maps()
    fine = pd.read_csv(TOPICS / "topic_assignments.csv.gz")
    assert fine.submission_id.equals(maps.submission_id)
    maps["fine"] = fine.fine
    mat_all = pd.read_csv(OUTPUT / "topic_year_maturity.csv.gz")
    mat_fine = maturity(maps.fine, maps.year).assign(map="fine")
    mat_all = pd.concat([mat_all, mat_fine], ignore_index=True)

    authors = load_authors(maps.submission_id)
    team = authors.groupby("submission_id").key.nunique()
    ev_path = OUTPUT / "earlier_versions.csv.gz"
    earlier = None
    if ev_path.exists():
        ev = pd.read_csv(ev_path)
        if "probable_earlier_version" in ev:
            earlier = ev.set_index("submission_id").probable_earlier_version
    names = [c for c in maps.columns if c not in ("submission_id", "year")]
    frames, checks = [], {"maps": names, "papers": int(len(maps)),
                          "papers_without_author_key": int((~maps.submission_id.isin(team.index)).sum()),
                          "s4_available": earlier is not None, "by_map": {}}
    for m in names:
        inc = incumbency(authors, maps[m], maps.year, maps.submission_id, earlier)
        hot = hot_flags(mat_all[mat_all["map"] == m])
        df = maps[["submission_id", "year"]].assign(map=m, topic=maps[m].astype(str).values)
        hot["topic"] = hot.topic.astype(str)
        df = df.merge(hot, on=["topic", "year"], how="left").merge(inc, left_on="submission_id", right_index=True, how="left")
        df["has_author_key"] = df.submission_id.isin(team.index)
        df["team_size"] = df.submission_id.map(team).fillna(0).astype(int)
        for c in ["incumbent", "incumbent_w2", "incumbent_s4"]:
            df.loc[~df.has_author_key, c] = np.nan
        if earlier is None:
            df["incumbent_s4"] = np.nan
        df["newcomer"] = 1 - df.incumbent
        frames.append(df)
        keyed = df[df.has_author_key]
        checks["by_map"][m] = {
            "incumbent_rate_by_year": keyed.groupby("year").incumbent.mean().round(4).to_dict(),
            "incumbent_w2_rate_by_year": keyed.groupby("year").incumbent_w2.mean().round(4).to_dict(),
            "hot_topics_by_year": hot.groupby("year").hot.sum().to_dict(),
            "paper_share_in_hot_topics_by_year": df.groupby("year").hot.mean().round(4).to_dict(),
            "hot_persistence": float(hot.pivot(index="topic", columns="year", values="hot")
                                     .pipe(lambda w: np.nanmean([(w[y] * w[y - 1]).sum() / max(w[y].sum(), 1)
                                                                 for y in range(2020, 2027)]))),
        }
    out = pd.concat(frames, ignore_index=True)
    cols = ["submission_id", "year", "map", "topic", "has_author_key", "team_size", "incumbent", "newcomer",
            "incumbent_w2", "incumbent_s4", "prior_growth", "hot"]
    write_csv_gz(out[cols], OUTPUT / "paper_variables.csv.gz")

    k = out[(out["map"] == "k100") & out.has_author_key]
    bins = pd.cut(k.team_size, [0, 1, 2, 4, 8, 1000], labels=["1", "2", "3-4", "5-8", "9+"])
    era = pd.cut(k.year, [2016, 2020, 2022, 2026], labels=["2017-20 (email ids)", "2021-22 (switch)", "2023-26 (profile ids)"])
    checks["k100_incumbent_rate_by_team_size_and_era"] = (k.groupby([era, bins], observed=True).incumbent.mean()
                                                          .round(4).unstack().to_dict(orient="index"))
    e = out[(out["map"] == "early") & out.has_author_key].set_index("submission_id").incumbent
    checks["incumbent_agreement_k100_vs_early_map"] = round(float((k.set_index("submission_id").incumbent == e.loc[k.submission_id]).mean()), 4)
    cat = pd.read_csv(TOPICS / "topic_catalog.csv", keep_default_na=False).set_index("topic").name
    hk = out[(out["map"] == "k100")].drop_duplicates(["topic", "year"])
    checks["k100_hot_topics"] = {int(y): [f"{t} {cat.get(t, '')}" for t in sorted(g[g.hot == 1].topic)]
                                 for y, g in hk.groupby("year") if g.hot.notna().all()}
    (CHECKS / "variables.json").write_text(json.dumps(checks, indent=2, default=str) + "\n")
    print(json.dumps({m: {"incumbent_2019": v["incumbent_rate_by_year"].get(2019), "incumbent_2023": v["incumbent_rate_by_year"].get(2023),
                          "incumbent_2026": v["incumbent_rate_by_year"].get(2026)} for m, v in checks["by_map"].items()}, indent=1))


if __name__ == "__main__":
    main()
