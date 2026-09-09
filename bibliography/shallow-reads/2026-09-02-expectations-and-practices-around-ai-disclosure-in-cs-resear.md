# Expectations and Practices around AI Disclosure in CS Research

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.23271
**Date read:** 2026-09-02
**Connected to:** L-003, seed-018
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical survey work documenting gap between stated AI disclosure policies at CS venues and actual researcher practice/interpretation. Primary contribution is descriptive (policy audit + N=109 survey) rather than theoretical or mechanistic; does not present a sustained argument about *why* the gap persists or what cascades from it.

## What I took from it

The paper confirms the operational premise of L-003 (Formalization Ratchet) — that policymakers respond to coordination stress (AI use in research) by formalizing previously informal norms into legible disclosure rules. However, the finding that policies remain "highly under-specified" is significant: it suggests that the formalization *attempt* fails to resolve ambiguity at the point of application. This creates a second-order coordination problem — researchers cannot reliably encode compliance because the protocol itself does not specify what "AI use" or "responsible disclosure" means operationally.

This differs from the classic ossification pattern (L-001). Instead, it maps onto **seed-062 (Formalization Opacity Collapse)**: the act of rendering disclosure "formal" (mandatory, policy-codified) collapses into opacity because formalization without legible operationalization leaves agents guessing. The gap between policy text and practice suggests that stress → formalization → under-specification → noncompliance or gaming. This is a failure mode of the Formalization Ratchet itself.

## Research connections

- **L-003:** Confirms that stress (AI adoption) triggers formalization of informal norms (disclosure); unclear whether policies actually improve coordination or simply create surface legibility.
- **seed-018:** Direct evidence that disclosure policies function as coordination ratchets, but ratchet may be mechanically broken (under-specification prevents reliable compliance).
- **seed-062:** Formalization without legible operationalization creates opacity at enforcement point; formal policies may mask rather than solve the underlying coordination problem.
- **seed-068 (Unmeasurability as Anomaly Insulation):** If "responsible AI use" remains unmeasurable, formal disclosure may insulate the protocol from pressure to actually clarify what counts as compliance.

## Method note

This work demonstrates the value of auditing the gap between policy text and researcher interpretation *before* attempting to evaluate policy efficacy. It suggests that meta-research on protocol design should routinely include legibility audits: does the formal rule actually specify what agents are supposed to do? The finding that policies are under-specified is itself a replicable methodological signal — if formalization produces underspecification at scale, that is a pattern worth instrumentalizing into future protocol design research. Future work should track whether under-specification of disclosure policies correlates with increased opacity in AI use (agents hide use rather than disclose it ambiguously) or with convergent workarounds.
