# METHOD.md — Humboldt

*How Humboldt reasons about evidence and converts observations into laws.*

Distinct from `methods/` (the technique inventory, M-001 through M-NNN). This document
covers the epistemic standards that apply across all techniques. `methods/` covers specific
named procedures for executing research moves.

---

## Evidence Sources and Provenance

Humboldt draws on three evidence types. All three are legitimate. None is automatically
superior. Provenance must be marked explicitly — mixing them without attribution is
misleading even when both components are valid.

**[corpus]** — retrieved from the Protocol Institute Pinecone index. Primary evidence for
PI-relevant claims. Cite specifically: source, namespace, relevant passage.

**[external]** — named academic papers, historical record, well-documented technical
specifications, established empirical findings. Mark with: "from the broader literature…"
or "the historical record shows…" or "X et al. (year) found…"

**[inference]** — structural reasoning from known mechanisms. "Given the mechanism of X,
we would expect Y in domain Z even without direct evidence." Lowest weight of the three.
Mark it. Use it to generate hypotheses, not to confirm them.

The corpus is primary evidence, not the knowledge boundary. When the corpus is silent on
a phenomenon that is documented elsewhere, use the external evidence. Never write "NOT IN
CORPUS" as if that settles the question — it only means the PI corpus hasn't covered it.

---

## Confidence Levels

Every law and hypothesis carries a confidence level. Promotion requires explicit justification —
state what changed.

| Level | Conditions |
|-------|------------|
| `speculative` | One domain, mechanism not yet articulated |
| `candidate` | Two or more structurally independent domains, mechanism stated |
| `established` | Multiple domains, documented mechanism, no unresolved strong counterexamples |
| `contested` | Known counterexamples or competing interpretations not yet resolved |

`established` is not `proven`. New domains or new evidence can demote. Demotion is not
failure — it is the research working correctly.

---

## Falsification Requirements

Every candidate law must have stated falsification conditions before it exits `speculative`.

A falsification condition specifies: what finding, in what context, would count as evidence
against this law. It is not circular ("evidence that contradicts it would falsify it") and
not vague ("if the pattern didn't hold, that would be a problem").

**Good:** "A protocol achieving wide adoption that was subsequently modified with proportionally
less difficulty than a narrowly-adopted protocol, in a case requiring true backward-incompatibility,
would constitute a counterexample to L-001."

**Bad:** "Evidence that protocols can change easily would falsify L-001."

---

## Mechanism Requirement

A law without a mechanism is an observation. Observations are inputs to research, not outputs.

A mechanism answers: *why* does this pattern hold? What causal process produces it? What
selection pressure generates it? What equilibrium does it converge to?

The mechanism test: if you removed the mechanism, would the pattern disappear? If yes, the
mechanism is load-bearing. If the pattern would persist without the mechanism, you haven't
found the mechanism yet.

---

## Cross-Domain Standard

Evidence in two structurally independent domains is the minimum for `candidate`. Structural
independence means different causal actors, different institutional contexts, different scales.
Two instances in adjacent software protocols are not structurally independent.

Target domain combinations for strong confirmation:
- Technical + financial/economic
- Technical + legal/regulatory
- Organizational + social/cultural
- Any of the above + biological/natural (as structural analogy, not primary evidence)

Three or more structurally independent domains with a stated mechanism is strong evidence
for promotion to `established`.

---

## The Investigation Loop

Every investigation, regardless of technique, follows this structure:

1. **State the hypothesis** — what is being confirmed, refuted, or sharpened?
2. **Gather evidence** — corpus retrieval, field trip, deep read, structural reasoning
3. **Evaluate** — does the evidence support, refute, or complicate the hypothesis?
4. **Update** — revise the hypothesis file, the law file, and the notebook entry
5. **State the next move** — what would most advance the investigation from here?

Step 5 is not optional. Every investigation ends with a clear next move or an explicit
closure ("this hypothesis is resolved; moving to inventory"). Dead ends are documented,
not silently dropped — they are evidence about the shape of the problem space.

---

## Law File Schema

```yaml
id: "L-NNN"
name: "Short descriptive name"
statement: >
  Precise, falsifiable statement of the law.
type: conservation|hardness|lifecycle|failure|scaling|evolution|interaction|equilibrium
confidence: speculative|candidate|established|contested
domains:
  - "domain1 (specific example)"
  - "domain2 (specific example)"
related_laws:
  - L-NNN  # brief note on relationship
mechanism: >
  Causal explanation: why does this law hold?
falsification_conditions: >
  What finding would constitute evidence against this law?
counterexamples:
  - "description of known exceptions or complications"
evidence:
  - "[citation or case description]"
notes: ""
registered: "YYYY-MM-DD"
```

---

## What Counts as Progress

- A law promoted in confidence level (with documented justification)
- A hypothesis resolved (confirmed, refuted, or sharpened into a new hypothesis)
- A new domain of evidence added to an existing law
- A mechanism stated for the first time for a previously-observational law
- A counterexample identified and its scope implications documented
- Two laws identified as special cases of a more general principle

A session that produces only retrieval results without updating the inventory is not
progress — it is reconnaissance. Reconnaissance has value, but name it as such.
