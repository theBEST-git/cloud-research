# Story P4: "The Herd in Hindsight" (the ACL / NLP framing of one story line)

Built 2026-11-03 as a story design for the ACL ARR long paper. It is a design, not the paper: it fixes the title,
thesis, conversations, novelty wording, abstract, contributions, section-by-section argument, Table 1, figures and
the honest limits. Only sentences whose exact wording matters are written out.

## 0. Sources, conventions and what this design is for

**Audience.** An ACL ARR senior area chair who cares about three things:
1. computational (NLP) methods for studying science;
2. the hindsight lesson for the ACL genre of "computational histories of the field";
3. LLM-era debates about hype and herding in ML and NLP.

**What P4 keeps and what it changes.** P4 keeps the substance of landscape.md Candidate 1 ("Anchored, not herded")
and the imitation/continuity frame of theory_anchors.md. It changes the spine: **reading forward versus reading
backwards** organises every act. In each act the herd-like signal is first read backwards (fitted with hindsight, or
formed and judged on the same papers), then read forward (prospective measures, registered tests, held-out papers),
and the paper reports what survives. The herd story is the one hindsight tells best; what survives forward reading
is a package, proposing entrants and continuity at the gate. This is one story line, not a methods note with
findings appended: the forward-reading discipline is the test, and the findings are its verdicts.

**Pointers** (all files read in full or at the stated lines; no data file, outcome column or forbidden script was
opened or run):

| Pointer | File |
|---|---|
| `DC:n` | `paper_ws/dossier_core.md`, line n |
| `DP:n` | `paper_ws/dossier_posthoc.md`, line n |
| `LS:n` | `paper_ws/landscape.md`, line n |
| `VP:n` | `paper_ws/verify_prior.md`, line n |
| `TA:n` | `paper_ws/theory_anchors.md`, line n |
| `NJ` | `paper_ws/output/novelty_newcomer.json` (the new novelty analysis; `analysis_novelty.md` was not written, so the JSON is the source) |
| `PRE:n` | `research/fashion/PREREGISTRATION.md`, line n (definitions only) |
| `RES:n` | `research/fashion/RESULTS.md`, line n |
| `TOP` | `research/topics/README.md`, "Hindsight check" |
| `lit` | the `lit_*.md` / `lit_*.bib`, `verify_prior.bib`, `theory_anchors.bib` keys |

**Tiers** (DC:25-31; DP:12-19): **A** registered and replicated on held-out papers; **B** post hoc in discovery,
then a held-out test declared before the held-out run, supported; **C** registered but inconclusive or not
replicated; **D** discovery only; **E** descriptive, no acceptance outcome; **E\*** earlier title analysis,
outcome-free share re-verified; **D\*** earlier title analysis, acceptance ratio not re-run.

**Two facts checked for this design** (both close open items):
- The far-jump measure F_max uses the centred SPECTER2 vector of title [SEP] abstract (PRE:1373, 1379-1380). So
  "our closeness measure follows Bao and Li (2025), who use SPECTER2 similarity to a researcher's own earlier papers"
  is accurate (closes VP:495-498).
- The keyword timing states behind A1 are prospective: onset is the first year a keyword's cumulative count reaches
  10, and momentum is share t−1 over share t−2 (PRE:1258-1262). The PH6 wave set is retrospective: a keyword counts
  as a wave only if its share peaked in 2019-2024 and fell to at most half the peak by 2026 (RES:968-969). The paper
  must say so (Section 8, W9).
- Every paper has a topic in each hindsight map (`hindsight_assignments.csv.gz`; TOP), so "same papers" holds for the
  29-vs-8 comparison. The early map fits 2017 papers better than 2026 papers (0.69 vs 0.53; TOP), so it cannot
  represent topics born after 2020: 8 is the low end of a bracket, not the true count.

---

## 1. Title and thesis

### Title

**The Herd in Hindsight: Reading Machine Learning's Foundation-Model Wave as It Unfolded**

Alternatives:
- *Read Forward: Entry, Continuity and Review in Machine Learning's Foundation-Model Wave (ICLR 2017–2026)*
- *A Herd Only in Hindsight? Who Carried Machine Learning's Foundation-Model Wave, and What Review Went With*

(Avoid "manufactures", "illusion" or "is not a herd" in the title: the field-level convergence is real (A), and the
flocking half of herding is untested (C).)

### Thesis (the story line, one sentence)

> Read backwards, machine learning's foundation-model wave looks like a herd; read as it unfolded — with measures
> that see only the past and registered predictions replicated on held-out papers — it is convergence on a shared
> technical package, carried by topic entrants who propose rather than imitate, through a review gate that goes with
> continuity to a team's own record rather than with following the crowd.

### The spine (every section serves it)

| Act (section) | The herd story, read backwards | The same question, read forward | What survives (tier) |
|---|---|---|---|
| 1. The waves (§4) | An all-years topic map finds 29 emerging topics; topic size "predicts" growth (R² 0.28); the share of papers with a same-year twin rises from 19.5% to 48.8% | A 2017-20 map finds 8; size does not predict growth (R² −0.03); twins per paper per 1,000 submissions fall from 0.32 to 0.19 | Convergence on a package: where prior FM adoption is higher, fewer new-architecture papers, −8.0 discovery, −11.0 held-out (**A**) |
| 2. The people (§5) | Entrants flood a hot field and write follow-on work (our own registered prediction; the herding account) | The registered test, run once and replicated: reversed. Entrants' papers sit further from strictly earlier work; first-time teams adopt the package and trending keywords more slowly | Entrants propose: method +3.60, measurement −2.10 held-out (**A, reversed**); novelty +5.90 percentile points (**E**); FM uptake −4.6 to −14.7 pp (**E**) |
| 3. The gate (§6) | Vivid in-sample signals: federated learning's gap (−11.3), a least-novel-fifth penalty (−3.27), topic edges | Held-out: federated learning −4.9 (uninformative), least-novel fifth −0.13 (uninformative), topic edges regress (b 0.60); crowding uninformative | Continuity: far jump −6.09, within-author closeness +1.06, one insider +3.88 held-out (**B**); arriving early, weakly (**B weak**) |

**The memorable formulation:** *Hindsight tells the herd story; foresight tells a different one.* (Echoes Fischhoff
1975, "Hindsight ≠ foresight"; `fischhoff1975hindsight`, verified VP:376.)

### Definitions the whole paper uses (fixed; do not vary)

| Term | Definition | Source |
|---|---|---|
| **Reading forward** | (a) *Temporal*: a measure for year t uses only submissions before t (or lagged shares), or the claim must also hold on topic maps fitted without later years. (b) *Inferential*: a claim formed on discovery papers counts as replicated only if a test declared before the held-out run supports it. Reading backwards is the opposite on either axis. | design, from PRE "Decision rule" (DC:239) and DC:43-45 |
| **Imitation** | Conformity that refers to what others are doing now: popularity, momentum, hot topics. | TA:559-566 |
| **Continuity** | Conformity that refers to an accumulated record: the team's own past work, or the topic's past work carried by a team member. "Anchored" only as a defined adjective, with a footnote: not the anchoring heuristic (Tversky and Kahneman 1974). | TA:567-574 |
| **Newcomer paper** | No author ID has an earlier ICLR submission (any outcome) in the paper's k100 topic, strictly before year t. Not "no author published". | DC:53, 144 |
| **First-time team** | No author ID has any earlier discovery submission, in any topic, with any outcome. | PRE:1281 via TA:684-685 |
| **Topic insider** | An author with at least one earlier ICLR submission (any outcome) in the paper's k100 topic; estimated at fixed team size and number of experienced authors. A proven record is not required. | PRE:1569, 1659 via TA:587-591 |
| **Far jump** | F_max, the cosine (centred SPECTER2) between the paper and the closest experienced co-author's earlier ICLR submissions since 2021; contrast p10 vs p50. | PRE:1373-1380; DP:231-233 |
| **Method / measurement paper** | LLM-codebook primary contribution type; measurement = dataset/benchmark or evaluation. A contribution *type*, not novelty. | DC:129, 137, 313-314 |
| **Novelty (field distance)** | 1 − mean cosine to the 10 nearest submissions from strictly earlier years (centred SPECTER2), as a percentile within topic × year. | NJ; DP:255 |
| **Emerging keyword** | Young (1-2 years since onset) × rising (top tercile of lagged growth) — a prospective state. | PRE:1258-1262 |
| **Emerging topic** | 2024-26 share ≥ 3× its 2017-20 share. | DC:183 |
| **Held-out** | "A pre-registered out-of-sample replication, not a certified untouched holdout"; it shares years, reviewers and authors with discovery. | DC:43-45 |

---

## 2. Conversations, gap, novelty wording, and why it matters beyond ICLR

### 2.1 The conversations (primary first)

