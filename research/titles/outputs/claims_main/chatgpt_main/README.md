# Main annotation package — ICLR claims study (3,981 items, 40 batches)

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
