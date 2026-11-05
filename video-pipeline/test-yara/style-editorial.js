// Editorial style (trend look): paper background with a dot grid, mono step label top-left, brand top-right,
// the current phrase builds word by word top-left (HILITE words italic accent), scene layer moved below the headline.
// Use: copy over style.js. Optional talking host: include ../../modules/lipsync/host.js and call host(t) (see README).
const PAPER = BRAND.paper || '#EFEDE8', INK = COL.text, ACCENT = COL.accText;
function background(t) {
  const c = X0; c.fillStyle = PAPER; c.fillRect(0, 0, W, H);
  c.fillStyle = 'rgba(17,20,24,0.05)'; for (let y = 30; y < H; y += 46) for (let x = 23; x < W; x += 46) { c.beginPath(); c.arc(x, y, 1.6, 0, 7); c.fill(); }
  const k = SC.findIndex(([a, b]) => t >= a && t < b); const lab = (TIMELINE.LABELS || [])[Math.max(0, k)] || '';
  c.font = '500 26px "DejaVu Sans Mono", monospace'; c.fillStyle = 'rgba(17,20,24,0.45)'; c.textAlign = 'left'; c.textBaseline = 'middle'; c.fillText(lab, 64, 112);
}
function brand(t) {
  const c = X0; c.save(); c.globalAlpha = lin(t, 0.1, 0.5); c.font = `800 28px ${BRAND.font}`; c.textAlign = 'right'; c.textBaseline = 'middle';
  c.fillStyle = INK; c.fillText(BRAND.name || '', W - 64, 112); c.beginPath(); c.arc(W - 64 - c.measureText(BRAND.name || '').width - 22, 112, 9, 0, 7); c.fillStyle = COL.acc; c.fill(); c.restore();
}
function blit(o) {
  const c = X0; c.save(); c.globalAlpha = o.a; if (o.blur > 0.3) c.filter = `blur(${o.blur.toFixed(1)}px)`;
  const ox = o.ox ?? 540, oy = o.oy ?? 760; c.translate(0, 205); c.translate(ox + (o.x || 0), oy + (o.y || 0)); c.scale(o.s * 0.96, o.s * 0.96); c.translate(-ox, -oy);
  c.drawImage(OC, 0, 0); c.restore();
}
const PHR = (() => { const out = []; let cur = []; WORDS.forEach((w, i) => { const gap = i ? w[1] - WORDS[i - 1][2] : 0;
  if (cur.length && (gap > 0.2 || cur.length >= 6)) { out.push(cur); cur = []; } cur.push(w); }); if (cur.length) out.push(cur); return out; })();
function captions(t) {
  let pi = -1; PHR.forEach((p, i) => { if (t >= p[0][1] - 0.1) pi = i; }); if (pi < 0) return; const ph = PHR[pi];
  const end = PHR[pi + 1] ? PHR[pi + 1][0][1] - 0.1 : ph[ph.length - 1][2] + 1.2; if (t > end) return;
  const c = X0, fs = 66, maxW = 950, lh = 84; let x = 64, y = 205;
  ph.forEach(w => { if (t < w[1] - 0.06) return; const hi = HILITE.has(w[0]);
    c.font = hi ? `italic 700 ${fs}px ${BRAND.font}` : `700 ${fs}px ${BRAND.font}`;
    const ww = c.measureText(w[0]).width; if (x + ww > 64 + maxW) { x = 64; y += lh; }
    const p = eExpo(lin(t, w[1] - 0.06, w[1] + 0.12)); c.save(); c.globalAlpha = p; c.translate(0, (1 - p) * 18);
    c.fillStyle = hi ? ACCENT : INK; c.textAlign = 'left'; c.textBaseline = 'middle'; c.fillText(w[0], x, y); c.restore(); x += ww + 18; });
}
