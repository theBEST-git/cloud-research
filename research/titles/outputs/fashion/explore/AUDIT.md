# Adversarial audit of the fashion candidate findings (discovery split only)

Date 2026-10-17. Only the on-disk discovery data were used (no held-out or confirmation data, and `fashion/confirm.py` was not opened). Every model is an LPM with year FE and SEs clustered by topic100, unless the row says otherwise. Estimates are b (SE).
Scripts: `src/fashion/audit_{common,loc,vars,tests,decomp,yearslopes,dehub,dehub_tests}.py`. Output files: `outputs/fashion/explore/audit/{loc_variants,loc_dehub}.parquet` and `results*.csv`. All baseline numbers were reproduced exactly.

## Verdicts

| H | Claim | Verdict | Discovery → post-audit validity spec |
|---|---|---|---|
| H1 | Readers reward momentum (top10) | **WEAKENED** | +0.133 (0.015) stays positive in every spec, but mature cohorts give +0.063 (0.019), and +0.017 (0.021) with de-hubbed momentum |
| H2 | Reviewers do not reward momentum | **SURVIVES** (as a non-superiority claim) | −0.013 (0.011); one-sided 95% upper bound +0.005; years differ (p = 0.002) |
| H3 | Reviewers reward established neighbourhoods | **BROKEN** | +0.078 (0.012) → +0.025 (0.018) with a centrality control, and +0.018 (0.013) with de-hubbed density |
| H4 | Wave payoff goes to insiders (hit) | **WEAKENED** (close to broken) | insider minus entrant slope +0.056 (0.010) → +0.036 (0.009) → +0.012 (0.013) |
| H5 | Insiders get +5 pp over entrants | **SURVIVES** as an association; the "switching cost" reading is **WEAKENED** | +0.049 (0.007) → +0.042 (0.007); +0.018 (0.007) for insiders whose close prior paper was not accepted |
| H6 | Naming pays in rising areas | **BROKEN** (fragile) | +0.104 (0.029) → +0.087 (0.028) with year slopes; +0.001 (0.027) on the citation percentile; +0.048 (0.030) with de-hubbed momentum |
| NNR | Closeness lowers acceptance and raises citations | acceptance: SURVIVES; citations: WEAKENED | acceptance −0.020 to −0.036 in every variant; citations +0.021 to +0.034 (t 1.8–2.8) |

## Cross-cutting problems found

1. **Hubness (embedding anisotropy).** bge cosines between any two abstracts average about 0.70, so a count at cos ≥ 0.80 partly measures how *central or generic* an abstract is. `hub_p` is the within-year percentile of the mean cosine to all t−1 papers, which is look-ahead free. It correlates 0.75 with `size_p`. Density built on de-hubbed embeddings (centred on the t−1..t−2 mean, with a per-year threshold that matches the mean count) correlates only 0.47 with `size_p`. `mom_p` and `nnr_p` are much less affected: they correlate 0.77 and 0.91 with their de-hubbed versions.
2. **Pooled interactions are confounded by year.** The momentum slope rises over time (H1 by year), and so do the moderator shares: NAME titles go from 13% to 34% of accepted papers, and insiders from 29% to 49%. If G1_name is permuted *within year*, the null t-stat for G1:mom_p is centred at **+0.74**, not 0. Adding `mom_p:C(year)` re-centres it at +0.02, with 5.0% of |t| > 1.96. The SEs themselves are calibrated: a permuted mom_p gives sd(t) = 0.98.
3. **Own versions and same-team papers do not inflate the measures.** Insiders have on average 1.73 team neighbours (at cos ≥ 0.80) in t−1 and 0.87 in t−2; entrants and newcomers have 0 by construction. Removing these neighbours leaves H1 at 0.133 and H4 at 0.057. Near-duplicates (cos ≥ 0.95) are rare (about 500 in total). One caveat: author keys are email-based in 2017–20 and profile-based from 2021, so this check, and the insider/entrant history, cannot link 2021–22 papers back to 2019–20.
4. **Camera-ready drift.** I compared 206 accepted papers (2019+) with their pre-decision arXiv v1 abstracts. Median cosine between the two abstracts is 0.997. The change in hubness is +0.0004 (sd 0.007, against a cross-paper sd of 0.022), and the change in log density is +0.03 (sd 0.38). This is not an artefact.
5. **S2 matching.** Among accepted papers, P(matched) does not depend on mom_p: −0.001 (0.007).

