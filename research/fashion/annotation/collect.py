"""Collect blind-judge answers from workflow journals and audit the judges' transcripts (PREREGISTRATION.md D6, R1).

Each judging agent is labelled "<judge>/b<k>" (or "<judge>/b<k> re-ask") and returns {"answers": [{"item_id", ...}]}.
Only answers for items of that agent's batch (from manifest.json) are kept; the first answer per (judge, item) wins.
The audit lists every tool call; reading anything but instructions.md and the agent's own batch file, or running any
other tool, is a violation.

    python research/fashion/annotation/collect.py <task dir> <workflow transcript dir> [...] [--out returned]
Writes <task dir>/<out>/<judge>.jsonl, <out>/missing.json and <out>/audit.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def tool_calls(transcript: Path) -> list[tuple[str, dict]]:
    out = []
    for line in transcript.open():
        m = json.loads(line).get("message")
        content = m.get("content") if isinstance(m, dict) else None
        if isinstance(content, list):
            out += [(c["name"], c.get("input", {})) for c in content if c.get("type") == "tool_use"]
    return out


def main() -> None:
    argv = sys.argv[1:]
    out_name = "returned"
    if "--out" in argv:
        i = argv.index("--out")
        out_name = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    task, runs = Path(argv[0]).resolve(), [Path(p) for p in argv[1:]]
    manifest = json.loads((task / "manifest.json").read_text())["files"]
    got: dict[str, dict[str, dict]] = {}
    audit = {"agents": 0, "violations": []}
    for run in runs:
        label_of = {}
        for line in (run / "journal.jsonl").open():
            r = json.loads(line)
            if r.get("type") == "started":
                label_of[r["agentId"]] = r["label"]
            if r.get("type") != "result":
                continue
            label = label_of[r["agentId"]].split(" ")[0]
            judge, batch = label.split("/")
            want = set(manifest[f"batches/{judge}/{batch}.md"]["items"]) if judge != "pilot" else set(manifest["batches/pilot.md"]["items"])
            for a in (r.get("result") or {}).get("answers") or []:
                if a.get("item_id") in want:
                    got.setdefault(judge, {}).setdefault(a["item_id"], a)
        for aid, label in label_of.items():
            judge, batch = label.split(" ")[0].split("/")
            own = f"batches/{judge}/{batch}.md" if judge != "pilot" else "batches/pilot.md"
            allowed = {str(task / "instructions.md"), str(task / own)}
            audit["agents"] += 1
            for name, inp in tool_calls(run / f"agent-{aid}.jsonl"):
                if name == "StructuredOutput":
                    continue
                if name == "Read" and str(Path(inp.get("file_path", "")).resolve()) in allowed:
                    continue
                audit["violations"].append({"agent": label, "tool": name, "input": json.dumps(inp)[:300]})
    out = task / out_name
    out.mkdir(exist_ok=True)
    missing = {}
    for path, f in manifest.items():
        parts = Path(path).parts
        judge = "pilot" if parts[-1] == "pilot.md" else parts[1]
        if judge not in got:
            continue
        miss = [i for i in f["items"] if i not in got.get(judge, {})]
        if miss:
            missing[path] = miss
    for judge, answers in got.items():
        with (out / f"{judge}.jsonl").open("w") as fh:
            for item in sorted(answers):
                fh.write(json.dumps(answers[item], sort_keys=True) + "\n")
    (out / "missing.json").write_text(json.dumps(missing, indent=1) + "\n")
    (out / "audit.json").write_text(json.dumps(audit, indent=1) + "\n")
    print(json.dumps({"answers": {j: len(a) for j, a in got.items()}, "missing": {k: len(v) for k, v in missing.items()},
                      "agents": audit["agents"], "violations": len(audit["violations"])}, indent=1))


if __name__ == "__main__":
    main()
