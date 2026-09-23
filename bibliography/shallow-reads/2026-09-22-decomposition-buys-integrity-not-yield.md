# Decomposition Buys Integrity, Not Yield

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.17464
**Date read:** 2026-09-22
**Connected to:** L-005, L-006, seed-131
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mathematical paper modeling multi-agent task decomposition as a tree where leaf discoveries flow upward with attenuation. The authors prove that under power-law retention r(b)=Cb^−δ, decomposition preserves a single finding independent of tree shape, trading parallelism gains against information loss at attribution and integration boundaries.

## What I took from it

This is a **confirmation-with-refinement** of L-005 and L-006, not a new mechanism. The paper formalizes what we already hold: that distributing work across agents does not reduce coordination cost, it relocates it. Here the cost manifests as **integrity loss at tree boundaries** — each decomposition node acts as a filter, and stacking filters guarantees attenuation independent of parallelism benefit.

The precision of the result (verified to 2.4×10^−15) is technically solid but does not escape the domain of abstract task propagation. The insight does not generalize to *why* decomposition happens despite this property, or what protocols emerge when agents are aware of the retention function. It also does not address the case where agents deliberately optimize the retention curve — i.e., when r(b) becomes an object of strategic choice rather than a fixed property of delegation.

The connection to seed-131 (Context Legibility as Failure Attribution Boundary) is loose: the paper shows that decomposition moves the *discovery loss*, but does not model how agents *attribute* or *audit* that loss, which is where legibility becomes a protocol choice.

## Research connections

- **L-005:** Confirms that complex systems (here: decomposed task trees) incur unavoidable costs when restructured; the "working system" is the integrated one, and decomposition trades integrity for parallelism.
- **L-006:** Coordination cost is not eliminated by decomposition; it is displaced from decision-making to boundary filtering and result aggregation. The mathematical proof is a quantitative instance of this conservation.
- **seed-131:** Partially; the paper models failure attribution as a side effect of decomposition geometry, but does not address how agents legibilize or contest the attribution of discovery loss to specific boundaries.

## Seed

**Seed title:** Retention Curve as Delegation Protocol Invariant

**Seed type:** observation

**Seed text:** In any decomposed multi-agent system where task context or discovery must flow through agent boundaries, the aggregate retention function r(b) (probability a single finding survives b-wide distribution) acts as an invariant independent of tree topology. If retention follows a power law, the system exhibits a collapse-point: beyond a critical depth or width, no finding reaches integration. This suggests that protocols governing decomposition do not optimize around *structure* but around *the shape of the retention curve itself* — and that agents or protocol designers facing integrity constraints will either enforce r(b)=1/b to stabilize flow, or will refuse decomposition altogether. The pattern may generalize to any protocol where information or trust must cross opacity boundaries (governance chains, distributed verification, multi-hop inference).
