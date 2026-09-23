# Learning How Much to Collaborate: Difficulty-Aware Topology Selection for Multi-Agent Code Generation

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.13890
**Date read:** 2026-09-22
**Connected to:** L-010, seed-144
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study on multi-agent code generation showing that communication topology effectiveness varies nonmonotonically with problem difficulty, and proposing a learned selector (DATS) to switch topologies adaptively. The work evaluates five topologies across 614 problems, finding that hierarchical collaboration yields 2.4 points on easy problems but 21.1 points on hard ones, at a constant 10x token cost.

## What I took from it

The paper documents a real instantiation of L-010 (Coordination Adoption Nonmonotonicity): agents' willingness to adopt more expensive coordination structures is sensitive to environmental pressure (problem difficulty), not uniform. The result is intuitive but mechanistically underdeveloped — the paper does not explain *why* hierarchy becomes beneficial only under difficulty stress, nor does it investigate whether this threshold is predictable from first principles or merely from post-hoc regression.

The adaptive selector itself (DATS) is a pragmatic response to the nonmonotonicity, but it exemplifies seed-144 (Informality as Coordination Cost Refuge): when formal coordination becomes optional, agents will revert to cheaper structures under low-stress conditions. The paper shows the boundary empirically but does not theorize what determines whether that boundary is stable, reversible, or subject to path dependence.

## Research connections

- **L-010:** Direct confirmation that coordination adoption is nonmonotonic in task difficulty; provides empirical grounding but no mechanism for predicting the threshold.
- **seed-144:** Demonstrates cost-driven abandonment of formal coordination under low-stress conditions; implies coordination cost refuge as a rational equilibrium, not a failure mode.

## Seed

**Seed title:** Coordination Structure Elasticity Under Difficulty Variance

**Seed type:** observation

**Seed text:** In multi-agent systems performing heterogeneous tasks, agents will oscillate between low-cost and high-cost coordination structures depending on task difficulty, not task type. The elasticity of this oscillation (how sharp the threshold, how reversible the choice) may be determined by the cost of topology switching and the variance of difficulty signals. This suggests that systems designed with high switching costs or noisy difficulty signals will lock into suboptimal topologies — a case of L-005 (Gall Generalization) operating on the coordination layer itself.
