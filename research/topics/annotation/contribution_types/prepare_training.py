"""Sample and batch ~2,000 papers for the classifier training set (contribution type + foundation model).

- excludes the 200 open-coding and 300 pilot papers
- 1,700 random papers (proportional to the corpus) + 300 enriched for rare contribution types
- batches of 100 papers; abstracts wrapped so no line is cut when annotators read the file
- writes the annotator instructions: codebook v1 plus the foundation-model rule from facets codebook v1, verbatim

    python research/topics/annotation/contribution_types/prepare_training.py
"""
from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
OUT = HERE / "training"
sys.path.insert(0, str(HERE.parents[1]))
from common import embedded_corpus  # noqa: E402

SEED, RANDOM_N, BATCH = 31, 1700, 100
ENRICH = {   # stratum: (cue pattern on title + abstract, papers)
    "enriched_benchmark": (r"\bwe (?:introduce|present|release|construct|curate|build)\b.{0,40}\b(?:benchmark|dataset|corpus)", 80),
    "enriched_theory": (r"\bwe (?:prove|derive|establish)\b|\b(?:theorem|lower bound|sample complexity|convergence rate)\b", 70),
    "enriched_empirical": (r"\bwe (?:investigate|study|analy[sz]e|examine)\b|\b(?:empirical|systematic|large-scale) (?:study|analysis)\b", 60),
    "enriched_evaluation": (r"\b(?:new|novel) (?:metric|evaluation protocol|evaluation framework)\b|\bwe propose\b.{0,30}\b(?:metric|evaluation)\b", 50),
    "enriched_other": (r"\b(?:this survey|we survey|position paper|we argue that|toolkit|software library|open-source platform|case study|deployed)\b", 40),
}


def instructions() -> str:
    codebook = (HERE / "codebook.md").read_text().split("## Pilot evidence")[0].rstrip()
    facets = (HERE / "facets_codebook.md").read_text()
    fm = re.search(r"## Foundation model \(yes/no\)\n(.*?)(?=\n## )", facets, re.S).group(1).strip()
    return (f"{codebook}\n\n## Foundation model (yes/no)\n\n"
            "Also record `foundation_model` for the paper's main contribution, using this rule from facets codebook v1:\n\n"
            f"{fm}\n")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / "instructions.md").write_text(instructions())
    corpus = embedded_corpus()
    used = set(pd.read_csv(HERE / "open_coding_sample.csv").submission_id) | set(pd.read_csv(HERE / "pilot_sample.csv").submission_id)
    pool = corpus[~corpus.submission_id.isin(used)]
    picked = pool.sample(RANDOM_N, random_state=SEED).assign(stratum="random")
    text = (pool.title + " " + pool.abstract).str.lower()
    for name, (pattern, n) in ENRICH.items():
        cand = pool[text.str.contains(pattern, regex=True) & ~pool.submission_id.isin(picked.submission_id)]
        picked = pd.concat([picked, cand.sample(n, random_state=SEED).assign(stratum=name)])
    picked = picked.sample(frac=1, random_state=SEED).reset_index(drop=True)
    picked["paper"] = [f"t{i + 1:04d}" for i in range(len(picked))]
    picked["batch"] = picked.index // BATCH + 1
    picked[["paper", "submission_id", "year", "stratum", "batch"]].to_csv(OUT / "training_sample.csv", index=False)
    for b, part in picked.groupby("batch"):
        blocks = []
        for r in part.itertuples():
            abstract = textwrap.fill(" ".join(r.abstract.split()), width=300)
            blocks.append(f"### paper {r.paper}\ntitle: {r.title.strip()}\nabstract:\n{abstract}\n")
        (OUT / f"batch_{b:02d}.md").write_text("\n".join(blocks))
    print(f"{len(picked)} papers in {picked.batch.nunique()} batches | strata {picked.stratum.value_counts().to_dict()}")
    print("years:", picked.year.value_counts().sort_index().to_dict())


if __name__ == "__main__":
    main()
