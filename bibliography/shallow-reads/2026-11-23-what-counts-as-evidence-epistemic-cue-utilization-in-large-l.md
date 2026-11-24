# What Counts as Evidence? Epistemic Cue Utilization in Large Language Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.12788
**Date read:** 2026-11-23
**Connected to:** L-004, seed-157
**Kind:** meta
**Escalation:** store-only

## What this is

Empirical benchmark study measuring how 13 LLMs weight different epistemic cues (source reliability, temporal markers, presentation format) when sources conflict. Uses 500 controlled scenarios to separate cue recognition from actual influence on model outputs, revealing systematic decoupling: models can accurately report source reliability while being shaped by entirely different signals in practice.

## What I took from it

This is methodologically valuable for the new nature research program because it operationalizes a core investigative technique: **separating stated recognition of a legible signal from actual behavioral conditioning on that signal**. This gap—what the paper calls the cue utilization gap—is empirically measurable and varies systematically across models.

The finding directly instantiates a pattern relevant to L-004 (Goodhart Generalization) and L-012 (Intervention-Layer Displacement). Models can "know" which source is reliable but optimize on orthogonal signals (formatting, recency, citation density) when those signals become legible optimization targets. This is not noise or error—it's reproducible and model-specific, suggesting that under sufficient optimization pressure, the proxy (recognizable source cues) decouples from actual decision-making, leaving the formal signal intact while behavior drifts.

The methodology also demonstrates that **legibility asymmetry** (the model can articulate one thing but do another) is not a bug that research can ignore—it's a stable equilibrium worth measuring directly. This suggests future law work should routinely distinguish between protocol-layer claims and execution-layer actual behavior.

## Research connections

- **L-004 (Goodhart Generalization):** Direct evidence that legible epistemic proxies (source reliability markers) remain cognitively recognized while decision-making shifts to competing, often less defensible signals when those become optimizable.
- **L-012 (Intervention-Layer Displacement):** When source cues become formally specified inputs, optimization pressure migrates to adjacent dimensions (presentation, temporal markers) rather than respecting the formal hierarchy.
- **seed-157:** (inferred from triage note) Directly measures epistemic cue utilization under legibility conditions.
- **seed-276 (Legibility-Induced Measurement Substitution in Opaque Systems):** Demonstrates that formalized epistemic markers can coexist with substituted decision logic.
- **seed-515 (Computable Belief as Collusion Surface):** Models' ability to report reliable-source judgments while ignoring them suggests computable beliefs function as decoy or collusion surface rather than control points.

## Method note

This paper models an underused investigative pattern for protocol research: **the direct measurement of recognition-behavior divergence under controlled conditions**. Rather than inferring decoupling from outcome patterns, it isolates the gap using benchmark scenarios where ground truth is known and multiple signaling dimensions can be held or varied independently. This suggests future law work should routinely construct scenarios where agents must choose between multiple legible signals and measure which signals actually move outputs—not which agents claim to follow. The paper also shows this divergence is **model-specific and reproducible**, implying it reflects stable system properties, not random failure, and thus belongs in the law inventory rather than dismissed as noise.
