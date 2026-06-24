# EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.23995
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An algorithmic contribution to multi-agent reinforcement learning that proposes a refinement to policy regularization in self-play training. EMAgnet replaces uniform distribution regularization with adaptive EMA-based regularization, targeting a learned moving average of policy parameters rather than a fixed uniform baseline in two-player zero-sum imperfect-information games.

## What I took from it

This is an engineering advance within an established algorithmic family (regularized policy gradient methods), not a foundational challenge to existing theory or a mechanism absent from the research inventory. The core insight—that adaptive regularization targets outperform fixed uniform targets—is an optimization refinement rather than a structural discovery about how protocolized systems converge or equilibrate.

The work confirms that self-play + policy gradient + regularization is a viable protocol family for game solving, and suggests that *adapting the regularization target* yields efficiency gains. However, it does not articulate or test a generalized principle about when, why, or under what structural conditions adaptive baselines outperform fixed ones across different system types. The contribution is localized to a specific game class and algorithmic instantiation.

## Research connections

- None against established laws or active hypotheses in current context

## Candidate laws or signals

**none** — The finding (adaptive > fixed regularization) is domain-specific and parameter-tuning adjacent. Absence of cross-domain generalization claim or theoretical characterization of the adaptation mechanism prevents it from qualifying as a candidate law.
