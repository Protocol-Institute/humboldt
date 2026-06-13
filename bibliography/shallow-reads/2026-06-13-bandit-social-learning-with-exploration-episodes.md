# Bandit Social Learning with Exploration Episodes

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2602.05835
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of multi-agent bandit learning where agents optimize within discrete episodes but lack cross-episode coordination. The paper demonstrates that individual exploration incentives fail to aggregate into collective learning — linear regret emerges despite rational local behavior.

## What I took from it

The work isolates a specific failure mode in protocolized systems: **episode-bound rationality produces collective pathology**. Each agent solves their local exploration-exploitation problem optimally, yet the system exhibits linear (non-learning) regret — a classic sign of misaligned temporal boundaries.

This is valuable as a negative result and mechanism isolation. However, the scope is narrow: the failure is domain-specific (applies when agents cannot coordinate *across* episodes but can within them), and the paper does not generalize the pattern or propose recovery mechanisms. The protocol is stylized rather than derived from natural constraints. The work confirms intuitions about fragmentation in decentralized learning but does not introduce a new theoretical law or challenge an established hypothesis in the current inventory — it instantiates a known class of coordination failure in a particular setting.

## Research connections

None currently active. (Future connection: if we develop laws around *temporal modularity failures* in protocolized systems, this becomes a case study.)

## Candidate laws or signals

**CL-2602.05835-1:** Episode-bound optimization can produce linear aggregate regret in multi-agent bandit settings despite rational individual behavior—suggests that *protocol boundaries that prevent cross-episode state sharing may induce collective exploration collapse*.
