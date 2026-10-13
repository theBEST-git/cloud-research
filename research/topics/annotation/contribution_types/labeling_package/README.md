# ICLR contribution labelling package (v1.1)

**Task.** Label 43,480 ICLR submissions (2017–2026) for the *kind of contribution* each one makes, judged from its
title and abstract. The labels feed research on research fashions in machine learning.

**Why an LLM has to read every paper.** The label scheme was validated in a pilot: two independent annotators agreed
on the main contribution class for 97.7% of papers and on the foundation-model flag for 99.7%. A trained classifier
reached only 83% on the main class and missed most of the rare classes, so each paper needs to be read by a strong LLM.

## What changed in v1.1

The v1 calibration run passed (main class 95.7%, foundation-model flag 97.7%), but its errors leaned one way:
named "frameworks"/"agents" were labelled `system`, learned distances or similarities were labelled `evaluation`,
and papers that only mention LLMs were flagged as foundation-model work. v1.1 adds three clarifications for these
boundaries (`prompts/clarifications_v1_1.md`, also included in the system prompt). No definition changed.

Because the clarifications were written after seeing the v1 calibration results, step 1 now also labels a **fresh
check set** of 300 papers that were not looked at; the go/no-go decision is based on that set.

## What you get

```
README.md                    this file
OUTPUT_SPEC.md               exactly what to send back  ← read this
prompts/system_prompt.md     the full labelling instructions (codebook v1 + foundation-model rule
                             + v1.1 clarifications + output format)
prompts/clarifications_v1_1.md   the v1.1 additions on their own (already in the system prompt)
prompts/user_prompt_template.md  the per-request message; {n} and {papers} are filled in
prompts/output_schema.json   JSON schema of one response (for structured-output APIs)
data/check_300.jsonl         step 1: 300 fresh papers with reference labels on our side (decides go/no-go)
data/calibration_300.jsonl   step 1: the same 300 papers as the v1 calibration (shows the effect of v1.1)
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

### Step 1: check (600 papers). Send the result back and wait for our go before step 2.

With an API (Python 3.9+, no extra packages, the key in an environment variable, never in a file):

```bash
export OPENROUTER_API_KEY=...        # or set --base-url / --api-key-env for another provider
python scripts/run_labeling.py --input data/check_300.jsonl --output output/check_labels.jsonl --model <model-id>
python scripts/run_labeling.py --input data/calibration_300.jsonl --output output/calibration_labels.jsonl --model <model-id>
python scripts/validate_output.py --input data/check_300.jsonl --labels output/check_labels.jsonl
python scripts/validate_output.py --input data/calibration_300.jsonl --labels output/calibration_labels.jsonl
```

We compare `check_labels.jsonl` with our reference labels and reply go or no-go. The reference labels are not in
this package on purpose.

### Step 2: full run, then the independent second pass on 5% of papers

```bash
python scripts/run_labeling.py --input data/papers_all.jsonl --output output/labels.jsonl --model <model-id>
python scripts/run_labeling.py --input data/papers_all.jsonl --ids data/double_label_ids.txt \
    --output output/labels_second_pass.jsonl --model <model-id>
python scripts/validate_output.py --input data/papers_all.jsonl --labels output/labels.jsonl \
    --second output/labels_second_pass.jsonl
```

The runner is resumable: rerun the same command after an interruption and it continues where it stopped, retrying
failed papers.

### Running with chat agents instead of an API

That is fine if every batch is labelled the same way:

- give each agent `prompts/system_prompt.md` verbatim as its instructions, and one batch of 25 papers at a time in
  the form of `prompts/user_prompt_template.md`;
- the same model and settings (e.g. reasoning effort) for steps 1 and 2;
- agents must not see other batches' labels, the v1 run's labels, or look papers up; title and abstract only;
- for the second pass, use fresh agents that never saw the first-pass labels;
- merge the agents' answers without editing them, then run `scripts/validate_output.py`;
- record the setup (model, settings, number of agents, how the prompt was given) in `run_info.json`.

## Model and cost

- Use one strong, current frontier model for everything, at temperature 0 where it can be set, and record its exact id.
- Batch size 25 papers per request is a good balance; smaller batches cost more and may help weaker models.
- Rough volume of step 2 at batch size 25: ~1,830 requests, ~20M input tokens (about a fifth is the repeated system
  prompt, which prompt caching reduces) and ~2M output tokens. Step 1 is 24 requests.

## Notes

- `papers_all.jsonl` deliberately includes 2,300 papers we have already labelled (among them the 600 step-1 papers).
  Label them like any other paper: they let us measure agreement on a large sample.
- 36 submissions with placeholder abstracts (e.g. "We have withdrawn our paper.") are not included.
- The text is public OpenReview metadata of ICLR submissions; use it only for this labelling task.
- Questions or changes to the prompts: tell us first, so the codebook version stays traceable.
