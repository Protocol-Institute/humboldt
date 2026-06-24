# Societal Alignment Frameworks Can Improve LLM Alignment

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2503.00069
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper arguing that LLM alignment failures stem from a specification gap—the mismatch between complex, distributed human values and narrow technical objectives. The work proposes that societal-level alignment frameworks (drawing on contract theory and institutional design) could better ground alignment methods than current narrow optimization approaches.

## What I took from it

The paper identifies a real structural problem in protocolized systems: **specification-reality gap under value pluralism**. When a system must align with a heterogeneous population holding incommensurable values, single-objective proxies (RLHF, constitutional AI, etc.) become incomplete contracts—they systematically misspecify the target. This is a coordination problem, not purely a technical one.

However, the work does not propose a *mechanism* for how societal frameworks would resolve this—it gestures toward institutional economics without formalizing how distributed preference aggregation would be *protocolized* or what happens when alignment frameworks themselves become contested. The abstraction level remains at diagnosis rather than system design. It also stays within the LLM domain and does not demonstrate whether this is a general law of protocolized systems under value heterogeneity or artifact-specific.

## Research connections

- none currently active (no established laws or active hypotheses to reference)

## Candidate laws or signals

- **CL-Alignment-1:** *Systems designed to satisfy heterogeneous, non-decomposable values cannot achieve alignment via single objective functions; they require meta-protocol that surfaces rather than elides value trade-offs.*
