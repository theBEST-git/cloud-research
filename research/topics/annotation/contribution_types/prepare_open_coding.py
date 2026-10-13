"""Sample papers for open coding of contribution types (step 2: discover which types exist).

20 random papers per year, 2017-2026 (seeded), so early years are not swamped by 2025-26.
Annotators see only title and abstract. Writes four mixed-year batches of 50.

    python research/topics/annotation/contribution_types/prepare_open_coding.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from common import embedded_corpus  # noqa: E402

PER_YEAR, BATCHES, SEED = 20, 4, 11


def main() -> None:
    corpus = embedded_corpus()
    sample = corpus.groupby("year").sample(PER_YEAR, random_state=SEED).sample(frac=1, random_state=SEED).reset_index(drop=True)
    sample["paper"] = [f"q{i + 1:03d}" for i in range(len(sample))]
    sample[["paper", "submission_id", "year"]].to_csv(HERE / "open_coding_sample.csv", index=False)
    size = len(sample) // BATCHES
    for b in range(BATCHES):
        part = sample.iloc[b * size:(b + 1) * size]
        lines = [f"### paper {r.paper}\ntitle: {r.title.strip()}\nabstract: {' '.join(r.abstract.split())}\n" for r in part.itertuples()]
        (HERE / f"open_coding_batch_{b + 1}.md").write_text("\n".join(lines))
    print(f"{len(sample)} papers -> {BATCHES} batches; years: {sample.year.value_counts().sort_index().to_dict()}")


if __name__ == "__main__":
    main()
