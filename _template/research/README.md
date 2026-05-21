# Research Inventory Pattern

The research inventory (`research/`) is the cumulative knowledge base — the structured output of research sessions, maintained across all time.

## Directory structure

```
research/
├── laws/           YAML files — candidate and established laws
├── hypotheses/     YAML files — active research questions
└── theories/       Markdown files — unified theory development
```

## Naming conventions

- Laws: `L-NNN-short-name.yaml` (e.g., `L-001-ossification.yaml`)
- Hypotheses: `H-NNN-short-name.yaml` (e.g., `H-001-coordination-cost.yaml`)
- Theories: descriptive markdown file names

Numbers are permanent. Names may evolve.

## Law schema (YAML)

```yaml
id: "L-NNN"
name: "Short descriptive name"
statement: >
  Precise, domain-neutral statement of the law. Should be falsifiable.
type: conservation | hardness | lifecycle | failure | scaling | evolution | interaction | equilibrium
confidence: speculative | candidate | established | contested
domain_scope:
  - Domain where confirmed
  - Domain where confirmed
adversarial_domain: >
  Description of the best counterexample or falsifying case examined.
  Outcome: falsified / scope-refined / survived.
evidence:
  - "Short description of supporting evidence with source"
related_laws:
  - L-NNN  # brief comment on relationship
producing_technique: M-NNN
opened: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
notes: >
  Optional elaboration, open questions, suggested next investigations.
```

## Hypothesis schema (YAML)

```yaml
id: "H-NNN"
question: "The research question, as a question."
motivation: >
  Why this question opened; what produced it.
candidate_law_statement: >
  Best current statement of what the answer might be.
type: [same type list as laws]
retrieval_queries:
  - "Query 1"
  - "Query 2"
adversarial_domain: >
  Best current counterexample; how it refines the hypothesis.
status: active | suspended | promoted | falsified
producing_technique: M-NNN
opened: "YYYY-MM-DD"
notes: >
  Open questions, suggested next investigations.
```

## The formalization pipeline

```
Notebook entry → Hypothesis YAML → Candidate law YAML → Established law
```

Hypotheses are promoted to laws when: multi-domain evidence exists, at least one adversarial test has been attempted, and the scope conditions are defined. Do not promote early — the hypothesis stage is where refinement happens.
