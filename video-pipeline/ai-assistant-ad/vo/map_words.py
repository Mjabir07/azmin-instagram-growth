"""take1 word times -> final VO times (pause cuts + tempo) -> words.js"""
import json, re
cm=json.load(open('vo/cutmap.json')); cuts=cm['cuts']; tempo=cm['tempo']
d=json.load(open('vo/words-take1.json')); W=d['words'] if isinstance(d,dict) else d
def m(t):
    off=0
    for a,b in cuts:
        if t>=b: off+=b-a
        elif t>a: off+=t-a
    return (t-off)/tempo
out=[]
for w in W:
    if w.get('type','word')!='word': continue
    tx=w['text']
    if tx.startswith('[') or tx.endswith(']') or tx=='—': continue
    out.append([re.sub(r'[?!.,…]+$','',tx).rstrip('.'), round(m(w['start']),3), round(m(w['end']),3), tx])
open('words.js','w').write('window.WORDS='+json.dumps(out,ensure_ascii=False)+';\n')
print(len(out), out[0], out[-1])
