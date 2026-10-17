# Talk script: "Following the Fashion?"

- **Length:** about 1,420 spoken words, about 12 minutes at a calm pace (120 words a minute). The timing table
  allows 13:00, which leaves 2 minutes of buffer under the 15-minute limit.
- **Rehearsal:** time yourself once. If you run over 14 minutes, cut the sentences marked *(cut if short on
  time)* first, then shorten slide 12 (title style).
- **Questions:** see `qa.md`. Appendix slides A1–A12 and the references come after the "Thank you" slide.

| Slide | Target | Ends by |
|---|---|---|
| 1 Title | 0:15 | 0:15 |
| 2 Outline | 0:05 | 0:20 |
| 3 Motivation | 0:45 | 1:05 |
| 4 Research questions and hypotheses | 0:50 | 1:55 |
| 5 Related work | 0:45 | 2:40 |
| 6 Data and measurement | 0:55 | 3:35 |
| 7 Hindsight bias in topic maps | 1:05 | 4:40 |
| 8 Consequence | 0:50 | 5:30 |
| 9 Empirical strategy | 1:00 | 6:30 |
| 10 RQ1 | 0:50 | 7:20 |
| 11 RQ2 | 1:10 | 8:30 |
| 12 Exploratory: title style | 0:25 | 8:55 |
| 13 RQ3 | 0:40 | 9:35 |
| 14 Which areas are accepted more or less often? | 0:55 | 10:30 |
| 15 Why is federated learning falling out of favour? | 1:15 | 11:45 |
| 16 Contributions | 0:40 | 12:25 |
| 17 Limitations and future work | 0:30 | 12:55 |
| 18 Thank you | 0:05 | 13:00 |

---

## Slide 1: Title (0:15)

Good morning, everyone. I'm [name]. Today I'll present a study of research fashions in machine learning: how
trends rise, who drives them, and whether following them pays off at review.

## Slide 2: Outline (0:05)

Here is the plan for the talk.

## Slide 3: Motivation (0:45)

Table 1 shows three shifts at ICLR between 2017 and 2026.
- The share of submissions proposing a new architecture fell from 24 to 8 percent.
- The share building on a foundation model rose from almost zero to 54 percent.
- Titles of the form "NAME, colon, subtitle" rose from 9 to 41 percent.

So ML research moves in waves, in what is studied and in how it is presented. Our question is whether these are
fashions, and if so: what they displace, who drives them, and whether followers are rewarded.

## Slide 4: Research questions and pre-registered hypotheses (0:50)

This gives three research questions. The table shows the key hypothesis for each; all ten are in Appendix A1.

- **RQ1, rise.** H1d predicts that when more of a topic's papers build on foundation models, fewer of its papers
  propose new architectures.
- **RQ2, following.** We predicted that newcomer papers would be *less* often new-method papers and *more* often
  benchmark or evaluation papers. In other words, newcomers imitate and insiders innovate.
- **RQ3, reward.** H3a predicts that papers in more mature, crowded topics are accepted less often.

All of these were registered before any analysis.

## Slide 5: Related work and positioning (0:45)

Our RQ2 prediction followed one view in the literature.
- **Fashion and herding** work argues that ideas spread by imitation, which implies that newcomers follow.
- **Outsider innovation** work finds the opposite. Azoulay and colleagues show that outsiders move into a field after
  a leading scientist dies, and their work is often highly cited.

Studies like these face three measurement challenges, which we address:
1. survivorship, because usually only published papers are observed;
2. hindsight in how topics are defined;
3. forking paths, which we handle with pre-registration.

## Slide 6: Data and measurement (0:55)

Our corpus is 43,480 ICLR submissions from 2017 to 2026, taken from OpenReview. It includes accepted, rejected and
withdrawn papers, and a held-out split is reserved for replication.

- **Topics.** We embed each title and abstract with SPECTER2 and cluster the papers into 100 topics. These topics
  match ICLR's own area labels better than a keyword baseline.
- **Contribution type.** An LLM applies a fixed codebook. A blind second labelling pass agrees at kappa 0.93.
- **Newcomer paper.** None of the authors has an earlier ICLR submission in that topic. That's 73 percent of
  papers.
- **Acceptance** stayed sealed until the single registered run.

## Slide 7: Hindsight bias in topic maps (1:05)

First, a methodological finding. 69 percent of submissions are from 2024 to 2026, so a topic map fitted on all
years is mostly a map of the present.

Figure 1 shows a measure of diversity per year, under three maps that differ only in which years they were fitted
on.
- The **standard map**, in blue, suggests diversity rose almost every year.
- The map fitted on **2017–2020** papers, in green, peaks in 2020.
- The map fitted on **2024–2026** papers, in orange, peaks in 2025.

Each map finds peak diversity in the years used to fit it. Topic maps are not neutral preprocessing: the fitting
window shapes the history one observes.

## Slide 8: Consequence (0:50)

This changes substantive conclusions.
- The number of emerging topics is 8 under the early map, but 29 under the standard map.
- Do topics age, from new methods towards benchmarks? With the same model on the same papers, the standard map
  says no: both estimates are essentially zero. The early map points towards a lifecycle.

