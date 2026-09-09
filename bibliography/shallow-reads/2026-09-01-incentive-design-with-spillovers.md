# Incentive Design with Spillovers

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2411.08026
**Date read:** 2026-09-01
**Connected to:** L-006, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper extending classical contract design to multi-agent settings with spillovers (externalities). The main contribution is a characterization of optimal incentive allocation: pay should be proportional to the product of individual productivity, organizational centrality (network position), and monetary responsiveness. Standard technical work in mechanism design.

## What I took from it

The result is competent but localized to principal-agent optimization under known externality structures. The paper assumes the principal can observe or infer: (i) individual productivity measures, (ii) network centrality (spillover topology), and (iii) each agent's sensitivity to monetary incentives. These are assumptions about *legibility* — the paper does not investigate what happens when these quantities become computable post-hoc through behavioral data, or when agents strategically obscure their position or responsiveness.

The framing is consequentialist: optimize payment allocation to maximize effort extraction. This does not intersect with L-006 (Coordination Cost Conservation) in any deep way — the paper does not model what happens to informal coordination, norm-based contribution, or trust when explicit monetary incentives are introduced and then varied. Seed-048 (Capability-Cooperation Inversion) is tangentially relevant only if one read the paper as showing that *increasing* legibility of individual contribution creates conditions for *decreased* spontaneous cooperation — but the paper makes no such claim and does not measure it.

## Research connections

- **L-006:** The paper does not track where coordination costs migrate when a protocol shifts from informal to incentive-based; assumes costs are already formalized and measurable.
- **seed-048:** No mechanism proposed for inversion; the paper assumes capability (legibility of productivity/centrality/responsiveness) and cooperation (effort) are jointly optimized, not inverted.
- **L-004 (Goodhart):** Indirect: the use of "productivity" and "responsiveness" as proxies for unmeasurable goals (actual value creation, true willingness) is a setup for capture, but not examined.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
