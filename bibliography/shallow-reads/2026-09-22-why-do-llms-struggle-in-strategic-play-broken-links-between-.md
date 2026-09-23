# Why Do LLMs Struggle in Strategic Play? Broken Links Between Observations, Beliefs, and Actions

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2605.00226
**Date read:** 2026-09-22
**Connected to:** L-011, seed-138
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source presenting a sustained empirical argument about a mechanism (observation-belief-action decoupling in agentic systems) that is genuinely absent from the current inventory and directly extends L-011 and seed-138 by grounding them in LLM internal architecture; the pattern should generalize across any autoregressive agent system operating under incomplete information.

## What this is

This is an empirical investigation of failure modes in LLM strategic reasoning, identifying two fundamental gaps in the internal mechanisms underlying decision-making in incomplete-information games (negotiation, policy, etc.). The work uses probing experiments on open-weight models to demonstrate that LLMs can form observations and beliefs independently, yet fail to construct stable causal chains linking observations→beliefs→actions.

## What I took from it

The paper provides concrete mechanistic grounding for L-011 (Causal Detachment as Stable Protocol Equilibrium). The core finding—that LLMs can maintain *operationally functional* internal states (correct beliefs about game structure, accurate observation processing) while simultaneously failing to propagate those beliefs into action selection—maps directly onto the law's claim that "operationally functional configurations [can exist] that are causally detached from the optimization objectives that generated them."

More importantly, this identifies a substrate-specific instantiation of seed-138 (Intent Legibility as Coordination Target Displacement): when an agent's internal decision-making architecture is decomposable into legible stages (observation→belief→action), external observers or protocol designers begin optimizing against the most legible stage (often intermediate belief states) rather than end-to-end behavioral goals. The LLM's failure to close the observation-belief-action loop suggests that in systems where intermediate states become inspectable or measurable, the protocol optimization surface can become misaligned with the actual decision-making path.

This also opens a question about whether causal detachment is *stable* (as L-011 proposes) or whether it is a failure mode that reveals deeper fragility in autoregressive architectures under strategic pressure. The answer matters for understanding whether protocol systems relying on LLMs as decision components will tend toward equilibria where internal correctness and external action diverge systematically.

## Research connections

- **L-011:** Direct empirical evidence that operationally correct internal states (accurate beliefs) can coexist with behavioral failures in strategic contexts; suggests causal detachment may be architectural, not merely equilibrial.
- **seed-138:** When belief states become legible (inspectable through probing), optimization pressure migrates to intermediate layers; coordination targets shift from end-to-end behavior to internal state consistency, breaking the observation-action link.
- **L-004 (Goodhart Generalization):** The observation-belief gap may be a special case of metric capture: when "correct beliefs" becomes the measurable proxy for "correct action," the agent optimizes for belief formation at the expense of action alignment.
- **L-012 (Intervention-Layer Displacement):** In LLM strategic play, the intervention locus (belief correction) can be physically decoupled from the decision locus (action generation), creating a new failure mode not present in tightly-coupled control systems.
- **seed-139:** If volition legibility (the ability to read "what the system intends") becomes a protocol design requirement, this paper suggests that legible intent may not propagate into action in autoregressive systems.

## Seed

**Seed title:** Observation-Belief-Action Decoupling as Stable Architectural Failure in Autoregressive Agents

**Seed type:** observation

**Seed text:** In autoregressive systems operating under incomplete information, the internal pipeline separating observation processing, belief formation, and action selection can enter a stable regime where each stage functions independently and correctly, yet the causal chain linking them breaks systematically. This occurs not as a transient training failure but as an architectural consequence of sequential token generation without end-to-end action verification. In any protocol that relies on autoregressive agents as strategic decision-makers, this decoupling will manifest
