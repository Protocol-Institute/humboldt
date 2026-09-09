# Quantifying Inefficiency

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2412.11984
**Date read:** 2026-09-02
**Connected to:** L-004
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper axiomatizing a cardinal social inefficiency function that assigns numerical measures to alternatives based on von Neumann-Morgenstern preferences, without exogenous interpersonal comparison or outside options. It frames inefficiency as endogenously normalized per-capita utility loss.

## What I took from it

This work provides formal machinery for *measuring* inefficiency in protocol outcomes, which is foundational scaffolding for studying L-004 (Goodhart Generalization), but it does not itself interrogate what happens when protocols *optimize toward* such measurements. The paper is upstream of the dynamic we track: it solves the "what is inefficiency?" question mathematically, but leaves open the question of how optimizing agents degrade or distort efficiency metrics under protocol pressure.

The axiomatization is elegant precisely because it brackets the question of measurement capture—it assumes stable preferences and does not model strategic behavior around the metric itself. This is appropriate for the paper's goal (establishing a cardinal comparison), but means it cannot illuminate L-004's core claim: that any measurable proxy for an unmeasurable goal (e.g., "social utility") becomes corrupted under sustained optimization pressure. The paper is a measuring rod; we need to track what happens when agents bend the rod.

## Research connections

- **L-004:** Provides formal toolkit for defining "social inefficiency" as a measurable quantity; confirms that cardinal comparison is possible without external grounding, but does not address what happens when protocols optimize toward such metrics.
- **seed-077:** Metric-Induced Preference Ratcheting — the axiomatization is metric-neutral but could serve as baseline against which to measure ratcheting effects in actual protocol deployment.

## Method note

This work exemplifies a useful pattern: axiomatically establish a *static* measurement framework first, then layer in dynamics (agent optimization, strategic distortion, temporal evolution). For the new nature research agenda, we should note that foundational measurement papers like this are necessary preconditions but cannot themselves detect protocol-induced measurement capture. The next move would be to study how protocols using this inefficiency function as an optimization target diverge from the axiomatically justified baseline. Store for reference in the L-004 evidence stream.
