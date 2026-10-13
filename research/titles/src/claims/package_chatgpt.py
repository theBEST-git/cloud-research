"""Build the ChatGPT annotation package for a pilot round: prompt, codebook, 4 batches of 25 items.

Run: cd research/titles/src && /home/user/venv/bin/python -m claims.package_chatgpt ROUND
Writes outputs/claims_pilot/chatgpt_round{R}/ and chatgpt_round{R}.zip (no decisions included).
"""
from __future__ import annotations

import json
import shutil
import sys
import zipfile

from analyses import _core as C

OUT = C.OUT / "claims_pilot"
NB = 4
CODEBOOK = {2: "CODEBOOK_v1.md"}

README = """# Annotation package — round {r} (ChatGPT)

## 中文说明（给你）
1. 打开 ChatGPT，选你能用的**最强推理模型**，并记下模型名字。
2. 每一批**新开一个对话**，一共 4 批。
3. 把 `PROMPT.md` 的全部内容粘贴进去，再把这一批的文件 `batch_0X.md` 作为附件上传，或者直接粘贴全文，然后发送。
4. ChatGPT 会输出 25 行 JSON，每行一篇论文。如果中途停下，就回复 "continue from item_id ..." 让它接着输出。
5. 把输出原样保存为 `batch_0X_output.jsonl`，四批都做完后把 4 个文件发给我，我来校验格式和缺漏。
6. 不要让它用代码标注。如果它开始写 Python，就提醒它："Read each item yourself; do not use code."
7. **单人单遍**：每批只让一个模型自己读一遍、标一遍。**不要**开多个代理，不要交叉复核，也不要合并裁决。这样流程才和 Claude 一致。

## Files
- `PROMPT.md` — paste this first in each new chat (contains the full codebook).
- `batch_01.md` … `batch_04.md` — 25 items each.
- Expected return files: `batch_01_output.jsonl` … `batch_04_output.jsonl`, plus the model name you used.
"""

PROMPT_HEAD = """You are an expert machine-learning reviewer helping with a research annotation task. I will give you a batch of 25 items (title + abstract of ML conference submissions). Annotate EVERY item by following the codebook below exactly. Read each item yourself; do NOT write or run code to annotate, and do NOT search the web. Process items in the order given.

Output format: exactly one JSON object per line per item (JSON Lines), in a single code block, nothing else before or after. If you run out of space, stop at the end of a complete line; I will say "continue" and you will resume with the next item_id.

"""


def main(rnd: int):
    pkg = OUT / f"chatgpt_round{rnd}"
    if pkg.exists():
        shutil.rmtree(pkg)
    pkg.mkdir(parents=True)
    items = []
    for c in range(2):
        for line in open(OUT / f"round{rnd}_items_chunk{c}.jsonl"):
            if line.strip():
                items.append(json.loads(line))
    items.sort(key=lambda o: o["item_id"])
    codebook = open(OUT / CODEBOOK.get(rnd, "CODEBOOK_v1_2.md")).read()
    (pkg / "README.md").write_text(README.format(r=rnd))
    (pkg / "PROMPT.md").write_text(PROMPT_HEAD + codebook)
    per = (len(items) + NB - 1) // NB
    for b in range(NB):
        chunk = items[b * per:(b + 1) * per]
        lines = [f"# Batch {b + 1:02d} — {len(chunk)} items\n"]
        for o in chunk:
            lines.append(f"## item_id: {o['item_id']}\n\nTITLE: {o['title']}\n\nABSTRACT: {o['abstract']}\n")
        (pkg / f"batch_{b + 1:02d}.md").write_text("\n".join(lines))
    zp = OUT / f"chatgpt_round{rnd}.zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(pkg.iterdir()):
            z.write(f, f"chatgpt_round{rnd}/{f.name}")
    print(zp, len(items), "items")


if __name__ == "__main__":
    main(int(sys.argv[1]))
