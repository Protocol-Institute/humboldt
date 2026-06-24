# Idea: Procedure has a fixed sequence, while protocol operates over a typed space of possible values

**Source:** Discord #I imagine the gap is outline in that ZIP (by humboldt)
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** The distinction articulated here is structurally sound but does not yet constitute a novel empirical claim about protocolized systems. It restates a formal category difference without proposing a law governing *how* or *why* systems exhibit one structure versus the other, or what consequences follow from that difference. Stored for refinement pending evidence of differential behavior, failure modes, or design constraints that bind to this distinction.

## What this is

The claim that procedures are constrained to deterministic linear execution paths while protocols are defined over typed value spaces, implying they require distinct formal frameworks for description and analysis.

## What I took from it

This idea correctly identifies a *structural* difference in how these two system types are typically formalized—and it is true that a linear state machine differs formally from a state space defined by type signatures and allowed transitions across values. However, the idea remains at the level of *category distinction* rather than *law*. It does not yet explain: (1) whether this difference is *fundamental* or merely conventional in how we currently model these systems; (2) what empirical or behavioral consequences follow from operating over typed spaces vs. fixed sequences; (3) whether hybrid systems (e.g., protocols with sequence constraints, procedures with value type guards) blur or validate the boundary.

The triage note's assessment that this "reiterates protocol/procedure typing distinction; conceptually redundant with 1, 4, 7" suggests this observation is already captured in the inventory—likely as part of the *definitions* of protocol and procedure rather than as a *law* governing their behavior.

## Research connections

- **None currently mapped** — awaiting explicit hypothesis linking formal structure to measurable system properties (e.g., failure propagation, composition difficulty, adaptability).

## Candidate laws or signals

**None.** 

This idea is a useful *analytical clarification* but does not yet contain sufficient predictive or explanatory power to warrant promotion. It would escalate if paired with evidence such as: "Systems with fixed-sequence structure exhibit higher cascade-failure rates than typed-space systems under identical perturbation" or "Protocol-based governance adapts faster to new value types than procedure-based governance adapts to sequence changes." Until such a differential law is proposed and tested, this remains a structural observation in the existing taxonomy.
