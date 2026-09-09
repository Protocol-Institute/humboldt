# Stop Shipping AI Agents on Faith: Capability Is Not Production Readiness

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.27677
**Date read:** 2026-09-02
**Connected to:** L-001, L-004, L-007
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A governance framework (ProofAgent Index) for assessing AI agent deployment readiness across evaluation, context, compliance, and operational dimensions. The paper argues that capability benchmarks do not predict production safety or stability, and proposes a four-dimensional index to bridge the gap between lab performance and field deployment constraints.

## What I took from it

The work confirms the empirical reality that capability and operability are decoupled — a core stress point in L-001 (ossification under adoption pressure) and L-007 (trust accumulation as a function of operational age, not technical superiority). The paper's framing of "production readiness" as a separate evaluative axis from capability suggests that protocols governing agent deployment will face pressure to formalize legible readiness signals, which creates a natural target for Goodhart dynamics (L-004).

However, the paper remains prescriptive rather than explanatory. It does not investigate *why* capability metrics fail to predict production readiness, what mechanism drives that decoupling, or how readiness indices themselves become captured or ossified under deployment pressure. It proposes an index but does not model how that index will degrade, be gamed, or fail to generalize across heterogeneous production contexts. The work is a competent governance intervention, but does not furnish new law-shaped insight into how protocols governing agentic systems behave under stress.

## Research connections

- **L-001:** Confirms the observation that capability adoption pressure creates readiness assessment pressure, but does not model the mechanism of ossification itself.
- **L-004:** The PAI index itself becomes a measurable proxy for an unmeasurable goal (true production readiness); this paper does not investigate whether the index will be captured by optimization pressure.
- **L-007:** Aligns with the principle that trust accumulates through operational history, but treats this as a design input rather than a law-like regularity.
- **L-012:** Tangentially relevant — the paper proposes to formalize readiness as a legible input to deployment decisions, but does not examine how this legibility reshapes optimization pressure.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
