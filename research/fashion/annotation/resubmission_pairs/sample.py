"""Blind calibration sample for the resubmission threshold tau (PREREGISTRATION.md R1, D15). Outcome-free.

draw() rebuilds the design from output/earlier_versions.csv.gz and a fixed seed: 40 (paper, nearest earlier-year
paper) pairs from each of the four centred-cosine bins in resubmissions.TAU_BINS, plus 8 pilot pairs from the same
bins outside the sample. Pairs get random ids; the bin is never shown. Each judge gets its own shuffle into batches
of 20. No key file is written: score.py calls draw() again.

    python research/fashion/annotation/resubmission_pairs/sample.py      # writes batches/ and manifest.json
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
from resubmissions import TAU_BINS  # noqa: E402

SEED = 20261016
PER_BIN, PILOT_PER_BIN, BATCH = 40, 2, 20
JUDGES = ("haiku_a", "haiku_b", "sonnet_a")
BATCHES = HERE / "batches"


def draw() -> tuple[pd.DataFrame, pd.DataFrame]:
    """(sample, pilot). Columns: pair_id, bin (index into TAU_BINS), submission_id (B, later), nn_id (A, earlier), nn_cos."""
    rng = np.random.default_rng(SEED)
    ev = pd.read_csv(OUTPUT / "earlier_versions.csv.gz").dropna(subset=["nn_id"])
    ev = ev.sort_values("submission_id", kind="stable").reset_index(drop=True)
    sample, pilot = [], []
    for b, (lo, hi) in enumerate(TAU_BINS):
        pool = ev[(ev.nn_cos >= lo) & (ev.nn_cos < hi)]
        pick = pool.iloc[rng.permutation(len(pool))[: PER_BIN + PILOT_PER_BIN]].assign(bin=b)
        sample.append(pick.iloc[:PER_BIN])
        pilot.append(pick.iloc[PER_BIN:])
    cols = ["bin", "submission_id", "nn_id", "nn_cos"]
    sample = pd.concat(sample, ignore_index=True)[cols]
    pilot = pd.concat(pilot, ignore_index=True)[cols]
    pilot = pilot.iloc[rng.permutation(len(pilot))].reset_index(drop=True)
    ids = rng.choice(16 ** 6, len(sample) + len(pilot), replace=False)
    names = [f"R{i:06x}" for i in ids]
    sample.insert(0, "pair_id", names[: len(sample)])
    pilot.insert(0, "pair_id", names[len(sample):])
    return sample, pilot


def batches_for(sample: pd.DataFrame, judge: int) -> list[list[str]]:
    rng = np.random.default_rng(SEED + 1 + judge)
    order = list(rng.permutation(sample.pair_id.to_numpy()))
    return [order[i:i + BATCH] for i in range(0, len(order), BATCH)]


def pair_text(pair_id: str, a: tuple[str, str], b: tuple[str, str]) -> str:
    clean = lambda s: " ".join(str(s).split())
    return (f"### pair {pair_id}\n\n**Paper A (submitted earlier)**\n\nTitle: {clean(a[0])}\n\nAbstract: {clean(a[1])}\n\n"
            f"**Paper B (submitted later)**\n\nTitle: {clean(b[0])}\n\nAbstract: {clean(b[1])}\n")


def write() -> None:
    sample, pilot = draw()
    corpus = topic_layer().embedded_corpus().set_index("submission_id")
    ta = lambda s: (corpus.title[s], corpus.abstract[s])
    text = {r.pair_id: pair_text(r.pair_id, ta(r.nn_id), ta(r.submission_id)) for df in (sample, pilot) for r in df.itertuples()}
    manifest = {"seed": SEED, "bins": TAU_BINS, "pairs": len(sample), "pilot_pairs": len(pilot), "files": {}}
    BATCHES.mkdir(exist_ok=True)

    def put(path: Path, items: list[str], header: str) -> None:
        body = header + "\n" + "\n".join(text[i] for i in items)
        path.write_text(body, encoding="utf-8")
        manifest["files"][str(path.relative_to(HERE))] = {"items": items, "sha256": hashlib.sha256(body.encode()).hexdigest()}

    put(BATCHES / "pilot.md", pilot.pair_id.tolist(), f"# Pilot batch ({len(pilot)} pairs)\n")
    for j, judge in enumerate(JUDGES):
        (BATCHES / judge).mkdir(exist_ok=True)
        for b, items in enumerate(batches_for(sample, j)):
            put(BATCHES / judge / f"b{b}.md", items, f"# Batch {b} ({len(items)} pairs)\n")
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    print(f"{len(sample)} pairs ({sample.groupby('bin').size().to_dict()} per bin); {len(pilot)} pilot pairs")


if __name__ == "__main__":
    write()
