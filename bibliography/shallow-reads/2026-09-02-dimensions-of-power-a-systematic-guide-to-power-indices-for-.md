# Dimensions of Power: A Systematic Guide to Power Indices for Explainable AI

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.05031
**Date read:** 2026-09-02
**Connected to:** L-001, L-004
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A taxonomy paper surveying power indices (game-theoretic attribution measures) as explainability tools for AI systems. The work organizes existing indices along three dimensions to guide selection of attribution proxy for a given explanation task — primarily a methodological review rather than a primary empirical or theoretical argument introducing a novel mechanism.

## What I took from it

This is a **proxy-selection problem made visible**. The paper documents that there exist multiple defensible ways to measure "influence" or "attribution" in a system, that they can yield substantially different results, and that practitioners lack systematic guidance on which proxy to choose for a given task. This is recognizable as an instance of L-004 (Goodhart Generalization) *in the epistemic layer* — the choice of power index is itself a measurable proxy for the unmeasurable goal of "true explanatory influence," and different indices will optimize differently under pressure.

The deeper resonance is with L-001 *implicitly*: as explainability becomes a regulatory or protocol requirement (fairness auditing, compliance documentation), the choice of power index gets locked in by adoption and precedent. Once a firm, regulator, or standard body selects Shapley value (or LIME, or permutation importance) as the canonical attribution method, switching becomes costly — the index ossifies not because it's technically superior but because coordination around it has hardened. The paper does not examine this dynamic, but its taxonomy makes the **multiple equilibria** visible.

This also touches seed-069 (Transparency-Legibility as Trust Proxy Substitution) and seed-082 (Additive Intervention in Overloaded Protocols Preserves Root Pressure): deploying an explainability index does not resolve the underlying fairness or accountability question; it substitutes a legible proxy (attributed influence scores) for the unmeasurable goal (true causal responsibility), and systems under audit pressure will optimize toward whichever index is formally adopted.

## Research connections

- **L-004:** Power index selection is proxy choice for unmeasurable explainability goal; different indices are Goodhart-vulnerable under optimization pressure.
- **L-001:** Once a power index is standardized in practice (regulation, compliance frameworks), switching becomes coordination-costly and the choice ossifies.
- **seed-069:** Explainability via power indices exemplifies trust-as-legibility substitution in asymmetric-knowledge protocols.
- **seed-082:** Adding an attribution layer does not resolve root accountability pressure; pressure migrates to the choice of index itself.

## Method note

This paper illustrates a research pattern we should monitor: **taxonomy papers that make visible a space of defensible but incommensurable choices**. Such work is valuable for surfacing Goodhart/ossification risks *before* they calcify in practice, but the paper itself remains neutral on which choice is "correct." The research opportunity is not in the taxonomy but in tracking what happens *after* adoption — which indices get selected, why, and whether the choice becomes locked in as a protocol component. Shallow taxonomy work should be paired with longitudinal audits of standardization and adoption to generate testable predictions about L-001 and L-004 in the explainability domain.
