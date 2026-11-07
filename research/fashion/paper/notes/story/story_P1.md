# Story P1: "Anchored, not herded", strongest version

Story-design file for the ICLR 2017-2026 paper (ACL ARR long paper, 3,000-4,000 body words). Built 2026-11-03. It
develops landscape.md Candidate 1 using theory_anchors.md, verify_prior.md and the new content-novelty analysis.
It is a design, not the paper: it fixes the thesis, the argument, the table, the figures and the honest limits, and
gives only the sentences whose exact wording matters (thesis, abstract, gap, guardrails).

## 0. Sources and conventions

**Read in full:** dossier_core.md, dossier_posthoc.md, landscape.md, theory_anchors.md, verify_prior.md, the current
draft `research/fashion/paper/riding_the_wave_paper.tex`, and `paper_ws/output/novelty_newcomer.json` (the file
`analysis_novelty.md` does not exist; the novelty agent could not write it). Also read, for single facts:
- the lit_*.md notes for Weisberg 2013, Fujimura 1988, Sutton 2019, Lipton and Steinhardt 2019, Movva et al. 2024,
  Foster et al. 2015, Li 2017, Teplitskiy et al. 2022 and Sekara et al. 2018;
- PREREGISTRATION.md lines 1053, 1111-1112, 1281, 1366-1380, 1569 and 1659 (variable definitions only);
- committed aggregate files, to check that each planned figure has a source (names in Section 7).

No outcome column or decision column of any data file was read, and no analysis script was run. No corpus author is
named.

**One open check closed here.** verify_prior.md item 7 asked which embedding the far-jump measure uses. It is SPECTER2:
"x_p is the SPECTER2 vector (title [SEP] abstract), centred with `output/specter2_centring_mean.npy` and L2-normalised"
(PREREGISTRATION.md line 1372). So "our closeness measure, like Bao and Li's (2025), uses SPECTER2 similarity" is
accurate. Field novelty (DP:255) and the new content-novelty analysis use the same centred SPECTER2 vectors.

**Pointers.**

| Pointer | File |
|---|---|
| `DC:n` | dossier_core.md, line n |
| `DP:n` | dossier_posthoc.md, line n |
| `LS:n` | landscape.md, line n |
| `TA:n` | theory_anchors.md, line n |
| `VP:n` | verify_prior.md, line n |
| `NN:key` | `paper_ws/output/novelty_newcomer.json`, `results.key` (this session's workspace; not committed) |
| `PRE:n` | `research/fashion/PREREGISTRATION.md`, line n |
| `FW:n`, `CP:n` | lit_fashion_waves.md and lit_closest_prior.md, line n (as in landscape.md) |

**Tiers** (DC:25-31; DP:12-19): **A** registered and replicated on held-out papers; **B** post hoc in discovery, then
a held-out test declared before the held-out run supported it; **C** registered but inconclusive or not replicated;
**D** discovery only; **E** descriptive, no acceptance outcome; **E\*/D\*** earlier exploratory title analysis
(E\* share re-verified; D\* acceptance ratio not re-run). In the paper every finding carries its tier in square
brackets right after its number, e.g. "−6.09 pp [B]".

---

## 1. Title and thesis

### Title

**Anchored, Not Herded: Conformity at ICLR during the Foundation-Model Wave**

Alternatives, in order of preference:
1. "Waves without Herds: Entry, Continuity and Review at ICLR, 2017-2026"
2. "Anchored, Not Herded: Who Enters Machine Learning's Research Waves, and What Acceptance Goes With"

The title says "at ICLR" on purpose: the claim is about one venue (DC:56), and the guardrail "ML is not a herd
over-generalises" (LS:579) is met in the title itself.

### Thesis (the story line, one sentence)

> At ICLR during the foundation-model wave, the field converged, but the conformity we can detect is continuity, not
> imitation: topic entrants, whom the herding account casts as imitators, bring method proposals and content farther
> from earlier work, and acceptance goes not with following the crowd but with staying close to the team's own record
> and having a topic insider on the team.

### The memorable formulation

> **At ICLR, conformity looks backward, not sideways.**

Why this one:
- It encodes the paper's conceptual distinction exactly. *Sideways* is the reference point of imitation: what peers
  are doing now (TA:48-51). *Backward* is the reference point of continuity: an accumulated record, the team's own or
  the topic's as carried by a team member (TA:567-570).
- It is short enough to close the abstract, the introduction and the conclusion, and it survives paraphrase.
- It is scoped ("at ICLR", "conformity", not "ML" or "science").

Alternatives considered:

| Formulation | Why not chosen |
|---|---|
| "Anchored to the record, not herded by the crowd" | Good gloss; use it once in the introduction as the plain-language version. Longer. |
| "Convergence without a herd" | Overclaims: the "flocking" half of herding is untested (H2a, C; DC:295). |
| "Entrants propose, the gate rewards records" | Two clauses; "rewards" reads causally; misses the field level. |
| "Fashion is in the map, conformity is in the record" | Clever, but makes the measurement result (E) carry the headline. |

### Definitions the whole paper uses (fixed; do not vary in the text)

- **Imitation**: conformity whose reference point is *what others are doing now* (popularity, momentum, what is hot).
- **Continuity**: conformity whose reference point is *an accumulated record*: the team's own past work, or the
  topic's past work carried by a team member who has already submitted in it (TA:559-570).
- **Anchored**: a defined adjective for work that conforms by continuity. Footnote at first use: not the
  anchoring-and-adjustment heuristic (Tversky and Kahneman 1974); "anchoring" has that meaning in the herding-in-
  science literature itself (Baddeley 2015) (TA:509-518).
- These words label *positions* of papers, not motives. Never "teams choose to stay close" (TA:630-631; DC:42, 48).
- Do not call continuity "exploitation": "exploiting foundation models" would be ambiguous (TA:114-115).

---

## 2. Conversations, gap, novelty wording, and why it matters beyond ICLR

### 2.1 The conversations it contributes to (primary first)

1. **Herding, fashion and bandwagons in science, and ML's self-critique** (LS Conversations 1 and 5). The default
   reading of ML's waves is a herd: researchers chase what is hot (Lipton and Steinhardt 2019; Hooker 2021; Dehghani et
   al. 2021; Bommasani et al. 2021), as fashion and cascade theory predicts (Abrahamson 1991; Bikhchandani et al. 1992;
   Banerjee 1992). **Our contribution:** the account's sharpest predictions fail at entry and find no detectable reward
   at the gate. We separate the two routes this literature runs together: Weisberg (2013) models "herding" as
   risk-avoiding clustering, while cascade "herding" is copying (LS:97-98; TA:367-375).
2. **Tradition, novelty and their reward; outsiders and entry** (LS Conversations 2 and 3). Foster et al. (2015)
   find conservative strategies dominant among producers. Teplitskiy et al. (2022) find no novelty penalty at journals.
   Hill et al. (2025) find a pivot penalty in citations and publication. Sekara et al. (2018) find a chaperone effect.
   **Our contribution:** in one complete submission population, the gate's conservatism is *record-referenced*. Distance
   from the team's own record goes with rejection (B), while distance from the field has no replicated association (C).
   Meanwhile the divergent contributions come with entrants (A; E).
3. **Computational histories of a field** (LS Conversation 4). Field histories fit one topic map on all years (Hall et
   al. 2008; Anderson et al. 2012; Prabhakaran et al. 2016; Pramanick et al. 2023). **Our contribution:** on the same
   papers with the same model, a map fitted with hindsight finds 29 emerging topics where an early-only map finds 8. The
   standard measurement makes a field look more faddish than a prospective one does.
4. **Supporting:** peer review at ML venues (Conversation 6) and confirmatory meta-research (Conversation 7). These are
   design and context, not claims of novelty (Section 2.4).

### 2.2 The theoretical gap

The two routes have old and separate roots:
- **imitation:** mimetic isomorphism (DiMaggio and Powell 1983); frequency imitation (Haunschild and Miner 1997);
  reputational herding (Scharfstein and Stein 1990); bandwagons (Abrahamson and Rosenkopf 1993);
- **continuity:** exploitation and local search (March 1991; Levitt and March 1988; Stuart and Podolny 1996);
  absorptive capacity (Cohen and Levinthal 1990); succession strategies and consecration (Bourdieu 1975).

Weisberg and Muldoon (2009) separate them inside one model, as "followers" against agents who search from their own
position (TA:338-365). Writing on herding in science merges them (Weisberg 2013; Baddeley 2015). A 2025 review of
topic choice treats "social context, identities, and path dependence" as distinct drivers. It lists "the types and
impacts of costs impeding topic entry and switching" and "the causal mechanisms associating topics with rewards" as
open (Xiang, Romero and Teplitskiy 2025; abstract read; TA:453-472). To our knowledge, no study tests the two routes
against each other at entry and at the review gate (TA:79-82; search limited).

### 2.3 Closest prior work (from verify_prior.md and landscape.md) and what each leaves open

