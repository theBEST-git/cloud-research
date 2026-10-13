export const meta = {
  name: 'contribution-type-open-coding',
  description: 'Open-code 200 ICLR abstracts for contribution type (2 coders each), then derive categories bottom-up',
  phases: [
    { title: 'Open coding', detail: '4 batches x 2 independent coders, free-text labels, no predefined list' },
    { title: 'Synthesis', detail: 'group all free-text labels bottom-up into contribution-type categories' },
  ],
}

const CODE_GUIDE = `You are doing OPEN CODING for a study of what kinds of contributions machine-learning papers make.
For each paper below (title + abstract from ICLR submissions, 2017-2026), describe the KIND of contribution the paper
offers the research community - what it gives others - NOT its subject area. For example, "graph neural networks" or
"reinforcement learning" are subjects, not kinds of contribution.

For every paper write:
- primary: a short label (2-6 words) in YOUR OWN words for the main kind of contribution
- secondary: a second kind of contribution if one is clearly present, otherwise an empty string
- evidence: a short quote or paraphrase from the abstract that supports your label (max 20 words)
- clarity: "clear" if the abstract makes the kind of contribution obvious, "ambiguous" otherwise
There is no predefined list of labels: use whatever vocabulary describes the paper best, but stay consistent across papers
(use the same words when two papers make the same kind of contribution). Work independently.`

const CODES = {
  type: 'object',
  properties: {
    codes: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          paper: { type: 'string' }, primary: { type: 'string' }, secondary: { type: 'string' },
          evidence: { type: 'string' }, clarity: { type: 'string', enum: ['clear', 'ambiguous'] },
        },
        required: ['paper', 'primary', 'secondary', 'evidence', 'clarity'],
      },
    },
  },
  required: ['codes'],
}
const SYNTH = {
  type: 'object',
  properties: {
    categories: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' },
          definition: { type: 'string', description: '1-2 sentences' },
          decision_rule: { type: 'string', description: 'how to tell it apart from the closest other categories' },
          free_text_labels: { type: 'array', items: { type: 'string' } },
          example_papers: { type: 'array', items: { type: 'string' } },
          confusable_with: { type: 'array', items: { type: 'string' } },
        },
        required: ['name', 'definition', 'decision_rule', 'free_text_labels', 'example_papers', 'confusable_with'],
      },
    },
    assignments: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          paper: { type: 'string' }, coder: { type: 'string', enum: ['A', 'B'] },
          primary_category: { type: 'string' }, secondary_category: { type: 'string' },
        },
        required: ['paper', 'coder', 'primary_category', 'secondary_category'],
      },
    },
    observations: { type: 'array', items: { type: 'string' }, description: 'tensions, rare types, merges considered, mixed papers' },
  },
  required: ['categories', 'assignments', 'observations'],
}

phase('Open coding')
const runs = await parallel(args.batches.flatMap((path, i) => ['A', 'B'].map(coder => () =>
  agent(`${CODE_GUIDE}

TASK: Use the Read tool to read ${path}. It contains 50 papers (headings "### paper qNNN"). Code every one of them,
copying the paper id exactly (e.g. q001). Do not read any other file.`,
    { label: `batch ${i + 1} · coder ${coder}`, phase: 'Open coding', schema: CODES })
    .then(r => (r ? r.codes : []).map(c => ({ ...c, coder, batch: i + 1 }))))))
const codes = runs.filter(Boolean).flat()
log(`collected ${codes.length} codes (expected ${args.batches.length * 100})`)

phase('Synthesis')
const listing = codes.map(c => `${c.paper} | coder ${c.coder} | primary: ${c.primary} | secondary: ${c.secondary || '-'} | ${c.clarity}`).join('\n')
const syn = await agent(`You are synthesising an open-coding study of what KINDS of contributions machine-learning papers make
(not their subject areas). Two independent coders described each of 200 ICLR papers in their own words; their free-text
labels are below. Build the category scheme BOTTOM-UP from these labels:
- group labels that describe the same kind of contribution, and name each group;
- let the number of categories follow from the data; merge groups that coders could not reliably tell apart, and keep a
  separate category only if it is clearly distinct and judgeable from an abstract;
- note rare or unusual kinds of contribution, and how often papers make more than one kind;
- do not impose a standard taxonomy from the literature.
Then assign every coder's primary (and secondary, if any; else empty string) label to one of your categories, so that
agreement between the two coders can be measured (400 assignments: each paper x coder A and B).
If you need context, the abstracts are in: ${args.batches.join(', ')}.

${listing}`, { label: 'synthesiser', phase: 'Synthesis', schema: SYNTH })

// agreement between coders on synthesised primary categories
const byPaper = {}
for (const a of (syn ? syn.assignments : [])) (byPaper[a.paper] ||= {})[a.coder] = a.primary_category
const pairs = Object.values(byPaper).filter(p => p.A && p.B)
const cats = [...new Set(pairs.flatMap(p => [p.A, p.B]))]
const n = pairs.length, agree = pairs.filter(p => p.A === p.B).length
const pa = c => pairs.filter(p => p.A === c).length / n, pb = c => pairs.filter(p => p.B === c).length / n
const pe = cats.reduce((s, c) => s + pa(c) * pb(c), 0)
const kappa = n ? (agree / n - pe) / (1 - pe) : null
log(`coder agreement on synthesised categories: ${n ? (100 * agree / n).toFixed(1) : '-'}% of ${n} papers, kappa ${kappa === null ? '-' : kappa.toFixed(2)}`)
return { codes, synthesis: syn, agreement: { papers: n, raw: n ? agree / n : null, kappa } }