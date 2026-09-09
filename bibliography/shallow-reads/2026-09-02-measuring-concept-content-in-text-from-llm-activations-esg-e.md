# Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2608.07208
**Date read:** 2026-09-02
**Connected to:** L-019, seed-046
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A measurement paper proposing that frozen LLM activations can serve as a proxy for measuring concept presence in text, tested on ESG classification tasks. The work argues that internal model states encode richer semantic content than surface-level outputs, and that linear probes on these activations can replace task-specific fine-tuning for concept detection.

## What I took from it

The paper identifies a gap between internal LLM representation and expressed output—a legibility asymmetry common in automated systems. However, the core claim is instrumentalist: that we can *read* internal states to measure external concepts more accurately. This is a measurement technique, not a law-forming observation about how protocols behave under stress, adoption, or optimization pressure.

The work does touch on a relevant motif: the substitution of legible proxies (activation patterns) for unmeasurable targets (actual concept content in human judgment). But it does not present evidence that this substitution generates downstream distortions, gaming, or systematic protocol failure. It also does not generalize beyond measurement; it does not articulate a mechanism that would apply across different protocol architectures or domains. The ESG application is domain-specific validation, not cross-domain evidence.

## Research connections

- **seed-046:** Mentions embedded explanation opacity in LLM systems; this paper attempts to *reduce* that opacity via activation monitoring, but does not study what happens when that legible signal becomes an optimization target downstream.
- **seed-069:** Touches on transparency-as-trust-proxy dynamics, but from the measurement angle only, not from the equilibrium or capture angle.
- **L-004 (Goodhart):** Latent connection—if activation-based concept scores become used as ESG compliance signals, the conditions for metric capture would apply—but the paper does not study this failure mode.

## Seed

**Seed title:** Legibility-Induced Measurement Substitution in Opaque Systems

**Seed type:** question

**Seed text:** When internal states of opaque automated systems become legible via technical instrumentation (activation monitoring, probe extraction), do the legible proxies replace unmeasurable ground-truth targets in downstream protocols, creating a new layer of proxy-capture risk? The paper demonstrates that activation-based measures can out-perform surface metrics for concept detection, but does not study whether systems optimizing directly on these legible signals would distort the very internal representations being measured. This generalizes beyond LLMs: any system with hidden state + external measurement layer faces this risk once the measurement becomes protocol-observable.
