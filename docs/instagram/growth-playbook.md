# Instagram growth playbook: using the Instagram agent skill pack

Source: [Instagram Agent Skill](https://haristiks.vercel.app/resources/instagram-agent-skill-ml) by Jake Schincariol (13 free Claude skills, MIT licence, [GitHub](https://github.com/Jakeschincariol/instagram-agent-skill)). It isn't made by Meta or Anthropic.

## What it is, in one paragraph

A pack of 13 Claude skills that **plan and write** Instagram content: reel scripts with scored hooks, captions, carousels, a profile score out of 100, weekly plans, comment replies, DMs, and audits of past posts. It **never logs in, never posts, and never sends DMs**; you post everything. That matters, because automated posting, commenting and DMing break Instagram's rules and get accounts restricted. The only automation Instagram allows is keyword auto-replies through its own tools, and the pack is built around that.

## Verdict for Azmin Digital

Worth using. We already have the hard part (the product: four demo sites, the 4K motion reels and Yara's voice). What we're missing is the **distribution system**: captions that get found in search, a profile that converts a reel viewer into a follower, a keyword DM that turns interest into a conversation, and a weekly routine. Eight of the 13 skills cover exactly that.

| Skill | What we use it for | Priority |
|---|---|---|
| `/ig-caption` | Caption for every reel: the ask in the first 125 characters, search phrases, up to 5 hashtags | ⭐ Now |
| `/ig-profile` | Score @azmin_digital out of 100 and rewrite the name field, bio, pinned three and highlights | ⭐ Now |
| `/ig-dm` | The reply people get when they DM "WEBSITE" | ⭐ Now |
| `/ig-reel` | Hooks and scripts for new reels (feeds Yara's narration and the Remotion reels) | ⭐ Every reel |
| `/ig-human` | Strip AI-sounding phrases from captions and scripts | ⭐ Every post |
| `/ig-plan` | Weekly plan plus 10 accounts to engage with | Weekly |
| `/ig-reply` | Sort comments and draft replies | Daily, 10 min |
| `/ig-audit` | After 2 weeks: what worked, from Instagram Insights numbers | Every 2 weeks |
| `/ig-viral`, `/ig-repurpose`, `/ig-carousel`, `/ig-story`, `/ig-comment` | Research, carousels from the demos, daily stories, comments on prospects' posts | Later |

## How to install it (your Claude app, free plan works)

Same as when you added the `yara-voice` skill:

1. claude.ai → Settings → Capabilities → turn on **Code execution and file creation**.
2. Open github.com/Jakeschincariol/instagram-agent-skill → **Code → Download ZIP**, unzip it, open the `skills` folder.
3. Zip each skill folder you want, starting with `ig-caption`, `ig-profile`, `ig-dm`, `ig-reel` and `ig-human`.
4. Settings → Capabilities → Skills → **Upload skill**, one zip at a time.
5. Give it our voice: start a chat, paste `docs/instagram/voice.md`, and ask it to save it as your voice file (the skills read it for every draft).

(Claude Code couldn't install it in this cloud session: adding outside code to the skill setup needs your go-ahead. I used the skills' method by hand for everything below instead.)

## How it fits what we've built

```
Idea ─▶ /ig-reel (hook + script) ─▶ Yara's voice (Kokoro) ─▶ Remotion motion reel (4K)
                                                                  │
            /ig-caption + /ig-human ◀──────────────────────────────┘
                     │
                  Post (you) ─▶ people DM "WEBSITE" ─▶ keyword auto-reply (/ig-dm text)
                     │                                        │
                /ig-reply (comments)                 real conversation ─▶ call ─▶ client
                     │
              /ig-audit every 2 weeks ─▶ next /ig-plan
```

---

## Ready now: captions for the four motion reels

Rules applied from `/ig-caption`: the reel already carries the hook, so line 1 is the **ask** (Job A); one ask only; no link in the caption; search phrases written as normal sentences; at most 5 hashtags; one emoji at most.

### S1: Palm Crest Villas

```
DM us WEBSITE and we'll send you the Palm Crest demo, plus what a launch site like this takes to build.

Palm Crest Villas is a concept off-plan launch site we built: a scroll film from the sky into the living room, floor plans that draw themselves, a payment plan buyers can work out, and English and Arabic in one tap.

It's for real estate developers and brokerages in Dubai who want their launch website to sell, not just sit behind a PDF.

Voice: Yara, our AI ambassador.

#DubaiRealEstate #OffPlanDubai #RealEstateMarketing #WebDesignDubai
```
Search phrases: "launch site", "real estate developers", "Dubai". Alt text: *Vertical video of a villa launch website scrolling on a laptop and a phone.*

### S2: Aurum Tower

```
DM us WEBSITE for the Aurum Tower demo and an idea of what a tower launch site like this involves.

Aurum Tower is a concept launch site for a luxury residential tower. The film rises from the street to the 48th floor, buyers pick a floor and see the view and price change, and the payment plan is worked out for them.

Built for property developers and sales teams in the UAE who answer "which floor, which view, what price" all day.

Voice: Yara, our AI ambassador.

#LuxuryRealEstate #DubaiProperty #PropTech #WebDesignDubai
```

### S3: Azmin Cars

```
DM us WEBSITE for the Azmin Cars demo and a look at what a rental site like this would need for your fleet.

Azmin Cars is a concept supercar rental website: the showroom plays as a film while you scroll, the whole fleet is priced up front, and customers book on WhatsApp in under a minute.

Made for car rental companies in Dubai that want bookings, not just enquiries.

Voice: Yara, our AI ambassador.

#CarRentalDubai #DubaiCars #Supercars #WebDesignDubai
```

### S4: Azmin Detailing (hold until the BMW badge is gone)

```
DM us WEBSITE for the Azmin Detailing demo and how a booking site like this would work for your studio.

Azmin Detailing is a concept website for a car detailing studio: it shows the finish before anyone books, builds the package and price live, and books a drop-off slot in two taps.

For detailing and ceramic coating studios in the UAE.

Voice: Yara, our AI ambassador.

#CarDetailing #CeramicCoating #DubaiCars #WebDesignDubai
```

Before posting each one: switch on **Add AI label** (Yara's voice is AI), add trending music at 10–15%, pick a cover where both screens are full.

---

## Ready now: the "WEBSITE" DM

From `/ig-dm`: send the thing **first**, no gate, then one short question.

**Set it up once (free):** Meta Business Suite → Inbox → **Automations** → **+ Create automation** → **Keywords** → keyword `WEBSITE` → reply with the message below. Instagram's own tool, so it's allowed. If your Business Suite doesn't show keyword automations, ManyChat's free plan (an approved Meta partner) does the same.

```
Here it is: work.azmindigital.com

Open it on your phone and scroll, the films play as you go. Palm Crest and Aurum are real estate, Azmin Cars and Azmin Detailing are automotive.

What are you launching or selling this year?
```

When they answer, reply personally (2–4 sentences, about their project, no calendar link in the first reply). Move to WhatsApp +971 56 724 7597 once they ask about price or timing.

---

## Ready now: profile fixes (from `/ig-profile`)

The rubric weights the **name field, the bio's first line and the pinned three** highest, because that's what a stranger arriving from one reel reads in 3 seconds. To score it properly, send me a screenshot of the top of the profile and the first two grid rows.

**Name field** (30 characters, searchable). Pick one:
- `Azmin Digital | Web & AI Dubai`
- `Azmin Digital | Websites Dubai`
- `Azmin Digital | Real Estate Web`

**Bio** (150 characters):
```
Scroll-driven websites that sell property and supercars 🇦🇪
Launch sites · booking systems · AI ambassadors
DM "WEBSITE" for our live demos
```

**Link:** work.azmindigital.com (one door, not a link menu).

**Pinned three**, each doing a different job:
1. **Proof:** S1 Palm Crest motion reel
2. **The offer:** S3 Azmin Cars motion reel (or a carousel "What we build")
3. **Intro:** Reel 1 "Meet Yara"

**Highlights** (4–6, named for buyers' questions): `Real estate` · `Cars` · `How it works` · `Yara` · `Contact`

---

## Two-week plan (from `/ig-plan`)

| Day | Post | Notes |
|---|---|---|
| Sun wk 1 | Reel 1: Meet Yara | Pin as "Intro" |
| Tue wk 1 | **S1 Palm Crest** motion reel | Pin as "Proof" |
| Thu wk 1 | Reel 2: Palm Crest Yara reel, or a carousel of 5 screenshots | Carousel via `/ig-carousel` |
| Sat wk 1 | **S3 Azmin Cars** motion reel | Pin as "Offer" |
| Mon wk 2 | **S2 Aurum Tower** motion reel | |
| Wed wk 2 | Reel 9: 3 things every launch site needs | Save-able tip |
| Fri wk 2 | Reel 10: Your own Yara | Sells the AI ambassador |
| Sun wk 2 | **S4 Detailing** (only after the logo fix) | |

**Daily, 20 minutes, done by you (never automated):**
- Reply to every comment in the first hour after posting (`/ig-reply` drafts them).
- Leave 5 thoughtful comments on posts from the 10 accounts below (`/ig-comment` drafts them).
- Post 1–3 stories: a frame from the next reel, a poll ("PDF or website for your next launch?"), a reply to a DM question (`/ig-story`).

**The 10 accounts to engage with:** pick them yourself from these groups, since prospects are better chosen by you than by a tool: 3 Dubai off-plan developers' marketing accounts, 2 large brokerages, 2 property marketing agencies or influencers, 2 supercar rental companies, 1 detailing studio. Comment on their posts for two weeks **before** any DM. Per `/ig-dm`, a cold DM to a stranger is the lowest-yield use of the same hour.

**Day 14:** paste each post's numbers from Insights (reach, plays, average watch time, shares, saves, DMs) into `/ig-audit`, and plan weeks 3–4 around what worked.

## Hashtags, honestly

Instagram cut hashtags to **5 per post** in December 2025 and says they label a post rather than spread it. Search reads the **caption text**, so the phrases buyers type ("real estate website Dubai", "car rental website") go into normal sentences, which is what the captions above do.
