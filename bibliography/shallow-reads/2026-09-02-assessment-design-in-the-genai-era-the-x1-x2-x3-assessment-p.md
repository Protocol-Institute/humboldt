# Assessment Design in the GenAI Era: The X1-X2-X3 Assessment Pattern for Testing Students' AI Literacy, Learning Outcomes, and Reflection

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.12351
**Date read:** 2026-09-02
**Connected to:** L-004
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A case study reporting on a three-part assessment design (X1-X2-X3) deployed in a second-year undergraduate database systems module to preserve learning outcome validity under GenAI availability. The work combines documentation of sourced answers, student-generated answers, and comparative evaluation to surface AI literacy and reflection rather than raw knowledge reproduction.

## What I took from it

This is a **local adaptation response** to metric capture in action — it does not theorize the capture itself or offer a mechanism that generalizes beyond educational assessment. The paper observes that traditional assessments (reproduce knowledge, solve problem correctly) become Goodhart-vulnerable once GenAI can perform them costlessly, and proposes a structural workaround: shift the measurable target from correctness to *process visibility and critical judgment*.

This is important to document, but it is a **symptom diagnosis and engineering patch**, not a primary source advancing a law. The paper does not investigate why educational institutions face this particular form of metric capture, how the capture propagates across other domains with similar structure (audit, compliance, evaluation), or what systemic pressures prevent institutions from abandoning the invalid metric altogether rather than layering verification onto it. It treats the problem as local to assessment design rather than as an instance of a generalizable protocol dynamics.

## Research connections

- **L-004:** Confirms that measurable proxies (correctness score) become optimization targets under pressure; the proposed solution is to add a secondary verification layer (process documentation) rather to replace the proxy.
- **seed-072:** Implicit: the X1-X2-X3 structure attempts to decouple the explanation (student reasoning) from the marker (final answer), but does not address whether the *second-order marker* (process quality) itself becomes gamifiable.
- **seed-082:** The addition of X2 and X3 layers is an additive intervention into an overloaded protocol (assessment must simultaneously measure knowledge, deter cheating, and enable learning); it may preserve root pressure on the foundational metric rather than resolve it.

## Method note

This paper exemplifies how **applied domains (education, compliance, auditing) generate live case studies of protocol dynamics** before those dynamics are theorized. The escalating adoption of GenAI creates natural experiments in metric capture and verification layering that are visible in real time. Future deep reads should attend to whether local engineering solutions (X1-X2-X3 patterns, multi-stage audits, human-in-the-loop verification) reveal structural limits — i.e., whether they stabilize or merely postpone capture at the next layer. This suggests that research on the new nature should maintain systematic attention to applied literature in regulated and safety-critical domains, not only to academic computer science.
