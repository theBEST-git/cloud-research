# Story P3: "Herds in Hindsight" (the most ambitious framing)

Story-design file for the ICLR 2017-2026 paper (ACL ARR long paper, 3,000-4,000 body words). Built 2026-11-03.
This file is a design, not the paper. It fixes the thesis, the argument, the main table, the figures and the
honest limits. It gives exact wording only where wording carries weight: thesis, abstract, gap, novelty and guardrails.

## 0. Sources, conventions, and how this framing differs

**Files read in full:**
- dossier_core.md and dossier_posthoc.md;
- landscape.md;
- theory_anchors.md and verify_prior.md;
- the current draft, `research/fashion/paper/riding_the_wave_paper.tex`;
- `paper_ws/output/novelty_newcomer.json` and `.csv`. The file `analysis_novelty.md` does not exist; the novelty
  agent could not write it.

**Also read:**
- the lit_*.md entries for the works cited below;
- story_P1.md, sections 1-4 only, so that P3 does not duplicate P1;
- the headers of committed result files, to confirm a source exists for each figure (Section 7);
- Figure 1 and three presentation figures (`hindsight_emerging.png`, `premia_scatter.png`, `fig1_waves.png`).

**What was not touched:**
- no outcome or decision column of any data file;
- no analysis script run;
- no corpus author named.

**Pointers.**

| Pointer | File |
|---|---|
| `DC:n` / `DP:n` | dossier_core.md / dossier_posthoc.md, line n |
| `LS:n` | landscape.md, line n |
| `TA:n` / `VP:n` | theory_anchors.md / verify_prior.md, line n |
| `NN:key` | `paper_ws/output/novelty_newcomer.json`, `results.key` (workspace file, **not committed**) |
| `FW:`, `ME:`, `NR:`, `OUT:`, `CP:` | lit notes, as in landscape.md |

**Tiers** (DC:25-31; DP:12-19):

| Tier | Meaning |
|---|---|
| A | Registered and replicated on held-out papers |
| B | Post hoc in discovery, then a declared held-out test supported it |
| C | Registered but inconclusive or not replicated |
| D | Discovery only |
| E | Descriptive; no acceptance outcome |
| E\* / D\* | Earlier exploratory title analysis. E\*: share re-verified. D\*: acceptance ratio not re-run. |

In the paper, every number carries its tier in brackets, e.g. "−6.09 pp [B]".

**Mandatory wording, which travels with every use** (DC:38-56; DP:35-61; LS:897-925):
- "Held-out" means "a pre-registered out-of-sample replication, not a certified untouched holdout".
- A supported held-out test confirms direction, not size.
- An underpowered null is "uninformative", not "no effect".
- Crowding: say "no detectable premium".
- Every result is an association; never write "causes", "choose" or "should", and give no advice.
- A method paper is a contribution *type*, not novelty.
- Labels are LLM labels, not human labels.
- FL is "not confirmed". P1b "did not replicate". For A1, say the CI includes 0. For PH6, say it leans on six
  inspected keywords. Apply the P2 and E2 quoting rules.
- No effect-size comparisons across modules.

### How P3 differs from P1 and from the seven landscape candidates

**P1 and Candidate 1** ("Anchored, not herded"):
- They organise the paper around *two routes to conformity*.
- The hindsight result is Act 1, a measurement lesson.

**Candidate 4** ("History without hindsight"):
- It makes hindsight the headline.
- The substance becomes a sorted list (LS:672-676).

**P3 joins the two through one new spine: hindsight against foresight.**
- **The claim is general.** It is about how science comes to *see* a field as a herd. A field looks herd-like when
  it is read in hindsight, in three ways:
  - categories fitted after the fact;
  - cases chosen for their outcome;
  - patterns estimated on the data that suggested them.
- **The study is the test.** Each hindsight channel has a foresight counterpart, and the study applies all three to
  the herding account at the three points where it makes predictions: the waves, the entrants and the review
  decision.
- **The result is differential survival.** Under foresight, every imitation signature we could test shrinks, fails
  or reverses. The package shift and three associations referenced to a team's own record hold.
- **The design becomes the evidence for the thesis**, not a methods section. The registered prediction that failed,
  our own herding forecast, becomes the hook. The weak and failed results (FL, PH6 without the inspected keywords,
  P1b) stop being embarrassments and become demonstrations of the thesis.
- **The imitation/continuity distinction is kept** (TA §3) as the *substantive* theory that the foresight test
  adjudicates.

Alternatives were considered and set aside:
- **"Entrants vary, records are selected"**, an evolutionary division of labour. Its reward half invites a reading of
  newcomer bias, and the newcomer gap is mostly composition (D; DP:181-183).
- **"Novel to the field, not to yourself"** as the headline. Its field-novelty leg is C/D only (DP:257-266). Both
  survive as expansions inside P3 (§5 and §6.2).

---

## 1. Title and thesis

### Title

**Herds in Hindsight: Machine Learning's Research Waves, Tested in Foresight**

Alternatives, in order of preference:
1. "Herds in Hindsight: Entry, Continuity and Review at ICLR, 2017-2026"
2. "A Herd Only in Hindsight? Testing the Fashion Account of Machine Learning's Foundation-Model Wave"

**Why this title.**
- It names a phenomenon ("herds appear in hindsight") without asserting that herds are absent.
- The flocking half of herding is untested (H2a, C; DC:295), and unrewarded bandwagons cannot be ruled out
  (TA:280-286). A title such as "No Herd" would overclaim.

### Thesis (one sentence)

> Read in hindsight, machine learning's foundation-model wave looks like a herd; tested in foresight on the same ICLR
> submissions, the testable signatures of imitation shrink, fail or reverse. What survives is a shared technical
> package, topic entrants who bring proposals rather than follow-on work, and acceptance that goes with continuity of
> a team's own record rather than with following the crowd.

**Short form:** "In foresight, the herd fades and the record remains."

### The memorable formulation (closes the abstract, introduction and conclusion)

> **Hindsight sees a herd; foresight finds a record.**

"Record" carries both meanings the paper needs: the field's record as it was *at the time* (foresight measurement),
and the team's track record (continuity).

### Definitions the whole paper uses (fixed)

**Foresight evidence** is evidence about a period that is built without access to the outcome it is used to explain.
It comes in three forms, one per hindsight channel:

| Channel | Hindsight form | Foresight counterpart |
|---|---|---|
| **Categories** | A topic map fitted on all years, including the years it describes | A map fitted on 2017-2020 papers only (DC:179), applied unchanged to later papers |
| **Cases / claims** | Patterns or cases chosen after their outcome was seen | Hypotheses registered or declared before the outcome they test was seen (DC:237-246, 390; DP:140, 226) |
| **Estimates** | Contrasts estimated on the same papers that suggested them | The same contrasts re-estimated on 11,099 held-out papers (DC:72), or a topic's edge in a later period (DC:376) |

**Hindsight evidence** is the mirror image. A fourth, minor channel is **text written after the decision**:
camera-ready abstracts carry code links (17.6% of accepted vs 0.5% of rejected, 2023-26; DP:83). It is closed in
discovery by the link-removal re-run (DP:369-372) and open in held-out (DP:25).

**The two routes to conformity** (TA:559-575):

| Term | Definition |
|---|---|
| **Imitation** | Conformity whose reference point is *what others are doing now* (popularity, momentum, what is hot) |
| **Continuity** | Conformity whose reference point is *an accumulated record*: the team's own past work, or the topic's past work carried by a team member who has already submitted in it |
| **Priority** (timing) | Belongs to neither route. It is the test that separates rewarded imitation from priority-based reward (TA:552-553). |

**Usage rules:**
- These words label *positions* of papers, not motives (TA:630-631).
- "Anchored" appears at most as a defined adjective, with the Tversky-Kahneman footnote (TA:573-574).
- Never "exploitation" (TA:114-115).

---

## 2. Conversations, gap, novelty wording, and why it matters beyond ICLR

### 2.1 The conversations (primary first)

1. **Fashion, herding and bandwagons in science, and ML's self-critique** (LS Conversations 1 and 5).
   - **The claim we test:** fast fields move by imitation. This is argued in theory (Abrahamson 1991; Bikhchandani et
     al. 1992; Banerjee 1992) and asserted for ML (Lipton and Steinhardt 2019; Hooker 2021; Dehghani et al. 2021;
     Bommasani et al. 2021).
   - **The open problem:** the evidence for fashion is overwhelmingly retrospective.
     - Lifecycles are drawn from discourse counts after the fashion has passed (Abrahamson and Fairchild 1999; FW:33-37).
     - Hype-cycle shapes are inconsistent when tested (Dedehayir and Steinert 2016; van Lente et al. 2013).
     - Fads are narrated from success stories (Strang and Macy 2001).
     - ML critiques are mostly essays (FW:308; CP:137).
   - **Our contribution:** the account's predictions tested in foresight at three points. The entrant prediction
     reversed (A). The gate's fashion signals shrink or are not confirmed (B, C). What remains is continuity (B).
