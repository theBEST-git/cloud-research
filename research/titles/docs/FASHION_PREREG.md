# Pre-registration: choosing and "chasing" a research area at ICLR — held-out confirmation

Status: **frozen 2026-10-17, before any held-out data were requested.** Hashes are in `outputs/fashion/prereg_hashes.json`. The frozen code is `src/fashion/confirm.py`; the calibration files are in `outputs/fashion/frozen/`.

## 0. Exploration history (what was looked at before freezing)

- **Exploration used the full discovery split** (43,482 submissions). The PI decided on 2026-10-17 not to split discovery into halves, because the data are limited. Every claim below is tested **once** on the never-used held-out split (about 20% of submissions).
- **Look-ahead bias, found and fixed.** The first heat measure used fixed topic clusters fitted on all years, 2026 included. Under it, "small but rising" topics looked like a 3.6× jackpot for hits; most of that was survivorship. Every measure here uses only papers of t−1 and t−2.
- **Adversarial audit** (`outputs/fashion/explore/AUDIT.md`, discovery only). It changed the plan:
  1. **"Established neighbourhood" (local density) mostly measures how central or generic an abstract is** (embedding hubness). The old H3 ("reviewers reward large areas") is replaced by a centrality claim with team controls.
  2. **Pooled interactions with momentum were biased by year composition.** Interaction specs now include year-specific momentum slopes, `i(year, mom_p)`. "Naming pays in rising areas" fails on the citation percentile and is demoted to secondary.
  3. **The insider premium is partly team productivity and partly teams continuing an accepted line.** Specs now control `l_team_prev` (and its interaction with momentum) and the team's accepted history; the split is reported.
  4. **The momentum–citation association is concentrated in the 2024–25 cohorts**, which have short citation windows. A period split is pre-registered.
- **Search breadth, reported honestly.**
  - About 5 outcomes × 10+ heat measures × 12+ moderators were available, roughly 50 main effects and 600 interactions.
  - About 80 estimates were inspected in exploration; the audit ran about 150 robustness specifications on the shortlisted claims.

## 1. Claims (each is advice for choosing what to work on)

| ID | Claim |
|---|---|
| H1 | **Momentum and readers.** An accepted paper whose idea neighbourhood was growing before submission is more likely to become top-10% cited. |
| H2 | **No reviewer premium for momentum.** Momentum's effect on acceptance, from the bottom to the top percentile, is below **+3 percentage points** (non-superiority; about 10% of the base rate). |
| H3 | **Off-centre abstracts are accepted less.** Acceptance rises with centrality, i.e. the abstract's mean similarity to last year's papers, for teams with comparable history. |
| H4 | **The wave's payoff goes to insiders.** Among teams with earlier ICLR submissions, momentum raises P(hit) more for teams that already worked within cos 0.80 of the idea (insiders) than for teams new to it (entrants). This holds net of team productivity × momentum and year-specific momentum slopes. |
| H5 | **Continuing a line is accepted more.** Insiders are accepted more often than entrants with the same team history (max and total prior acceptances, number of prior submissions). |

## 2. Data handling

- **Held-out data are read once.** The command is `python -m fashion.confirm heldout <submissions.csv.gz> <submission_authors.csv.gz>`. It writes a guard file and refuses a second run.
- **Run order.** The older WP9 bundle (`analyses.prereg_confirm heldout`, CT1–CT12) is run first, then this study.
- **Frame construction.** `fashion.confirm.raw_frame` builds the held-out frame from raw rows:
  - pools, title features and topic100 come from `prereg_confirm.prepare_frame` (frozen MiniLM centroids);
  - abstracts are name-masked and embedded with bge-small;
  - citations come from the same Semantic Scholar venue cache (retrieved 2026-10-17), with the same title-match rule as `cites/match.py`.
- **Pipeline check.** The same code was run on 1,500 discovery papers taken from the raw CSV; results are in `outputs/fashion/pipeline_check.json`.
  - All categorical variables agree 100%: topic, pools, NAME, entry status, top-10%, hit.
  - Continuous measures correlate above 0.9999. The small differences come from float16 vs float32 embeddings near the 0.80 threshold.
- **Fixed reference.** Every measure for a paper of year t, whether discovery or held-out, is computed against **discovery** papers of t−1 and t−2. Percentiles use the discovery ECDF of the paper's year.

## 3. Measures

Embeddings are bge-small, abstracts name-masked; the neighbour threshold is cos 0.80.

| Variable | Definition |
|---|---|
| `loc1`, `loc2` | Neighbours among discovery papers of t−1 / t−2, per 1,000 submissions. `size_p` is the percentile of `loc1`. |
| `mom_p` | Percentile of `log((c1+1)/N1) − log((c2+1)/N2)`. |
| `hub_p` | Percentile of the mean cosine to all discovery papers of t−1 (centrality). |
| `nnr_p` | Percentile of the residual of the closest-predecessor cosine on a per-year quadratic in `log1p(loc1)`. |
| `acc_rev` | Accepted among reviewed (ACC vs REJ + WD). |
| `top10` | Citations ≥ the discovery top-decile threshold of that year, among accepted, matched papers. |
| `hit` | Accepted and top-10%, among reviewed. Accepted but unmatched papers are excluded. |
| `entry` (2022+) | *Newcomer*: no earlier discovery submission shares an author key. *Insider*: an earlier team submission has cosine ≥ 0.80. *Entrant*: otherwise. |
| `lprior_acc`, `lsum_prior_acc` | log1p of the max and of the sum, over authors, of earlier accepted discovery submissions. |
| `l_team_prev` | log1p of the number of earlier team submissions. |
| `team_area_acc` | An earlier **accepted** team submission lies within cos 0.80. |

