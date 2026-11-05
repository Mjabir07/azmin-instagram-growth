#!/usr/bin/env bash
# Pendulum reel: frames (render.js) -> procedural music (audio.py) -> whoosh per swing -> limiter to about -14 LUFS.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PY:-../../.venv/bin/python}
rm -rf frames && DUR=12 node render.js
sed -i "s/^SR = 48000; DUR = .*; N = /SR = 48000; DUR = 12.0; N = /" audio.py && $PY audio.py
ffmpeg -v error -y -framerate 30 -i frames/f%05d.jpg -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -profile:v high -r 30 -t 12 picture.mp4
# swings start at T0=0.35 s, one per HALF=1.0 s; the whoosh lands on the fastest point (middle of the swing)
F=""; IN=""; L=""
for k in 0 1 2 3 4 5 6; do
  t=$(python3 -c "print(int((0.35 + $k*1.0 + 0.5 - 0.22)*1000))"); s=$([ $((k%2)) = 0 ] && echo swing || echo swing2); p=$([ $((k%2)) = 0 ] && echo 0.35 || echo -0.35)
  IN="$IN -i sfx/$s.mp3"; F="$F[$((k+2)):a]aresample=48000,aformat=channel_layouts=stereo,volume=0.55,adelay=$t|$t,stereotools=balance_out=$p[w$k];"; L="$L[w$k]"
done
ffmpeg -v error -y -i picture.mp4 -i music.wav $IN -filter_complex "$F[1:a]volume=0.55[m];[m]${L}amix=inputs=8:normalize=0:duration=first,atrim=0:12,loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -t 12 out.mp4
ffmpeg -v error -y -i out.mp4 -af "aresample=192000,volume=2.2dB,alimiter=limit=0.8:level=false,aresample=48000" -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart final.mp4
ffmpeg -i final.mp4 -af loudnorm=print_format=summary -f null - 2>&1 | grep -E "Input Integrated|Input True Peak"
