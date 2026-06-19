# Coarse Preference Reporting in the Bottleneck Model: Approximate Strategyproofness and Efficiency

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.17400
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mechanism design paper studying scheduling through a bottleneck resource under incomplete preference revelation. The work trades off exact strategyproofness (achievable via VCG) for computational simplicity and practical tractability by allowing agents to report preferences from a discrete menu rather than continuously.

## What I took from it

The paper addresses a real tension in protocolized systems: exact truthfulness under full information revelation is theoretically clean but operationally expensive. By introducing coarse reporting, the authors implicitly accept approximate strategyproofness—agents still have limited incentive to misreport, but not zero. This is pragmatically important for the "new nature" because it shows mechanism design moving toward bounded rationality and resource constraints *as design features*, not failures. 

However, the contribution is narrowly circumscribed: it applies a known engineering tradeoff (discretization) to a specific bottleneck scheduling problem. The paper does not appear to establish a new principle about how protocolized systems degrade gracefully under information constraints, nor does it provide a generalizable law about the relationship between preference granularity and mechanism stability across domains. It is a competent local optimization, not a foundational insight.

## Research connections

- none (no active hypotheses yet established in this research context)

## Candidate laws or signals

- **CL-CoarseReport-1:** Discrete preference reporting reduces strategyproofness to an approximation, but may be inevitable in large-scale protocolized systems where exact preference elicitation and VCG-type computation become infeasible; the loss in truthfulness may be acceptable if bounded and predictable.
