# Title-writing guide: which title choices go with more citations?

**Sample.** 8,602 accepted ICLR papers from 2017–2025, in the discovery split. Venue and decision are held fixed.

**Outcome.** Semantic Scholar citations as of 2026-10-17.

**Model.** The pre-registered primary is `log(1+cites) ~ feature + team size + abstract length + 20 abstract-embedding PCs | year × topic`, with Holm correction over the 8 tests (`docs/CITES_PREREG.md`).

**Reading.** Every statement below is an association: papers whose titles do X receive Y% more citations on average than accepted papers with similar content. None of them shows that changing a title would change its citations.

Figure: `fig_title_guide.png`. Numbers: `joint_results.json` and `G*/RESULTS.md`.

| Title choice | Primary % [95% CI] | Matched pairs: raw R1 / calibrated† | Holm p | Verdict | Audit confidence |
|---|---|---|---|---|---|
| G1 Leads with a method name ("NAME: …") | **+22.5** [+13.5, +32.1] | +8.4 / +31 [+19, +44] | 2.6e-5 | **more citations** | sign high, size medium |
| G2 States the finding (assertive verb) | +26.1 [+7.5, +47.8] | −6.5 / +17 [−3, +39] | 0.038 | inconclusive | medium |
| G3 Is a question | +14.3 [−2.8, +34.5] | −3.7 / +23 [−4, +57] | 0.35 | inconclusive | high (no advice) |
| G4 LLM-favoured words (enhancing, leveraging, …) | −9.0 [−20.7, +4.3] | −30.5 / −12 [−29, +8] | 0.36 | inconclusive | high (no advice) |
| G5a Length, per +5 words | −5.5 [−11.3, +0.7] | −23.0 / −8 [−16, +2]‡ | 0.35 | inconclusive | high (no reliable link) |
| G5b Closer in meaning to the abstract, per SD | **+8.0** [+5.0, +11.1] | +4.4 / +26 [+14, +39]‡ | 1.8e-5 | **more citations** | sign high, size medium |
| G6a Meme template (All You Need, …) | +37.9 [+2.9, +84.8] | +18.0 / +51 [+2, +124] | 0.18 | inconclusive | low–medium |
| G6b Tentative framing (Towards, Rethinking, …) | +3.7 [−7.8, +16.7] | −13.1 / +12 [−5, +31] | 0.54 | inconclusive | medium |

**† Raw vs calibrated matched pairs.** The pre-registered R1 is the raw value, and it feeds the verdict rule. Under the null, the R1 procedure runs about 17–22% low: nearest-neighbour matching picks "hub" papers as controls, and hubs are cited more. The calibrated value removes that placebo shift. It is a diagnostic (not pre-registered). For G1 and G2 it was computed at integration; for the others it comes from the audits.

**‡ Length and similarity rows.** Matched pairs compare the top with the bottom within-year tercile: 1.15 units for length and 2.06 SD for similarity. The figure rescales them to the primary's units.

## Advice by question

**G1: naming the method.**
- **Advice.** If the paper contributes a reusable method, a named title is the style most consistently linked to more citations. Named-title papers receive about 22% more citations; a plausible range is +15% to +30%.
- **Main caveat.** Teams that expect reuse, or that release code and promote their work, may both name the method and attract citations. Part of the gap sits in the top tail: without each year's top 5% most-cited papers it is +15%. The earlier low end of +5–8% came from raw matched pairs.

**G2: stating the finding.**
- **Advice.** No recommendation for or against.
- **Main caveat.** The regression association (+26%) halves without the top 5% (+11% [−3, +27]), and raw matched pairs have the opposite sign. The rule detects only about half of claim titles.

**G3: question titles.**
- **Advice.** No advice either way.
- **Main caveat.** There are only 223 question titles, 39% of them from 2025. The estimate leans on a few hits (GIN, SWE-bench): dropping the 10 most-cited question titles gives +2%.

