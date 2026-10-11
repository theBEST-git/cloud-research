"""Prepare the material used to name topics and to check the names blind.

Writes to annotation/:
- naming_batch_<n>.md   broad topics with their middle and fine topics: size, papers per year,
                        distinctive keywords and example titles (input for the naming annotators)
- name_check_papers.md  one random paper per fine topic (title + abstract opening) for the blind check
- name_check_truth.json the fine topic each check paper belongs to (kept away from the check annotators)

    python research/topics/naming_inputs.py
"""
from __future__ import annotations

import json

import pandas as pd

from common import HERE, OUTPUT, embedded_corpus

ANNOTATION = HERE / "annotation"
BATCHES = 5


def main() -> None:
    ANNOTATION.mkdir(exist_ok=True)
    cat = pd.read_csv(OUTPUT / "topic_catalog_auto.csv", keep_default_na=False)
    years = [c for c in cat.columns if c.startswith("y20")]
    corpus = embedded_corpus().merge(pd.read_csv(OUTPUT / "topic_assignments.csv.gz"), on=["submission_id", "year"])

    def describe(r, heading, n_titles):
        per_year = ", ".join(f"{c[1:]}:{r[c]}" for c in years if r[c])
        titles = corpus[corpus[r.level] == r.topic].sample(min(n_titles, r.papers), random_state=1).title
        lines = [f"{heading} {r.topic} — {r.papers} papers (per year {per_year})",
                 f"distinctive keywords: {r.keyword_signature or '(none)'}", "example titles:"]
        return lines + [f"  - {t[:150]}" for t in titles]

    coarse = cat[cat.level == "coarse"].sort_values("topic")
    n_fine = cat[cat.level == "fine"].groupby("parent_coarse").size()
    batches = [[] for _ in range(BATCHES)]
    load = [0] * BATCHES
    for c in sorted(coarse.topic, key=lambda c: -n_fine[c]):           # balance fine-topic counts across batches
        b = load.index(min(load)); batches[b].append(c); load[b] += n_fine[c]
    for b, members in enumerate(batches, 1):
        out = []
        for c in sorted(members):
            out += describe(coarse[coarse.topic == c].iloc[0], "# BROAD", 12) + [""]
            for _, m in cat[(cat.level == "mid") & (cat.parent_coarse == c)].sort_values("topic").iterrows():
                out += ["  " + x for x in describe(m, "## MIDDLE", 8)] + [""]
                for _, f in cat[(cat.level == "fine") & (cat.parent_mid == m.topic)].sort_values("topic").iterrows():
                    out += ["    " + x for x in describe(f, "### FINE", 8)] + [""]
        (ANNOTATION / f"naming_batch_{b}.md").write_text("\n".join(out) + "\n")
        print(f"batch {b}: broad topics {sorted(members)} ({load[b - 1]} fine topics)")

    check = corpus.groupby("fine", group_keys=False).apply(lambda g: g.sample(1, random_state=7)).sample(frac=1, random_state=7)
    lines, truth = [], {}
    for i, r in enumerate(check.itertuples(), 1):
        pid = f"p{i:03d}"
        truth[pid] = {"fine": r.fine, "mid": r.mid, "coarse": r.coarse}
        lines += [f"- paper {pid} | broad topic {r.coarse} | title: {r.title[:200]}",
                  f"  abstract opening: {' '.join(r.abstract.split()[:60])} ..."]
    (ANNOTATION / "name_check_papers.md").write_text("\n".join(lines) + "\n")
    (ANNOTATION / "name_check_truth.json").write_text(json.dumps(truth, indent=1) + "\n")
    print(f"name check: {len(truth)} papers, one per fine topic")


if __name__ == "__main__":
    main()
