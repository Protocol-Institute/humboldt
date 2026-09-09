# Pingquanqi (Equalizer): A Cross-Domain Sociotechnical Framework for Human-Agent Interaction Governance

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.26573
**Date read:** 2026-09-01
**Connected to:** L-007, seed-027
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper proposing a governance framework for LLM agents as permanent infrastructure, framed around a cost-chain model where unoptimized agentic systems leak "user lifetime" without compensation. The work treats human-agent interaction as a sociotechnical protocol requiring cross-domain governance design.

## What I took from it

The framing of agentic systems as infrastructure with a measurable "cost chain" ending in user lifetime is conceptually sharp, but the paper appears to remain at the framework-proposal stage rather than presenting empirical findings or a sustained theoretical argument about how such systems actually ossify, resist modification, or accumulate trust independent of performance.

The connection to L-007 (Trust Ratchet) is real but underdeveloped: the paper asserts that permanent infrastructure accumulates trust through operational stability, but does not investigate whether trust in agentic systems follows the same age-dependent dynamics as safety-critical protocols, or whether the presence of continuous algorithmic modification breaks that ratchet. The institutional memory angle (seed-027) is gestured at but not explored—what happens to governance authority and interpretive continuity when agents themselves become the records of their own behavior?

The work risks collapsing into tool design (how to optimize the cost chain) rather than law discovery (what regularities *must* emerge when optimization happens under infrastructure constraints).

## Research connections

- **L-007:** Asserts trust accumulates in permanent infrastructure but provides no evidence that trust in agentic systems follows the same mechanisms as safety-critical protocol trust—particularly given agents' continuous self-modification.
- **seed-027:** Raises but does not resolve the problem: when agents are the computational substrate *and* the record-keepers of governance history, how does institutional memory survive paradigm shifts in the agent's training or objectives?
- **L-004 (Goodhart):** The "user lifetime" metric is itself a measurable proxy for an unmeasurable goal (human flourishing, autonomy, dignity); the paper does not investigate what happens when governance protocols optimize for legible cost metrics.
- **L-012 (Intervention-Layer Displacement):** Governance interventions designed to protect user time will become legible optimization targets; the paper does not model this displacement.

## Seed

**Seed title:** Infrastructure-Trust Decoupling in Agentic Systems
**Seed type:** question
**Seed text:** In safety-critical protocols, trust accumulates through operational age and stability (L-007). But when the operational substrate itself is continuously modified (as in LLM agent retraining), does the trust ratchet still operate, or does algorithmic change break the causal chain between age and reliability? Specifically: can institutional trust in agentic infrastructure survive when the agents themselves are not stable entities but targets of continuous optimization? This would generalize beyond agent governance to any protocol where the enforcer or executor is itself a learning system.
