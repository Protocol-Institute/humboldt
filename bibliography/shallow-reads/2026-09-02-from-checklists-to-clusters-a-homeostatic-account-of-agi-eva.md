# From Checklists to Clusters: A Homeostatic Account of AGI Evaluation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2510.15236
**Date read:** 2026-09-02
**Connected to:** L-004, L-007
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological critique of snapshot-based AGI evaluation frameworks, arguing that symmetric domain weighting and instantaneous capability scoring miss the temporal and stress-resistant properties that characterize genuine general intelligence. The author proposes a homeostatic clustering model emphasizing durability and cross-domain coupling over additive multidomain profiles.

## What I took from it

The paper identifies a real tension in how protocol systems (here: evaluation protocols for AGI) can trap themselves via metric architecture. Symmetric weighting and snapshot scoring are *legible* and *commensurable* — they solve immediate coordination problems in evaluation governance — but they systematically filter out the very properties (durability, coherence under perturbation, temporal stability) that matter most for distinguishing robust capability from brittle performance.

This is a direct instance of **L-004 (Goodhart Generalization)** at work: the evaluation protocol optimizes toward measurable proxies (domain scores, aggregated metrics) that diverge from the unmeasurable goal (genuine general intelligence). The paper also echoes **L-007 (Trust Ratchet)** in reverse — current evaluation protocols accumulate *illegitimate* confidence because they conflate snapshot performance with validated durability. However, the paper does not examine the *protocol dynamics* that produced this misalignment (ossification pressure, adoption lock-in, coordination cost), nor does it trace how evaluation protocols themselves become resistant to redesign once institutions depend on their outputs. It remains a critique, not a causal or structural analysis.

## Research connections

- **L-004:** Snapshot metrics as proxy capture — evaluation protocols optimize toward commensurable scores while the goal (robust general intelligence) remains unmeasurable and multidimensional.
- **L-007:** Trust accumulation decoupled from structural validity — current evaluations accumulate institutional confidence faster than evidence of actual durability warrants.
- **seed-073:** Correlated failure under proxy consensus — symmetric domain weighting may induce spurious coherence, masking independent failure modes until stress testing.
- **seed-077:** Metric-induced preference ratcheting — once evaluation rankings become legible and consequential, downstream systems optimize toward evaluated properties rather than underlying capability.

## Method note

This work exemplifies a common pattern in meta-research: identifying the *symptoms* of a protocol misalignment without excavating its *structural causes*. Evaluation frameworks ossify not because their designers are unaware of their shortcomings, but because institutions, funding decisions, and public credibility become locked into their outputs. Future work on protocol evaluation should distinguish between "what the ideal metric would measure" (the paper's focus) and "why this suboptimal metric persists and resists change" (the causal question). The latter requires examining adoption pressure, coordination cost conservation, and institutional trust ratcheting — not just capability theory.
