# OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.05013
**Date read:** 2026-09-02
**Connected to:** L-011, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems engineering paper presenting OneDayAgent, a framework for managing long-horizon LLM agent tasks that span multiple steps, tools, and environments. The work addresses practical failure modes—goal drift, state loss, context overflow—in autonomous agents operating across heterogeneous backends, but remains fundamentally a tool-integration and prompt-engineering contribution rather than a theoretical or empirical investigation of underlying protocol laws.

## What I took from it

The paper documents a real engineering problem: agents operating under resource constraints and tool heterogeneity lose coherence around stated goals and constraints as task horizons extend. The proposed "harness" appears to be a control-layer addition: explicit goal/constraint preservation mechanisms, state management protocols, and context windowing strategies.

This touches L-011 and L-012 territory, but only surface-level. The work *observes* that goals become detached from execution trajectories in long-horizon settings, and that intervention (adding constraint-tracking layers) shifts optimization loci—but it does not investigate *why* these failures are stable equilibria or what conditions make them inevitable versus contingent. The paper is diagnostic of a symptom (goal drift) and prescriptive of a patch (better state tracking), not explanatory of the mechanism. No evidence that the problem generalizes beyond multimodal LLM agents, and no mechanism account for why formalized goal-preservation protocols would themselves resist modification or generate new failure modes.

## Research connections

- **L-011:** Observes that long-horizon agent execution decouples from stated goals; does not explain why this is stable or what conditions lock it in.
- **L-012:** Adds explicit constraint-legibility layers; does not track whether this displaces optimization pressure upstream (to goal specification itself or tool selection).
- **seed-068 (Unmeasurability as Anomaly Insulation):** The paper assumes goals are measurable/trackable; silent on what happens when they are not.
- **seed-070 (Obligate-Coordination-as-Infrastructure-Constraint):** Multi-tool coordination is enforced as infrastructure; no account of what coordination costs are preserved or displaced.

## Seed

**Seed title:** none
