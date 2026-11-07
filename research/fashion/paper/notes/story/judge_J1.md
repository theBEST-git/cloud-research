# Judge J1: senior area chair review of the four story proposals

Reviewer stance: a demanding ACL ARR senior area chair, Computational Social Science and Cultural Analytics track. I
reward a clear contribution to the ACL community, sound computational methods and honest claims. I punish laundry
lists of findings.

Built 2026-11-03.

## 0. Verdict in brief

**Ranking:**
1. **P4**, "The Herd in Hindsight": winner, 51/70.
2. **P1**, "Anchored, Not Herded": 45/70.
3. **P2**, "A Package, Not a Herd": 43/70.
4. **P3**, "Herds in Hindsight": 42/70.

**Why P4 wins.** P4 keeps the substance of P1, and its ordering of claims matches the strength of the evidence:
- **First contribution:** the hindsight measurement result (tier E). It is ACL-native, and its gap (G4) survived
  verification, narrowed only in wording.
- **Second:** the registered entrant reversal (tier A), whose gap (G2) holds.
- **Third:** continuity at the gate (tier B), whose gap (G3) was narrowed twice (Hill et al. 2025; Bao and Li 2025).

It has the cleanest wording of the four:
- The abstract tags the gate result "(post hoc, supported on held-out papers)".
- It writes "tested them again", not "replicated".
- The retrospective PH6 wave set is flagged.
- The SPECTER2 basis of F_max is checked.
- It adds an ethics statement.

It also adds a reusable instrument: a per-claim code (P prospective, H hindsight map, R retrospective, T post-decision
text) that any text-as-data history can adopt.

**What P4 still needs.** It must not win as written. It needs:
- the fixes in Section 5, including dropping one selective cross-split size comparison and correcting two
  prediction-column labels;
- the grafts in Section 4;
- two outcome-free checks of the content-distance result (Section 7).

---

## 1. What I read and what I checked

**Read in full:**
- the four proposals;
- `dossier_core.md` and `dossier_posthoc.md`;
- `verify_prior.md`;
- the frame and scorecard of `theory_anchors.md` (§2-4);
- the candidate and recommendation sections of `landscape.md`.

`analysis_novelty.md` does not exist. I read its numbers from `output/novelty_newcomer.json` instead.

**No outcome or decision column was read. No forbidden script was run. No corpus author is named.**

**Checks run for this review:**

| # | Check | Result |
|---|---|---|
| 1 | **Citation keys.** Every key the proposals cite beyond the core set (e.g. `lazaridou2021mind`, `kaufman2012leakage`, `bailey2017probability`, `klavans2020novel`, `bharadhwaj2020deanonymization`, `strang2001search`, `abrahamson1999management`) | Present in the workspace `.bib` files. Each work's verification status is as recorded in those files; I did not re-verify the works themselves. |
| 2 | **Novelty numbers.** Each interval quoted for `novelty_newcomer.json` | Matches the file, e.g. main [4.948, 6.848]; method only [4.162, 6.313]; team control [4.64, 6.537]; era difference p 0.439; 2019 p 0.704. Recorded but not quoted by anyone: the recomputed measure correlates 0.74 with the plain definition (`corr_nov_vs_plain`), and the module's cached values were never compared (caveat 6). |
| 3 | **P2's "[read here]" values,** against committed outcome-free files | Correct. `ph5_fmwave/free_entry.csv`, topic newcomer vs incumbent: +1.1 (p 0.06), −0.4 (0.73), −2.6 (0.11), +2.9 (0.31), −1.0 (0.10). `ph5_position/free_herding.csv`: first-time share 26.3%; FM row +11.0 [+8.0, +13.9]. They are not yet in a dossier. |
| 4 | **F_max definition** (PREREGISTRATION.md, distance features) | SPECTER2, centred and L2-normalised, as P1 and P4 say. P2's "still unconfirmed" and P3's "not verified myself" are stale. The measure is the maximum over experienced authors of the cosine to the *normalised mean* of that author's prior set. That set excludes the probable earlier version and every paper at cos ≥ 0.90. All four proposals paraphrase it as "the closest experienced co-author's earlier submissions", which is imprecise. |
| 5 | **Keyword states** (PREREGISTRATION.md, keyword frame) | Prospective: onset is the first year cumulative uses reach 10; momentum is share t−1 / share t−2. P4 is right. |
| 6 | **PH6 wave set** (RESULTS.md L968-969) | Retrospective: the share must peak in 2019-2024 and fall to at most half the peak by 2026. P4 is the only proposal that flags this. |
| 7 | **FM-entry model** (PREREGISTRATION.md, fmwave outcome-free part) | Includes class and log2 team controls, with first_time nested in newcomer. P1's description is right. The "no team-size control" caveat applies to the keyword profile only. |
| 8 | **Top-tenth retention** (+14.3 → +2.1) | A within-discovery number. DP:330 says "do not headline". `presentation/shortlist.md` L221 says "Do not quote top-tenth retention ... all CIs include 0". |

