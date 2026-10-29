from datetime import datetime

from agent.social import insights
from agent.social.queue import DUBAI

NOW = datetime(2026, 10, 29, 12, 0, tzinfo=DUBAI)


class FakeMeta:
    def __init__(self):
        self.calls = []

    def call(self, method, path, token=None, **params):
        assert method == "GET", "insights must be read-only"
        self.calls.append((path, params))
        if path == "ig":
            return {"username": "azmin_digital", "followers_count": 12, "follows_count": 0, "media_count": 2,
                    "name": "Azmin", "biography": "line 1\nline 2", "website": "https://azmindigital.com"}
        if path == "ig/media":
            return {"data": [
                {"id": "r1", "caption": "Ep 2 hook\nmore", "media_product_type": "REELS", "media_type": "VIDEO",
                 "timestamp": "2026-10-27T15:30:00+0000", "permalink": "https://ig/r1"},
                {"id": "p1", "caption": "Carousel", "media_product_type": "FEED", "media_type": "CAROUSEL_ALBUM",
                 "timestamp": "2026-10-23T08:30:00+0000", "permalink": "https://ig/p1"}]}
        if path == "ig/insights":
            return {"data": [{"total_value": {"breakdowns": [{"results": [
                {"dimension_values": ["FOLLOWER"], "value": 20}, {"dimension_values": ["NON_FOLLOWER"], "value": 80}]}]}}]}
        media_id, metric = path.split("/")[0], params["metric"]
        if media_id == "p1" and metric.startswith(("ig_reels", "reels_")):
            raise RuntimeError("metric not supported for this media")
        value = {"views": 400 if media_id == "r1" else 100, "reach": 200, "shares": 10, "follows": 4,
                 "ig_reels_avg_watch_time": 7500, "reels_skip_rate": 55}.get(metric, 1)
        return {"data": [{"values": [{"value": value}]}]}


def test_snapshot_report():
    text = insights.report(*insights.collect(FakeMeta(), "ig", 30, NOW), NOW)
    assert "@azmin_digital · 12 followers" in text
    assert "non-followers 80.0%" in text
    assert "Median views: 250" in text
    reel = next(line for line in text.splitlines() if "Ep 2 hook" in line)
    assert "1.6x" in reel and "7.5" in reel and "55%" in reel and "5.0%" in reel and "2.0%" in reel
    carousel = next(line for line in text.splitlines() if "Carousel" in line)
    assert "0.4x" in carousel  # unsupported reel metrics are skipped, not fatal
