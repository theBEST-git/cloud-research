# Annotation package — round 3 (ChatGPT)

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
