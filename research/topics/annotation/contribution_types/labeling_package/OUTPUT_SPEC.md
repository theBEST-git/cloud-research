# Output specification (what to send back)

Send back **one zip** (any name, e.g. `contribution_labels_2026-10-20.zip`) containing an `output/` folder:

| File | When | Contents |
|---|---|---|
| `output/calibration_labels.jsonl` | Step 1 (before the full run) | labels for the 300 papers in `data/calibration_300.jsonl` |
| `output/labels.jsonl` | Step 2 | labels for **all 43,480** papers in `data/papers_all.jsonl` |
| `output/labels_second_pass.jsonl` | Step 2 | an independent second labelling of the 2,174 papers in `data/double_label_ids.txt` |
| `output/run_info.json` | Always | `run_info_template.json` filled in |
| `output/*.failures.jsonl` | If any | papers that could not be labelled, with the error |

For step 1 you can send back just `calibration_labels.jsonl` and `run_info.json`.

## Line format (every `*labels*.jsonl` file)

UTF-8 text, **one JSON object per line, one line per paper**:

```json
{"paper_id": "Hk6a8N5xe", "primary_type": "method", "secondary_type": "theory", "foundation_model": "no", "uncertain": false}
```

| Field | Type | Allowed values |
|---|---|---|
| `paper_id` | string | exactly as in the input file |
| `primary_type` | string | `method`, `model`, `theory`, `empirical`, `system`, `dataset_benchmark`, `evaluation`, `problem`, `application`, `recipe`, `perspective`, `survey_position` |
| `secondary_type` | string | one of the same values, or `none`; must differ from `primary_type` |
| `foundation_model` | string | `yes` or `no` |
| `uncertain` | boolean | `true` or `false` |

## Rules

- Every paper in the input appears **exactly once**; no ids that are not in the input; line order does not matter.
- Extra keys (for example `"model"`) are allowed and ignored.
- Use the prompts in `prompts/` unchanged, **one model and temperature 0 for the whole run**, and record the model id in
  `run_info.json`. If anything has to change mid-run, say so in `run_info.json` → `notes`.
- The second pass must be **independent**: separate requests, never showing the model its first-pass labels.
- Before sending, run `python scripts/validate_output.py ...` (see README); it must print `READY TO SEND`.
