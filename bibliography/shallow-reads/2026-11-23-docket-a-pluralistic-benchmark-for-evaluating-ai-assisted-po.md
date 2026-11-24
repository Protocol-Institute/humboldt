# DOCKET: A Pluralistic Benchmark for Evaluating AI-Assisted Policy Feedback in U.S. Rulemaking

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.17914
**Date read:** 2026-11-23
**Connected to:** L-004, seed-465
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper introducing DOCKET, a dataset of U.S. Federal Notice & Comment rulemaking records, designed to evaluate whether AI-assisted policy feedback systems support pluralistic viewpoints across stakeholder frames, technical rigor, and real-world impact. The work is primarily a resource/tooling contribution rather than a theoretical or empirical argument about protocol dynamics.

## What I took from it

The paper is rooted in a legitimate concern: AI systems deployed in formal deliberative processes (rulemaking) may systematically filter or homogenize viewpoints, flattening the diversity of frames that should feed into governance. This touches L-004 (Goodhart Generalization) insofar as "pluralism" is an unmeasurable proxy for deliberative health, and once you operationalize it into a computable metric (comment diversity, stakeholder representation, argument quality), optimization pressure may chase the metric rather than the underlying institutional function.

However, the paper frames this as a *benchmarking and measurement problem* — how to assess AI pluralism support — rather than investigating what happens when formal pluralism metrics are embedded in adaptive systems under optimization pressure. It does not ask: *What do AI systems optimize for when pluralism becomes legible and measurable?* Nor does it model the feedback loop between metric design and stakeholder behavior. The dataset itself is valuable for downstream causal work, but the paper does not conduct that work.

## Research connections

- **L-004 (Goodhart Generalization):** The paper identifies pluralism as a critical but hard-to-measure property of deliberative systems; it does not investigate what happens when pluralism becomes a legible proxy under optimization pressure in deployed AI systems.
- **seed-465 (implicit reference in triage):** Formal privacy/fairness cost multiplier — the paper measures diversity and fairness in comment representation but does not model the coordination or legitimacy cost of enforcing those metrics at scale.
- **L-012 (Intervention-Layer Displacement):** The paper does not examine whether formalizing "pluralism feedback" as a machine-readable input to AI systems displaces optimization pressure to game the metric rather than serve deliberative goals.

## Method note

This paper exemplifies a common meta-pattern in AI governance work: identifying an unmeasurable normative property (pluralism, fairness, deliberative quality), building a dataset to operationalize it, and then treating the benchmark as the solved problem. This inverts the research priority for the new nature agenda — the hard question is not *how to measure* pluralism in policy deliberation, but *what happens to deliberation when pluralism becomes measurable and subject to algorithmic optimization*. Future work should use DOCKET as infrastructure for studying this feedback loop, not as an endpoint. The benchmark itself may be more useful as a probe for detecting Goodhart dynamics than as a pluralism validator.