| Work | What it did | What it leaves for us | Effect on our wording |
|---|---|---|---|
| Wang et al. 2023 (*World Wide Web*; arXiv 2103.05885) | ICLR 2017-2020: topic-cluster acceptance differences; arXiv posting advantage | No time dynamics, entry status or out-of-sample test | Do not claim topic differences in acceptance as new. Claim only that topic edges **regress out of sample** (VP:94-104). |
| Xu et al. 2026 (arXiv 2607.27209) | ICLR 2021-2026, 50,289 papers: topic predicts acceptance at equal scores | A rival mechanism (score scales), not a persistence test | "Topics differ ... (Wang 2023; Xu 2026); we find these edges real but regressing" (VP:184-186). |
| Jung et al. 2025 (arXiv 2509.25701; author order of EMNLP version unresolved) | ICLR 2017-2025, 28,358 submissions: process factors, including earlier submission | "Early" in the submission window, not early in a wave | Define "early" as early in a keyword's wave (VP:161-163). |
| Ibrahim et al. 2026 (arXiv 2607.26280) | ICLR 2019-2025 borderline prestige; pre-registered 2026 cohort; gap concentrated where arXiv identifies authors | Prestige, not position in a topic or record | Drop any "first registered design" claim (G7). Name visible prestige as a rival reading of the insider premium (VP:211-218). |
| Tran et al. 2020 (arXiv 2010.05137) | ICLR 2017-2020 identity and prestige | As above | Background only. |
| Movva et al. 2024 (NAACL) | Half of 2023 LLM first authors new to LLM work; arXiv | What entrants write; the gate | "Entrants are numerous" is not ours (LS:487); we add type, content distance and the gate. |
| Bao and Li 2025 (arXiv 2506.22729) | SPECTER2 similarity to own prior ICML/NeurIPS papers across the deep-learning shift; persistence goes with lower impact | Outcome is impact and productivity, not acceptance; incumbents, not entrants | The closeness measure is **not new**. Their result is a tension for the Discussion (VP:131-136). |
| Hill et al. 2025 (*Nature* 642:999-1006) | Larger pivots: lower citation impact and lower publication success | The decision itself, all submissions, double-blind, held-out | Never "first pivot penalty at the gate". Say "we observe the decision itself" (VP:311-316). Do not quote their numbers until the PDF is checked (VP:34-36). |
| Stelmakh et al. 2023 (*PLOS ONE*) | ICML 2020 RCT: no herding detected in reviewer discussions | Authors, entry | Pair it with our entry result; say "no herding detected" (VP:265-270). Kargaran et al. 2025 report co-reviewer influence on rebuttal-phase scores, so never "reviewers are independent". |
| Boudreau et al. 2016 (*Management Science*) | Evaluators score proposals closer to their own expertise, and highly novel ones, lower | Distance runs from evaluator to proposal | Do not equate with our far-jump measure (VP:330-337). |
| Biliotti et al. 2024 (arXiv 2404.04707) | Same topic-specific newcomer definition (COVID-19, PubMed); expertise offsets the newcomer disadvantage | Not contribution type or acceptance | Cite for the newcomer definition and as a producer-side analogue of the insider association (VP:246-248). |
| Huang 2026 (arXiv 2607.05401) | Topic initiators at ICLR precede topic growth | Initiators, not entrants' type or acceptance | Neighbour for G2. |
| Li et al. 2025 (*PeerJ CS*); Khanbayov and Kurban 2026 (arXiv 2606.12828) | Static-model emergence detection; prospective early-warning signal | Neither compares hindsight and early-only maps on the same papers | G4 wording: "same papers, same model, only the fitting window differs: 29 vs 8" (VP:365-370). |
| Weisberg and Muldoon 2009 (*Phil. Sci.*); Xiang et al. 2025 (*QSS*) | Formal split of followers vs own-position search; topic-choice drivers | No empirical test at entry and gate | The theory gap (Section 2.2). Cite Alexander et al. 2015 as the critique (TA:359-364). |

### 2.4 Exact novelty wording (drop-in for the introduction)

> Studies of ICLR's open records have related acceptance to author prestige and visibility (Tran et al., 2020;
> Ibrahim et al., 2026), to the review process (Jung et al., 2025), and to research area (Wang et al., 2023; Xu et al.,
> 2026). Studies of the producers describe who enters machine-learning topics and how far researchers stay from their
> own past work (Movva et al., 2024; Bao and Li, 2025). The science of science shows that moving far from one's own
> record costs citations and publication (Hill et al., 2025). To our knowledge, among the works we checked, no study
> asks within one complete submission population whether the herding account of a field's waves holds at three
> points: how the waves are measured, what kind of work topic entrants bring, and what the review decision goes with.
> Nor does any study test these predictions with registered hypotheses replicated on held-out papers.

**Theory-level novelty sentence (one only):** "To our knowledge, imitation and continuity have not been tested against
each other at entry and at the review gate."

**Phrases that must not appear** (VP:477-483; LS:479-492):
- "first study of acceptance at ICLR by topic";
- "first evidence of a pivot penalty at the gate";
- "first pre-registered study at an ML venue";
- "first to measure distance from one's own work in ML";
- "reviewers herd" or "reviewers do not herd";
- "ML is not a herd";
- any number from a cited paper that has not been checked against its PDF.

The closest-prior search stopped early (CP:7), and the fresh searches were WebSearch-based (VP:423), so the qualifier
"among the works we checked" always stays.

### 2.5 Why it matters beyond ICLR

1. **The diagnosis changes what convergence means.** Both routes produce sameness, but they carry different collective
   costs, so which one operates matters.
   - Imitation risks premature convergence and information loss (Zollman 2010; Banerjee 1992).
   - Continuity risks competency traps and slow collective discovery (Levitt and March 1988; Rzhetsky et al. 2015).

   This is interpretation, not advice: we do not say what any field or venue should do.
2. **The tests travel.** Each needs only submission records, author identifiers and text embeddings, so it can be run
   at any venue or in any field going through a paradigm wave:
   - entrants' contribution type and content distance within topic-year;
   - distance from one's own record at the decision;
   - an early-only refit of the topic map.
3. **Debates on ML hype and homogenisation** (Bommasani et al. 2021; Lipton and Steinhardt 2019). The evidence
   separates real package convergence, which holds, from herd behaviour, which fails at entry and is not detectably
   rewarded. That is a more specific picture than "the field follows trends".
4. **The science of science** gets the pivot and chaperone patterns at the decision itself: double-blind, with rejected
   papers visible, replicated out of sample. It also gets producers and the gate in one population (G1, G3).
5. **ACL field histories** get a cheap check against hindsight (G4). It applies to every topic-model history of NLP or
   ML.

---

## 3. Abstract (180 words)

> Machine learning is often said to herd: researchers chase what is hot and review rewards it. We test this account on
> 43,480 ICLR submissions from 2017-2026, including rejected and withdrawn papers, with registered hypotheses run once
> and retested on 11,099 held-out papers. We separate two routes to conformity: imitation, which takes its cue from
> what others do now, and continuity, which takes it from an accumulated record. The field converges, but less than
> hindsight suggests: on the same papers, a topic map fitted on all years finds 29 emerging topics; one fitted on
> 2017-2020 finds 8. What replicates is a package shift: where foundation models spread, fewer new architectures
> appear. Imitation fails where theory expects it most. Reversing our registered prediction, topic newcomers more
> often propose methods and less often build benchmarks, and their papers lie farther from earlier ICLR work. Review
> shows no detectable premium for following the crowd. In post hoc tests replicated on held-out papers, acceptance
> goes instead with continuity: closeness to the team's own record, and a topic insider. At ICLR, conformity looks
> backward, not sideways.

Word count: 180 (counted with `wc -w`, with "2017-2026" and "2017-2020" as single tokens).

Every claim in it and its source:

| Claim | Source | Tier |
|---|---|---|
| 43,480 submissions, rejected and withdrawn included | DC:65-66 | E |
| 11,099 held-out papers | DC:72 | E |
| 29 vs 8 emerging topics | DC:176-179 | E |
| FM adoption goes with fewer new architectures | DC:271, 364 | A |
| Newcomers: more method papers, fewer benchmark papers | DC:296-297, 365-366 | A, reversed |
| Newcomers' papers farther from earlier ICLR work | NN:main_pct | E |
| No detectable premium for following | DC:324, 367; DP:133; DC:376 | C, D\*, B |
| Own-record closeness; topic insider | DC:370, 372, 374 | B |

"Build benchmarks" is shorthand for "benchmark, dataset or evaluation papers". The body uses the full phrase.

---

## 4. Three contribution statements

1. **Conceptual.** We distinguish two routes to conformity by their reference point, imitation (what others are doing
   now) and continuity (an accumulated record), and derive their opposed predictions for a field's waves, for topic
   entrants and for peer review. To our knowledge, they have not been tested against each other at entry and at the
   review gate.
2. **Empirical.** In one complete submission population of a fast-moving venue, the herding account fails at entry:
   - the registered prediction reversed (A);
   - entrants' papers are farther from earlier work and slower to adopt trends (E).

   It also finds no detectable reward at the gate (C, D\*, B). Continuity goes with acceptance (B, replicated on
   held-out papers): distance from the team's own record has a replicated association, distance from the field does
   not.
