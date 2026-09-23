# Pareto-Improving Pricing: Why 3 Is Better Than 2

**Source:** arXiv.org — https://arxiv.org/abs/2609.22652
**Date read:** 2026-09-22
**Connected to:** L-004, L-019, seed-150
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A microeconomic design paper showing that three-tier priority pricing can Pareto-improve on equal-allocation baselines when quality provision is negatively correlated with aggregate supply. The work directly challenges the equity-efficiency tradeoff framing in pricing policy discourse by demonstrating a mechanism for simultaneous improvement on both dimensions.

## What I took from it

The paper's core move is a preference aggregation proxy substitution: it reframes "equity vs. efficiency" (a false scalar tradeoff) into a three-dimensional allocation space where agents are partitioned by willingness-to-pay and compensated differentially. This is not a law-discovery — the mechanism is domain-specific and the proof is equilibrium analysis, not generative.

However, the triage note correctly identifies a deeper pattern: the paper demonstrates how *formalized proxy design* (here: tier selection + compensation rules) can make previously invisible Pareto improvements legible to policymakers. The work operates under the assumption that the three-tier structure is *the natural formalization* of the problem. This is precisely the kind of threshold where L-004 (Goodhart Generalization) and L-019 (Representation-Rationalizability Tradeoff) should activate — the choice to formalize via price tiers rather than via, say, time-based access or randomized quality variation, constitutes a *particular* aggregation protocol. The paper does not examine whether this formalization itself reshapes agent behavior, introduces new optimization surfaces, or locks in interpretation paths downstream.

## Research connections

- **L-004:** The three-tier system is a proxy for "appropriate resource distribution" — under optimization pressure from agents and policymakers, does the tier boundary itself become the target, rather than the underlying preference heterogeneity it was designed to represent?

- **L-019:** The paper assumes a scalar preference aggregation (willingness-to-pay) can be reliably partitioned into three tiers. This directly instantiates the representation-rationalizability tradeoff: expressivity is gained (Pareto improvement is now visible) but only by accepting a fixed categorical structure that may not match actual preference topology.

- **seed-150:** (Not in inventory — cannot assess connection.)

- **seed-134:** Neutrality-Proxy Redistribution Under Legible Optimization — the move from "equal allocation" to "three-tier compensation" is a redistribution of what counts as "neutral" baseline; agents at different tiers now see different reference points.

## Seed

**Seed title:** Formalization-Induced Pareto Visibility as Proxy Lock
**Seed type:** observation
**Seed text:** When a policy problem framed as an intractable tradeoff (equity vs. efficiency) is reformalized via a legible, computable proxy (three-tier pricing with explicit compensation rules), previously dominant solutions (equal allocation) can be shown to be Pareto-suboptimal. The Pareto improvement is real but conditional on the choice of formalization itself. In subsequent iterations, agents and policymakers optimize *within* the formalized structure (boundary concentration, tier migration) rather than questioning the formalization. The question is whether the visibility gain (Pareto proof becomes computable) systematically locks in the proxy choice, preventing discovery of alternative formalizations that might yield different Pareto frontiers.
