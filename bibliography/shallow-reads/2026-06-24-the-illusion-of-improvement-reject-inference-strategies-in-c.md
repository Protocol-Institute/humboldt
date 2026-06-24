# The Illusion of Improvement: Reject Inference Strategies in Credit Scoring

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.18479
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Identifies a structural failure mode in retraining cycles where metric alignment breaks down (accuracy rises while rejection quality falls), revealing a mechanism for how protocolized systems can deteriorate while appearing to improve—absent from current inventory.

## What this is

A systematic empirical study of reject inference methods used to correct survival bias in credit scoring models. The paper demonstrates that standard retraining cycles create a pathological dynamic: models achieve higher accuracy while simultaneously losing the ability to identify defaulters, generating a false signal of improvement that masks performance collapse on the task that matters.

## What I took from it

This work exposes a critical misalignment between measurement and ground truth in adaptive systems. The core insight is that reject inference—a standard debiasing technique—creates conditions for metric gaming in retraining loops. When a model is retrained on newly labeled rejected applicants, accuracy can improve (as the training set becomes more balanced) while recall on the actual risk class deteriorates, because the distribution of rejections itself becomes corrupted by prior model decisions. This is not a calibration problem or a simple false positive rate issue; it's a **structural incentive failure** baked into the feedback loop.

The mechanism appears generalizable: any system that uses its own rejection decisions as training signal for the next iteration risks this collapse, especially when the measurement used to declare "improvement" is decoupled from the downstream consequence (default). This suggests a deeper law about how protocolized systems degrade through repeated cycles when ground truth is delayed or mediated by the system's own output.

## Research connections

- **Feedback loop corruption:** Systems that use their own decisions as training labels risk creating self-reinforcing degradation masked by upstream metrics.
- **Measurement-reality decoupling:** A system can satisfy its declared optimization target (accuracy) while failing catastrophically at its actual function (risk screening).

## Candidate laws or signals

- **CL-2606.18479-A:** In adaptive systems where ground truth arrives only for accepted cases, retraining on rejected cases labeled by the prior model creates a structural failure mode where optimization metrics decouple from functional performance across retraining cycles.
- **CL-2606.18479-B:** Protocolized systems exhibit "improvement illusions"—sustained periods where internal metrics improve while operational fitness declines—when measurement targets are upstream of the true loss function.
