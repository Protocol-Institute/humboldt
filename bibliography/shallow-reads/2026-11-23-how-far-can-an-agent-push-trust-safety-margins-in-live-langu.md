# How Far Can an Agent Push? Trust-Safety Margins in Live Language-Based Economic Games

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.25508
**Date read:** 2026-11-23
**Connected to:** L-007, seed-098
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of strategic agent behavior in a live language-based economic game (GLEE competition), testing how far policy modifications can push acceptance thresholds before detection or rejection occurs. The work deploys a protected agent (Milton) with gated policy changes alongside instrument agents running randomized trials, measuring adoption margins in negotiation and bargaining tasks.

## What I took from it

This is a narrow empirical probe into one instantiation of **trust accumulation under live deployment pressure** (L-007), but it does not generalize to the law itself. The paper measures *tactical* acceptance thresholds in a bounded, game-theoretic setting with explicit human evaluation or automated acceptors — not the institutional, long-term trust ratchet that L-007 targets. The gating mechanisms and rollback-guard architecture are themselves artifacts of *distrust*, not evidence of how trust accumulates. The work treats trust as a legible acceptability threshold to be tested incrementally, rather than as an operational-age-driven institutional phenomenon.

The setup is tight enough to generate local regularities (learned pricing yields ~7pp improvement), but these reflect optimization within a narrow competition frame, not behavior under the conditions L-007 specifies (operational stability, age effects, safety-critical deployment maturity). The language-based negotiation setting introduces human or agent-based judgment calls that are not modeled here — no account of how narrative, interpretation, or institutional memory shape acceptance over time.

## Research connections

- **L-007 (Trust Ratchet in Safety-Critical Protocols):** The paper measures threshold acceptance in a live competitive setting, but does not distinguish between tactical gaming of evaluation and genuine institutional trust accumulation over operational age. No temporal depth to establish ratchet behavior.
- **seed-098 (threshold legibility and sabotage detection):** The gating and rollback architecture presumes sabotage detection is feasible; the paper does not examine when detection fails or how strategic agents evade legible signals.
- **L-004 (Goodhart Generalization):** The learned pricing proxy may be optimizing for competition-specific acceptability rather than true bargaining efficiency; no examination of whether gains transfer or collapse under distribution shift.
- **seed-543 (Trust Ratchet Substrate Divergence):** Trust in this setting is measured against game outcomes (legible), not operational stability or institutional legitimacy (not measured).

## Seed

**Seed title:** Tactical Acceptability Thresholds as Distinct from Institutional Trust Ratchets

**Seed type:** observation

**Seed text:** In bounded, explicitly-evaluated game-theoretic settings, strategic agents can discover and incrementally push acceptability thresholds through controlled policy variation without triggering rejection. This *tactical threshold discovery* is mechanically different from institutional trust accumulation under operational age: the former requires legible evaluation events (round-by-round judgment); the latter depends on survival under opacity and interpretive continuity over time. The confusion between these two regimes may explain why competition-based safety tests (narrow domains, explicit evaluation, rapid feedback) often do not predict real-world deployment trust dynamics (interpretive drift, infrequent crises, long memory windows).
