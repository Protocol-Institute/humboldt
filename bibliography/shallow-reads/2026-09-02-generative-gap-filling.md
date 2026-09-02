# Generative Gap Filling

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.21401
**Date read:** 2026-09-02
**Connected to:** L-004, seed-026
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A legal studies paper examining how courts fill gaps in incomplete contracts through judicial gap-filling doctrine. The work challenges the conventional assumption that sparse textual evidence forces judges to rely on unstructured methods (commercial defaults, policy preference), proposing instead that generative methods—presumably including predictive or LLM-assisted approaches—can recover latent contractual intent from existing text.

## What I took from it

The paper is fundamentally about **proxy substitution at a boundary of incommensurability**: when text fails to express intent, courts have historically resorted to ad-hoc external methods. The introduction of generative gap-filling (likely LLM-based contract completion or intent inference) attempts to replace that unstructured residual with a computable, legible process. This is a *formalization of the unformalizable*—a classic Goodhart trigger.

However, the paper appears to operate within a single domain (contract law) without testing whether gap-filling generalization holds across protocol systems. The mechanism proposed—using statistical inference on textual fragments to recover intent—may work locally for contracts, but the paper does not explore the dynamics when gap-filling becomes the primary coordination surface (as it would in automated protocol systems). It also does not address what happens when the gap-filling proxy itself becomes a target for strategic behavior or when the assumptions underlying generative inference diverge from actual party intent under adversarial conditions.

The work confirms L-004's premise (formalization of unmeasurable goals invites capture), but does not test whether gap-filling protocols exhibit the instability patterns predicted by L-004 or L-008.

## Research connections

- **L-004 (Goodhart Generalization):** Gap-filling converts an unmeasurable (actual intent) into a computable proxy (generated contractual language); under adversarial pressure, parties will learn to write contracts that generate favorable completions rather than express true intent.
- **L-008 (Proxy Optimization Under Computable Enforcement):** If contract gaps become filled by legible generative methods, optimization pressure shifts from negotiating intent to constructing text that survives gap-filling favorably.
- **seed-026:** Direct connection noted by triage; gap-filling as formalization of an incommensurable boundary.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** If generative gap-filling is trained on historical contracts with systematic imbalances (e.g., institutional vs. individual parties), it will systematically mispredict intent for novel asymmetric pairs.

## Seed

**Seed title:** Formalization of Intent Residuals — Generative Gap-Filling as Protocol Boundary Crystallization

**Seed type:** motif

**Seed text:** When protocol systems (contracts, specifications, governance rules) contain irreducible gaps—points where formal language fails to capture the actual bargain or intent—those gaps have historically remained unstructured coordination surfaces (informal negotiation, judicial discretion, custom). Introduction of computable gap-filling (generative models trained on historical examples) formalizes the boundary itself, converting discretionary residual into a legible, optimizable target. This triggers two opposing pressures: (1) reduction in interpretive conflict through predictable completion, and (2) strategic divergence between written intent and text-optimized contracts designed to exploit gap-filling patterns. The mechanism generalizes wherever protocols must accommodate incommensurable human intent within computable systems—specifications, governance charters, resource allocation rules. The question is whether formalization of the residual eliminates ambiguity or merely relocates it upstream to the gap-filling model itself.
