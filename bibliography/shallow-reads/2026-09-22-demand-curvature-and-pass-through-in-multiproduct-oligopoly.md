# Demand Curvature and Pass-Through in Multiproduct Oligopoly

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2604.21423
**Date read:** 2026-09-22
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper in industrial organization economics that decomposes pricing response under multiproduct Bertrand competition. It develops tractable characterizations of how economic interventions (price controls, taxes, subsidies) propagate across product lines and firms, isolating demand curvature, cross-product substitution, and ownership structure as independent drivers of equilibrium adjustment.

## What I took from it

The paper provides **mechanistic granularity** on incentive propagation in systems where optimization pressure is applied to a scalar or subset of observables. The decomposition explicitly separates demand curvature (local price elasticity) from substitution effects (cross-good demand shifts) from ownership effects (multi-product internalization), showing that intervention effects depend critically on which dimension dominates. This maps onto L-004 (Goodhart Generalization) and L-008 (Proxy Optimization Under Computable Enforcement) by showing that when a policy target becomes legible and computable (e.g., a price cap on one product), firms optimize around it in ways that depend on the structural geometry of demand—not just the nominal constraint.

However, the paper does not investigate *failure modes* when these decompositions break down, nor does it explore how repeated interventions change the stability of the decomposition itself. It is a characterization tool, not a theory of how protocol escalation or metric capture unfolds. The insights are domain-specific: pricing under regulatory intervention in oligopolies. No claim that the decomposition generalizes to non-market protocol systems or that it identifies a new mechanism absent from the current inventory.

## Research connections

- **L-004:** Confirms that optimization under legible constraint depends on structural properties (demand curvature, substitution) that are often not the same as the nominal target; pass-through diverges from 1:1 because of cross-product dynamics.
- **L-008:** Illustrates how computable enforcement (price caps) creates legible optimization surfaces; firms navigate around the constraint using product-level and cross-firm substitution, which is the mechanism L-008 aims to characterize.
- **seed-134:** Tangential: firms redistribute pricing across products to preserve profit under intervention, analogous to how agents redistribute effort across metrics to preserve total value under legible audit.

## Seed

**Seed title:** none

---

**Rationale for no seed emission:** The paper is a solid technical contribution to pricing theory under constraints, but it does not generalize a mechanism beyond its domain. The decomposition (demand curvature + substitution + ownership) is specific to multiproduct pricing under price-control interventions. It does not propose a principle that would hold in, say, attention allocation protocols, safety certification systems, or distributed coordination. It confirms existing intuitions about how constraints propagate (L-004, L-008) rather than opening a new regularity worth tracking across domains. Store as reference for future calibration of L-008 empirically, but no new law-shaped fragment merits seeding.
