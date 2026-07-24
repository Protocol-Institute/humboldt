# Idea: Organizations face a coordination problem when the same question generates different answers across models, times, and effort levels

**Source:** Discord #Unfortunately, I did not keep the chat. (by humboldt)
**Date read:** 2026-07-24
**Connected to:** CL-002
**Escalation:** store-only
**Escalation rationale:** The idea correctly identifies a real organizational friction point, but it restates the coordination-cost-conservation principle without introducing new mechanistic detail, operationalization, or empirical boundary conditions. It would benefit from specification (variance across *what dimensions* creates *which* coordination costs?) before promotion.

## What this is

Organizations must absorb variance costs when identical queries to protocolized systems (models, APIs, question-answering pipelines) produce distributed rather than deterministic outputs, forcing reallocation of oversight labor rather than elimination of coordination burden.

## What I took from it

This observation sits squarely within CL-002's frame: costs are conserved, not eliminated. Where CL-002 posits that protocol automation trades direct coordination for indirect verification/reconciliation overhead, this idea grounds that claim in a concrete failure mode—the *instability* of outputs across repetition, model selection, or input framing.

The idea is sound but currently underdeveloped. It identifies *that* there is a problem but not *when* or *how much*. Key open questions:

- Is the variance problem primarily epistemic (models genuinely uncertain) or operational (hyperparameter/seed variance)? 
- Does the coordination cost scale with variance magnitude, or is there a step function (any variance triggers a verification layer)?
- What determines whether an organization tolerates variance vs. demands single-answer canonicality?

This could become a law if we operationalize the link between output variance and labor reallocation, or anchor it to measurable system properties (entropy, confidence bounds, decision-tree depth).

## Research connections

- **CL-002:** Directly instantiates the cost-conservation principle; variance-absorption is a mechanism for why protocol automation does not reduce net coordination burden.

## Candidate laws or signals

**None.** The idea is a sound *application* of CL-002, not a new pattern. Promote to **CL-Candidate** only if paired with:
1. Operationalized measure of variance (e.g., answer entropy, disagreement ratio across k runs)
2. Empirical correlation between variance magnitude and verification-labor hours
3. Boundary condition: under what system/organizational properties does variance become coordination-critical?
