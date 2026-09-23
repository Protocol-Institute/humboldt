# Strategic Classification Has a Missing Lever: Audit Risk

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.22534
**Date read:** 2026-09-22
**Connected to:** L-008, L-014
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This introduces audit cost as a discrete protocol lever that fundamentally restructures the optimization landscape for strategic agents — a mechanism absent from current inventory that generalizes across all proxy-enforcement regimes and directly tensions L-008 and L-014.

## What this is

A game-theoretic model of strategic classification where decision makers possess not only a classifier but also an audit/verification function. The work shows that when agents can be audited at cost, the classifier's role shifts: easily-fakeable features need not be discarded; instead, audit risk becomes a control instrument that trades off verification expense against classifier accuracy, reshaping incentive structure for misrepresentation.

## What I took from it

This paper identifies a missing degree of freedom in proxy optimization under enforcement: the cost and selectivity of verification. Where L-008 concerns proxy optimization under *computable* enforcement, this work shows that the *cost structure* of verification acts as a secondary control variable that changes which proxies remain viable and which misrepresentation strategies are rational. The decision maker can now tolerate (and price) imperfection in a feature by deploying audit pressure selectively—essentially converting a down-weighted or discardable feature into an auditable boundary.

This directly refines L-014 (Strategic Boundary Concentration): when legality or compliance becomes computable, agents concentrate at boundaries. But this model suggests a counter-dynamic: when audit cost is added as a legible parameter, the boundary itself becomes an optimization target—agents don't just cluster at the margin, they calibrate the *risk of crossing it* against audit likelihood. The protocol now has two levers (classification threshold + audit probability/cost), and their interaction creates new equilibrium structures that pure classification cannot achieve.

## Research connections

- **L-008:** Proxy optimization under computable enforcement gains a second dimension—audit cost creates a cost-benefit calculus for misrepresentation that changes which proxies remain informationally useful.
- **L-014:** Strategic boundary concentration is complicated by audit availability; the boundary becomes a probabilistic risk surface rather than a hard threshold, potentially dispersing rather than concentrating concentration.
- **seed-128 (Legibility-Driven Agent Convergence Under Computable Audit):** Audit availability as a legible mechanism may *force* convergence to auditable representations, creating a different lock-in than metric capture alone.
- **seed-145 (Enforcement Legibility as Escalation Trigger):** The paper's model assumes audit cost is transparent/legible; this may trigger strategic escalation when agents can estimate audit probability.

## Seed

**Seed title:** Audit Cost as Proxy Rehabilitation Lever Under Computable Opacity

**Seed type:** mechanism

**Seed text:** In classification protocols where agent features are subject to strategic misrepresentation, audit (verification) cost acts as a second-order control variable that permits a decision maker to retain informationally useful but fakeable features instead of discarding them. Under audit cost legibility, agents face a two-dimensional optimization problem: feature cost and audit risk. This creates a stable equilibrium that pure classification cannot reach—and importantly, the equilibrium cost structure itself becomes observable and susceptible to strategic gaming. The pattern should generalize across any protocol where a measurable proxy is both imperfect and verifiable, including compliance monitoring, resource allocation, and credentialing systems.
