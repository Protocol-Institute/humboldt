# Should I State or Should I Show? Aligning AI with Machine Preferences

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2603.29317
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study comparing two channels for preference learning: stated preferences (natural language instructions/"prompts") versus revealed preferences (behavioral choice data from binary lottery tasks). The work is domain-specific (preference alignment under risk) and tests a methodological question rather than advancing a theoretical mechanism about protocolized systems themselves.

## What I took from it

The paper investigates a practical alignment problem—whether AI agents learn human objectives better from what people *say* they want or what their *choices* reveal. This touches on a relevant tension in artificial systems: the gap between declarative (instructional/symbolic) and behavioral (inferred) preference protocols. 

However, the contribution is primarily empirical and comparative rather than structural. It treats preference learning as a straightforward inference problem and tests channel fidelity without examining why such divergence should occur at all, or what organizational or protocol-level properties generate systematic gaps between stated and revealed behavior. The paper does not theorize the *nature* of preference as a protocolized object, nor does it examine whether stated/revealed divergence is a law-like feature of systems under certain conditions.

## Research connections

- none identified in current context

## Candidate laws or signals

- **CL-2603.29317-1:** Stated and revealed preference channels may have systematically different fidelity for AI preference learning; worth tracking whether this varies by system transparency, instruction granularity, or environment complexity—but only if patterns generalize beyond risk choice domains.
