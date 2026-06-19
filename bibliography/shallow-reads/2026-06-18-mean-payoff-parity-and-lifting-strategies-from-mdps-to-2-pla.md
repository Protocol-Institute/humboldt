# Mean-Payoff-Parity and Lifting Strategies from MDPs to 2-Player Stochastic Games

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.19324
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A complexity-theoretic paper establishing tight bounds on strategy memory requirements when lifting optimal strategies from single-agent MDPs to two-player stochastic games. The work proves that an exponential blowup in memory modes (established as achievable in prior work) is also necessary in the worst case.

## What I took from it

This is a negative result about *strategy economy* in adversarial systems. The paper demonstrates that introducing a second strategic agent fundamentally increases the representational complexity required to maintain optimality—even with randomization permitted. This is a hard lower bound, not an artifact of proof technique.

The result touches on a persistent tension in protocolized systems: moving from open-world single-agent optimization (MDP) to contested multi-agent environments (stochastic games) induces unavoidable memory inflation. This may generalize beyond game theory to any system where strategy must be robust to adversarial perturbation rather than merely noise. However, the paper itself is narrowly scoped to strategy complexity in a specific game class, and does not develop broader mechanistic claims about why this happens or what principles govern the transition.

## Research connections

- None identified; no active hypotheses or established laws currently tracked in this research agenda.

## Candidate laws or signals

- **CL-2606.19324-1:** *Adversarial contexts require exponential memory overhead relative to single-agent settings, even when randomization is available.* (Narrow but potentially generalizable mechanism worth monitoring across other protocol domains.)
