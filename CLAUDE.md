# AZMIN DIGITAL Instagram growth: project brief for Claude Code

## What this repo is
Everything for growing **@azmin_digital** on Instagram (and the Facebook Page it cross-posts to):
strategy, the "AI Tools with Yara" series, reels, guides, carousels and stories, posting with Telegram ✅
approval, and comment → DM guides.

**Not here:** Meta ads (diagnose, health check, 09:00/14:00/20:00 reports, ad launches). They live in
`Mjabir07/azmin-digital-ads-agent`. Its ads code is never changed from here, and its workflows only change
with Jabir's OK. Jabir's website is `Mjabir07/azmin-digital-portfolio` (private, Cloudflare): never push
automation there, because every push rebuilds the live site. We only copied its `docs/instagram/` files.

## The owner
- Jabir (Dubai, Asia/Dubai) is **new to coding**. Explain each step in plain English, one step at a time.
- **Cloud-only:** never ask him to run commands on his PC. Work in the session, GitHub's web UI and Actions.
- Ask before anything that installs software, spends money, or posts/changes anything live.
- Every change: branch `feature/…`, `fix/…` or `content/…` → test → PR to `main`. Jabir said
  "merge and pull all, take care from your end": merge your own PRs once CI is green.

## Hard rules (never break these)
1. **Nothing is posted without Jabir's ✅ in Telegram.** The posting switch is `config/publishing.yaml`
   `live:` (or repo variable `PUBLISH_LIVE`). While it is off, publish and comment → DM only report.
2. **Prices and service claims only from `config/packages.yaml`.** Never invent them.
3. **Secrets only in GitHub Secrets / Cloudflare secrets.** Never in code, logs, commits or chat.
4. **This repo is PUBLIC.** Lead names and phone numbers never go in it.
5. **Yara is an AI presenter.** Always honest about that; never presented as a real person or a client.
6. Comment → DM sends only the fixed texts in `config/comment-dm.yaml`: no AI-written DMs, no prices.
7. **Freelance, not registered yet (Jabir 29 Oct): organic only.** No paid ads, and no prices, offers, or
   "agency"/"company" claims in posts, captions, guides or DMs. Calls to action = follow + comment WORD for a free
   guide. Real client work only with that client's OK. Until the business is registered, nothing is sold on Instagram.

## How it works
- `marketing/queue/*.yaml`: one file per post. Status: draft → pending (preview sent) → approved (✅) → posted.
- `agent/social/`: `queue.py`, `approvals.py` (Telegram previews with ✅/❌), `publish.py` (IG Reels/posts/
  stories + FB Page; media served from this public repo via jsDelivr/raw, using `$GITHUB_REPOSITORY`),
  `comment_dm.py` (keyword comment → private-reply DM with the guide PDF), `cleanup.py` (deletes media of
  posted items), `meta_check.py` (read-only connection test).
- `agent/media/collect.py`: Telegram ✅ taps and clips → `media/inbox/<caption>.mp4`.
- `agent/notify/telegram.py`, `agent/voice/tts.py` (Kokoro-82M, `uv` group `voice`),
  `agent/creatives/guide.py` (HTML → A4 PDF guide).
- `reels/` (Remotion 4): `src/YaraEpisode.tsx` = shared episode engine (`makeEpisode`), one file per episode in
  `src/episodes/`, `src/YaraThumb.tsx` = covers, `public/sfx` = our own beat + SFX, `scripts/*.yaml`.
  Render in a cloud session:
  `npx remotion render src/index.ts YaraEp02 out.mp4 --codec=h264 --crf=19 --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell`
- `cloudflare/telegram-worker.js`: Telegram webhook (instant ✅ taps, clips) + 5-min cron → GitHub dispatch to
  `GH_REPO`. One bot = one webhook = one repo.
- Accounts: `config/accounts.yaml` (Page 1289218264267511, IG 17841444179729405 @azmin_digital, app in dev mode).
- Strategy: `docs/instagram/` (growth playbook, profile score, voice), `marketing/content/yara-ai-series.md`.

