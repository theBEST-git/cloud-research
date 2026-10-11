export const meta = {
  name: 'keyword-type-annotation',
  description: 'Two independent annotators type 912 ICLR keywords; measure agreement; adjudicate disagreements',
  phases: [
    { title: 'Annotate', detail: '4 batches x 2 independent annotators with one shared codebook' },
    { title: 'Adjudicate', detail: 'one adjudicator resolves every disagreement consistently' },
  ],
}

const TYPES = ['generic_field', 'research_area', 'specific_topic', 'application_domain', 'property', 'contribution_type', 'unclear']
const CODEBOOK = `You are annotating author keywords from ICLR (a top machine-learning conference) submissions, 2017-2026.
Assign each keyword exactly ONE type. Judge what the keyword names, as used by ML researchers at ICLR.

TYPES
- generic_field: names the whole discipline; would fit most ICLR papers and identifies no subfield.
  e.g. deep learning, machine learning, neural networks, deep neural networks, artificial intelligence.
- research_area: a broad subfield that contains many distinct research lines, each with its own literature
  (you could name 5+ separately studied lines inside it); roughly the size of a conference track.
  e.g. reinforcement learning, computer vision, natural language processing, generative models, large language models, optimization.
- specific_topic: a specific problem, task, method, technique, model family, algorithm or research line.
  e.g. offline reinforcement learning, LoRA, contrastive learning, knowledge distillation, in-context learning, mixture-of-experts.
- application_domain: a real-world domain, science, or sector that ML is applied to (the keyword names the domain, not an ML method).
  e.g. drug discovery, protein design, healthcare, autonomous driving, weather forecasting, neuroscience, finance.
- property: a cross-cutting property, desideratum or phenomenon of models/methods studied across many areas.
  e.g. robustness, generalization, efficiency, fairness, privacy, calibration, uncertainty, scalability, memorization.
- contribution_type: the KIND of contribution rather than its subject.
  e.g. benchmark, dataset, evaluation, theory, empirical study, survey, analysis, position paper.
- unclear: genuinely ambiguous or uninterpretable even with the context given. Use sparingly.

DECISION RULES (apply in order)
1. If it names a kind of contribution -> contribution_type.
2. If it names a real-world domain/science/sector -> application_domain.
3. If it names a property/desideratum/phenomenon that cuts across areas -> property.
4. Otherwise decide granularity: whole discipline -> generic_field; track-sized subfield -> research_area; anything narrower -> specific_topic.
   Tie-break between research_area and specific_topic: if one survey paper could reasonably cover it -> specific_topic.
Use the context (paper count, co-listed keywords, example titles) only to resolve what the keyword means; do not let paper count alone decide granularity.`

const LABELS = {
  type: 'object',
  properties: {
    labels: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          keyword: { type: 'string', description: 'copied exactly from the file, without quotes' },
          type: { type: 'string', enum: TYPES },
        },
        required: ['keyword', 'type'],
      },
    },
  },
  required: ['labels'],
}
const DECISIONS = {
  type: 'object',
  properties: {
    decisions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          keyword: { type: 'string' },
          type: { type: 'string', enum: TYPES },
          reason: { type: 'string', description: 'at most 15 words' },
        },
        required: ['keyword', 'type', 'reason'],
      },
    },
  },
  required: ['decisions'],
}

const chunks = args.chunks
phase('Annotate')
const runs = await parallel(chunks.flatMap((c, i) => ['A', 'B'].map(rater => () =>
  agent(`${CODEBOOK}

TASK: Use the Read tool to read ${c.path}. It has ${c.n} lines; each line is one keyword with context.
Label EVERY keyword (exactly ${c.n} labels). Copy each keyword string exactly as written between the quotes after "keyword:".
Work independently; do not look for other annotators' files.`,
    { label: `batch ${i + 1} · annotator ${rater}`, phase: 'Annotate', schema: LABELS })
    .then(r => ({ chunk: i, rater, labels: r ? r.labels : [] })))))

// Agreement: plain code
const byChunk = chunks.map(() => ({ A: {}, B: {} }))
for (const r of runs.filter(Boolean)) for (const l of r.labels) byChunk[r.chunk][r.rater][l.keyword] = l.type
let n = 0, agree = 0
const cntA = {}, cntB = {}, confusion = {}, disputes = [], final = {}
const missing = []
chunks.forEach((c, i) => {
  const { A, B } = byChunk[i]
  const keys = new Set([...Object.keys(A), ...Object.keys(B)])
  for (const k of keys) {
    if (!(k in A) || !(k in B)) { missing.push(k); disputes.push({ keyword: k, a: A[k] || 'missing', b: B[k] || 'missing', chunk: i }); continue }
    n++; cntA[A[k]] = (cntA[A[k]] || 0) + 1; cntB[B[k]] = (cntB[B[k]] || 0) + 1
    if (A[k] === B[k]) { agree++; final[k] = A[k] } else {
      disputes.push({ keyword: k, a: A[k], b: B[k], chunk: i })
      const key = [A[k], B[k]].sort().join(' vs ')
      confusion[key] = (confusion[key] || 0) + 1
    }
  }
  log(`batch ${i + 1}: A labelled ${Object.keys(A).length}/${c.n}, B labelled ${Object.keys(B).length}/${c.n}`)
})
const po = agree / n
const pe = TYPES.reduce((s, t) => s + ((cntA[t] || 0) / n) * ((cntB[t] || 0) / n), 0)
const kappa = (po - pe) / (1 - pe)
log(`raw agreement ${(100 * po).toFixed(1)}% on ${n} keywords, Cohen's kappa ${kappa.toFixed(3)}; ${disputes.length} to adjudicate (${missing.length} labelled by only one annotator)`)

phase('Adjudicate')
const list = disputes.map(d => `- "${d.keyword}" | annotator A: ${d.a} | annotator B: ${d.b} | context file: ${chunks[d.chunk].path}`).join('\n')
const adj = await agent(`${CODEBOOK}

TASK: Two independent annotators disagreed on the keywords below. You are the adjudicator. For each one, decide the correct type
by the codebook and decision rules (you may choose a type neither annotator chose). For context on any keyword, Read its context file
and find the line for that keyword. Return one decision per keyword (${disputes.length} total), keyword copied exactly.

${list}`, { label: 'adjudicator', phase: 'Adjudicate', schema: DECISIONS })
const decided = {}
for (const d of (adj ? adj.decisions : [])) decided[d.keyword] = d
let unresolved = []
for (const d of disputes) {
  if (decided[d.keyword]) final[d.keyword] = decided[d.keyword].type
  else unresolved.push(d.keyword)
}
if (unresolved.length) log(`WARNING: ${unresolved.length} disputed keywords got no adjudication decision`)
const dist = {}
for (const t of Object.values(final)) dist[t] = (dist[t] || 0) + 1
return {
  n_expected: chunks.reduce((s, c) => s + c.n, 0), n_final: Object.keys(final).length,
  raw_agreement: po, kappa, n_double_labelled: n, n_disputes: disputes.length, missing_single_rater: missing.length,
  unresolved, confusion, final_distribution: dist,
  disputes: disputes.map(d => ({ ...d, final: final[d.keyword] || null, reason: decided[d.keyword] ? decided[d.keyword].reason : null })),
  final,
}