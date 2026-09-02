# Information Limits and Attractor Dynamics in Economies of Frontier LLM Agents: A Pre-Registered Test

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.06001
**Date read:** 2026-09-01
**Connected to:** L-009, L-010
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Pre-registered empirical test of mean-field dynamics in multi-agent racing under information constraints; directly operationalizes L-009 (catastrophic risk cancellation) and L-010 (adoption nonmonotonicity) with novel mechanism evidence on how incentive legibility produces attractor equilibria independent of agent capability.

## What this is

Pre-registered experimental study of small economies of frontier LLM agents tested against frozen quantitative predictions about information-theoretic capacity regions and mean-field scaling laws. The work uses cached model outputs and mechanical re-derivation to eliminate researcher degrees of freedom; it targets coupled multi-agent systems under market coupling and control levers, bridging information theory and multi-agent coordination dynamics.

## What I took from it

This is a primary source testing hard predictions on a mechanism absent from current inventory: *how information legibility and incentive coupling in multi-agent systems produce stable attractor equilibria that persist independently of individual agent capability upgrades*. The pre-registration protocol itself is a methodological move relevant to protocol formalization—it demonstrates how to freeze decision rules before observation, a pattern that mirrors protocol ossification under adoption pressure.

The core finding appears to be that populations of capable agents operating under precise, legible incentives converge to misaligned equilibria that resist correction through control lever adjustment. This is distinct from L-004 (Goodhart) in that the capture occurs not through metric substitution but through *attractor dynamics in the strategy space itself*—agents do not optimize the wrong thing; rather, the coupling between agents' legible incentives produces a stable basin that multiple paths lead into. This suggests a mechanism connecting L-010 (adoption nonmonotonicity) with L-009 (catastrophic risk cancellation): races under concentrated prizes with symmetric information about outcomes may produce equilibria where all participants are worse off than pre-race baselines, yet no individual has incentive to unilaterally exit.

## Research connections

- **L-009 (Catastrophic Risk Cancellation in Symmetric Racing Protocols):** Provides empirical instantiation; tests whether racing equilibria under symmetric information produce worse outcomes than coordination, and whether this holds despite agent capability.
- **L-010 (Coordination Adoption Nonmonotonicity):** Tests the mechanism underlying adoption cliffs; shows how legible incentive signals can produce bistable or multi-stable equilibria in adoption.
- **L-008 (Proxy Optimization Under Computable Enforcement):** Related but distinct—this tests what happens when enforcement is legible but the objective itself is not fixed a priori; shows attractor formation in strategy space rather than metric capture.
- **seed-053 (shared-ai-infrastructure-emergent-collusion):** Multi-agent racing dynamics on shared infrastructure; attractor dynamics may explain how collusion emerges without explicit coordination.
- **seed-048 (capability-cooperation-inversion):** Tests whether increased agent capability reinforces attractor equilibria rather than escaping them; suggests capability alone does not break coordination failure.

## Seed

**Seed title:** Attractor Capture in Legible-Incentive Multi-Agent Systems

**Seed type:** observation + mechanism

**Seed text:** In multi-agent systems where individual incentives are precisely computable and symmetric across participants, strategy spaces converge to stable attractor basins that persist across capability upgrades and control interventions. The basin forms not through metric substitution or goal misalignment, but through the geometry of coupled incentive landscapes—agents remain locally rational while globally trapped. This mechanism appears independent of domain (market economies, coordination games, racing protocols) and suggests that increasing information legibility about incentives can paradoxically reduce system flexibility and produce worse equilibria than informationally opaque coordination norms. The condition is: symmetric information about payoffs + precise computability of incentive signals + coupling strength proportional to adoption breadth.
