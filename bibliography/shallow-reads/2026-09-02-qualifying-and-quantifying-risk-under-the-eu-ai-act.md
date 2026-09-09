# Qualifying and Quantifying Risk under the EU AI Act

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.08564
**Date read:** 2026-09-02
**Connected to:** L-004, L-014
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A policy analysis paper addressing the tension between the EU AI Act's formal risk definition (probability × severity) and its qualitative focus on fundamental rights harms. It proposes a two-step reconciliation framework but does not present sustained empirical or theoretical argument about protocolized system behavior.

## What I took from it

This is a useful *instantiation* of the computable legality problem (L-014) but does not advance it mechanistically. The paper documents a real governance gap—regulators must render "risk" machine-legible to enable automated compliance checking and comparative assessment across vendors, yet fundamental rights harms resist quantification. This creates pressure toward proxy metrics (quantifiable proxy for unquantifiable harm).

The work confirms that L-004 (Goodhart Generalization) should apply downstream: whatever quantitative proxy the EU settles on will become the optimization target, potentially decoupling from actual rights protection. However, the paper does not investigate this dynamic empirically or theoretically—it stays at the problem-identification layer. No mechanism is proposed for *how* that decoupling occurs under scaled deployment, or what equilibria emerge.

## Research connections

- **L-004:** Fundamental rights as unmeasurable goal; quantitative risk proxy will be subject to capture under optimization pressure—but this paper does not model the capture dynamics.
- **L-014:** Computable legality as boundary concentration mechanism—the paper documents the legal encoding problem but not the agent response pattern.
- **seed-068:** Unmeasurability as Anomaly Insulation—the inability to quantify fundamental rights harm may act as structural insulation against certain forms of regulatory capture, worth investigating.
- **seed-080:** Proxy Collapse Under Upstream Asymmetry—if risk quantification is asymmetrically available to vendors vs. regulators, this could trigger proxy inversion.

## Method note

This work illustrates why policy analysis alone is insufficient for understanding protocolized systems: it identifies a gap (quantification vs. qualitative harm) without modeling what protocols or behavioral equilibria actually emerge *after* the formal rule is deployed. Future investigations should pair regulatory text analysis with post-deployment tracing of how vendors and systems actually operationalize the proxy, not just the tension at the drafting stage. The interesting science lies in the behavioral response to formalization, not in the formalization design itself.
