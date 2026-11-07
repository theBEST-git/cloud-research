# Judge J2: a science-of-science reading of story proposals P1-P4

Written 2026-11-03 from the point of view of a sociology- and science-of-science reviewer. The question this judge asks
of each proposal is whether the paper adds a new idea to theory about **how science changes and what it rewards**,
and whether the evidence carries that idea at the tier the text claims.

## 0. What was read and what was checked

**Read in full:**
- story_P1.md, story_P2.md, story_P3.md, story_P4.md;
- dossier_core.md and dossier_posthoc.md;
- verify_prior.md and theory_anchors.md;
- `output/novelty_newcomer.json` (the results and descriptives blocks) and `scripts/novelty_newcomer.py` (the novelty
  definition and the estimator).

**Read in part:**
- landscape.md: the bottom line, gaps, candidate comparison and recommendation;
- lit_novelty_reward.md / .bib and lit_outsiders.bib, to check which canonical works are verified.

**Checked here against committed, outcome-free sources:**

| Claim in a proposal | Source checked | Result |
|---|---|---|
| F_max is built on centred SPECTER2 (P1, P4) | `PREREGISTRATION.md` lines 1372 and 1377-1380 | **Confirmed.** Wording fix: prior_cos is the cosine with the normalised **mean** of an author's prior set, and F_max is its maximum over experienced authors. It is not the cosine with "the closest earlier submission". P2's statement that this is "still unconfirmed" is out of date. |
| First-time FM gap is estimated with class, team-size and topic × year controls (P1) | PRE lines 1111-1112 | Confirmed. first_time is nested in newcomer. |
| P2's **[read here]** values | `output/posthoc/ph5_fmwave/free_entry.csv`; `output/posthoc/ph5_position/free_herding.csv` | **All exact.** Topic newcomer (returning, with an ICLR record) vs incumbent, FM paper, by adoption bin: +1.10 (p 0.060), −0.41 (0.73), −2.58 (0.11), +2.87 (0.31), −1.01 (0.097). The 30-50% bin's CI is [−2.74, +8.48], so that bin is a wide, uninformative null. First-time share 26.3%. FM-twin row +11.0 [+8.0, +13.9]. |
| A1 states are prospective; the PH6 wave set is retrospective (P4) | PRE lines 1258-1261; DP:81 | Confirmed. The PH6 wave set needs the full series ("at most half the peak … in 2026"). |
| Content-distance numbers (all four) | novelty_newcomer.json | All quoted values match. The descriptives give a within-cell SD of 0.0618 and mean nov of 0.47 (2019) falling to 0.37 (2026). |

**Not touched:**
- no outcome or decision column;
- none of posthoc.py, run_frozen.py, run_confirmation.py or outcomes.py;
- no corpus author is named;
- nothing in the repository was written.

---

## 1. Verdict

**Ranking: P1 > P4 > P2 > P3. Winner: P1, "Anchored, not herded", with grafts from P4, P2 and P3 and three repairs
(Section 5).**

**Why P1 wins.** P1 is the only proposal whose story line is itself a claim about how science changes and what it
rewards. The claim: in a fast-moving field, the conformity we can detect refers to a **record**, not to the **crowd**.
- Entrants carry the divergent work.
- The gate's associations that replicate run from a team's own record, not from popularity.

The two routes have old roots (Levitt and March 1988; Weisberg and Muldoon 2009). What is new, to our knowledge, is
testing them against each other at entry and at the review decision. P1 also places every finding as an expansion,
using a route × site table (§7.1) that a reader can carry to other fields.

**Why the others lose.**
- **P4** is P1's substance in ACL dress. Its "reading forward" spine fits Acts 1 and 3, but it strains in Act 2: a
  registered prediction is not hindsight. Its Discussion contains one sentence that overclaims.
