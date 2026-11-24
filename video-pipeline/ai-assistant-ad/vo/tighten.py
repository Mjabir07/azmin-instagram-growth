"""Shorten VO pauses to 0.24 s, write vo/tight.wav and vo/cutmap.json (orig time -> tight time)."""
import numpy as np, wave, subprocess, re, json
w=wave.open('vo/take1.wav'); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16)
out=subprocess.run(['ffmpeg','-i','vo/take1.wav','-af','silencedetect=n=-40dB:d=0.3','-f','null','-'],capture_output=True,text=True).stderr
s=[float(v) for v in re.findall(r'silence_start: ([0-9.]+)',out)]; e=[float(v) for v in re.findall(r'silence_end: ([0-9.]+)',out)]
keep=0.24; segs=[]; pos=0; cuts=[]
for a,b in zip(s,e):
    if b-a<=keep: continue
    ca,cb=a+keep/2,b-keep/2; segs.append(x[int(pos*sr):int(ca*sr)]); cuts.append([ca,cb]); pos=cb
segs.append(x[int(pos*sr):]); y=np.concatenate(segs)
o=wave.open('vo/tight.wav','wb'); o.setnchannels(1); o.setsampwidth(2); o.setframerate(sr); o.writeframes(y.tobytes()); o.close()
json.dump({'cuts':cuts,'tempo':1.12},open('vo/cutmap.json','w'))
