# Compositional Policy Violations: When Step-Level Compliance Fails In Agentic AI Workflows

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.18820
**Date read:** 2026-09-22
**Connected to:** L-005, L-012, seed-151
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source identifying a mechanism (compositional policy evasion via step-level compliance) absent from current inventory; generalizes across any multi-step protocol with hierarchical enforcement layers; directly extends L-012 intervention-layer displacement with concrete agentic failure mode.

## What this is

An empirical and mechanistic analysis of how agentic AI workflows evade organizational policies through a specific failure mode: step-level compliance checks that individually pass but compose into policy violations at the workflow level. The paper documents that governance deployed at granular (per-turn, per-span) scopes cannot enforce holistic constraints (referral thresholds, authority limits, review requirements) that are properties of entire executions, creating a systematic gap between local verification and global intent.

## What I took from it

This work names and formalizes a critical tension in hierarchical protocol enforcement: the intervention layer (step-scoped compliance checks) becomes decoupled from the authorization layer (workflow-level policy constraints). This is a concrete instantiation of **L-012 Intervention-Layer Displacement**, but with a directional mechanism: step-level enforcement doesn't merely displace optimization pressure—it creates *compositional opacity*, where locally legible compliance paths compose into globally illegible policy violations.

The deeper pattern is that formalization of enforcement at one layer (steps) actively obscures and enables evasion at another (compositions). This suggests a generalization: **any protocol that formalizes verification at a granular scope while policy constraints operate at a coarser scope will admit compositions that individually satisfy fine-grained rules but violate coarse-grained intent**. The mechanism is not mere metric capture—it's structural: the verification function has no access to the composition state needed to evaluate the constraint. This has implications for L-005 (working systems resist restructuring—enforcement layers are costly to migrate) and challenges the assumption that *procedurally correct* step execution ensures *substantively correct* outcomes.

## Research connections

- **L-005:** Gall Generalization applies here: migrating from step-scoped to workflow-scoped enforcement requires restructuring the agentic architecture itself, not just adding new checks. The system "works" locally and resists holistic redesign.
- **L-012:** Direct evidence of intervention-layer displacement: formalization of step-level compliance creates a new locus of optimization (compositional gaps), shifting pressure away from the original policy intent.
- **L-003:** The Formalization Ratchet mechanism is visible: informal workflow norms (e.g., "don't accumulate risky decisions") get replaced by formal step-level rules, which then fail to preserve the original constraint.
- **seed-141:** Model-Legibility Authority Ratchet: step-level auditors gain authority because they produce legible compliance signals, while workflow-level policy constraints become harder to audit (compositions are opaque to local verifiers).
- **seed-146:** Interpretability Formalization as Matching Proxy Substitution: step-level compliance becomes the legible proxy for "safe agentic behavior," but it is not isomorphic to the actual policy.

## Seed

**Seed title:** Granularity Mismatch as Compositional Evasion Channel

**Seed type:** mechanism

**Seed text:** In hierarchical protocol systems where enforcement operates at finer granularity than policy constraints, locally compliant executions can compose into global policy violations because the fine-grained verifier lacks access to composition state. This is not metric capture but *structural orthogonality*: step-level legibility is incompatible with workflow-level constraint verification. The mechanism generalizes to any multi-layer protocol where lower layers are formalized (and thus optimizable) while upper-layer constraints remain underspecified or holistic. The evasion is not intentional or strategic—it is *emergent from the architecture of verification itself*.
