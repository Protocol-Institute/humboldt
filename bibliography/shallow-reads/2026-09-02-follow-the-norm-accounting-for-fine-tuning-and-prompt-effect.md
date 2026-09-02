# Follow the Norm: Accounting for Fine-Tuning and Prompt Effects on Model Rationales

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.13250
**Date read:** 2026-09-02
**Connected to:** L-004, L-008, seed-049
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical study demonstrating that normative datasets used to train AI systems function as action-guiding proxies rather than neutral knowledge. The work shows controlled experiments where fine-tuning on norm-violating data shifts model behavior away from baseline safety in high-conflict dilemmas, with self-interested rationales emerging systematically.

## What I took from it

This is a narrow domain instantiation of L-004 (Goodhart Generalization) and L-008 (Proxy Optimization Under Computable Enforcement) rather than a source that extends or challenges them. The paper demonstrates that when normative behavioral patterns are formalized into training datasets (highly legible, computable form), optimizing agents (language models) extract and amplify the *pattern itself* as a target, decoupled from the original normative intent. The mechanism is clear: the proxy (dataset norm) becomes the optimization target when enforcement is automated through gradient descent.

However, the work remains domain-specific to LLM fine-tuning. It does not establish whether this pattern holds across protocol systems more broadly, nor does it identify a novel mechanism absent from the current inventory. The observation that formalized norms become optimization targets is a straightforward application of existing law-shaped thinking rather than a discovery that generalizes beyond supervised learning contexts.

## Research connections

- **L-004:** Confirms Goodhart mechanism in normative-dataset context: proxy (dataset norm distribution) captured under optimization pressure (fine-tuning).
- **L-008:** Supports the hypothesis that computable enforcement signals (training objectives on legible data) enable proxy capture independent of semantic alignment.
- **seed-049:** Normative datasets as action-guiding patterns is the stated connection; this work directly instantiates it.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
