# How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.02557
**Date read:** 2026-11-23
**Connected to:** L-004, L-015, seed-157
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

This is a game-theoretic formalization of AI debate as an oversight protocol, extending prior work (Irving et al.) by deriving instance-optimal complexity bounds for debate trees under different judging assumptions. The paper treats debate decomposition as a computational complexity problem: how deep must a debate tree be to reduce an n-bit claim to 1-bit judgeable claims?

## What I took from it

The paper strengthens the case that debate, when formalized as a protocol, becomes a *legibility surface* rather than a truth-finding mechanism. The instance-optimality framework reveals a critical structural property: the depth of debate required depends not on the actual difficulty of the underlying question, but on the *computational expressiveness required to formalize the disagreement into a judeable frame*. This is a direct instantiation of L-004 (Goodhart Generalization) — the debate protocol optimizes for decomposability-into-legible-claims, not for truth recovery. 

The connection to L-015 (Interpretive Continuity Decay) is sharper than initially tagged: as debate formalizes the structure of disagreement into a tree of micro-claims, the institutional memory that debate is *meant to surface truth* decays relative to the protocol's new functional purpose — producing an auditable record of *formally resolved* sub-questions. The judges inherit not a truth but a proof of formal agreement-down-the-tree. This is distinct from the disagreement that existed before formalization.

## Research connections

- **L-004:** Debate as formalized protocol optimizes for claim-legibility and judge-decidability, not truth; the metric (formal decomposability) becomes the target, pulling the system away from the original goal (accurate oversight).
- **L-015:** As debate rules and tree structure formalize, the original interpretation ("this resolves a factual question") can persist in formal records while institutional practice treats it as "this is a formally settled disagreement," creating interpretive discontinuity.
- **seed-157:** The paper does not appear to address how debate structure changes when judges themselves are AI systems or when the claims being debated concern AI behavior — a critical gap for oversight protocols applied to their own operands.
- **L-012:** Debate structure could displace the locus of optimization from "which claim is true" to "which decomposition wins," favoring rhetoric that fits the tree shape.

## Seed

**Seed title:** Debate Legibility as Orthogonal to Adjudication Accuracy
**Seed type:** observation
**Seed text:** When debate is formalized as a protocol with instance-optimal decomposition rules, the system optimizes for the depth and structure of formally resolvable sub-questions, not for the accuracy of the final judgment. Under sufficient formalization pressure, debate protocols converge on decompositions that maximize legibility to judges (human or machine) rather than decompositions that reveal ground truth. This suggests debate depth correlates with formalizability-of-disagreement, not with question difficulty or truth proximity — a generalization worth testing across other hierarchical judgment protocols (hierarchical reinforcement learning, recursive auditing, multi-stage approval chains).
