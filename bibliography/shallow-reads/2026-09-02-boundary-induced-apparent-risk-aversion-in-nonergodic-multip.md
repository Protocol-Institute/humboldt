# Boundary-Induced Apparent Risk Aversion in Nonergodic Multiplicative Growth

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.28230
**Date read:** 2026-09-02
**Connected to:** L-006, seed-080
**Kind:** content
**Escalation:** store-only

## What this is

A mathematical analysis of optimal exposure selection in finite-horizon multiplicative processes with absorbing boundaries (ruin conditions). The paper derives exact lattice solutions showing that agents rationally reduce risk exposure below Kelly-optimal levels when continuation failure carries absorbing costs, parameterized by initial distance to boundary, time horizon, and residual value.

## What I took from it

The paper formalizes a classical insight from portfolio theory — that catastrophic-failure constraints induce conservative behavior — but does so in the language of nonergodic multiplicative systems. The relevance to protocol systems is indirect but real: any protocol system with hard failure states (e.g., cryptographic compromise, consensus collapse, trust depletion) that cannot be recovered from operates under similar boundary conditions. The mechanism here is *not* irrationality or risk aversion per se, but rational adaptation to the loss of ergodicity.

For the research agenda, this provides a mathematical grammar for understanding why safety-critical protocols (L-007) resist adoption of higher-efficiency strategies, and why coordination cost conservation (L-006) may be partly driven by boundary-proximity effects rather than pure coordination physics. The paper does not address protocols directly, so it remains domain-specific economics work. But the regularity — *compression of exposure under absorbing-boundary proximity* — generalizes to any system mixing multiplicative growth with hard failure states.

## Research connections

- **L-006:** Coordination Cost Conservation may partially reflect rational boundary-induced exposure reduction rather than pure coordination substrate constraint.
- **seed-080:** Proxy Collapse Under Upstream Asymmetry — absorbing boundaries create upstream asymmetry in value perception; agents reading a proxy signal (e.g., "distance to ruin") optimize differently than under symmetric growth conditions.

## Seed

**Seed title:** Absorbing-Boundary-Induced Rationality as Protocol Conservatism

**Seed type:** observation

**Seed text:** In protocol systems where failure states are absorbing (cannot be recovered from), agents rationally compress exposure and reduce innovation velocity below theoretical optima. This is not risk aversion or Goodhart pathology, but rational response to loss of ergodicity. The degree of conservatism scales with proximity to absorbing boundary, time-to-horizon, and residual recovery value. In safety-critical protocols (consensus, key management, payment finality), apparent ossification and resistance to upgrade may reflect this mechanism more strongly than adoption-pressure lock-in alone.
