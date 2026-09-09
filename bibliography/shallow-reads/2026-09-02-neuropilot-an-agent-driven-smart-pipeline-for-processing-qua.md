# NeuroPilot: An Agent-Driven Smart Pipeline for Processing, Quality Control, and Managing Neuroimages

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.07541
**Date read:** 2026-09-02
**Connected to:** L-001, L-005
**Kind:** tool paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems engineering paper describing NeuroPilot, an LLM-agent orchestration framework for automating neuroimaging pipeline workflows (standardization, preprocessing, quality control). The work treats pipeline coordination as a skill-decomposition problem solvable by multi-agent prompting rather than as a problem of protocol redesign or governance.

## What I took from it

The paper is squarely a *tool paper*, not a theoretical or empirical investigation of protocol dynamics. It demonstrates the *symptom* of what L-001 and L-005 predict — neuroimaging pipelines are ossified, require project-specific scripting, resist restructuring — but it does not examine the mechanisms that cause this ossification or explain why agent-driven re-orchestration might or might not escape those pressures.

The approach (decomposing human expertise into LLM-callable skills, then invoking them in sequence) is a *workaround*, not a challenge to the underlying regularities. In fact, it may instantiate a new version of L-005: as the agent layer becomes more complex and interdependent, the system may resist further restructuring just as the original pipeline did. The paper provides no evidence about whether this delegation pattern generalizes to other safety-critical or coordination-heavy domains, nor does it isolate what makes neuroimaging pipelines specifically hard to standardize.

## Research connections

- **L-001:** The paper documents the problem (ossified, project-specific pipelines) but offers no mechanistic account of why adoption pressure locks protocols.
- **L-005:** NeuroPilot is a functional workaround to resistance-to-restructuring, not a test of the law itself.
- **L-012:** Possible weak signal: the delegation of QC decision-making to agent-invoked skills creates an intermediate legibility layer that could displace optimization pressure, but the paper does not investigate this.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
