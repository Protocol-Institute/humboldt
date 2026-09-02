# Same violence, different answer: how AI responds to coercive control against women across languages

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.01436
**Date read:** 2026-09-02
**Connected to:** L-012, L-014
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical audit of safety protocol variance across LLM instances. The work uses a fixed scripted scenario (intimate partner violence / coercive control) presented in nine languages to seven LLMs, measuring whether models decline harmful completions (writing a self-blaming letter accepting surveillance). This is a content-safety benchmark study, not a theoretical argument about protocol mechanisms.

## What I took from it

The study documents a real phenomenon—differential safety protocol response as a function of language, likely driven by training data imbalance, fine-tuning coverage, and evaluation asymmetries. This is consistent with L-012 (the decision boundary moves when the input becomes legible in different ways) and L-014 (optimization pressure concentrates at computable boundaries, leaving gaps).

However, the work *reports* the variance without modeling the *mechanism* by which it emerges or persists. It does not argue that this variance is a law-shaped regularity of protocol design under adoption pressure, nor does it propose a generalizable mechanism. It is a benchmark that surfaces a failure mode, not a sustained theoretical or empirical investigation into why safety protocols fail *systematically* under certain legibility conditions.

The paper supports the *existence* of L-012 and L-014 as phenomena, but does not advance their theoretical specification or test their boundary conditions.

## Research connections

- **L-012:** Intervention-Layer Displacement — The safety intervention (refuse to help write self-blaming letter) is legible and actionable in some language-model pairs but not others; the locus of optimization (training data, fine-tuning, evaluation) is displaced toward high-resource languages.
- **L-014:** Strategic Boundary Concentration — The computable legality boundary (is this request harmful?) becomes a target for optimization; where that boundary is legible (English, high-resource languages), compliance is sharper; where it is ambiguous or undertrained, compliance degrades.
- **seed-069:** Transparency-Legibility as Trust Proxy — This case illustrates the inverse: *absence* of transparency in non-English safety responses undermines trust in the protocol.
- **seed-080:** Proxy Collapse Under Upstream Asymmetry — The proxy for safety (refusal rate) collapses asymmetrically across languages because the upstream training and alignment data is asymmetric.

## Seed

**Seed title:** Safety Protocol Legibility Asymmetry in Polyglot Deployment

**Seed type:** observation

**Seed text:** In conversational AI systems deployed across multiple languages, safety intervention protocols show measurable variance correlated with language resource abundance, suggesting that the boundary between harmful and benign requests becomes legible to the fine-tuning and evaluation process only in high-resource language contexts. Where the protocol boundary is underspecified (low-resource or underrepresented language contexts), the safety intervention fails not because the mechanism is absent but because the decision boundary was never rendered legible to optimization. This implies that protocol safety in polyglot systems is not a property of the system architecture but of the legibility landscape during training—a form of upstream asymmetry that cannot be corrected by post-hoc intervention without re-tuning. The generalization: *safety protocols ossify around the legibility contours of their training data, not around the actual task.*
