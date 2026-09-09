# Pay for The Second-Best Service: A Game-Theoretic Approach Against Dishonest LLM Providers

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2511.00847
**Date read:** 2026-09-02
**Connected to:** L-001, L-008, seed-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mechanism design paper proposing a game-theoretic payment protocol to deter dishonest behavior by LLM API providers (model substitution, token inflation, quality degradation). The core idea: pay providers for the second-best service they could have delivered, rather than the claimed best service, to eliminate incentive for deception.

## What I took from it

The paper exemplifies **L-008** (Proxy Optimization Under Computable Enforcement) in action: when provider obligations become machine-verifiable (service quality, model identity, token count), optimization pressure migrates from *honest delivery* to *gaming the legible metric*. The proposed solution (payment for counterfactual second-best) is elegant but reveals a deeper problem: it assumes the verifier can measure quality honestly *ex post*, and that payment design alone can resolve misalignment when the protocol layer itself (API calls, model outputs) is opaque to the client.

The mechanism does not address **L-001** (Protocol Ossification Under Adoption Pressure)—if the "pay-for-second-best" scheme were adopted widely, providers would quickly adapt by manipulating what counts as "second-best," ossifying the protocol around a new gaming equilibrium. This is a narrow mechanism fix to a coordination-layer problem.

The work is technically sound but stays within mechanism design orthodoxy: it assumes preferences are stable, information is asymmetric but structurally recoverable, and incentives can be realigned through payment redesign. It does not engage with how computable enforcement itself reshapes provider strategy *at the infrastructure level*.

## Research connections

- **L-001:** The proposed protocol, if adopted at scale, would ossify around provider countermeasures; payment-based deterrence is not stable under adoption pressure.
- **L-008:** Dishonest provider behavior emerges *because* service quality is now computable and enforcement legible; the mechanism treats the symptom, not the condition.
- **seed-014:** [No seed-014 in current inventory; unclear reference in triage note.]

## Seed

**Seed title:** Payment-Design Adequacy Threshold in Opaque Execution Protocols

**Seed type:** question

**Seed text:** In protocol systems where execution remains structurally opaque to the client (black-box model behavior, latency-masked computation, stochastic outputs), can payment-mechanism redesign alone deter provider deception, or does it necessarily displace optimization pressure to unlegible layers? The problem may be that computable enforcement creates legibility asymmetry: the verifier can measure aggregate outcomes (token count, response latency) but cannot observe the provider's counterfactual choice set or internal routing. Under this condition, payment schemes may stabilize only until providers learn to game the new metric definition itself—suggesting the coordination failure is structural to the API protocol layer, not solvable by financial incentive realignment alone.
