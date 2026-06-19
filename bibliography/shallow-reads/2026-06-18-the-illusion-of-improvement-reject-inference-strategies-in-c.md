# The Illusion of Improvement: Reject Inference Strategies in Credit Scoring

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.18479
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** This identifies a structural failure mode endemic to feedback cycles in scoring protocols—where standard accuracy metrics mask deterioration in decision quality—and proposes a mechanism for diagnosing it; the pattern likely generalizes across all selection/rejection systems under retraining.

## What this is

An empirical study of reject inference methods used to correct survival bias in credit scoring. The work systematically demonstrates that retraining cycles can produce models whose accuracy improves while their capacity to reject true defaulters collapses, creating a measurement illusion that leads operators to reinforce failing systems.

## What I took from it

This paper identifies a critical pathology in how protocolized systems *measure their own improvement*. The core insight is that accuracy (a global metric) and rejection quality (a domain-specific metric) can decouple under retraining, especially when the system selects its own training data. This is not a tool failure or a calibration problem—it's a structural trap: the protocol's feedback loop actively rewards the illusion of performance while the underlying decision boundary degrades.

This maps directly onto governance of artificial systems: practitioners observe the metric they're trained to optimize (accuracy) and miss the metric that matters for the system's stated purpose (safe rejection). The paper suggests this isn't accidental but *built into* how reject inference retraining works. If the mechanism is general, it should appear wherever selection bias is corrected via retraining on accepted cases.

## Research connections

- none yet (establishing baseline)

## Candidate laws or signals

**CL-2606.18479-1:** *Metric Decoupling Under Self-Selected Retraining* — In scoring systems that perform inference on rejected cases to correct survival bias, accuracy and rejection-quality metrics can diverge monotonically; improving one via standard retraining protocols degrades the other, producing an illusion of improvement that persists until domain-specific validation occurs.

**CL-2606.18479-2:** *Feedback Loop Inversion in Selection Systems* — Protocolized rejection systems under autonomous retraining can converge toward states where the optimization target (measured accuracy) becomes inversely correlated with the system's functional purpose (safe rejection), with no internal signal to detect this inversion.
