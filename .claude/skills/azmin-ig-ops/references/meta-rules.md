# Meta and Instagram rules we work inside (checked 29 Oct 2026)

Mostly from Meta's own pages and creator blog. Where only third-party sources were found, it says so. Re-check
every few months, because Meta changes these often.

## 1. What makes Instagram show a reel to new people
- The main signals named by Instagram's head, Adam Mosseri: **watch time, likes per reach and sends per reach**.
  Sends (shares by DM) weigh most for reaching **non-followers**; likes weigh more for followers.
  (Third-party summaries: Buffer, eClincher.)
- Reels are the main way to reach people who don't follow us. Carousels deepen trust with people who already do.
- **Original content only.** Since April 2026 Instagram can remove accounts that mostly repost other people's work
  from recommendations (Explore, Reels, suggested posts). Adding a watermark, border or credit doesn't make a repost
  original. Our own reels, demos and screen recordings are original. (Instagram creators blog: "Rewarding original
  creators on Instagram".)
- **Trial Reels** (when the account qualifies; third-party guides say about 1,000+ followers): a reel is shown only to
  non-followers first, so a hook can be tested without the grid seeing it.

## 2. Automation: what's allowed and what isn't
| Allowed | Not allowed |
|---|---|
| Publishing our own posts through the official Instagram API (our publisher) | Bots or browser agents that like, comment, follow or DM by themselves |
| **Private replies** through the official API: one DM per comment, to someone who commented on our post (our comment → DM) | Bulk or repeated identical comments, follow/unfollow loops |
| Reading our own insights through the API (our insights workflow) | Scraping other accounts' data at scale |
| An agent that *drafts* comments and opens the tabs, with Jabir pressing Post and Follow | Buying followers, likes or engagement pods |

- Instagram's terms forbid inauthentic activity and automated engagement. Limits aren't published and depend on the
  account's age and history, which is why our routine caps itself at 10 comments a day and stops on any warning.
- API publishing cap: currently 50 to 100 posts per 24 hours (sources differ). We post once a day, far below it.
- Private replies: one per comment. Third-party sources say the window is up to 7 days after the comment, and our
  config uses 7 (`lookback_days`). After someone writes to us, normal messaging is limited to a 24-hour window.
  The follow gate (a second DM) is blocked while the Meta app is in development mode, so it stays off.

## 3. AI disclosure
- Meta requires the **AI info** label on photorealistic video or **realistic-sounding audio** made or changed with
  AI, and gives "a reel narrated with a realistic AI voiceover" as an example. **So every reel with Yara's voice
  gets "Add AI label".** Meta can also apply the label itself, and may penalise posts that hide it.
- Yara is presented as AI in captions too (CLAUDE.md rule 5).

## 4. Selling, contests and the law (UAE, freelance not registered)
- Until the business is registered: no prices, offers or "agency/company" claims in public, and no paid work
  (CLAUDE.md rule 7). Helpful content and free guides are fine.
- Contests and giveaways with prizes: Instagram requires official rules and a statement that Instagram isn't
  involved, and in the UAE a prize promotion can need a permit. **Not now.**
- Real estate content: property advertising in Dubai has its own rules (RERA). Our demos are concept websites,
  not property ads: no real projects, prices or developer names.

## Sources
- Instagram ranking signals: https://buffer.com/library/instagram-algorithm/ ·
  https://www.eclincher.com/articles/how-the-instagram-algorithm-works-in-2026
- Original content: https://creators.instagram.com/blog/rewarding-original-creators-on-instagram ·
  https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/
- Trial Reels: https://techcrunch.com/2024/12/10/instagram-rolls-out-trial-reels-that-arent-shown-to-a-creators-followers
- Publishing limit: https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/content_publishing_limit
- Private replies: https://developers.facebook.com/documentation/business-messaging/instagram-messaging/features/private-replies
- AI labels: https://www.axios.com/2024/02/06/meta-ai-labeling-fix-oversight-board · https://www.gradually.ai/en/instagram-ai-label/
- Automation risk (third party): https://zorcha.com/blogs/13-best-practices-to-avoid-getting-suspended-on-instagram-in-2026/
