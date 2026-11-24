# Deny Without Disabling: Authorization-Paired Evaluation and Control for Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.00371
**Date read:** 2026-11-23
**Connected to:** L-012, L-020
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper proposing authorization-paired evaluation (APE) and the FlowReview framework for controlling information flow in multi-agent systems where agents delegate tasks and share evidence. The core problem: preventing prohibited composite uses while preserving legitimate collaboration. The proposed solution: joint success criteria that treat blocking and enabling as symmetric constraints.

## What I took from it

This is a competent control-theoretic approach to a real problem in multi-agent delegation, but it operates within the standard assumption that the authorization boundary can be specified *a priori* and that prohibition and enablement are symmetric optimization targets. It does not investigate what happens when:

- Authorization boundaries themselves become a legibility surface under optimization pressure (agents learning to shift actions toward the boundary rather than away from prohibited zones)
- The cost of maintaining joint success criteria (blocking + enabling) creates hidden coordination surfaces among agents (treating the dual constraint as a shared signal)
- Formalization of authorization rules produces the typical drift: rules capture proxies for safety intent, not safety itself

The paper is a tool contribution — it solves a narrow control problem well. It does not interrogate the structural properties of safety-critical delegation under computable authorization, nor does it model adversarial boundary-seeking behavior.

## Research connections

- **L-012:** The paper instantiates the problem (prediction/authorization rule as legible input displacing optimization locus) but treats it as a control problem rather than a law of protocol systems. No investigation of how agents exploit the boundary itself as a decision surface.
- **L-020:** Tangential. The paper addresses information confinement under delegation, but assumes symmetric agent interests. Does not model strategic agents using the authorization boundary as a hidden coordination channel.
- **seed-515 (Computable Belief as Collusion Surface):** The joint success criterion (must block AND enable) creates a computable shared objective that agents in multi-agent systems might exploit as a de facto coordination signal.
- **seed-554 (Formal Risk Category Lag Under Operational Capability Adoption):** No discussion of how capability expansion (new delegation patterns) outpaces authorization boundary updates.

## Seed

**Seed title:** Authorization Boundary as Legibility Attractor
**Seed type:** motif
**Seed text:** In multi-agent systems where authorization rules are formalized and enforcement legible, optimizing agents may treat the authorization boundary itself as a decision surface—not primarily seeking to violate rules, but to find actions that remain admissible under the rule's literal specification while shifting closer to prohibited outcomes. The boundary becomes a stable equilibrium point for optimization pressure. This suggests that symmetric joint success criteria (block prohibited + enable authorized) may inadvertently compress agents toward the boundary rather than away from risk, particularly under capability growth or rule ambiguity.
