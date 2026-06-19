# Idea: Protocols represent only a subset of all possible futures—those they were designed to guard against

**Source:** Discord #Discussion: 2026-06-17 (by humboldt)
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** Strong conceptual claim requiring formalization before promotion; introduces useful failure taxonomy but lacks operational definition of "unrepresented futures" and causal mechanism linking incompleteness to failure modes.

## What this is

This idea proposes that protocols inherently fail not through malfunction but through *design blindness*—they can only defend against futures their architects anticipated, leaving all others as structural vulnerabilities.

## What I took from it

The claim cuts against two common framings: (1) the assumption that protocols are exhaustive or universal safeguards, and (2) the notion that protocol failure is primarily a breakdown in execution. Instead, it locates failure in the *design boundary* itself. This is a genuine addition to the inventory because it shifts the failure site from "protocol vs. reality" to "imagined threat space vs. actual threat space."

The idea opens a crucial research direction: **What distinguishes futures that were designed-for from futures that were designed-against?** This inverts typical robustness thinking. It also suggests a taxonomy of protocol failure that's prior to implementation: some failures are *inevitable by design*, not contingent on performance.

However, the claim needs tightening. "Subset of all possible futures" is too broad—protocols don't typically aim at *all* futures, only relevant ones. The real question is whether the *relevant subset* (threats to a system) was correctly bounded at design time. That distinction matters for distinguishing between *incomplete protocols* and *inappropriately scoped protocols*.

## Research connections

- None currently in inventory (new direction).

## Candidate laws or signals

**CL-Humboldt-01:** *Protocol failure includes a non-contingent class: futures falling outside the threat-space designers anticipated, rendering protocols structurally blind rather than functionally broken.*

**Note:** Promote only after defining: (1) how to operationalize "designed-against" vs. "unrepresented," (2) whether blindness is *universal* (all protocols) or *contextual* (some threats intrinsically unforeseeable), and (3) whether this predicts failure *severity* or only *occurrence*.
