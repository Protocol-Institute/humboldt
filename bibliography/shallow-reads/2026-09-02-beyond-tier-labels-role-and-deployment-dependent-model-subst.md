# Beyond Tier Labels: Role- and Deployment-Dependent Model Substitution in Multi-Call LLM Workflows

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.09155
**Date read:** 2026-09-02
**Connected to:** L-006, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper on LLM routing and resource allocation in multi-call workflows, proposing that model substitution value depends on position in a computation DAG and surrounding deployment context, not on tier labels alone. Uses a predicate-action factorization framework evaluated against 8-64 call workflows with four three-tier model ladders.

## What I took from it

The paper operationalizes a micro-scale instance of intervention-layer displacement (L-012): the decision about *which* model to deploy (predicate) is separated from the decision about *where* to deploy it (action), and the substitution benefit becomes legible only *after* accounting for downstream dependencies. This echoes the principle that optimization pressure migrates when decisions become formally separable and computable.

However, the work remains confined to engineering optimization within a single bounded system (multi-call LLM workflows). It does not show whether the pattern generalizes to protocol-level systems with competing agents, embedded governance constraints, or heterogeneous incentives. The "deployment-dependent" observation is valid but local: it describes how computational context shapes utility, not how pressure propagates through distributed coordination systems or how formalization of routing decisions changes agent strategy at scale.

The connection to L-006 (Coordination Cost Conservation) is weak. There is no evidence here that coordination costs are conserved across protocol layer transitions — only that routing costs are reallocated within a fixed workflow.

## Research connections

- **L-012 (Intervention-Layer Displacement):** The separation of routing *predicate* from routing *action* is a formalization that makes substitution value legible at a new layer — consistent with the principle that computable decisions undergo pressure displacement. But this is within a single system, not across competing agents.

- **L-006 (Coordination Cost Conservation):** Mentioned in triage, but the paper does not demonstrate cost conservation across layers — only local optimization within a workflow.

- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** Model tier labels function as proxies for utility; this work shows they collapse under positional asymmetry (i.e., tier utility is not stable across deployment contexts). Weak connection.

- none

## Seed

**Seed title:** Positional Legibility Asymmetry in Substitutable Component Systems

**Seed type:** observation

**Seed text:** In multi-call or multi-stage systems using substitutable components (models, modules, agents), the utility of a component is not computable from its intrinsic properties alone — it depends critically on (1) its position in the execution graph and (2) its informational or functional relationship to upstream and downstream stages. When this dependency structure is made explicit and optimized over, the apparent "tier" or quality ranking of the component can reverse or become context-dependent. This suggests that any protocol system where components or agents are ranked by a single metric will experience metric collapse when deployment context becomes computable — a special case of proxy capture under asymmetric observability.
