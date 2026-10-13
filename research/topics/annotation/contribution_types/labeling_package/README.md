# ICLR contribution labelling package (v1)

**Task.** Label 43,480 ICLR submissions (2017–2026) for the *kind of contribution* each one makes, judged from its
title and abstract. The labels feed research on research fashions in machine learning.

**Why an LLM has to read every paper.** The label scheme was validated in a pilot: two independent annotators agreed
on the main contribution class for 97.7% of papers and on the foundation-model flag for 99.7%. A trained classifier
reached only 83% on the main class and missed most of the rare classes, so each paper needs to be read by a strong LLM.

## What you get

```
README.md                    this file
OUTPUT_SPEC.md               exactly what to send back  ← read this
prompts/system_prompt.md     the full labelling instructions (codebook v1 + foundation-model rule + output format)
prompts/user_prompt_template.md   the per-request message; {n} and {papers} are filled in
prompts/output_schema.json   JSON schema of one response (for structured-output APIs)
data/calibration_300.jsonl   step 1: 300 papers with reference labels on our side
data/papers_all.jsonl        step 2: all 43,480 papers (paper_id, title, abstract)
data/double_label_ids.txt    step 2: 2,174 papers (5%) to label a second time, independently
scripts/run_labeling.py      example runner for OpenRouter / any OpenAI-compatible API (standard library only)
scripts/validate_output.py   checks your output before you send it
run_info_template.json       fill in and send back with the labels
reference/codebook_v1.md     the contribution codebook with its pilot evidence (for reading; already in the system prompt)
MANIFEST.json                checksums of every file in this package
```

## Labels per paper

| Field | Values |
|---|---|
| `primary_type` | `method` · `model` (new architecture) · `theory` · `empirical` · `dataset_benchmark` · `evaluation` · `system` · `problem` · `application` · `recipe` · `perspective` · `survey_position` |
| `secondary_type` | a second, clearly claimed contribution of a different type, or `none` |
| `foundation_model` | `yes` if the work builds on a large pretrained model (LLM, CLIP, Stable Diffusion, …), else `no` |
| `uncertain` | `true` if the call was close |

Full definitions and decision rules are in `prompts/system_prompt.md`.

## How to run

Requirements: Python 3.9+, no extra packages, an API key in an environment variable (never in a file).

```bash
export OPENROUTER_API_KEY=...        # or set --base-url / --api-key-env for another provider

# Step 1 — calibration (300 papers, a few minutes). Send the result back before step 2.
python scripts/run_labeling.py --input data/calibration_300.jsonl --output output/calibration_labels.jsonl --model <model-id>
python scripts/validate_output.py --input data/calibration_300.jsonl --labels output/calibration_labels.jsonl

# Step 2 — full run, then the independent second pass on 5% of papers
python scripts/run_labeling.py --input data/papers_all.jsonl --output output/labels.jsonl --model <model-id>
python scripts/run_labeling.py --input data/papers_all.jsonl --ids data/double_label_ids.txt \
    --output output/labels_second_pass.jsonl --model <model-id>
python scripts/validate_output.py --input data/papers_all.jsonl --labels output/labels.jsonl \
    --second output/labels_second_pass.jsonl
```

The runner is resumable: rerun the same command after an interruption and it continues where it stopped, retrying
failed papers. You may use your own pipeline instead, as long as the output follows `OUTPUT_SPEC.md`.

**Step 1 is a go/no-go check.** We compare your calibration labels with our adjudicated reference labels. Go ahead with
step 2 if the main class agrees on at least ~90% of papers and the foundation-model flag on at least ~95%; otherwise
try a stronger model before spending the full budget.

## Model and cost

- Use one strong, current frontier model for everything, at temperature 0, and record its exact id.
- Batch size 25 papers per request is a good balance; smaller batches cost more and may help weaker models.
- Rough volume at batch size 25: ~1,740 requests, ~19M input tokens (about a fifth is the repeated system prompt,
  which prompt caching reduces) and ~2M output tokens. Wall time depends on your provider's rate limits.

## Notes

- `papers_all.jsonl` deliberately includes 2,300 papers we have already labelled (among them the 300 calibration papers).
  Label them like any other paper: they let us measure agreement on a large sample.
- 36 submissions with placeholder abstracts (e.g. "We have withdrawn our paper.") are not included.
- The text is public OpenReview metadata of ICLR submissions; use it only for this labelling task.
- Questions or changes to the prompts: tell us first, so the codebook version stays traceable.
