# Idea: Multiple-choice aggregation (N options) is fast but inconsistent; yes/no binary 

**Source:** Discord #🚜-protocols-for-business (by 4umd)
**Date read:** 2026-09-22
**Connected to:** L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** The idea correctly identifies a cost redistribution pattern but remains at the level of task-specific trade-off. It does not generalize the *mechanism* by which consistency demands migrate across protocol layers, nor does it isolate what makes binary ordering fundamentally different from N-ary aggregation under formalization pressure. Without that separation, it restates L-006 rather than seeding a new inquiry.

## What this is

The claim proposes that under resource abundance, protocol designers will shift from fast-but-inconsistent multiple-choice aggregation to slower-but-consistent binary aggregation, suggesting a preference for consistency over speed when coordination cost can be offloaded to parallelization.

## What I took from it

This is a competent application of L-006's core insight: protocol redesigns do not eliminate coordination cost, they redistribute it. The idea correctly observes that moving from N-ary to binary choice pushes computational/temporal cost into parallelization rather than eliminating the coordination burden.

However, the idea stops at the surface of the phenomenon. It does not ask *why* binary aggregation produces consistency while N-ary methods do not—a question that might reveal something deeper about legibility, verification asymmetry (L-002), or formalization ratcheting (L-003). The asymmetry could be mechanical (binary choice has lower decision-tree complexity) or epistemic (N-ary aggregation forces lossy compression of heterogeneous preferences, introducing variance). These are different regularities. The idea conflates cost-shifting with a solved trade-off, when the real research target is what makes certain aggregation topologies structurally inconsistent under certain constraints.

## Research connections

- **L-006:** Direct application; confirms that aggregation method choice redistributes rather than eliminates coordination cost across the parallelization layer.
- **L-002:** Possible connection: does binary verification have lower hardness asymmetry than N-ary? Worth testing.
- **L-004:** Possible connection: does the choice of N vs. binary reflect optimization pressure on a consistency proxy, and does that proxy capture the true coordination target?
- **seed-136:** Possible connection: binary choice may be a coordination *sink* because it is more legible/text-protocol-expressible than N-ary preference distributions.

## Seed

**Seed title:** None

**Seed type:** —

**Seed text:** —

---

**Decision:** The idea is a sound micro-observation but does not generalize beyond confirming an existing law. It does not isolate a new regularity, open a new causal question, or propose a mechanism worth tracking independently. Store as evidence for L-006; do not seed.
