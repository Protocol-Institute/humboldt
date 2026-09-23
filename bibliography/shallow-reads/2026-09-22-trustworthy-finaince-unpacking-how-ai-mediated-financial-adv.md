# Trustworthy FinAInce: Unpacking How AI-Mediated Financial Advice is Judged

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.20989
**Date read:** 2026-09-22
**Connected to:** L-007, seed-137
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A randomized vignette experiment (N=285) measuring how source labeling (AI vs. expert vs. community) shapes trust and safety appraisals of financial advice, holding recommendations constant. The work is primarily empirical and domain-specific (personal finance), designed to support UX/design decisions around AI advice disclosure.

## What I took from it

The paper demonstrates that *source label* dominates perceived trustworthiness of financial advice independent of recommendation quality—a behavioral finding, not a protocol mechanism. This touches L-007 (Trust Ratchet in Safety-Critical Protocols) but only as a snapshot: the experiment does not measure trust accumulation over operational time or stability, only initial appraisal conditional on source branding.

The more interesting signal for our inventory: the paper implicitly reveals an **incommensurability between how humans judge AI reasoning and how they judge expert reasoning**. Expert advice is appraised on perceived competence; AI advice appears appraised on legibility of process (or opacity anxiety). This suggests that when a protocol boundary exists between human-interpretable and machine-opaque decision sources, the *form of justification required* shifts, creating separate trust certification pathways. This is a coordination problem, not a technology problem—the protocol for accepting AI advice has not yet converged with the protocol for accepting expert advice, and source labels are being used as workarounds rather than solutions.

However, the paper does not investigate the *mechanism* of this incommensurability, nor does it track whether trust in AI advice changes under operational history (which would engage L-007 directly). It is a snapshot of label effects, not a law-seeking investigation.

## Research connections

- **L-007:** Partially engaged but not tested—measures initial trust appraisal, not accumulation over time or operational stability.
- **seed-137:** Confirms the observation that trust breaks down under protocol incommensurability (human vs. machine reasoning modes), but does not expose the mechanism.

## Seed

**Seed title:** none
