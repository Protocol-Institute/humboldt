# Online Learning in Stackelberg Security Games with Adaptive Attacker Sequences and Time-Varying Attack Intensities

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.01703
**Date read:** 2026-09-02
**Connected to:** L-009, L-001
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** [blank]

## What this is

A game-theoretic learning paper deriving no-regret algorithms (√T regret bound) for a defender in repeated Stackelberg security games where attackers adapt their target selection and attack intensity over time. The work formalizes the defender's optimization as a mixed-integer linear program and integrates it with Follow-the-Perturbed-Leader under full-information feedback.

## What I took from it

This is a competent algorithmic contribution within the security games domain, but it does not address the catastrophic risk dynamics that L-009 (Catastrophic Risk Cancellation in Symmetric Racing Protocols) is designed to capture. The paper assumes a single well-modeled defender with access to exact oracles and full-information feedback — a setting where optimization pressure is *transparent and legible*. It does not engage with what happens when multiple defenders race to deploy incompletely-understood security strategies, when the cost of first-mover disadvantage concentrates risk asymmetrically, or when verification of attack success/failure cascades across jurisdictions with misaligned incentives.

The triage note invokes L-009 and L-001, but the paper's concern is algorithmic convergence under adaptive adversaries, not the *dynamics of protocol adoption under racing pressure* or *ossification under deployment lock-in*. No mechanism addressed here — legible oracle access, full feedback, no deployment lag — maps onto the conditions where those laws would activate.

## Research connections

- **L-001:** No engagement with adoption pressure or modification difficulty; the security game formulation is static.
- **L-009:** Does not model symmetric racing, concentrated prizes, or asymmetric cost distribution across competitors.
- **seed-073 (Correlated Failure Under Proxy Consensus):** Tangentially relevant if defenders converge to the same mixed strategy; not explored.

## Seed

**Seed title:** none
