# The Context Access Divide: Interaction-Level Architecture as a Complementary Dimension of Agentic Inequality

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.08495
**Date read:** 2026-09-01
**Connected to:** L-006, seed-020
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A social science paper extending Sharp et al.'s "agentic inequality" framework by introducing interaction-level architectural differences as a source of disparity distinct from availability, quality, and quantity of agent access. The primary argument is that even nominally equivalent agent access produces unequal utility when systems vary in their capacity to autonomously retrieve, contextualize, and act on domain-specific information during interactions.

## What I took from it

The paper articulates a genuine architectural divide—one user's agent may have legible access to contextual data stores (medical records, transaction history, domain knowledge bases) while another's does not—that operates independently of person/org-level access metrics. This maps cleanly onto L-006 (Coordination Cost Conservation): the paper appears to argue that coordination overhead doesn't disappear when agent access is democratized; it *displaces* to the interaction level, where architectural heterogeneity in context-availability becomes the new locus of inequality.

The mechanism is protocol-adjacent: systems with higher context legibility reduce interaction-level friction costs, but this architectural advantage concentrates benefit among those whose data is already integrated into high-access infrastructure. This confirms seed-020 (symptom-hierarchy-coordination-displacement) — the coordination problem doesn't vanish, it moves to a finer grain where it becomes less visible and harder to address through access policy alone.

However, the paper appears primarily diagnostic rather than mechanistic. It identifies a structural divide but does not establish a generalizable law about *when* and *why* context-access architecture becomes the binding constraint on utility, nor does it theorize how this interacts with protocol adoption or formal governance.

## Research connections

- **L-006:** Confirms the displacement thesis — coordination costs don't vanish under democratized access; they concentrate at architectural layers below the formal access model.
- **seed-020:** Exemplifies symptom-hierarchy displacement — inequality shifts from visibility (who has agents?) to legibility (whose data is integrated?).
- **L-012:** Related but distinct — this is about context *availability* architecture, not about prediction-to-decision formalization; worth tracking whether they entangle in practice.

## Seed

**Seed title:** Context Legibility as Protocol Inequality Substrate

**Seed type:** observation

**Seed text:** In agent-mediated protocol systems, inequality indexed to person/organization-level access metrics can be conserved and displaced into interaction-level architectural heterogeneity — specifically, differential legibility of domain-specific context data to autonomous retrieval and reasoning processes. Systems with higher context integration deliver utility gains that scale with the agent's ability to autonomously access structured information, not with the agent's base capability. This creates a secondary inequality gradient orthogonal to formal access policy: two agents of identical capability and availability produce unequal outcomes when one operates in an information architecture with legible contextual integration and the other does not. This may generalize to any protocol system where autonomous components must retrieve external state to execute; the binding constraint shifts from access to the agent to access-architecture of the state the agent must act upon.
