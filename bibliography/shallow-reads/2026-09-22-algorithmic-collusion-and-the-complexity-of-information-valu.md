# Algorithmic Collusion and the Complexity of Information-Value-Free Equilibria

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.22757
**Date read:** 2026-09-22
**Connected to:** L-002, L-009, seed-138
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper examining the computational complexity of information-value-free correlated equilibria (IVF(C)CEs) — equilibria where players cannot extract value from recommendation signals — in succinct games. The work extends prior results on algorithmic collusion regulation from explicit normal form to compact representations of strategic interaction.

## What I took from it

The paper addresses a real constraint on coordination protocols: when information is rendered legible enough to regulate (verifiable recommendations), strategic agents face a choice between accepting the recommendation or committing to independent action. IVF equilibria formalize this as a refinement — equilibria robust to agents who ignore coordination signals entirely.

This is relevant to **L-009** (Catastrophic Risk Cancellation in Symmetric Racing Protocols) insofar as it characterizes equilibria under information constraints, but the work is primarily a complexity classification exercise rather than a mechanism explanation for why protocols fail under racing pressure. The paper confirms that correlated equilibrium computation remains tractable under certain restrictions, but does not investigate the conditions under which legible coordination signals *themselves* become weaponized or how agents discover channels that escape the IVF constraint. It is a regulatory modeling contribution, not a law-shaping one.

The connection to **seed-138** (Intent Legibility as Coordination Target Displacement) is suggestive but underdeveloped here: the IVF refinement assumes intent can be made unambiguous enough that commitment to fixed action is credible, but does not explore what happens when agents have incentive to *misrepresent* their commitment or when the legibility itself becomes the site of strategic manipulation.

## Research connections

- **L-002 (Hardness Asymmetry):** The paper shows IVF equilibria can be computed in polynomial time in explicit games but examines complexity in succinct games — relevant as boundary probe, but does not address asymmetry in verification vs. execution cost.
- **L-009 (Catastrophic Risk Cancellation):** Tangentially relevant — examines equilibrium constraints under information limits, but does not model racing or concentrated payoff structures.
- **seed-138 (Intent Legibility as Coordination Target Displacement):** The IVF refinement depends on credible commitment to *fixed* action; if intent legibility becomes the target of optimization, agents may fake commitment. Not explored here.

## Seed

**Seed title:** Coordination Legibility as Commitment-Evasion Surface
**Seed type:** motif
**Seed text:** In protocol systems where correlated equilibria are regulated by requiring agents to make payoff-matching commitments to fixed actions independent of coordinator recommendations (information-value-free constraints), the constraint does not eliminate coordination — it relocates the coordination surface to the credibility and verifiability of commitment itself. Strategic agents facing IVF refinements may exploit asymmetries in commitment verification, signal ambiguity about their own state, or invest in legible-but-false commitment signals rather than abandoning coordination entirely. The generalization: making a coordination channel formally illegible (by enforcing IVF) does not reduce total coordination; it migrates the coordination cost to the layer of commitment representation and authentication.
