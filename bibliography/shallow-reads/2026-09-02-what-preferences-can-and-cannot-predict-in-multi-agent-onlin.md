# What preferences can - and cannot - predict in multi-agent online learning

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.13810
**Date read:** 2026-09-02
**Connected to:** L-010, L-004
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper examining the relationship between ordinal preference structures (the "preference graph" of a game) and equilibrium selection under no-regret learning dynamics (FTRL). The work asks whether preference data alone can predict long-run behavioral outcomes, establishing conditions under which dynamically stable sets must be "preferentially stable" (closed under profitable deviations).

## What I took from it

The paper is technically sound but operates within the equilibrium-selection tradition of game theory, not in the protocol or automation domain. The core contribution—that preference graphs constrain but do not fully determine learning dynamics outcomes—is a negative result about predictability from ordinal data alone. This touches L-010 (Coordination Adoption Nonmonotonicity: under what conditions do preferences + learning dynamics produce nonmonotonic adoption?) and L-004 (Goodhart Generalization: optimization over preference proxies), but only tangentially.

The paper does not examine what happens when preferences themselves become formalized, computable, or embedded in automated enforcement machinery. It does not explore how legibility of preference data changes agent behavior, nor does it track preference ratcheting under repeated optimization cycles. The work is fundamentally about classical equilibrium prediction, not about how protocol formalization distorts or captures preference structures.

## Research connections

- **L-010:** Preferences alone do not determine adoption trajectories in multi-agent learning; additional dynamics factors intervene. But the paper does not ask whether *formalization* of preferences changes this relationship.
- **L-004:** The paper assumes preferences are given and stable; it does not examine metric capture or proxy drift when preference orderings become the target of optimization.
- **seed-077:** Metric-Induced Preference Ratcheting — not addressed; the paper does not track preference evolution under learning pressure.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
