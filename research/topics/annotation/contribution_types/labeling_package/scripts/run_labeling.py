"""Example runner: label papers with an OpenAI-compatible chat API (e.g. OpenRouter). Standard library only.

    export OPENROUTER_API_KEY=...            # never paste the key into files or chats
    python scripts/run_labeling.py --input data/calibration_300.jsonl --output output/calibration_labels.jsonl --model <model-id>
    python scripts/run_labeling.py --input data/papers_all.jsonl --output output/labels.jsonl --model <model-id>
    python scripts/run_labeling.py --input data/papers_all.jsonl --ids data/double_label_ids.txt \
        --output output/labels_second_pass.jsonl --model <model-id>

Resumable: papers already in --output are skipped. Papers still invalid after retries go to <output>.failures.jsonl.
You may use your own pipeline instead; the output just has to follow OUTPUT_SPEC.md.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYSTEM_PROMPT = (ROOT / "prompts" / "system_prompt.md").read_text(encoding="utf-8")
TEMPLATE = (ROOT / "prompts" / "user_prompt_template.md").read_text(encoding="utf-8")
TYPES = {"method", "model", "theory", "empirical", "system", "dataset_benchmark", "evaluation", "problem",
         "application", "recipe", "perspective", "survey_position"}
LOCK = threading.Lock()


def render(batch: list[dict]) -> str:
    papers = "\n\n".join(f"### paper {p['paper_id']}\ntitle: {p['title']}\nabstract:\n{p['abstract']}" for p in batch)
    return TEMPLATE.replace("{n}", str(len(batch))).replace("{papers}", papers)


def call_api(args, user_prompt: str) -> str:
    body = {"model": args.model, "temperature": 0, "max_tokens": args.max_tokens,
            "messages": [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_prompt}]}
    if args.json_mode:
        body["response_format"] = {"type": "json_object"}
    request = urllib.request.Request(args.base_url.rstrip("/") + "/chat/completions", data=json.dumps(body).encode(),
                                     headers={"Authorization": f"Bearer {os.environ[args.api_key_env]}",
                                              "Content-Type": "application/json"})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(request, timeout=300) as response:
                return json.load(response)["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < 5:
                time.sleep(2 ** attempt * 5)
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            if attempt < 5:
                time.sleep(2 ** attempt * 5)
                continue
            raise
    raise RuntimeError("unreachable")


def parse(text: str) -> list[dict]:
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    return json.loads(t[t.find("{"): t.rfind("}") + 1])["labels"]


def clean(label: dict, wanted: set[str]) -> dict | None:
    try:
        row = {"paper_id": str(label["paper_id"]), "primary_type": label["primary_type"],
               "secondary_type": label["secondary_type"], "foundation_model": label["foundation_model"],
               "uncertain": bool(label["uncertain"])}
    except (KeyError, TypeError):
        return None
    if (row["paper_id"] not in wanted or row["primary_type"] not in TYPES
            or row["secondary_type"] not in TYPES | {"none"} or row["foundation_model"] not in ("yes", "no")):
        return None
    if row["secondary_type"] == row["primary_type"]:      # codebook: a secondary must be a different type
        row["secondary_type"] = "none"
    return row


def label_batch(args, batch: list[dict]) -> tuple[list[dict], list[dict]]:
    remaining, done, error = {p["paper_id"]: p for p in batch}, [], ""
    for _ in range(args.retries + 1):
        if not remaining:
            break
        try:
            for raw in parse(call_api(args, render(list(remaining.values())))):
                row = clean(raw, set(remaining))
                if row:
                    done.append(row)
                    remaining.pop(row["paper_id"], None)
        except Exception as e:  # malformed JSON or API failure: retry the papers still missing
            error = repr(e)[:300]
    failed = [{"paper_id": pid, "error": error or "missing or invalid in model output"} for pid in remaining]
    return done, failed


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--ids", help="optional file with one paper_id per line to restrict the run")
    p.add_argument("--base-url", default="https://openrouter.ai/api/v1")
    p.add_argument("--api-key-env", default="OPENROUTER_API_KEY")
    p.add_argument("--batch-size", type=int, default=25)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--retries", type=int, default=2)
    p.add_argument("--max-tokens", type=int, default=4000)
    p.add_argument("--json-mode", action="store_true", help="send response_format=json_object (if the model supports it)")
    args = p.parse_args()
    if args.api_key_env not in os.environ:
        sys.exit(f"Set the {args.api_key_env} environment variable first.")
    papers = [json.loads(line) for line in open(args.input, encoding="utf-8")]
    if args.ids:
        keep = {line.strip() for line in open(args.ids) if line.strip()}
        papers = [x for x in papers if x["paper_id"] in keep]
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if out.exists():
        for line in open(out, encoding="utf-8"):
            try:
                done.add(json.loads(line)["paper_id"])
            except (json.JSONDecodeError, KeyError):   # e.g. a line cut off by an interrupted run
                pass
    todo = [x for x in papers if x["paper_id"] not in done]
    batches = [todo[i:i + args.batch_size] for i in range(0, len(todo), args.batch_size)]
    print(f"{len(papers)} papers, {len(done)} already labelled, {len(batches)} requests to send", flush=True)
    failures = out.with_suffix(out.suffix + ".failures.jsonl")
    n_ok = n_fail = 0
    with ThreadPoolExecutor(args.workers) as pool, open(out, "a", encoding="utf-8") as fo, open(failures, "a", encoding="utf-8") as ff:
        for i, fut in enumerate(as_completed(pool.submit(label_batch, args, b) for b in batches), 1):
            rows, failed = fut.result()
            with LOCK:
                for r in rows:
                    fo.write(json.dumps(r) + "\n")
                for f in failed:
                    ff.write(json.dumps(f) + "\n")
                fo.flush(); ff.flush()
            n_ok += len(rows); n_fail += len(failed)
            if i % 20 == 0 or i == len(batches):
                print(f"{i}/{len(batches)} requests | labelled {n_ok} | failed {n_fail}", flush=True)
    print(f"done: {n_ok} labelled this run, {n_fail} failed (see {failures}); rerun the same command to retry failures")


if __name__ == "__main__":
    main()
