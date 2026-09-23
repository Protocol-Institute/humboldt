# Policy Targeting with Binary Classification Trees: an Application to Rural Hospital Closures

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2609.13068
**Date read:** 2026-09-22
**Connected to:** L-004, seed-133
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper comparing classification tree algorithms (CART vs. MDFS) for identifying high-risk subgroups in policy targeting, applied to rural hospital closure prediction. The work is technical and domain-specific, focusing on algorithmic choice rather than examining how formalization of policy metrics itself shapes institutional behavior or locks protocols into particular failure modes.

## What I took from it

This is a *working example* of metric formalization at the operational level, but it does not investigate the mechanism by which formalization locks downstream behavior or creates paradigm resistance. The paper asks: which algorithm better identifies risk? It does not ask: what happens to institutional decision-making once a closure-risk metric becomes legible, computable, and actionable—i.e., how does metric formalization alter the strategic and operational surface of the system being measured?

The triage signal (seed-133, L-004) is reasonable but premature. The paper documents *how* to formalize a safety-critical prediction (hospital closure risk) into a targeting mechanism, but stops at algorithmic comparison. It does not examine whether hospitals that become legible as "high-risk" then change behavior in ways that either validate or invalidate the original metric, nor does it investigate institutional or regulatory lock-in around whichever algorithm becomes adopted as the standard.

## Research connections

- **L-004 (Goodhart Generalization):** Paper is silent on whether hospitals classified as high-risk subsequently change behavior in ways that either confirm or undermine the closure prediction, which is where metric capture manifests.
- **seed-133 (Metric Formalization as Paradigm Lock):** Paper documents formalization but not the lock. Lacks evidence on whether adoption of MDFS (or CART) creates institutional or regulatory stickiness that survives beyond its predictive usefulness.
- **seed-143 (Forensic Legibility Mandate Disconnect):** Implicit: once a hospital is classified as high-risk via tree algorithm, does the *enforcement* mechanism (regulatory intervention, funding withdrawal) align with the predictive threshold, or does legibility create a separate compliance surface?

## Method note

This paper illustrates a common research structure in applied policy science: optimize the measurement instrument, then apply it. The gap is that formalization research requires *post-deployment observation* of how legible metrics change the behavior of measured agents and how institutional commitment to a particular formalization persists even when empirical evidence drifts. A full read would be warranted only if the paper contained longitudinal data on hospital behavior *after* classification, or evidence of regulatory or institutional locking around the chosen algorithm. Neither appears present from the abstract.
