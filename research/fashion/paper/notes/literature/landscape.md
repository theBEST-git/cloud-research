# Landscape: academic conversations, gaps and candidate story lines

Synthesis for the ICLR 2017-2026 paper (ACL ARR long paper, 3,000-4,000 words). Built 2026-11-03 from the eight
workspace files only. No data file, outcome column or script was read or run.

## 0. How to read this file

**Source pointers.** Every number below carries a pointer, and every pointer is a file I read in full.
- `DC:n` = `dossier_core.md` line n.
- `DP:n` = `dossier_posthoc.md` line n.
- Literature notes:
  - `NR:n` = `lit_novelty_reward.md`
  - `OUT:n` = `lit_outsiders.md`
  - `FW:n` = `lit_fashion_waves.md`
  - `MM:n` = `lit_ml_metaresearch.md`
  - `ME:n` = `lit_methods_measurement.md`
  - `CP:n` = `lit_closest_prior.md`
- The BibTeX keys are those in the matching `lit_*.bib` files.

**Evidence tiers.** These follow DC:25-31 and DP:12-19.

| Tier | Meaning |
|---|---|
| A | Registered and supported on held-out papers |
| B | Post hoc in discovery; a declared held-out test then supported it |
| C | Registered but inconclusive or not replicated |
| D | Discovery only (exploratory or post hoc) |
| E | Descriptive, with no acceptance outcome |
| E\* / D\* | From the earlier exploratory title analysis. E\*: the outcome-free share was re-verified. D\*: the acceptance ratio was not re-run. |

**Which works may be cited.** Only works that a literature agent marked VERIFIED are cited below.
- Flags the agents raised are repeated where they matter.
- Unverified candidates appear only in Section 3.3, as things to check.

**Relation labels in Section 2:**
- **supports**: our finding agrees with the conversation's claim.
- **extends**: same direction, but a new setting, stage or measure.
- **complicates**: adds a condition or a rival reading.
- **contradicts**: the opposite direction.

### Bottom line

Recommended story line (Section 5): **"Anchored, not herded."**

The thesis: ML's foundation-model wave is not a herd.
- **Measured without hindsight**, the convergence that survives is a shared technical package. Foundation models
  displace new architectures (A).
- **Entrants to a topic** bring new methods, not the follow-on benchmarks that herding predicts. This reverses our own
  registered prediction (A). If anything, entrants are slower to take up trends (E).
- **The review gate** shows no detectable premium for following the crowd: crowding is C, branding D\*, and topic
  edges regress (B).
- **What goes with acceptance is anchoring.** Continuity with the team's own record and a topic insider on the team
  are both B. Arriving early is also favoured, but only weakly (B, weak).
- **The conceptual payoff:** conformity in this field shows up as continuity at the gate, not as imitation in the
  crowd. The herding and fashion literature and ML's own self-critique usually run these two together.

---

## 1-2. The conversations, and where our findings land

Seven conversations. Each block gives the core claim, the canonical verified works, the open questions, and then a
table of our findings that speak to it. A cross-tab matrix follows at the end of the section.

### Conversation 1: Fashion, herding and bandwagons in science

**Core claim.** Attention in science and organisations moves in fashions that need not track merit.
- Adopters imitate others. Herding is individually rational but collectively inefficient and fragile.
- Bandwagons form around transportable theory-and-method packages.
- Early adopters of a modestly useful idea gain; late imitators do not.

**Canonical verified works:**
- Fashion:
  - `abrahamson1991managerial` (FW:15)
  - `abrahamson1996management` (FW:23)
  - `abrahamson1999management` (lifecycle, upswing vs downswing; FW:31)
- Adaptive emulation: `strang2001search` (FW:39)
- Cascades and herding:
  - `bikhchandani1992theory` (FW:57)
  - `banerjee1992simple` (FW:65)
  - `weisberg2013modeling` (scientists herd to avoid risk; FW:73)
- Package bandwagon: `fujimura1988molecular` (FW:107; content seen only in secondary descriptions)
- Diffusion and hype cycles:
  - `rogers2003diffusion` (FW:173)
  - `dedehayir2016hype` (FW:197)
  - `vanlente2013comparing` (FW:206)
- Priority and timing:
  - `merton1957priorities` (NR:63)
  - `newman2009first` (NR:295)
- `crane1969fashion` (NR:82): end page not confirmed. Cite it for the question only.

**Open questions in this literature:**
1. It measures how much a fashion is talked about or adopted. It almost never observes an independent verdict on
   each adopter, so it cannot ask whether the same idea is rewarded differently on the way up and on the way down
   (FW:303).
2. Who rides a wave: cheap imitators or innovators (FW:305)?
3. Do the waves survive when the categories are not drawn with hindsight (FW:304)?
4. Weisberg's "herding" means clustering to avoid risk. Cascade "herding" means copying what others do. The literature
   rarely separates the two (FW:79 vs FW:61). This matters for us, because our data can separate them.

**Our findings in this conversation:**

