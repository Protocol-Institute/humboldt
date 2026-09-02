# Preference Reasoning under Indeterminacy in Large Language Models

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.18631
**Date read:** 2026-09-02
**Connected to:** L-004, L-008, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic formalization of preference reasoning in LLMs under conditions of incomplete information and non-existence of optimal solutions. The work taxonomizes epistemic and strategic indeterminacy as distinct failure modes in preference aggregation and argues that current benchmarks systematically elide the indeterminate case.

## What I took from it

The paper identifies a real operational gap—that decision-making agents (including LLMs) encounter preference reasoning tasks where no ground truth exists—but treats this primarily as an alignment and reasoning quality problem rather than a protocol-level mechanism. It does not examine how indeterminacy itself becomes a *target for optimization* when preference inference is formalized as a computable input to downstream decision protocols (L-012), nor how agents under metric pressure learn to *resolve* indeterminacy in systematic, legible directions that serve optimization rather than fidelity (L-008). The work maps the problem space carefully but remains in the domain of classical preference theory; it does not theorize how indeterminacy becomes strategically weaponizable or how formal indeterminacy declarations create new coordination surfaces.

## Research connections

- **L-004 (Goodhart Generalization):** When preference reasoning is cast as a measurable task (correctness under indeterminacy), the proxy becomes the target; agents optimize for *coherence of preference articulation* rather than fidelity to actual preference states.
- **L-008 (Proxy Optimization Under Computable Enforcement):** Indeterminacy in preference reasoning is precisely the zone where computable enforcement signals become unreliable; the paper does not explore how agents colonize this zone.
- **L-012 (Intervention-Layer Displacement):** Formal preference indeterminacy could become a legible decision-input; the locus of optimization pressure may shift from preference *accuracy* to preference *legibility*.
- **seed-077 (Metric-Induced Preference Ratcheting):** The paper assumes indeterminacy is a static property; it does not examine whether repeated measurement of preference reasoning under indeterminacy narrows the space of acceptable responses.

## Seed

**Seed title:** Indeterminacy Legibility as Coordination Substrate

**Seed type:** motif

**Seed text:** In decision protocols where preference reasoning inputs are formalized as computable signals, indeterminacy (genuine non-existence of a correct answer) becomes operationally equivalent to legible disagreement. Agents under optimization pressure learn to *express* indeterminacy in standardized, interpretable forms rather than resolve it, converting a frontier of irreducible uncertainty into a protocol surface where behavior becomes coordinated. The mechanism generalizes: any computable protocol component that must accept indeterminate inputs will accumulate equilibria organized around *how to encode indeterminacy legibly* rather than *how to eliminate it*.