1. **Computational histories of NLP and ML (primary; ACL-native).** The genre fits one topic model on a whole
   archive and reads trends forwards: Hall, Jurafsky and Manning (2008, EMNLP) on the ACL Anthology; Anderson,
   Jurafsky and McFarland (2012) on people flows; Pramanick et al. (2023, EMNLP) on paradigm shifts ("methods drive,
   datasets follow"); Gururaja et al. (2023, EMNLP) on explore/exploit cycles; Schäfermeier, Stumme and Hanika (2021)
   on ML topic trajectories; Klinger et al. (2020) on narrowing; BERTopic-style "topics over time"
   (Grootendorst 2022). Keys: `hall2008studying`, `anderson2012towards`, `pramanick2023diachronic`,
   `gururaja2023build`, `schafermeier2021topic`, `klinger2020narrowing`, `grootendorst2022bertopic`.
   **What we add:** the size of the hindsight distortion on the same papers, which trend claims survive forward
   reading, and the producers' and the gate's side of the same waves.
2. **LLM-era debates about hype and herding in ML (secondary; the ACL audience's live debate).** Rhetoric and growth
   (Lipton and Steinhardt 2019, Queue), the hardware and benchmark lotteries (Hooker 2021; Dehghani et al. 2021),
   homogenisation around foundation models (Bommasani et al. 2021), benchmark concentration (Koch et al. 2021),
   entry into LLM research (Movva et al. 2024, NAACL), history-repeats readings (Saphra et al. 2024, NAACL), and the
   efficiency counterpoint (Sutton 2019). Keys: `lipton2019troubling`, `hooker2021hardware`,
   `dehghani2021benchmark`, `bommasani2021opportunities`, `koch2021reduced`, `movva2024topics`, `saphra2024first`,
   `sutton2019bitter`. **What we add:** a registered, held-out test of the herding reading at entry and at the gate,
   rather than essays, interviews or descriptive trends (LS:315-319).
3. **Two routes to conformity (science of science; the theory that makes the test discriminating).** Imitation
   (cascades: `bikhchandani1992theory`, `banerjee1992simple`; mimetic isomorphism: `dimaggio1983iron`; modes of
   imitation: `haunschild1997modes`; reputational herding: `scharfstein1990herd`; bandwagons:
   `abrahamson1993institutional`) versus continuity (local search: `stuart1996local`; exploitation:
   `march1991exploration`; absorptive capacity: `cohen1990absorptive`; succession strategies and consecration:
   `bourdieu1975specificity`; pivot penalty: `hill2025pivot`; chaperones: `sekara2018chaperone`; persistence in ML:
   `bao2025persistence`). The formal precedent for the split is `weisberg2009epistemic` (followers vs agents searching
   from their own position; cite `alexander2015epistemic` alongside). The gap sentence is `xiang2025research`.
4. **Measurement hygiene for text-as-data (methods; ACL-native).** Temporal leakage (`kaufman2012leakage`,
   `kapoor2023leakage`), time-indexed language models (`lazaridou2021mind`), emergence detection
   (`rotolo2015what`, `li2025evaluation`, `khanbayov2026topical`, `leydesdorff2002dynamic`), confirmatory designs
   (`nosek2018preregistration`, `vandenakker2021preregistration`, `ibrahim2026bias`), LLM text in the corpus window
   (`liang2024mapping`, `kobak2025delving`).

### 2.2 Closest prior work and what each leaves open

| Work (key; status) | What it did | What we add / required narrowing |
|---|---|---|
| Hall et al. 2008; Pramanick et al. 2023; Schäfermeier et al. 2021 (V) | Trends from one model fitted on the whole archive; published papers only | Same papers, same pipeline, only the fitting window differs: 29 vs 8 emerging topics (E). We also observe producers and the decision. |
| Li et al. 2025, PeerJ CS (`li2025evaluation`; V) | Static topic models' ability to detect emergence | Not a refit of one model on early-only vs all-years windows (VP:349-370). |
| Khanbayov and Kurban 2026 (`khanbayov2026topical`; V-arXiv) | Prospective early-warning signature for AI topics, tested on later years | Does not compare hindsight and no-hindsight maps on the same papers. Must be cited in the gap (VP:58). |
| Movva et al. 2024 (`movva2024topics`; V) | Large-scale entry into LLM research on arXiv; descriptive | No contribution type, no rejected papers, no decision. We add what entrants write and how the gate treats position. |
| Gururaja et al. 2023; Saphra et al. 2024 (V) | Interviews and history of NLP paradigm shifts | Qualitative; H1d is a registered, held-out, topic-level instance of an "exploit" phase. |
| Bao and Li 2025 (`bao2025persistence`; V-arXiv) | SPECTER2 similarity to one's own prior ICML/NeurIPS papers across the deep-learning shift; persistence goes with lower impact | **The closeness measure is not new** (VP:123-126). Our outcome is the accept/reject decision on all submissions. The opposite sign (impact there, acceptance here) goes in the Discussion. |
| Hill et al. 2025, Nature (`hill2025pivot`; V) | Larger pivots are cited less and are less often published (2015-2018 preprints) | **Never "first pivot penalty at the gate."** We observe the decision itself, on every submission to one ML venue, under double-blind review, with held-out replication (VP:288-316). |
| Sekara et al. 2018 (`sekara2018chaperone`; V) | Chaperoned newcomers in top journals | Topic-level insider at a double-blind decision, held-out replicated (B). |
| Wang et al. 2023 (`wang2023what`; V) and Xu et al. 2026 (`xu2026reviewer`; P) | ICLR topic clusters differ in acceptance; topic predicts acceptance at equal scores | **Topic differences are documented.** We claim only that the edges regress out of sample (b 0.60) (VP:98-104, 184-186). |
| Jung et al. 2025 (`jung2025what`; P, cite arXiv) | Full ICLR 2017-2025 record; rebuttal, writing, *earlier submission* | Their timing is within a review cycle; ours is within a keyword's life. Define "early" (VP:155-163). |
| Ibrahim et al. 2026 (`ibrahim2026bias`; V-arXiv) | Borderline prestige effect at ICLR; pre-registered out-of-sample test on the 2026 cohort | **Drop any "first confirmatory design" claim (G7).** Rival reading of the insider premium: visible status via preprints (VP:202-218). |
| Stelmakh et al. 2023, PLOS ONE (`stelmakh2023large`; V) | ICML 2020 RCT: no herding detected in reviewer discussions | Pair it: "no herding detected" among reviewers there; entrants do not write the follow-on work herding predicts here. Mention Kargaran et al. 2025 so as not to claim reviewers are independent (VP:265-270). |
| Boudreau et al. 2016 (`boudreau2016looking`; V) | Evaluators score proposals closer to their own expertise, and highly novel ones, lower | Distance runs evaluator → proposal, not authors → own record; do not equate with the far jump (VP:318-337). |
| Biliotti et al. 2024 (`biliotti2024breaking`; V-arXiv) | Same topic-specific newcomer definition (COVID-19, PubMed); expertise offsets the newcomer disadvantage | Precedent for the definition; does not narrow the entry gap. |
| Huang 2026 (`huang2026catalyst`; V-arXiv) | Topic initiators at ICLR precede topic growth | Initiators, not entrants' contribution type or acceptance by entry status. |
| Xiang, Romero and Teplitskiy 2025 (`xiang2025research`; V, abstract read) | Review of topic choice: social context vs path dependence; entry costs and topic rewards open | Best single citation for the gap sentence (TA:453-471). |

### 2.3 Exact novelty wording (drop-in; Introduction or end of §2)

> Studies of ICLR's open records have related acceptance to author prestige and visibility (Tran et al., 2020;
> Ibrahim et al., 2026), to the review process (Jung et al., 2025), and to research area (Wang et al., 2023; Xu et
> al., 2026). Studies of the producers describe who enters machine-learning topics and how far researchers stay from
> their own past work (Movva et al., 2024; Bao and Li, 2025). The science of science shows that moving far from one's
> own record costs citations and publication (Hill et al., 2025). Computational histories of NLP and ML read trends
> from topic models fitted on the whole period (Hall et al., 2008; Pramanick et al., 2023); static models can miss
> small emerging topics (Li et al., 2025), and prospective early-warning signatures for AI topics have been tested on
> later years (Khanbayov and Kurban, 2026). To our knowledge, among the works we checked, no study asks within one
> complete submission population whether the herding account of a field's waves holds at three points: how the waves
> are measured, what kind of work topic entrants bring, and what the review decision goes with. Nor does any study
> test these predictions with registered hypotheses replicated on held-out papers.

The first three sentences and the last two are the verify_prior wording (VP:455-462, summary); the fourth sentence
adds the ACL measurement neighbours with the wording VP:365-368 recommends.

**Required narrowings (all seven from verify_prior, where each lands):**
1. Topic acceptance differences are known (Wang 2023; Xu 2026). Claim only that edges regress out of sample. → §6.1.
2. Hill et al. 2025 already report lower publication success for larger pivots. Say "we observe the decision itself,
   on every submission to an ML venue, under double-blind review, with held-out replication". → §2, §6.3.
3. Bao and Li 2025 already measure SPECTER2 closeness to one's own record; persistence goes with lower impact. →
   §3 (measure credit), §7 (tension).
4. Ibrahim et al. 2026 pre-registered an out-of-sample ICLR test. No "first confirmatory design"; their prestige
   result is a rival reading of the insider premium. → §3, §6.5.
5. Stelmakh et al. 2023: "no herding detected" among reviewers. → §5 opening, §7.
6. Boudreau et al. 2016: evaluator-to-proposal distance, not authors-to-record. → §2 or §6.3 footnote.
7. G4: cite Li et al. 2025 and Khanbayov and Kurban 2026; keep the claim to "same papers, same model, only the
   fitting window differs: 29 vs 8". → §4.1.

**Phrases never to use:** "first study of acceptance by topic"; "first evidence of a pivot penalty at the gate";
"first pre-registered study at an ML venue"; "first to measure distance from one's own work"; "reviewers (do not)
herd"; "hindsight manufactures"; "ML is not a herd"; "the gate rewards/punishes"; "should"; "choose"; any number from
another paper not re-checked against its PDF (VP:477-483).

### 2.4 Why it matters beyond ICLR

1. **For anyone writing a field's history with topic models.** The ACL Anthology, arXiv and Semantic Scholar
   histories all fit one map on the whole period. In our corpus, where 69.3% of papers are from 2024-2026 (DP:72),
   the all-years map counts 29 emerging topics and an early-years map 8 on the same papers. The check that exposes
   this (refit on early years; require trend claims to hold on that map; lag the predictors) costs one refit. The
   reasoning (not a finding) is that the faster a corpus grows, the more its recent years dominate the fit, which is
   exactly the situation of LLM-era corpora.
2. **For the LLM-era hype debate.** The debate is mostly argued from essays and aggregate trends (LS:315). We turn it
   into three falsifiable predictions that any venue with open submission records can test: what entrants write,
   whether following carries a premium at review, and whether the remaining convergence is a package or a herd.
3. **For the science of science.** We separate imitation from continuity in one population, observe the decision
   rather than citations, and find the two routes behave differently at entry and at the gate. Continuity
   associations known from citations and journals (pivot, chaperone) appear at a double-blind ML decision and hold on
   held-out papers (B).
4. **For text-as-data practice in NLP.** Post-decision text leaks outcomes: 17.6% of accepted vs 0.5% of rejected
   2023-26 abstracts carry a code link (DP:83). Any OpenReview text study inherits this; we show a link-removal
   re-run (DP:367-374).

All four are worded as implications for measurement or for the debate, never as advice to authors or venues.

### 2.5 Why this framing serves an ACL SAC (and the questions the SAC will ask)

| SAC question | Answer the paper gives |
|---|---|
| Why is this an ACL paper? | Its instruments are NLP (SPECTER2 topic maps, an LLM contribution codebook, keyword canonicalisation, embedding distances), its main measurement lesson concerns the ACL "history of the field" genre, and its object is the field the ACL community now works in: the "large language models" keyword went from 0.26% of ICLR submissions in 2022 to 16.7% in 2026 (pooled corpus; DP:80), and NLP authors increasingly publish at ML venues (`jurgens2026future`, V-arXiv). |
| Isn't the hindsight result obvious? | The direction is anticipated conceptually (Leydesdorff 2002; Rotolo et al. 2015); its size on the same papers was not measured among the works checked (VP:362; lit_methods_measurement (b)1). We also show which substantive claims survive it: H1d, H2b′, H2c′ pass; H3a and H2a fail (DC:271, 295-297, 324). |
| Are LLM labels valid? | Agreement is between LLM labellings (κ 0.93 blind second pass; 95.8% with an LLM-labelled reference set of 2,300; DC:132-133), so it shows consistency, not human-level validity (DC:52). A misclassification correction only enlarges H2b/H2c (+4.09/−1.84; DC:304). Larger human validation is future work (DC:136). |
| Is it causal? | No. Associations within topic and year (DC:42). |
| Is held-out independent? | No: a pre-registered split-sample replication within the same ICLR years (DC:43-45). |
| Does ICLR generalise? | One venue (DC:56). ICLR is chosen because rejected and withdrawn submissions are public (DC:66). |

---

## 3. Abstract (180 words; counted with `wc -w`)

> Machine learning is often said to move in herds, and its histories are usually read backwards, from topic models
> fitted on all years at once. We ask whether the herd survives when the field is read as it unfolded. Using 43,480
> ICLR submissions (2017-2026), including rejected and withdrawn papers, we registered predictions, ran them once and
> tested them again on 11,099 held-out papers. Hindsight inflates the waves: on the same papers, a topic map fitted on
> all years finds 29 emerging topics; one fitted on 2017-2020 finds 8. What survives is convergence on a shared
> package: where more of a topic's papers built on foundation models, fewer proposed new architectures. Topic
> entrants did not write the follow-on work herding predicts. Our registered prediction failed in the opposite
> direction: entrants' papers were more often method proposals and, descriptively, further from earlier work. At
> review we detect no premium for following the crowd. Acceptance goes instead with continuity: staying near a team's
> own record, and including a topic insider (post hoc, supported on held-out papers). All findings are associations
> at one venue.

Number check: 43,480 (DC:65); 11,099 (DC:72); 29 vs 8 (DC:176, 179); H1d (DC:271, 364); H2b′/H2c′ (DC:296-297);
novelty (NJ main_pct); "no premium" = H3a C plus branding D\* plus premia B (DC:324; DP:133; DC:376); far jump and
insider B (DC:370, 374). "Tested them again" (not "replicated them") because H3a was registered and not
replicated; the B-tier gate results carry their own qualifier in the abstract. Use an en dash in "2017–2026" in the LaTeX.

---

## 4. Three contribution statements

Each is a contribution to a conversation and an expansion of the one thesis.

1. **Measurement (computational histories; temporal leakage).** We show that reading a field backwards inflates its
   fashions. On the same papers, a topic map fitted on all years finds 29 emerging topics where a 2017–2020 map finds
   8, a trend conclusion ("topics age from methods to benchmarks") appears only on the early map, and topic growth
   looks predictable only with hindsight (R² 0.28 vs −0.03). We pair this with a forward-reading design in which
   every predictor uses only earlier submissions, or each registered claim must also hold on maps fitted without
   later years. (Tier E; DC:176-231.)
2. **Entry (herding and the LLM-era hype debate).** We test the herding account where it is sharpest. Our registered
   prediction that topic entrants write follow-on measurement work failed in the opposite direction, and the
   reversal replicated on held-out papers (A). Descriptively, entrants' papers also sit further from earlier work,
   and first-time teams take up the field's package and its trending keywords more slowly (E).
3. **The gate (imitation vs continuity).** We separate two routes to conformity, imitation of what others do now and
   continuity with an accumulated record. At the review gate of one ML venue we detect no premium for the first
   (C/B/D\*), while acceptance goes with the second: staying near the team's own record and having a topic insider
   (B, held-out supported). Every claim carries its evidence tier.

---

## 5. The argument, section by section

### 5.0 Word budget (body 3,000-4,000; abstract, captions, tables, Limitations, appendix excluded)

| Section | Words | Act |
|---|---|---|
| §1 Introduction | 600 | set-up |
| §2 Background: two routes and a ruler | 420 | set-up |
| §3 Data and a forward-reading design | 480 | set-up |
| §4 The waves, read forward | 520 | Act 1 |
| §5 Who carries the wave | 560 | Act 2 |
| §6 What the gate goes with | 720 | Act 3 |
| §7 Discussion: where conformity lives | 380 | payoff |
| §8 Conclusion | 100 | |
| **Total** | **3,780** | |

### §1 Introduction (600 words)

**Role.** State the herd story, the backwards ruler that supports it, the forward-reading question, the thesis and
the contributions. The reader must know by the end of §1 that each section tests one prediction of the same account.

**Paragraphs:**
1. **The waves (~110).** ICLR submissions grew from 384 (2017) to 15,411 (2026), ×40.1; 69.3% of the corpus is from
   2024–26 (DP:70-72). The share building on a foundation model (FM) rose from 0.3% to 54.4%; the share proposing a
   new architecture fell from 24.5% to 7.5% (DC:163-164). Keywords rise and fall (Figure 1): "large language models"
   from 0.26% (2022) to 16.7% (2026) and "generative adversarial networks" from 8.1% (2018) to 0.09% (2026) (pooled
   corpus; DP:80). Even titles move: the share opening with a short coined name and a colon rose roughly fourfold,
   from about one in ten to about four in ten (7–14% to 37–49% by definition; E\*, DP:124-125).
2. **The herd story (~120).** In the LLM era, ML and NLP describe themselves as hype-driven and homogenising
   (Lipton and Steinhardt 2019; Hooker 2021; Dehghani et al. 2021; Bommasani et al. 2021), with newcomers flooding
   new LLM work (Movva et al. 2024). Herding theory predicts exactly this: under uncertainty, agents copy others
   (Bikhchandani et al. 1992; Banerjee 1992), and fashions spread whether or not they pay (Abrahamson 1991). Sutton's
   (2019) counterpoint is that convergence on general methods can be efficient.
3. **The ruler (~100).** Claims about our field's waves are usually checked by fitting one topic model on the whole
   archive and reading it forwards (Hall et al. 2008; Pramanick et al. 2023). A model fitted on all years carries the
   future into the past: in prediction this is called leakage (Kaufman et al. 2012; Kapoor and Narayanan 2023), and a
   language model is known to be a model of when it was trained (Lazaridou et al. 2021). Hindsight is not foresight
   (Fischhoff 1975).
4. **What we do (~120).** We read the foundation-model wave forward, at the three points where the herding account
   makes predictions: how waves are measured, what entrants write, and what the review decision goes with. 43,480
   ICLR submissions (2017–2026), including rejected and withdrawn papers; NLP instruments (SPECTER2 topic maps, an
   LLM contribution codebook, embedding distances to each paper's past); predictions registered before any outcome
   was read, run once, and tested again on 11,099 held-out papers (a pre-registered out-of-sample replication, not
   a certified untouched holdout). Every finding carries an evidence tier (Table 1). All results are associations.
5. **Thesis and preview (~90).** The thesis sentence (Section 1 above), then one sentence per act: hindsight
   inflates the waves but package convergence survives (§4); the registered herding prediction for entrants failed
   in the opposite direction (§5); the gate shows no detectable premium for following, and goes with continuity
   (§6).
6. **Contributions (~60).** The three statements of Section 4, in one line each.

**Do not:** list RQ1–RQ3; say "we find ML is not a herd"; quote the FL case or the title ratio as findings.

### §2 Background: two routes to conformity, and the ruler that judges them (420 words)

**Role.** Give the reader the two accounts the tests separate, the measurement practice the paper corrects, and
the gap.

**§2.1 Imitation and continuity (~170).** Use TA:652-659 as the definitions paragraph, shortened:
- Imitation takes its cue from what others do now (Bikhchandani et al. 1992; DiMaggio and Powell 1983; Haunschild
  and Miner 1997). Continuity takes it from an accumulated record: one's own past work (March 1991; Stuart and
  Podolny 1996) or a topic's record carried by a collaborator (Sekara et al. 2018).
- Weisberg and Muldoon (2009) model the difference as "followers" versus agents who search from their own position
  (cite Alexander et al. 2015 with it). Writing on herding in science often merges the two (Weisberg 2013).
- Bourdieu (1975): entrants choose between "succession" and "subversion"; the dominant pursue conservation, and
  journals consecrate work faithful to "official science" (CONTENT-PRIMARY; TA:400-433).
- The two routes predict different things at entry (imitation: entrants, who face the most uncertainty, copy most;
  continuity: entrants bring their own record and take up a new package slowly, Cohen and Levinthal 1990) and at the
  gate (imitation pays only if evaluators reward conformity to peers, Scharfstein and Stein 1990; continuity is
  consecrated). Timing is a third account: under priority (Merton 1957; Strevens 2003), early arrival is rewarded
  and late riding is not.
- Gap sentence: a recent review of topic choice treats social context and path dependence as distinct drivers and
  lists entry costs and topic rewards as open questions (Xiang et al. 2025). Footnote on "anchored" (Tversky and
  Kahneman 1974; optionally Baddeley 2015).

**§2.2 The ruler (~130).** Computational histories (Hall et al. 2008; Anderson et al. 2012; Pramanick et al. 2023;
Schäfermeier et al. 2021; Klinger et al. 2020) and embed-then-cluster pipelines (Grootendorst 2022) fit topics on the
whole period; dynamic models still fit all slices jointly (Blei and Lafferty 2006). Emergence is partly defined by
what is visible later (Rotolo et al. 2015); static models can miss small emerging topics (Li et al. 2025);
prospective signatures have been tested on later years (Khanbayov and Kurban 2026).

**§2.3 The gate at ICLR (~120).** ICLR's open records have been used to study prestige and visibility (Tran et al.
2020; Ibrahim et al. 2026), the review process (Jung et al. 2025) and topic differences (Wang et al. 2023; Xu et al.
2026). An RCT at ICML found no herding among reviewers in discussions (Stelmakh et al. 2023). Close with the drop-in
novelty paragraph (Section 2.3 above).

