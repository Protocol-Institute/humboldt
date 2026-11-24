# The Complexity of Strategizing Against No-Regret Learners: Pure When It Is Easy, Hard Even When Mixed

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.36261
**Date read:** 2026-11-23
**Connected to:** L-001, L-009
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic hardness result proving that polynomial-time optimization against no-regret learners becomes NP-hard even when mixed strategies are permitted. The work studies finite-horizon repeated games with bounded payoffs, establishing computational barriers to strategic exploitation that persist across strategy representation classes.

## What I took from it

This is a narrow computational complexity result, not a primary theoretical argument about protocol or system behavior. It establishes a negative result (what cannot be computed efficiently) but does not propose or test a mechanism governing how protocols or artificial systems actually behave under adoption, coordination, or formalization pressure.

The connection to L-001 (ossification) and L-009 (catastrophic risk cancellation) is suggestive but not substantive: the paper does not address why protocols become harder to modify under adoption, nor does it model competitive races with asymmetric deployment risks. The hardness is about *computing* optimal strategy against a known learner class — a problem in mechanism design and optimization, not about how systems self-organize under real coordination pressure or how formalization changes system behavior.

The work is technically competent but confined to its own domain: it does not generalize a pattern about artificial systems as such, nor does it challenge or extend any law in the current inventory.

## Research connections

- **L-001:** Nominally related by triage note, but the hardness result describes computational barriers to strategy optimization, not protocol modification costs under adoption. No direct bearing.
- **L-009:** Hardness against learners does not map to asymmetric deployment risk or catastrophic cancellation in symmetric races. Tangential at best.
- none

## Seed

**Seed title:** none
