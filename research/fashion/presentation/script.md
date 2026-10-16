# Talk script: "Following the Fashion?"

- **Length:** about 1,400 spoken words, about 12 minutes at a calm pace (120 words a minute). The timing table
  allows 12.5 minutes, which leaves 2.5 minutes of buffer under the 15-minute limit.
- **Rehearsal:** time yourself once. If you run over 14 minutes, cut the sentences marked *(cut if short on
  time)*.
- **Questions:** see `qa.md`. Appendix slides A1–A11 and the references come after the "Thank you" slide.

| Slide | Target | Ends by |
|---|---|---|
| 1 Title | 0:15 | 0:15 |
| 2 Outline | 0:15 | 0:30 |
| 3 Motivation | 0:45 | 1:15 |
| 4 Research questions and hypotheses | 0:55 | 2:10 |
| 5 Related work | 0:55 | 3:05 |
| 6 Data and measurement | 1:05 | 4:10 |
| 7 Hindsight bias in topic maps | 1:10 | 5:20 |
| 8 Consequence | 0:55 | 6:15 |
| 9 Empirical strategy | 1:10 | 7:25 |
| 10 RQ1 | 0:55 | 8:20 |
| 11 RQ2 | 1:15 | 9:35 |
| 12 Exploratory: title style | 0:40 | 10:15 |
| 13 RQ3 | 0:50 | 11:05 |
| 14 Contributions | 0:40 | 11:45 |
| 15 Limitations and future work | 0:35 | 12:20 |
| 16 Thank you | 0:05 | 12:25 |

---

## Slide 1: Title (0:15)

Good morning, everyone. I'm [name]. Today I'll present a study of research fashions in machine learning: how
trends rise, who drives them, and whether following them pays off at review.

## Slide 2: Outline (0:15)

I'll start with the motivation and our research questions, then describe the data. I'll present one methodological
result and our empirical strategy, then the main results, and close with contributions and limitations.

## Slide 3: Motivation (0:45)

Table 1 shows three shifts at ICLR between 2017 and 2026.
- The share of submissions proposing a new architecture fell from 24 to 8 percent.
- The share building on a foundation model rose from almost zero to 54 percent.
- Titles of the form "NAME, colon, subtitle" rose from 9 to 41 percent.

So ML research moves in waves, both in what is studied and in how it is presented. Our question is whether these
are fashions, and if so: what they displace, who drives them, and whether followers are rewarded.

## Slide 4: Research questions and pre-registered hypotheses (0:55)

This gives three research questions. The table shows the key hypothesis for each; the full list of ten is in
Appendix A1.

- **RQ1, rise.** H1d predicts that when more of a topic's papers build on foundation models, fewer of its papers
  propose new architectures.
- **RQ2, following.** We predicted that newcomer papers would be *less* often new-method papers (H2b) and *more*
  often benchmark or evaluation papers (H2c). In other words, newcomers imitate and insiders innovate.
- **RQ3, reward.** H3a predicts that papers in more mature, crowded topics are accepted less often.

All hypotheses were registered before any analysis.

## Slide 5: Related work and positioning (0:55)

Our prediction for RQ2 followed one view in the literature.
- **Fashion and herding.** Classic work on fads and informational cascades argues that ideas spread by imitation
  (Abrahamson; Bikhchandani and colleagues). That implies newcomers follow.
- **Outsider innovation.** Other work finds that new entrants bring new ideas. Azoulay and colleagues show that
  outsiders move into a field after a leading scientist dies prematurely, and their work is often highly cited. Foster and
  colleagues describe the tension between tradition and innovation.

On ML specifically, Koch and colleagues show that research concentrates on fewer benchmarks over time.

Studies like these face three measurement challenges, which we address:
1. survivorship, because usually only published papers are observed;
2. hindsight in how topics are defined;
3. forking paths, which we handle with pre-registration.

## Slide 6: Data and measurement (1:05)

Our corpus is 43,480 ICLR submissions from 2017 to 2026, taken from OpenReview. It includes accepted, rejected and
withdrawn papers, and a separate held-out split is reserved for replication.

Table 3 lists the measures.
- **Topics.** We embed each title and abstract with SPECTER2 and cluster the papers into 100 topics. These topics
  agree with ICLR's own area labels better than a keyword baseline, and the results hold with 75 or 150 topics.
- **Contribution type.** An LLM applies a fixed codebook: new method, benchmark or evaluation, empirical study,
  theory, or other. A blind second labelling pass agrees at kappa 0.93.
- **Newcomer paper.** None of the authors has an earlier ICLR submission in that topic. That's 73 percent of
  papers.
- **Acceptance** stayed sealed until the single registered run.

## Slide 7: Hindsight bias in topic maps (1:10)

Before the main results, one methodological finding.

69 percent of submissions are from 2024 to 2026. A topic map fitted on all years is therefore mostly a map of the
present.

