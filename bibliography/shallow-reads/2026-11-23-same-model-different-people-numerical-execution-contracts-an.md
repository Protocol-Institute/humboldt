# Same Model, Different People: Numerical Execution Contracts and the Reproducibility of Fairness Audits

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.23657
**Date read:** 2026-11-23
**Connected to:** L-004, seed-465
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical audit study that isolates numerical precision and execution substrate as variables in fairness metric reproducibility. By holding model weights, code, threshold, and audit procedure constant while varying arithmetic precision (FP32 → BF16, FP8) and deployment kernels, the authors measure whether fairness outcomes are reproducible under different computational execution contracts. The work is domain-specific troubleshooting: a demonstration that audit reproducibility fails not at the statistical or algorithmic level but at the hardware/numerical layer.

## What I took from it

This is a sharp *instantiation* of L-004 (Metric Capture under Optimization Pressure) but it doesn't generalize the mechanism—it documents a specific failure mode of a specific mitigation (fairness auditing). The core finding—that fairness metrics are sensitive to numerical substrate and thus not stable across deployment contexts—confirms that formalized fairness proxies are legible to optimization pressure in the execution layer, not just the training layer. However, this is a *domain problem* (fairness auditing robustness) not a law about protocol systems. The paper does not argue that this represents a generalizable regularity about all protocol systems under formalization pressure, nor does it propose a mechanism that would apply beyond ML deployment contexts.

The work does touch on something the inventory tracks (seed-465: formal privacy/safety as alignment cost), but only incidentally: the implicit claim is that reproducible fairness requires either accepting a fairness cost (in precision) or accepting an audit cost (re-running audits per platform). It does not theorize this as a conservation law or escalation dynamic.

## Research connections

- **L-004:** Metric Capture confirmed in a narrow domain: fairness metrics optimized under different numerical contracts yield different audit outcomes. But this is Goodhart at the execution layer, not a new mechanism.
- **seed-465:** Formal fairness as a computational cost — precision reduction trades fairness reproducibility for deployment efficiency. Not explored as a generalizable principle.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
