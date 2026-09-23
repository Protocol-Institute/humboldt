# ERPBench: A State-Grounded Evaluation Paradigm for Computer-Use Agents in Enterprise Software

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.17885
**Date read:** 2026-09-22
**Connected to:** L-002, seed-131
**Kind:** benchmark/tool paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark and evaluation framework for testing agentic AI systems (computer-use agents) on enterprise resource planning (ERP) software. The work introduces ERPBench, a state-grounded evaluation environment for measuring agent performance on multi-step, consequential tasks in dense, coordinated enterprise interfaces where errors produce persistent changes rather than easily observable failures.

## What I took from it

The paper identifies a genuine gap in current evaluation infrastructure: existing benchmarks test agents on forgiving, feedback-rich environments (web tasks, desktop UI), but ERP systems present a different failure surface. Errors don't surface as visible UI anomalies—they corrupt persistent business state (accounting records, inventory counts, customer data). This creates an attribution problem: an agent can complete a sequence of actions that look correct locally but fail globally due to state inconsistency.

The work is primarily a tool/benchmark paper, not a theoretical contribution. However, it does surface an operationally interesting constraint: **when failure is invisible at the action layer but consequential at the state layer, the verification function becomes decoupled from the execution signal.** This is empirical scaffolding for L-002 (Hardness Asymmetry) and seed-131 (Context Legibility as Failure Attribution Boundary), but the paper doesn't theorize this—it just builds a test harness that makes the problem legible.

## Research connections

- **L-002 (Hardness Asymmetry):** ERP failures demonstrate the asymmetry empirically—verification (detecting state corruption) is orders of magnitude harder than execution (sending UI commands), but the paper doesn't formalize this as a general principle.
- **seed-131 (Context Legibility as Failure Attribution Boundary):** The core insight: in dense, multi-step coordinated protocols, local action legibility (screenshots, button presses) decouples from global state legibility (accounting consistency). Failure attribution becomes ambiguous. The benchmark makes this *visible* but doesn't theorize the boundary condition.
- **L-004 (Goodhart Generalization):** Tangentially relevant if evaluation metrics are constructed to measure "task completion" without capturing state integrity—the proxy could become adversarial.

## Seed

**Seed title:** State-Layer Invisibility as Verification Decoupling in Coordinated Multi-Agent Protocols

**Seed type:** observation

**Seed text:** In protocol systems where agents operate through legible local actions (screenshot, keystroke, query) but effects accumulate in hidden persistent state, the verification function becomes radically harder than the execution function, and this gap widens with protocol density and coordination coupling. Action-level success signals become unreliable indicators of state-layer consistency. This may be a general property of any multi-layer protocol where the agent's perception layer is coarse and the consequence layer is fine-grained; ERP systems are a canonical case, but the pattern should recur in any system where agents act through an interface disconnected from the state they're modifying.
