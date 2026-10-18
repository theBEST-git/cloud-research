# Work in progress: confirmation replication + pooled re-run (2026-10-18)

Working note for resuming after an interruption. Delete when the work is finished.

## Where things stand
- Done and committed:
  - released former-confirmation data (`data_confirmation/`, `data_confirmation_csv/` with author lists);
  - SPECTER2 vectors for 11,099 released papers (`research/topics/cache/specter2_released.npy`, git-ignored);
  - contribution labels for them (`research/topics/output/paper_contributions_released.csv.gz`; κ 0.93).
- In progress: the workflow "implement-pooled-confirmation" (run id `wf_d2a8daac-0e6`). Its stages:
  - A: topics side;
  - B: fashion plumbing and gate;
  - D: pooled features;
  - C: `ph5_confirm.py`;
  - then 3 reviews and a fix pass.
- The spec and maps are in the scratchpad: `final_round/POOLED_SPEC.md` and `final_round/pipeline_map.json`. Both are lost if the container was reclaimed; the decisions are summarised below.
- Files may be partial. This commit is a checkpoint, not a reviewed state.

## Resume steps
1. Check git status and whether the workflow finished. If the container still has the transcript, look at `~/.claude/projects/.../subagents/workflows/wf_d2a8daac-0e6/journal.jsonl`.
   - If the workflow died, resume it with `resumeFromRunId`.
   - If the container was reclaimed, finish the remaining stages from the committed files.
2. If git-ignored caches are missing, regenerate them in the background:
   - `research/topics/embed_specter2.py`, about 2 h, resumable chunks;
   - `embed_specter2_released.py`, about 30 min;
   - `research/fashion/build_pooled_inputs.py`, which builds the pooled author table.
3. Register everything in PREREGISTRATION.md before any confirmation outcome is read, then freeze and commit:
   - the confirmation tests (H1d, H2b′, H2c′, H3a and H4-FL as registered; PH5 E1 and P1b as primary, Holm over the two; E4, P7, teams H1, kwtiming A1 and premia out-of-sample as secondary);
   - the [C] clarifications collected by the review in `registration_items.md`;
   - the pooled exploratory plan.
   Then freeze with `freeze_confirmation.py` and commit.
4. Run `run_confirmation.py` once, then commit. After that, the pooled re-run (`run_pooled.py`, pooled RQ1, `ICLR_CORPUS=pooled posthoc.py`).
5. Update the presentation (plan: discovery stays the record; a new held-out slide; shortlist edits; pooled numbers labelled exploratory), then RESULTS.md, script.md and qa.md. Compile the PDF.

## Binding decisions (summary of the spec)
- **Corpus switch:** `ICLR_CORPUS=pooled`. When it is unset, everything is byte-identical to before.
- **Pooled order:** sorted by (year, submission_id).
- **Topic maps:** frozen. New papers get the nearest frozen centroid. The alternative maps use their exact refit centroids, gated on reproducing the saved labels.
- **Keywords:** the confirmation keywords use a lookup table learned on discovery; the discovery lists are never re-normalised.
- **Pooled features:** built on discovery ∪ confirmation, then filtered to confirmation for the tests (D14).
- **Frozen inputs:** the centring mean and τ = 0.90 stay frozen.
- **Writes:** never write `research/fashion/output/**`, `research/topics/output/**` or `FREEZE.json`.