| Our finding | Numbers (source) | Tier | Relation |
|---|---|---|---|
| Registered herding prediction for entrants came out reversed. Newcomer papers are more often method papers and less often benchmark, dataset or evaluation papers. | Method: +3.71 [+2.61, +4.80] discovery; +3.60 [+1.48, +5.71] held-out, one-sided p 0.0007. Measurement: −1.70 [−2.46, −0.93] discovery; −2.10 [−3.35, −0.85] held-out, p 0.0005 (DC:296-297, 365-366). | A (reversed) | **contradicts** the cascade picture of the entrant (FW:63) |
| First-time teams are not trend-chasers | Emerging keywords −3.7 pp (16.7% vs 25.0%; q 6e-6) (DP:315). FM papers −4.6 / −9.0 / −14.7 pp at 5-15 / 15-30 / 30-50% adoption (DP:360-362). | E | **contradicts** imitation by late entrants |
| Duplication grows with volume, not with herding per pair | Papers with a same-year twin: 19.5% (2019) → 48.8% (2026), but twins per paper per 1,000 submissions 0.32 → 0.19 (DP:78-79). Newcomer papers less often twinned: −3.9 pp [−5.0, −2.7] (DP:275). | E | **complicates**: the rise in twins is a volume effect, not more herding (DP:276) |
| Whether entrants flock to hot topics | H2a: −0.73 [−2.68, +1.22]; hindsight check fails (DC:295). Newcomer × hot, E5: −0.4 / −0.6 pp, both n.s. (DC:307). | C / D | Leaves the "flocking" half of herding **untested** |
| FM adoption goes with fewer new-architecture papers | −7.98 [−12.14, −3.82] discovery; −11.0 [−18.1, −3.9] held-out, one-sided p 0.0013 (DC:271, 364) | A | **supports** a Fujimura-type package bandwagon (FW:113). It cannot rule out the efficient-choice reading (Sutton; FW:238). |
| Early rising keywords favoured; premium falls after a keyword's peak | A1: +2.67 [+0.76, +4.58] discovery; +3.25 [−0.18, +6.69] held-out, p 0.031 (DC:375). PH6: −5.7 [−8.5, −2.9] discovery; −5.2 [−11.1, +0.7] held-out, p 0.043; −1.7 (p 0.33) without the six keywords inspected first (DP:389-397). | B (weak) | **extends**, weakly, the upswing/downswing asymmetry (FW:37) and the early-adopter advantage (FW:45) from discourse to the gate's verdict |
| The vivid fad case does not replicate | Federated learning: −11.3 [−17.9, −4.8] discovery (q 0.19); held-out −4.9 [−15.4, +5.7], uninformative. Trend has the opposite sign held-out (+3.2 pp/yr) (DC:368-369). | D / C | **complicates** fad narratives built on single cases (Strang and Macy's warning about success stories; FW:45) |
| Hindsight maps manufacture waves | 29 vs 8 emerging topics (DC:176-184) | E | **extends** the critique that hype-cycle shapes are inconsistent (FW:204, 212) to the measurement of topics |
| Branded titles rise without a premium | "NAME: subtitle" share 6.5-14.3% (2017) → 37.0-48.8% (2026), by definition (DP:106-121). Acceptance ratio 1.02 (DP:133). | E\* / D\* | **complicates** the idea that symbolic fashion pays at the gate (FW:220). Earlier exploratory; not re-run. |
| Far jumps penalised, staying close not | See Conversation 2 | B | **supports** Weisberg's premise that risk avoidance is rewarded (FW:79). But the reward is for staying near one's **own** record, not near the crowd. |

### Conversation 2: Tradition, novelty and their reward (the "essential tension"; conservative evaluation)

**Core claim.** Science needs both convergent tradition and divergent innovation (Kuhn).
- Researchers mostly choose strategies that deepen known work. Innovative strategies are rarer, riskier and more
  variable in payoff (Foster et al.).
- The best-cited work is conventional with a small atypical intrusion (Uzzi et al.).
- Novel work is penalised in short windows (Wang et al.).
- Whether gatekeepers penalise novelty is **contested**:
  - grant evaluators penalise the novelty tail (Boudreau et al.);
  - review files at 49 journals show no penalty (Teplitskiy et al. 2022);
  - group evaluation leans conservative (Lane et al.);
  - closeness to one's own area brings both bias and expertise (Li).

**Canonical verified works:**
- Kuhn:
  - `kuhn1977essential` (NR:35)
  - `kuhn1962structure` (NR:23; bibliographic facts only)
- Producer strategies and impact:
  - `foster2015tradition` (NR:99; end page not confirmed)
  - `uzzi2013atypical` (NR:114)
  - `wang2017bias` (NR:127)
- Evaluation:
  - `boudreau2016looking` (NR:217). OUT:122 flags that the direction of the distance effect was not seen; check the
    abstract.
  - `teplitskiy2022is` (NR:255)
  - `lane2022conservatism` (NR:269)
  - `li2017expertise` (NR:233)
  - `teplitskiy2018sociology` (NR:245)
- Consolidation and team size:
  - `park2023papers` (NR:158)
  - `wu2019large` (NR:169)
- Individual vs collective cost of conservative choices: `rzhetsky2015choosing` (FW:155)
- Cumulative advantage:
  - `merton1968matthew` (NR:50)
  - `price1976general` (NR:73)

**Open questions:**
1. Is the gate conservative, and towards what: novel content, or authors who move?
2. Which kind of novelty is penalised, and where in the process (NR:481-483)?
3. Does conservatism sit with producers (Foster et al.) or with evaluators (Boudreau et al., Teplitskiy et al.)? Few
   studies see both producers and the gate in the same complete population.

**Our findings in this conversation:**

| Our finding | Numbers (source) | Tier | Relation |
|---|---|---|---|
| Far jump from the team's own record goes with lower acceptance | −5.44 [−7.10, −3.78] discovery; −6.09 [−9.32, −2.86] held-out, one-sided p 0.0025 (DC:370) | B (primary) | **extends** Foster et al.'s "risky distance is less rewarded" (NR:111) to the evaluator, on all decided submissions |
| Closer to one's own past goes with acceptance, within the same author | +0.55 per +0.1 cosine discovery; +1.06 [+0.23, +1.89] held-out, p 0.006 (DC:372). Composition may explain half (DP:243). | B (secondary) | **extends** |
| Shape: a penalty for far, no extra gain for closest | Adjusted acceptance by closeness fifth, far to near: 39.7 / 41.8 / 44.4 / 47.2 / 46.9% (DP:236). Near minus middle +1.75, Holm 0.148 (D, quoting rule DP:40-41). | D | **complicates** "more tradition is always better". It reads as a threshold: leaving costs, repeating does not pay extra. |
| Novelty relative to the field: no detectable penalty at the top; the low-novelty penalty did not replicate | P1a, most-novel minus middle fifth: +0.44 [−1.41, +2.28]; held-out +2.54 (unregistered) (DP:261). P1b, least-novel fifth: −3.27 discovery, −0.13 held-out, uninformative (DC:371). P7: not supported (DC:373). | D / C | Weakly **consistent with** Teplitskiy 2022 (NR:263-267). Too weak to "reconcile" the debate on its own. |
| Topic entrants supply method papers | See Conversation 1, row 1 | A | **complicates** the "stable conservative distribution" picture (NR:105). Divergence enters with newcomers. But a method paper is a contribution *type*, not novelty (DC:313-314). |
| The gate does not favour the method type | Within topic-year, vs method papers: theory +8.9, dataset/benchmark +3.9, empirical −2.7 (DC:351) | D | **complicates** any reading that innovation as such is rewarded |
| Steep team-size gradient | +8.8 pp per doubling [+8.0, +9.7] (DC:395) | D | **supports** Wu et al.'s short-run reward to large teams that develop existing work (NR:175) |
| FM convergence | H1d (A). FM share 0.3% → 54.4% and new-architecture share 24.5% → 7.5%, 2017-2026 (DC:163-164). | A / E | **supports** consolidation (Park et al.; NR:165) and Kuhnian normal science inside a paradigm (NR:30). It gives a within-field mechanism. |
| One topic insider in the team | +3.42 [+1.18, +5.66] discovery; +3.88 [+0.28, +7.47] held-out, p 0.017 (DC:374) | B (secondary) | **complicated by** Li 2017: expertise vs bias (NR:240). We cannot tell them apart. |

### Conversation 3: Outsiders, entry and mobility (who brings new ideas, and how entrants fare)

**Core claim.** People at the margin produce disproportionate novelty, and their novelty is under-rewarded.
- Moving away from one's own past work costs impact.
- Ties to insiders ease entry. Mixed core-and-periphery teams do best.
- Incumbents shape when outsiders can enter.

**Canonical verified works:**
- Marginality and novelty:
  - `jeppesen2010marginality` (OUT:22)
  - `hofstra2020diversity` (OUT:34)
  - `painter2021innovations` (OUT:40)
  - `packalen2019age` (OUT:54)
  - `shi2023surprising` (NR:179)
- Entry and expertise: `arts2018paradise` (new fields: more novel, less valuable; experts mitigate the loss; OUT:66)
- Mobility:
  - `hill2025pivot` (OUT:74, NR:329). Fourth author's given name unconfirmed (NR:340).
  - `zeng2019increasing` (OUT:80)
  - `jia2017quantifying` (OUT:86)
  - `myers2020elasticity` (NR:363)
  - `leahey2017prominent` (OUT:92)
- Insiders and teams:
  - `sekara2018chaperone` (OUT:60)
  - `cattani2008core` (OUT:46)
  - `guimera2005team` (NR:390)
  - `zeng2021fresh` (NR:381)
- Incumbents: `azoulay2019does` (OUT:28)

**Open questions:**
1. What *type* of contribution do entrants bring? Prior work measures novelty, not type (OUT:225).
2. Do the pivot and chaperone patterns appear at the acceptance decision, under double-blind review, with rejected
   papers visible (OUT:226-229)?
3. Is the newcomer discount about the person or about the position (OUT:227)?

**Our findings in this conversation:**

| Our finding | Numbers (source) | Tier | Relation |
|---|---|---|---|
| Entrants propose, incumbents consolidate | H2b′ / H2c′, as above (DC:296-297) | A | **supports** "outsiders solve" (OUT:26). **Extends** it to a division of labour by contribution type. |
| Part of the benchmark gap is team size | H2c with log team size: −0.54 [−1.11, +0.04], p 0.07 (DC:301). Held-out −0.98 (DC:308). H2b unchanged at +3.92. | robustness of A | **complicates**: partly small all-new teams vs larger mixed teams |
| Newcomer acceptance gap is mostly about who writes | Raw: 37.2% vs 47.3% (DC:394). Within topic-year: −10.2 [−11.8, −8.7] (DC:343). Same sample: −5.4 without author fixed effects vs −3.1 [−4.5, −1.6] with them. An author new to the topic: −1.4 [−2.7, −0.0] (DP:178-179). | D | **complicates** the "discounting" reading (Hofstra et al.; OUT:38). The gap is mostly composition: experience, team size. A small cost remains for the same person entering a new topic. |
| Far jump penalty | −5.44 / −6.09 (DC:370). Correlation with the newcomer flag −0.57; −5.0 with a newcomer control (DP:247-248). | B | **extends** the pivot penalty (OUT:78) from citations to the decision. Hill et al. reportedly also find "lower publication success rates" for larger pivots (NR:335), so the stage itself is not wholly new (see 3.1). |
| One insider vs none | +3.42 / +3.88 (DC:374). Keyword-based insider: +0.0 (DP:289). Insider minus crossover per head: +0.58, p 0.16. Familiarity without an earlier acceptance: +0.2 [−3.8, +4.2], 767 papers (DP:292-296). | B (decomposition D) | **extends** the chaperone effect (OUT:64) and mixed core/periphery teams (OUT:50) to double-blind acceptance. **Complicates** the reading: the decomposition hints that a proven record matters, not only topic-specific knowledge. |
| Newcomer gap present everywhere | Negative in all 20 areas (−3.8 to −20.8). Smallest for theory (−5.1) and teams of 7+ (−6.4) (DP:152-154). | D | **supports** "insider ties help" (OUT:219) |
| First-time teams slower to adopt FMs and trending keywords | See Conversation 1 (DP:315, 360-362) | E | **complicates** the picture of outsiders rushing to the frontier (Movva et al. 2024: half of 2023 LLM first authors new to LLM work; CP:67). Entrants bring methods, but are not first onto trending keywords. |

### Conversation 4: Computational histories of a field, and measuring topics over time

**Core claim.** Field histories are written by fitting one topic model on the whole period and reading trends
forward. This holds for both the NLP and the scientometric traditions.
- "Dynamic" models still use all time slices when fitting.
- Topic reconstructions depend on method.
- "Emergence" is partly defined by attributes that are only visible later.
- Classifications should be updated as new years arrive. This point has been made in concept, not measured.
- Leakage of information that was not yet available inflates ML-based claims.

**Canonical verified works:**
- NLP histories:
  - `hall2008studying` (MM:27)
  - `anderson2012towards` (MM:33; Anthology author order: Anderson, Jurafsky, McFarland)
  - `prabhakaran2016predicting` (CP:57)
  - `pramanick2023diachronic` (MM:45)
  - `hoonlor2013trends` (CP:78)
  - `klinger2020narrowing` (MM:83)
- Topic models:
  - `griffiths2004finding` (ME:24)
  - `blei2006dynamic` (ME:29)
  - `wang2006topics` (ME:34)
  - `grootendorst2022bertopic` (ME:39)
- Scientometric maps:
  - `waltman2012new` (ME:68)
  - `small2014identifying` (ME:60)
  - `rotolo2015what` (ME:64)
  - `leydesdorff2002dynamic` (ME:77)
  - `klavans2014creation` (ME:72; no DOI)
  - `chavalarias2013phylomemetic` (ME:83)
  - `glaser2017same` (ME:87)
  - `held2021challenges` (ME:92)
  - `klavans2020novel` (ME:96)
  - `sjogarde2022association` (ME:100)
- Leakage:
  - `kaufman2012leakage` (ME:106)
  - `kapoor2023leakage` (ME:111)
  - `bailey2017probability` (ME:115; no pages)
  - `lazaridou2021mind` (ME:120)
- Our encoder:
  - `cohan2020specter` (ME:44)
  - `singh2023scirepeval` (ME:48)

**Open questions:**
1. How large is the hindsight distortion when the papers and the model are fixed and only the fitting window varies?
   No study found does this (ME:174, 194).
2. Which substantive trend claims survive a check without hindsight (ME:195-199)?

**Our findings in this conversation:**

| Our finding | Numbers (source) | Tier | Relation |
|---|---|---|---|
| Hindsight inflates the count of emerging topics | 29 on the all-years map (40.9% of 2024-26 papers) vs 8 on the 2017-20 map (22.3%). Late-only map: 28. Declining topics: 13 vs 26 on a year-balanced map (DC:176-186). | E | **extends** Leydesdorff (ME:81) and Rotolo et al. (ME:66) from concept to measurement. **Contradicts** single-map histories (ME:27, MM:31). |
| Trend conclusions flip with the map | "Topics age from methods to measurement": null on the all-years map (H1a −0.14, H1b +0.50). On the early map, 2021-26 papers: −3.48 [−6.21, −0.76] / +3.96 [+1.35, +6.57] (DC:201-205). | E (counted variants of C) | **extends**: the fitting window is a forking path (ME:138) |
| Diversity peaks in each map's own fitting years | Pooled map: 0.443 (2017) → 0.91 (2025). Pooled-map "diversity rising" is "not a finding" (DC:189-192). | E | **complicates** narrowing claims based on topic models fitted on the whole period (Klinger et al.; MM:87) |
| Hindsight makes growth look predictable | Size predicts 2-year growth out of time: R² 0.281 on the hindsight map vs −0.033 on the early map (DC:217). Maps differ in fitting corpus; no paired test (DC:227-231). | E | **complicates** forecasting from global maps (Klavans et al.; ME:98) |
| Which claims survive the hindsight variants | Pass: H1d, H2b′, H2c′. Fail: H3a, H2a (DC:271, 295-297, 324) | A / C | **extends** multiverse and specification-curve practice (Steegen et al.; Simonsohn et al.; ME:138-142) along a time axis |
| Apparent topic premia regress | A single year's topic acceptance rate is half noise at about 58 decided papers. Top tenth +14.3 → +2.1 pp. Premia b 0.38 discovery, 0.60 held-out (DP:324-330). | B / D | **extends** the measurement lesson from topic volume to topic rewards |
| Camera-ready text leaks outcomes into text measures | Code link in the abstract, 2023-26: 17.6% of accepted vs 0.5% of rejected (DP:83). The link-removal (cleantext) re-run holds for far jump and P1b (DP:371-372). | E / D | **extends**: a version problem (Re², Paper Copilot; MM:157-167) that affects every text-based ICLR study |

### Conversation 5: ML's self-critique — hype, homogenisation and narrowing

**Core claim.** ML is said to converge for reasons other than merit:
- the hardware lottery;
- the benchmark lottery;
- dataset concentration in elite institutions;
- benchmark construct validity;
- homogenisation around foundation models;
- compute and industry concentration;
- topical narrowing;
- rhetorical inflation under rapid growth.

There are counter-arguments. Sutton argues that convergence on general methods is efficient. Paradigm shifts recur in
explore/exploit cycles. Entrants flood new LLM work.

**Canonical verified works:**
- Lotteries:
  - `hooker2021hardware` (FW:224; no page range)
  - `dehghani2021benchmark` (FW:248)
- Datasets and benchmarks:
  - `koch2021reduced` (FW:256, MM:101)
  - `raji2021ai` (FW:272)
- Homogenisation: `bommasani2021opportunities` (FW:264)
- Counter-argument: `sutton2019bitter` (FW:232)
- Rhetoric: `lipton2019troubling` (FW:240). Queue volume is verified at FW:241 but marked unconfirmed at MM:110; cite
  the arXiv version or re-check.
- Compute and industry:
  - `ahmed2020dedemocratization` (MM:71)
  - `ahmed2023growing` (MM:77)
  - `abdalla2023elephant` (MM:89)
- Narrowing and values:
  - `klinger2020narrowing` (MM:83)
  - `birhane2022values` (MM:95)
- Paradigm shifts:
  - `gururaja2023build` (MM:39)
  - `saphra2024first` (CP:71)
- Entrants: `movva2024topics` (CP:64)

**Open questions.** Most of this literature is essays, interviews or descriptive trends (FW:308; CP:137). Open:
1. A topic-level test, registered in advance, of homogenisation.
2. Who builds benchmarks.
3. Whether marketing pays at the gate.
4. Whether entrants herd.

**Our findings in this conversation:**

| Our finding | Numbers (source) | Tier | Relation |
|---|---|---|---|
| FM adoption goes with fewer new-architecture papers | −7.98 / −11.0 (DC:271, 364). Variants 9/9; the hindsight check passes. | A | **supports** homogenisation (FW:270). **Extends** it to a lagged, topic-level, registered, held-out test. Cannot separate fad from efficient choice (FW:238). |
| Entrants seldom write benchmark papers | H2c′ (DC:297, 366) | A | **supports and extends** Koch et al.: benchmark building is concentrated, an insider activity (MM:105; FW:262) |
| Measurement papers on the rise | Share of dataset/benchmark and evaluation papers: 2.6% (2017) → 11.1% (2026) (DC:167) | E | **supports** the "benchmark culture" observation (MM:43) |
| Branding without a premium | See Conversation 1 (DP:106-133) | E\* / D\* | **complicates** Lipton and Steinhardt's worry that rhetoric pays (FW:246). Titles only; not re-run. |
| Entrants are numerous | Newcomer papers: 72.9% (DC:151) | E | **supports** Movva et al. (CP:69). We add contribution type and the gate. |
| FM papers accepted more often, and the premium does not shrink as adoption rises | +4.62 [+2.79, +6.44] (DC:342). Slope per logit unit of adoption: +0.19 [−0.96, +1.34] (DP:356). | D | **complicates** a pure fad reading of FMs, since a fad premium should fade. Caveat: the FM label is applied to partly camera-ready text (DP:362). |
| New architectures accepted relatively more where FMs dominate | +8.3 [+1.3, +15.4] (DC:349) | D | **complicates** "the gate enforces homogenisation" |

### Conversation 6: Peer review at ML venues (the gate)

**Core claim.** ML review is noisy and partly biased.
- Noise: about half of the papers one committee accepts, the other committee rejects.
- Identity and prestige matter at ICLR. Double-blind review reduced this but did not remove it.
- arXiv preprints leak author identity.
- Reviewers respond to signals about a paper's history.
- LLMs entered reviewing late in our window.

**Canonical verified works:**
- Noise:
  - `cortes2021inconsistency` (MM:133)
  - `beygelzimer2023has` (MM:139)
  - `shah2022challenges` (MM:145)
- ICLR studies:
  - `tran2020open` (MM:115; full author list unconfirmed)
  - `sun2022does` (MM:121, OUT:138)
  - `zhang2022investigating` (MM:127)
  - `bharadhwaj2020deanonymization` (CP:29)
  - `manzoor2021uncovering` (CP:43)
  - `kang2018dataset` (MM:151)
- Blinding and its limits:
  - `rastogi2022arxiv` (CP:36; first names missing)
  - `tomkins2017reviewer` (NR:280)
  - `stelmakh2021prior` (CP:50)
- LLMs in review:
  - `latona2024ai` (MM:169)
  - `liang2024monitoring` (MM:175)
- Proximity: `teplitskiy2018sociology` (NR:245)

**Open question.** Does a paper's position in a moving topic landscape relate to acceptance? Position here means its
entry status, its distance from its own team's record, and its timing in a wave. The question needs rejected and
withdrawn papers in view and a span across the FM transition (MM:245; CP:134).

**Our findings in this conversation:**

| Our finding | Numbers (source) | Tier | Relation |
|---|---|---|---|
| Position effects at the gate: far jump, insider, young rising keyword, post-peak fade | DC:370, 374, 375, 378 | B; A1 and PH6 weak | **extends** the question from author identity to the position of a paper |
| Newcomer gap mostly composition | DP:178-179 | D | **supports** the prestige-confounding caution (CP:159). Insider status may carry reputation via arXiv (CP:34). |
| Crowding and acceptance: uninformative | H3a −1.68 [−3.68, +0.32]; held-out −1.51 [−5.20, +2.19]; MDE80 4.8 pp (DC:324, 367) | C | **consistent with** noisy review: effects of a few points are below detection (MM:137, 143) |
| Withdrawal after review rises with maturity | +1.62 pp per log unit [+0.42, +2.81] (DC:344). RQ3 leaves out 9,986 withdrawn papers (DC:318). | D | **extends**: the gate selects through withdrawal as well as decisions |
| Post-2023 timing results fall in the LLM-review era | PH6 peaks 2019-2024 (DP:81). FL's gap appeared in 2024-26 (DP:220-222). | — | **complicates** the interpretation (MM:173, 179) |

### Conversation 7: Credible confirmatory meta-research (registering existing data; multiverse; forking paths)

**Core claim.** Committing to an analysis before seeing outcomes separates prediction from postdiction. This works
even for existing data.
- Multiverse and specification-curve analyses show how fragile a claim is.
- Forking paths make post hoc results exploratory.

**Canonical verified works:**
- Pre-registration:
  - `nosek2018preregistration` (ME:127)
  - `vandenakker2021preregistration` (ME:131)
- Multiverse and specification curves:
  - `steegen2016increasing` (ME:136)
  - `simonsohn2020specification` (ME:140)
- Forking paths: `gelman2014statistical` (ME:144; no issue number)
- Multiple testing and clustered inference:
  - `holm1979simple` (ME:149)
  - `cameron2008bootstrap` (ME:153)

**Open questions:**
1. These tools are rarely applied in science of science or in ACL "history of the field" papers (ME:201).
2. Standard multiverse lists omit time choices such as the fitting window (ME:210).

**Our findings in this conversation:**

| Our finding | Numbers (source) | Tier | Relation |
|---|---|---|---|
| A registered prediction failed, and its reversal then held on held-out papers | H2b/H2c → H2b′/H2c′ (DC:33-36, 296-297) | A | **supports** the value of registration (ME:129) |
| Single frozen run; sealed outcomes; held-out split | Run lasted 18 s at commit e08ece3 (DC:246). 11,099 held-out papers (DC:72). | E | **extends** Van den Akker et al. (ME:134). The held-out set is a split-sample replication, not an independent holdout (DC:43-45). |
| Honest size failure | Simulated null rejection rate: 12.6% / 10.0% at nominal 5%. The bootstrap did not fix it (12.4% / 9.6%) (DC:249-250). | E | **supports** the few-cluster warnings (ME:155) |
| What replicated and what did not | Replicated: H1d, H2b′, H2c′, E1, E4, teams H1, A1 (weak), premia b, EB D0, PH6 (weak). Not: P1b, P7, H4-FL, H3a (DC:364-378). | A–C | **supports** forking-paths logic (ME:147) |

### Cross-tab: our findings × conversations

Short labels in the cells:
- **S** = supports
- **X** = extends
- **Cx** = complicates
- **Ct** = contradicts
- blank = does not speak to it
- **C1 … C7** = Conversations 1-7 above

| Finding (tier) | C1 fashion/herding | C2 tradition/novelty | C3 outsiders/entry | C4 measurement | C5 ML self-critique | C6 ML review | C7 confirmatory |
|---|---|---|---|---|---|---|---|
| F1 Field waves and FM displacement (A/E) | S (package) | S (consolidation) | | X (survives hindsight) | S/X | | S |
| F2 Hindsight manufactures waves (E) | X | | | X/Ct | Cx (narrowing) | | X (temporal multiverse) |
| F3 Newcomers bring methods, not benchmarks (A, reversed) | Ct | Cx | S/X | X (survives) | S/X (Koch) | | S |
| F4 First-time teams not trend-chasers (E) | Ct | | Cx | | Cx | | |
| F5 Crowding and branding: no detectable reward (C/D\*) | Cx | | | Cx (H3a fails hindsight) | Cx (rhetoric) | S (noise) | S (uninformative) |
| F6 Timing: young keywords, PH6, FL (B weak / D–C) | X (weak); Cx (FL) | X (temporal) | | | | Cx (LLM era) | S (FL fails) |
| F7 Anchoring: far jump, insider (B) | S (Weisberg premise) | X | X | | | X | S |
| F8 Newcomer gap mostly composition (D) | | Cx | Cx | | | S (prestige caution) | |
| F9 Topic edges shrink (B) | Cx | | | X | | X | S |
| F10 FM premium; new architectures against the tide (D) | Cx | S | | | Cx | | |
| F11 Twins as volume (E; P2 acceptance D, mixed) | Cx/Ct | | | | | | |

---

## 3. The gaps: what no prior study we checked has done

### 3.1 Gap table (precise, with the closest prior work and the difference)

| # | Gap | Closest prior work (verified) | What they did | What we add | Honest limit |
|---|---|---|---|---|---|
| G1 | **Producers and gate in one complete population across a paradigm shift.** Who writes what kind of paper, and what the gate accepts, observed for every submission (including rejected and withdrawn) over ten years spanning the FM transition. | `foster2015tradition` (NR:99); `teplitskiy2022is` (NR:255); `tran2020open` (MM:115); `sun2022does` (MM:121) | Foster et al.: producer strategies; citations and prizes; published biomedical papers. Teplitskiy et al.: review files incl. rejected manuscripts at 49 journals; reference-based novelty. Tran et al.: ICLR 2017-20, identity bias. Sun et al.: 5,027 ICLR papers, blinding. | Entrants' contribution types plus position effects at the gate in the same corpus: 43,480 discovery + 11,099 held-out (DC:65, 72); 2017-2026. | "Rejected papers visible" is **not** new in itself. Teplitskiy 2022 (journals), Boudreau 2016 (grants) and Tran 2020 (ICLR) all see them. What is new is the combination. One venue only (DC:56). |
| G2 | **What kind of contribution entrants bring.** | `movva2024topics` (CP:64); `anderson2012towards` (MM:33); `pramanick2023diachronic` (MM:45); `prabhakaran2016predicting` (CP:57); `koch2021reduced` (MM:101) | Movva: entrants numerous in LLM work; descriptive; arXiv. Anderson: people flows; published papers. Pramanick: methods drive, datasets follow; no split by entry status. Prabhakaran: rhetorical roles predict rise and fall. Koch: benchmark concentration. | Newcomer vs incumbent contribution type within topic-year. The registered herding prediction reversed, then held out-of-sample (DC:296-297, 365-366). First-time teams' outcome-free adoption profiles (DP:315, 360). | Contribution type is not novelty (DC:313-314). Labels are LLM labels (DC:52). "Newcomer" = new to the topic *at ICLR*. The 2021 ID switch biases incumbency towards zero (DC:144-149). |
| G3 | **Pivot and chaperone patterns at the acceptance decision, under double-blind review, with a held-out test.** | `hill2025pivot` (NR:329); `sekara2018chaperone` (OUT:60); `arts2018paradise` (OUT:66); `boudreau2016looking` (NR:217) | Hill: citations; reportedly also lower publication success for larger pivots (NR:335). Sekara: new PIs at top journals. Arts and Fleming: patents; experts soften the loss. Boudreau: grant scores; intellectual distance. | Distance from the team's own ICLR record, and one insider vs none, against the decision on every decided submission, replicated on held-out papers (DC:370, 372, 374). | Hill et al. **already** touch the publication stage, so do not claim "first at acceptance". ICLR record only since 2021 (DP:249). Selection into teams (DP:297). Insider vs proven-record ambiguity (DP:292-296). |
| G4 | **Measuring hindsight distortion.** Same papers and model; only the fitting window varies. | `leydesdorff2002dynamic` (ME:77); `klavans2014creation` (ME:72); `glaser2017same` (ME:87); `held2021challenges` (ME:92); `rotolo2015what` (ME:64) | Leydesdorff: conceptual. Klavans and Boyack: a dynamic model for planning. Gläser et al. and Held et al.: method dependence on a fixed period. Rotolo et al.: emergence attributes judged after the fact. | 29 vs 8 emerging topics; 13 vs 26 declining; a trend conclusion reverses; forecastability R² 0.28 vs −0.03 (DC:176-231). | Maps also differ in fitting corpus, so the gap "cannot be attributed to hindsight alone" (DC:229). The early map cannot see topics born after 2020. One venue. ME and CP searches were budget-limited (ME:9; CP:7). |
| G5 | **A topic-level, registered, held-out test of FM displacement.** | `bommasani2021opportunities` (FW:264); `gururaja2023build` (MM:39); `saphra2024first` (CP:71); `klinger2020narrowing` (MM:83); `hooker2021hardware` (FW:224) | Essays, interviews, position papers, or descriptive topic-model trends | Lagged FM adoption, topic and year fixed effects, 9/9 variants, held-out −11.0 (DC:271, 364) | An association, possibly with reverse causality. An "adapter on an LLM" is labelled method (DC:283-284). Cannot separate fad from efficient choice. |
| G6 | **How a wave's reward evolves at the gate over the wave's life.** | `abrahamson1999management` (FW:31); `newman2009first` (NR:295); `strang2001search` (FW:39); `sjogarde2022association` (ME:100) | Abrahamson and Fairchild: discourse upswing/downswing. Newman: first-mover citations. Strang and Macy: a simulation model. Sjögårde and Didegah: topic growth vs citations. | The acceptance gap before vs after a keyword's peak, and the young-rising premium (DC:375, 378) | **Weak.** p 0.043, and −1.7 (p 0.33) without the six keywords inspected first (DP:50-51). A1's CI includes 0 (DP:48-49). Not a headline. |
| G7 | **A confirmatory design for a science-of-science question at an ML venue.** | `vandenakker2021preregistration` (ME:131); `nosek2018preregistration` (ME:127) | Templates and arguments | Sealed outcomes, a single frozen run, registered held-out tests, a size failure reported openly (DC:237-262) | The held-out split is not a certified independent holdout; the splits share years, reviewers and authors (DC:43-45) |

### 3.2 Gap statement for the paper (draft wording; every claim traceable)

Prior work describes ML's research waves in one of two ways:
- **From the outside**, by fitting topic models to published papers with hindsight.
- **From the gate**, by testing whether reviewers favour prestigious authors.

Among the works we checked, none joins the two. Joining them means asking:
- whether the waves survive measurement without hindsight;
- who carries them into a topic, and with what kind of contribution;
- what peer review rewards as they rise and fade.

The theories that would predict an answer come from citations, journals, patents and grants. Herding and fashion
theory predicts imitators. The pivot penalty, the chaperone effect and the first-mover advantage predict rewards for
proximity and timing. None of these comes from the full submission stream of a fast-moving ML venue.

### 3.3 Possibly closer prior work that must be checked before any novelty claim (unverified; do not cite yet)

| Candidate | Why it matters | Where seen |
|---|---|---|
| "What Have We Learned from OpenReview?" arXiv 2103.05885 | ICLR 2017-2020; area popularity and acceptance. Could be closest on topic popularity × acceptance. | CP:117 |
| "Persistence Paradox in Dynamic Science" arXiv 2506.22729 | Incumbents vs adapters during the deep-learning shift | CP:118 |
| Heo et al. / Jung et al., EMNLP 2026, "What Drives Paper Acceptance?" | ICLR 2017-2025, more than 28,000 submissions; process factors. Author order unresolved. | NR:430-435 |
| "Reviewer Scores Are Not Comparable Across Research Areas in ML Peer Review" arXiv 2607.27209 | Could explain persistent topic edges (premia b) | CP:119 |
| "Bias at the Borderline" arXiv 2607.26280 | ICLR borderline prestige effects. Rival explanation for the insider premium. | MM:225; CP:123 |
| "Breaking New Ground, Reinforcing Old Gaps" arXiv 2404.04707 | Same incumbent/newcomer operationalisation (PubMed) | CP:120 |
| Stelmakh et al., RCT on herding in review discussions (arXiv 2011.15083) | Reports no herding among *reviewers*. Would sharpen "herding is not where conformity lives". | FW:285 |
| 2025 PeerJ CS paper on emergence detection by static topic models | Very close to the hindsight point | ME:170 |
| Vicinanza et al. 2023, PNAS Nexus | Prescient ideas come from the periphery | OUT:206 |
| Fischhoff 1975 (hindsight bias); Kerr 1998 (HARKing) | Vocabulary anchors for hindsight and post hoc claims | ME:163-165 |

### 3.4 What we must NOT claim as new

These already exist in the literature:
- ICLR OpenReview as a data source (`kang2018dataset`, `tran2020open`, `zhang2022investigating`).
- That review is noisy (`cortes2021inconsistency`, `beygelzimer2023has`).
- Prestige effects (`sun2022does`, `bharadhwaj2020deanonymization`).
- FM growth and homogenisation as ideas (`bommasani2021opportunities`).
- Topic-model histories (`hall2008studying`).
- That entrants are numerous (`movva2024topics`).
- That the pivot penalty and chaperone effect exist (`hill2025pivot`, `sekara2018chaperone`).
- That rejected submissions are visible in evaluation studies (`teplitskiy2022is`, `boudreau2016looking`).

"First" claims must read "to our knowledge, among the works we checked". The closest-prior search stopped after 10 of
its planned searches (CP:7).

---

## 4. Candidate story lines

The findings, as used in every fit table below:

| ID | Finding | Numbers (source) | Tier |
|---|---|---|---|
| F1 | Field-level waves and displacement | Growth ×40.1; 69.3% of the corpus from 2024-26 (DP:71-72). FM 0.3% → 54.4%; new architectures 24.5% → 7.5% (DC:163-164). 17 of 68 keywords rose and fell (DP:81). H1d −7.98 / −11.0 (DC:271, 364). | E; H1d A |
| F2 | Hindsight measurement | 29 vs 8 emerging topics; lifecycle flip; R² 0.28 vs −0.03 (DC:176-231) | E |
| F3 | Newcomers bring methods, not benchmarks | DC:296-297, 365-366 | A, reversed |
| F4 | First-time teams not trend-chasers | DP:315, 360-362; newcomer papers less often twinned (DP:275) | E |
| F5 | Crowding and branding not rewarded | H3a: C, uninformative (DC:324, 367). Branding ratio 1.02 (DP:133). | C; D\* |
| F6 | Timing | A1 (B weak; DC:375). PH6 (B weak; DP:389-397). FL (D/C; DC:368-369). | — |
| F7 | Anchoring | Far jump (B; DC:370). Within-author closeness (B; DC:372). One insider (B; DC:374). | B |
| F8 | Newcomer acceptance gap mostly composition | −10.2 → −3.1 within authors; −1.4 for an author new to the topic (DC:343; DP:178-179) | D |
| F9 | Topic edges shrink | Premia b 0.38 / 0.60; EB D0 (B; DC:376-377). Keyword units 0.16 n.s. (DP:52-53). | B |
| F10 | FM premium | +4.62 (D; DC:342), stable across adoption (D; DP:356). E8: new architectures +8.3 against the tide (D; DC:349). | D |
| F11 | Twins as volume | 19.5% → 48.8% of papers twinned, but per-pair rate 0.32 → 0.19 (E; DP:78-79). P2 acceptance mixed: discovery +0.68, held-out +3.69 (unregistered), pooled +1.86 (DP:36-41). | E; D |

Fit labels: **core** = load-bearing; **support** = strengthens the line; **context** = background only; **awkward** =
needs explaining, or cuts against the line.

### Candidate 1: "Anchored, not herded" — where conformity lives in a fast-moving field (RECOMMENDED)

**Thesis.** ML's foundation-model wave is not a herd. Measured without hindsight:
- the convergence that survives is a shared technical package displacing new architectures;
- the people entering topics bring new methods rather than follow-on work;
- the review gate goes with continuity, not crowd-following. Continuity here means staying near the team's own record
  and having a topic insider, plus, weakly, arriving early.

**Conversations and why it is novel.**
- **Conversation 1 (fashion and herding)** and **Conversation 5 (ML self-critique)** both treat trend-following as the
  default reading of ML's waves. We registered that reading ourselves, and it failed in the opposite direction.
- **The conceptual contribution** is to separate two routes to conformity:
  - imitating others: cascades and fashion (FW:61, FW:27);
  - staying anchored in one's own and one's topic's record: Weisberg's risk-avoiding clustering (FW:79), the pivot
    penalty (OUT:78), the chaperone effect (OUT:64).

  The literature runs these together. Our data separate them. There is no evidence for the first among entrants, and
  no detectable reward for it at the gate. The second is rewarded at the gate.
- **For Conversation 2**, this places the conservative pressure on the evaluator side, as a premium on continuity
  rather than a penalty on novelty. This complements Foster et al., who find conservatism on the producer side (NR:111).
- **For Conversation 4**, the first step of the argument doubles as a measurement lesson: hindsight maps make a field
  look more faddish than it was.
- **Novelty.** Among works checked, no study tests the herding account of a field at all three points: measurement,
  entry and the gate. None does so with all submissions, maps without hindsight, and registered held-out tests (G1, G2,
  G4).

**How every finding fits:**

| Finding | Role under this line | Fit |
|---|---|---|
| F1 | Act 1. The convergence that survives hindsight and held-out testing is a package shift (Fujimura's package bandwagon; FW:113), not imitation per se. | core |
| F2 | Act 1. Retrospective maps inflate the appearance of fashion: 29 vs 8 emerging topics; a trend conclusion flips. | core |
| F3 | Act 2. The registered herding prediction reversed: entrants propose, incumbents consolidate. This is the hook. | core |
| F4 | Act 2. Entrants are slower to take up trending keywords and FMs, and less often twinned. | support |
| F11 | Act 2. Duplication rises with volume, not with herding per pair. | support |
| F5 | Act 3. No detectable reward for following the crowd. Must be worded as "no detectable premium", never "no effect" (DC:332). | support |
| F9 | Act 3. Topic acceptance edges regress (0 < b < 1). Picking a favoured topic is not a reward that keeps paying in full. Echoes Act 1's lesson that apparent signals shrink when measured out of time. | support |
| F7 | Act 3. The positive half: continuity with the team's own record, and one topic insider. | core |
| F8 | Act 3. The incumbency gap is mostly accumulated experience. The small within-person cost of entering a new topic (−1.4) mirrors the far-jump penalty. | support |
| F6 | Act 3. Earliness is favoured; late riders are not. Weak (B weak). FL is the cautionary tale: the vivid fad case did not replicate. | support (weak); FL is a caution |
| F10 | Discussion. A premium for the package that does not shrink with adoption looks less like a fad (cf. Sutton; FW:238). Against-the-tide architectures are not penalised. All D. | context / awkward |

**Weak or awkward for this line:**
- **The "flocking" half of herding is untested.** H2a is inconclusive (C; DC:295), and newcomer × hot is n.s. (DC:307).
  We can say what entrants write and how fast they adopt trends; we cannot say whether they crowd into hot topics.
- **A method paper is a contribution type, not novelty** (DC:313-314). The claim must be that entrants write proposals
  rather than follow-on measurement, which is exactly the registered herding prediction. It must not be "entrants are
  more innovative".
- **H2c′ shrinks with team size** (−0.54, p 0.07; DC:301). Part of the benchmark gap is a matter of team composition.
- **Some findings can be read as "riding pays":**
  - the FM premium (+4.62, D);
  - the held-out twin row (P2: +3.69, unregistered; DP:267-268);
  - young rising keywords (A1).

  Answer: A1 rewards being *early*, not following; the twin result is mixed and unregistered; the FM premium is D.
- **The insider premium may reflect a proven record rather than topic tradition.** Per head, an insider is worth about
  as much as a crossover author (+0.58, p 0.16), and familiarity without an earlier acceptance is worth +0.2 (DP:292-296;
  D). This means "anchoring" may be partly cumulative advantage (`merton1968matthew`, `price1976general`). Define
  anchoring to cover both readings.
- **Branding** is D\*: an earlier exploratory result, not re-run (DP:133).

**Overclaiming risks:**
- "ML is not a herd" over-generalises. Say "the herding account fails the tests we registered, at one venue".
- "The gate enforces convergence" is causal. Say "acceptance goes with continuity".
- The mechanism is unknown. Reviewer conservatism and better-informed, better-made papers (Li 2017; NR:240) are both
  live readings.
- arXiv can de-anonymise authors (CP:34, 40).
- The word "anchoring" collides with the cognitive-bias term. Define it at first use as "continuity with one's own and
  one's topic's record". "Continuity" is a fallback.
- Hindsight results are bracketed, not pinned down (DC:187).
- The held-out split is not independent (DC:43-45).

### Candidate 2: "The essential tension at the gate" — novelty is rewarded when anchored

**Thesis.** At a selective ML venue, what goes with rejection is not novel content but unanchored novelty: work far
from the team's own record, without a topic insider, or late in a wave. Meanwhile topic entrants supply the method
proposals.

**Conversation and novelty.** Conversation 2 (Kuhn; Foster; Uzzi; Wang; Boudreau vs Teplitskiy; Hill).
- It separates three kinds of "novelty" in one population: contribution type, biographical distance and temporal
  position. It proposes that these are received differently, which could reconcile the contested novelty penalty
  (NR:481-483).
- It fits the current draft's umbrella (draft lines 107-113).

**How every finding fits:**
- **F3** (divergent side) and **F7** (biographical and social anchoring): core.
- **F6**: temporal anchoring. Core, but weak.
- **F8**: anchoring as experience. Support.
- **F5**: popularity signals unrewarded. Support.
- **F1**: Kuhnian normal science and consolidation. Context.
- **F10**: work inside the paradigm is rewarded. Support. But E8 (against the tide also rewarded) is awkward.
- **F2**: a method caveat, outside the frame. Context.
- **F4**: awkward. Entrants innovate in type but are *not* early on trending keywords, so they are not "temporal
  innovators".
- **F9**, **F11**: context.

**Weak or awkward:**
- The "content novelty is not penalised" leg rests on P1a (D) and on P1b/P7 (C: not replicated, not supported)
  (DP:257-266). Without it, the reconciliation claim fails.
- Equating method papers with innovation (DC:313-314).
- "Essential tension" is broad enough that almost any result fits. Reviewers may see it as a theme, not a thesis. This
  is close to what the supervisor criticised.

**Overclaiming risks:**
- Calling far jumps "novelty". A far jump is distance from oneself, not novelty to the field.
- Claiming to reconcile Boudreau and Teplitskiy on D/C evidence.
- Implying that innovation is undervalued.

### Candidate 3: "A newcomer–novelty paradox at the gate"

**Thesis.** Topic entrants supply ML's method proposals and incumbents its benchmarks, yet acceptance favours
incumbents and insider ties. This would be a topic-level version of the diversity–innovation paradox.

**Conversation and novelty.** Conversation 3 (Hofstra; Arts and Fleming; Merton 1968). It moves the paradox from
demographic margins to topic margins (OUT:235).

**How every finding fits:**
- **F3**: core.
- **F7**: core.
- **F8**: core, but it undermines the line, because the gap is mostly composition (−3.1 within authors).
- **F4**: support (entrants are not imitators).
- **F1**, **F2**: context.
- **F5**, **F6**, **F9**, **F10**, **F11**: peripheral.

**Weak or awkward:**
- The paradox's reward half is E2 (D) and PH3 (D). PH3 shows most of the gap is who writes the paper.
- ICLR has been double-blind since 2018, so "discounting" by reviewers is hard to argue.
- Contribution type is not novelty.

**Overclaiming risks:**
- It implies reviewer bias against newcomers. PH3 shows the gap is mostly composition, and PH3 itself warns the
  residual "need not be reviewer bias" (DP:181-183).
- It builds the headline on D-tier evidence.
- It carries ethical overtones.

### Candidate 4: "Writing a field's history without hindsight"

**Thesis.** A topic map describes the years it was fitted on. Histories of ML and NLP that fit one map on all years
leak the future into the past: emerging topics are inflated (29 vs 8) and life-cycle conclusions flip. A dated,
registered, held-out design shows which wave stories survive.

**Conversation and novelty.** Conversation 4 (Hall; Griffiths and Steyvers; Anderson; Pramanick; Klinger; BERTopic;
Leydesdorff; Rotolo; Kaufman; Kapoor and Narayanan) and Conversation 7. Among the works checked, no study quantifies
hindsight distortion holding papers and model fixed (ME:174). This is very ACL-native.

**How every finding fits:**
- **F2**: core.
- **F1**: core. FM displacement survives hindsight.
- **F3**: survives (support).
- **F5**: H3a fails the hindsight variants (support).
- **F6**: FL does not survive held-out testing (support).
- **F7**: survives held-out testing (support).
- **F9**: apparent premia regress (support).
- **F4**, **F8**, **F10**, **F11**: listed as "sorted" items (context).

**Weak or awkward:**
- The headline is tier E. It covers one venue, and the maps differ in corpus as well as window (DC:229).
- The forecast comparison has no paired test.
- Most acceptance findings do not depend on topic maps at all (far jump uses cosine; A1 and PH6 use keywords).
- The substantive results become a sorted list, which is the presentation's failure mode again.

**Overclaiming risks:**
- "Manufacture" when the corpus confound exists.
- "First" when the search was budget-limited.
- Turning an ACL long paper into a methods note with substance appended.

### Candidate 5: "Fashion is in the verdict, not in the map"

**Thesis.** ML's topic waves are partly artefacts of hindsight maps, but a fashion signature appears in the gate's
verdict: young rising ideas are favoured, and the premium sours after a wave peaks.

**Conversation and novelty.** Conversation 1 (Abrahamson and Fairchild; Strang and Macy; Newman; Merton 1957). It
would be the first gatekeeper-side measure of a fashion's upswing and downswing (FW:303, 311).

**How every finding fits:**
- **F2**: core.
- **F6**: core.
- **F5**: support.
- **F7**: support.
- **F9**: support.
- **F3**: support (not imitators).
- **F11**: support.
- **F1**: context.
- **F10**: awkward. The FM premium is stable rather than souring.
- **F8**: peripheral.

**Weak or awkward:** the headline rests on the weakest tier.
- A1's CI includes 0 (DP:48-49).
- PH6 has p 0.043 and drops to −1.7 (p 0.33) without the six keywords inspected first (DP:50-51).
- FL is not confirmed.

**Overclaiming risks:** high. A reviewer can dismantle the headline with the DP:50-51 row alone.

### Candidate 6: "Bridging, not jumping" — science-of-science reward rules at the review gate

**Thesis.** The proximity rules that science of science found in citations and journal careers already go with the
acceptance decision at a double-blind ML venue, out of sample. These rules are the pivot penalty and the chaperone
effect. They also account for most of the newcomer gap.

**Conversation and novelty.** Conversation 3 (Hill; Sekara; Arts and Fleming; Cattani and Ferriani; Packalen and
Bhattacharya; Guimerà) and Conversation 6. The novelty is G3: the decision, every decided submission, a held-out test.

**How every finding fits:**
- **F7**: core.
- **F8**: core (the gap is mostly who; −1.4 within person).
- **F3**: support (entrants propose).
- **F6**: timing as a first-mover analogue (support, weak).
- **F1**, **F2**: context.
- **F4**, **F5**, **F9**, **F10**, **F11**: peripheral.

**Weak or awkward:**
- Hill et al. reportedly already find lower publication success for larger pivots (NR:335), so the novelty is narrower
  than it looks.
- Insider ≈ crossover (DP:294-296).
- The far-jump measure correlates −0.57 with the newcomer flag (DP:247).
- Selection into teams.

**Overclaiming risks:**
- "Remedy" or advice language, such as "add an insider". The shortlist forbids advice (DC:427; DP:298).
- A causal reading.
- It leaves the A-tier field results and the hindsight result as side notes, wasting the strongest material.

### Candidate 7: "Normal science arrives" — a paradigm package reorganises a field

**Thesis.** As the foundation-model package spreads topic by topic, ML shifts from building architectures to working
inside the package: new-architecture papers fall where FM adoption is high. Meanwhile entrants keep proposing methods,
and the gate does not penalise the scarce alternative.

**Conversation and novelty.** Conversations 2 and 5 (Kuhn 1962; Fujimura; Bommasani; Park et al.; Gururaja; Saphra;
Hooker vs Sutton). G5 gives the first registered, held-out, topic-level test among works checked.

**How every finding fits:**
- **F1**: core (A).
- **F10**: core, but D.
- **F3**: support.
- **F2**: support (how big the shift looks depends on the map).
- **F4**: awkward but interesting. First-time teams adopt FMs *less*.
- **F5**, **F6**, **F7**, **F8**, **F9**, **F11**: peripheral. The acceptance results hang loosely.

**Weak or awkward:**
- Only H1d is tier A. E8, E1 and fmwave are D.
- Fad vs efficient choice cannot be separated (FW:238).
- Possible reverse causality (DC:283).

**Overclaiming risks:**
- "Crowds out" or "revolution" language.
- Kuhnian claims we cannot observe (NR:33: "we do not observe revolutions").

### Comparison at a glance

| Candidate | Load-bearing tiers | Findings with a real role (of 11) | Novelty | Overclaim risk | ACL fit | Science-of-science fit |
|---|---|---|---|---|---|---|
| 1 Anchored, not herded | A + B + E | 10 (F10 in the discussion) | High: herding tested at three points; two routes to conformity separated | Medium; controllable with wording | High (computational histories, LLM-era field) | High (herding, essential tension, pivot/chaperone) |
| 2 Essential tension at the gate | B (+ D for the content-novelty leg) | 8 | Medium (reconciliation rests on D/C) | Medium-high | Medium | High |
| 3 Newcomer–novelty paradox | A + D | 5 | Medium | High (bias implication) | Low-medium | Medium |
| 4 History without hindsight | E + A | 6, mostly as a sorted list | High on one point | Medium | High | Low-medium |
| 5 Fashion in the verdict | B weak + E | 7 | High if true | High | Medium | Medium |
| 6 Bridging, not jumping | B + D | 5 | Medium (Hill touches the stage) | Medium (advice risk) | Low-medium | High |
| 7 Normal science arrives | A + D | 5 | Medium | Medium | Medium-high | Medium |

---

## 5. Recommendation: Candidate 1, "Anchored, not herded"

### Why this line, for a demanding ACL reviewer

1. **One falsifiable account, tested at three points, not three research questions.** The paper tests the herding
   account of ML's waves:
   - in how waves are measured;
   - in who rides them;
   - in what the gate pays for.

   Each section is one prediction of the same account, and each failure points to the same alternative. This answers
   the supervisor's criticism directly.
2. **It starts from a registered failure.** The headline people result is our own herding prediction coming out in the
   opposite direction and then holding on held-out papers (DC:296-297, 365-366). ACL reviewers trust a prediction that
   failed and was reported more than a story fitted after the fact (ME:129).
3. **It carries a lesson for the ACL genre.** Every NLP/ML field history we checked fits topics on the whole period
   (MM:244): Hall et al., Anderson et al., Prabhakaran et al., Pramanick et al., Klinger et al., and BERTopic-style
   trend studies. Act 1 shows this inflates the impression of fashion (29 vs 8) and offers a cheap check. NLP methods
   are central:
   - SPECTER2 topics;
   - an LLM codebook with κ 0.93 (DC:133);
   - keyword canonicalisation.
4. **Load-bearing claims sit on the strong tiers.** A: H1d, H2b′, H2c′. B: far jump, within-author closeness, insider,
   premia. E: hindsight. The weak results (A1, PH6) and the failed ones (FL, P1b) appear with their tiers. They support
   or caution; they do not carry the thesis.
5. **It speaks to an LLM-era debate the ACL audience cares about.** Is the field a hype-driven herd? This comes from
   Lipton and Steinhardt, Hooker, Dehghani et al., Bommasani et al., Gururaja et al. and Movva et al. (Conversation 5).
   The answer is nuanced: real convergence on a package (supports Bommasani), but no evidence of entrant herding and no
   detectable reward for following.

### Why this line, for a science-of-science reviewer

1. **A conceptual distinction the literature lacks.** The paper separates imitating others (cascade and fashion theory;
   FW:61, FW:27) from staying anchored in one's own and one's topic's record. The anchoring side covers:
   - Weisberg's risk-avoidance clustering (FW:79);
   - the pivot penalty (OUT:78);
   - the chaperone effect (OUT:64).

   Our data separate the two: imitation is not evident among entrants and not detectably rewarded; continuity is
   rewarded at the gate.
2. **It locates conservatism.** Foster et al. find conservatism in producers' strategies (NR:111). Teplitskiy et al.
   2022 find no penalty on content novelty at journals (NR:263). Hill et al. find a penalty for moving away from
   oneself (NR:333). In one complete population at one venue, we observe:
   - producers who are not conservative where it matters: entrants propose;
   - a gate whose premium is for continuity (B) rather than a penalty on field novelty (P1a, D: weak and consistent).
3. **It moves known reward rules to the decision stage and replicates them out of sample.** The rules are the pivot
   penalty and the chaperone effect (B), and they are reframed as two sides of continuity. Hill et al.'s note on
   publication success (NR:335) must be acknowledged.
4. **The design is rare in the field:**
   - registered hypotheses;
   - a single frozen run;
   - held-out replication;
   - an openly reported size failure (DC:249-250).

### How to organise the paper under this line

This replaces the "RQ1/RQ2/RQ3" structure of the current draft.

- **Title options** (the third keeps the current title's question):
  - "Anchored, Not Herded: Who Rides Machine Learning's Research Waves, and What Review Rewards"
  - "Waves Without Herds: Entry, Continuity and Review at ICLR, 2017-2026"
  - "Riding the Wave? Anchoring, Not Herding, in Machine Learning Research during the Foundation-Model Shift"
- **Introduction:**
  - ML is widely described as following trends. Herding and fashion theory predicts imitating entrants and rewards
    for riding waves.
  - We test that account at three points.
  - Thesis sentence.
  - Three contributions:
    1. conceptual: imitation vs continuity;
    2. measurement: hindsight inflates waves;
    3. evidence: registered and held-out, with tiers.
- **Background (one paragraph per side):**
  - herding and fashion (Conversation 1), with ML's self-critique (Conversation 5);
  - continuity and anchoring (Conversations 2 and 3);
  - computational histories (Conversation 4).
- **Data and design:** corpus, measures, tiers, protocol (Conversations 6 and 7).
- **§4 "Are the waves what they seem?"**
  - F2: hindsight.
  - F1: FM displacement survives.
- **§5 "Who rides the wave?"**
  - F3: reversed herding prediction.
  - F4: first-time teams.
  - F11: twins as volume.
  - H2a as an open limit.
- **§6 "What does the gate pay for?"**
  - Following: F5 and F9. No detectable premium; edges regress.
  - Continuity: F7 and F8.
  - Earliness: F6. A1 and PH6 are weak. FL is a caution.
  - F10 goes to the discussion only.
- **Discussion:**
  - where conformity lives;
  - two mechanisms for continuity, expertise vs bias (Li 2017), not separable here;
  - what this means for writing field histories and for debates on ML hype;
  - limits.
- **Table 1:** recast from the RQ grouping into a scorecard with columns: prediction of the herding account /
  prediction of continuity-plus-package / observed / tier. Every row is already in DC:364-378 and DP:429-454, for
  example:
  - "entrants write follow-on measurement" vs "entrants propose" → H2b′/H2c′ (A);
  - "duplication per pair rises" vs "volume" → 0.32 → 0.19 (E);
  - "crowded topics or branded titles rewarded" → H3a C, ratio 1.02 D\*;
  - "distance from own record is irrelevant" vs "penalised" → −5.44 / −6.09 (B);
  - "late riders gain" vs "early only" → PH6 (B weak).

### Draft thesis and contribution sentences

Every number below is checked against the dossiers.

- **Thesis:** "At ICLR, machine learning's foundation-model wave is real but is not a herd: the convergence that
  survives measurement without hindsight is a shared technical package, newcomers to a topic bring new methods rather
  than follow-on benchmarks, and acceptance goes with continuity — staying near a team's own record and having a topic
  insider — rather than with following the crowd."
- **C1 (conceptual):** "We separate two routes to conformity — imitating others and staying anchored in one's own
  record — and find evidence against the first and for the second."
- **C2 (measurement):** "Topic maps fitted with hindsight inflate a field's waves (29 vs 8 emerging topics on the same
  papers) and can reverse trend conclusions; we give a cheap check."
- **C3 (evidence):** "We test registered predictions once on 43,480 submissions, including rejected and withdrawn
  papers, and replicate them on 11,099 held-out papers, labelling every finding by its evidence tier."

### Wording guardrails (from the dossiers; non-negotiable)

**Language:**
- Associations only; never "causes", "choose" or "should" (DC:42, 48, 427).
- No advice, e.g. "add an insider" (DP:298).

**Held-out wording:**
- "A pre-registered out-of-sample replication, not a certified untouched holdout" (DC:43-44).
- Supported held-out tests confirm direction, not size (DC:47).

**Nulls:**
- Underpowered nulls are "uninformative", not "no effect" (DC:46, 426).
- Crowding: "no detectable premium" (DC:332).

**Definitions:**
- Method paper = contribution type, not novelty (DC:313-314).
- Newcomer = no author with an earlier ICLR submission in that topic (DC:53).

**Quoting rules:**
- FL: "not confirmed" (DC:55).
- P1b: "did not replicate" (DC:54).
- A1: say the CI includes 0 (DP:48-49).
- PH6: say it leans on six inspected keywords (DP:50-51).
- P2 and E2 rules (DP:36-41).
- No cross-module comparisons of effect size (DC:428).

**Labels:** they are LLM labels, not human labels (DC:52).

**Novelty claims:** say "to our knowledge, among the works we checked" (CP:160).

### Open checks before the writers start

1. **Insider definition.** The teams module's definition is not stated in the dossiers. Check RESULTS.md (teams
   section) whether an insider needs an earlier *accepted* paper in the topic. This decides whether "anchoring" means
   topic knowledge or a proven record (DP:292-296).
2. **"First-time team" definition** in the kwtiming and fmwave modules (DP:313-315, 360).
3. **Hill et al. 2025's claim on publication success** (NR:335). It narrows G3; read the abstract.
4. **Direction of the distance effect in Boudreau et al. 2016** (OUT:122 vs NR:223-225).
5. **Lipton and Steinhardt's Queue volume** (FW:241 vs MM:110).
6. **The Section 3.3 candidates.** Arxiv 2103.05885 and 2506.22729 come first; either could narrow G1 or G2.
7. **Branding ratio 1.02 is D\*,** earlier exploratory and not re-run. Either present it as such, or drop it from the
   scorecard.
8. **Bibliographic gaps:**
   - Crane 1969's end page;
   - Foster et al. 2015's end page;
   - Hill et al. 2025's fourth author;
   - Fortunato et al.'s middle authors;
   - Rastogi et al.'s first names;
   - Tran et al.'s author list.
