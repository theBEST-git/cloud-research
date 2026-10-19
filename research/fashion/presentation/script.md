# Talk script: "Riding the Wave?"

- **Length:** about 1,530 spoken words, about 12:50 at a calm pace (120 words a minute). The timing table below is
  computed from each slide's word count, rounded up to the next 5 seconds; it ends at 13:30. Numbers take longer to
  say than their word count suggests (about 90 extra spoken words, about 0:45), and each slide change costs 1–2
  seconds (about 0:30 in all), so expect about 13:50–14:10 in practice: a real buffer of about 0:50–1:10 under the
  strict 15:00 limit.
- **Rehearsal:** time yourself once. If you run over 14 minutes, cut the sentences marked *(cut if short on time)*
  first (about 30 words, about 0:15), then shorten slide 5 (related work) and slide 7 (hindsight).
- **Held-out wording (use it every time):** the held-out papers are the released former confirmation split, which this
  study had never analysed: a pre-registered out-of-sample replication, not a certified untouched holdout. Say "goes
  with", never "causes", "helps" or "penalises". A null is "no detectable" association; an underpowered null is
  "uninformative".
- **Questions:** see `qa.md`. Appendix slides A1–A19 and the references come after the "Thank you" slide.

| Slide | Words | Target | Ends by |
|---|---|---|---|
| 1 Title | 29 | 0:15 | 0:15 |
| 2 Outline | 7 | 0:05 | 0:20 |
| 3 Motivation | 88 | 0:45 | 1:05 |
| 4 Research questions and pre-registered hypotheses | 96 | 0:50 | 1:55 |
| 5 Related work and positioning | 62 | 0:35 | 2:30 |
| 6 Data and measurement | 111 | 1:00 | 3:30 |
| 7 Hindsight bias in topic maps | 102 | 0:55 | 4:25 |
| 8 Consequence | 100 | 0:50 | 5:15 |
| 9 Empirical strategy | 83 | 0:45 | 6:00 |
| 10 RQ1, foundation-model adoption and new architectures | 88 | 0:45 | 6:45 |
| 11 RQ2, newcomers and contribution types | 102 | 0:55 | 7:40 |
| 12 RQ3, is following the fashion rewarded? | 64 | 0:35 | 8:15 |
| 13 Far jumps go with lower acceptance (post hoc, replicated) | 133 | 1:10 | 9:25 |
| 14 Why do some areas lose favour? (post hoc) | 156 | 1:20 | 10:45 |
| 15 Do the results hold on held-out papers? | 99 | 0:50 | 11:35 |
| 16 Contributions | 85 | 0:45 | 12:20 |
| 17 Limitations and future work | 59 | 0:30 | 12:50 |
| 18 Thank you | 7 | 0:05 | 12:55 |

---

## Slide 1: Title

Good morning, everyone. I'm [name]. I'll present a study of research fashions in machine learning: how trends rise,
who drives them, whether following goes with acceptance, and what replicates.

## Slide 2: Outline

Here is the plan for the talk.

## Slide 3: Motivation

Table 1 shows three shifts at ICLR between 2017 and 2026.
- The share of submissions proposing a new architecture fell from 24 to 8 percent.
- The share building on a foundation model rose from almost zero to 54 percent.
- Titles of the form "NAME, colon, subtitle" rose from 9 to 41 percent.

So ML research moves in waves, in what is studied and in how it is presented. Our question is whether these are
fashions, and if so: what they displace, who drives them, and whether followers are rewarded.

## Slide 4: Research questions and pre-registered hypotheses

This gives three research questions. The table shows the key hypothesis for each; all ten are in Appendix A1.

- **RQ1, rise.** H1d predicts that when more of a topic's papers build on foundation models, fewer of its papers
  propose new architectures.
- **RQ2, following.** We predicted that newcomer papers would be *less* often new-method papers and *more* often
  benchmark or evaluation papers. In other words, newcomers imitate and insiders innovate.
