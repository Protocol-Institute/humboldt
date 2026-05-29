# Long Live the Librarian! A Persistent Search Sub-Agent for Energy-Efficient Multi-Agent Software Engineering Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2605.27787
**Date read:** 2026-05-29
**Connected to:** L-001, H-001
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical optimization paper demonstrating that energy costs in multi-agent software engineering systems concentrate in redundant output token generation across agents, rather than distributed across the system. The work proposes a "persistent librarian" sub-agent to cache and reuse outputs, reducing per-episode computational waste.

## What I took from it

This is a tool/optimization paper, not a theoretical one. It identifies a *symptom* of coordination inefficiency—redundant communication across agents—but does not analyze the *protocol structure* that produces this redundancy. The energy asymmetry (30–1000× output vs. input token cost) is a physical property of transformer inference, not a governance or coordination law.

The paper supports H-001 (coordination cost conservation) weakly: if caching reduces output redundancy without reducing coordination quality, it suggests costs *shift* rather than *disappear*—the librarian agent itself becomes a new coordination bottleneck. But the paper does not investigate what happens to protocol robustness, latency, or failure modes under this architectural change, so the hypothesis remains untested here.

No challenge to L-001 (ossification), L-003 (formalization ratchet), or L-004/L-005 (Goodhart/Gall generalizations).

## Research connections

- **H-001:** Suggests coordination costs may concentrate in communication layers under certain architectures, but does not measure whether total coordination complexity is conserved or merely relocated to caching infrastructure.
- **L-001:** Not directly engaged; no discussion of how the "librarian" protocol might itself ossify under adoption.

## Candidate laws or signals

none
