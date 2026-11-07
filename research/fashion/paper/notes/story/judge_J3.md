# Judge J3: supervisor's verdict on story proposals P1-P4

Built 2026-11-03. I read the four proposals in full, along with dossier_core.md, dossier_posthoc.md, landscape.md
(sections 0, 3-5), theory_anchors.md, verify_prior.md and `output/novelty_newcomer.json`. I also read these
outcome-free committed files to check the proposals' numbers:
- `research/fashion/output/posthoc/ph5_fmwave/free_entry.csv`;
- `research/fashion/output/posthoc/ph5_position/free_herding.csv`;
- PREREGISTRATION.md, lines 1105-1114, 1256-1263, 1279-1283, 1370-1381, 1567-1571 and 1657-1661 (definitions only).

What I did not do:
- read any outcome or decision column;
- run any analysis script (the only computation was arithmetic on the JSON values);
- read the other judges' files;
- name any corpus author.

Pointers: `DC:n` and `DP:n` are line n of dossier_core.md and dossier_posthoc.md; `NN` is novelty_newcomer.json;
`VP`, `TA` and `LS` are verify_prior.md, theory_anchors.md and landscape.md.

---

## 1. Verdict in one paragraph

**Winner: P1, "Anchored, not herded"**, with four elements grafted on: P4's forward-reading discipline and ACL
packaging; P2's "the package travels with an ICLR record" rows; P3's audit of the post hoc patterns that failed;
and P3's reflexive hook.

P1 has the one story line that is a single, falsifiable, theory-level claim: **conformity at ICLR is
record-referenced (continuity), not crowd-referenced (imitation)**. Every finding has a place as a test of one
premise of the herding account. It is also the most disciplined about tiers.

P4 ties with P1 on points. It is P1's substance under a methodological spine, "reading forward", and it is the best
packaged for an ACL senior area chair. Its thesis is a compound of three claims rather than one, so it ranks second,
and its packaging is grafted onto P1.

P3 is the most ambitious and the most meaningful, but its slogan inverts the actual evidence chronology, and it reads
uninformative nulls as "fading". P2 rests on the safest tiers, but its headline, convergence on the FM substrate, is
close to what the field already says, and it turns an unregistered, confounded measure into a pillar.

---

## 2. Scores (1-10)

| Criterion | P1 Anchored, not herded | P2 A package, not a herd | P3 Herds in hindsight | P4 The herd in hindsight (ACL) |
|---|---|---|---|---|
| Meaningful (beyond ICLR) | 8 | 7 | 9 | 8 |
| Novel (vs verified prior work) | 7 | 5 | 8 | 7 |
| Contributive (reusable idea or method) | 7 | 6 | 8 | 8 |
| Evidence fit (load-bearing on A/B/E) | 6 | 7 | 5 | 6 |
| Honesty (no overclaim, causal wording or advice) | 8 | 6 | 5 | 7 |
| Coherence (one story, all findings expand it) | 8 | 7 | 7 | 7 |
| Fit to a 3,000-4,000-word ACL long paper | 8 | 7 | 5 | 9 |
| **Total (of 70)** | **52** | **45** | **47** | **52** |

**Ranking: P1 > P4 > P3 > P2.**

P1 and P4 tie on points. I break the tie on the supervisor's first criterion, one story line:
- P1's thesis is one claim: conformity looks backward, not sideways.
- P4's thesis is three claims (a package, proposing entrants, a continuity gate) held together by a design principle.

Everything P4 does better can be moved onto P1 without changing P1's thesis.

---

## 3. Proposal by proposal

### P1 "Anchored, not herded" (winner)

**Story.** Fields can become uniform by imitation (taking the cue from others now) or by continuity (taking it from
an accumulated record). The herding account of ML assumes imitation. P1 tests it at three points:
- **Field:** convergence is real (H1d, A), but hindsight inflates the fashions (29 vs 8, E).
- **Entry:** the registered herding prediction reversed (A), and entrants' content is farther from earlier work (E).
- **Gate:** there is no detectable premium for following (C, D\*, B). The associations that hold are record-referenced
  (B).

