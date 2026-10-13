export const meta = {
  name: 'contribution-training-labels',
  description: 'Label 2,000 papers (contribution type, secondary, foundation model); double-label 200 and adjudicate',
  phases: [
    { title: 'Label', detail: '20 batches of 100, one annotator each; batches 1-2 also get a second annotator' },
    { title: 'Retry', detail: 'relabel any papers an annotator skipped' },
    { title: 'Adjudicate', detail: 'resolve disagreements on the double-labelled papers' },
  ],
}

const TYPES = ['method', 'model', 'theory', 'empirical', 'system', 'dataset_benchmark', 'evaluation', 'problem',
  'application', 'recipe', 'perspective', 'survey_position']
const ITEM = {
  paper: { type: 'string' },
  primary_type: { type: 'string', enum: TYPES },
  secondary_type: { type: 'string', enum: [...TYPES, 'none'] },
  foundation_model: { type: 'string', enum: ['yes', 'no'] },
}
const LABELS = { type: 'object', properties: { labels: { type: 'array', items: { type: 'object',
  properties: { ...ITEM, uncertain: { type: 'boolean' } }, required: ['paper', 'primary_type', 'secondary_type', 'foundation_model', 'uncertain'] } } },
  required: ['labels'] }
const DECISIONS = { type: 'object', properties: { decisions: { type: 'array', items: { type: 'object',
  properties: { ...ITEM, reason: { type: 'string', description: 'max 20 words, citing the rule used' } },
  required: ['paper', 'primary_type', 'secondary_type', 'foundation_model', 'reason'] } } }, required: ['decisions'] }

const prompt = (path, n, only) => `You are annotating machine-learning papers (ICLR submissions) for the KIND of contribution they make.
First use the Read tool to read the instructions at ${args.instructions} and follow them exactly.
Then read ${path}: ${n} papers, each with title and abstract under a heading "### paper tNNNN" (read the whole file;
use several Read calls with offset/limit if needed).
${only ? `Label ONLY these papers: ${only.join(', ')}.` : 'Label EVERY paper in the file.'}
For each paper give primary_type, secondary_type (or "none"), foundation_model (yes/no) and uncertain, copying ids exactly.
Judge from the title and abstract only. Work independently; do not read any other file.`

const jobs = args.batches.flatMap((b, i) => [{ ...b, rater: 'A', i }, ...(b.double ? [{ ...b, rater: 'B', i }] : [])])
phase('Label')
const results = await parallel(jobs.map(j => () =>
  agent(prompt(j.path, j.n), { label: `batch ${j.i + 1} · annotator ${j.rater}`, phase: 'Label', schema: LABELS })
    .then(r => ({ j, labels: (r ? r.labels : []).filter(l => j.ids.includes(l.paper)) }))))

phase('Retry')
const retried = await parallel(results.filter(Boolean).map(res => () => {
  const got = new Set(res.labels.map(l => l.paper))
  const missing = res.j.ids.filter(p => !got.has(p))
  if (!missing.length) return Promise.resolve(res)
  log(`batch ${res.j.i + 1} annotator ${res.j.rater}: ${missing.length} papers missing, relabelling`)
  return agent(prompt(res.j.path, res.j.n, missing), { label: `retry batch ${res.j.i + 1} · ${res.j.rater}`, phase: 'Retry', schema: LABELS })
    .then(r => ({ j: res.j, labels: [...res.labels, ...(r ? r.labels : []).filter(l => missing.includes(l.paper))] }))
}))
const labels = retried.filter(Boolean).flatMap(res => res.labels.map(l => ({ ...l, rater: res.j.rater, batch: res.j.i + 1 })))
log(`${labels.filter(l => l.rater === 'A').length} primary labels, ${labels.filter(l => l.rater === 'B').length} second labels`)

phase('Adjudicate')
const by = {}
for (const l of labels) (by[l.paper] ||= {})[l.rater] = l
const fmt = l => `${l.primary_type} / ${l.secondary_type} / FM ${l.foundation_model}`
const disputes = Object.entries(by).filter(([, v]) => v.A && v.B &&
  (v.A.primary_type !== v.B.primary_type || v.A.secondary_type !== v.B.secondary_type || v.A.foundation_model !== v.B.foundation_model))
const adj = disputes.length ? await agent(`You are the adjudicator for a contribution-type annotation of ICLR papers.
First Read the instructions at ${args.instructions} and apply them exactly. Two independent annotators differed on the papers
below (format: primary / secondary / foundation model). For each, Read its title and abstract in the file given and decide
all three labels by the instructions (you may choose values neither annotator chose), with a short reason.
Return one decision per paper (${disputes.length} total), copying ids exactly.

${disputes.map(([p, v]) => `- ${p} | A: ${fmt(v.A)} | B: ${fmt(v.B)} | file: ${args.batches[v.A.batch - 1].path}`).join('\n')}`,
  { label: 'adjudicator', phase: 'Adjudicate', schema: DECISIONS }) : { decisions: [] }
return { labels, decisions: adj ? adj.decisions : [], n_disputes: disputes.length }