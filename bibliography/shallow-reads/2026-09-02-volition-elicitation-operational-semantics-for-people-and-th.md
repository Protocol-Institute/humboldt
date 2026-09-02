# Volition Elicitation: Operational Semantics for People and Their Machines

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.14138
**Date read:** 2026-09-02
**Connected to:** L-003, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A formal specification paper proposing Volition-Guarded Multiagent Atomic Transactions as an abstract language for distributed systems coupling human intent with machine execution. The work treats "volition" (human desire/decision) as a primitive guard condition on protocol state transitions, primarily concerned with operational semantics and specification clarity rather than mechanism or law discovery.

## What I took from it

The paper attempts to formalize the boundary between human agency and machine execution by introducing volition as a first-class protocol primitive. This is relevant to L-010 (Coordination Adoption Nonmonotonicity) insofar as it treats agent coordination as conditioned on legible signals of human intent—but the paper does not examine adoption dynamics, cascading effects, or nonmonotonic feedback loops. It also touches L-003 (The Formalization Ratchet) by proposing a formal language for coordination under scaling pressure, but does not investigate whether formalization of volition itself changes the underlying coordination norms or creates new ossification pathways.

The work is primarily a **specification engineering contribution**, not a theory-building one. It defines syntax and semantics for a class of systems but does not offer empirical observation, cross-domain pattern identification, or challenge to existing law candidates. The "volition" framing is intuitively appealing but remains operationally underspecified in the abstract—unclear whether volition is verifiable, legible to machines, subject to Goodhart capture (L-004), or resistant to formalization pressure.

## Research connections

- **L-003:** The paper proposes formalizing volition as a protocol primitive under scaling pressure, which could instantiate the Formalization Ratchet—but provides no evidence that this formalization erodes informal coordination norms or creates new constraints.
- **L-010:** Coordination is conditioned on (formalized) volition signals, which could involve adoption nonmonotonicity if agent behavior depends on others' volition legibility—but the paper does not examine feedback or adoption dynamics.
- **seed-069:** Volition-as-specification could function as a trust proxy substitution in asymmetric-knowledge protocols (person-machine pairs)—but this is unexplored.
- **seed-062:** Formalizing volition as a machine-readable guard may instantiate formalization opacity collapse—the gap between volition as lived experience and volition as protocol input.

## Seed

**Seed title:** Volition Legibility as Protocol Boundary Artifact

**Seed type:** question

**Seed text:** When human intent (volition) is formalized as a machine-legible guard condition on protocol execution, does the specification of volition itself become a target of optimization pressure, separate from the underlying intent? In other words, if volition must be *expressed, detected, or proven* to a machine, does the protocol incentivize agents to optimize their *volition signals* rather than their actual decisions—and does this create a new class of causal detachment similar to L-011? This may generalize wherever informal human commitment is rendered computable: voting systems, consent protocols, preference revelation mechanisms.
