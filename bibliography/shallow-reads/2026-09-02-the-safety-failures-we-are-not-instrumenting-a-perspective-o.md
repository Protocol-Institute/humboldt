# The safety failures we are not instrumenting: a perspective on hidden safety-critical challenges in modern AI systems

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.19292
**Date read:** 2026-09-02
**Connected to:** L-013, L-007
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper identifying a category of safety failure in deployed AI systems: distributed, normalized, and non-legible failures that escape instrumentation and safety review precisely because they lack spectacularity or localized attribution. The argument is that modern AI safety discourse systematically undercounts these failures due to paradigm commitment to measurable, dramatic, or model-output-localized harms.

## What I took from it

The paper strengthens the case for **L-013** (Paradigm-Locked Anomaly Tolerance) by naming a specific mechanism: safety instrumentation itself becomes a selective filter that renders certain failure modes invisible to governance systems. When failures are distributed across components, normalized into workflow practice, or lack a single legible attribution point, they fall outside both measurement apparatus and review psychology. This is not mere oversight — it is structural blindness induced by the formalization of safety signals.

The paper also echoes **L-007** (Trust Ratchet in Safety-Critical Protocols) but from the negative angle: accumulated trust in deployed systems may rest on trust in *instrumentation* rather than actual absence of failure. As systems age without dramatic incidents, confidence grows — but only because the detection apparatus was never tuned to the quiet failures. The ratchet operates upward on visibility-biased evidence.

The core observation—that safety paradigms are *paradigm-locked* to certain failure categories—does not advance new mechanism understanding, but it does sharpen the conditions under which L-013 should be expected to operate most strongly: safety-critical domains with high operational maturity.

## Research connections

- **L-013:** Paradigm commitment to legible failures creates toleration windows for non-legible ones; safety instrumentation acts as a selective filter that locks paradigm focus.
- **L-007:** Trust accumulation in safety-critical protocols may depend on instrumentation confidence rather than actual risk reduction.
- **seed-068 (Unmeasurability as Anomaly Insulation):** Failures that remain unmeasurable or distributed across non-legible boundaries are insulated from detection and thus from intervention pressure.
- **seed-072 (Explanation-Marker Decoupling Under Scaled Legibility):** Safety explanations (incident reports, post-mortems, audit trails) are locked to *observed* failures; unobserved failures produce no explanation marker.

## Seed

**Seed title:** Instrumentation Paradigm Lock in Safety Governance

**Seed type:** observation

**Seed text:** Safety governance systems in protocol-based AI deployments become progressively locked to the failure modes their instrumentation can detect and formalize. Failures that are distributed, normalized across workflow layers, or lack single-point attribution surfaces are systematically tolerated not because they are accepted as safe, but because the governance apparatus has no legible signal for them. This creates a stability trap: as the system ages without dramatic failures, trust accumulates based on silence from instrumentation rather than evidence of absence. The condition is sharpest in safety-critical domains where formalization of metrics has been deepest, and the pattern should generalize wherever observability is bought through selective measurement rather than comprehensive instrumentation.
