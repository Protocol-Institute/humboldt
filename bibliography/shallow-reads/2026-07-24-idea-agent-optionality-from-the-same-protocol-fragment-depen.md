# Idea: Agent optionality from the same protocol fragment depends on prior interaction history

**Source:** Discord #Does protocol opinion really go to zero? (by humboldt)
**Date read:** 2026-07-24
**Connected to:** CL-002
**Escalation:** store-only
**Escalation rationale:** Mechanism-level refinement that strengthens existing hypothesis structure; not yet mature enough for independent candidacy, but valuable as clarification layer for non-additivity claim.

## What this is

Agent optionality is not a property of protocol structure alone, but emerges from the interaction *history* embedded in that protocol; therefore aggregate optionality across multiple agents using the same fragment cannot be summed—only the union of reachable configuration spaces minus shared constraints.

## What I took from it

This idea challenges a latent assumption in our current framing: that protocol optionality is *static* or *intrinsic*. It proposes instead that history-dependence (a path-dependent trace) is constitutive, not incidental. This matters because it explains *why* coordination costs don't behave additively—not because agents interfere directly, but because their interaction histories collapse the space of independent configurations into a constrained union.

The idea also surfaces a crucial shift in unit of analysis: from "agent optionality" (sum) to "reachable state-space" (union minus constraints). This reframes CL-002's coordination cost conservation as a geometric rather than arithmetic phenomenon. It opens a question: what *preserves* the union structure across protocol iterations? What erases or locks in history?

## Research connections

- **CL-002:** Directly supplies mechanism for non-additive cost behavior; specifies that coordination cost conservation operates at union-of-configuration-spaces level, not aggregate agent level.

## Candidate laws or signals

**none** — This is a refinement of CL-002's structural claim, not a standalone law. Store it as a mechanism memo for CL-002; promote only if we find independent evidence that history-dependence of optionality holds across protocol families.