---

## 2. Scores (1-10)

| Criterion | P1 Anchored | P2 Package | P3 Herds in Hindsight | P4 Herd in Hindsight |
|---|---|---|---|---|
| Meaningful (beyond ICLR) | 7 | 7 | 8 | 8 |
| Novel (vs verified prior work) | 6 | 6 | 6 | 7 |
| Contributive (reusable idea or method) | 6 | 5 | 7 | 8 |
| Evidence fit (load-bearing on A/B/E, not D or weak B) | 5 | 7 | 4 | 6 |
| Honesty (no overclaiming, causal wording or advice) | 6 | 5 | 5 | 8 |
| Coherence (one story; every finding an expansion) | 8 | 6 | 7 | 7 |
| Fit to a 3,000-4,000-word ACL long paper | 7 | 7 | 5 | 7 |
| **Total (of 70)** | **45** | **43** | **42** | **51** |

### Why each score

**Meaningful**
- **P3 and P4: 8.** Both carry a general lesson: how a field comes to be read as a herd, and how computational
  histories should be checked. They also engage the LLM-era hype debate.
- **P1: 7.** Speaks mainly to science of science.
- **P2: 7.** Speaks to the homogenisation debate.

**Novel**
- **P4: 7.** It puts the two intact gaps first (G4 "same papers, same model, only the fitting window differs: 29 vs 8";
  G2, what entrants bring).
- **P1: 6.** Its distinctive claim sits on G3, which is narrowed twice and has a published rival reading (Ibrahim et
  al. 2026; VP:209-218). Its theory-level novelty rests on a search the theory file calls limited.
- **P2: 6.** Its G5 and G2 hold (VP:432, 435), but "foundation models homogenise the substrate" is Bommasani et al.'s
  own claim. The new element is one registered association.
- **P3: 6.** Hindsight bias, leakage and HARKing are known. Its "foresight design" cannot be novelty after Ibrahim et
  al. 2026.

**Contributive**
- **P4: 8.** The forward-reading audit (P/H/R/T per claim, refit on early years, lagged predictors) is a reusable
  method for the ACL genre.
- **P3: 7.** The three-channel taxonomy (categories, cases, estimates) is reusable, but it is an umbrella more than an
  instrument.
- **P1: 6.** The imitation/continuity split is a reusable concept.
- **P2: 5.** "Substrate vs people" is a label, not an instrument.

**Evidence fit**
- **P2: 7.** Its core rests on A and E. Its §6.2 claim, "review judges the package like a tool", rests on three D
  results (E1 +4.62; slope +0.19; E8 +8.3).
- **P4: 6.** Contributions 1-2 rest on E and A; contribution 3 rests on B and says so. But Table 1 carries a D row (row
  6), and Discussion item 3 makes a cross-split size comparison.
- **P1: 5.** Its title word ("Anchored") and its memorable line rest on B. Two of the three B tests are secondary,
  one-sided and unadjusted. The insider test is underpowered at its discovery effect (derived MDE80 about 4.5 vs
  +3.42; DC:374).
- **P3: 4.** Its "differential survival" counts uninformative nulls as failures: H3a (MDE80 4.8), FL (MDE80 14.5) and
  P1b (power 0.47). It also places the do-not-headline top-tenth retention in Table 1's "foresight" column, though that
  number is within-discovery.

**Honesty**
- **P4: 8.** See Section 3 for the three deductions.
- **P1: 6.** See Section 3.
- **P2: 5** and **P3: 5.** See Section 3.

**Coherence**
- **P1: 8.** One frame, each act testing one premise.
- **P3: 7** and **P4: 7.** Each stacks a measurement spine on the imitation/continuity theory. P4 subordinates the
  theory explicitly; P3 runs two theses.
