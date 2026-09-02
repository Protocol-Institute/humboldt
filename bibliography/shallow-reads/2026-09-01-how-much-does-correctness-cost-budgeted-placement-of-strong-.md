# How Much Does Correctness Cost? Budgeted Placement of Strong Correctors in a Weak Multi-Agent Swarm

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.09765
**Date read:** 2026-09-01
**Connected to:** L-004, seed-045
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An optimization paper modeling the cost-benefit placement of "oracle correctors" (high-confidence agents) in a weak swarm consensus system. The work proves that submodularity holds across oracle placement problems even with heterogeneous corrector strength, enabling greedy approximation guarantees. The domain is multi-agent consensus; the contribution is primarily technical (approximation bounds for a constrained placement problem).

## What I took from it

The paper formalizes a real tension—correctness requires resources, and those resources face diminishing returns—but does not examine how this constraint reshapes the protocol ecology itself. The submodularity result is clean but domain-local: it says *how much* correctness costs to purchase in a fixed consensus topology, not *what agents do* when correctness becomes expensive or scarce.

The work does not engage with L-004 (Goodhart Generalization) in the reverse direction: it assumes the oracle provides ground truth and asks where to place it for efficiency. It does not ask whether swarms under budget pressure develop compensatory metrics that *appear* correct but diverge from the oracle's signal—the actual mechanism by which metric capture would operate in decentralized systems. Similarly, seed-045 (intelligence-entropy monotonic disorder) is cited in the triage but the paper measures coherence via matrix inversion, not entropy dynamics or disorder accumulation. No treatment of how swarms behave when correction is withheld or when the cost signal itself becomes gamed.

## Research connections

- **L-004:** The paper assumes oracle correctness is exogenous and costless to verify; does not model how swarms optimize when ground truth itself becomes a computable proxy under budget constraints.
- **seed-045:** Measures coherence but not entropy or disorder accumulation; no evidence that correctness placement prevents or accelerates disorder in the agent belief landscape.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
