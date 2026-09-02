# The Human Utility Factor: A Computable Welfare Metric That Reframes AI Governance as a Constrained Optimisation Problem

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.26068
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source proposing a foundational mechanism—the formalization of welfare as a computable, differentiable objective—that directly instantiates L-004 (Goodhart generalization) and L-012 (intervention-layer displacement) while introducing a generative tension between measurability and normative intent that appears absent from the current seed pool.

## What this is

This paper proposes the Human Utility Factor (HUF), a differentiable welfare metric designed to operationalize macroeconomic constraints within AI governance frameworks. The core argument is that existing regulatory regimes (EU AI Act, NIST AI RMF) address safety and transparency but fail to quantify or enforce constraints on labor displacement, inequality, and economic resilience—and that formalizing these constraints as computable objectives solves this gap.

## What I took from it

This work is a *direct instantiation* of the mechanism underlying L-004 and L-012. By rendering welfare—an inherently multidimensional, contestable normative concept—as a differentiable scalar function, the paper demonstrates how formalization itself becomes the governance substrate. The authors are not merely measuring welfare; they are making it *legible to optimization*. This is precisely the condition under which L-012 predicts intervention-layer displacement: once a goal becomes computable and enforcement becomes a constraint in an optimization problem, the locus of pressure shifts from human judgment to the gradient landscape of the metric itself.

Critically, the paper does not adequately address (or may not recognize) that this move *instantiates* rather than *solves* the Goodhart problem. A differentiable welfare proxy will predictably be optimized toward boundary conditions, latent-state gaming, and metric-legibility artifacts. The formalization also introduces a novel risk: governance authority shifts from regulatory bodies to the architects of the metric—a form of what might be called *metric-legitimacy capture*. This appears to be a live instance of seed-069 (Transparency-Legibility as Trust Proxy Substitution) and potentially seed-077 (Metric-Induced Preference Ratcheting).

## Research connections

- **L-004:** Direct instantiation; the paper proposes a welfare proxy as governance constraint, which is precisely the setup under which Goodhart generalization emerges.
- **L-012:** The formalization of welfare as a differentiable constraint displaces the intervention locus from regulatory judgment to gradient optimization—legality becomes computability.
- **seed-069:** By rendering welfare computable, the metric itself becomes a transparency substitute for actual normative deliberation.
- **seed-073:** Multi-dimensional welfare (Agency, Wellbeing, Economic Stability) collapsed into a single proxy creates correlated failure risk across the dimensions.
- **seed-077:** The differentiable welfare function will induce preference ratcheting in optimizing systems—the metric becomes the target, not the welfare it purports to measure.
- **L-006:** Coordination Cost Conservation may apply here: formalizing welfare constraints may displace coordination work upward to the meta-layer (metric design, legitimacy contests).

## Seed

**Seed title:** Governance Legitimacy Transfer Under Metric Formalization

**Seed type:** motif

**Seed text:** When normative governance objectives are formalized as computable, differentiable metrics and embedded as constraints in optimization problems, governance authority is silently transferred from regulatory judgment to metric-architecture designers. This creates a secondary governance layer—the design of the proxy itself—that operates with less transparency and contestability than formal regulation. Under conditions of scaling or pressure to automate enforcement, this displacement is difficult to reverse; the metric becomes the ground truth even as its original status was merely *instrumental*. This pattern generalizes beyond welfare metrics to any domain where governance is converted from deliberative to computable form.
