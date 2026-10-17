# Pre-registration: how to choose and "chase" a research area (ICLR), held-out confirmation

Status: **DRAFT — not yet frozen.** It will be frozen (hash in `outputs/fashion/prereg_hashes.json`) before any held-out data are requested.

## 0. Why held-out, and what was explored

- **Exploration.** Exploration used the **full discovery split** (43,482 submissions). The PI decided on 2026-10-17 not to split discovery into explore/confirm halves because the data are limited. Every claim below is instead tested **once** on the never-used held-out confirmation split (~20% of submissions).
- **Look-ahead bias found and fixed.** The first heat measure used the fixed topic clusters, which were fitted on all years, 2026 included. Under it, "small but rising" topics looked like a 3.6× jackpot for hits. Most of that was survivorship: a topic that later grew large already existed as a cluster before it grew. All measures below use only papers from years t−1 and t−2.
- **What was searched (garden of forking paths, reported honestly):**

  | Dimension | Variants tried |
  |---|---|
  | Heat definition | 3: fixed clusters; rolling KMeans on t−2..t−1; cluster-free neighbourhoods |
  | Outcomes | 4: acceptance, top-10% citations among accepted, hit, log citations |
  | Interactions | heat × {size, closeness to predecessor, same-cycle surge, team prior acceptances, team entry status, 5 title features} |
  | Robustness splits | era, LLM vs non-LLM, resubmission exclusion |

  About 60–80 coefficient estimates were inspected in total. The six primary claims were chosen for being useful to authors and robust across eras and LLM vs non-LLM topics, not only for their size.

## 1. Questions (each is advice for someone choosing what to work on)

| ID | Claim |
|---|---|
| H1 | Readers reward momentum. An accepted paper whose idea neighbourhood was growing before submission is more likely to become top-10% cited. |
| H2 | Reviewers do not reward momentum. Its effect on acceptance (bottom → top percentile) is below +5 percentage points (non-inferiority bound). |
| H3 | Reviewers reward established neighbourhoods. Acceptance rises with the size of the paper's neighbourhood in t−1. |
| H4 | The wave's payoff goes to insiders. Among teams with earlier ICLR submissions, momentum raises P(hit) more for teams that already worked in the neighbourhood (insiders) than for teams entering it (entrants). |
| H5 | Switching areas costs acceptance. Insiders are accepted more often than entrants, with the same controls. |
| H6 | Naming pays in rising areas. The citation advantage of a "NAME: subtitle" title grows with momentum. |

## 2. Data and handling

- **Held-out split.** The held-out submissions and author tables are read once by `python -m fashion.confirm heldout <submissions.csv.gz> <submission_authors.csv.gz>`. The command writes a guard file and refuses a second run.
- **Order of use.** The older WP9 bundle runs first (`analyses.prereg_confirm heldout`, CT1–CT12), then this study.
- **Held-out frame.** `fashion.confirm.raw_frame` builds it with the same code that rebuilt a 1,500-paper discovery sample in `outputs/fashion/pipeline_check.json`:
  - pools, title features and topic100 via `prereg_confirm.prepare_frame` (frozen MiniLM centroids);
  - name-masked bge-small abstract embeddings;
  - citations matched to the same Semantic Scholar venue cache (retrieved 2026-10-17) with the same title rule as `cites/match.py`.
- **Fixed reference.** Every measure for a paper of year t, discovery or held-out, is computed against **discovery** papers of t−1 and t−2. Percentiles are the discovery ECDF of the paper's year. Frozen files are in `outputs/fashion/frozen/`.

## 3. Measures

Cosine is on name-masked bge-small abstract embeddings; the neighbour threshold is 0.80.

