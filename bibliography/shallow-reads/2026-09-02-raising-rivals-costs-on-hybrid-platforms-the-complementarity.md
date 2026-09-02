# Raising Rivals' Costs on Hybrid Platforms: The Complementarity of Fees and Self-Preferencing

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2608.02800
**Date read:** 2026-09-02
**Connected to:** L-001, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A microeconomic modeling paper analyzing hybrid platform monopolization through the interaction of two legible control instruments: transaction fees and algorithmic self-preferencing. The main argument is that these instruments are strategic complements rather than substitutes, so regulatory constraint on either curbs the other—contrary to the regulator's concern that tightening one would intensify the other.

## What I took from it

The paper presents a clean case of strategic boundary concentration (L-014): when platform obligations become precisely computable and legible—fee structures and ranking algorithms—optimizing agents (the platform) compress optimization pressure into the joint space of both instruments rather than sequentially. The complement structure is notable: the platform does not treat fees and self-preferencing as alternative levers but as coupled mechanisms that reinforce each other within the same constraint envelope.

However, the paper does not investigate the deeper protocol ossification mechanism. It treats the instruments as stable choice variables, not as objects that calcify under adoption pressure or that generate downstream coordination costs. The regulatory insight—that single-instrument constraint works—is tactically sound but does not expose whether this complementarity itself hardens over time, or whether the apparent effectiveness of regulation masks latent pressure displacement to unmeasured or newly-legible channels.

## Research connections

- **L-014:** Direct case instantiation—fees and ranking are computable-legible obligations that become joint optimization targets rather than substitutable levers; the boundary concentration is visible in the fee-preferencing coupling.
- **L-001:** The paper does not address ossification, but the stability of the fee-preferencing complementarity under regulatory pressure suggests the instruments may become harder to decouple once deployed as a coupled system.
- **seed-077:** Metric-Induced Preference Ratcheting — the legibility of both fee schedules and ranking signals may induce platform operators to optimize both simultaneously, locking in the complementarity.
- **seed-082:** Additive Intervention in Overloaded Protocols — if the platform absorbs regulatory pressure on fees by intensifying self-preferencing (or vice versa), regulation may preserve root pressure rather than remove it.

## Seed

**Seed title:** Computable-Instrument Complementarity Lock
**Seed type:** observation
**Seed text:** When a protocol system uses multiple precisely-computable control instruments (e.g., fees, ranking weights, allocation rules) to achieve a single strategic objective, these instruments tend to become strategic complements rather than substitutes, even when regulators intend them to be independent levers. The complementarity arises because both instruments are legible to the optimizing agent simultaneously, creating a joint optimization surface. This structure means that regulatory constraint on one instrument does not redistribute pressure toward the other—it curbs both—but also suggests that the instruments themselves may become harder to decouple from operational systems once cemented as a coupled configuration. Generalizes to any multi-instrument protocol (tax-transfer systems, lending-pricing pairs, credential-allocation bundles) where the principal assumes independence but the agent sees simultaneity.
