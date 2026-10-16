# Talk script: "Following the Fashion?"

- **Length:** about 1,500 spoken words, about 12.5 minutes at a calm pace (120 words a minute). That leaves about
  2 minutes of buffer under the 15-minute limit.
- **Rehearsal:** time yourself once. If you run over 14 minutes, cut the sentences marked *(cut if short on
  time)*.
- **Questions:** see `qa.md`. Backup slides B1–B11 sit after the "Thank you" slide.

| Slide | Target | Ends by |
|---|---|---|
| 0 Title | 0:15 | 0:15 |
| 1 Waves | 0:55 | 1:10 |
| 2 Questions and traps | 1:10 | 2:20 |
| 3 Data | 1:10 | 3:30 |
| 4 Contribution 1: hindsight | 1:20 | 4:50 |
| 5 Hindsight changes conclusions | 1:10 | 6:00 |
| 6 Contribution 2: design | 1:10 | 7:10 |
| 7 Finding 1: foundation models | 1:00 | 8:10 |
| 8 Finding 2: newcomers | 1:20 | 9:30 |
| 9 Finding 3: title style | 0:45 | 10:15 |
| 10 Reward | 0:55 | 11:10 |
| 11 Contributions | 0:50 | 12:00 |
| 12 Next steps, thanks | 0:20 | 12:20 |

---

## Slide 0: Title (0:15)

Hi everyone, I'm [name]. Today I'll talk about research fashions in machine learning: how trends rise, who
drives them, and whether following them actually pays off.

## Slide 1: Machine learning moves in waves (0:55)

Let me start with three numbers from ICLR.

In 2017, about a quarter of all submissions proposed a new architecture. By 2026, it's eight percent.

Over the same years, papers that build on a foundation model went from almost zero to more than half of all
submissions.

And it's not only *what* we study, it's also *how we write*. Titles of the form "NAME, colon, subtitle", like
"BERT: something", went from nine to forty-one percent.

So machine learning clearly moves in waves. The question is whether these are *fashions*. Who starts them, who
follows them, and does following them pay off?

## Slide 2: Three questions, three measurement traps (1:10)

That gives us three research questions.

- **RQ1, rise:** when a fashion rises, what does it crowd out?
- **RQ2, following:** who brings new kinds of work into a topic, newcomers or the people already there?
- **RQ3, reward:** does following the fashion get your paper accepted?

These sound simple, but they are hard to measure, for three reasons.

- First, **survivorship**. Most studies only see published papers. We use every submission, including rejected
  and withdrawn ones.
- Second, **hindsight**. Topics are usually defined with today's view of the field. We also build topic maps from
  the early years only, to see the past as it looked at the time.
- Third, **forking paths**. With this much data, you can always find *something*. So we pre-registered our
  hypotheses and ran the confirmatory analysis exactly once.

## Slide 3: Data (1:10)

Our data are 43,480 ICLR submissions from 2017 to 2026, from OpenReview, accepted or not. A separate held-out
set is saved for replication.

For each paper we measure four things.

- **Its topic.** We embed the title and abstract with a scientific-paper encoder and cluster the papers into
  100 topics.
- **Its contribution type:** a new method, a benchmark, theory, and so on. An LLM labels it with a fixed codebook.
  A blind second labelling pass agrees with a kappa of 0.93.
- **Its authors.** We call a paper a *newcomer paper* if none of its authors has submitted to ICLR in that topic
  before. That's 73 percent of papers.
- **Acceptance**, which stayed sealed until the very last step.

One important point: all comparisons are *within the same topic and the same year*. We never compare an LLM paper
from 2025 with a GAN paper from 2018.

## Slide 4: Contribution 1, topic maps carry hindsight (1:20)

Now our first contribution, which is about measurement.

69 percent of ICLR submissions are from the last three years. So if you build a topic map from all years, which is
the standard thing to do, you get a map of *today's* field.

Here is what that does. The y-axis shows how many of the 100 topics are really in use each year. Think of it as
the field's diversity.

- The **blue** line is the standard map. Diversity rises steadily, and you would conclude: "ML is getting more
  diverse."
- The **green** line is a map built only from 2017–2020 papers. It says the field was most diverse in 2020.
- The **orange** map, built only from recent papers, peaks in 2025.

Each map says the field was most diverse exactly in the years it was built from. So the topic map is not neutral
preprocessing. It decides which past you see.

## Slide 5: …and hindsight changes the conclusions (1:10)

And this changes real conclusions.

Take "emerging topics", topics that grew at least three-fold. With the early map there are 8. With the standard
map, 29. Same papers.

