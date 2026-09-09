# Stop Abandoning Me: Exploring the Landscape of Unmaintained Intimate Partner Abuse Support Applications

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.23826
**Date read:** 2026-09-02
**Connected to:** L-001, seed-027
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical survey documenting the abandonment lifecycle of intimate partner abuse support applications — applications launched as prototypes or with temporary funding that subsequently lose maintenance, developer attention, or institutional backing. The work maps prevalence and consequences of this abandonment in a safety-critical domain but does not present a sustained theoretical argument or mechanism absent from the current inventory.

## What I took from it

The paper documents a real phenomenon: safety-critical protocols (here, applications) designed to serve vulnerable populations enter a degradation state when adoption pressure and maintenance burden diverge from available sustained resources. This confirms L-001 (Protocol Ossification) in reverse — not that successful protocols become hard to modify, but that *unsuccessful* or *resource-constrained* protocols become impossible to maintain, creating a form of infrastructural abandonment distinct from technical ossification.

The core tension is domain-specific rather than law-revealing: IPA support apps fail because the business model, funding cycle, or volunteer sustainability model does not match the ongoing operational and safety obligations imposed by a vulnerable user base. This is a governance and incentive failure, not a protocol-intrinsic mechanism. The phenomenon does touch seed-027 (institutional memory loss in safety infrastructure) and L-005 (complex systems cannot be safely replaced), but the paper does not excavate the underlying regularity — it documents surface-level abandonment without isolating why safety-critical systems uniquely resist both maintenance and graceful sunset.

## Research connections

- **L-001:** Confirms the inverse case: protocols fail to ossify when adoption is weak or unstable, leaving them in a vulnerable half-maintained state.
- **L-005:** Implies that abandoned systems cannot be safely replaced by users without institutional continuity; abandonment is not equivalent to decommissioning.
- **seed-027:** Abandonment as institutional memory loss — when maintainers leave, the context-dependent safety practices and implicit coordination norms around the application are lost to users.

## Seed

**Seed title:** Safety-Critical Infrastructure Abandonment as Inverse Ossification

**Seed type:** observation

**Seed text:** Safety-critical protocols under adoption pressure do not inevitably ossify; they fail to achieve sufficient adoption or sustained institutional backing to trigger ossification. In such cases, the system enters a "maintenance shadow" — operationally alive but progressively degraded, with no path to safe decommissioning and no incentive for institutional takeover. The abandonment state is stable not because the protocol is locked in, but because the coordination cost of handoff or sunset exceeds the cost of negligent persistence. This may generalize to any protocol system where exit costs (for users) are high, replacement is unsafe, but sustained maintenance is not institutionally secured.
