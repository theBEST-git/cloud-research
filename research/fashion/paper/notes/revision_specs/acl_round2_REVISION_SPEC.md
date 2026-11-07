# Revision spec: "Herded or Anchored?" (round 2)

This spec is the result of two critiques of the current draft (an independent expert critique and an external
reviewer's feedback) and the author's decisions on them. Every item below is DECIDED. Implement all of them. Where a
choice is left to you, it says so.

Workspace: this directory (`paper.tex`, `appendix.tex`, `references.bib`, `figs/`, `acl.sty`, `acl_natbib.bst`).
`paper_v1.tex` / `appendix_v1.tex` are the untouched previous version (read-only reference).
Build: `pdflatex -interaction=nonstopmode paper && bibtex paper && pdflatex ... && pdflatex ...`.
Word count: `python ../scripts/wc_body.py paper.tex` (body = Introduction up to Limitations, floats excluded).
Record of every number: `/home/user/cloud-research/research/fashion/RESULTS.md` (authoritative), plus
`PREREGISTRATION.md` there. NEW results this round are in RESULTS.md sections "Post hoc: do branded titles go with
acceptance? (PH7 titles ...)", "Descriptive: what is the newcomer reversal made of?", "Record pointers for paper
tables". Do not introduce any number that is not in the current paper, RESULTS.md, or a committed output named there.

## 0. Hard constraints (unchanged from the author)

- University project that uses the ACL template. Do NOT argue venue fit; no "why ACL" material.
- Body 3,000–4,000 words (target ~3,600); abstract ≤ 200 words; the main text (through Conclusion) must end on page 8;
  then Limitations, Ethics Statement, Acknowledgments (keep as is), references, appendix.
- Associations only. No causal or advice language: never "penalise", "reward" (as a verb for review), "pays",
  "drives", "effect of", "leads to", "causes", "reviewers punish", "prove". Use "goes with", "is accepted less often",
  "is associated with". "Rewarded imitation" is fine as the NAME of a theoretical account.
- Every finding carries an evidence label (scheme in §2 below).
- Held-out set: keep, once, the phrase "a pre-registered out-of-sample replication, not a certified untouched holdout".
- Federated learning: "not confirmed" (appendix only now).
- LLM labels: say they are consistent (second pass κ 0.93) and were hand-checked by the author on a small random
  sample; no human–LLM agreement number is available, so give none; put `% TODO(author): sample size and agreement of
  the hand check` next to that sentence. Keep "consistency between LLM labellings, not human-level validity".
- Author block, acknowledgments, ethics statement: keep (update ethics only if a fact changes).
- Data provenance: keep Appendix A's provenance paragraphs (existing datasets audited, not pooled).
- Never print author names or IDs.

## 1. The story (main change)

Current problem: the paper reads like a lab notebook (chronology of what was guessed wrong, post hoc labels, internal
codes everywhere), and its thesis is stated more strongly than the evidence. Fix both.

**Thesis (use this logic; wording is yours):** Machine learning is said to herd. A field can converge without
copying: researchers can instead stay close to a record (their own earlier work, or a topic they already know). We
tested the herding account where imitation and continuity predict different things. At entry its sharpest registered
prediction failed in the opposite direction, and the reversal replicated; at the gate the registered crowding test
was uninformative and the form that spread most (branded titles) shows only a small premium that the held-out test
did not confirm. What did replicate at the gate is tied to a team's own record. Continuity predicts that; status and
expertise predict it too, and we cannot separate them. So: the conformity we can DETECT at ICLR points to a record,
not to the crowd.

- Present the imitation/continuity distinction as a reading that organises the tests. Imitation's predictions were
  registered (they are the herding hypotheses); continuity's were written after the tests ran. Say this ONCE, plainly,
  in §2 or §3 (and keep it in Limitations). Do not keep re-telling the chronology elsewhere.
- **Lead with discoveries, not with failure.** The entry result is "researchers entering a topic propose methods more
  often, and benchmark/evaluation work stays with incumbents" — a refutation of the follow-on-entry picture the herding
  account implies. Mention that it reversed our own registered prediction in ONE crisp sentence as a badge of honesty
  (abstract, intro, §5 each at most once). "The reversal" must not be the noun the paper is built on.
- **Substrate vs behaviour, up front (intro ¶2):** pre-empt "everyone switched to FMs (0.3% → 54.4%), isn't that
  herding?" Convergence on a substrate is predicted by lock-in, efficient choice and a bandwagon alike, so it cannot
  tell the routes apart; the herding question is about how researchers behave when they enter a topic and what the
  gate accepts. (Do not claim it IS lock-in.)
- The slogan "the conformity we can detect points to a record, not to the crowd" appears at most twice (abstract and
  conclusion).
- Title (decided): `Herded or Anchored? Testing Conformity in Machine Learning\\ on a Decade of ICLR Submissions`.
  Update the first comment line of the file too. "Anchored" = a position relative to a record, not a mechanism; keep a
  SHORT footnote distinguishing it from the anchoring heuristic.

## 2. Evidence labels (replace the A–E*/codes system in the main text)

Main text, figures and main tables use three plain labels plus plain words for registered non-results:
- **replicated** — registered before outcomes were read, supported again on held-out papers (old A).
- **held-out supported** — found post hoc, then supported by a test declared before the held-out data were read
  (old B). Drop "prim./sec." from prose.
- **exploratory** — discovery only, or descriptive (old D, E, D*, E*, and demoted results below).
- Registered or declared tests without a verdict: write "inconclusive" or "uninformative (below its 80%-power minimum
  detectable effect)" in words.

