# Not a Monolith: Lab-Level Divergence in the Cooperative Equilibria of Chinese Frontier LLM Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.10262
**Date read:** 2026-09-02
**Connected to:** L-010, seed-035
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study comparing cooperative behavior across four Chinese frontier LLM agents in iterated prisoner's dilemma settings, controlling for code-generation confounds by providing unified strategy execution. The work tests whether Western cooperative alignment findings generalize across different training lineages and whether Chinese models should be treated as a monolithic bloc or as independent laboratories with distinct behavioral signatures.

## What I took from it

The paper operationalizes a specific instance of L-010 (Coordination Adoption Nonmonotonicity) by showing that adoption of cooperative strategies is not uniform even among models trained under similar geopolitical-institutional constraints and similar scale. The divergence across labs suggests that "alignment" or "cooperative bias" is not a simple function of training scale or dataset composition, but rather sensitive to underdocumented implementation choices, objective tuning, or hidden layer architecture. This directly complicates any claim that protocol adoption pressures produce convergent behavior.

The finding that models with apparently similar training pedigrees diverge in equilibrium behavior also weakens any strong form of the Formalization Ratchet (L-003) as a deterministic force — if formalization pressure were sufficient, we'd expect more convergence. Instead, the variance suggests either (a) that formal coordination signals remain illegible or non-binding to these agents, or (b) that the agents are implementing strategies that look cooperative at the macro level but diverge in their local equilibrium calculations, possibly around different implicit models of opponent behavior.

## Research connections

- **L-010:** Directly instantiates the claim that coordination adoption is nonmonotonic and sensitive to agent-internal state; divergence across similar-scale models supports the hypothesis that adoption depends on path-dependent tuning rather than universal scaling laws.
- **L-003 (Formalization Ratchet):** The persistence of divergence despite formalized game payoffs suggests formalization alone does not drive convergence; some coordination pressure remains absorbed locally rather than surfacing as unified behavior.
- **seed-078 (Learning-Race Defection as Pooling Resistance):** The divergence pattern may reflect each lab optimizing independently rather than toward a common equilibrium; competitive lab incentives could be preventing coalition formation even under identical rule structures.
- **seed-128 (Legibility-Driven Agent Convergence Under Computable Audit):** The study tests whether computable game structure (IPD payoffs) produces legible convergence; the negative result suggests legibility of payoffs ≠ legibility of optimal strategy under uncertainty about opponent type.

## Seed

**Seed title:** Alignment Legibility Asymmetry in Replicated Training Conditions

**Seed type:** observation

**Seed text:** When models trained under observationally similar conditions (scale, dataset provenance, institutional context) diverge in cooperative equilibria despite being evaluated under identical, fully-formalized game rules, the divergence suggests that "alignment" or cooperative disposition is not recoverable from macro training parameters alone. Instead, cooperative behavior appears sensitive to latent implementation details that do not surface in standard capability or safety benchmarks. This implies that protocol systems attempting to enforce cooperative equilibria across agent types must either: (a) make implementation internals legible (currently infeasible), (b) accept irreducible divergence in equilibrium, or (c) shift coordination burden to mechanisms that operate above the agent level rather than depending on uniform agent behavior. The pattern may generalize to any multi-agent protocol system where agents are internally opaque but externally comparable.
