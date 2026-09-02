# ABIDES-MARL: A Multi-Agent Reinforcement Learning Environment for Optimal Execution with Endogenous Liquidity

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2511.02016
**Date read:** 2026-09-02
**Connected to:** L-009, L-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A tool paper introducing a multi-agent simulation environment for studying optimal execution under endogenous liquidity. The work reframes classical execution as a finite-horizon stochastic game where market makers adapt strategically, rather than treating market impact as exogenous. Primary domain: algorithmic trading and market microstructure simulation.

## What I took from it

This is a competent methodological contribution that shifts the framing from single-agent control to multi-agent interaction—a recognition that protocols (market structures) generate emergent dynamics when participants optimize simultaneously. The endogeneity insight is sound: once execution strategies become legible and reactive, liquidity ceases to be a stable exogenous parameter.

However, the work remains confined to mechanism design within a specific domain. It does not propose or test a general law about how strategic adaptation under protocol constraints induces failure modes, convergence pathologies, or governance pressure. The MARL environment is the contribution; the theorized dynamics of racing, coordination collapse, or catastrophic risk cancellation under symmetric pressure (L-009) are not explored empirically or proven to generalize beyond market microstructure. The paper treats endogenous adaptation as a technical problem to simulate, not as an instance of a broader pattern in artificial protocol systems.

## Research connections

- **L-009:** Tangentially touches the condition space (competitive protocol races with asymmetric payoffs), but does not investigate catastrophic risk cancellation or empirical evidence for the collapse threshold.
- **seed-080:** Proxy collapse under upstream asymmetry — market impact as a misspecified proxy for true liquidity when agents adapt — is implicit in the motivation, but not formalized or generalized.
- **seed-078:** Learning-race defection as pooling resistance — strategic execution algorithms may resist coordination in favor of defection, a dynamic present but not theorized here.

## Seed

**Seed title:** Endogenous Legibility Inversion in Competitive Execution Protocols
**Seed type:** observation
**Seed text:** When execution algorithms make their optimization targets (liquidity demand, pricing signals, counterparty willingness) legible to reactive market makers through repeated interaction, the market maker's adaptation flips the assumed causal direction: liquidity ceases to be an exogenous supply function and becomes a strategic response variable. This suggests a broader pattern: in any multi-agent protocol where one agent's assumption about the other's stationarity becomes computable and observable, the observing agent optimizes to break that stationarity, destabilizing the original single-agent model. The question is whether this extends to governance protocols, authentication systems, and auditing frameworks where similar legibility inversion could occur.