## H1: top10 ~ mom_p (accepted papers 2019–25, n = 8,207, base 0.10)

| Spec | mom_p |
|---|---|
| Baseline | +0.133 (0.015) |
| Same-team neighbours removed / near-duplicates and resubmissions excluded | +0.133 (0.015) / +0.134 (0.015) |
| τ 0.78 / 0.82 / 0.85 | +0.121 (0.014) / +0.126 (0.016) / +0.121 (0.018) |
| Momentum from t−3 to t−1 / de-hubbed momentum | +0.110 (0.014) / +0.108 (0.016) |
| c1+c2 ≥ 20 / ≥ 50 (noise and regression to the mean) | +0.153 (0.017) / +0.163 (0.019) |
| Outcome log1p citations / citation percentile / top 1% dropped | +0.945 (0.073) / +0.199 (0.015) / +0.118 (0.013) |
| Leave one topic50 out (range); cluster by topic50 or r_topic | 0.127 to 0.137; SE 0.016 |
| + llm_topic / non-LLM papers only | +0.086 (0.019) / +0.102 (0.020) |
| FE: rolling topic (look-ahead free) / topic50 / topic100 / topic100×year | +0.095 (0.019) / +0.056 (0.014) / +0.042 (0.014) / +0.066 (0.017) |
| By year 2019 … 2025 | .142, .005, .089, .007, .090, .204, .180 |
| 2019–23 (mature citations) / 2024–25; mom×post2024 | +0.063 (0.019) / +0.192 (0.022); +0.130 (0.030) |
| De-hubbed: 2019–23 / with topic50 FE | +0.017 (0.021) / +0.034 (0.017) |
| + ex-post neighbourhood growth (loc_cur, loc_next) | +0.041 (0.013) |

The mechanical checks all pass. The size of the effect, though, comes from the 2024–25 cohorts, which have at most about 2 years of citations, and largely from variation between topics. Most of it moves with the neighbourhood's later growth, which looks more like a larger pool of citers than like readers rewarding momentum. **Recommended changes:** keep the pooled spec. Pre-register the 2019–23 vs 2024–25 split and one within-topic spec (rolling-topic FE, which is look-ahead free) as secondary estimates. Drop the word "reward".

## H2 / H3: acc_rev ~ size_p + mom_p (reviewed papers 2019–26, n = 41,446, base 0.30)

| Spec | size_p (H3) | mom_p (H2) |
|---|---|---|
| Baseline | +0.078 (0.012) | −0.013 (0.011) |
| ACC vs REJ only / outcome = withdrawn | +0.071 (0.014) / −0.059 (0.015) | +0.009 (0.012) / **+0.047 (0.010)** |
| FE: topic100 / rolling topic / area_h×year (2024–26) | +0.080 / +0.101 / +0.080 | −0.011 / +0.004 / −0.000 |
| τ 0.78 / 0.82 / 0.85 | +0.089 / +0.061 / **+0.030 (0.015)** | −0.019 / +0.002 / +0.015 |
| Same-team neighbours removed / t−3 momentum / excluding 2026 | +0.077 / +0.079 / +0.085 | −0.012 / −0.011 / −0.001 |
| c1+c2 ≥ 20 | +0.051 (0.013) | −0.015 (0.013) |
| **+ hub_p** (hub_p coefficient +0.070, SE 0.020) | **+0.025 (0.018)** | −0.003 |
| + hub_p + topic100 FE | −0.000 (0.017) | |
| **De-hubbed density** / with topic100 FE / ACC vs REJ | **+0.018 (0.013)** / +0.008 (0.014) / +0.022 (0.015) | −0.010 (0.013) |
| 2022+: baseline / + lprior_acc / + ins, ent / + all three | +0.082 / +0.046 / +0.027 / +0.023 (0.012) | −0.012 |
| 2022+, all controls (hub, words, llm, team) | −0.024 (0.019) | |
| Raw size deciles vs d1: d2, d5, d10 | +0.049, +0.075, +0.104 | |
| By-year heterogeneity in mom_p | | Wald χ²(7) = 22.3, p = 0.002; range −0.085 (2019) to +0.059 (2020) |
| 90% CI; share of half-samples that pass a two-sided ±0.03 equivalence test | | [−0.031, +0.005]; 0.28 |

