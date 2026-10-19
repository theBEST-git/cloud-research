# Q&A preparation

Short answers first. Use the "If pushed" line only if they ask a follow-up. Appendix slides are A1–A19 (A19: federated-learning worked example): A9–A11 title
style, A12 definitions, A13 the earlier keyword grid, A14 held-out data, rules and power, A15 team experience (H1
held-out), A16 keyword timing, A17 topic edges out of sample, A18 the pooled re-run (exploratory).

**Three habits that keep answers safe:**
- Say "goes with" or "is associated with", never "causes".
- If you don't know, say "we didn't test that; it's a good next step."
- Point to a backup slide when a number helps.
- Held-out wording: "the released former confirmation split, which we had never analysed: a pre-registered
  out-of-sample replication, not a certified untouched holdout." Underpowered nulls are "uninformative", not "no
  effect".

---

## 0. Related work (slide 5)

Know one sentence per paper. If someone knows a paper better than you, agree and return to what *your* data
show.

| Paper | One-sentence summary | How it relates to us |
|---|---|---|
| Abrahamson (1991) | Management practices spread as fads and fashions through imitation, not only on merit | The fashion view behind our registered RQ2 prediction |
| Bikhchandani, Hirshleifer & Welch (1992) | Informational cascades: people copy earlier choices and ignore their own information | Also predicts that newcomers follow |
| Azoulay, Fons-Rosen & Graff Zivin (2019) | After a star scientist dies prematurely, outsiders enter the field, and their papers are often highly cited | Outsider innovation, which our RQ2 result is consistent with |
| Foster, Rzhetsky & Evans (2015) | Scientists face a trade-off: tradition is safer, innovation is riskier but sometimes highly rewarded | Background on the tradition vs. innovation tension |
| Wu, Wang & Evans (2019) | Large teams tend to develop existing ideas; small teams tend to disrupt | Fits our team-size caveat: larger teams write more benchmarks |
| Koch, Denton, Hanna & Foster (2021) | ML research concentrates on fewer benchmark datasets over time, often borrowed from other tasks | Context for benchmark papers as shared infrastructure |
| Birhane et al. (2022) | Highly cited ML papers mostly value performance and generalisation | Context on what ML rewards |
| Gelman & Loken (2014) | The "garden of forking paths": many possible analyses make false findings easy | Why we pre-registered |
| Nosek et al. (2018) | Pre-registration separates confirmatory from exploratory analysis | Our protocol |
| Singh et al. (2023) | SciRepEval benchmark; it introduced the SPECTER2 embeddings we use | Our topic embeddings |
| Cameron, Gelbach & Miller (2008) | The wild cluster bootstrap for inference with few clusters | Our registered p-value method for RQ2 |

*[Before the talk, open each reference once to confirm the details.]*

**What is new compared with this literature?**
Three things together:
- the full submission pool, including rejected papers;
- an explicit test of hindsight in topic definitions;
- a pre-registered, single-run design.

Substantively, we test the herding view against the outsider view on ML papers, and the data favour the outsider
view.

**Isn't "newcomers bring new methods" just Azoulay et al. again?**
It is consistent with them, but the setting differs. They study entry after a star's death in the life sciences
and measure citations. We study all ICLR submissions and measure the *type* of contribution. Agreement across such
different settings is useful.

## 1. Data and measurement

**Why ICLR?**
ICLR is one of the few major ML venues that has published its submissions, including rejected and withdrawn ones,
on OpenReview for ten years. That lets us avoid survivorship bias. The cost is that it's one venue. ACL is next.

**How were the topics built? Why 100?**
We embedded each title and abstract with SPECTER2, a model trained on scientific papers, and clustered the papers
into 100 groups. We re-ran everything with 75 and 150 topics, and the main results hold. (A4)
- *If pushed on quality:* the topics agree with ICLR's own area labels better than a keyword baseline (NMI 0.30 vs.
  0.27). From a paper's title and abstract, a blind checker picked its topic 80% of the time at the 100-topic level,
  and 61% among the 198 finer topics, where chance is 10%.

