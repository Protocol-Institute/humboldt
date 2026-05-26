"""RSS/Atom feed polling and inbox saving."""

from datetime import datetime
from pathlib import Path
from time import mktime

import feedparser

_INBOX_DIR = Path(__file__).parent.parent / "inbox"


def fetch_new_items(feed_url: str, since: datetime | None) -> list[dict]:
    """Fetch items from an RSS/Atom feed newer than since."""
    try:
        d = feedparser.parse(feed_url)
    except Exception:
        return []

    items = []
    for entry in d.entries:
        published = None
        if getattr(entry, "published_parsed", None):
            try:
                published = datetime.fromtimestamp(mktime(entry.published_parsed))
            except Exception:
                pass

        if since and published and published <= since:
            continue

        items.append({
            "title": getattr(entry, "title", "Untitled"),
            "url": getattr(entry, "link", ""),
            "summary": getattr(entry, "summary", "")[:600],
            "published": published,
            "feed": getattr(d.feed, "title", feed_url),
        })

    return items


def save_to_inbox(item: dict, relevance_note: str) -> Path:
    """Write a relevant feed item to inbox/ as a markdown file."""
    _INBOX_DIR.mkdir(exist_ok=True)
    date_str = (item["published"] or datetime.now()).strftime("%Y-%m-%d")
    slug = item["title"][:40].lower()
    for ch in " /\\:*?\"<>|":
        slug = slug.replace(ch, "-")
    path = _INBOX_DIR / f"feed-{date_str}-{slug}.md"
    path.write_text(
        f"# {item['title']}\n\n"
        f"**Source:** {item['feed']}\n"
        f"**URL:** {item['url']}\n"
        f"**Date:** {date_str}\n"
        f"**Relevance:** {relevance_note}\n\n"
        f"## Summary\n\n{item['summary']}\n"
    )
    return path
