# A latent dimension of Condorcet's jury theorem for multiple AI advisers

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.14438
**Date read:** 2026-09-22
**Connected to:** L-010, seed-017
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A theoretical paper applying binomial analysis to Condorcet's jury theorem under conditions of multiple independent AI advisers. The core argument is that while majority reliability increases with adviser count (classical theorem prediction), visible disagreement among advisers becomes nearly inevitable and approaches certainty at a different rate — creating a divergence between the mathematical reliability curve and the user's observational experience of dissent.

## What I took from it

This is a narrow but sharp observation about a coordination failure between what a protocol predicts (reliability gain) and what it reveals (escalating disagreement). The paper identifies that adding "competent independent" advisers increases both reliability *and* visible conflict — but these curves diverge. The user observing disagreement sees mounting evidence of uncertainty even as the formal majority decision becomes more reliable.

This touches L-010 (Coordination Adoption Nonmonotonicity) at the margin: adoption signals (here, adviser plurality) are meant to increase confidence, but the visible output (disagreement frequency) does the opposite. However, the paper treats this as a user perception problem rather than a protocol-level coordination failure. It does not explore whether the visibility of dissent itself becomes an adoption/trust barrier, nor does it investigate whether agents condition behavior on the disagreement signal rather than the majority signal. The mechanism is perceptual and informational, not structural.

## Research connections

- **L-010:** Touches adoption nonmonotonicity but only at observation level; does not examine whether visibility of dissent changes adopter behavior or coordination equilibrium.
- **seed-017:** Multiple independent signals should drive convergence; instead drives visible divergence — but this is framed as a display problem, not a coordination mechanism.
- **seed-138:** Intent legibility under adviser systems — disagreement makes the reliability claim less legible even when mathematically justified.

## Seed

**Seed title:** Confidence-Visibility Inversion in Competence Aggregation

**Seed type:** observation

**Seed text:** In protocols that aggregate independent competent signals and expose the full adviser output to decision-makers, reliability and visible disagreement approach certainty at different rates, creating a divergence between formal correctness guarantees and observational confidence. As aggregation width increases, users may rationally condition adoption or trust on the disagreement signal (which is more salient and directly observable) rather than on the formal reliability proof (which requires epistemic work). This suggests that transparency of internal disagreement in safety-critical aggregation protocols may invert the relationship between competence growth and adoption pressure.