## Skills
Jabir's `ig-*` skills (ig-plan, ig-reel, ig-caption, ig-carousel, ig-story, ig-dm, ig-reply, ig-viral, ig-audit,
ig-profile, ig-human, ig-comment, ig-repurpose) are on his Claude account: use them. Run `ig-human` on any
caption, script, reply or DM before showing it. Repo skills in `.claude/skills/` (remotion-best-practices,
playwright-recording, ffmpeg, social, find-skills, text-to-speech, azmin-brand, social-strategy, trend-scout).
**Day-to-day operator: `.claude/skills/azmin-ig-ops`** ("today", "engage", "write the next reel",
"check the numbers"; Meta rules in its `references/meta-rules.md`). The hard rules above always win over any skill.

## "AI Tools with Yara" series rules (for when it continues)
- English, Yara presents. Daily reel **7:30 PM Dubai** (Sat/Sun 12:30 PM). Normal speed: voice 1.1, ~40–47 s.
- Premium AZMIN Editorial look: cream `#F4F1EA`, ink, navy, blue `#0062F5`, cyan `#00D2E2`;
  Inter Tight + Instrument Serif italic.
- Every episode asks **"Follow @azmin_digital + Comment WORD"**: spoken, on screen and in the caption
  (`tests/test_series_cta.py`), and every WORD has a guide PDF in `config/comment-dm.yaml`.
- Each cover uses a frame of that day's Yara clip (different outfit/place/expression).
- Daily Flow clips: `marketing/flow/` (50 free credits/day), sent to the Telegram bot as `D0x-H` / `D0x-E`.

## Strategy (v2 proposal 29 Oct, waiting for Jabir's OK)
`marketing/content/strategy-nov-2026.md`: showcase-led. The 4 scroll-film demo sites (Palm Crest Villas, Aurum Tower,
Azmin Cars, Azmin Detailing; always labelled "concept", no real brand names or logos) and real client sites (only
with the client's OK) are the main content, with property and cars as the showcase niches and small-business tips
for reach. Yara narrates (AI, labelled). CTA = comment DEMO → link to work.azmindigital.com, no prices.
Hook rules: frame 1 = the best moment of the scroll film, hook done by 1.5 s, 15-35 s, ask for sends.
Insights: Actions → **insights** (read-only) saves `marketing/insights/<date>.md` for `ig-audit`.

## Status (30 Oct 2026)
- Old series "AI Tools with Yara" is **replaced** (audit 30 Oct: Ep 2 111 views, 100% non-followers, 0 likes, saves,
  shares or follows; Ep 1 12 views, only test comments). Don't make Ep 3.
- New showcase series: SC01 Palm Crest Villas (`reels/src/ShowcaseReel.tsx`, composition `ShowcasePalmCrest`,
  footage recorded from work.azmindigital.com with the demo's price lines hidden) posts Sat 31 Oct 12:30 after ✅.
- Azmin Detailing demo is being re-edited by Jabir (BMW badge): keep it out of the plan until he says it's ready.

## Migration from the ads repo (nothing may post twice)
1. ✅ Scaffold this repo. Publisher here is content-only and **manual-only**: no schedule, no push trigger,
   no Cloudflare dispatch, cleanup has no schedule, posting switch off (`tests/test_migration.py` guards this).
2. ✅ 29 Oct: Secrets added here (`META_ACCESS_TOKEN`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`,
   `TELEGRAM_WEBHOOK_SECRET`, `TELEGRAM_WEBHOOK_URL`). Variable `META_GRAPH_API_VERSION` still to add (code defaults to v24.0).
3. ✅ 29 Oct: dry run with posting off; Telegram preview sent, ✅ tap round trip works; test item removed.
4. ✅ 29 Oct: Cloudflare worker `GH_REPO` = this repo; its `GH_TOKEN` (fine-grained, Cloudflare Secret) covers both
   repos until step 6. Jabir keeps ONE bot (@azmin_digital_bot) for both repos: the ads repo still sends its reports
   with it, but ✅ taps (incl. "activate ads") land here. Organic only for now, so no ad launches.
5. ✅ 29 Oct cutover: ads repo publisher no longer runs comment → DM (Mjabir07/azmin-digital-ads-agent#30). Here:
   posting live (`config/publishing.yaml`), publisher on a 5-min timer + Cloudflare dispatch + queue pushes, weekly
   cleanup, comment → DM live with the same state file (nobody gets a DM twice).
6. Clean the ads repo of content folders (separate PR, Jabir's OK).
