# Blueprint: the final paper (ACL ARR long paper)

Built 2026-11-03 by the lead author from the four story proposals (P1-P4), the three judgements (J1-J3), the two
dossiers, landscape.md, verify_prior.md, theory_anchors.md and `output/novelty_newcomer.json`. This is the single
document the writer follows. It replaces `research/fashion/paper/riding_the_wave_paper.tex` entirely: its framing, its
RQ1-RQ3 structure, its findings table and its author block are not reused.

No outcome or decision column of a data file was read for this blueprint, and no forbidden script was run. No corpus
author is named. Numbers come from the dossiers or from committed result files read directly (listed in Section 0.3).
`analysis_novelty.md` was never written (the novelty agent was refused); its numbers are in `output/novelty_newcomer.json`.

---

## 0. Decision record, conventions and sources

### 0.1 The decision

**Story line: P1, "imitation versus continuity", with P4's measurement discipline and ACL packaging, P2's
record-holder rows and P3's audit and hook.**

- **Why P1's spine.** J2 and J3 ranked P1 first; J1 ranked P4 first and P1 second. J3 (the supervisor's view) broke a
  tie with P4 on the first criterion: P1 is one falsifiable claim, while P4's thesis is three claims held together by
  a design principle. P1 is also the only line that says something about how science changes and what it rewards.
- **Where J1 is honoured.** J1's main objection to P1 is that a tier-B result carries the title. The title is
  therefore a question ("Herded or Anchored?"), no B-tier result is asserted in the title, and the memorable line is
  hedged ("the conformity we can detect"). J1's fixes to P4 are applied here too: no cross-split size comparison,
  corrected prediction labels, exact F_max definition, "far from the team's earlier work" instead of "staying near",
  "having a topic insider on the team", "detected no herding".
- **Grafts taken.**
  - From P4: per-row information codes (P / H✓ / H✗ / R / T✓); the ACL conversation on computational histories and
    temporal leakage; the mechanistic sentence for 29 vs 8; "tested again" rather than "replicated" for the whole
    set; the closing scope clause; PH6 flagged as retrospective; the ethics statement; the Stelmakh pairing.
  - From P2: returning topic newcomers take up foundation models at the incumbents' rate while first-time teams lag
    ("the package travels with an ICLR record"); H1e as the limit of the package claim; the cumulative FM share
    against the keywords that rose and fell; the era sentence for the content gap; P2's verb guardrails.
  - From P3: "We expected a herd too" as the hook; an honest-denominator list of the post hoc patterns that did not
    hold; the Figure 1 caption admitting the keywords were chosen after their curves were known; "growth compounds
    hindsight" as one clause.
  - From J2 and J3: define continuity as the *position of a paper's content relative to a record*, name cumulative
    advantage and visible status as rivals, lead the gate evidence with E4 and E1, put the insider last as the result
    a status reading explains equally well; print MDE80 or power next to every replication verdict; producer-side
    convergent evidence (Zeng et al.; Packalen and Bhattacharya) so that "entrants bring new things" is not claimed as
    new; pre-empt the diversity-innovation-paradox reading.
- **Grafts rejected.** P4's "reading backwards / forwards" vocabulary (it collides with "points backward, to a
  record"); P4's §7.3 size comparison across splits; P3's "shrink, fail or reverse", "differential survival",
  "foresight finds a record" and the top-tenth retention row; P2's "Not a Herd", "tools, not people", the FM-twin row
  (fixed effects undocumented) and the FM premium as a section claim; the content-distance result in the abstract.
- **Content-distance result.** It stays in the body as tier E support, worded "farther from earlier ICLR work, partly
  by construction". All three judges asked for an outcome-free decomposition (own authors' earlier submissions removed
  from the reference set) before it can carry more weight. That check was not part of this step; Section H gives the
  wording for either outcome. Nothing in the blueprint depends on it.

### 0.2 Evidence tiers (use exactly these)

| Tier | Meaning | What the text may say |
|---|---|---|
| A | Registered before the discovery run (or before any held-out data) and supported on held-out papers | "replicated"; direction, not size |
| B | Post hoc in discovery (declared before it was run), then a held-out test declared before the held-out run supported it | "post hoc, supported on held-out papers"; never "replicated" |
| C | Registered, but inconclusive, not supported or not replicated | "not confirmed" / "uninformative" (if below MDE80) |
| D | Discovery only (exploratory or post hoc) | "discovery only" |
| E | Descriptive, no acceptance outcome | plain description |
| E\* / D\* | Earlier exploratory title analysis: E\* share re-verified; D\* acceptance ratio not re-run | "earlier exploratory" |

In the paper, the tier letter follows the interval in parentheses: "−6.09 pp [−9.32, −2.86] (B)".

### 0.3 Source pointers used below

| Pointer | File |
|---|---|
| `DC:n` / `DP:n` | `paper_ws/dossier_core.md` / `paper_ws/dossier_posthoc.md`, line n |
| `NN:key` | `paper_ws/output/novelty_newcomer.json`, `results.key` (workspace file, outcome-free, not committed) |
| `FE` | `research/fashion/output/posthoc/ph5_fmwave/free_entry.csv` (read directly; outcome-free) |
| `FH` | `research/fashion/output/posthoc/ph5_position/free_herding.csv` (read directly; outcome-free) |
| `FPS` | `research/fashion/output/posthoc/ph5_kwtiming/free_profile_states.csv` (read directly; outcome-free) |
| `FTS` | `research/fashion/output/posthoc/ph5_position/free_twin_share.csv` (read directly; outcome-free) |
| `HC` | `research/topics/output/hindsight_check.json` (read directly) |
| `LAB` | `research/topics/output/paper_contributions.csv.gz`, yearly shares recomputed for this blueprint (outcome-free labels) |
| `QT` | `research/fashion/output/posthoc/ph5_pivot/quintiles.csv` (committed result) |
| `CONF` | `research/fashion/output_pooled/confirmation_run/ph5/tests.csv` (committed result) |
| `FIG1` | the peaks annotated on `research/fashion/paper/figs/fig1_waves.png` (discovery corpus) |
| `PRE:n` | `research/fashion/PREREGISTRATION.md`, line n (definitions only) |
| `VP:n` / `TA:n` | `paper_ws/verify_prior.md` / `paper_ws/theory_anchors.md`, line n |

