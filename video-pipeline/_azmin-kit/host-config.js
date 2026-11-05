// Yara (AI presenter, AZMIN brand.json). Copy into a reel folder and edit only the schedule (pose changes on key words).
// colour-matched to the poses. Pose changes every ~1-2 s on key words.
window.HOST = {
  poses: { wave: 'host/pose1.png', point: 'host/pose2.png', think: 'host/pose3.png', explain: 'host/pose4.png' },
  mouths: [null, 'host/mouth_half.png', 'host/mouth_wide.png'],
  mouthAt: [435, 265, 126, 85],
  frame: 1000, scale: 0.86, top: 1075,
  schedule: [[0, 'point'], [1.75, 'explain'], [3.18, 'wave'], [4.45, 'explain'], [5.2, 'think'], [6.5, 'point'], [8.0, 'explain'], [9.45, 'wave']]
};
