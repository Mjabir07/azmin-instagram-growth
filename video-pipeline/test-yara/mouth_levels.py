#!/usr/bin/env python3
"""Mouth level per video frame from a voice-over: 0 closed, 1 half open, 2 wide open.

Usage: python3 mouth_levels.py vo/final.mp3 mouth.js [--fps 30]
Writes  window.MOUTH = [...]  for host.js. Needs ffmpeg on PATH.
Levels come from loudness relative to the VO's own loud parts (90th percentile), with 2-frame smoothing
and a half-open frame every 5th frame of a long wide-open run, so the flap looks natural.
"""
import json, subprocess, sys
import numpy as np

def main():
    src, out = sys.argv[1], sys.argv[2]
    fps = int(sys.argv[sys.argv.index('--fps') + 1]) if '--fps' in sys.argv else 30
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(float) / 32768
    hop = 16000 // fps; n = len(x) // hop
    db = np.array([20 * np.log10(np.sqrt(np.mean(x[i * hop:(i + 1) * hop] ** 2)) + 1e-6) for i in range(n)])
    ref = np.percentile(db[db > -50], 90)
    lv = [0 if d - ref < -24 else (1 if d - ref < -8 else 2) for d in db]
    for i in range(1, len(lv) - 1):
        if lv[i] != lv[i - 1] and lv[i] != lv[i + 1]: lv[i] = lv[i - 1]
    run = 0
    for i in range(len(lv)):
        run = run + 1 if lv[i] == 2 else 0
        if run and run % 5 == 0: lv[i] = 1
    open(out, 'w').write(f'// mouth level per frame ({fps} fps) from {src}\nwindow.MOUTH = {json.dumps(lv)};\n')
    print(out, n, 'frames')

if __name__ == '__main__':
    main()
