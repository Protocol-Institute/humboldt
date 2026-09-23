# Examining Community-Requested Fact-Checking: Request Alerts Are Associated with Greater Diversity and Visibility of Community Notes

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2604.17042
**Date read:** 2026-09-22
**Connected to:** L-013, seed-143
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Quantitative observational study of X's Community Notes system, examining how algorithmic alerts (triggered by user requests for fact-checks) correlate with the diversity and visibility of resulting notes. Non-causal comparison of note properties on posts with vs. without request alerts.

## What I took from it

The paper documents a legibility effect: making verification demand *visible* (via alert interface cue) correlates with greater heterogeneity and prominence of the resulting scrutiny. This sits at the intersection of L-013 (paradigm-locked anomaly tolerance) and seed-143 (forensic legibility mandate disconnect), but the mechanism here is inverse — legibility *increases* attention rather than masking it.

The work is empirically clean but mechanistically shallow. It shows correlation between signal visibility and contributor response diversity, but does not isolate whether the alert cues attention, legitimizes effort, creates a coordination surface, or simply selects for posts where many users already suspected problems. The paper is descriptive of platform behavior, not theoretical about why legibility reshapes verification distribution. It does not generalize beyond the specific design choice (request alerts) or test whether the pattern holds across other verification protocols.

## Research connections

- **L-013:** Documents one case where formalized legibility (the alert) *breaks* paradigm lock by making anomalies visible to a distributed contributor pool, rather than tolerating them invisibly. But this is a boundary case, not a violation of L-013.
- **seed-143:** The alert is a forensic legibility signal with no enforcement threshold — it marks a post as having verification *demand* but creates no obligation or outcome guarantee. Legibility without enforcement boundary.
- **seed-128:** Tangential: the alert may function as a legibility-driven coordination surface that concentrates contributor attention on specific posts.

## Seed

**Seed title:** Legibility-Driven Verification Asymmetry in Crowdsourced Protocols

**Seed type:** observation

**Seed text:** In crowdsourced verification systems, making aggregated *demand* for scrutiny legible (via alert signals) reshapes the diversity and visibility of verification outputs, independently of the underlying prevalence or severity of false claims. The alert functions as a coordination cue rather than evidence. This suggests that in distributed verification protocols, the distribution of scrutiny is governed not by ground truth or risk, but by legibility of collective attention — a form of second-order coordination where contributors optimize for visible demand signals rather than problem severity. The pattern may generalize to any audit or verification system where contributor effort is discretionary and cues to collective interest are legible.
