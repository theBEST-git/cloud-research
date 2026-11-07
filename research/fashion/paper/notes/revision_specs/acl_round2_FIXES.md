# Fix round 2 (decided; implement all)

Two independent reviews of your draft found no wrong number and no wrong label. These are the accepted precision
fixes. Line numbers refer to your current paper.tex / appendix.tex. Keep the body within 3,000–4,000 words and the
Conclusion on page 8; items in group E free words for the rest.

## A. Nulls and populations stated too strongly (main text and Table 4)
1. Contributions bullet 2 (≈ l. 122): "On every decided submission under double-blind review, acceptance goes with..."
   → "Using every decided submission under double-blind review, rejected ones included, acceptance goes with closeness
   to the team's own record among teams that have one (far jump −5.4 pp, held-out −6.1; HELD-OUT SUPPORTED), not
   detectably with the crowd." Also l. ≈497 "for every submission" → "for every decided submission".
2. Branded titles read as absence: §1 ¶4 "the branded title's small premium was not confirmed" → "the branded title's
   small premium lies below what the held-out test could detect"; Table 4 → "branded titles: small premium, held-out
   uninformative (EXPLORATORY)"; §7 (≈ l. 543) "does not rule out bandwagons that bring no premium; the spread of
   branded titles may be one" → "...the spread of branded titles may be one, or it may carry a small premium; the
   held-out test cannot tell."
3. §6 (≈ l. 475) "The field's record does not replicate." → "The field's record is undetermined (uninformative)."
4. FM adoption slope (≈ l. 411) "late adopters fare as early ones do" → "no detectable difference between late and
   early adopters"; Table 4 "FM premium not fading" → "no detectable change in the FM premium".
5. Division-of-labour takeaways: §5 opening "benchmark and evaluation work stays with incumbents and larger teams" →
   "while, in the FM era, benchmark and evaluation work sits with larger teams and topic incumbents"; Conclusion
   likewise ("and, in the FM era, benchmark and evaluation work sits with incumbents and larger teams").
6. "Much of the measurement gap is team size" (≈ l. 306) and "For first-time teams it is team size" (≈ l. 346) →
   "is accounted for by team size" (statistical sense).
7. (≈ l. 372) "these measures show that newcomers do not follow" → "these measures give no sign that newcomers follow".
8. §5 "goes with entering a topic, not with being new to ICLR or with small teams" → "goes mainly with entering a
   topic, ...".
9. §6 timing: "acceptance falls after a keyword's share peaks" → "acceptance may fall after ...".

## B. Framework consistency
10. Topic edges are "past acceptance" = imitation's outcome reference point. Table 3: record-group header → "The
    team's own record" (drop "a topic's"), topic-edge row stays in the other group. §7 "Every association that
    replicated at the gate is referenced to a record" → "Every association that replicated at the gate is referenced to
    the team's own record, except persisting topic edges, which fit imitation of past acceptance and a rival (regression
    to the mean in noisy review) alike."
11. Table 4 Imitation/Entry cell: delete "later onto FMs" (it does not discriminate; keep it only in the Continuity
    cell with the diffusion caveat).
12. Table 3 note b on "Emerging − Mainstream keyword": keyword popularity (a 23-keyword grid) was explored before
    registration; the discovery estimate IS a declared post hoc test (Holm 0.020 within discovery). Reword note b for
    that row: "Keyword popularity had been explored against acceptance before registration; the discovery estimate is a
    declared post hoc test on a dimension already seen." Keep "not a test" only for branded titles.

## C. Accuracy of protocol statements
13. Holm across the six secondary held-out tests: recompute from the exact one-sided p in
    /home/user/cloud-research/research/fashion/output_pooled/confirmation_run/ph5/tests.csv (0.003084, 0.005125,
    0.006184, 0.017427, 0.031489, 0.21699) → 0.019 (topic edge), 0.026 (edge prediction D0), 0.026 (same-author
    closeness), 0.052 (insider), 0.063 (Emerging keywords), 0.22 (P7). Update Table 3 note, §6 text ("Holm 0.052"),
    appendix (codes table caption, tests appendix, tab:app-main caption). Survivors unchanged. Also update
    REVISION-era statements elsewhere if any.
