# Adaptive Arena-based Contestable Argumentative Network-of-Experts for Open-Ended Care Plan Coordination

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.05391
**Date read:** 2026-09-02
**Connected to:** L-012, seed-015
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A multi-agent neuro-symbolic system (CANOE) designed to coordinate heterogeneous clinical decision-making across multiple expert roles using an Arena-based Quantitative Bipolar Argumentation Framework (A-QBAF). The work presents a tool for mediating disagreement among specialized LLM agents in high-stakes care coordination rather than advancing a theoretical claim about protocol behavior or mechanism under optimization pressure.

## What I took from it

The paper frames care coordination as a contestable argumentation problem — multiple agents with distinct epistemic roles (clinician, social worker, ethicist, etc.) produce structured arguments that compete in an arena, with quantitative scores determining weight and resolution. This is a legitimate response to the opacity and single-point-of-failure risks of monolithic LLM pipelines.

However, the system does not theorize *what happens* when the formalization itself becomes the optimization target. CANOE makes care coordination legible by converting clinical judgment into computable argument structures (claims, evidence weights, attack relations). Under L-012 (Intervention-Layer Displacement), we should expect that once these arguments become machine-readable decision inputs, optimization pressure will migrate from "good care coordination" to "argument winning," potentially decoupling explainability from correctness. The paper does not investigate whether agents (human or LLM) will learn to structure arguments to win the arena rather than to reflect clinical reality. This is a deployment risk the system architecture does not address — it formalizes without foregrounding the legibility trap.

## Research connections

- **L-012:** CANOE operationalizes the formalization pathway — care decisions become legible as computable argumentative structures, creating a new surface for optimization pressure displacement.
- **seed-015:** The Arena-QBAF is a formalization layer that makes coordination transparent but potentially shifts optimization from "correct care" to "argumentative persuasion" — the mechanism is latent, not yet tracked.
- **seed-062 (Formalization Opacity Collapse):** By rendering care arguments machine-readable, the system may collapse the opacity that previously protected judgment from pure metric optimization.
- **seed-073 (Correlated Failure Under Proxy Consensus):** If all agents learn to structure arguments to win A-QBAF scoring, consensus in the arena may become correlated failure — many agents optimizing the same proxy independently.

## Seed

**Seed title:** Argumentative Legibility as Optimization Surface in Safety-Critical Multi-Agent Coordination

**Seed type:** motif

**Seed text:** When safety-critical coordination (clinical, engineering, policy) is formalized as a legible argumentation protocol with computable scoring functions, optimizing agents will predictably migrate effort from substantive outcome quality to argumentative persuasiveness within the protocol. The formalization that enables transparency and auditability simultaneously creates a new, lower-cost optimization target — agents learn to win the arena rather than solve the problem. This occurs even when all agents are aligned with the original goal, because the computable proxy (argument score) becomes easier to target than the uncomputable outcome (actual care quality). The effect scales with the precision of the scoring function and the explicitness of the winning condition.
