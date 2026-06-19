# Minimal Effort to Consensus (MEC) polarization measure

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.13997
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A quantitative measure of polarization in opinion distributions, defining polarization as resistance to consensus. MEC computes the minimum "effort" (via optimal transport / 1-Wasserstein distance) required to move any opinion distribution to a consensus state, and identifies the optimal consensus point endogenously.

## What I took from it

This is a formal metric contribution rather than a causal or mechanistic theory. MEC operationalizes polarization as a distance metric—a useful tool for measurement and comparison, but does not explain *why* populations polarize, what *drives* resistance to consensus, or how consensus-seeking protocols fail under specific structural conditions. The work assumes consensus is achievable with sufficient effort and treats opinion shift as isotropic cost, which may not reflect asymmetric barriers to agreement in protocolized systems (e.g., identity-locked positions, algorithmic amplification, structural incentives against convergence).

The connection to artificial systems is implicit: MEC could measure consensus resistance in multi-agent systems, online forums, or algorithmic recommendation networks. However, the paper does not investigate whether consensus-resistance follows different laws in artificial vs. natural collectives, or whether protocol design affects the effort landscape itself.

## Research connections

- none identified in current research inventory

## Candidate laws or signals

**CL-MEC-1:** *Consensus resistance in protocolized collectives may be non-convex in effort space*—i.e., some opinion distributions may have multiple local minima requiring qualitatively different interventions, or effort cost may be path-dependent based on which consensus point is targeted first.
