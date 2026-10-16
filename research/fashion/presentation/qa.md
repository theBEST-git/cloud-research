# Q&A preparation

Short answers first. Use the "If pushed" line only if they ask a follow-up. Backup slides are B1–B11.

**Three habits that keep answers safe:**
- Say "goes with" or "is associated with", never "causes".
- If you don't know, say "we didn't test that; it's a good next step."
- Point to a backup slide when a number helps.

---

## 1. Data and measurement

**Why ICLR?**
ICLR is the one major ML venue that has published *every* submission, including rejected and withdrawn ones, on
OpenReview for ten years. That lets us avoid survivorship bias. The cost is that it's one venue. ACL is next.

**How were the topics built? Why 100?**
We embedded each title and abstract with SPECTER2, a model trained on scientific papers, and clustered the papers
into 100 groups. We re-ran everything with 75 and 150 topics, and the main results hold. (B4)
- *If pushed on quality:* the topics agree with ICLR's own area labels better than a keyword baseline (NMI 0.30 vs.
  0.27). A blind checker matched papers to topic names 61% of the time, against 10% by chance.

**Can you trust LLM labels for contribution type?**
They are very consistent: a blind second pass agrees at kappa 0.93. But the reference labels were also made by an
LLM, so this shows consistency, not human-level validity. A human check is our next step. (B4)
- *If pushed:* for label errors to create the newcomer result, they would have to differ between newcomer and
  incumbent papers. Correcting for the measured error rates makes the result slightly *larger*, not smaller.

**How do you know who is a newcomer?**
From OpenReview author IDs. A paper is a newcomer paper if none of its authors submitted to ICLR in that topic
before, whatever the outcome.
- *If pushed:* ICLR changed its ID system in 2021, so some experienced authors look new. That makes the two groups
  more alike, which pushes estimates *towards zero*. So our newcomer results are, if anything, conservative.
  Dropping 2021–22 gives the same results.

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
We registered before the full-corpus labels existed and before any acceptance data were opened. Acceptance stayed
sealed in code: only one file could read it, and that file refused to run unless the frozen code matched its
hashes. Then we ran it once, in 18 seconds, and report everything. We also disclosed earlier exploratory work on
the same corpus.

**What are the "10 alternative analyses"?**
The same test with:
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

**What does "within the same topic and year" mean?**
We compare each paper only with papers from the same topic and year. This removes differences between topics, such
as LLM papers vs. theory papers, and between years, such as acceptance rates. Technically: topic-by-year fixed
effects.

**Your simulation found 12.6% false positives. Are your results wrong?**
No. It means p-values from the standard method are a bit optimistic. Our key results are far stronger than that:
t = 6.7 and −4.4. Even after shrinking them by the inflation we saw in simulation, p stays below 0.001, and a
second clustering method agrees. (B3)

**What is Holm?**
A correction for testing several hypotheses at once. It keeps the chance of *any* false positive in the family at
5%.

**What's a wild cluster bootstrap?**
A resampling way of getting p-values when there are only 100 clusters. It was our registered fix. It didn't fully
fix the problem in simulation, and we report that openly.

## 4. Findings

### Foundation models

**Isn't the crowd-out just a time trend?**
No. We compare topics within the same year, so field-wide trends cancel out. The question is whether topics that
adopted foundation models *more* lost architecture papers *more*. They did.

**Could it be reverse causality? Topics where architecture work was already dying adopted foundation models?**
Possible. We use last year's adoption to predict this year's architecture papers, which helps with timing, but it is
still an association.

**Maybe architecture papers are just labelled differently now?**
Partly possible. A paper adding a small adapter to an LLM is labelled "method", not "new architecture". But that is
the crowd-out we mean: people build on top instead of designing new backbones.

### Newcomers

**Why did you predict the opposite?**
Ideas from herding and fashion research: newcomers imitate what is visible and safe, and insiders have the
expertise to innovate. Our data say the opposite, which fits "outsider innovation" ideas.

**Maybe newcomers are students writing small incremental methods?**
Possible. "New method" is a contribution *type*, not a measure of quality or novelty. What we show is who writes
which type of paper.

**Is it just team size?**
Not for methods: the method gap stays at +3.9 points with team size controlled. For benchmarks, team size explains
most of it (−1.7 shrinks to −0.5). Big teams build benchmarks, and big teams usually include an incumbent. (B2)

**Do newcomer papers get accepted less often?**
Yes, about 10 points less within the same topic and year. But most of that is about who writes them: team size and
experience. Within the same authors, the gap is about 3 points. ICLR is double-blind, so this need not be reviewer
bias; being new to a topic can simply make a paper weaker. (B6)

### Titles

**How did you define a branded title?**
A title that starts with a short name followed by a colon, like "BERT: …". *[Check the exact rule in your title
analysis before the talk.]*

**What does "returning authors lag on style" mean?**
Authors who submitted before adopt the new title style less than the field does, while they keep pace on topics.
The lag is largest for first authors. *[Check the exact definition of the lag measure in your title analysis.]*
(B9)

**Isn't this just ChatGPT?**
LLM-favoured words like "Enhancing" jump after 2023, but the "NAME:" structure rises with or without LLM
fingerprints in the abstract. (B10)

### Reward

**Your acceptance result for crowded topics isn't significant. So do they hurt or not?**
We can't tell. The test could only detect effects of about 4 points per 2.7× more papers. All we can say is that
there is no *premium*.

**Isn't "against the tide" overclaiming?**
That's why it's labelled exploratory: p = 0.02, not corrected. One reading is scarcity: fewer architecture papers
remain, and those that do may stand out. It's a hypothesis for the replication.

**So what should a researcher do?**
Don't count on following trends to get accepted. For people who study science: check your topic map with a
prospective version.

**What does go with acceptance?**
Theory papers (+9 points vs. method papers) and larger teams (+9 points per doubling). These are associations,
not advice; team size also stands for compute and seniority. (B7, B8)

## 5. Scope and next steps

**Is any of this causal?**
No. We say "associated with" throughout. Topic, team and paper type are chosen together.

**Why not use review scores?**
They weren't in our data snapshot. They are the next step, because they could separate reviewers from final
decisions.

**Will it replicate?**
We held out part of the ICLR data. The four key hypotheses are already registered for it, including the newcomer
results in their new direction.

**How reproducible is this?**
All code, the frozen inputs and every output are in the repository. One command re-runs the frozen analysis.

---

## Concepts in plain words（概念速查）

| Term | Plain English | 中文解释 |
|---|---|---|
| pp (percentage points) | difference between two percentages: 40% → 45% is +5 pp | 百分点：两个百分比的差 |
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
| FM crowd-out | −8 pp from 0 → 100% FM, so about a third fewer from 10 → 50% |
| Newcomers and methods | +3.7 pp (base 75%) |
| Newcomers and benchmarks | −1.7 pp (base 7.7%, about a fifth fewer) |
| Newcomer share | 73% of papers |
| Label agreement | κ = 0.93 |
| False positives found in simulation | 12.6% instead of 5% |
| Newcomer acceptance gap | −10 pp in the same topic and year; −3 pp within the same authors |
