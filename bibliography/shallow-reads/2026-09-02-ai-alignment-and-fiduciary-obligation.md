# AI Alignment and Fiduciary Obligation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.02660
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A normative/applied ethics paper extending fiduciary obligation frameworks from human relationship domains (bioethics, care ethics) to AI-user interaction in a triad structure (user-AI-developer). The work identifies alignment criteria by analogy to established moral traditions rather than deriving new mechanism or empirical pattern.

## What I took from it

The paper frames alignment as a fiduciary duty problem — treating the unmeasurable goal (user flourishing, trustworthiness, genuine benefit) as the anchor for obligation rather than any computable proxy. This echoes L-004 (Goodhart Generalization) in that fiduciary framing *resists* metric capture by design: the duty is precisely to optimize for the non-legible goal, not a measurable signal.

However, the work does not investigate what happens when fiduciary obligation itself becomes protocol-formalized — when the unmeasurable goal gets operationalized into computable compliance checks (as in L-012's displacement mechanism). The paper stays in normative space. It identifies the right *target* for alignment but does not examine the institutional or protocol mechanisms that would preserve that target under scaling, competition, or audit pressure — which is where the new nature emerges.

## Research connections

- **L-004:** Fiduciary obligation is presented as the antidote to metric capture, but the paper does not examine what happens when fiduciary duty itself is formalized into a measurable compliance regime.
- **L-012:** Mentions developer-in-triad but does not explore how legible accountability signals (e.g., safety audits, alignment metrics) displace the locus of actual optimization away from the user's unmeasurable interest.
- **seed-068:** Touches on the possibility that unmeasurability acts as insulation against capture, but does not develop it mechanistically.

## Seed

**Seed title:** Fiduciary Formalization Paradox — Unmeasurable Duty Under Legible Enforcement

**Seed type:** question

**Seed text:** When a fiduciary obligation (defined as fidelity to an unmeasurable goal) is embedded in a protocol system requiring computable compliance signals, the enforcement layer necessarily selects for measurable proxies of the duty. This creates a displacement: agents optimize for the legible fiduciary *marker* (audit compliance, alignment score, disclosed reasoning) rather than the duty itself. Does this pattern hold across other domains where normative or relational obligations are forced into protocol form? And if so, does formalizing unmeasurable duties accelerate their conversion into metric-capture problems rather than prevent it?
