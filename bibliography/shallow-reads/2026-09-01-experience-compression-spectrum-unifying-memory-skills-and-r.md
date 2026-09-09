# Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2604.15877
**Date read:** 2026-09-01
**Connected to:** L-003, seed-016
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A unification framework positioning memory abstraction, skill discovery, and rule extraction as points on a single compression spectrum in LLM agent systems. The work surveys citation networks across memory and skill literatures (1,136 references, <1% cross-citation) and proposes a continuous model where agents trade off fidelity, reusability, and computational cost along a single axis.

## What I took from it

This is a competent meta-analysis identifying genuine technical fragmentation in the LLM agent literature. The compression-spectrum framing is sensible: memory (high fidelity, low reusability), skills (intermediate), and rules (low fidelity, high reusability) do occupy different points in an abstraction-efficiency trade space. 

However, the work describes a **within-domain optimization trade-off**, not a mechanism of protocol transformation under pressure. The fragmentation it documents (disparate communities, low cross-citation) is real, but the paper treats this as a coordination failure amenable to taxonomy, not as evidence of something deeper. The scaling pressure that motivates the framework (long-horizon deployments, bottlenecked memory) is mentioned but not analyzed as a driver of *which abstraction form gets locked in*. This sits adjacent to L-003 (Formalization Ratchet) but does not itself investigate whether compression-spectrum position freezes under adoption or deployment pressure. The paper is a design contribution and a literature review, not a primary investigation of protocol rigidity or transformation dynamics.

## Research connections

- **L-003:** The scaling pressure on agent systems should produce formalization ratcheting (from memory → skills → rules), but the paper does not track whether adopted abstraction levels become sticky or resistant to change.
- **seed-016:** No direct engagement with stopping-rule substitution or what happens when the choice of memory/skill/rule balance becomes a frozen design decision.

## Seed

**Seed title:** none
