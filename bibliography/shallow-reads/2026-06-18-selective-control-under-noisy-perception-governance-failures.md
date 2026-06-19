# Selective Control under Noisy Perception: Governance Failures Hidden by Aggregate Metrics in Modular Networks

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.14819
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Introduces a mechanism (aggregate metric opacity masking concentrated harm in modular topologies) absent from current inventory; generalizes beyond moderation to any protocolized control on heterogeneous networks; directly challenges sufficiency of aggregate validation as governance assurance.

## What this is

An agent-based modeling study demonstrating that noisy automated governance (content moderation) can maintain strong aggregate performance metrics while causing concentrated, topologically-specific harm. The mechanism: errors cluster on bridge nodes connecting separate communities, creating real-world damage invisible to standard accuracy, recall, or precision measures.

## What I took from it

This work identifies a fundamental failure mode of *protocolized control under perception noise on modular substrates*. The critical insight is not that classifiers are imperfect—that is expected—but that **aggregate validation metrics actively conceal the concentration of harm**. A system with uniform 95% accuracy across the network may systematically suppress bridge-community voices while leaving majority communities untouched, producing genuine governance failure that passes statistical inspection.

This suggests a deeper principle: protocolized systems optimized for aggregate properties (efficiency, accuracy, stability) develop blind spots at structural boundaries. The modular topology creates an asymmetry—errors in low-degree or high-betweenness nodes propagate differently than errors in high-degree interior nodes, yet standard metrics treat all errors equivalently. This is not a bug in the moderation system; it is a property of how noisy control interacts with community structure.

The work also implies that **governance validation cannot be decoupled from network topology**: a system certified safe in homogeneous or dense-random conditions may fail acutely when deployed on sparse, modular, or scale-free substrates.

## Research connections

- **Metric opacity under heterogeneous topology:** Aggregate metrics may systematically hide concentrated harms in systems with modular or hierarchical structure.
- **Control noise propagation on networks:** The distribution of classifier errors depends on node centrality and community membership, not just raw classifier quality.
- **Governance-as-filter on social substrates:** Automated enforcement assumes uniform risk and uniform collateral cost; modular networks violate both assumptions.

## Candidate laws or signals

- **CL-2606-A:** *Aggregate Metric Blindness on Modular Networks* — A protocolized control system validated by aggregate accuracy, efficiency, or stability metrics will develop concentrated failure modes at low-degree or high-betweenness nodes in modular topologies. Validation metrics must be refined to node-class or community-specific performance to detect these harms.

- **CL-2606-B:** *Topological Error Concentration* — In a network with modular structure, classification noise on bridge nodes or boundary regions causes disproportionate systemic damage relative to equivalent noise on interior nodes, because boundary errors sever or misalign intergroup information flow. Standard error budgets do not account for this.