The closing line is "At ICLR, conformity looks backward, not sideways."

**Strengths.**
- **One claim, many expansions.** Table 1 is a scorecard with "imitation predicts" and "continuity predicts" columns
  and a fixed five-label reading column. Every one of the 24 rows has a reading, which answers the supervisor's
  objection to the earlier talk directly.
- **Strong theory anchoring.**
  - Weisberg and Muldoon 2009 is the formal precedent, with Alexander et al. 2015 cited as the critique.
  - Bourdieu 1975 was read in full.
  - Absorptive capacity (Cohen and Levinthal 1990) gives an *opposite* prediction to cascades at entry, and A- and
    E-tier data adjudicate it. This is where the frame earns its keep.
- **It is honest about its own asymmetry.** The negative half is A; the positive half is B, and §6 opens by saying
  so. The flocking test is shown as "untested" (H2a, C).
- **It applies every verify_prior narrowing**: Hill 2025, Bao and Li 2025, Wang 2023, Xu 2026, Ibrahim 2026,
  Stelmakh 2023 and Boudreau 2016.
- **It closes the SPECTER2 check**: PRE:1372 confirms that F_max uses centred SPECTER2, which I re-read.

**Weaknesses.**
- **The title word "Anchored" is carried by tier B.**
  - E1, the far jump, is the PH5 primary test and is adequately powered: held-out Holm 0.005, MDE80 4.9, power 0.89
    at the discovery effect (DP:233-235).
  - E4 and the insider test are secondary, one-sided and unadjusted. The insider test is underpowered (derived MDE80
    about 4.5 against +3.42) and its Holm 0.019 holds within its family only (DP:54-55).
- **The record-versus-field contrast in §6.2 is partly a contrast of power.** E1 had power 0.89; P1b had power 0.47
  and is uninformative (DP:259-260). P1 says "compare replication status, not size". It also needs to show power,
  or the reader will infer that field distance does not matter.
- **Act 1 is non-discriminating by P1's own account** (TA:600, 616). It takes 500 words to establish that
  convergence is real and that hindsight inflates fashions.
- **The abstract sentence "Imitation fails where theory expects it most" overstates.** Flocking, the core of
  cascade herding, is untested. What failed is our registered operationalisation: entrants write follow-on
  measurement work.
- **"Continuity" as a route to *conformity* needs an argument** (objection 3 in Section 6).

**Claim checks** (numbers re-verified against DC, DP, NN and the committed CSVs):
- H1d −7.98 [−12.14, −3.82] / −11.0 [−18.1, −3.9]: correct (DC:271, 364).
- H2b′/H2c′: correct (DC:296-297, 365-366).
- 29 vs 8 emerging topics; late-only map 28; balanced map 16; declining 13 vs 26: correct (DC:176-181).
- The first-time-team FM gaps −4.6 / −9.0 / −14.7 with class and log2 team-size controls: correct (free_entry.csv;
  PRE:1111).
- Twins per paper per 1,000 submissions 0.32 → 0.19: correct. My recomputation gives 0.321 and 0.190 from DP:79's
  inputs.
- Novelty +5.90 [4.95, 6.85]; method papers only +5.24; 0.22 within-cell SD: correct. My recomputation gives
  1.354 / 6.18 = 0.219.
- Minor: P1's closest-prior table carries a number from Movva et al. ("half of 2023 LLM first authors"), which has
  not been checked against the PDF (VP:33-36). Keep it out of the paper.

### P4 "The herd in hindsight" (ACL framing) — second

**Story.** This is P1's substance. The spine is "read backwards" against "read forward":
- temporal: lagged measures and early-fitted maps;
- inferential: registered or declared tests confirmed on held-out papers.

**Strengths.**
- **Best ACL fit.**
  - Conversations native to ACL: computational histories (Hall 2008, Pramanick 2023, Schäfermeier 2021,
    Grootendorst 2022), temporal leakage (Kaufman 2012, Kapoor and Narayanan 2023, Lazaridou 2021), and the LLM-era
    hype debate.
  - A table of the questions a senior area chair will ask, each with its answer.
  - An ethics statement.
  - The code-link leakage fact (17.6% vs 0.5%) used as a text-as-data lesson.
