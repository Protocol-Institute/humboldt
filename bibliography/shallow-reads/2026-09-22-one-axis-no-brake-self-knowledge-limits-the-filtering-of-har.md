# One Axis, No Brake: Self-Knowledge Limits the Filtering of Harmful Peer Conformity in LLMs

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.18998
**Date read:** 2026-09-22
**Connected to:** L-004, L-013, seed-129
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This presents a foundational mechanism — the impossibility of separating beneficial from harmful conformity filtering without solving the harder problem of self-knowledge — that generalizes across any multi-agent protocol where agents lack introspective access to their own correctness state.

## What this is

An empirical investigation into multi-agent LLM systems showing that peer correction in collaborative settings creates a structural bind: filtering harmful conformity requires knowing whether the original answer was correct, which is equivalent to solving the self-knowledge problem the system lacks. The work identifies a hard asymmetry between correction capacity and harm-prevention capacity.

## What I took from it

This cuts directly into L-004 (Goodhart Generalization) and L-013 (Paradigm-Locked Anomaly Tolerance) by showing that the *detection* of when a proxy (peer correction) has become harmful requires solving an unsolvable sub-problem. The paper does not merely show that peer correction can harm; it shows that the filtering mechanism itself is information-theoretically blocked unless the system can answer "was I correct?" — a question that defines the boundary of agent self-knowledge.

This is deeper than a Goodhart problem (metric captures the goal), because no metric is available: the system cannot compute whether correction was harmful without access to ground truth *and* access to its own prior epistemic state. The asymmetry is one-directional: agents can always be pushed to conform (conformity is cheap, requires only output alignment), but cannot reliably be held from conforming without solving introspection. This suggests conformity pressure is a fundamental property of multi-agent systems lacking introspective legibility.

## Research connections

- **L-004 (Goodhart Generalization):** The "brake" is an attempt to add a secondary metric to control the primary one (peer correction), but the control metric itself is uncomputable without self-knowledge.
- **L-013 (Paradigm-Locked Anomaly Tolerance):** The system cannot trigger on malignant conformity because detection requires the self-knowledge it does not possess; harmful corrections accumulate as undetected anomalies.
- **seed-129 (Legibility-Induced Conformity Locking):** Peer signals become legible correction inputs, but the legibility works only one direction — toward conformity, not toward discrimination between beneficial and harmful conformity.
- **seed-142 (Auditability-Legibility Trap in Trust Governance):** The system can audit what corrections were made, but cannot audit whether they were correct, creating a trap where transparency about corrections increases conformity pressure without enabling control.

## Seed

**Seed title:** Introspective Asymmetry in Multi-Agent Filtering

**Seed type:** mechanism

**Seed text:** In multi-agent systems where agents receive legible correction signals from peers, the filtering of harmful conformity is information-theoretically blocked unless the system can solve the introspection problem (knowing its own prior correctness). Beneficial and harmful conformity are indistinguishable at the point of decision without ground-truth access; therefore, filtering mechanisms designed to pass beneficial corrections and block harmful ones collapse to "deciding what was already known." This creates a one-directional ratchet: conformity pressure is always executable (requires only output alignment), but filtering always requires solving a harder problem than correction itself. The asymmetry is structural, not contingent on current model architecture.
