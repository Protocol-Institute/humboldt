# StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2607.05844
**Date:** 2026-07-08
**Relevance:** Directly addresses formal conflict resolution mechanisms in multi-agent coordination, exemplifying CL-002 (how systems minimize coordination overhead through deterministic memory abstractions) and CL-003 (trust requirements when agents must agree on divergent observations in safety-critical contexts).

## Summary

arXiv:2607.05844v1 Announce Type: cross 
Abstract: Agent systems accumulate conflicting observations across branches, retries, and replicas, yet many practical memory layers still collapse disagreement behind overwrite rules that are difficult to inspect or correct. We present StateFuse, a conflict-aware replicated memory contract built on standard OpSet/CRDT merge. StateFuse does not introduce a new join algebra; it defines an agent-facing semantics layer with immutable history, explicit conflict objects, exact and semantic correction handles (claim_id / claim_ref), deterministic predicate co
