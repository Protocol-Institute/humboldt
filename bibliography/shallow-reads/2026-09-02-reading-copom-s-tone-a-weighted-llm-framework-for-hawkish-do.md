# Reading Copom's Tone: A Weighted LLM Framework for Hawkish-Dovish Sentiment, Forward Guidance, and Uncertainty

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2608.07251
**Date read:** 2026-09-02
**Connected to:** L-004, seed-019
**Kind:** application / measurement tool
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical implementation paper applying LLM-based sentiment classification to Brazilian central bank (Copom) monetary policy statements. The work operationalizes hawkish/dovish tone detection via weighted intensity scoring and extends prior iSent methodology across multiple dimensions (sentence-level classification, intensity weighting, uncertainty quantification).

## What I took from it

This is a competent instrumentation paper — it builds a measurement apparatus for a pre-existing construct (central bank tone) using contemporary NLP tools. The work sits downstream of the actual dynamic of interest: *what happens when forward guidance becomes legible and measurable to market agents*. 

The paper does not examine whether or how the availability of precise tone measurement changes agent behavior, protocol dynamics, or the effectiveness of forward guidance itself. It is a measurement *layer* added to an existing protocol (central bank communication), not an analysis of how that layer introduces new optimization pressures. The triage note correctly identifies L-004 (Goodhart Generalization) as the relevant risk — once hawkish/dovish tone becomes a computable, marketable metric, market agents will optimize against the tone signal itself rather than the underlying policy intent — but the paper does not investigate this. It is a tool paper, not a law investigation.

## Research connections

- **L-004:** The paper operationalizes exactly the kind of metric proxy that triggers Goodhart capture — turning implicit central bank communication intent into a legible, optimizable signal. No analysis of downstream effects.
- **seed-012:** Legibility-induced agent convergence: if this tone measurement becomes industry-standard, market agents will condition on it, potentially creating new coordination equilibria around the *measured tone* rather than the *actual monetary stance*.
- **seed-069:** Transparency-legibility as trust proxy substitution — the paper implicitly assumes that measuring tone increases transparency, but does not examine whether the computable metric becomes a substitute target for the unmeasurable thing (actual policy intent).

## Seed

**Seed title:** Metric Legibility Displacement in Opaque Policy Signaling
**Seed type:** question
**Seed text:** When a central bank's implicit or qualitative communication signal (tone, intent, forward guidance) is converted into a computable, market-readable metric via automated measurement (LLM-based or otherwise), does the availability of that metric change the strategic structure of the signaling game itself? Specifically: do optimizing market agents begin conditioning on the metric rather than the underlying policy, and does this feedback loop cause the central bank to either ossify its communication (to preserve signal consistency) or abandon transparency (to preserve signal privacy)? This would generalize beyond monetary policy to any domain where informal or high-dimensional institutional signals are rendered legible and market-actionable.
