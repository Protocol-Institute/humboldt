# Electricity demand has not become more price-responsive despite ninety years of technological change

**Source:** arXiv:2607.21285v1
**Date read:** 2026-09-02
**Connected to:** L-004, L-013
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A meta-analysis of 4,720 own-price elasticity estimates across 90 years of electricity demand studies (1934–2024), ranked by identification quality from naive OLS to RCTs. The core finding: price responsiveness has remained flat or declined despite massive technological enablement (smart meters, automation, storage, real-time pricing). Better-identified studies find smaller effects than naive ones, suggesting publication bias masks a weaker true signal.

## What I took from it

This is a **sustained empirical challenge to a foundational assumption in protocol design**: that legibility + technology → behavior change. The energy pricing protocol assumes price signals will drive demand reduction; 90 years of data suggest they do not, independent of metering precision or automation capability. This directly engages L-004 (Goodhart Generalization) and L-013 (Paradigm-Locked Anomaly Tolerance), but in a specific way: the anomaly here is *not accumulating dysfunction* but rather *persistent null effect despite metric legibility improvement*.

The result hints at a deeper regularity: **making a coordination goal measurable and automatable does not increase agent responsiveness to it if the goal is orthogonal to agent incentive structure or identity**. Electricity consumers do not become price-sensitive because they gained access to price signals; they were never incentivized to be. The protocol assumed the problem was *information*; it was *motivation*. Technological legibility cannot solve misalignment at the preference level.

This also suggests L-013 (Paradigm-Locked Anomaly Tolerance) may apply not just to *safety-critical* systems but to *economic coordination protocols*: planners held the assumption that tech would increase elasticity for 90 years despite mounting counter-evidence, reshaping research framing and policy design around the assumption rather than abandoning it.

## Research connections

- **L-004 (Goodhart Generalization):** The price elasticity proxy is optimized under policy (real-time pricing pilots, smart meter rollouts) yet the underlying goal (demand reduction) does not follow. Suggests the proxy was misidentified—it measures information access, not preference alignment.

- **L-013 (Paradigm-Locked Anomaly Tolerance):** Decarbonization planning has embedded the assumption for decades; the persistence of flat elasticity across 90 years and multiple technological inflection points suggests the research establishment tolerates the anomaly by reframing rather than revising the model.

- **seed-068 (Unmeasurability as Anomaly Insulation):** The inverse case: *measureability* does not force behavior change if the unmeasurable thing (willingness to shift consumption) is the actual constraint.

- **seed-077 (Metric-Induced Preference Ratcheting):** Policy and pricing structures may have ratcheted upward in sophistication without shifting underlying demand preferences—a one-directional loop.

## Seed

**Seed title:** Legibility-Orthogonal Goal Resistance

**Seed type:** observation

**Seed text:** In coordination protocols where the goal is measurable and enforcement/feedback is automatable, but agent incentives are orthogonal to the goal, technological improvement in legibility and automation does not increase compliance or responsiveness. The electricity demand case suggests that 90 years of metering and pricing signal precision failed to increase price elasticity because consumer behavior is not primarily driven by price signals; the bottleneck is preference/motivation, not information. This may generalize: **making a protocol obligation computable and legible does not overcome misalignment between agent incentive structure and stated protocol goal.** Escalation occurs when protocol designers mistake information asymmetry for the problem.
