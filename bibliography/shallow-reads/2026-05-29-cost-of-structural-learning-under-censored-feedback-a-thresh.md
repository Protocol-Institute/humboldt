# Cost of Structural Learning Under Censored Feedback: A Threshold-Bandit Approach

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2605.27076
**Date read:** 2026-05-29
**Connected to:** H-001, L-003
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A multi-agent learning paper formalizing the problem of learning coalition structure when feedback is censored (reward only if threshold met, otherwise no signal). Uses threshold-activated cooperative bandits to analyze centralized vs. decentralized coordination under information asymmetry.

## What I took from it

The paper instantiates a specific failure mode of coordination under incomplete information: agents cannot distinguish whether lack of reward reflects bad strategy, stochastic variance, or insufficient coalition size. This maps directly onto the cost of coordination in H-001, but the paper does not theorize *across* protocol layers—it analyzes the information-theoretic cost within a single coordination problem.

The result (O(log T) centralized vs. worse decentralized regret) confirms that centralization reduces learning cost, which is consistent with L-003's prediction that coordination pressure drives formalization. However, the paper treats this as a technical optimization problem rather than examining whether the formalization itself creates new rigidities or ossification pressures. It does not engage with whether the "centralized solution" becomes harder to modify once deployed.

The work is solid within multi-agent learning but remains in the domain of algorithm design. It does not challenge or extend established laws about protocol systems, nor does it introduce a mechanism absent from the inventory (information censorship and threshold-triggered feedback are well-studied in bandit theory).

## Research connections

- **H-001:** Suggests coordination cost *increases* under information asymmetry and decentralization, but measures cost only within a single protocol instance, not across transitions.
- **L-003:** Consistent with the move from decentralized to centralized coordination under stress, but does not examine whether this formal solution resists later modification.

## Candidate laws or signals

none
