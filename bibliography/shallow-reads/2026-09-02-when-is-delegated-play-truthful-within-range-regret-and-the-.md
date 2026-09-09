# When Is Delegated Play Truthful? Within-Range Regret and the Trilemma of Aligned Delegation

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.14357
**Date read:** 2026-09-02
**Connected to:** L-008, L-012
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source presenting a sustained theoretical argument that directly extends L-008 (Proxy Optimization Under Computable Enforcement) by introducing within-range regret as a mechanistic measure of when optimization pressure displaces from truthful revelation to strategic misreporting; mechanism absent from current inventory.

## What this is

This is a theoretical computer science paper (multiagent systems) investigating the incentive structure of delegation protocols—specifically, when a principal has incentive to report their true preferences to an automated proxy acting on their behalf in a mechanism. The authors argue that a principal's optimal misreporting gain is bounded by the proxy's within-range regret, and identify a trilemma: you cannot simultaneously achieve truthful delegation, low regret, and certain other structural properties.

## What I took from it

The paper formalizes a critical gap in delegation protocol design: the revelation principle assumes principals report truthfully *to the mechanism*, but it remains silent on incentives *within the delegation layer itself*. The within-range regret metric quantifies exactly how much slack exists for a principal to gain by lying to their own proxy—effectively measuring the leakage of optimization pressure through the proxy boundary.

This directly extends L-008 by showing that computable enforcement at the proxy level creates a measurable surface for strategic gaming *before* the mechanism sees data. The trilemma suggests there is no free resolution: achieving truthful delegation imposes hard constraints on regret bounds, proxy expressiveness, or mechanism structure. This is not a tool-building paper; it identifies a structural impossibility in the delegation abstraction itself. The mechanism (within-range regret as the pivot quantity) appears novel to the protocols literature and has clear generalization potential beyond advertising and LLM agents to any system where a principal must communicate intent to an automated intermediary that optimizes in a legible space.

## Research connections

- **L-008:** The paper directly instantiates the mechanism of L-008 by showing that when proxy obligations become precisely computable (within-range regret is a formal quantity), optimization pressure does not disappear—it migrates to the principal's reporting layer.
- **L-012:** The proxy acts as an intervention layer that displaces the locus of optimization pressure from mechanism truth-telling to proxy-delegation honesty; the paper quantifies this displacement.
- **L-004 (Goodhart Generalization):** Within-range regret is itself a proxy for proxy quality; optimizing for low regret may degrade the proxy's ability to faithfully represent principal intent.
- **seed-069 (Transparency-Legibility as Trust Proxy Substitution):** The formalization of proxy behavior (regret bounds) becomes a substitute for trust in the proxy itself, with the trilemma showing this substitution is incomplete.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** The principal-proxy information asymmetry (principal knows their true preferences; proxy only sees reports) creates the conditions for the reported collapse.

## Seed

**Seed title:** Delegation Incentive Leakage Under Formalized Proxy Regret

**Seed type:** mechanism

**Seed text:** In any delegation protocol where the proxy's behavior is formalized as a computable regret bound, the principal faces an incentive to misreport preferences equal to the proxy's within-range regret. This creates a structural tension: reducing proxy regret below a threshold either requires constraining the principal's communication space, reducing the proxy's expressiveness, or accepting a trilemma where no two of {truthful delegation, low regret, expressive mechanism} can be simultaneously achieved. The generalization: formalization of intermediary performance creates a new optimization surface at the delegation boundary, not at the mechanism boundary. The principal's optimal reporting strategy becomes a function of the formal regret metric, not of mechanism incentives alone.
