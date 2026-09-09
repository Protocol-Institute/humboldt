# Fairness--Stability Trade-offs in Many-to-One Matching

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.17295
**Date read:** 2026-09-02
**Connected to:** L-006, seed-020
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper characterizing the trade-off between fairness (firm-side) and coalition stability (core stability) in many-to-one matching markets with monetary transfers. The authors develop a bottleneck characterization of the largest "core factor" supportable by a matching, derive polynomial-time algorithms, and prove that certain safe matching procedures satisfy envy-freeness-up-to-one (EF1).

## What I took from it

This is a competent technical contribution to mechanism design, but it operates entirely within the bounded domain of matching market design. The fairness-stability trade-off it surfaces is real and measurable — but it is a *consequence* of the formal constraints of the matching protocol itself (finite agents, transferable utility, coalition formation rules), not a candidate for generalization across protocol systems.

The paper does not investigate *why* this trade-off exists, whether it is conserved across protocol abstractions, or how it manifests when agents gain strategic awareness of the fairness metric itself. It does not ask whether fairness becomes a legible target for optimization pressure (L-004, L-008, L-012), or whether stability constraints shift coordination costs to other layers. It is domain-specific technical work with no mechanism hints that travel.

## Research connections

- **L-006:** The paper studies trade-offs in a single protocol layer (matching + transfer mechanism) but does not examine whether costs are displaced rather than eliminated across abstraction boundaries.
- **seed-020:** Mentioned in triage but the connection is not substantiated in the abstract or content — no evidence of paradigm-locked anomaly tolerance or governance layer displacement.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