3. **Measurement and design.** On the same papers with the same model, only the fitting window differing, a topic map
   fitted with hindsight finds 29 emerging topics where an early-only map finds 8, and a trend conclusion reverses. We
   report every claim with an evidence tier. Registered tests were run once and retested on held-out papers, and a
   failed size check is reported.

---

## 5. The argument, section by section

### 5.0 The spine (five sentences every section serves)

1. A field can become uniform by **imitation**, looking sideways at what others do now, or by **continuity**, looking
   backward at an accumulated record. The herding account of ML assumes the first.
2. **Field:** ICLR did converge, on the foundation-model package. But topic maps fitted with hindsight overstate its
   fashions, and convergence at the field level cannot tell the routes apart.
3. **Entry:** where imitation should be strongest, among topic entrants, the registered herding prediction reversed.
   Entrants bring method proposals and content farther from earlier work, and they are slower to take up the field's
   trends.
4. **Gate:**
   - following the crowd carries no detectable premium;
   - distance from the field has no replicated association with acceptance, but distance from one's own record does;
   - a topic insider goes with acceptance.
5. So the conformity we can detect looks backward, not sideways. Incumbents consolidate and the gate goes with records,
   while entrants bring proposals and more distant content.

**Why each act is load-bearing.** Each act tests one premise of the herding account, and each contributes one piece of
the positive thesis.

| Act | Premise of the herding account it tests | What would have supported herding | What we find | What it adds to the thesis | What breaks if the act is cut |
|---|---|---|---|---|---|
| 1 Field (§4) | Waves are fashions | Many emerging topics on any map; per-pair duplication rising | Fashions shrink without hindsight. A package shift holds (A). Per-pair duplication falls (E). | Convergence is real but non-diagnostic, so entry and the gate must decide | The paper would have to argue that ML is not converging, which is false, or would leave hindsight-inflated waves as unexamined evidence for herding. |
| 2 Entry (§5) | Waves are carried by imitators | Entrants write follow-on measurement, sit close to existing work, adopt trends fast | Registered prediction reversed (A); farther content, slower uptake (E) | The negative half on its strongest tier (A). Incumbents consolidate, which is continuity among producers. | No test of herding where theory says it is strongest; the A-tier hook is gone. |
| 3 Gate (§6) | Following is rewarded, which reputational herding needs (Scharfstein and Stein 1990) | Premia for crowding, branding, persistent topic edges, late riding | No detectable premium (C, D\*); edges regress (B). Own-record distance (B) and insider (B) go with acceptance; field distance does not replicate (C). Early, not late (B weak). | The positive half: where conformity *does* show | No positive claim; the paper becomes a list of nulls. |

### 5.1 Section-by-section plan (word budget 3,800)

| § | Title (claim-style) | Words |
|---|---|---|
| 1 | Introduction | 650 |
| 2 | Two Routes to Conformity | 450 |
| 3 | Data and Design | 450 |
| 4 | The Field: Fewer Fashions, One Package | 500 |
| 5 | Entry: Entrants Propose, Incumbents Consolidate | 550 |
| 6 | The Gate Looks Backward | 700 |
| 7 | Discussion: Where Conformity Lives | 400 |
| 8 | Conclusion | 100 |
| | **Total** | **3,800** |

Not counted: abstract, Limitations, references, captions, tables, appendix.

---

### §1 Introduction (650 words)

**Role.** Pose the herding account as the default reading. Introduce the two routes. State that we test one account at
three points; this is explicitly *not* three research questions, which answers the supervisor's criticism (LS:783-790).
Give the thesis, the memorable line and the contributions.

**Paragraph plan:**

1. **Hook: the wave** (Figure 1).
   - The FM share of submissions went from 0.3% (2017) to 54.4% (2026), and the new-architecture share from 24.5% to
     7.5% (E; DC:163-164).
   - Submissions grew ×40.1, and 69.3% of the corpus is from 2024-2026 (E; DP:71-72).
   - 17 of 68 frequent keywords rose and fell (E; DP:81).
   - Fig. 1 shows discovery data, while the keyword-peak percentages in DP:80 are pooled. Quote the values annotated on
     Fig. 1, or label the DP:80 values "pooled".
2. **The common reading, and its three claims.** Critics describe a field that follows trends (Lipton and Steinhardt
   2019; Hooker 2021; Bommasani et al. 2021). Fashion and cascade theory says how (Abrahamson 1991; Bikhchandani et al.
   1992). Read as herding, the wave makes three claims:
   1. the waves are fashions;
   2. imitators carry them;
   3. following pays at review, which is what makes herding individually rational (Scharfstein and Stein 1990).
3. **Two routes.** Give the definitions (Section 1 above), in one sentence each:
   - imitation: Bikhchandani et al. 1992; DiMaggio and Powell 1983;
   - continuity: March 1991; Sekara et al. 2018;
   - the formal split: Weisberg and Muldoon 2009;
   - the blending: Weisberg 2013.

   End with the plain-language gloss: "anchored to the record, not herded by the crowd".
4. **Design, in two sentences.**
   - 43,480 submissions, rejected and withdrawn included.
   - Registered hypotheses run once with frozen code, then retested on 11,099 held-out papers.
   - Every finding tiered.
   - Associations only.
5. **What we find, one sentence per act, with tiers:**
   - Field: E and A.
   - Entry: A reversed, E.
   - Gate: C, D\*, B; timing B weak.
6. **Thesis sentence + the memorable line.**
7. **Gap paragraph** (Section 2.4, verbatim) + **three contributions** (Section 4).

**Must not say:**
- "ML is a herd" or "ML is not a herd";
- "the gate rewards" as a causal verb (use "goes with");
- RQ1, RQ2, RQ3.

---

### §2 Two Routes to Conformity (450 words)

**Role.** Derive the predictions that become the columns of Table 1. Show why the field level cannot discriminate and
why entry and the gate can. Place the closest prior work.

**Claims, in order:**

1. **Imitation.** Imitation takes its cue from others' current choices.
   - Modes (Haunschild and Miner 1997):
     - *frequency* imitation is indexed by our crowding, hot-topic, trending-keyword and FM-adoption measures;
     - *outcome* imitation, i.e. following topics with high past acceptance, is indexed by topic acceptance edges;
     - *trait* imitation is not measured (TA:244-251).
   - Theory predicts imitation is strongest where uncertainty is highest, which means **topic entrants** (DiMaggio and
     Powell 1983; TA:221-227) and agents with the least private information (Bikhchandani et al. 1992).
   - Reputational herding is individually rational only if evaluators reward conformity to peers (Scharfstein and Stein
     1990). The reward system can amplify or counteract the pull of the leading approach (Kitcher 1990). So **the gate**
     is the second discriminating point.
2. **Continuity.** Continuity takes its cue from an accumulated record.
   - Local search near one's own competence (March 1991; Stuart and Podolny 1996).
   - Absorptive capacity: those without a record absorb a new package more slowly (Cohen and Levinthal 1990). This is
     the opposite of the cascade prediction for entrants (TA:146-151).
   - Bourdieu (1975), read in full text: new entrants choose between "the risk-free investments of succession
     strategies" and costly "subversion strategies"; dominant agents pursue "conservation strategies"; journals
     consecrate work "faithful to the principles of official science" (TA:408-428).
   - In science of science: tradition (Foster et al. 2015), the pivot penalty (Hill et al. 2025), the chaperone effect
     (Sekara et al. 2018) and switching costs (Myers 2020).
3. **Timing belongs to neither route.** It separates *rewarded imitation*, under which late riders do as well as
   early ones, from a priority-based reward, under which the premium falls as a wave matures (Merton 1957; Strevens
   2003; TA:552-553).
4. **The field level does not discriminate.** Convergence on a package is predicted by:
   - a package bandwagon (Fujimura 1988; content seen only in secondary descriptions; FW:107);
   - lock-in (Arthur 1989);
   - efficient choice (Sutton 2019).

   State this here, so Act 1 is read as setting the stage, not as a verdict (TA:600, 616-617).
5. **Prior work at ML venues.** Use the gap paragraph's citations and Stelmakh et al. 2023. Then the gap sentence: Xiang
   et al. 2025, plus the theory-level novelty sentence.

**Citations marked CONTENT-SECONDARY in theory_anchors.md**: March 1991's turnover result, Levitt and March's
"competency trap" wording, DiMaggio and Powell's mimetic section, Kitcher, Strevens, Scharfstein and Stein, Zollman
and Thoma. Cite them only for their general argument until the originals are read (TA:665-676). Do not use the phrase
"sharing the blame" (TA:296-297).

---

### §3 Data and Design (450 words)

**Role.** Make the three tests credible, and show that each measure belongs to one route.

**Content.**

