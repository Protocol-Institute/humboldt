# What's in a Queue? An Experimental Study of Job Ordering, Autonomy and Queue Visibility

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.28820
**Date read:** 2026-09-02
**Connected to:** L-003, L-012
**Kind:** content
**Escalation:** store-only

## What this is

An online experimental study manipulating three dimensions of queue design (job ordering rules, worker autonomy over sequencing, and visibility of queue state and arrival information) to measure effects on worker speed and quality. The work treats queue presentation as a protocol design variable and tests how legibility and agency affect task execution in service operations.

## What I took from it

This is a clean empirical study of a narrow design space, but it operates at the level of task performance optimization rather than protocol-level mechanism discovery. The paper varies legibility (visibility conditions) and autonomy (ordering control) as independent factors, which connects to L-012's concern about decision-protocol design. However, the read suggests this will document *performance effects* of these conditions rather than expose a deeper regularity about how legibility shapes optimization pressure or how autonomy constraints propagate through protocol layers. The abstract indicates real-effort task experiments—competent work, but bounded scope. No evidence yet of sustained theoretical argument about how queue protocols ossify, how formalization ratchets under stress, or how coordination costs are displaced when visibility changes. Likely to be a useful micro-level benchmark for queue design, not a mechanism discovery about protocolized systems more broadly.

## Research connections

- **L-012:** Queue visibility as a formalization of decision inputs; workers' optimization locus may shift based on what information becomes legible to their sequencing choice.
- **L-003:** If autonomy + visibility interact to produce formalization pressure (e.g., workers given ordering control but full queue visibility may converge on standardized heuristics), this could illuminate the Formalization Ratchet under operational stress.
- **seed-072:** Explanation/marker decoupling — if workers can see queue state but not the arrival logic generating it, performance may decouple from actual system demand.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**STORE-ONLY JUSTIFICATION:** This is a competent experimental design study, but lacks sustained theoretical argument at the protocol level. It measures performance outcomes under visibility/autonomy conditions; it does not propose or test a mechanism absent from the current inventory, nor does it challenge existing laws. The connection to L-012 is suggestive but thin — the paper is unlikely to generalize a regularity beyond queue task design. Recommend tracking as a micro-domain benchmark; deep read warranted only if results show counterintuitive interaction effects that violate assumptions in L-003 or L-012.