Typeset the label compactly and consistently (e.g. a small-caps tag via a macro such as `\lab{replicated}`), defined
once in the Introduction. Remove from the main text: tier letters, `\Hok`, `\Hno`, `\Tok`, [P], [R], "A (rev.)",
"B (prim.)", "B, weak", "D/C", "D*", "E*", and all internal codes (H1d, H2b′, H3a, P1b, E1, E4, PH5, PH6, PH7, A1, D0,
teams H1). The appendix keeps the detailed tiers and codes, with one mapping table from code to main-text name and
label (Appendix D "Every registered and declared test" is the place; update it).

Demotions decided:
- Keyword timing (Emerging vs Mainstream keywords; acceptance after a keyword's peak) → **exploratory**. Under Holm
  across the six secondary held-out tests (one-sided p: topic-edge slope 0.003, edge prediction D0 0.005,
  same-author closeness 0.006, insider 0.017, Emerging keywords 0.031, same-author distance-from-field 0.22) the
  Holm-adjusted values are 0.018, 0.025, 0.025, 0.051, 0.062, 0.22. The wave test leans on the six keywords inspected
  first. One or two sentences in §6 at most; details stay in the appendix.
- Topic insider: keep **held-out supported**, but say once that it does not survive a family-wise correction across
  the six secondary tests (Holm 0.051) and that a status reading fits it as well.
- Same-author closeness and the topic-edge regression survive that correction (say so where useful).
- Branded titles: **exploratory** (declared held-out test not supported, uninformative).

## 3. Structure, section by section

Target words (body ≈ 3,600): Intro ~650, §2 ~300, §3 ~450, §4 ~380, §5 ~650, §6 ~700, §7 ~320, §8 ~80. Each results
section (§4–§6) opens with ONE plain-English takeaway sentence before any number. Unpack jargon; prefer complete,
readable sentences over telegraphic compression (examples to avoid: "The tests need every submission, past-only
predictors and sealed outcomes."; "An insider is a record possessed, which cumulative advantage ... predict too.";
"The negative half of our thesis rests on a registered test (C), the positive half on post hoc tests ... (B)").

**Abstract** (≤ 200 words). Start from this draft (192 words) and keep its shape — problem → two routes → where they
are tested → field / entry / gate → takeaway. Do not end with a boilerplate "All findings are associations" (the verbs
carry it). Small permitted edits: "crowded topics show neither a detectable premium nor a penalty"; keep "post hoc,
confirmed on held-out papers" for the gate result.

> Machine learning is often said to herd: researchers chase what is hot, and review rewards it. But a field can
> converge without copying. Researchers may instead stay close to a record: their own earlier work, or a topic they
> already know. We separate these two routes to conformity, imitation and continuity, and test the herding account
> where they predict different things. The data are 43,480 ICLR submissions (2017–2026), rejected and withdrawn
> papers included, with hypotheses registered before outcomes were read and re-tested on 11,099 held-out papers. The
> field did converge on foundation models, but convergence fits both routes, and which topics look like passing
> fashions depends on hindsight: 8 to 29 emerging topics, depending on the years a topic map is fitted on. Where the
> routes part, we detect no herding. Researchers new to a topic propose new methods more often than incumbents do,
> the reverse of our registered prediction. At review, crowded topics show no detectable premium, while papers far
> from their authors' earlier work are accepted less often (post hoc, confirmed on held-out papers). The conformity
> we can detect at ICLR is tied to a record, not to the crowd.

**§1 Introduction** (~650).
- ¶1 The herding claim and the wave (keep: 40-fold growth 384 → 15,411; FM share 0.3% → 54.4%; new architectures
  24.5% → 7.5%; keywords rose and fell, Figure 1; GANs 8.1% in 2018, LLMs 16.7% in 2026). One clause on NLP is fine
  (its researchers publish at ML venues) but no venue argument. Critics' view (Lipton & Steinhardt; Hooker; Dehghani;
  Bommasani) and cascade/fashion theory, briefly.
