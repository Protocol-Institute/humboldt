# Proportional Representation for Almost-Solid Coalitions and the Proportional Veto Core for Rankings

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2611.25677
**Date read:** 2026-11-23
**Connected to:** L-019, seed-465
**Kind:** content
**Escalation:** store-only

## What this is

A formal social choice paper extending proportional representation guarantees from voting to ranking aggregation. The work addresses how to allocate representation to voter coalitions when their preferences are "almost solid" — i.e., when members agree on most but not all candidates — by generalizing the proportional veto core framework with candidatewise and setwise guarantees.

## What I took from it

This is technical work in preference aggregation that remains *internal* to the social choice domain. The core contribution is a tightening of the mathematical characterization of proportionality under partial preference alignment — a known problem class receiving incremental formal refinement.

The connection to L-019 (Representation-Rationalizability Tradeoff) is real but *descriptive rather than mechanistic*. The paper shows that certain rationalizability constraints (veto protections) can be preserved while maintaining proportional representation guarantees across prefix lengths. However, it does not investigate *why* this tradeoff emerges, what happens when optimization pressure is applied to the aggregation rule, or how the system behaves under strategic manipulation or metric capture. The work assumes well-behaved, sincere preference reports and does not examine what happens when agents learn the aggregation rule and begin gaming coalition membership or preference signals.

No mechanism is revealed about how formalization of aggregation rules affects strategic behavior, legibility asymmetries, or the emergence of hidden coordination channels — all central to the new nature research agenda.

## Research connections

- **L-019:** The paper provides a mathematical refinement of one specific point in the representation-rationalizability space (setwise veto guarantees), but does not interrogate the deeper tradeoff under optimization pressure or agent strategy.
- **seed-465:** No clear connection; the paper does not investigate how preference heterogeneity affects protocol stability or adoption dynamics.

## Seed

**Seed title:** none

---

**Store as shallow only.** This is competent formal work that solves a precise, bounded problem within social choice theory. It does not introduce a mechanism absent from the current inventory, does not challenge or extend a law under accumulation, and does not generalize the pattern beyond preference aggregation under sincerity assumptions.
