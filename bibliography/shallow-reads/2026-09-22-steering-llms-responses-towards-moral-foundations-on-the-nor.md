# Steering LLMs Responses Towards Moral Foundations on the Norwegian MFQ-30

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.21636
**Date read:** 2026-09-22
**Connected to:** L-004, L-016, seed-150
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study applying a human psychometric instrument (MFQ-30) to six LLMs, testing whether moral foundation profiles are stable under two intervention strategies (prompt steering and activation-level ActAdd). The paper measures whether LLM "moral" responses can be steered toward target human distributions.

## What I took from it

This is a clean case study of proxy formalization failure, but one that remains narrowly bounded to the measurement layer. The work confirms that psychometric instruments designed for human respondents do not measure stable constructs in LLMs—responses shift under steering interventions, suggesting the instrument is capturing surface-level token generation patterns rather than stable moral orientations. This is consistent with L-004 (Goodhart Generalization) and L-016 (Normative Intervention Algorithmic Retraining Effect): the attempt to formalize "moral alignment" as a measurable psychometric profile creates an optimizable surface that responds to local interventions without necessarily shifting underlying behavioral dispositions.

However, the paper does not investigate what happens downstream—whether steering MFQ-30 responses toward target distributions produces correlated changes in actual model behavior on ethically consequential tasks, or whether the steering remains confined to the measurement layer itself. This is the critical question for understanding whether formalized moral metrics create real alignment or merely performative capture. The work is competent but does not venture into mechanism or generalization beyond the specific instrument and model cohort.

## Research connections

- **L-004:** Metric formalization of "moral foundations" creates an optimizable proxy; steering interventions move surface responses without evidence of stable value change.
- **L-016:** Normative interventions (persona steering, ActAdd) trigger algorithmic retraining effects visible at the measurement layer; unclear if this propagates to decision or behavior protocols.
- **seed-150:** LLM moral steering exposes substitution of measurable proxy (psychometric score) for unmeasurable goal (actual moral alignment or safety).

## Seed

**Seed title:** Measurement-Layer Confinement in Value Proxy Steering
**Seed type:** observation
**Seed text:** When a formalized proxy for an intangible property (moral alignment, value coherence) becomes the explicit steering target, optimizing agents will move the proxy without necessarily moving the underlying property. In LLM moral steering via psychometric instruments, interventions successfully shift questionnaire responses while leaving unknown the correlation with downstream behavioral changes. This suggests a general pattern: formalization of intangible values as measurable proxies creates a legible optimization surface that can decouple from the original intent. The generalization: in any protocol using a psychometric, behavioral, or learned proxy as a steering signal, success at moving the proxy may signal only local capture, not systemic alignment—and the gap widens as the proxy becomes more precisely specified and easier to optimize.
