// AZMIN test reel scenes. Editorial style: keep cards in y 230-850 (the layer is shifted down 205 px under the headline);
// Yara's bust sits below (host.js). Animations are anchored to words with WT().
const IMG = {}; for (const [k, s] of Object.entries({ palm: 'img/palm.jpg' })) { const i = new Image(); i.src = s; IMG[k] = i; }
const SERIF = (s) => `italic 400 ${s}px ${BRAND.serif}`;
function phone(x, y, w, h, img, p) {
  X.save(); X.globalAlpha = cl(p * 1.5); X.translate(x + w / 2, y + h / 2); X.rotate((1 - p) * -0.12); X.scale(mix(0.85, 1, p), mix(0.85, 1, p)); X.translate(-(x + w / 2), -(y + h / 2));
  glow('rgba(7,26,61,0.35)', 60, 24); fillRR(x, y, w, h, 46, '#0B0B0C'); noGlow();
  X.save(); rr(x + 12, y + 12, w - 24, h - 24, 36); X.clip(); if (img.complete) X.drawImage(img, x + 12, y + 12, w - 24, (w - 24) * img.height / img.width); X.restore(); X.restore();
}
function s0(lt, t) {
  phone(640, 236, 330, 610, IMG.palm, eBack(lin(t, WT('launch') - 0.15, WT('launch') + 0.35)));
  const q = eBack(lin(t, WT('not') - 0.1, WT('not') + 0.3)); if (q <= 0) return;
  X.save(); X.globalAlpha = cl(q); X.translate(300, 540); X.rotate(-0.06); X.scale(q, q);
  card(-170, -220, 340, 440, 22); fillRR(-130, -180, 260, 46, 8, '#E6E1D6');
  for (let i = 0; i < 9; i++) fillRR(-130, -100 + i * 26, 260 - (i * 37) % 90, 12, 6, '#DDD7CA');
  txt('Brochure.pdf', 0, 175, F(700, 30), COL.text, 'center');
  cross(0, 0, 9, '#E5484D', lin(t, WT('PDF'), WT('PDF') + 0.35)); X.restore();
}
function s1(lt, t) {
  const p = eBack(lin(t, WT('AI') - 0.12, WT('AI') + 0.3)); if (p > 0) {
    X.save(); X.globalAlpha = cl(p); X.translate(540, 360); X.scale(p, p);
    card(-400, -110, 800, 220, 36); chip(-360, -40, 'AI PRESENTER', '#FFFFFF', F(800, 30), COL.acc);
    txt('Face and voice made with AI.', -360, 40, F(700, 40), COL.text); X.restore(); }
  const b = eExpo(lin(t, WT('AZMIN') - 0.1, WT('AZMIN') + 0.4)); if (b > 0) {
    X.save(); X.globalAlpha = b; X.translate(0, (1 - b) * 40);
    txt('AZMIN', 540, 650, F(900, 150), COL.text, 'center'); txt('digital', 540, 760, SERIF(120), COL.acc, 'center'); X.restore(); }
}
function s2(lt, t) {
  const p = eBack(lin(t, WT('Comment') - 0.1, WT('Comment') + 0.3)); if (p <= 0) return;
  X.save(); X.translate(540, 400); X.scale(p, p); glow('rgba(0,98,245,0.35)', 60, 20); fillRR(-420, -150, 840, 300, 48, COL.acc); noGlow();
  txt('Comment', 0, -50, F(700, 54), '#FFFFFF', 'center'); txt('DEMO', 0, 50, F(900, 130), '#FFFFFF', 'center'); X.restore();
  const d = eBack(lin(t, WT('live') - 0.15, WT('live') + 0.3)); if (d <= 0) return;
  X.save(); X.globalAlpha = cl(d); X.translate(540, 700); X.scale(d, d); card(-330, -70, 660, 140, 70);
  txt('📩  Live demo link in your DMs', 0, 2, F(700, 38), COL.text, 'center'); X.restore();
}
const SCENES = [s0, s1, s2];
window.thumb = () => { X0.setTransform(1, 0, 0, 1, 0, 0); X0.globalAlpha = 1; background(1.5); renderScene(0, 2.8); blit({ a: 1, s: 1, x: 0, y: 0, blur: 0 }); X = X0; if (typeof host === 'function') host(2.8); brand(5); captions(2.5); };
window.ready = (async () => { await document.fonts.ready; await Promise.all(Object.values(IMG).concat(typeof HIMG !== 'undefined' ? Object.values(HIMG) : [], typeof HMOUTH !== 'undefined' ? HMOUTH.filter(Boolean) : []).map(i => i.decode().catch(() => 0)));
  window.draw(0); return true; })();