2. **Measuring a field's topics and their emergence** (LS Conversation 4).
   - **Standard practice:** field histories and emergence indicators fit one classification on the whole period:
     - field histories: Hall et al. 2008; Anderson et al. 2012; Pramanick et al. 2023;
     - emergence indicators: Small et al. 2014; Klavans et al. 2020.
   - **What is known:** classifications re-read the past (Leydesdorff 2002), and "emergence" is partly judged after
     the fact (Rotolo et al. 2015).
   - **Our contribution:** the hindsight effect *quantified on the same papers with the same model*, with only the
     fitting window differing (29 vs 8 emerging topics). We also show that it compounds with growth, and that it
     changes which substantive claims hold.
3. **Tradition, novelty and their reward; outsiders and entry** (LS Conversations 2 and 3).
   - **Our contribution:** at the decision, in one complete population:
     - the associations that replicate are referenced to a team's own record (far jump, closeness, insider; B);
     - the associations referenced to the field's record do not replicate (P1b, P7; C);
     - topic entrants are where content farther from earlier work comes from (E), and they bring method proposals (A).
4. **Supporting conversations:** peer review at ML venues (LS Conversation 6) and confirmatory meta-research
   (LS Conversation 7). These supply design and rival readings, not novelty claims (Ibrahim et al. 2026 already
   pre-registered an ICLR out-of-sample test; VP:202-207).

### 2.2 The theoretical gap

**Imitation and continuity have old and separate roots** (TA §1-2):
- **imitation:** DiMaggio and Powell 1983; Haunschild and Miner 1997; Scharfstein and Stein 1990; Abrahamson and
  Rosenkopf 1993;
- **continuity:** March 1991; Levitt and March 1988; Stuart and Podolny 1996; Cohen and Levinthal 1990; Bourdieu 1975.

Weisberg and Muldoon (2009) separate the two inside one model. Writing on herding in science merges them (Weisberg
2013; Baddeley 2015). Xiang, Romero and Teplitskiy (2025) treat "social context, identities, and path dependence" as
distinct drivers of topic choice and list entry costs and topic rewards as open questions (TA:453-472).

**What P3 adds.** P3 adds a second, *epistemic* gap. The hindsight channels can produce the observable signatures of
imitation whichever route actually operates:
- **Categories:** a whole-period map splits the crowded late period finely, so many topics look "emerging".
- **Cases:** a fad narrated from a case chosen after it soured.
- **Estimates:** in-sample topic edges and momentum overstate persistence. Strang and Macy (2001) show these are the
  very "success stories" that drive outcome imitation.

A test of the herding account that does not close these channels cannot tell imitation from hindsight.

### 2.3 Closest prior work and what each leaves open

| Work | What it did | What remains for us | Effect on our wording |
|---|---|---|---|
| Wang et al. 2023 (*World Wide Web* 26:683-708; arXiv 2103.05885) | ICLR 2017-2020: topic-cluster acceptance differences; arXiv posting advantage | No time dynamics, no entry status, no out-of-sample test | Claim only that topic edges **regress out of sample** (VP:99-104) |
| Xu et al. 2026 (arXiv 2607.27209; middle-author order unresolved) | ICLR 2021-2026, 50,289 papers: topic predicts acceptance at equal scores | A rival mechanism (score scales), not a persistence test | "Topics differ in acceptance, even at equal scores (Wang 2023; Xu 2026); in foresight these edges are real but regress" (VP:184-186) |
| Jung et al. 2025 (arXiv 2509.25701; EMNLP author order unresolved) | ICLR 2017-2025, 28,358 submissions: process factors, including earlier submission | "Early" means early in the submission window, not early in a wave | Define "early" as early in a keyword's wave (VP:161-163) |
| Ibrahim et al. 2026 (arXiv 2607.26280) | Borderline prestige gap at ICLR 2019-2025; **pre-registered 2026 cohort**; gap concentrated where arXiv identifies authors | Prestige, not a paper's position in a topic or a record | No "first registered/prospective design". It is a rival reading of the insider premium (VP:211-218). |
| Bao and Li 2025 (arXiv 2506.22729) | SPECTER2 similarity to one's own prior ICML/NeurIPS papers across the deep-learning shift; persistence goes with lower impact | Outcome is impact, not acceptance; studies incumbents, not entrants | The closeness measure is **not new**. Their result is a tension for the Discussion (VP:131-136). |
| Hill et al. 2025 (*Nature* 642:999-1006) | Larger pivots: lower citations and lower publication success | The decision itself, every submission, double-blind, held-out | Never "first pivot penalty at the gate"; say "we observe the decision itself" (VP:311-316). Do not quote their numbers until the PDF is checked. |
| Stelmakh et al. 2023 (*PLOS ONE* 18(7):e0287443) | ICML 2020 RCT: no herding detected in reviewer discussions | Authors and entry | Pair it with our entrant result; say "no herding detected" (VP:265-270). Kargaran et al. 2025 report co-reviewer influence, so never "reviewers are independent". |
| Boudreau et al. 2016 (*Mgmt Sci* 62(10):2765-2783) | Evaluators score proposals closer to their own expertise, and highly novel ones, lower | Their distance runs from evaluator to proposal | Do not equate it with our far-jump distance (VP:330-337) |
| Li et al. 2025 (*PeerJ CS* 11:e2875); Khanbayov and Kurban 2026 (arXiv 2606.12828) | Static-model emergence detection; a prospective early-warning signal tested on later years | Neither compares hindsight and early-only maps on the same papers | "Same papers, same model, only the fitting window differs: 29 vs 8" (VP:365-370) |
| Leydesdorff 2002; Rotolo et al. 2015 | Classifications re-read the past; emergence attributes are judged after the fact | Stated in concept; not quantified | We measure it (ME:174, 194) |
| Movva et al. 2024; Huang 2026; Biliotti et al. 2024 | Entrants are numerous in LLM work; topic initiators precede growth; topic-specific newcomer definition | Contribution type and content distance of entrants; the gate | Neighbours for §5. "Entrants are numerous" is not ours (LS:487). |
| Strang and Macy 2001 | Adaptive emulation of success stories yields fad cycles | No test against an independent verdict | Theory for the case and estimate channels |

### 2.4 Exact novelty wording (drop-in for the introduction)

> Studies of ICLR's open records have related acceptance to author prestige and visibility (Tran et al., 2020;
> Ibrahim et al., 2026), to the review process (Jung et al., 2025), and to research area (Wang et al., 2023; Xu et al.,
> 2026). Studies of the producers describe who enters machine-learning topics and how far researchers stay from their
> own past work (Movva et al., 2024; Bao and Li, 2025), and the science of science shows that moving far from one's own
> record costs citations and publication (Hill et al., 2025). Static topic models can miss small emerging topics (Li et
> al., 2025), and prospective early-warning signals for AI topics have been tested on later years (Khanbayov and Kurban,
> 2026). To our knowledge, among the works we checked, no study asks within one complete submission population whether
> the herding account of a field's waves holds at three points — how the waves are measured, what kind of work topic
> entrants bring, and what the review decision goes with — nor tests these predictions in foresight: with maps fitted
> before the period they describe, hypotheses registered before outcomes were seen, and replication on held-out papers.

**Measurement sentence (G4):** "On the same papers, with the same model and only the fitting window differing, a map
fitted on all years finds 29 emerging topics where a map fitted on 2017-2020 finds 8."

**Theory sentence (one only):** "To our knowledge, imitation and continuity have not been tested against each other at
entry and at the review gate." (TA:79-82; the search was limited.)

**Phrases that must not appear:**

*From verify_prior.md (VP:477-483) and landscape.md (LS:479-492):*
- "first study of acceptance at ICLR by topic";
- "first evidence of a pivot penalty at the gate";
- "first pre-registered study at an ML venue";
- "first to measure distance from one's own work";
- "reviewers (do not) herd".

*Added for P3:*
- "ML is not a herd";
- "herding is an illusion" or "an artefact";
- "hindsight manufactures waves" without the bracket 8-29 and the corpus caveat (DC:187, 229);
- "first prospective" or "first foresight design";
- "the gate rewards" or "the gate penalises" (say "acceptance goes with");
- "entrants are more innovative" (say "propose methods" and "write farther from earlier work").

Keep "among the works we checked" (CP:7; VP:423).

### 2.5 Why it matters beyond ICLR

1. **It changes how fields are diagnosed.** Claims that a field moves by fashion usually rest on evidence exposed to
   all three hindsight channels:
   - histories drawn with whole-period topic maps;
   - fad stories told from cases chosen after they soured;
   - in-sample "hot topic" premia.

   We show, for one field, how far each inflates the herd-like picture. We also show that removing them changes the
   *substantive* conclusion, from imitation to continuity. The checks need only dated records and a held-out split,
   so they travel to any field.
2. **Growth amplifies hindsight.** The field grew 40-fold (DP:71), and 69.3% of papers come from 2024-26 (DP:72).
   - A map fitted on all years therefore finds as many emerging topics as one fitted on 2024-26 alone (29 vs 28;
     DC:176, 181).
   - Fast-growing fields, which are the ones most often called faddish, are where whole-period maps distort most.
   - The same maps underlie emergence indicators built for decision makers (Small et al. 2014; Klavans et al. 2020;
     ME:60, 96).
3. **The conservatism debate.**
   - Which distance goes with rejection is contested: novelty (Wang et al. 2017; Boudreau et al. 2016) or not
     (Teplitskiy et al. 2022).
   - At one double-blind gate, with rejected papers visible, the replicated associations are with distance from the
     team's *own* record. Associations with distance from the *field* do not replicate.
   - This is a narrower, decision-level version of the pivot penalty (Hill et al. 2025). It comes with an explicit
     expertise-versus-visibility caveat (Li 2017; Ibrahim et al. 2026).