**Can you trust LLM labels for contribution type?**
They are very consistent: a blind second pass agrees at kappa 0.93. But the reference labels were also made by an
LLM, so this shows consistency, not human-level validity. A human check is our next step. (A4)
- *If pushed:* for label errors to create the newcomer result, they would have to differ between newcomer and
  incumbent papers. Correcting for the measured error rates makes the result slightly *larger*, not smaller.

**How do you know who is a newcomer?**
From OpenReview author IDs. A paper is a newcomer paper if none of its authors submitted to ICLR in that topic
before, whatever the outcome.
- *If pushed:* ICLR changed its ID system in 2021, so some experienced authors look new. That mixes the two groups,
  which should push estimates *towards zero*; our registration assumes this. Dropping 2021–22 gives the same
  results, though later years still undercount incumbents.

**Newcomer to ML, or just to ICLR?**
Newcomer to that topic at ICLR. A senior person from another field or venue can count as a newcomer. We can't see
other venues, which is a limitation.

**What counts as "building on a foundation model"?**
The paper uses or adapts a large pre-trained model, such as an LLM, CLIP or a pre-trained diffusion model. This
label comes from the same LLM codebook.

**What is a "benchmark & evaluation" paper?**
A paper whose main contribution is a dataset, a benchmark, or an evaluation of existing methods. It's about 8% of
papers.

## 2. Hindsight (Contribution 1)

**Isn't the early map just worse for recent papers? Which map is right?**
Neither is "right", and that's the point. Each map fits its own era best. A result about change over time should
not depend on which era defines the topics, so we require it to hold on both. The early map is what a researcher
in 2020 would have seen. It uses no future information.

**Is this new? People know about topic drift.**
Topic drift is known, and there are dynamic topic models. But many trend studies still fit one map on all years and
read trends off it. Our contribution is to show, on a large corpus, how much that changes concrete conclusions, and
to give a cheap check: also fit a map on the early years.

**So do topics age or not?**
We don't claim either. By our pre-registered rule it is "not supported", because the main map shows nothing. The
lesson is that the answer depends on the map.

**What is "topics in real use"?**
The effective number of topics: it's 100 if papers are spread evenly over all 100 topics, and lower if they bunch
up in a few. It measures diversity.

## 3. Design and statistics (Contribution 2)

**You already had the data. What does pre-registration buy you?**
We registered before the full-corpus labels existed and before any registered test was run. For those tests,
acceptance stayed sealed in code: only one file could read it, and that file refused to run unless the frozen code
matched its hashes. Then we ran it once, in 18 seconds, and report everything. To be transparent: earlier
exploratory work on keywords, titles and acceptance in the same corpus came before the registration and is disclosed
in it.

**What are the "alternative analyses"?**
For the newcomer results there are 10; RQ1 uses 9 of them, and acceptance adds a logit and a resubmission check
(11). Each is the same test with:
- 75 or 150 topics;
- the year-balanced map, the early map, or the early map on later papers only;
- only papers with stable topics;
- only coherent topics;
- only confident labels;
- without 2026;
- only years with consistent author IDs.

**Why a linear model instead of logit?**
Linear models give answers directly in percentage points and handle many fixed effects easily. For acceptance we
also ran a logit; it gives the same direction.

**What does "controlling for topic and year" mean?**
Every model removes differences between topics, such as LLM papers vs. theory papers, and between years, such as
field-wide trends and acceptance rates. Technically: topic and year fixed effects. For the newcomer comparison we go
further: each paper is compared only with papers from the same topic *in the same year* (topic-by-year cells).

**Your simulation found 12.6% false positives. Are your results wrong?**
No, but the p-values are approximate. In one scenario, where topic structure cuts across our 100 topics, the
standard test rejected 12.6% (methods) and 10% (benchmarks) of the time instead of 5%. Our newcomer results are far
stronger than that inflation: t = 6.7 and −4.4. Even after shrinking them by the inflation we saw, p stays below
0.001, and a second clustering method agrees. (A3)