### §3 Data and a forward-reading design (480 words)

**Role.** Show that the instruments are NLP, that each measure is dated, and that the tiers are earned.

**Claims and facts:**
1. **Corpus (~90).** Our own dated acquisitions of official OpenReview records: 55,938 reconciled submission
   instances (DC:62); 43,480 discovery submissions with a usable abstract, 2017–2026, including rejected and
   withdrawn papers (DC:65-66); 11,099 released held-out papers (8,185 decided in 2018–26; DC:72-74). Acceptance
   tests use 32,190 decided papers, 40.1% accepted (DC:318). Existing ICLR dumps were audited and not pooled (Re²:
   main-conference coverage ends 2023 and omits 2019; DC:69). One sentence, in the ACL data-provenance register.
2. **Instruments (~140).**
   - Topics: SPECTER2 (Cohan et al. 2020; Singh et al. 2023) embeddings of title [SEP] abstract, PCA(128), spherical
     k-means, k = 100 (DC:86-87). NMI with ICLR primary areas 0.302 vs 0.272 for a TF-IDF/LSA baseline; blind name
     check 80% correct at the middle level; seed ARI 0.66 (DC:90-93).
   - Contribution type: a fixed LLM codebook (prompt v1), one primary type per paper; blind second pass κ 0.93
     (DC:129-133). "Consistency between LLM labellings, not human-level validity" (DC:52).
   - Keywords: 40,930 canonical expressions (DC:63).
   - Entry status from exact author IDs, never names (DC:144); the 2021 switch from email to profile IDs hides
     earlier history and biases entry contrasts towards zero (DC:145-146).
   - Distances: F_max (closeness to the team's own earlier submissions) and field novelty (distance to the 10
     nearest strictly earlier papers), both on centred SPECTER2 (PRE:1373; NJ). Credit Bao and Li (2025) for the
     own-record similarity measure.
