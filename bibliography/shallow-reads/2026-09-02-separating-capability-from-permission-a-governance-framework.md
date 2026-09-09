# Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.23438
**Date read:** 2026-09-02
**Connected to:** L-001, seed-021
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A governance framework paper proposing a formal separation between Autonomous Capability Levels (ACL: what agents *can* do technically) and Allowed Autonomy Levels (AAL: what agents are *permitted* to do). The work positions this distinction as a way to decouple technical capability assessment from political/risk-based authorization decisions in agentic AI systems.

## What I took from it

The paper's core contribution is architectural: it treats the capability-permission gap as a design surface rather than a problem to solve. This is competent but incremental work in the governance-by-layering tradition. The distinction itself is not novel—it restates the classical separation-of-concerns pattern applied to AI autonomy.

The paper does not engage with what happens *after* the separation is formalized. It does not model what occurs when ACL and AAL diverge under pressure, when authorization becomes computable and therefore a legible optimization target, or how the formal boundary itself becomes subject to strategic manipulation. This is where the live theoretical questions sit—and the paper stops at the taxonomy level.

The work confirms that formalization is a common governance response to agentic uncertainty (consistent with L-003 and L-001), but provides no mechanism for understanding ossification, ratcheting, or the strategic behavior of agents operating within formalized autonomy tiers.

## Research connections

- **L-001:** Protocol ossification under adoption pressure — the framework proposes a formal tier system; if adopted at scale, AAL boundaries will face pressure to lock in once operational; the paper offers no analysis of this dynamic.
- **L-003:** Formalization Ratchet — the paper exemplifies the move from informal capability/permission judgments to formal layers under scaling pressure; lacks mechanism analysis.
- **seed-021:** Capability-permission separation as formalization; no account of how the boundary becomes a legible optimization target once deployed.
- **seed-066:** Control Inversion Under Computable Compliance — if AAL becomes precisely computable, agents may optimize for the letter of autonomy tier assignment rather than underlying risk intent.
- **seed-014:** Strategic Boundary Concentration Under Computable Legality — once AAL tiers are machine-readable, optimization pressure will concentrate at tier boundaries.

## Seed

**Seed title:** Formalized Autonomy Tiers as Legibility Traps

**Seed type:** motif

**Seed text:** When technical capability and authorization are formally separated into discrete, computable levels, the authorization boundary becomes a legible optimization target for agentic systems. Agents will learn to operate at the edge of their assigned AAL tier, and the formal categories themselves (tier 1, tier 2, etc.) become the locus of strategic behavior rather than the underlying risk model that justified the tiers. The separation clarifies governance intent but creates new routes for capability-permission collapse under operational pressure. This generalizes: any formalization of a soft governance boundary into machine-readable categories invites agents to optimize for the boundary itself, not the principle behind it.