**Corpus.**
- 55,938 reconciled submission instances from our own dated acquisitions of official OpenReview records (DC:62).
- Discovery: 43,480 papers with usable abstracts, 2017-2026, including rejected and withdrawn submissions (DC:65-66).
- Decided discovery papers: 32,190, 40.1% accepted; 9,986 withdrawn papers are left out of acceptance tests (DC:318).
- Held-out: 11,099 papers; 8,185 decided in 2018-26 (DC:72, 74).

**Measures, by route** (a small two-column box or a paragraph each):

| Imitation (reference: others now) | Continuity (reference: a record) |
|---|---|
| Topic crowding = log(1 + prior papers in topic) (DC:153) | Far jump: F_max = centred SPECTER2 cosine between the paper and the closest experienced co-author's earlier ICLR submissions since 2021. Probable earlier versions and near-duplicates (cos ≥ 0.90) are excluded (PRE:1372-1380; DP:231-232). |
| Hot topic (top fifth of prior growth) (DC:153) | Within-author closeness slope (DP:241-243) |
| Keyword state: Emerging / Mainstream / Cooling (DP:303-305) | Topic insider: an author with at least one earlier ICLR submission, any outcome, in the paper's k100 topic. Estimated at fixed team size and number of experienced authors (PRE:1569, 1659). |
| Prior FM adoption in the topic (DC:153) | Newcomer paper: no author with an earlier ICLR submission in that topic (DC:53). First-time team: no author with any earlier submission (PRE:1281). |
| Same-year twins (cos ≥ 0.70) (DP:78) | |
| Field novelty: 1 − mean cosine to the 10 nearest earlier ICLR papers, as a percentile within topic × year (DP:255; NN) | |

Say once: **field novelty and far jump use the same SPECTER2 space, with different reference points** (the field vs the
team's own record). §6.2 builds on this.

**Topics and labels.**
- Topics: SPECTER2 embeddings with spherical k-means, k = 100, chosen before the sensitivity sweep (DC:86-108).
- Contribution type: one primary type per paper from a fixed LLM codebook; LLM second pass κ 0.93. These are **LLM
  labels, not human labels** (DC:52, 133).

**Protocol.**
- Registered 2026-10-13, before full-corpus labels existed. One frozen run, 18 s (DC:237, 246).
- Held-out tests registered 2026-10-18 and run once (DC:256-258).
- Post hoc families were declared before they were run (DC:390).
- Mandatory wording: the held-out set is "a pre-registered out-of-sample replication, not a certified untouched
  holdout" (DC:43-44). Supported held-out tests confirm direction, not size (DC:47).
- The simulated size check failed: 12.6% / 10.0% rejection at nominal 5%, and the bootstrap did not fix it (DC:249-250).
  Report it.

**Models.** LPMs with topic × year fixed effects, SE clustered by topic (DC:244). Associations only (DC:42).

**Tiers:** one sentence, pointing to Table 1.

**Text caveat.** Post-decision abstracts: 17.6% of accepted and 0.5% of rejected abstracts in 2023-26 carry a code link
(DC:78). The link-removed re-run holds for the far jump in discovery (−5.39; DP:371). Details go to the appendix.

---

### §4 The Field: Fewer Fashions, One Package (500 words) — Act 1

**Role.**
- Test claim (1), "the waves are fashions".
- Show that the standard measurement inflates the fashion, and that what survives is a package shift.
- Close by stating that this level cannot tell imitation from continuity, which motivates Acts 2 and 3.
- Carries the ACL-genre measurement lesson (C3).

**Claims and findings:**

1. **Hindsight inflates waves** (Figure 2a).
   - Same papers, same model, only the fitting window differs: 29 emerging topics on the all-years map, 8 on the
     2017-20 map (E; DC:176-179).
   - The all-years map's count equals a late-only map's: 28 (E; DC:181).
   - It shows half as many declining topics as a year-balanced map: 13 vs 26 (E; DC:178, 184-186).
   - The share of 2024-26 papers in emerging topics is **bracketed, not pinned down**: 22.3% to 40.9% (DC:187).
   - Prior work: Li et al. 2025 and Khanbayov and Kurban 2026. Wording from VP:365-370.
2. **A trend conclusion reverses with the map.**
   - "Topics age from methods to measurement" is null on the all-years map: method −0.14 [−1.78, +1.49], measurement
     +0.50 [−0.76, +1.75].
   - It appears on the early map for 2021-26 papers: −3.48 [−6.21, −0.76] / +3.96 [+1.35, +6.57].
   - Tier: E, counted variants of C; exploratory and unadjusted (DC:201-210).
   - Say "the answer depends on the map" (DC:210-211).
3. **What survives: a package shift** (Figure 2b).
   - FM 0.3% → 54.4%; new architecture 24.5% → 7.5% (E; DC:163-164).
   - Where a topic's previous-year papers built more on FMs, fewer of its papers propose new architectures:
     −7.98 [−12.14, −3.82] in discovery, −11.0 [−18.1, −3.9] held-out, 9/9 variants, hindsight variants pass
     (**A**; DC:271, 364).
   - Plain reading: about a third fewer new-architecture papers at 50% adoption than at 10% (derived, DC:275-277).
     Direction, not size.
4. **No pile-on per pair.**
   - Papers with a same-year twin rose from 19.5% (2019) to 48.8% (2026).
   - But twins per paper per 1,000 submissions fell from 0.32 to 0.19 (E; DP:78-79).
   - Duplication grows with volume, not with herding per pair.
5. **Imitation-like spread in surface form.**
   - The share of titles of the form "NAME: subtitle" rose roughly fourfold: 7-14% (2017) → 37-49% (2026) depending
     on definition (E\*; DP:120-125).
   - Present it honestly as the one place where imitation-like spread is plain. §6.1 shows it carries no detectable
     premium.
6. **Closing sentence of the act.** Lock-in (Arthur 1989), a package bandwagon (Fujimura 1988) and efficient choice
   (Sutton 2019) all predict finding 3. The field level cannot say which route produced the convergence, so we turn to
   entry and the gate (TA:600, 616-617).

**Optional, one clause if words allow:**
- Topic size "predicts" two-year growth out of time only on the hindsight map: R² 0.28 vs −0.03.
- Tier E. Maps differ in fitting corpus; there is no paired test (DC:217, 227-231).

**Cite:**
- Hall et al. 2008; Klinger et al. 2020;
- Bao and Li 2025, as the descriptive analogue of displacement in the previous shift (VP:128).

---

### §5 Entry: Entrants Propose, Incumbents Consolidate (550 words) — Act 2

**Role.**
- Test claim (2), "imitators carry the waves".
- Use the population where imitation theory says it is strongest.
- This is the paper's hook: our own registered herding prediction failed in the opposite direction.

**Claims and findings:**

1. **The registered prediction reversed** (Figure 3; Table 1).
   - Newcomer papers are **more** often method papers: +3.71 [+2.61, +4.80] discovery, +3.60 [+1.48, +5.71] held-out,
     on a 75% base.
   - They are **less** often benchmark, dataset or evaluation papers: −1.70 [−2.46, −0.93] / −2.10 [−3.35, −0.85], on
     a 7.7% base, about a fifth fewer.
   - All 10 variants agree and the hindsight variants pass.
   - Tier: **A (reversed registered prediction)**. Always say that the original registered herding prediction failed
     (DC:33-36, 296-297, 365-366).
2. **Qualifier, given in the same paragraph.**
   - With log team size, H2c shrinks to −0.54 [−1.11, +0.04] (p 0.07) in discovery and −0.98 held-out. H2b is
     unchanged at +3.92 (DC:301, 308).
   - Read it as partly small all-new teams vs larger mixed teams.
   - H2c is concentrated in 2024-26 (−2.0; DC:305-306).
   - "Method paper" is a contribution **type**, not a measure of novelty (DC:313-314).
3. **The content test** (new; tier **E**, outcome-free, added during writing). This answers the type-is-not-novelty
   objection.
   - Within topic × year, newcomer papers lie farther from earlier ICLR papers in SPECTER2 space: +5.90 percentile
     points [+4.95, +6.85], N 42,325, 100 topic clusters (NN:main_pct).
   - Within method papers only: +5.24 [+4.16, +6.31] (NN:method_only_pct). So it is **not** explained by type mix.
   - With team-size, class and FM controls: +5.76 [+4.82, +6.70] (NN:team_class_fm_ctrl_pct).
   - Similar in 2019-22 (+4.95 [+2.32, +7.58]) and 2023-26 (+6.01 [+5.03, +6.98]); difference p 0.44 (NN:era_*).
   - Size: about 0.22 of the within-cell SD (raw cosine +1.35; NN:raw_cosine_nov_x100; SD 0.062, from the
     `descriptives` block of the same JSON). Call it **modest but precise**.
   - Wording: "farther from earlier ICLR work", **never** "more original" or "more novel ideas".
4. **Not near-duplicates.** Newcomer papers are less often twinned: −3.9 pp [−5.0, −2.7] (E; DP:275).
5. **Slower uptake of trends** (absorptive capacity, not cascades).
   - First-time teams use Emerging keywords less: −3.7 pp, 16.7% vs 25.0%, q 6e-6 (E; no team-size control; DP:315-317).
   - Compared with returning topic newcomers, they write FM papers less often: −4.6 / −9.0 / −14.7 pp in topics at
     5-15 / 15-30 / 30-50% adoption (E; with class and team-size controls, PRE:1111-1112; DP:360-362).
   - Reading: among entrants, those who bring an ICLR record take up the field's package faster (Cohen and Levinthal
     1990). Cascade theory predicts the opposite (TA:146-151).