| Variable | Definition |
|---|---|
| `loc1`, `loc2` | Neighbours among discovery papers of t−1 / t−2, per 1,000 submissions of that year |
| `size_p` | Discovery percentile of `loc1` |
| `mom_p` | Discovery percentile of `log((c1+1)/N1) − log((c2+1)/N2)` |
| `nnr_p` | Percentile of the residual of the closest-predecessor cosine (max over t−1..t−2) on a per-year quadratic in `log1p(loc1)` (frozen coefficients) |
| Outcomes | `acc_rev` = accepted among reviewed (ACC vs REJ + WD); `top10` = citations ≥ the discovery top-decile threshold of the year, among accepted matched papers; `hit` = accepted & top10, among reviewed (accepted-but-unmatched excluded) |
| `entry` (2022+) | **newcomer:** no earlier discovery submission shares an author key. **insider:** an earlier team submission has cosine ≥ 0.80. **entrant:** otherwise. |
| `lprior_acc` | `log1p` of the maximum, over the team's authors, of earlier accepted discovery submissions |
| `G1_name` | `name_primary` |

## 4. Primary family

- **Model.** LPM with year fixed effects. SEs clustered by topic100. One-sided t-tests with df = clusters − 1 in the stated direction.
- **Multiplicity.** Holm across H1–H6 at α = 0.05.

| ID | Sample | Model (`| year`) | Coefficient | H1 (alternative) |
|---|---|---|---|---|
| H1 | Accepted, 2019–25 | `top10 ~ size_p + mom_p + nnr_p + log_authors` | mom_p | > 0 |
| H2 | Reviewed, 2019–26 | `acc_rev ~ size_p + mom_p + nnr_p + log_authors` | mom_p | < +0.05 |
| H3 | Reviewed, 2019–26 | same as H2 | size_p | > 0 |
| H4 | Reviewed insiders + entrants, 2022–25 | `hit ~ ins*mom_p + size_p + nnr_p + log_authors + lprior_acc` | ins:mom_p | > 0 |
| H5 | Reviewed insiders + entrants, 2022–26 | `acc_rev ~ ins + size_p + mom_p + nnr_p + log_authors + lprior_acc` | ins | > 0 |
| H6 | Accepted, 2019–25 | `top10 ~ G1_name*mom_p + size_p + nnr_p + log_authors` | G1_name:mom_p | > 0 |

**Verdicts:**
- **confirmed:** Holm-adjusted p < 0.05;
- **same direction, not significant:** otherwise, if the estimate lies on the predicted side of the null;
- **not replicated:** otherwise.

## 5. Secondary (reported, no multiplicity claim)

**S1–S7:**
- Closeness to a predecessor:
  - lowers acceptance (S1);
  - raises citations (S2);
  - both more so in rising areas (S3a, S3b).
- Size × momentum on top10 (S4).
- NAME × momentum on acceptance (S5).
- Title informativeness × size on log citations (S6).
- Entrants vs newcomers on acceptance (S7).

**Also reported:**
- Decision tables: P(accept), P(top10 | accepted), P(hit) by size × momentum tercile and by entry × momentum tercile.
- Pooled discovery + held-out estimates for H1–H6.

## 6. Discovery dry run (`outputs/fashion/dryrun.json`) and expected power

The held-out split is about 1/4 the size of discovery, so held-out SEs should be about 2× the discovery SEs.

| ID | Discovery estimate (SE) | Base rate | Expected held-out z |
|---|---|---|---|
| H1 | +0.134 (0.015) | 10.1% | ≈ 4.4 |
| H2 | −0.013 (0.011) | 30.7% | ≈ 2.9 (vs +0.05 bound) |
| H3 | +0.079 (0.012) | 30.7% | ≈ 3.3 |
| H4 | +0.055 (0.010) | — | ≈ 2.7 |
| H5 | +0.050 (0.007) | — | ≈ 3.5 |
| H6 | +0.103 (0.029) | — | ≈ 1.8 (lowest power, ~55%) |

## 7. Interpretation limits (stated in advance)

- **Observational.** Teams choose areas, so "insider" partly reflects expertise and resources. Momentum is measured on ICLR submissions only.
- **Citation snapshot.** Citations are a single snapshot (2026-10-17). Recent cohorts have short citation windows, and the momentum premium is larger for 2023–25 than for 2019–22, so part of the premium may be early attention.
- **Mechanism.** The likely mechanism for H1 is audience size (more later papers nearby to cite you). This is a description of the incentive, not a judgement of scientific value.
- **Topic definition.** Neighbourhoods are embedding-based (cosine ≥ 0.80), not author-declared topics.
