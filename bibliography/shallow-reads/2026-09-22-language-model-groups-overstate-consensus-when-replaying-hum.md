# Language-model groups overstate consensus when replaying human deliberation on a reasoning task

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.20543
**Date read:** 2026-09-22
**Connected to:** L-010, seed-138
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An experimental study comparing human deliberation groups on a reasoning task (Wason problem) with LLM agent groups seeded from human pre-discussion answers. The paper measures consensus across multiple operationalizations and finds that agent groups systematically report higher consensus rates than human groups, partly due to differential participation patterns and partly due to persistent anchoring effects.

## What I took from it

The work documents a gap between human and agent deliberation dynamics, but frames it as a measurement/replication fidelity problem rather than a mechanism problem. The core finding—that LLM agents remain anchored to seeded beliefs and participate more uniformly—is descriptive of *this task* rather than generalizable to protocol dynamics.

The paper does not investigate *why* agents anchor more persistently, nor does it test whether the observed consensus-overstatement is an artifact of the deliberation protocol itself (how beliefs are aggregated, when agents update, what counts as "consensus"). The operationalization variance (24%–57% consensus estimates across scoring definitions) is interesting but interpreted as a measurement problem, not as evidence that consensus itself is unstable under different formalizations—which would be protocol-relevant.

The differential participation (humans silent; agents active) is noted but not analyzed as a coordination dynamic. Under L-010, the question would be: does agent participation *encourage or suppress* actual convergence? Does the visible participation signal itself become a coordination target?

## Research connections

- **L-010:** Coordination Adoption Nonmonotonicity — The paper shows agents adopt more uniformly than humans, but does not test whether uniform adoption is *less* stable or whether it freezes exploration prematurely. The mechanism linking participation visibility to convergence speed is absent.
- **seed-138:** Intent Legibility as Coordination Target Displacement — Agent groups may be converging on a *legible signal* (stable responses, uniform participation) rather than on the underlying reasoning task. The paper does not distinguish between these.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Reasoning:** This is a competent experimental study, but it is fundamentally a *replication fidelity* paper, not a *law-shape* paper. It documents that LLM agents behave differently from humans in a specific reasoning task, but does not uncover a mechanism that would generalize to protocol design, governance, or coordination systems. The finding that consensus is operationalization-dependent is already anticipated by existing work on metric capture (L-004) and does not add a new mechanism or boundary condition. The participation differential is noted but not analyzed as a coordination phenomenon. Without a hypothesis about *why* agent participation patterns affect consensus under formalization, or *whether consensus-legibility itself distorts the deliberation protocol*, the work remains domain-specific.
