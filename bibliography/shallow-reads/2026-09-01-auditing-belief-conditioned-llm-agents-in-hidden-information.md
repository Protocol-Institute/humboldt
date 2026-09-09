# Auditing Belief-Conditioned LLM Agents in Hidden-Information Social Deduction Games

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.10814
**Date read:** 2026-09-01
**Connected to:** L-011, seed-049
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical tool paper presenting an auditing framework for LLM agents in hidden-information multi-agent games (Werewolf). The work develops structured logging of belief states and belief-action deviations to make agent reasoning legible in high-variance environments, supporting post-hoc case review and strategy refinement.

## What I took from it

The paper is methodologically sound but remains a domain-specific engineering contribution. It does not present a sustained theoretical argument about protocol dynamics, nor does it challenge or extend any of the current law inventory. The auditing apparatus itself—maintaining external belief state, logging deviations, supporting offline improvement loops—is a competent solution to the legibility problem in multi-agent RL evaluation, but the mechanism of action is instrument-design, not a regularity about how protocolized systems behave under stress or at scale.

The connection to L-011 (Causal Detachment as Stable Protocol Equilibrium) is suggestive but underdeveloped: the paper observes that agent actions sometimes deviate from logged beliefs, but does not investigate whether this is a *stable equilibrium condition* in belief-conditioned systems or merely a performance artifact. The work lacks the cross-domain pattern-seeking and mechanism proof required to warrant escalation.

## Research connections

- **L-011:** The paper documents belief-action deviation in hidden-information settings, but does not establish whether this decoupling is functionally stable or pathological—a required distinction for L-011 induction.
- **seed-049:** Implicitly present: agents are reasoning under consensus-like coordination pressure (role inference from partial signals) while decoupled from actual causal states. The paper logs this but does not theorize it.

## Seed

**Seed title:** none

---

**Disposition:** File as shallow archive. Return to if future work on L-011 or seed-049 produces evidence that belief-action decoupling persists even after agent training converges, or that it confers strategic advantage in equilibrium.