3. **Forward-reading rules (~130).**
   - Temporal: entry status uses submissions strictly before year t; FM adoption, heat and maturity are lagged;
     closeness uses each author's earlier submissions; novelty uses strictly earlier years; keyword states use onset
     and lagged momentum; topic edges from 2018–22 predict 2024–26 (DC:144, 153; PRE:1258-1262, 1373-1380; DP:326).
   - Hindsight variants: every registered time-trend claim must also hold on a year-balanced map and on the early
     (2017–20) map applied to 2021–26 papers (DC:194, 239).
   - Exceptions are flagged in Table 1's "info" column: k100 topic cells, the retrospective PH6 wave set, and
     post-decision text.
   - Outcome leakage into text: 17.6% of accepted vs 0.5% of rejected 2023–26 abstracts carry a code link (DP:83). A
     link-removed re-run keeps the far-jump result (−5.44 → −5.39; DP:371), discovery only.
4. **Protocol and tiers (~120).** Registered on 2026-10-13, before full-corpus labels existed (DC:237); outcomes
   readable only by a locked loader; one frozen run (DC:245-246); held-out tests registered before the held-out run
   (DC:256-258); tiers A–E (Table 1 legend). Linear probability models with topic and year (or topic × year) fixed
   effects, SEs clustered by topic (DC:244). Honest size: under a null that cuts across topics, the main entry test
   rejected 12.6% / 10.0% at nominal 5%, and a wild cluster bootstrap did not fix it (DC:249-250); report it.
   Non-supported tests below their MDE80 are "uninformative" (DC:46). One sentence on prior exposure: earlier
   exploratory work on keyword popularity and title style was seen before registration and is disclosed (DC:238).
   One sentence that Ibrahim et al. (2026) also pre-registered an out-of-sample ICLR test (no "first").

### §4 The waves, read forward (520 words) — Act 1

**Role.** The herd story's first evidence is the waves themselves. Show that reading them backwards inflates the
fashion, then what survives forward reading. Close by saying the field level cannot tell imitation from a package,
which motivates Acts 2 and 3.

**§4.1 Same papers, different ruler (E; ~240).**
- On the same 43,480 papers and the same pipeline, only the fitting window differs: the all-years map finds 29
  emerging topics holding 40.9% of 2024–26 papers; the 2017–20 map finds 8 holding 22.3% (DC:176, 179).
- Not seed noise: a seed refit of the all-years map finds 28. A year-balanced map finds 16; the late-only map 28.
  Declining topics: 13 on the all-years map vs 26 on the year-balanced map (DC:176-181).
- Why: 69% of papers are from 2024–26, so the all-years map is a present-day map; it fits 2026 papers better than
  2017 papers (0.65 vs 0.62), the early map the reverse (0.69 vs 0.53) (DC:67, 176-179; TOP).
- Bracket, not point: the share of 2024–26 papers in emerging topics lies between 22% and 41% (DC:187). The early
  map cannot represent topics born after 2020, so 8 is a lower bound for genuinely new topics (Section 8, W5).
- Diversity peaks in each map's own fitting years (all-years map 0.443 in 2017 to 0.91 in 2025; early map peaks at
  0.908 in 2020) (DC:189-191). "Diversity rose" is therefore not a finding (DC:192).
- A trend conclusion flips: whether topics "age" from method papers towards benchmark papers is null on the
  all-years map (method −0.14, measurement +0.50 per log unit of prior papers) but present on the early map applied
  to 2021–26 papers (−3.48 [−6.21, −0.76]; +3.96 [+1.35, +6.57]) (DC:201-202). Counted variants of a registered test
  that was not supported (C); read as exploratory; never "topics age".
- Growth looks predictable only with hindsight: out of time, topic size "predicts" 2-year growth with R² 0.28 on the
  all-years map and −0.03 on the early map (DC:217). Caveat: maps differ in fitting corpus, no paired test
  (DC:227-229).
- Prior work: Li et al. 2025; Khanbayov and Kurban 2026; Leydesdorff 2002 (conceptual).

**§4.2 What survives: a package (A; ~180).**
- Registered H1d: where more of a topic's previous-year papers built on FMs, fewer of its papers propose new
  architectures: −7.98 pp for 0 → 100% prior FM share [−12.14, −3.82] in discovery; −11.0 [−18.1, −3.9] on 10,978
  held-out papers (one-sided p 0.0013); 9/9 counted variants and both hindsight maps (DC:271, 364).
- Size reading: topics at 50% adoption have about a third fewer new-architecture papers than topics at 10% on a base
  near 9% (DC:274-277). The held-out test was underpowered at the discovery size (MDE80 12.0), so it confirms
  direction, not size (DC:380).
- Caveats in one sentence: lagged adoption helps timing only; reverse causality possible; "an adapter on an LLM" is
  labelled method, not new architecture (DC:283-284).
- Connect: Bommasani et al. 2021 (homogenisation), Gururaja et al. 2023 (exploit phases), Saphra et al. 2024.

**§4.3 Package or herd? (E; ~100).**
- The field level does not discriminate: package bandwagons (Fujimura 1988, cite for general argument), lock-in
  (Arthur 1989) and efficient choice (Sutton 2019) all predict H1d (TA:600, 616).
- One outcome-free observation leans against piling on: the share of papers with an independent same-year twin
  (cosine ≥ 0.70) rose from 19.5% (2019) to 48.8% (2026), but twins per paper per 1,000 submissions fell from 0.32
  to 0.19 (DP:78-79). Duplication grew with volume, not with more piling-on per pair (E).
- Transition sentence: whether this convergence is a herd is decided where the routes make different predictions,
  at entry and at the gate.

**Figures:** Figure 1 (waves; cited in §1 and here) and Figure 2 (same papers, different ruler).

**Do not:** say "manufactures"; report 28–33% emerging topics or rising diversity as findings (DC:110-111, 192);
present the lifecycle as found or absent (DC:423).

### §5 Who carries the wave (560 words) — Act 2

**Role.** The hook of the paper and the strongest discriminating test. The herding account's sharpest prediction is
about entrants: they lack a record in the topic, face the most uncertainty, and should imitate most (DiMaggio and
Powell 1983; cascades). Continuity predicts the opposite: entrants carry their own record in, and take up a new
package slowly (Cohen and Levinthal 1990).

**Opening sentence (wording matters):** "A randomised trial at ICML detected no herding among reviewers in
discussion (Stelmakh et al., 2023). We ask the corresponding question about authors entering a topic."