- **P2** has the cleanest evidence, but it gives the least to theory.
  - Its "package, not herd" opposition is conceptually unstable, because Fujimura's package is a *bandwagon*.
  - Its tier-A pillar (H1d) does not discriminate between the accounts, as P2 itself concedes.
  - "Converged in its tools, not in its people" overstates: entrants with an ICLR record take up the package at the
    incumbents' rate (FE rows above).
- **P3** has the most original idea: herd attributions as products of hindsight. But its central inference tallies
  heterogeneous tests whose survival tracks statistical power, and it counts nulls that were already null in
  discovery as "fading in foresight". Its evidence does not carry its thesis.

---

## 2. Scores (1-10)

| Criterion | P1 Anchored, not herded | P2 A package, not a herd | P3 Herds in hindsight | P4 The herd in hindsight (ACL) |
|---|---|---|---|---|
| Meaningful (matters beyond ICLR) | **8** | 7 | **8** | 7 |
| Novel (vs verified prior work) | 7 | 5 | **8** | 6 |
| Contributive (reusable idea or method) | 7 | 6 | 7 | **8** |
| Evidence fit (load-bearing on A/B/E, not D or weak B) | 6 | **7** | 4 | 6 |
| Honesty (no overclaiming, causal wording, advice) | **8** | 7 | 6 | 7 |
| Coherence (one story; findings as expansions) | **9** | 7 | 6 | 7 |
| Fit to a 3,000-4,000-word ACL long paper | 7 | 7 | 6 | **8** |
| **Total (of 70)** | **52** | 46 | 45 | 49 |

### Notes behind the scores

**Meaningful.**
- P1 and P3 speak to how any field's conformity and fashions should be diagnosed.
- P2 speaks mainly to ML's own homogenisation debate.
- P4 speaks mainly to the ACL "history of the field" genre.

**Novel.**
- **P1.**
  - The distinction is old: Levitt and March 1988 already separate learning from one's own experience from learning
    from others'.
  - The adjudication at entry and at the gate is new among the works checked (TA:79-82).
  - The pivot-at-publication result (Hill et al. 2025) and the closeness measure (Bao and Li 2025) are not new, and
    P1 says so.
- **P2.** Homogenisation of the substrate is Bommasani et al.'s own thesis. G5 survives, but it is a test, not an idea.
- **P3.** The three hindsight channels applied jointly to a fashion account are, to our knowledge, new. The channels
  themselves are standard (P3's W1).
- **P4.** Forward reading is temporal leakage (Kaufman et al. 2012) carried over to field histories. It is useful but
  derivative.

**Contributive.** P4's info-code column (P prospective, H hindsight-variant pass/fail, R retrospective by
construction, T post-decision text) is the most reusable device in the four files.

**Evidence fit.**
- **P1.** The negative half rests on A and C. The positive half rests on B, with E1 the primary test: held-out Holm
  0.005, MDE80 4.9 (DP:233-235). Two load-bearing pieces are weaker than the text admits:
  - the "field versus own record" contrast leans on an underpowered null (P1b power 0.47; DC:371);
  - the content-distance clause in the abstract is tier E and partly mechanical (Section 4.2).
- **P2.** Rests on A and E. But the A result does not discriminate, and the "people" layer is mostly E.
- **P3.** The thesis rests on:
  - a confounded E bracket;
  - one fad case that is D in discovery and uninformative held-out (MDE80 14.5; DC:368);
  - a survival tally that is blind to power.
- **P4.** The same as P1, plus §7.3 (below).

**Honesty.**
- **P3.** Its abstract says "foundation models displacing new architectures", a causal verb with FM as subject (P2's
  own guardrail bans it). It states "growth amplifies hindsight" as a general claim from one corpus.
- **P4.** §7.3 says "every herd signal in this paper was larger than its forward reading". That is selective:
  - the B associations all got *larger* held-out (−5.44 → −6.09; +3.42 → +3.88; +2.67 → +3.25; premia b 0.38 →
    0.60; DC:370-376);
  - it counts P1b, which is not a herd signal;
  - it reads held-out sizes as sizes, against DC:47 and DC:428.
