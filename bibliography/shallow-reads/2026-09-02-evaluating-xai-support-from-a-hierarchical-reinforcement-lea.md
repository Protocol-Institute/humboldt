# Evaluating XAI Support From A Hierarchical Reinforcement Learning Policy in Human-Agent Collaboration

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.06381
**Date read:** 2026-09-02
**Connected to:** L-012
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical evaluation paper testing whether explanations generated from a learned hierarchical RL policy improve human-agent teaming outcomes in the Overcooked-AI benchmark. The work treats XAI as an intervention layer inserted between agent policy and human partner, measuring effects on task success and human trust/workload.

## What I took from it

This is a clean instantiation of L-012's core mechanism: *when a prediction or decision process is made legible through explanation*, does the locus of optimization pressure shift? Here, the explanation becomes a legible interface—agents may optimize for *explainability* of their hierarchical choices rather than task performance, or humans may shift decision-making authority based on confidence in the explanation rather than ground-truth agent capability.

The work is methodologically sound but operates within the assumption that legibility (via XAI) is unambiguously beneficial. It does not investigate whether the explanation layer itself becomes a target of gaming, whether human reliance on explanations decouples from actual agent reliability, or whether the intervention displaces coordination burden to a different layer (e.g., humans now must interpret which explanation to trust). This is a common blind spot in XAI-for-teaming research: treatment of transparency as orthogonal to protocol dynamics rather than as an active structural element.

The choice of hierarchical policy is notable—subtask explanations are less granular than primitive-action explanations, potentially insulating the protocol from certain legibility-driven failure modes. But the paper does not theorize this tradeoff.

## Research connections

- **L-012:** Intervention-Layer Displacement — inserting XAI as a legible layer may redirect optimization pressure from task performance to explanation plausibility; no evidence presented that this does *not* occur.
- **seed-069:** Transparency-Legibility as Trust Proxy Substitution — explanations may substitute for actual reliability assessment; the paper measures trust post-intervention but not its calibration to true agent performance.
- **seed-072:** Explanation-Marker Decoupling Under Scaled Legibility — hierarchical abstractions allow explanations to be generated at one level while failure modes operate at another; not explored.

## Method note

This work exemplifies a common pattern in applied XAI research: intervention is treated as a unidirectional improvement rather than a structural modification with side effects. Future work in this space should adopt a protocol-dynamics frame: measure not only whether explanations help, but whether they alter the *surface* on which agents optimize, create new coordination failure modes, or displace trust calibration. Benchmarks like Overcooked-AI are valuable for isolating causal effects, but they require instrumentation to detect whether the explanation layer becomes a new site of gaming or decoupling. The field would benefit from explicit testing of negative hypotheses drawn from L-012 and related seeds.
