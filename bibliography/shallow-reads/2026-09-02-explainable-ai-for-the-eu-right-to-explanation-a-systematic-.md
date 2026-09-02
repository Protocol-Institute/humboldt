# Explainable AI for the EU Right to Explanation: A Systematic Review of the Law-XAI Translation Gap

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.02699
**Date read:** 2026-09-02
**Connected to:** L-015, seed-026
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systematic literature review mapping the gap between EU legal mandates for algorithmic explainability (GDPR Art. 15(1)(h), AI Act Art. 86) and what XAI methods can actually deliver in practice. The paper documents a translation problem: law assumes "explanation" is a legible, singular, contestable artifact; XAI research produces interpretability techniques that may satisfy technical measures but not legal sufficiency or user comprehension.

## What I took from it

This is empirical confirmation of **L-015** (Interpretive Continuity Decay in Distributed Governance Protocols) operating at the law-AI interface. The paper shows that formal legal records—statutes, regulatory guidance, audit trails—survive intact while the institutional capacity to interpret and apply them decays. Specifically: lawyers write rules assuming "explanation" is meaningful to humans; XAI researchers build systems that are mathematically explainable but incomprehensible to affected parties; regulators cannot close the gap because neither community speaks the other's language.

The work also touches **seed-026** (interpretive gap under scaled legibility): as decision-making systems scale and become more opaque, legal frameworks freezing the *form* of explanation (e.g., "provide an explanation") lose grip on *function* (whether the person can actually understand or contest it). The paper suggests that the problem is not that XAI fails to explain—it's that "explanation" was never operationalized in law with sufficient precision to translate into a protocol. This is institutional paradigm-lock under computable legality pressure.

## Research connections

- **L-015:** Formal law and XAI audit trails survive; shared institutional meaning of "explanation" decays across the law-technical boundary.
- **seed-026:** Legibility of compliance (XAI method deployed) decouples from legibility of meaning (user/regulator comprehension).
- **seed-069:** Explanation-as-transparency becomes a trust proxy substituted for actual contestability in asymmetric-knowledge protocols (decision-maker vs. affected party).
- **seed-072:** Explanation-marker decoupling: systems produce explanations (markers) that formal audit shows are present, while actual explanation (causal understanding enabling contestation) is absent upstream.

## Method note

This review models an important research operation: documenting *not* where a protocol works, but where two governance layers (law and technology) share a vocabulary but lose semantic coherence under translation. Such work should be elevated when it shows that the failure is structural—neither side is "wrong," but the protocol linking them is underspecified. The paper's value lies in demonstrating that law-technology translation gaps are themselves lawful phenomena, not merely implementation failures. Future systematic reviews should explicitly map which portions of a legal mandate remain unformalized in the technical layer, and vice versa.
