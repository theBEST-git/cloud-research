"""Blind validation sample for the buzzword measure (PREREGISTRATION.md D6). Outcome-free.

draw() rebuilds the whole design from output/keyword_uses.csv.gz and a fixed seed:
- 100 flagged uses (hot keyword, atypical use), at most one per paper;
- each paired with a non-flagged use (cosine at or above the threshold) of the same keyword in the same year (nearest
  year if none), from a paper not used elsewhere in the sample;
- 20 pilot items (10 flagged, 10 non-flagged) from papers outside the sample, for the format check only.
Items get random ids. For each judge, the two items of a pair go to different batches, and each judge has its own
shuffle. No key file is written: score.py calls draw() again.

    python research/fashion/annotation/keyword_centrality/sample.py      # writes batches/ and manifest.json
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from common import OUTPUT, topic_layer  # noqa: E402

SEED = 20261015
N_PAIRS, N_PILOT, BATCH = 100, 20, 25
JUDGES = ("sonnet_a", "sonnet_b", "haiku_a")
BATCHES = HERE / "batches"


def draw() -> tuple[pd.DataFrame, pd.DataFrame]:
    """(sample, pilot). sample: item_id, pair, role (flagged / nonflagged), submission_id, keyword, year."""
    rng = np.random.default_rng(SEED)
    u = pd.read_csv(OUTPUT / "keyword_uses.csv.gz").sort_values(["year", "keyword", "submission_id"], kind="stable")
    u = u.reset_index(drop=True)
    flagged = u[u.hot & u.atypical]
    flagged = flagged.iloc[rng.permutation(len(flagged))].drop_duplicates("submission_id")
    typical = u[~u.atypical]
    used, rows = set(), []
    for _, f in flagged.iterrows():
        if len(rows) == 2 * N_PAIRS:
            break
        if f.submission_id in used:
            continue
        cand = typical[(typical.keyword == f.keyword) & ~typical.submission_id.isin(used | {f.submission_id})]
        if not len(cand):
            continue
        gap = (cand.year - f.year).abs()
        best = cand[gap == gap.min()]
        best = best[best.year == best.year.min()]                     # tie between t-d and t+d: the earlier year
        nf = best.iloc[rng.integers(len(best))]
        pair = len(rows) // 2
        rows.append({"pair": pair, "role": "flagged", "submission_id": f.submission_id, "keyword": f.keyword, "year": f.year})
        rows.append({"pair": pair, "role": "nonflagged", "submission_id": nf.submission_id, "keyword": nf.keyword, "year": nf.year})
        used |= {f.submission_id, nf.submission_id}
    sample = pd.DataFrame(rows)
    pf = flagged[~flagged.submission_id.isin(used)].head(N_PILOT // 2)
    rest = typical[~typical.submission_id.isin(used | set(pf.submission_id))].drop_duplicates("submission_id")
    pn = rest.iloc[rng.permutation(len(rest))[: N_PILOT // 2]]
    pilot = pd.concat([pf.assign(role="flagged"), pn.assign(role="nonflagged")])[["role", "submission_id", "keyword", "year"]]
    pilot = pilot.iloc[rng.permutation(len(pilot))].reset_index(drop=True)
    ids = rng.choice(16 ** 6, len(sample) + len(pilot), replace=False)
    names = [f"K{i:06x}" for i in ids]
    sample["item_id"], pilot["item_id"] = names[: len(sample)], names[len(sample):]
    return sample, pilot


def batches_for(sample: pd.DataFrame, judge: int) -> list[list[str]]:
    """Judge-specific batches: one member of each pair in the first half of the batches, the other in the second."""
    rng = np.random.default_rng(SEED + 1 + judge)
    halves = [[], []]
    for p in rng.permutation(sample.pair.unique()):
        a, b = sample[sample.pair == p].item_id.tolist()
        first = rng.integers(2)
        halves[first].append(a)
        halves[1 - first].append(b)
    out = []
    for h in halves:
        h = list(rng.permutation(h))
        out += [h[i:i + BATCH] for i in range(0, len(h), BATCH)]
    return [out[i] for i in rng.permutation(len(out))]


def item_text(item_id: str, keyword: str, title: str, abstract: str) -> str:
    return f"### item {item_id}\n\nKeyword: {keyword}\n\nTitle: {title.strip()}\n\nAbstract: {' '.join(abstract.split())}\n"


def write() -> None:
    sample, pilot = draw()
    corpus = topic_layer().embedded_corpus().set_index("submission_id")
    text = {r.item_id: item_text(r.item_id, r.keyword, corpus.title[r.submission_id], corpus.abstract[r.submission_id])
            for df in (sample, pilot) for r in df.itertuples()}
    manifest = {"seed": SEED, "pairs": int(sample.pair.nunique()), "pilot_items": len(pilot), "files": {}}
    BATCHES.mkdir(exist_ok=True)

    def put(path: Path, items: list[str], header: str) -> None:
        body = header + "\n" + "\n".join(text[i] for i in items)
        path.write_text(body, encoding="utf-8")
        manifest["files"][str(path.relative_to(HERE))] = {"items": items, "sha256": hashlib.sha256(body.encode()).hexdigest()}

    put(BATCHES / "pilot.md", pilot.item_id.tolist(), f"# Pilot batch ({len(pilot)} items)\n")
    for j, judge in enumerate(JUDGES):
        (BATCHES / judge).mkdir(exist_ok=True)
        for b, items in enumerate(batches_for(sample, j)):
            put(BATCHES / judge / f"b{b}.md", items, f"# Batch {b} ({len(items)} items)\n")
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    print(f"{len(sample)} items in {sample.pair.nunique()} pairs; {len(pilot)} pilot items; "
          f"years {sample.year.min()}-{sample.year.max()}; keywords {sample.keyword.nunique()}; "
          f"non-flagged from another year: {int((sample[sample.role == 'nonflagged'].year.values != sample[sample.role == 'flagged'].year.values).sum())}")


if __name__ == "__main__":
    write()
