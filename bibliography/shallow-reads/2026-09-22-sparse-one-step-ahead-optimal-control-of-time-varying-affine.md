# Sparse One-Step-Ahead Optimal Control of Time-Varying Affine Opinion Networks: Tracking and Competitive Games

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.20450
**Date read:** 2026-09-22
**Connected to:** L-010, seed-138
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A control-theoretic paper studying resource-constrained intervention in opinion dynamics networks (DeGroot/Friedkin–Johnsen models). The work solves the one-step-ahead optimal control problem when an external controller can select a small set of agents and apply a scalar intervention per timestep, yielding sparse cardinality-constrained solutions.

## What I took from it

The paper is technically competent and well-scoped within its domain, but offers little that generalizes beyond the specific mathematical problem of sparse control in affine opinion systems. The core finding—that cardinality-constrained influence can be solved by selecting agents with largest or smallest residual components—is a local optimization result with no obvious bearing on protocol-level phenomena or coordination dynamics.

The triage note correctly identified a surface parallel to L-010 (coordination adoption nonmonotonicity) and seed-138 (intent legibility as coordination target displacement), but neither connection holds under inspection. L-010 concerns how adoption signals create *feedback loops* that produce non-monotonic adoption curves; this paper assumes a fixed network topology and optimizes intervention targeting, with no adoption feedback. Seed-138 tracks how making agent intent legible *shifts what becomes the optimization target*; this paper assumes intent (minimizing distance from target opinion) is already fully legible, and solves the resulting control problem deterministically. The resource constraint (sparsity) is present in both cases, but the mechanism is absent: there is no demonstration that legibility itself generates the sparsity requirement, nor that the sparse control structure feeds back to reshape agent coordination behavior.

## Research connections

- **L-010:** No real connection. L-010 requires endogenous adoption feedback; this work assumes fixed network structure and solves a deterministic control problem.
- **seed-138:** Shallow connection only. Intent is already fully legible; the paper does not show how legibility *creates* the targeting problem or displaces what agents coordinate on.

## Seed

**Seed title:** none
