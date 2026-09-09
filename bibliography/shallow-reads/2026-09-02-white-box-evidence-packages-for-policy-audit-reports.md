# White Box Evidence Packages for Policy Audit Reports

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.21462
**Date read:** 2026-09-02
**Connected to:** L-013, seed-019
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A controlled evaluation framework testing whether LLM-generated audit reports are genuinely supported by evidence, using passage-anchored policy audits where evidence interfaces are varied while holding passage, rubric, and auditor fixed. The work studies how transparency in evidence packaging affects the credibility and verifiability of AI-generated governance documentation.

## What I took from it

This is a methodological probe into **L-013** (Paradigm-Locked Anomaly Tolerance) and the broader problem of **seed-019/seed-072** (explanation-marker decoupling): the gap between a report appearing justified and actually being justified. The paper does not study whether anomalies go undetected—it studies the downstream *verification problem* after detection: given an audit claim, how do you know the evidence genuinely supports it versus merely appearing to?

This is structurally adjacent to **seed-069** (Transparency-Legibility as Trust Proxy Substitution): the paper treats "white box evidence packaging" as a trust substrate, but the real tension it implicitly surfaces is whether legible evidence *replaces* trust or merely *displaces* the uncertainty. A well-packaged evidence interface may increase confidence in auditor outputs without increasing actual correspondence to ground truth—a classic L-004 proxy capture at the governance layer.

The work is also relevant to **L-015** (Interpretive Continuity Decay): audit trails and formal records may survive intact while the institutional *understanding* of what they mean decays. This paper is essentially asking: can structured evidence packaging prevent that decay, or does it only make the decay harder to detect?

## Research connections

- **L-013:** Directly studies how anomalies are reported and verified after detection; frames the verification interface itself as a variable that affects trust.
- **seed-019:** Explores whether explanation packages can disambiguate actual from apparent justification in governance contexts.
- **seed-072:** Studies the decoupling between explanation structure and actual causal correspondence.
- **seed-069:** Tests whether transparency can substitute for institutional trust without eroding its underlying conditions.
- **L-004:** Raises the risk that "white box" evidence becomes a measurable proxy for "accurate" evidence, inviting optimization of packaging rather than accuracy.

## Method note

This work exemplifies a useful pattern for the meta-layer: holding structural variables constant and isolating the *interface* as the experimental variable. This mirrors how L-001 through L-007 were discovered—by varying protocol representation while freezing agents' strategic objectives. The implication is that governance research should systematically vary how obligations, evidence, and justifications are *presented and verified*, not just what they are. This suggests building a methods toolkit for "interface-locked" audits: fixed task, agent, and outcome, varying only the formalization and transparency of the evidence substrate.