- **P2.** "Not in its people" overstates. It also writes "the first topic-level test", which needs care even with the
  qualifier.
- **P1.** Its only slip is "Imitation fails where theory expects it most" in the abstract. Make it "the imitation
  prediction fails …".

**Fit.** All four budget about 3,800 words, but each adds a full-width table of 19-24 rows and four figures. That is
tight for an ARR long paper (eight content pages in recent ARR calls; confirm against the current call). Section 5.4
says what to cut.

---

## 3. Proposal-by-proposal

### P1 "Anchored, not herded" (winner)

**The new idea.** Where does a fast field's conformity live? P1 answers: in reference to a record, not to the crowd.
It derives opposed predictions for:
- entrants: imitation says entrants imitate most (DiMaggio and Powell 1983; Bikhchandani et al. 1992); continuity
  says they absorb slowly and bring their own work (Cohen and Levinthal 1990; Bourdieu 1975);
- the gate: rewarded imitation (Scharfstein and Stein 1990) against consecration of continuity (Bourdieu 1975).

The data side with continuity at both sites:
- at entry: A (reversed) plus E;
- at the gate: B for continuity, C/D\* for imitation.

**The most original single move.** In §6.2, field distance and own-record distance are measured in one embedding
(both centred SPECTER2; PRE:1372, DP:255), and only the own-record association replicates. A science-of-science
reader will see this as locating conservatism **biographically** (relative to the team's own record) rather than
**substantively** (relative to the field). That also reconciles three findings:
- Teplitskiy et al. 2022: no content-novelty penalty at journals (lit_novelty_reward.md C4);
- Foster et al. 2015: field-referenced tradition among producers;
- Hill et al. 2025: the pivot penalty.

As written, though, it overreads a power asymmetry (Section 6, objection 3).

**Factual checks.**
- Every number traced matches DC/DP/NN.
- One wording fix: F_max is the cosine with the mean of an author's prior set, maximised over experienced authors
  (PRE:1377-1380).

**Weak spots** (Section 4 and Section 6):
- the Matthew-effect rival is not engaged;
- the self-continuation confound in the content test;
- the method label includes adapters on an LLM (DC:283-284);
- canonical producer-side work is missing: Zeng et al. 2021; Packalen and Bhattacharya 2019; Hofstra et al. 2020.

### P4 "The Herd in Hindsight" (ACL framing) — second

**Strengths.**
- It has the most careful source work of the four:
  - it confirms the SPECTER2 pointer;
  - it flags PH6 as retrospective by construction;
  - its abstract says "tested them again", not "replicated", because H3a was not replicated;
  - it states "all findings are associations at one venue".
- It gives an SAC question-and-answer table, an ethics statement and the P/H/R/T info codes.
- It positions the paper in ACL's measurement conversation (Kaufman et al. 2012; Kapoor and Narayanan 2023;
  Lazaridou et al. 2021), all verified in lit_methods_measurement.bib.

**Weaknesses.**
1. **The spine bends in Act 2.** "The herd story read backwards" is our own *registered* prediction. A registered
   prediction is foresight, not hindsight, so the reversal is not a backward/forward contrast. The spine organises
   Acts 1 and 3 only.
