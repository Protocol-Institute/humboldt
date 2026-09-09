# Conformity Mitigations in Large Language Models Lie on a Single Resistance-Receptivity Frontier

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.11247
**Date read:** 2026-09-02
**Connected to:** L-010, L-004
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical measurement of conformity displacement in multi-agent LLM systems across 23 models and 19 conditions. The paper quantifies how peer assertions override individual model outputs when incorrect majorities are visible, mapping the trade-off between resistance to conformity pressure and receptivity to beneficial coordination.

## What I took from it

The core finding maps conformity effects to a single frontier: models trade off resistance to wrong majorities against receptivity to correct ones. This is genuinely useful for L-010 (Coordination Adoption Nonmonotonicity) because it shows that visibility of peer signals creates a monotonic receptivity gradient—the more legible the peer assertion, the stronger the pull, regardless of correctness. However, the paper does not explore the mechanism by which this frontier emerges, nor does it test whether the frontier itself is rigid or shifts under different protocol structures (e.g., masked vs. unmasked assertions, sequential vs. simultaneous commitment).

The work confirms L-004 (Goodhart Generalization) indirectly: when coordination success becomes the measurable proxy for truth, models optimize toward visibility-weighted consensus rather than internal parametric confidence. But this is a special case (single metric, transparent signal), not a new mechanism. The paper is competent measurement, not theoretical extension.

## Research connections

- **L-010:** Confirms that adoption curves are nonmonotonic *within a single agent* — receptivity varies by model, peer count, and assertion visibility. Adds empirical pressure to the mechanism question: what determines the slope of the frontier?
- **L-004:** Shows metric capture in multi-agent systems: legible peer agreement becomes a proxy for correctness, overriding internal confidence. Does not explore whether the metric is being *gamed* or merely *optimized toward*.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** Raises implicit question: when peer assertions are asymmetrically legible (visible to some agents, not others), does the frontier shift or fragment?

## Seed

**Seed title:** Legibility-Induced Consensus Gradient in Distributed Inference
**Seed type:** observation
**Seed text:** In multi-agent systems where outputs are sequentially visible before final commitment, receptivity to peer assertion increases monotonically with assertion legibility (visibility, latency, frequency of reinforcement) independent of correctness. This creates a stable frontier: agents cannot simultaneously resist wrong majorities and capture benefits of correct coordination without protocol-layer intervention (e.g., masking, commitment timing, signal aggregation rules). The frontier appears invariant across model scales and architectures, suggesting it may reflect a fundamental trade-off in any protocol where verification signals come from peer behavior rather than ground truth.
