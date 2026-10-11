export const meta = {
  name: 'topic-naming',
  description: 'Name 20 broad, 100 middle and 198 fine topics; consistency review; blind name check',
  phases: [
    { title: 'Name', detail: '5 batches of broad topics, named top-down with coherence flags' },
    { title: 'Review', detail: 'one reviewer checks all names for duplicates, vagueness and sibling distinctness' },
    { title: 'Blind check', detail: '2 annotators match held-out papers to fine-topic names' },
  ],
}

const H = args.hierarchy
const GUIDE = `You are naming research topics found by clustering ICLR submissions (2017-2026) by the content of their titles and abstracts.
Each topic shows its size, papers per year, its most distinctive author keywords, and example titles.
Topics are nested: broad (codes c..) contain middle topics (m..), which contain fine topics (f..).

For EVERY topic write:
- name: 2-6 words, sentence case (capitalise only the first word, proper nouns and acronyms), no trailing period.
  Name what the papers are actually about, based mainly on the example titles; the keywords are a hint.
  Use standard ML terminology; common acronyms are fine (LLM, RL, GNN, VLM, 3D, PDE).
- Distinctness: a fine topic's name must distinguish it from its sibling fine topics (same middle topic);
  a middle topic's name must distinguish it from its sibling middle topics (same broad topic);
  a broad topic's name must cover all of its middle topics. A child's name is narrower than (or, for an only child, equal to) its parent's.
- Avoid empty words such as "deep learning", "neural networks", "methods", "approaches", "various", "miscellaneous",
  "advances in", "applications" unless nothing more specific is true.
- description: one sentence (max 25 words) saying what papers in the topic typically do.
- coherence, judged from the example titles: "coherent" = one clear theme; "mostly_coherent" = one clear theme plus some outliers;
  "mixed" = two or more unrelated themes. For "mixed", name the dominant themes joined by "and", and explain in note (max 15 words).
Copy each topic code exactly.`

const NAMES = {
  type: 'object',
  properties: {
    topics: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          topic: { type: 'string' },
          name: { type: 'string' },
          description: { type: 'string' },
          coherence: { type: 'string', enum: ['coherent', 'mostly_coherent', 'mixed'] },
          note: { type: 'string' },
        },
        required: ['topic', 'name', 'description', 'coherence'],
      },
    },
  },
  required: ['topics'],
}
const REVISIONS = {
  type: 'object',
  properties: {
    revisions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          topic: { type: 'string' }, name: { type: 'string' },
          description: { type: 'string', description: 'only if it also needs changing' },
          reason: { type: 'string', description: 'max 15 words' },
        },
        required: ['topic', 'name', 'reason'],
      },
    },
  },
  required: ['revisions'],
}
const ANSWERS = {
  type: 'object',
  properties: { answers: { type: 'array', items: { type: 'object', properties: { paper: { type: 'string' }, fine: { type: 'string' } }, required: ['paper', 'fine'] } } },
  required: ['answers'],
}

const codesFor = cs => cs.flatMap(c => [c, ...Object.keys(H[c]), ...Object.values(H[c]).flat()])
const names = {}

phase('Name')
await parallel(args.batches.map((b, i) => () => agent(`${GUIDE}

TASK: Use the Read tool to read ${b.path}. It contains broad topics ${b.coarse.join(', ')} with all their middle and fine topics
(${codesFor(b.coarse).length} topics in total). Name every one of them. Do not read any other file.`,
  { label: `naming batch ${i + 1}`, phase: 'Name', schema: NAMES }).then(r => {
    for (const t of (r ? r.topics : [])) names[t.topic] = { name: t.name, description: t.description, coherence: t.coherence, note: t.note || '' }
  })))

const expected = codesFor(Object.keys(H))
const missing = expected.filter(c => !names[c])
if (missing.length) {
  log(`${missing.length} topics unnamed after first pass: ${missing.join(', ')} - naming them now`)
  const byBatch = args.batches.map(b => ({ b, codes: codesFor(b.coarse).filter(c => !names[c]) })).filter(x => x.codes.length)
  await parallel(byBatch.map(({ b, codes }) => () => agent(`${GUIDE}

TASK: Use the Read tool to read ${b.path}. Name ONLY these topics: ${codes.join(', ')}. Do not read any other file.`,
    { label: 'naming retry', phase: 'Name', schema: NAMES }).then(r => {
      for (const t of (r ? r.topics : [])) if (codes.includes(t.topic)) names[t.topic] = { name: t.name, description: t.description, coherence: t.coherence, note: t.note || '' }
    })))
}
log(`named ${Object.keys(names).length}/${expected.length} topics`)

const tree = Object.keys(H).sort().map(c => [
  `${c} [broad] ${names[c]?.name} - ${names[c]?.description}`,
  ...Object.keys(H[c]).sort().flatMap(m => [
    `  ${m} [middle in ${c}] ${names[m]?.name} - ${names[m]?.description} (${names[m]?.coherence})`,
    ...H[c][m].map(f => `    ${f} [fine in ${m}] ${names[f]?.name} - ${names[f]?.description} (${names[f]?.coherence})`),
  ]),
].join('\n')).join('\n')

phase('Review')
const rev = await agent(`${GUIDE}

TASK: Five annotators named the topics below independently, each covering different broad topics. Review ALL names together and
return revisions ONLY where needed:
- two topics at the same level with the same or nearly the same name (make both distinct),
- sibling names that do not distinguish the topics, or a child name broader than its parent,
- names that are vague or use empty words,
- the same concept worded differently across branches (pick one wording),
- style violations (length, sentence case).
If evidence is needed, the source material is in these files: ${args.batches.map(b => b.path).join(', ')}.
Keep good names unchanged; return an empty list if nothing needs fixing.

${tree}`, { label: 'consistency reviewer', phase: 'Review', schema: REVISIONS })
const revisions = (rev ? rev.revisions : []).filter(r => names[r.topic])
for (const r of revisions) {
  names[r.topic] = { ...names[r.topic], name: r.name, description: r.description || names[r.topic].description, revised: r.reason }
}
log(`reviewer revised ${revisions.length} names`)

phase('Blind check')
const options = Object.keys(H).sort().map(c =>
  `Options for papers in broad topic ${c}:\n` + Object.values(H[c]).flat().map(f => `  ${f}: ${names[f]?.name}`).join('\n')).join('\n\n')
const checks = await parallel(args.check_ranges.map((rg, i) => () => agent(`You are checking whether topic names describe their topics.
Use the Read tool to read ${args.check_path}. Do NOT read any other file. Handle ONLY papers ${rg[0]} to ${rg[1]} (inclusive).
For each of those papers, read its title and abstract opening, then choose the single best-fitting fine topic from the options
listed for that paper's broad topic below. Answer for every paper in your range, with the fine topic code copied exactly.

${options}`, { label: `blind checker ${i + 1}`, phase: 'Blind check', schema: ANSWERS })))
const answers = checks.filter(Boolean).flatMap(r => r.answers)
log(`blind check: ${answers.length} answers`)

return { names, revisions, missing_after_retry: expected.filter(c => !names[c]), answers }