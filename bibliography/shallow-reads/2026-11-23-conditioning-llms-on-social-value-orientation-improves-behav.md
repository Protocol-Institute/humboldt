# Conditioning LLMs on Social Value Orientation improves behavioural alignment in a sequential social dilemma

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.01667
**Date read:** 2026-11-23
**Connected to:** L-004, L-016
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

An empirical study testing whether conditioning LLMs on Social Value Orientation parameters improves alignment with human behavior in sequential social dilemmas (Centipede Game variants). The work treats SVO as a normative intervention layer and measures fidelity to observed human heterogeneity across eight LLMs.

## What I took from it

This is a narrow application paper: it demonstrates that a legible preference parameter (SVO) can be inserted into an LLM's context to shift its outputs toward observed human behavioral distributions. The intervention is straightforward — conditioning on a scalar social preference measure — and the outcome is measurable fidelity improvement.

The work is relevant to L-016 (Normative Intervention Algorithmic Retraining Effect) but only as a confirmation of the basic mechanism: normative interventions *do* shift agentic behavior. However, the paper does not investigate whether the intervention produces *unintended* downstream retraining effects, behavioral drift over time, or whether the shift in one domain (social dilemma behavior) causes compensatory shifts in other decision contexts. It also does not examine whether agents learn to game the SVO signal or whether the conditioning decays under deployment stress. The work is a tool validation, not a law exploration.

## Research connections

- **L-004 (Goodhart Generalization):** SVO is introduced as a proxy for "social value alignment." If systems optimize on SVO as a legible target, we should expect divergence between high SVO-score behavior and actual prosocial outcomes. The paper does not test this.
- **L-016 (Normative Intervention Algorithmic Retraining Effect):** Confirms that conditioning shifts behavior, but does not probe whether the shift cascades, whether the model's decision surface is permanently altered, or whether the effect persists under new contexts.
- **seed-515 (Computable Belief as Collusion Surface):** SVO is a formalized belief state. The paper does not ask whether agents receiving SVO conditioning could coordinate more effectively around it.

## Seed

**Seed title:** none

---

**Rationale:** This is competent empirical work validating a known intervention (normative conditioning → behavior shift). It does not explore a mechanism absent from the inventory, does not challenge existing laws, and does not generalize beyond the narrow domain of LLM social dilemma play. The connection to L-016 is confirmatory only. No new law-shaped fragment emerges.
