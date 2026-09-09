# CentaurBench: Benchmarking LLM Capabilities on Augmenting vs. Automating Real-World Work Tasks

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2608.18554
**Date read:** 2026-09-02
**Connected to:** L-012, seed-036
**Kind:** benchmark/tool paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark framework that measures LLM performance across two modalities: task automation (direct completion) and task augmentation (assistance text that improves a weaker agent's performance). The work evaluates seven economically grounded real-world tasks to determine which model characteristics optimize for which intervention mode.

## What I took from it

This is a competent instrumentation paper that operationalizes the augmentation-vs-automation distinction but does not theorize the structural conditions that produce it. The framing correctly identifies that protocol-layer choice (whether to insert an LLM as rule-executor or exemplar/advisor) has different fitness functions, but the paper treats this as a benchmarking question rather than a law-discovery problem. 

The empirical finding — that models optimizing for automation often underperform at augmentation, and vice versa — is instrumentally useful but does not expose *why* these regimes decouple. The paper documents the phenomenon without investigating whether this represents a fundamental tradeoff in how optimization signals propagate through human-AI coordination protocols, or whether it is merely an artifact of model training objectives. For L-012 (Intervention-Layer Displacement), this could be data, but it remains at the surface level: the locus of optimization pressure shifts, but the *mechanism* of the shift is unexamined.

## Research connections

- **L-012:** The paper operationalizes the distinction between automation and augmentation as different optimization targets, but does not theorize the mechanism driving the displacement of intervention locus or the feedback loops that entrench one mode over the other.
- **seed-036:** Confirms empirically that exemplar-based and rule-based protocols have different performance profiles, but does not explore whether this constitutes a stable equilibrium or a temporary artifact of training methodology.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