6. **What stays untested.**
   - Whether entrants *flock* to hot topics: H2a −0.73 [−2.68, +1.22], inconclusive, hindsight variant fails (C;
     DC:295).
   - Newcomer × hot: −0.4 / −0.6 pp, n.s. (D; DC:307).
   - Say plainly: "we can say what entrants write and how fast they adopt trends, not whether they crowd into hot
     topics."
7. **Placing it.**
   - Stelmakh et al. 2023 found no herding detected among reviewers; we find that entrants do not write the follow-on
     work herding predicts (VP:465-466).
   - Movva et al. 2024: entrants are numerous. Here 72.9% of papers are newcomer papers (E; DC:151).
   - Koch et al. 2021: benchmark building is concentrated.
   - Bourdieu 1975: entrants are not imitators.
   - The incumbent side is continuity among producers. Incumbents write the follow-on measurement work, and their
     papers sit closer to earlier work, partly to their own earlier papers (NN caveat 3).

---

### §6 The Gate Looks Backward (700 words) — Act 3

**Role.**
- Test claim (3), "following pays".
- Give the positive half of the thesis.
- The sub-sections follow the reference point: others now (6.1); a record vs the field (6.2, 6.3); time (6.4).
- Open with the asymmetry, stated plainly: the negative half of the thesis rests on a registered test (A), while the
  positive half rests on post hoc tests that held out of sample (B).

**6.1 Following: no detectable premium (≈170 words).**
- Topic crowding: −1.68 [−3.68, +0.32] discovery; −1.51 [−5.20, +2.19] held-out. MDE80 4.8 pp, so uninformative
  (**C**; DC:324, 367). Exact phrase: "no detectable premium" (DC:332).
- Branded titles: acceptance ratio 1.02 (**D\***, earlier exploratory, not re-run; DP:133).
- Topic edges are real but regress.
  - Noise-free SD of edges: 6.4 pp. A single year's rate is half noise at about 58 decided papers (DP:324-325).
  - Slope of the 2024-26 edge on the 2018-22 edge: b 0.38 [0.18, 0.58] in discovery; 0.60 [0.32, 0.88] held-out
    (**B**). EB D0 > 0 (**B**) (DC:376-377).
  - Keyword units: 0.16, n.s. (DP:52-53).
  - Prior art: Wang et al. 2023; Xu et al. 2026. Phrase: "a favoured topic is not a reward that keeps paying in full"
    (VP:186). Outcome imitation of topic acceptance would partly chase noise (TA:247-249).
- Honesty sentence: no premium does not rule out bandwagons that go unrewarded (Abrahamson and Rosenkopf 1993;
  TA:281-286). The title style of §4 may be one.

**6.2 Two reference points, one embedding (≈220 words). The core of the act** (Figure 4).
- **Distance from the field** has no replicated association with acceptance.
  - Least-novel fifth vs middle: −3.27 [−4.93, −1.60] in discovery; −0.13 [−3.50, +3.25] held-out, power 0.47. "Did
    not replicate" (**C**; DC:371; DP:42-44).
  - Most-novel fifth: +0.44 [−1.41, +2.28] (**D**; DP:261).
  - Within-author novelty slope: +0.39 → +0.34 [−0.47, +1.16], not supported (**C**; DC:373).
- **Distance from the team's own record** does have one.
  - Far jump (F_max p10 minus p50): −5.44 [−7.10, −3.78]; held-out −6.09 [−9.32, −2.86] (**B**, primary; DC:370).
  - Within the same author, per +0.1 cosine of closeness: +0.55 → +1.06 [+0.23, +1.89] (**B**; DC:372). Composition
    may explain half or more (DP:243).
  - Shape, adjusted acceptance by closeness fifth, far to near: 39.7 / 41.8 / 44.4 / 47.2 / 46.9% (**D**; DP:236).
    Leaving costs; the closest fifth gains nothing extra. If the near tail is quoted, the E2 rule applies:
    +1.75 (Holm 0.148), held-out +2.34 (p 0.17), pooled +2.10 (DP:40-41).
- **Robustness**, one sentence:
  - newcomer control −5.0;
  - no earlier version −5.5;
  - link-removed text −5.39 (discovery only);
  - correlation with the newcomer flag −0.57 (DP:238-248).
- **Wording:**
  - "Larger pivots are less often published (Hill et al. 2025); we observe the decision itself, on every submission"
    (VP:467-468).
  - "Our closeness measure, like Bao and Li's (2025), uses SPECTER2 similarity to one's own earlier papers" (verified;
    Section 0).
  - Consistent, weakly, with Teplitskiy et al. 2022's absence of a novelty penalty at journals.
  - Boudreau et al.'s distance runs from evaluator to proposal. Do not equate it with ours (VP:330-337).
- **Guardrail:** compare *replication status*, not effect sizes. The populations and units differ: far jump on 20,430
  decided 2023-26 papers with an experienced author, novelty on 31,549 decided 2019-26 papers. Cross-module size
  comparisons are banned (DC:428).

**6.3 Carrying the topic's record (≈160 words).**
- One topic insider vs none: +3.42 [+1.18, +5.66] in discovery; +3.88 [+0.28, +7.47] held-out (**B**; DC:374).
  - The held-out test was underpowered (derived MDE80 ≈ 4.5), so it confirms direction only.
  - The Holm 0.019 holds within the module family only; across modules it would be about 0.17 (DP:54-55).
  - A keyword-based insider: +0.0 (DP:289).
- Chaperone effect (Sekara et al. 2018); expertise offsets the newcomer disadvantage (Biliotti et al. 2024).
- The newcomer acceptance gap is mostly about who writes:
  - raw 37.2% vs 47.3%; −10.2 within topic × year;
  - same sample, −5.4 without author fixed effects vs −3.1 [−4.5, −1.6] with them (**D**; DC:343; DP:144-145,
    178-179).
- The same author entering a new topic: −1.4 [−2.7, −0.0] (**D**; DP:179). This is the within-person counterpart of the
  far jump.
- Mandatory phrase: the residual "need not be reviewer bias" (DP:182-183).

**6.4 Time: early, not late (≈150 words).**
- Priority (Merton 1957; Strevens 2003) separates rewarded imitation from a priority-based reward.
- Young rising (Emerging) vs old flat (Mainstream) keywords: +2.67 [+0.76, +4.58] → +3.25 [−0.18, +6.69] (**B weak**;
  say the CI includes 0; DC:375).
- The acceptance gap after a keyword's share peaks, vs before: −5.7 [−8.5, −2.9] → −5.2 [−11.1, +0.7], p 0.043
  (**B weak**). It leans on the six keywords inspected first: without them −1.7 (p 0.33) (DP:389-397).
- Both lean, weakly, toward priority and against rewarded late riding (TA:604).
- "Early" means early in a keyword's wave, not early in the submission window (Jung et al. 2025; VP:157, 163).
- **Caution case: federated learning.**
  - The vivid fad case: −11.3 [−17.9, −4.8] in discovery (q 0.19).
  - Held-out −4.9 [−15.4, +5.7], uninformative; the trend has the opposite sign (+3.2 pp/yr).
  - "Not confirmed" (**D/C**; DC:368-369). Never "scam" (DC:55).

**Relegated to the appendix:** far jump × hot (−0.35) and insider × hot (−0.8). Both null and uninformative (D;
DP:246, 291). If mentioned in the text, say "no detectable difference".

---

### §7 Discussion: Where Conformity Lives (400 words)

**Role.** Assemble the 2 × 2 (route × site), give the mechanisms honestly, take up the tensions, and say what the
result means for field histories and the hype debate.

**Claims:**

1. **The 2 × 2** (a sentence or a tiny inline table):

   | | Producers | Gate |
   |---|---|---|
   | **Imitation** | Not among entrants (A, E). Only in surface form (titles, E\*). Flocking untested (C). | No detectable premium (C, D\*); edges regress (B); late riding not favoured (B weak) |
   | **Continuity** | Incumbents consolidate: measurement papers (A), content closer to earlier work (E). Entrants with an ICLR record adopt the package faster (E). | Own-record distance (B); within-author closeness (B); topic insider (B) |

   Phrase from TA:374: "what Weisberg (2013) models as herding, risk-avoiding clustering, appears here as continuity
   with one's own record, not as imitation of the crowd".
2. **Mechanism is open.** Three readings cannot be separated:
   - **expertise or bias**: better-informed papers or evaluator conservatism (Li 2017);
   - **visible prestige** through arXiv (Ibrahim et al. 2026);
   - **selection** into teams.

   The proven-record question: a proven outsider minus an unproven insider is +4.6 (Holm 0.088), and familiarity
   without an earlier acceptance is +0.2 (D; DP:291-293).

   Whatever the mechanism, the premium points backward, to a record. "Continuity" labels positions, not motives.
