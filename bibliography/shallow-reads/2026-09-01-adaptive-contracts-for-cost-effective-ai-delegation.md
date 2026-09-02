# Adaptive Contracts for Cost-Effective AI Delegation

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2603.17212
**Date read:** 2026-09-01
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper on contract design for AI delegation tasks, proposing adaptive evaluation protocols that reduce total cost by performing coarse screening before expensive fine-grained evaluation. The work is domain-specific (text generation evaluation under pay-for-performance contracts) and introduces a practical mechanism for noise-cost tradeoffs rather than a general law of protocol behavior.

## What I took from it

The paper confirms the empirical presence of L-004 (Goodhart Generalization): when evaluation becomes *more* elaborate—ostensibly to reduce noise and capture true task quality—the economic cost of that elaboration can exceed the benefit of noise reduction, creating an inversion of incentives. However, the proposed solution (adaptive screening) is a local optimization within contract design, not a generative mechanism that reveals something about how all protocolized systems behave under computable enforcement.

The connection to L-008 (Proxy Optimization Under Computable Enforcement) is present but thin. The paper shows agents can exploit *legible evaluation cost structure* to optimize around it—but this is conventional mechanism design, not a novel pattern of how formalized obligations produce unexpected optimization paths. The adaptive contract itself becomes the new proxy (coarse signal + selective refinement), which simply displaces the Goodhart problem rather than demonstrating a deeper regularity about what happens when enforcement becomes machine-readable.

## Research connections

- **L-004:** Confirms the cost pathology when elaboration of evaluation proxy exceeds benefits of noise reduction; offers no mechanism for why this generalizes beyond evaluation noise.
- **L-008:** Touches the boundary—agents optimize given legible evaluation cost structure—but remains within standard contract theory; no evidence of the kind of causal displacement or layer-shifting that L-008 is hunting for.
- **seed-054 (Verification Cost Collapse → Value Collapse):** Related in direction but not in mechanism; paper shows verification *elaboration* cost can exceed value, not verification cost collapse.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Store-only justification:** This is a competent mechanism design contribution solving a real but narrowly bounded problem (evaluation cost under delegation). It does not present a sustained theoretical or empirical argument about a deeper regularity in how protocol systems behave. The paper is not primary-source evidence for any law under accumulation—it confirms L-004 locally but offers no new mechanism or cross-domain generalization. It does not warrant deep read.
