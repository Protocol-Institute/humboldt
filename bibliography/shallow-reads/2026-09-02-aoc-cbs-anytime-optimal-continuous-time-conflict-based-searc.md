# AOC-CBS: Anytime-Optimal Continuous-time Conflict-Based Search for Generalised Multi-Agent Path Finding

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.08175
**Date read:** 2026-09-02
**Connected to:** L-006, seed-049
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper extending Conflict-Based Search (CBS), a discrete-time multi-agent path-finding algorithm, to continuous time and heterogeneous agent types. The work relaxes standard MAPF assumptions (single goal per agent, geometric conflicts only, discrete timesteps) to enable application to more complex real-world coordination problems like warehouse automation and airport traffic.

## What I took from it

This is a competent algorithmic extension paper addressing computational efficiency in multi-agent coordination under relaxed constraints. The generalization from discrete to continuous time and from homogeneous to heterogeneous fleets is a natural engineering move, not a theoretical insight about how protocolized systems behave. The paper does not engage with questions about coordination cost displacement, the stability of conflict-resolution protocols under adoption pressure, or how the legibility of conflict detection affects optimizer behavior. The conflict-resolution mechanism itself (building a constraint tree and resolving cardinal conflicts) is treated as a given optimization target rather than as a social or computational phenomenon worth modeling. There is no investigation of how the protocol's behavior changes when agents can observe or game the conflict-detection signal, nor does it address whether anytime-optimality introduces new failure modes under strategic conditions.

## Research connections

- **L-006:** Implicit connection—the paper assumes coordination cost can be minimized through better algorithm design, but does not investigate whether cost shifts to a different layer (negotiation overhead, agent communication complexity, or constraint-tree explosion under heterogeneity).
- **seed-049:** No engagement with consensus reasoning or decoupling mechanisms in the conflict resolution protocol itself.

## Seed

**Seed title:** none
