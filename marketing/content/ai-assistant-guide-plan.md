# AI Business Assistant: paid setup guide, payment link and delivery plan (v1, 24 Nov 2026)

**What we sell:** a branded **AZMIN DIGITAL step-by-step guide**, plus the invite link, to set up and use a free AI assistant
(Instinct: it lives in WhatsApp and other chat apps, per `Instinct-AI-Intro.pptx`) for a small business.
**Who it's for:** Malayali business owners (Kerala + UAE) coming from the reel ("comment LINK / DM").
**The tool is free; the guide is paid.** The price lives only in Razorpay and on the payment page. It never goes in this
public repo, captions or automated DMs (CLAUDE.md rule 7 exception, 24 Nov).

---

## 1. Jabir's decisions first (nothing gets built before these)

| # | Question | Why it matters |
|---|---|---|
| D1 | Do you have an **Indian PAN + Indian bank account** in your name? | Razorpay KYC needs both. Without them: Stripe/Ziina (UAE) or a manual bank/UPI transfer. |
| D2 | Final guide price and whether **UAE buyers** pay in INR by card | International cards must be switched on in Razorpay (separate approval). |
| D3 | **What exactly is included?** Guide PDF + invite link only, or also a 30-min setup call / WhatsApp support for X days? | Sets the value promise and the refund policy. |
| D4 | **Refund policy** (e.g. "full refund within 7 days if the invite link doesn't work for you") | Razorpay asks for it, and it builds trust. |
| D5 | Guide language: Manglish (Malayalam + English tech words) **(recommended)** or English | Matches the ad audience. |
| D6 | Landing page on **guide.azmindigital.com** (new, separate) **(recommended)** or a page inside azmindigital.com | The main site repo (`azmin-digital-portfolio`) rebuilds the live site on every push, so we'd rather not touch it. |
| D7 | Test the lead-finding workflow (section 4, chapter 5) in Instinct **before** we write it | Hard rule: we never promise a feature we haven't seen working. |

---

## 2. The customer journey (one picture)

```
Reel (comment LINK / DM)
  → Jabir replies with the fixed text + brand link  (no price in the DM)
  → guide.azmindigital.com            (what you get, sample pages, FAQ, refund policy, price, "Get the guide")
  → Razorpay Payment Page             (name, WhatsApp number, email → UPI / card / netbanking)
  → Thank-you page                    ("check your email + WhatsApp in 10 minutes")
  → Delivery                          Phase 1: Jabir by hand · Phase 2: automatic email + Telegram alert to Jabir
  → Buyer gets: guide PDF (stamped with their name), invite link, prompt pack, lead sheet template, support WhatsApp
  → Day 2 + Day 7 check-in messages ("did setup work?") → reviews / testimonials (only with their OK)
```

**Brand links (short and easy to say in a reel):**
- **Built 24 Nov:** `azmindigital.com/ai-assistant` (separate Cloudflare Worker; code in the private website repo, branch `feature/ai-assistant-guide`, `workers/ai-assistant-guide/`).
- `guide.azmindigital.com` = the landing page itself.
- Razorpay page custom URL: `pages.razorpay.com/azmin-ai-guide` (or the `rzp.io/...` short link) as a fallback.
- WhatsApp: `wa.me/<number>?text=GUIDE` for people who'd rather pay after talking.

---

## 3. Payments: Razorpay setup (Jabir does the clicks, I write every step)

1. **Sign up** at razorpay.com → business type **"Unregistered / Individual"** (freelancer) → KYC with PAN, Aadhaar
   and bank account. Activation usually needs a live website with **Contact, Terms, Privacy, Refund** pages. I'll make
   these on guide.azmindigital.com first (azmindigital.com already has a privacy policy).
