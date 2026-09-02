# Proportional Committee Elections with Positive and Negative Votes

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2503.01985
**Date read:** 2026-09-02
**Connected to:** L-003, seed-029
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper extending proportional representation voting mechanisms to allow negative votes alongside positive ones. The work proposes two interpretations of negative votes (as explicit rejections vs. as dual-preference expressions) and develops axiomatically sound committee selection algorithms for each. Primary domain: computational social choice and voting theory.

## What I took from it

This is a competent domain-specific extension of voting protocol design, but it does not engage with the dynamics of formalization under pressure, protocol ossification, or the institutional costs of expanding expressiveness in coordination systems. The paper treats negative votes as a straightforward addition to the preference elicitation space and develops mechanisms that preserve classical proportionality axioms. 

However, there is a latent tension worth noting: allowing negative votes increases the expressiveness of the preference language, which typically drives formalization pressure (L-003 signal). The paper does not track whether this expressive richness creates new enforcement or interpretation costs, or whether real-world adoption of negative vote mechanisms produces unintended strategic behavior (e.g., preference manipulation via negative signaling). The two competing interpretations of negative votes themselves hint at the formalization-under-pressure dynamic — the protocol designers had to choose between two conceptually distinct formal models, each with different proportionality guarantees. This is a micro-instance of L-003's mechanism, but the paper does not frame it that way.

## Research connections

- **L-003 [The Formalization Ratchet]:** The need to formally disambiguate two competing interpretations of negative votes exemplifies how expressiveness pressure drives formalization choices, but the mechanism is latent rather than examined.
- **seed-029:** Not in current inventory — likely refers to proportionality axioms and exemplar-vs-rule tension in committee selection, which this paper instantiates but does not interrogate.

## Seed

**Seed title:** Expressiveness-Disambiguation Lock in Voting Protocol Formalization

**Seed type:** observation

**Seed text:** When voting protocols add expressive dimensions (e.g., negative votes), protocol designers must formally disambiguate competing interpretations of new preference signals. Each disambiguation choice locks in different equilibrium behaviors and fairness guarantees. The proliferation of axiomatically sound but semantically distinct formalizations may itself create coordination cost (agents and implementers must agree on which interpretation governs) that is not recovered by gains in expressiveness. This suggests a cost-hidden pathway through which L-003 operates: formalization under expressiveness pressure produces multiple valid formal solutions, forcing an additional meta-level coordination choice.
