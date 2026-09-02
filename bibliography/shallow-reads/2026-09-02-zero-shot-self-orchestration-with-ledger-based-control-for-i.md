# Zero-Shot Self-Orchestration with Ledger-Based Control for Improved LLM Coding Performance

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.26480
**Date read:** 2026-09-02
**Connected to:** L-005, L-011
**Kind:** empirical/benchmark
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A controlled empirical study of multi-agent LLM orchestration via shared filesystem "ledger" scaffolding, isolating the effect of coordination architecture from token budget and prompt confounds. The work compares manager-worker delegation against single-model baselines across nine LLM variants on coding tasks, with zero training and zero per-benchmark tuning.

## What I took from it

The paper is a competent ablation study addressing a real methodological problem in multi-agent LLM claims: most comparisons conflate coordination gains with resource increases. By fixing token budget and varying only the orchestration topology (single agent vs. manager-worker with shared ledger), it attempts to isolate the structural effect. However, the work remains a **benchmark comparison** rather than a theoretical or empirical investigation of *why* orchestration succeeds or fails, what makes coordination protocols stable, or how they degrade under pressure. It does not challenge or extend any of the current law inventory; it does not expose a mechanism absent from the research inventory. The ledger-based coordination is instrumentally useful but not law-shaped — it does not reveal a regularity about protocol systems that would generalize beyond LLM coding tasks.

## Research connections

- **L-005:** The shared ledger is a working coordination system that cannot easily be replaced; the paper documents its effectiveness empirically but does not examine the conditions under which it might resist restructuring or the mechanisms of that resistance.
- **L-011:** The manager-worker architecture with ledger-based state creates operationally functional configurations where causality between decisions and outcomes is mediated through a formal shared record; the paper does not investigate whether this creates causal detachment or under what conditions agents optimize for ledger legibility rather than task completion.
- **seed-070:** The ledger itself becomes an obligate coordination substrate; the paper shows this works but does not probe whether this creates infrastructure constraints or lock-in.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