4. **The ML hype debate.**
   - Real homogenisation around a package holds (A), which supports Bommasani et al. 2021.
   - Entrant herding fails (A, reversed), and following has no detectable premium (C).

   This is a more specific picture than "the field chases trends".
5. **The collective stakes differ by route.** This is interpretation, not advice.
   - Imitation's cost is premature convergence (Zollman 2010; Banerjee 1992).
   - Continuity's cost is competency traps and slow collective discovery (Levitt and March 1988; March 1991; Rzhetsky
     et al. 2015).

   Mistaking one for the other misdiagnoses the field.

---

## 3. Abstract (183 words)

> Fast-moving fields are often called herds: researchers chase what is hot, and review rewards it. Much of the
> evidence comes from hindsight: maps fitted afterwards, cases chosen for their outcome, patterns estimated on the data
> that suggested them. We test this account of machine learning's foundation-model wave in foresight on 43,480 ICLR
> submissions (2017-2026), rejected and withdrawn included, using maps fitted before the wave, registered hypotheses
> and 11,099 held-out papers. Hindsight inflates the waves: on the same papers, an all-years map finds 29 emerging
> topics, a 2017-2020 map 8. In foresight, the signatures of imitation shrink, fail or reverse. Our registered herding
> prediction reversed: topic newcomers more often propose methods and less often build benchmarks; descriptively, their
> papers also lie farther from earlier work. Topic acceptance edges regress, the starkest fad case is not confirmed,
> and crowding shows no detectable premium. What survives is a package shift, foundation models displacing new
> architectures, and continuity: in post hoc tests replicated on held-out papers, acceptance goes with closeness to the
> team's own record and a topic insider. Hindsight sees a herd; foresight finds a record.

The count was made with `wc -w` (182 for the saved draft in `paper_ws/_abs_p3.txt`, plus "comes from" in place of
"is"). "2017-2026" counts as one token.

**Where each claim comes from:**

| Claim | Source | Tier |
|---|---|---|
| 43,480 submissions; rejected and withdrawn included | DC:65-66 | E |
| 11,099 held-out papers | DC:72 | E |
| Maps fitted before the wave; registered hypotheses | DC:179, 193, 237 | E (design) |
| 29 vs 8 emerging topics, same papers | DC:176-179 | E |
| Imitation signatures shrink, fail or reverse | Table 1, Panels A-C | A/B/C/E |
| Newcomers: more method, fewer benchmark/dataset/evaluation papers | DC:296-297, 365-366 | A (reversed) |
| Newcomers' papers farther from earlier work | NN:main_pct (+5.90 [4.95, 6.85]) | E (unregistered) |
| Topic edges regress | DC:376 (b 0.60 [0.32, 0.88]) | B |
| Starkest fad case not confirmed (FL) | DC:368-369 | C (discovery: D) |
| Crowding: no detectable premium | DC:324, 367 | C |
| FM adoption with fewer new architectures | DC:271, 364 | A |
| Closeness to own record; topic insider | DC:370, 372, 374 | B |

**Abstract guardrails:**
- "Build benchmarks" is shorthand for "benchmark, dataset or evaluation papers"; the body uses the full phrase.
- "Signatures of imitation" means those tested in foresight. The FM premium (D) was never tested in foresight; the
  body says so (§6.3).

---

## 4. Three contribution statements

1. **Conceptual (how a field comes to look like a herd).**
   - We distinguish two routes to conformity, imitation of what others do now and continuity with an accumulated
     record.
   - We identify three hindsight channels that can produce imitation's signatures whichever route operates:
     categories fitted afterwards, cases chosen for their outcome, and patterns estimated on the data that suggested
     them.
   - Pairing each channel with a foresight counterpart turns the fashion account into tests at the three points where
     it makes predictions: the waves, the entrants and the review decision.
   - To our knowledge, the two routes have not been tested against each other at entry and at the gate.
2. **Empirical (differential survival).** In one complete submission population of a fast-moving venue, the
   imitation signatures we tested in foresight shrink, fail or reverse:
   - the registered herding prediction for entrants reversed [A];
   - topic acceptance edges regress [B];
   - the starkest fad case is not confirmed [C];
   - crowding shows no detectable premium [C].

   What holds:
   - the package shift [A];
   - all three record-referenced associations with acceptance [B].

   Entrants' papers also lie farther from earlier work [E].
3. **Measurement and design.**
   - On the same papers with the same model, only the fitting window differing, a hindsight map finds 29 emerging
     topics where an early map finds 8.
   - It makes topic growth look predictable (R² 0.28 vs −0.03).
   - It reverses a trend conclusion.
   - In a field that grew forty-fold, it finds as many emerging topics as a map of the last three years alone.
   - We give a cheap check for computational histories, and we report every claim with an evidence tier from a
     registered, sealed, single-run design with held-out replication and a disclosed size failure.

---

## 5. The argument, section by section

### 5.0 The spine (every section serves these five sentences)

1. A fast field looks like a herd when read backwards (Figure 1).
2. That reading passes through three hindsight channels, each of which can produce imitation's signatures by itself.
3. We close each channel and re-test the herding account at three points.
4. At every point the imitation signatures shrink, fail or reverse, while the package and the record-referenced
   associations hold.
5. Therefore the conformity this field shows in foresight is continuity, not imitation. How herd-like a field looks
   depends on how much hindsight went into looking.

**Word budget: 3,800 body words.**

| Section | Words |
|---|---|
| §1 Introduction | 650 |
| §2 Background | 450 |
| §3 Data and design | 450 |
| §4 Waves | 500 |
| §5 Entrants | 600 |
| §6 Gate | 700 |
| §7 Discussion | 350 |
| §8 Conclusion | 100 |

### §1 Introduction (650 words)

**Role.** Show the hindsight picture, name the problem with it, give the reflexive hook, state the move and the
answer.

**¶1. The hindsight picture (Figure 1).**
- Keyword shares:
  - "generative adversarial networks": 8.1% (2018) to 0.09% (2026);
  - "large language models": 0.26% (2022) to 16.7% (2026) (DP:80; E).
- 17 of 68 frequent keywords rose and fell (DP:81; E).
- Foundation-model (FM) papers: 0.3% to 54.4%. New-architecture papers: 24.5% to 7.5% (DC:163-164; E).
- Submissions grew 40-fold (DP:71; E).
- Read backwards, this is a herd. Critics say so of ML (Lipton and Steinhardt 2019; Hooker 2021; Bommasani et al.
  2021), and theory explains why it would be (Bikhchandani et al. 1992; Abrahamson 1991).

**¶2. The problem.**
- Pictures like Figure 1 are assembled with hindsight in three ways:
  - **topics** are fitted on the whole period (Hall et al. 2008; Leydesdorff 2002; Rotolo et al. 2015);
  - **cases** are shown because they rose and fell, as Figure 1's keywords were;
  - **contrasts** are estimated on the data that suggested them (Kerr 1998).
- Hindsight makes the past look more determined than it was (Fischhoff 1975). Each channel can make a field look
  herd-like whatever its researchers did.

**¶3. The reflexive hook.**
- "We expected a herd too." Before seeing any outcome we registered that topic newcomers would write more benchmark
  and evaluation papers and fewer method papers.
- The prediction came out reversed, and the reversal held on held-out papers [A] (DC:33-36, 296-297).

**¶4. Design in one paragraph.**
- 43,480 ICLR submissions, 2017-2026, rejected and withdrawn included (DC:65-66).
- One foresight counterpart per channel:
  - maps fitted on 2017-2020 papers;
  - hypotheses registered before any full-corpus label existed, with outcomes sealed and one 18-second run
    (DC:237, 245-246);
  - every post hoc pattern declared before being retested on 11,099 held-out papers (DC:72): "a pre-registered
    out-of-sample replication, not a certified untouched holdout".
- Tiers A-E.

**¶5. Results in one paragraph,** the same pattern at three points:
- **Waves:** hindsight inflates them (29 vs 8 [E]), but the package shift survives [A].
- **Entrants:** the herding prediction reversed [A]; their papers lie farther from earlier work [E]; first-time teams
  adopt trends more slowly [E].
- **Gate:**
  - imitation's signals shrink or fail: edges regress [B], FL is not confirmed [C], crowding shows no detectable
    premium [C];
  - the record holds: far jump, closeness and insider [B];
  - earliness holds only weakly [B weak].

**¶6. Thesis and contributions.** The thesis sentence; the three contributions (Section 4, compressed); the novelty
paragraph (Section 2.4, compressed to two sentences); the memorable line.

### §2 Background: Two Routes to Conformity, Three Routes to Hindsight (450 words)

**Role.** Supply the theory that makes the test discriminating. Say what each route predicts at each point, and how
hindsight would mimic imitation.

**¶1. Two routes** (TA:652-659, the drop-in paragraph, trimmed).
- Imitation: Bikhchandani et al. 1992; DiMaggio and Powell 1983; Haunschild and Miner 1997.
- Continuity: March 1991; Stuart and Podolny 1996; Sekara et al. 2018; Bourdieu 1975.
- Weisberg and Muldoon 2009 separate "followers" from agents who search from their own position. Cite Alexander et
  al. 2015 as the critique, and say we use the *taxonomy* only.
