// Renders a still from reel.html: FN=thumb|thumb2|thumb3|avatar[:BADGE]|avatar2[:nobot] NAME=<output.jpg>
// Uses an element screenshot (file:// images would taint canvas.toDataURL).
const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch({ args: ['--allow-file-access-from-files'] }); const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  p.on('pageerror', e => console.error('PAGE ERROR', e.message));
  await p.goto('file://' + path.join(__dirname, 'reel.html')); await p.evaluate(() => window.ready);
  const fn = process.env.FN || 'thumb';
  await p.evaluate(fn => { const [f, a] = fn.split(':'); window[f](f === 'avatar' ? (a || 'P') : a !== 'nobot'); }, fn);
  await p.locator('#c').screenshot({ path: path.resolve(__dirname, process.env.NAME || '../../examples/leads-reel-v3-thumbnail.jpg'), type: 'jpeg', quality: 95 });
  await b.close(); })();