Figure 1 shows the effective number of topics per year, a measure of diversity, under three maps that differ only
in which years they were fitted on.
- The **standard map**, in blue, suggests diversity rose almost every year.
- The map fitted on **2017–2020** papers, in green, peaks in 2020.
- The map fitted on **2024–2026** papers, in orange, peaks in 2025.

Each map finds peak diversity in the years used to fit it. So topic maps are not neutral preprocessing: the
fitting window shapes the history one observes.

## Slide 8: Consequence (0:55)

This matters for substantive conclusions.

First, the number of emerging topics, those that grew at least three-fold, is 8 under the early map but 29 under
the standard map.

Second, consider a lifecycle question: as a topic matures, does work shift from new methods towards benchmarks?
Figure 2 shows the same model on the same papers.
- Under the standard map, both estimates are essentially zero.
- Under the early map, they point towards a lifecycle: fewer new methods and more benchmarks.
- *(cut if short on time)* The pattern is stronger on papers written after the early map was fitted.

The early-map results are exploratory, but the lesson is clear. For that reason, every registered result must
also pass two hindsight checks.

## Slide 9: Empirical strategy (1:10)

Our models are linear probability models. The outcome is a 0/1 variable, such as whether a paper is a new-method
paper. The regressor of interest is, for example, whether it is a newcomer paper. We include topic and year fixed
effects; for RQ2 we use topic-by-year fixed effects, so each paper is compared only with papers from the same topic
in the same year. Standard errors are clustered by topic.

A hypothesis counts as supported only if:
- it has the predicted sign and a Holm-adjusted p below 0.05;
- at least 75 percent of the alternative specifications agree;
- both hindsight checks agree.

The protocol was pre-registered. We built every variable without seeing acceptance, tested the pipeline in 12,400
simulation runs, froze the code with hashes, and ran it once.

The simulation found something important. Under realistic no-effect data, standard clustered errors rejected up to
12.6 percent of the time instead of 5. So the RQ2 results get two extra checks.

## Slide 10: RQ1, foundation-model adoption and new architectures (0:55)

Now the results. Figure 3 shows the field-wide trends, but those are descriptive only.

The test is within topic, net of year effects. Does prior foundation-model adoption go with fewer new-architecture
papers?
- The coefficient is minus 0.08 for going from zero to full adoption, with a Holm-adjusted p of 0.001.
- All nine alternative specifications agree.

H1d is supported. In practical terms, a topic moving from 10 to 50 percent foundation-model adoption has about a
third fewer new-architecture papers, against a base rate of 9 percent.

## Slide 11: RQ2, newcomers and contribution types (1:15)

The RQ2 results went against our predictions. In Figure 4 the grey areas mark the predicted side, and both
estimates fall on the other side.
- Newcomer papers are 3.7 percentage points *more* likely to be new-method papers, on a base of 75 percent.
- They are 1.7 points *less* likely to be benchmark or evaluation papers, on a base of 7.7 percent. That's about a
  fifth fewer.

Both are significant with the wild cluster bootstrap. All ten alternative specifications agree, and so do both
extra checks.

These results are consistent with outsider innovation, not with herding.

One caveat: most of the benchmark gap goes with team size, because larger teams are more likely to include an
incumbent. The method gap does not depend on team size.

## Slide 12: Exploratory: title style (0:40)

One exploratory result, not pre-registered. Fashion also shows up in style.
- Branded titles rose more than fourfold.
- But, as the right panel shows, accepted papers carry them at the same rate as all submissions: the ratio is
  about one in every year.
- The rise appears with and without LLM-style wording in the abstract, so it is not only a writing-tool effect.

## Slide 13: RQ3, is following the fashion rewarded? (0:50)

Table 4 summarises the acceptance results.
- **Topic maturity (H3a).** The estimate is minus 1.7 points per log unit of prior papers. That is inconclusive:
  the test could only reliably detect effects of about 4 points.
- **Branded titles.** No premium.
- **New architectures where foundation models dominate.** Exploratory, but these papers are accepted relatively
  more often.

So we find no evidence that following the fashion is rewarded at review. If anything, going against the tide may
help, and that is a hypothesis for the replication.

## Slide 14: Contributions (0:40)

To summarise, three contributions.
1. **Methodological.** Topic maps fitted with hindsight can manufacture emerging topics and reverse trend
   conclusions. Early-year maps are a cheap check.
2. **Design.** A pre-registered, outcome-blind, simulation-checked, single-run protocol for science-of-science.
3. **Substantive.**
   - New architectures fade where foundation models spread.
   - Newcomer papers lean towards new methods, against the herding prediction.
   - Style follows fashions without a reward at review.

## Slide 15: Limitations and future work (0:35)

The main limitations:
- this is one venue;
- the results are associations, not causal effects;
- the labels come from an LLM: highly consistent, but not yet validated by humans.

Next, we will replicate the four key hypotheses on the held-out ICLR split, where they are already registered. We
will also extend the study to the ACL Anthology and validate the labels with human annotators.

## Slide 16: Thank you (0:05)

Thank you. I'm happy to take questions.