- **The most useful honesty device of the four.** Each row of Table 1 carries an info code:
  - P: prospective;
  - H: k100 cells, with H✓ or H✗ for the hindsight variants;
  - R: retrospective by construction;
  - T: post-decision text, with T✓ where the link-removal check passed.
- **Two checks no other proposal made:**
  - the keyword timing states behind A1 are prospective (PRE:1258-1262, which I re-read);
  - the PH6 wave set is retrospective by construction. A reviewer would otherwise catch this in a paper about
    hindsight.
- **A mechanistic sentence for the hindsight result.** 69% of papers are from 2024-26, so the all-years map is a
  present-day map. It fits 2026 papers better than 2017 papers (0.65 vs 0.62); the early map does the reverse (0.69
  vs 0.53) (DC:176-179).

**Weaknesses.**
- **Two spines at once.** Backward/forward and imitation/continuity both organise the paper, and the thesis is a
  three-part list.
- **"Read forward" fits Act 1 well but is forced at entry.** The herding prediction was registered: it was read
  forward and failed.
- **§7.3 overclaims.** "Every herd signal in this paper was larger than its forward reading" counts two things that
  cannot carry it:
  - federated learning (−11.3 vs −4.9) and the novelty floor (−3.27 vs −0.13) are uninformative held-out nulls (MDE80
    14.5; power 0.47). Comparing their sizes breaks DC:46-47;
  - the novelty floor is not a herd signal.
- **The memorable line is vague**: "Hindsight tells the herd story; foresight tells a different one."

### P3 "Herds in hindsight" — third

**Story.** A field looks like a herd when it is read through three hindsight channels:
- categories fitted after the fact;
- cases chosen for their outcome;
- estimates made on the data that suggested them.

Close each channel and imitation's signatures shrink, fail or reverse, while the package and the record hold.
Closing line: "Hindsight sees a herd; foresight finds a record."

**Strengths.**
- **The most meaningful and most reusable idea.** The three channels and their foresight counterparts form a
  checklist for diagnosing any field as faddish.
- **It turns the failures (FL, P1b, PH6 without the six inspected keywords) into part of the argument.** It also
  makes the failed registered prediction the hook ("We expected a herd too").
- **Its open-item list is sharp.** In particular it proposes re-running the novelty gap on early-map cells, so that
  the novelty result meets the same hindsight standard as the registered tests.

**Weaknesses (decisive).**
- **The slogan inverts the chronology of our evidence.**
  - The herd was predicted *in foresight*: H2b/H2c were registered before outcomes existed, and they failed.
  - The record was found *in hindsight*: E1, E4 and the insider test are post hoc patterns from discovery data,
    which is P3's own "estimates" channel, later supported on held-out papers.
  - A reviewer will turn "hindsight sees a herd; foresight finds a record" around in one sentence.
- **It reads uninformative nulls as fading.** "Signatures of imitation shrink, fail or reverse" counts FL (MDE80
  14.5), P1b (power 0.47) and H3a (uninformative) as failures. DC:46 forbids this.
- **"Differential survival" counts verdicts across tests of very different power.** The record tests survived
  partly because they were better powered.
- **"Foresight" is used for the held-out split**, which is the same conference-years (DC:45). It is out-of-sample,
  not later in time.
- **It repeats an error from verify_prior.md §6.** "Like Ibrahim et al. 2026, we test pre-registered predictions on
  *later* ICLR papers" is false for our design. Ibrahim et al. used a later cohort; our held-out set shares years,
  reviewers and authors with discovery.
- **Table row C2 headlines the top tenth's +14.3 → +2.1**, which DP:330 says not to headline. It is also a
  selected-extreme regression to the mean, not an imitation signature.
- **Too much for 3,800 words**: three channels, two routes, three points and a survival audit.

### P2 "A package, not a herd" — fourth

