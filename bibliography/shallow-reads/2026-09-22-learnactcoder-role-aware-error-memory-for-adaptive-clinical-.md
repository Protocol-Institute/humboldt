# LearnActCoder: Role-Aware Error Memory for Adaptive Clinical Coding Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.19721
**Date read:** 2026-09-22
**Connected to:** L-016, seed-149
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A tool paper proposing an inference-time adaptation framework (LearnActCoder) that uses error patterns from small labeled batches to route correction tasks to role-specialized agents in clinical coding. The work treats repeated failure modes as trainable knowledge, splitting false-negatives and false-positives into separate optimization targets.

## What I took from it

The paper is competent domain engineering: it identifies that clinical coding agents fail recurrently in specific, categorizable ways (unsupported codes, missed conditions, specificity errors) and proposes a lightweight adaptation mechanism to route these failures to specialized correctors. However, it does not examine whether this architecture itself generates new coordination problems, or whether role specialization under error-driven retraining produces unintended optimization surfaces.

The work is *about* algorithmic adaptation under failure feedback, which touches L-016 (Normative Intervention Algorithmic Retraining Effect), but it does not investigate whether the retraining protocol itself displaces the optimization target or creates emergent failure modes at the system level. It treats the Mistake Knowledge Database as a transparent improvement surface, not as a potential site for proxy capture or attractor formation.

## Research connections

- **L-016:** The paper instantiates error-driven retraining of recommendation/allocation components, but does not test whether role-specialization under error feedback produces unintended behavioral drift or metric capture within the specialized agents.
- **seed-149:** Confirms that epistemic faults (unsupported codes, missed documented conditions) are formalized and routed as protocol violations into a learning loop, but does not examine whether formalization of fault categories itself becomes a coordination target.

## Seed

**Seed title:** none
