# Peer review should constrain evaluative authority

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.28646
**Date read:** 2026-11-23
**Connected to:** L-003, seed-241
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper arguing that peer review reform should shift from improving evaluator quality or judgment aggregation toward constraining evaluative authority under conditions of irreducible uncertainty. The paper identifies a scaling collapse in academic review infrastructure: submission volume exceeds reviewer capacity, expertise, incentive alignment, and time, making quality assurance impossible while authority over opportunity allocation remains concentrated and unexamined.

## What I took from it

The paper frames peer review as a protocol system under stress (L-003: Formalization Ratchet applies directly—pressure to scale incentivizes metric capture and rigid gatekeeping). However, it makes a subtle move away from formalizing better: it argues *against* trying to solve uncertainty through procedural improvement, instead proposing bounded authority as an equilibrium condition. This resonates with L-005 (Gall Generalization) and seed-548 (Transition-State Topology Illegibility)—the system cannot be restructured from scratch and cannot be made adequate under current load, so the constraint becomes the design primitive.

The core insight relevant to the new nature inventory: when a protocol's evaluative or allocative function operates under *persistent* uncertainty that cannot be engineered away, formalizing the evaluation to improve it paradoxically concentrates and legitimizes authority that should itself be constrained. This is adjacent to L-012 (Intervention-Layer Displacement) and seed-452 (Legitimacy Collapse Under Macro Formalization)—the more you formalize the evaluation function to make it legible and fair, the more you lock in the assumption that evaluation *should* be centralized and binding. The paper is essentially proposing that some allocation decisions should be deliberately *de-formalized* or distributed to escape this trap.

## Research connections

- **L-003:** Peer review under scaling pressure is a textbook case of informal norms (editorial judgment, collegial trust) being replaced by formal metrics (impact factors, citation counts, reviewer scores), which then fail to capture what they were meant to protect.
- **L-005:** The paper implicitly accepts Gall's principle: you cannot replace peer review with a better system; you can only evolve constraints on what it is permitted to decide.
- **L-012:** Intervention-Layer Displacement: once evaluation becomes a legible, computable input to an opportunity-allocation decision, optimization pressure moves upstream to gaming the evaluation signal itself.
- **seed-241:** (inferred from triage note) Authority constraint under uncertainty—the paper's core move.
- **seed-452:** Legitimacy Collapse Under Macro Formalization: formalizing peer review to make it "fair" at scale paradoxically undermines its legitimacy by exposing its inability to deliver on the promise.
- **seed-547:** Contestation Foreclosure as Visibility Collapse—formalized review systems reduce the space for principled disagreement about what should even be evaluated.

## Method note

This paper models an important meta-pattern: when a governance or evaluation protocol faces an engineering problem it cannot solve (scaling review to match submission volume), the response is often to propose *more* formalization. The paper asks instead whether the problem should be solved by *constraint* rather than *improvement*—a reframe that suggests research on protocolized systems should inventory cases where formalizing the right answer paradoxically makes the system worse. This implies a need for adversarial research on what happens when you deliberately *de-formalize* allocation or evaluation under persistent uncertainty, rather than always assuming that legibility is the solution.
