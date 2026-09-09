# Capability-Based Planning for AI Crisis Preparedness

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.18357
**Date read:** 2026-09-02
**Connected to:** L-001, seed-016
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper proposing a framework for AI risk preparedness that decouples planning from likelihood prediction, drawing on decision theory under deep uncertainty rather than traditional risk ranking. The argument is that predict-then-act governance fails for high-variance, low-predictability threat classes and suggests capability-based alternatives.

## What I took from it

The paper identifies a genuine failure mode in protocol design for governance under uncertainty: the **formalization of prediction as a legible input to decision protocols** (resonant with L-012, L-004). By ranking risks by likelihood and impact and allocating preparation resources accordingly, governance systems create a measurable proxy (predicted probability) for an unmeasurable phenomenon (AI timeline and failure mode distribution), which then becomes the optimization target rather than actual preparedness.

However, the paper is primarily a call for methodological reform in policy design, not an empirical or theoretical investigation of *how this substitution happens* or *what conditions make it stable*. It diagnoses the problem but does not furnish mechanisms explaining why predict-then-act frameworks persist despite known failure, or how capability-based planning itself might ossify under adoption pressure. The connection to L-001 (Protocol Ossification) is tagged but unexplored — the paper does not ask whether capability frameworks themselves become rigid once institutionalized.

## Research connections

- **L-001:** Tagged by triage; paper identifies predict-then-act as a brittle protocol but does not examine ossification dynamics under adoption.
- **L-004 (Goodhart Generalization):** Paper implicitly argues that likelihood-ranking is a Goodhart proxy for actual preparedness, but treats this as a design error rather than an invariant system property.
- **L-012 (Intervention-Layer Displacement):** The shift from prediction to capability framing is itself an intervention that relocates optimization pressure; paper does not examine what optimization targets emerge under the new regime.
- **seed-016:** Stopping-rule substitution in policy design — predict-then-act is a stopping rule that fails; paper proposes alternatives but does not examine what stopping rules the alternative embeds.

## Method note

This paper suggests that governance protocol critique should separate *diagnosis of failure modes* from *investigation of causal mechanisms*. Identifying that a protocol is brittle is necessary but not sufficient for research — the funnel needs empirical or formal work on *why* maladaptive protocols persist and *under what conditions* replacements stabilize. The meta observation: policy papers often function as problem statements rather than evidence accumulation. For this agenda, we should route such work toward mechanism-grounded inquiry (does it explain a persistent pattern across domains?) rather than treating methodological reform proposals as self-justifying.
