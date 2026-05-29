# Decoupled Delay Compensation: Enhancing Pre-trained MARL Policies via Learned Dynamics Filtering

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2605.26286
**Date read:** 2026-05-29
**Connected to:** H-002, L-005
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper proposing a learned state-estimation layer to patch performance degradation in pre-trained multi-agent RL policies when exposed to realistic delays and stale observations. The core contribution is a modular compensation mechanism (gated transition model + recurrent filtering) applied at execution time without retraining the base policy.

## What I took from it

This is a *symptom paper*, not a law paper. It documents and engineers around a real friction point—the gap between idealized synchronous training and asynchronous real-world operation—but treats it as a technical problem to be solved locally, not as a window into structural properties of protocol systems.

The relevance to H-002 is inverted: rather than studying whether trust accumulates *despite* technical imperfection, this work shows engineers can defer trust issues downstream by adding compensatory layers. It's a manifestation of L-005 (working systems resist restructuring) applied pragmatically—the base policy is frozen and wrapped rather than redesigned—but the paper provides no theoretical insight into *why* this layering strategy works or when it fails. The learned model is a black box; the dynamics filtering is domain-specific. This is engineering resilience, not law discovery.

No generalization beyond MARL execution environments is attempted or visible.

## Research connections

- **H-002:** Observes that policies trained under idealized conditions degrade under realistic friction; does not examine whether age/stability of the base policy correlates with compensation difficulty.
- **L-005:** Instantiates the law (policy frozen, compensatory layer added rather than redesign), but does not probe the boundaries or costs of this approach.

## Candidate laws or signals

none
