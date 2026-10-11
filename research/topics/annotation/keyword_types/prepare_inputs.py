"""Build the annotation inputs for keyword typing: every keyword used by >=20 papers, with context.

Each line gives the keyword, its paper count, the keywords most often listed with it and two example
titles. Keywords are dealt round-robin into four batches so every batch mixes frequent and rare ones.

annotated_batch_<n>.txt are the exact files the annotators saw. They were produced by an earlier,
non-deterministic version of this script (equal counts were ordered by Python's per-process string
hashing), so a rerun reproduces the same keywords and context but may order ties differently.
This version breaks ties alphabetically and writes to regenerated/.

    python research/topics/annotation/keyword_types/prepare_inputs.py
"""
from __future__ import annotations

import collections
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from common import load_corpus  # noqa: E402

MIN_PAPERS, BATCHES = 20, 4


def main() -> None:
    out = HERE / "regenerated"
    out.mkdir(exist_ok=True)
    s = load_corpus()
    cnt = collections.Counter(k for kws in s.keywords for k in sorted(set(kws)))
    keep = sorted((k for k, v in cnt.items() if v >= MIN_PAPERS), key=lambda k: (-cnt[k], k))
    keepset = set(keep)
    co = {k: collections.Counter() for k in keep}
    titles = {k: [] for k in keep}
    for kws, title in zip(s.keywords, s.title):
        ks = set(kws)
        for k in sorted(ks & keepset):
            co[k].update(sorted(ks - {k}))
            titles[k].append(title)
    rnd = random.Random(0)
    batches = [[] for _ in range(BATCHES)]
    for i, k in enumerate(keep):
        ex = rnd.sample(titles[k], 2)
        top = [w for w, _ in sorted(co[k].items(), key=lambda x: (-x[1], x[0]))[:4]]
        batches[i % BATCHES].append(
            f"- keyword: \"{k}\" | papers: {cnt[k]} | often listed with: {'; '.join(top)} | "
            f"example titles: \"{ex[0][:90]}\"; \"{ex[1][:90]}\"")
    for j, lines in enumerate(batches):
        (out / f"batch_{j}.txt").write_text("\n".join(lines) + "\n")
    print(f"{len(keep)} keywords -> {[len(b) for b in batches]} in {out}")


if __name__ == "__main__":
    main()
