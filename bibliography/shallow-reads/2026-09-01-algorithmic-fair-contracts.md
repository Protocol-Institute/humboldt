# Algorithmic Fair Contracts

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2507.11214
**Date read:** 2026-09-01
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic study of contract design under fairness constraints (envy-freeness), where a principal allocates heterogeneous tasks to agents with differing costs and success probabilities. The paper establishes that while fair allocations always exist, optimizing revenue subject to fairness is computationally hard — no constant-factor approximation is achievable in polynomial time.

## What I took from it

This is a clean instantiation of L-004 (Goodhart Generalization) and L-008 (Proxy Optimization Under Computable Enforcement) in a legible domain. The fairness constraint (envy-freeness as a measurable proxy for distributional justice) becomes the optimization target; agents with precise cost/probability models can then exploit the boundary between what the fairness metric protects and what it leaves open — e.g., accepting "fair" allocations that are individually rational but systematically disadvantage certain agent classes. The computational hardness result is important: it suggests that when fairness is formalized as a computable constraint, the *tractability* of optimization under that constraint becomes a new mechanism for value leakage. The system is fair by the stated metric but expensive to optimize fairly, which creates pressure to weaken or selectively apply the fairness requirement.

The paper does not study this dynamics empirically or across protocol adoption. It is a single-layer game-theoretic model. No mechanism is presented that is absent from the current inventory; the result is a tighter bound on a known phenomenon rather than a new law.

## Research connections

- **L-004:** Fairness (envy-freeness) is a measurable proxy for an unmeasurable goal (justice/legitimacy); optimization under this constraint triggers Goodhart dynamics, though the paper does not study the long-term protocol-level effects.
- **L-008:** The computable enforcement of fairness constraints creates legible boundaries that optimizing agents can exploit; computational hardness of achieving both fairness and revenue optimality is a second-order manifestation of this.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