**Story.** What converged in the FM shift is the package papers build on, not the people:
- substrate: H1d (A) and the FM share;
- people: the reversal (A) and the E-tier profile;
- gate: no detectable premium for popularity, and a premium for records.

Short form: "converged in its tools, not in its people."

**Strengths.**
- **The thesis sits on A and E**, so it survives a reviewer who discounts every post hoc result.
- **One genuinely new descriptive point, which I verified in free_entry.csv.** Topic newcomers who already have an
  ICLR record write FM papers at the incumbents' rate in every adoption bin: +1.1 (p 0.06), −0.4 (0.73), −2.6
  (0.11), +2.9 (0.31), −1.0 (0.10). Teams new to ICLR lag (−4.6 / −9.0 / −14.7). So the package travels with an ICLR
  record, which is the absorptive-capacity pattern. It also answers the objection that entrants' extra method papers
  are merely FM applications.
- **Good contrasts for Act 1:**
  - the FM share rose every year since 2018 (DC:168), while 17 of 68 keywords rose and fell;
  - H1e is null (C), so the field-wide rise in measurement papers is not tied to adoption within topics.

**Weaknesses.**
- **The headline is close to known or near-trivial.**
  - "Homogenisation in the substrate" is Bommasani et al.'s claim, and 54.4% of 2026 papers build on an FM.
  - H1d confirms an expected pattern.
  - The discriminating work is still done by P1's entry evidence.
- **"Not in its people" overclaims.**
  - Flocking is untested.
  - Title style spread fourfold among people (E\*).
  - Incumbents consolidate.
- **It makes the content-distance result a pillar.** That result is unregistered, has not been checked against the
  module's cached features, and carries a self-continuation confound that may be large (Section 6, objection 2).
- **Its gate act includes a D-tier sub-claim** ("the package is judged like a tool, not like a fad").
- **Small errors:**
  - It says the F_max embedding is unconfirmed; PRE:1372 confirms SPECTER2.
  - "Topic-level fashions are partly a measurement artefact" uses a word the dossiers' bracket wording avoids.
  - C1 makes a "first" claim, qualified, that is better dropped.

---

## 4. Cross-cutting checks every writer must apply

| # | Issue | Affects | Correct handling |
|---|---|---|---|
| 1 | The premia result b = 0.60 [0.32, 0.88] rejects b = 0 (p 6.5 × 10⁻⁵), and EB D0 > 0 (DC:376-377). Topic edges are therefore **real and partly persistent**, not absent. | All four put premia under "no premium for following" | Wording: "a favoured topic keeps part of its edge but not all of it" (0 < b < 1). Use it as evidence against *full* persistence of outcome-imitation signals, never as "no premium". Crowding (H3a, C) is the "following the crowd" test. |
| 2 | Uninformative held-out nulls (FL MDE80 14.5; P1b power 0.47; H3a MDE80 4.8) | P3 and P4 most; P1 §6.2 | Never "shrank", "faded" or "larger in hindsight". Say "not confirmed" or "uninformative", and print MDE80 or power next to every replication verdict. |
| 3 | Held-out = the same years (DC:45) | P3; verify_prior §6 "Design" sentence | Never "later ICLR papers" or "foresight" for the held-out split. Say "a pre-registered out-of-sample replication, not a certified untouched holdout". |
| 4 | Content-distance self-continuation. Incumbents' own earlier papers in the topic stay in the 10-neighbour reference set (NN caveat 3). Back-of-envelope, not a measurement: the raw gap is 1.35 × 10⁻² on a mean of 10 cosines, so one own paper per incumbent paper that is about 0.135 more similar than the neighbour it displaces would produce the whole gap. Close follow-ups plausibly are. | All; P2 most | Keep it at tier E support, never a pillar. Re-run it outcome-free with all of the paper's own authors' earlier submissions removed from the reference set (author IDs used as keys only, never printed), and on early-map cells (P3's suggestion). Commit the script and output first. |
| 5 | Values first read by the story agents | P2 | The free_entry "topic newcomer vs incumbent" rows, the 26.3% first-time share and the FM-twin +11.0 are all correct in the files. The FM-twin model's fixed effects are undocumented, so drop that row. Add the first two to dossier_posthoc.md before quoting. |
| 6 | Numbers from cited papers (Hill's 35%, Movva's "half") | P1's design tables | Describe these works qualitatively until the PDFs are read (VP:33-36). |

