"""Collect and merge the labels of the released former-confirmation papers (same protocol as haiku_full_v1).

    python merge_released.py <prepare_released.py out dir> <workflow transcript dir> [...]

1. Reads every agent result from the label_batches.js journals and keeps, per batch, the labels of that batch's own
   papers (first answer per paper; a secondary type equal to the primary becomes "none", as for discovery). Writes
   returned/haiku_released_v1/{labels.jsonl, labels_second_pass.jsonl, double_label_ids.txt, run_info.json}.
2. Checks them with merge_labels.load (format, valid values, no duplicates) and coverage (every released paper with
   text exactly once; the second pass exactly the 5% sample).
3. Writes research/topics/output/paper_contributions_released.csv.gz (the columns of paper_contributions.csv.gz) and
   contribution_labels_quality_released.json: second-pass agreement and kappa, class and FM shares by year, next to
   the discovery shares of the same years (a drift check). Outcome-free.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2]))
from common import OUTPUT, write_csv_gz  # noqa: E402
from merge_labels import cls, compare, load  # noqa: E402
from released import embedded_released  # noqa: E402

RUN = HERE / "returned" / "haiku_released_v1"


def collect(configs: dict, journals: list[Path]) -> dict[str, dict]:
    got = {}
    for d in journals:
        label_of = {}
        for line in open(d / "journal.jsonl", encoding="utf-8"):
            r = json.loads(line)
            if r.get("type") == "started":
                label_of[r["agentId"]] = r["label"]
            if r.get("type") == "result":
                bid = label_of[r["agentId"]].split(" ")[0]
                if bid not in configs:          # a batch of the other pass
                    continue
                want = set(configs[bid]["ids"])
                for x in (r["result"] or {}).get("labels") or []:
                    if x["paper_id"] in want and x["paper_id"] not in got:
                        if x["secondary_type"] == x["primary_type"]:
                            x["secondary_type"] = "none"
                        got[x["paper_id"]] = {k: x[k] for k in ("paper_id", "primary_type", "secondary_type",
                                                                  "foundation_model", "uncertain")}
    return got


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def main() -> None:
    prep, journals = Path(sys.argv[1]), [Path(p) for p in sys.argv[2:]]
    configs = {c["id"]: c for c in json.loads((prep / "configs.json").read_text())}
    first_cfg = {k: v for k, v in configs.items() if k.startswith("R")}
    second_cfg = {k: v for k, v in configs.items() if k.startswith("Q")}
    got_first, got_second = collect(first_cfg, journals), collect(second_cfg, journals)
    corpus = embedded_released()
    ids = set(corpus.submission_id)
    double = set((prep / "double_label_ids.txt").read_text().split())
    RUN.mkdir(parents=True, exist_ok=True)
    write_jsonl(RUN / "labels.jsonl", [got_first[i] for i in sorted(got_first)])
    write_jsonl(RUN / "labels_second_pass.jsonl", [got_second[i] for i in sorted(got_second)])
    (RUN / "double_label_ids.txt").write_text("\n".join(sorted(double)) + "\n")
    (RUN / "run_info.json").write_text(json.dumps({
        "model": "haiku (Claude Code subagent alias)", "provider": "Claude Code workflows in this session",
        "how_run": "label_batches.js, unchanged: one fresh subagent per batch reads the prompt v1 system prompt and its "
                   "papers (two files) and returns labels through a structured-output schema; papers shuffled into "
                   "batches of 100 (prepare_released.py, seed 20261018)",
        "batch_size": 100, "parallel_agents": "6 workflows x 2 concurrent agents (first pass) + 1 x 2 (second pass)",
        "prompt_version": "contribution-codebook-v1 + foundation-model-rule-v1",
        "system_prompt_sha256": "aaa1478fb32e1559edc1e158133a562666d64b29cdf4335bd5361509c1a42410",
        "stage": "released former-confirmation papers", "date_utc": "2026-10-18",
        "papers_labelled": len(got_first), "second_pass_papers": len(got_second),
        "notes": "Second pass: 6 separate batches of fresh agents for the 5% sample in double_label_ids.txt; they never "
                 "saw first-pass labels."}, indent=2) + "\n")
    first = load(RUN / "labels.jsonl", ids)
    missing = ids - set(first.index)
    if missing:
        raise SystemExit(f"{len(missing)} of {len(ids)} papers have no label (e.g. {sorted(missing)[:5]})")
    second = load(RUN / "labels_second_pass.jsonl", ids)
    if set(second.index) != double:
        raise SystemExit(f"second pass covers {len(second)} papers, {len(double & set(second.index))} of {len(double)}")
    first = first.reindex(corpus.submission_id)
    out = pd.DataFrame({"submission_id": corpus.submission_id.values, "year": corpus.year.values,
                        "primary_type": first.primary_type.values,
                        "primary_class": first.primary_type.map(cls).values,
                        "secondary_type": first.secondary_type.values,
                        "secondary_class": first.secondary_type.map(cls).values,
                        "foundation_model": first.foundation_model.values,
                        "uncertain": first.uncertain.astype(bool).values})
    sp = second.reindex(out.submission_id)
    out["second_pass_primary_type"] = sp.primary_type.values
    out["second_pass_foundation_model"] = sp.foundation_model.values
    disc = pd.read_csv(OUTPUT / "paper_contributions.csv.gz")
    shares = lambda d: pd.crosstab(d.year, d.primary_class, normalize="index").round(4)  # noqa: E731
    fm = lambda d: d.groupby("year").foundation_model.apply(lambda s: round(float((s == "yes").mean()), 4))  # noqa: E731
    quality = {"run_info": json.loads((RUN / "run_info.json").read_text()), "papers": len(out),
               "second_pass_papers": len(second), "second_pass_vs_first": compare(second, first.dropna()),
               "class_shares": out.primary_class.value_counts(normalize=True).round(4).to_dict(),
               "class_shares_by_year": shares(out).to_dict(orient="index"),
               "discovery_class_shares_by_year": shares(disc).to_dict(orient="index"),
               "foundation_model_yes_by_year": fm(out).to_dict(),
               "discovery_foundation_model_yes_by_year": fm(disc).to_dict(),
               "uncertain_share": round(float(out.uncertain.mean()), 4),
               "discovery_uncertain_share": round(float(disc.uncertain.mean()), 4)}
    write_csv_gz(out, OUTPUT / "paper_contributions_released.csv.gz")
    (OUTPUT / "contribution_labels_quality_released.json").write_text(json.dumps(quality, indent=2, default=int) + "\n")
    s = quality["second_pass_vs_first"]
    print(f"{len(out)} papers | second pass ({len(second)}): main class {s['main_class']['agreement']:.1%} "
          f"(kappa {s['main_class']['kappa']}), FM {s['foundation_model']['agreement']:.1%} "
          f"(kappa {s['foundation_model']['kappa']})")


if __name__ == "__main__":
    main()
