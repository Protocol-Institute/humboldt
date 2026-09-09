# Voice AI in Firms: A Natural Field Experiment on Automated Job Interviews

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.28222
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A large-scale field experiment (N=70,000) comparing human vs. AI voice-agent job interviews, with hiring decisions made by humans post-interview. The paper reports that AI-interviewed applicants receive 12% more job offers and show higher retention, attributed to reduced variance in interview conditions.

## What I took from it

The work is primarily an empirical validation that automation reduces *variance* in information collection, producing measurable downstream benefits (job offer rates, retention). This is straightforward optimization through standardization—not a mechanism inquiry.

However, the structure does illustrate L-004 and L-008 in a clean way: the AI agent creates a *legible proxy* (standardized interview behavior, tone, question sequencing) that human recruiters then optimize around. The 12% uplift likely reflects that recruiters, evaluating the *interview record* rather than the raw applicant, are making decisions based on a more consistent signal. The paper does not investigate whether this consistency selects for *actual job performance* or merely *interview-game fitness*—a classic Goodhart candidate. The lack of *decline* in retention suggests the proxy may be reasonably aligned, but this is not proven.

The generalizability claim (variance reduction → better outcomes) is domain-specific to hiring, and the paper offers no mechanism that would hold across protocol systems broadly.

## Research connections

- **L-004:** Confirms Goodhart risk: the consistency proxy created by AI agents becomes a legible optimization target for recruiters; the paper does not measure proxy divergence from true job fitness.
- **L-008:** Illustrates the setup: computable enforcement (standardized interview) creates a legible signal that downstream decision-makers optimize around; no evidence of downstream gaming or perverse adaptation yet.
- **seed-062:** Light touch: formalization of interview (AI standardization) increases legibility; the paper does not examine whether this changes what recruiters *attend to*.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
