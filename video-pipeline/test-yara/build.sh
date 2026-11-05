#!/usr/bin/env bash
# Render frames + mix VO and music (ducked) -> out.mp4. SFX: add them afterwards with the real-sfx skill (see sound/README.md).
set -euo pipefail
cd "$(dirname "$0")"
VO=${VO:-vo/final.mp3}; OUT=${OUT:-out.mp4}; DUR=$(node -e "global.window={};require('./timeline.js');console.log(window.TIMELINE.END)")
rm -rf frames && DUR=$DUR node render.js
sed -i "s/^SR = 48000; DUR = .*; N = /SR = 48000; DUR = $DUR; N = /" audio.py && ../../.venv/bin/python audio.py
ffmpeg -v error -y -framerate 30 -i frames/f%05d.jpg -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -profile:v high -r 30 -t "$DUR" picture.mp4
ffmpeg -v error -y -i picture.mp4 -i "$VO" -i music.wav -filter_complex "\
[1:a]aresample=48000,aformat=channel_layouts=stereo,highpass=f=70,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,volume=1.6,asplit=2[vo][sc];\
[2:a]volume=0.5[mu];[mu][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=300[duck];\
[vo][duck]amix=inputs=2:normalize=0:duration=longest,atrim=0:$DUR,loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart -t "$DUR" "$OUT"
ffprobe -v error -show_entries format=duration,size -of compact "$OUT"
