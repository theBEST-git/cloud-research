# Final Round Shortlist: Findings for Future Authors

Final-round PH5 candidates. Audit corrections are applied and numbers re-checked against committed outputs; derived quantities (shrinkage multipliers, per-pair twin rate, 10→90% FM bound, 16/56 precision) and the uncommitted no-momentum simulation are labelled as such.
**Strength labels:** *strong* = the declared test is Holm-significant within its family, its raw p would also survive a Bonferroni correction across all PH5 tests (p ≤ 5e-4, i.e. over 100 tests), and its sign holds across declared variants (variants that lose significance are named); *moderate* = Holm-significant within its declared family only, or a single specification; *null-informative* = CI tight around zero per stated unit; *outcome-free descriptive* = no acceptance data used.
**Status:** all post hoc and exploratory. Each analysis family was declared in PREREGISTRATION.md before it was run. The shrinkage multipliers, per-pair twin rate, 10→90% FM bound and 16/56 precision are derivations from committed outputs, the no-momentum benchmark is an uncommitted simulation, and the EB tie rule was amended after outcome-free outputs. These are associations, mostly within topic × year, not effects of an author's choice.

**Fit for the 15-minute talk.** The script targets 13:00 plus a 2:00 buffer, so every added second comes out of the buffer unless something is cut. Comparable result slides take 0:55–1:15, so three new slides (~3:15–3:45) do not fit even after moving slide 15 (≈15:30, no buffer); moving slide 12 instead gives ≈16:20. Recommended plan, ending at ≈13:55 with ≈1:05 of buffer:
1. add finding 1 as ONE new slide after slide 13 (~1:15), with finding 3's concurrent-twin dot on the same figure;
2. add finding 2 as one note and one spoken sentence on slide 14 (+0:15);
3. add finding 4 as one bullet on slide 8 (+0:10);
4. make one-line edits on slides 13, 16 and 17 (+0:10).

