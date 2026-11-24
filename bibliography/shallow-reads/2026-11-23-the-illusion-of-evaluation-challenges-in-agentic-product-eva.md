# The Illusion of Evaluation: Challenges in Agentic Product Evaluation Practice

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.26923
**Date read:** 2026-11-23
**Connected to:** L-004, L-013, seed-157
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A practitioner-facing analysis of evaluation methodology failure in agentic AI systems, arguing that standard model and harness-based evaluation instruments do not transfer to deployed product risk. The work identifies a systematic gap between what we can measure in controlled settings and what actually fails in production configurations.

## What I took from it

This is a crisp diagnosis of **L-013 (Paradigm-Locked Anomaly Tolerance)** in action: the evaluation research community has built consensus around a measurement regime (model capabilities + sandboxed agent behavior) that is *formally tractable but operationally decoupled* from the actual risk surface of deployed systems. The paper suggests that this measurement regime persists not because it works, but because it is legible and publishable — a classic case of metric capture masquerading as method.

The work also implies a deeper coordination problem: the entities conducting evaluation (academic researchers, model teams, internal safety groups) are optimizing for different objectives (publishability, stakeholder reassurance, controllability) than deployed product risk. This creates what might be called **proxy-layer stratification** — multiple evaluation regimes coexist, each generating evidence that locally validates the system while globally missing failure modes. The paper hints that pre-deployment testing is structurally insufficient not just in degree but in kind: it cannot surface the interactions between agent autonomy, permissioning, data access, and operating conditions that only emerge under deployment.

## Research connections

- **L-004 (Goodhart Generalization):** Evaluation metrics (benchmark performance, sandboxed safety tests) become decoupled from actual risk under deployment optimization pressure; the metric survives while the underlying risk evolves.
- **L-013 (Paradigm-Locked Anomaly Tolerance):** The evaluation paradigm tolerates accumulating evidence of non-transfer (failed predictions, post-deployment surprises) without triggering methodological restructuring.
- **L-012 (Intervention-Layer Displacement):** When evaluation becomes the legible input to deployment decisions, optimization pressure moves upstream toward making evaluation pass rather than toward actual safety.
- **seed-157:** (not visible in provided seed pool — triage note references it; likely concerns evaluation opacity in adaptive systems)
- **seed-554 (Formal Risk Category Lag):** Evaluation frameworks formalize risk categories from prior operational regimes; new risk classes (tool interactions, permission cascades) remain uncategorized until post-deployment.
- **seed-452 (Legitimacy Collapse Under Macro Formalization):** As evaluation becomes more formal and institutionalized, it gains authority without gaining accuracy, creating a legitimacy-verification gap.

## Method note

This paper suggests that research on protocolized systems should not treat evaluation methodology as external infrastructure; it *is* part of the protocol system itself, and subject to the same laws of ossification, proxy capture, and paradigm lock as the systems it measures. Future work should explicitly model the incentive structure of evaluators as part of the protocol dynamics — evaluation is not a neutral measurement layer but an active layer that shapes what gets deployed and tolerated. This implies that understanding agentic product failure requires studying not just product behavior but the meta-protocol of how evaluation regimes themselves are adopted, defended, and displaced.
