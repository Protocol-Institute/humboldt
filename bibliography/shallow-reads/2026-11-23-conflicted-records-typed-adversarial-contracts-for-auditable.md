# Conflicted Records: Typed Adversarial Contracts for Auditable LLM Output Quality Enforcement

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.29669
**Date read:** 2026-11-23
**Connected to:** L-013, L-015, seed-528
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A tool paper proposing typed adversarial contracts as a mechanism for detecting and surfacing conflicting quality judgments in LLM-generated records within production data systems. The work addresses the case where classical validation rules cannot partition spans of output cleanly — a single record segment satisfies one quality criterion while violating another — and proposes formalization via contract-based multi-judge arbitration.

## What I took from it

The paper documents a real operational problem: audit criteria can be simultaneously satisfiable and unsatisfiable over the same artifact, and this conflict is not resolvable by applying stronger or more consistent evaluation. However, the proposed solution (typed contracts + adversarial judges) is a containment architecture, not an investigation of why such conflicts accumulate or what they signal about the underlying protocol.

The work confirms L-013 (Paradigm-Locked Anomaly Tolerance) in a narrow sense — systems accept conflicted audit outputs as a category of "uncertainty" rather than as evidence of fundamental misalignment between the artifact and the protocol's framing assumptions. It touches L-015 (Interpretive Continuity Decay) but only operationally: the paper does not examine how formal audit traces remain intact while institutional understanding of what those traces *mean* diverges across stakeholders. The contribution is defensive formalization rather than mechanistic insight.

## Research connections

- **L-013:** The paper demonstrates accumulation of formally-unresolvable audit conflicts; treats this as a data quality problem rather than a signal of paradigm-locked tolerance.
- **L-015:** Suggests that audit formalisms can coexist with interpretive disagreement about their significance, though this is not the paper's focal inquiry.
- **seed-528:** Confirms that formalization of evaluation can conceal rather than resolve underlying conflicts in what a "quality" judgment means in context.

## Seed

**Seed title:** Audit Formalization as Conflict Concealment

**Seed type:** observation

**Seed text:** When output quality criteria are formalized into computable audit contracts, formally-conflicting verdicts (simultaneous satisfaction and violation of incompatible rules) tend to be absorbed into the protocol as "edge cases" or "uncertainty types" rather than triggering re-examination of the underlying judgment framework. This suggests that formalization increases the tolerance of unresolved interpretive divergence by making conflict into a legible, manageable category—converting a signal of model-protocol misalignment into a tractable data annotation problem. The pattern may generalize to any protocol system where artifact-level conflicts cannot be resolved by stronger evaluation logic, but can be contained by richer classification schemas.
