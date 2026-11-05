---
name: reel-studio
description: Brand-neutral premium reel production for Instagram/TikTok/Shorts (1080×1920). Script → voice-over (ElevenLabs) → word timings → captions (pill or editorial) → canvas motion graphics with transitions → optional talking host with lip-sync → HyperFrames premium blocks → real CC0 sound effects placed by the real-sfx skill and checked with Earshot → −14 LUFS export → self-check → caption, thumbnail and auto-DM hand-over. Use when asked to make, edit or improve a reel, short, promo video, motion-graphics video, thumbnail or caption for any brand that keeps its brand profile in its own repo.
---

# Reel Studio

Brand-neutral. Every brand keeps its own `brand.json` (name, language, colours, voice, host, CTA, rules) in **its own
repository**; read it first and never mix brands. Never put a personal name on screen, in captions or in files – brand
names only.

## Step 1 – brief (ask in short multiple-choice rounds, recommend one option each)
Topic and hook · length (30–45 s) · CTA keyword and the deliverable sent by DM · caption style (pill / editorial) ·
host on/off · music on/off · anything that must not be said. Confirm the script before spending credits.

## Step 2 – produce
1. **Folder:** copy `templates/canvas-reel/` into the brand repo (`video-pipeline/<reel-name>/`); write `brand.js` from
   the brand's `brand.json`.
2. **Hook:** the first 2–3 s must say the benefit + "new/free/premium" and show the best visual at once.
3. **VO:** ElevenLabs `creative_generate_speech`, model `eleven_v4`, the brand's voice id, one tone tag at the start
   (`[casual]` or `[energetic]`), `[short pause]` where needed. 2 takes; tell the owner the credit cost first.
4. **Word timings:** pin the chosen take (`creative_add_flow_asset_node`) → `creative_transcribe_audio` → `words.js`
   (strip tags and punctuation; HILITE = key words). Check the transcript source URL is the chosen take.
5. **Scenes:** `timeline.js` (SC/TR/PUNCH/STICK/LABELS) + `scenes.js`; anchor every animation to `WT('word', n)`.
   One idea per scene, a change every 1–1.5 s. Keep cards inside the safe area (see scenes.js comment).
6. **Style:** default pill captions, or copy `style-editorial.js` over `style.js` (paper bg, mono label, word-by-word
   headline – the current trend look).
7. **Host (optional):** pose images + mouth patches made as in `prompts/host-character-flow.md`;
   `python3 modules/lipsync/mouth_levels.py vo/final.mp3 mouth.js`; include `mouth.js` and `modules/lipsync/host.js`
   with a `window.HOST` config and a pose schedule (change pose every ~1–1.5 s, specific poses on key words).
   Bust size: scale so raised arms stay inside 1080 px.
8. **HyperFrames:** for premium titles/charts/3D see `hyperframes/README.md`; use the real render in the reel.
9. **Previews:** `ONLY=t1,t2,… node render.js` → contact sheet → fix overlaps (text vs cards vs host) before the full
   render. Show the owner a 10–12 s test clip with VO before the full render when the format is new.
10. **Render + music:** `./build.sh` (frames, procedural music, ducking, −14 LUFS).
11. **SFX:** `sound/README.md` – events.json → real-sfx `from_cues` → highpass hits/risers → `mix --plan` → mix →
    `critique` → two-pass loudnorm −14 LUFS. Any SFX count shown on screen must come from the plan.

## Step 3 – self-check
- Contact sheet start/middle/end: no cut-off or overlapping text, captions clear of the host and Instagram UI.
- Export: 1080×1920, 30 fps, H.264 high, yuv420p, AAC 192k, −14 LUFS (±0.5), true peak ≤ −1 dB, < 100 MB.
- Honesty: every number on screen and in the caption must be real (from the tool, an API or the owner); no invented
  clients, results or earnings; say what is paid; say a tool's limit in one line.
- Report what you could NOT verify – Claude cannot hear: ask the owner to listen on headphones (lip-sync, first 3 s,
  the moments real-sfx critique lists).

## Step 4 – hand-over
1. Caption with `prompts/caption-prompt.md` (3 variations, recommend one, pinned comment, alt text).
2. Thumbnail (`FN=thumb node thumb.js`), key text inside the centre 4:5 area.
3. DM text + deliverable (PDF via Drive) + auto-DM setup (`prompts/autodm-chrome.md`; one reel = one tool).
4. Posting checklist: AI label ON for AI visuals/voice, cover set, keyword live, tested from another account.
5. Commit + push in the brand repo; send the mp4, thumbnail and PDF to the owner.
