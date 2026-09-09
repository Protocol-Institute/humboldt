# Why are all LLMs Obsessed with Japanese Culture? On the Hidden Cultural and Regional Biases of LLMs

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2604.21751
**Date read:** 2026-09-02
**Connected to:** L-004, L-013
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark/empirical survey paper that documents regional bias patterns in LLM outputs across 24 languages using a new dataset (CROQ). The work identifies and measures systematic overrepresentation of certain cultures (notably Japanese) in generic culture-related questions, but does not propose a mechanistic theory of why this occurs or how the bias propagates through training pipelines.

## What I took from it

The paper provides useful phenomenological evidence for L-013 (Paradigm-Locked Anomaly Tolerance) — the bias toward Japanese culture persists across multiple model families and sizes, yet has not triggered major architectural or training protocol changes. However, the work is descriptive rather than explanatory: it does not investigate *why* training objectives (coverage metrics, next-token prediction) fail to correct for regional imbalance, nor does it examine the feedback loops that lock this preference into place.

The connection to L-004 (Goodhart Generalization) is weaker than the triage suggested. The paper does not show that coverage metrics are *actively being optimized* to the point of distortion; rather, it shows that coverage imbalance emerges as a byproduct of training data composition and is then tolerated. This is passive anomaly tolerance, not metric capture.

## Research connections

- **L-004:** Weak connection. The paper shows regional bias in outputs but does not trace this to active optimization of a coverage proxy or demonstrate the feedback loop that would constitute Goodhart capture.
- **L-013:** Direct connection. LLM training protocols exhibit stable tolerance of documented regional preference anomalies despite their visibility and potential harm — exemplifying paradigm-locked tolerance in safety-critical decision protocols.
- **seed-069:** Transparency paradox: the biases are detectable and measurable, yet legibility does not trigger corrective action, suggesting that measurement alone does not substitute for trust-repair mechanisms.

## Seed

**Seed title:** Measurement-Resistant Bias Persistence in Training Protocols

**Seed type:** observation

**Seed text:** In large-scale training protocols where output bias is measurable and documented but orthogonal to the primary optimization objective (next-token prediction), systematic preference drift emerges and stabilizes without triggering architectural intervention. The bias persists across scaling and model families because the training objective does not encode correction for it, and no secondary protocol layer (e.g., preference-tuning, safety layer) has been formalized as *mandatory* rather than optional. This suggests that measurement of anomalies in protocol systems does not automatically induce repair when the anomaly is not encoded as a computable constraint within the primary objective function.
