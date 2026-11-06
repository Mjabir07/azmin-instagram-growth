# ReplyKaro setup (comment keyword -> DM, with Follow-Gate)

**Why:** ReplyKaro uses Meta's official Instagram API. Its **Follow-Gate** (send the link only after the person
follows) works, while our own app can't do that yet because it's still in development mode. The free plan
("Free Starter": 1 account, 3 active automations, 1,000 DMs a month) is enough for now.
Source: replykaro.com/pricing, checked 6 Nov 2026.

**Order (nobody gets two DMs):**
1. Jabir signs in to replykaro.com **with Instagram** himself (@azmin_digital, Free Starter, no card).
2. Claude in Chrome creates the automations below (paste the prompt).
3. Test: comment DEMO from another account on one of our reels and check the DM arrives.
4. Tell Claude Code "ReplyKaro live". It sets `mode: "off"` in `config/comment-dm.yaml`, so our own bot stops answering
   the same comments.

---

## Paste this into the Claude side panel (Chrome, after you're signed in to replykaro.com)

```
You are setting up comment -> DM automations in ReplyKaro (replykaro.com) for the Instagram account @azmin_digital.
Jabir is already signed in. Work step by step and tell me what you see.

HARD LIMITS (never break these):
- Stay on the FREE plan. Never click Upgrade, buy, start a trial that needs a card, or enter any payment details.
  If something is only on a paid plan, skip it and tell me.
- Never turn on lead collection (no name, email or phone questions), broadcasts, AI replies or Fan Mode.
- Never change the Instagram account, password or permissions. If ReplyKaro asks to log in again or reconnect, STOP and ask me.
- Only create the 2 automations below. Don't delete or change anything else.
- Copy the DM texts exactly (no prices, no offers).

AUTOMATION 1 - keyword DEMO
- Type: comment -> DM on Instagram posts/reels. Trigger: "Any post or reel" (if the free plan only allows one post,
  choose the newest reel and tell me which one).
- Keywords: DEMO, demo, demos (match even if the comment has other words).
- Public comment reply (if available): Sent! Check your DMs 📩 (or Message requests)
- Follow-Gate: ON. Nudge text for people who don't follow yet:
  Hi! 👋 Your live website demos are ready. Follow @azmin_digital first, then tap the button and they're yours 📩
- DM (sent to followers / after the follow check):
  Hi! 👋 As promised: our live website demos (open them on your phone and scroll)

  🔗 https://work.azmindigital.com

  ➕ Follow @azmin_digital for a new one every week.
  What are you working on at the moment? 🙂
- If there's a link button option, use button text "Open the demos" with the same link.

AUTOMATION 2 - keyword SWING
- Same type. Trigger: "Any post or reel" (if only one post is allowed: the pendulum reel "Want this for your brand?",
  which goes live Sat 7 Nov 12:30 Dubai; if it isn't live yet, tell me and stop here for this one).
- Keywords: SWING, swing.
- Public comment reply: Done ✅ Check your DMs (or Message requests) 📩
- Follow-Gate: ON. Nudge text:
  Hi! 👋 Your free pendulum reel guide is ready. Follow @azmin_digital first, then tap the button and it's yours 📩
- DM:
  Hi! 👋 As promised: how to make the pendulum reel for your brand (free guide)

  🔗 https://drive.google.com/file/d/1kxBU4W_zIfnLEPbumyhVefWQTi8bacAF/view?usp=sharing

  ➕ Follow @azmin_digital for a new one every week.
  What are you working on at the moment? 🙂
- Button text if available: "Get the guide".

Turn both automations ON. Then report: a table with automation | trigger (which posts) | keywords | Follow-Gate on/off |
status, plus anything you skipped because it needed a paid plan.
```

---

## After it's live

- **Test** from another account (or ask a friend): comment `DEMO` on a reel, check the public reply and the DM.
- Tell Claude Code **"ReplyKaro live"** so it turns our own comment -> DM off (`mode: "off"`).
- The free plan has 3 automation slots: 2 used here, 1 left for the next free guide (for example GOOGLE or REPLY).
- Free plan limit: 1,000 DMs a month. ReplyKaro's paid plans start at ₹99 / $3 a month (their pricing page); ask Jabir
  before any upgrade.
