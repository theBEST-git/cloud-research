# Related work (draft)

**Titles as an object of study.** Six decades of title scientometrics relate title form to
attention and impact in *published* papers. Titles have grown longer and more often compound
across disciplines (Lewison & Hartley 2005; Milojević 2017; Jiang & Hyland 2023), and colon use
in computer-science titles rose slowly from about 10% in the late 1970s to about 20% by 2018
(Nelson 2018). Associations between title form and citations are small, field-dependent and
largely absorbed by venue: short titles lose most of their advantage once journal prestige is
controlled (Letchford et al. 2015), colons help in some fields and not others (Buter & van Raan
2011; Hudson 2016; Donovan 2025), and question titles attract downloads but not citations (Jamali
& Nikzad 2011; Ball 2009). Twin-paper matching on DBLP gives the only causal-style estimate for
computer science, a modest colon effect on citations (Sato et al. 2022). Two lessons from this
literature shape our design. First, authors choose title style partly on their private view of
the paper, which confounds naive outcome comparisons (Heard et al. 2023). Second, almost every
study conditions on publication; the single study linking title structure to editorial
decisions covers one ecology journal (Fox & Burns 2015). Acronyms are the closest precedent to
the branded titles we study: their use in titles grew across science while most are rarely
reused (Barnett & Doubleday 2020), and NeurIPS title acronym density rose roughly tenfold since
1987 (Mandyam Rangarajan & Krishnan 2026). Within ML specifically, title evidence is limited to
term counts used as topic proxies (Mohammad 2019, 2020), stance classification (Beese et al.
2023), title generation (Chen & Eger 2023), and a raw-count history of the "all you need" meme
on arXiv (Alyakin 2025).

**Research fashion.** Fashion theory predicts that styles diffuse by imitation and decline
through differentiation (Simmel 1904/1957), that technical fashions follow bell-shaped
lifecycles supplied by fashion setters (Abrahamson 1991, 1996; Abrahamson & Fairchild 1999),
that tastes can change through internal dynamics alone (Lieberson 2000), and that faster rises
bring faster abandonment (Berger & Le Mens 2009). In science, bandwagons form around doable
problems and transportable packages (Fujimura 1988), and peer-recognition incentives can produce
research cycles (Bramoullé & Saint-Paul 2010). Computational histories of NLP trace topic
epochs and paradigm shifts in the ACL Anthology (Hall et al. 2008; Anderson et al. 2012;
Pramanick et al. 2023; Gururaja et al. 2023), and the rhetorical framing of a topic predicts its
rise or fall (Prabhakaran et al. 2016). At ICLR, the subfield landscape and its turnover have
been mapped from submissions (González-Márquez & Kobak 2024), and emerging topics show higher
topic-level acceptance that shrinks as they grow (Xu et al. 2026). Sociolinguistics offers the
distinction we test for titles: change can be *communal*, with the same speakers adopting a
new form, or *generational*, with new cohorts replacing old ones; in online communities, users
move from an innovative to a conservative phase (Danescu-Niculescu-Mizil et al. 2013), and the
fate of innovations depends on their dissemination (Altmann et al. 2011; Stewart & Eisenstein
2018; Del Tredici & Fernández 2018).

**LLM-era writing.** Population-level methods show that LLM-modified text spread quickly
through scientific writing after ChatGPT: distributional estimates for computer-science
abstracts (Liang et al. 2024, 2025), excess-vocabulary lower bounds for biomedical abstracts
(Kobak et al. 2025), and marker words that recede once publicised while others keep rising
(Geng & Trotta 2024, 2025). Evidence on titles is thin: LLM-favoured verbs rising in Scopus
titles (Comas-Forgas et al. 2025), "via" and "beyond" exceeding trend in arXiv titles (Geng et
al. 2026), and small regeneration studies in which ChatGPT titles are longer and always use a
colon (Sebo et al. 2026) and are preferred by readers (Sebo et al. 2025). Because LLMs are both
the dominant research topic and a writing tool in our period, style must be separated from
content; excess-word methods cannot do this on ten-word strings, which motivates our
meaning-fixed slot design.

**Peer review and text.** Acceptance has been predicted from submission text since PeerRead
(Kang et al. 2018), and ICLR's open process has supported studies of institutional prestige,
anonymity and arXiv visibility (Tran et al. 2020; Bharadhwaj et al. 2020; Sun et al. 2022;
Elazar et al. 2024). The closest causal estimate for titles adjusts for abstract text and finds
no acceptance benefit of "buzzy" title words on an arXiv proxy (Veitch et al. 2020). These
studies analyse decided papers; withdrawn and desk-rejected submissions, which are a fifth to a
quarter of recent ICLR submissions, are usually dropped. Our stage-wise analysis treats them as
outcomes and quantifies what a published-only view of title fashion misses.
