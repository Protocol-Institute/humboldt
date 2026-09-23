# When Does Communication Help? Beyond Spectral Descriptions of Collective Intelligence

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.23310
**Date read:** 2026-09-22
**Connected to:** L-010, L-019, seed-138
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source presenting a sustained empirical and theoretical argument that communication effects in distributed systems are fundamentally non-monotonic and spectral-invariant-opaque — directly extends L-010 (Coordination Adoption Nonmonotonicity) and L-019 (Representation-Rationalizability Tradeoff) with a novel mechanism: message orientation as a hidden control variable orthogonal to network topology and information content.

## What this is

This is a distributed inference paper identifying a sharp failure mode in standard aggregate (spectral) descriptions of multi-agent communication gains. The core empirical claim: systems with identical eigenvalue and singular-value spectra can produce opposite-sign accuracy changes (72.6% → 91.2% vs. 65.9%) by varying only message orientation, suggesting that communication harm/benefit cannot be predicted from network structure or information-theoretic measures alone.

## What I took from it

This work directly materializes a mechanism for L-010: coordination signals (here, agent communication in inference networks) exhibit nonmonotonic adoption effects not reducible to network topology or spectral properties. The paper suggests that agents optimizing on legible coordination signals (message content, network structure) while remaining blind to orientation/framing effects will systematically mispredict whether communication improves or degrades collective accuracy. This aligns with L-019's claim that preference aggregation protocols face an inherent tradeoff between representational fidelity and rationalizability — here the tradeoff appears as: *systems describable in spectral terms are blind to orientation-dependent coordination failure modes*.

The practical implication: communication protocols with fixed evidence, network topology, and aggregate metrics can become coordination *traps* where agents rationally adopt communication while systematically degrading outcomes. The nonmonotonicity is not due to information overload or conflicting evidence, but to hidden state-orientation dependencies that spectral analysis (the standard tool for aggregate descriptions) cannot capture.

## Research connections

- **L-010:** Direct extension — communication as a coordination signal exhibits nonmonotonic adoption effects; the mechanism is hidden state orientation, not network topology or information content.
- **L-019:** Related instance — preference aggregation (here, accuracy aggregation from distributed inference) cannot be predicted from spectral/aggregate measures alone; dimensionality of representation matters orthogonally.
- **seed-138:** Intent legibility as coordination target displacement — agents can optimize message content and network structure while remaining blind to message *orientation*, displacing the actual coordination target.
- **seed-128:** Legibility-driven agent convergence — agents adopt communication because it is legible (spectral, network-describable) while the actual coordination failure mode remains opaque.

## Seed

**Seed title:** Orientation Opacity in Spectral-Invariant Coordination Failures

**Seed type:** observation

**Seed text:** In distributed decision systems where agents condition adoption of communication on legible aggregate measures (spectral properties, network structure, information content), systems can become coordination traps where communication adoption is rational but outcome-degrading. The failure mode is orthogonal to legible network properties: identical topologies and spectral descriptions can produce opposite-sign coordination effects depending on message orientation — a dimension invisible to standard aggregate descriptions. This suggests a generalization: *any protocol system that selects for adoption based on a subset of invariant properties while remaining blind to orthogonal state variables can exhibit stable nonmonotonicity where increased adoption worsens outcomes*. The mechanism may generalize beyond distributed inference to any multi-agent protocol where the coordination signal is dimensionally richer than the metric used to evaluate it.