2. **Payment Page** (Dashboard → Payment Pages → Create):
   - Title: "AI Business Assistant – Setup Guide (AZMIN DIGITAL)". Logo, brand colours, a short description and what's included.
   - Fixed amount = D2 price. Customer fields: **Name, Email, WhatsApp number (+country code), Business type**.
   - After payment: redirect to `guide.azmindigital.com/thanks`.
   - Receipt email ON (Razorpay sends it automatically).
3. **International cards:** request activation if D2 = yes.
4. **Webhook** (for Phase 2): event `payment.captured` (plus `payment_link.paid` if we also send one-off links) →
   `https://guide.azmindigital.com/api/razorpay` with a webhook secret (stored as a Cloudflare secret, never in the repo).
5. **One-off links:** for buyers who talk on WhatsApp first, Razorpay **Payment Links** (Dashboard → Payment Links →
   amount, name, phone) send the link by SMS/WhatsApp/email from Razorpay itself.
6. **Costs:** Razorpay charges a percentage per payment (about 2% on domestic payments, more on international cards).
   Check today's rates on razorpay.com/pricing before we set the price. There's no monthly fee on the standard plan.
7. **Tax/legal (check with an accountant):** income from the guide in an Indian account, GST threshold, and your
   UAE visa/freelance status. I can't advise on this. It's a to-do for you.

---

## 4. The guide: what's inside (branded, AZMIN Editorial look, ~24–30 A4 pages)