Values first read from FE, FH, FPS and FTS for this blueprint (all match the judges' independent reads):
- FE, first-time team vs returning topic newcomer, FM paper, by prior-adoption bin: 0-5% −0.95 [−2.03, +0.13]
  (p 0.084); 5-15% −4.58 [−6.55, −2.60]; 15-30% −8.96 [−13.30, −4.63]; 30-50% −14.71 [−19.82, −9.61]; ≥50% −1.96
  [−4.60, +0.68] (p 0.14); n 33,993 submissions 2023-26, 100 clusters.
- FE, returning topic newcomer vs incumbent, same bins: +1.10 [−0.05, +2.24] (p 0.060); −0.41 [−2.77, +1.95] (p 0.73);
  −2.58 [−5.77, +0.61] (p 0.11); +2.87 [−2.74, +8.48] (p 0.31); −1.01 [−2.21, +0.19] (p 0.097).
- FH (model `any_twin ~ first_time + newcomer + class + FM + log2 team` within topic × year, CR1 by topic; PRE:1542;
  first_time nested in newcomer): newcomer paper → has an independent same-year twin −3.86 [−4.98, −2.74] (n 42,325);
  first-time team a further −0.32 [−1.64, +1.00] (p 0.63); first-time teams are 26.3% of RQ2 papers (`mean`).
- FPS: first-time vs returning teams, Emerging (young × rising) keyword use −3.74 [−5.14, −2.35] (16.7% vs 25.0%;
  q 5.9e-6; 26,640 papers); Cooling +2.40 [+1.45, +3.36]; Mainstream +2.30 [+0.92, +3.68].
- FTS (`all` rows): twins per paper 0.4006 (2019, 1,248 papers) and 2.9356 (2026, 15,411 papers), so twins per paper
  per 1,000 submissions 0.321 → 0.190; any-twin share 19.5% → 48.8%.
- LAB (43,480 papers): FM share 0.3, 0.0, 0.5, 3.3, 4.2, 5.4, 10.6, 26.7, 42.3, 54.4% (2017-2026); new-architecture
  share 24.5 → 7.5%; measurement (dataset/benchmark + evaluation) share 2.6 → 11.1%. Matches DC:163-170.
- HC: middle-era map = 2021-23 papers (`papers_by_era`: early 4,472; middle 8,881; late 30,127).

---

## A. Title, thesis, memorable line and abstract

### A.1 Title

**Herded or Anchored? Conformity at ICLR during the Foundation-Model Wave**

Alternatives (in order): "Anchored, Not Herded: Conformity at ICLR during the Foundation-Model Wave" (only if the
supervisor wants an assertive title; it puts a B-tier claim in the title); "Waves without Herds? Entry, Continuity
and Review at ICLR, 2017–2026".

"Anchored" appears in the title and in exactly one defined use in §1, with the footnote in G.1. The technical term in
the body is **continuity**.

### A.2 Thesis (one sentence)

> At ICLR during the foundation-model wave, the field converged on a shared technical package, but the conformity we
> can detect is continuity rather than imitation: topic newcomers, whom the herding account casts as imitators, write
> method proposals rather than the follow-on measurement work it predicts, and acceptance goes not with following the
> crowd but with a paper's position relative to a record, lower far from the team's earlier work and higher with a
> topic insider on the team.

### A.3 Memorable line (closes the abstract, §1 and §8)

> **At ICLR, the conformity we can detect points to a record, not to the crowd.**

Plain-language gloss for §1 (once): "anchored to a record, not herded by the crowd".

### A.4 Abstract (199 words, counted with `wc -w`; ready to use; en dashes in year ranges)

> Machine learning is often said to herd: researchers chase what is hot, and review rewards it. We test this account
> on 43,480 ICLR submissions (2017–2026), rejected and withdrawn papers included, with hypotheses registered before
> outcomes were read and tested again on 11,099 held-out papers. We separate two routes to conformity: imitation
> takes its cue from what others do now, continuity from an accumulated record. The field converged: topics where
> more previous-year papers built on foundation models had fewer papers proposing new architectures. Yet hindsight
> inflates the waves: on the same papers, a topic map fitted on all years finds 29 emerging topics, one fitted on
> 2017–2020 only 8. Among topic newcomers, where imitation theory expects herding most, our registered prediction
> failed in the opposite direction: their papers are more often method proposals and less often benchmark, dataset or
> evaluation papers, and the reversal replicated. Review shows no detectable premium for following the crowd. In post
> hoc tests supported on held-out papers, acceptance is instead lower far from the team's earlier work and higher with
> a topic insider on the team. At ICLR, the conformity we can detect points to a record, not to the crowd. All
> findings are associations.

| Claim in the abstract | Source | Tier |
|---|---|---|
| 43,480 submissions, rejected and withdrawn included | DC:65-66 | E |
| 11,099 held-out papers | DC:72 | E |
| Prior FM adoption with fewer new-architecture papers | DC:271, 364 | A |
| 29 vs 8 emerging topics, same papers | DC:176-179; HC | E |
| Newcomers: more method, fewer benchmark/dataset/evaluation papers; reversal replicated | DC:296-297, 365-366 | A (reversed) |
| No detectable premium for following | DC:324, 367 (crowding, C); DC:376 (edges regress, B); DP:133 (titles, D\*) | C / B / D\* |
| Far from own earlier work: lower; topic insider: higher | DC:370, 374 | B |

"Tested again" (not "replicated") covers the whole set because H3a was registered and not replicated.

---

## B. Positioning

### B.1 The conversations (primary first)

1. **Herding, fashion and bandwagons, and ML's self-critique.** The default reading of ML's waves is a herd
   (`lipton2019troubling`, `hooker2021hardware`, `dehghani2021benchmark`, `bommasani2021opportunities`), with entrants
   flooding new LLM work (`movva2024topics`); fashion and cascade theory says how (`abrahamson1991managerial`,
   `bikhchandani1992theory`, `banerjee1992simple`). *What we add:* the account's sharpest predictions, tested where
   they are sharpest (entrants, the review decision) with registered and held-out tests rather than essays or trends.
2. **Tradition, novelty, entry and their reward (science of science).** Producers lean conservative
   (`foster2015tradition`); pivots cost citations and publication (`hill2025pivot`); chaperones help newcomers
   (`sekara2018chaperone`); fresh teams and young researchers bring new ideas (`zeng2021fresh`, `packalen2019age`);
   whether gatekeepers penalise novelty is contested (`boudreau2016looking`, `teplitskiy2022is`, `li2017expertise`).
   *What we add:* producers and the gate observed in one complete submission population; the separation of imitation
   from continuity by reference point (`weisberg2009epistemic` is the formal precedent; `weisberg2013modeling` blends
   them); the gate's associations that hold point to a record.
3. **Computational histories of NLP and ML (ACL-native).** One topic model fitted on the whole archive, read forward
   in time (`hall2008studying`, `anderson2012towards`, `pramanick2023diachronic`, `schafermeier2021topic`,
   `klinger2020narrowing`, `grootendorst2022bertopic`). *What we add:* the size of the hindsight effect on the same
   papers with the same model, which trend claims survive it, and per-claim codes for prospective measurement.
4. **Supporting (design and rival readings, not novelty):** peer review at ICLR (`tran2020open`, `ibrahim2026bias`,
   `jung2025what`, `wang2023what`, `xu2026reviewer`, `stelmakh2023large`, `kargaran2025insights`) and confirmatory
   meta-research (`nosek2018preregistration`, `vandenakker2021preregistration`).

### B.2 The gap

- **Theory gap.** Imitation and continuity have old, separate roots (imitation: `dimaggio1983iron`,
  `haunschild1997modes`, `scharfstein1990herd`, `abrahamson1993institutional`; continuity: `march1991exploration`,
  `levitt1988organizational`, `stuart1996local`, `cohen1990absorptive`, `bourdieu1975specificity`). A recent review of
  topic choice treats social context and path dependence as distinct drivers and lists entry costs and topic rewards
  as open (`xiang2025research`; abstract-level claim only). To our knowledge, among the works we checked, the two
  routes have not been tested against each other at entry and at the review gate (TA:79-82).
- **Empirical gap.** Fourteen fresh searches found no study that tests author herding at ML/NLP venues with
  submission data, or relates topic-newcomer status or wave timing to ICLR/NeurIPS acceptance (VP:413-423).
- **Measurement gap.** Emergence has been judged after the fact in concept (`rotolo2015what`, `leydesdorff2002dynamic`)
  and static models can miss small emerging topics (`li2025evaluation`); prospective early-warning signals have been
  tested (`khanbayov2026topical`). None of the works we checked compares hindsight and early-only maps on the same
  papers (VP:362, 434).

### B.3 Closest prior work: what each did, what we add, exact wording

| Work (key; status) | What it did | What we add | Required wording |
|---|---|---|---|
| Hill et al. 2025 (`hill2025pivot`; V) | Larger pivots are cited less and less often published | The decision itself, every submission, double-blind, held-out | "Larger pivots are less often published (Hill et al., 2025); we observe the decision itself, on every submission to an ML venue, under double-blind review, with held-out replication." Never "first pivot penalty at the gate". Quote none of their numbers. |
| Bao and Li 2025 (`bao2025persistence`; V-arXiv) | SPECTER2 similarity to one's own prior ICML/NeurIPS papers across the deep-learning shift; persistence goes with lower later impact | Acceptance outcome on all submissions; entrants as well as incumbents | "Our closeness measure follows Bao and Li (2025), who use SPECTER2 similarity to a researcher's own earlier papers." The opposite-sign result goes in §7 as a tension. |
| Wang et al. 2023 (`wang2023what`; V); Xu et al. 2026 (`xu2026reviewer`; P) | ICLR topic clusters differ in acceptance; topic predicts acceptance at equal scores | Edges regress out of sample (0 < b < 1) | "Topics differ in acceptance at ICLR, even at equal reviewer scores (Wang et al., 2023; Xu et al., 2026); we find these edges real but regressing." |
| Ibrahim et al. 2026 (`ibrahim2026bias`; V-arXiv) | Borderline prestige gap at ICLR, pre-registered out-of-sample 2026 cohort, concentrated where arXiv identifies authors | Position relative to a record, not prestige | No "first registered/confirmatory design". Rival reading of the insider association (visible status). |
| Jung et al. 2025 (`jung2025what`; P, cite arXiv) | Full ICLR 2017-2025 record; process factors incl. earlier submission | Timing within a keyword's life | "'Early' means early in a keyword's life, not early in the submission window (cf. Jung et al., 2025)." |
| Tran et al. 2020 (`tran2020open`; V-arXiv) | ICLR 2017-2020 identity and prestige | — | Background only. |
| Movva et al. 2024 (`movva2024topics`; V) | Entry into LLM research is large (arXiv, descriptive) | What entrants write, how fast they adopt, and the gate | "Entrants are numerous" is not ours. Quote none of their numbers. |
| Stelmakh et al. 2023 (`stelmakh2023large`; V) | ICML 2020 RCT: no herding detected in reviewer discussions | The matching question for authors | "A randomised trial at ICML detected no herding among reviewers in discussion (Stelmakh et al., 2023)." Kargaran et al. (2025) report co-reviewer influence on rebuttal-phase scores, so never "reviewers are independent". |
| Boudreau et al. 2016 (`boudreau2016looking`; V) | Evaluators score proposals closer to their own expertise, and highly novel ones, lower | Our distance runs from a paper to its own authors' record | "Our distance is different: it is the distance of a submission from its own authors' record." |
| Biliotti et al. 2024 (`biliotti2024breaking`; V-arXiv) | Same topic-specific newcomer definition (COVID-19, PubMed); expertise offsets the newcomer disadvantage | Contribution type and acceptance | Cite for the definition and as a producer-side analogue of the insider association. |
| Huang 2026 (`huang2026catalyst`; V-arXiv) | Topic initiators at ICLR precede topic growth | What entrants write; acceptance by entry status | Neighbour only. |
| Li et al. 2025 (`li2025evaluation`; V); Khanbayov and Kurban 2026 (`khanbayov2026topical`; V-arXiv) | Static-model emergence detection; prospective early-warning signal | Same papers, same model, only the fitting window differs | "Same papers, same model, only the fitting window differs: 29 vs 8." |
| Zeng et al. 2021 (`zeng2021fresh`; V); Packalen and Bhattacharya 2019 (`packalen2019age`; V) | Fresh teams and younger researchers bring new ideas | A registered *herding* prediction for entrants failed in the opposite direction at a review gate | "Producer-side studies find that fresh teams and younger researchers try new ideas (Zeng et al., 2021; Packalen and Bhattacharya, 2019)." |
| Weisberg and Muldoon 2009 (`weisberg2009epistemic`; V); Alexander et al. 2015 (`alexander2015epistemic`; V) | Formal split of "followers" vs agents searching from their own position; critique of welfare conclusions | Empirical test at entry and gate | "We use the model's taxonomy of search strategies, not its welfare conclusions." |

### B.4 Novelty paragraph (drop-in, end of §1; keep the qualifier)

> Studies of ICLR's open records have related acceptance to author prestige and visibility (Tran et al., 2020;
> Ibrahim et al., 2026), to the review process (Jung et al., 2025), and to research area (Wang et al., 2023; Xu et al.,
> 2026). Studies of the producers describe who enters machine-learning topics and how far researchers stay from their
> own past work (Movva et al., 2024; Bao and Li, 2025), and the science of science shows that moving far from one's own
> record costs citations and publication (Hill et al., 2025). Computational histories read trends from topic models
> fitted on the whole period (Hall et al., 2008; Pramanick et al., 2023); static models can miss small emerging topics
> (Li et al., 2025), and prospective early-warning signals for AI topics have been tested on later years (Khanbayov
> and Kurban, 2026). To our knowledge, among the works we checked, no study asks within one complete submission
> population whether the herding account of a field's waves holds at three points: how the waves are measured, what
> kind of work topic entrants bring, and what the review decision goes with. Nor does any study test these
> predictions with registered hypotheses replicated on held-out papers.

**Theory-level novelty sentence (§2, once):** "To our knowledge, among the works we checked, imitation and continuity
have not been tested against each other at entry and at the review gate."

### B.5 Three contribution statements (§1, one bullet each)

