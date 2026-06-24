# Legal Reasoning Is Not Lawyering: Rethinking Legal Benchmarks for Pro Se Access to Justice

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.23716
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Identifies a fundamental measurement gap in how AI systems interact with human institutions—benchmarks measure expert-preprocessed inputs rather than real-world messy inputs—which challenges the validity of access-to-justice claims and suggests a generalizable pattern about protocol-system validity under distribution shift.

## What this is

This is a critical empirical/methodological paper arguing that legal AI benchmarks systematically misrepresent model capability for real-world access-to-justice applications. The core claim: existing benchmarks test performance on *cleaned, expert-preprocessed legal inputs*, not the unstructured, ambiguous, partially-informed inputs that pro se (self-represented) litigants actually produce. This creates a measurement illusion where models appear competent for justice access when they may not be.

## What I took from it

This work identifies a **validity collapse in protocolized systems**: when an AI system is evaluated in an idealized protocol environment (curated benchmarks) but deployed in an adversarial or uncontrolled environment (actual human legal needs), the measured capability becomes non-predictive. The paper suggests that institutional integration cannot be assumed from task performance—there is a hidden lower bound problem.

More broadly, this signals a pattern relevant to all protocol-system research: *benchmarks that measure only expert-mediated or pre-processed versions of a task are systematically misleading about real-world utility*. The gap between upper-bound and lower-bound performance may be a structural feature of how AI systems encounter human institutions, particularly where humans have heterogeneous inputs, knowledge states, and incentives.

This also touches on **legitimacy and capture**: benchmarks drive funding and deployment claims, but if benchmarks don't measure what matters for the stated purpose, the system creates false confidence in institutional adoption.

## Research connections

- **Protocol-system validity under distribution shift:** Real-world inputs from pro se litigants are a severe distribution shift from expert-curated legal text; benchmarks do not measure robustness to this shift.
- **Institutional integration assumptions:** Claims about AI improving access to justice assume seamless human-protocol interaction, but this paper suggests the assumption is empirically ungrounded.
- **Measurement bias in capability claims:** Benchmarks become decoupled from real-world utility when they test only the idealized protocol path, not the messy deployment path.

## Candidate laws or signals

- **CL-2606-1: Benchmark-Reality Gap in Institutional AI:** When an AI system is evaluated on expert-preprocessed or curated inputs and deployed against unmediated human inputs, measured capability becomes a misleading upper bound; real-world utility requires lower-bound testing on uncontrolled inputs from the actual user population.

- **CL-2606-2: Institutional Legitimacy Through Measurement Decoupling:** Benchmark design in high-stakes institutional domains (law, medicine, justice) can systematically inflate capability claims by testing only the path through expert gatekeepers, obscuring failure modes when users bypass or misalign with that path.
