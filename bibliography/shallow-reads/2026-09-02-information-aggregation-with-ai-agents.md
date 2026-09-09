# Information Aggregation with AI Agents

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2604.20050
**Date read:** 2026-09-02
**Connected to:** L-008, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Experimental game theory paper testing whether LLM-based trading agents can aggregate dispersed private information through prediction market price signals. Measures success by log error of final market price against ground truth across information structures of varying difficulty; finds performance degrades on harder structures.

## What I took from it

The paper is a competent empirical study in mechanism design but does not present a sustained theoretical or empirical argument about protocolized systems beyond its specific domain. It demonstrates that AI agents fail at information aggregation in complex structures, but the failure mode is attributed to agent reasoning capacity rather than to any structural feature of the protocol itself or to incentive dynamics that would generalize.

The work sits downstream of L-008 and L-012 but does not advance either. It shows agents optimizing a legible signal (price) in a controlled setting, but offers no mechanism by which that optimization restructures the protocol layer, displaces the intervention point, or produces asymmetric costs. The deterioration under complexity is cognitive, not structural. This is a tool-and-benchmark paper, not a primary source making a claim about law-shaped regularities in protocol behavior under optimization pressure.

## Research connections

- **L-008:** Agents do optimize computable enforcement signals (price), but paper does not isolate whether optimization pressure changes the protocol's equilibrium structure or only agent performance within it.
- **L-012:** No evidence of intervention-layer displacement; the prediction (private signal) remains cognitively integrated with the decision (trade), not separated into legible input → automated decision.
- **seed-128:** Tangential; agents do conform to legible audit (price history), but no evidence of convergence or drift in strategy space.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
