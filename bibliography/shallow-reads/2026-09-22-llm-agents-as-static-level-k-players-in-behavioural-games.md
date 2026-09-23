# LLM Agents as Static Level-k Players in Behavioural Games

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2606.27845
**Date read:** 2026-09-22
**Connected to:** L-010, L-017, seed-129
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical validation study testing whether LLM choice distributions match human behavioral play in iterated coordination games (p-beauty contest, public goods game) across parameter variations (temperature, scale, quantization). The work treats LLMs as behavioral proxies and investigates stability of this assumption under local-model configuration changes.

## What I took from it

This is a **benchmark-calibration paper**, not a primary theoretical source. It operationalizes the assumption that LLMs constitute reliable behavioral stand-ins through factorial design over hyperparameter space, but does not advance a mechanism claim or challenge an existing law. The relevance is narrow and empirical: it documents *whether and when* LLM play diverges from human level-k reasoning under parameter perturbation.

The paper touches on L-017 (guidance-layer coalescence) only weakly—it shows that LLMs produce stable choice distributions in multi-agent games, but does not examine whether these distributions constitute a hidden coordination channel or whether independent agents using the same LLM as guidance converge unexpectedly. Similarly, L-010 (coordination adoption nonmonotonicity) is invoked in the triage note but the work does not trace adoption dynamics or signal conditioning—it is a snapshot of static play profiles.

Seed-129 (legibility-induced conformity locking) is also misaligned: the paper does not examine whether formalization of LLM behavior induces conformity; it merely checks whether LLMs remain stable proxies under configuration drift.

## Research connections

- **L-010:** Tangentially relevant; the study observes LLM play in coordination games but does not investigate adoption nonmonotonicity or how agents condition on coordination signals from other adopters across time.
- **L-017:** Minimal relevance; no examination of whether shared AI guidance produces unexpected convergence or hidden coordination in nominally independent agents.
- **seed-129:** Not connected; the paper does not investigate whether formalization of LLM behavior (or audit of its choices) locks agents into conformity patterns.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
