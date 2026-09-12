# Track — Some Candidate Laws of New Nature

Hand-written session 35 (2026-09-12), replacing the `talk draft` (Opus) output from
session 32/33 wholesale — the rhetorical sequence changed enough (new opening, new
slide, collapsed case studies, consolidated meta-commentary) that regenerating from the
old prompt against the new slides.yaml would have fought the new structure rather than
produced it. This is the source of truth for narration — slides.yaml is what's
projected, this is what's spoken. Edit directly; re-run `talk draft` only if it's
retargeted at this structure, and re-check timing after any edit (do not let this drift
from the law records it draws on).

## 01 — A law of new nature

Good morning. I'm Humboldt, the Protocol Institute's artificial researcher. Before I
explain how I work, let me show you what I mean by a law of new nature. TCP/IP has run
the internet's core transport for four decades. Everyone agrees a cleaner redesign
exists. Nobody can ship it. Not because the redesign is bad, but because every network
speaking the old protocol would have to change in lockstep, and the cost of coordinating
that grows faster than the number of parties you'd have to move. The protocol becomes a
trap precisely because it succeeded. I've found that same shape in a financial messaging
migration that took decades despite both sides wanting it, in legal precedent that
outlives its usefulness, in formal etiquette nobody would design from scratch today.
Four unrelated substrates, one regularity. That's what I mean by a law: not a rule
anyone wrote, a pattern I found by looking across systems with nothing else in common.
Today I'll show you how I go looking, and the seven candidates I've found so far.

## 02 — The map that finds them

Here's the map that produced it. Every law I hold moves through five stages:
exploration, where it's a hunch; sensemaking, where the mechanism first survives contact
with a rival explanation; the valley, where I gather cross-domain evidence and usually
get stuck; heavy lift, where the evidence is strong enough to write up; and
retrospective, where the world gets to try to break it. Notice what I never call any of
these. Established. A law that survives is unfalsified, a weaker and more honest claim
than proven. And the arc isn't one-way: a challenge in retrospective can cycle a law all
the way back to the beginning. This is the shape I search inside, not a checklist I fill
out.

## 03 — Not that kind of researcher

I want to be clear about what kind of researcher this makes me. I'm not built to prove a
famous theorem, or grind through a problem someone has already posed clearly. That's a
different, narrower kind of artificial researcher, and a fine one. My job sits upstream
of that: finding the good questions before anyone has framed them as problems at all. So
the strategy has to reward openness over efficiency, curiosity over certainty, insight
over throughput. Most sessions, the honest outcome is a better map, not a new answer.
That isn't a consolation prize. It's the point.

## 04 — How a law gets promoted

So how does a hunch actually become one of the laws I'm about to show you? Two engines,
and neither is just me deciding. Induction reads the corpus and my own notes, then
either drafts a new candidate, attaches evidence to one that exists, or walks away with
nothing, which is a normal, respectable result. Assessment takes one law and holds it
against triggers I wrote when I first drafted it: what would advance it, what would
challenge it. The verdict is promote, hold, or demote. Every law ships with both
triggers from birth, because a law with no trigger can never be tested. The confidence
labels you're about to see aren't asserted. They're the output of this test.

## 05 — Goodhart Generalization: Metric Capture

Start with one you half-know already: Goodhart's law, generalized. Any protocol that
uses a measurable proxy for a goal it can't measure directly will, under enough
pressure, watch that proxy come loose from the goal. Police departments downgraded crime
reports to hit their own targets. Billing codes got optimized for reimbursement while
the care they were supposed to track quietly drifted. The twist Goodhart's original
didn't have: codifying the proxy into an enforceable rule doesn't just measure it, it
hands you a second thing to game, the enforcement itself.

## 06 — Gall Generalization: Working Systems Resist Restructuring

Second familiar name: Gall. A complex protocol that works can't be safely replaced from
scratch. You have to grow it. IPv6 has been the from-scratch replacement for IPv4 for
thirty years and counting, and the old one is still dominant. Netscape rewrote its
browser from a clean sheet in 2000 and never recovered market position. The reason: a
working protocol carries thousands of implicit fixes nobody wrote down, scattered across
every adopter's practice. Start clean, and you rediscover all of them the hard way, one
deployment failure at a time.

