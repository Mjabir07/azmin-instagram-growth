"""Read-only Instagram insights snapshot for ig-audit / ig-profile.

GET requests only: profile basics, the last posts with their insights, and account reach split into
followers vs non-followers. Writes marketing/insights/<date>.md (this repo is public: post metrics only,
never commenter names). Each metric is asked for on its own, because Meta refuses the whole request when
one metric doesn't apply to a media type.
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timedelta
from statistics import median

import yaml

from agent.config import DEFAULT_GRAPH_API_VERSION, ROOT, redact
from agent.social.publish import Meta
from agent.social.queue import DUBAI

OUT = ROOT / "marketing/insights"
MEDIA_METRICS = ["views", "reach", "likes", "comments", "saved", "shares", "follows", "profile_visits",
                 "total_interactions", "ig_reels_avg_watch_time", "ig_reels_video_view_total_time", "reels_skip_rate"]
PROFILE_FIELDS = "username,name,biography,website,followers_count,follows_count,media_count"


def media_insights(meta: Meta, media_id: str) -> dict:
    values = {}
    for m in MEDIA_METRICS:
        try:
            data = meta.call("GET", f"{media_id}/insights", metric=m).get("data") or []
        except RuntimeError:
            continue  # metric not available for this media type
        if data and data[0].get("values"):
            values[m] = data[0]["values"][0].get("value")
    return values


def reach_by_follow_type(meta: Meta, ig_id: str, since: datetime, until: datetime) -> dict:
    """Account reach in the window, split FOLLOWER / NON_FOLLOWER. Empty if Meta won't give the breakdown."""
    try:
        data = meta.call("GET", f"{ig_id}/insights", metric="reach", period="day", metric_type="total_value",
                         breakdown="follow_type", since=int(since.timestamp()), until=int(until.timestamp()))["data"]
        results = data[0]["total_value"]["breakdowns"][0]["results"]
        return {r["dimension_values"][0]: r["value"] for r in results}
    except (RuntimeError, KeyError, IndexError):
        return {}


def ratio(a, b) -> str:
    return f"{a / b * 100:.1f}%" if isinstance(a, (int, float)) and b else "-"


def report(profile: dict, posts: list[dict], split: dict, now: datetime) -> str:
    views = [p["insights"].get("views") for p in posts if isinstance(p["insights"].get("views"), (int, float))]
    med = median(views) if views else 0
    lines = [f"# Instagram insights snapshot · {now:%a %d %b %Y %H:%M} Dubai", "",
             f"@{profile.get('username')} · {profile.get('followers_count')} followers · "
             f"{profile.get('follows_count')} following · {profile.get('media_count')} posts", "",
             f"Name field: {profile.get('name')}", f"Bio: {(profile.get('biography') or '').replace(chr(10), ' / ')}",
             f"Link: {profile.get('website')}", ""]
    if split:
        total = sum(split.values())
        lines += [f"Account reach, last 28 days: {total} · non-followers {ratio(split.get('NON_FOLLOWER', 0), total)}", ""]
    lines += [f"Median views: {med:g}", "",
              "| Posted (Dubai) | Type | First line | Views | Outlier | Reach | Avg watch s | Skip rate | Likes | Comments"
              " | Saves | Shares | Sends/reach | Follows | Follows/reach | Profile visits |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for p in posts:
        i = p["insights"]
        watch = i.get("ig_reels_avg_watch_time")
        first = (p.get("caption") or "").strip().split("\n")[0][:60].replace("|", "/")
        lines.append(" | ".join([
            f"| {p['posted']:%a %d %b %H:%M}", p["type"], first, str(i.get("views", "-")),
            f"{i['views'] / med:.1f}x" if med and isinstance(i.get("views"), (int, float)) else "-",
            str(i.get("reach", "-")), f"{watch / 1000:.1f}" if isinstance(watch, (int, float)) else "-",
            f"{i['reels_skip_rate']}%" if "reels_skip_rate" in i else "-",
            str(i.get("likes", "-")), str(i.get("comments", "-")), str(i.get("saved", "-")), str(i.get("shares", "-")),
            ratio(i.get("shares"), i.get("reach")), str(i.get("follows", "-")), ratio(i.get("follows"), i.get("reach")),
            str(i.get("profile_visits", "-")) + " |"]))
    lines += ["", "Not available from the API (read them in the app, Insights on each reel): hold at 3 seconds,"
              " retention graph, followers vs non-followers per post.", f"Permalinks: {', '.join(p['permalink'] for p in posts)}"]
    return "\n".join(lines) + "\n"


def collect(meta: Meta, ig_id: str, limit: int, now: datetime) -> tuple[dict, list[dict], dict]:
    profile = meta.call("GET", ig_id, fields=PROFILE_FIELDS)
    media = meta.call("GET", f"{ig_id}/media", fields="id,caption,media_type,media_product_type,timestamp,permalink",
                      limit=limit).get("data", [])
    posts = []
    for m in media:
        posted = datetime.strptime(m["timestamp"], "%Y-%m-%dT%H:%M:%S%z").astimezone(DUBAI)
        kind = "reel" if m.get("media_product_type") == "REELS" else m.get("media_type", "").lower()
        posts.append({**m, "posted": posted, "type": kind, "insights": media_insights(meta, m["id"])})
    split = reach_by_follow_type(meta, ig_id, now - timedelta(days=28), now)
    return profile, posts, split


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=30)
    args = ap.parse_args()
    token = os.environ.get("META_ACCESS_TOKEN", "").strip()
    if not token:
        print("META_ACCESS_TOKEN not set.")
        return 1
    accounts = yaml.safe_load((ROOT / "config/accounts.yaml").read_text())["meta"]
    meta = Meta(token, (os.environ.get("META_GRAPH_API_VERSION") or DEFAULT_GRAPH_API_VERSION).strip())
    now = datetime.now(DUBAI)
    try:
        text = report(*collect(meta, accounts["instagram_account_id"], args.limit, now), now)
    except RuntimeError as e:
        print(redact(str(e), [token]))
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{now:%Y-%m-%d}.md").write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
