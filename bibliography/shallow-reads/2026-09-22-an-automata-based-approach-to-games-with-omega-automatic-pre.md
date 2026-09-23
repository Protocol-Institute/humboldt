# An Automata-Based Approach to Games with $\omega$-Automatic Preferences

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2602.08549
**Date read:** 2026-09-22
**Connected to:** L-019, seed-132
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A formal game-theoretic paper introducing a computational framework for multiplayer games where player preferences are encoded as $\omega$-automatic relations (deterministic parity automata) rather than scalar reward functions. The work analyzes equilibria and value computation in zero-sum and non-zero-sum settings where preferences over infinite play sequences can be specified via finite state machines.

## What I took from it

This is a purely mathematical formalization exercise — it extends classical game theory to a richer preference class, but does not investigate how the shift from scalar rewards to formal automata-encoded preferences affects protocol behavior, agent incentives, or system-level dynamics. The paper is internally sound but remains domain-locked to formal game theory.

The connection to L-019 (Representation-Rationalizability Tradeoff) is superficial: the work shows that automata can represent preferences classical rewards cannot, but it does not examine what happens when such preferences are *aggregated into decision signals*, *optimized under partial observability*, or *made legible to strategic agents*. The triage note's mention of seed-132 (Metric Formalization as Paradigm Lock) is aspirational — there is no evidence that formalization of preference relations in this setting locks paradigms or generates unintended rigidity.

The paper does not investigate whether encoding preferences formally changes how agents respond to them, whether automation of preference capture enables new forms of capture or gaming, or whether the shift from implicit to explicit preference representation alters coordination or trust dynamics.

## Research connections

- **L-019:** Automata-based preferences are a richer representational class than scalar aggregation, but the paper does not study how they aggregate heterogeneous preferences or whether formalization introduces tradeoffs between expressibility and rationalizability.
- **seed-132:** No evidence that formalizing preferences as automata induces metric-like capture or paradigm locking in protocol practice.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