---

## 5. Grafts onto the winner (P1)

### From P4 (ACL packaging and forward-reading discipline)

1. **Info codes in Table 1.** Add P / H(✓/✗) / R / T(✓) to each row. Mark PH6 R (retrospective wave set) and A1 P
   (prospective states; PRE:1258-1262). Say in §6.4 that PH6 is retrospective by construction.
2. **A short "forward-reading rules" paragraph in §3.** All entry, adoption, closeness and novelty measures use only
   earlier submissions. Registered trend claims must also hold on the balanced map and the early map. Code-link
   leakage is 17.6% vs 0.5%, with the discovery-only link-removal re-run. This is design, not thesis.
3. **ACL conversations in §2 and Act 1:** Hall 2008, Pramanick 2023, Schäfermeier 2021, Grootendorst 2022, Kaufman
   2012, Kapoor and Narayanan 2023, Lazaridou 2021. All keys exist in the workspace bibs.
4. **The mechanistic sentence for 29 vs 8**: the all-years map is a present-day map (69% of papers from 2024-26;
   fit 0.65 vs 0.62 against the early map's 0.69 vs 0.53). Add the seed refit (28), which shows the result is not
   seed noise.
5. **The senior area chair's questions**, answered in a sentence each:
   - Why ACL?
   - Are LLM labels valid? Consistency, not human validity; the misclassification correction can only enlarge the
     entry gaps (+4.09 / −1.84).
   - Is it causal? Is held-out independent? Does ICLR generalise?
6. **Abstract qualifiers.** Use "(post hoc, supported on held-out papers)", "tested them again" rather than
   "replicated" for the full set, and "All findings are associations at one venue."
7. **An ethics statement:** author identifiers are used only as keys; results are reported in aggregate; no review
   scores are used.

### From P3 (anti-cherry-picking and the hook)

8. **A small audit table of every post hoc pattern taken to held-out papers** (appendix, or a compact block in
   Table 1):
   - held: E1, E4, teams H1, premia b;
   - did not hold: P1b and P7, both not supported, P1b uninformative;
   - not supported: H4-FL;
   - weak: A1 and PH6.

   Each row gets its MDE80 or power. This pre-empts the charge that the continuity half was cherry-picked. Do not
   frame it as "imitation signatures fade".
9. **The reflexive hook for paragraph 3 of the introduction:** "We expected a herd too." Then the registered
   prediction and its reversal.
10. **The Figure 1 caption** should admit that the keywords shown were chosen after their curves were known.
11. **"Growth compounds hindsight":** the all-years map finds as many emerging topics as the late-only map (29 vs
    28). One clause.
12. **The early-map robustness run for the novelty gap** (outcome-free), before it enters Table 1.

### From P2 (the package travels with records; sharper Act 1)

13. **Add to §5:** topic newcomers with an ICLR record use FMs at the incumbent rate in every adoption bin (all
    n.s.), while teams new to ICLR lag. This shows that entrants' extra method papers are not just FM applications,
    and it sharpens absorptive capacity against cascades. Add the rows to the dossier first.
14. **Add to Act 1:**
    - the package is cumulative: the FM share rose every year since 2018, unlike the 17 of 68 keywords that rose
      and fell;
    - H1e (C): the field-wide rise in measurement papers is not tied to adoption within topics;
    - one sentence on Bommasani's "homogenisation", in the substrate sense only.
15. **Add to §5:** the entrant content gap did not shrink in the FM era: +4.95 in 2019-22 vs +6.01 in 2023-26,
    difference +1.06 [−1.64, +3.75], p 0.44 (NN).
16. **Make "continuity" the technical term in the body.** Keep "anchored" only in the title and one defined use,
    with the footnote citing Tversky and Kahneman 1974 and Baddeley 2015. This answers P2's "anchoring" hazard.

### Changes to P1's own text

17. **Replace** "Imitation fails where theory expects it most" with: "The herding prediction we registered for topic
    entrants failed in the opposite direction, and the reversal held on held-out papers."
18. **Cut Act 1 to about 400 words.** Move the lifecycle flip to one sentence plus Figure 2, and spend the saved
    words on objection 3 (Section 6).
19. **Rewrite §6.2** as "only the record-referenced association has been shown to replicate; the field-referenced
    one is undetermined (power 0.47)", not "distance from the field has no replicated association" alone.
20. **Trim the page budget.** 3,800 words plus a 24-row `table*` plus four figures is tight for 8 ACL pages. Keep
    Table 1 at about 16 rows (move the † rows and row 21 to the appendix table) or merge Figures 2 and 3.

---

## 6. The three sharpest reviewer objections to the winner, and how to pre-empt them

### Objection 1: "The positive half is post hoc, its contrast is a power artefact, and 'continuity' may just be status."

**The objection.**
- The continuity half (far jump, closeness, insider) was found in discovery data and is tier B.
- Two of the three held-out tests are secondary, one-sided and unadjusted, and one of them is underpowered.
- "Record-referenced replicates, field-referenced does not" compares a test with power 0.89 to one with power 0.47.
- Authors are identifiable through arXiv, and ICLR's borderline decisions lean towards visible prestige (Ibrahim et
  al. 2026). The "insider" may be a famous name rather than topic knowledge.

