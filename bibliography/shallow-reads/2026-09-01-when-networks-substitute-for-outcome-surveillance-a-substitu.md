# When Networks Substitute for Outcome Surveillance? A Substitution-Complementarity Framework for Behavioral Signals in Predictive Monitoring

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2510.20025
**Date read:** 2026-09-01
**Connected to:** L-006, seed-020
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study using epidemic forecasting as a test case to ask whether behavioral signal proxies (mobility networks) substitute for or complement outcome-based surveillance in predictive monitoring. The work formalizes this as a substitution-complementarity decomposition problem and applies variance partitioning methods to measure independent predictive contribution.

## What I took from it

The paper is technically competent but operates within a narrow empirical frame: it asks a well-posed question (does network structure predict beyond outcomes?) and answers it for one domain (epidemic spread via mobility). The core finding—that behavioral signals and outcome history carry partially substitutable but also partially complementary information—is domain-specific and does not generalize to the broader question of how coordination costs or protocol burden shift when monitoring transitions from outcome-centric to signal-centric architectures.

The work does *not* address the mechanism by which agents adapt their behavior when they become aware that behavioral signals (not just outcomes) are being monitored, nor does it examine whether the shift toward network-based surveillance creates new forms of gaming, signal distortion, or coordination cost displacement. It measures statistical substitution, not the structural or incentive dynamics that L-006 and seed-020 track. The paper is silent on whether adopting network monitoring changes the total coordination cost in a system or simply moves where that cost appears.

## Research connections

- **L-006:** The paper measures statistical substitutability between signal classes but does not examine whether the total coordination cost is conserved when monitoring shifts from outcome-based to network-behavioral architectures. It is a necessary but insufficient empirical probe.
- **seed-020:** Symptom hierarchy and coordination displacement—the paper does not address whether behavioral signal substitution for outcome surveillance creates new coordination burdens at a different protocol layer (e.g., agents coordinating their mobility patterns rather than their outcomes).

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
