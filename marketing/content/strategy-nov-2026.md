# Instagram strategy from November 2026 (proposal, 29 Oct)

Made with the `ig-audit`, `ig-profile` and `ig-plan` skills, from the real numbers in
`marketing/insights/2026-10-29.md` (read-only snapshot of the last 10 posts).

## 1. What the numbers say

| | |
|---|---|
| Followers | 0 (following 0) |
| Reach, last 28 days | 764 accounts, 99.9% non-followers |
| Median views per post | 3.5 |
| Likes, saves, shares, follows on all 10 posts | 0 |

| Post | Views | Avg watch | Skip rate |
|---|---|---|---|
| Ep 2 CODE (27 Oct) | 111 | 1.2 s | 95% |
| Ep 1 SKILL (26 Oct) | 0 (reach 8) | 4.0 s | 100% |
| "My Instagram page is enough" (20 Oct) | 15 | **8.9 s** | 82% |
| AI for small business (18 Oct) | 5 | 6.3 s | 50% |

**Findings** (10 posts is too few for patterns, so confidence is low, except for finding 1):
1. **It's a hook problem first.** Instagram did show Ep 2 to about 100 new people, and 95% swiped away in the
   first second (average watch 1.2 s). The first frame talked about us ("Every reel on this page is made with
   code"), not about the viewer. Nothing downstream matters until the first 2 seconds hold.
2. **The page talks to three audiences at once:** creators learning AI tools (Yara series), UAE small businesses
   (AED 999 posts), premium property and car brands (the playbook docs). A stranger can't tell who it's for, so
   nobody follows.
3. The two posts that held attention longest (8.9 s and 6.3 s) both spoke to **a UAE business owner's own
   problem**. n=2, so this is a lead, not proof.

## 2. The AED 999 offer: does it work?

The ad test was AED 200 (4 days × AED 50) and brought 4 chats, none of them serious. That's about AED 50 per chat
and zero real leads. It's a small test, but it points the same way as the organic numbers:
- A price-first message attracts price-shoppers, who ask "how much" and then go quiet.
- Strangers don't buy from a page with 0 followers and no proof, at any price.

**Recommendation:** stop advertising the price. Keep the Starter Combo for people who already trust you
(referrals, people who come through the free guides), and show the price only in a private chat, after the
licence (section 3). Revisit ads later with proof-led creatives, not price-led ones.

## 3. Freelance, not registered yet: keep it legally safe

Jabir is a freelancer and the business is not registered yet. Until it is:
- **Organic only.** No paid ads.
- **No prices, no offers, no "agency" or "company" claims** on Instagram. We teach and help for free.
- Calls to action are **follow + comment WORD for a free guide**. Nothing is sold in posts, captions or DMs.
- Profile category: "Digital creator", not "Software company".
- Real client work is shown only with that client's OK.

In the UAE, doing paid work for clients normally needs a trade licence or a freelance permit. Please check the
official options (government and free-zone freelance permits) before taking paid work. This is not legal advice.
The same care applies to azmindigital.com, which shows prices and services.

## 4. The new direction

**Who it's for:** UAE small business owners (shops, salons, restaurants, clinics, trades) who want more customers
and less busywork, and are curious about AI.

**What we're known for (3 themes):**
1. **AI that saves a business owner time:** WhatsApp replies, review replies, captions, quotes.
2. **Getting found online:** Google Business Profile, a simple website, WhatsApp Business setup.
3. **Honest opinions:** what's worth it and what's hype ("My Instagram page is enough", "Do you need an app?").

**Yara stays** as the presenter: always labelled as AI, and that suits an AI-tips page. The reel engine, look,
Telegram ✅ flow and comment → guide DM all stay the same. The series name changes from "AI Tools with Yara" to
**"AI for your business, with Yara"**. Final call on the old series after the Fri 31 Oct check (section 8).

**Hook rules for every reel** (from `ig-reel`):
- Frame 1 shows the viewer's problem or result in big text, with motion. No logo, no intro, nothing about us.
- The spoken hook is done by 1.5 s.
- 20 to 35 s for now. Shorter reels are easier to finish while the account has no followers.
- Targets for the next 2 weeks: skip rate under 70%, average watch over 5 s.

**Cadence:** 4 posts a week (3 reels + 1 carousel), stories most days, and a 20-minute engagement round daily.
Time: 7:30 PM Dubai on weekdays, 12:30 PM at weekends. The hour matters far less than the first 2 seconds.

## 5. First week (Mon 2 to Sun 8 Nov)

| Day | Post | Type | Hook formula | Angle | Comment word |
|---|---|---|---|---|---|
| Fri 30 Oct to Sun 1 Nov | profile fixes, stories, engagement round | | | | |
| Mon 2 Nov | Reel | Teach | #10 If This, Then Watch | "If customers ask you the same 5 questions on WhatsApp every day, this free setup answers them for you" (WhatsApp Business quick replies + greeting message) | REPLY |
| Tue 3 Nov | stories + engage | | | poll: "How many WhatsApp messages a day do you answer?" | |
| Wed 4 Nov | Reel | Opinion | #12 The Objection | "'My Instagram page is enough.' Fine. Here's what it can't do for you." (remake of our best-holding post) | GOOGLE |
| Thu 5 Nov | Carousel | Teach | #11 Numbered With A Favourite | "5 things to fix on your Google Business Profile today. Number 4 is the one nobody does." | GOOGLE |
| Fri 6 Nov | stories + engage | | | question box: "What's one task you'd love AI to do for your business?" | |
| Sat 7 Nov 12:30 | Reel | Teach | #5 Time Collapse | "Replying to Google reviews used to take me 30 minutes. Now it takes 2." (the exact AI prompt, on screen) | REVIEW |
| Sun 8 Nov | stories only | | | | |

Each comment word needs a free guide PDF in `config/comment-dm.yaml` before its reel goes out (REPLY, GOOGLE,
REVIEW), with no prices in them. Every post goes through `ig-caption` + `ig-human`, then Telegram ✅.

## 6. Profile fixes (ig-profile, do these first, about 10 minutes)

Score today: **43/100** (`docs/instagram/profile-score.md`).

1. **Name field** (pick one): `Azmin Digital | AI tips UAE` · `Azmin | AI for small business` ·
   `Azmin Digital | AI & business`
2. **Bio:**
   ```
   Simple AI and online tips for UAE small businesses 🇦🇪
   Presented by Yara, our AI host
   Comment the word on any reel for the free guide
   ```
3. **Category:** Digital creator. Remove "Software Company".
4. **Archive** (don't delete) the "AED 999 starter combo" post.
5. **Pin** "My Instagram page is enough" now. Pin the best two new reels after week 1.
6. **Highlights** from stories as they happen: `Free guides` · `AI tips` · `Google` · `About Yara`.
7. **Follow 10 to 20 accounts** (section 7). An account that follows nobody looks like a bot.

Expected after the fixes: about 65/100. The rest comes from posting, stories and replies, not rewrites.

## 7. Daily engagement round (20 minutes, before posting)

Jabir picks the accounts himself; the `ig-comment` skill drafts the comments. Never pitch in a comment.
- **5 reach:** big UAE business, startup and SME pages and Dubai business news pages, where a good early
  comment is seen by thousands.
- **3 peers:** UAE creators of a similar size posting about AI, marketing or small business.
- **2 buyers:** local businesses you'd love as clients one day (cafés, salons, clinics). Comment for weeks, no DMs.

## 8. How we measure

- Every Monday: run the **insights** workflow (Actions → insights → Run). It saves
  `marketing/insights/<date>.md`, and `ig-audit` reads it.
- Watch, in this order: skip rate → average watch → sends per reach → follows per reach → followers.
- **Fri 31 Oct:** Ep 2 reaches 72 hours. Send screenshots of Ep 1 and Ep 2 Insights from the app (the
  retention graph and "hold at 3 s" aren't in the API). That closes the old series audit.
- Check-in after 2 weeks (Mon 16 Nov): keep, change or drop each theme based on the numbers.