**G4: LLM-favoured words.**
- **Advice.** The data neither establish nor rule out a modest shortfall.
- **Main caveat.**
  - 81% of these papers are from 2024–25, with short citation windows.
  - With an arXiv-id control the estimate is −3%.
  - It cannot be separated from neutral "improving X" framing: those synonyms show −6%.
  - The leverag\* and boost\* families (about −30%) are untested hypotheses.

**G5a: length.**
- **Advice.** Write the length the content needs; no reliable association with citations.
- **Main caveat.** Part of the small negative estimate is an S2 split-record artefact: longer titles are retitled more often, and retitled papers lose citations to a separate record. With an arXiv-id control it is −0.2%.

**G5b: say what the paper does.**
- **Advice.** Titles closer in meaning to their abstracts go with more citations: about 8% per SD, with a range of +3% to +9% across measures.
- **Main caveat.** The size depends on the embedding model (MiniLM gives +4%). The measure partly captures topic vocabulary and names the title shares with the abstract.

**G6a: meme templates.**
- **Advice.** No reliable citation reason to adopt or avoid them.
- **Main caveat.** There are 83 papers. PatchTST alone holds 38% of their citations. Half of these titles are also assertive (G2), and the CI includes 0 once G2 is controlled for or richer content controls are used.

**G6b: tentative framings.**
- **Advice.** No clear difference.
- **Main caveat.** "Inconclusive" here does not mean null: up to +17% is not ruled out. "Rethinking" (+33%) is an uncorrected subgroup hypothesis.

**Pre-specified joint analyses** (prereg §6; no multiplicity claim; `src/cites/joint.py`).
- **All 8 features in one model.**
  - G1, G4, G5b and G6 stay near their primaries.
  - G2 (+34%), G3 (+27%) and G5a (−11%) move away from zero, because their reference group becomes plain titles.
- **LLM-topic papers.** No feature's association differs between LLM-topic papers and the rest (interaction p 0.15–0.76).

## Reviewers vs readers

- **Reviewer side** (`outputs/SUMMARY.md`): no title feature predicts acceptance once camera-ready edits are accounted for.
  - 0 of 18 auditable features pass the Holm gate on 1,311 pre-decision arXiv pairs (finding 7).
  - Named titles are neutral: accepted/all ratio 1.02, editing-corrected 90% CI 0.949–1.031 (finding 2).
- **Raw acceptance odds ratios** (`outputs/acceptance/feature_associations.csv`) are small:
  - NAME 1.05 [0.99, 1.11];
  - question 1.05 [0.92, 1.20];
  - "Towards" 1.02 [0.88, 1.18];
  - long titles (≥13 words) 0.91 [0.83, 1.00].
- **The exception is the R24 words (G4).** Desk rejection and withdrawal deplete them before the decision: pre-decision ratio 0.90 [0.87, 0.93] (finding 9). Accepted G4 papers are therefore a filtered group.
- **The contrast.** The NAME style, to which reviewers are neutral, is the one most consistently linked to readers' citations. Title style shows no identified association with acceptance, but some styles do go with citations after publication.
- **Not covered by the acceptance audit.** Meme templates, tentative framings, assertive titles and title–abstract similarity were not in it, so selection at acceptance on those styles is not directly ruled out.

## What this does and does not show

**It shows** how citation counts differ across title styles among accepted ICLR papers with similar abstracts, topic, year, team size and abstract length. Two associations pass the pre-registered rule: method names and title–abstract similarity.

**It does not show that a title causes citations.** Better or better-promoted work may select into some styles:
- reusable methods get names;
- analysis and benchmark papers ask questions.

Content controls, matched pairs and diagnostics reduce this concern but do not remove it. The diagnostics covered preprint timing, code links, paper type, split records, prior team success and retitling. Lab reputation and social-media promotion are untested.

**Limits.**
- **Scope.** Accepted ICLR papers only. Rejected papers and other venues are not covered.
- **Citation data.** Citations come from one S2 snapshot. Papers from 2024–25 have only 1–2 years of citations. Split S2 records add noise.
- **Multiplicity.** Secondary analyses and diagnostics are uncorrected. The calibrated matched pairs were added after the outcomes were seen.
- **Confirmation.** No held-out confirmation has been run yet.