2. **The thesis sentence has three clauses** (package, entrants, gate), and the memorable line ("Hindsight tells the
   herd story; foresight tells a different one") does not name what foresight tells.
3. **§7.3 overclaims** (Section 2, Honesty).

Its theory content is P1's, so it cannot beat P1 on contribution to theory. It beats P1 on ACL fit and reusable
method.

### P2 "A Package, Not a Herd" — third

**Strengths.**
- The best evidence discipline: the thesis would survive a reviewer who discounts every post hoc result (P2 §2.6).
- The **[read here]** values are exact (Section 0).
- A genuinely useful producer-side finding: **the package travels with an ICLR record**.
  - First-time teams write FM papers 4.6 / 9.0 / 14.7 pp less often in topics at 5-15 / 15-30 / 30-50% adoption
    (DP:360-362).
  - Returning topic newcomers do not differ detectably from incumbents (FE).
  - This is the absorptive-capacity pattern, and it qualifies the "package invites newcomers" reading of Fujimura.

**Weaknesses.**
1. **The opposition is unstable.** A Fujimura package is a bandwagon, and Arthur's lock-in includes expectations about
   others (TA:206-207). "Package, not herd" therefore sets one form of collective convergence against another.
   - H1d does not discriminate between them (P2 §2.6 point 3; TA:600).
   - So the "package" half is a location, not a finding against herding.
2. **The story is about ML, not about science.** "Homogenised in the substrate" restates Bommasani et al. at the
   topic level.
3. **"Not in its people" overstates.**
   - Record-holding entrants adopt at incumbent rates (FE).
   - Flocking is untested (DC:295).
   - The content-distance "pillar" carries the confound in Section 4.2. P2 promotes exactly that result to a pillar.
4. **Out of date and weakly tiered in places.**
   - It says the F_max embedding is unconfirmed; it is confirmed.
   - It treats the D-tier FM premium as package evidence (row G4).
   - It cites a power figure from the shortlist that no dossier carries (§6.2).

### P3 "Herds in Hindsight" — fourth

**Strength.** The most ambitious and most theory-novel idea: fashion attributions are partly produced by retrospective
evidence. The three channels (categories, cases, estimates) are well chosen and well cited:
- Leydesdorff 2002; Rotolo et al. 2015;
- Strang and Macy 2001;
- Fischhoff 1975; Kerr 1998.

If the evidence carried it, this would be the most citable paper of the four.

**Why it ranks last.**
1. **"Differential survival" is a power tally, not a hindsight effect.**
   - The survivors include E1, with power 0.89 (DP:234).
   - The "failures" include P1b (power 0.47), FL (MDE80 14.5) and H3a (MDE80 4.8). These are underpowered nulls, and
     the task constraints call such nulls uninformative.
   - Several imitation "signatures" were never present in discovery, so they cannot have "faded in foresight":
     - H3a: Holm 0.20 in discovery (DC:324);
     - P7: Holm 0.105 (DC:373).
   - The tally also omits the post hoc patterns that held: A1, PH6, premia b and EB D0 (DC:375-378).
2. **The entrant act is not a hindsight test.** The reversal of a registered prediction is a failed forecast, not an
   artefact of retrospective reading.
3. **The categories channel is tier E and confounded.**
   - The maps differ in fitting corpus (DC:229).
   - The early map cannot represent post-2020 topics (DC:228).
   - "Growth compounds hindsight" generalises from one growth path.
4. **Wording.**
   - "Foundation models displacing new architectures" (abstract).
   - "Top tenth +14.3 → +2.1" in Table 1, which DP:330 says not to headline.
   - "Hindsight sees a herd" needs someone who saw the herd in hindsight. The only hindsight analysis shown is our own
     all-years map.

---

## 4. Problems none of the four solves (the winner must)

### 4.1 The Matthew effect is the obvious rival to "continuity", and no proposal names it

**The rival.** A science-of-science reviewer will read "acceptance goes with a team's record and a topic insider" as
cumulative advantage (Merton 1968, `merton1968matthew`, verified in lit_outsiders.bib) or as Bourdieu's scientific
capital, not as a new route to conformity.

**The rival has support in the data.**
- Per head, a topic insider is worth about as much as an experienced author from another topic: +0.58, p 0.16 (D;
  DP:294-296).
- A keyword-defined insider shows nothing: +0.0 (DP:289).
- Borderline ICLR decisions lean towards visible prestige (Ibrahim et al. 2026).

**What separates continuity from status is not the insider result.** It is two tests that hold "having a record" fixed:
- **E1**: the population is papers with at least one experienced author (DP:232). The association survives a newcomer
  control (−5.0; DP:238). Its F_max distance is a content position relative to the record, not the existence of a
  record.
- **E4**: within the same author, a closer paper goes with higher acceptance: +1.06 [+0.23, +1.89] held-out (B;
  DC:372). Author fixed effects hold status constant. The caveat: co-author composition may explain half or more
  (DP:243).

The paper must:
- say this explicitly;
- lead the continuity claim with E1 and E4;
- present the insider association as the result that a status reading explains equally well.

### 4.2 The content-distance result is partly built in by the definition of incumbency

**How the confound arises.**
- Incumbency means some author has an earlier ICLR submission **in the same k100 topic** (DC:144).
- The novelty reference set is every earlier-year paper. Only the paper's own chain of probable earlier versions is
  removed (`novelty_newcomer.py`, docstring).
- So an incumbent paper's own team's earlier same-topic papers are eligible to be among its ten nearest neighbours. A
  newcomer paper has no such papers by definition.

**Size check (arithmetic on the JSON values; not a measurement).**
- The raw gap in mean top-10 cosine is 0.0135 (`raw_cosine_nov_x100` 1.354 ÷ 100).
- One own paper entering the ten nearest neighbours changes the mean by (its cosine − the cosine of the neighbour it
  displaces) ÷ 10.
- So the confound alone reaches the observed gap if that difference averages about 0.135 across incumbent papers.
- For scale: mean nov runs 0.37-0.47 by year (descriptives), so typical top-10 cosines are about 0.53-0.63. A
  same-team follow-up 0.135 above the tenth neighbour is plausible.
- **The confound can therefore be as large as the whole gap.** None of the existing sensitivities removes it:
  - excluding 2021;
  - newcomer_s4;
  - papers with no earlier version;
  - the plain definition.

P1's handling turns this into a feature: "this part *is* continuity among incumbents". That is fair for the incumbent
side. But it means the abstract cannot say that entrants' papers "lie farther from earlier ICLR work" as though this
described entrants.

**Required before the clause enters the abstract.** Rerun the outcome-free script with **every earlier submission by
any of the paper's own authors** removed from the reference set. Author IDs are used as join keys only and are never
printed. Report:
- newcomer vs incumbent;
- first-time teams vs returning topic newcomers.

Until then the result is §5 support, worded "partly by construction".

**Also from P3 §9.2.** Re-run the contrast on early-map (2017-20) topic × year cells. The registered entrant tests
passed both hindsight variants (DC:296-297); the E result should meet the same standard.

### 4.3 The entry result's novelty must be framed against canonical producer-side work

The following are verified in lit_novelty_reward.md / .bib but absent from all four proposals:
- **Zeng et al. 2021** (*Nature Human Behaviour* 5(10):1314-1324): fresh teams are associated with original work.
- **Packalen and Bhattacharya 2019** (*Journal of Human Capital* 13(2):341-373): younger researchers try new ideas
  more.
- **Hofstra et al. 2020** (*PNAS* 117(17):9284-9291): underrepresented scholars innovate more, and their novelty is
  discounted.
- **Chu and Evans 2021** (*PNAS* 118(41):e2021636118): large fields ossify their canon.

A reviewer from this literature will say "newcomers bring new things" is known. **The novelty is not that entrants
innovate.** It is that a registered **herding** prediction for entrants failed in the opposite direction, at a gate
where rejected papers are visible. Cite Zeng and Packalen as convergent producer-side evidence.

**Pre-empt the Hofstra reading explicitly.** "Entrants farther out, newcomers accepted less" invites a
diversity–innovation-paradox reading. The paper must say:
- it does **not** show that entrants' distant content is discounted;
- the newcomer acceptance gap is mostly about who writes (−10.2 within topic × year, falling to −3.1 with author fixed
  effects; D; DC:343, DP:178);
- field distance has no replicated association with acceptance (P1b; C; DC:371).

**Use Chu and Evans** in §6.1: ICLR grew forty-fold (DP:71), so it is a natural test of the large-field mechanism at
the gate, and crowding is uninformative there (C).

### 4.4 The "method" label includes adapters built on the hot package

An adapter on an LLM is labelled method, not new architecture (DC:283-284). A reviewer can argue that entrants writing
method papers on top of LLMs *is* herding. The registered reversal refutes the registered operationalisation (herding
as follow-on measurement work), not herding in general.

The counter-evidence is outcome-free and should sit next to the reversal:
- first-time teams write FM papers less often (E; DP:360-362);
- the content gap holds with an FM control (+5.76; NN `team_class_fm_ctrl_pct`).

Scope every "not herded" sentence to the follow-on work herding predicts. P1 does this; keep it.

---

## 5. Grafts onto the winner (P1)

### 5.1 From P4 (take)

1. **Info codes in Table 1.** Add a compact column or superscripts:
   - P: prospective (only earlier submissions or lagged shares);
   - H✓ / H✗: registered hindsight variants pass or fail;
   - R: retrospective by construction (PH6);
   - T / T✓: post-decision text, and whether the discovery link-removal check passed.

   This makes the measurement discipline visible on every row without making hindsight the spine.
2. **PH6 is retrospective by construction** (DP:81). Say so in §6.4. A1 is the prospective timing test (PRE:1258-1261).
3. **A compact "ruler" paragraph** in §2 or §4. Cite:
   - whole-period topic histories: Hall et al. 2008; Pramanick et al. 2023; Schäfermeier et al. 2021;
     Grootendorst 2022;
   - temporal leakage: Kaufman et al. 2012; Kapoor and Narayanan 2023;
   - emergence detection: Li et al. 2025; Khanbayov and Kurban 2026.

   This anchors Act 1 for ACL reviewers.
4. **Abstract wording.**
   - "tested them again on 11,099 held-out papers", because H3a was not replicated;
   - a closing scope clause, "All findings are associations at one venue". Keep the memorable line before it, or fold
     the two together.
5. **The Stelmakh pairing as the first sentence of the entry act,** plus the **ethics statement** and the
   **data-provenance sentence** (Re² audited and not pooled; DC:69).

**Do not take** P4's "reading backwards / forwards" vocabulary. It collides with P1's memorable line ("conformity looks
backward"), where "backward" means "towards the record", not hindsight.

### 5.2 From P2 (take)

1. **"The package travels with an ICLR record"** as the producer-side face of continuity in §5.5. Show the
   first-time-team bins together with the verified FE contrast (returning topic newcomers vs incumbents: +1.1, −0.4,
   −2.6, +2.9, −1.0; all p ≥ 0.06).
   - Say "not detectable", never "no difference".
   - The 30-50% bin is wide.
   - Add the FE rows to dossier_posthoc.md first.

   This closes P1's 2 × 2 cell "continuity among producers" with outcome-free evidence that does not depend on the
   confounded content test.
2. **The era sentence for entrants.** The content gap was no smaller in 2023-26, while the FM share rose from 10.6% to
   54.4% (+6.01 vs +4.95; difference p 0.44; NN; DC:168). Carry it with the Section 4.2 caveat.
3. **H1e as one clause in §4:** no detectable shift towards empirical or evaluation papers with adoption (−0.63
   [−3.64, +2.38]; C; DC:272). The package's within-topic signature is displacement of new architectures, nothing more.
4. **One Discussion sentence for the hype debate.** Claims of homogenisation need to say which layer they measure. At
   ICLR the substrate converged (A), while no herding of the testable kinds was detected among entrants. Use
   "homogenisation in Bommasani et al.'s sense".
5. **P2's verb guardrails, adopted in full:** never "crowds out", "causes" or "displaces" with FM as subject, nor
   "choose".

### 5.3 From P3 (take, sparingly)

1. **A reflexive caption for Figure 1.** "These keywords were chosen for display after their curves were known." One
   sentence; it is honest and memorable.
2. **Honest denominators.** Next to the three B continuity results, list the post hoc patterns that did not hold
   held-out:
   - P1b, C;
   - P7, C;
   - FL, D/C.

   Then the B rows are not read as cherry-picked survivors. **Do not** take P3's "differential survival" sentence or
   its claim that imitation "fades in foresight". Both are blind to power.
3. **The early-map rerun of the content-distance contrast** (P3 §9.2), as above.
4. **Fischhoff 1975** as the one-line anchor for the hindsight result in §4.

### 5.4 Fit repairs to P1

1. **Cut Table 1 to its unmarked rows (18 of 24)** and move the † rows to the appendix table.
2. **Drop Figure 4b.** It duplicates Table 1's rows 13 and 16-20, and it is the figure most likely to invite
   cross-module size comparisons (DC:428).
3. **Keep the figures to three:**
   - Figure 1, the waves;
   - Figure 2, hindsight bars plus the FM / new-architecture trend;
   - Figure 3, the entry forest.

   Show the closeness-fifth shape (D) only if space remains.
4. **Recount the body words after these edits.** Target about 3,600, to leave room for the Matthew-effect and
   self-continuation paragraphs.

---

## 6. The three sharpest reviewer objections to P1, and how the paper should pre-empt them

### Objection 1: "Continuity" is the Matthew effect, or visible status, relabelled

**The objection, as a reviewer would write it.** "Acceptance going with experienced and insider teams is cumulative
advantage (Merton 1968). At ICLR it is status made visible through arXiv (Ibrahim et al. 2026), or simply experience
and selection into teams. Calling it a 'route to conformity' adds a word, not an idea."

**Pre-emption.**
1. In §2, define continuity by **the position of a paper's content relative to a record**, not by having a record.
   Name cumulative advantage and visible prestige as the rival readings in the same paragraph.
2. In §6.2, order the evidence by how well it holds status fixed:
   - **E4 first.** Within the same author: +1.06 [+0.23, +1.89] held-out (B; DC:372). Note that co-author composition
     may explain half or more (DP:243).
   - **E1 second.** Among teams that all have a record: −6.09 [−9.32, −2.86] held-out, primary test, held-out Holm
     0.005 (B; DC:370). With a newcomer control: −5.0 (DP:238).
   - **The insider last,** stated as the result a status reading explains equally well: per head, insider ≈
     crossover, +0.58, p 0.16 (D; DP:294-296); keyword insider +0.0 (DP:289).
3. Discussion sentence: "Status and expertise readings cannot be separated here. What the within-author and
   within-record associations add is that, holding who writes fixed, acceptance goes with how close the content stays
   to that record."
4. Keep "positions, not motives" (TA:630-631). Never write "bias" or "discount".

### Objection 2: Entrants "propose" by label, and their content is "farther" partly by construction

**The objection, as a reviewer would write it.**
- "'Method' is a type, and it includes adapters on LLMs, so entrants may be herding onto the package while being
  labelled proposers.
- Your content test is unregistered, and incumbency is defined by an earlier same-topic paper that sits in the
  reference set.
- Fresh teams being more original is known (Zeng et al. 2021).
- Flocking is untested."

**Pre-emption.**
1. **Before drafting:** run the author-excluded content-distance rerun and the early-map rerun (Section 4.2). Then:
   - if the gap survives, keep the abstract clause with "descriptively";
   - if it shrinks to near zero, delete the clause, and say in §5 that the incumbent side's closeness is
     self-continuation (which is itself continuity).
2. **In §5, next to the reversal:**
   - "A method paper is a contribution type, not novelty; an adapter on an LLM counts as method" (DC:283-284, 313-314);
   - the outcome-free FM-uptake evidence: first-time teams adopt more slowly (E), and record-holding newcomers adopt at
     incumbent rates (FE);
   - the H2c team-size qualifier (−0.54, p 0.07; DC:301).
3. **Position the novelty correctly.** "Producer-side studies find that fresh teams and younger researchers bring new
   ideas (Zeng et al. 2021; Packalen and Bhattacharya 2019). Our contribution is that a registered *herding*
   prediction for topic entrants failed in the opposite direction at the review gate of a fast-moving venue, and the
   reversal replicated."
4. **Scope the claim.** "We can say what entrants write and how fast they adopt trends, not whether they crowd into
   hot topics" (H2a, C; DC:295). Name our own registered prediction as proof that the herding account is not a straw
   man: we held it ourselves.

### Objection 3: The positive half is post hoc, and "record not field" compares a powered test with an underpowered one

**The objection, as a reviewer would write it.** "The continuity tests were found in discovery. Six secondary held-out
tests are one-sided and unadjusted. Your centrepiece contrast says own-record distance replicates and field distance
does not. But E1 had power 0.89 on 5,344 papers (2023-26, experienced teams), while P1b had power 0.47 on 8,010
papers (2019-26, all teams). The difference between significant and non-significant is not itself significant."

**Pre-emption.**
1. **Open §6 with the asymmetry.** "The negative half of our thesis rests on registered tests; the positive half on
   post hoc tests that a declared held-out test supported" (P1 §6 already plans this). Give E1's primary status and
   adequate power (DP:233-235). Give the insider and E4 tests as "direction only".
2. **Reword §6.2's contrast.**
   - Write: "the own-record association replicated; whether distance from the field matters, our held-out test cannot
     say (power 0.47)".
   - Never write "the gate ignores novelty" or "field distance does not matter".
   - Compare replication status only, as P1's guardrail already requires (DC:428). Add the power and population
     difference to the Table 1 caption.
3. **Honest denominators** (Section 5.3 item 2), and Holm within family only (insider ≈ 0.17 across modules; DP:54-55).
4. **Keep the "biographical vs substantive" reading in the Discussion as an interpretation.** Use it to reconcile
   Teplitskiy et al. 2022, Foster et al. 2015 and Hill et al. 2025. Label it a hypothesis that this design could not
   test, because a joint model of both distances on one population was not run.

---

## 7. Checklist: changes to P1 before the writers start

1. **Abstract.**
   - "the imitation prediction fails where theory expects imitation most";
   - "tested them again";
   - the content clause only after the author-excluded rerun;
   - end on "associations at one venue".
2. **§2 definitions.**
   - Continuity is a content position relative to a record.
   - Name Merton 1968 and Ibrahim et al. 2026 as rivals.
   - Keep the Tversky-Kahneman footnote for "anchored".
3. **§3.** The F_max wording is the cosine with the mean of each experienced author's prior set, maximised over authors
   (PRE:1377-1380). Add the P/H/R/T codes.
4. **§5.**
   - Add the FE record-holder rows and the era sentence.
   - Add the adapter-is-method caveat.
   - Add Zeng, Packalen and Hofstra positioning, plus the explicit "no discounting claim" sentence.
5. **§6.**
   - Lead continuity with E4 and E1.
   - Insider last, as status-compatible.
   - Reword the field-vs-own contrast; add honest denominators.
   - Mark PH6 retrospective.
   - Use Chu and Evans 2021 for crowding.
6. **§7.** Biographical vs substantive conservatism as an interpretation. Add the layer sentence for the homogenisation
   debate.
7. **Fit.** Table 1 cut to its 18 unmarked rows, three figures, about 3,600 body words.
8. **Open items carried forward:**
   - commit the novelty script and outputs;
   - add the FE rows to the dossier;
   - read the CONTENT-SECONDARY theory originals before citing specific results (TA:665-676);
   - confirm the ARR page limit against the current call.
