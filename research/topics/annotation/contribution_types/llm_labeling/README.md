# LLM labelling of all papers: returned runs and checks

Every paper is labelled by an external LLM run, using the package in `../labeling_package/`. This folder keeps what
comes back and how it was checked.

| Run | Prompt | Set | Main class | Foundation model | Verdict |
|---|---|---|---|---|---|
| `returned/calibration_v1` | v1 | pilot 300 | 95.7% (kappa 0.90) | 97.7% (kappa 0.95) | passed, but errors lean one way |

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

```bash
python research/topics/annotation/contribution_types/llm_labeling/compare_returned.py <run dir> \
    --previous research/topics/annotation/contribution_types/llm_labeling/returned/calibration_v1
```
