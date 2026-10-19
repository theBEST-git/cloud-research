# Talk script: "Riding the Wave?"

- **Speaker:** Minghan Li (supervisor: A/Prof Jianzhong Qi).
- **Length:** about 1,020 spoken words, about 8:30 at a calm pace (120 words a minute). The timing table below is
  computed from each slide's word count, rounded up to the next 5 seconds; it ends at 9:00. Numbers take longer to
  say than their word count suggests, and each slide change costs 1–2 seconds, so expect about 9:30–10:00 in
  practice: about 5 minutes of buffer under the strict 15:00 limit, enough to slow down on the figures (slides 7,
  8, 10 and 11) or take a question during the talk.
- **Revised after supervisor feedback:** the far-jump and area slides were cut, and every slide keeps only its key
  point. Their material is in `qa.md` for questions.
- **Held-out wording (use it every time):** the held-out papers are the released former confirmation split, which this
  study had never analysed: a pre-registered out-of-sample replication, not a certified untouched holdout. Say "goes
  with", never "causes", "helps" or "penalises". A null is "no detectable" association; an underpowered null is
  "uninformative".
- **Questions:** see `qa.md`. The references are the last page, after the "Thank you" slide.

| Slide | Words | Target | Ends by |
|---|---|---|---|
| 1 Title | 43 | 0:25 | 0:25 |
| 2 Outline | 7 | 0:05 | 0:30 |
| 3 Motivation | 84 | 0:45 | 1:15 |
| 4 Research questions and hypotheses | 66 | 0:35 | 1:50 |
| 5 Related work and positioning | 59 | 0:30 | 2:20 |
| 6 Data and measurement | 107 | 0:55 | 3:15 |
| 7 Hindsight bias in topic maps | 88 | 0:45 | 4:00 |
| 8 Consequence | 64 | 0:35 | 4:35 |
| 9 Empirical strategy | 87 | 0:45 | 5:20 |
| 10 RQ1, where foundation models spread, new architectures fade | 67 | 0:35 | 5:55 |
| 11 RQ2, newcomers bring new methods | 67 | 0:35 | 6:30 |
| 12 RQ3, is following the fashion rewarded? | 68 | 0:35 | 7:05 |
| 13 Do the results hold on held-out papers? | 85 | 0:45 | 7:50 |
| 14 Contributions | 64 | 0:35 | 8:25 |
| 15 Limitations and future work | 49 | 0:25 | 8:50 |
| 16 Thank you | 20 | 0:10 | 9:00 |

---

## Slide 1: Title

Good morning, everyone. I'm Minghan Li, and this work is supervised by A/Prof Jianzhong Qi. I'll present a study of
research fashions in machine learning: how trends rise, who drives them, whether following them goes with
acceptance, and what replicates on held-out papers.

## Slide 2: Outline

Here is the plan for the talk.

## Slide 3: Motivation

The table shows three shifts at ICLR between 2017 and 2026.
- The share of submissions proposing a new architecture fell from 24 to 8 percent.
- The share building on a foundation model rose from almost zero to 54 percent.
- Titles of the form "NAME, colon, subtitle" rose from 9 to 41 percent.

So research moves in waves, in what is studied and in how it is presented. Are these fashions? And if so, what do
they displace, who drives them, and are followers rewarded?

## Slide 4: Research questions and hypotheses

This gives three research questions, each with a key prediction.
- **RQ1:** when more of a topic's papers build on foundation models, fewer of them propose new architectures.
- **RQ2:** we predicted that newcomers imitate, so their papers would less often propose new methods and more often
  be benchmark papers.
- **RQ3:** papers in crowded topics are accepted less often.

We wrote all predictions down before running any test.

## Slide 5: Related work and positioning

Our RQ2 prediction followed one view in the literature: fashion and herding, where ideas spread by imitation, so
newcomers follow. The other view is outsider innovation: new entrants bring new ideas.

Compared with earlier meta-research on machine learning, we add three things: all submissions, not only accepted
papers; topics defined without hindsight; and registered tests, with a held-out replication.

## Slide 6: Data and measurement

Our data are an integrated, curated ICLR corpus: our own OpenReview collection, reconciled with existing archives,
namely Paper Copilot, Re-squared and Louis's ICLR archive. It holds 43,480 submissions from 2017 to 2026, including
rejected and withdrawn papers, plus 11,099 held-out papers for the replication.
- **Topics:** we embed titles and abstracts with SPECTER2 and cluster them into 100 topics. With 75 or 150 topics,
  the results agree.
