# Title-writing guide: which title choices go with more citations?

**Scope.** 8,602 accepted ICLR papers from 2017–2025 (discovery split), so venue and decision are held fixed. The outcome is Semantic Scholar citations as of 2026-10-17.

**Model.** The pre-registered primary is `log(1+cites) ~ feature + team size + abstract length + 20 abstract-embedding PCs | year × topic`. Holm correction runs over the 8 tests (`docs/CITES_PREREG.md`).

**Reading.** Every statement is observational: papers whose titles do X receive Y% more citations on average than accepted papers with similar content. None shows that retitling a paper would change its citations.

Figure: `fig_title_guide.png`. Numbers: `joint_results.json` and `G*/RESULTS.md`.

| Title choice | Primary % [95% CI] | Matched pairs: raw R1 / calibrated† | Holm p | Verdict | Audit confidence |
|---|---|---|---|---|---|
| G1 Leads with a method name ("NAME: …") | **+22.5** [+13.5, +32.1] | +8.4 / +31 [+19, +44] | 2.6e-5 | **more citations** | sign high, size medium |
| G2 States the finding (assertive verb) | +26.1 [+7.5, +47.8] | −6.5 / +16 [−3, +39] | 0.038 | inconclusive | medium |
| G3 Is a question | +14.3 [−2.8, +34.5] | −3.7 / +23 [−4, +57] | 0.35 | inconclusive | high (no advice) |
| G4 LLM-favoured words (enhancing, leveraging, …) | −9.0 [−20.7, +4.3] | −30.5 / −12 [−29, +8] | 0.36 | inconclusive | high (no advice) |
| G5a Length, per +5 words | −5.5 [−11.3, +0.7] | −23.0 / −8 [−16, +2]‡ | 0.35 | inconclusive | high (no reliable link) |
| G5b Closer in meaning to the abstract, per SD | **+8.0** [+5.0, +11.1] | +4.4 / +26 [+14, +39]‡ | 1.8e-5 | **more citations** | sign high, size medium |
| G6a Meme template (All You Need, …) | +37.9 [+2.9, +84.8] | +18.0 / +51 [+2, +124] | 0.18 | inconclusive | low–medium |
| G6b Tentative framing (Towards, Rethinking, …) | +3.7 [−7.8, +16.7] | −13.1 / +12 [−5, +31] | 0.54 | inconclusive | medium |

**† Calibrated matched pairs.** Raw R1 is pre-registered and feeds the verdict rule. Under the null it runs 17–22% low, because nearest-neighbour matching picks well-cited "hub" papers as controls. The calibrated value removes that placebo shift. It is a diagnostic (not pre-registered): computed at integration for G1–G2 and taken from the audits for the others.

**‡ Length and similarity.** These pairs compare the top with the bottom within-year tercile: 1.15 units for length, 2.06 SD for similarity.

## Advice by question

- **G1, naming the method.** If you contribute a reusable method, a named title is the style most consistently linked to more citations: about +22%, with a plausible range of +15% to +30%.
  - *Caveat:* teams that expect reuse or promote their work may both name it and attract citations.
  - The gap is +15% without each year's top 5% most-cited papers.
- **G2, stating the finding.** No recommendation.
  - *Caveat:* without the top 5%, the estimate is +11% [−3, +27].
  - Raw pairs have the opposite sign.
  - The rule misses about half of claim titles.
- **G3, question titles.** No advice either way.
  - *Caveat:* only 223 papers, and the estimate leans on a few hits. Dropping the 10 most-cited question titles gives +2%.
- **G4, LLM-favoured words.** The data neither establish nor rule out a modest shortfall.
  - *Caveat:* 81% of these papers are from 2024–25.
  - With an arXiv-id control the estimate is −3%.
  - Neutral "improving X" synonyms show −6%, so the vocabulary cannot be separated from the framing.
- **G5a, length.** Write the length the content needs. Length has no reliable association with citations.
  - *Caveat:* the small negative estimate is partly an S2 split-record artefact. It is −0.2% with an arXiv-id control.
- **G5b, saying what the paper does.** Titles closer in meaning to their abstracts receive about 8% more citations per SD (+3% to +9% across measures).
  - *Caveat:* the size depends on the embedding model (MiniLM +4%), and the measure partly captures topic vocabulary.
- **G6a, meme templates.** No reliable citation reason to adopt or avoid them.
  - *Caveat:* 83 papers, and PatchTST alone holds 38% of their citations.
  - The CI includes 0 with a G2 control: half of these titles are also assertive.
- **G6b, tentative framings.** No clear difference, but up to +17% is not ruled out.

**Pre-specified joint analyses** (`src/cites/joint.py`; no multiplicity claim).
- **All 8 features in one model.**
  - G1, G4, G5b and G6b move by at most 3.5 points, and G6a falls to +31%.
  - G2 (+34%), G3 (+27%) and G5a (−11%) move away from zero, because their reference becomes plain titles.
- **LLM-topic papers.** No feature's association differs between LLM-topic papers and the rest (interaction p 0.15–0.76).

## Reviewers vs readers

**Reviewers.** Title features do not predict acceptance once camera-ready edits are accounted for: 0 of 18 auditable features pass the Holm gate (`outputs/SUMMARY.md`, finding 7). Named titles are neutral: accepted/all ratio 1.02, editing-corrected 90% CI 0.949–1.031.

**Acceptance odds ratios before the audit** (`outputs/acceptance/feature_associations.csv`; decided papers; adjusted for year, team size and topic) are small:
- NAME 1.05 [0.99, 1.11];
- question 1.05 [0.92, 1.20];
- "Towards" 1.02 [0.88, 1.18];
- long titles 0.91 [0.83, 1.00].

**The exception is R24 words (G4).** Desk rejection and withdrawal deplete them before the decision (0.90 [0.87, 0.93], finding 9). Accepted G4 papers are therefore a filtered group.

**The contrast.** Reviewers are neutral to the NAME style, yet it is the style most consistently linked to readers' citations.

**Not audited.** Meme templates, tentative framings, assertive titles and title–abstract similarity were not in the acceptance audit.

## What this does and does not show

**It shows** how citations differ by title style among accepted ICLR papers with similar abstracts, topic, year, team size and abstract length. Two associations pass the pre-registered rule: method names and title–abstract similarity.

**It does not show causation.** Better or better-promoted work may select into some styles: reusable methods get names, and benchmark papers ask questions.
- **Checks run.** Diagnostics covered preprint timing, code links, paper type, split records, prior team success and retitling. They reduce this concern but do not remove it.
- **Checks not run.** Lab reputation and social-media promotion are untested.

**Limits.**
- Accepted ICLR papers only.
- One S2 snapshot, so 2024–25 papers have only 1–2 years of citations.
- Uncorrected secondary analyses, and post-hoc diagnostics.
- No held-out confirmation yet.
