# A Protocol for Evaluating the Accessibility of AI-Generated Educational Materials: Prompt Configuration, WCAG-Derived Criteria, and Content Overload

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.00749
**Date read:** 2026-09-02
**Connected to:** L-004
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper proposing a formal evaluation protocol for measuring accessibility compliance of AI-generated educational content against WCAG standards. The work tests whether prompt engineering (explicit accessibility instructions vs. generic instructions) improves measurable compliance across multiple content modalities and generative tools.

## What I took from it

This is a canonical *instantiation* of L-004 (Goodhart Generalization: Metric Capture) rather than a challenge or extension of it. The paper operationalizes accessibility—an unmeasurable design goal involving user experience, cognitive load, and inclusive learning—into computable WCAG criteria, then measures whether prompt-based optimization improves those metrics. This creates the precise conditions for Goodhart dynamics: once WCAG compliance becomes a legible optimization target for prompt engineering, generative systems will optimize for WCAG checkpoints rather than accessibility itself. The title's reference to "content overload" suggests the researchers have already observed metric-proxy divergence (compliance metrics improving while user experience degrades). The work documents the *mechanics* of how an unmeasurable goal gets collapsed into measurable proxies, but does not theorize or test the downstream capture dynamics—making it useful as a case study of protocol formalization but not as evidence for the law itself.

## Research connections

- **L-004:** Direct instantiation—accessibility rendered as WCAG metrics, then used to optimize generative prompts; tests whether explicit metrics improve compliance without measuring actual accessibility outcomes.
- **seed-062 (Formalization Opacity Collapse — Automation Legibility):** Protocol formalizes an opaque design goal into transparent optimization targets; legibility enables automation but may degrade the original goal.
- **seed-077 (Metric-Induced Preference Ratcheting in Adaptive Systems):** Prompt optimization under WCAG metrics will ratchet system behavior toward metric satisfaction rather than accessibility; explores how adaptation shifts when targets become computable.

## Method note

This paper exemplifies a class of work that is *necessary but not sufficient* for protocol-law research: it documents the formalization moment (how unmeasurable goals become measurable proxies) but stops short of measuring the divergence that follows. Future work should pair such protocol specifications with longitudinal testing of whether optimized-for-metrics outputs diverge from user-centered outcomes, and whether this divergence is predictable from the structure of the proxy itself. The paper's implicit finding (content overload despite improved WCAG scores) should be formalized as a test case for L-004 divergence dynamics, not buried in the title.
