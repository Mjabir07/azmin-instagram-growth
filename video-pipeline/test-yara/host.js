// Talking host (bust) for the canvas reel template – include after scenes.js and style.js, plus mouth.js.
// Needs HOST config: images that share the SAME head position (generate pose variants from one base image),
// mouth patches cut from the same frame, and a pose schedule.
// window.HOST = { poses: { name: 'path.png', ... }, mouths: [null, 'half.png', 'wide.png'], mouthAt: [x, y, w, h],
//                 frame: 2000, scale: 0.56, top: 1215, schedule: [[t, 'pose'], ...] }
const HIMG = {}; Object.entries(HOST.poses).forEach(([k, s]) => { const i = new Image(); i.src = s; HIMG[k] = i; });
const HMOUTH = HOST.mouths.map(s => { if (!s) return null; const i = new Image(); i.src = s; return i; });
function host(t) {
  const c = X0, s = HOST.scale, w = HOST.frame * s; let k = 0; const S = HOST.schedule;
  for (let i = 0; i < S.length; i++) if (t >= S[i][0]) k = i;
  const [since, pose] = S[k]; const pop = 1 + 0.035 * Math.sin(Math.PI * cl((t - since) / 0.22));
  const fi = Math.floor(t * 30), lv = (window.MOUTH && fi < MOUTH.length) ? MOUTH[fi] : 0;
  const bob = Math.sin(t * 2 * Math.PI * 1.1) * 6 + (lv === 2 ? -6 : 0), tilt = Math.sin(t * 1.7) * 0.02 + (lv === 2 ? 0.01 : 0);
  const enter = eExpo(lin(t, 0, 0.4)), x = (W - w) / 2, y = HOST.top + bob + (1 - enter) * 600;
  c.save(); c.translate(W / 2, y + w * 0.7); c.rotate(tilt); c.scale(pop, pop); c.translate(-W / 2, -(y + w * 0.7));
  c.shadowColor = 'rgba(17,20,24,0.16)'; c.shadowBlur = 40; c.shadowOffsetY = 14; c.drawImage(HIMG[pose], x, y, w, w); c.shadowColor = 'transparent';
  const m = HOST.mouthAt; if (lv > 0 && HMOUTH[lv]) c.drawImage(HMOUTH[lv], x + m[0] * s, y + m[1] * s, m[2] * s, m[3] * s);
  c.restore();
}
