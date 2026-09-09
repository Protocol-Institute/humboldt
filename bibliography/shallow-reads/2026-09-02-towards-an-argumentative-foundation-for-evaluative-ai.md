# Towards an Argumentative Foundation for Evaluative AI

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.07473
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper proposing computational argumentation as a formal foundation for evaluative AI systems that present competing hypotheses with evidence rather than single recommendations. The work positions itself as a design approach to prevent metric capture and recommendation capture by making decision inputs contestable and explicitly structured.

## What I took from it

The paper frames the problem at the intervention-layer level: by refusing to collapse competing claims into a single output, argumentation-based systems attempt to prevent the displacement of optimization pressure from the unmeasurable evaluative goal onto a legible proxy (L-004, L-012). However, the paper does not examine what happens when argumentation *itself* becomes the legible object — when argument structure, strength metrics, or evidence weighting become optimizable targets. There is no engagement with the possibility that formalization of "competing hypotheses" creates new capture surfaces rather than preventing them. The work is normative rather than empirical about protocol behavior under optimization pressure.

The meta-level interest is stronger: this paper advocates for *deliberately preserving interpretive pluralism* in a formal system, which is an unusual design stance. It suggests awareness that making decision inputs fully computable may be counterproductive, but it does not ground this in protocol-scale analysis of what pluralism costs or how it degrades under scale.

## Research connections

- **L-004:** The paper proposes argumentation as a design constraint *against* metric capture, but does not examine whether argumentation frameworks themselves become capture surfaces.
- **L-012:** Directly relevant — argumentation preserves multiple intervention layers (evidence layer, argument-structure layer, evaluation layer) rather than collapsing them into a single legible prediction-to-action pipeline.
- **seed-071:** The work implicitly argues that contestability and expressiveness cannot be fully compressed into computable protocols — governance as irreducible residual.
- **seed-069:** The paper does not address whether "evidence for and against" functions as a trust proxy substitute rather than a mitigation.

## Method note

This paper models a design philosophy (pluralism under formalization) rather than testing protocol behavior. The Humboldt inventory would benefit from empirical work on whether argumentation-based systems actually resist metric capture or merely displace it to meta-layer (which arguments are salient, which evidence weighs more). The position suggests that some protocols *should* resist full legibility, but without operational evidence from deployed systems, this remains aspiration. Future work on contestable AI should include observational study of how optimization actually behaves when forced to work through multiple formally-structured but semantically-open layers.
