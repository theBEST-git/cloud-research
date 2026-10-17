# Pre-registration: research fashion in ML (ICLR 2017–2026)

**Registered:** 2026-10-13, by commit on branch `claude/clever-edison-oe9pzv`. The git history is the time stamp.
**Status at registration:** contribution labels for the full corpus do not exist yet; they are being produced by an
external LLM run. No analysis of these hypotheses has been run on real labels or on acceptance outcomes.

## What had been seen before registration (disclosure)

- **Topic layer:** topic assignments, quality checks, k sweep and hindsight check. All of it is outcome-blind and
  label-free.
- **Hindsight check result** (`research/topics/README.md`): the published map is dominated by 2024–2026 papers.
  - It shows as many emerging topics as a map fitted on 2024–26 alone, and half as many declining topics as a
    year-balanced map.
  - Diversity trends reverse depending on which years define the topics.

  This result is the reason for the mandatory hindsight variants below.
- **Label validation:** contribution labels for 2,300 papers, used only to validate the labelling:
  - reference labels for 300 pilot papers and 2,000 training papers;
  - LLM labels for 600 of them (the pilot 300 and the 300 check papers, which are a subset of the 2,000).

  No RQ analysis was run on them.
- **Earlier exploratory work on the same corpus:** keyword popularity vs acceptance, and title style vs acceptance.
  Some of it found that popularity-based keyword portfolios lag their complements. RQ3 is therefore not naive about
  popularity and acceptance; its hypotheses are stated with that knowledge.
- **Code dry-runs:** the analysis code was tested only on synthetic labels (shuffled, or with a planted effect).

## Data and units

- **Corpus:** discovery split, 43,480 submissions with a usable abstract.
- **Topics:** published middle level, 100 topics (`research/topics/output/topic_assignments.csv.gz`). Other maps
  (k75, k150, year-balanced, era-specific) are in `k_sensitivity_assignments.csv.gz` and
  `hindsight_assignments.csv.gz`.
- **Contribution labels:** LLM labels, prompt v1 (sha256 `aaa1478f…`), merged by `merge_labels.py` into
  `research/topics/output/paper_contributions.csv.gz`.
- **Main classes:** method (incl. `model`), theory, empirical, dataset_benchmark, evaluation, other. `other` is not
  analysed on its own; its validation showed low reliability.
- **Label quality gate (before any RQ analysis):** the full run must reach
  - main-class agreement ≥ 93% with the 300 pilot reference papers;
  - second-pass main-class kappa ≥ 0.80.

  If it fails, the labels are not used for the RQs until the cause is understood. Any fix is documented as a
  deviation.

## Variables (all prospective: computed from years before t unless noted)

| Name | Definition |
|---|---|
| `maturity` | log(1 + papers in the topic in all years before t) |
| `fm_adoption` | share of the topic's year t−1 papers labelled foundation_model = yes |
| `hot` | topic's `prior_growth` (share in t−1 over share in t−2, counts + 0.5) is in the top 20% of topics that year |
| `measurement` | primary class dataset_benchmark or evaluation |
| `studies_models` | primary class empirical or evaluation |
| `incumbent` | at least one author ID (exact `declared_id_key`) has an ICLR paper in the same topic in an earlier year |
| `accepted` | `decision == 'accepted'` (RQ3 only) |

## RQ1: Rise (outcome-free)

How does a topic's contribution mix change as it matures? The foundation-model era is the main case.

**Model:** paper-level linear probability model with topic and year fixed effects, SE clustered by topic.
Years 2018–2026. Code: `research/fashion/rq1_rise.py`.

| ID | Outcome | Regressor | Prediction |
|---|---|---|---|
| H1a | method | maturity | negative |
| H1b | measurement | maturity | positive |
| H1c | empirical | maturity | positive |
| H1d | model (new architecture, fine type) | fm_adoption | negative |
| H1e | studies_models | fm_adoption | positive |

Exploratory, not tested: whether the measurement rise comes earlier in a topic's life than the empirical rise
(class shares by maturity tercile); theory share vs maturity.

## RQ2: Following

Who joins hot topics, and do they bring different contributions? Years 2019–2026 (incumbency and `hot` need
earlier years).

**Models:** linear probability models with SE clustered by topic.

| ID | Population | Outcome | Regressor | Fixed effects | Prediction |
|---|---|---|---|---|---|
| H2a | all papers | incumbent | hot | topic, year | negative |
| H2b | all papers | method | incumbent = 0 | topic × year | negative |
| H2c | all papers | measurement | incumbent = 0 | topic × year | positive |

**H2d (conditional): buzzword use.** For keywords typed `research_area` or `specific_topic` and used by ≥20 papers:
1. Compute each keyword's centroid in year t from papers using it before t.
2. A paper's use of the keyword is *atypical* if its similarity to that centroid is below the 10th percentile of
   earlier users of the keyword.
3. *Buzzword use* = the paper lists at least one keyword in the top 20% of keyword growth (t−1 vs t−2) and uses
   it atypically.

H2d predicts that buzzword use is more common among non-incumbent papers (topic × year fixed effects; positive).

The measure must first pass a blind validation:
- 100 flagged and 100 non-flagged uses of the same keywords;
- judged "keyword central to the contribution?";
- flagged uses must be judged peripheral at least twice as often as non-flagged uses, and in ≥50% of cases.

If validation fails, H2d (and H3c) are dropped and reported as such.

## RQ3: Reward (acceptance)

**Population:** `administrative_status == 'ordinary_submission'`, `outcome_eligible == 1`,
`decision in {'accepted','rejected'}`. Years 2018–2026.

**Model:** linear probability model of `accepted` with topic and year fixed effects, contribution-class dummies and
`foundation_model`, SE clustered by topic.

| ID | Regressor | Prediction |
|---|---|---|
| H3a | maturity | negative |
| H3b | maturity × method (vs all other classes) | negative |
| H3c (conditional on H2d validation) | buzzword use | negative |

Exploratory, not tested: the foundation-model gap in acceptance within topic-year; acceptance by
incumbency.

## Decision rule, multiple testing, robustness

- **Holm correction** within each family: H1a–e, H2a–c (+H2d), H3a–b (+H3c), at α = 0.05, two-sided.
- **Supported** = all of the following; everything else is "not supported", and all estimates are reported
  either way:
  - predicted sign and Holm-adjusted p < 0.05 in the main specification;
  - predicted sign in at least 75% of robustness variants;
  - predicted sign in both mandatory hindsight variants.
- **Main specification:** map k100, all papers in the population.
- **Mandatory hindsight variants:** a hypothesis is supported only if its sign is also as predicted under
  - the year-balanced map;
  - the 2017–2020-only map applied to 2021–2026 papers (fully prospective topics).

  These variants also count among the robustness variants.
- **Robustness variants:**
  - maps k75 and k150 (k sweep);
  - year-balanced and 2017–2020-only maps (hindsight check), and the 2017–2020-only map on 2021–2026;
  - k100 restricted to papers that keep their topic in ≥2/3 refits;
  - k100 without mixed topics;
  - k100 without `uncertain` labels;
  - k100 without 2026.
- **RQ3 also:**
  - logit instead of the linear probability model;
  - first submission per `family_id` only.
- **Label error:** report the second-pass reliability next to every RQ1/RQ2 estimate.
- **Interpretation:** all results are associations between topic dynamics, contribution types and acceptance; none is
  a causal effect of choosing a topic.

## Confirmation

When the held-out confirmation split is available:
1. Assign topics with the frozen model (`research/topics/assign_topics.py`, no refitting).
2. Label it with prompt v1.
3. Run the same code.

Alternative maps (k75, k150, balanced, early) are frozen the same way. Each topic's centroid is the normalised mean
of its discovery papers' projected embeddings (from the saved assignments), and confirmation papers go to the
nearest one.

Hypotheses supported in discovery are tested there one-sided at α = 0.05 in the predicted direction.

## Deviations

Any change to this plan after registration is listed here with its date and reason.

- **2026-10-15, label source.** The full-corpus labels were produced in this project with Claude Haiku subagents
  (prompt v1 unchanged, batches of 100, one fresh agent per batch), not by the external run. The plan never fixed
  the model.
  - Haiku was validated first on the check set and on all 2,300 reference papers.
  - The full run passed the label-quality gate before any RQ analysis: 97.7% main-class agreement with the pilot
    300, and second-pass kappa 0.93.
  - Run record: `research/topics/annotation/contribution_types/llm_labeling/returned/haiku_full_v1/`.

### 2026-10-15: pre-run log for RQ2 and RQ3

Written before any RQ2 or RQ3 variable was built and before any acceptance outcome was analysed. Facts checked
without outcomes:
- 2017–2020 author IDs are 98–99.6% email-based; 2021 is 85% profile-based and 2025–26 are 100% profile-based;
- `family_id` is unique per submission;
- the registered RQ3 population leaves out 9,986 withdrawn submissions.

Tags:
- **[C]** clarifies something the registration left open; it defines the main specification.
- **[R]** replaces an infeasible item; it counts in the 75% rule.
- **[S]** supplementary; reported, never part of the verdict.
- **[E]** planned exploratory analysis; always labelled exploratory.

**Clarifications [C]**

- **D1. Earlier ICLR paper (for `incumbent`).** Any earlier discovery submission with a topic, whatever its status or
  outcome. No outcome is ever used to build RQ2 variables.
- **D2. Incumbency mechanics.**
  - Author = exact `declared_id_key`. Positions without a key are ignored.
  - "Earlier" means strictly before year t; history starts in 2017.
  - "Same topic" uses the map under analysis, so incumbency is recomputed for every map.
  - Email and profile IDs are not bridged, and names are not matched.
  - Two known gaps: the 2021 ID-type switch, and earlier papers that sit in the held-out confirmation split. Both
    turn true incumbents into newcomers, so they bias towards zero.
  - Papers without any author key are dropped from RQ2.
  - For the confirmation run, history = discovery ∪ confirmation papers before t.
- **D3. `hot`.** The map's `prior_growth` (from `topic_year_maturity.csv.gz`) is at or above the 80th percentile
  (numpy linear) of that map's topics in year t. It is computed on the full corpus before any sample filter.
- **D4. H2b–d mechanics.**
  - Regressor: `newcomer = 1 − incumbent`.
  - The topic×year fixed effect is absorbed as one group; no year dummies.
  - Singleton topic-year cells are dropped.
  - SE clustered by topic.
  - A control without variation in a variant is dropped and logged; the tested regressor is never dropped.
- **D5. H2d construction.** Everything uses only papers from before year t.
  - Embedding: raw SPECTER2 vectors, L2-normalised, no PCA (the PCA was fitted on all years).
  - Eligible keyword in year t: typed research_area or specific_topic, ≥20 papers overall (as registered), and ≥10
    users before t.
  - Centroid: normalised sum of the earlier users' vectors.
  - Reference set: leave-one-out cosine of each earlier user to the centroid of the others. A use is *atypical* if
    the paper's cosine is below the 10th percentile (numpy linear) of that set.
  - Keyword growth: `((c_{t−1}+0.5)/N_{t−1}) / ((c_{t−2}+0.5)/N_{t−2})`, where N is the number of papers with a topic
    that year. A keyword is *hot* if its growth is at or above the 80th percentile of that year's eligible keywords.
  - *Buzzword* = the paper lists at least one hot keyword and uses it atypically. Papers without an eligible hot
    keyword are 0.
  - Keywords match by exact string. Years 2019–2026.
- **D6. H2d blind validation.**
  - Sample: 100 flagged (paper, hot keyword) uses, at most one per paper. Each is paired with a non-flagged use of
    the same keyword in the same year (nearest year if none), from a different paper.
  - Judges see only the title, the abstract and the one keyword. Items carry random ids, the two items of a pair go
    to different batches, and each judge gets its own shuffle.
  - No key file exists during judging; the scorer rebuilds the key from the seeded sampler. Judge transcripts are
    audited for reading other files.
  - Three independent LLM judges: two Opus runs with different batch orders, and one Sonnet run. Forced choice:
    - *central*: the main contribution proposes, studies or is chiefly evaluated on what the keyword names;
    - *peripheral*: background, motivation, a minor component, an application mentioned in passing, or an umbrella
      label the paper does not specifically address.
  - A 20-item pilot outside the sample checks the format only; then the instructions are frozen.
  - An item is peripheral if at least 2 of 3 judges say so.
  - **Gate passes** if p_flag ≥ 0.50 and p_flag ≥ 2·p_nonflag. One attempt only; the thresholds are not re-tuned.
- **D7. One model per hypothesis.**
  - Base = class dummies (reference `method`) + foundation-model dummy + topic FE + year dummies.
  - H3a = base + maturity.
  - H3b = base + maturity + maturity×method.
  - H3c = base + buzzword, years 2019–2026 (buzzword needs t−2).
- **D8. Logit variant.**
  - Maximum-likelihood logit with topic and year dummies, Newton steps with step-halving.
  - Topics with no variation in the outcome are dropped and reported.
  - CR1 cluster sandwich by topic, scaled G/(G−1)·(N−1)/(N−K) to match statsmodels; p-values from t(G−1).
  - The verdict uses the sign of the log-odds coefficient. Average marginal effects are reported for reading only.
- **D9. Variant mechanics.**
  - Variables are built on the full corpus first; sample filters come after.
  - A variant that cannot be estimated counts as wrong sign.
  - Counted variants:
    - RQ2: k75, k150, balanced, early, early_prospective (2021–26), stable_papers, coherent_topics, certain_labels,
      without 2026, and R2.
    - RQ3: the same nine (without R2), plus logit and R1.
- **D10. Holm families follow the H2d gate**, read from `output/h2d_validation.json` and never set by hand: {H2a–c}
  plus H2d if the gate passes; {H3a–b} plus H3c if it passes.
- **D11. Label error.**
  - Report the second-pass κ (0.93) and the class-specific agreement for `method` and `measurement` next to each RQ2
    estimate.
  - S8 corrects H2b–c for misclassification.
- **D12. Equivalence and power.**
  - Smallest effects of interest (SESOI): H2a ±2 pp; H2b ±2 pp; H2c ±1 pp; H2d ±1 pp; H3a and H3b ±1 pp per log
    unit; H3c ±2 pp.
  - A non-supported hypothesis is reported as *equivalent to null* if its 90% CI lies inside the bounds, otherwise as
    *inconclusive*.
  - The minimum detectable effect at 80% power (MDE80) from the dry-runs is added here at freeze.
  - Equivalence statements about RQ1 are labelled post hoc.
- **D13. Outcome-blind protocol.**
  - Only `outcomes.py` may name outcome or review columns; a lint test enforces this.
  - Its permuted and simulated modes are used for dry-runs. Its real mode refuses to run unless the hashes in
    `FREEZE.json` match, git is clean, and the call comes from `run_frozen.py`.
  - The real run happens once and is committed immediately. A bug found afterwards: fix, rerun, report both, log it.
- **D14. Confirmation split.** New variables are recomputed on discovery ∪ confirmation with the frozen code, the same
  keyword list and the same τ.

**Replacements [R] (counted in the 75% rule)**

- **R1. "First submission per family" is vacuous**, because `family_id` is unique per submission. It is replaced by
  *no probable earlier version*.
  - Drop a paper if an earlier-year paper has the same normalised title, or SPECTER2 cosine ≥ τ.
  - τ is calibrated without outcomes: three blind judges rate 4 cosine bins × 40 pairs, answering "Is B a revised
    version of A?".
  - τ is the lowest bin edge at which that bin and all higher bins get ≥90% majority "yes". If none qualifies: exact
    titles, or cosine ≥ the edge of the top bin.
- **R2. ID-consistent years (RQ2).** The same models on 2019–2020 plus 2023–2026, leaving out the 2021–22 ID
  transition.

**Supplementary variants [S]** (never part of the verdict)

- **S1.** + log(team size), in all RQ2 and RQ3 models.
- **S2.** H2a with pool controls: maturity, log(1 + papers in t−1), log team size.
- **S3.** Incumbency from a fixed two-year window (t−1, t−2), 2023–2026 only.
- **S4.** Incumbency ignoring the paper's own probable earlier version.
- **S5.** Fine-level topics.
- **S6.** H2d and H3c among papers that list at least one hot keyword.
- **S7.** H2d and H3c with fixed effects for the number of eligible keywords.
- **S8.** H2b–c corrected for label misclassification.
- **S9.** RQ3 with withdrawals after review (`administrative_status == 'withdrawn'` and at least one review) counted
  as not accepted. Excluding them conditions on a choice made after review; counting them brackets the estimate.
  Withdrawals before review are excluded from both.
- **S10.** RQ3 + newcomer control.
- **Fragile flag:** a supported hypothesis is marked *fragile* if any S-variant is significant (p < 0.05) with the
  opposite sign.

**Planned exploratory analyses [E]**

| ID | Analysis |
|---|---|
| E1 | Foundation-model acceptance gap within topic-year |
| E2 | Acceptance by incumbency |
| E3 | Withdrawal as an outcome, after vs before review |
| E4 | Heterogeneity by era (2018–20, 2021–23, 2024–26) for H2b–c and H3a–b |
| E5 | Newcomer × hot |
| E6 | Dose-response plots after removing fixed effects (H1d, H2a, H3a) |
| E7 | Buzzword decomposition: listing a hot keyword vs atypical use |
| E8 | Acceptance of new-architecture papers by prior FM adoption |
| E9 | Equivalence tests (TOST) and MDE80 for all non-supported hypotheses |
| E10 | Acceptance trend by contribution class |

