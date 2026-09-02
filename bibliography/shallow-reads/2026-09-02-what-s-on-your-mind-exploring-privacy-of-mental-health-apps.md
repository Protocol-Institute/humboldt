# What's on Your Mind? Exploring Privacy of Mental Health Apps

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2605.02016
**Date read:** 2026-09-02
**Connected to:** L-012, seed-019
**Kind:** empirical survey
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A static and dynamic analysis of privacy practices across 25 popular Android mental health and life-coaching apps (Replika, Headspace, etc.), examining how user-generated sensitive data (mental health disclosures, trauma, desires) are handled, stored, and transmitted. Standard privacy audit paper in the applied security domain.

## What I took from it

The paper documents privacy vulnerabilities and data-handling gaps in mental health apps — a domain where user input is semantically legible (therapy transcripts, mood logs, etc.) and therefore valuable for downstream optimization (targeting, monetization, model training). This instantiates L-012's prediction: when prediction inputs become formalized and legible, optimization pressure shifts downstream. However, the paper does not theorize the *mechanism* by which legibility drives protocol mutation, nor does it examine whether privacy-protective protocol layers themselves become optimization targets. It is a competent case study without sustained theoretical claim about how protocols evolve under legibility pressure.

The work confirms that sensitive-data protocols attract extraction pressure, but does not distinguish between extraction-as-violation and extraction-as-protocol-redesign. This is empirical ground truth for L-012 but not a mechanism inquiry.

## Research connections

- **L-012:** Prediction inputs (mental health disclosures) are formalized as legible data; optimization pressure concentrates at extraction boundaries rather than on therapeutic protocol itself.
- **seed-019:** Privacy protocols become surfaces for computable enforcement and audit; this legibility makes them targets for boundary-shifting optimization.
- **seed-069:** Apps present "transparency" and "privacy policies" as trust proxies while actual data flow remains opaque — legibility-as-substitution.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
