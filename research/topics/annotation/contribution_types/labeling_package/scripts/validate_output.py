"""Check a labels file against OUTPUT_SPEC.md before sending it back. Standard library only.

    python scripts/validate_output.py --input data/papers_all.jsonl --labels output/labels.jsonl
    python scripts/validate_output.py --input data/papers_all.jsonl --labels output/labels.jsonl \
        --second output/labels_second_pass.jsonl          # also reports agreement between the two passes
    python scripts/validate_output.py --input data/calibration_300.jsonl --labels output/calibration_labels.jsonl

Exit code 0 = ready to send; 1 = fix the errors listed.
"""
from __future__ import annotations

import argparse
import collections
import json
import sys

TYPES = ["method", "model", "theory", "empirical", "system", "dataset_benchmark", "evaluation", "problem",
         "application", "recipe", "perspective", "survey_position"]
CLASS_OF = {"model": "method", "system": "other", "problem": "other", "application": "other", "recipe": "other",
            "perspective": "other", "survey_position": "other"}
REQUIRED = ["paper_id", "primary_type", "secondary_type", "foundation_model", "uncertain"]


def load(path: str, ids: set[str], errors: list[str]) -> dict[str, dict]:
    rows = {}
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            errors.append(f"{path}:{n}: not valid JSON"); continue
        missing = [k for k in REQUIRED if k not in r]
        if missing:
            errors.append(f"{path}:{n}: missing keys {missing}"); continue
        pid = r["paper_id"]
        if pid not in ids:
            errors.append(f"{path}:{n}: unknown paper_id {pid!r}")
        elif pid in rows:
            errors.append(f"{path}:{n}: duplicate paper_id {pid!r}")
        if r["primary_type"] not in TYPES:
            errors.append(f"{path}:{n}: invalid primary_type {r['primary_type']!r}")
        if r["secondary_type"] not in TYPES + ["none"]:
            errors.append(f"{path}:{n}: invalid secondary_type {r['secondary_type']!r}")
        elif r["secondary_type"] == r["primary_type"]:
            errors.append(f"{path}:{n}: secondary_type equals primary_type (use 'none')")
        if r["foundation_model"] not in ("yes", "no"):
            errors.append(f"{path}:{n}: invalid foundation_model {r['foundation_model']!r}")
        if not isinstance(r["uncertain"], bool):
            errors.append(f"{path}:{n}: uncertain must be true or false")
        rows[pid] = r
    return rows


def kappa(a: list[str], b: list[str]) -> tuple[float, float]:
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[c] * cb[c] for c in set(a) | set(b)) / n / n
    return po, (po - pe) / (1 - pe) if pe < 1 else 1.0


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--input", required=True)
    p.add_argument("--labels", required=True)
    p.add_argument("--second")
    a = p.parse_args()
    ids = {json.loads(line)["paper_id"] for line in open(a.input, encoding="utf-8")}
    errors: list[str] = []
    rows = load(a.labels, ids, errors)
    missing = ids - set(rows)
    if missing:
        errors.append(f"{len(missing)} of {len(ids)} papers have no label (e.g. {sorted(missing)[:5]})")
    cls = collections.Counter(CLASS_OF.get(r["primary_type"], r["primary_type"]) for r in rows.values())
    print(f"labelled {len(rows)} of {len(ids)} papers")
    print("primary class:", {k: f"{v / len(rows):.1%}" for k, v in cls.most_common()} if rows else "-")
    if rows:
        print(f"foundation model yes: {sum(r['foundation_model'] == 'yes' for r in rows.values()) / len(rows):.1%} | "
              f"uncertain: {sum(r['uncertain'] is True for r in rows.values()) / len(rows):.1%}")
    if a.second:
        second = load(a.second, ids, errors)
        both = sorted(set(rows) & set(second))
        if both:
            for name, f in [("primary class", lambda r: CLASS_OF.get(r["primary_type"], r["primary_type"])),
                            ("fine type", lambda r: r["primary_type"]), ("foundation model", lambda r: r["foundation_model"])]:
                po, k = kappa([f(rows[i]) for i in both], [f(second[i]) for i in both])
                print(f"second pass ({len(both)} papers) {name}: agreement {po:.1%}, kappa {k:.2f}")
    for e in errors[:50]:
        print("ERROR", e)
    if len(errors) > 50:
        print(f"... and {len(errors) - 50} more errors")
    print("READY TO SEND" if not errors else f"{len(errors)} errors: fix before sending")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