- Weisberg 2013 merges the two.
- Footnote on "anchored": Tversky and Kahneman 1974; Baddeley 2015.

**¶2. Predictions at three points** (TA:598-606, condensed):
- **Waves.**
  - Both routes, and efficient choice, predict convergence on a package (Fujimura 1988; Arthur 1989; Sutton 2019),
    so this is a weak test.
  - Imitation alone predicts that duplication *per pair* rises.
- **Entry.**
  - Imitation predicts that entrants, who face the most uncertainty, imitate most (DiMaggio and Powell 1983): they
    write follow-on work, flock to hot topics and adopt trends fast.
  - Continuity predicts that entrants bring proposals from elsewhere (Jeppesen and Lakhani 2010; Azoulay et al.
    2019; Bourdieu's "succession or subversion") and absorb the field's package slowly (Cohen and Levinthal 1990).
- **Gate.**
  - Rewarded imitation (Scharfstein and Stein 1990) predicts premia for crowded topics, for favoured topics and for
    late riding.
  - Continuity predicts lower acceptance for far jumps and higher acceptance with an insider (Hill et al. 2025; Sekara
    et al. 2018).
  - Timing separates rewarded imitation from priority (Merton 1957; Strevens 2003).
  - An absence of premium does not rule out unrewarded bandwagons (Abrahamson and Rosenkopf 1993).

**¶3. Three routes to hindsight, and why each mimics imitation.**
- **Categories.** A map fitted on all years partitions the crowded late years finely, so topics appear to "emerge"
  (Leydesdorff 2002; Rotolo et al. 2015; Li et al. 2025). This is temporal leakage applied to description (Kaufman et
  al. 2012; Kapoor and Narayanan 2023).
- **Cases.** Fads are narrated from vivid cases chosen after they soured (Strang and Macy 2001; Kerr 1998).
- **Estimates.** In-sample extremes overstate persistence (Bailey et al. 2017; Gelman and Loken 2014). In Strang and
  Macy's model such success stories are what outcome imitation follows (Haunschild and Miner 1997).
- Growth amplifies the first channel (Price 1963).
- **The hindsight account's meta-prediction:** imitation signatures weaken under foresight, while real regularities
  hold whichever route they belong to.

**¶4. The gap paragraph** (Section 2.4), with Xiang et al. 2025 as the theory-gap sentence.

### §3 Data and a Foresight Design (450 words)

**Role.** Show how each hindsight channel is closed. Define the measures once.

**Corpus.**
- Our dated acquisitions of official OpenReview records: 43,480 discovery submissions with usable abstracts,
  2017-2026 (DC:62-65), rejected and withdrawn included.
- Acceptance tests: 32,190 decided papers, 40.1% accepted; 9,986 withdrawn papers are left out (DC:318).
- Held-out: 11,099 papers, 8,185 of them decided in 2018-26 (DC:72-74).
- Say that full ICLR records are a standard source (Wang et al. 2023; Jung et al. 2025; Xu et al. 2026), so the data
  source is not a contribution.

**Measures (one line each):**
- **Topics:** SPECTER2 embeddings of title and abstract (Cohan et al. 2020; Singh et al. 2023), spherical k-means with
  k = 100. NMI with ICLR primary areas 0.302, against 0.272 for a word-count baseline (DC:86-90).
- **Contribution type:** a fixed LLM codebook; κ 0.93 against an LLM reference; LLM labels, not human (DC:129-133).
- **Newcomer paper:** no author has an earlier ICLR submission in that topic, whatever its outcome (DC:144). The
  definition is relative to the topic, as in Biliotti et al. 2024. The 2021 author-ID switch biases it towards zero
  (DC:145-146).
- **First-time team:** no author has any earlier ICLR submission (TA:684-685).
- **Far jump:** F_max, the SPECTER2 cosine between a paper and the closest experienced co-author's earlier ICLR
  submissions, histories since 2021 (DP:231-232). This is the same kind of measure as Bao and Li 2025.
- **Topic insider:** an author with any earlier submission in the topic; an acceptance is not required (TA:587-591).
- **Content distance:** one minus the mean cosine to the 10 nearest papers from earlier years, ranked as a
  percentile within topic and year (NN; DP:255).

**Foresight devices, one per channel** (the paragraph that carries the story):
- **Categories:** every registered claim must also hold on the 2017-2020 map, read on 2021-2026 papers, and on a
  year-balanced map (DC:193, 239).
- **Claims:**
  - registered on 2026-10-13, before any full-corpus label existed (DC:237);
  - outcomes readable by one sealed module only (DC:245);
  - a single frozen run (DC:246);
  - post hoc analyses declared before they were run (DC:390; DP:140, 226);
  - earlier exploratory looks disclosed (DC:238).
- **Estimates:** registered one-sided tests on 11,099 held-out papers (DC:256-259). These are pre-registered
  out-of-sample replications that support direction, not size (DC:43-47).
- **Text:** camera-ready leakage (17.6% vs 0.5% code links) is handled by the link-removal re-run in discovery
  (DP:369-372). Held-out text has no such check (DP:25).

**Honesty line.**
- Under one simulated null, the main entrant test rejected 12.6% / 10.0% at a nominal 5%, and a bootstrap did not fix
  it (DC:249-250).
- Like Ibrahim et al. 2026, we test pre-registered predictions on later ICLR papers.

### §4 The Waves, in Foresight (500 words)

**Role.** Act 1. The field-level picture: how much of the wave is hindsight, and what survives foresight.

**Claims and findings:**
1. **The number of waves depends on when the map was fitted** [E].
   - Emerging topics on the same papers, same model and same rule (≥3× share growth):
     - all-years map: **29**;
     - 2017-2020 map: **8**;
     - year-balanced map: 16;
     - 2024-26 map: 28 (DC:176-181).
   - The share of 2024-26 papers in emerging topics is bracketed between 22.3% and 40.9% (DC:187).
   - Declining topics: 13 on the all-years map vs 26 on the year-balanced map (DC:176, 178).
   - Wording: "inflates", with the bracket. Caveat: the early map cannot represent topics born after 2020, so the
     truth lies inside the bracket (DC:187, 228).
2. **Growth compounds hindsight** [E].
   - 69.3% of papers come from 2024-26 (DP:72).
   - The all-years map finds as many emerging topics as a map of those three years alone (29 vs 28).
3. **Hindsight makes growth look predictable** [E].
   - Topic size predicts two-year growth out of time with R² 0.281 [0.217, 0.335] on the all-years map, and −0.033
     [−0.082, −0.002] on the early map (DC:217).
   - In-sample probability of top-fifth growth by size tercile (small / mid / large): 40 / 21 / 2% on the all-years
     map, 22 / 20 / 20% on the early map (DC:224).
   - Caveat, stated: the maps also differ in fitting corpus, and there is no paired test (DC:227-231).
4. **Conclusions flip with the map** [E; counted variants of C].
   - "Topics age from method papers to measurement papers" is null on the all-years map: H1a −0.14 [−1.78, +1.49];
     H1b +0.50.
   - On the early map, read on 2021-26 papers: −3.48 [−6.21, −0.76] / +3.96 [+1.35, +6.57] (DC:201-202).
   - Exploratory and unadjusted. By the registered rule the claim is "not supported"; we claim neither reading
     (DC:210-211).
   - Expansion: in hindsight new topics multiply; in foresight existing topics mature. This is one sentence, flagged
     exploratory, and it foreshadows §5's incumbents who consolidate.
5. **What survives: the package** [A].
   - Where more of a topic's previous-year papers built on FMs, fewer of its papers propose new architectures:
     −7.98 [−12.14, −3.82] in discovery; −11.0 [−18.1, −3.9] held-out, one-sided p 0.0013.
   - Robustness: 9/9 variants; both hindsight variants pass; the weakest held-out variant is the prospective early
     map, −5.4 (two-sided p 0.24) (DC:271, 278).
6. **Interpretation.**
   - A Fujimura-type package bandwagon fits (Fujimura 1988; Bommasani et al. 2021), but so do lock-in (Arthur 1989)
     and efficient choice (Sutton 2019). The field level cannot tell the routes apart (TA:614-617).
   - Bao and Li 2025 describe the analogous displacement in the previous shift; theirs is descriptive.
   - Transition to §5: "The field converges. Whether its people herd is a question for the entrants."

**Placement.**
- F1 and F2 are core here.
- The diversity-peaks finding (DC:189-192) goes in one clause or the appendix.

### §5 The Entrants, in Foresight (600 words)

**Role.** Act 2, the sharpest discriminating test. Imitation predicts that entrants imitate most.

**Claims and findings:**
1. **The registered herding prediction reversed** [A, reversed].
   - Newcomer papers (72.9% of papers; DC:151) are more often method papers: +3.71 [+2.61, +4.80] in discovery,
     +3.60 [+1.48, +5.71] held-out, one-sided p 0.0007.
   - They are less often benchmark, dataset or evaluation papers: −1.70 [−2.46, −0.93] in discovery, −2.10
     [−3.35, −0.85] held-out.
   - Base rates: 75% method, 7.7% measurement.
   - Robustness: 10/10 variants; both hindsight variants pass (+3.10 / +2.16; −1.41 / −0.86) (DC:296-297).
   - Sentence on the size failure: t = 6.7 and −4.4, against stress inflation factors of 1.31 and 1.22 (DC:311-312).
2. **Part of the measurement gap is team composition** [robustness of A].
   - With log team size, H2c shrinks to −0.54 [−1.11, +0.04] (p 0.07); held-out −0.98.
   - H2b is unchanged at +3.92 (DC:301, 308).
   - Reading: small all-new teams against larger mixed teams.
3. **Not just a label: the content is farther from earlier work** [E, unregistered, added during writing].
   - Newcomer papers sit +5.90 percentile points [4.95, 6.85] higher in content distance from earlier ICLR papers
     than incumbent papers in the same topic and year (N 42,325; 100 topic clusters; NN:main_pct).
   - Within method papers only: +5.24 [4.16, 6.31] (NN:method_only_pct). Size: 0.22 of the within-cell SD
     (NN:raw_cosine_nov_x100).
   - With team, class and FM controls: +5.76 [4.82, 6.70] (NN:team_class_fm_ctrl_pct).
   - By year: +5.0 to +6.4 in 2020 and in 2022-2026; 2019 +1.26 (p 0.70); 2021 unreliable, with about 11 incumbent
     papers (NN:year_*).
   - This answers "contribution type is not novelty" (DC:313-314). It is descriptive and is not originality.
4. **Entrants are not trend-chasers** [E].
   - First-time teams use young rising ("Emerging") keywords less often than returning teams: 16.7% vs 25.0%,
     −3.7 pp, q 6e-6 (DP:315-316).
   - Against returning teams new to the topic, they write FM papers less often: −4.6 / −9.0 / −14.7 pp at 5-15 /
     15-30 / 30-50% prior adoption; −2.0 at ≥50% (p 0.14) (DP:360-362).
   - Expansion, interpretive: "the package travels with records". Teams with an ICLR record carry it into new topics;
     novices do not (absorptive capacity; Cohen and Levinthal 1990; TA:147-152).
5. **Duplication follows volume, not piling on** [E].
   - The share of papers with a same-year twin rose from 19.5% to 48.8%, but twins per paper per 1,000 submissions
     fell from 0.32 to 0.19 (DP:78-79).
   - Newcomer papers are less often twinned: −3.9 [−5.0, −2.7] (DP:275).
   - This is the categories channel's cousin: a raw count read without normalising for growth.
6. **What we cannot say** [C].
   - Whether entrants flock to hot topics is untested. H2a: −0.73 [−2.68, +1.22]; the hindsight variant fails
     (DC:295). Newcomer × hot is n.s. (DC:307).
   - State it in this section, not only in the Limitations.
7. **Pairing.**
   - "A randomised trial found no herding detected among reviewers at ICML (Stelmakh et al. 2023). We find that topic
     entrants do not write the follow-on work herding predicts."
   - Neighbours: Movva et al. 2024 (entrants are numerous); Huang 2026 (initiators).

**Placement.** F3 is core; F4, F11 and the novelty analysis are support; H2a is an explicit limit.

### §6 The Review Decision, in Foresight (700 words)

**Role.** Act 3. Ask what acceptance goes with once each in-sample pattern meets held-out papers. Two sub-acts: what
fades, and what holds.

**§6.1 Imitation's signals shrink or fail (330 words).**
1. **Topic edges are real but regress** [B].
   - Regressing the 2024-26 topic edge on the 2018-22 edge: within discovery b 0.38 [0.18, 0.58]; held-out
     **0.60 [0.32, 0.88]** (75 units). Empirical-Bayes-shrunk premia beat zero: D0 1.71 [0.42, 3.01] × 10⁻³
     (DC:376-377).
   - A single year's topic acceptance rate is about half noise at roughly 58 decided papers (DP:325).
   - Descriptive: the top tenth's edge went from +14.3 to +2.1 pp (DP:330).
   - Keyword units show no detectable persistence: b 0.16 [−0.34, 0.66], unregistered (DP:52-53).
   - Prior art: Wang et al. 2023; Xu et al. 2026.
   - Reading: "a favoured topic is not a reward that keeps paying in full". Outcome imitation of topic success would
     follow edges that partly regress (Haunschild and Miner 1997; Strang and Macy 2001).
2. **Crowding: no detectable premium** [C].
   - H3a: −1.68 [−3.68, +0.32] in discovery; −1.51 [−5.20, +2.19] held-out; MDE80 4.8, so uninformative (DC:324).
3. **The starkest fad case is not confirmed** [discovery D; held-out C].
   - Federated learning: −11.3 [−17.9, −4.8] (q 0.19) in discovery; −4.9 [−15.4, +5.7] held-out.
   - Its trend has the opposite sign held-out: +3.2 pp/yr (DC:368-369).
   - This is the cases channel, demonstrated.
4. **Branded titles** [E\* / D\*].
   - The share of titles opening with a short coined name and a colon rose roughly fourfold: 7-14% (2017) to 37-49%
     (2026), depending on the definition (DP:124-125).
   - Acceptance ratio 1.02 (DP:133). This is earlier exploratory work, not re-run; mark it so, or drop it (LS:937-938).
5. **Timing leans towards priority, weakly** [B weak].
   - Young rising against old flat keywords: +3.25 [−0.18, +6.69] held-out, one-sided p 0.031; the CI includes 0
     (DC:375).
   - Gap after a keyword's peak minus gap before it: −5.2 [−11.1, +0.7], p 0.043. Without the six keywords inspected
     first it is −1.7 (p 0.33) (DP:391-392).
   - Two expansions:
     - this direction fits priority (Merton 1957; Strevens 2003), not rewarded late imitation;
     - PH6's dependence on the keywords seen first is our own cases channel at work.
   - Note on terms: Jung et al. 2025's "earlier submission" is a different notion of time.
6. **Distance from the field: no replicated association either way** [C/D].
   - Least-novel fifth: −3.27 [−4.93, −1.60] in discovery; −0.13 [−3.50, +3.25] held-out. Not replicated (DC:371).
   - Within-author novelty slope: not supported (DC:373).
   - Most-novel fifth: +0.44 [−1.41, +2.28] (D; DP:261).
   - Consistent with Teplitskiy et al. 2022, but too weak to settle the novelty-penalty debate (LS:164).

**§6.2 What holds is the record (290 words).**
1. **Far jump from the team's own record** [B].
   - −5.44 [−7.10, −3.78] in discovery; **−6.09 [−9.32, −2.86]** held-out, one-sided p 0.0025 (DC:370).
   - Population: 2023-26 papers with at least one experienced author (DP:232).
   - Robustness:
     - with a newcomer control: −5.0;
     - link-removed text: −5.39;
     - early map: −5.2 (DP:238, 371).
   - Shape [D]: adjusted acceptance by closeness fifth, far to near, is 39.7 / 41.8 / 44.4 / 47.2 / 46.9% (DP:236).
     Leaving costs; the closest fifth adds nothing beyond the fourth. Any "near" number must carry the E2 rule
     (DP:40-41).
2. **Same author, closer paper** [B].
   - +0.55 per +0.1 cosine in discovery; **+1.06 [+0.23, +1.89]** held-out (DC:372).
   - Co-author composition may explain half or more (DP:243).
3. **One topic insider vs none** [B].
   - +3.42 [+1.18, +5.66] in discovery; **+3.88 [+0.28, +7.47]** held-out, at fixed team size and fixed number of
     experienced authors (DC:374; DP:285).
   - Decomposition [D]:
     - a keyword-based insider: +0.0;
     - familiarity without an earlier acceptance: +0.2 [−3.8, +4.2] on 767 papers (DP:289, 293).

     A proven record may matter more than topic knowledge.
4. **The newcomer gap is mostly who writes** [D].
   - Raw acceptance: 37.2% vs 47.3%.
   - Within topic and year: −10.2 [−11.8, −8.7]. Within the same authors: −3.1 [−4.5, −1.6]. The same author new to
     a topic: **−1.4 [−2.7, −0.0]** (DC:343; DP:178-179).
   - This mirrors the far jump at the level of the person. Wording: it "need not be reviewer bias" (DP:181-183).
5. **Differential survival** (the synthesis sentence, counting verdicts, not effect sizes).
   - Of the post hoc patterns we took to held-out papers:
     - all three record-referenced associations held (E1, E4, Teams H1);
     - neither field-novelty association did (P1b, P7);
     - the fad case did not (H4-FL level and trend).
   - Of the registered imitation predictions, none was supported: H2b and H2c reversed; H2a and H3a were
     inconclusive (DC:364-378).
   - Caveats:
     - the six PH5 secondary tests are one-sided and unadjusted, so "one false positive would not be surprising"
       (DP:29-30);
     - Holm within a module family only (DP:54-55).
6. **Prior.**
   - Hill et al. 2025: "we observe the decision itself".
   - Bao and Li 2025: the measure.
   - Sekara et al. 2018: the chaperone effect.
   - Biliotti et al. 2024: the producer-side analogue.
   - Ibrahim et al. 2026: the rival reading.

**§6.3 The package at the gate (80 words)** [D; not tested in foresight].
- FM papers are accepted more often: +4.62 [+2.79, +6.44] (DC:342).
- The premium does not detectably fade as adoption rises: +0.19 [−0.96, +1.34] per logit unit (DP:356). A fad
  premium should fade.
- New-architecture papers are not penalised against the tide: +8.3 [+1.3, +15.4] (DC:349).
- All three are discovery-only. The FM label is applied to partly camera-ready text (DP:362).

**Placement.**
- Core: F5, F6, F7, F9.
- Support: F8.
- Context: F10.

### §7 Discussion (350 words)

1. **Where the herd went.**
   - The field looks most herd-like in the evidence most exposed to hindsight, and growth amplifies it.
   - This is not "ML is not a herd":
     - flocking into hot topics is untested (C);
     - unrewarded bandwagons among producers remain possible (Abrahamson and Rosenkopf 1993);
     - the result is for one venue.
2. **What remains is conformity by continuity.**
   - What Weisberg (2013) models as herding, risk-avoiding clustering, appears here as continuity with one's own
     record, not imitation of the crowd (TA:374-375).
   - Two readings remain, and the data cannot separate them:
     - better-informed, better-made papers (expertise; Li 2017);
     - visible status, since authors are often identifiable through preprints and borderline ICLR decisions lean
       towards visible prestige (Ibrahim et al. 2026; Bharadhwaj et al. 2020).
   - Selection into teams is uncontrolled.
3. **A tension.**
   - In the previous shift, persistence went with lower later impact (Bao and Li 2025). The gate and the citation
     record need not reward the same thing; our data cannot test this.
4. **Why the route matters** (interpretation, not advice).
   - Imitation's collective cost is premature convergence (Zollman 2010).
   - Continuity's is competency traps (Levitt and March 1988; Rzhetsky et al. 2015).
5. **For writing a field's history.**
   - Fit the map early and test it late; report which claims survive (Hall et al. 2008; Small et al. 2014).
   - The check is cheap, and it changed our conclusions.

### §8 Conclusion (100 words)

- Restate the three points in one sentence each.
- End on "Hindsight sees a herd; foresight finds a record."

### Limitations (ARR section; not counted)

1. **One venue.** Incumbency counts ICLR submissions only (DC:56, 149).
2. **The held-out split is not independent.** It shares years, reviewer pools and authors with discovery (DC:45).
3. **Underpowered tests confirm direction only.** H1d, H2c′, Teams H1 and A1 were underpowered at the discovery
   effect (DC:380-381).
4. **Size failure:** 12.6% / 10.0% rejection under a cross-map null (DC:249-250).
5. **Labels.** Contribution and FM labels are LLM labels. The FM label is applied to partly camera-ready text, and
   held-out text has no link-removal check (DP:25).
6. **Author IDs.** The 2021 ID switch biases incumbency towards zero (DC:146).
7. **The hindsight bracket is not a point estimate.** The maps differ in corpus as well as window, and the forecast
   comparison has no paired test (DC:187, 229).
8. **Content distance:**
   - unregistered;
   - SPECTER2 distance, not originality;
   - incumbents' self-continuation lowers their distance;
   - ranked within k100 cells only;
   - not yet a committed output (NN; Section 9).
9. **Uninformative nulls:** H3a, H2a, FL and P1b.
10. **Mechanisms:**
    - selection into teams;
    - arXiv de-anonymisation;
    - whether the continuity association reflects expertise or status.
11. **Coverage.**
    - Withdrawn papers are left out of the acceptance tests (DC:318).
    - The far-jump and insider tests cover 2023-26 only, which overlaps the era of LLM-assisted reviewing
      (LS:375; MM:169-179).

### Appendix (relegated, with the reason for each)

| Item | Numbers (tier; source) | Why it goes to the appendix |
|---|---|---|
| Full held-out table, all registered and declared tests | DC:364-378 | Table 1 carries the story rows; the full table is the audit trail |
| Team-size gradient | +8.8 pp per doubling [+8.0, +9.7] (D; DC:395; DP:164) | A control in the insider test. It stands in for compute and seniority and does not separate the routes. |
| Acceptance by contribution class | Theory +8.9, dataset/benchmark +3.9, empirical −2.7 vs method (D; DC:351) | One clause in §5 at most: the gate does not favour the method type entrants bring. The detail is D. |
| Withdrawal after review rises with maturity | +1.62 pp per log unit (D; DC:344) | The gate also selects through withdrawal. Not a route test. |
| Concurrent-twin acceptance (P2) | Discovery +0.68; held-out +3.69 (unregistered); pooled +1.86 (D; DP:36-39) | Mixed and unregistered. It must carry the P2 rule. Cited in §8 of this file as a "riding pays" reading. |
| Near-closeness contrast (E2) | +1.75, Holm 0.148; held-out +2.34; pooled +2.10 (D; DP:40-41) | Only the shape sentence in §6.2 uses it, with the rule |
| Keyword winner's curse | Raw top-growth keywords top again 16.0% vs 20.6% (D/E; DP:334-338) | Unit-dependent: on topic maps the raw lift is not negative. One sentence at most, in the appendix. |
| Interactions with topic heat | Far jump −0.35; insider −0.8; newcomer × hot −0.4 / −0.6 (D null; DP:246, 291; DC:307) | Uninformative (TA:606) |
| PH1 subgroups and PH4 area spread | Gap negative in all 20 areas; ±10 pp spread (D; DP:150-154, 192-197) | Descriptive spread; no area survives Holm |
| Diversity by map; k-sensitivity; topic quality; label quality | DC:86-123, 189-192 | Measurement audit |
| Novelty by year, era, controls and definition | NN (all keys) | Robustness of §5.3 |
| Title side findings (first-author lag, LLM verbs) | E\*, not re-verified (DP:134-136) | Not re-verified; the evidence is weak |
| Lind-Mehlum inverted-U; the do-not-quote list | DP:56-61, 263 | Must not be quoted |

### Placement map: every major finding has a place

| Finding (LS:500-512) | Where | Role in the story | Fit |
|---|---|---|---|
| F1 Field waves and FM displacement (E; H1d A) | §1 ¶1, Figure 1; §4.5 | The hindsight picture; then what survives foresight at the field level | Core |
| F2 Hindsight measurement (E) | §4.1-4.4, Figure 2 | The categories channel, measured. Growth compounds it. | Core |
| F3 Newcomers: methods, not benchmarks (A, reversed) | §1 ¶3 hook; §5.1-5.2, Figure 3 | The registered herding forecast fails in foresight | Core |
| Novelty analysis (E, new) | §5.3 | Answers "type is not novelty". Entrants are where content farther from earlier work comes from. | Support |
| F4 First-time teams are not trend-chasers (E) | §5.4, Figure 3b | Entrants adopt trends slowly; the package travels with records | Support |
| F11 Twins as volume (E; P2 D) | §5.5; P2 in the appendix | A raw count read with hindsight (no normalisation) looks like piling on | Support |
| F5 Crowding and branding (C; D\*) | §6.1.2, §6.1.4 | No detectable premium for following | Support |
| F9 Topic edges shrink (B) | §6.1.1, Figure 4a | The estimates channel, demonstrated at the gate | Core |
| F6 Timing: A1, PH6 (B weak); FL (D/C) | §6.1.3, §6.1.5 | FL shows the cases channel. PH6 shows our own cases channel. Timing leans towards priority. | Support (weak); FL is the demonstration |
| F7 Continuity: far jump, closeness, insider (B) | §6.2.1-6.2.3, Figure 4b | What holds in foresight | Core |
| F8 Newcomer gap mostly composition (D) | §6.2.4 | The record at the person level (−1.4) | Support |
| F10 FM premium; against the tide (D) | §6.3 | The package premium does not fade, unlike a fad. Not tested in foresight. | Context |
| P1a/P1b/P7 field novelty (D/C) | §6.1.6 | Field-referenced distance does not replicate. It is the foil to the record. | Support |
| H1a-c lifecycle (C) | §4.4 | The conclusion flips with the map | Support |
| H2a flocking (C) | §5.6 | An explicit limit | Limit |

---

## 6. Main-text table: Table 1, "The foresight test"

**Design.**
- One full-width table (`table*`), in three panels by point and a fourth for patterns never tested in foresight.
- Each row is a *signature* of a route:
  - I = imitation;
  - C = continuity;
  - P = package;
  - T = timing (priority);
  - N = distance from the field.
- Columns:
  1. Signature (route)
  2. **In hindsight**: the all-years map, the in-sample estimate, or the received prediction
  3. **In foresight**: the 2017-2020 map, the registered test, or held-out papers
  4. **Fate**
  5. Tier

**Fate vocabulary:**

| Mark | Meaning |
|---|---|
| ✓ | Holds |
| ✓w | Holds, weak |
| ↓ | Shrinks |
| ∅ | Vanishes |
| ⇄ | Reverses or flips |
| ✗ | Not confirmed / not replicated |
| ? | Inconclusive or uninformative |

The story is visible if the I rows carry ↓ ∅ ⇄ ✗ ? and the C and P rows carry ✓.

**Caption.** "Each row is a signature that the herding account (I) or a rival (C, P, T, N) predicts.
- *In hindsight:* the all-years map, the discovery or in-sample estimate, or our registered prediction.
- *In foresight:* the 2017-2020 map, the held-out estimate or a later period.
- Units: pp of probability unless noted; 95% intervals. All rows are associations within topic and year.
- Held-out tests are one-sided pre-registered out-of-sample replications, not a certified untouched holdout. A
  supported test can therefore have an interval that includes 0, and it supports direction, not size.
- Tiers as in §3."

Units and sources are in the last column (design file only; the paper drops it).

| # | Signature (route) | In hindsight | In foresight | Fate | Tier | Source |
|---|---|---|---|---|---|---|
| **A** | **The waves** | | | | | |
| A1 | Many topics emerge (I) | All-years map: 29 emerging, 13 declining. 2024-26 map: 28 emerging. | 2017-20 map: 8 emerging. Year-balanced map: 16 emerging, 26 declining. | ↓ (bracket 8-29) | E | DC:176-181, 187 |
| A2 | Topic growth is predictable from size (I, momentum) | R² 0.28 [0.22, 0.34] | R² −0.03 [−0.08, −0.00] | ∅ | E | DC:217 |
| A3 | Topics age from method to measurement papers (pp per log unit) | Null: −0.14 [−1.78, +1.49] / +0.50 [−0.76, +1.75] | 2021-26 papers on the 2017-20 map: −3.48 [−6.21, −0.76] / +3.96 [+1.35, +6.57] (exploratory) | ⇄ (flips with the map) | E (variants of C) | DC:201-202 |
| A4 | Duplicated work piles up (I) | Papers with a same-year twin: 19.5% → 48.8% (2019 → 2026) | Twins per paper per 1,000 submissions: 0.32 → 0.19 | ↓ (volume, not per pair) | E | DP:78-79 |
| A5 | FM adoption goes with fewer new-architecture papers, 0 → 100% (P) | −7.98 [−12.14, −3.82] | −11.0 [−18.1, −3.9]; 9/9 variants; both hindsight maps pass | ✓ | A | DC:271, 364 |
| **B** | **The entrants** | | | | | |
| B1 | Entrants write follow-on benchmark, dataset or evaluation papers (I; registered H2c) | Registered: more | −1.70 [−2.46, −0.93] → held-out −2.10 [−3.35, −0.85] | ⇄ | A (reversed) | DC:297, 366 |
| B2 | Entrants write fewer method papers (I; registered H2b) | Registered: fewer | +3.71 [+2.61, +4.80] → held-out +3.60 [+1.48, +5.71] | ⇄ | A (reversed) | DC:296, 365 |
| B3 | Entrants' content stays close to earlier work (I) | — | +5.90 percentile points [4.95, 6.85] farther; method papers only +5.24 [4.16, 6.31] | ⇄ (farther) | E (unregistered) | NN:main_pct, method_only_pct |
| B4 | First-time teams adopt trends fast (I) | — | Emerging keywords −3.7 pp (16.7% vs 25.0%). FM papers −4.6 / −9.0 / −14.7 pp at 5-15 / 15-30 / 30-50% adoption. | ⇄ (slower) | E | DP:315-316, 360-362 |
| B5 | Entrants duplicate others (I) | — | Newcomer papers less often twinned: −3.9 [−5.0, −2.7] | ⇄ (less) | E | DP:275 |
| B6 | Entrants flock to hot topics (I; registered H2a) | — | −0.73 [−2.68, +1.22]; hindsight variant fails | ? (untested) | C | DC:295 |
| **C** | **The review decision** | | | | | |
| C1 | Crowded topics favoured (I; registered H3a; pp per log unit) | −1.68 [−3.68, +0.32] | −1.51 [−5.20, +2.19]; MDE80 4.8 | ? (no detectable premium) | C | DC:324, 367 |
| C2 | Favoured topics stay favoured (I, outcome imitation) | Top tenth of topics +14.3 pp in-sample | Later-period slope b 0.60 [0.32, 0.88] (discovery 0.38 [0.18, 0.58]); top tenth +2.1 | ↓ | B (top tenth descriptive) | DC:376; DP:330 |
| C3 | The starkest fad case, federated learning (I) | −11.3 [−17.9, −4.8], q 0.19 | −4.9 [−15.4, +5.7]; trend +3.2 pp/yr (opposite sign) | ✗ | D → C | DC:368-369 |
| C4 | Branded "NAME:" titles pay (I) | Share ~4× (7-14% → 37-49%, 2017 → 2026) | Acceptance ratio 1.02 (earlier exploratory) | ? (no premium) | E\* / D\* | DP:106-133 |
| C5 | Late riders do as well as early ones (T); gap after the peak minus before | −5.7 [−8.5, −2.9] (not a test) | −5.2 [−11.1, +0.7], p 0.043; −1.7 (p 0.33) without the 6 keywords seen first | ✓w (leans on cases seen first) | B (weak) | DP:391-394 |
| C6 | Early arrival: young rising minus old flat keywords (T) | +2.67 [+0.76, +4.58] | +3.25 [−0.18, +6.69], p 0.031 | ✓w (CI includes 0) | B (weak) | DC:375 |
| C7 | Least-novel fifth penalised (N) | −3.27 [−4.93, −1.60] | −0.13 [−3.50, +3.25] | ✗ | C | DC:371 |
| C8 | Same author, more novel paper (N; per 10 percentile points) | +0.39 [+0.09, +0.69], Holm 0.105 | +0.34 [−0.47, +1.16] | ✗ | C | DC:373 |
| C9 | Far jump from the team's own record (C; p10 vs p50) | −5.44 [−7.10, −3.78] | −6.09 [−9.32, −2.86] | ✓ | B | DC:370 |
| C10 | Same author, closer paper (C; per +0.1 cosine) | +0.55 [+0.21, +0.90] | +1.06 [+0.23, +1.89] | ✓ | B | DC:372 |
| C11 | One topic insider vs none (C) | +3.42 [+1.18, +5.66] | +3.88 [+0.28, +7.47] | ✓ | B | DC:374 |
| **D** | **Not tested in foresight (discovery only)** | | | | | |
| D1 | Newcomer gap is about who writes (C) | Raw 37.2% vs 47.3%; within topic-year −10.2 [−11.8, −8.7] | Within the same authors −3.1 [−4.5, −1.6]; same author new to the topic −1.4 [−2.7, −0.0] | — (mostly composition) | D | DC:343, 394; DP:178-179 |
| D2 | A fad premium fades as adoption rises (I vs P) | FM papers +4.62 [+2.79, +6.44] | Slope +0.19 [−0.96, +1.34] per logit unit of adoption | — (no detectable fade) | D | DC:342; DP:356 |

**If space forces a cut:**
- Move A3, B5, C8 and D2 to the appendix version of the table.
- Keep A1, A5, B1-B4, C1-C3, C5-C7 and C9-C11. They carry the visible pattern.

**Footnotes:**
- B3 is outcome-free and was added during writing; it is not a registered test.
- C4 is an earlier exploratory analysis, not re-run.
- D1 must say the residual "need not be reviewer bias".

---

## 7. Figure plan (four figures; Figure 1 exists)

All sources are committed files under `research/fashion/` or `research/topics/`, except the optional novelty panel.

### Figure 1: "The hindsight picture" (exists)

- **File:** `research/fashion/paper/figs/fig1_waves.pdf`.
- **Data:** keyword shares, `output_pooled/posthoc/ph5_waves/wave_table.csv` (pooled corpus; DP:80).
- **Message:** read backwards, ML moves in waves. GANs peak at 8.1% (2018) and fade; LLMs reach 16.7% (2026); graph
  neural networks, federated learning and self-supervised learning rise and fall.
- **Caption change:** say the reflexive point outright. "These keywords were chosen for display after their curves
  were known, as waves usually are. Sections 4-6 ask what survives when the categories, cases and estimates are fixed
  in advance." This turns the existing figure into the setup of the thesis.

### Figure 2: "Hindsight in categories" (§4)

Three small panels in one `figure*`.
- **(a) Emerging topics by fitting window.** Bars for the 2017-20 map (8), year-balanced (16), all-years (29) and
  2024-26 (28), with declining counts as a second marker (17, 26, 13, 6).
  - Source: `research/topics/output/hindsight_check.json` (keys `maps`, `ratio_rule`).
  - A rendering exists: `presentation/figs/hindsight_emerging.png`.
- **(b) Growth looks predictable only in hindsight.** Probability of top-fifth two-year growth by size tercile,
  hindsight map (40 / 21 / 2%) against early map (22 / 20 / 20%), annotated with R² 0.28 vs −0.03.
  - Source: `output/ph5_forecast/b4_conditional.csv`, `output/ph5_forecast/summary.json`.
- **(c) A conclusion flips.** H1a/H1b coefficients with CIs on the all-years map against the early map on 2021-26
  papers.
  - Source: `output/rq1_results.csv`.
  - A rendering exists: `presentation/figs/lifecycle_flip.png`.
- **Message:** how many waves a field shows, how predictable they look, and which trend conclusion holds all depend
  on when the map was fitted.
- **Tier:** E; caption states the corpus caveat.

### Figure 3: "The entrants, in foresight" (§5)

- **(a) The registered prediction and what happened.** For method share and for measurement share:
  - an arrow for the registered herding direction;
  - the discovery and held-out newcomer-minus-incumbent estimates with 95% CIs;
  - the two hindsight-variant points.
  - Sources: `output/frozen_run/rq2_results.csv` (main and variants) and `output_pooled/confirmation_run/rq2_rows.csv`
    (held-out).
- **(b) First-time teams adopt the package slowly.** The FM-paper gap of first-time teams against returning teams new
  to the topic, by prior-adoption bin (−1.0, −4.6, −9.0, −14.7, −2.0 pp), with CIs.
  - Source: `output/posthoc/ph5_fmwave/free_entry.csv`.
  - Annotate the keyword result (−3.7 pp, Emerging) from `output/posthoc/ph5_kwtiming/free_profile_states.csv`.
- **(c) Optional: content distance by year,** newcomer minus incumbent percentile, 2019-2026.
  - **Not committed.** Source: `paper_ws/output/novelty_newcomer.csv` (rows `year_*`). Include only after committing
    the script and output to the repository (Section 9). Otherwise state +5.90 [4.95, 6.85] in the text.
- **Message:** the herding prediction reversed; entrants propose and lag the trend.
- **Tiers:** A (a), E (b, c).

### Figure 4: "The gate, in foresight: the crowd's edge regresses, the record holds" (§6)

Two panels.
- **(a) Topic edges regress.** Each early-map topic's 2024-26 held-out acceptance edge against its 2018-22 discovery
  edge, with a fitted slope b 0.60 [0.32, 0.88] and the y = x line.
  - Sources: `output_pooled/confirmation_run/ph5/premia_units.csv` (columns `unit, w1, v1, eb1, unit_type, w2, v2,
    papers_w2, used`) and `output/posthoc/ph5_premia/`.
  - A rendering exists: `presentation/figs/premia_scatter.png`.
  - Tier B.
- **(b) The record holds.** Adjusted acceptance by fifth of closeness to the team's own record (39.7 / 41.8 / 44.4 /
  47.2 / 46.9%; D, discovery), annotated with the held-out far-jump contrast −6.09 [−9.32, −2.86] (B).
  - Sources: `output/posthoc/ph5_pivot/quintiles.csv` and `output_pooled/confirmation_run/ph5/tests.csv` (row E1).
  - A rendering exists: `presentation/figs/far_jump.png`.
