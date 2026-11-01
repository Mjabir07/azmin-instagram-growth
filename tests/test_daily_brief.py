from datetime import datetime

import yaml

from agent.social import daily_brief, queue
from agent.social.queue import DUBAI

SNAP = """# Instagram insights snapshot · Sun 01 Nov 2026 09:00 Dubai

@azmin_digital · {f} followers · 14 following · 7 posts

| Posted (Dubai) | Type | First line | Views | Outlier | Reach | Avg watch s | Skip rate | Likes | Comments | Saves | Shares | Sends/reach | Follows | Follows/reach | Profile visits |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 31 Oct 12:31 | reel | This is what an off-plan launch page | 240 | 2.0x | 200 | 6.3 | 60% | 3 | 1 | 2 | 4 | 2.0% | 1 | 0.5% | 5 |
"""


def test_brief(tmp_path, monkeypatch):
    ins, q = tmp_path / "insights", tmp_path / "queue"
    ins.mkdir(); q.mkdir()
    (ins / "2026-10-31.md").write_text(SNAP.format(f=1))
    (ins / "2026-11-01.md").write_text(SNAP.format(f=4))
    (q / "a.yaml").write_text(yaml.safe_dump({"id": "sc02-azmin-cars", "type": "reel", "post_at": "2026-11-02 19:30", "status": "approved"}))
    (q / "b.yaml").write_text(yaml.safe_dump({"id": "sc03-no-pdf", "type": "reel", "post_at": "2026-11-04 19:30", "status": "pending"}))
    monkeypatch.setattr(daily_brief, "INSIGHTS", ins)
    monkeypatch.setattr(queue, "QUEUE", q)
    text = daily_brief.build(datetime(2026, 11, 1, 9, 0, tzinfo=DUBAI))
    assert "Followers 4 (+3)" in text
    assert "240 views" in text and "shares 4" in text
    assert "no post today" in text
    assert "Mon 19:30 reel sc02-azmin-cars: approved" in text and "Wed 19:30 reel sc03-no-pdf: pending" in text
    assert "Waiting for your ✅ in Telegram: sc03-no-pdf" in text
    assert "Business + local" in text and "dreamize_" in text  # Sunday rotation + daily peers