Anything added after the freeze is labelled post hoc.

- **2026-10-15, before any judging: judge models.** On cost and speed grounds, model tier is matched to task
  difficulty.
  - H2d judges (D6): two Sonnet runs with different batch orders, plus one Haiku run, replacing two Opus runs plus one
    Sonnet run.
  - R1 resubmission judges: two Haiku runs plus one Sonnet run.
  - Gate, thresholds and majority rule are unchanged.
- **2026-10-15, before any judging: D15, resubmission similarity.**
  - R1 uses the cosine of mean-centred SPECTER2 embeddings. Raw SPECTER2 cosines are compressed (median 0.95), so
    the raw percentiles would mostly pick papers on the same topic.
  - The four judging bins are fixed at centred cosine [0.80, 0.85), [0.85, 0.90), [0.90, 0.95) and [0.95, 1].
  - The bins come from an outcome-free check: the share of nearest-earlier pairs with a shared author key rises from
    17% to 57% to 97% to 100% across these bins (profile-ID years only).
  - The τ rule is unchanged.
- **2026-10-15, before any RQ2/RQ3 estimate: review round A (variable builders).** Two independent reviewers
  (prospectivity and blinding; conformance), each blocker or major finding checked by a separate verifier. No blocker
  and no confirmed major finding. Changes made:
  - Exact ties at the 80th percentile are now decided exactly. Keyword growth is rounded to 10 decimals and the fine
    map's `prior_growth` to 6 decimals (as the maturity file already was), so logically equal values are bit-identical
    and all of them count as hot under "at or above". Effect: 12 papers' `lists_hot` and 76 fine-map (S5) hot flags; no
    `buzzword` value and no main-map flag changed.
  - Tests added for ties, the keyword eligibility boundary, hot keywords over eligible keywords only, atypical use,
    per-paper flags and S4 chains; each was checked to fail on a deliberately broken copy of the code.
  - The outcome lint now also catches sealed names inside query strings and calls to the loader's private readers,
    and checks the loaded corpus columns at runtime.
  - S4 follows the paper's whole chain of probable earlier versions ("own earlier version" read as the chain).
  - D15 clarification: the centring mean is the mean over all discovery papers, a fixed constant (saved as
    `output/specter2_centring_mean.npy`) that the confirmation split (D14) reuses unchanged.
- **2026-10-15, P3 results, before any RQ2/RQ3 estimate.** Judges, prompts and samples as in D6, R1 and the judge-model
  entry. Format-only pilots outside the samples; instructions unchanged afterwards. Every batch answered in full; the
  transcript audit found 0 reads of anything but the instructions and the judge's own batch.
  - **H2d validation gate: fails.** Peripheral share (2 of 3 judges) among flagged uses 0.42 (95% CI 0.33–0.52), among
    non-flagged uses 0.15 (0.09–0.23); ratio 2.8. The ratio condition holds, but p_flag < 0.50. Fleiss κ 0.77.
    As registered (D6, D10), **H2d and H3c are dropped**; the Holm families are {H2a, H2b, H2c} and {H3a, H3b}; S6 and
    S7 lapse. The exploratory analyses that use the buzzword variable (E3, E7) are still run and reported, labelled as
    using a measure that failed validation. `output/h2d_validation.json`.
  - **τ = 0.90** (R1). Majority-yes share by centred-cosine bin: 0.10, 0.475, 0.90, 1.00; Fleiss κ 0.99.
    170 papers get a probable earlier version (167 by cosine, 3 more by exact title); 93.5% of them share an author key
    with it. `output/resubmission_tau.json`, `output/checks/resubmissions.json`.