Made with our own pipeline: HTML → `agent/creatives/guide.py` → PDF, in the AZMIN look (cream #F4F1EA, ink, navy,
blue #0062F5, Inter Tight + Instrument Serif italic). Malayalam headings + English tech words (D5).
**The paid PDF is never committed to this public repo**: its source sits in a private place (section 6).

| Ch | Title | Contents (value) |
|---|---|---|
| 0 | Cover + "how to use this guide" | Buyer's name stamped on every page footer (anti-sharing), version, date, support number |
| 1 | What this AI assistant is (and isn't) | Plain explanation from the deck: lives in WhatsApp, text or voice, asks before sending/paying. Honest limits + "Instinct is a third-party tool; AZMIN is not affiliated" |
| 2 | Get access in 10 minutes | Invite link, step-by-step with **real screenshots** (taken by Jabir, phone numbers masked), first message to send, common errors |
| 3 | Safe setup | Which accounts to connect (email, calendar), permissions explained, **approval before send/pay ON**, what never to share (bank OTPs, passwords) |
| 4 | Daily business use: 30 ready prompts (copy-paste, Malayalam + English) | Customer replies, quotations, supplier price compare, meeting scheduling, payment reminders, proposals/presentations, daily plan, end-of-day summary |
| 5 | **Find clients with Google Maps + AI** (only what D7 confirms works) | ① search Google Maps by area + category (e.g. "restaurants Karama") ② shortlist 10/day in the lead sheet ③ ask the assistant to study each one (website, reviews, what's missing) ④ it drafts a **personal** WhatsApp message + email for each ⑤ **you approve** → email goes out from your inbox ⑥ WhatsApp: a one-click `wa.me` link with the message pre-filled, so you tap Send yourself |
| 6 | Message + email templates | First message, follow-up Day 3, Day 7, "not now" reply, meeting confirmation. Worked examples are labelled **Sample** |
| 7 | Lead sheet template (Google Sheet) | Columns: business, area, link, what we noticed, message sent, reply, next step. Copy link in the guide |
| 8 | Rules that keep your number + email safe | Max ~20 new WhatsApp chats/day, one-to-one only (no bulk tools), stop when asked, unsubscribe line in emails, use public business contact details only, respect Google Maps terms (no scraping tools). Bulk messaging gets WhatsApp numbers banned |
| 9 | 7-day starter plan | Day 1 setup → Day 2 prompts → Day 3 first 10 leads → … Day 7 review |
| 10 | FAQ + troubleshooting | "Invite not working", "it replied wrongly", "Malayalam voice notes?", "is my data safe?" (answers only from the tool's own docs) |
| 11 | Support + what's next | What D3 includes, response hours, refund policy, follow @azmin_digital |

**Bonuses (cheap to make, high perceived value):**
- **Prompt pack** as a separate 2-page PDF.
- Lead sheet template.
- 3 short screen-recorded walkthrough videos (Playwright/phone recording, faceless).
- WhatsApp templates as a `.txt` for quick copy.

**What we must test before writing (D7):** Google Maps research, email sending after approval, calendar booking, and
voice notes in Malayalam. Every claim in the guide has to have a screenshot from Jabir's own test. Anything that
doesn't work goes out, or becomes "do it manually like this".

---

## 5. Messages (fixed texts, no price)

- **Reply to a LINK comment / DM (Jabir by hand, or ReplyKaro):**
  "Hi 👋 Thanks for your interest! AI assistant setup guide-ന്റെ full details ഇവിടെ ഉണ്ട്: azmindigital.com/guide
  എന്തെങ്കിലും സംശയം ഉണ്ടെങ്കിൽ ഇവിടെ ചോദിക്കൂ 🙂"
- **After payment (email + WhatsApp):** thanks + guide link (expires in 7 days, re-send on request) + invite link +
  "start with Chapter 2" + support number.
- **Day 2:** "Setup ശരിയായോ? എന്തെങ്കിലും stuck ആണെങ്കിൽ screenshot അയക്കൂ."
- **Day 7:** "First week എങ്ങനെ ഉണ്ടായിരുന്നു? ഒരു ചെറിയ review തരാമോ? (only if you're happy)"
- **First 10:** keep a count. After 10 sales, close the page or say "next batch" honestly.

---

## 6. Build plan (who does what)

**Phase 1: launch fast, manual delivery (about 2–3 days after D1–D7)**
1. Claude: guide HTML in a **private** repo (new `Mjabir07/azmin-guides`, or Drive) → PDF. Plus landing page, Terms,
   Privacy, Refund and Contact pages on Cloudflare Pages (guide.azmindigital.com) → preview for Jabir's ✅.
2. Jabir: Razorpay sign-up + KYC, then the Payment Page with the fields above (I write a click-by-click checklist).
3. Jabir: Cloudflare dashboard → redirect rule `azmindigital.com/guide` → landing page (I write the exact steps).
4. Delivery by hand: Razorpay app notification → Jabir sends the guide PDF + invite link on WhatsApp/email.
5. Claude: Telegram note to Jabir for every payment? Only in Phase 2. In Phase 1 the Razorpay app shows it.

**Phase 2: automatic delivery (after the first 3–5 sales prove it sells)**
1. A Cloudflare Worker route `/api/razorpay` checks the webhook signature (`X-Razorpay-Signature`, HMAC-SHA256 with the secret).
2. The guide PDF sits in private **Cloudflare R2**. The worker makes a **signed download link valid 7 days**.
3. The email goes through an email API (e.g. Resend, free tier) from `guide@azmindigital.com`: guide link + invite link.
4. A Telegram message to Jabir says: buyer name + business, and a **one-click WhatsApp button** (`wa.me/<buyer>?text=…`
   pre-filled with the welcome message), so Jabir taps once to send it.
5. Buyer data stays in Cloudflare KV/R2 or a private Google Sheet, **never in this public repo** (rule 4).
6. Optional: a stamped PDF per buyer (name in the footer), made by a GitHub Action in the private repo.

**Phase 3: improve**
- Testimonials (with permission), a v2 guide with screenshots from real buyers' questions, and an FAQ from DMs.

---

## 7. Honest-marketing checklist (for the landing page and DMs)
- Say clearly: **the tool is free; you're paying for the guide + invite + support**.
- No income or result promises ("get 10 clients a week" ✗). The examples say **Sample**.
- No tool logo, and no claim that AZMIN made the tool or partners with it.
- Show 2–3 sample pages of the guide on the landing page so people see what they're buying.
- AI label on the reel. The refund policy is visible before payment.