- **RQ3, reward.** H3a predicts that papers in more mature, crowded topics are accepted less often.

All of these were registered before any test of them was run.

## Slide 5: Related work and positioning

Our RQ2 prediction followed one view in the literature.
- **Fashion and herding** work argues that ideas spread by imitation, so newcomers follow.
- **Outsider innovation** work finds the opposite: outsiders who enter a field often bring new ideas.

Studies like these face three measurement challenges, which we address: survivorship, hindsight in how topics are
defined, and forking paths, which we handle with pre-registration.

## Slide 6: Data and measurement

Our discovery corpus is 43,480 ICLR submissions from 2017 to 2026, including rejected and withdrawn papers. We then
tested the results on 11,099 held-out papers, the released former confirmation split, which we had never analysed: a
pre-registered out-of-sample replication, not a certified untouched holdout.

- **Topics.** We embed titles and abstracts with SPECTER2 and cluster them into 100 topics; held-out papers go on the
  frozen maps.
- **Contribution type.** An LLM applies a fixed codebook; a blind second pass agrees at kappa 0.93 in both splits.
- **Newcomer paper.** No author has an earlier ICLR submission in that topic: 73 percent of papers.
- **Acceptance** stayed sealed in code until each split's single registered run.

## Slide 7: Hindsight bias in topic maps

69 percent of submissions are from 2024 to 2026, so a topic map fitted on all
years is mostly a map of the present.

Figure 1 shows diversity per year under three maps that differ only in their fitting years.
- The **standard map**, in blue, suggests diversity rose almost every year.
- The map fitted on **2017–2020** papers, in green, peaks in 2020.
- The map fitted on **2024–2026** papers, in orange, peaks in 2025.

Each map finds peak diversity in the years used to fit it. *(Cut if short on time: Topic maps are not neutral
preprocessing; the fitting window shapes the history one observes.)*

## Slide 8: Consequence

This changes substantive conclusions.
- The number of emerging topics is 8 under the early map, but 29 under the standard map.
- On the standard map, small topic size seems to predict two-year growth, with an R-squared of 0.28; on the early
  map it predicts nothing. The hindsight map lets the future leak in.
- Do topics age, from new methods towards benchmarks? With the same model on the same papers, the standard map says
  no. The early map points towards a lifecycle.

The early-map results are exploratory, but the lesson is clear. Every registered result must also pass two
hindsight checks.

## Slide 9: Empirical strategy

We use linear probability models: a 0/1 outcome, topic and year fixed effects, topic-by-year cells for RQ2, and
standard errors clustered by topic.

A hypothesis counts as supported only if it has the predicted sign and a Holm-adjusted p below 0.05, at least 75
percent of the alternative specifications agree, and both hindsight checks agree.

The protocol was pre-registered, frozen with hashes and run once. The held-out tests were registered before the run:
one-sided at alpha 0.05, with frozen code and topic maps.

## Slide 10: RQ1, foundation-model adoption and new architectures

Now the results. Within topic, net of year effects: does prior foundation-model adoption go with fewer
new-architecture papers?

Yes. In discovery, the coefficient is minus 0.08 for going from no adoption to full adoption, with a Holm-adjusted p
of 0.001, and all nine alternative specifications agree. In discovery, topics at 50 percent adoption have about a
third fewer new-architecture papers than topics at 10 percent.

On the held-out papers, the estimate is minus 0.11, with a one-sided p of 0.001: the same direction. H1d is supported
and replicated.

## Slide 11: RQ2, newcomers and contribution types

The RQ2 results went against our predictions. The grey areas mark the predicted side, and both discovery estimates
fall on the other side.
- Newcomer papers are 3.7 percentage points *more* likely to be new-method papers.
- They are 1.7 points *less* likely to be benchmark or evaluation papers. That's about a fifth fewer.