1. **A test of the herding account where it is sharpest** (herding and fashion theory; ML's hype debate). We separate
   imitation and continuity by their reference point and derive opposed predictions for topic newcomers and for
   review. Our registered prediction that newcomers write follow-on measurement work failed in the opposite direction
   and the reversal replicated (A); teams new to ICLR also take up the field's package and its rising keywords more
   slowly (E).
2. **Where the gate's conservatism sits** (science of science on tradition and evaluation). In one complete
   submission population under double-blind review, following the crowd carries no detectable premium (C; edges
   regress, B), while acceptance goes with a paper's position relative to its team's record (B, post hoc, supported
   on held-out papers); a field-referenced distance test is undetermined (C).
3. **A measurement lesson for computational histories** (ACL). On the same papers with the same model, a topic map
   fitted on all years finds 29 emerging topics and one fitted on 2017–2020 finds 8, and a trend conclusion reverses
   (E). Every claim carries an evidence tier and a code saying whether its measure uses only earlier data, passed the
   registered hindsight variants, or is retrospective by construction.

The design (registration, sealed outcomes, single frozen run, held-out tests, disclosed size failure) is described in
§3 and is **not** a contribution: Ibrahim et al. (2026) already pre-registered an out-of-sample ICLR test.

### B.6 What we must not claim as new

ICLR OpenReview as a data source; noisy review; prestige effects; FM growth and homogenisation as ideas; topic-model
histories; that entrants are numerous; that pivot penalties and chaperone effects exist; that rejected submissions
are visible in evaluation studies; topic differences in acceptance; SPECTER2 closeness to one's own record as a
measure; a pre-registered out-of-sample ICLR test; that newcomers bring new ideas (LS:479-489; VP:477-483).

### B.7 Reviewer objections and where the paper answers them

| Objection | Answer (where) |
|---|---|
| "Continuity" is the Matthew effect or visible status relabelled | Continuity is defined as a content position relative to a record (§2.2); rivals named (Merton 1968; Ibrahim et al. 2026); evidence ordered by how well it holds the writer fixed: E4 within author, E1 among teams that all have a record, insider last as status-compatible (§6.2-6.3); mechanism open (§7.2). |
| Method papers are a label; adapters on LLMs count as method; content distance is built in | "A method paper is a contribution type, not novelty; an adapter on an LLM counts as method" (§5.3); returning topic newcomers adopt FMs at incumbents' rate while first-time teams lag (§5.5); content distance worded "partly by construction" (§5.4). |
| The positive half is post hoc and the record-vs-field contrast is a power contrast | Asymmetry stated in abstract, §1, §6.0; E1 is the declared primary test with power 0.89; the field test had power 0.47 and is "undetermined"; honest denominators (§6.4). |
| You tested a strawman of herding | Our own registered prediction encoded it (§5.1); flocking is named untested (§5.6, Limitations). |
| The hindsight result is obvious or confounded | Gradient across six maps, seed refit 28, bracket 22.3-40.9%, "maps differ in fitting corpus as well as window" (§4.2); which registered claims pass the hindsight variants (§4.3, Table 1 codes). |
| Continuity is not conformity | Conformity here means convergence towards the established (Bourdieu's succession and consecration; Weisberg's risk-avoiding clustering), not identical choices; the split buys opposite predictions at entry (§2.3). |

---

## C. Paragraph-level outline of the body

### C.0 Word budget (body only; abstract, captions, tables, Limitations, Ethics, references and appendix excluded)

| § | Title | Words |
|---|---|---|
| 1 | Introduction | 630 |
| 2 | Two Routes to Conformity | 400 |
| 3 | Data and Design | 440 |
| 4 | The Field: One Package, Fewer Fashions than Hindsight Shows | 420 |
| 5 | Entry: Newcomers Propose, Incumbents Consolidate | 600 |
| 6 | The Gate: What Acceptance Goes With | 720 |
| 7 | Discussion: Where Conformity Lives | 340 |
| 8 | Conclusion | 80 |
| | **Total** | **3,630** |

Paragraph budgets below sum to the section budgets. Recount after drafting; the hard range is 3,300-3,800.

### §1 Introduction (630)

**¶1.1 The wave (90).**
- Point: ICLR's foundation-model wave is vivid, and it invites a herd reading.
- Evidence: submissions 384 (2017) → 15,411 (2026), ×40.1; 69.3% of the corpus from 2024–26 (DP:70-72; E). FM share
  0.3% → 54.4%; new-architecture share 24.5% → 7.5% (DC:163-164; LAB; E). Figure 1 (discovery): GANs peak 8.1% (2018),
  large language models 16.7% (2026) (FIG1). 17 of 68 frequent keywords rose and fell (pooled wave table; DP:81; E).
- Citations: none. Figure 1 is cited here.

**¶1.2 The herding reading (90).**
- Point: critics and theory both read such waves as herding, which makes three claims: the waves are fashions,
  imitators carry them, and following pays at review.
- Evidence: none (framing).
- Citations: `lipton2019troubling`, `hooker2021hardware`, `dehghani2021benchmark`, `bommasani2021opportunities`,
  `movva2024topics`; `bikhchandani1992theory`, `banerjee1992simple`, `abrahamson1991managerial`; following pays only
  if evaluators reward conformity (`scharfstein1990herd`, general argument); counterpoint `sutton2019bitter`.

**¶1.3 Two routes, and the hook (100).**
- Point: conformity has two routes that the herding literature runs together; we expected the first ourselves.
- Content: imitation takes its cue from what others do now; continuity from an accumulated record (the team's own past
  work, or a topic's record carried by a team member). We call work that conforms by continuity *anchored*
  (footnote, G.1). "We expected a herd too": before any outcome was read, we registered that topic newcomers would
  write fewer method papers and more benchmark and evaluation papers (DC:33-36, 237).
- Citations: `weisberg2009epistemic`, `weisberg2013modeling`; footnote `tversky1974judgment`, `baddeley2015herding`.

**¶1.4 Design (70).**
- Point: one complete submission population, registered tests, a held-out split, tiered findings.
- Evidence: 43,480 submissions with usable abstracts, 2017–2026, rejected and withdrawn included (DC:65-66);
  registered 2026-10-13 before any full-corpus label existed, one frozen run (DC:237, 246); tested again on 11,099
  held-out papers, "a pre-registered out-of-sample replication, not a certified untouched holdout" (DC:43-44, 72).
  Every finding carries a tier (Table 1). All results are associations (DC:42).
- Citations: none.

**¶1.5 What we find, and the thesis (110).**
- Point: one sentence per test, with tiers, then the thesis (A.2) and the memorable line (A.3).
- Content: field: converged on a package (A) but hindsight inflates the waves (E); entry: the registered herding
  prediction reversed (A) and teams new to ICLR come later to the package (E); gate: no detectable premium for
  following (C; edges regress, B), while acceptance goes with continuity (B, post hoc, supported on held-out papers).
  State the asymmetry in one clause: the negative half is registered, the positive half post hoc.
- Citations: none.

**¶1.6 Gap (110).** The B.4 novelty paragraph, verbatim.

**¶1.7 Contributions (60).** B.5, one line each. Never "RQ1/RQ2/RQ3"; say "we test one account at three points".

### §2 Two Routes to Conformity (400)

**¶2.1 Imitation (120).**
- Point: imitation refers to others now, and theory predicts it is strongest among those with the least information,
  and individually rational only if evaluators reward it.
- Content: frequency imitation (crowding, hot topics, rising keywords, FM adoption) and outcome imitation (topics with
  high past acceptance); trait imitation is not measured (`haunschild1997modes`). Uncertainty breeds mimicry, so
  entrants to a topic are predicted to imitate most (`dimaggio1983iron` general argument; `bikhchandani1992theory`). Reputational
  herding needs evaluators who reward conformity (`scharfstein1990herd`); a reward system can amplify or counteract the
  pull of the leading approach (`kitcher1990division`, general argument). Bandwagons can spread without any reward
  (`abrahamson1993institutional`).
- Evidence: none.

**¶2.2 Continuity (130).**
- Point: continuity refers to a record; it predicts entrants bring their own work and absorb a new package slowly, and
  a gate that consecrates succession.
- Content: local search near one's competence (`march1991exploration`, `stuart1996local`); learning from one's own
  experience versus others' (`levitt1988organizational`, general argument); absorptive capacity, so teams without a
  record take up a new package more slowly, the opposite of the cascade prediction (`cohen1990absorptive`). Bourdieu
  (read in full; TA:408-418): new entrants choose between "the risk-free investments of succession strategies" and
  costly "subversion strategies"; journals "consecrate productions faithful to the principles of official science"
  (`bourdieu1975specificity`). Science of science: tradition (`foster2015tradition`), the pivot penalty
  (`hill2025pivot`), chaperones (`sekara2018chaperone`).
- Definition sentence (exact): "Continuity is a position of a paper's content relative to a record, not the possession
  of one. Having a record also brings cumulative advantage (Merton, 1968) and, where authors are identifiable, visible
  status (Ibrahim et al., 2026); §6 orders the evidence by how well it holds the writer fixed."
- Citations add: `merton1968matthew`, `ibrahim2026bias`.

**¶2.3 Timing, and where the routes can be told apart (70).**
- Point: timing belongs to neither route but separates rewarded imitation (late riders do as well as early ones) from
  priority (the premium falls as a wave matures); the field level cannot discriminate.
- Content: priority (`merton1957priorities`; `strevens2003role`, general argument). Convergence on a package is
  predicted by a package bandwagon (`fujimura1988molecular`, general argument), lock-in (`arthur1989competing`) and
  efficient choice (`sutton2019bitter`) alike (TA:600, 616-617). Hence entry and the gate decide; §4 sets the stage.

**¶2.4 Gap and terms (80).**
- Point: the routes are rarely tested against each other; we say "to our knowledge" and use the taxonomy only.
- Content: theory-level novelty sentence (B.4); `xiang2025research` (abstract-level: social context vs path
  dependence; entry costs and topic rewards open). Use the Weisberg-Muldoon taxonomy, not its welfare conclusions
  (`alexander2015epistemic`). "These words label positions of papers, not motives."

### §3 Data and Design (440)

**¶3.1 Corpus (90).**
- Evidence: our own dated acquisitions of official OpenReview records, 55,938 reconciled submission instances (DC:62);
  discovery 43,480 papers with usable abstracts (DC:65); acceptance tests use 32,190 decided papers, 40.1% accepted,
  with 9,986 withdrawn papers left out (DC:318, 408); held-out 11,099 papers, 8,185 decided in 2018–26 (DC:72-74);
  existing ICLR dumps were audited and not pooled (DC:69; details Appendix A). One clause: NLP researchers
  increasingly publish at ML venues (`jurgens2026future`), so ICLR is part of the field ACL readers work in.
- Citations: `jurgens2026future`; Appendix A cites `zhang2025re2`.

**¶3.2 Instruments (150).**
- Topics: SPECTER2 embeddings of title [SEP] abstract, unit-length PCA(128), spherical k-means, k = 100, chosen before
  a sensitivity sweep; NMI with ICLR primary areas 0.302 vs 0.272 for a TF-IDF/LSA baseline; blind name check 80%
  correct at this level; seed ARI 0.66; no outcome field read (DC:86-93, 108). `cohan2020specter`,
  `singh2023scirepeval`.
- Contribution type: one primary type per paper from a fixed LLM codebook; method (incl. new architecture), theory,
  empirical, dataset/benchmark, evaluation, other; blind second pass κ 0.93 on 2,174 papers, held-out κ 0.931 on 555;
  "consistency between LLM labellings, not human-level validity" (DC:52, 129-135). FM paper = uses or adapts a large
  pre-trained model (DC:138).
- Entry status from exact author IDs, never names; newcomer, first-time team, insider as in G.1 (DC:144; PRE:1281,
  1567-1569, 1659). The 2021 email-to-profile ID switch hides earlier histories (k100 incumbency 18% in 2020,
  0.5% in 2021), biasing entry contrasts towards zero (DC:145-146).
- Distances, both on centred SPECTER2: closeness to the team's own record (F_max, exact definition in G.1;
  PRE:1372-1380) and distance from earlier ICLR work (G.1; DP:255; NN). Same space, different reference points.
  Credit `bao2025persistence` for the own-record measure.

**¶3.3 Prospective measurement and information codes (100).**
- Point: every predictor uses only the past, and each Table 1 row says so.
- Content: entry status uses submissions strictly before year t; FM adoption, heat and crowding are lagged; closeness
  uses each author's earlier submissions; distance uses strictly earlier years; keyword states use onset and lagged
  momentum; topic edges from 2018–22 predict 2024–26 (DC:144, 153; PRE:1259-1262, 1372-1380; DP:326). Registered
  time-trend claims must also hold on a year-balanced map and on the 2017–20 map applied to 2021–26 papers (DC:193,
  239). Codes: **P** prospective; **H✓/H✗** registered hindsight variants pass/fail; **R** retrospective by
  construction; **T✓** discovery estimate held after removing links and availability sentences from abstracts.
  Outcome leakage into text: 17.6% of accepted vs 0.5% of rejected 2023–26 abstracts carry a code link (DC:78).
- Citations: `kaufman2012leakage`.

**¶3.4 Protocol, models, tiers, inference (100).**
- Evidence: decision rule (Holm within family, ≥75% of counted variants, both hindsight variants; DC:239); outcomes
  readable only by a sealed loader, one frozen run of 18 s (DC:245-246); held-out tests registered 2026-10-18 and run
  once (DC:256-258); post hoc families declared before they were run (DC:390); earlier exploratory looks at keyword
  popularity and title style disclosed (DC:238). Linear probability models with topic and year (or topic × year)
  fixed effects, SEs clustered by topic (DC:244). Size failure: under a null that cuts across topics, the main entry
  tests rejected 12.6% / 10.0% at nominal 5%, and a wild cluster bootstrap did not fix it (12.4% / 9.6%) (DC:249-250).
  Non-supported tests below MDE80 are "uninformative" (DC:46). Ibrahim et al. (2026) also pre-registered an
  out-of-sample ICLR test (no "first").
- Citations: `nosek2018preregistration`, `vandenakker2021preregistration`, `holm1979simple`, `cameron2008bootstrap`,
  `ibrahim2026bias`.

### §4 The Field: One Package, Fewer Fashions than Hindsight Shows (420)

**¶4.1 The usual ruler (70).**
- Point: field histories fit one topic map on all years and read it forward, which leaks the future into the past.
- Citations: `hall2008studying`, `anderson2012towards`, `pramanick2023diachronic`, `schafermeier2021topic`,
  `grootendorst2022bertopic`, `blei2006dynamic` (dynamic models still fit all slices jointly), `rotolo2015what`,
  `leydesdorff2002dynamic`, `li2025evaluation`, `khanbayov2026topical`, `kapoor2023leakage`, `fischhoff1975hindsight`.

**¶4.2 Hindsight inflates the waves (150).** (Figure 2a)
- Point: on the same papers and pipeline, the count of emerging topics depends on which years the map was fitted on.
- Evidence (E; DC:176-187; HC): emerging topics (2024–26 share ≥ 3× the 2017–20 share): 2017–20 map 8 (22.3% of
  2024–26 papers in them); 2021–23 map 10 (20.9%); year-balanced 16 (42.2%); 2024–26 map 28 (31.0%); all-years 29
  (40.9%); a seed refit of the all-years map 28. Declining topics: 13 all-years vs 26 year-balanced. Mechanism:
  69% of papers are from 2024–26, so the all-years map is a present-day map; it fits 2026 papers better than 2017
  papers (0.65 vs 0.62), the early map the reverse (0.69 vs 0.53) (DC:67, 176-179). Growth compounds hindsight: the
  all-years map finds as many emerging topics as the 2024–26 map (29 vs 28). Bracket, not point: 22.3%–40.9% (DC:187);
  the early map cannot represent topics born after 2020, and the maps differ in fitting corpus as well as window
  (DC:229).
- One sentence (E; counted variants of C; exploratory, unadjusted): whether topics "age" from method to measurement
  papers is null on the all-years map (method −0.14 [−1.78, +1.49], measurement +0.50 [−0.76, +1.75] pp per log unit)
  but appears on the 2017–20 map for 2021–26 papers (−3.48 [−6.21, −0.76]; +3.96 [+1.35, +6.57]) (DC:201-202). "The
  answer depends on the map." Topic size "predicting" growth (R² 0.28 vs −0.03) goes to the Figure 2 caption and
  Appendix C only (no paired test; DC:227-229).

**¶4.3 What survives: a package (120).** (Figure 2b)
- Evidence: FM share rose every year since 2018 (0.3% → 54.4%), unlike the 17 of 68 keywords that rose and fell
  (DC:168; DP:81; LAB; E). Registered H1d: where more of a topic's previous-year papers built on FMs, fewer of its
  papers propose new architectures: −7.98 pp for 0 → 100% prior FM share [−12.14, −3.82] (n 42,990), held-out −11.0
  [−18.1, −3.9] (n 10,978; one-sided p 0.0013); 9/9 counted variants; both hindsight variants pass (A; DC:271, 364).
  Plain reading: about a third fewer new-architecture papers at 50% adoption than at 10%, on a base near 9%
  (DC:274-277). The held-out test was underpowered at the discovery size (MDE80 12.0): direction, not size (DC:380).
  Limit (C): no detectable shift towards empirical or evaluation papers with adoption, −0.63 [−3.64, +2.38] (DC:272);
  the package's within-topic signature is fewer new architectures, nothing more. Reverse causality is possible; an
  adapter on an LLM is labelled method (DC:283-284).
- Citations: `bommasani2021opportunities` (homogenisation in the substrate sense; "consistent with", never
  "confirms"), `gururaja2023build`, `saphra2024first`, `bao2025persistence` (descriptive displacement in the
  previous shift).

**¶4.4 What the field level cannot decide (80).**
- Point: package bandwagon, lock-in and efficient choice all predict H1d; two outcome-free observations are context.
- Evidence: the share of papers with an independent same-year twin rose from 19.5% (2019) to 48.8% (2026), but twins
  per paper per 1,000 submissions fell from 0.32 to 0.19: duplication grew with volume, not per pair (DP:78-79; FTS;
  E). Imitation-like spread is plain in surface form: titles opening with a short coined name and a colon rose
  roughly fourfold, from 7–14% (2017) to 37–49% (2026) by definition (E\*; DP:120-125). Transition: entry and the gate
  decide.
- Citations: `fujimura1988molecular`, `arthur1989competing`, `sutton2019bitter`, `hooker2021hardware`.

### §5 Entry: Newcomers Propose, Incumbents Consolidate (600)

**¶5.1 Where imitation is predicted to be strongest (60).**
- Opening sentence (exact): "A randomised trial at ICML detected no herding among reviewers in discussion (Stelmakh
  et al., 2023). We ask the corresponding question about authors entering a topic, where imitation theory expects
  herding most and absorptive capacity expects the opposite."
