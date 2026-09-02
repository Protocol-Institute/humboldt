# Pezego-HITL: A policy-grounded large language model architecture for agricultural extension in Ghana

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.13934
**Date read:** 2026-09-01
**Connected to:** L-012, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** [blank]

## What this is

A two-year design study introducing P-EVAL, a validation protocol that formalizes policy constraints into the LLM evaluation framework for agricultural decision support in Ghana. The work treats safety compliance, helpfulness, latency, and expert workload as a joint optimization problem under adaptive compute allocation.

## What I took from it

The paper is competent domain-specific engineering: it operationalizes policy guardrails by making them legible inputs to a compute-allocation decision. This is a real-world instantiation of the conditions under which L-012 (Intervention-Layer Displacement) and L-008 (Proxy Optimization Under Computable Enforcement) would activate—when normative constraints become machine-readable metrics in an optimization loop, the system will tend to optimize the legible proxy (policy compliance signal) rather than the underlying intent (safe agricultural advice). 

However, the paper does not investigate or theorize this displacement. It is a tool-building effort that assumes the formalization solves the problem, rather than asking whether formalizing policy into P-EVAL might shift optimization pressure to a new boundary (e.g., gaming the policy evaluation signal, or finding advice that passes P-EVAL but violates the spirit of agricultural safety). The work confirms that high-stakes domains *are* moving toward computable enforcement, but it does not examine the mechanism by which that formalization itself becomes a new site of strategic behavior.

## Research connections

- **L-012:** The paper instantiates the conditions (policy made legible, optimization under enforcement signals) but does not examine displacement.
- **L-008:** Formalizing policy compliance as a measurable metric in the evaluation loop; no investigation of proxy capture.
- **seed-014 (if in inventory):** Expert supervision workload as a metric — question whether formalizing "expert burden" inverts the direction of optimization (systems optimizing to appear low-burden rather than safe).

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
