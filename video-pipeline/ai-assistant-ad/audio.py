"""Our own dark cinematic bed (procedural, no licences) + SFX from reels/public/sfx placed by events.json.
Writes music.wav and sfx.wav (48 kHz stereo). numpy only."""
import numpy as np, wave, json
SR = 48000; DUR = 86.0; N = int(SR * DUR)
VO_END = 82.0

def write(path, x):
    y = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    with wave.open(path, 'wb') as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(y.T.copy().tobytes())
def read(path):
    with wave.open(path) as w: return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
def place(buf, snd, t, gain=1.0, pan=0.0):
    i = int(t * SR); j = min(N, i + len(snd))
    if i >= N or i < 0: return
    buf[0, i:j] += snd[:j - i] * gain * np.sqrt(.5 * (1 - pan)) * 1.4
    buf[1, i:j] += snd[:j - i] * gain * np.sqrt(.5 * (1 + pan)) * 1.4
def smooth(x, k):  # cheap lowpass: moving average of k samples
    return np.convolve(x, np.ones(k) / k, mode='same')

hz = lambda m: 440 * 2 ** ((m - 69) / 12)
BPM = 92; beat = 60 / BPM; bar = 4 * beat
rng = np.random.default_rng(3)
mus = np.zeros((2, N))
chords = [[45, 52, 57, 60, 64], [41, 48, 53, 57, 64], [43, 50, 55, 59, 62], [40, 47, 52, 55, 59]]   # Am  F  G  Em (dark, minor)
for b in range(int(DUR / bar) + 1):
    s0 = b * bar
    if s0 > VO_END + 3: break
    ch = chords[b % 4]; n = int((bar + 1.2) * SR); tt = np.arange(n) / SR
    pad = sum(np.sin(2 * np.pi * hz(m) * tt + .4 * np.sin(2 * np.pi * .3 * tt)) * (1.4 if m < 50 else 1) for m in ch)
    pad += sum(.5 * np.sin(2 * np.pi * hz(m) * 1.004 * tt) for m in ch[2:])
    e = np.minimum(1, tt / .9) * np.minimum(1, np.maximum(0, (n / SR - tt) / 1.2))
    place(mus, smooth(pad, 12) * e * .045, s0, pan=(-.2 if b % 2 else .2))
    for k in range(4):                                         # soft sub pulse on each beat
        tb = s0 + k * beat
        if tb < 1.0: continue
        m = np.arange(int(.45 * SR)) / SR; f = 38 + 40 * np.exp(-m * 30)
        place(mus, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-m * 7) * .32, tb)
        for h in (0, .5):                                    # muted hats (eighths), off before the drop
            th = tb + h * beat; nh = int(.05 * SR)
            hat = rng.standard_normal(nh); hat = hat - smooth(hat, 6); place(mus, hat * np.exp(-np.arange(nh) / (.012 * SR)) * .035, th, pan=.35)
# arrangement: thin intro, lift at the reveal, quieter under the CTA, out after the VO
t = np.arange(N) / SR
amp = np.interp(t, [0, 1, 19, 21, 49.8, 52.7, 66, 82, 84, DUR], [.55, .7, .75, 1, .9, 1, .85, .8, .25, 0])
mus *= amp
write('music.wav', mus)

sfx = np.zeros((2, N)); lib = {}
for t0, name, g in json.load(open('events.json')):
    if name not in lib: lib[name] = read(f'sfx/{name}.wav')
    place(sfx, lib[name], t0, g * .55, pan=((hash(name + str(t0)) % 7) - 3) * .06)
write('sfx.wav', sfx)
print('music + sfx', DUR, 's; cues', len(json.load(open('events.json'))))