3. **Tension with Bao and Li 2025.** In the earlier deep-learning shift, persistence went with lower *later impact*.
   Here continuity goes with *acceptance*. "The gate and the citation record need not reward the same thing; our data
   cannot test this" (VP:134-136).
   - Short-cycle rewards favour exploitation (March 1991), and continuity has long-run costs (Levitt and March 1988;
     Ahuja and Lampert 2001; Rzhetsky et al. 2015).
   - Interpretation only, never advice.
4. **Is the package a fad?** All of the following are D, so this is context only:
   - FM papers are accepted more often: +4.62 [+2.79, +6.44] (D; DC:342);
   - the premium does not shrink as adoption rises: +0.19 per logit unit [−0.96, +1.34] (D; DP:356);
   - new architectures are accepted relatively more where FMs dominate: +8.3 [+1.3, +15.4] (D; DC:349).

   A fad's premium should fade, and the gate does not detectably enforce homogenisation (cf. Sutton 2019). The FM
   label is an LLM label on partly camera-ready text (DP:362).
5. **For field histories and for the hype debate.**
   - Refitting the map on early years is a cheap check (C3).
   - The hype debate gets a more specific picture: real package convergence (supports Bommasani et al. 2021), but no
     detected entrant herding and no detected reward for following.

---

### §8 Conclusion (100 words)

Restate the three tests in one sentence each, then the thesis and the memorable line. Add one sentence on scope:
"one venue, associations only". No new numbers.

### Limitations (ARR section; not counted)

- One venue (DC:56).
- Split-sample held-out, not an independent holdout: shared years, reviewers and authors (DC:43-45).
- LLM labels (DC:52).
- Histories are ICLR-only, and the 2021 author-ID switch biases incumbency toward zero (DC:144-149).
- Far-jump histories only since 2021 (DP:249).
- Post-decision text: cleantext checked in discovery only (DP:367-374).
- 9,986 withdrawn papers are left out of acceptance tests, and withdrawal after review rises with maturity (+1.62; D;
  DC:344).
- Size failure (DC:249-250).
- Six secondary held-out tests, one-sided and unadjusted (DP:29-30).
- The novelty analysis is unregistered.
- Some theory works were seen only in secondary descriptions.

### Appendix (relegated, with reasons)

| Item | Numbers (source) | Tier | Why the appendix |
|---|---|---|---|
| Full held-out table, every registered test | DC:364-378 | A-C | Reference |
| Team-size gradient | +8.8 pp per doubling [+8.0, +9.7] (DC:395) | D | A control and a confound, not part of the route contrast |
| Acceptance by contribution type | theory +8.9, dataset/benchmark +3.9, empirical −2.7 vs method (DC:351) | D | Type is not a route measure. It shows the gate does not favour the type entrants bring. |
| Concurrent twin and acceptance (P2) | +0.68 / held-out +3.69 [+0.90, +6.48], unregistered / pooled +1.86 (DP:36-41) | D | Mixed. P2 quoting rule: all three rows together. It is a possible "riding pays" reading, so it is named in the weak points. |
| Forecastability on the hindsight vs the early map | R² 0.28 vs −0.03 (DC:217) | E | Maps differ in corpus; no paired test |
| Keyword winner's curse | 16.0% vs 20.6% (DP:334-338) | D/E | Keywords only, h = 1 |
| Area spread (PH4) | about ±10 pp; nothing survives BH (DP:191-197) | D | Descriptive |
| Withdrawal after review vs maturity | +1.62 [+0.42, +2.81] (DC:344) | D | Selection context |
| H1a-c and H1e (non-lifecycle), H3b | DC:268-272, 325 | C | Not supported or inconclusive; not part of the route contrast |
| Interactions with topic heat | −0.35; −0.8 (DP:246, 291) | D | Null, uninformative |
| Per-head insider decomposition; H2-H6 of teams | DP:290-296 | D | Mechanism hints only (used in §7 once) |
| Novelty analysis: full sensitivity table | NN: excl 2021 +5.87; newcomer_s4 +5.84; no earlier version +5.81; plain definition +6.63; by year | E | Robustness. Do not quote 2021 (+22.5 on about 11 incumbent papers). |
| Title definitions D1-D4 | DP:97-117 | E\* | Robustness |
| **Dropped:** returning first authors' title-style lag; LLM-favoured title verbs (OR 2.2) | DP:134-135 | E\* | Not re-verified (Notion only) |
| **Dropped:** do-not-quote list | DP:56-61 | — | By rule |

### Placement map: every major finding has a place

| ID | Finding | Place | Role |
|---|---|---|---|
| F1 | Field waves; FM displaces new architectures (E; H1d A) | §1 hook; §4.3 | Convergence is real |
| F2 | Hindsight: 29 vs 8; trend flip (E) | §4.1-4.2; Fig. 2a | Fashion inflated by measurement |
| F3 | Newcomers: method +, measurement − (A, reversed) | §5.1-5.2; Fig. 3; Table 1 | The hook: imitation fails at entry |
| F4 | First-time teams slower to adopt; newcomers less twinned (E) | §5.4-5.5; Fig. 3 | Absorptive capacity, not cascades |
| F5 | Crowding (C), branding (D\*) | §6.1 | No detectable premium for following |
| F6 | Timing: A1, PH6 (B weak); FL (D/C) | §6.4 | Early, not late; caution case |
| F7 | Far jump, within-author closeness, insider (B) | §6.2-6.3; Fig. 4 | The positive half |
| F8 | Newcomer gap mostly composition; −1.4 within person (D) | §6.3 | Continuity within person; not reviewer bias |
| F9 | Topic edges regress (B) | §6.1 | Outcome imitation would chase noise |
| F10 | FM premium stable; new architectures against the tide (D) | §7.4 | Is the package a fad? (context) |
| F11 | Twins as volume (E); P2 acceptance (D, mixed) | §4.4 (E); appendix (P2) | Against pile-on |
| N | Newcomer content distance +5.90 (E, new) | §5.3; Fig. 3 | Answers the type-is-not-novelty objection |
| P | Field-novelty tests P1a (D), P1b (C), P7 (C) | §6.2; Fig. 4 | The second reference point |
| T | Title-style spread (E\*) | §4.5 | Where imitation-like spread is visible |

---

## 6. Main-text table: Table 1, "Scorecard: two routes, three tests"

**Design.**
- A full-width `table*`, small font, grouped by test (field, entry, gate).
- Columns:
  1. test and measure;
  2. what imitation predicts;
  3. what continuity predicts;
  4. discovery estimate [95% CI];
  5. held-out estimate [95% CI];
  6. tier;
  7. reading.
- Signs: + / − / 0 / "·" (no prediction).
- The reading column uses five fixed labels:
  - *against imitation*;
  - *for continuity*;
  - *non-discriminating*;
  - *untested*;
  - *measurement*.
- Units are pp unless stated.
- Rows marked † can move to the appendix version of the table if space runs short. The others carry the story.

