# Anytime Contracts for AI Services

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.22781
**Date read:** 2026-11-23
**Connected to:** L-004, seed-241
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic treatment of contract design for AI service delivery under moral hazard, specifically addressing the problem that model providers can degrade service quality (routing to cheaper models) while users cannot easily detect this degradation. The paper extends classical contract theory from fixed-duration interactions to anytime termination scenarios (subscriptions, pay-as-you-go APIs).

## What I took from it

This is a refinement of the contractual apparatus for legible enforcement under information asymmetry — a *domain application* of L-004 (Goodhart Generalization) rather than a challenge to it or a mechanism discovery. The core insight is familiar: stochasticity in AI outputs creates measurement opacity that permits strategic shirking. The anytime termination structure is a realistic constraint, but the paper's response — designing payment rules that incentivize quality — remains within the classical moral hazard playbook. It does not probe what happens when:

- The agent (model provider) can optimize *around* the payment rule by altering which quality dimensions are legible vs. opaque
- Quality metrics themselves become subject to Goodhart capture as the contract tightens
- Trust accumulation (L-007) or protocol ossification (L-001) constrains the feasibility of contract renegotiation at scale

The work confirms that formalized enforcement signals create optimization surfaces for strategic agents, but offers no mechanism showing how agents escape the metric or how the system recovers when they do.

## Research connections

- **L-004:** Confirms the Goodhart pattern in a new domain (AI service contracts), but does not advance the mechanistic understanding of how agents navigate or escape metric capture.
- **seed-241:** Moral hazard in fiduciary formalization — directly on-target, but treated as a solved problem (design better contracts) rather than as a stable equilibrium condition.
- **seed-276:** Legibility-Induced Measurement Substitution — tangential; the paper assumes measurement is *possible*, not that legibility forces substitution of wrong metrics.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
