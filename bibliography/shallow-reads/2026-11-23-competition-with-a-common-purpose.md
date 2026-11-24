# Competition with a Common Purpose

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2610.08455
**Date read:** 2026-11-23
**Connected to:** L-006, L-010, seed-325
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An economic analysis of NGO fundraising competition under partial mission alignment. The paper decomposes fundraising effects into aggregate lift (expanding total funding to a cause) versus shift (redirecting between organizations), examining how incomplete alignment between organizations' purposes creates divergence between individual and collective incentives.

## What I took from it

The paper operationalizes a classic coordination problem—shared goals but competing actors—through the lift/shift decomposition. This maps cleanly onto L-006 (Coordination Cost Conservation), suggesting that when multiple agents compete for a fixed pool while nominally coordinated on outcome, the coordination cost doesn't disappear; it gets displaced into either wasteful duplication (lift attempts that fail) or strategic repositioning (shift attempts). The incompleteness of alignment acts as a legibility escape hatch: agents can claim coordination on the goal while optimizing locally on market share.

This also touches L-010 (Coordination Adoption Nonmonotonicity), but in reverse: shared purpose doesn't automatically create smooth adoption of coordinated fundraising. Instead, the wedge between marginal mission return and marginal organizational return creates a discontinuity. Organizations adopt competitive rather than cooperative fundraising regimes precisely because their metrics diverge from the shared goal. The formalization of "social outcome" as measurable proxy doesn't resolve the coordination problem; it externalizes it to the funding allocation layer.

## Research connections

- **L-006:** Coordination cost is not eliminated by declaring shared purpose; it migrates from decision-making to market-layer inefficiency (lift/shift waste).
- **L-010:** Incomplete alignment creates adoption nonmonotonicity: more precise goal specification does not increase coordination adoption; it increases strategic opacity about individual incentive divergence.
- **L-004 (Goodhart):** The "social outcome" proxy is shared, but each organization optimizes against its own measurement of contribution to it, creating divergent strategies.
- **seed-515 (Computable Belief as Collusion Surface):** Shared public commitment to a cause becomes a surface for strategic behavior differentiation underneath.

## Seed

**Seed title:** Alignment Transparency as Coordination Illegibility Displacement
**Seed type:** observation
**Seed text:** When multiple agents are explicitly aligned on a shared measurable outcome but remain in competitive market positions, transparent declaration of that alignment does not reduce coordination cost—it displaces it into the gap between aggregate and individual optimization. The agents become *more* strategically differentiated, not less, because they can now claim coordination on the goal while optimizing local metrics. This suggests that formal alignment statements in protocol systems may function as coordination *obscuration* channels: they create plausible deniability for divergent local behavior. The pattern should generalize to any multi-agent protocol where goal alignment is declared at the system level but incentive alignment remains incomplete at the agent level.