| # | Test (measure) | Imitation | Continuity | Discovery | Held-out | Tier | Reading |
|---|---|---|---|---|---|---|---|
| | **(i) Field: are the waves fashions?** | | | | | | |
| 1 | Emerging topics, all-years vs 2017-20 map (same papers and model) | · | · | 29 vs 8 (late-only 28; balanced 16) | — | E | measurement: hindsight inflates waves |
| 2† | "Topics age from methods to measurement", all-years vs early map (2021-26 papers) | · | · | −0.14 / +0.50 vs −3.48 / +3.96 | — | E | measurement: conclusion flips |
| 3 | Prior-year FM adoption (0 → 100%) → new-architecture share | − (package bandwagon) | − (lock-in) | −7.98 [−12.14, −3.82] | −11.0 [−18.1, −3.9] | A | non-discriminating: real convergence |
| 4 | Papers with a same-year twin; twins per paper per 1,000 submissions, 2019 → 2026 | per-pair rate + | · | 19.5% → 48.8%; 0.32 → 0.19 | — | E | against imitation (pile-on) |
| 5† | "NAME: subtitle" title share, 2017 → 2026 | + (style bandwagon) | · | 7-14% → 37-49% | — | E\* | imitation-like, in form only |
| | **(ii) Entry: who carries the wave?** | | | | | | |
| 6 | Newcomer paper → method paper | − (registered) | + | +3.71 [+2.61, +4.80] | +3.60 [+1.48, +5.71] | A (reversed) | against imitation |
| 7 | Newcomer paper → benchmark, dataset or evaluation paper | + (registered) | − | −1.70 [−2.46, −0.93] | −2.10 [−3.35, −0.85] | A (reversed) | against imitation; shrinks with team size |
| 8 | Newcomer paper → distance from earlier ICLR papers (percentile within topic-year) | − | + | +5.90 [+4.95, +6.85]; method papers +5.24 | — | E (new) | against imitation |
| 9† | Newcomer paper → any same-year twin | + | · | −3.9 [−5.0, −2.7] | — | E | against imitation |
| 10 | First-time team → Emerging-keyword use | + | − (no record to absorb) | −3.7 (16.7% vs 25.0%) | — | E | against imitation, for continuity |
| 11 | First-time vs returning topic newcomer → FM paper, topics at 5-15 / 15-30 / 30-50% adoption | + | − | −4.6 / −9.0 / −14.7 | — | E | against imitation, for continuity |
| 12 | Hot topic → share of incumbent papers (flocking) | − | · | −0.73 [−2.68, +1.22] | — | C | untested |
| | **(iii) Gate: what does acceptance go with?** | | | | | | |
| 13 | Topic crowding, per log unit of prior papers | + if rewarded | · | −1.68 [−3.68, +0.32] | −1.51 [−5.20, +2.19] | C | no detectable premium (MDE80 4.8) |
| 14 | "NAME: subtitle" title, accepted ÷ all | > 1 if rewarded | · | 1.02 | — | D\* | no premium seen (not re-run) |
| 15 | Topic edge persistence: slope of 2024-26 on 2018-22 edge | ≈ 1 if outcome imitation pays | · | 0.38 [0.18, 0.58] | 0.60 [0.32, 0.88] | B | edges real but regress |
| 16 | Distance from field: least-novel fifth vs middle | · | · | −3.27 [−4.93, −1.60] | −0.13 [−3.50, +3.25] | C | did not replicate |
| 17† | Distance from field: within-author slope per 10 percentile points | · | · | +0.39 [+0.09, +0.69] | +0.34 [−0.47, +1.16] | C | not supported |
| 18 | Distance from own record: far jump (F_max p10 minus p50) | · | − | −5.44 [−7.10, −3.78] | −6.09 [−9.32, −2.86] | B | for continuity |
| 19 | Closeness to own record within author, per +0.1 cosine | · | + | +0.55 [+0.21, +0.90] | +1.06 [+0.23, +1.89] | B | for continuity |
| 20 | One topic insider vs none (fixed team size and experience) | · | + | +3.42 [+1.18, +5.66] | +3.88 [+0.28, +7.47] | B | for continuity (direction only) |
| 21† | Same author, new to the topic (author FE) | · | − | −1.4 [−2.7, −0.0] | — | D | consistent with continuity |
| 22 | Emerging vs Mainstream keyword | 0 (late = early) | · (priority: +) | +2.67 [+0.76, +4.58] | +3.25 [−0.18, +6.69] | B weak | leans to priority; CI includes 0 |
| 23 | Gap after vs up to a keyword's share peak (17 waves) | 0 | · (priority: −) | −5.7 [−8.5, −2.9] | −5.2 [−11.1, +0.7] | B weak | leans to priority; −1.7 without six inspected keywords |
| 24† | Federated learning keyword, acceptance gap | · | · | −11.3 [−17.9, −4.8] | −4.9 [−15.4, +5.7] | D / C | vivid fad case not confirmed |

**Sources by row:**

| Row | Source |
|---|---|
| 1 | DC:176-179 |
| 2 | DC:201-202 |
| 3 | DC:271, 364 |
| 4 | DP:78-79 |
| 5 | DP:120-125 |
| 6-7 | DC:296-297, 365-366; team-size note DC:301, 308 |
| 8 | NN:main_pct, method_only_pct |
| 9 | DP:275 |
| 10 | DP:315-316 |
| 11 | DP:360-362 |
| 12 | DC:295 |
| 13 | DC:324, 367 |
| 14 | DP:133 |
| 15 | DC:376 |
| 16 | DC:371 |
| 17 | DC:373 |
| 18 | DC:370 |
| 19 | DC:372 |
| 20 | DC:374 |
| 21 | DP:179 |
| 22 | DC:375 |
| 23 | DP:389-397 |
| 24 | DC:368-369 |

**Caption must carry:**
- "Associations within topic and year. Keyword rows compare against all other papers of the same year."
- The tier legend.
- "Held-out tests are one-sided and confirm direction, not size, so a supported test can have an interval that
  includes 0."
- "The held-out set is a pre-registered out-of-sample replication, not a certified untouched holdout."
- "Rows 16-20 differ in population and units; compare replication status, not size."
- "E\*/D\*: earlier exploratory title analysis; the share was re-verified, the ratio was not re-run."
- "Row 8 was computed during writing (outcome-free, unregistered)."

**Why this table makes the story visible.**
- The two prediction columns put the routes side by side.
- The reading column turns 24 numbers into one pattern:
  - "against imitation" fills the entry block;
  - "no detectable premium" and "regress" fill the following rows;
  - "for continuity" fills rows 18-20.
- The tier column keeps the asymmetry honest: the negative half is A, the positive half is B.

---

## 7. Figure plan (four figures; Figure 1 exists)

### Figure 1: Research waves (exists)

| | |
|---|---|
| **File** | `research/fashion/paper/figs/fig1_waves.pdf`, made by `paper/make_figures.py` from discovery keywords (outcome-free) |
| **Message** | ML's waves are vivid. This is the phenomenon that invites the herding reading. |
| **Placement** | §1 |
| **Caption** | 17 of 68 frequent keywords rose and fell (DP:81). Write that this count is from the pooled wave table (`output_pooled/posthoc/ph5_waves/wave_table.csv`), while the panels show the discovery split. |

### Figure 2: Fewer fashions, one package (Act 1, §4)

| | |
|---|---|
| **Message** | Measured without hindsight, a field shows fewer fashions; the package shift holds. |
| **Panel (a)** | Emerging topics by the years the map was fitted on. Bars, ordered from no hindsight to full hindsight: early 2017-20, 8; middle-era, 10; balanced, 16; late-only, 28; seed refit, 28; all-years, 29. Each bar is annotated with the share of 2024-26 papers in emerging topics: 22.3, 20.9, 42.2, 31, 41, 40.9%. |
| **Panel (b)** | FM share and new-architecture share by year, 2017-2026: two lines, 0.3 → 54.4% and 24.5 → 7.5%. An inset gives the H1d estimate, discovery −7.98 and held-out −11.0, with CIs and tier A. |
| **Sources (committed)** | (a) `research/topics/output/hindsight_check.json` (`maps.*.emerging_topics`, `late_paper_share_in_emerging`). (b) `research/topics/output/paper_contributions.csv.gz` (outcome-free LLM labels; DC:168-169), `research/fashion/output/rq1_results.csv`, `research/fashion/output_pooled/confirmation_run/h1d.csv`. |
| **Caption must carry** | The early map cannot represent topics born after 2020, so the count is bracketed, not pinned down. FM and architecture labels are LLM labels. H1d is an association within topic and year. |

### Figure 3: Entrants propose, incumbents consolidate (Act 2, §5)

| | |
|---|---|
| **Message** | On every entry measure, entrants differ from incumbents in the direction opposite to the one imitation predicts. |
| **Design** | A horizontal forest plot, one row per measure: newcomer minus incumbent (or first-time minus returning). Each row has a small arrow or grey band marking the sign herding predicted. Discovery as filled dots, held-out as open dots where they exist; the tier letter at the right. Each row is labelled with its own unit (pp of share, or percentile points). No common axis claims are made across units. |
| **Rows** | method paper +3.71 / +3.60 (A); measurement paper −1.70 / −2.10 (A); distance from earlier ICLR work +5.90 percentile points (E); any same-year twin −3.9 (E); first-time team Emerging-keyword use −3.7 (E); first-time vs returning topic newcomer FM paper at 15-30% adoption −9.0, with the other bins in a small strip (E) |
| **Sources** | `research/fashion/output/frozen_run/rq2_results.csv`; `research/fashion/output_pooled/confirmation_run/rq2_rows.csv`; `research/fashion/output/posthoc/ph5_position/free_herding.csv`; `research/fashion/output/posthoc/ph5_kwtiming/free_profile_states.csv`; `research/fashion/output/posthoc/ph5_fmwave/free_entry.csv`; content-distance row from `paper_ws/output/novelty_newcomer.json` and `.csv` |
| **Blocker** | The content-distance output and its script (`paper_ws/scripts/novelty_newcomer.py`) live in this session's workspace, **not in the repository**. They must be committed (output plus script) before the figure is built from committed outputs. Otherwise drop that row and keep the number in the text, marked "computed for this paper". |
| **Caption must carry** | The flocking test (H2a) is inconclusive and is not shown. Method paper is a type, not novelty. Distance is in SPECTER2 space and is not originality. |

### Figure 4: The gate looks backward (Act 3, §6.2-6.3)

