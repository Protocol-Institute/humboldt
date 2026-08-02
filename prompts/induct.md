# Induction Sweep — epistemic core prompt

<!-- Used by agent/induct.py (funnel stage 5). Model: Sonnet.
     Template slots: {{LAW_INVENTORY}} {{SEEDS}} {{RECENT_READS}} {{IDENTITY_EXCERPT}}
     Written by Fable 2026-08-01 (redesign §5); supervisor-editable.
     The bar defined here is the KPI's quality control: the law accumulation rate
     only means something if what accumulates are actually laws. -->

{{IDENTITY_EXCERPT}}

You are running an induction sweep: the pass that turns accumulated raw material into
law records, or strengthens existing ones. This is the sensemaking engine of the
funnel — the only place new laws enter the encyclopedia.

## Inputs

**Current law inventory** (id, title, stage, statement):
{{LAW_INVENTORY}}

**Unconsumed seeds** (law-shaped fragments from reads and captures):
{{SEEDS}}

**Recent read summaries** (shallow and deep, since the last sweep):
{{RECENT_READS}}

## Your task

For each candidate pattern you find in the seeds and reads, decide exactly one of:

1. **NEW LAW** — draft a new exploration-stage law record.
2. **EVIDENCE** — attach an example, counterexample, or reference to an existing law.
3. **LEAVE** — leave the material in the seed pool. This is the default.

## The bar for a new law

A law is a **general, falsifiable, mechanism-bearing claim about how protocolized or
artificial systems behave**. To qualify, you must be able to write all four of:

- **Statement** — 1–3 sentences, general (not about one case), falsifiable in
  principle. "X tends to happen under conditions Y because Z" is the shape.
- **Mechanism sketch** — a causal account of *why* the regularity would hold. A
  correlation with no candidate mechanism is a seed, not a law.
- **At least one concrete example** — a real case, with enough specificity that
  someone could check it.
- **Falsification sketch** — an observation that would refute it. If you cannot
  imagine the refuting observation, it is not a law.

**Disqualifiers** — do not create a law that is:
- A **topic or theme** ("trust in multi-agent systems matters").
- A **trend report** ("more papers are using X").
- A **single-case observation** without a generality argument.
- A **duplicate or near-duplicate** of an inventory law. If it overlaps, prefer
  EVIDENCE, or — if it genuinely refines scope — propose it as a *scoping amendment*
  in the evidence attachment, never as a parallel law.
- A **restatement of an established outside law** (Goodhart, Gall, Conway, etc.)
  without a protocol-theoretic delta. Imports must add something: a mechanism
  sharpening, a new structural variable, a protocol-specific signature. If you find
  an import candidate with a real delta, mark it `origin: imported` and name the
  source.

## The bar for evidence attachment

Attach evidence to an existing law only when the source actually bears on the law's
statement or one of its open questions — name which. Counterexamples are more valuable
than confirmations: if material contradicts a law, attach it as a counterexample with
`resolution: OPEN`. Never discard contradicting material, and never resolve a
counterexample yourself — that is the assess pass's job.

## Volume discipline

Quality over quantity, strictly. **Zero new laws is a normal and respectable outcome**
of a sweep — most sweeps should produce evidence attachments and nothing else. One
genuinely law-shaped record is worth more than five weak ones; weak records poison the
KPI and waste every downstream assessment pass. When torn between NEW LAW and LEAVE,
choose LEAVE — the seed pool persists and a future sweep with more material can
promote it.

## Output format

Return YAML only:

```yaml
new_laws:            # usually empty
  - title: ""
    statement: ""
    mechanism: ""
    justification: ""   # why this is law-shaped; which seeds/reads fed it
    origin: discovered  # or imported
    source: ""          # REQUIRED when origin is imported: the source law/work generalized (e.g. "arxiv-2512.07526 (Tan)")
    examples: [{domain: "", description: "", source: ""}]
    falsification: ""
    seeds_consumed: []  # seed ids folded into this law
evidence:
  - law: "L-NNN"
    kind: example | counterexample | reference
    bears_on: ""        # which part of the law / which open question
    domain: ""
    description: ""
    source: ""
leave: []               # seed ids reviewed and deliberately left, with one-line reason
```
