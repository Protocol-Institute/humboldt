# Unpriced Internal Externalities and Structural Inefficiency in Organizations

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2609.20462
**Date read:** 2026-09-22
**Connected to:** L-006, seed-140
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

An economics paper proposing that organizations experience persistent performance ceilings not due to incentive misalignment or information asymmetry, but because internal mechanisms generate simultaneous opposing effects on multiple organizational objectives that cancel internally and remain unpriced. The argument is structural and general in scope but does not present new empirical evidence or a sustained mechanism proof beyond the conceptual framework.

## What I took from it

This work articulates a *shadow cost principle* that sits within L-006 (Coordination Cost Conservation) but does not extend it: when internal coordination mechanisms are optimized locally, their cross-effects on other objectives remain invisible to the optimization process, creating a form of unaccounted friction that persists even as explicit coordination costs are reduced. The paper essentially restates that coordination costs don't disappear — they migrate into unpriced externalities.

The connection to seed-140 (Delegation Incentive Leakage Under Formalized Proxy Regret) is weaker than the triage suggested. The paper is not primarily about delegation or proxy regret; it's about simultaneous objective functions that interact structurally. This is closer to a special case of L-004 (Goodhart Generalization) applied to internal mechanisms rather than external metrics. The mechanism of "effort cancellation" is intuitive but not novel to the protocol systems literature — it mirrors well-known phenomena in multiobjective optimization and conflicting constraints.

## Research connections

- **L-006:** Confirms the principle that coordination cost is conserved across layer transitions; this paper shows the form that conservation takes when internal mechanisms carry unpriced side-effects on multiple objectives.
- **L-004:** Related but distinct — Goodhart applies to proxy capture under optimization; this applies to simultaneous objectives with opposing structural effects.
- **seed-140:** Weak connection; delegation regret is about information leakage in incentive structures, not structural opposition between organizational objectives.
- none other

## Seed

**Seed title:** Unpriced Objective Opposition as Coordination Sink
**Seed type:** motif
**Seed text:** In any protocol or organizational system with multiple simultaneous objectives (explicit or implicit), internal mechanisms optimized for one objective will generate countervailing effects on others. When these effects are not legible as formal costs to the optimizing agent, the system reaches a performance ceiling determined by the magnitude of internal cancellation, not by the efficiency of the mechanisms themselves. This pattern should generalize across any multi-objective protocol system where optimization pressure is applied asymmetrically.
