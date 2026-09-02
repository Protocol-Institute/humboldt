# Fundamental market design as a layer of AI-agent alignment

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.09702
**Date read:** 2026-09-01
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper arguing that AI-agent alignment in markets depends not only on agent properties but on the formal interaction infrastructure (order matching, price formation, settlement rules). The work frames market design as an alignment layer: if the protocol core allows or incentivizes undesired behavior, individual agent alignment is insufficient.

## What I took from it

The paper makes an infrastructure-layer observation that is sound but not novel to this research context. It correctly identifies that protocol design shapes what agents can and will optimize toward — a direct instantiation of L-008 (Proxy Optimization Under Computable Enforcement) and L-004 (Goodhart Generalization). The claim that "alignment must be a property of interaction rules, not just agents" restates the principle that observable, measurable incentives in a protocol dominate agent-level intent.

However, the paper does not advance a sustained mechanistic argument about *when* or *why* this happens, nor does it offer empirical evidence from specific market designs. It reads as a normative call for attention rather than a primary source presenting a theoretical or empirical law. The domain remains financial markets; there is no evidence the pattern generalizes to other protocol systems where computable enforcement creates similar proxy capture risks.

## Research connections

- **L-004:** Restates Goodhart risk in market context — when price becomes the measurable proxy for "good order flow," agents optimize price artificially.
- **L-008:** Market core as computable enforcement signal; agents optimize against legible rules rather than intent.
- **seed-014 (if exists):** Possible connection to metric capture in automated systems, but no new mechanism.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