Or take a classic question: do topics age? As a topic matures, do people shift from proposing new methods to
building benchmarks?

- With the standard map, the answer is no. Both estimates are basically zero.
- With the early map, on exactly the same papers and the same model, the answer becomes yes: fewer new methods,
  more benchmarks.
- *(cut if short on time)* It gets even stronger if we only use papers written after the map was built.

So "no lifecycle" becomes "lifecycle" just by changing the map. That's why, in our study, every trend result must
also hold on the prospective maps.

## Slide 6: Contribution 2, a design that keeps us from fooling ourselves (1:10)

Our second contribution is the design. Read the boxes from left to right.

1. We registered the hypotheses and the decision rule first.
2. We built every variable without looking at acceptance.
3. We tested the whole pipeline on 12,400 simulated datasets where we knew the true answer.
4. We froze the code with cryptographic hashes.
5. Then we ran the real analysis once, and we report every result, including the ones that didn't work out.

A claim needs all four conditions on the left: the predicted direction, a corrected p-value below 0.05, the same
direction in at least 75 percent of ten alternative analyses, and agreement on the prospective maps.

And the simulation was worth it, because it caught a real problem. In one realistic scenario, the standard
clustered standard errors gave 12.6 percent false positives instead of 5. So for every key result we report two
extra checks.

## Slide 7: Finding 1, foundation models crowd out new architectures (1:00)

Now the findings. First: foundation models crowd out new architectures.

On the left you see the overall trend. But a trend alone doesn't prove much, because lots of things change over
time.

So we look *within the same topic*. When more of last year's papers in a topic built on foundation models, does
that topic see fewer new architectures this year? Yes. Going from 10 to 50 percent foundation-model use goes with
about a third fewer architecture papers.

This was a pre-registered prediction. It is supported, and it holds in all nine alternative analyses. In plain
words: once a topic adopts foundation models, people stop designing their own architectures and build on top
instead.

## Slide 8: Finding 2, newcomers bring new methods, incumbents build benchmarks (1:20)

The second finding surprised us.

We predicted that newcomers would *follow*: they would enter a topic and write the safer kind of paper, such as
benchmarks and evaluations. Incumbents, who know the topic, would bring the new methods.

We found the opposite. Within the same topic and year:

- newcomer papers are 3.7 points *more* likely to propose a new method;
- and 1.7 points *less* likely to be a benchmark or evaluation paper. Only about 8 percent of papers are
  benchmarks, so that's about a fifth fewer.

The grey areas show where we predicted the results would be. Both land on the other side. The small tick marks are
the ten alternative analyses, and they all agree.

One honest caveat: the benchmark gap is partly about team size, because big teams are more likely to include an
incumbent. The method gap is not.

So the picture is: new people bring new methods, and established people build the shared infrastructure of their
field, the benchmarks.

## Slide 9: Finding 3, fashion in style, too (0:45)

Third, fashion isn't only about topics. It's also about style.

Branded titles quadrupled. But look at the right panel: accepted papers carry them at about the same rate as all
submissions, every year. A catchy name doesn't help you get in.

And it's not just LLMs writing our titles. The branded style rises strongly even in papers whose abstracts show
no sign of LLM writing.

## Slide 10: Does following the fashion pay off? (0:55)

So, does following the fashion pay off? We find no sign that it does.

- **Crowded topics** get no acceptance premium. If anything, it's slightly lower, but that estimate is not
  significant, and the test had limited power.
- **Branded titles:** no premium.
- **Against the tide**, interestingly: in topics dominated by foundation models, the few remaining architecture
  papers are accepted relatively *more* often. That one is exploratory, so take it as a hint, not a result.

The overall message: fashion spreads, but the review process does not visibly reward following it.

## Slide 11: Contributions (0:50)

To sum up, three contributions.

1. **A measurement warning, with a fix.** Topic maps built with hindsight invent emerging topics and can flip
   conclusions. Checking a prospective map is cheap.
2. **A rigorous template for science-of-science:** pre-registered, outcome-blind, simulation-checked, one frozen
   run.
3. **New evidence on research fashions:**
   - foundation models crowd out new architectures;
   - newcomers, not incumbents, bring new methods;
   - and style spreads like topics, without a reward.

The main limits: this is one venue; these are associations, not causes; and our labels come from an LLM. They are
highly consistent, but humans have not checked them yet.

## Slide 12: Next steps (0:20)

Next, we'll replicate the key results on the held-out ICLR papers, where the hypotheses are already registered.
We'll also extend the study to ACL and add a human check of the labels.

Thank you. I'm happy to take questions.
