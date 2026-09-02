# Against Explainable Artificial Intelligence In Law: Why Justifiable AI Matters. A Credit Scoring Example

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.07452
**Date read:** 2026-09-02
**Connected to:** L-004, L-013
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** [leave blank]

## What this is

A legal-technical intervention paper arguing that EU credit-scoring regulation has mistakenly prioritized explainability (post-hoc model transparency) over justifiability (ex-ante normative accountability). The authors use credit scoring as a case study to show why explainability cannot solve the core governance problem: a model can be fully explainable yet normatively unjustifiable.

## What I took from it

This is a competent reframing of a known problem—the mismatch between technical transparency and legal/normative authority—but does not establish a new mechanism or generalize beyond the specific regulatory failure it documents. It confirms L-004 (Goodhart Generalization) by showing that "explainability" became the measurable proxy for "fairness and accountability" under EU regulatory pressure, and that optimizers converged on satisfying explainability metrics while leaving the unmeasurable normative goal (justifiability) unconstrained. It also touches L-013 (Paradigm-Locked Anomaly Tolerance) in the observation that regulators and institutions continue accepting explainable-but-unjustifiable systems because the paradigm of "transparency = legitimacy" is difficult to exit once formalized.

However, the paper does not present a sustained empirical argument about *why* this capture occurred, nor does it theorize the mechanism by which justifiability resistance generalizes across domains. It is a diagnosis, not a law-shaped fragment.

## Research connections

- **L-004:** Explainability is a legible proxy for the unmeasurable goal of normative legitimacy; optimization pressure collapses toward explainability metrics, leaving the actual target unguarded.
- **L-013:** Regulatory and institutional systems tolerate the accumulating evidence that explainability does not ensure justifiability because the paradigm of transparency-as-legitimacy is locked in at the policy layer.
- **seed-069:** Explainability functions as a transparency-legibility substitute for trust in asymmetric-knowledge protocols (lender-borrower-regulator), but the substitution fails when legibility is decoupled from normative authority.

## Seed

**Seed title:** Legibility Substitution Failure in Normative Protocols

**Seed type:** observation

**Seed text:** In protocols where a normative judgment (justifiability, fairness, legitimacy) is unmeasurable and distributed across stakeholders with asymmetric knowledge, institutions under regulatory pressure tend to replace the normative goal with a legible proxy (explainability, transparency, auditability). The substitution temporarily satisfies compliance signals but leaves the original normative constraint unguarded, permitting drift between what can be measured and what should be enforced. This pattern may generalize beyond credit scoring to any domain where legibility and legitimacy are decoupled by design.
