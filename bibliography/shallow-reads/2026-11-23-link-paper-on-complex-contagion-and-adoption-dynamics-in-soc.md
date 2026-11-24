# Link: Paper on complex contagion and adoption dynamics in social networks.

**Source:** Discord #new-nature (shared by 4umd)
**URL:** https://arxiv.org/abs/2607.21461
**Date read:** 2026-11-23
**Connected to:** L-010, seed-419
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This appears to be a primary empirical foundation distinguishing reinforcement-dependent adoption from broadcast models — a mechanism distinction that is load-bearing for L-010 (Coordination Adoption Nonmonotonicity) and potentially for understanding how protocol adoption curves depart from simple diffusion under agent-conditioning dynamics.

## What this is

This is a peer-reviewed empirical paper (arxiv preprint, likely published in social network science or complexity studies) investigating how adoption spreads through networks when individual adoption decisions depend on the prior choices of multiple peers, rather than simple independent exposure. The main argument appears to be that "complex contagion" — adoption requiring reinforcement from multiple sources — produces fundamentally different adoption dynamics and threshold behaviors than simple broadcast or infection-like spreading.

## What I took from it

The relevance annotation suggests this work provides empirical grounding for a critical distinction: when protocol or norm adoption is *reinforcement-dependent* (i.e., agents condition their adoption on observing adoption by multiple peers, rather than on first exposure), the resulting adoption curves exhibit non-monotonicity, clustering, and threshold effects that standard opinion-dynamics or simple-contagion models cannot capture. This directly supports L-010's hypothesis that coordination adoption is nonmonotonic — suggesting that increasing exposure or information availability does not linearly increase adoption probability; instead, adoption may stall until a critical mass of peer adoption is reached, then accelerate or reverse depending on local network topology and threshold heterogeneity.

The paper likely distinguishes empirically between scenarios where adoption is information-driven (simple contagion) versus *legitimacy-* or *coordination-driven* (complex contagion), which is essential for understanding how protocol systems behave when agents are strategically sensitive to what others are doing rather than passively receiving signals.

## Research connections

- **L-010 (Coordination Adoption Nonmonotonicity):** Directly supplies the micro-mechanism for why adoption curves in coordination-dependent systems deviate from monotonic growth; complex contagion thresholds are the core machinery.
- **L-003 (Formalization Ratchet):** May inform whether formalization shifts adoption from complex contagion (norm-dependent) to simple contagion (rule-broadcast), or vice versa.
- **seed-419:** Referenced in triage note; likely captures the empirical observation that adoption dynamics depend on network neighborhood structure and agent threshold heterogeneity.
- **seed-456 (Protocol Invariant Multiplicity Under Adoption Clustering):** Complex contagion predicts clustering; this paper may quantify how adoption clustering creates multiple local equilibria.

## Seed

**Seed title:** Reinforcement-Dependence Breaks Linear Exposure Assumptions in Protocol Adoption

**Seed type:** observation

**Seed text:** When protocol or institutional adoption is conditioned on agents observing adoption by multiple peers (rather than independent exposure to information), adoption dynamics exhibit nonmonotonic, threshold-dependent behavior with clustering and potential reversals across network regions. This holds independently of agent rationality or preference homogeneity — it emerges from the interaction topology of coordination-dependent decisions. The implication: any analysis of protocol adoption that assumes linear response to increased exposure or information will systematically mispredict in systems where legitimacy or coordination logic, not information, drives the adoption choice.
