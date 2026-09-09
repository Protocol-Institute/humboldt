# One Vote, Several Parliaments: An Empirical Analysis of the Algorithmic Ambiguity of the Italian Electoral Law on the 2022 General Election Data

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.11676
**Date read:** 2026-09-02
**Connected to:** L-014, seed-026
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary empirical source demonstrating that statutory text rendered computationally legible admits multiple incommensurable implementations, producing divergent electoral outcomes from identical input — direct evidence for L-014 (Strategic Boundary Concentration Under Computable Legality) and introduces a generalizable mechanism: formalization collapse under boundary compression.

## What this is

An empirical implementation study that takes a prior theoretical observation (Crafa's algorithmic analysis showing three interpretations of Italian electoral law Art. 83(1)(h)) and executes all three interpretations on complete 2022 election data, demonstrating that identical votes produce different seat allocations depending on which formal reading of the statute is chosen. This is a domain-specific instantiation of a core problem in protocolized systems: the gap between natural language law and computable implementation.

## What I took from it

This paper provides concrete empirical weight to L-014 (Strategic Boundary Concentration Under Computable Legality) by showing that when legal obligations are rendered machine-readable, the compression of statute into algorithm creates *branching points* where formally admissible readings diverge. Critically, this is not a case of ambiguity *discovered* during implementation — it is ambiguity *created* by the requirement that law become executable code. The three algorithms all follow the statute faithfully; none is "wrong." The problem is that natural language law permits interpretive slack that computable protocols cannot tolerate. 

This also opens a sharp question for L-015 (Interpretive Continuity Decay in Distributed Governance Protocols): the formal record (the law text) remains constant, but its operational meaning is unstable under formalization. The "institutional memory" of how to read Art. 83(1)(h) is not preserved by the statute itself — it lives in interpretation practice, which breaks when the rule must become deterministic code. This is a case where transparency (full algorithmic specification) and legibility (computable unambiguity) are actually in tension with continuity.

## Research connections

- **L-014:** Direct evidence — computable legality creates optimization boundaries (choice of algorithm) that optimizing agents (parties, jurisdictions) can weaponize; the boundary is *inbuilt* into formalization, not external to it.
- **L-015:** Shows the decay mechanism empirically — formal record survives intact but its interpretation bifurcates under computational pressure; institutional continuity breaks even when documentation persists.
- **seed-026:** Confirms the original observation at scale; provides outcome divergence magnitudes.
- **seed-061:** Proof architecture (the algorithm) becomes a governance lock — the choice of which algorithm to implement is now a political/legal act disguised as technical neutrality.
- **seed-062:** Formalization Opacity Collapse — the compression of natural-language statute into deterministic code surfaces previously-invisible interpretive choices as *explicit algorithmic branches*.

## Seed

**Seed title:** Formalization as Boundary Multiplication in Statute-to-Code Translation

**Seed type:** observation

**Seed text:** When natural-language legal text is formalized into executable protocol, the requirement of computational determinism does not *resolve* ambiguity — it *multiplies* it by forcing explicit choices at points where the statute permits interpretive slack. Each formally admissible reading becomes an independent implementation branch, and these branches can produce materially divergent outcomes from identical inputs. The "correct" algorithm is underdetermined by the source text; formalization requires *prior commitment* to an interpretive frame. In distributed or adversarial governance contexts, this turns the formalization choice itself into a strategic control point, where opacity about which interpretation was chosen becomes a form of power. This suggests that computable legality does not eliminate interpretive authority — it *concentrates* and *formalizes* it.
