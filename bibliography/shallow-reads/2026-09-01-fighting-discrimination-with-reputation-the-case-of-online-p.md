# Fighting discrimination with reputation: The case of online platforms

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.05627
**Date read:** 2026-09-01
**Connected to:** L-002, L-007
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An econometric study of earnings discrimination on a French ridesharing platform, showing that minority drivers face an 11.6% revenue penalty that decays as they accumulate reviews. The mechanism is modeled as Bayesian updating: passengers hold pessimistic priors about minority entrants, which are corrected through review signals, with exogenous demand shocks (railway strikes) accelerating review accumulation and thus discrimination closure.

## What I took from it

The paper is a well-executed empirical confirmation that **trust accumulation follows signal velocity, not just time or operational maturity** (L-007 refinement). The trust ratchet does not operate on calendar time alone; it operates on legible evidence density. This is mechanistically sound but domain-specific: it demonstrates the law in the narrow case of reputation systems where signals are abundant, cheap, and Bayesian-rational.

However, the paper does not generalize the mechanism to *when legible signals are absent, manipulated, or fail to update priors*. It also does not address the asymmetry between verification cost (reading reviews) and execution cost (establishing a reputation), which is the core of L-002. The discrimination gap exists precisely *because* verification of minority driver quality is costly relative to priors, not because reputation is slow to accumulate.

## Research connections

- **L-007 (Trust Ratchet):** Confirms that trust in safety-critical protocols (passenger safety) accumulates via legible signals rather than operational age alone. Refines: signal *velocity* (demand shocks accelerating reviews) matters more than duration.
- **L-002 (Hardness Asymmetry):** Implicit: building a new reputation is vastly cheaper than verifying it ex ante. The 11.6% gap reflects the verification cost imposed on new entrants; closure depends on evidence density, not protocol change.
- **seed-033 (Aesthetic Conversion in Early Adoption):** Tangentially related: minority drivers face a non-rational prior that requires evidence to overcome; reviews function as conversion signals in early adoption.

## Seed

**Seed title:** Verification Cost Asymmetry Masks as Discrimination
**Seed type:** observation
**Seed text:** In protocols where verification of quality is expensive relative to prior cost, new entrants from low-trust groups face disproportionate friction not because the protocol is biased but because the *verification burden* falls on them. This friction vanishes only when signal generation becomes dense and cheap enough to overcome priors. The law may generalize: in any legible protocol system, discrimination against novel agents is a side effect of verification cost asymmetry, not bias in the decision rule itself. This implies interventions must reduce verification cost (accelerate signal generation) rather than alter decision rules.
