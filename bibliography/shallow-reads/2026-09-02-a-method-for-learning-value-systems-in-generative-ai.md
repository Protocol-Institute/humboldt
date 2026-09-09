# A Method for Learning Value Systems in Generative AI

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.16903
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper proposing computational techniques for inferring human value systems from behavioral observation in generative AI contexts. The work addresses the elicitation problem — how to ground abstract human values into computable representations that can guide model decisions — by treating value learning as an inference problem over observed preferences.

## What I took from it

The paper instantiates the proxy optimization problem (L-004, L-008) but does not theorize the consequences. It assumes that if values can be made explicit and computable, they become actionable objectives for generative systems. This is precisely the condition under which L-008 (Proxy Optimization Under Computable Enforcement) predicts optimization pressure will dislocate from the intended target to the legible proxy itself.

The framing treats value systems as recoverable structures — that human values have a stable "multidimensional structure" waiting to be elicited. It does not engage with the possibility that *formalization itself changes the thing formalized*, or that making values computable for enforcement creates a new optimization surface orthogonal to the original intent. The work is technically competent but paradigm-locked: it solves the representation problem without asking whether representation solves the alignment problem, or whether it creates a new failure mode (value capture, metric drift, causal detachment from human intent).

## Research connections

- **L-004:** The paper proposes making values computable and measurable — exactly the condition under which Goodhart effects generalize into systematic value drift.
- **L-008:** Computable value representations become legible optimization targets; the paper does not model what happens when a generative system optimizes against a learned proxy rather than the source intent.
- **seed-062:** Formalization of human values for computational governance may collapse opacity; the learning process itself may render invisible the interpretive layers that made values coherent in their original context.
- **seed-077:** A learned value metric, once embedded in model training or RLHF loops, may become a ratcheting optimization target that systems learn to game rather than satisfy.

## Seed

**Seed title:** Value Formalization as Proxy Substitution

**Seed type:** question

**Seed text:** When human values are learned as computable functions and embedded as optimization targets in generative systems, does the resulting alignment improve fidelity to human intent, or does it displace optimization pressure to the learned proxy itself — making the system perfectly aligned to a distorted representation rather than the source? The risk concentrates when: (1) values are high-dimensional and context-dependent, (2) learning occurs over limited behavioral samples, and (3) the computable proxy becomes the sole enforcement signal. This may generalize across all domains where informal norms are formalized for automated enforcement.