**§5.1 The registered prediction failed (A, reversed; ~200).**
- Before any outcome was read, we registered that newcomer papers would less often be method papers and more often
  measurement papers, i.e. follow-on work (DC:33-36).
- Discovery: +3.71 pp [+2.61, +4.80] for method papers (base 75.0%), −1.70 [−2.46, −0.93] for measurement papers
  (base 7.7%), both significant in the opposite direction (DC:296-297).
- The reversed hypotheses were registered before any held-out data: held-out +3.60 [+1.48, +5.71] and −2.10
  [−3.35, −0.85] on 10,718 papers (one-sided p 0.0007 and 0.0005); 10/10 counted variants; both hindsight maps
  (DC:365-366). Same sign at k = 75 and 150 (DC:118-119).
- Qualifier: with a team-size control the measurement gap shrinks to −0.54 [−1.11, +0.04] (held-out −0.98), the
  method gap does not (+3.92) (DC:301, 308). Part of the benchmark gap is small all-new teams vs larger mixed teams.
- Interpretation sentence: "Entrants write proposals rather than the follow-on measurement work herding predicts. A
  method paper is a contribution type, not a measure of novelty." Connect to Koch et al. 2021 (benchmark building is
  concentrated) and Pramanick et al. 2023 (methods drive, datasets follow). Movva et al. 2024 showed entry is large;
  we add what entrants write.

**§5.2 Further from earlier work (E, added during writing; ~150).**
- Because type is not novelty, we also measured each paper's distance from strictly earlier ICLR submissions
  (definition in Section 1). Within topic × year, newcomer papers sit **+5.90 percentile points [4.95, 6.85]** above
  incumbent papers (N 42,325; 786 topic-year cells; SEs clustered by 100 topics; NJ main_pct).
- Not a type effect: within method papers +5.24 [4.16, 6.31] (N 31,764); with team size +5.59 [4.64, 6.54]; with
  type, FM and team controls +5.76 [4.82, 6.70] (NJ).
- Stable: +4.95 [2.32, 7.58] in 2019–22 and +6.01 [5.03, 6.98] in 2023–26 (difference +1.06, p 0.44); without
  2021 +5.87; excluding papers with an earlier version +5.81 (NJ).
- Size: about 0.22 of a within-cell SD on the raw cosine scale (+1.35 [1.16, 1.55] × 10⁻², SD 0.0618) (NJ). Modest
  but precise.
- Caveats in the text: descriptive, unregistered, added during writing; incumbents' own earlier papers stay in the
  reference set, so part of the gap is self-continuation; SPECTER2 distance is not originality, and entrants from
  other fields may simply use other vocabulary.

**§5.3 Slower, not faster, onto the trend (E; ~130).**
- Compared with returning topic newcomers, first-time teams submit FM papers less often by 4.6, 9.0 and 14.7 pp in
  topics at 5–15%, 15–30% and 30–50% prior FM adoption (not detectable at 0–5% or ≥ 50%) (DP:360-362;
  `free_entry.csv`).
- They list Emerging (young, rising) keywords less often: 16.7% vs 25.0% of uses, −3.7 pp (q 6 × 10⁻⁶) (DP:315).
- Newcomer papers are less often twinned: −3.9 pp [−5.0, −2.7] (DP:275).
- Reading: what absorptive capacity predicts (Cohen and Levinthal 1990), the opposite of the mimetic prediction.
  Caveats: descriptive; FM label on partly camera-ready text; no team-size control for the keyword result (DP:317,
  362).

**§5.4 What stays open (C; ~80).** Whether entrants crowd into hot topics is not settled: the incumbent share in hot
vs other topics is −0.73 pp [−2.68, +1.22], inconclusive, and fails the hindsight check (DC:295); newcomer × hot
interactions are not detectable (DC:307). "Entrants do not write the follow-on work herding predicts; whether they
flock to hot topics we cannot say."

**Figure:** Figure 3 (who carries the wave).

### §6 What the gate goes with (720 words) — Act 3

**Role.** Herding is individually rational only if evaluators reward conformity to peers (Scharfstein and Stein
1990), and a community's reward system can counteract the pull of the leading approach (Kitcher 1990, for general
argument only). Test the reward side for each route: following (imitation), timing (priority), continuity. Open
with the asymmetry stated plainly: the negative half of the thesis rests on registered tests, the positive half on
post hoc tests replicated on held-out papers.

**§6.1 Following: no detectable premium, and edges that regress (C, D\*, B; ~200).**
- Crowding: acceptance per log unit of prior topic papers −1.68 pp [−3.68, +0.32] in discovery, −1.51 [−5.20,
  +2.19] held-out; MDE80 4.8; fails the hindsight check (DC:324, 367). "No detectable premium" (DC:332); effects below
  about 5 pp per log unit cannot be told from zero.
- Branded titles: their share rose roughly fourfold (E\*), yet in an earlier exploratory analysis accepted papers
  carried them at the submitted rate (ratio 1.02; D\*, not re-run; DP:133). One clause, flagged as earlier
  exploratory. Bears on Lipton and Steinhardt's worry that packaging pays.
- Topic edges: topics differ in acceptance (Wang et al. 2023; Xu et al. 2026; our noise-free SD 6.4 pp, DP:324), but
  the edges regress: 2018–22 edges predict held-out 2024–26 edges with slope b = 0.60 [0.32, 0.88] (0 < b < 1;
  discovery 0.38) (DC:376; DP:326-328), and empirical-Bayes-shrunk edges predict better than zero (B; DC:377). With
  keywords as units the slope is 0.16 [−0.34, 0.66] (unregistered; DP:52-53). A single year's topic rate is half
  noise at about 58 decided papers (DP:325). Reading: copying topics with high past acceptance (outcome imitation,
  Haunschild and Miner 1997) would chase a signal that is partly noise. "A favoured topic is not a reward that keeps
  paying in full" (VP:186).
- Honesty sentence: an absence of premium does not rule out bandwagons that go unrewarded (Abrahamson and Rosenkopf
  1993).

**§6.2 Timing: early, weakly; the vivid fad case fails forward reading (B weak, C; ~170).**
- Define "early" as early in a keyword's life, not early in the submission window (contrast Jung et al. 2025).
- A1 (prospective states): papers listing young, rising keywords vs old, flat ones +2.67 pp [+0.76, +4.58] in
  discovery, +3.25 [−0.18, +6.69] held-out; supported one-sided (p 0.031), but the two-sided interval includes 0
  (DC:375; DP:48-49).
- PH6 (retrospective wave set): a keyword's acceptance gap after vs up to its share peak, 17 waves: −5.7 [−8.5, −2.9]
  in discovery, −5.2 [−11.1, +0.7] held-out (one-sided p 0.043; below MDE80 7.4); −1.7 (p 0.33) without the six
  keywords inspected first (DP:389-392). Say that the wave set itself is defined with hindsight.
- Both lean towards priority (Merton 1957; Strevens 2003) and away from rewarded late riding, weakly.
- Federated learning, the most quotable fad case: −11.3 pp [−17.9, −4.8] in discovery (q 0.19); held-out −4.9
  [−15.4, +5.7], uninformative (MDE80 14.5), and its trend has the opposite sign (DC:368-369). "Not confirmed."
  This is the gate's version of Act 1: the story hindsight tells best is the one that did not survive forward
  reading.

**§6.3 Continuity: what acceptance goes with (B; ~220).**
- Far jump: papers at the 10th percentile of closeness to the team's own earlier work vs the median: −5.44 pp
  [−7.10, −3.78] in discovery; −6.09 [−9.32, −2.86] on 5,344 held-out papers (one-sided p 0.0025; MDE80 4.9)
  (DC:370). Holds with a newcomer control (−5.0) and on link-removed text (−5.39) (DP:238, 371). Shape by closeness
  fifth, far to near: 39.7 / 41.8 / 44.4 / 47.2 / 46.9% (D; DP:236): leaving costs; the closest fifth gains nothing
  further.
- Within the same author: +0.55 pp per +0.1 cosine in discovery, +1.06 [+0.23, +1.89] held-out (B; DC:372).
  Co-author composition may account for half (DP:243).
- One topic insider vs none, at fixed team size and number of experienced authors: +3.42 [+1.18, +5.66] in
  discovery, +3.88 [+0.28, +7.47] on 6,243 held-out papers (one-sided p 0.017) (B; DC:374). Underpowered at the
  discovery size (derived MDE80 about 4.5): direction, not size. Holm 0.019 holds within its module only (DP:54-55).
- The newcomer acceptance gap mirrors this at the person level (D): −10.2 pp within topic × year (DC:343); on the same
  sample −5.4 without and −3.1 [−4.5, −1.6] with author fixed effects; the same author entering a new topic −1.4
  [−2.7, −0.0] (DP:177-179). Most of the gap is about who writes; a small cost remains for the same person moving.
- Prior-work sentences: "Larger pivots are less often published (Hill et al., 2025); we observe the decision itself,
  on every submission, at one ML venue, under double-blind review." "Our closeness measure follows Bao and Li (2025)."
  Chaperones: Sekara et al. 2018.

**§6.4 Distance from the field vs distance from oneself (C, D; ~60).** In discovery, the least-novel fifth (relative
to earlier ICLR papers) was accepted 3.27 pp less often than the middle fifth, but held-out −0.13 [−3.50, +3.25],
uninformative (DC:371); the most-novel fifth +0.44 (D; DP:261). With §5.2: entrants' papers sit further from the
field, and we detect no field-novelty association that survives held-out testing; the replicated penalty attaches to
distance from one's own record. Never present the "two tails" or the novelty floor as findings (DP:42-44).

