// Renders reel.html frame by frame (JPEG) into frames/, or preview stills with ONLY=1.2,5.6
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const FPS = 30, DUR = Number(process.env.DUR || 45.4);
const OUT = process.env.OUT || path.join(__dirname, 'frames');
const ONLY = process.env.ONLY ? process.env.ONLY.split(',').map(Number) : null;
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  page.on('pageerror', e => console.error('PAGE ERROR', e.message));
  await page.goto('file://' + path.join(__dirname, 'reel.html'));
  await page.evaluate(() => window.ready);
  const times = ONLY || Array.from({ length: Math.round(DUR * FPS) }, (_, i) => i / FPS);
  for (let i = 0; i < times.length; i++) {
    const data = await page.evaluate(t => { window.draw(t); return document.getElementById('c').toDataURL('image/jpeg', 0.94); }, times[i]);
    const name = ONLY ? `preview_${times[i].toFixed(2)}.jpg` : `f${String(i).padStart(5, '0')}.jpg`;
    fs.writeFileSync(path.join(OUT, name), Buffer.from(data.split(',')[1], 'base64'));
  }
  await browser.close(); console.log('frames', times.length);
})();
