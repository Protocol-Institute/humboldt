# Shared Models, Selective Trading, and Order Flow

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2610.01897
**Date read:** 2026-11-23
**Connected to:** L-004, L-010, seed-023
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An experimental economics paper studying whether diversity in decision-making agents (language models) persists through market selection. The authors run synthetic trading markets with a fixed population of three LM families, then observe shifts in model representation across orders as news events change—finding dramatic representation swings (40–48 percentage points) with minimal change in aggregate order volume, suggesting news selectively activates certain model architectures while suppressing others.

## What I took from it

The work is a clean demonstration of **preference aggregation under legible optimization pressure** (L-004, L-010 adjacent), but limited in scope. The key empirical finding is that identical news stimuli produce dramatically different *model-conditional* trading signals—not because models disagree on fundamentals, but because their internal decision procedures weight the same information differently. This is a narrow, controlled instance of Goodhart capture: the "goal" is trading profitably; the proxy is model output; the optimization surface is news framing; the outcome is model-selective activation rather than diversity-preserving aggregation.

However, the paper does not investigate *why* this selection persists, whether it accumulates over time, or whether it generalizes to multi-round protocols where agents condition on prior peer output. It is a snapshot, not a law-tracing instrument. The "homogeneous populations remove opposing flow" fragment at the abstract's end hints at L-010 (nonmonotonic adoption) but is left unexplored.

## Research connections

- **L-004 (Goodhart Generalization):** News framing acts as a proxy for trading signal quality; different models optimize the proxy differently, producing selective representation collapse rather than aggregate drift.
- **L-010 (Coordination Adoption Nonmonotonicity):** The order flow reversals and representation shifts suggest adoption of model outputs is not monotonic with information arrival—suggests possible herding or threshold crossing under information design.
- **seed-023 (Informality as Novelty Sink):** Model diversity is treated as a "formal" property (fixed mixture); selection into legible trading action removes diversity without changing the nominal population. Suggests diversity may be maintained informally (in latent space) but cannot survive formalization as trading orders.
- **seed-515 (Computable Belief as Collusion Surface):** Models with shared training corpora or architecture families may converge on the same trading signal under specific news events—not through explicit coordination, but through identical computable beliefs embedded in architecture.

## Seed

**Seed title:** Model-Conditional Representation Collapse Under Legible Decision Forcing

**Seed type:** observation

**Seed text:** When heterogeneous decision-making agents (differing in training, architecture, or heuristics) are forced to output legible, comparable actions in response to identical information, their representation in the action stream becomes volatile and selective rather than preserving population diversity. The same information stimulus produces dramatically different activation profiles across agent types, and this activation is not stable across stimulus framing—suggesting that diversity exists in latent reasoning but collapses under computable action legibility. This may generalize beyond trading to any protocol that aggregates agent outputs into a legible, comparable, optimizable action space.
