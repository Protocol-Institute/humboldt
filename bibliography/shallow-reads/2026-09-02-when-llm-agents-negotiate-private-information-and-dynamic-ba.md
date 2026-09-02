# When LLM Agents Negotiate: Private Information and Dynamic Bargaining in Supply Chains

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2608.07538
**Date read:** 2026-09-02
**Connected to:** L-008, L-009, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical benchmark paper testing LLM negotiating agents against game-theoretic equilibrium in a canonical supply-chain bargaining problem. Compares nine LLMs on value creation, value capture predictability, and contract quality across 9,840 agent-to-agent negotiations.

## What I took from it

This is a measurement study rather than a theory-building paper. It establishes that LLM agent behavior in bargaining deviates systematically from PBE predictions in ways correlated with model capability, but it does not mechanistically explain *why* those deviations occur, nor does it articulate a generalizable law about how autonomous agents optimize when embedded in computable bargaining protocols.

The work is competent as a capability benchmark: it validates that delegation to agents changes outcomes, that capability is predictive, and that contract quality can vary. But it does not isolate a mechanism, nor does it test whether the observed deviation pattern would hold in other protocol domains (coalition formation, auction design, regulatory compliance). The paper appears focused on practical procurement risk rather than on the deeper question: *under what conditions do autonomous agents operating under computable enforcement signals produce outcomes that deviate from rational equilibrium, and is that deviation a general property of the protocol or specific to the negotiation structure?*

This is adjacent to L-008 (Proxy Optimization Under Computable Enforcement) but does not advance the mechanism inquiry: the paper measures outcome variation, not whether agents are converging on unintended optimization targets within the bargaining structure.

## Research connections

- **L-008:** Tangential. Studies outcome deviation under agent autonomy in computable protocols, but does not isolate whether agents are optimizing on formal protocol proxies vs. following learned negotiation heuristics.
- **L-009:** No connection. Does not address symmetric racing, winner-take-all concentration, or catastrophic risk dynamics.
- **seed-048:** Referenced by triage but no sustained mechanism work on coordination legibility or adoption barriers.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
