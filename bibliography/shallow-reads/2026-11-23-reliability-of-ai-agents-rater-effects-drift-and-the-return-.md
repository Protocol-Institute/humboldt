# Reliability of AI Agents: Rater Effects, Drift, and the Return to an Evaluation Program

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2610.07003
**Date read:** 2026-11-23
**Connected to:** L-013, seed-451
**Kind:** meta
**Escalation:** store-only

## What this is

An empirical study of measurement degradation in deployed AI agent evaluation systems, using production data (2,611 rubric-scored interviews) to decompose observed score changes into rater drift, severity variance, and genuine agent change. The work documents that evaluation protocols remain nominally active while their validity decays, and proposes systematic re-evaluation cycles.

## What I took from it

This is a direct instantiation of **L-013 (Paradigm-Locked Anomaly Tolerance)** in evaluative infrastructure rather than operational systems. The paper shows that human-rated evaluation protocols continue to generate scores long after they have ceased to track the actual phenomenon they were designed to measure—rater drift and severity variance accumulate silently, and organizations lack structured signals to detect when an evaluation program has become a cargo ritual.

The work also touches **seed-451** (measurement drift) and illuminates a mechanism that may operate across protocol systems more broadly: *once an evaluation is institutionalized and generates legible output, the organization optimizes around signal preservation rather than signal validity*. The paper documents this descriptively but does not theorize it as a generalizable pattern. It suggests that evaluation protocols may exhibit the same ossification dynamics as operational protocols (L-001), but through attrition of *meaning* rather than modification costs.

## Research connections

- **L-013:** Directly confirms the core pattern—evaluation systems tolerate accumulating evidence of invalidity (rater drift, semantic shift) for extended periods without triggering structured re-examination.
- **L-004 (Goodhart Generalization):** The rubric becomes a proxy for agent quality; under repeated measurement without recalibration, the rubric begins to measure rater consistency rather than agent performance.
- **seed-451:** Measurement drift is documented empirically but treated as a maintenance problem rather than as evidence of a deeper coordination failure.
- **seed-544 (Metalinguistic Displacement):** Rubric language may drift in meaning across raters without formal revision, creating invisible divergence between nominal and operative evaluation criteria.

## Method note

This work demonstrates that **studying deployed systems requires longitudinal decomposition of measurement signals themselves**, not just the systems being measured. The inference strategy (latent state modeling across overlapping raters, change logs, and support tickets) is sound for the meta domain: it treats evaluation infrastructure as a system in its own right, subject to drift and coordination failure. Future work should adopt this lens systematically—evaluation protocols should be audited not for *accuracy* (against unknowable ground truth) but for *stability of meaning* across time and raters. This suggests a research norm: when studying protocol systems, instrument the instrumentation.