**Pre-emption.**
- **State the asymmetry in the abstract, the introduction and §6:** the negative half is registered (A, C); the
  positive half is post hoc, supported on held-out papers (B).
- **Lead with E1, the declared primary**, and give its credentials: held-out −6.09 [−9.32, −2.86], one-sided p
  0.0025, Holm 0.005, MDE80 4.9, power 0.89. Present E4 and the insider test as direction only, with the
  within-family Holm caveat (about 0.17 across modules).
- **Print MDE80 or power beside every replication verdict** in Table 1 and Figure 4. Call field distance
  "undetermined", not "irrelevant".
- **Show the audit table** (graft 8): the post hoc patterns that *failed* are reported too, so the B rows are not
  survivors picked after the fact.
- **Give E1's robustness:**
  - newcomer control −5.0;
  - no earlier version −5.5;
  - link-removed text −5.39;
  - early map −5.2;
  - correlation with the newcomer flag −0.57 stated openly.
- **Name the rival mechanisms in one paragraph and say the data cannot separate them:**
  - expertise or better-made papers (Li 2017);
  - visible status (Ibrahim et al. 2026);
  - selection into teams.
- **Give the hints, at tier D:**
  - most of the newcomer gap is about who writes (−5.4 → −3.1 with author fixed effects);
  - the same author entering a new topic: −1.4;
  - an insider is worth about as much per head as a crossover author (+0.58, p 0.16).
- **Wording rules:** "continuity" labels positions, not motives; never "bias", "discount" or "rewards" as a causal
  verb.

### Objection 2: "You tested a strawman of herding, and your best rebuttal is mechanically confounded."

**The objection.**
- Cascade herding is about *which topics people enter*. You did not test that (H2a inconclusive, fails its
  hindsight variant).
- "Entrants write method, not benchmark, papers" is your own operationalisation.
- A "method paper" can itself be imitative: applying the hot model to a new topic.
- The content-distance result that answers "type is not novelty" puts incumbents' own earlier papers in the
  reference set, so their papers look closer to earlier work *by construction*.

**Pre-emption.**
- **Derive the follow-on prediction from theory in §2**, with its sources:
  - mimetic isomorphism under uncertainty (DiMaggio and Powell 1983, general argument only);
  - Weisberg and Muldoon's "followers", biased towards approaches others have explored.

  Call it "the follow-on half of the herding account", and say in §5 and in the abstract's scope that the
  "flocking half" is untested. Cite Borjas and Doran 2015 only as context.