**H3 is broken.** The size effect comes from closeness to the field's centroid, not from local density. hub_p is still +0.066 (0.020) with team controls in 2022+, while size_p falls to −0.027. Most of the effect sits in the bottom decile, i.e. outlying abstracts are rejected. In 2022+, two thirds of it is also explained by team experience: insiders make up 29%, 48% and 63% of the low, middle and high size terciles. **Recommendation:** do not freeze H3 as stated. If something is kept, freeze it as a new exploratory claim: "off-centre abstracts are accepted less", with exposure hub_p and team controls from 2022.
**H2 survives** as "no positive reward". **Recommendation:** freeze it as a one-sided non-superiority test with a pre-registered margin (for example b < +0.03, or about 10% of the base rate). Report ACC vs REJ and withdrawal separately, because momentum raises withdrawals by 4.7 pp.

## H4: hit ~ insider vs entrant momentum slope (2022–25, n = 20,903)

| Spec | slope(insider) − slope(entrant) |
|---|---|
| Baseline | +0.056 (0.010) |
| Same-team-free mom / τ 0.78, 0.82, 0.85 / t−3 / de-hubbed | +0.057 / 0.053, 0.062, 0.049 / 0.050 / 0.058 |
| **+ mom_p × year** (fixes the composition bias) | +0.054 (0.010) |
| + mom×year + **l_team_prev × mom** (median prior team submissions: insiders 11, entrants 3) | **+0.036 (0.009)** |
| + mom×year + team_area_acc × mom / + both | +0.021 (0.013) / +0.012 (0.013) |
| Strict (team-free heat + all team×mom terms + no versions) | +0.011 (0.015) |
| Outcome acc_rev / top10 among accepted (with year slopes) | −0.014 (0.025) / +0.103 (0.026) |
| By year, insider:mom vs newcomers: 2022, 2023, 2024, 2025 | +0.035, −0.013, +0.093, +0.105 |
| Non-LLM / topic100 FE / 2023–25 (with year slopes) | +0.037 (0.013) / +0.042 (0.010) / +0.052 (0.011) |
| Insiders vs entrants, by team_prev_n tercile (low, mid, high) | 0.013 / 0.032 / 0.069 |

The premium is entirely a citation effect: there is no acceptance difference. It appears only in 2024–25. Part of it is a productivity artefact: the more submissions a team has, the more likely one of them falls within cos 0.80, so prolific teams are more often classed as insiders. Of the remaining premium, most comes from insiders following up their own accepted paper (63% of insiders have such a paper). **Recommendation:** add `mom_p:C(year)` and `l_team_prev*mom_p` to the frozen spec, both on validity grounds. Expect about +0.035, and report the team_area_acc split as a decomposition.

## H5: acc_rev, insider − entrant (2022–26, n = 35,789)

| Spec | insider − entrant |
|---|---|
| Baseline / no controls except log_authors | +0.049 (0.007) / +0.080 (0.006) |
| + l_team_prev / team_prev_n bin FE / + all experience controls with bin FE | +0.053 / +0.051 / +0.042 (0.007) |
| Excluding versions (team cos ≥ 0.95) and resubmissions / strict spec | +0.051 / +0.042 (0.008) |
| ACC vs REJ / topic100 FE / area×year FE / non-LLM / 2023–25 | +0.041 / +0.046 / +0.055 / +0.041 / +0.048 |
| De-hubbed heat controls / + hub_p | +0.054 / +0.050 |
| By year 2022 … 2026 | +0.020 (0.029), +0.016 (0.022), +0.079, +0.043, +0.057 |
| Insider threshold 0.75 / 0.78 / 0.82 / 0.85 / 0.90 (+ l_team_prev) | 0.060 / 0.060 / 0.047 / 0.040 / 0.010 |
| Dose response in team_area_cos vs < 0.6 (non-newcomers) | .6–.7 +.030, .75–.8 +.098, .8–.85 +.132, .85–.9 +.159, .9–.95 +.153, ≥ .95 +.055 |
| Vs newcomers: insiders with an accepted close prior / insiders without / entrants | +0.135 / +0.078 / +0.060, so **insiders without − entrants = +0.018 (0.007)** |

The association is robust, and the gradient in team_area_cos is smooth, so the 0.80 cut-off is not critical. Near-copies of earlier papers do worse. However, two thirds of the gap is teams continuing a line that was already accepted. That is consistent with team lines that keep succeeding, more than with a cost of switching areas. The gap is not detectable in 2022–23, when only short key histories are available. **Recommendations:** add `l_team_prev` (or the bin FE) and `lsum_prior_accs`. Pre-register the team_area_acc split as a secondary analysis. Describe the result as "papers continuing a team's line are accepted more".

