# Randomness in large language models: What researchers need to know (and report)

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.24372
**Date read:** 2026-09-02
**Connected to:** L-004, seed-054
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** —

## What this is

A methodological paper documenting sources of non-determinism in LLM outputs (sampling, silent updates, numerical rounding, expert routing) and arguing for standardized reporting of randomness parameters in research using LLMs as measurement instruments. The work targets reproducibility and reliability of LLM-based annotation, classification, and scoring tasks.

## What I took from it

This paper identifies a critical measurement protocol failure in the emerging use of LLMs as research instruments: the appearance of determinism (fixed prompt, fixed "settings") masks multiple stochastic mechanisms operating at different layers. This directly implicates L-004 (Goodhart Generalization), since researchers optimizing for apparent reproducibility by controlling visible parameters are blind to hidden sources of variation that corrupt the proxy reliability of their measurement.

The deeper observation is that LLMs as measurement tools violate a foundational assumption of classical research protocols—that repeated application of a procedure yields repeatable results. The paper does not theorize this as a governance or protocol design problem, but it documents a structural vulnerability in how measurement protocols interact with opaque, multi-layered optimization systems. The call for standardized *reporting* of randomness sources is pragmatic but suggests the research community is treating randomness as a transparency problem rather than as evidence of uncontrolled proxy capture in the measurement apparatus itself.

## Research connections

- **L-004 (Goodhart Generalization):** Researchers optimizing for control of visible parameters (prompt, temperature setting) while unmeasured sources of variation persist in the system; the proxy (apparent determinism) decouples from the actual goal (reproducible measurement).
- **seed-054:** Proxy reliability collapse under measurement protocol conditions; LLMs as measurement instruments exhibit silent failure modes that are invisible to standard validation procedures.
- **seed-062 (Formalization Opacity Collapse):** Formalizing measurement as "LLM + fixed prompt" creates an appearance of legibility while concealing operational sources of nondeterminism.

## Method note

This paper highlights a critical gap in research standards: documentation of what is *not* being controlled or reported in protocol-based research. When using systems with hidden stochastic mechanisms as measurement instruments, negative results (sources of variation discovered *after* publication) should be treated as protocol failures, not as minor reporting oversights. Future work using LLMs or similar opaque optimization systems as research tools should frontload adversarial discovery of hidden degrees of freedom before designing around them. Absence of evidence of randomness should not be treated as evidence of absence.
