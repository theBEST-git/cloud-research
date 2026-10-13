"""Compare returned LLM calibration labels with the adjudicated pilot reference labels.

    python research/topics/annotation/contribution_types/llm_labeling/compare_calibration.py \
        research/topics/annotation/contribution_types/llm_labeling/returned/calibration_v1

Writes calibration_metrics.json and calibration_disagreements.csv next to the returned labels.
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

import pandas as pd

CT = Path(__file__).resolve().parents[1]
CLASS_OF = {"model": "method", "system": "other", "problem": "other", "application": "other", "recipe": "other",
            "perspective": "other", "survey_position": "other"}
cls = lambda t: CLASS_OF.get(t, t)


def kappa(a, b) -> dict:
    a, b = list(a), list(b)
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[c] * cb[c] for c in set(a) | set(b)) / n / n
    return {"agreement": round(po, 4), "kappa": round((po - pe) / (1 - pe), 4), "n": n}


def main() -> None:
    run = Path(sys.argv[1])
    llm = pd.DataFrame([json.loads(line) for line in open(run / "calibration_labels.jsonl", encoding="utf-8")])
    d = pd.read_csv(CT / "pilot_gold_facets.csv").merge(llm, left_on="submission_id", right_on="paper_id", validate="1:1")
    assert len(d) == 300, len(d)
    d["llm_class"], d["ref_class"] = d.primary_type.map(cls), d.gold_primary.map(cls)
    d["A_class"], d["B_class"] = d.primary_type_A.map(cls), d.primary_type_B.map(cls)
    out = {"run_info": json.loads((run / "run_info.json").read_text(encoding="utf-8"))}
    for name, sub in [("all_300", d), ("random_240", d[d.stratum == "random"])]:
        out[name] = {
            "llm_vs_reference": {"main_class": kappa(sub.llm_class, sub.ref_class), "fine_type": kappa(sub.primary_type, sub.gold_primary),
                                 "secondary_type": kappa(sub.secondary_type, sub.gold_secondary),
                                 "foundation_model": kappa(sub.foundation_model, sub.gold_foundation_model)},
            "annotator_A_vs_B": {"main_class": kappa(sub.A_class, sub.B_class), "fine_type": kappa(sub.primary_type_A, sub.primary_type_B),
                                 "foundation_model": kappa(sub.foundation_model_A, sub.foundation_model_B)},
            "prevalence_reference": sub.ref_class.value_counts().to_dict(), "prevalence_llm": sub.llm_class.value_counts().to_dict(),
            "foundation_model_yes": {"reference": int((sub.gold_foundation_model == "yes").sum()), "llm": int((sub.foundation_model == "yes").sum())},
        }
    out["per_class_all_300"] = {c: {"reference_n": int((d.ref_class == c).sum()), "llm_n": int((d.llm_class == c).sum()),
                                    "recall": round(((d.ref_class == c) & (d.llm_class == c)).sum() / max(1, (d.ref_class == c).sum()), 3),
                                    "precision": round(((d.ref_class == c) & (d.llm_class == c)).sum() / max(1, (d.llm_class == c).sum()), 3)}
                                for c in sorted(set(d.ref_class) | set(d.llm_class))}
    out["main_class_confusion_all_300"] = pd.crosstab(d.ref_class, d.llm_class).to_dict(orient="index")
    out["foundation_model_confusion_all_300"] = pd.crosstab(d.gold_foundation_model, d.foundation_model).to_dict(orient="index")
    out["uncertain_flag"] = {"share": round(d.uncertain.mean(), 4),
                             "main_class_agreement_if_uncertain": round((d[d.uncertain].llm_class == d[d.uncertain].ref_class).mean(), 4),
                             "main_class_agreement_if_certain": round((d[~d.uncertain].llm_class == d[~d.uncertain].ref_class).mean(), 4)}
    (run / "calibration_metrics.json").write_text(json.dumps(out, indent=2, default=int) + "\n", encoding="utf-8")
    dis = d[(d.llm_class != d.ref_class) | (d.foundation_model != d.gold_foundation_model)]
    dis[["submission_id", "stratum", "gold_primary", "gold_secondary", "primary_type", "secondary_type", "primary_type_A", "primary_type_B",
         "gold_foundation_model", "foundation_model", "uncertain"]].to_csv(run / "calibration_disagreements.csv", index=False)
    a = out["all_300"]["llm_vs_reference"]
    print(f"main class {a['main_class']['agreement']:.1%} | fine {a['fine_type']['agreement']:.1%} | "
          f"secondary {a['secondary_type']['agreement']:.1%} | FM {a['foundation_model']['agreement']:.1%} | {len(dis)} disagreement rows")


if __name__ == "__main__":
    main()
