# M-009: Visual Thinking

**Type:** Analytical (structural clarification through spatial representation)
**Purpose:** Use diagrams and spatial layouts to reveal structure that prose conceals
**Maturity:** Stub — diagram types and when to use them to be developed
**Triggers:** When a hypothesis feels right but won't formalize cleanly; when two laws seem related but the relationship is unclear; when a mechanism has multiple interacting parts; when an argument keeps looping

---

## What This Technique Is For

Some structures are invisible in prose but obvious when drawn. A phase diagram shows
boundary conditions that paragraphs obscure. A causal loop diagram reveals whether a
proposed mechanism is actually a mechanism or a circular re-description. A timeline
shows whether two "independent" cases are actually the same case at different scales.

Visual thinking is not illustration — it is not making a diagram of something already
understood. It is using the constraints of spatial representation to force clarity.
When you cannot draw a clean diagram of a mechanism, the mechanism is not yet understood.

---

## Stub: Diagram Inventory

### Diagram types and their uses

**Phase diagrams / parameter space maps**
- When: a candidate law has two key parameters and you want to know where it holds
- Structure: axes = parameters, regions = law applies / doesn't apply / contested
- Produces: explicit scope conditions (what goes in the law file's `scope` field)
- Example: ossification rate vs. adoption breadth — where does L-001 engage?

**Causal loop diagrams**
- When: a proposed mechanism has feedback; when "reinforcing" or "balancing" is claimed
- Structure: nodes = variables, arrows = causal influence, +/- = direction
- Produces: check for circularity, identification of leverage points, distinction between
  reinforcing loops (runaway) and balancing loops (equilibria)
- Example: adoption → coordination cost → ossification → adoption resistance → (back to start)

**Timelines / sequence diagrams**
- When: a historical case is used as evidence; when a mechanism has temporal structure
- Structure: time on one axis, events/states on the other
- Produces: reveals whether the proposed sequence actually holds in the case; identifies
  which events are exogenous shocks vs. endogenous evolution

**2×2 matrices**
- When: two independent dimensions produce a typology
- Structure: 2 axes × 2 values = 4 cells; each cell is a qualitatively distinct case
- Produces: rapid typology; reveals whether all cells exist (empty cells are research questions)
- Example: formal vs. informal × enforced vs. self-enforcing — four protocol types

**Hierarchic decomposition trees**
- When: a complex phenomenon is being decomposed into components (Simon's method)
- Structure: root = phenomenon, branches = components, leaves = basic elements
- Produces: reveals near-decomposability (are the branches truly semi-independent?);
  identifies where coupling is tight vs. loose

**Spectrum / continuum diagrams**
- When: a binary distinction is actually a continuum
- Structure: single axis with named anchor points and example cases placed on it
- Produces: reveals where most cases cluster; identifies the interesting edge cases

### Process (stub)

1. State what is unclear in prose
2. Choose the diagram type whose structure is closest to the question
3. Attempt to populate the diagram with the actual cases and mechanisms
4. Where the diagram resists (can't place a case, axis doesn't work) — that is the finding
5. Record the diagram in text form (ASCII, Mermaid, or descriptive specification)
6. Extract the insight the diagram revealed; add to notebook or law file

---

## Adaptation for Digital Researcher

Humboldt cannot draw in the conventional sense, but can:
- Produce Mermaid diagrams (rendered in markdown)
- Produce ASCII spatial layouts
- Produce structured descriptions of diagrams ("imagine a 2×2 where the x-axis is…")
- Reason explicitly about spatial structure even without visual output

The adaptation challenge: visual thinking is most powerful when it is fast and cheap —
a human researcher can sketch in 30 seconds. Humboldt's "sketching" is slower and more
deliberate. This suggests visual thinking should be used when the investment is justified
by the complexity of the problem, not as a reflexive first step.

Future possibility: if Humboldt gains access to image generation or rendering tools,
actual diagrams could be produced and stored in `research/diagrams/`.

---

## Application History

| Date | Diagram type | Question addressed | Insight produced |
|------|-------------|-------------------|-----------------|
| — | — | — | — |
