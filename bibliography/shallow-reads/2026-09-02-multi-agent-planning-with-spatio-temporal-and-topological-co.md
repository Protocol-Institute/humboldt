# Multi-Agent Planning with Spatio-Temporal and Topological Constraints using STL-GO

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.28679
**Date read:** 2026-09-02
**Connected to:** none
**Kind:** content
**Escalation:** store-only

## What this is

An engineering paper presenting STL-GO, a framework for multi-agent planning under spatio-temporal logic (Signal Temporal Logic) and topological graph constraints. The work addresses coordination problems in robotics and autonomous systems by formalizing "when/where/what" and "how agents interact" as logical constraints, then solving the resulting constrained planning problem.

## What I took from it

This is competent constraint-satisfaction engineering work, but it does not engage with how formal legibility of constraints shapes agent behavior, how ossification emerges when constraints become computational, or how the act of formalizing coordination creates new failure modes. The paper treats spatio-temporal logic as a neutral representation language—a tool for expressing pre-existing coordination needs—rather than investigating whether the act of formalization itself reorganizes incentives, creates optimization targets, or locks in particular equilibria. No mechanism is offered for how agents might exploit the boundary between what is formally specified and what remains informal. The constraint system is assumed to be authoritative and unambiguous; the paper does not explore how multi-agent systems escape, reinterpret, or corrupt formally specified topological and temporal requirements once they face optimization pressure or resource scarcity.

## Research connections

- **L-003 (Formalization Ratchet):** The paper formalizes coordination as logical constraints, but does not measure whether this formalization reduces or increases coordination cost, or whether it creates new categories of coordinative brittleness under stress.
- **L-014 (Strategic Boundary Concentration Under Computable Legality):** STL-GO renders topological and spatio-temporal obligations machine-readable; the paper does not investigate whether agents will concentrate optimization effort at the formal boundary (e.g., satisfying letter of constraint while violating spirit).
- **seed-076 (Handler-Lodged Ossification in Opaque Protocols):** Once spatio-temporal constraints are encoded as logical formulas, modification and adaptation become subject to verification overhead; the paper does not track how this locks in initial constraint choices.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
