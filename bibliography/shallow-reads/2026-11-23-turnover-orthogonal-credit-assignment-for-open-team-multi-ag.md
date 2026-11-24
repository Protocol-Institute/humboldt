# Turnover-Orthogonal Credit Assignment for Open-Team Multi-Agent Reinforcement Learning

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.02847
**Date read:** 2026-11-23
**Connected to:** L-006, L-009
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper in multi-agent RL proposing TOCA, a credit assignment method that decouples agent contribution from team composition change in open-team settings where agents join/leave during episodes. The work is domain-specific: it addresses a legibility problem (separating signal from noise in a reward attribution task) rather than making a claim about protocol dynamics or coordination structure.

## What I took from it

The paper identifies a real coordination cost in open-team systems: when you can't distinguish agent action value from turnover effects, surviving agents face reward noise that breaks learning. TOCA attempts to orthogonalize these by factoring out the population-change component. 

However, this is engineering-level problem-solving, not a law or mechanism discovery. It doesn't argue that coordination costs are *conserved*, that they're *displaced*, or that turnover creates *nonmonotonic adoption dynamics*. It assumes the right solution is better signal isolation. It does not examine whether agents under turnover-noise actually use that signal, whether credit legibility itself triggers defection or strategic behavior, or whether the cost of computing TOCA-style separation is itself a form of coordination tax that gets paid elsewhere (L-006 territory). The paper does not test whether agents receiving cleaner credit signals behave differently in ways that break the team, nor does it model multi-round protocol evolution under turnover — it optimizes within a single regime.

## Research connections

- **L-006 (Coordination Cost Conservation):** The paper addresses turnover-induced noise in credit signals but does not test whether clarifying agent contribution shifts the coordination burden to other layers (e.g., strategic defection, population churn acceleration, or coalitional blocking).
- **L-009 (Catastrophic Risk Cancellation):** No connection — the paper does not study racing or concentrated-prize scenarios.
- **seed-553 (Coordination Infrastructure Formalization as Legibility-Without-Cost-Reduction):** Potential surface connection — TOCA is itself a formalization (orthogonal decomposition) that increases legibility; worth tracking whether it reduces or merely displaces coordination cost.
- none

## Seed

**Seed title:** Legibility Tax Under Credit Orthogonalization
**Seed type:** question
**Seed text:** When credit assignment protocols become more legible through explicit factorization (e.g., separating agent contribution from exogenous population dynamics), do agents receiving clearer signals exhibit increased strategic behavior in response — such as coalitional defection, timing-sensitive exit, or contribution withholding — that recovers or exceeds the original noise cost? In open-team systems, does better credit isolation create new coordination problems at the boundary between agent choice and team membership?
