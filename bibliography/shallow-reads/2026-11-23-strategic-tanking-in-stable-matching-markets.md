# Strategic Tanking in Stable Matching Markets

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.42105
**Date read:** 2026-11-23
**Connected to:** L-004, L-010, seed-325
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of "strategic tanking" — deliberate self-degradation in matching markets where agents misrepresent their own attractiveness rather than their preferences to improve assignment outcomes. The work formalizes a manipulation strategy orthogonal to classical preference misreport and establishes connections to preference manipulation literature.

## What I took from it

The paper identifies a legible optimization surface (one's rank in others' preference orderings) that is decoupled from actual preference truthfulness, creating a manipulation channel that classical stable matching theory does not fully address. This is relevant to L-004 (Goodhart Generalization) insofar as the protocol's metric — an agent's attractiveness — becomes subject to gaming when assignment depends on relative standing. It also touches L-010 (Coordination Adoption Nonmonotonicity) in that an agent's incentive to tank depends nonmonotonically on beliefs about others' behavior: tanking is rational only if enough others do not tank, but widespread tanking collapses the signal.

However, the work is primarily a local game-theoretic result. It characterizes equilibria in a specific protocol under strategic misrepresentation of a secondary signal (attractiveness), not a law governing how protocols degrade under optimization pressure more broadly. The mechanism (preference aggregation capture via self-handicapping) is narrow and domain-bound. The paper does not engage with how tanking behavior might persist, scale, or displace coordination in real matching systems, nor does it challenge or extend the theoretical scaffolding of the law inventory.

## Research connections

- **L-004:** Tanking exploits the measurable proxy (agent attractiveness) used by the matching protocol; under sufficient strategic pressure, this proxy loses fidelity to true fit, confirming the generalization. However, the paper does not articulate this as a generalizable mechanism.
- **L-010:** Tanking incentives are nonmonotonic in adoption: rational only below a threshold of tanking prevalence. The paper models this but does not connect it to broader coordination dynamics.
- **seed-325:** Directly relevant (preference aggregation capture), but the paper does not generalize the observation beyond matching markets.
- none

## Seed

**Seed title:** Self-Handicapping as Legible Signal Exploitation in Ranked Aggregation

**Seed type:** observation

**Seed text:** In protocols where agent ranking or attractiveness is computed from legible signals (outputs, attributes, historical performance), agents can degrade those signals selectively to manipulate aggregate rank assignment without misreporting their own preferences. This exploitation arises because the protocol treats the signal as a legible proxy for fit or value, decoupled from the agent's actual utility. As adoption of this strategy increases, the signal loses fidelity; at equilibrium, ranking becomes noise. This suggests a general mechanism: any ranking system with a legible, agent-controllable signal will attract self-handicapping under sufficient competitive pressure, displacing the protocol's intended coordination function into an arms race in signal spoofing.
