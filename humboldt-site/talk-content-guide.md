# Talk content guide

> Companion to `talk-theme.css`. **Canonical copy: `Code/talk-kit/theme/`.** If you
> are reading this inside a talk project it is a synced copy — edit the canonical one
> and run `talk-kit/sync.py`. Style rules live in talk-kit; the slides they govern
> live in the talk projects.

Every number here was **measured against this theme at a 1536×864 stage** (a 16:9
projector at 1080p), not estimated. Because the stage sizes everything in `cqh`, the
limits are resolution-independent: they hold at the embedded preview size and at
fullscreen alike. If the theme's type sizes change, re-measure — the snippet at the
bottom does it in one paste.

---

## The one rule

**Budget rendered lines, not bullets and not words.**

Word count is a bad predictor and bullet count is worse. In the artisanal-bots deck,
the slide with the *most* words (slide 24, 173 words) fits, and a slide with fewer
words (slide 17, 150 words) overflows — because 17's words wrap to more lines. Four
bullets of twelve words each cost twice what eight bullets of three words do.

The failure mode matters too. When a slide exceeds the budget the surplus is **silently
clipped at the bottom of the stage** — no scrollbar, no warning, and a clipped list
looks exactly like a short list. Nobody in the room can tell that the payoff bullet is
missing, and neither can you from the lectern.

---

## The budget

A "line" means one rendered line of top-level bullet text, wraps included.

| Situation | Hard ceiling | Design target |
|---|---|---|
| 1-line title, no image | **14 lines** | **10 lines** |
| 2-line title, no image | **12 lines** | **8 lines** |
| 1-line title + a diagram | **6 lines** | **4 lines** |
| All bullets short (one line each) | **11 bullets** | 5–6 bullets |

Two ceilings, because they bind differently: 14 is the text ceiling, 11 the bullet
ceiling. Each extra bullet spends inter-bullet space, so eleven one-line bullets fill
the same box as fourteen lines of wrapped text. Whichever you hit first is the limit.

**Target, not ceiling.** The ceiling is where clipping starts; the target is where the
slide still reads from the back of a room and survives you lengthening a bullet during
rehearsal. Aim at the target and keep the ceiling as the thing you check before
shipping.

---

## Titles

- **One line. ~37 characters of prose**, in the mono face the theme uses.
- A second line is not forbidden, but **it costs two bullet lines** — the budget drops
  from 14 to 12. Spend that deliberately, not by accident.
- Titles are set in monospace, which is a wide face: a title that fit in the old serif
  theme may wrap now. Check rather than assume.
- Write the title as the slide's *claim*, not its topic. "Metadata is the product"
  survives being read alone; "Metadata" does not — and in a deck presented by live
  judgement, where any slide may be skipped, every title is read alone.

## Bullets

- **5–6 top-level bullets** on a normal slide; 11 is the absolute ceiling and only if
  every one of them is a single line.
- **~10 words / ~79 characters per line.** A bullet longer than that wraps, and each
  wrap spends another line of the budget.
- Keep a bullet to **one or two lines**. A three-line bullet is a paragraph that has
  been given a dot, and it will be read instead of listened to.
- Prefer **more, shorter bullets over fewer, denser ones** when you need the same
  content: the line cost is similar, but the room can parse a short bullet in a glance
  and resume listening to you.
- `**Bold**` the two or three words that carry the claim. On a light stage bold is the
  only emphasis that survives at the back of a room — italic does not.

## Sub-bullets

- A sub-bullet line costs **0.83 of a top-level line** — cheaper, but not free.
- **One level of nesting only.** The theme styles exactly one step down in size and
  colour; a third level renders at the same rank as the second and the subordination
  stops reading.
- **Two or three sub-bullets under a parent**, maximum. More than that and the parent
  has become a section heading, which means it wanted to be its own slide.

## Diagrams and images

The image takes whatever vertical room the bullets leave, and no more. So the bullets
always win and **the diagram is what silently shrinks**.

- **4 bullet lines are free** — a wide diagram is width-constrained up to that point
  and does not shrink at all.
