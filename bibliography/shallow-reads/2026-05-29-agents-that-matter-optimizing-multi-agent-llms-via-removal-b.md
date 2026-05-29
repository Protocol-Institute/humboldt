# Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2605.27621
**Date read:** 2026-05-29
**Connected to:** L-005
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper formalizing credit assignment in multi-agent systems through cooperative game theory, demonstrating that simple removal-based methods (Leave-One-Out) can identify critical agents with computational efficiency comparable to combinatorial approaches. The work is domain-specific (LLM agent optimization) and methodological rather than presenting a sustained theoretical argument about protocol dynamics.

## What I took from it

The paper addresses a real problem in complex MAS: determining which agents matter for overall system performance. The framing as a cooperative game is sound, but the relevance to L-005 (Gall's principle on system restructuring) is indirect and shallow. L-005 concerns *whether* complex systems can be safely modified; this work assumes you *can* identify which components are critical and proceeds to optimize around them. 

The implicit assumption—that removing agents one-by-one provides sufficient attribution for optimization—actually sidesteps the Gall problem rather than engaging it. It doesn't test whether optimizing based on removal-identified bottlenecks actually destabilizes the broader system, nor does it examine whether the attribution method itself becomes a Goodhart proxy (H-004) under sustained optimization pressure. The work is mechanically competent but theoretically modest.

## Research connections

- **L-005:** Indirectly related—the paper assumes bottleneck identification enables safe incremental restructuring, but doesn't test whether removal-based optimization violates system coherence.
- **H-004 (Goodhart):** Potential vulnerability: if "agent importance" (measured by removal impact) becomes the optimization target, the metric may diverge from actual system robustness under novel conditions.

## Candidate laws or signals

none
