# Does Multi-Agent Collaboration Pay When Agents Serve Users? Testing Agent Scaling in Dual-Control Settings

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.27655
**Date read:** 2026-11-23
**Connected to:** L-006, seed-462
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical benchmarking study testing whether multi-agent LLM systems outperform single-agent systems when operating under user-interaction constraints and written policy, extending prior autonomous-benchmark findings into dual-control settings. The work reports capability-saturation effects but does not advance theoretical mechanism or generalize the pattern beyond the specific task domain.

## What I took from it

The paper tests L-006 (Coordination Cost Conservation) in a user-facing context, finding that the prior autonomous-benchmark rule (coordination helps below ~45% SAS accuracy, hurts above) may not hold identically when users are in the loop. This is a domain-specific modulation of the law, not a challenge to it or a mechanism clarification. The dual-control setting introduces human judgment as a variable, but the paper does not theorize how user-driven interruption, overrides, or policy constraints *change the structure* of coordination cost — it appears to treat user presence as a task-difficulty modifier rather than a protocol-layer reorganization. No novel mechanism for cost displacement emerges; no new equilbrium topology is exposed. The work is competent but descriptive rather than law-generative.

## Research connections

- **L-006:** Finds capability-saturation crossing in dual-control; consistent with coordination-cost conservation but does not expose the mechanism of cost displacement under user interaction.
- **seed-462:** Mentions mean-field legibility and equilibrium targeting; the paper does not examine whether user presence creates new legibility surfaces or shifts equilibrium target.

## Seed

**Seed title:** none
