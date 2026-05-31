# Idea: Standardization specifications like GD&T (Geometric Dimensioning and Tolerancing)

**Source:** Discord #🦾-distributed-robotics (by 4umd)
**Date read:** 2026-05-31
**Connected to:** L-004
**Escalation:** store-only
**Escalation rationale:** The idea applies L-004 to a concrete domain (manufacturing metrology) but does not reveal a new law or challenge the existing inventory. It is an instructive case study, not a novel pattern.

## What this is

GD&T specifications encode domain expertise into formal metrics, which then become optimization targets in contexts beyond their original design purpose, exemplifying metric capture under adoption pressure.

## What I took from it

This is a well-observed instantiation of L-004 (Goodhart Generalization), not a distinct claim. The idea correctly identifies that formalizing tacit manufacturing knowledge into standardized tolerances creates a measurable proxy that can decouple from the underlying goal (robust, fit-for-purpose design) when applied outside its original calibration context—e.g., when GD&T becomes a quality assessment tool in domains with different failure modes or cost structures than the ones it was designed for.

However, L-004 already captures this mechanism: *any* measurable proxy under optimization pressure causes the proxy to degrade as a measure of the original goal. GD&T is an exemplar, not a exception or refinement. The idea does not challenge the law, extend its scope conditions, or propose a new interaction pattern.

The connection to L-003 (Formalization Ratchet) is also present but secondary—formalization *enables* metric capture, but the capture itself is the mechanism L-004 describes.

## Research connections

- **L-004:** Direct instantiation; GD&T metrics become targets rather than measures under adoption pressure in new domains.
- **L-003:** Formalization of tacit manufacturing norms into explicit GD&T standards exemplifies the ratchet, but does not extend it.
- **H-002:** Implicit signal: GD&T is trusted *because* it is old and widely adopted, not necessarily because it remains technically correct for all downstream applications.

## Candidate laws or signals

None. This idea is well-integrated into L-004 and requires no promotion.
