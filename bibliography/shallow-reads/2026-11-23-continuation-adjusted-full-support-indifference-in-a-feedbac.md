# Continuation-Adjusted Full-Support Indifference in a Feedback Stackelberg Attacker--Defender Attrition Game

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2512.17284
**Date read:** 2026-11-23
**Connected to:** L-009, seed-098
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of finite-horizon attacker-defender contests under strong Stackelberg equilibrium with stagewise feedback and recommitment. The paper shows that successful asset removal breaks classical static defense regularities (coverage need not deter; defenders need not saturate budget or targets) and proposes a continuation-adjustment method that converts multi-period nodes into equivalent static games with shifted payoffs.

## What I took from it

This is a formal treatment of sequential attack-defense races, but it operates entirely within the equilibrium-convergence frame of classical game theory. The core contribution—that dynamic attrition games can be decomposed into static equivalents via payoff shifting—is elegant but does not engage with the protocol-level phenomena we track: emergence of unintended equilibria, verification-execution asymmetries, legibility-driven optimization pressure, or the structural vulnerabilities of computable enforcement signals.

The paper does not address how the formalization itself (rendering attack sequences and coverage as computable, legible quantities) alters strategic behavior, nor does it examine what happens when the game's rules or payoff structure become visible to and exploitable by agents. It remains a closed-form analysis tool, not an investigation of how protocol design creates new failure modes under realistic adoption and competitive pressure.

## Research connections

- **L-009:** Relates tangentially — competitive racing with asymmetric costs — but does not engage with risk cancellation or the dynamics of first-mover advantage under catastrophic outcome concentration.
- **seed-098:** Mentioned in triage but not substantially developed in the abstract; attacker-defender asymmetry is formalized but not tied to legibility or enforcement structure.
- **seed-515 (Computable Belief as Collusion Surface):** The reduction of attack-defense to computable payoff matrices could enable strategic agents to coordinate around the equilibrium prediction itself, but this is not explored.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Decision:** This is competent technical game theory within a narrow equilibrium frame. It does not present sustained argument about protocol-level regularities, does not challenge or extend any law under accumulation, and introduces no mechanism absent from our current inventory. Store as shallow reference for future GT-formalism cross-check; no escalation warranted.