**What is Holm?**
A correction for testing several hypotheses at once. It keeps the chance of *any* false positive in the family at
5%.

**What's a wild cluster bootstrap?**
A resampling way of getting p-values when there are only 100 clusters. It was our registered fix. It didn't fully
fix the problem in simulation, and we report that openly.

## 4. Findings

### Foundation models

**Isn't the foundation-model result just a time trend?**
No. The model controls for year, so field-wide trends cancel out. The question is whether topics that
adopted foundation models *more* lost architecture papers *more*. They did.

**Could it be reverse causality? Topics where architecture work was already dying adopted foundation models?**
Possible. We use last year's adoption to predict this year's architecture papers, which helps with timing, but it is
still an association.

**Maybe architecture papers are just labelled differently now?**
Partly possible. A paper adding a small adapter to an LLM is labelled "method", not "new architecture". But that is
the pattern we mean: people build on top instead of designing new backbones.

### Newcomers

**Why did you predict the opposite?**
Ideas from herding and fashion research: newcomers imitate what is visible and safe, and insiders have the
expertise to innovate. Our data say the opposite, which fits "outsider innovation" ideas.

**Maybe newcomers are students writing small incremental methods?**
Possible. "New method" is a contribution *type*, not a measure of quality or novelty. What we show is who writes
which type of paper.

**Is it just team size?**
Not for methods: the method gap stays at +3.9 points with team size controlled. For benchmarks, team size accounts
for about two-thirds of it (−1.7 shrinks to −0.5). Big teams write more benchmark papers, and big teams usually
include an incumbent. (A2)

**Isn't +3.7 points small?**
On a 75% base, the method gap is modest. But it is very precise (t = 6.7), it holds everywhere we looked, and it
points the opposite way from our prediction. The benchmark gap is about a fifth of its base rate. The main message is
the direction: newcomers are not the followers we expected.

**Do newcomer papers get accepted less often?**
Yes, about 10 points less within the same topic and year. But most of that is about who writes them: team size and
experience. Within the same authors, the gap is about 3 points. ICLR is double-blind, so this need not be reviewer
bias; being new to a topic can simply make a paper weaker. (A6)

### Titles

**How did you define a branded title?**
A title that starts with a short name followed by a colon, like "BERT: …". *[Check the exact rule in your title
analysis before the talk.]*

**What does "returning authors lag on style" mean?**
Authors who submitted before adopt the new title style less than the field does, while they keep pace on topics.
The lag is largest for first authors. *[Check the exact definition of the lag measure in your title analysis.]*
(A10)

**Isn't this just ChatGPT?**
LLM-favoured words like "Enhancing" jump after 2023, but the "NAME:" structure rises with or without LLM
fingerprints in the abstract. (A11)

### Reward

**Your acceptance result for crowded topics isn't significant. So do they hurt or not?**
We can't tell. The discovery test could only detect effects of about 4 points per 2.7× more papers, and the held-out
test about 5 (−1.5 points, SE 1.9, one-sided p = 0.21). Inconclusive in both splits. All we can say is that there is
no detectable *premium*.

**Isn't "against the tide" overclaiming?**
That's why it's labelled exploratory: p = 0.02, not corrected. One reading is scarcity: fewer architecture papers
remain, and those that do may stand out. It was not among the registered held-out tests, so it stays exploratory.

**So what should a researcher do?**
We found no detectable acceptance premium for crowded topics, but the tests were too weak to rule one out. Far jumps
from the team's own earlier ICLR work go with lower acceptance, in discovery and on held-out papers; we don't know
whether changing closeness would change anything. For people who study science: check your topic map with a
prospective version.

