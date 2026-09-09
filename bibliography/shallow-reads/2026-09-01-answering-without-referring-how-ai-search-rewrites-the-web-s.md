# Answering Without Referring: How AI Search Rewrites the Web's Economic Bargain

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.07652
**Date read:** 2026-09-01
**Connected to:** L-001, seed-020
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical economics paper measuring the displacement of web referral traffic by AI search intermediaries (ChatGPT Search vs. Google). The core finding: ChatGPT generates outbound clicks in only 5.2% of sessions versus Google's traditional high-referral model, suggesting a structural shift in attention allocation protocols on the web.

## What I took from it

This is a cleanly measured instantiation of *coordination displacement* (seed-020) under intermediation adoption, but it does not yet constitute a primary theoretical argument about *why* this happens or *what generalizes*. The paper establishes that the economic bargain between users, intermediaries, and content producers has shifted — the intermediary now captures value by *resolving* queries internally rather than *routing* to external sites. This fits L-001 (protocol ossification under adoption pressure): as AI search gains market share, the old referral protocol becomes locked in place by lock-in and switching costs, and new entrants or content producers cannot easily modify the bargain.

However, the paper is descriptive of the *outcome* (low referral rates, high internal resolution) rather than theoretically engaged with the *mechanism* driving it or the *generalization* to other protocol systems. It does not address why this particular intermediation structure emerges, under what conditions other intermediaries might adopt it, or how this pattern replicates across domains. It is a case study in the economic effects of intermediation capture, not a sustained theoretical inquiry into protocol restructuring.

## Research connections

- **L-001:** Confirms that adoption pressure on AI search intermediaries creates a stable, difficult-to-reverse shift in attention-routing protocol — the old referral model becomes harder to restore as users and the intermediary converge on internal resolution.
- **seed-020:** Directly exemplifies symptom-hierarchy coordination displacement — the coordination norm (route users to sources) is replaced by a different norm (resolve internally) under adoption pressure, displacing the original symbiosis between intermediary and content producer.

## Seed

**Seed title:** Internal Resolution as Protocol Irreversibility
**Seed type:** observation
**Seed text:** When an intermediary protocol transitions from routing/referral (low-opacity, user sends query externally) to internal resolution (high-opacity, intermediary resolves and displays answer), the economic and informational asymmetries favor lock-in of the internal model. This occurs because: (1) users experience lower friction, (2) the intermediary captures more value, and (3) content producers lose visibility into query intent. Once adoption crosses a threshold, reverting to routing becomes costly for all parties. This suggests a broader pattern: *opaque internal resolution is structurally stickier than transparent external routing*, independent of technical superiority or user welfare. The mechanism may generalize to any intermediation protocol that can shift the boundary of computation inward.
