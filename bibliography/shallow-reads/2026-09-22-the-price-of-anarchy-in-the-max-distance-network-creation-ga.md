# The price of anarchy in the max-distance network creation game is not constant

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.17395
**Date read:** 2026-09-22
**Connected to:** L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic proof establishing tight bounds on the price of anarchy (PoA) in the max-distance network creation game: the authors construct an infinite family of pure Nash equilibria exhibiting superpolynomial inefficiency ($2^{\Theta(\sqrt{\log n})}$), closing a gap between lower and upper bounds. The work is domain-specific — a mathematical result in network formation games — with no sustained theoretical claim about protocol systems beyond the specific game analyzed.

## What I took from it

This is a refined technical result within game theory, not a contribution to the mechanics of protocolized systems or artificial coordination under adoption pressure. The PoA literature documents equilibrium efficiency gaps, but the paper does not examine how these gaps emerge under real protocol adoption, scaling pressure, or when agents are adaptive over time. L-006 (Coordination Cost Conservation) predicts that total coordination cost is *conserved* across protocol layer transitions — this result measures inefficiency *within* a single equilibrium class, not the dynamics of cost redistribution when a protocol ossifies or when agents shift between coordination modes. The construction is elegant but inert relative to the inventory: it strengthens a bound, not a mechanism of artificial systems under strain.

## Research connections

- **L-006:** PoA measures equilibrium inefficiency; L-006 concerns whether and how coordination cost redistributes when protocols transition. Related only in that both concern coordination cost, but at different grain sizes and temporal frames.

## Seed

**Seed title:** none