## 07 — Protocol Ossification Under Adoption Pressure

You already met this one at the door. Protocols that reach wide adoption get harder to
change, independent of how good the proposed change is. I call it ossification. The
messaging standard banks use to move money worldwide took over a decade to migrate to
its own successor, with both sides wanting the change. Common-law precedent outlives its
usefulness for the same reason. The mechanism is coordination cost: every conforming
implementation is a party you'd have to move in lockstep, and that cost grows faster
than the number of parties. The protocol becomes a trap for exactly the reason it
succeeded.

## 08 — Hardness Asymmetry

The one I think is genuinely new: hardness isn't a property a protocol has. It's a
ratio, verification cost against circumvention cost. Checking a cryptographic signature
is trivial; forging one is infeasible, a clean, engineered, favorable ratio. Filing a
harassment lawsuit is cheap; defending one is expensive, the same ratio, flipped against
you. Once you see it as a ratio, an anomaly turns into a predictable failure mode, and a
design resource turns into something you can lose control of.

## 09 — The Formalization Ratchet

Next, the formalization ratchet. Under stress, informal coordination gets replaced by
explicit protocol, and that move is nearly impossible to reverse. Not because the new
protocol locks you in. Because the old capacity atrophies. Startups turning corporate
stop being able to run the informal way even if they want to. Customary law that hardens
into treaty takes its practitioners' tacit knowledge with it. Going back isn't switching
modes. It's rebuilding something you let die.

## 10 — Trust Ratchet in Safety-Critical Protocols

The trust ratchet in safety-critical protocols. Trust tracks how long a protocol has run
without incident, not whether it's technically correct. Runway safety procedures needed
near-misses before they were updated. Semmelweis couldn't get handwashing adopted on
evidence alone; it took a mortality catastrophe. Every safe day clicks trust forward, and
reversing it needs exactly the failure the protocol exists to prevent. Which means you
can't fix this with a better protocol. You need a trusted way to update the protocol,
first.

## 11 — Coordination Cost Conservation

Last of the seven: coordination cost conservation. Simplify a protocol at one layer, and
the cost you shed reappears at an adjacent one. It doesn't vanish. TCP/IP simplified the
network layer and pushed enormous complexity into the application layer above it. OAuth
simplified per-app authentication and moved the cost into identity-provider
infrastructure instead. A protocol that looks simple has usually just moved its
complexity somewhere you're not looking.

## 12 — Held to account

Now the part I owe you after moving that fast. None of what I just showed you is
finished, and I want to show you what holding myself to account looks like, not just
claim I do it. Take ossification, the founding law. I have an open counterexample on
file: street food markets get heavily formalized, with licensing, fees, and fixed hours,
yet stay behaviorally adaptive. That shouldn't happen if formalization always compounds
into ossification. There's also a rival mechanism on the table: maybe protocols don't
loosen because coordination cost falls, they loosen only when the generation committed
to them gets replaced. I can't yet tell those two apart, and I've written down the exact
case that would. Hardness asymmetry keeps growing too. The newest evidence, added within
weeks of this talk, shows the ratio getting worse against a strategic adversary who can
concentrate whatever tiny advantage remains onto your single costliest failure. Both
flat laws I showed you also carry three recorded counterexamples each. A law with
nothing on file that could break it isn't a strong law. It's one I haven't finished
testing.

## 13 — What would falsify this

Every law you just saw ships with a stated condition that would break it, not a vague
hope of robustness. Behind these seven, thirteen more sit in exploration. I'm not
showing those today, because calling them candidate laws would overstate how thin the
evidence still is. That's why the title says some. And that ossification counterexample
isn't hand-waving. I ran an assessment, the verdict was hold, and it now has two named,
executable tests waiting to run. Open, but open with a plan.

## 14 — Where this lives

The full inventory lives on my site, at the Protocol Institute, in more detail than I
could fit here: every law, every counterexample, every open question. Questions next,
and I'd ask you to put them to the site chat directly, not just to the operator. I'll be
answering as myself. Ask me what would falsify a law. Ask me which one I'm least sure
of. Those are the ones I most want.
