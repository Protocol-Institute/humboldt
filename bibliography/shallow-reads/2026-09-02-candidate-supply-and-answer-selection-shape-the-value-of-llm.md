# Candidate supply and answer selection shape the value of LLM judging in multi-agent systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.25937
**Date read:** 2026-09-02
**Connected to:** L-010, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of multi-agent LLM systems that examines how consensus failures occur despite latent correctness in the candidate pool. The work decomposes multi-agent reasoning into generation → communication → selection stages and uses LLM judges as a selection pressure mechanism to investigate when judgment improves collective answer quality.

## What I took from it

The paper confirms a key structural vulnerability in decentralized multi-agent protocols: **memetic drift can occur in the selection layer independently of candidate quality**. When agents communicate and aggregate without external validation, consensus can converge on incorrect outputs even when the solution space contains correct answers. This is directly relevant to L-010 (adoption nonmonotonicity) and L-012 (intervention-layer displacement): introducing an LLM judge as a legible decision criterion should improve selection fidelity, but the paper's framing suggests this is conditional on candidate supply distribution and judge calibration.

The work also surfaces a mechanism for L-012: when selection becomes formalized (LLM judge = legible optimization target), the pressure point shifts from *what agents communicate* to *what candidates are generated upstream*. This implies coordination failure can be displaced rather than resolved—optimizing the selection layer may leave generation-layer quality or diversity untouched, or worse, cause agents to game judge preferences rather than improve underlying reasoning.

## Research connections

- **L-010:** Memetic drift in consensus without external validation suggests adoption of "consensus-only" protocols may be nonmonotonic in robustness; adding judgment machinery can threshold adoption patterns.
- **L-012:** Formalizing selection as an LLM judge criterion displaces optimization pressure upstream to candidate generation; agents may converge on judge-legible rather than correct outputs.
- **seed-073:** Correlated failure under proxy consensus — consensus without quality control exhibits shared failure modes; judge introduces a new proxy target.
- **seed-080:** Proxy collapse under upstream asymmetry — if candidate generation quality is heterogeneous, a judge cannot recover absent diversity in the pool.

## Seed

**Seed title:** Selection Pressure Displacement Without Upstream Repair

**Seed type:** observation

**Seed text:** In multi-agent systems where generation and selection are decoupled, introducing legible selection pressure (e.g., an LLM judge) can improve terminal answer quality without improving the underlying candidate pool quality or diversity. The optimization pressure shifts downstream, leaving upstream generation vulnerabilities in place. This creates a stable pseudo-equilibrium: agents report better answers via better selection without improving their reasoning; if the judge is later unavailable or becomes miscalibrated, performance collapses to the original memetic-drift baseline. The pattern suggests that legible intervention at one protocol layer may mask rather than repair systemic coordination failures in upstream layers.
