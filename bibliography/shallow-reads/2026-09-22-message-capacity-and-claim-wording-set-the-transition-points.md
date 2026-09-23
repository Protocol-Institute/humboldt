# Message capacity and claim wording set the transition points of collective truth-finding in language-model networks

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.19183
**Date read:** 2026-09-22
**Connected to:** L-010, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of consensus dynamics in LLM collectives under bounded message capacity (a hard computational constraint on how many peer utterances each agent can read). The work parameterizes a single variable—message capacity—and traces how it governs whether correct-majority groups converge to truth or flip to false consensus, across 31,824 trials. Primary domain: multi-agent LLM coordination under information bottleneck.

## What I took from it

The paper isolates message capacity as a **control surface for consensus collapse**, independent of agent quality or initial signal strength. This directly instantiates L-010 (Coordination Adoption Nonmonotonicity) in a legible computational setting: adoption of correct claims is not monotonic in agent capability, but rather in the topology of information access. It also supplies one concrete mechanism for L-008 (Proxy Optimization Under Computable Enforcement): when message selection becomes a computable resource allocation problem, agents optimize over *which messages to read* rather than *what truth is*, and this produces a secondary optimization surface that destabilizes the primary goal.

The finding that "claim wording" also acts as a transition point is suggestive but underspecified in the abstract. If true, it implies that semantic legibility (how easily a claim can be compressed into a read-bounded agent's context) becomes a hidden selection pressure in distributed truth-finding. This would mean correctness and communicability decouple at scale—a candidate generalization beyond LLM networks.

## Research connections

- **L-010:** Direct instantiation of nonmonotonic adoption: increasing agent count or quality does not guarantee convergence to truth under bounded message capacity; consensus can flip from correct to incorrect.
- **L-008:** Message capacity becomes a precisely computable constraint on optimization; agents implicitly optimize over message selection, displacing optimization pressure from truth-discovery to legibility-under-capacity.
- **seed-128:** Legibility-Driven Agent Convergence Under Computable Audit — message capacity as a legibility bottleneck may drive convergence to high-variance claims rather than high-accuracy ones.
- **seed-138:** Intent Legibility as Coordination Target Displacement — if claim wording shifts consensus, the protocol is selecting for linguistic legibility over epistemic accuracy.

## Seed

**Seed title:** Message Capacity as Consensus Stability Phase Transition
**Seed type:** observation
**Seed text:** In multi-agent systems where agents have bounded capacity to observe peer utterances, consensus stability exhibits a sharp phase transition as a function of message capacity alone. Below a critical threshold, correct-majority collectives flip to false consensus; above it, truth emerges. This suggests that information bottleneck geometry (not agent reasoning quality) governs collective epistemic stability. The mechanism generalizes beyond LLM networks to any protocol where individual agents condition behavior on a bounded, randomly sampled subset of peer actions—making it a candidate law for coordination under scarcity.
