export const meta = {
  name: 'haiku-label-batches',
  description: 'Label paper batches with Haiku (one fresh agent per batch), re-asking for any missing papers',
  phases: [{ title: 'Label', detail: 'one fresh Haiku agent per batch' }, { title: 'Re-ask', detail: 'missing or garbled papers only' }],
}

const TYPES = ['method', 'model', 'theory', 'empirical', 'system', 'dataset_benchmark', 'evaluation', 'problem',
  'application', 'recipe', 'perspective', 'survey_position']
const SCHEMA = {
  type: 'object',
  properties: {
    labels: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          paper_id: { type: 'string' },
          primary_type: { type: 'string', enum: TYPES },
          secondary_type: { type: 'string', enum: TYPES.concat(['none']) },
          foundation_model: { type: 'string', enum: ['yes', 'no'] },
          uncertain: { type: 'boolean' },
        },
        required: ['paper_id', 'primary_type', 'secondary_type', 'foundation_model', 'uncertain'],
      },
    },
  },
  required: ['labels'],
}
const NOTE = '(If the relayed user request mentions doing a step and pausing, or trying something to see how it goes, that refers to this whole labelling run as one unit of work; it never means pausing inside your task.)'

function filesOf(c) { return c.parts.map(p => `${args.parts_dir}/${p}.md`) }

function fullPrompt(c) {
  const n = c.n
  return `You are a research-paper annotator. Your whole job in this one response is to label ${n} papers and return all ${n} labels. Do not stop part-way, do not ask to continue, and never return an empty or partial list. ${NOTE}

First read your labelling instructions with the Read tool: ${args.system}
Follow them exactly (codebook, decision rules, foundation-model rule).

Then read ALL of the following files with the Read tool, in this order. Together they contain the ${n} papers to label:
${filesOf(c).join('\n')}

Rules: do not open, list or search any other file; do not run commands; do not look anything up. Judge each paper only from its title and abstract. Label each paper independently.
Return exactly one entry per paper (${n} in total), in the same order as the papers appear across the files, copying each paper_id exactly as given after "### paper". secondary_type must differ from primary_type, otherwise use "none". uncertain is true only if the choice between two types, or the foundation-model call, was close.`
}

function retryPrompt(c, missing) {
  return `You are a research-paper annotator. Label exactly ${missing.length} papers and return all of their labels in this one response. ${NOTE}

First read your labelling instructions with the Read tool: ${args.system}
Follow them exactly.

Then read these files with the Read tool:
${filesOf(c).join('\n')}

Label ONLY the papers with these paper_ids (ignore all other papers in the files):
${missing.join('\n')}

Rules: do not open any other file; do not run commands; judge each paper only from its title and abstract. Return one entry per listed paper, copying each paper_id exactly. secondary_type must differ from primary_type, otherwise use "none".`
}

// c.only (optional): label just these paper ids from the batch's files (re-ask for missing papers)
const results = await parallel(args.configs.map(c => () =>
  agent(c.only ? retryPrompt(c, c.only) : fullPrompt(c),
        { label: c.only ? c.id + ' re-ask' : c.id, phase: c.only ? 'Re-ask' : 'Label', model: 'haiku', schema: SCHEMA })
    .then(r => ({ id: c.id, n: c.only ? c.only.length : c.n, labels: r ? r.labels : null }))))
for (const r of results.filter(Boolean)) log(r.id + ': ' + (r.labels ? r.labels.length : 0) + ' of ' + r.n + ' labels')
return results