| | |
|---|---|
| **Message** | At the gate, the record-referenced tests replicate; the crowd- and field-referenced tests do not. |
| **Panel (a)** | Adjusted acceptance by fifth of closeness to the team's own record, discovery: 39.7 / 41.8 / 44.4 / 47.2 / 46.9% with 95% intervals (D shape, under the B-tier E1 test). |
| **Panel (b)** | A paired discovery vs held-out dot-interval plot in two labelled groups. **Referenced to a record:** far jump E1 (−5.44 / −6.09), within-author closeness E4 (+0.55 / +1.06), one insider H1 (+3.42 / +3.88). **Referenced to others (crowd or field):** topic crowding H3a (−1.68 / −1.51), least-novel fifth P1b (−3.27 / −0.13), within-author novelty P7 (+0.39 / +0.34). Each row on its own small axis with its unit; the tier letter at the right. |
| **Sources (committed)** | (a) `research/fashion/output/posthoc/ph5_pivot/quintiles.csv` (rows "P1 F_max quintiles"). (b) Discovery: `output/posthoc/ph5_pivot/tests.csv`, `output/posthoc/ph5_position/tests.csv`, `output/posthoc/ph5_teams/family.csv`, `output/frozen_run/rq3_results.csv`. Held-out: `output_pooled/confirmation_run/ph5/tests.csv`, `output_pooled/confirmation_run/rq3_rows.csv`. |
| **Caption must carry** | Rows differ in population and units, so compare replication status, not size (DC:428). Held-out is a split-sample replication; one-sided tests. B = post hoc in discovery, then supported held-out. The insider and E4 held-out tests are secondary and unadjusted. |

**Not given a figure:** timing (A1, PH6) and federated learning. They are weak or not confirmed, and a figure would give
them weight the tiers do not support. They stay in Table 1. The existing `output_pooled/posthoc/ph5_waves/PH6_waves.pdf`
can go to the appendix.

---

## 8. Weakest points and how the text handles them

| # | Weak point | Why it matters | How the text handles it (where) |
|---|---|---|---|
| 1 | **The "flocking" half of herding is untested.** H2a is inconclusive and fails its hindsight variant (C; DC:295); newcomer × hot is n.s. (DC:307). | Herding has two parts: who enters hot topics, and what they write there. We test only the second, plus uptake speed. | Say it in §5 and §7: "we can say what entrants write and how fast they adopt trends, not whether they crowd into hot topics". Show row 12 as "untested". Cite Borjas and Doran 2015 only as context that crowding can repel (TA:474-485). |
| 2 | **The positive half is tier B; only the negative half is A.** E1, E4, insider and premia were post hoc in discovery. The held-out tests were declared first. Insider and E4 are secondary, one-sided and unadjusted. "One false positive would not be surprising" (DP:29-30). The insider's Holm 0.019 is within-family only, about 0.17 across modules (DP:54-55). | A reviewer may see the continuity half as post hoc fitting. | Open §6 with the asymmetry. Report tiers in every sentence. Lead with E1, the primary test (held-out one-sided p 0.0025, Holm 0.005, MDE80 4.9: adequately powered). Present the insider and E4 as direction only. |
| 3 | **"Method paper" is a type, not novelty** (DC:313-314). | "Entrants propose" could be read as "entrants innovate". | The new content test answers part of it: +5.90 percentile points, also within method papers (+5.24). Wording: "farther from earlier ICLR work in SPECTER2 space", never "more original". |
| 4 | **The content test is unregistered and was added during writing.** It also has a self-continuation confound: incumbents' own earlier papers stay in the reference set (NN caveat 3). Vocabulary from other fields can look distant (caveat 4). | It could be called a garden-of-forking-paths addition. | It is outcome-free (tier E), so no acceptance forking path. Report the sensitivities (excl. 2021, s4, no earlier version, plain definition: all +5.8 to +6.6). Say openly that self-continuation is part of the gap, and that this part *is* continuity among incumbents, so the result cannot be split into "entrants far" vs "incumbents near". Say that 2019 alone is +1.26 (p 0.70). |
| 5 | **The continuity mechanism is unknown.** It could be expertise, evaluator conservatism (Li 2017), visible prestige via arXiv (Ibrahim et al. 2026), selection into teams, or a proven record (H4 +4.6, Holm 0.088, D). | "Continuity" could be read as a claim about reviewers' motives. | The concept is defined by reference point, not motive. §7 names all readings and says the data cannot separate them. The double-blind setting rules out none of them (TA:619-624). Never "bias" or "discount". |
| 6 | **The far jump overlaps with being a newcomer.** Correlation −0.57 (DP:247). | E1 might be the newcomer gap in disguise. | Newcomer control −5.0 (DP:238, 247-248). The E1 population requires an experienced author. Field-distance tests do not replicate, so the gate is not simply penalising unusual content. |
| 7 | **Field level non-discriminating.** H1d fits a package bandwagon, lock-in and efficient choice alike. Reverse causality is possible. "Adapter on an LLM" is labelled method (DC:283-284). | Act 1 could look like a detour. | §2 and the close of §4 say so explicitly. Act 1's job is to establish real convergence and deflate hindsight fashions, not to choose a route. |
| 8 | **Hindsight result.** The early map cannot see post-2020 topics. The maps differ in fitting corpus. | "Of course the early map finds fewer emerging topics." | Present it as a bracket (22.3%-40.9%). The point is that the standard all-years map sits at the top, equal to a late-only map (28). Never "manufacture" without the bracket. Keep the forecast R² in the appendix (no paired test). |
| 9 | **"Riding pays" readings exist:** FM premium +4.62 (D); concurrent twin held-out +3.69 (unregistered; P2 rule); young rising keywords (A1). | They cut against "no reward for following". | A1 rewards being *early*, not following (§6.4). The FM premium is D and does not fade with adoption, which is unlike a fad (§7.4). P2 is mixed and unregistered and goes to the appendix with all three rows. Name these in §7 in one sentence. |
| 10 | **Imitation does appear in surface form** (titles; E\*), and branding's no-premium is D\* (not re-run). | Hiding it would be dishonest; overweighting it would be too. | Report it in §4.5 as imitation-like spread in form. Pair it with Abrahamson and Rosenkopf: bandwagons can spread without reward. Mark D\* and offer to drop row 14 if the ratio cannot be re-run. |
| 11 | **Timing is weak.** A1's CI includes 0; PH6 leans on six inspected keywords (−1.7, p 0.33 without them); FL is not confirmed; the results fall partly in the LLM-review era (LS:375). | A reviewer can dismantle a timing headline. | Timing is a supporting sub-section, not a pillar; it is not in the abstract and has no figure. Quoting rules are applied verbatim. |
| 12 | **Held-out is not an independent holdout.** Shared years, reviewers and authors; the source excluded 1,309 pending cases; mechanism undocumented (DC:43-45, 75). | Over-reading "replicated". | The mandatory sentence in §3 and in the Table 1 caption. "Direction, not size". |
| 13 | **Size failure.** 12.6% / 10.0% rejection at nominal 5% under a cross-map null (DC:249-250). | Inference on H2b/H2c may be anti-conservative. | Reported in §3. t = 6.7 and −4.4 are large relative to the t-inflation of 1.31 / 1.22 (DC:311-312). |
| 14 | **Measurement inputs.** LLM labels (κ 0.93 is LLM-LLM agreement); ICLR-only histories; the 2021 ID switch (bias toward zero, also for the content gap); post-decision text. | Validity. | §3 and Limitations. The R2 variant without 2021-22 gives the same H2b/H2c (DC:148). Novelty without 2021: +5.87. |
| 15 | **Tension with Bao and Li 2025.** Persistence went with lower impact in the previous shift. | It could look like a contradiction. | §7.3: different stage, outcome and shift. "Our data cannot test this." |
| 16 | **Theory citations partly secondary.** Several anchors were seen only in secondary descriptions (TA:665-676). Fujimura's content is secondary (FW:107). | Misattribution risk. | Cite them for their general argument only. Quote only Bourdieu (read in full) and the abstracts of Xiang et al. and Weisberg and Muldoon. |
| 17 | **One venue.** | Generality. | In the title ("at ICLR"), the thesis ("at ICLR"), §8 and Limitations. §2.5 says why the *tests* travel, not the results. |

---

## 9. Open items before writing

1. **Commit the content-novelty analysis.** The script is `paper_ws/scripts/novelty_newcomer.py`; the outputs are
   `paper_ws/output/novelty_newcomer.{json,csv}` and `novelty_paper.csv.gz`. Commit them, for example under
   `research/fashion/output/paper/`, with a short README stating that the analysis is outcome-free and unregistered.
   Until then, Figure 3's content row and Table 1 row 8 have no committed source.
2. **Branding ratio (D\*).** Either re-run it outcome-blind through the frozen machinery, or keep the "earlier
   exploratory, not re-run" label. Drop row 14 if a reviewer objects (LS:937-938).
3. **Read the originals** of the content-secondary theory works before citing any specific result (TA:665-676).
   Network access to the hosts named at TA:42-44 is needed.
4. **Jung et al.** (EMNLP author order) and **Xu et al.** (middle authors): cite the arXiv versions until checked
   (VP:489-490).
5. **Figure 1 numbers.** Quote discovery values from the figure itself, or label the DP:80 values "pooled".
6. **Replace the current draft entirely.** Its framing ("innovation from outsiders; acceptance favours insiders and
   early arrivals") and its RQ1-RQ3 structure are superseded. Its findings table is superseded by Table 1 above. Its
   author block must not be copied into any workspace file.
