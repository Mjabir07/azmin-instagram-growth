"""Guards for the move from azmin-digital-ads-agent: nothing posts twice, nothing ads-related lives here."""

import sys

import yaml

from agent.config import ROOT
from agent.social import comment_dm, publish

WORKFLOWS = ROOT / ".github/workflows"


def test_guide_links_point_to_this_repo():
    assert comment_dm.guide_link("marketing/guides/x.pdf").startswith(
        "https://cdn.jsdelivr.net/gh/Mjabir07/azmin-instagram-growth@main/")


def test_posting_switch(monkeypatch, tmp_path):
    monkeypatch.setattr(publish, "ROOT", tmp_path)
    (tmp_path / "config").mkdir()
    cfg = tmp_path / "config/publishing.yaml"
    monkeypatch.delenv("PUBLISH_LIVE", raising=False)
    cfg.write_text("live: false\n")
    assert not publish.posting_live()
    monkeypatch.setenv("PUBLISH_LIVE", "true")
    assert publish.posting_live()
    monkeypatch.delenv("PUBLISH_LIVE")
    cfg.write_text("live: true\n")
    assert publish.posting_live()


def test_comment_dm_is_dry_run_while_posting_is_off(monkeypatch):
    seen = {}

    def fake_run(meta, cfg, accounts, state, now, live):
        seen["live"] = live
        return []

    monkeypatch.setattr(publish, "ROOT", ROOT)
    monkeypatch.setattr(comment_dm, "posting_live", lambda: False)
    monkeypatch.setattr(comment_dm, "run", fake_run)
    monkeypatch.setattr(comment_dm, "save_state", lambda *a: seen.setdefault("saved", True))
    monkeypatch.setenv("META_ACCESS_TOKEN", "t")
    monkeypatch.setattr(sys, "argv", ["comment_dm"])
    assert comment_dm.main() == 0
    assert seen == {"live": False}  # no DMs, no state saved


def test_no_ads_code_or_ads_steps():
    assert not (ROOT / "agent/ads").exists()
    for wf in WORKFLOWS.glob("*.yml"):
        assert "agent.ads" not in wf.read_text(), wf.name


def test_only_tests_and_inbox_start_on_their_own():
    """Until cutover, Telegram/Meta workflows only run when started by hand, so the two repos never both post.
    telegram-inbox only runs when the Cloudflare worker dispatches to this repo (step 4)."""
    for wf in WORKFLOWS.glob("*.yml"):
        on = yaml.safe_load(wf.read_text())[True]  # YAML reads the key `on` as True
        if wf.stem == "tests":
            continue
        if wf.stem == "telegram-inbox":
            assert set(on) == {"repository_dispatch"}
            continue
        assert set(on) == {"workflow_dispatch"}, wf.name


def test_hand_started_publisher_does_not_read_telegram():
    """A manual dry run must not take ✅ taps meant for the ads repo, which still owns the bot until cutover."""
    wf = yaml.safe_load((WORKFLOWS / "publisher.yml").read_text())
    assert wf[True]["workflow_dispatch"]["inputs"]["read_telegram"]["default"] is False
    step = next(s for s in wf["jobs"]["publish"]["steps"] if "agent.media.collect" in s.get("run", ""))
    assert step["if"] == "github.event_name != 'workflow_dispatch' || inputs.read_telegram"
