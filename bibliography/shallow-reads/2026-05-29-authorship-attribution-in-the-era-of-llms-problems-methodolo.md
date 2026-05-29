# Authorship Attribution in the Era of LLMs: Problems, Methodologies, and Challenges

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2408.08946
**Date read:** 2026-05-29
**Connected to:** L-002, L-004
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A literature review surveying authorship attribution methods under pressure from LLM-generated content. The work is taxonomic rather than presenting a sustained theoretical argument or novel mechanism — it catalogs existing methodologies and their failure modes without proposing foundational grounding for a new law.

## What I took from it

The paper confirms L-002 (Hardness Asymmetry) at the authorship layer: verification of human authorship is computationally expensive (stylometric analysis, forensic review, multi-modal signals), while forgery via LLM is now nearly free. The asymmetry has sharpened recently, not reversed or stabilized. This is an applied instantiation rather than a novel mechanism.

L-004 (Goodhart Generalization) is also present: any protocol that uses stylometric or statistical proxies for "human authorship" degrades under adversarial optimization. LLMs trained to mimic human writing naturally target these proxies, collapsing the distinction the metric was meant to preserve. However, this is a straightforward application of existing law to a new domain (LLM authorship), not an extension or challenge to L-004 itself.

The paper does not engage with protocol-level design, ossification, formalization pressure, or the dynamics of trust accumulation in safety systems.

## Research connections

- **L-002:** Exemplifies verification-forgery hardness asymmetry in authentication protocols; asymmetry is *worsening* with LLM capability scaling, not stabilizing.
- **L-004:** Demonstrates proxy capture under adversarial optimization; stylometric markers are Goodhartable and being actively gamed by generative systems.

## Candidate laws or signals

none
