# Complete strategy spaces reveal hidden pathways to cooperation

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2511.17794
**Date read:** 2026-09-02
**Connected to:** L-010, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic study extending prior work on cheap talk and cooperation by moving from hand-picked four-strategy sets to the complete eight-strategy space that emerges naturally from communication + decision-making choices. The claim is that unrestricted strategy spaces reveal cooperation pathways missed by restricted models.

## What I took from it

The paper tests a real concern in protocol design: that architectural constraints on available moves (who can signal, when, to whom, with what binding force) may artificially suppress or enable cooperation modes that would emerge under less restricted conditions. This is relevant to L-010 (Coordination Adoption Nonmonotonicity) insofar as it examines whether cooperation adoption curves shift nonmonotonically as the strategy space itself expands—a question about the relationship between expressiveness floor and coordination stability.

However, the work remains within classical game-theoretic equilibrium analysis. It does not address what happens when strategy spaces themselves become *legible* to optimization or when agents can *dynamically* alter the available strategy space under pressure (the actual concern in protocolized systems). The eight-strategy frame is still finite, enumerated, and stable across the game. In real protocol systems, the risk is different: that expanding expressiveness creates new optimization targets (seed-067, seed-082), or that cooperation emerges only to be captured once the mechanism becomes legible (L-004, seed-059). The paper shows that restricted frames can hide cooperation; it does not show whether *complete* frames preserve it under computable optimization pressure.

## Research connections

- **L-010:** Tests whether cooperation adoption is monotonic in strategy-space size; finds nonmonotonicity, but under idealized game-theoretic conditions where optimization pressure is absent.
- **seed-048:** Directly connected; examines capability-cooperation dynamics when strategy expressiveness is unrestricted.
- **seed-062:** Inverse angle—the paper shows that formalization (enumeration to eight strategies) can reveal hidden patterns, but does not ask whether that formalization itself becomes a new optimization target.
- **L-004:** Raises but does not address: once cheap talk is formalized as a legible cooperation pathway, will agents optimize the signal itself away from its original function?

## Seed

**Seed title:** Expressiveness-Cooperation Plateau Under Legibility
**Seed type:** question
**Seed text:** In game-theoretic models, cooperation emerges more reliably as strategy spaces expand toward completeness, suggesting an expressiveness floor below which cooperation cannot be reliably achieved. However, when strategy spaces become *machine-legible* and subject to real-time optimization pressure (as in protocolized systems), this relationship may invert: beyond a threshold of formalized expressiveness, cooperation pathways become targets for metric capture and strategic boundary concentration. Does there exist a "sweet spot" of expressiveness—complete enough to sustain cooperation equilibria, but opaque enough to resist decomposition into optimizable subgoals?
