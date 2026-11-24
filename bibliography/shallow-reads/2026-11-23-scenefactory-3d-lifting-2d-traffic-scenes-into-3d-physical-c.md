# SceneFactory-3D: Lifting 2D Traffic Scenes into 3D Physical Counterfactuals for Scalable Physically Grounded Safety Evaluation

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.02874
**Date read:** 2026-11-23
**Connected to:** none
**Kind:** tool/benchmark
**Escalation:** store-only

## What this is

A GPU-batched physics simulator for autonomous vehicle safety evaluation that grounds multi-agent traffic dynamics in wheel-level tire-road interface physics rather than kinematic approximations. The work addresses the gap between prescribed behavioral models and physical realism in scalable driving simulators.

## What I took from it

This is a competent engineering contribution to safety evaluation infrastructure, but it does not engage with the question of how safety protocols themselves behave under adoption pressure, formalization, or optimization. The paper improves the fidelity of *counterfactual execution* within a fixed evaluation regime, but does not examine how safety evaluation protocols ossify, how metrics capture safety intent, how distributed safety governance breaks down, or how physical realism in simulation couples to trust ratcheting in deployed systems.

The work is orthogonal to protocolized artificial systems research. It is a measurement tool, not an investigation of measurement protocol dynamics.

## Research connections

- none

## Seed

**Seed title:** none

---

**Decision:** Store only. This is a benchmark/tool paper with high technical quality and clear domain utility (AV safety simulation), but it presents no sustained theoretical or empirical argument about *protocol dynamics*, introduces no novel mechanism of coordination failure or optimization pressure, and does not generalize beyond its specific simulator design problem. No escalation warranted.