**What does go with acceptance?**
Theory papers (+9 points vs. method papers) and larger teams (+9 points per doubling). These are associations,
not advice; team size also stands for compute and seniority. (A7, A8)

### Why areas differ (slide 14; post hoc)

**Q: What explains the low areas besides federated learning?**
Across 50 keywords, areas where more papers come from topic newcomers are accepted less often (ρ = −0.40, p = 0.004);
CNN and classification papers are 85–88% newcomer papers. Paper type and team size explain little (adjusted vs raw
gaps r = 0.97), and foundation-model share does not predict an area's acceptance (ρ = 0.07). The "saturated paradigm"
reading for CNNs and image classification (shares peaked in 2018) is a hypothesis we could not test.
*If pushed:* the newcomer gap (~10 pp) times the extra newcomer share of these areas covers only a few points of a
−10 to −14 pp gap, so composition is part of the story, not all of it.

### Areas and federated learning (slide 14 and A19; post hoc PH4)

**Is federated learning a scam?**
*Don't use the word "scam" yourself.* Answer: "Submissions on federated learning fell: its share fell by two-thirds
after 2023. In our discovery papers, FL papers were also accepted 11 to 15 points less often than other papers each
year since 2023, and adjusting for who writes them changes that little: FL authors became *more* experienced. On the
held-out papers the acceptance gap was smaller and not significant (−4.9 points, an underpowered test), so that part
is not confirmed. We can't observe reviewers' reasons."

**Is the FL result significant?**
On its own, yes: about −11 points (keyword) or −14 points (topic), p = 0.005 each. After correcting for testing 68
keywords, no single area is significant (q ≈ 0.17–0.19), and our test is conservative. Two things make FL more
credible than a random hit:
- two independent definitions agree (author keywords and our content-based topic);
- the gap is negative in every year since 2023, at about 100 papers a year.

We registered it for the held-out papers (H4-FL), and it was **not confirmed**: −4.9 points (CI −15.4 to +5.7;
one-sided p = 0.14). See "Held-out replication" below.

**Is acceptance in FL *declining* over time, or just low?**
Mostly low. The discovery trend is −3 points per year (p = 0.08), and the early "premium" rests on 11 papers in 2020.
The registered held-out trend went the other way: +3.2 points per year (CI −3.3 to +9.6; not supported), and in the
pooled re-run the trend roughly halves (−1.9, p 0.18). The clearer "decline" is in submissions: from 3.2% of all
submissions in 2023 to 1.1% in 2026.

**How do you know it's not just weaker authors moving in?**
Three checks:
- the share of FL papers with an author who already had an accepted ICLR paper *rose* from 4% to about 60%;
- team size and the share of method papers stayed flat;
- adjusting for type, foundation-model use and team size barely changes the level (−11.3 → −10.5 points);
- adding author experience keeps 76% of the decline, but the decline itself is not significant (trend p = 0.08;
  adjusted p = 0.20), so don't lean on that number.

**Then why are FL papers accepted less (in discovery)?**
Two explanations remain, and we can't separate them without review texts:
- reviewers became more sceptical (novelty fatigue, or doubts about practical value);
- the remaining papers are more incremental, as the big ideas were taken early.

Both fit "the field moved on".

**Which areas are favoured?**
Descriptively:
- above average: pre-training, imitation learning, language models, generative models, diffusion (+6 to +10 points);
- by topic: neural rendering and robot learning (about +11 to +14);
- below average: FL, CNNs, image classification, data augmentation (−10 to −14).

These are associations with the same year's papers, not advice on what to work on.

**Did you go fishing for FL?**
The question came from an earlier keyword grid, so FL was not a blind discovery. We say this openly. That is why:
- we ran a *systematic* screen of all 68 keywords and 100 topics, declared before running;
- we corrected for multiple comparisons;
- we registered FL for a held-out test before the run. It was not confirmed (−4.9 points, underpowered), so the FL
  acceptance gap stays discovery evidence only.

