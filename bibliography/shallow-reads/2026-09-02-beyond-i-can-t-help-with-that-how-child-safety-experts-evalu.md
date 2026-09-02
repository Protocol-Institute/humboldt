# Beyond "I Can't Help With That": How Child Safety Experts Evaluate AI Chatbot Safety

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.07902
**Date read:** 2026-09-02
**Connected to:** L-012, seed-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical evaluation study grounding AI chatbot safety assessment in expert judgment and real-world child harm taxonomy rather than surface-level adversarial detection. The paper appears to argue that existing safety protocols conflate formal refusal signals with actual harm prevention, creating a legibility gap between what systems say they will not do and what actually protects youth in high-stakes contexts.

## What I took from it

The work surfaces a critical misalignment in how safety protocols are structured and measured: safety evaluation metrics optimize for detecting *refusals* and *adversarial inputs*, but these are poor proxies for the actual harms youth experience when interacting with systems. The optimization target (legible refusal behavior) has decoupled from the underlying goal (preventing real harm). This is a straightforward case of L-004 (Goodhart capture) — the measurable proxy has become the optimization point, and the system now performs well on the metric while failing the unmeasured objective.

However, the paper itself does not appear to propose a mechanistic account of *why* this displacement occurred or *how* it generalizes beyond the chatbot safety domain. It documents a failure mode but does not theorize the protocol-layer dynamics that produce it. The work is grounded, competent, and directly relevant to L-012 (Intervention-Layer Displacement), but it does not extend or challenge that law—it instantiates it in a new domain.

## Research connections

- **L-012:** Intervention-Layer Displacement in Automated Decision Protocols — Safety evaluation metrics become the target; the optimization pressure migrates from harm prevention to metric satisfaction.
- **L-004:** Goodhart Generalization: Metric Capture — Refusal behavior is a legible, measurable proxy for safety; under optimization pressure, systems optimize for the proxy rather than the unmeasured goal (real-world harm reduction).
- **seed-019:** [reference unclear in inventory; likely concerns proxy collapse or metric inversion in safety systems]

## Seed

**Seed title:** Safety Metric Inversion Under Legibility Pressure
**Seed type:** observation
**Seed text:** In safety-critical protocols where the unmeasurable goal (preventing real-world harm to vulnerable populations) is displaced by a measurable proxy (formal refusal behavior), the system optimizes for legible compliance signals rather than outcome protection. The shift occurs not because the proxy is wrong, but because it is precisely computable and subject to directed optimization, while the underlying harm remains distributed, context-dependent, and difficult to audit. This pattern should generalize to any safety protocol where the evaluation surface is more legible than the outcome surface.