**§6.5 Rival readings (~70).** Continuity at the gate may reflect better-informed, better-made papers or evaluator
conservatism (Li 2017; Bourdieu 1975), visible status via preprints (Ibrahim et al. 2026), or selection into teams.
Per head, an insider is worth about as much as an experienced author from another topic (+0.58, p 0.16; D), and a
keyword-defined insider shows nothing (+0.0) (DP:289, 294-296), so "topic knowledge" and "a record of any kind" are
not separated. Interactions with topic heat are null and uninformative (DP:246, 291).

**Figure:** Figure 4 (what the gate goes with, read forward).

### §7 Discussion: where conformity lives (380 words)

**Role.** Turn the three verdicts into the conceptual payoff and the ACL lesson, then the one tension.

1. **Where conformity lives (~110).** In this field, at this venue, the conformity we can detect is continuity, not
   imitation: entrants do not write the follow-on work imitation predicts (A), following carries no detectable
   premium (C; B), and acceptance goes with staying near a team's own record and with a topic insider (B). What
   Weisberg (2013) models as herding, risk-avoiding clustering, appears here as continuity with one's own record
   (TA:374-375). Bourdieu's gate consecrates succession.
2. **The package (~80).** H1d is real but does not discriminate. Three discovery-only results lean towards a package
   rather than a fad (D): FM papers are accepted 4.62 pp more often within topic × year [+2.79, +6.44] (DC:342), the
   premium does not shrink as adoption rises (slope +0.19 [−0.96, +1.34]; DP:356), and new-architecture papers are
   accepted relatively more where FMs dominate (+8.3 [+1.3, +15.4]; DC:349). A fad's premium should fade. Hooker
   (2021) and Sutton (2019) both remain live.
3. **The lesson for field histories (~100).** Read backwards, every herd signal in this paper was larger than its
   forward reading: emerging topics (29 vs 8), growth predictability (R² 0.28 vs −0.03), topic edges (b 0.60 < 1),
   federated learning's gap (−11.3 vs −4.9), the novelty floor (−3.27 vs −0.13). Leakage of later information into
   earlier measurement is to field histories what leakage is to prediction (Kaufman et al. 2012). The check costs one
   refit on early years, lagged predictors and a held-out split. (Phrase as a property of measurement, not advice.)
4. **Tension (~60).** In the previous shift, researchers who stayed close to their own record had lower later impact
   (Bao and Li 2025); here continuity goes with acceptance. The gate and the citation record need not reward the same
   thing; our data cannot test this. Short-run rewards for exploitation can carry long-run costs (March 1991;
   Rzhetsky et al. 2015).
5. **Scope (~30).** One venue; double-blind but de-anonymisable; associations only.

### §8 Conclusion (100 words)

