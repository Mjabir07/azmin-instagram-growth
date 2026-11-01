"""Daily brief for Jabir (09:00 Dubai): yesterday's numbers, what posts today and next, what waits for ✅,
today's engagement group and his to-do list.

Reads only repo files (the insights snapshots, the queue, marketing/engage/targets.md). Writes
marketing/daily/<date>.md (the azmin-daily Chrome skill reads it) and sends the same text to Telegram.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import date, datetime, timedelta

from agent.config import ROOT
from agent.notify import telegram
from agent.social import queue
from agent.social.queue import DUBAI

INSIGHTS = ROOT / "marketing/insights"
TARGETS = ROOT / "marketing/engage/targets.md"
OUT = ROOT / "marketing/daily"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def account_numbers(text: str) -> dict:
    """followers / following / posts from a snapshot's header line."""
    m = re.search(r"· (\d+) followers · (\d+) following · (\d+) posts", text)
    return dict(zip(("followers", "following", "posts"), map(int, m.groups()))) if m else {}


def latest_reel(text: str) -> dict:
    """Newest reel row of a snapshot table: when, first line, views, reach, avg watch, skip rate, shares, follows."""
    for row in text.splitlines():
        cells = [c.strip() for c in row.strip("|").split("|")]
        if len(cells) >= 16 and cells[1] == "reel":
            return {"posted": cells[0], "line": cells[2], "views": cells[3], "reach": cells[5], "watch": cells[6],
                    "skip": cells[7], "shares": cells[11], "follows": cells[13]}
    return {}


def engage_today(day: date) -> tuple[str, list[str], list[str]]:
    text = TARGETS.read_text()
    group, accounts = "", []
    for row in text.splitlines():
        cells = [c.strip() for c in row.strip("|").split("|")]
        if len(cells) == 3 and cells[0] == DAYS[day.weekday()]:
            group, accounts = cells[1], [a.strip() for a in cells[2].split(",")]
    peers = text.split("## Every day", 1)[1].splitlines()[1].split(",") if "## Every day" in text else []
    return group, accounts, [p.strip() for p in peers if p.strip()]


def build(now: datetime) -> str:
    today = now.date()
    snaps = sorted(INSIGHTS.glob("*.md"))
    nums = account_numbers(snaps[-1].read_text()) if snaps else {}
    prev = account_numbers(snaps[-2].read_text()) if len(snaps) > 1 else {}
    reel = latest_reel(snaps[-1].read_text()) if snaps else {}
    items = queue.load_all()
    todays = [i for i in items if i.post_at.date() == today]
    upcoming = sorted((i for i in items if today < i.post_at.date() <= today + timedelta(days=3)), key=lambda i: i.post_at)
    waiting = [i for i in items if i.status in ("draft", "pending") and i.post_at >= now]
    group, accounts, peers = engage_today(today)

    def delta(k: str) -> str:
        if k not in nums:
            return "?"
        d = nums[k] - prev.get(k, nums[k])
        return f"{nums[k]} ({'+' if d >= 0 else ''}{d})" if prev else str(nums[k])

    lines = [f"☀️ AZMIN daily brief · {now:%a %d %b}", ""]
    lines += [f"📊 Followers {delta('followers')} · following {delta('following')} · posts {delta('posts')}"]
    if reel:
        lines += [f"🎬 Latest reel ({reel['posted']}): {reel['views']} views · reach {reel['reach']} · avg watch "
                  f"{reel['watch']} s · skip {reel['skip']} · shares {reel['shares']}"]
    lines += ["", "📅 Today:"]
    lines += [f"• {i.post_at:%H:%M} {i.data.get('type', 'post')} {i.id}: {i.status}" for i in todays] or ["• no post today (stories + engagement only)"]
    lines += ["", "🔜 Next 3 days:"]
    lines += [f"• {i.post_at:%a %H:%M} {i.data.get('type', 'post')} {i.id}: {i.status}" for i in upcoming] or ["• nothing queued yet: ask Claude Code \"write the next reel\""]
    if waiting:
        lines += ["", "⏳ Waiting for your ✅ in Telegram: " + ", ".join(i.id for i in waiting)]
    lines += ["", f"💬 Engagement group today: {group or '?'}", "   " + ", ".join(accounts + peers)]
    lines += ["", "✅ Your to-do (about 25 min):",
              "1. Chrome → Claude extension → type: azmin-daily (it prepares comments, replies and follows)",
              "2. Press Post / Follow yourself on what it prepared",
              "3. Reply to new comments on our posts (it drafts them)",
              "4. 1 story (it suggests one)"]
    if waiting:
        lines.append("5. Tap ✅ on the Telegram previews above")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-telegram", action="store_true")
    args = ap.parse_args()
    now = datetime.now(DUBAI)
    text = build(now)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{now:%Y-%m-%d}.md").write_text(text)
    (OUT / "today.md").write_text(text)
    print(text)
    token, chat = os.environ.get("TELEGRAM_BOT_TOKEN", ""), os.environ.get("TELEGRAM_CHAT_ID", "")
    if token and chat and not args.no_telegram:
        telegram.send_message(token, chat, text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
