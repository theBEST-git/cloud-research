"""Sample 300 fresh papers (none from open coding) to pilot the contribution-type codebook.

- 240 random papers drawn in proportion to the corpus (prevalence and agreement estimates use these)
- 60 enriched papers, 20 each likely to be benchmark/dataset, theory, or survey/position/system,
  so rare types are tested too (stratum recorded; excluded from prevalence estimates)
Writes four batches of 75 (title + abstract) and pilot_sample.csv.

    python research/topics/annotation/contribution_types/prepare_pilot.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from common import embedded_corpus  # noqa: E402

SEED, RANDOM_N, ENRICH_N, BATCHES = 23, 240, 20, 4
ENRICH = {
    "enriched_benchmark": r"\bwe (?:introduce|present|release|construct|curate|build)\b.{0,40}\b(?:benchmark|dataset|corpus)",
    "enriched_theory": r"\bwe (?:prove|derive|establish)\b|\b(?:theorem|lower bound|sample complexity)\b",
    "enriched_survey_system": r"\b(?:this survey|we survey|position paper|we argue that|open-source (?:library|toolkit|framework)|software library|toolkit)\b",
}


def main() -> None:
    corpus = embedded_corpus()
    used = set(pd.read_csv(HERE / "open_coding_sample.csv").submission_id)
    pool = corpus[~corpus.submission_id.isin(used)]
    picked = pool.sample(RANDOM_N, random_state=SEED).assign(stratum="random")
    text = (pool.title + " " + pool.abstract).str.lower()
    for name, pattern in ENRICH.items():
        cand = pool[text.str.contains(pattern, regex=True) & ~pool.submission_id.isin(picked.submission_id)]
        picked = pd.concat([picked, cand.sample(ENRICH_N, random_state=SEED).assign(stratum=name)])
    picked = picked.sample(frac=1, random_state=SEED).reset_index(drop=True)
    picked["paper"] = [f"p{i + 1:03d}" for i in range(len(picked))]
    picked[["paper", "submission_id", "year", "stratum"]].to_csv(HERE / "pilot_sample.csv", index=False)
    size = len(picked) // BATCHES
    for b in range(BATCHES):
        part = picked.iloc[b * size:(b + 1) * size]
        lines = [f"### paper {r.paper}\ntitle: {r.title.strip()}\nabstract: {' '.join(r.abstract.split())}\n" for r in part.itertuples()]
        (HERE / f"pilot_batch_{b + 1}.md").write_text("\n".join(lines))
    print(picked.stratum.value_counts().to_dict(), "| years:", picked.year.value_counts().sort_index().to_dict())


if __name__ == "__main__":
    main()
