"""Batch files for labelling the released former-confirmation papers with the frozen discovery protocol.

Same protocol as returned/haiku_full_v1 (run_info.json): prompt v1 (system prompt sha256 aaa1478f...), one fresh Haiku
subagent per batch of 100 papers given as two 50-paper files ("### paper <id>" / "title:" / "abstract:"), papers
shuffled into batches; then an independent second pass on 5% of the papers with fresh agents, in separate batches.

    python prepare_released.py <out dir>
writes <out dir>/parts/{R,Q}NNN_{0,1}.md, configs.json (all batches with their paper ids), first_groups.json (the
first-pass batches in 6 groups, one workflow each) and second_args.json, plus double_label_ids.txt. Outcome-free:
reads only released.embedded_released() (ids, titles, abstracts).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2]))
from released import embedded_released  # noqa: E402

sys.path.insert(0, str(HERE.parent / "labeling_package"))
from build_package import sha256, system_prompt  # noqa: E402

SEED, BATCH, GROUPS, SECOND_SHARE = 20261018, 100, 6, 0.05
SYSTEM_SHA256 = "aaa1478fb32e1559edc1e158133a562666d64b29cdf4335bd5361509c1a42410"   # prompt v1, as in haiku_full_v1


def paper_md(r) -> str:
    return f"### paper {r.submission_id}\ntitle: {r.title}\nabstract:\n{r.abstract}\n\n"


def write_batches(papers, prefix: str, parts: Path, sizes: list[int]) -> list[dict]:
    out, start = [], 0
    for b, n in enumerate(sizes):
        chunk = papers.iloc[start:start + n]
        start += n
        bid = f"{prefix}{b:03d}"
        half = (n + 1) // 2
        for i, sub in enumerate([chunk.iloc[:half], chunk.iloc[half:]]):
            (parts / f"{bid}_{i}.md").write_text("".join(paper_md(r) for r in sub.itertuples()), encoding="utf-8")
        out.append({"id": bid, "parts": [f"{bid}_0", f"{bid}_1"], "n": n, "ids": chunk.submission_id.tolist()})
    return out


def main() -> None:
    out = Path(sys.argv[1])
    prompt = system_prompt()
    assert sha256(prompt) == SYSTEM_SHA256, "the system prompt is not prompt v1 of the discovery run"
    out.mkdir(parents=True, exist_ok=True)
    (out / "system_prompt.md").write_text(prompt, encoding="utf-8")
    parts = out / "parts"
    parts.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    corpus = embedded_released()
    corpus = corpus.assign(abstract=corpus.abstract.fillna(""), title=corpus.title.fillna(""))
    shuffled = corpus.iloc[rng.permutation(len(corpus))].reset_index(drop=True)
    n = len(shuffled)
    first = write_batches(shuffled, "R", parts, [BATCH] * (n // BATCH) + ([n % BATCH] if n % BATCH else []))
    double = shuffled.iloc[np.sort(rng.choice(n, int(round(SECOND_SHARE * n)), replace=False))]
    double = double.iloc[rng.permutation(len(double))].reset_index(drop=True)
    k = int(np.ceil(len(double) / BATCH))
    second = write_batches(double, "Q", parts, [len(a) for a in np.array_split(np.arange(len(double)), k)])
    (out / "configs.json").write_text(json.dumps(first + second))
    groups = [[{k_: c[k_] for k_ in ("id", "parts", "n")} for c in first[g::GROUPS]] for g in range(GROUPS)]
    common = {"system": str(out / "system_prompt.md"), "parts_dir": str(parts)}
    (out / "first_groups.json").write_text(json.dumps([{**common, "configs": g} for g in groups]))
    (out / "second_args.json").write_text(json.dumps({**common, "configs": [{k_: c[k_] for k_ in ("id", "parts", "n")}
                                                                            for c in second]}))
    (out / "double_label_ids.txt").write_text("\n".join(sorted(double.submission_id)) + "\n")
    print(json.dumps({"papers": n, "first_batches": len(first), "second_batches": len(second),
                      "second_papers": len(double), "groups": [len(g) for g in groups]}))


if __name__ == "__main__":
    main()