**Why both keywords and topics?**
Keywords are chosen by the authors, so they carry no topic-map hindsight. Topics are content-based. Agreement between
the two is the robustness check.

## 5. Held-out replication (slides 13 and 16; A14–A17)

**What exactly are the held-out papers? Is this a true holdout?**
They are the 11,099 papers (with text) of the source's former confirmation split, released on 18 October 2026. We
had never analysed them. We registered every test before the single run, ran frozen code once, and report every
result. But the source's policy says it does not certify an untouched, independent holdout, so we call this a
*pre-registered out-of-sample replication*, not an independent confirmation.
- *If pushed:* the source does not document how papers were assigned to the split; it excluded 1,309 pending
  family/link cases. H4-FL's out-of-sample status is weaker still: the earlier keyword grid that suggested FL has
  unknown provenance, so we cannot check whether it overlapped these papers.

**Why one-sided tests?**
Each held-out test asks one registered question: does the discovery direction hold? One-sided at α = 0.05 was
registered in the original pre-registration, before any held-out data were available. Two-sided p are in the run
output; H1d, H2b′, H2c′ and E1 would pass two-sided as well.

**Why are some held-out estimates larger (H1d −0.110 vs −0.080; far jump −6.1 vs −5.4)?**
The held-out sample is about a quarter of the size, so its intervals are wide (H1d: −0.181 to −0.039), and some tests
(H1d, H2c′) were underpowered at the discovery size; significant estimates from underpowered tests tend to overstate.
The replication supports the direction, not the size. Don't compare the sizes as if they had replicated.

**The novelty floor did not replicate. Was it false?**
Say it plainly: it did not replicate. In discovery, the least-novel fifth sat 3.3 points below the middle fifth; on
the held-out papers it is −0.1 (CI −3.5 to +3.2). The held-out test had only 47% power at the discovery size
(MDE₈₀ 5.4 points), so by our registered reading rule the result is uninformative: it neither confirms nor rules
out a 3-point gap. We no longer claim the novelty floor.
- *If pushed on why:* we don't know. It was post hoc, picked from many tests; novelty on held-out papers is measured
  against the pooled earlier papers; and held-out abstracts had no cleaned-text check. We have not tested any of
  these explanations.

**So is federated learning just noise?**
Not confirmed is not refuted. The held-out gap is −4.9 points, the same direction, with a CI from −15.4 to +5.7. With
134 FL papers the test could only detect gaps of about 15 points (MDE₈₀ 14.5), so it is uninformative. The FL
acceptance gap stands as discovery evidence only. The fall in FL's share of submissions is a separate, outcome-free
observation in discovery.
- *If pushed:* the held-out yearly gaps are mixed (2021: −20, 2022: −17, 2023: +6, 2024: −4, 2025: −11, 2026: −0
  points, on 13–36 FL papers a year), and the registered trend test was not supported either. Don't read anything into
  single years.

**Is the far-jump gap just the newcomer gap?**
Not only. In discovery it is −5.0 points with newcomer status controlled, vs −5.4 without. It also appears within the
same author: closer papers go with higher acceptance, +0.55 (discovery) and +1.06 points (held-out) per +0.1 cosine.
Co-author choice and failure-driven pivots are not controlled, so it is an association, not advice to stay put.

**Isn't staying close then "safe"?**
Near papers (90th percentile of closeness) are not accepted less often than the median: +1.7 points in discovery (CI
−0.2 to +3.7), +2.3 on held-out papers (not registered, p 0.17), and +2.1 in the pooled re-run (Holm 0.036,
exploratory). So no lower acceptance near the own record, and possibly a small gain; we did not register this
contrast, and it is an association, not advice to stay put.

**Isn't reporting the "supported" ones cherry-picking?**
Every registered held-out test is on slide 16 or in A14, including the failures: P1b (not supported), H4-FL level
and H4-FL trend (not supported; the trend had the opposite sign, +3.2 points per year), H3a (inconclusive), P7 (not
supported). Secondary tests are each one-sided at 0.05 without adjustment, so with six of them one false positive
would not be surprising; they carry less weight than the Holm-adjusted families.