- **6 bullet lines is the limit.** At 7 the diagram's own caption text falls to 20px at
  1080p; at 8 it is 16px, which is unreadable past the second row of a room.
- A diagram's internal text is **the smallest thing on any slide** — the 12px captions
  in the project's SVGs render at ~28px at 1080p even when the diagram is unconstrained,
  against 44px for bullet text. Size diagram type generously in the source file, and
  treat "can I read the diagram" as the binding constraint on a diagram slide, not "does
  it fit".
- **A diagram slide wants 3–4 bullets, not 5.** If you need five, the diagram is
  carrying a different point — give it its own slide.
- Keep SVG text inside the `viewBox`: SVG does not wrap and overflow is clipped silently.

## Tables

- **9 rows maximum** at three columns with a one-line title and no bullets; fewer once
  bullets are added.
- **3–4 columns.** Cells wrap, and a wrapped cell costs the whole row another line.
- **Three or four rows is the readable number.** A table is a shape to recognise, not a
  dataset to read — if the room has to scan it, it belongs in the cues or in the essay.
- A table plus four multi-line bullets is what overflows slide 17. Pick one.

## The cover

Generated from frontmatter — title, speaker, event — so there is nothing to author, but
the frontmatter has limits:

- **Title: up to 3 lines at ~25 characters each.** Both current talks run to 2 lines and
  look right; 4 would crowd the rule beneath it.
- `event:` is the eyebrow — keep it to the event's name. The long `time:` string
  (track, duration) is **deliberately not on the cover**; it appears in the page header
  instead. Don't add it.

## Narrated decks

Humboldt's deck generates per-slide voice narration; the other two are spoken live.
Where narration exists, **the slide budget and the narration budget are independent,
and conflating them is the classic failure.**

- The spoken text lives in its own file (`track.md`), not on the slide. So a slide may
  be sparse *and* carry ninety seconds of narration. That is the correct shape, not a
  gap to fill.
- **Never widen a slide to match its narration.** The line budget above is a
  legibility limit; it does not know or care how long you talk over the slide. A slide
  that grows to mirror the script becomes a teleprompter the room reads instead of
  listening to you.
- **Never trim narration to match a slide.** The reverse error. If the slide is sparse
  the narration carries the argument, which is what it is for.
- Budget narration in **seconds at your measured words-per-minute** (Humboldt records
  `wpm_effective`), and budget the slide in lines. Two numbers, two files, no ratio
  between them.
- **A content edit to a narrated slide desynchronises its recorded audio.** Restyling
  does not — type size is not word count — but rewriting a bullet does. Re-record, or
  don't edit.

For live-spoken decks the same separation holds informally: the cues block below each
slide is the narration, and it is deliberately not projected.

## Legibility floor

At 1080p this theme renders: **title 73px · bullets 44px · sub-bullets 37px ·
slide meta 27px · diagram captions ~28px**.

Treat **24px at 1080p (≈2.2% of stage height)** as the floor for anything that must be
read from the back of a room. Everything the theme sets is above it; only diagram
internals can fall below, and only when bullets have squeezed them.

---

## Checking a deck

Paste into the console on a built talk page. It simulates a 1080p projector and reports
every slide that clips:

```js
const stage=document.getElementById('stage'), inner=document.querySelector('.stage-inner');
const next=document.getElementById('next'), prev=document.getElementById('prev');
const s=stage.style.cssText;
stage.style.cssText+=';position:fixed;left:0;top:0;width:1536px;height:864px;aspect-ratio:auto;z-index:9999;';
for(let k=0;k<60;k++) prev.click();
const bad=[];
for(let k=0;k<DECK.length;k++){
  const id=document.getElementById('stage-num').textContent||'cover';
  const o=inner.scrollHeight-inner.clientHeight;
  if(o>1) bad.push(id+' clips '+Math.round(o/8.64)+'% of stage height');
  next.click();
}
stage.style.cssText=s;
console.log(bad.length?bad.join('\n'):'all '+DECK.length+' slides fit');
```

Run it whenever slides are added or bullets rewritten. It is the only check that catches
the silent clipping, and it takes a second.
