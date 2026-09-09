# RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.12216
**Date read:** 2026-09-01
**Connected to:** L-006, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A measurement protocol (RCWT) that quantifies the token-budget tradeoff between coordination overhead and task capacity in multi-agent LLM systems operating under fixed context windows. The paper operationalizes a real constraint in deployed systems but does not present a primary theoretical argument or introduce a mechanism absent from the current inventory.

## What I took from it

The work provides empirical grounding for L-006 (Coordination Cost Conservation) in a specific contemporary domain—it demonstrates that coordination costs do not vanish under adoption pressure but rather displace task-relevant capacity in a measurable, zero-sum manner. This is useful validation rather than novelty.

The paper sits adjacent to L-012 (Intervention-Layer Displacement) but does not substantially engage with the mechanism: it measures *that* displacement occurs under budget constraint, not *why* optimization pressure migrates upward through protocol layers or what conditions trigger runaway displacement. The RCWT protocol itself is competent instrumentation but designed for local measurement, not generalizable law-finding.

## Research connections

- **L-006:** Direct operationalization in the LLM domain. Confirms that coordination cost conservation holds under finite resource constraints; adds no new mechanism or cross-domain pattern.
- **L-012:** Adjacent. Measures displacement of task capacity by coordination signals but does not examine how legibility of coordination content affects optimization pressure migration.
- **seed-020 (symptom-hierarchy-coordination-displacement):** Mild connection. The token-displacement effect is a symptom; unclear whether the paper addresses hierarchy questions about which coordination signals are sacrificed first.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
