# Fairness and Incentive Compatibility via Percentage Fees

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2402.14173
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mechanism design paper proposing a modification to the standard incentive-compatibility framework by introducing percentage-fee charging. The authors argue that traditional IC mechanisms cannot maximize Nash Social Welfare even approximately, and propose shifting from fixed-fee or utility-based mechanisms to ones where agents pay a percentage of their realized value, showing exact NSW maximization is achievable under this model.

## What I took from it

This is a narrow technical fix to a specific equilibrium problem in mechanism design — it relocates the optimization target (from utility preservation to percentage extraction) rather than addressing a deeper law about proxy capture or formalization pressure. The work does not investigate *why* the percentage model works, what happens when agents can compress or misreport value, or how this model behaves under adoption pressure or agent coordination. It does not generalize to broader protocol systems; it is a local solution to incentive compatibility in auction-like settings.

The paper confirms that formal incentive structures are vulnerable to incompleteness (traditional IC cannot guarantee NSW), but does not present evidence that the percentage-fee fix is itself robust to gaming, misreporting, or the secondary effects of formalization. This is competent technical work within game theory, but it treats fairness and incentive alignment as separable and solvable via a cleaner fee structure — a premise that sits *within* rather than investigates the laws of protocolized systems.

## Research connections

- **L-004 [Goodhart Generalization]:** The paper implicitly accepts that any proxy for welfare (fixed fees, utility-based IC) fails under optimization. The percentage fee is offered as a better proxy, but the paper does not investigate whether percentage fees themselves become targets for obfuscation, value misreporting, or coalition-based circumvention under sustained optimization pressure.

- **L-008 [Proxy Optimization Under Computable Enforcement]:** The percentage fee is a precisely computable enforcement signal. The paper does not explore what happens when agents can formalize or game the value computation itself — e.g., by coordinate misreporting or by structuring transactions to make their "realized value" legally or technically ambiguous.

- none (no direct bearing on formalization ratchet, trust ratchet, coordination cost conservation, or protocol ossification)

## Seed

**Seed title:** Fee-Structure Proxy Stability Under Value Legibility
**Seed type:** question
**Seed text:** Percentage-fee mechanisms make payoff extraction a linear function of realized value, which is more transparent than fixed or utility-contingent fees. But they also make the definition and computation of "value" a critical legibility chokepoint. When value itself becomes a computable quantity subject to formal audit, does the optimization pressure shift from outcome-gaming to value-reporting and value-definition gaming? And does the stability of percentage-fee IC depend on value being unmeasurable or ambiguous enough that agents cannot coordinate false value claims?
