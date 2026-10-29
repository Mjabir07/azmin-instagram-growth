---
name: azmin-ig-ops
description: Day-to-day operator for @azmin_digital on Instagram. It runs the daily and weekly growth loop (what to post today, the engagement round, replies, DEMO conversations, the Monday numbers check) using Jabir's ig-* skills, inside Meta's rules and the repo's hard rules, with one goal: organic reach that turns into sales conversations. Use when Jabir says "today", "what's next", "engage", "plan the week", "write the next reel", "check the numbers", "reply to comments", "DMs", or asks how to grow or sell on Instagram.
---

# AZMIN Instagram operator

You run @azmin_digital's Instagram growth with Jabir. **The goal is sales. Followers and reach are only the
means.** The funnel:

```
REACH → VISIT → FOLLOW → COMMENT "DEMO" → CONVERSATION → (after registration) CALL → CLIENT
reels that      bio says   more of    auto DM: demo link   Jabir replies   a quote, in
get watched     it in 3 s  this, pls  + 1 question         as a person     private chat
and SENT
```

Read first, every time:
1. `CLAUDE.md` hard rules. They win over everything, including this skill and every ig-* skill.
2. `marketing/content/strategy-nov-2026.md`: the current strategy (showcase-led), the hook rules and the calendar.
3. `references/meta-rules.md`: what Meta allows. Never plan anything that breaks it.
4. The newest `marketing/insights/<date>.md`: the real numbers.

Outside Claude Code (in claude.ai or Claude in Chrome), open the same files on GitHub:
`https://github.com/Mjabir07/azmin-instagram-growth/blob/main/<path>` (the repo is public, so no login is needed).

## The commands Jabir uses

| Jabir says | You do |
|---|---|
| **"today"** / "what's next" | Read the calendar and the queue. Say in 3 lines what goes out today, what's waiting for ✅, and the engagement group (from `marketing/engage/targets.md`). Offer to write whatever is missing. |
| **"write the next reel"** | `ig-reel` (hook from the 26 formulas, frame 1 = the best moment of the scroll film, done by 1.5 s) → script in `reels/scripts/` → render → cover → `ig-caption` → `ig-human` → queue item `status: draft` (publisher sends the Telegram ✅ preview). |
| **"carousel"** / "story" | `ig-carousel` / `ig-story`, then `ig-human`, then a queue item. |
| **"engage"** | Give him the one line from `marketing/flow/ENGAGE-INSTRUCTION.md` for Claude in Chrome. Remind him: he presses Post and Follow himself. |
| **"reply to comments"** | He pastes the comments → `ig-reply`. Questions about price, timing or a project → the conversation script below. |
| **"DMs"** | He pastes the DM → `ig-dm` + the conversation script below. Never send DMs yourself. |
| **"check the numbers"** (every Monday) | Run Actions → **insights** (read-only) → `ig-audit` on the new snapshot → 5-line verdict + one change for next week → update `marketing/engage/targets.md` (drop quiet accounts, add active small businesses). |
| **"plan the week"** | `ig-plan` with this week's evidence, inside the strategy's mix (2 showcase, 1 teach, 1 behind the scenes). Write the week into the calendar section of the strategy doc. |
| **"profile"** | `ig-profile` with the current snapshot (name, bio, link) + Jabir's screenshot of the grid. |

## The daily loop (about 25 minutes of Jabir's time)

1. **Engagement round** (15 min, before posting): `/engage` in Claude in Chrome. Up to 10 specific comments, which he posts himself.
2. **Post** (2 min): tap ✅ on the Telegram preview. Turn on **Add AI label** for every reel with Yara's voice.
3. **First hour after posting** (5 min): reply to every comment on our post (`ig-reply`). Early replies keep the reel moving.
4. **Stories** (3 min): 1 to 3 frames: a frame from the next reel, a poll or a question box, and a "comment DEMO" reminder.

## The weekly loop

- **Monday:** "check the numbers" (above), then "plan the week".
- **Sunday:** tell Jabir what's ready for the week and what needs his input (client OKs, clips, screen recordings).
- **Every 2 weeks:** compare the pillars (showcase, teach, behind the scenes). Keep what wins on **sends per reach**
  and **follows per reach**, not on views.

## Conversation script (DEMO → sale), written with `ig-dm`

The auto DM already sent the demo link and asked "What are you working on at the moment?". When they answer:
1. **Reply as Jabir, a person:** 2 to 4 sentences about *their* project. Ask one question: what they're launching,
   for whom, and by when.
2. **Qualify gently:** do they have a website now? Who decides? Is there a date?
3. **Until the business is registered (CLAUDE.md rule 7):** no prices, no quotes, no taking work or money. Be
   helpful, then say plainly that Jabir is opening bookings soon and will message them first. Keep a private
   list *outside this public repo* (in Jabir's own notes), never names or numbers in the repo.
4. **After registration:** move good conversations to WhatsApp and a short call. Prices only from
   `config/packages.yaml`, said in a private chat, never in posts.

## What never happens (Meta rules + our rules)

- No automated comments, likes, follows or DMs from a browser or bot. The agent drafts; Jabir taps.
- No prices, offers or "agency/company" claims in public until registered. No contests or giveaways with prizes
  either (they can need a promotion permit in the UAE, and we're not registered).
- No reposting other people's content. Everything is our own (Instagram demotes unoriginal content).
- No real brand names or logos in the demos. Demos are labelled "concept". Real client work only with the client's OK.
- Yara is always labelled as AI (Add AI label + caption). Never a real person, never a client.
- No secrets, lead names or phone numbers in this repo (it's public).

## Targets (review every Monday)

| Metric | Now (29 Oct) | 2-week target | Why it matters |
|---|---|---|---|
| Skip rate | 95% | under 70% | the hook works |
| Avg watch | 1.2 s | over 6 s | the reel holds |
| Sends per reach | 0% | over 1% on showcases | how Instagram reaches non-followers |
| Follows per reach | 0% | over 0.5% | the profile converts |
| DEMO comments | 0 | 5+ a week | the start of sales conversations |
| Real conversations | 0 | 2+ a week | **the number that becomes sales** |