- **P2: 6.** Its gate act is bolted on. The "records" of §6 (topical closeness to a team's own work) are not the
  "records" of §5 (any earlier ICLR submission).

**Fit**
- **P3: 5.** It must set up two routes, three hindsight channels and three foresight devices in about 900 words of
  §2-3.
- **The other three: 7.** Each plans about 3,800 words and is feasible. Every proposal's full-width table of 22-24
  rows, plus four figures, is tight in eight pages.

---

## 3. Proposal-by-proposal findings checked against the dossiers

### P1, "Anchored, Not Herded"

**Strengths:**
- The best conceptual hygiene:
  - fixed definitions;
  - "positions, not motives";
  - the "anchoring" footnote;
  - "never exploitation".
- The clearest "why each act is load-bearing" table.
- A useful route × site 2×2 in the Discussion.
- It alone reports the title-style spread honestly, as "the one place where imitation-like spread is plain". The share
  of "NAME: subtitle" titles rose from 7-14% to 37-49% (E\*; DP:120-125).
- It frames the self-continuation confound of the content-distance result as part of the thesis, not a defect.

**Defects:**
1. **Abstract and contribution 2 say "post hoc tests replicated on held-out papers".** The tier key reserves
   "replicated" for A. B is "post hoc, supported on held-out papers" (DP:14-15).
2. **The abstract joins the E-tier content result to the registered reversal without "descriptively":** "...less
   often build benchmarks, and their papers lie farther from earlier ICLR work". A reader takes both as registered.
3. **"The field converges, but less than hindsight suggests" conflates two things.** The 29-vs-8 result counts
   emerging topics, which is change, not convergence. Hindsight inflates the waves. It does not inflate convergence.
4. **The title and the memorable line put B-tier evidence in front.** "Conformity looks backward" also invites a
   motive reading that the definitions forbid.

### P2, "A Package, Not a Herd"

**Strengths:**
- The most conservative evidence base.
- The H1e limit: no detectable shift towards empirical or evaluation papers with adoption (C; DC:272). It keeps the
  package claim narrow.
- The contrast between a cumulative FM share (rising every year since 2018; DC:168) and 17 of 68 keywords that rose
  and fell.
- The era-stability sentence for the content gap: +4.95 in 2019-22 and +6.01 in 2023-26, difference +1.06
  [−1.64, +3.75].
- The nested FM-entry rows (verified above). They make "the package travels with an ICLR record" a precise
  absorptive-capacity pattern.

**Defects:**
1. **"Not a Herd" and "converged in its tools, not in its people" overclaim:**
   - Flocking is untested (H2a, C).
   - Title style spread (E\*).
   - Researchers' papers did converge on the package: 54.4% build on an FM in 2026 (DC:163).
2. **The thesis is not discriminated by its own central result,** as P2 concedes: H1d fits a bandwagon, lock-in and
   efficient choice alike (TA:600).
3. **Table row S1 sets up a strawman:** "herding predicts a wave that rises and falls" for a nine-year window.
4. **"The first topic-level test ... registered in advance and replicated"** is a first-claim about design after
   Ibrahim et al. 2026. It is qualified, but needless.
5. **§6.2 makes a section-level claim on D evidence.**
6. **The SPECTER2 caveat is stale** (Section 1, check 4).
7. **The "[read here]" values are correct but not yet in a dossier.**

### P3, "Herds in Hindsight"

**Strengths:**
- The most ambitious and general framing.
- The operational taxonomy of hindsight channels: categories, cases and estimates, plus post-decision text.
- The reflexive hook: "we expected a herd too".
- "Growth compounds hindsight": the all-years map (29) behaves like the late-only map (28) because 69.3% of papers are
  from 2024-26 (DP:72).
- A recommended outcome-free check: re-run the content-distance contrast on early-map cells.

**Defects:**
1. **"In foresight, the signatures of imitation shrink, fail or reverse" lumps uninformative nulls with failures.**
   H3a, FL and P1b fall below their MDE80 or have low power. The paper constraints say such nulls are uninformative,
   not evidence. Recasting FL and P1b as "demonstrations of the thesis" turns uninformative results into support.
2. **"Every imitation signature we could test" ignores the title-style spread,** which is imitation-like and holds
   (E\*).
3. **Table 1 row C2 uses the top-tenth retention (+14.3 → +2.1)** and labels the +2.1 as "foresight". It is a
   within-discovery number with CIs that include 0, and the sources forbid headlining it (DP:330; shortlist L221).
4. **The abstract says "post hoc tests replicated".**
5. **"Hindsight sees a herd; foresight finds a record" rests its second half on B.**
6. **"Differential survival" vote-counts tests of very unequal power and status:** registered tests against six
   one-sided, unadjusted secondary tests.
7. **Field novelty and FL are not imitation signatures.** If imitation were rewarded, a penalty on derivative work or a
   punished fad would count against it, not for it. Using their non-replication as evidence against imitation is a
   category error.

### P4, "The Herd in Hindsight" (winner)

**Strengths:**
- The evidence ordering described in Section 0.
- The ACL-native primary conversation: computational histories of NLP and ML.
- The best guardrail compliance. It flags:
  - PH6 as retrospective;
  - pooled keyword shares against Figure 1's discovery data;
  - "Isn't the hindsight result obvious?" in advance. The seed refit finding 28 shows the gap is not seed noise.
- §6.5 names the fact that most threatens the continuity reading: per head, an insider is worth about as much as an
  experienced author from another topic (+0.58, p 0.16; D; DP:296), and a keyword-defined insider shows nothing (+0.0;
  DP:289).

**Defects to fix:** see Section 5.

---

## 4. Grafts onto the winner

### From P1
1. **Scope in the title.** "...Reading ICLR's Foundation-Model Wave as It Unfolded".
2. **The definitional discipline:**
   - imitation and continuity label positions, not motives;
   - the "anchored" footnote, only if the adjective is used at all;
   - never "exploitation";
   - never "teams choose".
3. **The honest title-style paragraph.** Report the rise as imitation-like spread in surface form (E\*). Pair it with
   Abrahamson and Rosenkopf 1993 (bandwagons can spread without reward) and the D\* ratio 1.02, labelled "earlier
   exploratory, not re-run".
4. **The route × site 2×2** as a compact Discussion table. It replaces P4's Discussion item 3.
5. **Figure 4 grouped by reference point:**
   - **record-referenced:** E1, E4, insider;
   - **referenced to others or to the field:** H3a, P1b, P7.

   Compare replication status, not size. Add the sentence that field novelty and far jump use the same SPECTER2 space
   with different reference points.
6. **The "each act tests one premise of the herding account" logic** for the introduction's preview.

### From P2
1. **The H1e limit sentence:** the package's within-topic signature is fewer new architectures, nothing more.
2. **The cumulative-FM-share vs rise-and-fall-keywords contrast** (E) in §4.2 or the Figure 2 caption.
3. **The era-stability sentence for the content gap.**
4. **The nested FM-entry comparison.** First-time vs returning topic newcomers: −4.6 / −9.0 / −14.7. Returning topic
   newcomers vs incumbents: no detectable difference in any bin. Use "no detectable difference", never "no
   difference". Add both rows to the dossier first.
5. **"Homogenisation in Bommasani et al.'s sense (the substrate)"** and "consistent with", never "confirms".
6. **The principle that no B-tier result goes in the title or the memorable line.**

### From P3
1. **The operational "cases" channel** to label Figure 1 (keywords shown after their curves were known), the PH6 wave
   set and the FL case. These become P4's R code.
2. **"Growth compounds hindsight",** with the full monotone gradient across maps. Emerging topics by map: early 8,
   middle-era 10, balanced 16, late-only 28, seed refit 28, all-years 29 (DC:176-181).
3. **The size-tercile panel** (top-fifth growth by size tercile: 40/21/2% vs 22/20/20%; DC:224) as a vivid E panel in
   Figure 2, with the "no paired test" caveat.
4. **The reflexive hook**, "we expected a herd too", to open §5.
5. **The early-map-cells re-run** of the content-distance contrast (Section 7).

### Do not graft
- **P1's "conformity looks backward, not sideways".** In P4, "backward" means hindsight. Grafting it would give one
  word two opposite meanings, and it invites a motive reading.
- **P2's "Not a Herd" and "tools, not people".**
- **P3's "shrink, fail or reverse", its "differential survival" count, the top-tenth retention, and "foresight finds a
  record".**

---

## 5. Required fixes to P4 itself

1. **Drop Discussion item 3** ("Read backwards, every herd signal in this paper was larger than its forward reading").
   - It compares discovery and held-out sizes, which the rules forbid (DC:428; DC:47).
   - It is selective: H1d (−7.98 → −11.0), H2c′ (−1.70 → −2.10) and E1 (−5.44 → −6.09) all moved the other way.
   - Replace it with the 2×2, and with a verdict-only sentence: vivid in-sample cases (FL, P1b) were "not confirmed
     (uninformative)" on held-out papers. That shows why they cannot carry claims, not that herding is absent.
2. **Fix two prediction-column labels in Table 1.**
   - **Row 24, least-novel fifth.** "Herding predicts − (gate penalises derivative work)" has the wrong motivation:
     rewarded imitation would favour derivative work, if anything. Set the herding cell to "·". Frame row 24 as the
     field-referenced counterpart of rows 20-21.
   - **Row 19, FL.** This is a fashion-cycle case, not a herding prediction. Set "·" and mark it R (cases channel).
   - **Row 6** (FM premium; D) goes to the appendix, as P4's own space plan allows.
3. **Use the exact F_max definition** from PREREGISTRATION.md: the maximum over experienced authors of the cosine to
   the normalised mean of each author's earlier ICLR submissions since 2021, excluding the probable earlier version and
   near-duplicates (cos ≥ 0.90).
4. **Abstract.**
   - Replace "staying near a team's own record" with "papers far from the team's own earlier work are accepted less
     often". The shape shows the closest fifth gains nothing over the fourth: 47.2 vs 46.9% (D; DP:236). The near
     contrast E2 is not significant.
   - Replace "including a topic insider" with "having a topic insider on the team". "Including" reads as a choice.
5. **Memorable line.** The current line is weak, and P3's rests on B. Use a line resting on A and E only, e.g.:
   "Hindsight tells a herd story; read forward, the field converges on a package while its entrants propose."
6. **Confine "reading forward" to the temporal axis:** dated measures, lagged predictors, early-fitted maps.
   - Call the inferential axis what it is: a pre-registered split-sample replication within the same years.
   - Do not describe the held-out test as reading the field "as it unfolded".
7. **§2.3 wording.** "An RCT at ICML found no herding among reviewers" becomes "detected no herding" (VP:269-270).
8. **Table length.** Keep at most about 16 rows in the main text, with the full 24 rows in the appendix.
   - **Never drop:** the honest nulls and failures (rows 13, 14, 19, 24).
   - **Do drop:** row 3 (R², no paired test) to the Figure 2 caption, and row 12 into row 5.
9. **Add the grafted title-style paragraph (graft P1-3) to §4.** Without it, the paper hides the one imitation-like
   signal that holds.

---

## 6. The three sharpest reviewer objections to the winner, and how to pre-empt them

### Objection 1: "The positive half is post hoc and is probably experience, quality or visible status, not 'continuity', let alone conformity."

**The evidence a reviewer will cite:**
- Far jump, within-author closeness and insider are tier B.
- Two of the three are secondary, one-sided and unadjusted tests. "One false positive would not be surprising"
  (DP:29-30).
- The insider's Holm 0.019 is within-family only, about 0.17 across modules (DP:54-55).
- F_max correlates −0.57 with the newcomer flag (DP:247).
- Co-author composition may explain half or more of E4 (DP:243).
- Per head, an insider ≈ an experienced author from another topic (+0.58, p 0.16; D), and a keyword-defined insider
  shows nothing (DP:289, 296).
- Ibrahim et al. 2026 offer visible prestige via arXiv as a rival reading.

**Pre-emption:**
- Open §6 with the asymmetry. The negative half rests on registered tests (A, C); the positive half on post hoc tests
  supported by declared held-out tests (B).
- Lead with E1, the primary test: held-out −6.09 [−9.32, −2.86], one-sided p 0.0025, Holm 0.005, MDE80 4.9, power
  0.89 at the discovery effect (DP:233-235). Present E4 and the insider as direction only.
- Put the B rows next to the post hoc tests that did *not* survive (P1b, P7, PH6 without the six inspected keywords),
  so the reader sees the B rows are not a list of survivors only.
- Define continuity by reference point, not motive.
- State in one paragraph that expertise, evaluator conservatism (Li 2017), visible status and selection cannot be
  separated. Give the insider ≈ crossover fact openly: "a record of any kind" is not separated from "topic knowledge".
- Keep continuity out of the title and the memorable line.
- Say "acceptance goes with", never "the gate rewards".

### Objection 2: "'Reading forward' is a rhetorical umbrella, and the hindsight result is either obvious or confounded."

**The evidence a reviewer will cite:**
- The early map cannot represent topics born after 2020. It fits 2026 papers worse (0.53 vs 0.69 for 2017; DC:179).
- The maps differ in fitting corpus as well as window (DC:229).
- The R² comparison has no paired test.
- The held-out split is not forward in time. It shares years, reviewers and authors (DC:43-45).
- The vivid cases (FL, novelty floor) are used as if their non-replication proved something.

**Pre-emption:**
- Define the two axes once. Use "forward" only for the temporal one (fix 6).
- Show the result as a monotone gradient in the amount of late data in the fit: 8, 10, 16, 28, 28, 29 (DC:176-181).
  This includes the seed refit (28), so the gap is not seed noise.
- Report the bracket (22.3% to 40.9% of 2024-26 papers in emerging topics; DC:187), and use "inflates", never
  "manufactures".
- Show that a substantive conclusion changes with the window: the lifecycle flip, exploratory and unadjusted (DC:201-202).
  The registered H1d, H2b′ and H2c′ pass both hindsight variants, while H2a and the held-out H3a fail them.
- Make no claim for the R² gap beyond "E, no paired test".
- Drop Discussion item 3 (fix 1). Present FL and P1b as "not confirmed (uninformative)", never as support.

### Objection 3: "Beyond the registered reversal, the entry evidence is descriptive and partly mechanical."

**The evidence a reviewer will cite:**
- A method paper is a type, not novelty (DC:313-314).
- **The content-distance gap is built in.** Incumbent papers by definition have an author with an earlier submission
  in the topic. That paper sits in the "strictly earlier" reference set and pulls their distance down (NN caveat 3).
- SPECTER2 distance may reflect vocabulary from other fields (caveat 4).
- The analysis is unregistered and recomputed: it correlates 0.74 with the plain definition, and the module's cached
  features were never compared (caveat 6).
- Labels are LLM labels checked against LLM labels (DC:52).
- The 2021 ID switch hides earlier histories (DC:145-146).

**Pre-emption:**
- Run, before writing, the decomposition in Section 7 (excluding the paper's own authors' earlier submissions from the
  reference set) and the early-map-cells re-run. Report whichever way they come out.
  - If the gap survives, "farther from earlier work" stands apart from self-continuation.
  - If it shrinks, write that incumbents' papers sit closer to their own earlier work. That is still evidence against
    the follow-on prediction and for continuity among incumbents (P1's framing).
- Keep:
  - the within-method estimate (+5.24 [4.16, 6.31]);
  - the size in plain terms (about 0.22 of a within-cell SD, "modest but precise");
  - the 2019 null (+1.26, p 0.70).
- Keep "descriptively" in the abstract.
- For the labels, report:
  - κ 0.93;
  - that the misclassification correction can only enlarge H2b′/H2c′ (+4.09 / −1.84; DC:304);
  - that H2c′ shrinks with a team-size control (−0.54 discovery; −0.98 held-out). H2b′ carries the reversal.
- The R2 variant without 2021-22 gives the same entry results (+3.72 / −1.74; DC:148), and the content gap without
  2021 is +5.87.
- State inside §5, not only in the Limitations, that flocking (H2a) is untested.

**Standing caveats** (one venue, held-out not independent, the 12.6% / 10.0% size failure) are already handled in
P4's §3 and Limitations. Keep them verbatim.

---

## 7. Outcome-free checks to run before drafting

1. **Content-distance decomposition.**
   - Recompute each paper's novelty with every earlier submission by any of its own authors removed from the
     reference set. Then re-estimate the newcomer gap within topic × year.
   - Author IDs are used as join keys only, never printed.
   - This is the single most important check for P4's §5.2.
2. **Early-map cells.** Re-estimate the gap with 2017-2020-map topic × year cells and newcomer flags, as P3 recommends.
3. **Commit and cross-check.** Commit `scripts/novelty_newcomer.py` and its outputs, labelled "added during writing,
   outcome-free". Cross-check against the position module's cached novelty features.
4. **Dossier additions:**
   - the novelty rows;
   - the nested FM-entry rows from `free_entry.csv`;
   - the first-time share (26.3%) from `free_herding.csv`.
5. **The branding ratio (D\*).** Re-run it outcome-blind through the frozen machinery, or keep it only as "earlier
   exploratory, not re-run" in one clause and the appendix.
