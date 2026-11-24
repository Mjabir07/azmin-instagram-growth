// SFX cue list from the scene code (times = when the sound starts). node events.js > events.json
global.window = {}; require('./words.js'); const WT = i => window.WORDS[i][1];
const E = [];
const add = (t, s, g = 1) => E.push([+t.toFixed(3), s, g]);
add(0, 'boom', .7); add(0, 'whoosh', .6);
[8, 9, 10, 11, 12, 13].slice(0, 5).forEach((w, i) => add(WT(8 + i) - .08, 'pop', .8 + i * .05));
add(WT(14) - .1, 'swoosh', .5);                                     // zoom into clock
for (let k = 0; k < 6; k++) add(7.5 + k * .45, 'click', .35);        // clock ticks
add(WT(19) - .1, 'ding', .25);
add(WT(21) - .15, 'whoosh', .6);                                    // whip
for (let i = 0; i < 12; i++) add(10.7 + i * .46, i % 3 ? 'pop' : 'click', .45);   // notifications
add(WT(37), 'swoosh', .6);                                          // grow card pushed off
add(WT(41) - 1.1, 'riser', .7);                                     // into smart solution
add(WT(42) - .1, 'sparkle', .5);
add(WT(45) - .05, 'boom', .6);                                      // reveal cut
add(WT(55) - .05, 'boom', .9); add(WT(55), 'sparkle', .5);           // PERSONAL AI ASSISTANT
add(WT(58) - .2, 'whoosh', .5);
[58, 61, 63, 67, 70, 73].forEach(w => { add(WT(w) - .08, 'swoosh', .35); add(WT(w) + .05, 'ding', .22); });
add(WT(76) - .15, 'swoosh', .5); add(WT(79) - .05, 'click', .6);    // text/voice toggle
add(WT(85) - .15, 'swoosh', .5); add(WT(91) - .3, 'click', .8); add(WT(91), 'ding', .45);
add(WT(92) - .15, 'whoosh', .55);
[98, 100, 105].forEach(w => add(WT(w) - .1, 'pop', .7));
add(WT(111), 'swoosh', .4); add(WT(119) - 1.2, 'riser', .75); add(WT(119) - .05, 'boom', 1.0); add(WT(119), 'shutter', .7);
add(WT(124), 'swoosh', .5); add(WT(125) - .1, 'pop', .8);
add(WT(126) - .2, 'whoosh', .5); [129, 132, 138].forEach(w => add(WT(w) - .1, 'pop', .75));
add(62.4, 'swoosh', .6); add(62.6, 'boom', .45); [0, 1, 2].forEach(i => add(64.4 + i * .45, 'ding', .2));
add(WT(149) - .1, 'pop', .8);
add(WT(152) - .15, 'swoosh', .5); [154, 156, 157].forEach(w => add(WT(w) - .15, 'pop', .7));
add(WT(159) - .1, 'whoosh', .4); add(WT(161), 'swoosh', .45);
for (let k = 0; k < 4; k++) add(WT(163) - .1 + k * .125, 'type', .9);
add(WT(163) + .55, 'pop', .9); add(WT(163) + .6, 'boom', .5);
add(WT(167) - .15, 'whoosh', .55); for (let i = 0; i < 10; i++) add(WT(173) - .1 + i * .09, 'click', .5);
add(WT(180) - .3, 'swoosh', .4); add(82.1, 'boom', .7); add(82.15, 'sparkle', .4);
console.log(JSON.stringify(E.sort((a, b) => a[0] - b[0])));
