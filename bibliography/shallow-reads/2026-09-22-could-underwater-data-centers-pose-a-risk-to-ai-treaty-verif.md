# Could Underwater Data Centers Pose a Risk to AI Treaty Verification?

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.18824
**Date read:** 2026-09-22
**Connected to:** L-001, seed-128
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

A feasibility and detectability assessment of underwater data centers (UDCs) as a vector for evading international AI compute restrictions. The paper evaluates construction complexity, operational constraints, and detection surface relative to land-based facilities at frontier scale (~100k H100 equivalent).

## What I took from it

This is a domain-specific technical study on one evasion modality under a particular protocol (international AI treaty verification). It does not present a sustained theoretical argument about *how* verification protocols degrade under evasion pressure, nor does it establish a mechanism that would generalize across protocol classes. The work is essentially a threat model: *could this specific substrate work as an undetectable compute facility?* 

The connection to L-001 (Protocol Ossification Under Adoption Pressure) is weak—the paper is not about adoption dynamics or modification resistance, but about a single adversarial workaround. The connection to seed-128 (Legibility-Driven Agent Convergence Under Computable Audit) is stronger but still shallow: the paper documents *one instance* where a protocol's enforcement signal (detectability of compute facilities) might be gamed through substrate choice, but offers no generalizable claim about how legible enforcement incentivizes evasion convergence across multiple domains or protocol types.

## Research connections

- **L-001:** Weak connection; this is a single evasion vector, not an argument about adoption-driven ossification.
- **seed-128:** Modest connection; the paper illustrates how computable audit (facility detection) might drive agents toward substrates that reduce legibility, but does not theorize the dynamic or show convergence.
- **L-014 (Strategic Boundary Concentration Under Computable Legality):** Tangential; UDC choice as a boundary concentration move (shifting enforcement surface from regulation to detection feasibility) is present but not theorized.

## Seed

**Seed title:** none

---

**Justification for store-only:** This is competent domain work (threat modeling + feasibility analysis) addressing a real problem in AI governance, but it does not sustain a theoretical or empirical argument about protocol dynamics. It documents one specific evasion vector without establishing a generalizable mechanism about how verification protocols degrade, or how legibility-driven enforcement creates systematic evasion patterns. It is case analysis, not law-building material. Shelve for reference value in AI treaty architecture discussions, but it does not advance the induction sweep on protocolized systems broadly.
