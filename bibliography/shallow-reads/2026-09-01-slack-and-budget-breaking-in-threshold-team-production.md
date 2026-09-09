# Slack and Budget Breaking in Threshold Team Production

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.06197
**Date read:** 2026-09-01
**Connected to:** L-006, L-003
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of threshold team production under public commitment constraints. The paper models how slack (excess share opportunities beyond the minimum needed to complete a task) affects coalition incentives to delay or sabotage, and characterizes the fee structures required to prevent budget-breaking by coordinated withholding.

## What I took from it

This work instantiates L-006 (Coordination Cost Conservation) at the mechanism design level: the paper shows that when you formalize the verification of contribution (public commitment of shares), you do not eliminate the coordination problem — you relocate it. The problem shifts from *coordination to produce* to *coordination to withhold*. The slack parameter (Δ) becomes the new locus of strategic behavior. The analysis is tight enough to suggest that protocols cannot reduce total strategic vulnerability; they can only change its shape and location.

This also touches L-003 (Formalization Ratchet): the requirement for public, verifiable commitment of shares formalizes what might otherwise be informal signaling or trust, but this formalization creates a new surface for exploitation (the sabotage set becomes mathematically legible and thus targetable). The cheapest sabotage set is now a computable quantity, which confirms the direction of L-008 (Proxy Optimization Under Computable Enforcement) — when obligations become precisely computable, they become targetable by rational optimizers.

However, the paper does not generalize beyond threshold systems and does not offer a mechanism absent from existing game-theoretic inventory. It is a competent instantiation, not a breach.

## Research connections

- **L-006:** Slack dynamics confirm that formalizing one coordination layer (verifiable shares) does not reduce coordination cost — it relocates it to the withholding coalition problem.
- **L-003:** Public commitment requirement formalizes what was informal; formalization creates new legibility and thus new exploitation surfaces.
- **L-008:** The analysis makes the cheapest sabotage set computable, confirming that precise enforcement legibility enables rational optimization against the mechanism.
- **seed-016 (stopping-rule-substitution):** Slack creates a substitution point: completing the task vs. triggering delay payoffs; the protocol must price this boundary.

## Seed

**Seed title:** Sabotage Legibility Ratchet in Threshold Protocols

**Seed type:** observation

**Seed text:** In threshold team production under public commitment, formalizing the verification function does not eliminate coalition exploitation — it renders the minimum sabotage set (the cheapest withholding coalition) mathematically computable. Protocol designers must then price against this computable quantity, which forces the fee structure to encode a model of the adversary's cost. This creates a ratchet: as protocols become more formally specified and verifiable, the strategic vulnerability surface becomes more legible, and thus requires ever-more-refined defensive pricing. The total coordination cost is conserved, but now must be paid continuously in mechanism design overhead rather than absorbed in informal trust. This may be a special case of L-006 under conditions of high formalization and public auditability.
