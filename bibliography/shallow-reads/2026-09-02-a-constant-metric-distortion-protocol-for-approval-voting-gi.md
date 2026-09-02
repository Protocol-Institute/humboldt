# A Constant Metric Distortion Protocol for Approval Voting Given Plurality Polls

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.28340
**Date read:** 2026-09-02
**Connected to:** L-006, L-004
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper on voting protocol design: given only plurality poll data (first-choice rankings), the authors develop an approval voting mechanism that bounds distortion between the outcome and a ground-truth social preference order. This is a mechanism design response to incomplete preference information.

## What I took from it

The paper is a competent but narrow contribution to social choice theory. It does not engage with how voting protocols evolve under adoption pressure, how metric proxies (plurality polls as a stand-in for full preference data) shape agent behavior over time, or how the incompleteness of the input signal cascades into equilibrium distortion.

The work is *downstream* of the relevant dynamics: it takes the plurality poll as exogenous input and optimizes a protocol given that constraint. It does not ask why plurality polls are the available legible signal, why agents converge on reporting first preferences only, or what happens when agents strategically shape what plurality polls reveal. Those are the questions that touch L-004 and L-006.

## Research connections

- **L-004 (Goodhart Generalization):** The paper implicitly assumes plurality polls are faithful proxies for preference; it does not examine what happens when voters strategically report first-choice rankings to influence the polling signal itself.
- **L-006 (Coordination Cost Conservation):** The paper shifts coordination burden from explicit approval-set specification to implicit inference from plurality data; this is a real cost displacement, but the paper treats it as solved rather than conserved.
- **seed-073 (Correlated Failure Under Proxy Consensus):** If all agents converge on using plurality polls as coordination device, systematic failures in preference aggregation become correlated rather than distributed.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**STORAGE NOTE:** Competent mechanism design within well-understood social choice landscape. Does not investigate protocol-system dynamics, agent incentives to shape legible signals, or long-horizon equilibrium behavior. File as reference for approval voting mechanics; no generative theoretical friction with the new nature agenda.