- **Contribution type:** an LLM with a fixed codebook; a blind second pass agrees at kappa 0.93.
- **Newcomer paper:** no author has an earlier ICLR submission in that topic. That's 73 percent of papers.
- **Acceptance** stayed locked until the single registered run.

## Slide 7: Hindsight bias in topic maps

Before the results, one methodological finding. A topic map is the set of 100 topic clusters, fitted on papers from
chosen years; every paper is then assigned to its nearest topic.

The figure shows topic diversity per year under three maps that differ only in their fitting years. Each map finds
peak diversity in the years it was fitted on. The all-years map, in blue, is dominated by recent papers: 69 percent
of submissions are from 2024 to 2026. So the fitting window shapes the history one sees.

## Slide 8: Consequence

This changes conclusions.
- The number of emerging topics is 8 on the 2017–20 map, but 29 on the all-years map.
- Do topics age, moving from new methods towards benchmarks? With the same papers and the same model, the all-years
  map says no and the 2017–20 map says yes.

So every registered result must also hold on the 2017–20 map and on a year-balanced map.

## Slide 9: Empirical strategy

We use linear probability models: a 0/1 outcome, such as paper type or acceptance, with topic and year fixed
effects, so papers are compared within the same topic and year. Standard errors are clustered by topic.

A hypothesis counts as supported only if it has the predicted sign with a Holm-adjusted p below 0.05, at least 75
percent of the alternative specifications agree, and both hindsight checks agree. Everything was registered in
advance and run once with frozen code; the held-out tests were registered before their run.

## Slide 10: RQ1, where foundation models spread, new architectures fade

Now the results. The figure shows the field-wide trends.

Within topic and year, going from no foundation-model adoption to full adoption goes with 8 points fewer
new-architecture papers in discovery, and 11 points fewer on the held-out papers. Both intervals exclude zero. In
plain terms, topics at 50 percent adoption have about a third fewer new-architecture papers than topics at 10
percent. H1d is supported and replicated.

## Slide 11: RQ2, newcomers bring new methods

RQ2 went against our prediction. The grey areas mark the predicted side, and both estimates fall on the other side.
Newcomer papers are 3.7 points *more* likely to be method papers and 1.7 points *less* likely to be benchmark papers.

Before the held-out run, we registered the reversed predictions, and both held: plus 3.6 and minus 2.1 points. This
is consistent with outsider innovation, not with herding.

## Slide 12: RQ3, is following the fashion rewarded?

For acceptance:
- **Crowded topics:** minus 1.7 points per log unit of prior papers in discovery, and minus 1.5 on held-out papers.
  Neither test could detect effects below about 4 to 5 points, so this is inconclusive.
- **Branded titles** carry no premium.
- **Against the tide:** new-architecture papers in topics dominated by foundation models do relatively better. This
  is exploratory.

So we find no detectable reward for following the fashion.

## Slide 13: Do the results hold on held-out papers?

Here is the replication in one table. The held-out papers come from a released former test split that we had never
analysed, and every test was registered before one run. The source does not certify them as untouched, so we call
this an out-of-sample replication.

Three of the four key results replicated; crowding stays inconclusive, as the dagger marks. We also registered post
hoc tests from discovery. For example, far jumps from a team's own past work go with lower acceptance, and that
replicated too.

## Slide 14: Contributions

To summarise, three contributions.
1. **Method:** topic maps fitted with hindsight can manufacture trends; an early-year map is a cheap check.
2. **Design:** a registered, outcome-blind, single-run protocol, with a held-out replication.
3. **Findings,** all associations: where foundation models spread, new architectures fade, and newcomers lean
   towards new methods, not imitation; both replicated. And we find no detectable acceptance reward for following
   the fashion.

## Slide 15: Limitations and future work

The main limitations: one venue; associations, not causes; LLM labels that are consistent but not yet
human-validated; held-out papers that are not certified untouched; and a 2021 author-ID change that undercounts
incumbents.

Next: a prospective test on future ICLR submissions, the ACL Anthology, and human validation of the labels.

## Slide 16: Thank you

Thank you, and many thanks to my supervisor, A/Prof Jianzhong Qi, for guidance and feedback. I'm happy to take
questions.
