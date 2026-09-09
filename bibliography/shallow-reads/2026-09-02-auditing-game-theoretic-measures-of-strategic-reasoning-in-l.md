# Auditing Game-Theoretic Measures of Strategic Reasoning in LLMs

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2603.10029
**Date read:** 2026-09-02
**Connected to:** L-004
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark audit paper that discovers systematic failures in a widely-used game-theoretic test suite for LLM strategic reasoning. The authors re-ran 1,855 interactions across seven LLMs and found that token limits caused silent parser failures—empty model outputs were replaced with fixed default actions—invalidating reported capability profiles and contaminating downstream comparisons.

## What I took from it

This is a textbook instantiation of L-004 (Goodhart Generalization: Metric Capture), but operating at the *measurement layer* rather than the optimization layer. The benchmark itself became the target, not through model gaming, but through invisible measurement corruption. The paper shows that when a protocol (here: the evaluation framework) promises legibility via structured game-theoretic output, silent degradation under load conditions can invert the semantic meaning of "no response" into a false semantic signal. This matters because it suggests that metric capture in artificial protocol systems doesn't require intentional adversarial optimization—it can arise from routine implementation constraints meeting poorly-audited parsers.

The work doesn't generalize a new law or mechanism; it is a high-fidelity confirmation that measurable proxies for unmeasurable constructs (here: "strategic reasoning capacity") will degrade under stress. What it adds is precision about *where* degradation occurs: not in the model's reasoning, but in the instrumentation boundary between the model's output space and the observer's interpretation layer.

## Research connections

- **L-004:** Direct confirmation. Token limits created conditions under which the proxy (parsed game move) diverged from the construct (actual strategic reasoning), but the divergence was transparent only under audit. The metric was captured not by the model optimizing for it, but by the measurement apparatus failing silently.

- **seed-072 (Explanation-Marker Decoupling Under Scaled Legibility):** The paper shows how formalized output parsing creates a legible surface (move selection) that can decouple from actual reasoning state, especially under resource constraints.

- **seed-062 (Formalization Opacity Collapse):** Automation of result parsing collapsed an apparent opacity (model behavior) into a false certainty (fixed default action as semantic meaningful output).

## Seed

**Seed title:** Silent Parser Capture Under Constraint Stress

**Seed type:** observation

**Seed text:** In protocol systems where model or agent output is automatically parsed into a fixed semantic space (game moves, classification labels, structured decisions), silent failure modes—where empty or truncated output is replaced by default actions—can corrupt the metric without triggering anomaly signals. The legibility of the formalized output boundary masks degradation in the underlying reasoning. This suggests that measurement corruption in artificial systems scales not with optimization pressure on models, but with the invisibility of the instrumentation layer to auditors.
