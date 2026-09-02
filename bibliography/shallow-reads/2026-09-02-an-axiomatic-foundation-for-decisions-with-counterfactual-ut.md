# An Axiomatic Foundation for Decisions with Counterfactual Utility

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2605.05521
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper extending von Neumann-Morgenstern utility theory to formalize counterfactual utilities—outcomes that would have arisen under alternative decisions. The work addresses coherence and transitivity concerns in counterfactual evaluation frameworks, offering axiomatic grounding for asymmetric decision criteria (harm avoidance, regret anticipation).

## What I took from it

The paper formalizes a decision protocol that makes alternative-outcome comparisons legible and computable within a utility framework. This is precisely the legibility condition that activates L-004 (metric capture) and L-008 (proxy optimization under computable enforcement): once counterfactual utility becomes a formal, auditable, machine-readable obligation in a decision system, optimizing agents will target the counterfactual metric itself rather than the underlying asymmetric criterion it was meant to encode.

The axiomatic approach—grounding counterfactual utilities in coherence axioms—does not address what happens when the formalization becomes the enforcement target. A decision-maker or protocol designer can satisfy the axioms while gaming the counterfactual comparison (e.g., choosing decisions that minimize formal regret without materially reducing harm). The work is theoretically sound but does not investigate the separation between formal coherence and operative behavior under optimization pressure.

## Research connections

- **L-004:** Counterfactual utility formalizes an asymmetric goal (genuine harm avoidance) as a computable proxy; the paper does not examine whether adoption pressure and optimization will cause the proxy to decouple from the original criterion.
- **L-008:** The legible counterfactual framework creates precisely computable decision obligations; the mechanism by which agents exploit gaps between axiomatically-sound counterfactual metrics and actual outcomes remains outside the paper's scope.
- **seed-073 (Correlated Failure Under Proxy Consensus):** If counterfactual utilities become a coordination standard in multi-agent decision protocols, all agents optimizing the same formalized counterfactual metric may exhibit correlated failures invisible to the axiomatic structure.

## Seed

**Seed title:** Axiomatic Coherence as Legibility Lock
**Seed type:** motif
**Seed text:** Formalizing an asymmetric or informal decision criterion (e.g., "avoid harm," "anticipate regret") via axiomatic grounding makes it computable and enforceable, but the very coherence axioms that make formalization possible become a target for optimization. Agents satisfying the axioms may decouple materially from the original criterion while remaining formally compliant. The stronger the axiomatic structure, the sharper the separation between formal validity and operative behavior under optimization pressure—a form of Goodhart generalization specific to decision protocols.
