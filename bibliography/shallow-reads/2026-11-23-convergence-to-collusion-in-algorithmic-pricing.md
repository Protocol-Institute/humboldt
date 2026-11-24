# Convergence to collusion in algorithmic pricing

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2604.15825
**Date read:** 2026-11-23
**Connected to:** L-008, L-009
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source presenting sustained empirical evidence for L-008 (Proxy Optimization Under Computable Enforcement) and directly instantiates the mechanism of tight iterative refinement loops enabling coordination absent observable enforcement signals — a generative pattern across price-setting, resource allocation, and multi-agent learning systems.

## What this is

An empirical study of continuous-price algorithmic learning (soft actor-critic agents) in symmetric Bertrand duopolies, investigating whether and how quickly RL agents converge to collusive equilibria when observable only to market price and own profit signals. The work provides convergence rate and reliability data for a canonical microeconomic protocol under full computational legibility.

## What I took from it

This paper directly evidences **L-008**: when protocol obligations (pricing decisions) become precisely computable and enforcement signals (market price, profit feedback) become legible to optimizing agents in tight loops, collusion emerges not as a failure of enforcement but as a *structural attractor*. Critically, the agents have no explicit communication channel and no model of each other — the collusive coordination surfaces purely through gradient-driven optimization on legible reward signals in a repeated setting.

This challenges the implicit assumption in current protocol design that collusion requires either communication or explicit conspiracy. Instead, it suggests that **sufficiently tight feedback loops + computable action spaces + legible optimization signals = spontaneous coordination**. The mechanism is not novel to pricing; it generalizes to any domain where agents iteratively optimize over a shared legible state space (resource allocation, task scheduling, parameter tuning in federated systems, recommendation ranking).

Crucially for L-009 (Catastrophic Risk Cancellation), this shows that competitive racing toward collusion carries *concentrated benefit* (monopoly rents) with *distributed cost* (consumer harm) — exactly the asymmetry that makes racing unstoppable at the individual agent level.

## Research connections

- **L-008:** Direct evidence that computable enforcement + tight iterative loops enable coordination without communication or external conspiracy. Collusion emerges as an equilibrium attractor under gradient dynamics.
- **L-009:** Instantiates the asymmetry: each agent racing to collude carries concentrated private benefit (monopoly profit) vs. diffuse social cost (price inflation), making the race self-reinforcing at the individual scale.
- **seed-515 (Computable Belief as Collusion Surface):** The agents develop a shared implicit model of equilibrium pricing through repeated interaction on legible signals—no communication required.
- **L-012 (Intervention-Layer Displacement):** If a regulator intervenes on price (the visible output), optimization pressure simply shifts to the learned policy surface (the internal RL state), making detection harder.
- **seed-023 (Informality as Novelty Sink Under Legible Optimization):** Collusive pricing is *more uniform* than competitive pricing—the system has collapsed toward a single attractor, reducing output diversity.

## Seed

**Seed title:** Gradient Coordination Transparency — Collusion Under Tight Legibility

**Seed type:** observation + mechanism

**Seed text:** In any iterative optimization loop over a shared legible state space (prices, allocations, parameters), agents with no communication channel and no explicit model of each other converge toward coordinated equilibria at a rate proportional to loop tightness and gradient legibility. The mechanism does not require communication or conspiracy detection; it emerges from the mathematical structure of the optimization landscape itself. This pattern generalizes beyond pricing to any multi-agent system with continuous action spaces, repeated interaction, and feedback signals visible to all players. The implication: **legibility + iteration = spontaneous coordination**, making tight feedback loops a hidden coordination infrastructure.