- **2026-10-15, before any RQ2/RQ3 estimate: review round B (analysis code).** Four independent reviewers (numerics
  and leakage/blinding; conformance and data plumbing), each blocker or major finding checked by a separate verifier.
  Confirmed and fixed:
  - Blinding. (i) Estimates no longer carry sample means except in the frozen run: in a dry-run, the mean of a product
    of two real columns (E5's newcomer x hot) would reveal the H2a relationship. (ii) The RQ2 and exploratory guard
    now fails closed: a dry-run must simulate every outcome-side column (incumbent and its S3/S4 versions, method,
    measurement, buzzword, lists_hot), and newcomer is then derived from the simulated incumbency. (iii) The loader's
    permuted mode moves each paper's whole derived block (populations and outcomes together) to a random paper of the
    same year, so it no longer reveals any paper's real status.
  - Also: the entry-point check uses the resolved path; the outcome lint covers the loader's private readers and the
    permuted mode; run_frozen.py records every attempt (and any traceback) before it touches real data and needs
    `--rerun-reason` for a second run; scipy and matplotlib versions are recorded; exploratory rows that use the
    buzzword measure carry a "failed validation" status and are listed in the summary; a withdrawal without a review
    count is an error (there are none); the S8 misclassification rates use the random reference stratum only
    (method 0.905 instead of 0.920); freeze.py refuses a dry-run that does not come from the current code and inputs,
    misses a hypothesis, or fails criterion (a) or (b) without a registered remedy.
  - **Disclosure.** Before fix (ii), one reviewer's end-to-end check with simulated outcomes left the real `lists_hot`
    in place, so the exploratory E7 row "lists_hot ~ newcomer | topic x year" was computed on real data, and its value
    (about −0.012, p ≈ 0.01) reached the analyst. That exploratory estimate is therefore not blind and is reported as
    seen before the freeze. No reviewer computed any confirmatory relationship (H2a–c, H3a–b) or any acceptance result.
  - A first dry-run (v1), started before review B, was stopped once review B showed its power design was flawed;
    none of its results were written or seen.
- **2026-10-15, before any dry-run v2 result: D16, dry-run design and criteria.**
  - Blinding as above; results keep coefficients, SEs, p-values, sample sizes and verdicts only.
  - RQ2 data-generating process: each outcome's variance components (topic, year, topic-specific linear trend,
    topic-year cell beyond binomial noise) are calibrated by method of moments from that outcome's own topic-year cell
    means on k100 (no regressor involved; calibration recovers known components on synthetic data). Simulated
    incumbency is paper-level, shared by all maps.
  - RQ3 data-generating process: no real acceptance information is used, because topic-level acceptance trends are
    close to H3a itself. Base 0.32, sd_topic 0.05, sd_year 0.03, and two settings for the components that drive the SE
    of a within-topic regressor: lo (sd_cell 0.02, sd_trend 0.004) and hi (sd_cell 0.04, sd_trend 0.016).
  - Nulls (500 replications each): RQ2 with structure on k100 and on the early map; RQ3 with the loader's permuted mode,
    k100 lo, k100 hi and early hi.
  - Power: one hypothesis planted at a time (others null) at 0.5, 1, 1.5, 2 and 3 x SESOI on the k100 regressor
    (H3b on the interaction centred at the mean method share, so H3a stays null); 200 replications (RQ3 lo: 100),
    main specification only; full decision rule at 1 and 3 x SESOI with 100 replications. The realised effect is the
    main-specification coefficient with the true probability as outcome (clipping included).
  - Detection = predicted sign and p < 0.05/m in the main specification (m = family size, Holm's first step).
    **MDE80** = realised effect at 80% detection, linear interpolation; frozen for RQ2 (calibrated) and RQ3 (hi
    setting, the conservative one); RQ3 lo reported alongside.
  - **Criteria.** (a) Main-specification size (two-sided p < 0.05) within [0.02, 0.08] for every confirmatory
    hypothesis and null scenario. (b) The full decision rule supports a hypothesis in at most 5% of null replications.
    (c) Detection at 3 x SESOI >= 80%; otherwise the hypothesis is reported as underpowered.
  - **Remedy, fixed now.** If (a) fails upwards or (b) fails for a hypothesis, its confirmatory p-value is computed by a
    wild cluster restricted bootstrap (Rademacher weights by topic, null imposed, 9,999 draws) instead of CR1 with
    t(G−1), implemented and validated before the freeze, and logged. A downward size violation is only reported.
- **2026-10-15, before any dry-run v2 result: review round B2 (re-review of the round-B fixes).** Three reviewers
  (blinding; dry-run design; fix conformance), verifiers as before. No blocker. Two confirmed major findings, fixed:
  - The permuted mode still shuffled only among the ids the caller passed, so a chosen subset got its own real
    outcomes back. It now shuffles the derived block of the whole table within year and only then selects the ids;
    the result for any subset equals the matching rows of the full permutation (tested). The dry-run always passed the
    full corpus, so no dry-run output was affected.
  - `freeze.py --remedy` accepted any text as a waiver of every problem, and the registered bootstrap remedy did not
    exist. Now: a stale digest, replication counts other than the registered ones (500 / 200 / 100), or a missing
    hypothesis are always fatal; only an upward size violation (> 0.08) or false support > 0.05 can be remedied, and
    only by `bootstrap:<hypothesis>` for exactly the hypotheses concerned, which freeze.py refuses until the wild
    cluster bootstrap is implemented; run_frozen.py refuses to start if FREEZE.json lists a remedy it does not apply. A
    size below 0.02 is only reported, as D16 says.
  - Minor fixes: the entry point is checked on every call and the verification is released when the run ends; a
    refused rerun verifies nothing; attempts are counted by their "started" line; the dry-run digest also covers the
    topic maps, the contribution labels and the outcome table; E9 rows say explicitly when 80% detection was not
    reached; and new tests fail when any of the round-B/B2 fixes is reverted (checked by mutation).
  - **Disclosure.** To write the loader, the analyst once read the distinct values of `decision`, `administrative_status`
    and `outcome_eligible`, and whether `review_count` has missing values (none, including among withdrawals), with an
    ad hoc command outside `outcomes.py`. No counts, rates or joins with any other column were computed.
- **D16 amendments, before any dry-run v2 result.**
  - Power grid: 0.5, 1, 1.5, 2, 3, 4 and 6 x SESOI, so that an MDE80 above 3 x SESOI is located instead of undefined.
    Criterion (c) is still read at 3 x SESOI.
  - Realised effect: the main-specification coefficient with the planted part of the true probability (with minus
    without the planted effects, same random draws) as the outcome, so the topic and cell draws add no noise to it.
  - MDE80 notes flag a value at or below the smallest planted effect, beyond the grid, or on a curve that dips below
    80% again after crossing it.
- **2026-10-15, before any dry-run v2 result: review round B3 (re-review of the round-B2 fixes).** Two reviewers,
  verifiers as before. **No confirmed blocker or major finding**, which ends the review loop of the plan. One reported
  major (the permuted mode's seeded shuffle can be re-created and inverted by someone who deliberately reimplements the
  loader) was judged by its verifier to be deliberate circumvention, which the protocol already forbids; the loader's
  description now states this limit. Minor fixes: the frozen run refuses to run under a debugger, a trace function or an
  interactive session; E9 carries the dry-run's MDE80 notes (and FREEZE.json the low-variance notes too); freeze.py
  also requires every registered null scenario, full-rule power for every hypothesis and no missing p-values in any
  null scenario; and tests now fail when any round-B2/B3 fix is reverted (mutation-checked, incl. the frozen run's
  refusal order, release and attempt log, the remedy rules, the realised-effect measurement, the grid, the permuted
  block and the derived newcomer columns). The first dry-run v2 launch was stopped at 4% to apply these fixes; none of
  its results were written or seen.
- **2026-10-15, dry-run v2 results (D16), before any RQ2/RQ3 estimate.** 12,400 jobs on the final code; outputs kept in
  `output/dryrun_v2/` (code digest in its provenance file).
  - **Criterion (a) fails** in one scenario: under the RQ2 null whose structure follows the early map, the main
    specification rejects 12.6% of the time for H2b and 10.0% for H2c (all other sizes 3.8–7.2%, incl. RQ3's permuted
    real-loader null). The cause: there the simulated regressor (newcomer) and outcome share a topic structure that cuts
    across k100 topics, which k100-clustered standard errors do not capture.
  - **Criterion (b) passes**: the full decision rule supports a hypothesis in at most 3.2% of null replications.
  - **Criterion (c)**: H3a reaches only 54% detection at 3 x SESOI (high-variance setting; 88% in the low setting), so
    it is reported as underpowered; H2a, H2b, H2c and H3b reach 80% by 3 x SESOI.
  - MDE80 (realised effect at 80% detection with p < 0.05/m): H2a 3.6 pp, H2b 1.7 pp, H2c 1.1 pp (CR1);
    H3a 4.1 pp per log unit (2.8 in the low setting), H3b 2.4 pp per log unit (2.1).
  - **The registered remedy is triggered for H2b and H2c**: their confirmatory p-values will come from the wild cluster
    restricted bootstrap (Rademacher weights by k100 topic, null imposed, 9,999 draws). Because this bootstrap still
    clusters by k100 topic, it is not expected to remove a bias from structure that cuts across k100 topics; a validation
    dry-run (v3, same seeds) measures its size in every null scenario, and the result is reported whatever it is.
  - **New supplementary analysis S11, declared now:** every confirmatory model re-estimated with two-way clustered
    standard errors (k100 topic and early-map topic; Cameron–Gelbach–Miller, with the larger one-way variance if the
    two-way variance is not positive; p from t(min(G1, G2) − 1)). It is reported next to each verdict and enters the
    fragile flag like any S-variant; it does not change the decision rule. Its size is also measured in dry-run v3.
- **2026-10-15, before any RQ2/RQ3 estimate: review round B4 (the remedy and S11 code).** Two reviewers (remedy
  statistics; wiring and protocol), verifiers as before. The bootstrap matches a brute-force implementation exactly and
  the two-way variance matches statsmodels; no wrong estimate, verdict or blinding break was found.
  - **One confirmed major finding, fixed:** no test exercised the remedy wiring behaviourally (17 of the reviewer's 26
    wiring mutations left the suite green). `tests/test_remedy_wiring.py` now runs RQ2 and RQ3 on simulated outcomes
    and checks that each remedied hypothesis gets the registered bootstrap p-value (9,999 draws, seed 20261015, on the
    confirmatory population) in its Holm family while everything else is unchanged; that S11 rows exist for every
    hypothesis and cluster by the early map; that `run_frozen.py` passes FREEZE.json's remedies to both families; and
    that dry-run v3's null and power replications record and use the right p-values; and, end to end on a fabricated
    dry-run, that `freeze.py` records the remedies with their validation and refuses anything else. All 29 mutations
    the analyst tried (the reviewer's surviving kinds plus the new checks) are caught.
  - **Not a defect (verifier), now stated:** for H2b and H2c only the p-value comes from the bootstrap. The CIs, TOST
    and the "equivalent to null" label stay CR1 with t(G−1), as D8 and D12 define them and as D16 registered (it
    replaces only the confirmatory p-value). A CR1 interval can therefore exclude zero beside a bootstrap p above 0.05,
    or the reverse. The summary and E9 now name both methods next to each verdict, and S11 is reported beside each
    verdict as the cross-check of the CR1 interval. No bootstrap-inverted interval is added: that would be a new,
    unregistered method.
  - **Minor:**
    - A bootstrap p-value can be exactly 0 (no draw reaches |t|). It stays as registered (share of |t*| ≥ |t|), is
      stored as 0 in the outputs and is reported as "< 1/9,999". The alternative (1 + count)/(B + 1) would raise every
      bootstrap p by (1 − p)/(B + 1) ≤ 10⁻⁴ and a Holm-adjusted p by at most 3 × 10⁻⁴, so it could change a decision
      only if a Holm-adjusted p fell in [0.0497, 0.05); that would be reported.
    - In `rq2_null_early` and `rq3_null_early_hi` the two-way size is close to tautological, because those nulls'
      structure lies on the early map, which is S11's second clustering. Those sizes show the two-way variance is
      computed correctly; they do not show S11 is robust to cross-cutting structure along other maps.
    - `freeze.py` now also refuses a dry-run that lacks:
      - a bootstrap size for any remedied hypothesis, or an S11 size for any hypothesis, in any null scenario;
      - complete null replications;
      - any CR1, bootstrap or two-way p-value. A missing one would have counted as a non-rejection in the summary's
        sizes.
    - The S11 combination and the early-map column now have tests that run without statsmodels.
  - None of these changes touches a file in the dry-run digest. Dry-run v3, started from the committed remedy code,
    stays valid.
- **2026-10-15, before any RQ2/RQ3 estimate: review round B5 (re-review of the round-B4 fixes).** One reviewer and its
  verifiers. The code changes were found correct and safe for the real freeze and run, and the B4 commits touch no file
  in the dry-run digest. The reviewer's own 18 mutations exposed test gaps:
  - **Confirmed major, fixed:** no test checked the *value* of the bootstrap p-value. The wiring tests compared the
    pipeline with the same function, so a one-sided, signed or complementary p (1 − p) went unnoticed. A test now
    checks p = share of |t*| ≥ |t| against an independently computed t (t* is pinned by the brute-force test), with
    negative, positive and very large t.
  - **Confirmed, minor after verification, fixed by tests:**
    - S11 reaches the fragile flag in both families, and a significant opposite S11 makes a supported hypothesis
      fragile.
    - The S11 values in `summary.json` match the two-way estimates.
  - **Other minors fixed by tests:**
    - the RQ3 simulated dry-run job records all three p-values;
    - MDE80 uses the bootstrap p, and the CR1 MDE80 uses the CR1 p;
    - the two-way fallback (including a variance of exactly 0) and its CIs;
    - Holm treats a missing p as 1;
    - `freeze.py` refuses a missing CR1 p;
    - the printed result line shows the bootstrap p.
  - Two statements in the B4 entry were corrected above: the early-map caveat also applies to `rq3_null_early_hi`,
    and the bound on the p = 0 convention.
  - The reviewer's 18 surviving kinds plus two more, re-applied by the analyst, are all caught by the new tests. One of
    them (S11's second cluster count read from the first) is invisible on the real maps, which both have 100 topics,
    and is caught by a direct test.
  - No file in the dry-run digest was changed.
- **2026-10-15, dry-run v3 results (remedy validation), before any RQ2/RQ3 estimate.** 12,400 jobs with v2's seeds; the
  CR1 sizes, false-support rates and MDE80 inputs reproduce v2 exactly, so v3 is the same simulation with the bootstrap
  and two-way p-values added. Outputs: `output/dryrun/`; reported diagnostics: `dryrun_diagnostics.py` →
  `output/checks/dryrun_v3_diagnostics.json`.
  - **The registered remedy does not restore size under the cross-map null.** In `rq2_null_early` the bootstrap
    rejects 12.4% (H2b) and 9.6% (H2c) of the time at nominal 5% (CR1: 12.6%, 10.0%). In all other null scenarios its
    size is 3.8–6.4%. This is as anticipated, since the bootstrap still clusters by k100 topic. So if the real data
    hold topic structure that cuts across k100 topics, the confirmatory p-values of H2b and H2c are anti-conservative.
    In the simulated cross-map scenario they reject about 10–12% of the time at a nominal 5%. How strong such
    structure is in the real data is unknown.
  - **S11 (two-way clustering):** size 4.4–7.6% in every null scenario. In `rq2_null_early` it is 7.6% (H2b) and
    7.0% (H2c): better, not good, although it clusters on the very map that generates that null's structure (round
    B4). Per round B7's reproduction, one-way clustering on that map gives 8.2%, so no simple clustering choice
    restores 5% there; CR1 with these 100 unbalanced clusters is itself part of the problem.
  - **Criterion (b) passes, but the decision rule does not neutralise the size problem** (corrected after round B7;
    figures in the diagnostics file).
    - **Per hypothesis:**
      - the full rule supports a hypothesis in at most 3.2% of the replications of any null (H2b 3.2%, H2c 3.0% in
        `rq2_null_early`; identical to v2), so criterion (b), which is defined per hypothesis, passes;
      - "significant in the opposite direction" occurs in at most 2.8%.
    - **Per family, under the cross-map null:**
      - H2b or H2c is supported in 5.8% of replications;
      - some RQ2 hypothesis is supported in 6.4% (2.0% under the k100 null), above Holm's nominal 5%;
      - some directional claim (supported or opposite) is made in 11.2% (4.6%).
    - **RQ3, per family:** some hypothesis is supported in at most 2.8% of the replications of any RQ3 null, and some
      directional claim is made in 6.4% under `rq3_null_early_hi` (5.2% permuted). RQ3's family-wise error is
      approximate under the same caveat.
    - **The 75% and hindsight requirements give no protection against it.** Every H2b/H2c replication that was
      Holm-significant in the predicted direction also passed them (31 of 31), because the variants re-estimate on
      the same papers. The low per-hypothesis rate comes from Holm's α/3 and the sign requirement applied to
      t-statistics whose standard deviation is 1.31 (H2b) and 1.22 (H2c) instead of 1.
  - **Criterion (c):** H3a reaches only 54% detection at 3 x SESOI (88% in the low-variance setting), so it is
    reported as underpowered. All others reach at least 97%. Pre-declared reading (round B8):
    - every verdict in the frozen summary carries its MDE80 and underpowered flag;
    - a supported H3a is reported with the caveat that, at this power, estimates that reach significance overstate
      the effect;
    - a non-supported H3a is reported as uninformative about effects below its MDE80 (about 4 pp per log unit), never
      as evidence of no effect.
  - **MDE80, frozen** (realised effect at 80% detection with p < 0.05/m):
    - H2a 3.6 pp;
    - H2b 1.7 pp and H2c 1.1 pp with the bootstrap p (CR1 1.70 and 1.10);
    - H3a 4.1 pp per log unit (low-variance setting 2.8);
    - H3b 2.4 pp per log unit (2.1).
  - **Equivalence labels at "1 x SESOI"** (diagnostic): H2a 3%, H2b 3%, H2c 19%. The H2c effect realised there is
    0.8 pp, because clipping at the low base rate of measurement papers shrinks it. That is inside its ±1 pp bounds,
    so those labels are not false equivalences.
  - **Decision, made blind to every RQ2/RQ3 estimate.**
    - **The confirmatory procedure stays as registered:** H2b/H2c take their p-value from the bootstrap, and the
      decision rule is unchanged.
    - **Not adopted: S11 as the confirmatory test.** Its improvement in the failing scenario comes from clustering on
      that scenario's own map and still leaves 7–8%; it is no evidence that S11 controls size under other
      cross-cutting structure.
    - **Not adopted: requiring both p-values** (an intersection–union rule, corrected reason after round B7). It can
      only be stricter than the registered test. Round B7's reproduction of the dry-run seeds suggests a small power
      cost (0.5–3 points near the MDE) and family-wise false support of 4.4% under the cross-map null. It is still
      not adopted, for three reasons:
      - it would change the registered decision rule after the validation run;
      - its power is not part of the frozen dry-run;
      - its benefit rests on the same scenario.
      It is reported instead: the S11 qualifier below is its reporting form. Under the cross-map null, "supported
      without the qualifier" occurs for some RQ2 hypothesis in 4.4% of replications (1.4% under the k100 null).
    - **No registered element protects against cross-k100 structure.** The H2b/H2c p-values, and family-wise error
      under such structure, are therefore reported as approximate, with the figures above.
    - **Pre-declared reporting qualifiers** (extended to all directional and equivalence claims after round B7):
      - S11's p-values are Holm-adjusted within each family (a missing p counts as 1).
      - A "supported" or "significant in the opposite direction" verdict whose S11 estimate lacks that verdict's sign,
        or has an adjusted p ≥ 0.05, is reported as "not robust to two-way clustering (S11)".
      - An "equivalent to null" verdict whose S11 90% CI is not inside the SESOI bounds is reported as "equivalence
        not robust to two-way clustering (S11)".
      - Verdicts are unchanged; `run_frozen.py` computes the qualifiers mechanically (tested).
      - The qualifier flags about 44% (H2b) and 33% (H2c) of the false supports under the cross-map null, and per
        round B7's reproduction it would also flag about 0.5–4% of true effects near the MDE.
    - **Pre-declared stress sensitivity for H2b and H2c** (round B7):
      - p from the CR1 t-statistic divided by its standard deviation under `rq2_null_early` (1.3078 and 1.2198,
        computed by `freeze.py` from the v3 replications and frozen in `FREEZE.json`), with t(G − 1);
      - Holm-adjusted within the family, the other hypotheses keeping their p;
      - written beside each remedied verdict as a sensitivity, never as the verdict.
      - The factor comes from one simulated scenario. It is a bracket, not a correction: its rejection rate is 4.2%
        (H2b) and 4.8% (H2c) in that scenario (calibrated in-sample) and 0.6% and 1.8% under the k100 null
        (diagnostics file, `stress_p_size`).
    - **Reporting:**
      - the main-specification p-values of H2b and H2c are described as approximate;
      - their CR1 CIs, TOST p-values and "equivalent to null" labels are approximate in the same way (round B8). Under
        the cross-map null the 95% CI covers 0 in 87.4% (H2b) and 90.0% (H2c) of replications (1 minus the CR1
        size). Round B8's approximate reproduction (shifting the null replications to the SESOI bound, ignoring
        clipping) finds a false equivalence in about 8–11% (H2b) and 8–9% (H2c), about 6–8% with the S11 equivalence
        qualifier, against about 4–7% under the k100 null. The S11 equivalence qualifier is the pre-declared check;
        no stressed interval is added;
      - the v3 sizes (copied from `FREEZE.json` into the frozen summary) and the stress sensitivity are stated next to
        them.
    - **What `FREEZE.json` will record:**
      - the size violations as `dryrun_problems`;
      - the remedies `bootstrap:H2b` and `bootstrap:H2c`;
      - the v3 bootstrap and two-way sizes as `remedy_validation`;
      - the stress inflation factors;
      - the hashes of the v3 diagnostics and of the v2 summary.
- **2026-10-15, before any RQ2/RQ3 estimate: review round B6 (re-review of the round-B5 fixes).** One reviewer and its
  verifiers.
  - **Found sound:** the B5 tests are deterministic and use simulated data only, and the B4/B5 log statements are
    accurate.
  - **Five confirmed major test gaps in the decision path,** all pre-dating B5 (the code was correct):
    - Holm-adjusted values were tested only against the same `holm()`.
    - The four legs of "supported" were not value-tested: the inclusive 75% share, both hindsight variants (present
      and same sign), the sign of the main estimate, and the Holm-adjusted bootstrap p as the significance test.
    - The fragile flag was not tested for unsupported hypotheses or at its p threshold.
    - The default Rademacher weights of the bootstrap were untested.
    - The dry-run's counts were untested: detection at p < 0.05/m with the predicted sign, false support, full rule.
  - **Fixed by `tests/test_decision_rule.py` and new estimator tests,** with hard-coded expected values, including:
    - Holm step-down, running maximum and cap;
    - every verdict and the equivalence/TOST definitions (90% interval, t with the estimate's df, both one-sided
      tests);
    - the default 9,999 seeded Rademacher draws by topic;
    - the dry-run's family sizes (m = 3 for RQ2, 2 for RQ3).
  - **Mutation check:** all 18 surviving mutations the reviewer listed, plus the mirror mutation of the other one-sided
    TOST test, are now caught. Two minor test weaknesses (the printed p-value, the two-way fallback mock) were fixed as well.
  - **Statsmodels cross-checks:** the full suite (115 tests) passes with statsmodels available, so the cross-checks
    that are skipped by default were also run.
  - No file in the dry-run digest was changed.
- **2026-10-15, before any RQ2/RQ3 estimate: review round B7 (the dry-run v3 decision and its code).**
  - **Reviewers:** an Opus methodologist and a Sonnet code-and-numbers reviewer, with Sonnet verifiers. The
    methodologist reproduced dry-run seeds on simulated data only.
  - **Sound:** keeping the registered remedy, and not making S11 the confirmatory test. The qualifier code and the
    diagnostics reading are correct, and the v3 numbers check out.
  - **Confirmed major findings (log statements), fixed by correcting the v3 entry above:**
    - The entry credited the 75% and hindsight requirements with protecting against the cross-map structure. They
      removed none of the 31 main-specification false positives of H2b/H2c.
    - "At most 3.2%" was per hypothesis; the family-wise rate under the cross-map null is 6.4%.
  - **Reviewer majors judged minor by their verifiers, acted on anyway:**
    - The stated reason for not requiring both p-values did not apply to that stricter rule. The reason is now
      corrected.
    - The qualifier covered only "supported". It now also covers "significant in the opposite direction" and
      "equivalent to null".
  - **Minor findings, all acted on:**
    - The S11 wording is now "better, not good".
    - The "approximate p" commitment was prose only. A frozen stress-calibrated sensitivity and the v3 sizes are now
      written into the frozen summary.
    - A test now covers a missing S11 p within a family.
    - `FREEZE.json` now also hashes the v3 diagnostics, the v2 summary and provenance, and the cross-map replications.
  - **Diagnostics** (`dryrun_diagnostics.py`) now reproduce every family-wise and conditional figure quoted above.
    They also check that the CR1 columns (coef, se, p, n) and verdicts of every null scenario are identical in v2 and
    v3.
  - **Mutation check:** 8 mutations of the new reporting code are all caught.
  - No file in the dry-run digest was changed.
- **2026-10-15, before any RQ2/RQ3 estimate: review round B8 (re-review of the B6/B7 fixes; last before the
  freeze).**
  - **Reviewers:** an Opus reviewer of the log and method, and a Sonnet reviewer of code and tests, with Sonnet
    verifiers.
  - **Checked and correct:**
    - every number in the corrected v3, B6 and B7 entries;
    - the diagnostics script, which reproduces its committed output;
    - `freeze.py`'s checks on the real outputs: no fatal problem, remediable = {H2b, H2c}, inflation 1.3078/1.2198.
  - **No confirmed blocker or major finding, which ends the review loop.** Both reported majors were judged minor by
    their verifiers:
    - the CIs, TOST and equivalence label of H2b/H2c are approximate too (now stated above, with figures);
    - the registered specification table and variants were not pinned by tests (now `tests/test_registered_spec.py`).
  - **Minor findings, all acted on:**
    - The E9 table now carries the S11 qualifiers.
    - Every verdict carries its MDE80 and underpowered flag, and H3a's reading is pre-declared above.
    - The frozen run refuses a `FREEZE.json` without the stress factors before reading any data.
    - Two degenerate inputs (no second cluster count; zero SE) no longer crash.
    - The single-scenario origin of the 10–12% and of the stress factor is stated, with the stress p's rejection
      rates.
    - RQ3's family-wise rates are stated.
    - New tests cover verdict precedence and the CIs' t(G − 1).
    - New tests check that every hashed output exists, and cover the diagnostics functions.
  - No file in the dry-run digest was changed.

### 2026-10-15: post-run record (nothing below changes the frozen analysis)

- **The single frozen run.**
  - Attempt 1 of `run_frozen.py` started at 19:03:11 UTC and finished at 19:03:29 UTC.
  - It ran on commit e08ece3, whose `FREEZE.json` has sha256 15bc822e…548fd6.
  - It exited normally. Its outputs were committed unchanged in 604f41c, before any interpretation, with the printed
    result lines in `stdout.txt`.
  - There was no rerun and no deviation after the run. The results are reported in `RESULTS.md`.
- **Figures.** After the run, `figures.py` was edited for presentation only (F1 titles; F7 legend). These are the
  only code changes since the freeze. They read the frozen outputs and change no number.
- **Registered for the confirmation split** (post hoc, from the discovery results, before any confirmation data
  exist).
  - Besides H1d, as registered, three hypotheses are tested one-sided at α = 0.05 with the same frozen code, variants
    and decision rule, on the same model as their discovery counterpart:
    - **H2b′:** newcomer papers are more likely to be method papers (positive);
    - **H2c′:** newcomer papers are less likely to be measurement papers (negative);
    - **H3a:** acceptance decreases with topic maturity (negative, the registered direction).
  - H2b′ and H2c′ reverse the discovery predictions because discovery found the opposite. They are new hypotheses,
    and are labelled so.
- **Tests after the run.** `test_frozen_run_refuses_a_debugger_or_trace_function` called `run_frozen.py`, which now
  refuses earlier because the attempt log holds the single run. It now calls the guard directly, and was
  mutation-checked. No analysis code was changed.
- **Audit round C** (two Sonnet number checkers, one Opus interpretation auditor, Sonnet verifiers).
  - No wrong number or verdict was found in `RESULTS.md` or the README.
  - Confirmed overstatements, corrected:
    - the reference labels are LLM labels, not human labels;
    - the H3a and H3b summaries stated non-significant results as findings;
    - the stress factor is a single-scenario bracket, not "the worst";
    - "holds in every variant" ignored S1;
    - the README lacked the association and approximation caveats;
    - the incumbency undercount extends to every year after 2020;
    - "One venue" was misattributed to the confirmation split;
    - newcomer was described as "no author published" instead of the registered definition.
  - Minor wording and completeness fixes were made as well.
  - One auditor premise was checked and rejected: mean prior FM adoption is 29%, not 1.6%, so E8's 0 → 100% scale
    is not an extreme extrapolation.
- **Audit round C2** (one Sonnet checker of every statement changed after round C).
  - Corrected: the RQ1 early-map remark now names only H1a/H1b, since H1c has the wrong sign there.
  - Also fixed:
    - the two H3a readings were made consistent;
    - H3a's power is now given for both variance settings;
    - "before any RQ2/RQ3 estimate" now says "confirmatory", with the E7 exception;
    - the treatment of downgraded review findings is stated accurately;
    - the τ-judge models are stated as unregistered rather than replaced;
    - experience at other venues is now outside D2's undercount.

### 2026-10-16: post hoc exploratory analyses (declared before they were run)

- **PH1: among newcomer papers, what goes with a higher acceptance rate?** (`posthoc.py`; the question came from the
  user after the results.)
  - **Population:** E2's population (RQ3 filter, at least one author ID, 2019–2026); newcomer as in D1/D2.
  - **A1:** newcomer papers only. Acceptance ~ class (ref. method) + FM + team-size band (ref. 3–4) + hot +
    maturity, with topic FE and year dummies.
  - **A2:** newcomer papers only. Acceptance ~ class + FM, with topic × year FE.
  - **B:** the newcomer gap within topic × year, separately by class, FM, team-size band, hot and maturity tercile.
  - **C:** by the 20 coarse areas:
    - the newcomer gap within topic × year;
    - newcomer acceptance minus the year's overall acceptance, per area and per area × year (cells with ≥ 50
      newcomer papers).
  - **Inference:** CR1 SE by k100 topic. Holm within each block, to rank evidence only.
  - **Status:** everything is exploratory and post hoc. These are associations, not effects. Nothing is
    confirmatory.
