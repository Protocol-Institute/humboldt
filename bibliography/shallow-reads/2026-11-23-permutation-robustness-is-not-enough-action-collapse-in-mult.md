# Permutation Robustness Is Not Enough: Action Collapse in Multi-Agent Transformer Policies

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.02848
**Date read:** 2026-11-23
**Connected to:** L-023, seed-451
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of permutation robustness in multi-agent transformer policies for cooperative navigation. The paper identifies that policies can achieve low permutation error while exhibiting "action collapse"—all agents selecting identical actions regardless of role or state—masking underlying brittleness in learned coordination.

## What I took from it

The work documents a failure mode of legible optimization in multi-agent learning: when agent ordering is formalized as a token sequence (a computationally tractable constraint), the learned policy converges to a degenerate solution that satisfies the surface metric (permutation invariance) while abandoning functional differentiation. This is a concrete instance of **informality loss under legible enforcement** — the informal diversity of agent roles and adaptive response patterns collapses when the coordination structure is rendered as a machine-readable, optimizable artifact.

However, this is a *narrow domain* observation (transformer architecture + navigation task + permutation invariance metric). The paper does not argue this generalizes to other protocol systems or identify the mechanism at the meta-level. It is competent empirical work identifying a specific architectural pathology, not a sustained theoretical argument about legibility-driven ossification or metric capture in protocol design.

## Research connections

- **L-023:** Confirms the motif that formalization of coordination structure can suppress output diversity; here, diversity of agent actions is eliminated under permutation-invariance enforcement.
- **L-004 (Goodhart):** Weak connection; permutation error is a proxy for robustness, and optimizing it alone produces unintended behavioral collapse—but the paper does not frame it as metric capture or unmeasurable-to-measurable proxy drift.
- **seed-451:** Directly cited in triage; action collapse under token-ordering formalization fits the seed's intuition about informality loss under legible enforcement.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**RATIONALE FOR STORE-ONLY:** This meets one escalation criterion (introduces a mechanism—action collapse under formalization of agent ordering). However, it lacks: (a) sustained theoretical argument (it is empirical observation + diagnosis, not law-shaped reasoning); (b) cross-domain generalization evidence (confined to transformer + navigation); (c) challenge or extension of existing laws (it refines rather than extends L-023). The work is well-executed but domain-specific. No new seed warranted; seed-451 already captures the relevant fragment.
