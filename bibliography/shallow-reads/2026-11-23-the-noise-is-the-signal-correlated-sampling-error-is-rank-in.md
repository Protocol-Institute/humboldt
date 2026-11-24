# The Noise Is the Signal: Correlated Sampling Error Is Rank-Informative for Proxy Metric Selection

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2610.08194
**Date read:** 2026-11-23
**Connected to:** L-004, L-022
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** [none]

## What this is

A statistical methods paper addressing proxy metric selection in A/B testing under real-world constraints. The core finding: when north-star metrics are slow and noisy, teams select proxy metrics by historical correlation—but validation is circular (only the noisy north star benchmarks the choice). The authors argue that *correlated sampling error itself* carries rank-informative signal about proxy quality, enabling better validation without access to future north-star data.

## What I took from it

This is a narrow fix to a real operational problem in metric-driven optimization loops. The insight—that measurement noise structure itself encodes information about proxy fidelity—is technically sound but stays within the existing framework of proxy selection under legibility constraints. It does not challenge the deeper pathology that L-004 tracks: that optimization pressure on a proxy metric (however well-selected) will eventually decouple the proxy from the unmeasurable goal it was chosen to track. The paper solves a *selection* problem, not a *drift* problem.

The work does surface a genuine friction: correlated sampling errors create an inference problem that standard methods miss. This friction might generalize—it hints that systems relying on joint measurement of a proxy and a ground truth will accumulate systematic biases in their own validation procedures. But the paper does not pursue that direction; it stays in econometric solution space.

## Research connections

- **L-004 (Goodhart Generalization):** The paper assumes proxy metrics can be validated against a noisy north star, but does not address the mechanism by which optimization pressure causes the proxy to diverge from the goal after selection. This is orthogonal to the core L-004 risk.
- **L-022 (Oracle Fitness Decoupling):** Tangential. The paper treats the north star as a fixed (albeit noisy) oracle. It does not examine what happens when the proxy itself feeds back into the system and reshapes the measurement landscape.
- **seed-276 (Legibility-Induced Measurement Substitution):** Weak connection. The paper's entire framing assumes that measurement structure (correlation, noise variance) can be parsed to improve metric choice—a legibility play. It does not ask whether the act of making the proxy legible for optimization changes the metric's relationship to the goal.

## Seed

**Seed title:** none

---

**Rationale for store-only:** This is competent work on a real operational problem, but it operates within the existing proxy-selection paradigm rather than challenging or extending the laws under accumulation. The technical insight about correlated sampling error is local to econometric inference and does not generalize to a protocol-level regularity. The paper does not expose a new mechanism of protocol failure or coordination breakdown. It solves a measurement problem, not a system-level law.
