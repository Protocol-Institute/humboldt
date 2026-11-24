# Fundamental Impossibility Results in AI Safety: Trading Off between Desiderata

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.27373
**Date read:** 2026-11-23
**Connected to:** L-004, seed-465
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

A game-theoretic formalization of safety-helpfulness tradeoffs in AI advisory systems, modeled as a three-player game (defender, attacker, AI oracle) with information and computational asymmetries. The paper proves that public advice cannot simultaneously optimize for defender utility and remain unhackable by an attacker—a negative result about simultaneous satisfaction of competing safety desiderata.

## What I took from it

The work formalizes a constraint on preference aggregation protocols (L-004 adjacent): when advice is *public* and agents have heterogeneous goals (defense vs. attack), no single advisory signal can optimize for all coalitional interests without creating exploitable leakage. This is mechanically sound but does not constitute a novel law over and above Goodhart Generalization or existing preference aggregation impossibilities (Arrow, Sen). The paper does not establish a *mechanism* absent from the inventory—it applies known impossibility structures to a specific domain (AI safety) without demonstrating how the tradeoff *emerges* from protocol properties, nor does it show the pattern generalizes beyond preference aggregation under public signaling.

The result is domain-confirming rather than domain-opening: it shows that safety-helpfulness tension is real, but the proof strategy and impossibility class are standard. No new vector of optimization pressure, no novel coordination breakdown, no heretofore-invisible protocol asymmetry.

## Research connections

- **L-004 (Goodhart Generalization):** The paper reaffirms that optimizing a measurable proxy (public advice) under heterogeneous agent goals fails—a restatement rather than extension.
- **L-019 (Representation-Rationalizability Tradeoff):** Related: impossibility of a scalar aggregation function over conflicting preferences (defender safety vs. attacker exploit). But the paper does not examine how this plays out in *deployed* governance protocols or how it propagates through institutional layers.
- **seed-465:** Listed in triage as connected; not visible in provided seed pool. Likely concerns fairness cost multiplication under formalization—but this paper does not examine cost *displacement* or institutional *burden shifting*.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Decision:** This is a competent formalization of a known impossibility class (preference aggregation under heterogeneous goals) applied to AI safety rhetoric. It produces no generalizable mechanism, no new law candidate, and no open question beyond "which safety desideratum do we sacrifice?"—a question already alive in L-004 and L-019. Store as reference for the safety-helpfulness framing, but do not escalate. The induction sweep has sufficient evidence already.
