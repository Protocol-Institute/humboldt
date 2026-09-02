# Incentivizing Forecasters to Learn: Summarized vs. Unrestricted Advice

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2310.19147
**Date read:** 2026-09-02
**Connected to:** L-008, L-004
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mechanism design paper studying how to structure reward schedules to incentivize expert information acquisition over time. The authors model a principal-expert dynamic where the principal chooses whether to solicit summarized reports at a terminal date or allow unrestricted reporting throughout, then proves conditions under which each structure maximizes the expert's incentive to learn.

## What I took from it

The paper is technically sound but operates within a narrow equilibrium-theoretic frame. It does confirm that **the legibility of the reporting channel affects optimization pressure** — restricting reports to a summary forces the expert to consolidate learning in a way that changes the incentive landscape. This is relevant to L-008 (proxy optimization under computable enforcement): the choice of report structure is itself a legibility choice, and it reshapes what the expert optimizes toward.

However, the mechanism is designed to *align* incentives, not to study what happens when alignment fails or when the report structure itself becomes the target of optimization. The paper assumes the expert reports truthfully within the chosen structure; it does not examine whether the expert might distort their learning process to game the reporting constraint itself, or whether the principal's choice of structure might accidentally create perverse incentive cascades downstream. The contribution is local: a better contract design in a two-player setting, not a regularity about how protocol design propagates side effects.

## Research connections

- **L-008:** Confirms that computable reporting constraints reshape optimization; but does not explore what happens when the expert optimizes for the constraint rather than for truth.
- **L-004 / Goodhart:** Report structure is a proxy for "true learning"; the paper does not ask whether terminal-summary incentives might cause the expert to optimize for reportable patterns rather than robust knowledge.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** The expert's private information state is asymmetric; the principal can only see reports. The paper assumes reports remain reliable; it does not study proxy collapse.

## Seed

**Seed title:** none

The paper is a competent contribution to mechanism design but does not generalize a regularity about how protocol design propagates or fails. It operates entirely within the frame of designing better incentive structures under ideal conditions, not studying how those structures degrade or how agents exploit the legibility boundaries the structures create.
