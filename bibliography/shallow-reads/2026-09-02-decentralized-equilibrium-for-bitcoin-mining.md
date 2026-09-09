# Decentralized Equilibrium for Bitcoin Mining

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2604.06092
**Date read:** 2026-09-02
**Connected to:** L-001, L-009
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of Bitcoin mining protocol equilibria under decentralized adoption. The paper addresses the known non-equilibrium of Nakamoto's original protocol (Eyal & Sirer's selfish mining result) and investigates whether an incentive-compatible equilibrium can be sustained when all participants behave strategically.

## What I took from it

This is competent domain-specific work on protocol incentive alignment, but it does not sustain a generalizable law or mechanism absent from the current inventory. The core question — whether a decentralized protocol can be equilibrium-stable under strategic play — is directly addressed by L-001 (Protocol Ossification Under Adoption Pressure) and L-009 (Catastrophic Risk Cancellation in Symmetric Racing Protocols). The paper appears to be a narrow resolution attempt within game-theoretic foundations rather than an investigation of how protocols *actually degrade* under real adoption, scaling, or enforcement conditions.

The selfish-mining equilibrium literature has already established that Nakamoto's protocol is exploitable; this work likely formalizes corrective equilibria or boundary conditions. This is important for Bitcoin specifically but does not appear to generalize a mechanism about how verification/execution hardness asymmetry, metric capture, or coordination cost conservation operates across protocol classes — which is where the new nature framework concentrates.

## Research connections

- **L-001:** Directly touches protocol ossification, but from the equilibrium-theoretic angle rather than the adoption-pressure and modification-difficulty angle that L-001 emphasizes.
- **L-009:** Addresses symmetric racing (mining competition) and concentrated prizes, but likely focuses on individual equilibrium strategy rather than the catastrophic risk cancellation mechanism (where symmetric racing produces systemic failure modes).
- **L-002 (Hardness Asymmetry):** Mining involves verification vs. execution, but paper likely remains at the game-theoretic level rather than cost structure generalization.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