14. Declared held-out tests: the general protocol sentence (≈ l. 235) and Fig. 4 caption (≈ l. 487) say post hoc tests
    were declared "before the held-out data were read". Untrue for PH6 (declared 2026-10-28) and PH7 (2026-11-04),
    which were declared after the registered held-out run had read held-out outcomes for other questions. Use: "declared
    before any held-out estimate for that question was computed". For the branded-title row in Fig. 4's caption: title
    style was explored before registration (not found post hoc in discovery). Same fix in the appendix codes-table
    group heading (≈ appendix l. 393).
15. Code links (≈ l. 227): "the distance-based gate estimates hold without them" → "in discovery, the distance-based
    gate estimates hold without them (no link-removed text exists for held-out papers)".
16. Same-author closeness simulation (≈ l. 464): "though a confounder in co-author quality could also produce it, as a
    simulation in its declaration showed" → "though a confounder in co-author quality could also bias it: in a
    simulation reported in its declaration, such a confounder moved the estimate". Appendix (≈ l. 1012) same.
17. Twins: the −3.86 [−4.98, −2.74] estimate comes from a model with first_time nested in newcomer, so it compares
    returning topic newcomers with incumbents. Text (≈ l. 368) and Fig. 3 caption (row 3): say "papers by topic newcomers
    with an ICLR record are less likely than incumbent papers to have a same-year twin (with first-time teams
    controlled separately)". Do not add a first-time number.
18. H1e (≈ l. 286 and appendix codes table): "inconclusive" → "not supported (inconclusive)".
19. Profiles CIs from the CSV (not the double-rounded json): +0.09 [−0.63, +0.80]; −0.81 [−1.46, −0.16]; +5.02 [+3.12,
    +6.91]. Fix in main text and appendix tables.
20. Fig. 4 caption legend: add "not supported: a declared test without a registered MDE80" for the same-author
    distance row.
21. Label definition (§1): "REPLICATED (registered before outcomes were read and supported again on held-out papers)"
    → "REPLICATED (from a registered test, supported again on held-out papers)" (the entry reversal was registered as a
    reversed hypothesis after discovery).
22. Table 2 team-size row: label column "registered variant" (it is the registered supplementary variant S1), not
    EXPLORATORY.
23. §3 Corpus: "8,185 decided held-out papers" → "8,185 decided held-out papers from 2018–2026".

## D. Small wording
24. Abstract: "propose new methods more often" → "propose methods more often"; "Where the routes part, we detect no
    herding." → "Where the routes part, no herding is detectable."
25. §1 ¶4: "no crowd premium is detectable" → "no premium for crowded topics is detectable".
26. Bullet 3: drop "only" in "depending only on the years ...".
27. §2: "benchmark use concentrates on ever fewer datasets" → "benchmark use concentrates on a small set of datasets,
    increasingly so".
28. §6 units: gloss once: "per log unit (natural log of one plus the topic's earlier papers)" and "per logit unit
    (log-odds of the topic's prior FM adoption)".
29. Fig. 2: the inset no longer shows a code (figure regenerated: "Registered test, prior FM adoption 0→100%"). Remove
    the caption's "its code and tier refer to Appendix D" and label it REPLICATED in the caption instead.

## E. De-densify (frees ~120–150 words)
30. §5 "Entering a topic, not ICLR": move the per-era numbers to Appendix E (keep one sentence in the main text: the
    method surplus is present in every era, so it predates the FM wave; the measurement gap appears only in 2024–2026,
    with its one number −2.75 [−4.07, −1.44]).
31. §6 timing: keep one sentence with the held-out numbers only (Emerging +3.25 [−0.18, +6.69]; after-peak −5.2
    [−11.1, +0.7], −1.7 without the six inspected keywords); details in Appendix D.
32. §7: cut the Weisberg sentence ("appears here as continuity") that precedes "But the record-side gate results do not
    single out continuity". Keep the Pramanick parallel.

## F. Keep as is
- The hand-check sentence and its `% TODO(author)` comment (the author will supply the numbers).
- The title.

After editing: rebuild, rerun the acceptance checks (0 overfull, 0 undefined, Conclusion on p. 8, body 3,000–4,000,
abstract ≤ 200, grep list), render pages 1–9 and look. Report the wc output, page count, and anything you could not do.
