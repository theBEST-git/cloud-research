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