## 4. Primary family

- **Model.** LPM with year fixed effects; SEs clustered by topic100.
- **Test.** One-sided t-tests (df = clusters − 1) in the stated direction.
- **Multiplicity.** Holm across H1–H5 at α = 0.05.

| ID | Sample | Model (`\| year`) | Test |
|---|---|---|---|
| H1 | Accepted, 2019–25 | `top10 ~ size_p + hub_p + mom_p + nnr_p + log_authors` | mom_p > 0 |
| H2 | Reviewed, 2019–26 | `acc_rev ~ size_p + hub_p + mom_p + nnr_p + log_authors` | mom_p < +0.03 |
| H3 | Reviewed, 2022–26 | `acc_rev ~ hub_p + mom_p + nnr_p + log_authors + ins + ent + lprior_acc + lsum_prior_acc + l_team_prev` | hub_p > 0 |
| H4 | Reviewed insiders + entrants, 2022–25 | `hit ~ ins + ins:mom_p + i(year, mom_p) + l_team_prev + l_team_prev:mom_p + size_p + hub_p + nnr_p + log_authors + lprior_acc` | ins:mom_p > 0 |
| H5 | Reviewed insiders + entrants, 2022–26 | `acc_rev ~ ins + size_p + hub_p + mom_p + nnr_p + log_authors + lprior_acc + lsum_prior_acc + l_team_prev` | ins > 0 |

Each claim gets two pre-specified labels:

- **Confirmed:** Holm-adjusted p < 0.05.
- **Replicated (unadjusted):** one-sided p < 0.05 in the held-out data alone. This is reported for every claim.

If neither applies, the claim is labelled "same direction, not significant" when the estimate falls on the predicted side of the null, and "not replicated" otherwise. **Pooled** (discovery + held-out) estimates are reported as the best estimates of effect size.

## 5. Secondary (reported, no multiplicity claim; `SECONDARY` in `confirm.py`)

- **H1 qualifiers:** 2019–23 vs 2024–25, and on the citation percentile.
- **H2 components:** acceptance among decided papers; withdrawal (momentum raises withdrawals in discovery); a +5 pp margin.
- **H3 variants:** a bottom-decile centrality indicator; 2019–26 without team controls; centrality and top-10% citations.
- **H4 decomposition:** insiders continuing an **accepted** line vs other insiders, each × momentum; top10 given acceptance.
- **H5 split:** insiders with vs without an accepted close prior paper, each vs entrants.
- **Closeness to the nearest predecessor:** acceptance (−) and top10 (+), plus their interactions with momentum (with year slopes).
- **Titles:** NAME × momentum on top10, citation percentile and acceptance (with year slopes); informativeness × size on log citations; entrants vs newcomers on acceptance.
- **Decision tables:** P(accept), P(top10 | accepted) and P(hit) by size × momentum tercile and by entry × momentum tercile.

## 6. Discovery dry run (`outputs/fashion/dryrun.json`) and expected power

The held-out split is about a quarter the size of discovery, so its SEs should be roughly 2× the discovery SEs.

| ID | Discovery estimate (SE) | Expected held-out z | Rough power (one-sided, unadjusted) |
|---|---|---|---|
| H1 | +0.136 (0.015) | 4.5 | > 0.99 |
| H2 | −0.006 (0.011) vs +0.03 margin | 1.6 | ≈ 0.5 |
| H3 | +0.044 (0.013) | 1.7 | ≈ 0.55 |
| H4 | +0.034 (0.009) | 1.8 | ≈ 0.6 |
| H5 | +0.047 (0.008) | 3.1 | ≈ 0.95 |

Discovery effects are probably inflated by selection (winner's curse), so the true power for H2–H4 is likely below these values. Under Holm, H2–H4 will be confirmed only if they come out stronger than expected; the unadjusted replication label is reported so that the evidence is visible either way.

## 7. Interpretation limits (stated in advance)

- **Observational.** Teams choose areas; "insider" partly reflects expertise, resources and a running research line. Momentum and centrality are measured on ICLR submissions only.
- **Citation snapshot.** Citations are one snapshot (2026-10-17). In discovery, the momentum premium is much larger for 2024–25 than for 2019–23, and it moves with the neighbourhood's later growth. It is therefore read as "more later papers nearby to cite you", not as a judgement of quality.
  - A same-age comparison (citations by the end of t+1 for 2019–21 papers) is being fetched from Semantic Scholar as an exploratory, discovery-only analysis. It is not part of this confirmation.
- **Neighbourhood definition.** Neighbourhoods are embedding based (cos ≥ 0.80), not author-declared topics. Centrality is "close to the average ICLR abstract", not a measure of novelty or quality.
