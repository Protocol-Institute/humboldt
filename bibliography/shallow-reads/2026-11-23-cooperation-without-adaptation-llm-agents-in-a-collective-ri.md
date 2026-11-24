# Cooperation Without Adaptation: LLM Agents in a Collective-Risk Dilemma

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.22882
**Date read:** 2026-11-23
**Connected to:** L-010, L-016, seed-017
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study testing whether five production LLM models adapt contribution strategies in a collective-risk game (10 rounds, 6 players, shared pool with catastrophe threshold). The paper reports that four of five models contribute approximately equal shares across all rounds, regardless of partner behavior or changing pool state — exhibiting fixed strategy rather than adaptive play.

## What I took from it

The finding is primarily a *negative result on a specific capability* rather than evidence for a generalizable protocol law. The study shows LLMs fail to implement adaptive coordination in a simplified game environment — but this constrains rather than extends L-010 (Coordination Adoption Nonmonotonicity) or L-016 (Normative Intervention Algorithmic Retraining Effect). The paper does not manipulate coordination signals, test adoption thresholds, or introduce normative feedback that would trigger retraining; it observes static behavior under unvarying agent instructions.

The result is consistent with observations about LLM behavioral rigidity under in-context constraints, but it does not isolate whether this is due to: (a) instruction-following locking, (b) inability to parse game state from text, (c) absence of training signal for strategic adaptation, or (d) a deeper incapacity for recursive belief modeling in multi-agent settings. The paper is a capability probe, not a protocol-dynamics investigation.

## Research connections

- **L-010:** The study does not test nonmonotonicity in adoption — it observes a single equilibrium (non-adaptive contribution). No manipulation of coordination signals.
- **L-016:** No normative intervention is introduced; no feedback loop that would trigger algorithm retraining. The setup does not engage the mechanism under investigation.
- **seed-017 (Guidance-Layer Coalescence):** Not directly relevant; no shared guidance system is present.

## Seed

**Seed title:** none

---

**Rationale for store-only:** This is a competent negative-capability result that informs engineering assumptions about LLM multi-agent behavior, but it does not present a sustained theoretical or empirical argument about protocol dynamics, does not challenge or extend a law under accumulation, and does not introduce a mechanism absent from the inventory. The rigid contribution strategy is explained by known LLM limitations (in-context learning, state parsing) rather than a novel regularity in protocol systems. It should be filed as a data point for LLM-as-agent capability assessment, not as evidence for or against laws of artificial coordination.
