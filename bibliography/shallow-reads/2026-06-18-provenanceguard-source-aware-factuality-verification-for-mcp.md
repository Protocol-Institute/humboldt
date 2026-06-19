# ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.18037
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A tool paper introducing ProvenanceGuard, a verification system that audits factuality claims in LLM agents using the Model Context Protocol (MCP) by checking whether answers are attributed to correct sources rather than merely supported somewhere in pooled evidence. The work identifies "cross-source conflation" as a failure mode in heterogeneous tool-using systems.

## What I took from it

The paper makes a real observation about information integrity in multi-source agent systems: standard factuality metrics operate on pooled evidence and are blind to *which source* a claim should be attributed to, creating a failure where correct facts become corrupted through misattribution. This is a local verification problem rather than a systemic one — it addresses how to audit and correct a specific category of error rather than understanding why conflation occurs or how it propagates through agent policies.

The contribution is methodological (a verifier design) rather than theoretical. It confirms that heterogeneous sourcing creates novel error classes, but doesn't explain the generative mechanism or test whether this pattern holds across different protocol architectures or agent types. The MCP context is incidental; the problem would exist in any multi-source system where source identity must be preserved.

## Research connections

- **[Pending law: Information integrity under heterogeneous sourcing]:** Confirms that pooled-evidence metrics miss source-attribution failures; doesn't explain conditions that trigger conflation or whether it's inevitable vs. design-dependent.

## Candidate laws or signals

- **CL-Attribution-Pooling-Gap:** When multi-source systems aggregate evidence without explicit source tracking, verifiers trained on pooled support may conflate correct facts with incorrect source assignment, creating a class of errors invisible to unsourced factuality metrics.
