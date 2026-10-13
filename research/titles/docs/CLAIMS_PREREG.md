# Pre-registration: rhetorical overreach in ICLR titles and abstracts

Status: **frozen 2026-10-13, before any claim label is joined to a decision.** Codebook v1.4 and this plan are hashed in `outputs/claims_main/prereg_hashes.json`. No decision, withdrawal or review outcome has been read for any claims-study item at the time of freezing.

## 1. Questions

- **Q1 (trend).** Has rhetorical overreach in titles and abstracts risen over 2017–2026, and did it shift in the LLM-writing era (2024–2026)?
- **Q2 (review).** Is overreach associated with acceptance, positively (rewarded), negatively (penalised) or not at all (ignored)?
- **Q3 (where).** Does the title or the abstract carry the association, and does it differ from plain hype wording (boosters, superlatives) that does not exceed the evidence?

"Overreach" means rhetorical overreach as stated in the paper itself: a claim in the title or abstract that goes beyond the evidence the abstract reports (codebook v1.4, core principle 1). It is not a judgement of whether results are true; the full text is not read.

## 2. Data and sample

- **Frame.** The 43,482-submission ICLR 2017–2026 discovery universe (`outputs/core/universe.parquet`).
- **Sample.** `src/claims/sample_main.py`, seed 20261013: a simple random sample of 400 submissions per year (2017: 381 of 384 available), 3,981 in total, excluding the 500 items used in pilots and the gold set. Pooled estimates use weights N_year / n_year.
- **Robustness subset.** 100 random items per year (1,000) flagged `gpt_subset`, annotated additionally by ChatGPT and by a second Claude pass. If ChatGPT capacity is limited the subset is cut to the first 50 per year (500), chosen by item order, before any outcome is joined.

## 3. Measurement

- **Codebook.** v1.4 (`outputs/claims_pilot/CODEBOOK_v1_4.md`), frozen. It includes the PI calibration rules H1–H7 (`HUMAN_CALIBRATION.md`).
- **Annotators.**
  - Claude pass A covers all 3,981 items. Each subagent labels 50 items in file order, single pass, blind to decisions, titles of other items and other labels. This is the primary label source.
  - Claude pass B (reverse order) and ChatGPT (single model, single pass, PI's app) label the robustness subset.
- **Reliability achieved before freezing** (gold block 1, held-out 43 items), Claude v1.4 vs ChatGPT: title overreach κ 0.78–0.90, abstract overreach κ 0.67–0.72, four-way joint κ 0.70–0.73.
- **Variables.**
  - `T_claim` = title_strength ≥ 1.
  - `T_over` = title_vs_evidence ∈ {mild, clear}. Coded 0 for no-claim titles (NA) in the primary analysis; restricted to claim titles in a secondary analysis.
  - `A_over` = abstract_overreach ∈ {mild, clear}.
  - `Joint` = {neither, title only, abstract only, both}.
  - Hype flags: booster, superlative, universal; hedge.
  - Overreach types.
  - Contribution type.
- **QC.** Schema validation of every output file. Chunks that fail are re-run once with the same instructions. Item-level label files are hashed before outcomes are joined.

## 4. Outcomes and populations (joined only after Claude pass A is complete and hashed)

- **Primary population: reviewed submissions.** ACC, REJ or WD, excluding desk-rejected and other.
- **Primary outcome:** acceptance (ACC vs REJ + WD, i.e. among all reviewed submissions; withdrawal counts as non-acceptance).
- **Secondary outcomes:**
  - acceptance among decided papers (ACC vs REJ);
  - withdrawal (WD vs ACC + REJ).

## 5. Analyses

### Primary family (Holm-adjusted, four tests, two-sided α = 0.05)

| ID | Estimand | Model |
|---|---|---|
| P1 | Change in A_over prevalence, 2024–26 vs 2018–23 | Weighted logit of A_over on era indicator + linear year; inference by wild cluster bootstrap over years (Webb weights, 9,999 draws) |
| P2 | Same for T_over | Same |
| P3 | Association of A_over with acceptance | Logit of acceptance on A_over + year FE + topic50 FE + log team size + contribution type; SEs clustered by topic50 |
| P4 | Association of T_over with acceptance | Same as P3 with T_over |

### Secondary (no multiplicity claim)

- S1: P3 and P4 entered jointly, plus the Joint category (title only / abstract only / both vs neither).
- S2: P3 and P4 among decided papers, and for withdrawal.
- S3: T_over among claim titles only.
- S4: Era interaction, i.e. whether the association differs in 2024–26.
- S5: Hype flags (booster, superlative) in the same model as overreach, separating hype wording from overreach.
- S6: Overreach types (scope, certainty, magnitude, novelty, causal, unsupported) as separate indicators.
- S7: Heterogeneity by contribution type.
- S8: Prevalence by year, with weighted shares and Wilson CIs.

### Exploratory

- E1: Camera-ready check. Items in the sample that have a pre-decision arXiv v1 abstract (`cache/arxiv_audit_*`) get their v1 title and abstract labelled with v1.4. Compare overreach in v1 vs the final version, for ACC vs REJ.
- E2: Misclassification-corrected estimates. Use the Claude-vs-ChatGPT confusion matrix on the robustness subset, assuming non-differential error.

## 6. Decision rules

- **Rewarded / penalised.** P3 or P4 has Holm-adjusted p < 0.05 with OR > 1 (rewarded) or OR < 1 (penalised), **and** the estimate is label-robust.
- **Label-robust.** On the robustness subset, the ChatGPT-label estimate has the same sign as the Claude-A estimate on the same subset, and their difference is within 1.96 bootstrap SEs.
- **Ignored.** The 90% CI of the OR lies within [0.80, 1.25] (TOST). Otherwise the result is reported as inconclusive.
- **Trend.** P1 or P2 is significant after Holm, and the sign agrees under ChatGPT labels on the subset.
- **Interpretation.** All associations are observational. Overreach is not randomly assigned; better papers may both claim more and be accepted more. The within-paper title-vs-abstract contrast (S1) is the closest we get to holding paper quality fixed.

## 7. Power (two-sided α = 0.05, 80% power, design effect 1.3)

| Exposure | Acceptance | Withdrawal |
|---|---|---|
| A_over (prevalence ~0.5) | MDE OR ≈ 1.25 | ≈ 1.29 |
| T_over (~0.15) | ≈ 1.37 | ≈ 1.43 |
| T_over, claim titles only (n ≈ 2,000) | ≈ 1.40 | — |

The robustness subset is for label agreement, not for standalone tests (MDE ≈ 1.6–1.9).

## 8. Blinding and order of work

1. Label all 3,981 items with Claude pass A; validate and hash.
2. Write the analysis code. Dry-run it with **permuted** decisions (within year) to check the code end to end.
3. Join real decisions and run the pre-registered models exactly as specified.
4. Add the robustness-subset labels (Claude B, ChatGPT) as they arrive. They are produced blind to decisions.

Any deviation from this plan is logged in `outputs/claims_main/DEVIATIONS.md` with its reason and timing.
