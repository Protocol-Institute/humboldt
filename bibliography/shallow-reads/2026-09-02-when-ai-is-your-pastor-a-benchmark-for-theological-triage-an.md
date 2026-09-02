# When AI Is Your Pastor: A Benchmark for Theological Triage and Pastoral Guidance in Large Language Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.12324
**Date read:** 2026-09-02
**Connected to:** L-004, L-013
**Kind:** benchmark/evaluation paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper (FMG-Bench) designed to evaluate how LLMs handle pastoral and theological guidance—questions that involve unmeasurable judgment calls, doctrinal disagreement, prudential reasoning, and safety-critical referral decisions. The work identifies that existing evaluation frameworks flatten these distinctions into generic "correctness" metrics.

## What I took from it

The paper identifies a real structural problem in how AI systems are evaluated on tasks where the output space is irreducibly normative and context-dependent. The authors correctly observe that theological triage cannot be reduced to a single metric without collapsing the very distinctions that make the task non-trivial: core doctrine vs. tradition-specific interpretation vs. pastoral safety vs. referral judgment.

However, the work does not propose a mechanism for *why* this collapse happens or why it persists. The paper is constructive (building a better benchmark) rather than investigative (explaining the law governing metric capture in normative domains). It documents the symptom—LLMs optimized on generic metrics fail at task-structure sensitivity—but does not treat this as a generalizable constraint on how formalized systems handle unmeasurable goals. The benchmark itself, while more nuanced, still faces the core problem it identifies: any evaluation grid will eventually become a target for optimization under deployment pressure (L-004, L-013 territory, but not advancing mechanism understanding).

## Research connections

- **L-004 (Goodhart Generalization):** The paper documents metric capture in a normative domain (theological triage), but treats it as a benchmark design problem rather than a regularity under protocol-wide adoption pressure.
- **L-013 (Paradigm-Locked Anomaly Tolerance):** The implicit argument—that systems trained on generic metrics will systematically mishandle structure-sensitive tasks—describes observed malfunction without triggering architectural reconsideration.
- **seed-077 (Metric-Induced Preference Ratcheting):** LLMs optimized on "guidance quality" metrics may be converging toward safer, less differentiated outputs rather than toward theologically sound ones.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
