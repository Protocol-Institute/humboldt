# Contracting for LLM Delegation: Moral Hazard in Technology and Effort Choice

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.18232
**Date read:** 2026-09-02
**Connected to:** L-008, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A principal-agent framework extension modeling scenarios where agents select both technology (LLM model) and effort level (e.g., token budget) under hidden action conditions. The work treats output quality as a concave saturating function of the two-dimensional action choice, analyzing contract design under moral hazard when both technology and effort are unobservable.

## What I took from it

This is a competent extension of classical principal-agent theory into the LLM delegation space, but it does not sustain a theoretical or empirical argument that generalizes beyond the specific domain. The paper appears to be a mechanism design exercise: given hidden actions on two dimensions, what contracts extract incentive compatibility? This is technically sound but does not challenge L-008 (Proxy Optimization Under Computable Enforcement) or open new mechanism-level inquiry.

The framing treats technology selection as a cost-capability tradeoff that agents can hide, which is relevant to understanding capability-shopping under opacity. However, the paper does not investigate whether the presence of *legible* capability metrics (model benchmarks, token counts, etc.) systematically reshapes which contracts agents actually prefer, or whether agents optimize toward proxy visibility in their technology choice. The moral hazard framing assumes hidden actions; it does not examine the dynamics when capabilities become *computable* and *legible to enforcement*—the core condition for L-008.

## Research connections

- **L-008:** Touches the precondition (hidden technology-effort selection) but does not investigate the reversal case: when capability and effort become legible, does the optimization locus shift upstream to *capability selection itself* as the new hidden dimension? This is left unexamined.
- **seed-048:** Related by design (principal-agent LLM delegation) but does not advance the specific hypothesis about computable enforcement triggering proxy optimization.

## Seed

**Seed title:** none

**Seed type:** 

**Seed text:**
