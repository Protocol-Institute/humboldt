# Calibrating WEAT Against Anisotropy: ZCA Whitening as a Geometric Pre-Processing Step for Embedding Association Tests

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.06908
**Date read:** 2026-09-02
**Connected to:** L-004
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical methods paper proposing a geometric correction (ZCA whitening) to improve the validity of WEAT, a widely-used bias measurement protocol for language embeddings. The work addresses a known mismatch between WEAT's assumption of isotropic embedding spaces and the anisotropic geometry of real language models.

## What I took from it

This is a **calibration paper**, not a law-generative one — it improves measurement fidelity within an existing protocol rather than revealing how protocols break or stabilize under pressure. However, it is directly relevant to L-004 (Goodhart Generalization: Metric Capture) as a case of *defensive metrication*: the authors are attempting to shore up a measurement proxy before it becomes a widespread optimization target.

The deeper problem the paper surfaces is that WEAT's reliability depends on unstated geometric assumptions that vary across embedding architectures. This means bias metrics were already subject to Goodhart capture—organizations optimizing against WEAT scores were optimizing against a proxy whose validity was unknown and geometry-dependent. The ZCA correction is a necessary but partial fix: it restores isotropic assumptions, but does not address whether "semantic association distance" is the right unmeasurable goal being proxied. The paper assumes the protocol is sound; it corrects only the measurement instrument.

This suggests **protocol robustness often requires hidden geometric or structural assumptions to remain opaque**—making them explicit and correcting for them may paradoxically invite agents to optimize around the corrected metric in new ways.

## Research connections

- **L-004:** WEAT is a measurement proxy for unmeasurable bias; its capture has likely already occurred in fairness-optimizing systems. ZCA correction is mitigation, not prevention.
- **seed-062 (Formalization Opacity Collapse):** Rendering a measurement rigorous exposes its assumptions and invites optimization around the now-legible correction.
- **seed-069 (Transparency-Legibility as Trust Proxy Substitution):** Publishing the anisotropy problem and its fix may shift trust from "WEAT works" to "WEAT is now corrected"—a substitution of one proxy for another.

## Method note

This paper exemplifies a recurrent pattern in protocol measurement research: identifying and correcting for a hidden structural violation (anisotropy) tends to *increase* the legibility and thus the optimizability of the metric, not reduce it. Future work on protocol measurement should distinguish between corrections that make a proxy *more valid* and those that make it *more legible-to-gaming*. The fact that this correction is presented as a methodological improvement may obscure that it simultaneously increases the surface area for strategic metric capture.
