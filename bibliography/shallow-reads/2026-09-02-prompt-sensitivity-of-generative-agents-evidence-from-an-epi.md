# Prompt Sensitivity of Generative Agents: Evidence from an Epidemic Model

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.26221
**Date read:** 2026-09-02
**Connected to:** L-008, L-011
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study measuring how much generative agent behavior in an epidemic simulation varies with prompt wording and persona assignment. The work treats LLM-based agents as proxies for human behavioral modeling and tests whether small textual changes produce large behavioral divergences.

## What I took from it

The paper demonstrates acute fragility in using generative agents as behavioral proxies: behavior is volatile across semantically minor prompt variations and persona labels. This is relevant to L-008 (Proxy Optimization Under Computable Enforcement) and L-011 (Causal Detachment as Stable Protocol Equilibrium) as evidence that generative agents exhibit *apparent* causal coherence in their outputs while remaining radically dependent on formatting, framing, and naming — which have no ground truth relationship to the underlying model's decision surface.

However, the work is narrowly confirmatory: it shows sensitivity exists in one domain (epidemic modeling) without establishing whether this sensitivity is a property of the proxy itself, the task, the prompt engineering practice, or the evaluation metrics. It does not isolate mechanism or test generalization across protocol contexts. The paper reads as a competent empirical failure report, not a theoretical or mechanistic contribution. It does not challenge or extend the current law inventory; it adds surface-level evidence to a well-known phenomenon (prompt sensitivity) without explaining why the sensitivity persists or what structural features of protocol systems would or would not reproduce it.

## Research connections

- **L-008:** Proxy Optimization Under Computable Enforcement — The paper shows that behavioral proxies (generative agents) exhibit high sensitivity to legible input formatting, but does not trace whether this sensitivity reflects optimization pressure or inherent instability in the proxy architecture itself.
- **L-011:** Causal Detachment as Stable Protocol Equilibrium — The variance across persona names and prompt framings suggests generative agents may maintain operational functionality (producing epidemiologically plausible output) while remaining causally detached from the semantic content agents are supposed to represent.
- **seed-062:** Formalization Opacity Collapse — Automation Legibility — The findings hint that formalizing behavioral instructions (as prompts) may collapse behavioral opacity in ways that create brittle rather than robust proxy performance.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Rationale for store-only:** The paper is a narrow empirical observation (prompt sensitivity exists in LLM agents) within a single domain. It does not present a sustained theoretical argument, does not introduce a novel mechanism absent from the inventory, and does not establish a generalizable law. It is evidence gathering for existing lines of inquiry, not a primary source advancing mechanism or theory. Competent work; insufficient escalation bar.
