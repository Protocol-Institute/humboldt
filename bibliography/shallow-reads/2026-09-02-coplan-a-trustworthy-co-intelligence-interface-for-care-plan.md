# CoPlan: A Trustworthy Co-Intelligence Interface for Care Planning through Role-Based Contestable Argument Graphs

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.05107
**Date read:** 2026-09-02
**Connected to:** L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper describing a multi-agent workflow and UI design for care planning that permits contestation of AI recommendations through role-based argument graphs. The work is primarily a tool/interface contribution addressing the specific domain of clinical care coordination, not a theoretical or empirical investigation of how intervention-layer transparency affects optimization pressure or agent behavior under formalization.

## What I took from it

The paper demonstrates a legitimate concern (L-012 adjacent): when AI outputs are made legible and formally contestable, the locus of optimization *could* shift from the recommendation layer to the contestation layer — i.e., agents optimize toward arguments that survive challenge rather than toward sound plans. However, CoPlan does not investigate this mechanism. Instead, it assumes that transparency and contestability are unambiguously beneficial and designs a system to maximize both.

The work is valuable as a case study in *how* to make intervention-layer decisions inspectable and contestable, but it does not empirically track whether introducing formal argument structures changes what kinds of plans are proposed, whether optimization pressure migrates to meta-level argumentation, or whether "contestability" becomes a new surface for gaming. The absence of adversarial analysis or behavioral telemetry around contestation patterns is notable—the paper does not ask whether the contestation interface itself becomes subject to Goodhart-style capture.

## Research connections

- **L-012:** CoPlan instantiates legible intervention-layer transparency but does not empirically track whether optimization pressure relocates to argument crafting or contestation-resistance rather than care quality.
- **L-004 (Goodhart):** The system assumes role-based argument graphs prevent metric capture, but does not monitor whether agents optimize arguments rather than outcomes.
- **seed-069 (Transparency-Legibility as Trust Proxy):** The paper treats contestable transparency as intrinsically trust-generating without testing whether formal argumentation becomes a trust proxy decoupled from actual care effectiveness.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
