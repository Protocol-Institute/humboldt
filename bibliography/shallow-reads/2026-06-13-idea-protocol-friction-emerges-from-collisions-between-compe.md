# Idea: Protocol friction emerges from collisions between competing temporal systems (clocks)

**Source:** Discord #External rhythm as temporal protocol (by sachbenny)
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** Introduces a governance-layer framework for understanding protocol failure modes. Not yet mechanically developed enough to warrant hypothesis promotion, but identifies a genuine conceptual gap: current inventory treats temporal coordination as a technical problem; this frames it as a *jurisdictional* one. Warrants observation across multiple protocol domains before formalizing.

## What this is

Protocol friction arises not from temporal desynchronization alone, but from structural collisions between systems that enforce *different* clocks with mutually incompatible claims to authority and coordination authority.

## What I took from it

This reframes a category of protocol failures we've been observing as technical glitches (clock drift, latency, synchronization loss) into *governance* failures. The idea surfaces that two systems can both be functioning correctly according to their own temporal rules and still produce friction—because those rules conflict at the boundary, and neither has clear precedence. This is distinct from mere misalignment; it's a claim about *enforceability*.

The contribution opens a research direction: protocol friction may be predictable and mappable not by studying individual clock mechanisms, but by analyzing the *stakes and jurisdictional claims* each temporal system asserts. A blockchain consensus layer, a database transaction log, and a human-facing UI may all have internally coherent clocks, but their collision points are where power is disputed, not where signals are garbled.

This challenges the implicit assumption that better synchronization alone solves protocol failures. It suggests some failures are *structural* to the claim-conflict itself.

## Research connections

- None yet. Current inventory does not contain established laws or active hypotheses on temporal governance or jurisdictional conflict in protocolized systems.

## Candidate laws or signals

**CL-sachbenny-1:** Protocol friction correlates with jurisdictional collision between enforcement mechanisms, not merely with temporal desynchronization; where two systems assert incompatible authority over a clock boundary, friction emerges regardless of technical precision.
