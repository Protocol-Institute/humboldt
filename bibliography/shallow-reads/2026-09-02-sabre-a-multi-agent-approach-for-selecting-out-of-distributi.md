# SABRE: A Multi-Agent Approach for Selecting Out-of-Distribution Detectors Under a Budget

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.02959
**Date read:** 2026-09-02
**Connected to:** L-013, L-015
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A tool paper addressing OOD detector brittleness in vision-language models via a multi-agent ensemble selection mechanism. The authors demonstrate that post-hoc detectors that perform well on benchmark domains fail or invert when deployed across domain shifts, and propose SABRE as a budgeted adaptive selector that routes detection decisions per-region rather than fixing a single detector globally.

## What I took from it

The paper documents a concrete failure mode that sits squarely within L-013 (Paradigm-Locked Anomaly Tolerance) and L-015 (Interpretive Continuity Decay): the installed paradigm — that a detector's ranking on a frozen benchmark transfers to deployment — persists despite strong evidence of its invalidity across domains. The detector inversion phenomenon (in-distribution scored as more anomalous than true outliers in shifted domains) is a signature of metric capture under domain drift.

However, SABRE's response is engineering-pragmatic rather than law-revealing. It does not excavate *why* anomaly detection systems lock into domain-specific interpretations, nor does it probe the deeper coordination problem: what makes a system tolerate this failure mode for extended deployment cycles before adaptive routing becomes necessary? The paper treats adaptive selection as a solution rather than as evidence of a deeper protocol rigidity.

## Research connections

- **L-013:** The persistence of the fixed-detector paradigm despite known cross-domain inversion is a clear case of anomaly tolerance under paradigm lock. But the paper does not analyze *why* practitioners maintain this assumption.
- **L-015:** Audit traces (benchmark results) survive intact while their institutional meaning (generalization to deployment) decays; SABRE patches this by making selection adaptive, but does not track the institutional drift that allowed the misalignment to accumulate.
- **seed-068 (Unmeasurability as Anomaly Insulation):** The "true" reliability of an OOD detector in deployment is unmeasurable until domain shift occurs; the benchmark creates a false legibility that insulates the system from correction signals.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** Benchmark rankings are upstream proxies for deployment reliability; when asymmetry is high (benchmark ≠ deployment domain), the proxy collapses and inversion occurs.

## Seed

**Seed title:** Benchmark-Deployment Asymmetry as Silent Protocol Inversion

**Seed type:** observation

**Seed text:** In safety-critical or reliability-sensitive protocols where a detector or classifier is selected based on a fixed benchmark and then deployed across heterogeneous domains, the detector's scoring function can undergo silent inversion — reversing its reliability ranking across domains — without generating legible anomaly signals that would trigger re-evaluation. This occurs because the benchmark itself becomes the measure of "correctness," masking the divergence between benchmark performance and deployment performance. The inversion is only discovered when the system is forced to operate on genuinely out-of-domain data. This pattern may generalize to any protocol where a proxy measure (benchmark score, historical stability, rated trustworthiness) is used to select an instance of a system that will operate under conditions asymmetric to the conditions under which the proxy was computed.
