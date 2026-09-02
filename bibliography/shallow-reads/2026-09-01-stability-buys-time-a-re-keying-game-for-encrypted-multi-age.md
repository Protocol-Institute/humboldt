# Stability Buys Time: A Re-Keying Game for Encrypted Multi-Agent Control

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.12742
**Date read:** 2026-09-01
**Connected to:** L-002, L-007
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic treatment of key rotation in fully homomorphic encrypted multi-agent control systems. The paper models the security game between an honest-but-curious cloud coordinator and persistent adversaries who can harvest decryption noise leaks from the control loop feedback over time, then studies re-keying cadences that maximize operational stability before key compromise.

## What I took from it

The paper is technically sound but domain-constrained. It confirms L-007 (Trust Ratchet in Safety-Critical Protocols) in a narrow setting: the cloud coordinator's trustworthiness accumulates as a function of operational time *without compromise*, and re-keying intervals must balance the operational cost of key rotation against the cryptographic cost of noise leakage over repeated control cycles. The honest-but-curious assumption severely limits generalization — the threat model assumes the coordinator will not actively collude or deceive, which evacuates most coordination risk in distributed governance contexts.

The paper does not engage with how agents *believe* the system remains uncompromised, or how trust signals propagate when compromise is asymmetrically detectable. It treats trust as a binary state (compromised/uncompromised) rather than a distributed epistemic property. This is competent crypto-game theory but does not open new mechanism territory for protocol systems more broadly.

## Research connections

- **L-002 (Hardness Asymmetry):** The verification cost (detecting compromise via noise patterns) is substantially higher than the exploitation cost (harvesting noise), but the paper does not generalize this or measure the actual asymmetry.
- **L-007 (Trust Ratchet):** Confirms that trust in the coordinator accumulates with operational age, but assumes perfect observability of non-compromise—a condition that rarely holds in real distributed systems.
- **L-012 (Intervention-Layer Displacement):** Not engaged; re-keying is a protocol-layer fix, not an intervention that reveals where optimization pressure migrates.

## Seed

**Seed title:** none

---

**Rationale for store-only:** This is a well-executed domain-specific result (encrypted control + game theory), but it does not challenge or extend existing laws, introduce a novel mechanism absent from the inventory, or generalize beyond its cryptographic setting. It provides evidence *for* L-007 in a narrow honest-but-curious regime, but does not discover or test new regularities about protocol stability, adoption, or coordination under adversarial conditions. It belongs in the reference library but does not warrant deep induction.
