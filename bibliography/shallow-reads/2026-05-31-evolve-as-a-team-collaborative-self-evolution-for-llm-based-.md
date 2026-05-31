# Evolve as a Team: Collaborative Self-Evolution for LLM-based Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2605.29790
**Date read:** 2026-05-31
**Connected to:** L-005
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems engineering paper proposing methods for multi-agent LLM systems to self-improve through experience-driven evolution, addressing execution failures that persist despite design-phase optimization. The work treats MAS failure recovery as a learning problem rather than a redesign problem.

## What I took from it

This is a practical engineering response to L-005 (working systems resist restructuring), but it does not challenge or extend the law—it operationalizes avoidance of it. The paper assumes that MAS evolution must happen *post-deployment, within constraints*, rather than investigating *why* redesign resistance emerges in multi-agent systems or what conditions make it stronger or weaker.

The work is relevant to H-002 (trust accumulation via age/stability) only tangentially: it shows that systems *can* improve through experience, but does not examine whether execution-driven patches generate trust differently than design-phase correctness does. The framing treats evolution as a technical optimization problem (how to extract and apply lessons from tangled execution traces) rather than as a protocol governance or coordination problem.

## Research connections

- **L-005:** Confirms that complex MAS systems resist redesign; proposes in-place evolution as a workaround rather than investigating the mechanism of resistance itself.
- **H-002:** Silent on whether accumulated experience-driven patches create durable confidence in the system or merely mask underlying structural brittleness.

## Candidate laws or signals

none
