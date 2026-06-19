# Online Optimization Algorithms in Repeated Price Competition: Equilibrium Learning and Algorithmic Collusion

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2412.15707
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary theoretical source investigating mechanism (tacit collusion emergence) absent from inventory; pattern generalizes across algorithmic pricing systems; directly challenges competitive market assumptions in protocolized systems.

## What this is

A game-theoretic study of multi-armed bandit (MAB) learning algorithms deployed in repeated pricing competition, investigating whether decentralized online optimization produces competitive equilibria or supra-competitive tacit collusion. The work bridges algorithmic learning theory and industrial organization, examining a fundamental tension in how protocolized agents behave under minimal information constraints.

## What I took from it

This work identifies a structural vulnerability in protocolized competition: algorithms optimizing locally under exploration-exploitation tradeoffs can converge toward collusive outcomes *without explicit coordination*. This is critical because it suggests collusion is not aberrant behavior requiring coordination infrastructure, but an attractor state emergent from standard learning dynamics. The MAB framework is particularly important—these algorithms are information-parsimonious (agents need not model competitors' strategies), making them deployable at scale in real digital markets, yet they still generate supra-competitive pricing.

The theoretical contribution reframes algorithmic collusion from a regulatory anomaly into a predictable consequence of how certain learning algorithms interact in repeated games. This challenges the implicit assumption that transparent, decentralized price-setting by autonomous agents produces competitive outcomes. The mechanism appears to be an interaction between the exploration bonus (which keeps prices elevated during learning) and the coordination-free convergence properties of Nash equilibrium in pricing games.

## Research connections

- **None yet documented:** This appears to be first systematic treatment of MAB-driven tacit collusion in the inventory; relevant to any future law governing emergence of coordination in non-communicating protocolized systems.

## Candidate laws or signals

- **CL-2412.15707-1:** *Collusion-as-attractor in decentralized learning*: Online learning algorithms operating on exploration-exploitation principles in repeated competitive markets converge toward supra-competitive equilibria proportional to the information sparsity constraint and time horizon, absent explicit coordination mechanisms.

- **CL-2412.15707-2:** *MAB-driven price elevation*: Multi-armed bandit algorithms in pricing games produce systematic price inflation during exploration phases that persists into exploitation; magnitude correlates with bandit variance and convergence speed.
