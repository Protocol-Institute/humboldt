# Welfare-Opaque Income: Taxation under AI-Agent Delegation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.20425
**Date read:** 2026-09-22
**Connected to:** L-012, seed-139
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A theoretical economics paper studying how AI-agent delegation—where a hidden rule maps observable income to unobservable welfare consequences—creates a taxation design problem under double unobservability. The core contribution is showing that identical tax-base statistics can mask divergent welfare effects when the preference-to-execution mapping is hidden from the fiscal authority.

## What I took from it

This is a clean formalization of **L-012** (Intervention-Layer Displacement): when a prediction or observable (income response) is legible but the mapping from volition to execution is not, the optimization target shifts from actual welfare to tax-base behavior. The paper demonstrates that agents delegating to opaque AI systems create a new kind of adversarial separation: the government can observe and optimize tax policy around behavioral responses, but cannot recover the underlying preferences driving those responses.

The work does *not* argue that this is a new mechanism in protocol systems generally—it is anchored to taxation and delegation. It does not challenge any of the standing laws, nor does it establish generalizable conditions for when this opacity arises or what its equilibrium properties are across other domains. It is a competent theoretical contribution that sharpens one instance of volition-execution detachment without providing evidence of a pattern that transcends the tax domain.

## Research connections

- **L-012:** Confirms the mechanism: when execution is delegated to an agent with a hidden policy, the fiscal authority's optimization target becomes the observable tax response rather than true welfare, displacing the intervention locus upstream (to taxation design) away from the actual source of preference (the hidden rule).

- **seed-139:** Direct instantiation: the paper shows that volition legibility becomes itself a protocol boundary artifact—the government must treat the hidden preference-execution map as an exogenous, unobservable boundary, making volition itself a formal constraint rather than a recoverable quantity.

## Seed

**Seed title:** none
