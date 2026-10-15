"""Collect Haiku workflow results, find missing papers, and score against the reference labels.

    python collect.py <configs.json> <out.jsonl> <workflow transcript dir> [...]
Prints coverage, timing, and agreement with the pilot 300 (adjudicated), training double 200 and single 1,800.
"""
import collections
import glob
import json
import os
import sys

import pandas as pd

CT = "/home/user/cloud-research/research/topics/annotation/contribution_types/"
CLASS = {"model": "method", "system": "other", "problem": "other", "application": "other", "recipe": "other",
         "perspective": "other", "survey_position": "other"}
cls = lambda t: CLASS.get(t, t)

configs = {c["id"]: c for c in json.load(open(sys.argv[1]))}
out_path = sys.argv[2]
got, times = {}, []
for d in sys.argv[3:]:
    label_of = {}
    for line in open(os.path.join(d, "journal.jsonl")):
        r = json.loads(line)
        if r.get("type") == "started":
            label_of[r["agentId"]] = r["label"]
        if r.get("type") == "result":
            bid = label_of[r["agentId"]].split(" ")[0]
            want = set(configs[bid]["ids"])
            for x in (r["result"] or {}).get("labels") or []:
                if x["paper_id"] in want and x["paper_id"] not in got:
                    if x["secondary_type"] == x["primary_type"]:
                        x["secondary_type"] = "none"
                    got[x["paper_id"]] = x
    for f in glob.glob(os.path.join(d, "agent-*.jsonl")):
        ts = [json.loads(l).get("timestamp") for l in open(f)]
        ts = [t for t in ts if t]
        if ts:
            times.append((pd.Timestamp(ts[-1]) - pd.Timestamp(ts[0])).total_seconds())
all_ids = [i for c in configs.values() for i in c["ids"]]
missing = {bid: [i for i in c["ids"] if i not in got] for bid, c in configs.items()}
missing = {k: v for k, v in missing.items() if v}
with open(out_path, "w") as f:
    for i in all_ids:
        if i in got:
            f.write(json.dumps(got[i]) + "\n")
json.dump(missing, open(out_path + ".missing.json", "w"))
print(f"labelled {len(got)} of {len(all_ids)}; missing {sum(map(len, missing.values()))} in {len(missing)} batches")
if times:
    s = pd.Series(times)
    print(f"agent minutes: median {s.median() / 60:.1f}, max {s.max() / 60:.1f}, n {len(s)}")

L = pd.DataFrame(list(got.values())).set_index("paper_id")
pilot = pd.read_csv(CT + "pilot_gold_facets.csv").rename(columns={"gold_primary": "ref_p", "gold_foundation_model": "ref_fm"})
train = pd.read_csv(CT + "training/training_labels.csv").rename(columns={"primary_type": "ref_p", "foundation_model": "ref_fm"})
sets = {"pilot_adjudicated_300": pilot, "training_double_200": train[train.source != "single"],
        "training_single_1800": train[train.source == "single"]}
for name, ref in sets.items():
    j = ref.set_index("submission_id")[["ref_p", "ref_fm"]].join(L, how="inner")
    mc = (j.ref_p.map(cls) == j.primary_type.map(cls)).mean()
    fm = (j.ref_fm == j.foundation_model).mean()
    print(f"{name}: n={len(j)} main class {mc:.1%} | fine {(j.ref_p == j.primary_type).mean():.1%} | FM {fm:.1%} | "
          f"FM yes {int((j.ref_fm == 'yes').sum())}->{int((j.foundation_model == 'yes').sum())}")
    if name != "training_single_1800":
        cnt = {k: f"{int((j.ref_p.map(cls) == k).sum())}->{int((j.primary_type.map(cls) == k).sum())}"
               for k in ["method", "theory", "empirical", "dataset_benchmark", "evaluation", "other"]}
        print("   counts", cnt)
allref = pd.concat([pilot[["submission_id", "ref_p", "ref_fm"]], train[["submission_id", "ref_p", "ref_fm"]]]).drop_duplicates("submission_id")
j = allref.set_index("submission_id").join(L, how="inner")
print(f"all reference papers: n={len(j)} main class {(j.ref_p.map(cls) == j.primary_type.map(cls)).mean():.1%} | "
      f"FM {(j.ref_fm == j.foundation_model).mean():.1%} | uncertain {L.uncertain.mean():.1%}")