Before the held-out run, we registered the reversed predictions. Both held: plus 3.6 and minus 2.1 points, each with
a one-sided Holm p of 0.001.

This is consistent with outsider innovation, not with herding. One caveat: most of the benchmark gap goes with team
size. The method gap does not.

## Slide 12: RQ3, is following the fashion rewarded?

For acceptance:
- **Crowded topics.** Inconclusive: minus 1.7 points per log unit of prior papers in discovery and minus 1.5 on the
  held-out papers. Neither test could detect effects smaller than about 4 to 5 points.
- **Branded titles.** No premium.
- **Against the tide.** Where foundation models dominate, new-architecture papers do relatively better. This is
  exploratory.

So we find no detectable reward for following the fashion.

## Slide 13: Far jumps go with lower acceptance (post hoc, replicated)

One post hoc finding replicated clearly. For teams with an experienced author, we measure how close a paper is to
that author's earlier ICLR work.

Panel (a): in discovery, adjusted acceptance rises from about 40 percent for the farthest fifth to about 47 for the
closest; a far jump versus the median is minus 5.4 points.

Panel (b): on the held-out papers it is minus 6.1, with a confidence interval from minus 9.3 to minus 2.9. Within the
same author, closer papers also go with higher acceptance, in both splits.

The novelty floor did not replicate: minus 3.3 points in discovery, minus 0.1 held-out. That test was too weak to say
whether a 3-point gap exists, so we no longer claim it.

These are associations: co-author choice and failed projects are not controlled.

## Slide 14: Why do some areas lose favour? (post hoc)

This slide is post hoc. We compared each author keyword's acceptance with all other papers of the same year.
- Areas differ by about plus or minus 10 points. Generative and pre-training work sits above; maturing areas such as
  CNNs, image classification and federated learning sit below.
- Why would an area fall? We checked three explanations on the clearest case, federated learning, at minus 11
  points. Weaker authors moving in? No: its authors actually became more established. The field moving on? Yes: its
  share of submissions peaked in 2023 and has fallen to about a third of that. A higher bar for a cooling area? That
  fits: since 2023 its papers were accepted 11 to 15 points less often every year.
- To be careful: no single area survives correction for 68 comparisons, and on the held-out papers area edges
  persist but shrink, while the federated-learning gap points the same way but is not confirmed.

## Slide 15: Do the results hold on held-out papers?

Here is the full held-out picture: the released former confirmation split, which we had never analysed, with every
test registered before the single run. The source does not certify these papers as untouched, so this is an
out-of-sample replication.
- **Replicated:** foundation models and architectures, both newcomer results, and the far-jump gap.
- **Not replicated:** the novelty floor.
- **Not confirmed:** federated learning.
- **Inconclusive:** crowded topics.

Daggers mark tests too weak to tell either way, including those last three. *(Cut if short on time: Of the six
secondary tests, five held; the within-author novelty slope did not, nor did the federated-learning trend.)*

## Slide 16: Contributions

To summarise, three contributions.
1. **Methodological.** Topic maps fitted with hindsight can manufacture emerging topics and reverse trend
   conclusions. Early-year maps are a cheap check.
2. **Design.** A pre-registered, single-run protocol, now with a registered held-out replication.
3. **Substantive.** New architectures fade where foundation models spread, newcomer papers lean towards new methods,
   and far jumps from a team's own record go with lower acceptance; all three replicated. The novelty floor did not,
   though that test was too weak to tell; federated learning is not confirmed; crowding stays inconclusive.

## Slide 17: Limitations and future work

The main limitations: one venue; associations, not causes; LLM labels; camera-ready text, checked in discovery but
not on the held-out papers; and a released former holdout, not a certified untouched one. The pooled re-run in the
appendix is exploratory and confirms nothing.

Next: a prospective test on future ICLR years, the ACL Anthology, and human validation of the labels.

## Slide 18: Thank you

Thank you. I'm happy to take questions.
