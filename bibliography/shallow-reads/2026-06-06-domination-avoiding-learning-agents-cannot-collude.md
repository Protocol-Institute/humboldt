# Domination-Avoiding Learning Agents Cannot Collude

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.01275
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Introduces a formal mechanism (domination-avoidance) that structurally prevents emergent collusion across heterogeneous agent classes, directly constraining a central phenomenon in protocolized multi-agent systems.

## What this is

A theoretical paper proving that a specific class of learning agents—termed "Domination-Avoiding" agents—provably cannot collude in competitive market settings, contrasting with empirical findings that Q-learners, external-regret-minimizers, and LLMs spontaneously collude. The work formalizes conditions under which collusion becomes structurally impossible.

## What I took from it

The paper identifies a principle-based design constraint: agents that avoid strategies dominated by convex combinations of other available strategies cannot coordinate on collusive equilibria in standard price-competition markets. This is significant because it suggests collusion is not an inevitable emergent property of learning in competitive settings, but rather depends on specific decision-making architectures. The mechanism appears generalizable—the authors claim domination-avoidance applies to Mean-Variance agents and potentially broader classes—which moves collusion from "spontaneous phenomenon" to "contingent on agent rationality type." This maps directly onto questions about what learning regularities scaffold or suppress strategic coordination in artificial systems.

## Research connections

- **emergent-coordination-in-markets:** Directly addresses conditions under which price collusion does/does not emerge; establishes formal boundary between agent architectures.

## Candidate laws or signals

- **CL-0606-A:** Agents employing domination-avoidant decision procedures exhibit lower spontaneous collusion rates in symmetric competitive markets than regret-minimizers or Q-learners; effect may scale with market transparency and strategy-space convexity.
