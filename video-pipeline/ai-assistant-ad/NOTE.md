# AI business assistant ad (24 Nov 2026)

Organic ad for Malayali business owners on @azmin_digital (rule-7 exception, see CLAUDE.md). The AI tool is free; Jabir's
setup guide is paid, and he sends the payment link by hand. **No price anywhere** (video, caption, auto-DM).

- Footage: `src/flow-clips.mp4` (Google Flow, 4 scenes in one 18 s file, audio muted). Upscaled 720×1280 → 1080×1920.
- VO: ElevenLabs `eleven_v4`, voice "Sunaina – Relatable Reels Creator" (8VTILyp3oibFrXwPpZJQ), 1 take (1,657 credits).
  Script as given, line 16 changed to "ഈ AI tool free ആയി ഉപയോഗിക്കാം." 96 s raw → pauses cut to 0.24 s
  (`vo/tighten.py`) → atempo 1.12 → 81.9 s. Word times: Scribe on the take, mapped with `vo/map_words.py` → `words.js`.
- Picture: `reel.html` (14 scenes, transitions, Malayalam word-by-word subtitles) → `render.js` → `picture.mp4`.
- Audio: `audio.py` (own procedural dark bed + `sfx/` from reels/public/sfx, cues in `events.js` → `events.json`) → `mix.sh`
  (VO + ducked music + SFX, two-pass loudnorm −14 LUFS, limiter, TP ≈ −1.7 dB).
- `cutdown.sh` → 45.6 s version (hook | smart solution → features | free | comment LINK → end).

Rebuild:
```
ffmpeg -i src/flow-clips.mp4 -an -vf "scale=1080:1920:flags=lanczos,unsharp=5:5:0.4" -q:v 3 clipframes/c%04d.jpg
python3 vo/tighten.py && ffmpeg -i vo/tight.wav -af atempo=1.12 -ar 48000 vo/final.wav   # vo/take1.wav from take1.mp3
node events.js > events.json && python3 audio.py
DUR=86 node render.js && ffmpeg -framerate 30 -i frames/f%05d.jpg -c:v libx264 -crf 17 -pix_fmt yuv420p -profile:v high picture.mp4
./mix.sh && ./cutdown.sh
```

## Caption (draft)
Business നടത്താൻ ദിവസവും എത്ര മണിക്കൂർ പോകുന്നു? ⏳
Customer replies, quotations, meetings, payment reminders… ഒരു chat app-ൽ നിന്ന് തന്നെ ചെയ്യാൻ സഹായിക്കുന്ന Personal AI Assistant.
Text ആയോ voice ആയോ പറഞ്ഞാൽ മതി. പ്രധാന കാര്യങ്ങൾക്ക് മുമ്പ് നിങ്ങളുടെ approval ചോദിക്കും.
AI tool free ആണ്, monthly subscription വേണ്ട.
Setup guide വേണോ? 👉 Follow @azmin_digital + comment **LINK** അല്ലെങ്കിൽ DM ചെയ്യൂ. ആദ്യത്തെ 10 പേർക്ക് മാത്രം.
#smallbusiness #aitools #keralabusiness

## Replies for likely comments (honest, no price in public)
- "How much?" / "എത്രയാ?" → AI tool free ആണ് 👍 Setup guide-ന്റെ details DM-ൽ അയക്കാം.
- "Free ആണോ?" → Tool free ആണ്, monthly subscription ഇല്ല. Step-by-step setup guide-നെ കുറിച്ച് DM-ൽ പറയാം.
- "Which app?" → Full details guide-ൽ ഉണ്ട്. DM ചെയ്യൂ 🙂
- "Is it safe?" → പ്രധാന കാര്യങ്ങൾ ചെയ്യുന്നതിന് മുമ്പ് assistant നിങ്ങളുടെ approval ചോദിക്കും. Guide-ൽ setup steps clear ആയി ഉണ്ട്.
- "UAE-ലും work ചെയ്യുമോ?" → Guide-ൽ setup details ഉണ്ട്, DM ചെയ്യൂ, നോക്കി പറയാം.

## Posting checklist
- AI info label ON (AI visuals + AI voice; the chat contact avatar is an AI face).
- Cover: frame from S5 ("PERSONAL AI ASSISTANT") or the FREE stamp.
- LINK is **not** in `config/comment-dm.yaml`: the automation must not send prices, so Jabir answers LINK comments/DMs himself.
- Honour "first 10": after 10 people, reply honestly that the spots are full.
