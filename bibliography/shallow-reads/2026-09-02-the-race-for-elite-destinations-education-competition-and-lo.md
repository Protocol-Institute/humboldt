# The Race for Elite Destinations: Education Competition and Low Fertility in Korea

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2608.27980
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical economics paper demonstrating that South Korean families engage in zero-return educational spending (9% of lifetime income to private tutoring) driven by positional competition for elite university placement. The author models this as an assignment externality—when all families increase spending, admission thresholds rise, negating individual gains—and proposes a lottery-based alternative that increases completed fertility by 0.24 children per couple.

## What I took from it

This is a clean empirical instantiation of **L-004 (Goodhart Generalization)**: test scores and admission rankings function as measurable proxies for actual career/life outcomes, and under optimization pressure (family competition for scarce elite slots), the proxy becomes the target. Families optimize test performance knowing it yields zero measured return—a canonical case of metric capture eating the goal.

More interesting for L-008 (Proxy Optimization Under Computable Enforcement): admission decisions are now fully legible and algorithmically addressable (score thresholds, ranking functions). This legibility *enables* the race—families can compute their relative position and calculate marginal returns to tutoring spend with precision. The assignment protocol itself (rank-based admission) creates the optimization surface. The lottery proposal works precisely because it removes the legible optimization target, displacing the game entirely.

The fertility collapse is a second-order effect: the protocol (rank-based assignment) creates a coordination trap where individual rationality (spend to stay competitive) produces collective irrationality (fertility collapse). This echoes **L-010 (Coordination Adoption Nonmonotonicity)** and touches **seed-073 (Correlated Failure Under Proxy Consensus)**: all families converge on the same losing strategy because the proxy is shared and legible.

## Research connections

- **L-004:** Metric capture in education: test scores as proxy for career fitness, optimization under pressure yields zero return but persists.
- **L-008:** Legible admission thresholds enable precise marginal calculation by families; the protocol's computability sustains the race.
- **seed-073:** Correlated failure: all families adopt tutoring because all others do; proxy consensus locks in collective loss.
- **seed-077:** Metric-Induced Preference Ratcheting: admission bar rises monotonically as spending rises; families cannot exit without falling behind.

## Seed

**Seed title:** Legibility-Driven Coordination Traps in Assignment Protocols

**Seed type:** observation

**Seed text:** In assignment protocols where selection is based on a computable, legible metric (test scores, ranking), families or agents can calculate their exact marginal position and cost-to-compete. This legibility enables fine-grained optimization but locks all participants into a symmetric arms race where individual rationality produces collective irrationality (zero-return spending, fertility collapse). The trap persists because exiting is individually catastrophic; it can only be broken by removing legibility itself (e.g., lottery-based assignment). Generalizes: any protocol where the optimization target is publicly computable and the cost of non-participation is individually concentrated tends toward correlated failure at scale.