- ¶2 Substrate vs behaviour (see §1 of this spec); the two routes in plain words; "anchored" + short footnote.
- ¶3 What we do: the herding account makes three claims (waves are fashions; newcomers carry them by following; the
  gate rewards following); we test each at the field, at entry and at the gate, on every submission including
  rejected and withdrawn ones. Design in two sentences (registered before full-corpus labels existed; outcomes sealed
  until one frozen run; held-out phrase). Evidence-label scheme in one or two sentences.
- ¶4 What we find, leading with discoveries (field / entry / gate), one sentence each.
- ¶5 **Contributions** as a bulleted list (3 bullets, one or two sentences each, each with its label):
  1. Entry: a registered test of herding where imitation predicts it most; researchers entering a topic propose
     methods more often (+3.7 pp; replicated), including researchers with ICLR work in other topics, and the pattern
     predates foundation models; benchmark and evaluation work sits with topic incumbents and larger teams.
  2. Gate: on every decided submission under double-blind review, acceptance goes with closeness to the team's own
     record (far jump −5.4 pp, held-out −6.1; held-out supported), not detectably with the crowd. Position against
     Hill et al. (2025): they already relate pivots to publication success; what we add is the accept/reject decision
     itself for every submission, rejected ones included. Never "first to show/prove".
  3. Method for histories of the field: on the same papers, the number of "emerging" topics ranges from 8 to 29
     depending only on the years the topic map is fitted on; reporting an early-window refit is a cheap check for
     trend claims (precedents already in the bib: Rotolo et al. 2015; Li et al. 2025; Khanbayov & Kurban 2026 — the
     existing "a prospective signal has been tested" citation).
- Keep the related-work positioning short (Ibrahim et al. prestige gap with the same design idea; Movva et al.;
  Bao & Li; Hill et al.) and keep the hedge "to our knowledge, among the works we checked".

