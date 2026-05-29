# Improved Hardness Results for Nash Social Welfare, Budgeted Allocation and GAP via the Unique Games Conjecture

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2605.27098
**Date read:** 2026-05-29
**Connected to:** L-004
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A complexity-theoretic paper proving hardness-of-approximation results for Nash social welfare and related allocation problems under the Unique Games Conjecture. The work contributes technical machinery (a novel dictator test) to establish computational barriers, but remains within the standard competitive analysis framework of algorithmic game theory.

## What I took from it

The paper strengthens known computational limits on welfare-maximizing allocation protocols—specifically, that no efficient algorithm can approximate Nash welfare beyond certain thresholds. This exemplifies L-004 (Goodhart Generalization) in a narrow sense: Nash welfare is itself a measurable proxy for "fair allocation," and the hardness result shows that optimizing it algorithmically becomes intractable near optimal points. However, the paper does not examine *behavioral* capture—what happens when designers and agents actually use welfare-proxies under operational pressure. It remains in the abstract hardness domain, not the protocolized systems domain. The connection to L-004 is real but oblique: the hardness *permits* metric capture downstream (by making true welfare unmeasurable in practice), but the paper itself doesn't investigate that phenomenon in protocol contexts. No implications for protocol ossification, formalization ratchets, or coordination cost conservation.

## Research connections

- **L-004:** Hardness results on Nash welfare approximation show why welfare proxies *cannot* be optimized exactly; they remain crude approximations under computational constraint, predisposing systems to Goodhart effects when deployed operationally—but this paper does not examine that deployment or capture dynamics.

## Candidate laws or signals

none
