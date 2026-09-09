# Difference-in-Differences on a Censored Rating Scale Can Manufacture an Effect: Evidence from a Pre-Registered LLM-Judge Audit

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.27309
**Date read:** 2026-09-02
**Connected to:** L-004, seed-016
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological critique demonstrating that difference-in-differences estimators applied to bounded rating scales produce spurious interaction effects due to censoring. The paper shows how standard LLM-judge audit designs—which double-difference within-item contrasts across manipulated attributes—conflate true preference shifts with differential attenuation (ceiling/floor effects), manufacturing statistically detectable bias signals where none exists substantively.

## What I took from it

This is a technical indictment of a specific measurement protocol widely deployed in LLM fairness auditing. It does not theorize protocolized systems or their dynamics; instead, it exposes how a particular research *method* for certifying protocol behavior can itself become a source of artifact.

The relevance to L-004 (Goodhart Generalization: Metric Capture) is narrow and mechanical: the paper shows one specific way a proxy—the bounded rating scale—fails to isolate the quantity of interest when optimization pressure (the audit design) meets geometric constraint (censoring). This is a **failure mode of measurement**, not a law of protocol systems themselves.

The connection to seed-016 is similar: it illustrates measurement-induced bias in stopping-rule substitution (auditors stop at the double-difference because it is statistically "clean," ignoring that cleanness is an artifact). But this is a meta-level observation about research practice, not about how protocolized systems themselves evolve.

## Research connections

- **L-004:** Confirms one mechanism by which a proxy (rating scale) fails to track its target (true bias) under measurement-driven optimization, but the failure is measurement-geometric, not protocol-dynamic.
- **seed-016:** Illustrates how stopping rules in audit design can create illusions of effect through censoring artifacts, but this is about research methodology, not system behavior.
- **none** (to open lines of inquiry): This paper does not generalize to L-008 through L-016, which concern how protocol systems themselves respond to legibility and optimization pressure, not how we measure them.

## Method note

This paper demonstrates the necessity of pre-specification and sensitivity analysis in audit design, particularly when using bounded outcome spaces. It suggests that auditing protocols relying on bounded scales with potential floor/ceiling effects require explicit modeling of attenuation or use of uncensored intermediate measures. More broadly, it signals a risk in the current research ecosystem: well-intentioned standardization of audit methods (double-difference design) can calcify around a measurement artifact, creating false consensus that a bias signal is real when it is an artifact of scale geometry. Future meta-reviews of LLM audits should include censoring diagnostics as a standard check.
