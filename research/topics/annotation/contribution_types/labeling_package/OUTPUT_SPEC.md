# Output specification (what to send back)

Send back **one zip** per step (any name, e.g. `contribution_labels_step1_v1_1.zip`) containing an `output/` folder:

| File | Step | Contents |
|---|---|---|
| `output/check_labels.jsonl` | 1 | labels for the 300 papers in `data/check_300.jsonl` |
| `output/calibration_labels.jsonl` | 1 | labels for the 300 papers in `data/calibration_300.jsonl` |
| `output/labels.jsonl` | 2 | labels for **all 43,480** papers in `data/papers_all.jsonl` |
| `output/labels_second_pass.jsonl` | 2 | an independent second labelling of the 2,174 papers in `data/double_label_ids.txt` |
| `output/run_info.json` | 1 and 2 | `run_info_template.json` filled in |
| `output/*.failures.jsonl` | if any | papers that could not be labelled, with the error |

Run step 2 only after we have replied "go" to step 1.

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
- Use `prompts/system_prompt.md` (v1.1) unchanged, and **the same model and settings for steps 1 and 2**. Record them
  in `run_info.json`. If anything has to change, say so in `run_info.json` → `notes`.
- Label every batch from scratch: no access to other batches' labels, earlier runs (v1) or any reference labels,
  and no looking papers up elsewhere. Judge from the title and abstract given.
- The second pass must be **independent**: separate requests or agents, never shown the first-pass labels.
- Before sending, run `python scripts/validate_output.py ...` (see README) on each labels file; it must print
  `READY TO SEND`.