- **Access to outcomes.** Real outcomes reach post hoc code only through `outcomes.load("posthoc")`. It refuses
  unless all of the following hold:
  - the caller is `posthoc.py`;
  - the frozen run has finished;
  - no debugger is attached;
  - the tree is clean, so the code is committed before it reads.

  Each access is logged to `output/posthoc/access_log.jsonl`. The pipeline was first run end to end on simulated
  outcomes; under that null, nothing survived Holm.
- **PH2: which contribution types and areas favour small or large teams?** (`posthoc.py ph2`; declared before it
  was run.)
  - **Population:** the RQ3 filter, 2018–2026, at least one author. Team size is capped at 16.
  - **Within topic × year, controlling class and FM:**
    - acceptance per doubling of team size;
    - team-size bands 1–2, 5–6 and 7+ against 3–4.
  - **Groups:** overall (plus a newcomer control on papers with an author ID), and separately within each
    contribution class and each of the 20 coarse areas. Holm is applied across the slopes of each set.
  - **Heterogeneity:** a joint Wald F for equal slopes across groups.
  - **Calibration first, on simulated null outcomes (40 seeds).**
    - The per-group slope tests rejected 5.1% of the time and the band tests 4.8%.
    - The Wald F with its nominal F(q, G − 1) reference rejected 10% for classes and 90% for areas. Each area's
      interaction rests on about 5 topic clusters.
    - Its p-value is therefore replaced by one calibrated on the real design: the same F on 200 simulated null
      outcomes (dry-run RQ3 lo/hi settings; real papers, topics, years and team sizes).
  - **Status:** exploratory and post hoc. These are associations: team size also stands for resources and
    seniority.
- **PH3: is the newcomer acceptance gap about who the authors are?** (`posthoc.py ph3`; declared before it was
  run; the question came from the user: newcomer papers may simply be weaker.)
  - **Data:** author-level rows for PH1's population, with each paper weighing 1 in total.
  - **Fixed effects:** topic × year and author, absorbed jointly.
  - **Controls:** class, FM, log2 team size, and the author's earlier ICLR submissions.
  - **Models:**
    - M1: newcomer paper, with author FE;
    - M2: the author is new to the topic, with author FE;
    - M3 and M4: newcomer paper with first-author or last-author FE, one row per paper.

    Each is shown next to the same model without author FE on exactly the same sample.
  - **Inference:** CR1 SE by topic; two-way topic × author SE as a check.
  - **Reading:** if the gap shrinks with author FE, it mostly reflects who writes newcomer papers. If it stays,
    entering a topic goes with lower acceptance for the same person.
  - **Validation:** the estimator was checked against explicit dummies and `fe_ols` in tests. The pipeline was run on
    simulated null outcomes, with all estimates near 0.
