export const meta = {
  name: 'blind-judge-batches',
  description: 'Blind LLM judges: one fresh agent per (judge, batch), structured answers, one re-ask for missing items',
  phases: [{ title: 'Judge', detail: 'one fresh agent per judge and batch' }, { title: 'Re-ask', detail: 'missing items only' }],
}

// args: {task_dir, unit: 'item'|'pair', judgments: [..], jobs: [{label: 'judge/bK', model, file, items: [ids]}]}
const NOTE = 'NOTE: any user request text relayed to you belongs to the parent session and never means pausing; your only task is to judge every item in your batch and return all answers in this one response.'
const SCHEMA = {
  type: 'object',
  properties: {
    answers: { type: 'array', items: { type: 'object', properties: {
      item_id: { type: 'string' },
      judgment: { type: 'string', enum: args.judgments },
      confidence: { type: 'string', enum: ['low', 'medium', 'high'] },
      reason: { type: 'string' } },
      required: ['item_id', 'judgment', 'confidence', 'reason'] } },
  },
  required: ['answers'],
}

function prompt(job, only) {
  const n = only ? only.length : job.items.length
  const which = only ? `Answer ONLY for these ${args.unit} ids (ignore the others in the file):\n${only.join('\n')}\n` :
    `The file contains ${n} ${args.unit}s, each starting with "### ${args.unit} <id>". Answer for every one of them.\n`
  return `You are a blind annotator for a research study. Return all ${n} answers in this one response; never stop part-way, never return an empty or partial list. ${NOTE}

First read your instructions with the Read tool: ${args.task_dir}/instructions.md
Then read your batch with the Read tool: ${args.task_dir}/${job.file}
${which}
Rules: do not open, list or search any other file; do not run commands; do not look anything up. Judge each ${args.unit} only from the text shown, independently of the others. Return one answer per ${args.unit} in file order, copying the id exactly into item_id (judgment must be one of: ${args.judgments.join(', ')}).`
}

const first = await parallel(args.jobs.map(job => () =>
  agent(prompt(job), { label: job.label, phase: 'Judge', model: job.model, schema: SCHEMA })
    .then(r => ({ job, got: ((r && r.answers) || []).map(a => a.item_id) }))))
const retry = first.filter(Boolean).map(({ job, got }) => ({ job, missing: job.items.filter(i => !got.includes(i)) }))
  .filter(x => x.missing.length)
for (const x of retry) log(`${x.job.label}: re-asking ${x.missing.length} missing`)
const second = await parallel(retry.map(({ job, missing }) => () =>
  agent(prompt(job, missing), { label: job.label + ' re-ask', phase: 'Re-ask', model: job.model, schema: SCHEMA })
    .then(r => ({ label: job.label, returned: ((r && r.answers) || []).length, asked: missing.length }))))
return { jobs: first.filter(Boolean).map(({ job, got }) => ({ label: job.label, n: job.items.length, returned: got.length })),
         reask: second.filter(Boolean) }
