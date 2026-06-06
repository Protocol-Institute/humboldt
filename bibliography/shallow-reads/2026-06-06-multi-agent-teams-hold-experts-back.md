# Multi-Agent Teams Hold Experts Back

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2602.01011
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical study of coordination failure in free-form multi-agent LLM systems, examining whether self-organizing teams (without pre-specified roles or workflows) achieve effective collaboration. Draws on organizational psychology to investigate emergence of coordination through interaction rather than design.

## What I took from it

The work addresses a real gap in deployment practice: most multi-agent systems impose coordination structure top-down, but production systems increasingly allow agents to interact freely. The premise is sound for the new nature research agenda — coordination is indeed a protocolized system problem, and studying *emergent* coordination (vs. designed) maps to questions about what structure must be specified vs. what can self-organize.

However, the abstract truncates before revealing findings or mechanisms. The title ("Hold Experts Back") suggests a negative result — that teams *underperform* specialists — but the mechanism is unclear. Is this a bandwidth problem? A consensus cost? An attention fragmentation effect? Without the mechanism, this reads as a domain-specific observation rather than a generalizable law about coordination structures or scalability in multi-agent systems.

The organizational psychology framing is apt but needs to clarify whether insights transfer: org psych studies coordination among humans with bounded rationality, social pressure, and information asymmetry. LLM agents have different failure modes.

## Research connections

- **none (no established laws or active hypotheses yet defined)**

## Candidate laws or signals

- **CL-2602.01011-1:** Free-form multi-agent systems may exhibit a coordination-performance tradeoff where emergent coordination imposes efficiency costs that exceed fixed-protocol overhead, even when fixed protocols are suboptimal for individual agents.
