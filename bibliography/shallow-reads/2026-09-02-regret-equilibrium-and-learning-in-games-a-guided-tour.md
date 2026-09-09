# Regret, equilibrium, and learning in games: A guided tour

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.09389
**Date read:** 2026-09-02
**Connected to:** none
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A survey/tutorial paper on learning dynamics in multi-agent game-theoretic settings, structured around regret minimization and equilibrium convergence. It bridges single-agent sequential decision problems with multi-agent interaction, synthesizing results on how learners adapt in unknown, non-stationary, and adversarial environments.

## What I took from it

This is a methodological and conceptual anchor rather than a primary source generating novel laws. The framing is useful as context: it establishes that learning in games produces convergence to equilibria under specific conditions (full information, stationary play, etc.) — but the survey itself does not interrogate what happens when these conditions fail or when protocol systems embed learning agents with asymmetric information, computable legibility, or misaligned objectives.

The paper's treatment of "non-stationary and possibly adversarial" environments is where protocol-systems research should listen closely: game-theoretic learning theory typically assumes agents optimize according to stated objectives. It does not address what happens when the environment itself is a protocol (with boundary conditions, audit visibility, or metric capture) that modifies agent incentives *during* learning. This is closer to L-008, L-012, and L-014 territory — but the survey does not explore those displacement effects.

## Research connections

- **L-004 (Goodhart Generalization):** The survey covers equilibrium stability under metric optimization, but does not examine proxy capture in safety-critical or governance protocols where the metric itself becomes the target.
- **L-008 (Proxy Optimization Under Computable Enforcement):** Learning in games assumes agents see the full problem; this survey does not address how computable legibility reshapes the learning surface itself.
- **seed-077 (Metric-Induced Preference Ratcheting in Adaptive Systems):** Learning agents can exhibit preference drift under repeated metric exposure; the survey treats preferences as fixed.
- **seed-073 (Correlated Failure Under Proxy Consensus):** Multi-agent learning toward consensus equilibria is covered; correlated failure modes under shared proxies are not.

## Method note

This survey highlights a methodological gap: game-theoretic learning theory is a well-developed formal apparatus, but it operates *inside* an assumed protocol structure. For the new nature research agenda, the lever should be: how does embedding a learner *within* a protocol with computable verification, asymmetric information, or metric-driven enforcement change the learning dynamics themselves? The survey is a necessary reference baseline for defining what *doesn't* happen in idealized settings — which clarifies where protocol-specific effects should appear. Future work should treat the protocol boundary (audit visibility, formalization, cost structure) as a parameter of the learning problem, not a fixed container.
