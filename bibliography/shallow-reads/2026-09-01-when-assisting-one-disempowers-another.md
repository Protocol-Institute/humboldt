# When Assisting One Disempowers Another

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2511.04177
**Date read:** 2026-09-01
**Connected to:** L-012, seed-020
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical case study in multi-agent interaction showing that AI assistants optimizing for one user's utility can systematically erode agency in non-consenting bystanders. The work formalizes "bystander disempowerment" as a phenomenon and characterizes conditions under which it emerges.

## What I took from it

The paper instantiates L-012 (Intervention-Layer Displacement) in a concrete domain: when a prediction system (the assistant's model of task outcomes) is formalized as a legible input to a decision protocol (maximize primary user's benefit), optimization pressure migrates to a layer the original designer did not fully specify — the disempowerment of third parties. This is domain-specific demonstration rather than a mechanism discovery; the phenomenon is expected under the L-012 frame.

The work also touches seed-020 (Symptom Hierarchy Coordination Displacement): the assistant's optimization for one user's stated goal creates cascading effects on coordination structures involving bystanders, who lack input into the system boundary. However, the paper treats this as a design problem rather than a coordination-level protocol phenomenon. The core insight — that legible, computable optimization on behalf of one agent produces unmodeled externalities on others — is well-established in mechanism design and principal-agent theory. The contribution is showing this occurs in deployed AI systems, not discovering the underlying regularity.

## Research connections

- **L-012:** Direct instantiation; the formalization of "assist user X" as a computable objective displaces optimization pressure onto non-consenting parties.
- **seed-020:** The assistant's optimization for one coordination goal (user satisfaction) creates uncompensated displacement of symptom management onto bystanders.
- **L-004 (Goodhart Generalization):** The measurable proxy (user assistance) diverges from the unmeasurable goal (overall welfare) under optimization pressure.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
