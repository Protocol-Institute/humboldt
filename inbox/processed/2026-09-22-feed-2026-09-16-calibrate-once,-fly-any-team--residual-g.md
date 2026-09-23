# Calibrate Once, Fly Any Team: Residual-Grounded Low-Fidelity Training for Cooperative Drone Swarms

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2609.17265
**Date:** 2026-09-16
**Relevance:** Directly addresses multi-agent training efficiency for drone swarms through low-fidelity simulation approaches, relevant to cooperative robotics and scalable RL policy learning.

## Summary

arXiv:2609.17265v1 Announce Type: new 
Abstract: Training multi-agent drone-swarm policies directly in high-fidelity (HF) rigid-body physics is accurate but computationally expensive. This cost scales poorly with team size, as each additional agent multiplies contact-resolution complexity and sharply raises the in-simulation crash rate. To address this, we propose a mixed-fidelity training scheme that eliminates HF reinforcement learning entirely.
  A single shared, decentralized policy is optimized inside a fully-differentiable, JAX-native low-fidelity (LF) point-mass simulator. The simulator