**§2 Two Routes to Conformity** (~300; halve the current section).
- One paragraph per route: what it is, what it predicts at entry and at the gate. Keep the core citations
  (Bikhchandani; Banerjee; DiMaggio & Powell; Abrahamson; Scharfstein & Stein for imitation. March; Cohen & Levinthal;
  Stuart & Podolny; Zeng et al. / Packalen & Bhattacharya for outsider accounts for continuity; Weisberg & Muldoon). Drop
  the Bourdieu quotations and the separate "Timing" and "Gap" paragraphs (fold the gap into one sentence; move
  priority/timing citations to §6 only if still used).
- Name the rival readings once: visible status and expertise also predict record-side gate associations; network
  diffusion (peripheral actors adopt later; e.g. Coleman, Katz & Menzel 1957, if verified) also predicts that teams
  new to ICLR take up the package later, so that contrast does not discriminate.
- Add a compact single-column **predictions table** ("Table 1"): rows Imitation (reference point: others, now) and
  Continuity (reference point: a record); columns Field / Entry / Gate; cells = the prediction in a few words (field:
  convergence on a package — both, and lock-in and efficient choice too; entry: imitation → entrants flock to hot
  topics and write follow-on benchmark/evaluation work, adopt the rising package early; continuity → entrants bring
  other work, incumbents consolidate, the package travels with a record; gate: imitation → premium for crowded topics,
  popular form, riding a wave; continuity → acceptance tracks closeness to the team's record). Caption: imitation's
  entry and gate predictions were registered; continuity's were written after the tests. This replaces the
  "Predicted" column of the old Table 1.

**§3 Data and Design** (~450).
- Corpus, populations, instruments (topics, LLM labels with the hand-check sentence + TODO, FM paper, method paper,
  measurement paper), the entry profiles defined clearly: newcomer paper (no author has an earlier ICLR submission in
  this topic); among newcomer papers, first-time team (no author has any earlier ICLR submission) and returning topic
  newcomer (an author has one in another topic); incumbent paper; topic insider. State "newcomer" is topic-relative and
  ICLR-only. Two distances (closeness to own record F_max; distance from earlier ICLR work). Prospective measurement
  and code-link leakage (17.6% vs 0.5%).
- Protocol: registration, sealed outcomes, one frozen run, declared post hoc tests, held-out tests run once; the
  support rule; size failure (12.6%/10.0%, not fixed by wild bootstrap); define MDE80 and "uninformative" HERE (before
  any results table). Add the disclosure (missing until now): before registration, keyword popularity and title style
  had been explored against acceptance on the discovery papers, so discovery estimates on those two dimensions are not
  tests. One or two sentences may credit the sealed-outcome engineering (outcomes readable only by committed code in a
  logged gated run).

**§4 The Field: What Is Fashion and What Lasts** (~380). Takeaway first: keyword waves are real, how many topics look
emergent depends on hindsight, and the one durable shift (the FM package) fits every route.
- Waves at keyword level are real: 17 of the 68 most frequent keywords rose and fell (keywords do not depend on a map).
- Emerging topics: 8 (2017–2020 map) to 29 (all years), same papers and pipeline (exploratory). State it as a bracket
  and name both reasons: the window leaks the future, and the early map cannot represent topics born after 2020.
  Do NOT say topic fads are "mostly an artifact". Keep the 22.3% vs 40.9% share and the forecast asymmetry (R² 0.28 vs
  −0.03) in Figure 2's caption or the appendix.
- Durable: the FM share rose every year; where more of a topic's previous-year papers built on FMs, fewer of its papers
  proposed new architectures (−7.98 pp [−12.14, −3.82] for 0 → 100%; held-out −11.0 [−18.1, −3.9]; replicated,
  direction only); no detectable shift to empirical/evaluation papers (−0.63 [−3.64, +2.38]; inconclusive); reverse
  causality possible (one clause). Fits lock-in, efficient choice and a bandwagon alike → the field level cannot
  decide; entry and the gate must.
- Remove the branded-title and twins sentences from §4 (titles move to §6; twins: keep only in §5 if needed).

**§5 Entry: Who Writes What** (~650). Frame: a division of labour. Takeaway first: researchers entering a topic bring
methods; benchmark and evaluation work stays with incumbents and larger teams; this is the opposite of the follow-on
entry the herding account implies.
- Registered result (replicated): newcomer papers more often method papers, +3.71 pp [+2.61, +4.80] discovery,
  +3.60 [+1.48, +5.71] held-out; less often measurement papers, −1.70 [−2.46, −0.93] and −2.10 [−3.35, −0.85]; all 10
  counted variants agree. Newcomer papers are 72.9% of 42,325 papers. One sentence that it reversed our registered
  prediction. Say plainly that much of the measurement gap is team size: with log team size −0.54 [−1.11, +0.04] in
  discovery and −0.98 held-out, while the method gap is unchanged (+3.92 / +3.64).
- NEW decomposition (exploratory; RESULTS.md "what is the newcomer reversal made of?"): profile shares 26.3% first-time
  teams, 46.7% returning topic newcomers, 27.0% incumbents; median team 3 / 5 / 5. Method: returning topic newcomers
  +3.43 [+2.31, +4.55] vs incumbents (same median team size; +3.62 with team size); first-time teams +4.35 [+2.82,
  +5.89]; first-time vs returning +0.92 [−0.44, +2.29], no detectable difference. → The method surplus goes with
  entering a topic, not with being new to ICLR or with small teams. Measurement: first-time teams −2.24 [−3.24,
  −1.25] vs incumbents but +0.09 [−0.63, +0.81] with team size; returning topic newcomers −1.47, −0.81 [−1.47, −0.16]
  with team size. By era: the method surplus is present in every era (first-time − incumbent +6.61 in 2019–20, +5.00
  in 2021–23, +3.74 in 2024–26), i.e. it predates foundation models; the measurement gap appears only in 2024–26
  (first-time − incumbent −2.75 [−4.07, −1.44]; earlier eras −0.70, −0.71, n.s.). Reading: in the FM era, benchmark
  and evaluation work sits with topic incumbents and larger teams (team size is the resource we measure; do not claim
  compute). Pramanick et al. (2023) found in NLP that methods drive and datasets follow — cite as a parallel.
  Do NOT claim the FM era "inverted the scientific lifecycle".
- Distance (exploratory): newcomer papers sit farther from earlier ICLR work, +5.90 percentile points [+4.95, +6.85]
  within topic × year, +4.33 [+3.44, +5.22] with the authors' own earlier papers excluded; method papers alone +5.24.
  The follow-on prediction expects them closer. Newcomer papers less often have a same-year twin (−3.86 [−4.98, −2.74];
  exploratory). Keep ONE short caveat inline (a method paper is a contribution type, not novelty; embedding distance
  is not originality) — the rest goes to Limitations.
- Package uptake (exploratory): first-time teams come later to the FM package (FM-paper gap vs returning topic
  newcomers −4.58 [−6.55, −2.60] to −14.71 [−19.82, −9.61] at 5–50% prior adoption, 2023–2026; returning topic
  newcomers do not differ detectably from incumbents) and list Emerging keywords less often (−3.74 [−5.14, −2.35]).
  Both absorptive capacity (continuity) and network diffusion predict this; it does not discriminate. Figure moved to
  the appendix (figA_fm_entry).
- Flocking (registered, inconclusive): one sentence (−0.73 [−2.68, +1.22]).
- End: "no detectable difference fits the follow-on prediction" (replace "every detectable difference runs against
  imitation").
- Figure 3 (new file, panel (a) only, already regenerated): rows Method paper, Benchmark/dataset/evaluation paper
  (discovery and held-out), Has a same-year twin, First-time vs returning team: method paper, First-time vs returning
  team: Emerging keyword. Caption must say rows 1–2 are registered and replicated (held-out confirms direction, not
  size), rows 3–5 exploratory (discovery only), grey = side the herding prediction expected, no acceptance data.

**§6 The Gate: Does the Crowd Pay, or the Record?** (~700; choose a title without causal "pay" if you prefer, e.g.
"The Gate: Crowd or Record?"). Two questions as the structure. Takeaway first.
- Q1 Does acceptance go with following the crowd? (a) Crowding (registered): uninformative, −1.68 per log unit
  [−3.68, +0.32] discovery, −1.51 [−5.20, +2.19] held-out, MDE80 4.8; the registered prediction was a penalty; neither
  a penalty nor a premium is detectable; held-out premiums above +2.19 lie outside the interval. (b) Branded titles
  (NEW, PH7): the share of titles that open with a short coined name and a colon rose from 10.9% (2017) to 44.6% (2026)
  — the plainest imitation-like spread in the corpus. Within topic and year with class, FM and team-size controls,
  branded titles are accepted +1.74 pp [+0.37, +3.11] more often in discovery (not a test: title style had been
  explored before registration), and the declared held-out test gives +1.76 [−0.82, +4.34], one-sided p 0.089, MDE80
  3.2: not supported, uninformative (exploratory). Raw within-year gaps are larger (+3.3 discovery, +4.0 held-out);
  about half goes with topic, type, FM and team size. Titles can be revised after the decision (camera-ready), which
  could create such a premium. This replaces the old "ratio 1.02" claim everywhere (that number is superseded: delete
  it). (c) FM papers are accepted more often, +4.62 [+2.79, +6.44] (exploratory), and the premium does not change
  detectably with the topic's prior adoption, +0.19 [−0.96, +1.34] per logit unit: late adopters fare as early ones
  do, which fits rewarded imitation and efficient choice alike. (d) Topic edges are real but regress: a topic's
  2018–2022 acceptance edge (vs all other papers of the same year) predicts its 2024–2026 edge with slope 0.38 [0.18,
  0.58] among discovery papers, and the held-out papers' 2024–2026 edges regress on the discovery 2018–2022 edges with
  slope 0.60 [0.32, 0.88] (held-out supported; two different comparisons — say so). (e) Timing (exploratory, one or two
  sentences): Emerging keywords +2.67 [+0.76, +4.58] discovery, held-out +3.25 [−0.18, +6.69]; after a keyword's peak
  −5.7 discovery (not a test), held-out −5.2 [−11.1, +0.7], −1.7 (p 0.33) without the six keywords inspected first;
  neither shows the flat premium that rewarded imitation of what is popular predicts.
- Q2 What does acceptance go with? Centrepiece: the far jump. Among 20,430 decided 2023–2026 papers with an
  experienced author, acceptance at the 10th percentile of F_max minus at the median is −5.44 [−7.10, −3.78] in
  discovery and −6.09 [−9.32, −2.86] held-out, power 0.89 (held-out supported, the declared primary test); adjusted
  acceptance rises with closeness up to the fourth fifth (appendix figure figA_closeness). Same author, a paper 0.1
  closer in cosine to that author's earlier work: +0.55 [+0.21, +0.90] discovery, +1.06 [+0.23, +1.89] held-out
  (held-out supported; survives the family-wise correction). REPLACE the unsupported "co-author composition may
  explain half or more of this" with: controls for newcomer status and for co-authors' experience move it little
  (+0.48 and +0.50 per 0.1 cosine), though a co-author quality confounder could also produce it (a simulation in the
  declaration showed this is possible). Within-person entry (exploratory, PH3 in RESULTS.md): the same author is
  accepted about 1.4 pp less often [−2.7, −0.0] on a paper in a topic new to them (author fixed effects). One topic
  insider vs none: +3.42 [+1.18, +5.66] discovery, +3.88 [+0.28, +7.47] held-out (held-out supported, not under the
  family-wise correction; status-compatible; per head only +0.58 pp more than an experienced author from another
  topic, p 0.16, exploratory). Newcomer papers' raw −10.2 pp gap stays a footnote (mostly who writes, Appendix).
- Field record: distance from the field's earlier work is undetermined: least-distant fifth vs middle −3.27 [−4.93,
  −1.60] in discovery, −0.13 [−3.50, +3.25] held-out, power 0.47 (uninformative). Write "only the own-record
  associations replicated"; NEVER "distance from the field is not penalised".
- Rivals in one or two sentences (status, expertise, evaluator conservatism, de-anonymisation through preprints), with
  the rest in Limitations. Relation to Hill et al. as in the contributions bullet. Boudreau et al. / Teplitskiy et al.
  contrast can stay (one sentence).
- Figure 4 is now the gate-test forest (already regenerated, `figs/fig4_gate.pdf`): groups "Referenced to a record"
  (far jump, same author +0.1 cosine, one topic insider) and "Referenced to others or the field" (crowding, branded
  title, least-distant fifth vs middle, same author +10 pct of distance); discovery (blue circles) and held-out declared
  tests (orange squares), 95% intervals, verdict words on the right; rows have their own x-scales (pp; per log unit;
  per 0.1 cosine; per 10 percentile points). Write the caption accordingly. The old quintile curve is now
  `figs/figA_closeness.pdf` (appendix).

**§7 Discussion** (~320). Keep a compact routes × sites summary table (single column) — it is the story map; update it
to the new labels, add branded titles, drop D*/E*, and move timing to exploratory. Paragraphs: what the evidence
supports (stated honestly: registered herding predictions failed at entry and were uninformative at the gate; the
replicated positive associations are referenced to a record; status/expertise remain live), what remains open, why
the distinction matters (imitation → fragile consensus; continuity → long-run costs, March; for histories of the
field, an early refit and lagged predictors are a cheap check). Weisberg's risk-avoiding clustering can stay; drop the
Bourdieu sentence or keep it to one clause.

**§8 Conclusion** (~80). Field / entry / gate in one line each; the slogan once.

**Limitations.** Trim repeats; collect here the caveats removed from §4–§6: associations; one venue; held-out set
(shares years, reviewer pools, authors; confirms direction, not size); continuity frame post hoc; size failure; LLM
labels (consistency + author hand check; method paper ≠ novelty; an adapter on an LLM counts as method); embedding
distance ≠ originality; "newcomer" is ICLR-only and the 2021 identifier switch pulls entry contrasts towards zero;
abstracts and titles partly camera-ready (links removed and text re-embedded for discovery only; titles not
correctable); withdrawn papers left out of acceptance tests; status vs continuity (the identifiability test was not
run); hindsight comparison is a bracket; prior exploration of keyword popularity and title style before registration.

## 4. Tables (main text)

Replace the full-page old Table 1 (16 rows, ~230-word caption, notes a–i) with:
- Table 1 (§2): predictions, as above (single column).
- Table 2 (§5): entry results, single column, ≤ 7 rows (method; measurement; measurement with team size; returning
  topic newcomer − incumbent: method; first-time − returning: method; distance from earlier ICLR work (own work
  excluded); flocking), columns: discovery [95% CI] | held-out [95% CI] | label. ≤ 3 short notes.
- Table 3 (§6): gate results, single column, ≤ 9 rows (crowding; branded title; FM premium slope or FM premium; topic
  edge slope; far jump; same author +0.1 cosine; one topic insider; field distance; timing in one row or omitted),
  same columns, ≤ 3 short notes.
- Table 4 (§7): routes × sites summary (updated).
You may merge Tables 2 and 3 into one compact single-column table if space requires. Plain-English row names, no codes.
Move the complete old Table 1 (all 16 rows, codes, notes a–i), updated (row 3 code: twins are same-year, so not
"only earlier data"; row 10 estimands; row 11 labels; branded-title row added; timing demoted), to the appendix next to
the existing table of every test, or merge it into that table — your choice; keep every number.
Field rows (emerging topics; twins per pair 0.32 → 0.19 per 1,000) go to text or appendix.

## 5. Figures

Already regenerated in `figs/` by the repo script (do not edit images): `fig1_waves` (unchanged), `fig2_field`
(unchanged), `fig3_entry` (panel (a) only, new rows), `fig4_gate` (gate-test forest, NEW main figure), `figA_closeness`
(old Fig. 4 quintile curve, appendix), `figA_fm_entry` (old Fig. 3b, appendix). `fig4b_tests` no longer exists: update
every reference in paper.tex and appendix.tex (the appendix figure `fig:gate-tests` becomes the main Figure 4; the
appendix gets `figA_closeness` and `figA_fm_entry` with captions). Figure captions use the new labels and plain words;
keep "uses no acceptance data" (one phrase, used consistently) where true.

## 6. Appendix edits

- App D (every test): add the mapping table code → main-text name → label; add the Holm-across-secondaries values
  (0.018, 0.025, 0.025, 0.051, 0.062, 0.22 for topic-edge slope, D0, same-author closeness, insider, Emerging
  keywords, P7); note A1 and PH6 demoted to exploratory in the main text; add PH7 branded-title rows (discovery and
  held-out, D1–D4 variants from `research/fashion/output_pooled/posthoc/ph5_titles/tests.csv`, all numbers ×100 = pp).
- Add a short subsection or table "What the newcomer reversal is made of" (profiles table from RESULTS.md, incl. era
  rows).
- App F (other gate modules): fix "may be explained half or more by co-author composition" as in §6 above.
- App G (title style): now backed by committed outputs. Replace the E*/D* framing: shares table from
  `output_pooled/posthoc/ph5_titles/shares.csv` (discovery rows; the numbers match the current table to within a few
  hundredths except the n column, which becomes the 43,480-paper corpus counts: 384, 770, 1,248, 2,070, 2,360, 2,649,
  3,872, 5,765, 8,951, 15,411); add the PH7 test table (controls and raw models, both splits, D1–D4) and the timing
  rows; delete "ratio 1.02" and "not re-run".
- App C (hindsight): add the record pointers for Tables 7 and 8 (hindsight_check.json; ph5_forecast/summary.json).
- App A: say "8,185 decided held-out papers from 2018–2026" where the main text uses 8,185.
- Keep everything else; fix cross-references.

## 7. Citations

Already in references.bib and should now be cited: `koch2021reduced` (benchmark concentration in ML: herding at the
dataset level; cite in §2 or §5). Consider adding (verify each by web search — authors, title, venue, year, pages —
before adding; drop any you cannot verify; at most 6 new entries): Crane 1969 "Fashion in science: does it exist?"
(Social Problems); Tomkins, Zhang & Heavlin 2017 PNAS on single- vs double-blind review; Cortes & Lawrence 2021 and/or
Beygelzimer et al. 2023 on NeurIPS review consistency (supports "edges regress"); Coleman, Katz & Menzel 1957 (network
diffusion); one LLM-annotation validity reference (Gilardi et al. 2023 PNAS or Ziems et al. 2024 Computational
Linguistics). Do not cite anything for a claim it does not make.

## 8. Acceptance checks (run them and report)

- Compiles with 0 undefined references/citations and 0 overfull boxes (> 1pt) in main text; bibtex 0 warnings.
- Conclusion ends on page 8; body 3,000–4,000 words (report the wc_body.py output); abstract ≤ 200.
- `grep` the main text (before \appendix) for: H1d|H2|H3|P1b|E1|E4|PH[0-9]|A1|D0|\\Hok|\\Hno|\\Tok|D\^\*|E\^\*|1\.02|
  half or more|penali|reward(s|ed)? (as a verb)|pays|first to|prove — none should remain (except "rewarded imitation"
  as a theory name and "reward" in quoted theory names).
- Every number in the main text appears in paper_v1.tex, RESULTS.md, or the committed outputs named above.
- Render pages 1–9 to PNG (pdftoppm -r 70) and look at them: no float overlaps, tables readable, figures legible.
