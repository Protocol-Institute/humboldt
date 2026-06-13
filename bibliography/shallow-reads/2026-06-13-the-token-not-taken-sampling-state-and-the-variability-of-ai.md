# The Token Not Taken: Sampling, State, and the Variability of AI Agent Outputs

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2606.08998
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** This appears to be a primary source systematically decomposing sources of variability in agentic systems—separating sampling stochasticity from state dependency—introducing a mechanism (multi-layer variability architecture) absent from our current inventory and potentially generalizing beyond individual agent implementations to a class property of orchestrated AI systems.

## What this is

A theoretical and empirical investigation into why agentic AI systems produce different outputs across identical requests, decomposing variability into distinct layers: foundation model sampling, orchestration state, tool selection, and observation updating. The work treats agentic systems as composite protocols where variability emerges not from a single source but from interacting stochastic and deterministic processes.

## What I took from it

This paper directly addresses a blind spot in our treatment of protocolized systems: we have largely treated stochasticity as a property of *individual components* (e.g., sampling temperature in LLMs) rather than as a *compositional property* emerging from agent loops. The abstraction of agentic systems as layered—foundation model → orchestration → tool calls → state updates—suggests that variability is not noise to be suppressed but a structural feature of how these systems serialize decisions across a loop. 

This matters for our hypothesis space because it implies that reproducibility and determinism in agentic systems cannot be achieved by simply fixing the model output; you must also freeze orchestration state, tool availability, and observation traces. This hints at a deeper law: **protocolized systems inherit variability from every stateful layer they compose**, and the interaction between layers can amplify or suppress variance in non-obvious ways. The work appears to provide empirical grounding for why agent behavior is inherently path-dependent.

## Research connections

- **Compositionality of protocol behavior:** Agents as nested loops suggest that system-level properties (variance, reproducibility, drift) emerge from layer interactions, not individual layer properties alone.

## Candidate laws or signals

- **CL-2606.08998-1:** Variability in agentic systems is a composite property: V_agent = f(V_sampling, V_state, V_orchestration, V_tool-selection), where suppressing any one component does not yield determinism unless all are fixed simultaneously.

- **CL-2606.08998-2:** The depth of an agent's orchestration loop (number of plan-observe-update cycles) correlates with cumulative variance unless explicit checkpointing or deterministic replay is enforced at each layer.
