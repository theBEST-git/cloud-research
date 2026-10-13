"""Compare returned LLM labels with our reference labels and apply the go/no-go criteria.

    python research/topics/annotation/contribution_types/llm_labeling/compare_returned.py <run dir> [--previous <run dir>]

<run dir> holds the returned files (check_labels.jsonl and/or calibration_labels.jsonl, run_info.json).
References: check set → check_300.csv (training labels); calibration set → ../pilot_gold_facets.csv.
--previous: an earlier run on the calibration set, for a paired comparison (e.g. v1 vs v1.1).
Writes <set>_metrics.json and <set>_disagreements.csv into <run dir>.

Go/no-go (on the check set; fixed before any v1.1 labels existed):
  main class agreement >= 95%, foundation-model agreement >= 97%,
  every main class count within max(3, 25%) of the reference count, foundation-model "yes" count within max(5, 5%).
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
CLASS_OF = {"model": "method", "system": "other", "problem": "other", "application": "other", "recipe": "other",
            "perspective": "other", "survey_position": "other"}
cls = lambda t: CLASS_OF.get(t, t)
GO = {"main_class": 0.95, "foundation_model": 0.97}


def kappa(a, b) -> dict:
    a, b = list(a), list(b)
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[c] * cb[c] for c in set(a) | set(b)) / n / n
    return {"agreement": round(po, 4), "kappa": round((po - pe) / (1 - pe), 4) if pe < 1 else None, "n": n}


def reference(name: str) -> pd.DataFrame:
    """Reference labels as ref_primary / ref_secondary / ref_fm, plus annotator A/B columns for the pilot."""
    if name == "check":
        r = pd.read_csv(HERE / "check_300.csv")
        return r.rename(columns={"primary_type": "ref_primary", "secondary_type": "ref_secondary", "foundation_model": "ref_fm"})
    r = pd.read_csv(HERE.parent / "pilot_gold_facets.csv")
    return r.rename(columns={"gold_primary": "ref_primary", "gold_secondary": "ref_secondary", "gold_foundation_model": "ref_fm"})


def load(path: Path) -> pd.DataFrame:
    return pd.DataFrame([json.loads(line) for line in open(path, encoding="utf-8") if line.strip()])


def compare(name: str, run: Path, previous: Path | None) -> dict:
    ref = reference(name)
    d = ref.merge(load(run / f"{name}_labels.jsonl"), left_on="submission_id", right_on="paper_id", validate="1:1")
    assert len(d) == len(ref) == 300, (len(d), len(ref))
    d["llm_class"], d["ref_class"] = d.primary_type.map(cls), d.ref_primary.map(cls)
    m = {"llm_vs_reference": {"main_class": kappa(d.llm_class, d.ref_class), "fine_type": kappa(d.primary_type, d.ref_primary),
                              "secondary_type": kappa(d.secondary_type, d.ref_secondary),
                              "foundation_model": kappa(d.foundation_model, d.ref_fm)}}
    for col in [c for c in ["stratum", "check_part"] if c in d]:
        m[f"main_class_agreement_by_{col}"] = {k: kappa(g.llm_class, g.ref_class) for k, g in d.groupby(col)}
    if "primary_type_A" in d:
        m["annotator_A_vs_B"] = {"main_class": kappa(d.primary_type_A.map(cls), d.primary_type_B.map(cls)),
                                 "foundation_model": kappa(d.foundation_model_A, d.foundation_model_B)}
    m["class_counts"] = {c: {"reference": int((d.ref_class == c).sum()), "llm": int((d.llm_class == c).sum()),
                             "recall": round(((d.ref_class == c) & (d.llm_class == c)).sum() / max(1, (d.ref_class == c).sum()), 3),
                             "precision": round(((d.ref_class == c) & (d.llm_class == c)).sum() / max(1, (d.llm_class == c).sum()), 3)}
                         for c in sorted(set(d.ref_class) | set(d.llm_class))}
    m["fine_type_counts"] = {t: {"reference": int((d.ref_primary == t).sum()), "llm": int((d.primary_type == t).sum())}
                             for t in sorted(set(d.ref_primary) | set(d.primary_type))}
    m["foundation_model_yes"] = {"reference": int((d.ref_fm == "yes").sum()), "llm": int((d.foundation_model == "yes").sum())}
    m["main_class_confusion"] = pd.crosstab(d.ref_class, d.llm_class).to_dict(orient="index")
    m["uncertain_flag"] = {"share": round(d.uncertain.mean(), 4),
                           "main_class_agreement_if_uncertain": round((d[d.uncertain].llm_class == d[d.uncertain].ref_class).mean(), 4),
                           "main_class_agreement_if_certain": round((d[~d.uncertain].llm_class == d[~d.uncertain].ref_class).mean(), 4)}
    a = m["llm_vs_reference"]
    checks = {"main_class_agreement": a["main_class"]["agreement"] >= GO["main_class"],
              "foundation_model_agreement": a["foundation_model"]["agreement"] >= GO["foundation_model"],
              **{f"count_{c}": abs(v["llm"] - v["reference"]) <= max(3, 0.25 * v["reference"]) for c, v in m["class_counts"].items()},
              "count_foundation_model_yes": abs(m["foundation_model_yes"]["llm"] - m["foundation_model_yes"]["reference"])
                                            <= max(5, 0.05 * m["foundation_model_yes"]["reference"])}
    m["go_checks"] = checks
    if previous is not None and (previous / f"{name}_labels.jsonl").exists():
        p = d[["submission_id", "ref_class", "ref_fm", "llm_class", "foundation_model"]].merge(
            load(previous / f"{name}_labels.jsonl"), left_on="submission_id", right_on="paper_id", suffixes=("", "_prev"))
        p["prev_class"] = p.primary_type.map(cls)
        m["paired_with_previous"] = {
            "previous_run": previous.name, "n": len(p),
            "main_class": {"previous": round(float((p.prev_class == p.ref_class).mean()), 4), "now": round(float((p.llm_class == p.ref_class).mean()), 4),
                           "fixed": int(((p.prev_class != p.ref_class) & (p.llm_class == p.ref_class)).sum()),
                           "broken": int(((p.prev_class == p.ref_class) & (p.llm_class != p.ref_class)).sum())},
            "foundation_model": {"previous": round(float((p.foundation_model_prev == p.ref_fm).mean()), 4), "now": round(float((p.foundation_model == p.ref_fm).mean()), 4),
                                 "fixed": int(((p.foundation_model_prev != p.ref_fm) & (p.foundation_model == p.ref_fm)).sum()),
                                 "broken": int(((p.foundation_model_prev == p.ref_fm) & (p.foundation_model != p.ref_fm)).sum())}}
    (run / f"{name}_metrics.json").write_text(json.dumps(m, indent=2, default=int) + "\n", encoding="utf-8")
    keep = [c for c in ["submission_id", "year", "stratum", "check_part", "source", "ref_primary", "ref_secondary", "primary_type",
                        "secondary_type", "primary_type_A", "primary_type_B", "ref_fm", "foundation_model", "uncertain"] if c in d]
    d[(d.llm_class != d.ref_class) | (d.foundation_model != d.ref_fm)][keep].to_csv(run / f"{name}_disagreements.csv", index=False)
    return m


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("run", type=Path)
    p.add_argument("--previous", type=Path)
    a = p.parse_args()
    for name in ["check", "calibration"]:
        if not (a.run / f"{name}_labels.jsonl").exists():
            continue
        m = compare(name, a.run, a.previous)
        r = m["llm_vs_reference"]
        print(f"{name}: main class {r['main_class']['agreement']:.1%} (kappa {r['main_class']['kappa']}) | "
              f"fine {r['fine_type']['agreement']:.1%} | secondary {r['secondary_type']['agreement']:.1%} | "
              f"FM {r['foundation_model']['agreement']:.1%} (kappa {r['foundation_model']['kappa']})")
        print("  counts (reference → LLM):", {c: f"{v['reference']}→{v['llm']}" for c, v in m["class_counts"].items()},
              f"FM yes {m['foundation_model_yes']['reference']}→{m['foundation_model_yes']['llm']}")
        if "paired_with_previous" in m:
            print("  paired with", m["paired_with_previous"]["previous_run"], {k: v for k, v in m["paired_with_previous"].items() if k != "previous_run"})
        if name == "check":
            failed = [k for k, ok in m["go_checks"].items() if not ok]
            print("  GO" if not failed else f"  NO-GO: {failed}")


if __name__ == "__main__":
    main()