**The emerging-keyword result (A1) has a CI that includes zero. Why "supported"?**
The 95% CI is two-sided (−0.2 to +6.7 points); the registered test is one-sided (p = 0.031), and it also had to pass
a null-frame check (p = 0.020). It passes both, but only just. Treat it as weak support. (A16)

**Topic acceptance edges: 0.60 out of sample vs 0.38 within discovery. Which is right?**
They answer different questions with different windows: discovery 2018–22 vs held-out 2024–26 papers, against
discovery 2018–22 vs discovery 2024–26 papers. The registered prediction was only 0 < b < 1, and it held: edges
persist but shrink. Read raw topic rankings as shrunk towards zero. (A17)
- *If pushed on the keyword ranking (slide 14):* the registered test used early-map topic units. For author keywords
  like those plotted, held-out edges showed no detectable persistence: b = 0.16 (CI −0.34 to 0.66; not registered).

**What is the pooled re-run?**
After the held-out run, every analysis was re-run on all 54,579 papers (A18). It is exploratory and confirms nothing:
about 80% of each pooled sample is discovery papers, and pooling changes some discovery features (hot topics, author
histories). Every registered hypothesis keeps its discovery sign (H1d −8.9 points, H2b +3.5, H2c −1.7). H3a reaches
p = 0.049, Holm 0.098, so it is still inconclusive. The FL topic is flagged (q = 0.037), but the registered held-out
FL test was not supported. The pooled novelty floor (−3.0) is driven by the discovery papers. The discovery results
stay the registered record.

## 6. Scope and next steps

**Is any of this causal?**
No. Everything is an association. "Fade" and "lean" describe patterns, not proven causes. Topic, team and paper
type are chosen together.

**Do you drop withdrawn papers in the acceptance analysis?**
Yes, the main model uses the 32,190 papers with a final decision. Counting papers withdrawn after review as
rejections gives a similar estimate (−2.1 points instead of −1.7).

**Why not use review scores?**
They weren't in our data snapshot. They are the next step, because they could separate reviewers from final
decisions.

**Did it replicate?**
Partly, and we report all of it. On 11,099 held-out papers, with every test registered before the single run: the
foundation-model result, both newcomer results and the far-jump gap replicated; the novelty floor did not (an
uninformative test); the federated-learning gap was not confirmed (underpowered); crowding stayed inconclusive.
(Slide 16, A14)

**How reproducible is this?**
All code, the frozen inputs and every output are in the repository. One command re-runs the frozen analysis.

---

## Concepts in plain words（概念速查）

| Term | Plain English | 中文解释 |
|---|---|---|
| pp (percentage points) | difference between two percentages: 40% → 45% is +5 pp | 百分点：两个百分比的差 |
| Linear probability model (LPM) | a regression with a 0/1 outcome; each coefficient is a change in probability, in pp | 线性概率模型：因变量是0/1，系数就是概率变化（百分点） |
| Within topic and year (fixed effects) | compare a paper only with papers from the same topic and year | 只和同主题、同年份的论文比较，排除主题和年份差异 |
| 95% CI | the range of values consistent with the data | 置信区间：数据支持的合理范围 |
| Clustered standard errors | papers in the same topic are not independent, so uncertainty is computed by topic | 同一主题的论文不独立，按主题计算误差 |
| Holm correction | adjusts p-values when testing several hypotheses together | 多重检验校正，防止“测得多总能撞上一个” |
| Pre-registration | hypotheses and analysis written down before seeing results | 预注册：先写好假设和分析方法，再看结果 |
| Outcome-blind | acceptance data locked until the final run | 结果盲：最终运行前看不到录取数据 |
| Hindsight bias (topic maps) | defining topics with today's view distorts the past | 后见之明：用今天的主题划分去看过去，会扭曲历史 |
| Prospective map | map built only from early papers, applied to later ones | 前瞻地图：只用早期论文建的主题图 |
| Kappa (κ) | agreement beyond chance; 0.93 is very high | 一致性指标，0.93 很高 |
| Power / MDE | the smallest effect the test could reliably detect | 检验能可靠发现的最小效应 |
| Exploratory vs. confirmatory | exploratory = found while looking; confirmatory = registered in advance | 探索性 vs 验证性（预注册） |

