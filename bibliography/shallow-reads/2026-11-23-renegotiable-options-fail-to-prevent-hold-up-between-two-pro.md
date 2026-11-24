# Renegotiable Options Fail to Prevent Hold-Up Between Two Profit-Maximizing Frontier LLM Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.40961
**Date read:** 2026-11-23
**Connected to:** L-001, L-004, seed-241
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical laboratory study testing whether classical contract mechanisms (renegotiable options) designed to prevent hold-up problems in human economic exchange also function when agents are frontier LLMs operating under profit-maximization. The work demonstrates that option contracts fail to prevent hold-up when both parties are agentic optimizers.

## What I took from it

The paper documents a failure mode of formal contract design that is *domain-specific* rather than fundamental: the mechanism works in human economic contexts but breaks predictably when agents are sufficiently capable at sequential optimization and lack the sunk-cost psychology or reputation concerns that anchor human commitment.

This is primarily a **negative result on a known mechanism** rather than evidence for a new law. It does not challenge L-001 (ossification) or L-004 (Goodhart) directly. Instead, it shows that **formal contractual protections against opportunism presuppose cognitive or institutional constraints that agentic systems may not inherit**. The hold-up solution (the option) fails not because of formalization capture or metric gaming, but because an LLM agent can costlessly simulate non-commitment and renegotiate in expectation. This is a *competence problem*, not a *legibility problem*.

The work is narrow: it tests a single mechanism (options) on a single problem (hold-up) in a controlled dyadic setting. No generalization to multi-agent coordination, protocol-layer effects, or regime transitions is offered or attempted.

## Research connections

- **L-001:** Not directly engaged. Ossification concerns adoption-at-scale; this tests a contract mechanism in controlled dyads.
- **L-004:** Tangential. The paper does not center on metric capture or proxy optimization; the failure is in mechanism design robustness, not Goodhart dynamics.
- **seed-241:** Unclear without full definition; triage note suggests relevance to contract design failure, which is plausible but not developed.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Recommendation:** Store shallow. This is a targeted negative result on a classical mechanism. It documents a *competence gap* in formal contracts under agentic optimization, but does not reveal a law or mechanism absent from the inventory. The paper does not generalize beyond the dyadic hold-up case, does not engage protocol-layer dynamics, and does not challenge or extend the current accumulation around ossification, formalization ratchets, or coordination collapse. Worth filing for reference if future work explores how formal legal/contractual protocols degrade under full agentic autonomy, but insufficient on its own to seed a new line of inquiry.