The early-map results are exploratory, but the lesson is clear. Every registered result must also pass two
hindsight checks.

## Slide 9: Empirical strategy (1:00)

We use linear probability models. The outcome is a 0/1 variable, such as whether a paper is a new-method paper. We
include topic and year fixed effects; for RQ2 we use topic-by-year cells. Standard errors are clustered by topic.

A hypothesis counts as supported only if:
- it has the predicted sign and a Holm-adjusted p below 0.05;
- at least 75 percent of the alternative specifications agree;
- both hindsight checks agree.

The protocol was pre-registered, tested on 12,400 simulation runs, frozen with hashes and run once. The simulation
also showed that standard clustered errors can give up to 12.6 percent false positives instead of 5, so the RQ2
results get two extra checks.

## Slide 10: RQ1, foundation-model adoption and new architectures (0:50)

Now the results. The test for RQ1 is within topic, net of year effects. Does prior foundation-model adoption go
with fewer new-architecture papers?

Yes. The coefficient is minus 0.08 for going from no adoption to full adoption, with a Holm-adjusted p of 0.001,
and all nine alternative specifications agree. In practical terms, a topic moving from 10 to 50 percent
foundation-model adoption has about a third fewer new-architecture papers. H1d is supported.

## Slide 11: RQ2, newcomers and contribution types (1:10)

The RQ2 results went against our predictions. The grey areas mark the predicted side, and both estimates fall on
the other side.
- Newcomer papers are 3.7 percentage points *more* likely to be new-method papers.
- They are 1.7 points *less* likely to be benchmark or evaluation papers. That's about a fifth fewer.

Both are significant with the wild cluster bootstrap, and all ten alternative specifications agree. This is
consistent with outsider innovation, not with herding.

One caveat: most of the benchmark gap goes with team size. The method gap does not.

## Slide 12: Exploratory: title style (0:25)

One exploratory result on style. Branded titles rose more than fourfold, but accepted papers carry them at the same
rate as all submissions. The rise appears with and without LLM-style wording in the abstract.

## Slide 13: RQ3, is following the fashion rewarded? (0:40)

For acceptance:
- **Crowded topics.** The registered test is inconclusive: minus 1.7 points per log unit of prior papers, and the
  test could only detect effects of about 4 points.
- **Branded titles.** No premium.
- **Against the tide.** Where foundation models dominate, new-architecture papers do relatively better. This is
  exploratory.

So we find no evidence that following the fashion is rewarded.

## Slide 14: Which areas are accepted more or less often? (0:55)

The next two slides are post hoc. We declared the analysis before running it, but it was prompted by an earlier
keyword grid.

We screened 68 author keywords and 100 topics. For each area, we compare its papers' acceptance with all other
papers from the same year.
- Areas differ by about plus or minus 10 points. Generative and pre-training work sits above average. Federated
  learning, CNNs and image classification sit below.
- Federated learning is low under *both* definitions: minus 11 points as a keyword and minus 14 as a topic, each
  with p = 0.005.
- To be precise: after correcting for 68 comparisons, with a conservative test, no single area is significant on
  its own.

## Slide 15: Why is federated learning falling out of favour? (1:15)

So why is federated learning falling? We proposed three explanations and checked each against the data.
- **An influx of inexperienced authors?** No. FL authors became *more* established over time: the share of papers
  with an author who already had an accepted ICLR paper went from 4 to about 60 percent. Paper type and team size
  were stable, and adjusting for them leaves most of the decline.
- **The field moved on?** Yes. Panel (a) shows that FL's share of submissions peaked in 2023 at 3.2 percent and
  has fallen to 1.1 percent.
- **FL papers judged more harshly?** Consistent with the data. Panel (b) shows that since 2023, FL papers have been
  accepted 11 to 15 points less often than other papers every year. The decline appears in every author group,
  although each group alone is too small to be significant.

So our reading is that the community has cooled on federated learning. Authors are leaving, and the papers that
remain do worse at review, and this is not because of who writes them. Scepticism about the area's research value
fits the data, but we cannot observe reviewers' reasons. We have registered this result for replication on the
held-out papers.

## Slide 16: Contributions (0:40)

To summarise, three contributions.
1. **Methodological.** Topic maps fitted with hindsight can manufacture emerging topics and reverse trend
   conclusions. Early-year maps are a cheap check.
2. **Design.** A pre-registered, outcome-blind, simulation-checked, single-run protocol.
3. **Substantive.**
   - New architectures fade where foundation models spread.
   - Newcomer papers lean towards new methods.
   - Following fashions is not rewarded, and an area like federated learning can fall out of favour as the field
     moves on.

## Slide 17: Limitations and future work (0:30)

The main limitations:
- this is one venue;
- the results are associations;
- the labels come from an LLM.

Next, we will replicate the registered hypotheses on the held-out ICLR split, extend the study to the ACL Anthology,
and validate the labels with human annotators.

## Slide 18: Thank you (0:05)

Thank you. I'm happy to take questions.
