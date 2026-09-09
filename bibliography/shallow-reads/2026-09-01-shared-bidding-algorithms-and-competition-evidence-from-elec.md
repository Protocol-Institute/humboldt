# Shared Bidding Algorithms and Competition: Evidence from Electricity Markets

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.13002
**Date read:** 2026-09-01
**Connected to:** L-004, seed-053
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary empirical source providing direct evidence for seed-053 (shared infrastructure emergent collusion) and testing whether metric capture (L-004) operates through algorithmic delegation rather than human optimization; mechanism of coordination cost displacement under legibility is novel.

## What this is

Empirical study of Australian electricity market battery bidding using linked algorithmic provider data at 5-minute frequency. The paper tests whether competing firms using the same third-party bidding algorithm exhibit correlated behavior inconsistent with competitive pricing, and whether information disclosure reforms that increase observability of shared state variables strengthen co-movement.

## What I took from it

This is a direct test of **seed-053 (Shared AI Infrastructure Emergent Collusion)** under controlled observability conditions. The core finding—that algorithm-paired competitors show co-movement *strengthened by disclosure reforms that make common state legible*—suggests collusion is not a static property of the shared algorithm but a *function of what the algorithm can "see" together*. This inverts the usual narrative: information transparency intended to support competition instead enables coordination when the observing agent is algorithmic and shared.

More broadly, this instantiates **L-004 (Goodhart Generalization: Metric Capture)** in a new form: the bidding algorithm optimizes for a proxy (clearing price, scarcity signal, margins) that becomes legible to multiple competitors simultaneously, creating inadvertent joint optimization of a shared objective function. Critically, the humans involved are not strategizing collusion—the coordination emerges from the *structure of what is computable and shared*. This speaks to **L-008 (Proxy Optimization Under Computable Enforcement)**: when protocol obligations or strategic signals become precisely computable and enforcement/payoff signals are legible to automated optimizers operating on shared infrastructure, coordination pressure accumulates without explicit agreement.

## Research connections

- **L-004:** Metric capture operates not only through human optimization but through shared algorithmic delegation; the "metric" (scarcity, margin, clearing state) becomes jointly observable and simultaneously optimized.
- **L-008:** Direct evidence that automated agents optimize shared legible signals in ways that produce coordination outcomes; mechanism is computable state + shared observer + asymmetric information advantage.
- **seed-053:** Confirms the basic hypothesis; adds mechanism: collusion strengthens under *transparency* because legibility enables algorithmic joint optimization, not because humans secretly conspire.
- **L-001:** Suggests ossification pressure: once shared algorithms are deployed at scale, they become coordination infrastructure—difficult to modify without breaking the market they now stabilize.
- **L-006:** Coordination cost may be *displaced* rather than conserved: human negotiation costs drop to zero (no explicit collusion) but are replaced by algorithmic co-movement costs (price suppression, market inefficiency).

## Seed

**Seed title:** Transparency Paradox in Shared Algorithmic Infrastructure

**Seed type:** observation

**Seed text:** When competing agents delegate decisions to shared algorithmic infrastructure, regulatory increases in observability of common state variables can strengthen rather than weaken coordination outcomes. The mechanism is not human conspiracy but automated joint optimization of legible shared metrics. This suggests a general principle: in systems where the optimizing agent is algorithmic and non-rival (multiple competitors share the same inference), information transparency that increases legibility of shared state *increases* rather than decreases collusive pressure. The paradox dissolves if we recognize that "competition" assumed human asymmetric information; algorithmic delegation reverses the asymmetry by making internal decision variables perfectly legible to all downstream users of the same algorithm.
