# Hidden Errors in Big Data: The Case of Property Records

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.28827
**Date read:** 2026-09-02
**Connected to:** L-004, L-007
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical audit of brokered property datasets widely used in academic research and deployed in valuation models, documenting systematic errors that bias inequality measures. The work treats property records as a proxy data system and demonstrates failure modes in that proxy infrastructure.

## What I took from it

This is a concrete instance of L-004 (Goodhart Generalization) and L-007 (Trust Ratchet) in tension: property records serve as measurable proxies for unmeasurable ground truth about property value and ownership, and they accumulate institutional trust through operational age and adoption breadth despite containing hidden systematic errors. The audit reveals that the proxy *itself* becomes the optimization target—models and research train downstream on corrupted signals—and that trust in the data layer persists independent of error detection. This is not a case of protocol ossification preventing *repair* (L-001) but rather a case where the proxy achieves sufficient adoption that downstream users cannot easily switch, even after errors are documented.

The work does not theorize the mechanism or generalize beyond the domain. It is a high-quality case study of proxy failure in an applied system, but does not propose a sustained argument about when or why such failures accumulate in protocol systems more broadly, nor does it challenge the law statements themselves.

## Research connections

- **L-004:** Property datasets as measurable proxies for unmeasurable (ground truth ownership/value); optimization pressure on downstream models locks in proxy use despite error discovery.
- **L-007:** Trust accumulation in property record systems driven by operational age and adoption breadth, not by validation or error correction.
- **seed-073:** Correlated failure under proxy consensus — multiple downstream systems train on the same corrupted proxy, amplifying bias.
- **seed-080:** Proxy collapse under upstream asymmetry — users have no legible way to detect or correct errors at the source, forcing reliance on corrupted signals.

## Seed

**Seed title:** Proxy Durability Through Downstream Lock-In

**Seed type:** observation

**Seed text:** In systems where a measurable proxy achieves widespread downstream adoption (in models, policies, or research), the proxy persists even after documented errors are discovered, because the cost of switching or correcting is distributed across many dependent systems rather than concentrated in the proxy provider. The proxy becomes irreplaceable not because it is accurate, but because the coordination cost of migration is higher than the cost of operating with known bias. This is distinct from L-004 (metric capture) — here the proxy has *already* been captured; what sustains it is adoption stickiness, not continued optimization pressure.