- **Message:** a topic's in-sample edge only partly carries forward; distance from one's own record goes with
  acceptance in foresight too.
- **Caption must label tiers per panel.** The adjusted shares are discovery-only (D).

**Not chosen: a "survival plot".** A forest of all discovery against held-out estimates on one axis was considered
and dropped. It would invite cross-module effect-size comparisons (DC:428), and Table 1 already shows survival
row by row.

---

## 8. The weakest points, and how the text handles them

| # | Weak point | Honest handling in the text |
|---|---|---|
| 1 | **"Hindsight" could read as a rhetorical umbrella.** Map windows, case selection and in-sample estimates are different things. | Define each channel operationally with its foresight counterpart (§1 definitions; §3 paragraph). Use "hindsight" only for those three, plus post-decision text. Admit the tools are standard (Leydesdorff 2002; Kaufman et al. 2012; Gelman and Loken 2014). What is new is applying them jointly to a field's fashion account and showing that the *substantive* conclusion changes. |
| 2 | **The headline measurement result is tier E and confounded.** The early map cannot see topics born after 2020, so 29 vs 8 brackets the truth; the forecast comparison has no paired test. | Use "inflates", never "manufactures", and always give the bracket (8-29; 22-41% of 2024-26 papers). State DC:187 and DC:229 in the text, not only in the Limitations. The abstract carries 29 vs 8 as "on the same papers"; the body adds the caveat in the same paragraph. |
| 3 | **Asymmetry of evidence.** The continuity associations were found post hoc (B); the imitation predictions were registered (A/C). A sceptic will say continuity "survived" because we picked it after looking. | The held-out test is the same foresight test for both. Say plainly that the continuity tests were formed in discovery: six secondary tests, one-sided and unadjusted, "one false positive would not be surprising" (DP:29-30); Holm within family only, so the insider result is about 0.17 across modules (DP:54-55). Also report the post hoc patterns that *failed* in foresight (P1b, P7, FL). The B rows are not cherry-picked survivors. |
| 4 | **Imitation's nulls are uninformative, not absences.** H3a has MDE80 4.8, H2a is inconclusive, FL has MDE80 14.5. | Wording: "no detectable premium", "not confirmed", "uninformative". Flocking is named as untested inside §5, not only in the Limitations. Abrahamson and Rosenkopf: no premium does not rule out unrewarded bandwagons. The title is a phenomenon, not "No Herd". |
| 5 | **A method paper is a type, not novelty; the content-distance measure is new and unregistered.** | The novelty analysis is offered as the answer to the type objection, at tier E. It carries five caveats: unregistered; descriptive; SPECTER2 distance is not originality (vocabulary from other fields); incumbents' self-continuation lowers their distance; ranked in k100 cells only. Never "entrants are more innovative". |
| 6 | **The mechanism behind continuity is unknown.** Expertise, visible status, or selection into teams. | §7 gives both readings with citations (Li 2017; Ibrahim et al. 2026). Double-blind review does not settle it (arXiv). No causal or advice language. The insider decomposition (D) hints that a proven record matters; say so. |
| 7 | **"Foresight" may be over-read as independent future data.** | Every held-out mention says "a pre-registered out-of-sample replication, not a certified untouched holdout" and "direction, not size". The early map is a construction from dated data, not a contemporaneous forecast. One venue (DC:56). |
| 8 | **Size failure for the entrant test** (12.6% / 10.0%). | Reported in §3 with the stress factors. t = 6.7 and −4.4 are large relative to the 1.31 and 1.22 inflation (DC:311-312). Family-wise false support is 6.4% under the cross-map null (DC:252). |
| 9 | **Prior art narrows several "new" elements.** Hill 2025 (publication pivot penalty), Bao and Li 2025 (closeness measure; a contrary impact result), Wang 2023 and Xu 2026 (topic edges), Ibrahim 2026 (pre-registered ICLR test), Stelmakh 2023 (reviewer herding). | Use the exact Section 2.4 wording and the phrases-to-avoid list. Bao and Li's contrary result goes in §7 as a tension. Novelty sits in the *combination* and the *foresight test of the herding account*, always "to our knowledge, among the works we checked". |
| 10 | **Some results can be read as "riding pays."** The FM premium (+4.62, D), the held-out twin row (+3.69, unregistered) and early arrival (A1). | A1 rewards *early*, not following; it is priority, weak. The FM premium is D, never tested in foresight, and does not fade with adoption, which is the opposite of a fad signature (§6.3). The twin row is unregistered and must carry the P2 rule; appendix only. |
| 11 | **Some evidence is post-decision text and some falls in the LLM-review era.** The FM label and held-out abstracts are partly camera-ready; far-jump and insider tests cover 2023-26. | The fourth hindsight channel (post-decision text) is named in §3, together with the discovery link-removal check (far jump −5.39; DP:371). The Limitations name the 2023-26 window and LLM-assisted reviewing (LS:375). |
| 12 | **Risk that the paper reads as a methods note.** This was Candidate 4's failure mode (LS:672-681). | The substantive answer (continuity, entrants propose) is in the title alternatives, the thesis, the last line of the abstract and the two largest sections (§5, §6). The hindsight lens organises; it does not replace the substance. |
| 13 | **The 2021 author-ID switch and ICLR-only incumbency.** | Both bias the newcomer contrasts towards zero (DC:146-147). The R2 variant without 2021-22 gives the same results (DC:148). Also: without 2021 the novelty gap is +5.87 (NN:excl_2021_pct). |