Pay for this by moving slide 12 (title style) to the appendix (−0:25; A9–A10 already cover titles, and slide 13's table keeps 'Branded title: ratio 1.02') and trimming slide 15 from ~200 to ~140 spoken words (−0:30; the 'influx' details are already in qa.md). Keep slide 15 in the main deck: it is the deck's only worked example of a trend falling out of favour. If it is ever moved, also edit slide 14's script ('The next two slides are post hoc'), the FL bullet on slide 16, 'incl. federated learning' on slide 17, and the qa.md heading 'Areas and federated learning (slides 14–15)'. A second new slide (finding 2 on its own, ~1:00 instead of the note) brings the plan to ≈14:40; it needs about 0:45 of further cuts (e.g. slide 5 to ~50 words, slide 9 to ~85 words) to keep a 1:00 buffer, so rehearse it before committing. Findings 3 (full forest plot), 5, 6 and 7 go to backup. The script's rehearsal fallback ('cut the sentences marked *(cut if short on time)*') has no marked sentences yet; mark some before rehearsing.

**Proposed running order:** 1–11 unchanged (slide 8 gets the finding-4 bullet) → RQ3 (old 13, + footnote) → NEW 'Lower Acceptance Sits in Two Tails' (finding 1 + twin dot) → Areas (+ finding-2 note) → FL (trimmed) → Contributions (edited) → Limitations (+ camera-ready line) → Thank you. Appendix: old slide 12 joins A9; A7 updated with finding 5; A13 finding-3 forest plot; A14 finding-7 keyword states; A15 finding-6 first-time teams; A16 finding 2 as a full slide. Then update script.md (timing table, the rehearsal line that names slide 12, 'Appendix slides A1–A12') and, in qa.md, 'Appendix slides are A1–A12' and 'Numbers to remember'.

> **Robustness to camera-ready text.** Accepted abstracts are post-decision text: in 2023–26, 17.6% of accepted vs 0.5% of rejected abstracts carry a code link. The declared PH5 cleantext check removed URLs and availability sentences, which changed the text of 22.4% of accepted vs 8.5% of rejected decided 2019–26 papers. It then re-embedded those abstracts and re-ran the declared pivot (E1–E4) and position (P1a–P7) families with the code frozen; secondary and robustness variants (e.g. the newcomer control and the 11 P1b variants) were not re-run.
> - E1 far jump −5.44 → −5.39 pp (Holm 1.3e-8 → 2.0e-8): **holds**. E4 within-author +0.55 → +0.53 pp per +0.1 cos (Holm 0.006 → 0.009): **holds**.
> - P1b least-novel fifth −3.27 → −3.51 pp (Holm 0.0014 → 0.0004): **holds**.
> - P7 within-author novelty +0.39 → +0.46 pp per 10 pct points (Holm 0.105 → 0.035): **consistent, not upgraded**: a robustness re-run cannot strengthen a result, so P7 stays not Holm-significant.
> - Not covered: other camera-ready edits (rewritten results, polished wording) and other text measures (FM/contribution labels, topics, title style).
> - Figure: `/home/user/cloud-research/research/fashion/output/posthoc/ph5_cleantext/PH5_cleantext.png`

## Ranked shortlist

### 1. Lower Acceptance Sits in Two Tails (Post Hoc): **ADD AS SLIDE**
*Message:* Within topic and year, lower acceptance goes with two tails: abstracts most similar to earlier ICLR work, and papers far from every experienced co-author's earlier ICLR submissions (visible since 2021). Beyond the middle, more novelty or more closeness shows no reliable further gain.
- **Field:** the least-novel fifth is −3.3 pp vs the middle fifth (CI −4.9 to −1.6; Holm 0.0014; n = 31,549, 2019–26), negative in 11/11 variants (Holm-significant in 8; −2.0 pp, Holm 0.65, with the percentile taken within class × year; −2.4 pp, Holm 0.12, with prior density controlled; −2.5 pp, Holm 0.050, with a fixed reference). The most-novel fifth is +0.4 pp (CI −1.4 to +2.3).
- **Own record** (n = 20,430 papers with at least one experienced author, 2023–26): p10 vs median closeness is −5.4 pp (CI −7.1 to −3.8; Holm 1.3e-8). By quintile of closeness, adjusted acceptance is 39.7 / 41.8 / 44.4 / 47.2 / 46.9%. Staying close shows no detectable penalty (+1.7 pp, CI −0.2 to +3.7).
- **Checks:** −5.0 pp with newcomer status controlled (original text). On text with links and availability sentences removed, −5.39 / −3.51 pp. Within-author counterpart +0.55 pp per +0.1 cos (Holm 0.006), but co-author composition could account for half or more of it.

*Figure:* new figure needed: difference dots with CIs, one panel per module on its own axis. Field panel (position): Q1−Q3, Q5−Q3, plus a dot 'has a concurrent twin (vs none)' from finding 3 (same position model, n = 31,549). Own-record panel (pivot): p10−p50, p90−p50. Fallback: `/home/user/cloud-research/research/fashion/output/posthoc/ph5_pivot/PH5_pivot_curve.png`, showing only the dashed curve and quintile dots (hide the hot/not-hot curves).
*Strength:* **strong**. Both contrasts are Holm-significant, their raw p (1.8e-4, 3.4e-9) would survive a cross-module correction, and both keep sign and Holm significance after removing links and availability sentences. P1b loses Holm significance in 3 of 11 variants (named above). The within-author support is moderate.
*For authors:* Two places where lower-acceptance papers sit. They can serve as pre-submission checks, but they are not levers. (1) Field: the abstract is in the fifth of same-topic, same-year submissions most similar to earlier ICLR papers (SPECTER2, mean cosine to the 10 nearest earlier papers in any topic; last year's submissions in the topic are only a rough stand-in). (2) Own record, for teams with at least one experienced author: the cosine between the abstract and the closest experienced co-author's earlier ICLR submissions is below about 0.14 (bottom fifth). Beyond the middle, neither more novelty nor more closeness shows a reliable further gain. Whether rewording the abstract or adding a co-author with nearby work changes outcomes is untested (co-author choice and failure-driven pivots are not controlled).
*Caveats:*
- The two distances come from separate models and populations, and their correlation is unknown.
- Undetected resubmissions may feed the novelty floor; the prior-density control shrinks it to −2.4 pp (not Holm-significant).
- Own-record histories cover ICLR discovery-split submissions since 2021 only (2023 papers see 2021–22), so 'far' means far from the visible ICLR record.
- Both distances use post-decision abstracts. Removing links and availability sentences leaves both gaps intact, but rewritten results and polished wording remain unaddressed.

*Q&A:*
- *Just the newcomer gap?* Not only: −5.0 vs −5.4 pp with the newcomer flag controlled.
- *Is maximal novelty risky?* Not at quintile resolution (+0.4 pp, CI −1.4 to +2.3); the data cannot rule out a dip confined to the top few percent.
- *Does a hot topic change these gaps?* None of the tested gaps differs detectably in hot topics: far jump −0.4 pp (CI −3.1 to +2.4), concurrent twin −1.5 pp (CI −4.5 to +1.5), first topic insider −0.8 pp (CI −4.9 to +3.2). Power is limited (MDE80 about 4–6 pp), and the hot flag uses the k100 map.

*Where:* new slide right after slide 13 (RQ3); it also carries finding 3's twin dot.

### 2. Trend Signals Have a Winner's Curse (Post Hoc): **ADD AS NOTE ON SLIDE 14** (optional own slide; else backup A16)
*Message:* The fastest-growing-keyword and highest-acceptance-topic lists largely fail to persist exactly where they look most extreme. Noise-weighted versions keep a real but much smaller signal.
- Raw-growth top keywords are top again the next year less often than the base rate (16.0% vs 20.6%; lift −0.045; Holm 0.018; 2,491 keyword-years). EB (count-weighted) top keywords persist (40.3% vs 22.1%; Holm 0.006), yet gain share **less** often than others (28.6% vs 36.1%; −7.6 pp, CI −12.0 to −3.0).
- A topic's 2018–22 acceptance edge goes with 0.38× of itself in 2024–26 (CI 0.18 to 0.58; Holm 0.001; 82 topics). The top tenth went from +14.3 to +2.1 pp.
- A real spread remains: noise-free SD 6.4 pp (CI 5.0 to 7.2; p_perm 0.005). A single year's rate is half noise at about 58 decided papers.

*Figure:* `/home/user/cloud-research/research/fashion/output/posthoc/ph5_premia/PH5_premia_winners.png` (left and right panels) and the keywords panel of `/home/user/cloud-research/research/fashion/output/ph5_forecast/forecast_persistence.png`.
*Strength:* **strong** for topic shrinkage (b = 0.38, Holm 0.001; raw p 3e-4 also survives a cross-module correction). **Moderate** for the keyword lifts: Holm-significant within their family (0.018 / 0.006) but not across modules, and keyword-specific (on topic maps the raw lift is not negative: early map +0.04, Holm 0.25; k100 +0.11). The keyword part is outcome-free (submission shares).
*For authors:* Before choosing a topic for its acceptance record, shrink its multi-year gap. A 5-year (2018–22) gap measured on 75 / 150 / 300 decided (accepted or rejected) papers has gone with about 0.37 / 0.52 / 0.65 of itself in 2024–26 (a derivation from early-map topics). A single year's rate is half noise at about 58 decided papers. Rank keyword growth by noise-weighted (EB) growth rather than raw percentage jump. Even EB-hot keywords' share rises the next year less often than others' (28.6% vs 36.1%).
*Caveats:*
- Noise predicts the sign, not the size, of the raw reversal. A no-momentum simulation (uncommitted) gives about −0.11; the observed −0.045 fits real momentum masked by noise.
- The raw reversal holds for keywords only (on k100 topics the lift is +0.11).
- The raw keyword reversal is confined to the 1-year horizon and 10–19-user keywords (h = 2: lift −0.003, p 0.88; 20–49 users: +0.015).
- The tails hold 7–9 topics, and topics needed ≥50 submissions in both windows.
- Top-tenth retention R = 0.15 has CI −0.11 to 0.42 (includes 0).
- The multipliers assume the 2018–22 → 2024–26 relation carries forward.
- The EB tie rule was changed after seeing outcome-free outputs (disclosed).

*Q&A:*
- *Regression to the mean?* Largely, yes. The contribution is the size: about 0.4×, and the extremes keep roughly 15–25% of their edge (wide CIs that include 0).
- *Doesn't this undercut the FL slide?* No. FL was not an extreme in 2018–22 (topic −4.6 pp, keyword −0.6 pp). Its gap appeared in 2024–26 (−11.7 / −11.5 pp on 297 decided papers).

*Where:* one note and one spoken sentence on slide 14 (area ranking; text under Corrections). If time allows, its own slide right after slide 14; otherwise backup A16.

### 3. Concurrent Crowding Shows No Detectable Acceptance Gap (Post Hoc): **ADD AS ONE DOT ON FINDING 1's SLIDE + BACKUP SLIDE A13**
*Message:* Within topic × year, three usual worries show no detectable association with acceptance: a concurrent same-problem paper, an unexpected topic boom, and the FM-vs-non-FM gap changing as a topic's FM share rises. Similarity to earlier cycles' work does show one (finding 1).
- 48.8% of 2026 submissions (19.5% in 2019) have an independent same-year "twin" on the same narrow problem (cos ≥ 0.70), rarely the identical idea. Twinned papers: +0.7 pp (CI −0.8 to +2.2; Holm 1.0; n = 31,549). Twins per paper per 1,000 submissions fell from 0.32 to 0.19 (derived from `ph5_position/free_twin_share.csv`), which is consistent with volume rather than herding.
- Booms: incumbents −0.6 and newcomers +0.7 pp per SD (Holm 0.50). FM premium slope with prior adoption: +0.19 pp per logit unit (CI −0.96 to +1.34).
- Per unit, the CIs exclude gaps beyond about 1–2 pp. Over larger contrasts (10→90% FM adoption, a derived bound of about −4.2 pp; hot-topic twin difference, −4.5 pp) gaps of about 4–4.5 pp remain possible.

*Figure (backup A13):* new two-panel figure. Left panel: position-module concurrent rows only (P2 any twin; P4 hot − other), in pp, with CIs. Right panel, with its own axis: P1b (least-novel fifth − middle fifth). Do not put E1 (pivot), the premia surge slopes or the fmwave slope on the same axis, because they differ in module, population, years and unit. E1 measures distance from the team's own record and runs in the opposite direction. Report surge and FM slopes in text with their units. Supporting: `/home/user/cloud-research/research/fashion/output/posthoc/ph5_position/PH5_position_twin_share.png`.
*Strength:* **null-informative** per unit. Per-unit CIs exclude gaps beyond about 1–2 pp, but power against a planted FM fading of −1.3 pp per logit unit was only about 60–70%, and over larger contrasts gaps of about 4–4.5 pp remain possible. The twin share is outcome-free.
*For authors:* Among submitted papers, a concurrent paper on the same narrow problem (not the identical idea) is common (48.8% of 2026 discovery-split submissions) and shows no detectable acceptance gap (+0.7 pp, CI −0.8 to +2.2; +1.0 pp, CI −0.6 to +2.6, after removing links and availability sentences). Projects abandoned after a scoop are not observed, and identical ideas, earlier preprints, citations and visibility are not tested. This does not show that continuing a scooped project carries no cost.
*Caveats:*
- Twins are counted in the discovery split only (likely attenuated). Identical ideas (cos ≥ 0.80, 692 decided pairs) have no acceptance-gap test, only an underpowered shared-fate test (p 0.15).
- Selection: only submitted papers are observed.
- Acceptance stage only; citations and visibility are not measured.
- Cooling keywords: +0.1 pp (CI −2.0 to +2.3). The one timing contrast that shows an association is finding 7.

*Q&A:* *Isn't 49% twins herding?* It fits volume better: the per-pair rate fell about 40%, and newcomers are less often twinned (−3.9 pp).
*Where:* on the finding-1 figure, add a dot labelled 'has a concurrent twin (vs none)': +0.7 pp (CI −0.8 to +2.2; same position model, n = 31,549). Say: 'Similarity to earlier ICLR work goes with lower acceptance; similarity to concurrent submissions shows no detectable gap.' The full figure (booms, FM-premium slope, hot-topic rows) goes to backup A13 for Q&A.

### 4. Topic-Growth Forecastability Appears Only on the Hindsight Map: **ADD AS BULLET**
*Message:* On a map fitted with papers through 2026, small size "predicts" 2-year topic growth out of time (R² 0.28). On a map fitted on 2017–20 papers only, size shows no detectable predictive value (R² −0.03).
- Test origins 2021–24: k100 Spearman 0.59 vs early −0.04 (p 0.39). Without the LLM/VLM areas, R² is 0.30 vs −0.09.
- P(top-fifth growth) by size tercile, small/mid/large (in-sample): 40 / 21 / 2% on the hindsight map vs 22 / 20 / 20% on the prospective map.
- Real forecasting is weak: momentum Spearman 0.20; top-fifth precision 0.39 (30/76; chance 20%) over origins 2021–24, but only 16/56 (29%) for origins 2021–23 (per-year counts recomputed from `b4_predictions.csv`). Most of it comes from the single 2024 origin (14/20), whose target year is LLM-dominated.

*Figure:* middle column of `/home/user/cloud-research/research/fashion/output/ph5_forecast/forecast_topics.png`; better, a new tercile bar chart from `b4_conditional.csv` beside `figs/hindsight_emerging.pdf`.
*Strength:* **outcome-free descriptive**. The contrast is large and survives dropping the LLM areas, but there is no paired test and the maps differ in corpus.
*For authors:* Distrust "this cluster grew 5×" motivations built on clusters fitted with later papers; re-check them on clusters fitted on earlier papers only.
*Caveats:*
- The early map cannot represent topics born after 2020.
- The maps also differ in fitting corpus and eligibility timing (early: 100 topics from 2021; k100: 85–100), so the gap cannot be attributed to hindsight alone.
- Tercile rates are in-sample cells, not the out-of-time test; B4 metrics are unadjusted.
- Year-to-year persistence of topic premia (0.91 vs 0.61) has overlapping CIs; do not headline it.

*Q&A:* *Regression to the mean?* That would act on both maps, yet the prospective map is flat.
*Where:* extra bullet on slide 8 ("Consequence: Substantive Conclusions Depend on the Map").

### 5. Experience More Than Headcount: The First Topic Insider Carries the Insider Association (Post Hoc): **APPENDIX (update A7)**
*Moved up from #6 after the audit: all numbers committed; the former #5 relies partly on uncommitted checks.*
*Message:* Within topic and year, the per-author association with acceptance is about three times larger for venue-experienced authors than for novices. At fixed team size and number of experienced authors, one topic insider (vs none) goes with +3.4 pp.
- Per author (n = 24,601, 2023–26): novice +1.47 pp (CI 0.95 to 1.99), crossover +4.77, insider +5.34. Crossover minus novice is +3.3 pp (p 3e-16).
- One insider vs none: +3.4 pp (CI +1.2 to +5.7; Holm 0.019). Two or more vs one: +0.5 pp (CI −2.2 to +3.2; concavity Holm 0.55).
- Familiarity without an earlier acceptance on record (767 papers): +0.2 pp (CI −3.8 to +4.2).

*Figure:* new per-head coefficient plot from `decomposition.csv`. Existing: `/home/user/cloud-research/research/fashion/output/posthoc/ph5_teams/teams_family.png`.
*Strength:* **moderate**. The decomposition is one specification outside the family, and H1 survives Holm only within its family.
*For authors:* Much of the per-head association sits with venue-experienced members (about +5 pp each vs +1.5 pp per novice, which is still nonzero). No model splits the team-size slope itself by author type. Selection is heavy, so this is not advice to recruit names.
*Caveats:*
- Histories start in 2021.
- H1 is null with a keyword-based insider (+0.0 pp) and holds on the early map (+3.0 pp).
- Heavy selection: experienced and insider authors may join better projects.
- Holm 0.019 holds within the teams family only; across the seven modules it would not survive (Bonferroni about 0.17).
- H1 is n.s. in the small 2019–20 replication (+4.3 pp, CI −2.9 to +11.5).

*Q&A:* *Obvious?* The direction is; the sizes (+1.5 vs about +5 pp per head) are not.
*Where:* update appendix A7 (team size).

### 6. First-Time Teams List Fewer Emerging Keywords and Submit Fewer FM Papers (Outcome-Free): **BACKUP ONLY**
*Message:* Within topic and year, first-time ICLR teams list Emerging keywords less often and Mainstream or Cooling keywords more often. At 5–50% prior adoption, they also submit FM papers less often than returning authors new to the topic.
- Keyword uses (26,640 papers): Emerging −3.7 pp (raw 16.7% vs 25.0%), Cooling +2.4, Mainstream +2.3 (BH q ≤ 0.004). Young-flat and young-falling show no detectable difference.
- FM papers (33,993 submissions, 2023–26): −4.6 / −9.0 / −14.7 pp at 5–15 / 15–30 / 30–50% adoption (p ≤ 1e-4). At 0–5% it is −1.0 (p 0.08); at ≥50%, −2.0 (p 0.14).
- The link to acceptance is not established. The declared profile interactions (teams with no earlier acceptance vs established teams, not first-time teams specifically) are n.s.: kwtiming D_E/D_C MDE80 5.7–6.2 pp, and fmwave B1/B2 n.s.

*Figure:* right panels of `/home/user/cloud-research/research/fashion/output/posthoc/ph5_fmwave/PH5_fmwave_fm_share.png` and `/home/user/cloud-research/research/fashion/output/posthoc/ph5_kwtiming/PH5_kwtiming_free.png`.
*Strength:* **outcome-free descriptive**. The gaps are large; the odds ratios and robustness re-runs are uncommitted.
*For authors:* First-time teams can check a target topic's FM share and keyword vintage. Whether matching them goes with acceptance is not established: the related profile interactions are n.s. and underpowered (MDE80 5.7–6.2 pp), and they compare teams without an earlier acceptance with established teams, not first-time teams.
*Caveats:*
- Descriptive and conditional on submission.
- The 2021–22 ID switch misclassifies some teams.
- The keyword model has no team-size control.
- The FM label is an LLM label on partly camera-ready abstracts. Accepted abstracts are more often camera-ready, so groups accepted less often (likely including first-time teams) differ in text state, and the link-removal check did not cover FM labels.

*Q&A:* *Does this contradict RQ2?* No: topic-newcomer papers are more often method papers; first-time teams use older keywords and fewer FMs. Definitions differ.
*Where:* backup A15 (see running order).

### 7. Emerging vs Mainstream Keywords: A Modest Edge (Post Hoc): **BACKUP A14 + one footnote on slide 13**
*Message:* Within topic and year, papers listing a still-rising keyword 1–2 years old are accepted 2.7 pp more often than papers listing an old, flat one. Age alone is not established: the declared age gradient is not supported.
- +2.7 pp (CI +0.8 to +4.6; Holm 0.020; null-frame p 0.005), positive in 7/7 variants (n = 22,302).
- Age gradient +1.7 pp (Holm 0.077, not supported). Old rising keywords are also +3.9 pp (nominal), so the contrast may reflect a low Mainstream baseline as much as keyword age.
- Within a keyword, rising vs flat is +0.9 pp (CI −0.8 to +2.7).

*Figure:* `/home/user/cloud-research/research/fashion/output/posthoc/ph5_kwtiming/PH5_kwtiming_states.png` (cells descriptive; only A1 and A2 are declared cell contrasts; A3, the declared age gradient, is not supported).
*Strength:* **moderate**. It is Holm-significant within its 3-test family only.
*For authors:* Within the same keyword, rising and flat years show no detectable difference (+0.9 pp, CI −0.8 to +2.7). Between keywords, papers listing young rising keywords sit 2.7 pp above those listing old flat ones. Neither result shows that choosing or relabelling a keyword changes acceptance.
*Caveats:*
- Age, size and breadth are confounded (reinforcement learning is about 18% of Mainstream).
- Labels are author-chosen.
- Holm 0.020 holds within the 3-test family only; pooled across modules (about 41 declared tests) A1 would be about 0.18.
- Young cells come from 2020–26 only.

*Q&A:* *Add a new keyword?* Relabelling is untested.
*Where:* backup A14; one footnote on slide 13 as a post hoc association, not an exception (text under Corrections).

## Corrections to the existing deck
- **A8, FM +4.6 pp:** add: in 2023–26, within topic × year in topics with ≥50% prior adoption, the premium is +2.5 pp on k100 (CI −1.3 to +6.3, Holm 0.38) vs +6.0 pp on the early map (CI +3.1 to +8.8). It may depend on the comparison set and period: period and population also differ (the deck's +4.6 pp covers all years, E1), and A2 is a mildly liberal test. The k100 comparison is not "content-matched".
- **Slide 14, area ranking:** the figure ranks author keywords, and the bullets also cite k100 topics. Add \gnote{Re-measured extremes shrink: a 2018–22 acceptance gap goes with about 0.5× of itself in 2024–26 for keywords (0.53, CI 0.10 to 0.95) and 0.35× for k100 topics (CI 0.17 to 0.54) (post hoc). Federated learning is not such a case: its gap opened later (topic −4.6 → −11.7 pp; keyword −0.6 → −11.5 pp).} The noise-free spread is 4.7 pp for keywords and 6.1 pp for k100 topics (6.4 on the early map). Slide 14 shows pooled 2018–26 gaps, which are less noisy than one window, so read the ±10 pp extremes as shrunk towards zero rather than heavily shrunk. Do not quote top-tenth retention on this slide (k100 topics +14.5 → +2.7 pp, about a fifth; early map +14.3 → +2.1; keywords R 0.43; all CIs include 0).
- **Slide 13:** add \gnote{\footnotesize Post hoc association: papers listing a young, still-rising keyword sit 2.7\pp{} above papers listing an old, flat one (Holm $p = 0.02$ within its family; may reflect a low baseline for old flat labels; relabelling untested; A14).} **Slide 16, Substantive bullet 3:** 'Following fashions is not detectably rewarded or penalised at review; lower acceptance sits with papers most similar to earlier ICLR work and with far jumps from the team's own record (post hoc). Areas such as federated learning fall out of favour as the field moves on, not because of who writes the papers (post hoc).' The finding-3 nulls go in the spoken line of the finding-1 slide and in backup A13.
- **Slide 17, limitations:** add the 17.2 pp code-link gap (17.6% vs 0.5%, 2023–26). After removing URLs and availability sentences only, the key pivot and position tests (E1, E4, P1b) keep sign and Holm significance; P7 is consistent but not upgraded. Other camera-ready edits (rewritten results, polished wording) cannot be removed without the submitted versions. Labels, topics and titles were not re-checked.
- **A7:** add the per-head split, novice +1.5 vs experienced +4.8 to +5.3 pp.
- **A6:** the far-jump gap persists with newcomer status controlled (−5.0 pp).

## Do not put on slides
1. Teams H5 hot-topic reversal (116 papers, Holm 0.19); `teams_proven_familiar.png`.
2. The position most-novel-with-twin cell (+3.5 pp, q 0.38); `PH5_position_surface.png`.
3. P6 maturity × novelty (Holm 0.24) and any advice built on it; twin shared fate.
4. The fmwave spline hump (`PH5_fmwave_premium.png`); C1 framing; B1/B2.
5. The pivot "sweet spot" (cos 0.535), hot/not-hot curves, "47–60% survives author FE".
6. Premia asymmetry, named low-topic lists, flow slope, mature-topic surge term.
7. "Saturation" readings of the raw lift; the FM-share boom screen; claims from the single 2024→2026 window.
8. The kwtiming off-trend +2.0 pp, the profile splits, and anything LLM-keyword-specific.
9. E4 or P7 as standalone slides; P7 as Holm-significant; the 2019–20 replications.
10. Effect-size comparisons across modules (e.g. "far jump larger than FM premium").
11. Mechanical results: "past acceptance predicts acceptance", the n_exp gradient, and the raw twin share without per-pair normalisation.
12. Uncommitted verifier numbers presented as committed outputs.

## Guide for authors (post hoc associations at one venue)
1. **Check whether the abstract sits in the derivative tail; the most-novel fifth shows no detectable gain over the middle fifth.** The least-novel fifth is −3.3 pp (−3.5 after removing links and availability sentences); the most-novel fifth is +0.4 pp (CI −1.4 to +2.3); the data cannot rule out a dip confined to the top few percent. *[strong in the main fit; sign holds in 11/11 variants, Holm-significant in 8]*
2. **Far moves from the team's own record sit in a low-acceptance tail.** Among 2023–26 papers with at least one experienced author, adjusted acceptance is 39.7% where the closest experienced co-author's earlier ICLR work is far (bottom fifth, cos < 0.14), vs 44.4% in the middle fifth and about 47% in the top two fifths. The declared p10-vs-median contrast is −5.4 pp (CI −7.1 to −3.8; −5.39 after removing links and availability sentences). Whether bridging to earlier work changes outcomes is untested: co-author choice and failure-driven pivots are not controlled, and histories cover ICLR since 2021 only. Staying close shows no detectable penalty (+1.7 pp, CI −0.2 to +3.7). *[strong; E2 null-informative]*
3. **Shrink a topic's multi-year acceptance gap by size** (×0.37 / 0.52 / 0.65 at 75 / 150 / 300 decided papers). Topics do differ (SD about 6 pp), but by less than raw rankings suggest. *[strong; derivation]*
4. **Timing: rank keyword trends by noise-weighted (EB) growth, not raw percentage jump, and expect topic growth to be hard to forecast.** EB-hot keywords are top again at 40% vs a 22% base, yet their share rises the next year less often than others' (28.6% vs 36.1%). On a map fitted on earlier papers only, momentum ranks 2-year topic growth with Spearman 0.20; top-fifth precision is 0.39 (30/76; chance 20%) over origins 2021–24, but 16/56 (29%) for 2021–23. Size "predicts" topic growth on the hindsight (k100) map but not on the prospective map (R² 0.28 vs −0.03). Within a keyword, rising or falling years show no detectable acceptance gap vs flat ones (+0.9 / +1.2 pp), and unexpected topic booms show none (−0.6 / +0.7 pp per SD). *[keyword lifts moderate; forecasting outcome-free descriptive; acceptance nulls]*
5. **A concurrent same-problem paper or an unexpected boom showed no detectable acceptance gap within topic × year, and the FM-vs-non-FM gap did not change detectably as a topic's FM share rose.** Twins +0.7 pp (CI −0.8 to +2.2); booms within about ±2 pp per SD; FM-premium slope +0.2 pp per logit unit (CI −1.0 to +1.3). Gaps of about 4–4.5 pp over large contrasts are not excluded. A descriptive −2.5 pp per SD boom association in mature topics is not Holm-tested. The FM premium at saturation is uncertain (+2.5 pp k100 vs +6.0 pp early map). Hot topics do not detectably change the far-jump, twin or insider gaps (−0.4 / −1.5 / −0.8 pp; MDE80 about 4–6 pp). Abandoned projects, identical ideas, citations and visibility are unobserved. *[null-informative; acceptance stage only]*
6. **Papers listing young rising keywords sit 2.7 pp above papers listing old flat ones (Holm 0.020 within family).** Cooling (old falling) is +0.1 pp and middle-aged rising +0.4 pp vs Mainstream; other cells are nominal, and old rising keywords are +3.9 pp (nominal), so this may reflect a low Mainstream baseline as much as keyword age. Momentum within a keyword shows no detectable difference (+0.9 pp). Relabelling is untested. *[moderate]*
7. **Experience more than headcount.** About +5 vs +1.5 pp per head, and one topic insider +3.4 pp; selection is heavy. *[moderate]*
8. **First-time teams may want to check the topic's FM share and keyword vintage.** First-timers submit 4.6–14.7 pp fewer FM papers at 5–50% adoption; whether this goes with acceptance is not established. *[outcome-free descriptive]*

Scope: ICLR discovery split only. The held-out confirmation split is not in this repository, so these post hoc associations stay unconfirmed until it is analysed; it is where the top findings should be confirmed.
