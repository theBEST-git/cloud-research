# Deviations from the pre-registration (docs/CLAIMS_PREREG.md, hash 75d8b5b3…)

## D1 — 2026-10-13 — primary annotator changed from Claude to ChatGPT (before any outcome was joined)
- **Change.** ChatGPT (PI's Codex/app, single pass per item) labels all 3,981 items and is the primary label source. Claude (default model, single pass) labels the 1,000-item robustness subset (`gpt_subset`) and takes the robustness role; decision rules in §6 apply with the roles swapped.
- **Reason.** On the PI calibration cases ChatGPT matched the PI 7/7 (Claude v1.3: 1/7) and its overreach prevalence is closest to the PI standard; a cheaper Claude model (Haiku) was tested on gold block 1 and rejected (abstract-overreach κ vs ChatGPT 0.45–0.63, self-agreement 0.42; results in outputs/claims_pilot/gold_b1_haiku_test.json).
- **Timing.** Recorded before any label of the main sample existed and before any outcome was joined to any claims item.
- **Safeguards.** Format validation; per-batch distribution drift checks; checks for templated or code-generated labels; MODEL.txt records model version and any mid-run model change.
