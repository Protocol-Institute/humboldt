# Clinical Pathways as Safety Specifications for Physical AI in Hospital Wards

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.19827
**Date read:** 2026-09-02
**Connected to:** L-007, L-003
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems architecture paper proposing that clinical pathways — existing informal/semi-formalized coordination protocols in hospital settings — be reinterpreted as explicit runtime safety specifications for embodied medical AI (robots, wearable sensors, smart devices). The work is domain-specific: it constructs a concrete integration framework for hospital ward safety, not a theoretical argument about protocol dynamics or formalization mechanics.

## What I took from it

The paper sits at the intersection of L-007 (trust accumulation through operational stability) and L-003 (formalization under stress), but treats these as engineering constraints rather than investigating the mechanism or generalizability of either. It observes that clinical pathways function as de facto safety norms that have accumulated trust through decades of operational use, and proposes formalizing them for AI compliance. This is a sensible applied move, but the paper does not examine: (1) what happens to the informality-formality boundary when existing trusted norms are machine-encoded, (2) whether formalization of safety-critical coordination norms follows the patterns described in L-003, or (3) the risk that metric capture (L-004) might emerge when pathway compliance becomes legible and optimizable by learning systems. The work assumes formalization improves safety; it does not investigate whether it might displace or hollow out the trust that the pathways currently carry.

## Research connections

- **L-007:** The paper relies on trust accumulated in clinical pathways over time, but does not investigate whether that trust transfers to formalized versions or whether formalization resets the trust ratchet.
- **L-003:** Implicit connection — safety stress is driving formalization of informal norms — but no analysis of the mechanism or costs of that transition.
- **L-004:** Unexamined risk: clinical pathway compliance becomes a measurable proxy for patient safety; optimization pressure from learning systems could decouple the two.
- **seed-062 (Formalization Opacity Collapse):** The paper moves from opaque informal coordination to transparent machine-readable specification; no discussion of whether legibility introduces new failure modes.

## Seed

**Seed title:** Trust Discontinuity in Formalized Safety-Critical Norms
**Seed type:** question
**Seed text:** When informal, operationally-trusted safety coordination norms are formalized for machine enforcement, does the trust function transfer to the formal representation, or is trust reset by the formalization boundary itself? Under what conditions does the operationally-accumulated credibility of a norm survive its encoding as a computable specification — and under what conditions is it replaced by confidence in the formal system, creating a discontinuity? This may generalize beyond clinical pathways to any migration of safety-critical coordination from human-legible implicit norms to machine-computable explicit rules.
