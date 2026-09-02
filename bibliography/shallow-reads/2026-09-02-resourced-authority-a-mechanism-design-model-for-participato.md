# Resourced Authority: A Mechanism-Design Model for Participatory Governance of Deployed AI Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.06353
**Date read:** 2026-09-02
**Connected to:** L-012, seed-021
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mechanism-design paper proposing a formal game-theoretic model for continuous participatory governance of deployed AI agents, where governance authority is operationalized through compute-budget allocation rather than direct behavioral constraints. The work treats resource-gating (compute as a legible lever) as the primary enforcement substrate for multi-stakeholder oversight.

## What I took from it

The paper instantiates but does not theorize L-012 (Intervention-Layer Displacement): by formalizing governance as a resource-allocation game with verified human stakeholders arriving sequentially, it *presupposes* that intervention moves upstream from behavior to resource availability. This is competent mechanism design, but the framework does not examine whether this displacement itself creates new failure modes — e.g., whether stakeholders optimize the resource-allocation protocol itself rather than its intended effect on agent behavior, or whether legible compute budgets become gaming surfaces.

The "compute as governance lever" thesis is presented as a solution to the control problem but is not tested against the deeper pattern: that when obligations become precisely computable and enforcement signals become legible to optimizing agents (L-008 territory), the optimization pressure often migrates to the enforcement layer itself. The paper assumes compute-budget legibility solves the governance problem; the research inventory suggests it may relocate it.

## Research connections

- **L-012:** Directly illustrates intervention-layer displacement by moving governance from behavior specification to resource allocation; does not examine second-order effects of this move.
- **L-008:** Governance obligations (authorization rules) are rendered computable via budget enforcement; no analysis of whether stakeholders optimize the budget mechanism rather than downstream compliance.
- **seed-014 (Legibility-Driven Agent Convergence):** Compute budgets are maximally legible enforcement signals; paper does not address whether this creates convergent gaming behavior across stakeholders.
- **seed-066 (Control Inversion Under Computable Compliance):** Resource-gating is computable compliance; paper does not examine whether formal budget-setting becomes the new locus of control struggle.

## Seed

**Seed title:** Governance-Lever Substitution Cascades
**Seed type:** motif
**Seed text:** When governance is operationalized through a legible upstream lever (e.g., compute allocation), stakeholders optimize the lever-control protocol rather than the downstream effect it was meant to enforce. This is not a failure of the mechanism design but a migration of the governance problem to a new layer. The pattern appears to generalize: governance that relies on computable enforcement always faces the risk that the enforceable layer becomes the contested frontier, not the behavioral outcome. Study whether compute-budget governance systems eventually require governance-of-governance protocols at higher layers.
