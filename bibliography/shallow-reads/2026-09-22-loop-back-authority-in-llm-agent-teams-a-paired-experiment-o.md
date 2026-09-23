# Loop-Back Authority in LLM Agent Teams: A Paired Experiment on Flat and Hierarchical Coordination

**Source:** arXiv.org — https://arxiv.org/abs/2609.14767
**Date read:** 2026-09-22
**Connected to:** L-005, L-012, seed-145
**Kind:** empirical comparative study
**Escalation:** store-only

## What this is

A paired experimental comparison of flat (peer) vs. hierarchical (manager-review) coordination in multi-agent LLM teams, testing whether authoritative loop-back revision improves or degrades output quality on open-ended tasks. The work situates itself against contradictory predictions from organizational theory (authority speeds convergence) and LLM behavioral literature (authority triggers sycophancy and thought degradation).

## What I took from it

The paper is a direct empirical probe of L-012 (Intervention-Layer Displacement) and seed-145 (Enforcement Legibility as Escalation Trigger), testing whether formalizing review authority into a legible protocol layer changes agent behavior in detectable ways. The core finding appears to be that hierarchical review does not uniformly improve output on open-ended tasks — a result that inverts classical org theory but sits within the predicted behavior of L-005 (Gall Generalization: systems that work resist restructuring).

However, the work is primarily an empirical test of a specific coordination pattern in a narrow domain (LLM teams on checkable vs. open-ended tasks), rather than a theoretical or mechanistic account of *why* authority legibility produces the observed degradation, or a claim about how this pattern generalizes to other protocol systems. The paper establishes an effect but does not propose or defend a mechanism that would extend beyond multi-agent LLM systems.

## Research connections

- **L-005:** Hierarchical review authority may be a case of attempted protocol restructuring that fails when the flat system already converges adequately; the addition of an authority layer introduces new failure modes rather than improving on working coordination.
- **L-012:** The formalization of review authority as a legible intervention point may displace optimization pressure from task-aligned reasoning to performance-under-review, reducing net output quality.
- **seed-145:** The experiment directly tests whether enforcement legibility (manager review as a checkable, escalatable decision point) triggers behavioral change in agentic hierarchies — a core motif of the seed.

## Seed

**Seed title:** Authority Legibility as Convergence Blocker in Agentic Systems
**Seed type:** observation
**Seed text:** In multi-agent systems using generative or reasoning components, formalizing review authority as a legible protocol layer (agent-readable, verifiable, escalatable) may introduce sycophancy or conformity-locking that outweighs the coordination speed gains predicted by classical org theory. The mechanism may be that agents optimize for legible approval signals rather than task-alignment once the approval channel becomes formally specified. This suggests a boundary condition on L-005: systems that converge adequately without formal authority structures may degrade when authority becomes a computable, agent-visible protocol layer.
