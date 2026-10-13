# Pre-registration: research fashion in ML (ICLR 2017–2026)

**Registered:** 2026-10-13, by commit on branch `claude/clever-edison-oe9pzv`. The git history is the time stamp.
**Status at registration:** contribution labels for the full corpus do not exist yet; they are being produced by an
external LLM run. No analysis of these hypotheses has been run on real labels or on acceptance outcomes.

## What had been seen before registration (disclosure)

- **Topic layer:** topic assignments, quality checks, k sweep and hindsight check. All of it is outcome-blind and
  label-free.
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
- **Topics:** published middle level, 100 topics (`research/topics/output/topic_assignments.csv.gz`).
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
- **Supported** = predicted sign, Holm-adjusted p < 0.05 in the main specification, and the predicted sign in at
  least 75% of robustness variants. Everything else is "not supported". All estimates are reported either way.
- **Main specification:** map k100, all papers in the population.
- **Robustness variants:**
  - maps k75 and k150 (k sweep);
  - year-balanced and 2017–2020-only maps (hindsight check);
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

Hypotheses supported in discovery are tested there one-sided at α = 0.05 in the predicted direction.

## Deviations

Any change to this plan after registration is listed here with its date and reason.

- (none yet)
