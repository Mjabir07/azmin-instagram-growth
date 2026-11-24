#!/usr/bin/env bash
# picture.mp4 + VO + ducked music + SFX -> two-pass loudnorm (-14 LUFS, TP -1) -> out/ai-assistant-ad.mp4
set -euo pipefail; cd "$(dirname "$0")"; mkdir -p out
DUR=86
FC="[1:a]aresample=48000,aformat=channel_layouts=stereo,highpass=f=70,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,volume=1.5,asplit=2[vo][sc];\
[2:a]volume=0.32[mu];[mu][sc]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=350[duck];\
[3:a]volume=0.9[fx];[vo][duck][fx]amix=inputs=3:normalize=0:duration=longest,alimiter=limit=0.7:attack=2:release=80:level=false,apad,atrim=0:$DUR"
ffmpeg -v error -y -i picture.mp4 -i vo/final.wav -i music.wav -i sfx.wav -filter_complex "$FC[pre]" -map "[pre]" -c:a pcm_s16le premix.wav
M=$(ffmpeg -hide_banner -i premix.wav -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 | sed -n '/{/,/}/p')
g(){ echo "$M" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -v error -y -i picture.mp4 -i premix.wav -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,aresample=192000,alimiter=limit=0.79:attack=1:release=60:level=false,aresample=48000" \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart -t $DUR out/ai-assistant-ad.mp4
ffmpeg -hide_banner -i out/ai-assistant-ad.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E '^\s+(I|LRA|Peak):' | tr -s ' '
