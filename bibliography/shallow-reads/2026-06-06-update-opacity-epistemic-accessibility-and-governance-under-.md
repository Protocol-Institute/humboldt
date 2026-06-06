# Update Opacity: Epistemic Accessibility and Governance Under AI System Change

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.00037
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Introduces update opacity as a diachronic epistemic failure mechanism absent from current inventory; generalizes beyond specific systems to a structural property of adaptive deployed systems; directly enables governance under model change.

## What this is

A theoretical paper arguing that routine ML model updates in deployed systems create a distinct epistemic problem—update opacity—where users cannot understand why identical inputs now produce different outputs. The work frames this as a *diachronic* failure of epistemic accessibility (across time), not a static interpretability problem, and connects it to governance, calibration, and appropriate reliance.

## What I took from it

This identifies a governance failure mode that emerges specifically from the temporal structure of adaptive systems. The paper distinguishes between opacity *of a system* (interpretability at a moment) and opacity *of change* (inability to track or understand what shifted). This is crucial: it suggests that protocolized systems face a unique epistemic burden as they evolve—the users' mental models and calibrations can become systematically misaligned with the actual system, even if the system itself is locally interpretable. 

The work implicitly treats deployed AI as a *new natural object* that exhibits properties not present in static systems: the requirement to maintain epistemic accessibility *across updates*. This opens a research direction on temporal coherence of governance structures. If users cannot track why behavior changed, they cannot exercise oversight, cannot learn system boundaries, and cannot build appropriate trust. This is a failure mode of the system-as-evolving-whole, not just of transparency or explainability.

## Research connections

- **Epistemic accessibility under change:** A structural property of adaptive protocolized systems; governance cannot function without diachronic transparency.
- **Calibration and reliance:** Update opacity breaks the feedback loop that allows users to calibrate their trust and behavioral response to system capabilities.

## Candidate laws or signals

- **CL-2606-01:** Adaptive deployed systems generate epistemic obligations that exceed static interpretability requirements; update opacity is a distinct governance failure mode that arises from temporal misalignment between user models and system behavior.
