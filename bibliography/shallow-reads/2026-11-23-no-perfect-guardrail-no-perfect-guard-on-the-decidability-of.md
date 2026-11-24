# No Perfect Guardrail & No Perfect Guard: On the Decidability of Output Policies for Large Language Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.27260
**Date read:** 2026-11-23
**Connected to:** L-004, L-013, L-015
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper establishing computational decidability limits on output policy enforcement for LLMs. The authors argue that guaranteeing safety via guardrails is impossible in principle (not merely difficult in practice), and that framing enforcement this way constitutes both precision failure and moral abdication. The work is primarily conceptual/argumentative rather than presenting novel empirical evidence or mechanism.

## What I took from it

The paper articulates a hard boundary between what can be computationally *specified* and what can be *enforced* — relevant to L-004 (metric capture under optimization pressure) and L-013 (paradigm-locked anomaly tolerance). The core claim — that perfect decidability of output legality is unattainable — echoes the realizability gap, but does not propose a mechanistic account of how systems *respond* when this limit is discovered or ignored.

The work's ethical framing (responsibility cannot be discharged into a guardrail) is a normative claim about institutional behavior under legibility pressure, tangentially touching L-015 (interpretive continuity decay in distributed governance). However, the paper offers no mechanism for why institutions *persist* in invoking impossible guarantees, nor does it empirically track how anomaly evidence accumulates when perfection claims fail. It diagnoses a problem but does not explain the protocol dynamics that cause systems to remain locked in the diagnosis rather than revising their operating model.

## Research connections

- **L-004:** Metric capture assumes the metric is computable; this paper argues some safety properties are fundamentally non-decidable. Establishes a necessary condition for where Goodhart *cannot* occur.
- **L-013:** Paradigm-locked anomaly tolerance — the paper's argument predicts that guardrail systems should accumulate failures without triggering regime change, but provides no empirical mechanism for why institutions tolerate non-closure of the decidability gap.
- **L-015:** Institutional memory of interpretive standards can survive even when the formal computational envelope proves inadequate; relevant to how "guardrail sufficiency" narratives persist despite proven limits.
- **seed-544:** Metalinguistic displacement under formalization pressure — guardrails are a formalization attempt; the paper argues formalization *fails*, but does not model what happens to discourse when failure is structurally unavoidable.

## Method note

This work demonstrates the value of establishing *negative results* — computational impossibility theorems — as anchors for the new nature research agenda. However, the gap between proving something is impossible and explaining why systems continue to behave *as if* it were possible is a critical one for protocol research. The paper would strengthen the funnel if paired with empirical tracking of how guardrail failure evidence feeds back into institutional decision-making (or fails to). Meta-research should consider: what is the relationship between decidability arguments and actual protocol reform velocity?
