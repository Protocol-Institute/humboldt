# Toward a Threat Actor Profiling Taxonomy for Pre-Release Risk Management of Open-Weight Frontier Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.25361
**Date read:** 2026-09-02
**Connected to:** L-008, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A taxonomy design paper proposing six-dimensional threat actor characterization (technical sophistication, domain knowledge, organizational capacity, infrastructure, financial capacity, time horizon) for pre-release AI safety evaluation. The work argues that explicit adversary modeling should ground risk assessments and make them interpretable and comparable.

## What I took from it

The paper formalizes what has been implicit — threat actor assumptions — into a legible, computable classification scheme. This is a direct instantiation of L-014 (Strategic Boundary Concentration Under Computable Legibility): by rendering "who poses a threat" as machine-readable attributes, the paper makes threat profiling auditable and standardizable. This creates new optimization surface.

However, the work remains taxonomic rather than mechanistic. It does not investigate whether formalizing threat actors produces unintended shifts in what gets protected, what gets neglected, or whether the legibility itself becomes a new attack surface (e.g., adversaries gaming their own classification to fall outside formal concern scope). The paper does not examine whether pre-release risk management itself undergoes ossification once threat taxonomy becomes protocol infrastructure — a secondary instance of L-001. The contribution is competent institutional hygiene, not law discovery.

## Research connections

- **L-014:** Formalizing threat actor categories as computable attributes exemplifies strategic boundary concentration; the taxonomy enables agents to optimize classification membership rather than underlying capability.
- **L-008:** If adoption of this taxonomy drives enforcement legibility, it creates computable proxy obligations (a model "must handle actor class X") that become subject to proxy capture.
- **seed-069:** Threat taxonomy risks substituting legible categorization for actual trust assessment of model robustness; classification transparency becomes a proxy for safety.
- **seed-073:** Multi-stakeholder adoption of a single threat taxonomy creates correlated failure risk if the taxonomy's frame is misaligned with actual attack surfaces.

## Seed

**Seed title:** Threat Legibility as Governance Lock
**Seed type:** motif
**Seed text:** When adversary models are formalized as computable taxonomies for protocol compliance (e.g., pre-release safety evaluation), the taxonomy's dimensionality and boundaries become sticky governance infrastructure. Refinement, amendment, or paradigm shift in threat modeling becomes coordination-costly, creating pressure to route novel threat types into existing categories rather than expand the taxonomy. This produces systematic undercounting of threats that don't fit the canonical profile — a form of paradigm-locked anomaly tolerance (L-013) specific to formalized opponent modeling.
