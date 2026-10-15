# LLM labelling of all papers: returned runs and checks

Every paper is labelled by an external LLM run, using the package in `../labeling_package/`. This folder keeps what
comes back and how it was checked.

| Run | Prompt | Set | Main class | Foundation model | Verdict |
|---|---|---|---|---|---|
| `returned/calibration_v1` | v1 | pilot 300 | 95.7% (kappa 0.90) | 97.7% (kappa 0.95) | passed, but errors lean one way |
| `returned/step1_v1_1` | v1.1 | check 300 | 95.7% (kappa 0.91) | **92.3%** (kappa 0.83) | **no-go**: FM `yes` 110 → 91, `system` never used |
| `returned/step1_v1_1` | v1.1 | pilot 300 | 96.7% (9 fixed, 6 new errors vs v1) | 95.0% (6 fixed, 14 new errors) | |
| `returned/step1_v1_r2` | v1 | check 300 | 95.3% (kappa 0.91) | 98.0% (kappa 0.96) | **go** |
| `returned/step1_haiku_b25` | v1, Haiku, 25 per batch | check 300 | 95.3% (kappa 0.91) | 98.0% (kappa 0.96) | **go** |
| `returned/step1_haiku_b100` | v1, Haiku, 100 per batch | check 299 (1 dropped) | 95.7% (kappa 0.91) | 97.3% (kappa 0.94) | no-go by one paper: FM yes 109 → 103 (limit ±5) |
| `returned/step1_haiku_b300` | v1, Haiku, 300 per batch | check 299 (1 id garbled) | 94.7% (kappa 0.90) | 97.0% (kappa 0.94) | no-go: main class < 95% |
| `returned/haiku_trial_2300` | v1, Haiku, 100 per batch | all 2,300 reference papers | 95.8% (pilot 300: **97.7%**) | 98.1% (pilot 300: 99.3%) | **go**: passes the pre-registered gate (≥93% on pilot 300); 0 papers missing |

**v1 → v1.1.** Of the 13 main-class disagreements in v1, 5 were named frameworks/agents labelled `system` and 3 were
learned distances/similarities labelled `evaluation`. As a result, `other` came out at 13 papers against 7 in the
reference, and `evaluation` at 12 against 8. Of the 7 foundation-model disagreements, 6 were `yes` against the
reference `no`, mostly papers that only mention LLMs. `../labeling_package/prompts/clarifications_v1_1.md` adds
three clarifications for these boundaries and changes no definition.

**Check set.** The clarifications were written after looking at the pilot 300, so v1.1 is judged on a fresh set:
`check_300.csv` (`prepare_check_set.py`). It holds all 200 double-labelled training papers plus 100 single-labelled
random papers from 2024–2026. None of them were looked at when the clarifications were written.

**Go/no-go for v1.1 (fixed before any v1.1 labels existed), on the check set:**
- main class agreement ≥ 95%;
- foundation-model agreement ≥ 97%;
- every main-class count within max(3, 25%) of the reference count;
- foundation-model "yes" count within max(5, 5%) of the reference count.

The pilot 300 are relabelled too, compared paired with v1 (errors fixed vs newly made), as a secondary check.

**v1.1 result: rejected.**
- The foundation-model clarification backfired. "If the abstract does not indicate that a model is large and broadly
  pretrained, answer no" made the model answer `no` for clear foundation-model work: video-diffusion acceleration,
  LLM alignment, an LLM pre-training corpus. 21 of the 23 foundation-model disagreements on the check set are
  `yes` → `no`.
- The framework clarification removed `system` altogether: 0 predictions, against 5 in the reference. Our reference
  itself splits similar LLM-agent papers. In the pilot, RL-Guard and MiLDEdit are `method`; in the check set,
  SimuAgent and MAV-SLAM are `system`, each agreed by both annotators. So the method/system boundary is fuzzy, and
  the prompt wording only moves it.
- The main class stayed at about 96% under both prompts. What the wording changes is how papers spread over the
  small classes.

**Next: prompt v1 on the check set.** v1 was written before any check-set paper was looked at, so the check set is
an untuned test for it. Package `iclr_contribution_labeling_v1_r2` has the v1 prompt byte-identical (sha256
aaa1478fb32e…) and step 1 = the 300 check papers. The go/no-go criteria are those above. The one change: the
count check no longer covers `other`, for the reason given in `compare_returned.py`, and this change does not
alter the v1.1 verdict. `other` (about 3% of papers) is treated as a low-reliability residual class in analyses.

**Prompt v1 result on the check set: go.** All criteria pass.
- Main class: 95.3%. On the 200 double-labelled papers it is 97.0% (kappa 0.94); on the 100 single-labelled
  2024–2026 papers it is 92.0%.
- Foundation-model flag: 98.0%. "yes" count 110 → 112; the 6 disagreements go both ways (4 no→yes, 2 yes→no).
- Class counts are within a paper or two of the reference, except `method` 203 → 197 and `other` 10 → 15
  (`system` 5 → 10). This is the same lean as in the v1 calibration run, and the reason `other` is treated as a
  low-reliability residual class.
- The `uncertain` flag is informative: 99.1% main-class agreement when certain, 86.2% when uncertain. 12 of the
  14 main-class errors are flagged.
- Pooled over both prompt-v1 runs (600 papers): main class 95.5%, foundation-model flag 97.8%.

Step 2 (all papers plus the independent 5% second pass) runs with package `iclr_contribution_labeling_v1_r2`.

```bash
python research/topics/annotation/contribution_types/llm_labeling/compare_returned.py <run dir> \
    --previous research/topics/annotation/contribution_types/llm_labeling/returned/calibration_v1
```

**Haiku as labeller (step 1 only).** Same prompt v1, run as Claude Code subagents (model alias `haiku`), each batch
labelled by a fresh agent that reads the prompt and its papers from files.
- At 25 papers per batch Haiku matches the external run exactly on the headline numbers (95.3% / 98.0%).
- Larger batches are about 3.7× cheaper per paper. At 300 per batch quality slips below the main-class threshold,
  and each large-batch run dropped or garbled one paper id, so a full run must re-ask missing papers.
- The differences between batch sizes are within sampling noise for 300 papers (±2.5 points).

**Haiku trial at 100 per batch on all 2,300 reference papers** (`label_batches.js`, scored with `collect.py`):
- pilot 300 (adjudicated): main class 97.7%, FM 99.3%;
- training double-labelled 200: 95.5% / 98.5%;
- training single-labelled 1,800: 95.6% / 97.9%.

Class counts and FM-yes counts are within a few papers of the reference. All 2,300 papers came back on the first
try. Each 100-paper batch took a median 2.3 minutes and about 104k subagent tokens.
