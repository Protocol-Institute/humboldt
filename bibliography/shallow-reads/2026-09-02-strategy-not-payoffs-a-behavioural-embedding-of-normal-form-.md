# Strategy, Not Payoffs: A Behavioural Embedding of Normal-Form Games

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.27536
**Date read:** 2026-09-02
**Connected to:** L-008, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of transfer learning in LLM game-playing, examining how fine-tuning on one game class affects strategic reasoning in another. The work uses game embeddings to predict positive and negative transfer effects across normal-form games.

## What I took from it

The paper is a competent benchmark-style investigation of a genuine phenomenon: strategic capability transfer is asymmetric and game-structure-dependent. This is relevant to L-008 (Proxy Optimization Under Computable Enforcement) in a narrow sense — the study shows that agents optimize differently depending on which game protocol they've been trained on, suggesting that computable game structure acts as an attractor for learned heuristics that don't transfer cleanly.

However, the work does not sustain a theoretical argument about *why* this happens or *when* it should be expected to happen across arbitrary protocol classes. It documents transfer asymmetry within a fixed domain (normal-form games with explicit payoff matrices) rather than demonstrating a mechanism that would generalize to real protocol ecosystems or safety-critical systems. The "strategy not payoffs" framing is intriguing but underdeveloped — it gestures at a separation between formal game structure and agent reasoning, but does not establish what the law-shaped regularity is or under what conditions it holds beyond games.

The connection to L-010 (Coordination Adoption Nonmonotonicity) is tangential: the paper does not address coordination signals or multi-agent adoption cascades.

## Research connections

- **L-008:** Suggests that agents optimize toward legible game structure rather than underlying payoff goals; transfer failure may reflect protocol-specific optimization locks rather than true strategic understanding. But scope is too narrow (single-domain benchmark) to confirm the generalized law.

- **seed-077 (Metric-Induced Preference Ratcheting in Adaptive Systems):** Transfer asymmetry could reflect ratcheting of strategic heuristics to game-class-specific metrics (win rate, equilibrium distance, etc.) that become irreversible or costly to unlearn.

- none otherwise.

## Seed

**Seed title:** Protocol-Locked Strategic Embedding

**Seed type:** observation

**Seed text:** Agents trained on explicit formal protocols (here: normal-form games) develop task-specific strategic embeddings that transfer unpredictably to structurally similar but formally distinct protocols, suggesting that learned representations couple tightly to computable legible structure rather than to the underlying problem invariants. If this pattern holds across protocol families (not just games), it would imply that computable enforcement and formal specification, while enabling optimization, also create local optimization traps that resist transfer. The regularity: *transfer asymmetry increases as a function of formal legibility and decreases with domain abstraction*.
