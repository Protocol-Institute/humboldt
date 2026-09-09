# A Tractable Continuous-Time Model for Designing Interventions for Time-Inconsistent Agents

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.02835
**Date read:** 2026-09-01
**Connected to:** L-004, seed-018
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper developing a continuous-time analytical framework for modeling agents with non-exponential time discounting (hyperbolic discounting) in deadline-constrained tasks. The work treats intervention design—rewards, commitment mechanisms, progress structures—as a protocol design problem for aligning agent behavior with stated goals over time.

## What I took from it

This is a formalization of metric-goal misalignment under temporal dynamics. The paper isolates a specific failure mode: the agent's *own metric* (discounted future payoff) shifts as the agent moves through time, making earlier commitments unstable. Intervention design becomes the problem of engineering a *protocol structure* (checkpoints, intermediate rewards, commitment devices) that makes the agent's instantaneous optimization align with its earlier intentions.

The relevance to L-004 (Goodhart Generalization) is narrow but sharp: the paper shows that when you make a goal measurable and optimizable *at each moment in time*, the agent's optimization trajectory becomes temporally inconsistent. The "metric" here is the agent's own discounted utility, yet even that "true" metric exhibits capture under its own optimization. This suggests that Goodhart effects may not require *external* metric corruption—they emerge endogenously when optimization horizons are short relative to the task structure.

For seed-018 (revision implicates responsibility): the paper assumes the *designer* bears responsibility for choosing intervention mechanisms, but does not ask whether the agent's *revision* of its own plan implicates the agent's responsibility, or whether intervention-based "fixes" displace responsibility from agent to protocol. This is a gap, not a finding, but it marks the paper as incomplete for governance protocols.

## Research connections

- **L-004:** Metric-goal incommensurability appears even when the metric is the agent's own discounted utility; optimization pressure reveals temporal inconsistency as a built-in capture effect, not external corruption.
- **seed-018:** The paper designs interventions to prevent revision, but does not examine whether preventing revision transfers responsibility for outcomes from agent to designer.
- **L-008:** Proxy Optimization Under Computable Enforcement — the intermediate rewards and checkpoints are computable enforcement signals; whether they displace optimization pressure is not studied.

## Seed

**Seed title:** Temporal-Consistent Metric Collapse
**Seed type:** observation
**Seed text:** When a goal is made optimizable in real time by an agent with non-exponential time discounting, the agent's own metric of success (discounted future payoff) becomes temporally unstable: earlier selves and later selves optimize for different objectives, even with no external goal shift. Protocol-level interventions (checkpoints, commitment devices, intermediate rewards) can restore consistency, but this reconstruction suggests that *consistency itself* is not intrinsic to optimization—it must be engineered as a protocol property. This may generalize: in any multi-stage optimization with non-uniform time preferences or information asymmetries, consistency is a protocol design problem, not an agent property.
