# Compensation Design

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.14438
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper on payment rule design for decentralized contribution systems under budget constraints. The work proves existence and efficiency bounds for cost-oblivious marginal-contribution payment mechanisms in settings where agents have private costs and opt-in decisions.

## What I took from it

This is competent mechanism design work, but operates within settled game-theoretic territory. The marginal-contribution payment rule is a known construct (Shapley-adjacent), and the result—that anonymous, cost-oblivious pricing stabilizes equilibrium with PoA ≤ 2—is a technical contribution to the mechanism design literature rather than evidence for or against the law candidates in our funnel.

The paper does not expose a mechanism genuinely absent from the protocol research inventory. It does not directly challenge or substantially extend L-004 (Goodhart Generalization) or L-008 (Proxy Optimization Under Computable Enforcement): the payment rule *is* a measurable proxy (marginal contribution), but the paper assumes agents are rational and information-symmetric about costs, and does not track what happens when the proxy itself becomes the optimization target under sustained pressure—i.e., when agents learn to game contribution *measurement* rather than contribution *quality*. The absence of strategic misreporting in the model is the core limitation for our purposes.

This reads as a tool/design paper, not a primary source on the laws governing how protocol-mediated incentive systems degrade under real conditions.

## Research connections

- **L-004:** The payment rule is a measurable proxy for contribution quality, but the paper does not model the optimization pressure that would activate Goodhart capture.
- **L-008:** The mechanism computes payment from legible contributions, but assumes agents do not learn to game the legibility itself.

## Seed

**Seed title:** none
