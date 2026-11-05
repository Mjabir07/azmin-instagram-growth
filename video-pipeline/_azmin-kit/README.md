# AZMIN reel kit (reel-studio + Yara)

Everything AZMIN-specific a new reel needs, on top of the brand-neutral `reel-studio` template. AZMIN only:
never copy these files into another brand's repo.

| File | What |
|---|---|
| `brand.js` | generated from `/brand.json` (name, fonts, AZMIN colours) |
| `style.js` | AZMIN Editorial: cream paper, Inter Tight + Instrument Serif italic accents, word-by-word headline |
| `fonts/` | Inter Tight, Instrument Serif italic (+ template fonts) |
| `host/` | Yara: 4 Flow poses aligned to one head position and cut out (`pose1` wave, `pose2` point, `pose3` think, `pose4` explain), mouth patches `mouth_half`/`mouth_wide` colour-matched to the poses |
| `host-config.js` | `window.HOST` (mouthAt, frame, scale, top) + an example pose schedule |
| `host.js` | lip-sync renderer (reel-studio `modules/lipsync/host.js`) |
| `mouth_levels.py` | mouth level per frame from the VO, with `--wide-db` |

## New reel in 6 steps
1. Copy `reel-studio/templates/canvas-reel/` to `video-pipeline/<reel>/`. Then copy this kit over it
   (`cp -r video-pipeline/_azmin-kit/. video-pipeline/<reel>/`) and add the host scripts to `reel.html` after `style.js`:
   `mouth.js`, `host-config.js`, `host.js` (see `video-pipeline/test-yara/reel.html`).
2. VO: ElevenLabs, voice from `brand.json` (Sarah `EXAVITQu4vr4xnSDxMaL`, `eleven_v4`, `[casual]`), 2 takes, show the
   credit estimate first. Download the chosen take to `vo/final.mp3`.
3. Word timings: pin the take → Scribe → `words.js` (strip tags and punctuation; HILITE = key words).
4. **Mouth: `python mouth_levels.py vo/final.mp3 mouth.js --wide-db -3`** (`brand.json` → `host.lipsync.wide_db`).
   Our wide mouth is a big open "aah", so it's used only on the loudest syllables, and half-open the rest of the time.
5. `timeline.js` + `scenes.js` (cards in y 230–850; Yara's bust sits below), `host-config.js` schedule: change pose
   every ~1–2 s on key words (point at screens, wave on the intro, explain on claims).
6. `ONLY=… node render.js` previews → `bash build.sh` (point it at the project venv for `audio.py`, as in test-yara)
   → check 1080×1920, H.264 High, −14 LUFS, true peak ≤ −1 dB → queue item with the DEMO caption + AI label note.

Replacing Yara's images: send new ones from Flow to the Telegram bot as files (`YARA-POSE-1..4`,
`YARA-MOUTH-HALF`, `YARA-MOUTH-WIDE`), then re-run the alignment (face template match on POSE-1 + rembg
`isnet-general-use`, mouth box 292,515–418,600 in POSE-1 coordinates) to rebuild `host/`.