- Citations: `stelmakh2023large`, `kargaran2025insights` (one clause: co-reviewer influence exists), `dimaggio1983iron`,
  `cohen1990absorptive`.

**¶5.2 The registered prediction reversed (150).** (Figure 3a; Table 1 rows 4-5)
- Evidence (A, reversed registered prediction; DC:33-36, 296-297, 365-366): newcomer papers (72.9% of 42,325 papers;
  DC:151) are more often method papers, +3.71 pp [+2.61, +4.80] on a 75.0% base, held-out +3.60 [+1.48, +5.71]
  (n 10,718; one-sided p 0.0007; MDE80 2.8); less often benchmark, dataset or evaluation papers, −1.70 [−2.46, −0.93]
  on a 7.7% base (about a fifth fewer), held-out −2.10 [−3.35, −0.85] (one-sided p 0.0005; MDE80 2.4). All 10 counted
  variants agree; hindsight variants +3.10 / +2.16 and −1.41 / −0.86; same sign at k = 75 and 150 (DC:118-119). The
  reversed hypotheses were registered after discovery and before any held-out data. Inference: t = 6.7 and −4.4
  against stress inflation factors of 1.31 / 1.22 (DC:311-312). A misclassification correction can only enlarge them
  (+4.09 / −1.84; DC:304); without the ID-switch years 2021–22: +3.72 / −1.74 (DC:148).
- Always say the original registered herding prediction failed.

**¶5.3 What the reversal does and does not mean (90).**
- Evidence: with log team size the measurement gap shrinks to −0.54 [−1.11, +0.04] (p 0.07; held-out −0.98), the
  method gap does not (+3.92) (DC:301, 308): part of it is small all-new teams vs larger mixed teams. It is
  concentrated in 2024–26 (−2.0; D; DC:305-306).
- Wording (exact): "A method paper is a contribution type, not a measure of novelty; an adapter on an LLM counts as
  method." Benchmark building is concentrated (`koch2021reduced`); methods drive and datasets follow
  (`pramanick2023diachronic`). Producer-side studies find that fresh teams and younger researchers try new ideas
  (`zeng2021fresh`, `packalen2019age`); what is new here is that a registered herding prediction failed in the
  opposite direction.

**¶5.4 Farther from earlier work, partly by construction (110).** (Table 1 row 6)
- Evidence (E; outcome-free, unregistered, computed during writing; NN): within topic × year, newcomer papers sit
  +5.90 percentile points [+4.95, +6.85] farther from earlier ICLR papers than incumbent papers (N 42,325; 786
  topic-year cells; SEs clustered by 100 topics; NN:main_pct). Within method papers +5.24 [+4.16, +6.31] (N 31,764);
  with team-size, class and FM controls +5.76 [+4.82, +6.70]. No smaller in 2023–26 (+6.01 [+5.03, +6.98]) than in
  2019–22 (+4.95 [+2.32, +7.58]), difference +1.06 [−1.64, +3.75], p 0.44, while the FM share went from 10.6% to 54.4%.
  Size: +1.35 [+1.16, +1.55] × 10⁻² on the raw cosine scale, 0.22 of a within-cell SD (NN:raw_cosine_nov_x100;
  descriptives SD 0.0618): modest but precise. 2019 alone +1.26 (p 0.70).
- Caveat sentence (exact): "Part of this gap is built in: an incumbent paper's team has, by definition, earlier
  submissions in the topic that can be among its nearest earlier neighbours, while a newcomer paper's team has none
  there. The gap therefore fits both entrants arriving from elsewhere and incumbents continuing their own work; either
  way, newcomer papers do not sit closer to earlier work than incumbent papers, as the follow-on prediction expects.
  Distance in SPECTER2 space is not originality, and vocabulary from other fields may look distant."
- Never "more novel", "more original" or "more innovative".

**¶5.5 Later onto the package and the trend (120).** (Figure 3b; Table 1 row 7)
- Evidence (E; outcome-free): teams new to ICLR (first-time teams, 26.3% of papers; FH) write FM papers less often
  than returning topic newcomers by 4.58 [2.60, 6.55], 8.96 [4.63, 13.30] and 14.71 [9.61, 19.82] pp in topics at
  5–15%, 15–30% and 30–50% prior adoption, with class and team-size controls (FE; PRE:1111-1112; DP:360-362); not
  detectable at 0–5% (−0.95) or ≥50% (−1.96). Returning topic newcomers do not differ detectably from incumbents in
  any bin (−2.58 to +2.87; all p ≥ 0.06; the 30–50% bin is wide, [−2.74, +8.48]) (FE). First-time teams list Emerging
  (young, rising) keywords less often: 16.7% vs 25.0% of uses, −3.74 pp [−5.14, −2.35], q 6e-6, no team-size control
  (FPS; DP:315-317). Newcomer papers are less often twinned than incumbent papers: −3.86 [−4.98, −2.74], with class, FM
  and team-size controls; first-time teams differ by a further −0.32 (n.s.) (FH; PRE:1542; DP:275).
- Reading: the package travels with an ICLR record, the order absorptive capacity predicts and the opposite of the
  mimetic prediction (`cohen1990absorptive`; `dimaggio1983iron`). The FM label is an LLM label on partly camera-ready
  text; descriptive, no acceptance link (DP:362).

**¶5.6 What stays untested (70).**
- Evidence: whether entrants crowd into hot topics is not settled: incumbent share in hot vs other topics −0.73
  [−2.68, +1.22], inconclusive, hindsight variant fails (C; DC:295); newcomer × hot −0.4 / −0.6 pp, n.s. (D; DC:307).
- Sentence (exact): "We can say what entrants write and how fast they adopt the field's package, not whether they
  crowd into hot topics." Context only: crowding can also repel (`borjas2015cognitive`). Who starts topics is a
  different question (`huang2026catalyst`).

### §6 The Gate: What Acceptance Goes With (720)

**¶6.0 The asymmetry (50).**
- Sentence (exact): "The negative half of our thesis rests on registered tests (A, C); the positive half rests on
  post hoc tests that a held-out test declared in advance supported (B)." Six secondary held-out tests were one-sided
  and unadjusted: "one false positive would not be surprising" (DP:29-30). Holm values hold within module families
  only (DP:54-55).

