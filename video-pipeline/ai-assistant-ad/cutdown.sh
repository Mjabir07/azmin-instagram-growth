#!/usr/bin/env bash
# 45 s cutdown from the full ad, cut at sentence edges: hook | smart solution -> features | free | comment LINK -> end
set -euo pipefail; cd "$(dirname "$0")"
IN=out/ai-assistant-ad.mp4; OUT=out/ai-assistant-ad-45s.mp4
SEG=("0 10.30" "19.02 35.00" "51.66 55.30" "70.33 86.00")
FC=""; CAT=""; i=0
for s in "${SEG[@]}"; do set -- $s; d=$(python3 -c "print(round($2-$1,3))")
  FC+="[0:v]trim=$1:$2,setpts=PTS-STARTPTS[v$i];[0:a]atrim=$1:$2,asetpts=PTS-STARTPTS,afade=t=in:d=0.04,afade=t=out:st=$(python3 -c "print(round($d-0.06,3))"):d=0.06[a$i];"
  CAT+="[v$i][a$i]"; i=$((i+1)); done
ffmpeg -v error -y -i $IN -filter_complex "${FC}${CAT}concat=n=$i:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -profile:v high -r 30 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart $OUT
ffprobe -v error -show_entries format=duration,size -of compact $OUT
