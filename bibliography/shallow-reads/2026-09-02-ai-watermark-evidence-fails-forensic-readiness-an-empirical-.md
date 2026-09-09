# AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.16010
**Date read:** 2026-09-02
**Connected to:** L-002, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical evaluation paper testing whether three representative LLM watermarking methods (KGW, Unigram, SynthID-Text) produce detection evidence robust enough to meet legal standards for court admissibility. The paper measures false positive rates, robustness to removal attacks, and detection reliability across different deployment scenarios — directly challenging the forensic fitness of mandates in the EU AI Act and California SB 942 that assume watermarks provide "reliable" proof of LLM generation.

## What I took from it

The paper demonstrates a **hardness asymmetry** in watermark verification: embedding is computationally cheap and scales easily, but detection produces unreliable signals under adversarial or noisy conditions (false positives spike under paraphrase, text truncation, cross-language translation). This is a concrete instantiation of L-002, but the deeper pattern is the **legalization-without-mechanism problem**: lawmakers have rendered a technical obligation (watermarking) computable and legally binding (California SB 942: "permanent or extraordinarily difficult to remove") without empirical evidence that the verification function actually works at forensic threshold. 

The result is a protocol where the verification burden has been formally assigned to watermarks, but the verification signal is demonstrably insufficient. This creates a trap: jurisdictions that mandate watermarking legally must treat detection as evidence, but detection fails under real-world conditions. The system is now locked into a legible compliance target (watermark presence) that does not deliver the claimed function (forensic-grade proof of origin). This is a form of **strategic boundary concentration** (L-014) — the law has crisply defined the obligation (watermarks) to make it machine-readable and enforceable, but enforcement now rests on a verification mechanism that cannot meet the implicit forensic standard.

## Research connections

- **L-002 (Hardness Asymmetry):** Watermark embedding is trivial; detection under adversarial conditions (paraphrase, truncation, translation) fails reliably. Verification cost rises sharply; execution cost stays flat.
- **L-014 (Strategic Boundary Concentration Under Computable Legality):** Legal mandate has rendered watermarking a precisely computable obligation, but the legible target (watermark presence) decouples from the actual goal (forensic proof of origin).
- **seed-080 (Proxy Collapse Under Upstream Asymmetry in Automated Systems):** Watermark detection acts as a proxy for "LLM-generated." The proxy collapses under adversarial text transformation because the upstream signal (watermark robustness) was asymmetrically weak in deployment.
- **L-013 (Paradigm-Locked Anomaly Tolerance):** Jurisdictions may tolerate accumulating evidence of watermark unreliability (this paper's findings) because the mandate is already law and reversing it is politically costly.

## Seed

**Seed title:** Forensic Legibility Mandate Disconnect — Verification Without Threshold

**Seed type:** observation

**Seed text:** When regulatory bodies mandate a technical mechanism (e.g., watermarking) and render compliance legible and computable (verifiable presence of watermark), the system can lock in place even if the mechanism cannot meet the underlying forensic or evidentiary standard it was meant to serve. The legal obligation becomes decoupled from the functional requirement. The system is now in a state where enforcement points to a legible signal (watermark presence/absence) that does not reliably indicate the target condition (true origin). This pattern may generalize to any domain where law formalizes a proxy before the proxy's reliability is empirically validated at the threshold where it will be used.