---

## 9. Open items before writing

1. **Commit the novelty analysis.** Commit the script and output (`paper_ws/scripts/novelty_newcomer.py`, `output/
   novelty_newcomer.{json,csv}`) to the repository, so that §5.3 and the optional Figure 3c rest on a committed
   source. Until then, cite it in the text only.
2. **Foresight-categories check for the novelty gap** (recommended; outcome-free).
   - Re-run the newcomer content-distance contrast with 2017-2020-map topic×year cells and newcomer flags. The current
     run uses k100 cells only.
   - The registered entrant tests passed both hindsight variants (DC:296-297). The novelty result should be held to
     the same standard before it appears in Table 1.
3. **Confirm that F_max uses SPECTER2.**
   - story_P1.md reports PREREGISTRATION.md line 1372: "centred SPECTER2 … L2-normalised". I did not read that line
     myself; confirm before writing "as Bao and Li (2025)".
4. **Read the originals of the theory anchors cited for specific claims.**
   - Marked CONTENT-SECONDARY: Strevens 2003, Kitcher 1990, DiMaggio and Powell 1983 (mimetic section), Scharfstein
     and Stein 1990, Levitt and March 1988 ("competency trap"), Zollman 2010 (TA:665-676).
   - Strang and Macy 2001 content is from abstract-level and secondary descriptions (FW:43); cite it for its general
     mechanism only.
5. **Bibliographic statuses to carry into the .bib:**
   - Jung et al. 2025: arXiv author order; EMNLP order unresolved.
   - Xu et al. 2026: middle authors unresolved; use "and others".
   - Wang et al. 2023: issue omitted.
   - Klavans and Boyack 2014: no DOI.
   - Bailey et al. 2017: no pages.
   - Hooker 2021: no page range.
   - Gelman and Loken 2014: no issue.
   - Do not cite "Who Pays for Open Review?" (authors unverified; VP:62).
6. **Decide the branded-title row (C4).** Keep it with D\* and "earlier exploratory, not re-run", or drop it from
   Table 1 (LS:937-938). Its outcome-free share (E\*) can stay in §1 either way.
7. **Quoting rules to wire into the draft:** P2, E2, P1b, FL, A1, PH6, and the do-not-quote list (DP:35-61).
