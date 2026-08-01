# Behavior Definition Rubric

<!-- Written by Fable 2026-08-01 (redesign §6.3); supervisor-editable.
     Applied whenever a behavior request is filed — by a meta read's graph-change
     proposal, an analytics flag (prune/split), a session, or the supervisor. -->

Every new behavior, behavior split, or trigger redefinition enters as a **behavior
request** and gets classified before anything is built. The classification decides who
designs it. The purpose of this rubric is to keep the supervisor off the critical path
for routine graph evolution while guaranteeing that nothing epistemically or
externally consequential ships without supervisor design.

## Classification

Walk the HARD criteria first. **Any single HARD hit → supervisor design queue.**
Otherwise classify SIMPLE.

### HARD — supervisor designs (or answers the brief, demoting it to SIMPLE)

1. **Changes what counts as knowledge.** Touches the law-worthiness bar, evidence or
   independence standards, confidence semantics, promotion/demotion logic — i.e.,
   would edit `prompts/induct.md`, `prompts/assess.md`, `laws/_schema.yaml` stage
   rules, or `METHOD.md`.
2. **Touches identity or voice.** Would edit `IDENTITY.md`, `LINEAGE.md`,
   `MEMORY.md`, or the persona layer of Discord prompts.
3. **External side effects.** Posts, publishes, emails, or writes anywhere outside
   the repo and its own Pinecone index — anything a non-operator can see.
4. **Hard to reverse.** Deletes or rewrites existing records (laws, bibliography,
   notes) rather than appending; changes git history; touches another project's
   resources (c3po namespaces).
5. **New spending shape.** Introduces a new model tier, a new external API, or a
   plausible >2x change in scheduled API spend.
6. **Splits or replaces an epistemic-core behavior** (`induct`, `assess`, `monitor`)
   — even when the split itself looks mechanical.

### SIMPLE — Claude drafts, supervisor approves

All of: clear inputs and outputs (files/queues in, files/queues out); a precedent
behavior exists whose shape it follows; side effects internal (repo files, own index,
log entries); errors recoverable by re-running; no HARD criterion touched.

Typical SIMPLE requests: a new intake source; a re-chunking or re-formatting pass; a
report/analytics view; a trigger-condition tightening on a non-core behavior; a
scheduling change; a prune of an inactive behavior.

**Model tier for drafting:** Sonnet by default. Use Opus when the draft requires
multi-step judgment about *content* (e.g., a new read-processing variant, a
non-trivial trigger interacting with law stages) — the giveaway is that the trigger
or prompt needs reasoning about research semantics, not just plumbing.

## The SIMPLE path

Claude drafts the complete registry entry — `id`, `name`, `phase`, `trigger`,
`action` (entrypoint, model, prompt file), `produces` — plus the prompt file if one
is needed, and files it in the approval queue with a three-line rationale (what need,
why simple, what precedent). The supervisor approves, edits-then-approves, or rejects
in the console. **Nothing runs before approval.**

## The HARD path — the brief

A HARD request goes to the supervisor design queue as a structured brief:

```yaml
request: ""          # one sentence: the behavior or change wanted
origin: ""           # meta-read proposal (bib id) | analytics flag | session | supervisor
why_hard: []         # which HARD criteria hit, one line each
claude_would: ""     # 3-6 lines: the design Claude would attempt, so the supervisor
                     #   reacts to something concrete instead of starting cold
questions: []        # the specific decisions only the supervisor can make —
                     #   answered well, these often demote the request to SIMPLE
```

The brief is the bottleneck-killer: most HARD requests are hard because of one or two
embedded decisions. If the supervisor answers `questions` without designing the whole
behavior, the request re-enters as SIMPLE with the answers as constraints.

## Anti-accumulation rule

Every request — including approved ones — names the behavior it expects to relieve,
replace, or feed. A request that adds a node without connecting to the funnel's
existing flow is rejected by default: the 26-behavior stub graveyard this redesign
cleaned up is what unconnected additions grow into.