- **Review scores (the user's second request) are not available.** The repository has no review ratings, and the
  OpenReview API refuses this environment with a challenge. A conditional-on-scores analysis needs the ratings from
  the upstream corpus.
- **PH4: which research areas are accepted more or less often, and how does that change over time?**
  (`posthoc.py ph4`; declared 2026-10-17, before it was run. The user and their supervisor asked for it after seeing
  the earlier keyword × year acceptance grid.)
  - **Disclosure.** That earlier exploratory grid (23 author keywords, before registration) already showed some
    patterns, for example a falling gap for federated learning. PH4 is therefore not a test of those keywords. It adds
    a systematic screen of every eligible area, with uncertainty and a multiple-testing correction.
  - **Population:** the RQ3 filter (decided ordinary submissions), 2018–2026.
  - **Units, two sets.**
    - K: author keywords typed `research_area`, `specific_topic`, `property` or `application_domain` and used by at
      least 200 discovery submissions (any outcome). That is 68 keywords, fixed before the run. A paper belongs to a
      keyword if it lists it. Keywords are chosen by authors, so they carry no topic-map hindsight.
    - T: the 100 k100 topics. These are content-based and carry the hindsight caveat.
  - **Cell gap:** for unit u and year t, g = the acceptance rate of u's papers minus that of all other papers in year t.
    Its binomial variance uses the rates shrunk to (k + 0.5) / (n + 1).
  - **Level L:** the average of g over 2018–2026, weighted by u's papers per year.
    - Its SE comes from the cell variances, multiplied by max(1, √φ). φ is the weighted dispersion of g around L
      across the years with at least 10 papers in u (m years). This allows for year-to-year shocks within an area.
    - The p-value uses t(m − 1).
    - **Recent level R:** the same over 2024–2026, using the unit's φ and m.
  - **Trend S:**
    - weighted least squares of g on year, with weights 1/variance, over the years with at least 10 papers in u, in
      pp per year;
    - SE multiplied by max(1, √(weighted RSS / (m − 2))); p from t(m − 2);
    - estimated only if m ≥ 4. Otherwise the unit is "too new for a trend".
  - **Check:** the level adjusted for contribution class, FM and log2 team size (a linear probability model with
    year fixed effects, HC1 SE). It shows whether type or team size explains the gap.
  - **Multiple testing:**
    - Benjamini–Hochberg FDR within each set (K, T) and each estimand (L, R, S); q < 0.05 is "flagged";
    - Holm is reported alongside;
    - **calibration:** 200 within-year permutations of acceptance on the same units; we report the per-test rejection
      rate at 0.05 and the share of permutations with any BH flag.
  - **Selection rules for figures:**
    - the keyword map shows level against trend for every keyword with a trend, labelling the flagged ones;
    - the trend panels show up to four flagged keywords with the most negative trends and up to four with the most
      positive, by trend estimate, plus "federated learning" as the motivating example, flagged or not;
    - topic m029 ("Federated learning") is reported next to the keyword.
  - **Reading:** these are associations. A falling gap means papers in that area were accepted relatively less often
    over time. That may reflect reviewers' views, the quality or composition of the papers, or who submits them. It is
    not a judgement of an area's merit.
  - **Validation before the run:**
    - unit tests of the gap, level, trend and BH computations against direct calculations;
    - an end-to-end run on simulated outcomes (rq3 and accepted drawn at random by year), checking that per-test
      sizes are near 5%.
  - **PH4b, mechanism probes** (added 2026-10-17 at the user's request, before PH4 was run). These ask *why* an area's
    gap moves, not only whether it does.
    - **Units:** the keywords whose trend is flagged, plus "federated learning" (the PH4 trend-panel rule, at most 9).
    - **Candidate explanations, each with a probe:**
      1. **Composition / influx.** Less experienced authors and smaller teams move in. Probe: the trend of the gap
         after adjusting acceptance for contribution class, FM, log2 team size and "established author" (an author
         with an accepted ICLR paper in an earlier year, any topic; uses earlier outcomes, inside this run). The
         adjustment is an LPM with year FE on all PH4 papers, and the adjusted gap uses the residuals. We report the
         share of the raw trend that the adjustment removes.
      2. **Change in how the area's papers are judged** (reviewer scepticism or saturation of ideas; the supervisor's
         reading for federated learning). Probe: does the decline also appear among papers by experienced authors?
         We report the trend of the gap separately for the unit's papers with and without an established author, and
         with and without a keyword incumbent (an author ID with an earlier discovery submission listing the
         keyword, any outcome). Each subgroup is compared with all papers outside the unit.
      3. **Hype cycle.** Probe: the year in which the keyword's share of all discovery submissions peaks, and whether
         the decline comes before or after it. This is descriptive.
    - **Composition by year:** for the population, newcomer and established-author shares, mean team size, method
      share and FM share; the keyword's share of all submissions.
    - **Reading rules, fixed now:**
      - If the adjusted trend keeps at least half of the raw trend, and the decline also appears among established or
        incumbent papers, the pattern points to a change in how the area's papers are judged, not only to who submits
        them.
      - If the adjustment removes more than half, and the decline is confined to newcomer or non-established papers,
        composition is the leading explanation.
      - Anything in between is reported as mixed.
      - Operationally, "appears among established or incumbent papers" means that at least one of those two
        subgroups has a trend with the same sign as the raw trend and an unadjusted p < 0.05. "Confined to newcomer
        or non-established papers" means that neither experienced subgroup qualifies while at least one of the other
        two does.
      - None of this observes reviewers' beliefs. Those are explanations consistent with the data, not tested causes.
  - **PH4 validation result (before the real run).** On simulated outcomes (acceptance drawn at random, 40% within
    the simulated decided papers, no area effects), the end-to-end run flagged no unit in either set. The per-test
    rejection at nominal 0.05 was 0.4–1.4% for level, recent level and trend: the tests are conservative under pure
    binomial noise, because the dispersion factor never shrinks a SE and the t reference has few degrees of freedom.
    The method is kept as declared. Flags are therefore conservative, and a non-flagged area is not evidence of no
    change.
  - **PH4 run note.** The first real attempt stopped with an error before any estimate was written or printed: in
    the real population every decided paper has an author ID, so the `has_key` control in the PH4b adjustment was
    constant. Constant controls are now dropped, nothing else changed, and the run was repeated. Both attempts are in
    `output/posthoc/access_log.jsonl`.
- **Registered for the confirmation split after PH4 (2026-10-17, before any confirmation data exist): H4-FL.**
  - Primary: papers listing "federated learning" are accepted less often than other papers of the same year (the
    PH4 level, one-sided, α = 0.05).
  - Secondary: the FL gap's trend is negative (one-sided).
  - Same PH4 code, keyword rule and population definition.
  - This is a new hypothesis, derived from the discovery results and labelled as such.
- **PH5, the final post hoc round (declared 2026-10-17, before any PH5 module read a real outcome).** The user asked for
  results that help future authors choose topics and chase trends well, with rich multi-feature relationships and no
  annotation.
  - **How the analyses were chosen.** 56 ideas from 7 lenses were merged into 27 candidates. Three judges scored them
    on value to authors, feasibility, richness, novelty and soundness. A selector then fixed seven specifications
    (`scratchpad final_round/ideation.json`).
  - **How they were built.** One agent per analysis implemented it, working only on simulated outcomes
    (`ph5_common.simulated_frame`). A separate adversarial reviewer then fixed each module; all seven were marked ready
    and pass their tests.
  - **How they run.** The gated modules run once each through `python research/fashion/posthoc.py ph5 <slug>`.
    `ph5_forecast` reads no outcome and runs on its own.
  - **Status.** Everything is post hoc and exploratory. Holm and BH are applied within each module's declared families
    only. The results are associations, not causal effects.
  - **Data.** The held-out confirmation split is not in this repository (the export holds discovery papers only), so
    PH5 uses the discovery split. Re-running on pooled data, if the held-out split is exported later, is one command
    per module.
  - **Calibration.** The planned lead-run 200-frame calibration of every module was replaced, for time, by the
    development calibrations on record. These used 100–600 null frames for most declared tests, plus planted-effect
    recovery; the summaries are in the implementation reports. kwtiming (200 null reference frames) and position
    (nulls for the interaction tests) compute their calibrated p-values inside the real run.
  - **Mildly liberal tests.** The reviewers flagged several tests at about 6–8% under the null at nominal 5%: fmwave
    A2, C1 and C2; premia rho_1 and the flow slope; kwtiming D_E; pivot E3; teams H3–H5. They are reported with that
    caveat.
  - **Two decisions made now.**
    - fmwave keeps the specification's model as primary; the within-year (fm × year) model is a declared robustness
      check.
    - kwtiming family B counts as supported only if both its Holm p and its null-frame p are below 0.05.
  - **PH5 forecast (selection S6): does a hot keyword or topic stay hot over a project's lead time, and which signals visible when a new author keyword appears predict that it booms?**
    - `ph5_forecast.py` and `tests/test_ph5_forecast.py`; declared 2026-10-17.
    - **Outcome-free.** No acceptance outcome is read. `compute(k)` drops every outcome column and equals `compute_free()`.
      - This was verified: compute(simulated_frame()) reproduces the outcome-free outputs.
    - **Running it.** `python research/fashion/ph5_forecast.py` writes `output/ph5_forecast/*.csv`, `summary.json` and the figures.
    - **Disclosure.** The module was developed on the real outcome-free data, because nothing here needs gating. Three rules were changed after seeing first outputs, and all are now fixed:
      - **(i) EB ranking when the signal variance is zero.** Under the literal rule, every keyword was shrunk to the year mean in 2022-2024 and 2026, and all of them were flagged hot.
      - **(ii) Feature scaling.** Model features are standardised within their own cohort or year, not on the pooled training rows. FM share is 0 for every 2019 new keyword, so pooled scaling made it explode out of time.
      - **(iii) F7 centring (from the code review).** F7 is now centred on the year-t mean. The all-years centring constant carried papers after t into a feature at t.
    - **Reading.** Everything is exploratory: descriptions and forecasts of submission shares, not causal effects.
    - **Units (Part A).**
      - **Keywords:** every normalised author keyword in the topic-layer corpus.
        - Share = users_t / P_t, where P_t is the number of year-t papers listing at least one keyword.
      - **Topics:** early-map topics (prospective; the primary topic unit) and k100 topics (the hindsight contrast).
        - Share = papers_t / N_t.
      - **Eligible in t:** at least 10 users (papers) before t.
      - **Size band:** earlier users 10-19, 20-49, 50+.
    - **Growth and hot.**
      - **Raw growth:** g_t = log((c_t + 0.5)/P_t) - log((c_{t-1} + 0.5)/P_{t-1}).
      - **EB growth:**
        - v = 1/(c_t + 0.5) + 1/(c_{t-1} + 0.5).
        - Per year, over the eligible units: m_t = mean(g) and tau2_t = max(var(g) - mean(v), 0).
        - g_eb = m_t + tau2_t (g - m_t)/(tau2_t + v).
        - EB flags rank (g - m_t)/(tau2_t + v). This gives the same order as g_eb when tau2_t > 0, and is its limit when tau2_t = 0.
        - tau2_t = 0 occurs for keywords in 2022-2024 and 2026, for the early map in 2020, and for k100 in 2018 and 2020.
        - In those years EB hotness favours large units with above-mean growth.
      - **hot_t:** growth at or above the year's 80th percentile (numpy linear) among eligible units. Terciles falling / flat / rising use average ranks within the year.
    - **A1, persistence.**
      - **Pairs:** an eligible unit at origin t, joined to the same unit at t + h. Origins are 2018-2025 for h = 1 and 2018-2024 for h = 2.
      - **Estimates:**
        - P(hot_{t+h} | hot_t) and P(hot_{t+h} | not hot_t);
        - the base P(hot_{t+h}) in the same pairs;
        - lift = P(hot_{t+h} | hot_t) - base;
        - P(s_{t+h} > s_t) and P(s_{t+h} < s_t), given hot and not hot, and their differences.
      - **Breakdown:** by unit type x raw/EB x h x band.
      - **Inference:** a 999-draw unit bootstrap in which all pairs of a drawn unit move together. CIs are percentile intervals, and p = min(1, 2(1 + min(#draws <= 0, #draws >= 0))/(B + 1)).
      - **Declared tests:** the lift at h = 1, all bands, for keywords, the early map and k100.
        - **Primary family:** Holm over the three with raw growth (the registered hot rule).
        - **Secondary family:** Holm over the three with EB growth.
      - **What the lift does and does not test.**
        - The lift describes what an author observes. Its null (lift = 0) is not "no momentum".
        - Poisson noise in c_t, which g_t and g_{t+1} share, makes raw hotness anti-persistent even when log shares follow a random walk.
        - Observed lifts are therefore read against the pipeline benchmarks in calibrate(): a random walk, and AR(1) latent momentum phi = 0.5.
    - **A2, transitions.** P(state at t + h | state at t).
      - **Origin rows:** falling, flat, rising, plus an entry row (the first eligible year).
      - **Destination columns:** exit (fewer than 3 users at t + h; this overrides the tercile), falling, flat, rising.
      - **Breakdown:** h = 1 and 2; raw and EB; all units and by band. CIs come from the unit bootstrap.
    - **A3, hot spells.**
      - A spell is a maximal run of consecutive hot years.
      - **Censoring:** a spell still hot in 2026 is censored. It is known to last at least L years, so it is at risk of ending after d years only for d <= L - 1.
      - **Survival:** Kaplan-Meier S(d) = P(the spell lasts more than d years), with Greenwood normal CIs clipped to [0, 1]. By unit type, raw/EB, and the band at spell start.
    - **Part B, emerging keywords.**
      - **Risk set:** every normalised keyword whose first year with at least 5 users is t in 2019-2024. Fizzles are included.
      - **Boom:** s_{t+2} >= 2 s_t and users_{t+2} >= 10, using the coverage share.
      - **Continuous target:** log((users_{t+2} + 0.5)/P_{t+2}) - log((users_t + 0.5)/P_t), demeaned within cohort.
      - **Features at t, from papers <= t (a fixed list):**
        - F1: log users_t.
        - F2: log((users_t + 0.5)/P_t) - log((users_{t-1} + 0.5)/P_{t-1}).
        - F3: connected components of the year-t users linked by a shared declared_id_key, divided by users_t.
        - F4: the largest component's share of users.
        - F5: the share of users with an author ID that has any discovery submission in t-2..t-1. Computed for cohorts 2019, 2020, 2023 and 2024 only, and missing otherwise.
        - F6: the entropy (in nats) of the users' coarse areas.
          - This uses the 20-area coarse map of topic_assignments.csv.gz, which was fitted on all years (a hindsight partition), as the spec requires.
        - F7: the mean pairwise cosine of the users' SPECTER2 vectors.
          - Each vector is centred on the mean of all year-t papers and then L2-normalised.
        - F8: the FM share.
        - F9: the dataset_benchmark + evaluation share.
        - F10: the share of users whose lower-cased title contains the keyword string. This is a substring match, so plurals count.
    - **B1, screen.**
      - **Per feature:**
        - AUC for boom (ties count 1/2), with a 999-draw keyword-bootstrap percentile CI;
        - the AUC over same-cohort pairs only, as a check;
        - a two-sided pooled Mann-Whitney p.
      - **Correction:** Holm over the ten features.
      - **Terciles:** P(boom | pooled tercile), terciles by average rank, with Wilson CIs. Tied values share a tercile, so some terciles are empty.
    - **B2, out of time.**
      - **Rolling origin:** test cohort t in 2021-2024, trained on cohorts <= t - 2.
      - **Features:** z-scores within their own cohort.
      - **Baseline:** an unpenalised logit on F1 + F2.
      - **Full model:** an L2 logit on F1-F4 and F6-F10.
        - It minimises mean log loss + lambda/2 |beta|^2, with the intercept unpenalised.
        - lambda is chosen from {0, 10^-4 ... 10^1 in 11 log steps} by leave-one-cohort-out log loss.
        - When only one cohort trains, 5 random folds are used instead.
      - **Pooled metrics over the test cohorts:**
        - AUC, PR-AUC (average precision) and Brier score;
        - delta AUC, with 999 keyword bootstraps (percentile CI; p as in A1).
      - **OLS on the continuous target:**
        - baseline (F1 + F2) and full (the nine features);
        - out-of-time R2 = 1 - SSE/SST on the pooled test rows, Spearman, and delta R2, all with bootstrap CIs.
    - **B3.** P(boom | at least 3 components x at least 3 distinct coarse areas), with counts and Wilson CIs.
    - **B4, topics.**
      - **Maps:** the early map (primary) and k100 (hindsight contrast).
      - **Rows:** topic-years with at least 10 papers, origins 2019-2024.
      - **Target:** the log share ratio t -> t+2 (counts + 0.5), demeaned within year.
      - **Features at t, as within-year z-scores:**
        - g_t and log share;
        - FM share and the map-specific newcomer share;
        - measurement share and new-architecture share;
        - mean log team size.
      - **Models:**
        - momentum-only OLS;
        - size-only OLS;
        - ridge on all seven, with lambda from {0, 10^-3 ... 10^2} chosen by leave-one-year-out CV (5 folds when one year trains).
      - **Rolling origin:** test years 2021-2024, trained on years <= t - 2.
      - **Pooled metrics:**
        - out-of-time R2 and Spearman;
        - precision at the top quintile, within each test year;
        - delta R2 of ridge over each baseline;
        - all with 999 topic-cluster bootstraps.
      - **Conditional table:** P(top-quintile growth t -> t+2 | hot_t, size tercile, age tercile), with margins and Wilson CIs.
        - hot_t is the A1 raw flag; size and age terciles are within-year.
        - Age = t minus the first year with at least 10 papers (0 when that year is t; the registered variable is NaN there).
        - Topic-years not yet eligible for hot are left out.
    - **Robustness.**
      - **Keywords: paper share** (P_t = N_t). This leaves within-year growth ranks, and therefore the hot flags, unchanged.
      - **Keywords: LLM family left out** (llm|language model|gpt|chatgpt|foundation model|vlm|multimodal|agent|reasoning).
      - **What these two report:** A1 for keywords, B1 and B2.
      - **Part B:**
        - entry threshold 3 or 10;
        - horizon 3: cohorts <= 2023, test cohorts 2022-2023, training on <= t - 3.
      - **B4:** without papers in coarse areas c01, c02, c08, c10 and c15; everything is recomputed.
      - Near-synonyms are merged only through the existing normalisation.
    - **Reproduction check.** The prototype persistence numbers, rebuilt from the registered hot flags (keyword_year.csv.gz, and the panel hot flags of the early map and k100).
    - **Calibration** (`calibrate(n_null, n_planted, seed, rho=0.25, phi=0.5, beta=0.6, r2=0.15)`). Acceptance plays no role, so the forecast targets are simulated on the real panels.
      - **A1:**
        - **Null:** each year's hot flags are shuffled across that year's eligible units.
        - **Planted:** AR(1) latent hot score (rho) with hot = the top 20% within year. The true lift comes from the bivariate normal.
        - **Reported:** size, Holm family-wise size, bias, coverage and Holm power.
        - **Pipeline benchmarks:** counts are Poisson around a latent log share whose growth is AR(1) with phi = 0 (random walk) or phi. The innovation variance is the unit type's mean tau2.
          - Reported for raw and EB: the mean lift and the signed Holm rejection rates.
      - **B1/B2:**
        - **Null:** boom and the target are permuted within cohort.
        - **Planted:** a latent y = 0.6(z_F3 + z_F6) + logistic noise, with cohort offsets matching the boom rates. True AUCs come from the latent probabilities.
      - **B4 (early map):**
        - **Null:** the target is permuted within year.
        - **Planted:** target = sqrt(0.15) z_FM + sqrt(0.85) e.
    - **Figures** (in `output/ph5_forecast/`, as .png and .pdf): persistence bars, transitions heatmaps, Kaplan-Meier curves, feature-AUC forest plot, out-of-time ROC, B3 heatmap, and B4 predicted vs realised.
    - **Reading.** A hot or booming keyword describes where submissions move. It says nothing about whether such papers are accepted.
  - **PH5 fmwave (selection S2): riding the foundation-model wave. Does the FM acceptance premium fade as a topic saturates, and for whom?**
    (`posthoc.py ph5 fmwave`, module `ph5_fmwave.py`. Declared before it is run, built and tested only on `ph5_common.simulated_frame`, and run once on real outcomes. Post hoc and exploratory: all estimates are associations within topic × year.)
    - **Variables.** All are outcome-free, recomputed by the module from repo files and built on every discovery submission.
      - `fm`: the LLM label `foundation_model == yes`.
      - `adoption`: the k100 topic's FM share in t − 1 (`panel` `fm_adoption`).
      - `ladopt` = logit(clip(adoption, 0.02, 0.98)). l = ladopt − c, where c is the mean ladopt of the FM papers in the primary population (stored in the summary).
      - Adoption bins, left-closed: [0, 5%), [5, 15%), [15, 30%), [30, 50%), [50%, 100%].
      - `framed` = 1 if the title or the first abstract sentence (title and abstract from `topic_layer().embedded_corpus()`) matches, case-insensitive, `\b(LLMs?|large language models?|language models?|foundation models?|VLMs?|vision[- ]language models?|MLLMs?|multimodal (large )?language models?|GPT[- ]?\w*|ChatGPT|LLaMA\w*)\b`.
        - The first sentence is the text up to the first `.`, `!` or `?` that is followed by whitespace and then a capital letter, digit or bracket. A break is not taken after "e.g.", "i.e.", "al.", "vs." or "cf.".
      - `first_time`: no author ID of the paper has a discovery submission in an earlier year (any topic, any outcome). NaN if the paper has no author ID.
      - `code_link`: the abstract matches `github\.com(?!/anonymous)` (case-insensitive).
      - `fm_primary_area`: the primary area starts with "foundation or frontier models" (2025–26 only).
    - **Gated profile.**
      - `established` = `posthoc.established_authors(k)`: some author ID had an accepted ICLR paper in an earlier year, any topic.
      - `no_acc` = 1 − established for papers with an author ID (NaN otherwise).
    - **Population:** RQ3 decided papers, 2023–2026, with a prior-year adoption.
    - **Estimation.**
      - LPM with topic × year (k100 cell) fixed effects absorbed.
      - CR1 SE clustered by k100 topic, p-values from t(G − 1).
      - Check: a two-way (k100 topic, early-map topic) Cameron–Gelbach–Miller SE, each component with its own CR1 factor. If the two-way variance is not positive, the larger one-way variance is used. p from t(min(G1, G2) − 1).
      - Controls X: contribution class (reference: method) + log2 team size (capped 1–16) + topic newcomer + has_earlier_version. A control with no within-cell variation in a subsample drops out.
    - **Models.**
      - F1 bins: accepted ~ Σ_b fm × 1[bin b] + X. Descriptive, except the ≥ 50% bin, which is test A2.
      - F1 linear: accepted ~ fm + fm × l + X.
        - Crossing a* = expit(c − b_fm / b_fm×l).
        - CI: 999-draw cluster bootstrap by topic (seed 20261017), percentile CI. Each draw is the FE-OLS fit on the resampled topics, with a pseudo-inverse so that a control absent from a draw drops out. Draws outside [2%, 98%] are open ends; an open CI end is reported as 0 or 1.
        - The status is "crossing in range" only if a* and both CI ends lie in [2%, 98%]. Otherwise it is "not reached in range".
      - F1 spline (figure): accepted ~ fm + fm × ladopt + fm × RCS(ladopt) + X. RCS is Harrell's restricted cubic term with 3 knots at the 10/50/90th percentiles of ladopt among FM papers. Pointwise 95% band.
      - F2 profile, papers with an author ID: accepted ~ fm + fm × l + fm × no_acc + fm × l × no_acc + no_acc + no_acc × l + X.
      - F3 framing, FM papers only: accepted ~ framed + framed × l + X.
      - P0 (gated, descriptive):
        - By year 2019–2026: the `code_link` share among accepted minus rejected decided papers.
        - If the paper-weighted mean of the yearly differences over 2023–2026 exceeds 0.03, family C is labelled "possibly contaminated by camera-ready edits".
    - **Declared tests, Holm within each family.**
      - F-A:
        - A1: the slope b_fm×l, i.e. the FM premium per logit unit of prior adoption;
        - A2: the FM premium in the ≥ 50% bin (F1 bins).
      - F-B:
        - B1: the no_acc minus established FM premium at 10% adoption, b_fm×no_acc + b_fm×l×no_acc · (logit 0.10 − c);
        - B2: the difference in slopes, b_fm×l×no_acc.
      - F-C (secondary):
        - C1: the framing premium among FM papers at l = 0 (the FM papers' mean adoption);
        - C2: its slope, b_framed×l.
      - The bins, spline, profile bins and first-time bins are descriptive.
    - **Descriptive outputs.**
      - The linear premium at 2/10/25/50/75/90% adoption.
      - FM-premium bins by profile, from one pooled model with fm × bin × {established, no_acc} + no_acc + no_acc × l + X.
      - First-time bins: fm × bin × {first_time, returning} + first_time + first_time × l + X.
      - Framing bins among FM papers.
      - Counts by bin and profile.
    - **Sensitivities and robustness.** Every declared test is re-estimated in each variant where it is defined, with the same centre c, and Holm is reported within variant × family.
      - Years 2024–2026.
      - fm × year (families A and C): fm × year dummies centred at the FM papers' year mix (F1), and framed × year dummies centred at the framed FM papers' year mix (F3). The slopes A1 and C2 are then identified only within year, while A2 and C1 stay at the average year composition.
      - Era-specific curves, 2019–2026:
        - fm, fm × l and fm × bin are interacted with the era (2019–23 vs 2024–26), in one model with common cell FE and controls;
        - reported: A1 and A2 per era, the premium at c per era, the late minus early slope, and FM papers per bin and era.
      - Early-map adoption (`panel.frame('early').fm_adoption`, joined by row and `submission_id`) with early-map topic × year FE. CR1 by early topic, two-way with k100 topic.
      - fm × coarse-area dummies (A only). The dummies are centred at the FM papers' area mix and the first area is dropped, so the bins and the level stay at the average FM area composition.
      - Topics with ≥ 30 papers in t − 1.
      - The second-pass FM label: the second-pass label where it exists (2,174 papers), otherwise the first pass. fm and adoption are both rebuilt from it.
      - Logit (all six tests):
        - `logit.fe_logit` with topic × year dummies (flat cells dropped), CR1 by topic; log-odds plus AME.
        - B1 is the fm × no_acc coefficient with l centred at logit(0.10).
      - s9_accepted on the S9 population.
      - Without primary area "foundation or frontier models".
    - **Outcome-free part (`compute_free()`; also inside `compute`).**
      - FM share by adoption bin and year, all submissions 2019–2026.
      - Who brings FMs into low-adoption topics: LPM fm ~ first_time × bin + newcomer × bin + class + log2 team | topic × year, CR1 by topic, all submissions 2023–2026 with an author ID.
        - first_time is nested in newcomer. So the first_time terms compare first-time with returning topic newcomers, and the newcomer terms compare returning topic newcomers with incumbents.
      - Raw FM shares by profile × bin.
    - **Figures** (written into `output/posthoc/ph5_fmwave/`):
      - PH5_fmwave_premium: the spline with its 95% band, the five bin estimates with 95% CIs, the linear-in-logit line, and a* if it is in range;
      - PH5_fmwave_profiles: two panels, established and no acceptance;
      - PH5_fmwave_framing;
      - PH5_fmwave_fm_share: the outcome-free FM share by bin and year (bin × year cells with ≥ 30 papers), plus the entry coefficients.
    - **Calibration** (`calibrate(n_null, n_planted, seed)`), on simulated frames:
      - plants:
        - null;
        - fading: +0.35 log-odds × (1 − fm_adoption) for FM papers;
        - constant: +0.2 for FM papers;
        - calendar: +0.4 log-odds × (2026 − year)/3 for FM papers, unrelated to adoption, a confound check for A1.
      - per plant and test:
        - rejection at 0.05 (raw, Holm, two-way), the mean estimate, and bias and 95% CI coverage relative to a target;
        - the target is the same LPM fitted to the true simulated probabilities on the same sample;
        - families A and C are also run with the fm × year terms (tests suffixed "fm_x_year").
      - per family: the any-Holm-rejection rate.
      - for a*: the in-range share and coverage. A target outside [2%, 98%] counts as the open end on its side, the same rule as the draws.
      - Required: A1 detects the fading plant and rejects at about the nominal rate under the constant plant.
    - **Reading:** associations only.
      - The primary A1 compares adoption levels both across topics within a year and across years, because mean adoption rises from 2023 to 2026. A calendar trend in the FM premium would therefore load on it. If A1 and its fm × year version disagree, the slope is (partly) a calendar trend, not saturation.
      - Early adopters in low-adoption topics are self-selected (S2 hypothesis 6).
      - Author histories before 2021 are invisible, so 2023 established teams are partly classed as no_acc. This attenuates family B; the 2024–26 variant is the check.
      - A flat curve is consistent with legitimacy rather than novelty decay; it does not establish legitimacy.
      - F3 may reflect how deeply a paper engages with FMs, not framing alone.
  - **PH5 premia (selection S5): do topic acceptance advantages last?** (`posthoc.py ph5 premia`, module `ph5_premia.py`; declared 2026-10-17, before it was run; post hoc and exploratory. Every estimate is an association. Holm within each declared family ranks the evidence and makes nothing confirmatory.)
    - **Question.**
      - (a) How large is the noise-corrected spread (tau) of acceptance premia across topics within a year?
      - (b) How persistent is that spread across lags of 1–4 years?
      - (c) How much of an extreme past premium survives (winner's curse), and what shrinkage should authors apply to a past topic rate?
      - Secondary: (d) do submissions flow towards high-premium topics, and does inflow erode the premium? (e) When a topic's submissions surge unexpectedly, are incumbents accepted less often too (competition), or only newcomers (dilution)?
    - **Population:** the RQ3 filter (decided ordinary submissions), 2018–2026. For (e): the decided papers of 2019–2026 that have an author ID.
    - **Units.** Memberships are outcome-free and use the panel.frame("k100") row order.
      - **early:** the 100 early-map topics, fitted on 2017–2020 papers only. These are the primary, prospective units.
      - **k100:** the 100 k100 topics. These are fitted on all years and serve as the hindsight comparison.
      - **keywords:** the 68 PH4 keywords (posthoc.ph4_members). A paper can be in several keywords.
      - **areas:** the 20 coarse areas.
    - **Cell premium.**
      - For unit u and year t, g = the acceptance rate of u's papers minus that of all other papers of year t.
      - Its null variance is v = p_t(1 − p_t)(1/n_u + 1/n_rest), where p_t is year t's pooled acceptance rate.
        - The spec's per-cell shrunk rates were not used. They correlate with g, and in simulated null frames they inflated the DerSimonian–Laird (DL) tau² by 3–7 pp².
      - A cell is eligible with at least 15 decided papers. A year enters (a) and (b) only with at least 5 eligible units.
    - **(a) Spread.**
      - Each year: the DL moment estimate tau_t² = (Q_t − (m_t − 1))/C_t, not truncated.
      - Pooled: tau² = max(0, Σ m_t tau_t² / Σ m_t), with m_t = the eligible units in year t. Tau is reported in pp.
      - Checks: the same pooling over per-year estimates each truncated at 0, and per-year REML.
      - Signal share = tau²/(tau² + median v).
      - p(tau > 0) = (1 + #{tau_perm ≥ tau})/201, over 200 within-year permutations of acceptance. This is the test.
      - 95% CI: 999 unit bootstraps (percentile). The CI is approximate: it ignores the correlation of gap noise across overlapping keywords, and it can exclude 0 when p is not small.
      - Reliability rel(n) = tau²/(tau² + p(1 − p)/n), and n* = p(1 − p)/tau², the size at which rel = 0.5.
    - **(b) Persistence.**
      - For each year pair (t, t + h) with both years in (a), use the units eligible in both years.
      - Weights: w = 1/√((v_t + tau²)(v_{t+h} + tau²)).
      - Signal covariance: the weighted covariance divided by C = W − Σw²/W. Binomial noise is independent across years, so this needs no correction.
      - Signal variances: (Σw(x − x̄)² − Σw·v + Σw²·v/W)/C.
      - The covariance and variances are pooled over pairs, weighted by the number of overlapping units.
      - rho_h = cov/√(var_t · var_{t+h}) for h = 1–4. It is clipped to [−1, 1] and undefined unless both variances are positive. We report the share of bootstrap draws that are undefined or clipped.
      - p(rho_1 = 0): two-sided z of the pooled covariance, using its unit-bootstrap SD. This test was slightly liberal in development: 5–8% at 0.05.
      - CI: unit-bootstrap percentile.
      - **Window version:** one pair, W1 = 2018–2022 and W2 = 2024–2026.
        - Window premium: the paper-weighted mean of the unit's yearly gaps within the window, with variance Σ(n_t/n)² v_t.
        - Window units need at least 50 submissions (any status) and at least 15 decided papers in each window. That gives 82 early topics, 62 k100 topics, 41 keywords and 20 areas.
        - The units are therefore conditional on topics still active in 2024–26.
    - **(c) Winner's curse and shrinkage.**
      - Window premia are centred on their 1/v-weighted mean.
      - tau_W² = the DL estimate across window units. EB posterior = tau_W1²/(tau_W1² + v) × the centred W1 premium.
      - Units are ranked two ways: by the raw W1 premium and by the EB posterior.
      - Retention R = mean W2 / mean W1 premium, for the top and bottom decile (quintile for areas; at least one unit). For the EB ranking we also report mean W2 / mean EB.
      - Unit-bootstrap CIs, with the centring, tau_W1² and the selection redone in each draw.
      - Shrinkage b = the WLS slope of W2 on W1, weights 1/(v_W2 + tau_W2²), with an HC3 SE and t(m − 2). HC1 rejected 7–13% under the null in development; HC3 rejected 5–7%.
    - **(d) Flows** (secondary). The early map enters the family; k100 is reported as a check.
      - Unit-years t = 2019–2025 with an eligible cell.
      - Outcome: dshare = log share_{t+1} − log share_t, over all submissions, with counts + 0.5.
      - Model: dshare ~ EB premium_t per 10 pp + log growth t−1→t + log prior growth (t−2→t−1, as in topic_maturity) + log share_t | year FE.
        - The EB premium uses the pooled tau² and is shrunk to the year's random-effects mean.
        - The t−1→t growth is added to the spec's controls. Without it, a surge that lowers the premium and then reverts makes a spurious flow association: 37% rejections under a simulated surge plant, against 7% with the control.
        - The flow slope is undefined (p treated as 1 in Holm) when tau² = 0.
      - Erosion: g_{t+1} ~ g_t + inflow + g_t × inflow | year FE, for t = 2018–2025 with eligible cells in both t and t + 1.
        - g_t is centred within year (1/v weights).
        - inflow = dshare demeaned within year.
      - Both models weight unit-years equally, with CR1 SEs by unit and t(G − 1).
      - With the share series fixed, the flow-slope test rejected 6–8% at 0.05 in development, so its p is approximate.
    - **(e) Surge** (secondary; k100).
      - Outcome-free first stage on topic_year_maturity (k100, 2019–2026): log(papers + 0.5) ~ log(papers_{t−1} + 0.5) + log prior_growth | year FE, by OLS. The surge s = the residual divided by its SD.
      - LPM: accepted ~ s×incumbent + s×newcomer + newcomer + class + FM + log2 team | topic FE + year FE. CR1 SEs by topic, t(G − 1). Coefficients are in pp per SD of s.
      - Reading, at Holm-adjusted p < 0.05:
        - competition if beta_inc < 0;
        - dilution if beta_new < 0 and beta_inc is not significant;
        - proportional allocation if neither is significant;
        - otherwise "other".
      - Descriptive: s × maturity tercile, plus tercile dummies.
    - **Families (Holm):**
      - for each unit type, {tau > 0, rho_1, b}; the early map is primary;
      - {flow slope, erosion interaction}, early map;
      - {beta_inc, beta_new, beta_new − beta_inc}.
    - **Robustness.** (a)–(c) are re-estimated, with no family:
      - composition-adjusted premia: residuals of accepted ~ class + FM + log2 team | year FE. The gap is the mean residual inside the unit minus outside, with the year's residual variance. In development, a planted FM/theory composition effect produced raw tau 3–4 pp, which the adjustment brought down to 0.6–0.9 pp;
      - minimum cell 30;
      - the S9 population, using s9_accepted;
      - without 2021–2022;
      - ICLR primary areas, 2024–2026, spread only. That is 27 area strings, with renamed areas counted as separate units, and 62 area-year cells;
      - the mid_seed_refit map. Its difference from k100 (|k100 − seed_refit|) is the noise ceiling for |early − k100| on tau, rho_1 and b.
    - **Figures:**
      - a funnel of the premia against n per unit type, with the binomial-null band, the tau band and the 95th-percentile tau of the permutation null;
      - rho_h by lag, plus W1 → W2, for the four unit types;
      - a W1 vs W2 scatter (early map) with the b line, the retention bars and the reliability curves;
      - the surge coefficients, with the 3 × 3 reading grid and the observed cell highlighted.
    - **Validation before the run** (development calibration on simulated frames, final code: 100 null; 25 persistent; 25 transient; 20 AR(1); 20 surge).
      - **Null, raw rejection at 0.05 (tau / rho_1 / b):**

        | Unit type | tau | rho_1 | b |
        |---|---|---|---|
        | early | 4% | 8% | 7% |
        | k100 | 11% | 5% | 7% |
        | keywords | 6% | 6% | 4% |
        | areas | 3% | 5% | 5% |

        - The k100 tau figure was chance: a separate 400-frame check of the permutation test gave 2.5%.
      - **Null, any Holm rejection:** early 4%, k100 9%, keywords 4%, areas 6%, flows 4%, surge 5%. The surge reading was "proportional allocation" in 95% of null frames.
      - **Persistent early-map effect** (N(0, 0.25²) log-odds):
        - tau 5.62 pp vs a target of 5.67 pp, coverage 100%;
        - rho_1 0.95 vs 1.00;
        - b 0.448 vs 0.459;
        - R top (raw) 0.48 vs 0.47; R top (EB) 0.49 vs 0.48;
        - family power 100% for early and k100.
      - **Transient effect** (independent yearly premia, sd 0.25):
        - tau 5.67 vs 5.79;
        - rho_1 −0.02 vs 0.01;
        - b 0.003 vs −0.009;
        - in larger runs, rho_1 rejected 6–7% (260 frames) and b 4–7% with HC3 (300 frames).
      - **AR(1) effect with rho = 0.5:** rho_1 0.515 vs 0.497, power 80%.
      - **Surge penalty for newcomers** (−0.15 log-odds per SD):
        - beta_new −3.45 pp per SD vs −3.36, power 100%;
        - beta_inc rejected in 0% of frames;
        - the reading was "dilution" in 100% of frames;
        - the k100 flow slope rejected 0% (33% before the growth control was added).
    - **Reading:** these are associations. A real, persistent premium may reflect reviewer pools, how a topic's papers are judged, or who submits to it. It says nothing about the merit of a topic.
  - **PH5 kwtiming (selection S1): when should authors enter a trend keyword?** (`posthoc.py ph5 kwtiming`, module `ph5_kwtiming.py`. Declared 2026-10-17, before it was run. Post hoc and exploratory: every estimate is an association within the stated fixed effects.)
    - **Question.** Take papers that list a trend author keyword and compare them with papers in the same k100 topic and year. Four sub-questions:
      - How does P(accept) vary with the keyword's prospective lifecycle state, defined as age since onset × within-year momentum?
      - For a keyword that is globally old, is a paper accepted more often when the keyword has only just reached the paper's own coarse area?
      - Do these timing patterns differ between teams with no earlier ICLR acceptance and established teams?
      - How much does the early-entry premium vary across keywords?
    - **Keyword frame (outcome-free; every discovery submission, any outcome).**
      - V: the author keywords typed `research_area` or `specific_topic` (`buzzwords.TYPES`), 759 keywords.
      - One row per (paper, distinct keyword in V), 65,702 uses.
      - **Onset o_k:** the first year (data start 2017) in which the cumulative number of papers listing k reaches 10. A keyword is eligible in year t iff t ≥ o_k + 1; the code asserts this equals `keyword_year.eligible`.
      - **Age bins:** a = t − o_k gives young (1–2), middle (3–4) and old (≥ 5). The 28 keywords with o_k ≤ 2018 are left-censored and coded old in every year. As a result, 2019 holds only old states, the middle bin first occurs in 2022, and uncensored old keywords appear only from 2024.
      - **Momentum:** `keyword_year.growth` (share t−1 / share t−2, +0.5), cut into terciles within each year among the eligible keywords. The cut uses the percentile rank pr = (average rank − 0.5)/n: falling if pr < 1/3, flat if pr < 2/3, rising otherwise. Tied growth values share a tercile.
      - **States:** the 9 cells of age × momentum. Emerging = young × rising; Mainstream (reference) = old × flat; Cooling = old × falling; Fizzling = young × falling; Resurgent = old × rising.
      - **Eligible uses 2019–2026, any outcome:** 53,458 uses on 29,816 papers.

        | age | falling | flat | rising |
        |---|---|---|---|
        | young | 2,154 | 3,419 | 12,276 |
        | middle | 2,285 | 4,004 | 8,116 |
        | old | 5,499 | 12,541 | 3,164 |

        The spec's checked counts differ because that check gave censored keywords their measured age (verified).
      - **Stacked rows:** one row per (paper, eligible keyword), with weight w = 1/(the paper's number of eligible rows in the model sample), so each paper weighs 1. Papers with no eligible keyword are left out of Models A and B. Their level is reported descriptively: the raw rate, and an LPM difference within topic × year with CR1 SE by topic.
      - **Local arrival (Model C):**
        - Keywords: the 129 keywords of V with ≥ 100 listing papers in 2017–2026. This set is chosen with hindsight; under keyword × year FE it only selects the sample.
        - Area: the coarse topic (20 areas, `topic_assignments.coarse`). k100 topics nest in coarse areas.
        - A_{k,area}: the first year in which the cumulative number of k's users inside the area reaches 3.
        - locally_early = 1 if t ≤ A + 1, or if the area never reaches 3 users by 2026; otherwise 0 (t ≥ A + 2). Equivalently, locally_early = 1 iff the area had fewer than 3 users of k up to t − 2. The flag is therefore prospective; a test checks this.
        - Rows are limited to "globally late" uses: global age bin middle or old, censored keywords included.
        - Any-outcome counts, 2019–2026: 28,777 rows, 5,278 of them locally early, in 471 keyword-year cells that hold both kinds.
      - **Profiles.**
        - first_time: no author ID has an earlier discovery submission (any topic, any outcome). Outcome-free.
        - established: `posthoc.established_authors(k)`, i.e. an author had an accepted ICLR paper in an earlier year. Gated.
        - no_acc = 1 − established, among papers with an author ID.
        - profile3: first-time / returning but never accepted / established.
        - Profile models use 2019–20 and 2023–26. Adding 2022 is a robustness check; 2021 is never used.
      - **Keyword incumbent (row level, outcome-free):** some author ID of the paper listed the keyword in an earlier year. This is `posthoc.keyword_incumbent`, vectorised; equality is tested.
    - **Outcome-free part (`compute_free`):**
      - share of eligible uses per state, by year (raw and paper-weighted);
      - for each of the 9 state indicators, an LPM on first_time (2019–20 and 2023–26, papers with an author ID). It uses k100 topic × year FE, weights w and two-way SE (keyword, topic). BH q across the 9 states is descriptive;
      - diffusion lags A_{k,area} − o_k for the 129 keywords, with the median lag per area (all keywords, and those with an uncensored onset).
    - **Gated models.**
      - **Population:** RQ3 decided papers, 2019–2026. Outcome: accepted.
      - **Estimator:** LPM, WLS with weights w and k100 topic × year FE absorbed. It is posthoc.wls_fe extended to return the full covariance matrix: same singleton dropping, `posthoc.twfe` and CR1 factor.
      - **Controls X:** class dummies (ref. method), fm, log2 team (capped at 16), newcomer, and log(1 + the number of V keywords listed).
      - **SE:** two-way clustered by keyword and k100 topic (Cameron–Gelbach–Miller V_kw + V_topic − V_kw∩topic, each with a CR1 factor). Eigenvalues of the sum are clipped at 0. The t reference has min(G) − 1 df.
      - **A (state surface):**
        - Model: accepted ~ 8 state dummies (ref. Mainstream) + X | topic × year.
        - Reported: each state's effect, and adjusted P(state) = effect + the weighted raw Mainstream rate of the model's rows.
        - Omnibus "timing does not matter" test: a Wald F on the 8 dummies. Its p is calibrated: p = (1 + #{F_null ≥ F})/201, where F_null comes from 200 null frames. Each null frame draws the decided set and acceptance from `ph5_common.fake_outcomes(k, seed)`, seeds 0–199; profiles stay as in the run. The nominal F(8, G − 1) p is shown as well.
      - **B (who):**
        - Model: Model A + state × no_acc + no_acc, years 2019–20 and 2023–26.
        - Descriptive EB table of adjusted P(accept | state, profile3): 26 cell dummies (ref. Mainstream × established) + X. Adjusted rate = coefficient + the reference cell's weighted raw rate.
        - Each cell is shrunk towards its state's mean of the 3 profile cells by τ²/(τ² + SE²). τ² comes from the method of moments: max(0, [Σ(m − m̄_s)² − Σ((J_s − 1)/J_s)·SE²] / Σ(J_s − 1)), with cells treated as independent. The reference cell has SE 0 and is not shrunk. n per cell is shown.
      - **C (globally late, locally early):**
        - Model: accepted ~ locally_early + X | keyword × year FE + topic × year FE (alternating projections). Weight = 1/(the paper's number of Model C rows). Two-way SE by keyword and topic.
        - Descriptive 2 × 2 grid of global age (3–4 vs ≥ 5, censored included) × local stage. It gives raw weighted rates, and the locally-early effect within each age group from one model with locally_early × age-bin terms. The age main effect is not identified under keyword × year FE.
        - Descriptive importer split: domain insider (k100 topic incumbent) × keyword incumbent, giving 4 groups. One model holds locally_early × group terms and group main effects, with X minus newcomer (newcomer = 1 − domain insider). It reports each group's effect with MDE80, and the domain-insider-only minus keyword-incumbent-only contrast.
      - **D (dispersion; descriptive):**
        - r = accepted − the leave-one-out mean of the paper's topic × year cell (decided papers 2019–2026; singleton cells dropped).
        - For each keyword with ≥ 30 decided young-stage uses: premium = mean r, with sampling variance s²/n_k. Here s² is the pooled within-keyword variance of r. A keyword's own variance is not used: for a binary outcome it moves with the mean and biases μ and τ.
        - Reported: the DerSimonian–Laird τ, μ, Q and I²; EB posterior means and SDs (μ treated as known); and the share of keywords with a positive posterior mean. When τ = 0 this share is degenerate (0 or 1).
        - τ null: 50 within-cell permutations of acceptance (seed 20261017), giving the null mean, the 95th percentile and a permutation p (ties counted, so τ = 0 gives p = 1).
        - Survivorship gap (hindsight): the mean premium of keywords with ≥ 100 papers, compared with all keywords and with the rest.
      - **Risk view:** Model A on the S9 population, with s9_accepted and with withdrawn_after_review. Nominal p, no adjustment.
    - **Declared tests and multiple testing.**

      | Family | Correction | Test | Contrast |
      |---|---|---|---|
      | A | Holm over 3 | A1 | Emerging − Mainstream |
      | A | Holm over 3 | A2 | Cooling − Mainstream |
      | A | Holm over 3 | A3 | (1/3) Σ over the three momentum terciles of (young − old) |
      | B | Holm over 2 | D_E | coefficient of Emerging × no_acc = (Emerging − Mainstream \| no_acc) − (same \| established) |
      | B | Holm over 2 | D_C | the same for Cooling |
      | C | single test | C1 | β(locally_early) |

      - Each test is reported with its analytic MDE80, (t.975 + t.80) × SE.
      - It is also reported with a simulated MDE80, (t.975 + t.80) × the SD of the estimate over the 200 null frames, and with its rejection rate at 0.05 in those frames (`size_in_null_frames`).
      - It also gets a size check that is not counted: p_null_frames = (1 + #{|t_null| ≥ |t|})/201.
      - **Reading rule:** a declared test is called supported only if p_holm < 0.05 **and** p_null_frames < 0.05. In development D_E rejected 6–7% of null frames at a nominal 5%.
      - The omnibus is calibrated as above.
      - The profile cells, Model D, the importer split and the risk view are descriptive.
    - **Robustness (reported, not counted; nominal p).** A1–A3 under each of the following:
      - censored keywords dropped (weights recomputed);
      - 2-year momentum (share t−1 / share t−3, +0.5, terciles as above; 2020–2026, since 2016 does not exist);
      - 2022–2026 only;
      - early-map topic × year FE with clusters (keyword, early-map topic);
      - unweighted rows;
      - a weighted FE logit (Newton with topic × year intercepts; cells with a constant outcome dropped; partialled-score two-way sandwich; log-odds);
      - papers without a probable earlier version.

      Further checks:
      - keyword FE + topic × year FE with momentum terciles only (rising − flat, falling − flat). Age is not identified with keyword FE;
      - Model B with 2022 added (D_E, D_C);
      - Model C with arrival threshold 5;
      - Model C with censored keywords dropped;
      - Model C with ICLR primary areas: rows from 2025–2026 only, using the author-chosen area. Arrival is counted over all years, and papers before 2025 get the modal 2025–26 primary area of their fine topic. The 2024 taxonomy differs, and primary areas do not exist before 2024.
    - **Calibration before the real run.** `calibrate(n_null, n_planted, seed)` works on `ph5_common.simulated_frame`:
      - null frames;
      - the 'timing' plant: +0.3 log-odds if all of a paper's eligible keywords are Emerging, −0.3 if all are Cooling;
      - the 'local' plant: +0.3 log-odds for papers with a locally-early Model C row.

      Reported:
      - per-test rejection (raw and Holm), and any-Holm family rejection;
      - bias and 95% CI coverage against the target, which is the same estimator applied to the true probabilities on the same rows;
      - omnibus size, nominal and leave-one-out calibrated, and its power.

      The lead runs the full calibration with 200 null frames.
    - **Outputs:** `output/posthoc/ph5_kwtiming/{tests, state_effects, profile_cells, local_early, keyword_premia, robustness, reference_null, free_state_shares, free_profile_states, free_diffusion_lags, free_area_lags}.csv` and `summary.json`.
    - **Figures:**
      - (i) `PH5_kwtiming_states`: a 3 × 3 heatmap (age × momentum) of pp vs Mainstream, with 95% CI and n (uses), and the omnibus F and calibrated p in the title;
      - (ii) `PH5_kwtiming_profiles`: the same as two panels, no earlier acceptance vs established;
      - (iii) `PH5_kwtiming_local`: Model C and its splits and robustness as a forest plot, plus the 2 × 2 grid of raw rates;
      - (iv) `PH5_kwtiming_premia`: a caterpillar plot of raw and EB keyword premia, with the μ ± 1.96τ band;
      - (v) `PH5_kwtiming_free`: named-state shares by year, and first-time minus returning differences in state shares.
    - **Reading:** these are associations. A Cooling penalty, for example, may reflect reviewer saturation, weaker late entrants, or both. Nulls are read through their MDEs.
  - **PH5 pivot (selection S3): how far to jump. Acceptance as a curve of distance from the authors' own earlier work, by destination heat, and within the same author** (`posthoc.py ph5 pivot`; module `ph5_pivot.py`; declared 2026-10-17, before it was run. It was built and calibrated only on `ph5_common.simulated_frame`. Post hoc and exploratory: every estimate is an association.)
    - **Question.** For papers with at least one author who has earlier ICLR submissions, how does acceptance vary with the semantic distance between the paper and the authors' own earlier work, within topic × year?
      - Is the curve monotone (a pivot penalty) or an inverted U?
      - Is the far-jump penalty different in hot topics?
      - Is the same author accepted less often far from their own earlier work?
    - **Distance features** (outcome-free; every discovery submission, any outcome).
      - x_p is the SPECTER2 vector (title [SEP] abstract), centred with `output/specter2_centring_mean.npy` and L2-normalised.
      - **History.**
        - A paper in 2023–2026 uses an author's submissions from 2021 on (profile IDs; the few email-ID keys of 2021–24 match their own rows).
        - A paper in 2019–2020 uses them from 2017 on (email IDs).
        - Papers from 2021–2022 serve as history only.
      - **P_a**, the prior set of author a for paper p in year t: a's submissions in [first history year, t − 1], minus p's probable earlier version (`earlier_versions.csv.gz`), and minus every paper with cos(x_p, x_q) ≥ 0.90.
      - An author is "experienced" if P_a is still non-empty after those exclusions.
      - **prior_cos** = x_p · c_a, where c_a is the normalised mean of P_a. Higher means closer to the author's earlier work.
      - **F_max** (primary) = the maximum prior_cos over the experienced authors.
      - **n_exp** = the number of experienced authors.
      - **Variants:**
        - F_first / F_last: the first / last author's prior_cos, if that author is experienced. Positions are among keyed authors; keys are complete from 2021.
        - F_team: cos to the normalised mean of the union of the P_a.
        - F_nn: the maximum cos to any paper in that union.
        - n_prior_team: the size of that union.
        - F_max3: F_max over authors with |P_a| ≥ 3.
    - **Frozen reference points.** These are outcome-free, taken from all 2023–2026 submissions that have the distance (any outcome), and rounded to 4 decimals. `reference_points()` recomputes them; the test asserts that they are equal.
      - F_max:
        - knots (5/35/65/95th pct): −0.0476, 0.2629, 0.4613, 0.7117
        - p10 / p50 / p90: 0.0339 / 0.366 / 0.6508
        - quintile edges: 0.1431, 0.298, 0.4293, 0.5661
      - F_first: knots −0.0998, 0.2056, 0.4394, 0.7284; p10 / p50 / p90 −0.0302 / 0.3247 / 0.6597.
      - F_last: knots −0.1335, 0.1543, 0.3624, 0.6507; p10 / p50 / p90 −0.061 / 0.2576 / 0.5791.
      - F_team: knots −0.1196, 0.178, 0.3813, 0.6497; p10 / p50 / p90 −0.0423 / 0.2792 / 0.5836.
      - F_nn: knots 0.0273, 0.3297, 0.5027, 0.7192; p10 / p50 / p90 0.1139 / 0.4191 / 0.6632.
      - F_max3: knots −0.0829, 0.2345, 0.4307, 0.677; p10 / p50 / p90 0.0023 / 0.3368 / 0.619.
      - prior_cos quintile edges (author rows): 0.0351, 0.1872, 0.3303, 0.4883.
    - **Population.** RQ3 decided papers 2023–2026 with n_exp ≥ 1. Replication: 2019–2020. 2021–2022 are excluded.
    - **P1 (paper level, linear probability model).**
      - Model: accepted ~ RCS(F_max) + RCS(F_max) × (hot − the sample's hot share) + class + FM + log2 team + n_exp dummies + log(1 + n_prior_team) + has_earlier_version | k100 topic × year FE.
        - The n_exp dummies are for 2, 3 and 4+; the reference is 1.
        - RCS is Harrell's restricted cubic spline: F plus two nonlinear terms, linear beyond the outer knots.
        - hot is absorbed by the FE. Centring it makes the main spline the hot-share-weighted, population-average curve.
      - SE: CR1 by topic, t(G − 1).
      - **Adjusted curves** for all papers, hot topics and other topics:
        - each curve is the group's mean acceptance + Σ_j b_j (B_j(f) − the group's mean B_j), with controls at their means;
        - 61 points over [p5, p95], the knot range;
        - pointwise 95% CIs from the lincom of the centred spline part (the level's uncertainty is not included, so the band pinches near the group mean);
        - the vertical gap between the hot and non-hot curves comes from raw group means, because hot is absorbed by the FE.
      - **Arg-max** of each curve over that grid, with a 999-draw topic cluster bootstrap. Reported: the percentile CI, the shares of draws at either edge, and the share of the group at or below the arg-max.
      - **Display:** F_max quintile dummies (no hot interaction), centred at the quintile shares.
    - **P2 (within author).**
      - One row per (paper, experienced author), weight 1 / n_exp.
      - Model: accepted ~ prior_cos + log1p(|P_a|) + class + FM + log2 team | author FE + topic × year FE (`posthoc.wls_fe`; singletons dropped iteratively).
      - SE: CR1 by topic, t(G − 1).
        - The small-sample factor also counts the absorbed author FE, since they are not nested in topics: SE × √((n − k)/(n − k − (A − 1))), where A is the number of authors in the sample.
        - The two-way (topic, author) SE for the slope is reported as a check.
      - Descriptive: prior_cos quintile dummies (reference Q3) in place of prior_cos.
    - **Declared tests (Holm over four):**
      - E1, far jump: the P1 population curve at the F_max p10 minus at p50;
      - E2, near: p90 minus p50. Negative E2 means close follow-ups do worse (an inverted U);
      - E3: E1 in hot topics minus E1 in other topics (the spline × hot terms);
      - E4: the P2 slope per +0.1 cos. The CR1 p enters Holm.
    - **Secondary (BH over seven; descriptive).** E1 within each of these groups:
      - papers with / without an established author (an author ID with an earlier ICLR acceptance; `posthoc.established_authors`);
      - method / theory / measurement papers (measurement = dataset_benchmark + evaluation).
      - Both sets come from one pooled model each, with group-specific regressors and group × topic × year FE; the point estimates equal separate fits.
      - E1 with the first-author distance and with the last-author distance, each with its own frozen reference points.
      - The no-acceptance minus established E1 is reported alongside, outside the family.
    - **Robustness.** E1–E4 are re-estimated where defined, with Holm within each variant; nothing is counted.
      - Topic-newcomer control. P1: the paper's newcomer flag. P2: the author is new to the topic (`posthoc.author_rows`).
      - Team-experience control, P2 only (E4): the P1 team controls are added (n_exp dummies, log(1 + n_prior_team), has_earlier_version).
        - Within author and topic × year, and given log2 team, prior_cos and n_exp correlate 0.12.
        - In simulation, a planted n_exp effect moved E4 and this variant removed it.
      - F_last, F_team or F_nn in place of F_max (P1 only, E1–E3).
      - Authors with ≥ 3 prior papers. P1 uses F_max3 with its own knots and keeps the paper's n_exp dummies. P2 uses rows with |P_a| ≥ 3.
      - Within team-size bands 2–4, 5–7 and 8+ (solo papers left out).
      - Without papers that have a probable earlier version.
      - Logit: P1 with topic × year dummies (`logit.fe_logit`, flat cells dropped).
        - E1–E3 are in log-odds, through a reparametrised spline basis whose first coefficient is the contrast.
        - E4 is not estimated, because author dummies are infeasible.
      - s9_accepted on the S9 population.
      - The 2019–2020 replication, with the same frozen reference points.
      - Early-map topic × year FE with early-map hot (CR1 by early topic).
    - **Outcome-free part** (`compute_free`, also inside `compute`; all 2023–2026 submissions with n_exp ≥ 1, any outcome):
      - F_max and F_last ~ hot | year FE + coarse-area FE, without and with controls (n_exp dummies, log2 team, log(1 + n_prior_team), class, FM), CR1 by topic;
      - F_max by hot × year, n_exp, class, topic newcomer and team band;
      - histograms;
      - correlations among the distance variants;
      - the reference points recomputed against the frozen values.
    - **Figures:**
      - `PH5_pivot_curve`: adjusted P(accept) vs F_max with 95% bands, hot vs non-hot overlaid, quintile dots, and the F_max histogram underneath;
      - `PH5_pivot_within_author`: within-author prior_cos quintile effects with E4;
      - `PH5_pivot_heat`: outcome-free F_max by destination heat.
    - **Calibration before the run** (`calibrate`; the full 200-frame run is left to the lead).
      - **Plants:**
        - 'far': −0.5 log-odds for F_max below the frozen 20th percentile (0.1431);
        - 'within': +1 log-odds per unit of the paper's mean prior_cos.
      - **Reported:**
        - size, Holm and two-way (E4) rejection for each test;
        - bias and coverage of the pseudo-true target (the same model fitted to the true probabilities on the same sample);
        - the SD of the errors (estimate − target) against the mean SE;
        - the secondary family's null rejection and any-BH rate.
      - The arg-max is not calibrated: under the step plant it is not well defined.
    - **Reading.**
      - These are associations within topic × year (and within author for E4). Patterns could reflect:
        - lost topic know-how;
        - relatedness, where incremental follow-ups do worse;
        - disguised resubmissions, which the exclusions only partly remove;
        - writing style picked up by the embedding.
      - E4 compares one author's papers with different co-authors. So it can also reflect co-author composition: their experience (see the team-experience variant) and their unobserved quality. A between-author quality confounder that runs through co-authors moved the E4 target in simulation.
      - None of these is a tested cause.
  - **PH5 position (selection S4): where to stand inside a topic.** Two dimensions: novelty relative to earlier ICLR work, and concurrent near-duplicates ("twins"). We ask for whom and where these matter, within the same author, and whether twins share fate.
    - Code: `ph5_position.py`, run once by `posthoc.py ph5 position`. Declared 2026-10-17, before the run. Exploratory and post hoc: every estimate is an association within topic × year. Holm within each family only ranks the evidence.
    - **Features** (outcome-free, all 43,480 discovery submissions; SPECTER2 centred by `output/specter2_centring_mean.npy` and L2-normalised):
      - **Novelty.** nov = 1 − the mean of the 10 largest cosines with all papers of earlier years, excluding the paper's own chain of probable earlier versions (`earlier_versions.csv.gz`; 170 papers have one).
      - **Novelty percentile.** nov_pct = (rank − 0.5) / n within the k100 topic × year cell, over all submissions. Quintiles Q1 (least novel) to Q5 are cut at 0.2, 0.4, 0.6 and 0.8; terciles at 1/3 and 2/3.
      - **Twins.** Same-year pairs with cos ≥ 0.70.
        - Independent: the two papers share no declared_id_key and no normalised author name (lower case, whitespace collapsed), and neither is in the other's earlier-version chain. Sibling: they share an author.
        - any_twin = at least one independent twin; sibling_twin = at least one sibling twin.
        - Dose = log1p(independent twins per 1,000 same-year submissions).
      - **Precedents.** Earlier papers with cos ≥ 0.70. Prior density = log1p(1,000 × precedents / earlier papers).
      - **first_time.** No author ID with an earlier submission; used in the outcome-free part only.
      - **Reading check** (titles of 20 random independent pairs per bin, read before declaring):
        - [0.60, 0.70): the same sub-area.
        - [0.70, 0.80): the same narrow problem.
        - ≥ 0.80: the same narrow problem with near-identical framing.
        - So a twin is a concurrent competitor on the same narrow problem. It is rarely the identical idea.
    - **Population:** RQ3 decided papers 2019–2026. The author-FE model (Q5) uses their 2023–2026 papers.
    - **Models.** LPM with k100 topic × year FE absorbed; CR1 SE by topic, t(G − 1). Controls X: class (ref. method), FM, log2 team size, newcomer, sibling_twin.
      - Q0: accepted ~ q1 + q2 + q4 + q5 (ref. Q3) + any_twin + X.
      - Q1: Q0 + tercile main effects (low, high) + any_twin × mid + any_twin × high. The interaction reference is low, so P3 is a single coefficient; this is the same model as using mid as the reference.
      - Q2: Q0 + any_twin × hot.
      - Q3: Q0 + quintile × newcomer.
      - Q4: Q0 + quintile × maturity tercile (the `posthoc.add_columns` tercile of the population; ref. young).
      - Q5 (within author):
        - one row per (paper, author ID), weight 1 / the paper's number of author IDs;
        - accepted ~ nov_pct × 10 (per 10 percentile points) + any_twin + X;
        - author FE and topic × year FE absorbed jointly (`posthoc.twfe`, singletons dropped; the same estimate as `posthoc.wls_fe`);
        - CR1 SE by topic and two-way topic × author SE. Both count the absorbed author FE in the small-sample factor, (n − 1)/(n − k − (authors − 1)), because authors are not nested in topics. Without that factor the null t had SD 1.14.
    - **Family 1 (Holm over 8):**
      - P1a: Q5 − Q3 (Q0).
      - P1b: Q1 − Q3 (Q0).
      - P2: any_twin (Q0).
      - P3: twin association in the high minus the low novelty tercile (Q1).
      - P4: twin association in hot minus other topics (Q2).
      - P5: (Q5 − Q3) for newcomer minus incumbent papers (Q3).
      - P6: (Q5 − Q3) in mature minus young topics (Q4).
      - P7: the within-author novelty slope (Q5).
      - **Calibrated p for P3–P7.** Each gets a p-value from 200 simulated nulls on the same papers: accepted ~ Bernoulli(the paper's topic × year acceptance rate), p = (1 + #{|t_null| ≥ |t|}) / 201.
      - **p used in Holm:** the largest of the test's CR1 p, its calibrated p (P3–P7) and, for P7, its two-way p.
    - **Secondary (no Holm):**
      - **Lind–Mehlum inverted-U test.** A quadratic in nov_pct plus any_twin and X, within topic × year. Slopes are evaluated at the observed minimum and maximum, and p is the larger of the two one-sided p-values. We also report the turning point with a delta-method SE.
      - **Adjusted P(accept | tercile, any_twin, hot).** Each group's difference from (mid tercile, no twin) of the same hot stratum, plus that reference group's raw rate. Hot is constant within topic × year, so levels are not compared across strata. BH over the 10 groups.
      - **Surface.** Novelty quintile × any_twin against (Q3, no twin); BH over the 9 cells.
      - **Risk view.** Q0 on the S9 population, once with s9_accepted and once with withdrawn_after_review; BH over the 10 cells. A cell is "polarising" if both coefficients are > 0 with q < 0.05.
      - **Novelty curves** for newcomer vs incumbent papers (Q3) and by maturity tercile (Q4).
    - **Family 3, shared fate (Holm over the 3 bins, cell variant):**
      - **Pairs:** independent same-year pairs of decided papers, 2018–2026, with cos in [0.60, 0.70), [0.70, 0.80) and ≥ 0.80.
      - **Residual:** r = accepted − the leave-one-out mean of the paper's topic × year cell. Papers in single-paper cells are dropped.
      - **Statistic:**
        - rho_b = mean r_i r_j / var(r) over the pairs in bin b;
        - rho_0 = the same quantity on 100,000 random same-cell pairs with cos < 0.30 and no shared author (fixed seed);
        - the statistic is rho_b − rho_0.
      - **Inference:** two-sided p (deviation from the permutation mean) from 1,000 within-cell permutations of accepted, recomputing r each time. The LOO residual makes same-cell pairs negatively correlated by construction, so the statistic is not 0 under the null. We therefore also report stat_excess = statistic − permutation mean.
      - **Also reported:** P(both accepted) and P(exactly one accepted), against their expectation under independence given the cell rates, with permutation bands and p-values.
      - **Variant (total shared fate, topic level included; no Holm):** year means, rho_0 on 100,000 random same-year pairs (cos < 0.30, no shared author), and within-year permutations.
    - **Robustness.** Family 1 is re-estimated under each variant, with Holm within the variant on the CR1 p-values (P7: the larger of CR1 and two-way; no calibrated p):
      - twin threshold τ = 0.65 and 0.75;
      - K = 5 and 20;
      - novelty against the prior 3 years only;
      - fixed-reference novelty: 5,000 random earlier papers, mean over 5 draws. In 2018–2021 there are fewer earlier papers, so this equals the main measure there;
      - class × year percentile;
      - prior-density control;
      - early map: early-topic × year FE and clusters, early-map hot, maturity tercile and newcomer, and the percentile within the early cell;
      - without papers that have an earlier version;
      - logit with topic × year dummies (P1a–P6, log-odds; flat cells dropped);
      - twin dose in place of any_twin (P2 only).
    - **Outcome-free part** (`compute_free`, also inside compute):
      - any_twin share by year, by hot / FM / class / newcomer.
      - **Herding LPM:** any_twin ~ first_time + newcomer + class + FM + log2 team, within topic × year. Submissions 2019–2026 with an author ID; CR1 by topic. first_time is nested in newcomer.
      - Descriptive checks.
    - **Figures:**
      - heatmap of adjusted pp by novelty quintile × any_twin;
      - novelty curves (newcomer vs incumbent; by maturity);
      - rho_b − rho_0 by bin with permutation bands, for both variants;
      - the outcome-free twin share by year, hot vs other.
    - **Validation before the run** (simulated outcomes only):
      - unit tests of features, estimators, tables and the dyadic permutation test against direct computation and planted data;
      - an end-to-end run on `simulated_frame`;
      - development calibration: 40 + 20 null frames and planted frames (inverted U, twin penalty in hot topics, a shared shock redrawn per frame);
      - review checks: an author-confounding plant, a cell-heterogeneity plant and a competition plant;
      - the full 200-frame calibration is left to the lead.
    - **Reading:** these are associations.
      - Twins mark crowded narrow problems, and novelty is measured relative to the topic-year cell. Neither tests what reviewers believe, and neither is a causal effect of positioning.
      - "Within author" does not hold co-authors fixed.
      - Shared fate in Family 3 includes shared observable characteristics of the two papers.
  - **PH5 teams (selection S7): who to bring when entering a topic. How many topic insiders, a proven outsider or an unproven insider, and in which author role, by topic heat.**
    - **Logistics.** Run with `posthoc.py ph5 teams`; the module is `ph5_teams.py`. Declared 2026-10-17, before it is run. It is post hoc and exploratory, and every result is an association. It was developed, tested and calibrated only on `ph5_common.simulated_frame`.
    - **Population.**
      - RQ3 filter (decided ordinary submissions), 2023–2026, with at least one author ID. These years come after the 2021–22 switch of author-ID systems.
      - Replication: 2019–2020.
      - 2021–2022 are excluded.
      - The code also requires a hot flag. Every paper of 2019–2026 has one, so this removes no paper.
    - **Author types.** These are outcome-free. There is one per paper × author ID. History is every discovery submission by the same ID in an earlier year, with any outcome, as in `posthoc.author_rows`.
      - novice: no earlier submission;
      - crossover: earlier submissions, none in the paper's k100 topic;
      - insider: at least one earlier submission in the paper's k100 topic.
      - For the main population, histories start in 2021, so they span 2 years for 2023 papers and 5 years for 2026 papers. For the replication they start in 2017.
    - **Paper features.**
      - n_ins (0, 1, 2, 3+).
      - n_exp = n_cross + n_ins (0, 1, 2, 3, 4+).
      - team = distinct author IDs, as dummies 1–7 and 8+. This is identical to the frame's `team_size`.
      - First and last author: the author IDs with the minimum and maximum `source_list_position`, and their types.
      - mid_ins: insiders in neither the first nor the last position.
      - prior: the sum of the authors' earlier submissions.
      - familiar = n_ins ≥ 1. This is identical to the frame's `incumbent`.
      - proven = `posthoc.established_authors`: an author ID had an accepted ICLR paper in an earlier year, in any topic. It uses earlier outcomes and is computed only inside the gated run.
      - alphabetical: at least 3 listed authors whose surnames are in non-decreasing order. The surname is the last token of `declared_name_json`, ASCII-folded, with Jr, Sr and II–IV dropped.
    - **Models (gated).** Linear probability models with k100 topic × year fixed effects, CR1 SE by topic, and p-values from t(G − 1).
      - Shorthand used below:
        - C (controls): contribution class (reference: method), FM, has_earlier_version and log(1 + prior);
        - B: class + FM + has_earlier_version;
        - TS: team-size dummies (reference: 1; reference 2 in T3);
        - EXP: n_exp dummies (reference: 0).
      - T1: accepted ~ 1[n_ins = 1] + 1[n_ins ≥ 2] + TS + EXP + C.
      - T1h: T1 plus each insider dummy × hot. Hot itself is absorbed by the fixed effects.
      - T2: accepted ~ proven outsider + unproven insider + proven insider + TS + EXP + C. The reference cell is "neither".
      - T2h: T2 plus each of the three cells × hot.
      - T3 (papers with at least 2 author IDs): accepted ~ 1[first author insider, last not] + 1[last author insider, first not] + 1[both] + mid_ins + n_ins dummies (1, 2, 3+) + TS + EXP + C.
      - A regressor without variation within topic-years, or collinear with earlier regressors in a subsample, is dropped and reported as NaN.
    - **Family (Holm over 6).**
      - H1: one insider vs none, the n_ins = 1 coefficient (T1).
      - H2: concavity, (1 vs 0) − (2+ vs 1) = 2·b1 − b2+ (T1).
      - H3: (1 vs 0) in hot minus other topics, the 1[n_ins = 1] × hot coefficient (T1h).
      - H4: proven outsider − unproven insider (T2).
      - H5: H4 in hot minus other topics, po×hot − ui×hot (T2h).
      - H6: last-author insider − first-author insider, last only − first only (T3).
      - Each test is reported with:
        - estimate, CR1 SE, p, Holm p and 95% CI;
        - MDE80 = (z.975 + z.80) × the SD of the estimate over 200 within-topic-year permutations of acceptance (seed 20261017); also at Holm's first-step α = 0.05/6, and as 2.80 × the CR1 SE;
        - the permutation p, as a check only.
    - **Also reported, outside the family.** Every focal coefficient of T1–T3 and these derived contrasts:
      - 2+ vs 1 insiders;
      - 1 vs 0 and 2+ vs 0 insiders, each in hot and in other topics;
      - PO − UI in hot and in other topics;
      - proven insider − unproven insider, and proven insider − proven outsider;
      - both insiders − first only, and both − last only.
    - **Descriptive estimates, separately for hot and other topics.**
      - Method: an LPM with group dummies (reference: the largest group), topic × year fixed effects and CR1 by topic. Adjusted P(g) = the heat level's mean acceptance + b_g − Σ_h w_h·b_h, where w are the group shares. Its SE comes from the CR1 covariance of that contrast, with the heat level's mean taken as fixed.
      - Groups and controls:
        - team size (2–7, 8+) × n_ins (0, 1, 2, 3+), teams of 2 or more, controls B;
        - first × last author type (3 × 3), teams of 2 or more, controls TS + B, with n;
        - proven × familiar (4 cells), controls TS + EXP + C, as in T2.
      - The curves and the role grid leave out log(1 + prior). It rises mechanically with team size and with insiders, and would absorb part of the gradients these figures describe.
      - Additive decomposition over all papers: accepted ~ n_nov + n_cross + n_ins (each capped at 4) + B | topic × year, with the insider − crossover and crossover − novice contrasts. It is shown next to PH2's gradient on the same papers and controls: the slope on log2 team size (team capped at 16).
    - **Robustness.** H1–H6 are re-estimated with raw p and no family correction:
      1. Logit with topic × year dummies, on the log-odds scale. The dummies are concentrated out in the Newton steps, topic-years without outcome variation are dropped, and SEs are CR1 by topic.
      2. Keyword insider: an author ID with an earlier-year submission listing one of the paper's author keywords typed research_area, specific_topic, property or application_domain. Only papers listing such a keyword are used (80%).
      3. Early-map insider: insider in the paper's early-map topic. The fixed effects and the heat flag stay k100.
      4. Without papers that have a probable earlier version.
      5. H6 (T3) without alphabetical author lists.
      6. The 2019–2020 replication, with the same code. Here proven uses 2018–2019 acceptances.
      - A variant whose fit fails on the outcomes (e.g. logit separation) is reported with its error and does not stop the run.
    - **Figures** (drawn from the saved outputs only):
      - `teams_curves`: adjusted P(accept) by team size, one line per n_ins, panels for other and hot topics, groups with at least 30 papers;
      - `teams_proven_familiar`: bars for the 4 proven × familiar cells by heat, with 95% CI and n;
      - `teams_role_grid`: 3 × 3 heatmaps for other and hot topics, with adjusted P and n;
      - `teams_family`: H1–H6 with 95% CI and ± MDE80.
    - **Validation before the run.**
      - Unit tests check:
        - the LPM against `ols.fe_ols`;
        - the logit against `logit.fe_logit`;
        - contrasts against a reparametrised regression;
        - adjusted probabilities against raw means when there is a single cell;
        - permutation draws against refits;
        - the feature construction, on toy data and on real outcome-free data;
        - the meaning of each family contrast, using LPM targets computed on known probabilities:
          - a hot-only insider plant loads on H3;
          - a first-author plant gives H6 < 0;
          - a proven-outsider plant loads on H4 (and H5 if hot-only);
          - plants on experience alone or on team size alone give 0 on all six tests;
        - the decoding of the descriptive groups;
        - that a failing robustness variant is reported, not fatal.
      - The real outcome-free checks confirm that familiar equals the frame's incumbent, team equals the frame's team_size, and the 2023–26 n_ins counts are 23,581 / 4,703 / 2,637 / 3,077.
      - Calibration on simulated frames:
        - null: acceptance depends on year only;
        - threshold plant: +0.3 log-odds if n_ins ≥ 1, nothing more;
        - last-author plant: +0.3 log-odds if the last author is an insider.
      - The calibration reports, per test:
        - size and Holm family-wise rejection;
        - power;
        - bias and 95% CI coverage of the target, which is the same LPM contrast computed on the true probabilities (the estimator's expectation).
      - The lead runs the full calibration: 200 nulls and 50 frames per plant.
      - In a fixed-design check (7,000 null draws on 3 frames), CR1 sized about 5% for H1, H2 and H6, and 5.6–5.8% for H3, H4 and H5. These rest on small or hot-only cells; hot topics give about 25 effective clusters.
    - **Reading.**
      - These are associations within topic-year, at a fixed team size and a fixed number of authors with ICLR experience.
      - With experience held fixed, an insider coefficient compares turning a crossover author into a topic insider. It measures topic familiarity net of general ICLR experience.
      - T1's reference (no insider) includes proven outsiders, so H1 is "an insider vs the mix of no-insider teams". The proven-versus-familiar question is answered by T2 and H4.
      - Keyword-based and k100 insider status correlate only 0.18–0.29 at fixed n_exp; early-map status correlates 0.42–0.55. These variants measure related but different constructs. A null keyword variant next to a positive k100 H1 is expected even if the k100 association is real.
      - Biases that apply:
        - selection: experienced and insider authors may join better projects;
        - truncated histories (before 2021, and outside the discovery split), which bias contrasts towards zero;
        - own resubmissions make returning authors insiders mechanically. This is rare here (1.6% of 2023–26 papers have a shared-author nearest earlier paper with centred cosine ≥ 0.80), and only flagged earlier versions (0.4%) are controlled or dropped.
      - H6 rests on few papers whose only insider is the first author (about 460), so its MDE80 is about 6–7 pp. H5's is about 11 pp. A null result there is not evidence that roles do not matter.
  - **PH5 cleantext: are the pivot and position results produced by post-decision text?** (`posthoc.py ph5 cleantext`, module `ph5_cleantext.py`. Declared 2026-10-17, after the pivot and position runs and before this one. Post hoc and exploratory; a robustness check of results already seen, so it cannot strengthen them, only weaken them.)
    - **Why.** The abstracts are the OpenReview versions after the decision. A de-anonymised code link or a "code is available" sentence appears in 15–19% of accepted abstracts and in under 1% of rejected ones (`ph5_fmwave/code_links.csv`). Novelty (position) and distance from the authors' earlier work (pivot) are both cosines of SPECTER2 vectors of that text. A lab's GitHub link shared between its accepted papers could pull a paper towards its authors' earlier work, and an unusual URL token could push it away from the field. Either could manufacture or inflate the pivot and position findings.
    - **Input.** `research/topics/embed_specter2_clean.py` (outcome-free; it reads only titles and abstracts):
      - It drops every availability sentence, present or future tense ("code is available", "code will be released upon acceptance"), so submitted versions lose theirs too.
      - It drops every sentence that points to a URL: the sentence minus its URLs mentions code, a page, a release, a repository and the like, or has at most 30 words. In a longer content sentence only the URL is removed.
      - It then removes any remaining URL (plain, `\url{}`, `\href{}{}`, github.io, anonymous 4open.science links) and collapses whitespace.
      - It re-embeds only the papers whose text changed beyond whitespace (5,820 of 43,480), with the same model, revisions, input format, pooling and length limit as `embed_specter2.py`. A reproduction check re-embeds 64 random unchanged papers with the same code and compares them with `specter2.npy` (minimum cosine recorded in `cache/specter2_clean_meta.json`).
      - It writes `cache/specter2_clean.npy`, in the original row order, with every other row copied unchanged, plus `cache/specter2_clean_changed.csv`.
      - Amended before the run (outcome-free; no acceptance was read):
        - The first rule removed only present-tense availability sentences and bare URLs. It left 895 dangling stubs such as "Code available at", and it counted whitespace-only differences as changes (18,651 papers).
        - The first embedding job was killed for memory. The script now embeds in resumable chunks.
        - About 10% of the sentences dropped by the availability pattern are ordinary content (e.g. "no negative data are available"). The pattern reads the text only, never the decision, so these drops hit accepted and rejected papers alike.
      - Other venue markers are negligible in the outcome-free counts: "ICLR" appears in 81 abstracts, "camera-ready / published at / accepted at" in 28, "oral/spotlight" in 14 (all years together). They are left in.
      - The file is frozen by its sha256, `f4a2af266b56dbcafecfbcf4cfedd6f1beb893a13e0604fd10ee520572bd6aa4` (`CLEAN_SHA256` in the module), recorded before the run. `compute()` refuses any other file.
      - Outcome-free build facts:
        - 5,820 papers changed: 2,487 in 2026, 1,486 in 2025, 811 in 2024, 435 in 2023, 9–218 per year before.
        - The 64 unchanged papers re-embedded as a check match `specter2.npy` (minimum cosine 0.99999994).
        - For changed papers, the cosine between the original and clean vectors has a median of 0.9993 and a minimum of 0.961.
        - In 11 changed papers the removed text lay beyond the 512-token limit, so their vectors are identical.
    - **Analyses** (everything else unchanged: the same code paths, the same frozen `ph5_pivot.REF` reference points and knots, the same seeds and the same 200 calibration nulls):
      - pivot: the declared family E1–E4 (Holm over the four), via `ph5_pivot.declared`;
      - position: Family 1, P1a–P7 (calibrated p for P3–P7, Holm over the eight, p_used as declared), via `ph5_position.declared` and `calibrated_p`.
      - Secondary, robustness, dyadic and bootstrap parts of the two modules are not re-run.
    - **Key tests and reading** (fixed now): E1 and E4 (pivot), P1b and P7 (position), the four results the PH5 synthesis would present. Each is read as:
      - **holds**: same sign as the committed run and Holm p < .05 in its family;
      - **attenuated**: same sign, Holm p ≥ .05, and the clean 95% CI contains the committed estimate or half of it;
      - **does not hold**: otherwise.
      - A key result that does not hold is dropped from the shortlist. An attenuated one is shown only with this caveat.
    - **Also reported:**
      - how far each feature moved (correlation and mean absolute difference, original vs clean, for all 2019–2026 papers and separately for those whose own text changed; the share of papers whose novelty quintile changed);
      - the share of decided 2019–2026 papers whose text changed, accepted vs rejected;
      - the `REF` reference points recomputed on the clean vectors (reported, not used).
    - **Not addressed.** Other camera-ready edits (rewritten results, added experiments, polished wording) cannot be removed without the submitted versions. This check covers only the visible markers.
    - **Development.** Tested on `ph5_common.simulated_frame` (switching the vectors and back, an end-to-end run with 3 nulls, the verdict logic); no real outcome was read.
