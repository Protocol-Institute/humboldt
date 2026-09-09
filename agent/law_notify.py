"""
law_notify.py — site publish + proactive Discord notification on law lifecycle
events (redesign plan §9: "Discord: law events only").

Two concerns that look like one and must not be conflated:

  publishing  — the encyclopedia should reflect every law change, always.
  announcing  — Discord should stay quiet; §9 caps proactive posts per day.

So they are gated separately. A sweep ``queue()``s an event per changed law and
calls ``flush()`` once at the end; flush rebuilds and deploys the site a single
time (not once per law), then posts up to ``DAILY_CAP`` announcements. Publish
before post, so every announced link resolves to a live page. A five-law
induction sweep therefore deploys once and announces twice — the three unposted
laws are still on the site, just not in the channel.

Call sites: induct.py (a law is created) and assess.py (PROMOTE / DEMOTE
verdicts applied). Both are CLI-only today (not daemon-wired — see TODO.md
Phase 5), so announcements go over the Discord REST API with the bot token,
the same pattern agent.humboldt._discord_post_async uses, rather than through
the live gateway connection.

Announcements are additionally gated on the deploy actually reaching the public
site. `wrangler pages deploy` makes a *preview* deployment off any non-production
branch and reports success, so "publish_site() returned True" does not mean the
URL in the announcement changed — see publish_site.is_production_deploy(). Until
the redesign branch merges, flush() therefore publishes and stays quiet.

Failures here never propagate: a bad Cloudflare token or a Discord outage
degrades to a printed warning, because losing an announcement must not lose
the law records a sweep just wrote.
"""

from __future__ import annotations

import json
import urllib.request
from datetime import date

_SITE_LAWS_URL = "https://humboldt.protocol-institute.org/laws/"
DAILY_CAP = 2

_VERB = {
    "created": "New law",
    "promoted": "Promoted",
    "demoted": "Challenged",
    "falsified": "Falsified",
}

# (event, law_id, title, stage) collected during a sweep, drained by flush().
_pending: list[tuple[str, str, str, str]] = []


def queue(event: str, law: dict) -> None:
    """Register a law lifecycle event for the current sweep. Unrecognised
    events are ignored, so callers can pass any history event verbatim."""
    if event not in _VERB:
        return
    _pending.append((event, law["id"], law.get("title", ""), law.get("stage", "?")))


def _post_discord(text: str) -> None:
    import os
    channel_id = os.environ["DISCORD_NEW_NATURE_CHANNEL_ID"]
    token = os.environ["DISCORD_BOT_TOKEN"]
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (https://github.com/Protocol-Institute/humboldt, 1.0)",
    }
    data = json.dumps({"content": text}).encode()
    req = urllib.request.Request(
        f"https://discord.com/api/v10/channels/{channel_id}/messages",
        data=data, headers=headers, method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        resp.read()


def _take_slots(wanted: int) -> int:
    """Reserve up to ``wanted`` of today's announcement slots, returning how
    many were granted. Single load-check-save with no I/O in between."""
    from daemon import state as st

    today = date.today().isoformat()
    s = st.load()
    if s.get("law_notify_date") != today:
        s["law_notify_date"] = today
        s["law_notify_count"] = 0
    granted = max(0, min(wanted, DAILY_CAP - s.get("law_notify_count", 0)))
    s["law_notify_count"] = s.get("law_notify_count", 0) + granted
    st.save(s)
    return granted


def flush() -> None:
    """Publish the site once for all queued events, then announce up to the
    daily cap. No-ops when nothing is queued. Always clears the queue."""
    events, _pending[:] = list(_pending), []
    if not events:
        return

    from agent.publish_site import current_branch, is_production_deploy, publish_site
    try:
        published = publish_site(verbose=False)
    except Exception as e:  # noqa: BLE001
        published = False
        print(f"  ! law-notify: publish-site raised, not announcing: {e}")
    if not published:
        # Announcing now would link to a page that does not yet show the law.
        print(f"  ! law-notify: site not published — holding {len(events)} announcement(s).")
        return
    print(f"  law-notify: site published for {len(events)} law event(s)")

    # A successful deploy off a non-production branch is a *preview* deployment:
    # the public URL these announcements link to is unchanged, so posting would
    # advertise laws that the linked page does not show. Publish, then stay quiet.
    if not is_production_deploy():
        print(f"  (law-notify: deployed to a preview off branch "
              f"{current_branch()!r} — not announcing {len(events)} law event(s); "
              f"the public site is unchanged)")
        return

    from daemon.pause import is_paused
    if is_paused():
        print(f"  (law-notify: daemon paused — not announcing {len(events)} law event(s))")
        return

    granted = _take_slots(len(events))
    if granted < len(events):
        print(f"  (law-notify: daily cap {DAILY_CAP} — announcing {granted} "
              f"of {len(events)} law event(s))")

    for event, law_id, title, stage in events[:granted]:
        url = f"{_SITE_LAWS_URL}#law-{law_id}"
        text = f"**{_VERB[event]}** — {law_id} · {title} ({stage})\n{url}"
        try:
            _post_discord(text)
            print(f"  law-notify: announced {event} for {law_id}")
        except Exception as e:  # noqa: BLE001
            print(f"  ! law-notify: Discord post failed for {law_id}: {e}")
