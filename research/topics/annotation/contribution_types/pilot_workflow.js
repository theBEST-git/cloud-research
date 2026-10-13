export const meta = {
  name: 'contribution-type-pilot',
  description: 'Pilot the contribution-type codebook: 300 fresh papers, 2 independent annotators each, adjudicate disagreements',
  phases: [
    { title: 'Annotate', detail: '4 batches x 2 independent annotators using codebook v0.9' },
    { title: 'Adjudicate', detail: 'one adjudicator resolves every paper where annotators differ' },
  ],
}

const TYPES = ['method', 'model', 'theory', 'empirical', 'system', 'dataset_benchmark', 'evaluation', 'problem',
  'application', 'recipe', 'perspective', 'survey_position']
const LABELS = {
  type: 'object',
  properties: {
    labels: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          paper: { type: 'string' },
          primary_type: { type: 'string', enum: TYPES },
          secondary_type: { type: 'string', enum: [...TYPES, 'none'] },
          uncertain: { type: 'boolean' },
        },
        required: ['paper', 'primary_type', 'secondary_type', 'uncertain'],
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
          paper: { type: 'string' },
          primary_type: { type: 'string', enum: TYPES },
          secondary_type: { type: 'string', enum: [...TYPES, 'none'] },
          reason: { type: 'string', description: 'max 20 words, citing the codebook rule used' },
        },
        required: ['paper', 'primary_type', 'secondary_type', 'reason'],
      },
    },
  },
  required: ['decisions'],
}

phase('Annotate')
const runs = await parallel(args.batches.flatMap((path, i) => ['A', 'B'].map(rater => () =>
  agent(`You are annotating machine-learning papers (ICLR submissions) for the KIND of contribution they make.
First use the Read tool to read the codebook at ${args.codebook} and follow it exactly.
Then read ${path}: 75 papers, each with title and abstract under a heading "### paper pNNN".
For EVERY paper give primary_type, secondary_type (or "none") and uncertain, copying the paper id exactly.
Judge from the title and abstract only. Work independently; do not read any other file.`,
    { label: `batch ${i + 1} · annotator ${rater}`, phase: 'Annotate', schema: LABELS })
    .then(r => (r ? r.labels : []).map(l => ({ ...l, rater, batch: i + 1 }))))))
const labels = runs.filter(Boolean).flat()
const by = {}
for (const l of labels) (by[l.paper] ||= {})[l.rater] = l
const disputes = Object.entries(by).filter(([, v]) => !v.A || !v.B || v.A.primary_type !== v.B.primary_type || v.A.secondary_type !== v.B.secondary_type)
log(`${labels.length} labels; ${disputes.length} of ${Object.keys(by).length} papers need adjudication`)

phase('Adjudicate')
const batchOf = p => args.batches[(by[p].A || by[p].B).batch - 1]
const list = disputes.map(([p, v]) => `- ${p} | A: ${v.A ? v.A.primary_type + ' / ' + v.A.secondary_type : 'missing'} | B: ${v.B ? v.B.primary_type + ' / ' + v.B.secondary_type : 'missing'} | file: ${batchOf(p)}`).join('\n')
const adj = disputes.length ? await agent(`You are the adjudicator for a contribution-type annotation of ICLR papers.
First Read the codebook at ${args.codebook} and apply it exactly. Two independent annotators disagreed on the papers below
(format: primary / secondary). For each paper, Read its title and abstract in the file given, then decide the correct
primary_type and secondary_type by the codebook (you may choose a type neither annotator chose) and give a short reason
citing the rule. Return one decision per paper (${disputes.length} total), copying ids exactly.

${list}`, { label: 'adjudicator', phase: 'Adjudicate', schema: DECISIONS }) : { decisions: [] }
return { labels, decisions: adj ? adj.decisions : [], n_disputes: disputes.length }