## Numbers to remember

| Fact | Number |
|---|---|
| Submissions | 43,480, 2017–2026 |
| New-architecture papers | 24% → 8% |
| Building on a foundation model | 0.3% → 54% |
| Branded titles | 9% → 41% |
| Papers from 2024–26 | 69% |
| "Emerging" topics | 8 (early map) vs. 29 (standard map) |
| Foundation models vs. new architectures (discovery) | −8 pp from 0 → 100% FM, so about a third fewer at 50% vs 10% adoption |
| Newcomers and methods | +3.7 pp (base 75%) |
| Newcomers and benchmarks | −1.7 pp (base 7.7%, about a fifth fewer) |
| Newcomer share | 73% of papers |
| Label agreement | κ = 0.93 |
| False positives found in simulation | up to 12.6% instead of 5% (one scenario) |
| Newcomer acceptance gap | −10 pp in the same topic and year; −3 pp within the same authors |
| Federated learning acceptance gap (discovery) | −11 pp (keyword) / −14 pp (topic), p = 0.005; −11 to −15 pp each year since 2023 |
| Federated learning share of submissions | 3.2% (2023 peak) → 1.1% (2026) |
| Federated learning authors with an earlier accepted ICLR paper | 4% (2021) → about 60% |
| **Held-out papers** | 11,099 (released former confirmation split; never analysed before the run); 8,284 decided, 8,185 in 2018–26 (acceptance tests) |
| Held-out label agreement | κ = 0.93 (555-paper second pass) |
| H1d held-out | −0.110 (CI −0.181 to −0.039), one-sided p 0.001: replicated (discovery −0.080) |
| Newcomers held-out (H2b′ / H2c′) | +3.6 / −2.1 pp, one-sided Holm p 0.001 each: replicated |
| Crowding held-out (H3a) | −1.5 pp (SE 1.9), p 0.21: inconclusive in both splits (MDE₈₀ 4.8 pp) |
| Far jump vs median (E1) | −5.4 pp discovery; −6.1 pp held-out (CI −9.3 to −2.9), Holm p 0.005 |
| Adjusted acceptance by closeness fifth (discovery) | 39.7 / 41.8 / 44.4 / 47.2 / 46.9% (far → close) |
| Same author, per +0.1 cosine (E4) | +0.55 pp discovery; +1.06 pp held-out |
| Novelty floor (P1b) | −3.3 pp discovery; −0.1 pp held-out (CI −3.5 to +3.2): not replicated, uninformative (power 0.47, MDE₈₀ 5.4 pp) |
| Federated learning held-out (H4-FL) | −4.9 pp (CI −15.4 to +5.7), p 0.14; 134 FL papers, MDE₈₀ 14.5 pp: not confirmed; trend +3.2 pp/yr, not supported |
| One topic insider vs none (teams H1) | +3.4 pp discovery; +3.9 pp held-out |
| Emerging vs Mainstream keyword (A1) | +2.7 pp discovery; +3.3 pp held-out (one-sided p 0.031) |
| Topic edges out of sample (premia b) | 0.60 (CI 0.32–0.88; early-map topics); within discovery 0.38; keywords 0.16 (not registered) |
| Pooled re-run (exploratory, A18) | 54,579 papers; H1d −8.9 pp; far jump −5.5 pp; confirms nothing |
| Hindsight map "forecast" of topic growth | R² 0.28 (standard map) vs −0.03 (2017–20 map) |
