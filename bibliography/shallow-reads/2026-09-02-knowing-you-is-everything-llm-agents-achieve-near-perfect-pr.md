# Knowing You Is Everything: LLM Agents Achieve Near-Perfect Profile-Consistent Reaction Prediction in Social Media Simulation

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.07498
**Date read:** 2026-09-02
**Connected to:** L-010, seed-049
**Kind:** benchmark / empirical validation
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper testing whether persona-conditioned LLMs can predict individual social media reactions (like/dislike) with high accuracy across profile completeness and model configurations. The work measures generalization failure on novel content and validates the feasibility of LLM agents as simulators for both risk assessment and recommender system testing.

## What I took from it

This is a competent demonstration that **legible behavioral profiles enable high-fidelity agent simulation**, but it does not theorize the mechanism or explore the downstream consequences that generalize beyond social media. The paper confirms that when individual preference structure is sufficiently formalized (persona prompt + post content as legible input), predictive accuracy approaches ceiling — but it stops at the empirical result without investigating what happens when such predictability becomes operational in a system with feedback loops, strategic adaptation, or multi-agent coordination pressure.

The work is *adjacent* to L-010 (Coordination Adoption Nonmonotonicity) and seed-049, but only in the sense that it demonstrates a precondition: that individual behavior under profile legibility is *highly* predictable. It does not test whether coordination signals degrade or bifurcate adoption when agents know they are being modeled, or whether the predictability itself becomes a target for strategic deception. The paper is a tool validation, not a law inquiry.

## Research connections

- **L-012 (Intervention-Layer Displacement):** The paper demonstrates that when social media reactions become precisely computable from profile data, the system is now ready for legible optimization — but does not study where the optimization pressure relocates.
- **seed-069 (Transparency-Legibility as Trust Proxy Substitution):** High prediction accuracy may create a false sense of platform understanding, substituting legible behavioral models for actual user autonomy or preference stability.
- **seed-128 (Legibility-Driven Agent Convergence):** The near-perfect accuracy suggests agents conditioned on the same profile will converge to identical outputs — a precondition for downstream coordination anomalies not explored here.

## Seed

**Seed title:** Profile Legibility as Coordination Target Under Simulation Transparency

**Seed type:** question

**Seed text:** When individual behavioral profiles become formalized and legible enough to support high-fidelity agent simulation, what prevents strategic agents (users, platform actors, coordinated groups) from treating the profile itself as an optimization target rather than a stable model of preference? In social systems where simulation fidelity becomes public or discoverable, does the predictability of one's own profile collapse as agents alter behavior to evade or manipulate the model? Does this create a ratchet where only profiles that remain *opaque to formalization* retain stability — and if so, does the system progressively lock out legitimate coordination signals in favor of unintelligible behavior?
