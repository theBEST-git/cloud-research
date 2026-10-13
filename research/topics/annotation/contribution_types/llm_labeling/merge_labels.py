"""Check the returned full labelling run and merge it into one contribution table (outcome-blind).

    python research/topics/annotation/contribution_types/llm_labeling/merge_labels.py <run dir> [--output <dir>]

<run dir> holds labels.jsonl (all papers), labels_second_pass.jsonl (5% independent relabel) and run_info.json.
Checks, then reports:
- format and coverage: every paper with a topic exactly once, valid values (stops on any error)
- second pass: agreement and kappa with the first pass (label reliability ceiling)
- reference: agreement with our 2,300 reference labels (pilot 300 adjudicated, 200 double-labelled training papers,
  1,800 single-labelled training papers)
- retest: agreement with the step-1 run on the same 300 check papers (same prompt, separate run)
Writes research/topics/output/paper_contributions.csv.gz and contribution_labels_quality.json.
"""
from __future__ import annotations

import argparse
import collections
import json
import random
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
CT = HERE.parent
sys.path.insert(0, str(HERE.parents[2]))
from common import OUTPUT, embedded_corpus, write_csv_gz  # noqa: E402

TYPES = ["method", "model", "theory", "empirical", "system", "dataset_benchmark", "evaluation", "problem",
         "application", "recipe", "perspective", "survey_position"]
CLASS_OF = {"model": "method", "system": "other", "problem": "other", "application": "other", "recipe": "other",
            "perspective": "other", "survey_position": "other"}
cls = lambda t: CLASS_OF.get(t, t) if t != "none" else "none"
RETEST_RUN = HERE / "returned" / "step1_v1_r2" / "check_labels.jsonl"
DOUBLE_SHARE, DOUBLE_SEED = 0.05, 41   # must match labeling_package/build_package.py


def load(path: Path, ids: set[str]) -> pd.DataFrame:
    rows, errors = [], []
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            errors.append(f"{path.name}:{n}: not JSON")
            continue
        bad = [k for k in ("paper_id", "primary_type", "secondary_type", "foundation_model", "uncertain") if k not in r]
        if bad or r["paper_id"] not in ids or r["primary_type"] not in TYPES or r["secondary_type"] not in TYPES + ["none"] \
                or r["secondary_type"] == r["primary_type"] or r["foundation_model"] not in ("yes", "no") \
                or not isinstance(r["uncertain"], bool):
            errors.append(f"{path.name}:{n}: invalid record {line.strip()[:120]}")
            continue
        rows.append(r)
    df = pd.DataFrame(rows)
    if df.paper_id.duplicated().any():
        errors.append(f"{path.name}: {int(df.paper_id.duplicated().sum())} duplicated paper ids")
    if errors:
        raise SystemExit("\n".join(errors[:30]) + f"\n{len(errors)} errors in {path.name}: fix before merging")
    return df.set_index("paper_id")


def agreement(a: pd.Series, b: pd.Series) -> dict:
    a, b = a.align(b, join="inner")
    n = len(a)
    po = float((a == b).mean())
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[c] * cb[c] for c in set(ca) | set(cb)) / n / n
    return {"n": n, "agreement": round(po, 4), "kappa": round((po - pe) / (1 - pe), 4) if pe < 1 else None}


def compare(x: pd.DataFrame, y: pd.DataFrame) -> dict:
    """x, y indexed by paper id with primary_type, secondary_type, foundation_model."""
    return {"main_class": agreement(x.primary_type.map(cls), y.primary_type.map(cls)),
            "fine_type": agreement(x.primary_type, y.primary_type),
            "secondary_type": agreement(x.secondary_type, y.secondary_type),
            "foundation_model": agreement(x.foundation_model, y.foundation_model)}


def references() -> dict[str, pd.DataFrame]:
    pilot = pd.read_csv(CT / "pilot_gold_facets.csv").rename(columns={
        "gold_primary": "primary_type", "gold_secondary": "secondary_type", "gold_foundation_model": "foundation_model"})
    train = pd.read_csv(CT / "training" / "training_labels.csv")
    cols = ["submission_id", "primary_type", "secondary_type", "foundation_model"]
    return {"pilot_adjudicated_300": pilot[cols].set_index("submission_id"),
            "training_double_200": train[train.source != "single"][cols].set_index("submission_id"),
            "training_single_1800": train[train.source == "single"][cols].set_index("submission_id")}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("run", type=Path)
    p.add_argument("--output", type=Path, default=OUTPUT, help="where to write the table (default: topic-layer output/)")
    args = p.parse_args()
    run = args.run
    corpus = embedded_corpus()
    ids = set(corpus.submission_id)
    first = load(run / "labels.jsonl", ids)
    missing = ids - set(first.index)
    if missing:
        raise SystemExit(f"{len(missing)} of {len(ids)} papers have no label (e.g. {sorted(missing)[:5]})")
    second = load(run / "labels_second_pass.jsonl", ids)
    double_ids = set(random.Random(DOUBLE_SEED).sample(sorted(ids), round(len(ids) * DOUBLE_SHARE)))  # as in build_package.py
    if set(second.index) != double_ids:
        raise SystemExit(f"second pass covers {len(second)} papers, {len(double_ids & set(second.index))} of the "
                         f"{len(double_ids)} in double_label_ids.txt")
    quality = {"run_info": json.loads((run / "run_info.json").read_text(encoding="utf-8")),
               "papers": len(first), "second_pass_papers": len(second),
               "second_pass_vs_first": compare(second, first),
               "reference": {name: compare(first, ref) for name, ref in references().items()}}
    if RETEST_RUN.exists():
        quality["retest_vs_step1_check_run"] = compare(first, load(RETEST_RUN, ids))
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
    quality["class_shares"] = out.primary_class.value_counts(normalize=True).round(4).to_dict()
    quality["class_shares_by_year"] = (pd.crosstab(out.year, out.primary_class, normalize="index").round(4)
                                       .to_dict(orient="index"))
    quality["foundation_model_yes_by_year"] = out.groupby("year").foundation_model.apply(lambda s: round(float((s == "yes").mean()), 4)).to_dict()
    quality["uncertain_share"] = round(float(out.uncertain.mean()), 4)
    args.output.mkdir(parents=True, exist_ok=True)
    write_csv_gz(out, args.output / "paper_contributions.csv.gz")
    (args.output / "contribution_labels_quality.json").write_text(json.dumps(quality, indent=2, default=int) + "\n")
    s, r = quality["second_pass_vs_first"], quality["reference"]
    print(f"{len(out)} papers | second pass: main class {s['main_class']['agreement']:.1%} (kappa {s['main_class']['kappa']}), "
          f"FM {s['foundation_model']['agreement']:.1%}")
    for name, v in r.items():
        print(f"  vs {name}: main class {v['main_class']['agreement']:.1%} (n={v['main_class']['n']}), FM {v['foundation_model']['agreement']:.1%}")
    if "retest_vs_step1_check_run" in quality:
        t = quality["retest_vs_step1_check_run"]
        print(f"  retest vs step-1 check run: main class {t['main_class']['agreement']:.1%}, FM {t['foundation_model']['agreement']:.1%}")


if __name__ == "__main__":
    main()
