# Funding the runners-up beats a golden ticket

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.19552
**Date read:** 2026-09-22
**Connected to:** L-004, seed-130
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical comparison of allocation rules in peer-review funding protocols. Uses 10,625 rejected conference submissions (2017–2024) and later citation percentiles as ground truth to evaluate whether a "golden ticket" rule (minority-support override) outperforms alternative allocation methods at the same budget constraint (10% of annual acceptance count).

## What I took from it

This is a narrow domain-specific evaluation of a single protocol variant. The paper tests whether a known anti-Goodhart mechanism (amplifying minority signal rather than maximizing a scalar metric) produces better downstream outcomes than competing rules. The citation-percentile outcome is itself a proxy—a reasonable one for research impact, but a proxy nonetheless—and the paper does not investigate whether the allocation rule generalizes across different evaluation criteria or whether the superiority of "runners-up" funding depends on hidden structural properties of the review pool or citation ecology.

The work touches L-004 (Goodhart Generalization) by showing that a protocol designed to resist metric capture (golden ticket as a circuit-breaker on consensus scoring) can be outperformed by a different anti-capture strategy (distributed minority support). However, the paper treats this as a straightforward empirical question rather than probing *why* distributed minority support might be more robust, or under what conditions the advantage would reverse. No mechanism is offered; no generalization pathway beyond peer review is explored.

## Research connections

- **L-004:** Tests empirically whether override-based metric resistance beats consensus-based resistance; confirms that naive metric maximization underperforms, but does not isolate the mechanism or boundary conditions.
- **seed-130:** The finding that "distributed sufficiency" (runners-up aggregation) beats "concentrated override" (golden ticket) may reflect heterogeneous evaluator competence or domain-specific signal patterns rather than a general principle; treats boundary displacement as an allocation outcome rather than a protocol invariant.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
