# Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.14399
**Date read:** 2026-09-02
**Connected to:** L-008, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A prespecified randomized algorithm audit of seven LLMs (six open-weight plus gpt-4o-mini) measuring what attributes causally drive physician recommendations in synthetic choice sets. The work is a domain-specific empirical probe into recommendation bias, not a sustained theoretical argument or mechanism discovery.

## What I took from it

The paper documents a narrowly framed phenomenon: LLMs show statistically detectable preference patterns across physician attributes (reputation signals, demographic features) when forced to choose among synthetic profiles. This is instrumentally useful — it identifies empirical regularities in a specific intermediation layer.

However, the work does not propose or test a mechanism explaining *why* these preferences emerge, nor does it establish that the pattern generalizes beyond LLM physician recommendation or scales to other intermediation protocols. It measures correlation in a legible choice space but does not address the deeper question: whether the *formalization of choice into a legible, auditable proxy* itself induces optimization pressure that distorts the allocation, independent of the LLM's training data or stated objectives. The audit reveals the output; it does not probe whether legibility itself drives convergence toward measurable proxies (reputation, demographic markers) as optimization targets.

## Research connections

- **L-008:** Proxy Optimization Under Computable Enforcement — The paper shows LLMs optimize over legible attributes (reputation scores, demographic signals) in a precisely computable choice space, but does not examine whether the *formalization* of the choice itself creates the optimization pressure or merely reveals pre-existing biases.

- **L-012:** Intervention-Layer Displacement in Automated Decision Protocols — The work documents that physician recommendation has been displaced from patient-doctor direct negotiation into an LLM intermediation layer with its own legible optimization surface, but treats this as a static phenomenon rather than as a mechanism that might drive preference distortion *due to* the layer shift itself.

- **seed-080:** Proxy Collapse Under Upstream Asymmetry in Automated Systems — The audit shows reputation and demographic signals dominate recommendations; the seed would ask whether these are collapsing toward computable proxies because upstream information about physician quality is asymmetric and unmeasurable.

## Seed

**Seed title:** Legible-Attribute Dominance in Intermediated Choice Under Asymmetric Quality Information

**Seed type:** observation

**Seed text:** When an intermediation protocol (LLM-assisted recommendation, algorithmic allocation) formalizes choice into a legible, auditable decision space, recommending systems converge toward measurable and verifiable attributes (reputation scores, demographic markers, easily tokenizable signals) at the expense of unmeasurable quality signals (clinical judgment, relational trust, contextual fit). This occurs not necessarily due to training data bias alone, but because legibility itself creates an optimization attractor: only attributes that can be formalized, audited, and debugged become decision-relevant in practice. The pattern should generalize across intermediation protocols whenever quality is genuinely hard to formalize but compliance/auditability is easy.