**¶6.1 Following: no detectable premium, and edges that regress (170).** (Table 1 rows 9-10)
- Evidence: acceptance per log unit of prior topic papers −1.68 pp [−3.68, +0.32] in discovery (32,190 papers), −1.51
  [−5.20, +2.19] held-out (8,185 papers; MDE80 4.8; hindsight variants fail): uninformative; "no detectable premium"
  (C; DC:324, 332, 367). Large fields can ossify their canon (`chu2021slowed`); at this gate, effects below about
  5 pp per log unit cannot be told from zero. Branded titles, whose share rose fourfold, were accepted at the
  submitted rate in an earlier exploratory analysis (ratio 1.02; D\*, not re-run; DP:133); one clause. Topic edges:
  topics differ (noise-free SD 6.4 pp [5.0, 7.2]; DP:324) but a single year's rate is half noise at about 58 decided
  papers (DP:325); 2018–22 edges predict 2024–26 edges with slope 0.38 [0.18, 0.58] in discovery and 0.60
  [0.32, 0.88] on held-out papers (75 units; 0 < b < 1; B; DC:376); empirical-Bayes-shrunk edges predict better than
  zero (D0 1.71 [0.42, 3.01] × 10⁻³; B; DC:377). With keywords as units the slope is 0.16 [−0.34, 0.66]
  (unregistered; DP:52-53).
- Reading (exact): "A favoured topic keeps part of its edge, not all of it; copying topics with high past acceptance
  would partly chase noise." An absence of premium does not rule out bandwagons that go unrewarded.
- Citations: `wang2023what`, `xu2026reviewer`, `haunschild1997modes`, `abrahamson1993institutional`, `chu2021slowed`.

**¶6.2 Continuity: closeness to the team's own record (200).** (Table 1 rows 14-15; Figure 4a)
- Order: E4 first (holds the person fixed), then E1 (the declared primary test).
- Evidence E4 (B, secondary): within the same author, per +0.1 cosine of closeness to their earlier work, +0.55 pp
  [+0.21, +0.90] in discovery (54,303 author rows, 19,266 papers), +1.06 [+0.23, +1.89] held-out (4,311 papers;
  one-sided p 0.006); co-author composition may explain half or more (DC:372; DP:241-243).
- Evidence E1 (B, primary): among decided 2023–26 papers with at least one experienced author (20,430; acceptance
  44.1%), papers at the 10th percentile of F_max vs the median: −5.44 [−7.10, −3.78] (Holm 1.3e-8), held-out −6.09
  [−9.32, −2.86] (5,344 papers; one-sided p 0.0025; Holm 0.005; MDE80 4.9; power 0.89 at the discovery effect)
  (DC:370; DP:233-235). Robustness: newcomer control −5.0; no earlier version −5.5; link-removed text −5.39; early map
  −5.2; correlation with the newcomer flag −0.57 (DP:238-248, 371). Shape (D; QT): adjusted acceptance by closeness
  fifth, far to near, 39.7 / 41.8 / 44.4 / 47.2 / 46.9%: leaving costs, the closest fifth gains nothing over the
  fourth. If the near tail is quoted, the E2 rule applies (DP:40-41).
- Wording: the Hill sentence and the Bao and Li sentence from B.3; Boudreau's distance is a different construct.
- Citations: `hill2025pivot`, `bao2025persistence`, `boudreau2016looking`, `stuart1996local`.

**¶6.3 Carrying the topic's record (140).** (Table 1 row 16)
- Evidence (B, secondary): one topic insider vs none, at fixed team size and number of experienced authors: +3.42
  [+1.18, +5.66] in discovery (24,601 decided 2023–26 papers), +3.88 [+0.28, +7.47] held-out (6,243 papers;
  one-sided p 0.017); underpowered at the discovery size (derived MDE80 ≈4.5), so direction only; Holm 0.019 holds
  within its module only, about 0.17 across modules (DC:374; DP:54-55, 283-288). Early-map insider +3.0 (p 0.003); a
  keyword-defined insider +0.0, a null the registration anticipated because the two definitions correlate only
  0.18–0.29 (DP:288-289; PRE:1661).
- Person level (D): the newcomer acceptance gap is −10.2 [−11.8, −8.7] within topic × year (DC:343); on the same 28,370
  papers −5.4 [−7.1, −3.7] without and −3.1 [−4.5, −1.6] with author fixed effects; the same author entering a new
  topic −1.4 [−2.7, −0.0] (DP:177-179). Most of the gap is about who writes; the residual "need not be reviewer bias"
  (DP:181-183).
- Reading: the result a status reading explains equally well (say so here). Chaperones (`sekara2018chaperone`);
  expertise offsets newcomer disadvantage (`biliotti2024breaking`); young-plus-experienced configurations
  (`packalen2019age`).

