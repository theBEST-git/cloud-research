"""ChatGPT/Codex package for the main claims sample (primary annotator after deviation D1):
40 batch files of ~100 items, PROMPT.md with frozen codebook v1.4, README with protocol.

Run: cd research/titles/src && /home/user/venv/bin/python -m claims.package_main_chatgpt
Writes outputs/claims_main/chatgpt_main.zip
"""
from __future__ import annotations

import json
import shutil
import zipfile

from analyses import _core as C

OUT = C.OUT / "claims_main"
NB = 40

README = """# Main annotation package — ICLR claims study (3,981 items, 40 batches)

## 中文说明（给你 / 给 Codex）
1. 用你能用的最强 ChatGPT/Codex 模型，记下模型名字；如果中途模型更新了，请记录从哪一批开始。
2. 每个 batch 文件独立处理：先读 `PROMPT.md`（完整编码手册 v1.4），再标这个文件里的每一篇。
3. **每篇只标一遍**：可以开多个代理并行处理不同的 batch，但同一篇只能由一个代理标一次。**不要**交叉复核、投票或合并裁决。
4. **不能用代码或规则标注**：每篇都必须由模型亲自读标题和摘要后判断。代码只能用来拆分文件、检查格式、打包。
5. 每个 batch 输出一个文件 `batch_XX_output.jsonl`：每行一个 JSON，字段严格按 PROMPT.md 末尾的格式，item_id 和输入一致。
6. 全部完成后，把 40 个输出文件和 `MODEL.txt`（模型名、流程、偏离）打包发给我，我负责校验。

## Files
- `PROMPT.md` — instructions + frozen codebook v1.4.
- `batch_01.md` … `batch_40.md` — ~100 items each (item_id, TITLE, ABSTRACT).
- Return: `batch_01_output.jsonl` … `batch_40_output.jsonl` + `MODEL.txt`.
"""

PROMPT_HEAD = """You are an expert machine-learning reviewer doing a research annotation task. Each batch file contains about 100 items (title + abstract of ML conference submissions). Annotate EVERY item by following the codebook below exactly. Read each item yourself; do NOT write or run code, rules or keyword matching to produce labels, and do NOT search the web. Each item is annotated once, in the order given; do not revise labels by comparing items or by consulting other annotators.

Output: exactly one JSON object per item per line (JSON Lines), with the fields and value formats given at the end of the codebook, and the item_id copied exactly. No other text in the output file.

"""


def main():
    pkg = OUT / "chatgpt_main"
    if pkg.exists():
        shutil.rmtree(pkg)
    pkg.mkdir(parents=True)
    items = [json.loads(l) for l in open(OUT / "sample_items.jsonl") if l.strip()]
    (pkg / "README.md").write_text(README)
    (pkg / "PROMPT.md").write_text(PROMPT_HEAD + open(OUT / "CODEBOOK_v1_4_FROZEN.md").read())
    per = (len(items) + NB - 1) // NB
    for b in range(NB):
        chunk = items[b * per:(b + 1) * per]
        lines = [f"# Batch {b + 1:02d} — {len(chunk)} items\n"]
        lines += [f"## item_id: {o['item_id']}\n\nTITLE: {o['title']}\n\nABSTRACT: {o['abstract']}\n" for o in chunk]
        (pkg / f"batch_{b + 1:02d}.md").write_text("\n".join(lines))
    zp = OUT / "chatgpt_main.zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(pkg.iterdir()):
            z.write(f, f"chatgpt_main/{f.name}")
    print(zp, len(items), "items", per, "per batch")


if __name__ == "__main__":
    main()
