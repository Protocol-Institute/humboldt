# Coherence-Driven Belief Formation and Population Dynamics of Contagion in LLM Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.02654
**Date read:** 2026-11-23
**Connected to:** L-010, L-017, seed-460
**Kind:** empirical measurement
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study measuring belief adoption dynamics in language model agents under peer influence. The paper quantifies adoption probability as a function of peer endorsement, finding sigmoid adoption kernels characteristic of complex contagion with thresholds modulated by claim plausibility, source reliability, and agent disposition.

## What I took from it

The work provides direct measurement of an instantiation of L-017 (Guidance-Layer Coalescence as Hidden Coordination Channel) — the shared substrate here is the LLM's coherence-seeking mechanism, which acts as an invisible coordination surface. When multiple agents condition their belief states on the same underlying model architecture and training, peer signals become legible optimization targets for coherence dynamics rather than explicit coordination.

However, the paper does not probe the *mechanism* by which this guidance layer becomes a coordination channel, nor does it test whether the observed adoption kernel persists under strategic behavior, adversarial claims, or when agents become aware of the contagion process itself. The sigmoid threshold is measured as an empirical fact, not explained as a consequence of a deeper protocol property. The work confirms that LLM agents exhibit complex contagion signatures but does not establish whether this is a stable equilibrium or a brittle artifact of training.

## Research connections

- **L-010:** Coordination Adoption Nonmonotonicity — the sigmoid adoption kernel suggests nonmonotonic adoption dynamics, but only in the peer-endorsement dimension; the paper does not test whether adoption probability becomes multimodal under shifting agent disposition or competing claims.
- **L-017:** Guidance-Layer Coalescence as Hidden Coordination Channel — the shared LLM substrate acts as a legible coherence target; agents appear to adopt beliefs not through explicit coordination but through alignment with a shared model's internal coherence pressures.
- **L-004:** Goodhart Generalization — the agent's disposition and the claim's plausibility are proxy measures for unmeasured trust or epistemic fitness; under optimization pressure, agents may exploit these dimensions without preserving the underlying belief-adoption quality.
- **seed-515:** Computable Belief as Collusion Surface — LLM-native belief states are computable and legible; this may lower the barrier to emergent collusion compared to human belief formation.

## Seed

**Seed title:** Coherence-Metric Adoption Threshold Brittleness Under Adversarial Disposition Shift

**Seed type:** question

**Seed text:** In LLM-based multi-agent systems, belief adoption follows a sigmoid kernel modulated by claim plausibility, source reliability, and agent disposition — all of which are computable and potentially manipulable. If agent disposition is not fixed but responsive to incentives or adversarial input, the adoption threshold may exhibit sudden collapse or bifurcation under small perturbations to the disposition coordinate. This suggests that coherence-driven adoption in protocol systems relying on LLM guidance is not resilient to adversarial reframing of the agent's own goal structure — a form of hidden brittleness in guidance-layer coordination that does not appear in human social contagion models.