**¶6.4 Two reference points in one space, and honest denominators (80).** (Table 1 rows 13-16; Figure 4b)
- Evidence: distance from the field (same centred SPECTER2 space, the field's earlier papers as reference): least-
  distant fifth vs middle fifth −3.27 [−4.93, −1.60] in discovery, −0.13 [−3.50, +3.25] held-out (8,010 papers;
  power 0.47; MDE80 5.4): uninformative (C; DC:371); within-author slope not supported (+0.34 [−0.47, +1.16]; C;
  DC:373). Of the post hoc patterns taken to held-out papers, E1, E4, the insider and the edge regression were
  supported; A1 and PH6 weakly; P1b, P7 and the federated-learning gap were not (DC:364-378).
- Sentence (exact): "The own-record association held on held-out papers; whether distance from the field matters,
  our held-out test cannot say." Compare replication status, not size: populations and units differ.
  Weakly consistent with no novelty penalty at journals (`teplitskiy2022is`).

**¶6.5 Timing: early, weakly; the vivid fad case not confirmed (80).** (Table 1 rows 11-12)
- Evidence (B weak): Emerging vs Mainstream keywords +2.67 [+0.76, +4.58] in discovery, +3.25 [−0.18, +6.69] held-out
  (one-sided p 0.031; the two-sided interval includes 0) (DC:375; DP:48-49). A keyword's acceptance gap after vs up
  to its share peak, 17 waves: −5.7 [−8.5, −2.9] in discovery (not a test), −5.2 [−11.1, +0.7] held-out (one-sided
  p 0.043; MDE80 7.4); −1.7 (p 0.33) without the six keywords inspected first; the wave set is retrospective by
  construction (DP:389-397). Both lean, weakly, towards priority. Federated learning: −11.3 [−17.9, −4.8] in
  discovery (q 0.19), held-out −4.9 [−15.4, +5.7] (MDE80 14.5), trend opposite in sign: "not confirmed" (D/C;
  DC:368-369).
- Wording: "early" means early in a keyword's life, not early in the submission window (`jung2025what`). Citations:
  `merton1957priorities`, `strevens2003role`.

### §7 Discussion: Where Conformity Lives (340)

**¶7.1 The pattern (90).** (Table 2)
- Point: in producers and at the gate, the imitation predictions fail or show no detectable reward, and the
  continuity associations hold; this is conservatism and consolidation, not identical choices.
- Sentence (exact): "What Weisberg (2013) models as herding, risk-avoiding clustering, appears here as continuity with
  a record, not as imitation of the crowd." Bourdieu's gate consecrates succession. "Continuity labels positions, not
  motives."
- Citations: `weisberg2013modeling`, `bourdieu1975specificity`.

**¶7.2 Mechanism is open (100).**
- Point: expertise, evaluator conservatism, visible status, cumulative advantage and selection into teams cannot be
  separated here.
- Evidence (D): per head, an insider is worth about as much as an experienced author from another topic (+0.58,
  p 0.16); a proven outsider minus an unproven insider +4.6 (Holm 0.088) (DP:290-296). What E4 and E1 add (exact):
  "holding who writes fixed, acceptance goes with how close the content stays to that record." Double-blind review
  rules out none of the readings, since preprints can identify authors. We do not show that entrants' distant content
  is discounted: the newcomer gap is mostly who writes (D), and field distance has no replicated association (C).
- Citations: `li2017expertise`, `ibrahim2026bias`, `bharadhwaj2020deanonymization`, `merton1968matthew`,
  `hofstra2020diversity` (the reading we pre-empt).

**¶7.3 A tension and its costs (60).**
- Sentence (exact): "In the previous shift, researchers who stayed close to their own record had lower later impact
  (Bao and Li, 2025); here continuity goes with acceptance. The gate and the citation record need not reward the same
  thing; our data cannot test this." Short-cycle rewards favour refining existing competence, which carries long-run
  costs (interpretation, not advice).
- Citations: `bao2025persistence`, `march1991exploration`, `levitt1988organizational`, `rzhetsky2015choosing`.

**¶7.4 For the hype debate and for field histories (90).**
- Point: whether a field looks homogenised depends on the layer measured; topic histories can be checked
  prospectively at the cost of one refit.
- Content: at ICLR the substrate converged (A), consistent with homogenisation in Bommasani et al.'s sense, while no
  herding of the testable kinds was detected among entrants. One sentence (D, discovery only): FM papers are accepted
  more often (+4.62 [+2.79, +6.44]), the premium does not detectably change with adoption (+0.19 [−0.96, +1.34] per
  logit unit), and new-architecture papers are accepted relatively more where FMs dominate (+8.3 [+1.3, +15.4]); a
  fad premium would be expected to fade (DC:342, 349; DP:356). For histories: one refit on early years, lagged predictors and the
  P/H/R codes expose hindsight cheaply (a property of measurement, not an instruction).
- Citations: `bommasani2021opportunities`, `hall2008studying`.

### §8 Conclusion (80)

- Restate the three tests in one sentence each (field: package real, waves inflated by hindsight; entry: the
  registered herding prediction reversed; gate: no detectable premium for following, continuity associations held
  out of sample), then the memorable line, then scope: "one venue, associations only, every claim tiered". No new
  numbers.

### C.9 Placement map (every major finding has a place)

| Finding | Tier | Place |
|---|---|---|
| Growth, FM share, new-architecture share, keyword waves | E | §1.1, §4.3, Fig 1, Fig 2b |
| H1d package displacement | A | §4.3, Table 1 row 2, Fig 2b |
| H1e limit; H1a-c not supported | C | §4.3 (H1e); Appendix D (H1a-c) |
| Hindsight: 29 vs 8; gradient; lifecycle flip; forecast R² | E | §4.2, Fig 2a, Table 1 row 1; R² in caption and Appendix C |
| Twins as volume | E | §4.4, Table 1 row 3 |
| Title style share | E\* | §4.4; ratio D\* in §6.1; definitions Appendix G |
| H2b′/H2c′ reversal | A | §5.2-5.3, Table 1 rows 4-5, Fig 3a |
| Content distance (new) | E | §5.4, Table 1 row 6; full specs Appendix E |
| First-time teams: FM uptake, Emerging keywords; returning newcomers at incumbent rate | E | §5.5, Table 1 row 7, Fig 3 |
| Newcomers less often twinned | E | §5.5, Fig 3a |
| Flocking H2a; newcomer × hot | C; D | §5.6, Table 1 row 8 |
| Crowding H3a | C | §6.1, Table 1 row 9, Fig 4b |
| Topic edges regress; EB D0 | B | §6.1, Table 1 row 10 |
| Far jump E1; within-author E4 | B | §6.2, Table 1 rows 14-15, Fig 4 |
| Topic insider | B | §6.3, Table 1 row 16, Fig 4b |
| Newcomer gap mostly composition; −1.4 within person | D | §6.3 |
| Field distance P1b, P7; P1a | C; D | §6.4, Table 1 row 13, Fig 4b |
| A1, PH6 | B weak | §6.5, Table 1 row 11 |
| Federated learning | D / C | §6.5, Table 1 row 12 |
| FM premium, against-the-tide architectures | D | §7.4 one sentence; Appendix F |
| Insider decomposition, proven outsider | D | §7.2; Appendix F |
| Team size, PH1 correlates, E3 withdrawal, E10 class acceptance, P2 twins, E2 near, winner's curse, PH4 areas | D / E | Appendix F |
| Code-link leakage; cleantext | E; D | §3.3; Appendix F |
| Size failure | E | §3.4; Appendix H |

---

## D. Main-text tables

### D.1 Table 1 (`table*`, full width, `\small`, booktabs): "The herding account tested at three points"

Columns: **#** | **Observable [code]** | **Imitation predicts** | **Continuity (or alternative) predicts** |
**Discovery [95% CI]** | **Held-out [95% CI]; MDE80 or power** | **Tier** | **Reading**. Units: pp of probability or
share unless noted. "·" = no prediction.

| # | Observable [code] | Imitation | Continuity / alternative | Discovery | Held-out | Tier | Reading |
|---|---|---|---|---|---|---|---|
| | ***(i) The field: are the waves fashions?*** | | | | | | |
| 1 | Emerging topics on the same 43,480 papers: all-years map vs 2017–20 map [H vs P] | · | · | 29 (40.9% of 2024–26 papers) vs 8 (22.3%); year-balanced 16 | — | E | hindsight inflates waves |
| 2 | Prior-year FM adoption, 0 → 100%, → new-architecture paper [P, H✓] | − (package bandwagon) | − (lock-in) | −7.98 [−12.14, −3.82] | −11.0 [−18.1, −3.9]; MDE80 12.0^a | A | real convergence; does not discriminate |
| 3 | Twins per paper per 1,000 submissions, 2019 → 2026 [P] | rises (piling on) | · | 0.32 → 0.19 (papers with a twin 19.5% → 48.8%) | — | E | volume, not piling on |
| | ***(ii) Entry: what topic newcomers write*** | | | | | | |
| 4 | Newcomer paper → method paper (base 75.0%) [P, H✓] | − (registered) | + | +3.71 [+2.61, +4.80] | +3.60 [+1.48, +5.71]; MDE80 2.8 | A (reversed) | against imitation |
| 5 | Newcomer paper → benchmark, dataset or evaluation paper (base 7.7%) [P, H✓] | + (registered) | − | −1.70 [−2.46, −0.93] | −2.10 [−3.35, −0.85]; MDE80 2.4 | A (reversed) | against imitation; partly team size^b |
| 6 | Newcomer paper → distance from earlier ICLR papers (percentile points within topic × year) [P] | − (follow-on stays close) | · | +5.90 [+4.95, +6.85]; method papers +5.24 [+4.16, +6.31] | — | E^c | against imitation; partly built in |
| 7 | First-time team → Emerging keyword; → FM paper vs returning topic newcomers at 5–15 / 15–30 / 30–50% adoption [P] | + (the uncertain adopt fastest) | − (absorptive capacity) | −3.74 [−5.14, −2.35]; −4.58 / −8.96 / −14.71 | — | E^d | later onto the trend and the package |
| 8 | Hot topic → share of incumbent papers (flocking) [P, H✗] | − | · | −0.73 [−2.68, +1.22] | not registered | C | untested |
| | ***(iii) The gate: following and timing*** | | | | | | |
| 9 | Topic crowding, per log unit of prior papers → acceptance [P, H✗] | + if rewarded | · | −1.68 [−3.68, +0.32] | −1.51 [−5.20, +2.19]; MDE80 4.8 | C | no detectable premium^l |
| 10 | Topic edge 2018–22 → edge 2024–26, slope b [P] | ≈ 1 if outcome imitation keeps paying | · | 0.38 [0.18, 0.58] | 0.60 [0.32, 0.88] | B | edges real but regress^e |
| 11 | Emerging minus Mainstream keyword [P]; gap after vs up to a keyword's share peak, 17 waves [R] | 0; 0 (late = early) | priority: +; − | +2.67 [+0.76, +4.58]; −5.7 [−8.5, −2.9] | +3.25 [−0.18, +6.69], MDE80 ≈4.3; −5.2 [−11.1, +0.7], MDE80 7.4 | B weak | leans to priority^f |
| 12 | Federated-learning keyword, acceptance gap [R] | · | · | −11.3 [−17.9, −4.8] | −4.9 [−15.4, +5.7]; MDE80 14.5 | D / C | vivid case not confirmed^g |
| | ***(iv) The gate: distance from the field and from one's own record*** | | | | | | |
| 13 | Field distance: least-distant fifth vs middle fifth [P, T✓] | · | · | −3.27 [−4.93, −1.60] | −0.13 [−3.50, +3.25]; power 0.47 | C | undetermined^h |
| 14 | Far jump from the team's own record: F_max p10 − p50 [P, T✓] | · | − | −5.44 [−7.10, −3.78] | −6.09 [−9.32, −2.86]; MDE80 4.9 | B (primary) | for continuity^i |
| 15 | Within-author closeness, per +0.1 cosine [P, T✓] | · | + | +0.55 [+0.21, +0.90] | +1.06 [+0.23, +1.89] | B (secondary) | for continuity (direction)^j |
| 16 | One topic insider vs none, fixed team size and experience [P] | · | + | +3.42 [+1.18, +5.66] | +3.88 [+0.28, +7.47]; MDE80 ≈4.5 | B (secondary) | for continuity; status-compatible^k |

**Row sources:** 1 DC:176-179, HC; 2 DC:271, 364; 3 DP:78-79, FTS; 4-5 DC:296-297, 365-366; 6 NN:main_pct,
method_only_pct; 7 FPS, FE, DP:315-316, 360-362; 8 DC:295; 9 DC:324, 367; 10 DC:376; 11 DC:375, DP:389-392;
12 DC:368-369; 13 DC:371; 14 DC:370, DP:233-235; 15 DC:372; 16 DC:374.

**Table notes (print under the table):**
- a. Held-out test underpowered at the discovery size; confirms direction, not size.
- b. With log team size: −0.54 [−1.11, +0.04] in discovery, −0.98 held-out; row 4 unchanged (+3.92).
- c. Outcome-free; unregistered; computed during writing. Incumbents' own earlier papers are eligible neighbours,
  so part of the gap is built in.
- d. First-time teams vs returning topic newcomers; not detectable at 0–5% (−0.95) and ≥50% (−1.96). Returning topic
  newcomers vs incumbents: no detectable difference in any bin (−2.58 to +2.87). The keyword profile has no team-size
  control; the FM model has class and team-size controls.
- e. Keyword units: 0.16 [−0.34, 0.66] (unregistered). EB-shrunk edges beat zero (D0 1.71 × 10⁻³, B).
- f. A1's two-sided interval includes 0. The PH6 wave set is retrospective; without the six keywords inspected first,
  −1.7 (p 0.33).
- g. Held-out trend has the opposite sign (+3.2 pp per year).
- h. Uninformative (power 0.47 at the discovery effect). Rows 13–16 differ in population and unit: compare
  replication status, not size.
- i. Newcomer control −5.0; link-removed text −5.39; early map −5.2; correlation with the newcomer flag −0.57.
- j. Co-author composition may explain half or more.
- k. Underpowered at the discovery size; Holm within module only (≈0.17 across modules); early-map insider +3.0;
  keyword-defined insider +0.0.
- l. Hindsight variants were negative in discovery but fail on held-out papers; effects below about 5 pp per log
  unit cannot be told from zero.

**Caption (exact):** "The herding account tested at three points. Each row is one observable, the sign that
imitation predicts, and the sign that continuity or the named alternative (lock-in, absorptive capacity, priority)
predicts. Estimates are percentage points with 95% intervals unless noted, associations within topic and year
(keyword rows: against all other papers of the same year). Row 1 compares two topic maps fitted on different years.
Held-out: a pre-registered out-of-sample replication on released papers, not a certified untouched holdout; held-out
tests are one-sided and confirm direction, not size, so a supported test can have an interval that includes 0.
Codes: P uses only earlier submissions or lagged shares; H✓/H✗ registered hindsight variants pass/fail; R
retrospective by construction; T✓ discovery estimate held after removing links from post-decision abstracts.
Tiers: A registered and replicated; B post hoc, then supported by a declared held-out test; C registered,
inconclusive or not replicated; D discovery only; E descriptive. Full table of every registered and declared test:
Appendix D."

**Space rule.** If the page limit binds, move row 3 into the Figure 2 caption first, then merge rows 14-15. Never drop
rows 8, 9, 12 or 13 (the honest nulls and failures).

### D.2 Table 2 (single column, §7.1): "Where conformity shows, by route and site"

| | Producers (what is written) | Gate (what acceptance goes with) |
|---|---|---|
| **Imitation** (others now) | Not among newcomers: registered follow-on prediction reversed (A); first-time teams later onto FMs and rising keywords (E); fewer twins (E). Flocking untested (C). Imitation-like spread only in title form (E\*). | No detectable premium for crowding (C); branded titles at the submitted rate (D\*); topic edges regress (B); late riding not favoured (B weak). |
| **Continuity** (a record) | Incumbents write more measurement papers (A); the package travels with an ICLR record (E); incumbents' content closer to earlier work, partly their own (E). | Lower far from the team's own record (B); higher for a closer paper by the same author (B); higher with a topic insider (B); same author new to a topic −1.4 (D). |

Caption: "Tiers in parentheses. Cells summarise Table 1 and Sections 4-6; no new estimates."

---

## E. Figures (four, including the existing Figure 1)

All figure scripts read only committed result files or outcome-free label files. No figure script reads an outcome
or decision column. A new script (e.g. `research/fashion/paper/make_figures.py`, extended) is written by the repository
owner; agents do not write into the repository.

### Figure 1 (exists; `figure*`, top of page 1 or 2; §1.1)

- **File:** `/home/user/cloud-research/research/fashion/paper/figs/fig1_waves.pdf`, built by
  `research/fashion/paper/make_figures.py` from the discovery corpus keywords (outcome-free). No change to the file.
- **Message:** ML's waves are vivid; this is the picture that invites a herd reading.
- **Layout:** 2 × 4 small multiples (GANs, adversarial attacks, meta-learning, graph neural nets, federated learning,
  self-supervised, diffusion models, large language models), share of submissions 2018–2026, peak marked.
- **Caption (exact):** "Research waves at ICLR: share of discovery submissions listing each author keyword,
  2018–2026; dots mark the peak. The eight keywords were chosen for display after their curves were known. Across
  the 68 most frequent keywords, 17 peaked in 2019–2024 with shares of at most half the peak both before it and in
  2026 (pooled corpus; Section 6.5). Outcome-free."
- Quote Figure 1's own peaks in the text (GANs 8.1% in 2018; large language models 16.7% in 2026). The DP:80 keyword
  shares are pooled; if quoted, say "pooled corpus".

### Figure 2 (single column, two stacked panels; §4.2-4.3): "One package, fewer fashions than hindsight shows"

- **Message:** how many waves a field shows depends on when the map was fitted; the package shift does not.
- **Panel (a), bars:** emerging topics per map, x-axis ordered by fitting years: 2017–20 (8), 2021–23 (10),
  year-balanced (16), 2024–26 (28), all-years seed refit (28), all-years (29); declining topics as dots (17, 17, 26,
  6, 15, 13); bar labels = share of 2024–26 papers in emerging topics (22.3, 20.9, 42.2, 31.0, 40.9, 40.9%).
  - Source: `research/topics/output/hindsight_check.json`, keys `maps.{early, middle, balanced, late, seed_refit,
    pooled}.{emerging_topics, declining_topics, late_paper_share_in_emerging}`; rule from `ratio_rule`.
  - Existing rendering to adapt: `research/fashion/presentation/figs/hindsight_emerging.pdf`.
- **Panel (b), lines:** share of submissions that build on a foundation model (0.3% → 54.4%) and that propose a new
  architecture (24.5% → 7.5%), 2017–2026; inset text "H1d: −7.98 [−12.14, −3.82] discovery; −11.0 [−18.1, −3.9]
  held-out (A)".
  - Source: `research/topics/output/paper_contributions.csv.gz`, columns `year`, `foundation_model` (== "yes"),
    `primary_type` (== "model"); inset from `research/fashion/output/rq1_results.csv` (row hypothesis H1d, variant
    main: `coef`, `se`) and `research/fashion/output_pooled/confirmation_run/h1d.csv` (row H1d, main: `coef`,
    `ci95_lo`, `ci95_hi`).
  - Existing rendering to adapt: `research/fashion/presentation/figs/fm_trend.pdf` (`presentation/make_figures.py`,
    `fm_trend()`).
- **Caption (exact):** "(a) Emerging topics (2024–26 share at least three times the 2017–20 share; bars) and
  declining topics (at most a third; dots) on k = 100 SPECTER2 topic maps that differ only in the years used to fit
  them; same 43,480 papers and pipeline. Labels: share of 2024–26 papers in emerging topics. Maps fitted without
  2024–26 papers cannot represent topics born after 2020, and the maps differ in fitting corpus as well as window, so
  the counts bracket the effect of hindsight rather than pin it down. Topic size 'predicts' two-year growth out of
  time only on the all-years map (R² 0.28 vs −0.03; no paired test). (b) Share of submissions building on a
  foundation model and proposing a new architecture (LLM labels). Inset: registered H1d, change in the
  new-architecture share for prior-year FM adoption from 0 to 100% within topic and year (tier A; the held-out test
  confirms direction, not size). No acceptance data are used."

### Figure 3 (single column, two panels; §5.2, §5.5): "Newcomers propose and come later to the package"

- **Message:** on every entry measure, newcomers differ from incumbents in the direction opposite to the one herding
  predicts.
- **Panel (a), dot-and-interval rows:** newcomer minus incumbent paper, within topic × year, pp of share: method paper
  (discovery +3.71 [+2.61, +4.80] filled; held-out +3.60 [+1.48, +5.71] open; A); benchmark/dataset/evaluation paper
  (−1.70 [−2.46, −0.93]; −2.10 [−3.35, −0.85]; A); has an independent same-year twin (−3.86 [−4.98, −2.74], class, FM and team-size controls; E). A
  separated fourth row, labelled with its own population: first-time minus returning teams, Emerging-keyword use
  (−3.74 [−5.14, −2.35]; E). A grey arrow on each row marks the sign herding predicted (H2b −, H2c +, twin +,
  Emerging +). Tier letter at right.
  - Sources: `research/fashion/output/frozen_run/rq2_results.csv` (rows hypothesis H2b and H2c, variant main:
    `coef`, `ci95_lo`, `ci95_hi`); `research/fashion/output_pooled/confirmation_run/rq2_rows.csv` (same rows,
    held-out); `research/fashion/output/posthoc/ph5_position/free_herding.csv` (row `newcomer`);
    `research/fashion/output/posthoc/ph5_kwtiming/free_profile_states.csv` (row `young_rising`). Multiply by 100.
  - Existing rendering for H2b/H2c: `research/fashion/presentation/figs/newcomers.pdf`.
- **Panel (b), two series by prior FM-adoption bin (0–5, 5–15, 15–30, 30–50, ≥50%):** FM-paper gap, first-time team
  vs returning topic newcomer (filled: −0.95, −4.58, −8.96, −14.71, −1.96) and returning topic newcomer vs incumbent
  (open: +1.10, −0.41, −2.58, +2.87, −1.01), 95% intervals.
  - Source: `research/fashion/output/posthoc/ph5_fmwave/free_entry.csv` (columns `term`, `bin`, `coef`,
    `ci95_lo`, `ci95_hi`), × 100.
- **Not in the figure:** the content-distance gap (its output is a workspace file, not a committed output); it stays
  in Table 1 and §5.4. Add it as a fifth row of panel (a) only if the script and output are committed (Section H).
- **Caption (exact):** "(a) Newcomer minus incumbent papers within topic and year, discovery (filled) and held-out
  (open), with the sign the registered herding prediction expected (arrows). The last row compares first-time with
  returning teams. A method paper is a contribution type, not a measure of novelty. (b) Gap in the share of
  foundation-model papers by the topic's prior-year adoption, 2023–2026 submissions, with class and team-size
  controls. Labels are LLM labels on partly camera-ready abstracts. Flocking into hot topics (inconclusive) is not
  shown. No acceptance data are used."

### Figure 4 (single column, two panels; §6.2-6.4): "Acceptance goes with the record"

- **Message:** at the gate, the record-referenced tests held on held-out papers; the crowd- and field-referenced tests
  are uninformative or not supported.
- **Panel (a):** adjusted acceptance by fifth of F_max (far → near), discovery decided 2023–26 papers with an
  experienced author: 39.7 [38.1, 41.2], 41.8 [40.3, 43.3], 44.4 [43.1, 45.8], 47.2 [45.8, 48.6], 46.9 [45.2, 48.6]%
  (tier D shape), annotated "held-out E1: −6.09 [−9.32, −2.86] (B)".
  - Sources: `research/fashion/output/posthoc/ph5_pivot/quintiles.csv` (rows `model` = "P1 F_max quintiles
    (adjusted P(accept))": `quintile`, `coef`, `ci95_lo`, `ci95_hi`, `papers`); held-out from
    `research/fashion/output_pooled/confirmation_run/ph5/tests.csv` (row `test` = E1).
  - Existing rendering to adapt: `research/fashion/presentation/figs/far_jump.pdf`.
- **Panel (b):** six small rows in two labelled groups, each with its own x-axis, unit and zero line; discovery open,
  held-out filled; verdict and MDE80 or power printed at right. *Referenced to a record:* far jump E1 (−5.44 / −6.09;
  supported; MDE80 4.9), within-author closeness E4 (+0.55 / +1.06; supported), one insider (+3.42 / +3.88;
  supported; MDE80 ≈4.5). *Referenced to others or the field:* crowding H3a (−1.68 / −1.51; uninformative; MDE80 4.8),
  least-distant fifth P1b (−3.27 / −0.13; uninformative; power 0.47), within-author field distance P7 (+0.39 / +0.34;
  not supported).
  - Sources: discovery `research/fashion/output/posthoc/ph5_pivot/tests.csv` (E1, E4),
    `research/fashion/output/posthoc/ph5_teams/family.csv` (H1), `research/fashion/output/posthoc/ph5_position/tests.csv`
    (P1b, P7), `research/fashion/output/frozen_run/rq3_results.csv` (H3a, main); held-out
    `research/fashion/output_pooled/confirmation_run/ph5/tests.csv` (E1, E4, H1, P1b, P7: `coef`, `ci95_lo`,
    `ci95_hi`, `verdict`, `power_at_discovery_effect`) and `research/fashion/output_pooled/confirmation_run/rq3_rows.csv`
    (H3a, main).
- **Caption (exact):** "(a) Adjusted acceptance by fifth of closeness to the team's own earlier ICLR work (discovery,
  decided 2023–2026 papers with an experienced author; tier D shape) and the declared held-out contrast (tier B).
  (b) Discovery (open) and held-out (filled) estimates of the gate tests, grouped by reference point. Rows differ in
  population and unit, so compare replication status, not size. Held-out tests are one-sided; B rows were post hoc in
  discovery; E4 and the insider test are secondary and unadjusted. Associations within topic and year."
- **Page rule:** if the paper exceeds eight pages, move panel (b) to the appendix first.

---

## F. Limitations, ethics statement and appendix plan

### F.1 Limitations (ACL-required; 224 words; ready to use)

> All results are associations at one venue; none is a causal effect of a topic, team or contribution type. The
> held-out set is a pre-registered out-of-sample replication, not a certified untouched holdout: it shares
> conference-years, reviewer pools and authors with the discovery papers, so it guards against analyst overfitting but
> not against year- or reviewer-specific patterns, and supported tests confirm direction, not size. The continuity
> results were found post hoc; their held-out tests were declared in advance, but two of the three are among six
> secondary tests run one-sided and unadjusted. Under one simulated null the main entry tests rejected 12.6% and 10.0%
> of the time at a nominal 5%. Contribution and foundation-model labels are LLM labels checked against LLM labels, and
> abstracts are partly camera-ready; links were removed and the text re-embedded for discovery papers only. Entry
> status counts ICLR submissions only, and the 2021 switch from e-mail to profile identifiers hides earlier histories,
> which biases entry contrasts towards zero. Withdrawn papers are left out of acceptance tests. Whether entrants crowd
> into hot topics is untested, and the absence of a premium does not rule out unrewarded bandwagons. The hindsight
> comparison is a bracket, because the maps differ in fitting corpus as well as window. The content-distance comparison
> was added during writing, is unregistered, and is partly built into the definition of incumbency.

Sources: DC:42-45, 47, 52, 56, 77-78, 145-149, 249-250, 295, 318; DP:29-30, 373; TA:280-286; DC:229; NN caveats.

### F.2 Ethics statement (after Limitations; about 70 words)

> Author identifiers were used only as keys to compute entry status and closeness; no author is named and all results
> are aggregates. The data are public OpenReview records, collected in our own dated acquisitions under the platform's
> terms. No review scores are used. Contribution labels were produced by an LLM (Claude Haiku) with a fixed codebook;
> agreement figures compare LLM labellings, not human judgement.

Sources: DC:62, 71, 130, 144; DC:52.

### F.3 Appendix plan

| App. | Content | Sources | Why not main text |
|---|---|---|---|
| A | Data provenance: acquisitions, reconciliation, papers by year (discovery and held-out), held-out release (1,309 pending cases excluded by the source), Re² audited and not pooled (`zhang2025re2`), Paper Copilot and the Louis archive used only for comparison | DC:62-78 | Detail |
| B | Measurement validation: topic quality, k-sensitivity tables (2b, 2c), label agreement and error rates, keyword canonicalisation (40,930 expressions) and held-out keyword map, earlier-version detection, dropped buzzword measure | DC:86-155, 262 | Instrument detail |
| C | Hindsight details: all six maps (ARI, fit by year), diversity by year per map ("not a finding"), forecast metrics and size terciles (40/21/2% vs 22/20/20%), lifecycle flip with all variants | DC:174-231 | Supports §4.2 |
| D | Every registered and declared test: the full held-out table with MDE80 and verdicts (incl. P7, EB D0, H4-FL trend, PH6 variants), unregistered held-out rows (labelled "not interpreted"), pooled re-run ("confirms nothing"), H1a-c, H1e, H2a, H3b | DC:268-386; DP:389-397 | Audit trail |
| E | Content-distance analysis: definition (reimplements the position module's measure at K = 10; own earlier-version chain removed), every specification and sensitivity (excl. 2021 +5.87; newcomer_s4 +5.84; no earlier version +5.81; plain definition +6.63), by year (2019 +1.26, p 0.70; 2021 rests on about 11 incumbent papers, do not interpret), correlation 0.74 with the plain definition, the six caveats; "added during writing, outcome-free, unregistered" | NN | Full transparency |
| F | Other gate modules, all D or with quoting rules: team size (+8.8 pp per doubling), PH1 newcomer correlates, PH3 details, PH4 areas and federated-learning mechanism probes, E3 withdrawal after review (+1.62), E1 FM premium and E8 against the tide, E10 acceptance by class, P2 twins (all three rows together), E2 near closeness (with its rule), keyword winner's curse, insider decomposition and H2-H6, interactions with topic heat, cleantext re-run | DC:342-351, 394-397; DP:142-347 | Off the spine or discovery only |
| G | Title style: definitions D1-D4 and yearly shares (E\*), the 1.02 ratio (D\*, earlier exploratory, not re-run) | DP:89-136 | Earlier exploratory |
| H | Size calibration: dry-run nulls, bootstrap, two-way clustering, family-wise error under the cross-map null, MDE80 tables | DC:248-260 | Methods detail |

---

## G. Wording guardrails specific to this story

### G.1 Definitions at first use (fixed; never vary in the text)

| Term | Definition (first use) | Source |
|---|---|---|
| Imitation | Conformity whose reference point is what others are doing now (popularity, momentum, what is hot) | TA:48-52, 559-566 |
| Continuity | Conformity whose reference point is an accumulated record: the team's own past work, or a topic's past work carried by a team member who has already submitted in it. Operationally, a position of a paper's content relative to a record, not the possession of one. | TA:567-575; J2 §6 |
| Anchored | Title and one defined use only. Footnote (exact): "We use 'anchored' for work that conforms by continuity, a position relative to a record; it is not the anchoring-and-adjustment heuristic (Tversky and Kahneman, 1974), the sense in which writing on herding in science uses the word (Baddeley, 2015)." | TA:509-518 |
| Positions, not motives | These words label positions of papers. Never "teams choose to stay close". | TA:630-631 |
| Topic | One of 100 clusters of SPECTER2 embeddings of title and abstract (spherical k-means), fitted on all years unless a map is named | DC:86-87 |
| All-years / 2017–20 (early) / 2021–23 / year-balanced / 2024–26 map | k = 100 maps fitted on all papers / 2017–2020 papers / 2021–2023 papers / all years with equal weight / 2024–2026 papers; same papers assigned to each | DC:174-181; HC |
| Emerging / declining topic | 2024–26 share at least 3× / at most 1/3 of the 2017–20 share | DC:183 |
| Newcomer paper | No author ID has an earlier ICLR submission, with any outcome, in the paper's topic, strictly before year t. Never "no author published". Incumbent paper: at least one has. | DC:53, 144 |
| First-time team | No author ID has any earlier ICLR submission, in any topic, with any outcome | PRE:1281 |
| Returning topic newcomer | A newcomer paper with at least one author who has an earlier ICLR submission in another topic | PRE:1112 |
| Topic insider | An author with at least one earlier ICLR submission (any outcome) in the paper's topic; histories since 2021; estimated at fixed team size and number of experienced authors, so it measures topic familiarity net of general ICLR experience. A proven record is not required. | PRE:1567-1569, 1659 |
| Method / measurement / new-architecture / FM paper | LLM-codebook primary class method (incl. new architectures) / dataset-benchmark or evaluation / primary type "model" / uses or adapts a large pre-trained model. A contribution type, not novelty. | DC:129, 137-138, 313-314 |
| Prior FM adoption | Share of a topic's papers in year t−1 that are FM papers | DC:153 |
| Crowding | log(1 + number of earlier papers in the topic); registered as "maturity". Hot topic: top 20% of prior growth that year. | DC:153 |
| F_max (far jump) | For each experienced author, the cosine between the paper's centred, L2-normalised SPECTER2 vector and the normalised mean of that author's earlier ICLR submissions since 2021, excluding the paper's probable earlier version and any paper at cosine ≥ 0.90; F_max is the maximum over experienced authors. Far jump = acceptance at the 10th percentile of F_max minus the median. | PRE:1372-1380 |
| Within-author closeness | The same author's papers compared by prior cosine, author fixed effects, per +0.1 cosine | DP:241-243 |
| Distance from earlier ICLR work (field distance) | 1 − mean cosine to the 10 nearest submissions from strictly earlier years (centred SPECTER2), as a percentile within topic × year. Never "novelty" or "originality" in the text. | DP:255; NN |
| Same-year twin | An independent same-year submission at cosine ≥ 0.70 | DP:78, 267 |
| Emerging / Mainstream / Cooling keyword | Young (1–2 years since the cumulative count first reached 10) × rising (top tercile of lagged share growth) / old (≥ 5 years) × flat / old × falling | PRE:1258-1261 |
| Wave (PH6) | A keyword whose share peaked in 2019–2024 with at most half the peak before it and in 2026; retrospective by construction | DP:81; RESULTS L968-969 via DP |
| Topic edge; slope b | A topic's acceptance minus that of all other papers of the same year; b = slope of the 2024–26 edge on the 2018–22 edge (early-map topic units) | DP:326 |
| Held-out | "A pre-registered out-of-sample replication, not a certified untouched holdout"; it shares years, reviewers and authors with discovery | DC:43-45 |

### G.2 Verbs and phrases

- **Use:** "goes with", "is associated with", "is lower/higher", "acceptance goes with", "fewer … where adoption is
  higher", "no detectable premium", "uninformative", "not confirmed", "undetermined", "post hoc, supported on held-out
  papers", "replicated" (tier A only), "tested again" (for the whole set), "inflates" (hindsight), "consistent with".
- **Never:** "causes", "drives", "crowds out", "displaces" with FM as subject, "choose", "should", "the gate rewards"
  or "penalises" as causal verbs, "bias", "discount", "manufactures", "illusion", "artefact" (for waves), "ML is not
  a herd", "reviewers (do not) herd", "entrants are more innovative/original/novel", "first", "confirms Bommasani",
  "topic choice is not rewarded", "exploitation" as a name for continuity, "foresight" or "later papers" for the
  held-out split, "replicated" for a B result, "no effect" for an underpowered null, any advice ("add an insider",
  "stay close").
- **Novelty claims** always carry "to our knowledge, among the works we checked".
- **Numbers from cited papers:** none (Hill's 35%, Movva's "half", Stelmakh's sample size, Wang's acceptance rates
  were seen only in search snippets; VP:33-36).

### G.3 Quoting rules that travel with findings

- H2b′/H2c′: always say the original registered herding prediction failed (DC:33-36).
- Supported held-out tests underpowered at the discovery effect (H1d, H2c′, insider, A1) confirm direction, not size;
  never read a larger held-out estimate as a larger effect; never compare effect sizes across modules (DC:47, 380, 428).
- A1: say the two-sided interval includes 0. PH6: say it leans on the six keywords inspected first and that its wave
  set is retrospective. Federated learning: "not confirmed", never "scam". P1b: "did not replicate", "uninformative",
  "undetermined"; never "the gate ignores field distance". Crowding: "no detectable premium".
- P2 (concurrent twin) and E2 (near closeness): quote only with the held-out and pooled rows (DP:36-41); appendix.
- Title ratio 1.02: "earlier exploratory, not re-run" (D\*). Do not quote the returning-author title lag or the LLM
  title verbs (E\*, not re-verified).
- Do-not-quote list (DP:56-61): teams H5; position cells; P6; fmwave spline, C1, B1/B2; pivot sweet spot; premia
  asymmetry and named lists; top-tenth retention; saturation readings; off-trend +2.0; E4/P7 as standalone; P7 as
  Holm-significant; 2019-20 replications; mechanical results; uncommitted verifier numbers.
- Pooled re-run "confirms nothing"; unregistered held-out rows are "reported, not interpreted".
- Labels are LLM labels; agreement "shows consistency between LLM labellings more than human-level validity".

### G.4 Citation-use rules

- Cite for the general argument only (content seen in secondary descriptions; TA:665-676; FW:107):
  `fujimura1988molecular`, `dimaggio1983iron` (mimetic section), `scharfstein1990herd`, `kitcher1990division`,
  `strevens2003role`, `levitt1988organizational` (no "competency trap" quotation), `baddeley2015herding` (footnote
  only), `xiang2025research` (abstract-level claims only).
- Quote verbatim only Bourdieu (read in full) and the abstract phrases of Xiang et al. and Weisberg and Muldoon.
- Do not use "sharing the blame" for Scharfstein and Stein (TA:296-297).
- Partly verified entries: cite `jung2025what` as the arXiv version; `xu2026reviewer` as "Xu et al." (two middle
  authors unresolved).
- Use only keys present in `paper_ws/references_merged.bib` (78 entries, all verified; compiled cleanly with
  `acl_natbib.bst`).

### G.5 Formatting

- Minus sign "−" for negatives, en dash for ranges, "pp" for percentage points, intervals in square brackets, tier in
  parentheses after the interval. Year ranges "2017–2026" in the text.
- Report discovery first, then held-out: "−5.44 [−7.10, −3.78] in discovery, −6.09 [−9.32, −2.86] held-out (B)".

---

## H. Open items (none blocks writing)

1. **Content-distance decomposition (outcome-free; recommended by all three judges).** Re-run
   `paper_ws/scripts/novelty_newcomer.py` with every earlier submission by any of the paper's own authors removed from
   the reference set (author IDs as join keys only, never printed), and on 2017–20-map topic × year cells. Then:
   - if the gap stays clearly positive, §5.4 may drop "partly by construction" in favour of "the gap remains when the
     authors' own earlier papers are excluded", and one clause ("and, descriptively, farther from earlier work") may
     enter the abstract if a word is cut elsewhere;
   - if it shrinks towards zero, §5.4 says the incumbent side's closeness is largely self-continuation, which is
     itself continuity among producers, and Table 1 row 6 is relabelled "for continuity (incumbents)".
2. **Commit the content-distance script and outputs** (`paper_ws/scripts/novelty_newcomer.py`,
   `paper_ws/output/novelty_newcomer.{json,csv}`) to the repository with a note "added during writing, outcome-free,
   unregistered", and cross-check against the position module's cached features (NN caveat 6). Only the repository
   owner can do this; agents may not write into the repository.
3. **Dossier additions:** the FE "topic newcomer (vs incumbent)" rows, the FE confidence intervals, the FH first-time
   share (26.3%) and the FPS intervals listed in 0.3 (verified here from committed files).
4. **Theory originals:** read March 1991 (turnover), Levitt and March 1988, Kitcher 1990, Strevens 2003, DiMaggio and
   Powell 1983 (mimetic section), Scharfstein and Stein 1990 and the body of Xiang et al. 2025 before citing any
   specific result (hosts listed at TA:42-44 must be allowed).
5. **Bibliography:** EMNLP 2026 author order of Jung et al. and the middle authors of Xu et al. (cite arXiv until
   resolved); Biliotti et al. version year.
6. **ARR call:** confirm the current long-paper page limit (eight content pages assumed) and choose the
   computational-social-science area.
7. **Title ratio (D\*):** keep it as one clause labelled "earlier exploratory, not re-run", or have it re-run
   outcome-blind through the frozen machinery by the owner.
8. **Figures 2-4:** extend the repository's outcome-free figure script to read exactly the files and rows listed in
   Section E.
