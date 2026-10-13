export const meta = {
  name: 'facets-pilot',
  description: 'Pilot stage / goal / foundation-model facets on the 300 pilot papers: 2 independent annotators, then adjudication',
  phases: [
    { title: 'Annotate', detail: '4 batches x 2 independent annotators using facets codebook v0.9' },
    { title: 'Adjudicate', detail: 'one adjudicator resolves every paper where any facet differs' },
  ],
}

const STAGES = ['data', 'architecture', 'training', 'post_training', 'inference', 'evaluation', 'system', 'general']
const GOALS = ['capability', 'efficiency', 'data_efficiency', 'generalization', 'robustness_security', 'safety_alignment',
  'understanding', 'reliability', 'privacy_fairness']
const ITEM = {
  paper: { type: 'string' },
  stage: { type: 'string', enum: STAGES },
  goal: { type: 'string', enum: GOALS },
  foundation_model: { type: 'string', enum: ['yes', 'no'] },
}
const LABELS = {
  type: 'object',
  properties: { labels: { type: 'array', items: { type: 'object', properties: { ...ITEM, uncertain: { type: 'boolean' } },
    required: ['paper', 'stage', 'goal', 'foundation_model', 'uncertain'] } } },
  required: ['labels'],
}
const DECISIONS = {
  type: 'object',
  properties: { decisions: { type: 'array', items: { type: 'object', properties: { ...ITEM,
    reason: { type: 'string', description: 'max 20 words, citing the codebook rule used' } },
    required: ['paper', 'stage', 'goal', 'foundation_model', 'reason'] } } },
  required: ['decisions'],
}

phase('Annotate')
const runs = await parallel(args.batches.flatMap((path, i) => ['A', 'B'].map(rater => () =>
  agent(`You are annotating machine-learning papers (ICLR submissions) on three facets of their main contribution.
First use the Read tool to read the codebook at ${args.codebook} and follow it exactly.
Then read ${path}: 75 papers, each with title and abstract under a heading "### paper pNNN".
For EVERY paper give stage, goal, foundation_model and uncertain, copying the paper id exactly.
Judge from the title and abstract only. Work independently; do not read any other file.`,
    { label: `batch ${i + 1} · annotator ${rater}`, phase: 'Annotate', schema: LABELS })
    .then(r => (r ? r.labels : []).map(l => ({ ...l, rater, batch: i + 1 }))))))
const labels = runs.filter(Boolean).flat()
const by = {}
for (const l of labels) (by[l.paper] ||= {})[l.rater] = l
const same = (a, b) => a && b && a.stage === b.stage && a.goal === b.goal && a.foundation_model === b.foundation_model
const disputes = Object.entries(by).filter(([, v]) => !same(v.A, v.B))
log(`${labels.length} labels; ${disputes.length} of ${Object.keys(by).length} papers differ on at least one facet`)

phase('Adjudicate')
const fmt = l => l ? `${l.stage} / ${l.goal} / FM ${l.foundation_model}` : 'missing'
const list = disputes.map(([p, v]) => `- ${p} | A: ${fmt(v.A)} | B: ${fmt(v.B)} | file: ${args.batches[(v.A || v.B).batch - 1]}`).join('\n')
const adj = disputes.length ? await agent(`You are the adjudicator for a facet annotation of ICLR papers.
First Read the codebook at ${args.codebook} and apply it exactly. Two independent annotators differed on at least one
facet for the papers below (format: stage / goal / foundation model). For each paper, Read its title and abstract in
the file given and decide all three facets by the codebook (you may choose values neither annotator chose), with a
short reason citing the rule. Return one decision per paper (${disputes.length} total), copying ids exactly.

${list}`, { label: 'adjudicator', phase: 'Adjudicate', schema: DECISIONS }) : { decisions: [] }
return { labels, decisions: adj ? adj.decisions : [], n_disputes: disputes.length }