Restate the thesis and the three verdicts in one sentence each; end with the memorable formulation ("Hindsight
tells the herd story; read forward, the field's wave is a package carried by proposers past a gate that goes with
continuity"). One sentence of scope: one venue, associations, tiers.

### Limitations (ARR section; not counted)

One venue; held-out split shares years, reviewers and authors (DC:45); post hoc B-tier gate results with six
secondary one-sided unadjusted tests (DP:29-30); test size above nominal under a cross-topic null (DC:249-252); the
2021 author-ID switch and ICLR-only histories bias entry contrasts towards zero (DC:145-149); LLM labels validated
against LLM labels (DC:52); post-decision text (DC:77-78; DP:25); flocking untested (DC:295); the novelty analysis
was added during writing and is unregistered (NJ); the PH6 wave set is retrospective (RES:968-969); FM and title
measures on LLM-era text (Liang et al. 2024; Kobak et al. 2025); hindsight comparison bracketed, early map blind to
post-2020 topics (TOP); no causal identification (DC:42).

### Ethics statement (optional in ARR; recommended here)

Author identifiers are used only as keys to compute entry status and closeness; no author is named; results are
reported in aggregate; data come from public OpenReview records under their terms (DC:62). No review scores are used
(DC:71).

### Appendix (relegated, each with its reason)

| Appendix | Content | Why not main text |
|---|---|---|
| A. Every registered and declared test | The full held-out table (DC:362-378) and unregistered rows (DC:383-386) | Table 1 shows the story rows; this is the audit trail |
| B. Measurement validation | Topic quality and k-sensitivity (DC:89-123); label agreement (DC:129-138); keyword map (DC:262); earlier-version detection (DC:154); buzzword measure dropped (DC:155) | Instrument detail |
| C. Hindsight details | All six maps (DC:174-181); diversity by year (DC:189-191); forecast metrics and size terciles (DC:217-231) | Supports §4.1 |
| D. Novelty analysis | Every NJ specification, by year (2019 +1.26, p 0.70; 2021 +22.5 on about 11 incumbent papers), plain definition +6.63 | Added during writing; full transparency |
| E. Other gate modules | PH1 newcomer correlates; PH2 team size (+8.8 pp per doubling); PH4 areas and FL mechanisms; E3 withdrawal after review (+1.62 per log unit); E10 acceptance by class; P2 twins (with the P2 quoting rule); E2 near closeness (with the E2 rule); keyword winner's curse (16.0% vs 20.6%); cleantext | Discovery-only (D) or off the spine; quoting rules need room |
| F. Title style | Share by definition (E\*; DP:106-118); ratio 1.02 (D\*); returning first authors' lag and LLM-favoured verbs (E\*, not re-verified) | Earlier exploratory; only the share is re-verified |
| G. Size calibration | Dry-run nulls, bootstrap, S11 (DC:249-255) | Methods detail |

### 5.9 Placement map: every major finding has a place

| ID | Finding | Tier | Where | Role in the story |
|---|---|---|---|---|
| F1 | Waves and FM displacement (growth ×40.1; FM 0.3% → 54.4%; new architectures 24.5% → 7.5%; H1d −7.98 / −11.0; 17 of 68 keywords rose and fell) | A; E | §1, §4.2, Fig 1, Table 1 rows 4 | What survives forward reading at the field level: a package |
| F2 | Hindsight measurement (29 vs 8; lifecycle flip; R² 0.28 vs −0.03; diversity) | E | §4.1, Fig 2, rows 1-3 | Act 1's backward vs forward reading; the ACL lesson |
| F3 | Newcomers bring methods, not benchmarks (registered prediction reversed) | A | §5.1, Fig 3, rows 7-8 | The hook; the sharpest test of herding |
| N | Newcomer papers further from strictly earlier work (+5.90 percentile points) | E | §5.2, Fig 3, row 9 | Answers "type is not novelty"; entrants are not followers in content either |
| F4 | First-time teams slower onto FMs and Emerging keywords; newcomer papers less often twinned | E | §5.3, Fig 3, rows 10-12 | Imitation's "fast adoption by the uncertain" fails descriptively |
| F11 | Twins as volume (19.5% → 48.8%; per pair 0.32 → 0.19); P2 acceptance mixed | E; D | §4.3, row 5; P2 in Appendix E | Field-level herd signal that shrinks when normalised |
| F5 | Crowding and branding: no detectable premium | C; D\* | §6.1, Fig 4, rows 14-15 | Rewarded imitation not detected |
| F9 | Topic edges regress (b 0.38 / 0.60; EB D0) | B | §6.1, Fig 4, row 16 | Outcome imitation would chase noise; gate-side mirror of Act 1 |
| F6 | Timing: A1, PH6 (weak); FL not confirmed | B weak; D/C | §6.2, Fig 4, rows 17-19 | Priority, weakly; the vivid fad case fails forward reading |
| F7 | Continuity: far jump, within-author closeness, insider | B | §6.3, Fig 4, rows 20-22 | The positive half of the thesis |
| F8 | Newcomer gap mostly composition (−10.2 → −3.1; −1.4 within person) | D | §6.3, row 23 | Person-level mirror of the far jump; guards against a bias reading |
| — | Field novelty at the gate (P1b not replicated; P1a; P7) | C; D | §6.4, row 24; Appendix E | Distance from the field vs from oneself |
| F10 | FM premium (+4.62), stable across adoption; new architectures against the tide (+8.3) | D | §7, row 6; Appendix E | Leans to package over fad; discovery only |
| — | Team size gradient (PH2), PH1 correlates, E3 withdrawal, E10 class acceptance, keyword winner's curse | D; D/E | Appendix E (team size also as a control in §5.1) | Off the spine; discovery only |
| — | Code-link leakage (17.6% vs 0.5%) and cleantext | E; D | §3 | Forward reading also means guarding against outcome leakage into text |
| — | Size failure (12.6% / 10.0%) | E | §3, Appendix G | Honesty about inference |
| — | Title share (E\*), returning-author title lag and LLM verbs (E\*, not re-verified) | E\* | §1 (share only); Appendix F | Only the share is re-verified |

---

## 6. Main-text table: Table 1, "The herd account read forward: predictions, observations and tiers"

**Layout.** `table*`, full width, `\small`, booktabs; four row blocks. Columns:

| Col | Header | Content |
|---|---|---|
| 1 | # | row number (referenced in the text) |
| 2 | Observable | what is measured, with an **info code**: **P** prospective (only earlier submissions or lagged shares); **H** k100 cells, all-years map (registered tests also required to hold on the balanced and early maps; "H✓" passes, "H✗" fails); **R** retrospective by construction; **T** post-decision text |
| 3 | Herding (imitation) predicts | sign or pattern |
| 4 | Alternative predicts | sign or pattern, with the account named: Continuity, Package or Priority |
| 5 | Discovery / all-years map | estimate [95% CI], pp unless noted |
| 6 | Held-out / early map | estimate [95% CI] |
| 7 | Tier | A–E, E\*, D\* |
| 8 | Reading | three to six words |

**Rows (all of them):**

| # | Observable [info] | Herding predicts | Alternative predicts | Discovery / all-years | Held-out / early | Tier | Reading |
|---|---|---|---|---|---|---|---|
| | ***I. The waves: how they are measured and what converged*** | | | | | | |
| 1 | Emerging topics, same 43,480 papers [H vs P] | Count should not depend on the fitting window | — | 29 (40.9% of 2024–26 papers) | 8 (22.3%); balanced 16; seed refit 28 | E | Hindsight inflates waves |
| 2 | "Topics age": method / measurement share per log unit of prior papers [H vs P] | — | — | −0.14 [−1.78, +1.49] / +0.50 [−0.76, +1.75] | −3.48 [−6.21, −0.76] / +3.96 [+1.35, +6.57] (2021–26 papers) | E (variants of C) | Conclusion depends on the map |
| 3 | Topic size → 2-year growth, out of time, R² [H vs P] | — | — | 0.28 | −0.03 | E | Predictable only in hindsight |
| 4 | Prior FM adoption (t−1), 0 → 100% → new-architecture share [P, H✓, T] | − (bandwagon) | − (Package: lock-in, efficiency) | −7.98 [−12.14, −3.82] | −11.0 [−18.1, −3.9] | **A** | Package convergence; not discriminating |
| 5 | Same-year twins per paper per 1,000 submissions, 2019 → 2026 | Rising (piling on) | Flat or falling (volume) | 0.32 → 0.19 (share twinned 19.5% → 48.8%) | — | E | Volume, not pile-on |
| 6 | FM paper → acceptance; premium slope per logit unit of prior adoption [P, T] | Premium fades as adoption rises (fad) | Stable premium (Package) | +4.62 [+2.79, +6.44]; slope +0.19 [−0.96, +1.34] | — | D | Leans to package (discovery) |
| | ***II. Entry: what topic entrants write*** | | | | | | |
| 7 | Newcomer paper → method paper [P, H✓, T] | − (registered) | + (Continuity) | +3.71 [+2.61, +4.80] | +3.60 [+1.48, +5.71] | **A** (reversed) | Registered herding prediction failed |
| 8 | Newcomer paper → measurement paper [P, H✓, T] | + (registered) | − (Continuity) | −1.70 [−2.46, −0.93] | −2.10 [−3.35, −0.85] | **A** (reversed) | Partly team size |
| 9 | Newcomer paper → novelty percentile vs strictly earlier papers [P, H, T] | − (follow-on is closer) | + (own record from elsewhere) | +5.90 [4.95, 6.85]; method papers +5.24 [4.16, 6.31] | — | E (added during writing) | Further from earlier work |
| 10 | First-time team → FM paper, vs returning newcomers, topics at 5–15 / 15–30 / 30–50% adoption [P, T] | + (fast adoption under uncertainty) | − (absorptive capacity) | −4.6 / −9.0 / −14.7 | — | E | Slower onto the package |
| 11 | First-time team → Emerging-keyword use [P] | + | − | −3.7 (16.7% vs 25.0%) | — | E | Slower onto the trend |
| 12 | Newcomer paper → has a same-year twin | + | − | −3.9 [−5.0, −2.7] | — | E | Less duplicated |
| 13 | Hot topic → incumbent share (flocking) [P, H✗] | − | 0 | −0.73 [−2.68, +1.22] | — | C | Untested |
| | ***III. The gate: following and timing*** | | | | | | |
| 14 | Topic crowding, per log unit of prior papers → acceptance [P, H✗] | + (rewarded imitation) | 0 | −1.68 [−3.68, +0.32] | −1.51 [−5.20, +2.19] | C | No detectable premium (uninformative) |
| 15 | Branded "NAME: subtitle" title → share among accepted ÷ among all [T] | > 1 | 1 | 1.02 | — | D\* (not re-run) | No premium, earlier exploratory |
| 16 | Topic edge 2018–22 → edge 2024–26, slope b [P] | b ≈ 1 (outcome imitation pays) | 0 < b < 1 (edges partly noise) | 0.38 [0.18, 0.58] | 0.60 [0.32, 0.88] | **B** | Edges regress |
| 17 | Emerging minus Mainstream keyword → acceptance [P] | ≤ 0 (late riding rewarded) | + (Priority) | +2.67 [+0.76, +4.58] | +3.25 [−0.18, +6.69] | B weak | Early, weakly (CI includes 0) |
| 18 | Gap after vs up to a keyword's share peak, 17 waves [R] | ≥ 0 | − (Priority) | −5.7 [−8.5, −2.9] | −5.2 [−11.1, +0.7] | B weak | Leans on six inspected keywords |
| 19 | Federated-learning keyword → acceptance gap [R] | − (fad punished) | — | −11.3 [−17.9, −4.8] | −4.9 [−15.4, +5.7] | C (discovery D) | Vivid fad case not confirmed |
| | ***IV. The gate: continuity and distance*** | | | | | | |
| 20 | Far jump from the team's own record (F_max p10 − p50) [P, T✓] | 0 | − (Continuity) | −5.44 [−7.10, −3.78] | −6.09 [−9.32, −2.86] | **B** | Leaving one's record costs |
| 21 | Within-author closeness, per +0.1 cosine [P, T] | 0 | + (Continuity) | +0.55 [+0.21, +0.90] | +1.06 [+0.23, +1.89] | **B** | Same author, closer, accepted more |
| 22 | One topic insider vs none, fixed team size [P, H] | 0 | + (Continuity) | +3.42 [+1.18, +5.66] | +3.88 [+0.28, +7.47] | **B** | Insider on the team |
| 23 | Newcomer paper → acceptance: within topic × year; same sample with author FE; same author new to topic [P] | 0 | − (Continuity) | −10.2 [−11.8, −8.7]; −3.1 [−4.5, −1.6]; −1.4 [−2.7, −0.0] | — | D | Mostly who writes |
| 24 | Least-novel fifth vs middle, relative to earlier papers [P, H, T✓] | − (gate penalises derivative work) | 0 (Continuity is about one's own record) | −3.27 [−4.93, −1.60] | −0.13 [−3.50, +3.25] | C | Not replicated (uninformative) |

**Caption (draft; wording matters).** "The herding account read forward. Each row is one prediction of herding
(imitation) and of the alternative named (continuity, a shared package, or priority). Estimates are percentage
points with 95% intervals unless noted, associations within topic and year. *Discovery / all-years*: the registered
or declared discovery estimate, or, in rows 1–3, the topic map fitted on all years. *Held-out / early*: the
pre-registered out-of-sample replication on released papers (not a certified untouched holdout), or, in rows 1–3,
the map fitted on 2017–20 papers. Held-out tests are one-sided, so a supported test can have an interval that
includes 0. Info: P prospective; H uses k100 cells (H✓/H✗: registered hindsight variants pass/fail); R retrospective
by construction; T post-decision text (T✓: link-removal check passed, discovery only). Tiers: A registered and
replicated; B post hoc, then supported by a declared held-out test; C registered, inconclusive or not replicated; D
discovery only; E descriptive; D\* earlier exploratory, not re-run."

**Footnotes to attach:** row 4 held-out underpowered at discovery size (MDE80 12.0) → direction only; row 8 −0.54
with team size; row 9 unregistered, self-continuation; row 10 vs returning topic newcomers, not detectable at 0–5% and
≥ 50%; row 16 keyword units 0.16 [−0.34, 0.66]; row 18 without the six inspected keywords −1.7 (p 0.33); row 22
derived MDE80 about 4.5, Holm within module only, early-map insider +3.0 (p 0.003; DP:288); row 23 discovery only.

**Space plan.** If the table must shrink, merge rows 2–3 into the Figure 2 caption, merge row 12 into row 5, and move
row 6 to Appendix E (it is discussed in §7). Never drop rows 13, 14, 19 or 24: they are the honest nulls and failures.

**Sources for every cell:** rows 1–3 DC:176-181, 201-202, 217; row 4 DC:271, 364; row 5 DP:78-79; row 6 DC:342,
DP:356; rows 7–8 DC:296-297, 365-366; row 9 NJ; row 10 DP:360-362; row 11 DP:315; row 12 DP:275; row 13 DC:295;
row 14 DC:324, 367; row 15 DP:133; row 16 DC:376; row 17 DC:375; row 18 DP:389-392; row 19 DC:368; rows 20–22
DC:370, 372, 374; row 23 DC:343, DP:177-179; row 24 DC:371.

---

## 7. Figure plan (four figures; Figure 1 exists)

| Fig | Title | Message (one sentence) | Panels | Data source (committed unless flagged) | Placement |
|---|---|---|---|---|---|
| 1 | Research waves at ICLR (exists) | Waves are easy to see afterwards: eight keywords rose and fell or surged, 2018–2026. | 2 × 4 small multiples of keyword share, peak marked | `research/fashion/paper/figs/fig1_waves.pdf`, built by `paper/make_figures.py` from the discovery corpus keywords (outcome-free) | `figure*` top of page 1–2; cited in §1 and §4 |
| 2 | Same papers, different ruler | On the same papers, the number of emerging topics and the shape of diversity depend on which years the map was fitted on. | (a) emerging and declining topics for the six k100 maps (all-years, seed refit, balanced, early, middle, late); (b) effective topics / k by year, one line per map, fitting window shaded; optional (c) H1a/H1b estimates on all-years vs early map | (a, b) `research/topics/output/hindsight_check.json` (`maps.*.emerging_topics`, `declining_topics`, `late_paper_share_in_emerging`, `effective_topics_over_k_by_year`); (c) `research/fashion/output/rq1_results.csv`. Existing drafts: `presentation/figs/hindsight_emerging.pdf`, `hindsight_diversity.pdf`, `lifecycle_flip.pdf` | single column, §4.1 |
| 3 | Who carries the wave | Entrants' papers are more often proposals, less often benchmarks, further from earlier work, and first-time teams come later to the package. | (a) newcomer minus incumbent: method share, measurement share (discovery and held-out points), novelty percentile, twinned (each on its own labelled axis; no common scale); (b) first-time minus returning newcomer teams: FM-paper share by topic adoption bin (0–5, 5–15, 15–30, 30–50, ≥ 50%), with CIs | (a) `research/fashion/output/frozen_run/rq2_results.csv`; `research/fashion/output_pooled/confirmation_run/summary.json`; `research/fashion/output/posthoc/ph5_position/free_herding.csv`; novelty from `paper_ws/output/novelty_newcomer.json` (**flag: scratchpad, not committed; commit the script and output before the figure is final, or drop the novelty point to the text**); (b) `research/fashion/output/posthoc/ph5_fmwave/free_entry.csv`. Existing draft: `presentation/figs/newcomers.pdf` | single column, §5 |
| 4 | What the gate goes with, read forward | Following shows no detectable premium and the fad case fails; distance from one's own record and an insider on the team go with acceptance in discovery and on held-out papers. | Small-multiple rows, each with its own x-axis and unit and an aligned zero line (no common scale, to respect the no cross-module comparison rule): crowding (H3a), federated learning, PH6, A1, P1b, far jump (E1), within-author closeness (E4), insider (teams H1); open marker = discovery, filled = held-out, tier label at right. Inset: premia slope b with the 0–1 band; or F_max quintile acceptance (39.7 … 46.9%) | `research/fashion/output_pooled/confirmation_run/summary.json` (H3a, H4-FL); `research/fashion/output_pooled/confirmation_run/ph5/tests.csv` (E1, E4, P1b, teams H1, A1, premia); `research/fashion/output_pooled/posthoc/ph5_waves/tests.csv` (PH6); `research/fashion/output/frozen_run/rq3_results.csv`; `research/fashion/output/posthoc/ph5_pivot/tests.csv`, `ph5_pivot/quintiles.csv`, `ph5_position/tests.csv`, `ph5_teams/family.csv`, `ph5_kwtiming/tests.csv`, `ph5_premia/tests.csv`, `ph4_keywords.csv`; `research/fashion/output_pooled/confirmation_run/ph5/premia_units.csv`. Existing drafts: `presentation/figs/far_jump.pdf`, `premia_scatter.pdf`, `replication_table.tex` | single column (or `figure*` if Table 1 is shortened), §6 |

**Caption guardrails.** Figure 1: say the keywords were chosen after the fact (it is a backward view by design).
Figure 2: "bracket, not point"; maps differ in fitting corpus. Figure 3: "contribution type is not novelty; novelty
is distance in SPECTER2 space, descriptive". Figure 4: "associations within topic and year; held-out one-sided; B
tests post hoc; underpowered supported tests confirm direction, not size". Figures are produced by scripts that read
only committed result files; no figure script reads an outcome column.

---

## 8. The weakest points, and how the text handles them

| # | Weak point | Why it matters | How the text handles it (exact move) |
|---|---|---|---|
| W1 | **The positive half of the thesis is post hoc (B).** Far jump, closeness and insider were found in discovery, then tested on held-out papers; six secondary held-out tests were one-sided and unadjusted; the insider's Holm 0.019 holds within its module only (about 0.17 across modules) (DP:29-30, 54-55). | A reviewer can discount every B result. | State the asymmetry at the top of §6: "The negative half of our thesis rests on registered tests (A, C); the positive half on post hoc tests that a declared held-out test supported (B)." Use "post hoc, supported on held-out papers" each time. The far jump is the primary PH5 test (Holm 0.005 held-out, MDE80 4.9, power 0.89) (DP:233-235). |
| W2 | **The flocking half of herding is untested** (H2a C; E5 n.s.; DC:295, 307). | "Not a herd" would overreach. | §5.4 says it explicitly; title uses "in hindsight" not "not a herd"; abstract claims only "did not write the follow-on work". |
| W3 | **No premium is not no bandwagon** (Abrahamson and Rosenkopf 1993). | Producers may imitate without reward. | One sentence in §6.1; the gate claim is about rewarded imitation only. |
| W4 | **Field-level H1d does not discriminate** imitation from package from efficient choice (TA:600, 616). | The strongest A result cannot carry the herd verdict. | §4.3 says so; H1d is "what survives", not evidence against herding; F10 (D) discussed as leaning only. |
| W5 | **The hindsight comparison is a bracket.** The early map is fitted on fewer papers and cannot represent post-2020 topics (fit 0.69 vs 0.53; TOP); the forecast comparison has no paired test (DC:227-229). | "29 vs 8" could be read as the true inflation. | Report the bracket (22%–41% of 2024–26 papers; seed refit 28; balanced 16); write "inflates", never "manufactures"; Figure 2 caption says "bracket". |
| W6 | **Held-out is not independent** (DC:43-45). | Replication guards against analyst overfitting, not reviewer- or year-specific patterns. | Use the exact wording once in §1 and §3; Limitations repeats it. |
| W7 | **Method paper ≠ novelty**; the novelty analysis that answers it is E, unregistered, added during writing, partly self-continuation, and SPECTER2 distance is not originality (NJ caveats). | The entry result could be misread as "entrants are more innovative". | §5.1 sentence "a contribution type, not a measure of novelty"; §5.2 labelled "descriptive, added during writing" with its three caveats; the abstract says "descriptively". |
| W8 | **Insider and far-jump rival readings**: expertise vs evaluator conservatism (Li 2017); visible prestige via preprints (Ibrahim et al. 2026); selection into teams; F_max correlates −0.57 with the newcomer flag; co-author composition may explain half of E4; insider ≈ crossover per head (D); keyword-insider null (DP:243, 247-248, 289, 294-296). | "Continuity" might be "status" or "a record of any kind". | §6.5 names all of them; "continuity" is defined as a position relative to a record, not a motive (TA:630-631); never "teams choose to stay close". |
| W9 | **Timing results are weak, and PH6 is itself retrospective**: A1's two-sided CI includes 0; PH6 p 0.043 and −1.7 (p 0.33) without the six inspected keywords; PH6's wave set requires the full series (RES:968-969). | In a paper about hindsight, a hindsight-defined test is an easy target. | Say it in §6.2: A1 is the prospective timing test; PH6 is retrospective by construction; both "weak". Neither carries the thesis; Table 1 marks row 18 with R. |
| W10 | **Entry contrasts are attenuated by measurement**: the 2021 email-to-profile ID switch hides earlier histories (k100 incumbency 18% in 2020, 0.5% in 2021); ICLR-only histories; earlier work in the held-out split invisible (DC:145-149). | Newcomer status is noisy. | Registered as bias towards zero; ID-consistent-years variant gives the same entry results (+3.72 / −1.74; DC:148); novelty gap unchanged without 2021 (+5.87; NJ). |
| W11 | **LLM labels and LLM-era text**: labels validated against LLM labels; FM label and novelty on partly camera-ready, partly LLM-written text (DC:52; DP:362; `liang2024mapping`). | ACL reviewers will press on LLM-as-annotator validity. | §3 wording "consistency, not human-level validity"; misclassification correction (DC:304); link-removal re-run (DP:371); Limitations. |
| W12 | **Inference size above nominal** (12.6% / 10.0% under a cross-topic null; DC:249-250). | p-values for the entry tests are approximate. | Report in §3; t = 6.7 and −4.4 are large relative to the 1.31 / 1.22 inflation factors (DC:311-312); held-out simulated sizes 2.0–2.5% (DC:260). |
| W13 | **The vivid cases did not replicate** (FL; P1b). | Tempting to quote; a reviewer can dismantle them. | Present both as failures of backward reading, which is what they are in this story; "not confirmed", "did not replicate", "uninformative". |
| W14 | **Prior art narrows several claims** (Hill 2025; Bao and Li 2025; Wang 2023; Xu 2026; Ibrahim 2026; Li 2025; Khanbayov and Kurban 2026). | Novelty could look overstated. | Use the drop-in paragraph and the seven narrowings (Section 2.3); every novelty claim says "to our knowledge, among the works we checked". |
| W15 | **One venue, one shift.** | Generalisation. | §7 scope sentence; "at one venue" in the abstract; the four "beyond ICLR" points are about measurement and the debate, not about other venues' behaviour. |
| W16 | **Tension with Bao and Li (2025)**: persistence went with lower impact in the previous shift. | Could read as contradiction. | §7 item 4: different stage, different shift, different outcome; "our data cannot test this" (VP:134-136). |

---

## 9. Open checks before writing

1. **Commit the novelty analysis.** Its script and outputs (`paper_ws/scripts/novelty_newcomer.py`,
   `paper_ws/output/novelty_newcomer.{json,csv}`) live in the scratchpad. Before the paper cites them or Figure 3 uses
   them, someone with write access must commit them to the repository, labelled "added during writing,
   outcome-free". The novelty values were recomputed and not checked against the module's cached features (NJ caveat
   6).
2. **Bibliographic items still open** (VP:487-499; TA:663-686): EMNLP 2026 author order for Jung et al. (cite arXiv);
   Xu et al. middle authors (use "et al."); Wang et al. 2023 issue number (omit); Biliotti et al. version; Vicinanza
   DOI; Cohen and Levinthal end page; Thoma given name.
3. **Content read only in secondary sources** (TA:665-676): Kitcher 1990, Strevens 2003, DiMaggio and Powell's
   mimetic section, Scharfstein and Stein 1990, Levitt and March's competency-trap wording, March's turnover result,
   the body of Xiang et al. 2025, Fujimura 1988. Cite for general arguments only until read.
4. **Numbers from other papers.** Quote none (e.g., Hill's 35%, Movva's "half of first authors") until checked
   against the PDF (VP:33-36).
5. **ARR area.** Choose the computational-social-science / science-of-science area that fits; check the current ARR
   area list (not verified here).
6. **Figure 1 numbers vs text.** The introduction's keyword shares (DP:80) are from the pooled corpus; Figure 1 plots
   the discovery corpus. Either quote Figure 1's discovery peaks or say "pooled corpus" in the text.
7. **Twin definition wording.** "Independent same-year twin, cosine ≥ 0.70" (DP:267); twins counted in discovery
   only (DP:277).