- **Present entry as four independent imitation signatures, not as H2b/H2c alone:**
  - contribution type (A);
  - content distance (E);
  - same-year twins, −3.9 pp (E);
  - uptake of trending keywords and FMs, −3.7 pp and −4.6 to −14.7 pp (E).
- **Use graft 13 to answer "method papers are imitative FM applications":** topic newcomers with an ICLR record use
  FMs at the incumbent rate in every bin, and the content gap holds within method papers (+5.24 [4.16, 6.31]).
- **Before submission, run the content-distance gap with all of the paper's own authors' earlier submissions
  removed from the reference set**, and on early-map cells. Both runs are outcome-free.
  - If the gap survives, the rebuttal is clean.
  - If it shrinks, report that honestly: the shrunk part is incumbents' own continuity, which supports the thesis
    from the producer side. Then drop "entrants bring content from elsewhere".

  Until then, word it as "farther from earlier ICLR work, partly because incumbents' own earlier papers are in the
  reference set". Never write "more original" or "more novel".

### Objection 3: "Continuity is not conformity. This relabels known effects, and Act 1 tests nothing."

**The objection.**
- Teams staying near their own records would *preserve* diversity across teams. So why is that a route to
  uniformity?
- The far-jump penalty is Hill et al.'s pivot penalty; the insider is Sekara et al.'s chaperone; closeness is Bao
  and Li's measure.
- The field-level act (H1d, 29 vs 8) fits lock-in, a package bandwagon and efficient choice alike.
- So the new idea seems to be a word.

**Pre-emption.**
- **Define the property in §2 as the source of a field's pull towards the established:**
  - Bourdieu's "limited innovations within authorised limits" and consecration of work "faithful to the principles
    of official science" (read in full);
  - Levitt and March's two kinds of learning, direct experience against the experience of others (content partly
    secondary).

  Say plainly that continuity produces conservatism and consolidation rather than identical choices, and that
  Weisberg (2013) calls exactly this risk-avoiding clustering "herding". The contribution is to split the literature's
  single word into two reference points and test them against each other.
- **Show what the split buys that relabelling does not:**
  - **at entry, opposite predictions.** Cascades say the least-informed entrants imitate fastest; absorptive capacity
    says they adopt the package slowest. The A- and E-tier data favour the latter.
  - **one population for both sides.** Producers and the gate are observed together, so the continuity reading
    links incumbents' consolidation (measurement papers, closer content) with the record-referenced acceptance
    associations.
- **Use the verify_prior narrowings verbatim:**
  - "Larger pivots are less often published (Hill et al., 2025); we observe the decision itself, on every
    submission to an ML venue, under double-blind review, with held-out replication."
  - "Our closeness measure, like Bao and Li's (2025), uses SPECTER2 similarity."
  - Put the Bao and Li tension (impact vs acceptance) in the Discussion.
- **Cut Act 1 to about 400 words, and give it one declared job:** convergence is real (A) and hindsight inflates the
  fashions (E), so the field level cannot decide between the routes; entry and the gate can. Say this in §2 before
  Act 1, so a reader does not take it as a verdict.
- **The novelty sentence stays at:** "To our knowledge, imitation and continuity have not been tested against each
  other at entry and at the review gate", with "among the works we checked".

---

## 7. Before the writers start (outcome-free; ordered)

1. **Commit the novelty analysis** (`paper_ws/scripts/novelty_newcomer.py` and its outputs) and cross-check it
   against the position module's cached features (NN caveat 6).
2. **Run the two outcome-free novelty variants** from objection 2: own-author exclusion and early-map cells. Use
   author IDs only as join keys; never print them.
3. **Add P2's verified free_entry rows** (topic newcomer vs incumbent, all five bins) and the 26.3% first-time share
   to dossier_posthoc.md.
4. **Fix verify_prior.md §6's "Design" sentence.** Our held-out set is not "later ICLR papers".
5. **Keep every number from a cited paper out of the text** until its PDF is read. Cite the content-secondary theory
   works (TA:665-676) for their general argument only.
6. **Branding ratio 1.02 (D\*):** label it "earlier exploratory, not re-run", or drop that Table 1 row.
