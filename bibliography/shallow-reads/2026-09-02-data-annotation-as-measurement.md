# Data Annotation as Measurement

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.07297
**Date read:** 2026-09-02
**Connected to:** L-004
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological critique of how annotation quality is evaluated in AI systems. The paper argues that treating inter-annotator agreement as a proxy for annotation validity mistakes measurement validity for reliability, and proposes framing annotation as a genuine measurement problem with construct validity requirements.

## What I took from it

This is a meta-level observation about how a key protocol substrate (the labeled dataset) collapses validity into a legible but misleading metric. The paper identifies a case where Goodhart's law operates *silently*: agreement becomes the optimization target precisely because it is computable and auditable, while the unmeasurable question ("does this label capture the concept?") atrophies from the research agenda. 

The relevance is not to annotation systems themselves but to how protocolized systems inherit measurement assumptions from their training substrate. If L-004 (Goodhart Generalization) predicts metric capture under optimization pressure, this paper documents the *anterior* failure: the metric was never validated as measuring the right thing. This suggests a predecessor mechanism — call it **measurement-construct decay** — where protocols adopt proxies not because they were optimized away from a valid target, but because the valid target was never established in the first place. The paper does not theorize this, but it documents the pattern.

## Research connections

- **L-004:** Illustrates proxy capture at the *foundation* of AI training pipelines, before optimization pressure is applied. Agreement is chosen as a proxy not under pressure but by default, suggesting Goodhart operates on pre-existing measurement failures, not only on downstream optimization.
- **seed-068 (Unmeasurability as Anomaly Insulation):** The paper shows how relegating validity to the unmeasurable domain (while keeping reliability legible) insulates the protocol from detecting construct failure.
- **seed-072 (Explanation-Marker Decoupling Under Scaled Legibility):** Agreement metrics decouple from whether annotations explain the underlying concept; scaling annotation pipelines amplifies this decoupling.

## Method note

This suggests that research on protocolized systems should include *genealogical audits* of foundational metrics — tracing backward from deployed proxies to ask whether they were ever validated against their target construct. Meta-research on AI systems needs to examine not just how metrics are gamed under pressure, but how invalid metrics become entrenched *before* pressure applies. The paper reveals that documentation of inter-annotator agreement can mask rather than evidence measurement validity, suggesting that audit trails and legible records are not sufficient substitutes for foundational validity work.
