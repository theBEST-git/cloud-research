"""Merge topic names, stability and the blind name check into output/topic_catalog.csv.

Inputs: output/topic_catalog_auto.csv (build_topics.py), output/topic_stability.csv (evaluate_topics.py),
annotation/topic_names.json (naming workflow), annotation/name_check_answers.json and
annotation/name_check_truth.json (blind check). Writes output/topic_catalog.csv and output/name_check.json.

    python research/topics/finalize_catalog.py
"""
from __future__ import annotations

import json

import pandas as pd

from common import HERE, OUTPUT

ANNOTATION = HERE / "annotation"


def main() -> None:
    cat = pd.read_csv(OUTPUT / "topic_catalog_auto.csv", keep_default_na=False)
    names = json.loads((ANNOTATION / "topic_names.json").read_text())
    stab = pd.read_csv(OUTPUT / "topic_stability.csv")
    missing = sorted(set(cat.topic) - set(names))
    if missing:
        raise RuntimeError(f"Unnamed topics: {missing}")
    cat["name"] = cat.topic.map(lambda t: names[t]["name"])
    cat["description"] = cat.topic.map(lambda t: names[t]["description"])
    cat["coherence"] = cat.topic.map(lambda t: names[t]["coherence"])
    cat["coherence_note"] = cat.topic.map(lambda t: names[t].get("note", ""))
    cat["renamed_in_review"] = cat.topic.map(lambda t: names[t].get("revised", ""))
    cat = cat.merge(stab[["topic", "stability_jaccard"]], on="topic", how="left")

    truth = json.loads((ANNOTATION / "name_check_truth.json").read_text())
    answers = {a["paper"]: a["fine"] for a in json.loads((ANNOTATION / "name_check_answers.json").read_text())}
    fine = cat[cat.level == "fine"].set_index("topic")
    options = fine.groupby("parent_coarse").size()
    rows = []
    for pid, t in truth.items():
        guess = answers.get(pid)
        rows.append({"paper": pid, "true_fine": t["fine"], "guess": guess,
                     "fine_correct": guess == t["fine"],
                     "mid_correct": guess in fine.index and fine.parent_mid.get(guess) == t["mid"],
                     "chance": 1 / options[t["coarse"]]})
    check = pd.DataFrame(rows)
    summary = {"papers": len(check), "answered": int(check.guess.notna().sum()),
               "fine_accuracy": round(float(check.fine_correct.mean()), 3),
               "mid_accuracy": round(float(check.mid_correct.mean()), 3),
               "chance_fine_accuracy": round(float(check.chance.mean()), 3),
               "note": "one random paper per fine topic; checker saw only title + abstract opening and the fine-topic names "
                       "inside the paper's broad topic"}
    (OUTPUT / "name_check.json").write_text(json.dumps(summary, indent=2) + "\n")
    cat["name_check_correct"] = cat.topic.map(dict(zip(check.true_fine, check.fine_correct))).map(
        {True: "yes", False: "no"}).fillna("")

    lead = ["level", "topic", "name", "description", "parent_mid", "parent_coarse", "papers"]
    years = [c for c in cat.columns if c.startswith("y20")]
    tail = ["coherence", "coherence_note", "stability_jaccard", "name_check_correct", "renamed_in_review",
            "mean_mid_similarity", "keyword_signature", "example_titles"]
    cat[lead + years + tail].to_csv(OUTPUT / "topic_catalog.csv", index=False)
    print(json.dumps(summary, indent=2))
    print(cat.groupby("level").coherence.value_counts().unstack(fill_value=0).to_string())


if __name__ == "__main__":
    main()
