"""Build the contribution labelling package as a zip (data + prompts + spec + scripts).

    python research/topics/annotation/contribution_types/labeling_package/build_package.py --out <path>.zip

The zip is deterministic for unchanged inputs (fixed file times, sorted entries).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
import zipfile
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
CT = HERE.parent
sys.path.insert(0, str(HERE.parents[2]))
from common import embedded_corpus  # noqa: E402

ROOT_DIR = "iclr_contribution_labeling_v1"
DOUBLE_SHARE, SEED = 0.05, 41
STATIC = ["README.md", "OUTPUT_SPEC.md", "prompts/user_prompt_template.md", "prompts/output_schema.json",
          "scripts/run_labeling.py", "scripts/validate_output.py"]


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def system_prompt() -> str:
    instructions = (CT / "training" / "instructions.md").read_text(encoding="utf-8")
    instructions = re.sub(r"\nLocked after a pilot.*?version\.\n", "\n", instructions, flags=re.S)  # points to a section not included
    instructions = instructions.replace(" (see `open_coding_synthesis.json`)", "")              # internal file, not shipped
    return instructions.rstrip() + "\n\n" + (HERE / "prompts" / "output_format.md").read_text(encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", required=True)
    out = Path(p.parse_args().out)
    corpus = embedded_corpus()
    clean = lambda s: " ".join(str(s).split())
    papers = [{"paper_id": r.submission_id, "title": clean(r.title), "abstract": clean(r.abstract)} for r in corpus.itertuples()]
    by_id = {x["paper_id"]: x for x in papers}
    calibration = pd.read_csv(CT / "pilot_sample.csv").submission_id.tolist()
    double = sorted(random.Random(SEED).sample(sorted(by_id), round(len(papers) * DOUBLE_SHARE)))
    prompt = system_prompt()
    info = json.loads((HERE / "run_info_template.json").read_text(encoding="utf-8"))
    info["system_prompt_sha256"] = sha256(prompt)
    files = {
        "data/papers_all.jsonl": "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in papers),
        "data/calibration_300.jsonl": "".join(json.dumps(by_id[i], ensure_ascii=False) + "\n" for i in calibration),
        "data/double_label_ids.txt": "\n".join(double) + "\n",
        "prompts/system_prompt.md": prompt,
        "run_info_template.json": json.dumps(info, indent=2) + "\n",
        "reference/codebook_v1.md": (CT / "codebook.md").read_text(encoding="utf-8"),
        **{f: (HERE / f).read_text(encoding="utf-8") for f in STATIC},
    }
    files["MANIFEST.json"] = json.dumps({"package": ROOT_DIR, "papers": len(papers), "calibration_papers": len(calibration),
                                         "double_label_papers": len(double),
                                         "files": {k: {"bytes": len(v.encode("utf-8")), "sha256": sha256(v)} for k, v in sorted(files.items())}},
                                        indent=2) + "\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name in sorted(files):
            info_ = zipfile.ZipInfo(f"{ROOT_DIR}/{name}", date_time=(2026, 10, 13, 0, 0, 0))
            info_.compress_type = zipfile.ZIP_DEFLATED
            info_.external_attr = 0o644 << 16
            z.writestr(info_, files[name])
    print(f"{out} | {len(papers)} papers, {len(calibration)} calibration, {len(double)} double-label | "
          f"{out.stat().st_size / 2**20:.1f} MB | system prompt sha256 {info['system_prompt_sha256'][:12]}…")


if __name__ == "__main__":
    main()
