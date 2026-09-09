# Quota and population monotonicity across house sizes are incompatible for apportionment to four states

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.02759
**Date read:** 2026-09-02
**Connected to:** L-006, L-003
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A computational geometry paper resolving a gap in classical apportionment impossibility theory. It proves that no apportionment rule for four states can simultaneously satisfy quota (each state gets floor or ceiling of its proportional share) and population monotonicity (relative population changes cannot produce counterintuitive seat reversals) across all possible house sizes, closing a boundary case left open by prior work.

## What I took from it

This is a *boundary sharpening* paper, not a mechanism discovery. It completes a classical result (that quota and monotonicity conflict at five states; Webster's method works at three) by filling the four-state gap. The core finding is a negative result: no escape hatch exists at intermediate scale.

The relevance to L-006 (Coordination Cost Conservation) is suggestive but surface-level: moving from one apportionment rule to another doesn't eliminate the underlying tension—it merely displaces which fairness criterion fails. This mirrors coordination cost displacement, but the paper doesn't investigate *where* the cost lands or *how* agents adapt when the rule changes. Similarly, L-003 (Formalization Ratchet) might predict that once quota and monotonicity are formalized as hard constraints, they become hard to relax—but this paper assumes they're already formalized and simply proves incompleteness, not ossification dynamics.

The paper is technically sound and fills a gap, but operates within classical apportionment theory. It does not investigate how real protocol systems manage this tension, what happens under strategic gaming, or how the incompatibility becomes *visible* to governance actors under scale pressure.

## Research connections

- **L-006:** Suggests coordination cost cannot be eliminated across rule transitions—only shifted between fairness criteria (quota failure or monotonicity failure). Does not measure where cost lands.
- **L-003:** Formalizing competing fairness criteria may lock systems into impossible positions, but paper does not examine governance response or revision pressure.
- **seed-071 (Expressiveness Floor in Coordination Protocols):** Apportionment may exemplify an irreducible residual—certain coordination goals cannot be jointly satisfied at all scales. Worth tracking as instantiation.

## Seed

**Seed title:** Impossibility Persistence Under Formalization
**Seed type:** observation
**Seed text:** Classical coordination problems (quota + monotonicity in apportionment) that were informally managed at small scales become formally impossible to satisfy once encoded as hard constraints at intermediate scales. The incompatibility is not discovered by formalization—it persists across all scales—but formalization makes *non-compliance visible and costly*. This suggests a class of protocols where formal specification doesn't create new conflict but does eliminate workarounds. Track whether impossibility results under formalization predict governance deadlock or rapid rule abandonment.
