"""Procedural music bed (no external assets). Writes music.wav (48 kHz stereo); build.sh sets DUR."""
import numpy as np, wave, sys
SR = 48000; DUR = 12.0; N = int(SR * DUR)
rng = np.random.default_rng(7)
def write(path, x):
    x = np.clip(x, -1, 1); y = (x * 32767).astype(np.int16)
    with wave.open(path, 'wb') as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(y.T.copy().tobytes())
def place(buf, snd, t, gain=1.0, pan=0.0):
    i = int(t * SR); j = min(N, i + snd.shape[-1])
    if i >= N: return
    l, r = np.sqrt(0.5 * (1 - pan)), np.sqrt(0.5 * (1 + pan))
    buf[0, i:j] += snd[:j - i] * gain * l * 1.4; buf[1, i:j] += snd[:j - i] * gain * r * 1.4
def env(n, a, d):
    e = np.ones(n); na = max(1, int(a * SR)); e[:na] = np.linspace(0, 1, na); e[na:] = np.exp(-np.arange(n - na) / (d * SR)); return e
def lp(x, k):  # one-pole lowpass, k in (0,1)
    y = np.empty_like(x); s = 0.0
    for i in range(len(x)): s += k * (x[i] - s); y[i] = s
    return y
# ---------------- music: 96 BPM, soft pads + pluck + kick/hat ----------------
BPM = 96; beat = 60 / BPM; t = np.arange(N) / SR
mus = np.zeros((2, N))
chords = [[57, 60, 64, 67], [53, 57, 60, 64], [48, 52, 55, 59], [55, 59, 62, 66]]  # Am7 Fmaj7 Cmaj7 G(add)
hz = lambda m: 440 * 2 ** ((m - 69) / 12)
bar = 4 * beat
for b in range(int(DUR / bar) + 1):
    ch = chords[b % 4]; s0 = b * bar; n = int(bar * SR) + SR // 2
    tt = np.arange(n) / SR
    pad = sum(np.sin(2 * np.pi * hz(m) * tt + 0.3 * np.sin(2 * np.pi * 0.4 * tt)) + 0.5 * np.sin(2 * np.pi * hz(m) * 1.003 * tt) for m in ch) / 6
    e = np.minimum(1, tt / 0.6) * np.minimum(1, (n / SR - tt) / 0.5)
    place(mus, pad * e * 0.10, s0)
    # bass
    bs = np.sin(2 * np.pi * hz(ch[0] - 24) * tt) * env(n, 0.01, 0.9)
    place(mus, bs * 0.16, s0)
    # pluck arpeggio 8ths
    for k in range(8):
        m = ch[[0, 2, 1, 3, 2, 1, 3, 2][k]] + 12; nn = int(0.5 * SR); t2 = np.arange(nn) / SR
        pl = (np.sin(2 * np.pi * hz(m) * t2) + 0.3 * np.sin(4 * np.pi * hz(m) * t2)) * env(nn, 0.004, 0.18)
        place(mus, pl * 0.05, s0 + k * beat / 2, pan=(-0.4 if k % 2 else 0.4))
# drums from bar 1 (after hook 0-1.2 s keep light)
for i in range(int(DUR / beat)):
    s0 = i * beat
    if s0 < 1.2: continue
    nn = int(0.35 * SR); t2 = np.arange(nn) / SR
    if i % 2 == 0:
        kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-t2 * 30)) * t2) * env(nn, 0.002, 0.12)
        place(mus, kick * 0.32, s0)
    hat = rng.standard_normal(int(0.06 * SR)); hat = (hat - lp(hat, 0.3)) * env(len(hat), 0.001, 0.015)
    place(mus, hat * 0.05, s0 + beat / 2, pan=0.3)
    if i % 4 == 2:
        sn = rng.standard_normal(int(0.2 * SR)); sn = (sn - lp(sn, 0.08)) * env(len(sn), 0.001, 0.05)
        place(mus, sn * 0.08, s0)
# fade in/out
fade = np.minimum(1, t / 0.4) * np.minimum(1, (DUR - t) / 1.2); mus *= fade
write('music.wav', mus)
# ---------------- SFX ----------------
sfx = np.zeros((2, N))
def whoosh(d=0.5):
    n = int(d * SR); x = rng.standard_normal(n); out = np.zeros(n); s = 0.0
    for i in range(n): k = 0.02 + 0.25 * np.sin(np.pi * i / n) ** 2; s += k * (x[i] - s); out[i] = s
    return out * np.sin(np.pi * np.arange(n) / n) ** 1.5 * 2.2
def pop(f=900, d=0.09):
    n = int(d * SR); tt = np.arange(n) / SR; return np.sin(2 * np.pi * f * tt * (1 - 0.4 * tt / d)) * env(n, 0.002, d / 4)
def click():
    n = int(0.025 * SR); x = rng.standard_normal(n); return (x - lp(x, 0.2)) * env(n, 0.0005, 0.004) * 0.8
def ding(f=1320):
    n = int(0.9 * SR); tt = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * tt) + 0.5 * np.sin(2 * np.pi * f * 1.5 * tt) + 0.3 * np.sin(2 * np.pi * f * 2 * tt)) * env(n, 0.003, 0.25) / 1.8
W = whoosh()
for c in [3.88, 9.8, 16.9, 23.54, 29.22, 35.61, 39.72]: place(sfx, W, c - 0.3, 0.22)
def typing(a, b, rate=16):
    for tt in np.arange(a, b, 1 / rate): place(sfx, click(), tt + rng.uniform(-0.01, 0.01), 0.14, pan=rng.uniform(-0.3, 0.3))
for i in range(3): place(sfx, pop(800 + i * 150, 0.1), 0.05 + i * 0.15, 0.16)    # phones
place(sfx, pop(260, 0.2), 2.16, 0.35); place(sfx, ding(1568), 2.3, 0.1)            # stamp
for tt in [4.32, 5.44]: place(sfx, pop(300, 0.14), tt, 0.22)                       # crosses
typing(7.68, 7.9); typing(8.8, 9.6)
for tt in [12.48, 13.56, 14.88, 15.96]: place(sfx, pop(1100, 0.08), tt, 0.16)
for tt in [18.72, 20.0]: place(sfx, whoosh(0.2), tt, 0.12)
place(sfx, pop(900, 0.1), 21.04, 0.18); place(sfx, pop(700, 0.12), 22.32, 0.2)
for tt in [26.56, 27.6, 28.1, 28.16]: place(sfx, ding(1568), tt + 0.1, 0.08)
place(sfx, pop(260, 0.18), 30.72, 0.3); place(sfx, pop(400, 0.14), 32.16, 0.22); place(sfx, ding(1320), 34.08, 0.12)
place(sfx, pop(700, 0.14), 36.24, 0.25)
for i in range(3): place(sfx, pop(900 + i * 120, 0.08), 37.6 + i * 0.15, 0.14)
place(sfx, ding(1175), 38.68, 0.16)
place(sfx, pop(700, 0.1), 40.37, 0.25); place(sfx, ding(1568), 40.47, 0.08)           # follow
typing(41.2, 41.55, 14); place(sfx, pop(1000, 0.1), 41.2, 0.2)
place(sfx, ding(1175), 43.68, 0.18); place(sfx, ding(1568), 43.8, 0.12)
write('sfx.wav', sfx)
print('ok')
