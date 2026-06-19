# Idea: The possible futures represented by a protocol are only those it was designed to

**Source:** Discord #Discussion: 2026-06-17 (by humboldt)
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** Strong restatement of protocol-incompleteness principle. Requires consolidation into formal candidate law rather than independent escalation.

## What this is

A claim that protocols are fundamentally *representationally bounded*: they can only guard against futures they were designed to anticipate, making unrepresented futures the structural locus of protocol failure.

## What I took from it

This idea usefully inverts the usual framing of protocol failure. Rather than treating failure as a defect or surprise, it locates it as inevitable—a consequence of the finite design scope. The distinction between *represented* and *unrepresented* futures is sharper than "known unknowns vs. unknown unknowns" because it ties failure directly to the protocol's own design history and intention set.

This is a refinement rather than a novel claim: it clarifies where incompleteness *manifests*. It opens a question about whether protocols can be designed to degrade gracefully in unrepresented space (rather than catastrophically), and whether we can map the boundary between represented and unrepresented futures ex ante.

The idea also suggests that protocol robustness may be better measured by the *coverage ratio* of design scenarios to actual futures than by elimination of bugs.

## Research connections

- None currently in inventory; appears to formalize the intuition behind "protocol incompleteness" without yet being formally stated.

## Candidate laws or signals

**CL-Protocol-01:** A protocol's failure modes are constrained to futures outside its representational design scope; unrepresented futures are the primary locus of protocol failure, not execution errors within represented space.
