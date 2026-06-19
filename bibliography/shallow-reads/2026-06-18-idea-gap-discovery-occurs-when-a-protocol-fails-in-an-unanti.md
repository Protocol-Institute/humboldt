# Idea: Gap discovery occurs when a protocol fails in an unanticipated way — a failure mode not in its error-correction set

**Source:** Discord #Discussion: 2026-06-17 (by humboldt)
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** Idea articulates a useful distinction between *anticipated* and *unanticipated* failure modes and proposes a risk metric (consequence × arrival speed), but does not yet establish a generative law. The framework assumes error-correction sets exist and are knowable; the idea documents what happens when they fail rather than proposing new protocol behavior. Worth preserving for future law development once we have empirical data on gap danger correlation.

## What this is

When a protocol encounters a failure mode outside its designed error-correction set, the resulting "gap" poses risk proportional to both the severity of consequences and the speed at which the failure arrives.

## What I took from it

This idea makes explicit a distinction that has been implicit in protocol design thinking: the difference between *failures we anticipated and built safeguards for* versus *failures we did not anticipate*. It proposes that gap danger is not merely the presence of an unanticipated failure, but a function of two measurable variables—consequence magnitude and arrival velocity.

The claim complements but does not displace existing thinking about error-correction. It assumes error-correction sets are intentionally bounded and finite, which is reasonable; it then names the space outside that boundary as a legible risk surface. This is useful for triage and auditing: it gives us a way to ask *which unanticipated failures matter most?* rather than treating all unknowns as equal.

The idea does not yet establish *why* these two variables correlate with danger, or whether gap danger follows a predictable function (additive? multiplicative?). That gap remains open for empirical work.

## Research connections

- *None at present inventory.*

## Candidate laws or signals

**CL-2026-Gap-01:** Gap danger = f(consequence magnitude, arrival speed), where gaps are protocol failures outside the error-correction set; candidate law pending empirical measurement of the functional relationship and validation across protocol types.
