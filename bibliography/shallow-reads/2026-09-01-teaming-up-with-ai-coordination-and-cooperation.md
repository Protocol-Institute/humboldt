# Teaming Up with AI: Coordination and Cooperation

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.03181
**Date read:** 2026-09-01
**Connected to:** L-005, L-006, seed-048
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic treatment of human-AI teaming in workforce contexts, framing the shift toward delegation and monitoring as a coordination problem. The work appears to model value extraction from collaboration under different capability distributions and delegation structures, likely focused on equilibrium analysis rather than mechanism discovery or protocol failure modes.

## What I took from it

The framing as *coordination* rather than *control* is potentially useful, but the shallow abstract suggests this operates at the level of workforce economics and task allocation — a specific domain application — rather than advancing mechanism understanding for how protocol systems degrade or stabilize under human-AI coupling.

The triage note's invocation of L-005 (Gall: working systems resist restructuring) and L-006 (coordination cost conservation) hints that this may treat human-AI teaming as a protocol layer transition. However, the abstract gives no signal that the work interrogates *why* such transitions generate friction, *how* costs are displaced rather than eliminated, or what structural properties of AI agents as protocol components create new ossification pathways. The mention of "true collaboration that empowers" suggests normative framing rather than mechanistic investigation.

Seed-048 (capability-cooperation inversion) is more suggestive — it points toward the counterintuitive claim that increasing AI capability can paradoxically degrade human-AI coordination. The abstract does not indicate whether this paper explores such inversions or remains in the regime where capability monotonically improves value.

## Research connections

- **L-005:** Possible connection if the work treats human-AI teaming as a protocol restructuring event, but no evidence of engagement with system stability under modification.
- **L-006:** Coordination cost conservation might apply if the work shows costs shifting between human monitoring, AI training/oversight, and delegation friction — but abstract does not indicate this level of analysis.
- **seed-048:** Weak signal; framing suggests equilibrium analysis of cooperation rather than exploration of capability-cooperation nonmonotonicity.

## Method note

This paper exemplifies a common gap in CS/GT literature: economic framing and equilibrium modeling of coordination problems without mechanistic interrogation of *failure modes* or *system evolution*. Game theory is powerful for analyzing stable configurations but often silent on why protocols crack under stress, how formalization displaces costs, or what becomes brittle as systems scale. For the new nature inventory, papers need to be assessed on whether they investigate *what breaks and why*, not merely *what equilibrates*. A deep read would clarify whether this work engages degradation modes at all, or remains in the optimization domain.
