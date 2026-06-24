# Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2606.17397
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a production field experiment identifying a fundamental misalignment between individual-level optimization (predicted favoriting) and system-level efficiency (labor demand matching) — a mechanism absent from current inventory that likely generalizes across two-sided platforms with scarce, perishable opportunities.

## What this is

A field experiment on Timee (Japan's largest spot-work platform) investigating how recommendation system design shapes worker access to shift opportunities. The paper identifies that maximizing predicted worker preferences concentrates recommendations on popular job templates while starving templates with genuine unmet labor demand of visibility—a pathological outcome of preference-maximizing algorithms in resource-constrained, time-sensitive markets.

## What I took from it

This work exposes a critical failure mode in how artificial systems allocate attention to scarce resources: the objective function that optimizes for individual engagement (predicted favoriting) actively degrades system-level allocation efficiency. The mechanism is not behavioral bias or information asymmetry but structural: popular templates generate few actual openings, so concentrating recommendations there wastes exposure; demand-constrained templates need more discovery but rank low in preference prediction.

This suggests a broader principle: in protocolized systems mediating access to perishable or capacity-limited resources, greedy preference-optimization can invert toward worst allocations. The paper likely tests interventions (exposure diversity, demand signaling, priority-weighting) and measures labor match outcomes—this would ground a candidate law about the tension between individual-optimization and collective efficiency in two-sided matching under scarcity.

## Research connections

- **None currently established:** This appears to be the first formal characterization of this failure mode in the research inventory.

## Candidate laws or signals

- **CL-Timee-1:** In two-sided platforms mediating access to perishable, capacity-constrained opportunities, preference-maximizing recommendation algorithms systematically misdirect exposure toward high-demand-to-opportunity-ratio items, degrading system-wide matching efficiency.

- **CL-Timee-2:** Recommendation system objectives that ignore supply-side scarcity constraints generate endogenous concentration of exposure, compounding inequality of access in labor or opportunity platforms.