## H6: top10 ~ G1_name × mom_p (accepted papers 2019–25)

| Spec | G1_name:mom_p |
|---|---|
| Baseline / null t under within-year permutation | +0.104 (0.029) / centred at +0.74 |
| + mom_p × year | +0.087 (0.028) |
| + G5a, G2, llm_topic / plus topic50 FE / + controls×mom + topic50 FE (all with year slopes) | +0.090 / +0.104 / +0.087 (0.028) |
| + controls×mom + topic100×year FE (no year slopes) | +0.069 (0.028) |
| Non-LLM / same-team-free (with year slopes) | +0.115 (0.043) / +0.084 (0.029) |
| τ 0.78 / 0.82 / 0.85 (with year slopes) | 0.096 / 0.063 / 0.052 (0.031) |
| **De-hubbed momentum** (with year slopes) | **+0.048 (0.030)** |
| **Outcome citation percentile** / log1p citations (with year slopes) | **+0.001 (0.027)** / +0.110 (0.134) |
| Top 1% dropped / 2019–23 / 2024–25 | +0.085 (0.026) / +0.062 (0.047) / +0.107 (0.038) |
| By year 2019 … 2025 | .20, .17, −.12, −.01, .12, .21, .06 |
| Family of 11 title features × mom: rank of G1 by \|t\| / empirical-Bayes shrinkage factor / share of half-samples that replicate | 1st / 0.54 / 0.73 |

The effect appears only at the top-decile cut-off and is absent on the citation percentile. It is also sensitive to τ and to de-hubbing, and part of it is the year-composition artefact. After the fix, t ≈ 3.1, which is below a reasonable multiplicity bar. **Recommendation:** do not freeze H6 as confirmatory. If it is frozen, include `mom_p:C(year)`, add cite_pct as a co-primary outcome, and plan power for about +0.05 (the shrunken estimate).

## NNR (exploratory)

On acceptance, nnr_p is −0.027 (0.009) at baseline, and stays negative with non-team nearest neighbours (−0.032), without near-duplicates (−0.026), excluding versions and resubmissions (−0.026), with de-hubbing (−0.036) and with topic100 FE (−0.020). On top10 it is +0.028 (0.012) at baseline, +0.033 non-team, +0.024 (0.013) de-hubbed, and +0.021 (0.011) with topic100 FE. The mom×nnr interactions, with year slopes, are −0.058 (0.027) on acceptance and +0.120 (0.043) on top10.
The acceptance penalty is real and is not driven by resubmissions. The citation side and both interactions have t ≈ 2–2.8, so they should stay secondary.

## Multiple comparisons

The frame supports about 5 outcomes × at least 10 heat measures (three stage schemes; size, mom, nnr and gcur as percentiles or terciles; nov; crowd; r_mom) × at least 12 moderators (entry, exp3, newcomer_team, 9+ title features, llm_topic, resub). That gives roughly 50 main effects and about 600 interactions, before choices such as τ, the percentile scale and the nn residualisation. The Bonferroni bar on |t| is 3.29 for 50 tests, 3.48 for 100 and 3.93 for 600.

Post-audit t in the validity spec:

| Claim | Post-audit t | Bar |
|---|---|---|
| H1 | 8.8 (3.3 for 2019–23) | clears |
| H3 | 1.4 | fails |
| H4 | 3.8 | borderline |
| H5 | 6.0 (2.6 for the switching-cost version) | clears |
| H6 | 3.1 (0.0 on the citation percentile) | fails |
| H2 | null; judge it by the margin, not by multiplicity | — |

In 100 random half-splits, H1, H3, H4 and H5 replicated every time, H6 in 73%, and H2 met a two-sided ±0.03 equivalence test in 28%. These rates are optimistic because the specs were selected on the full data.

## Recommended changes to the frozen specification (validity only)

1. Every specification that interacts with mom_p should add `mom_p:C(year)` (H4, H6, the nnr×mom terms).
2. Add `hub_p` as a control to the loc-based specs, or report de-hubbed density alongside, and do not interpret size_p as "neighbourhood".
3. Insider and entrant contrasts should control `l_team_prev` (H5), or `l_team_prev*mom_p` (H4), and should report the team_area_acc split.
4. H2 should be tested as one-sided non-superiority against a pre-stated margin.
5. Pre-register period-split (2019–23 vs 2024–25) secondary estimates for H1 and H4.
6. None of these checks call for a restriction on c1+c2; H1 is stronger in dense neighbourhoods.
