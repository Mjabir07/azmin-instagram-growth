import React from "react";
import { AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { C } from "./brand";
import { PAPER, clamp, sfx, smooth } from "./YaraEpisode";
import pal from "./data/sc01-palm-crest.json";
import cars from "./data/sc02-azmin-cars.json";

/**
 * Showcase reels: a concept demo site recorded as a real scroll on a phone (frame-by-frame, prices hidden before
 * recording), narrated by Yara (AI). One config per reel; the layout is shared.
 * Strategy: marketing/content/strategy-nov-2026.md (hook in frame 1, done by 1.5 s; ask for sends; comment DEMO).
 */

type Word = { word: string; start: number; end: number };
type Line = { id: string; text: string; src: string; duration: number; words: Word[] };
type Clip = { src: string; len: number; freezeAfter?: number; chip?: string };
export type ShowcaseConfig = {
  data: { lines: Line[] };
  clips: Clip[];                    // played back to back from frame 0
  vo: Record<string, number>;       // line id -> start frame (the "hook" line has no caption: the title says it)
  title: [string, string];          // frame-1 hook: plain part, accent part
  kicker: string;                   // end card, e.g. "PALM CREST VILLAS · CONCEPT SITE"
  poster: string;                   // end card phone image
  endLen?: number;
};
const f = (s: number) => Math.round(s * 30);

const fonts = `
@font-face { font-family: Inter Tight; font-weight: 100 900; src: url(${staticFile("InterTight.woff2")}); }
@font-face { font-family: Serif; font-style: italic; src: url(${staticFile("InstrumentSerif-400i.woff2")}); }
`;

/** Word-by-word caption for the line that is speaking now. */
const Caption: React.FC<{ cfg: ShowcaseConfig }> = ({ cfg }) => {
  const fr = useCurrentFrame();
  const line = (id: string) => cfg.data.lines.find((l) => l.id === id)!;
  const active = (Object.entries(cfg.vo) as [string, number][]).find(([id, at]) => id !== "end" && id !== "hook" && fr >= at && fr < at + f(line(id).duration) + 8);
  if (!active) return null;
  const [id, at] = active;
  const t = (fr - at) / 30;
  const words = line(id).words;
  const o = interpolate(fr - at, [0, 6], [0, 1], clamp);
  return (
    <div style={{ position: "absolute", left: 70, right: 70, top: 200, display: "flex", justifyContent: "center", opacity: o }}>
      <div style={{ background: "rgba(7,16,34,.82)", borderRadius: 36, padding: "26px 38px", maxWidth: 940, textAlign: "center", boxShadow: "0 30px 80px rgba(0,0,0,.35)" }}>
        {words.map((w, i) => {
          const on = t >= w.start;
          const now = t >= w.start && t < w.end;
          return (
            <span key={i} style={{ font: "800 62px/1.18 Inter Tight", letterSpacing: -1.5, color: now ? C.cyan : on ? "#fff" : "rgba(255,255,255,.35)", marginRight: 16, display: "inline-block" }}>
              {w.word.replace(/[.,]$/, "")}
            </span>
          );
        })}
      </div>
    </div>
  );
};

/** Frame 1 hook: big title that is already on screen at frame 0 (no fade-in from nothing). */
const Hook: React.FC<{ title: [string, string] }> = ({ title }) => {
  const fr = useCurrentFrame();
  const out = interpolate(fr, [70, 84], [1, 0], clamp);
  const pop = interpolate(fr, [0, 10], [0.94, 1], { ...clamp, easing: smooth });
  const arrow = Math.sin(fr / 5) * 12;
  return (
    <div style={{ position: "absolute", left: 60, right: 60, top: 190, opacity: out, transform: `scale(${pop})`, transformOrigin: "50% 0" }}>
      <div style={{ display: "inline-block", background: C.blue, color: "#fff", font: "700 34px Inter Tight", letterSpacing: 3, padding: "12px 26px", borderRadius: 99 }}>CONCEPT BUILD</div>
      <div style={{ font: "800 112px/1.0 Inter Tight", letterSpacing: -4, color: PAPER, marginTop: 26, textShadow: "0 8px 40px rgba(0,0,0,.45)" }}>
        {title[0]}<br /><span style={{ font: "400 132px/1 Serif", fontStyle: "italic", letterSpacing: -1, color: C.cyan }}>{title[1]}</span>
      </div>
      <div style={{ font: "700 46px Inter Tight", color: PAPER, marginTop: 28, transform: `translateY(${arrow}px)`, textShadow: "0 6px 30px rgba(0,0,0,.5)" }}>↓ just scroll</div>
    </div>
  );
};

/** A small chip on top of the footage (e.g. "English ⇄ العربية"). */
const Chip: React.FC<{ text: string; top?: number }> = ({ text, top = 470 }) => {
  const fr = useCurrentFrame();
  const s = spring({ frame: fr - 4, fps: 30, config: { damping: 14 } });
  return (
    <div style={{ position: "absolute", top, left: 0, right: 0, display: "flex", justifyContent: "center", transform: `scale(${s})` }}>
      <div style={{ background: C.blue, color: "#fff", font: "800 52px Inter Tight", padding: "18px 40px", borderRadius: 99, boxShadow: "0 20px 60px rgba(0,98,245,.45)" }}>{text}</div>
    </div>
  );
};

const Footage: React.FC<{ src: string; len: number; freezeAfter?: number }> = ({ src, len, freezeAfter }) => {
  const fr = useCurrentFrame();
  const o = interpolate(fr, [len - 6, len], [1, 0.85], clamp);
  return (
    <AbsoluteFill style={{ opacity: o }}>
      {freezeAfter !== undefined && fr >= freezeAfter
        ? <OffthreadVideo src={staticFile(src)} startFrom={freezeAfter - 1} endAt={freezeAfter} muted />
        : <OffthreadVideo src={staticFile(src)} muted />}
    </AbsoluteFill>
  );
};

const EndCard: React.FC<{ kicker: string; poster: string }> = ({ kicker, poster }) => {
  const fr = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = (d: number) => spring({ frame: fr - d, fps, config: { damping: 15 } });
  const phone = s(0);
  return (
    <AbsoluteFill style={{ background: `radial-gradient(120% 80% at 50% 40%, #13254a 0%, ${C.navy} 60%, #050b18 100%)` }}>
      <div style={{ position: "absolute", left: "50%", top: 150, width: 380, height: 676, marginLeft: -190, borderRadius: 60, background: "#05080f", padding: 14, boxSizing: "border-box",
        boxShadow: "0 40px 120px rgba(0,98,245,.4), 0 0 0 3px #1d2a44", transform: `scale(${0.85 + 0.15 * phone}) rotate(${(1 - phone) * -4}deg)`, opacity: phone }}>
        <Img src={staticFile(poster)} style={{ width: "100%", height: "100%", borderRadius: 48, objectFit: "cover" }} />
      </div>
      <div style={{ position: "absolute", left: 60, right: 60, top: 880, textAlign: "center", color: PAPER }}>
        <div style={{ opacity: s(8), transform: `translateY(${(1 - s(8)) * 30}px)`, font: "700 40px Inter Tight", letterSpacing: 2, color: C.cyan }}>{kicker}</div>
        <div style={{ opacity: s(14), transform: `translateY(${(1 - s(14)) * 40}px)`, font: "800 120px/1 Inter Tight", letterSpacing: -4, marginTop: 30 }}>
          Comment <span style={{ background: C.blue, borderRadius: 24, padding: "0 22px" }}>DEMO</span>
        </div>
        <div style={{ opacity: s(20), font: "400 66px/1.1 Serif", fontStyle: "italic", marginTop: 26 }}>for the live link on your phone</div>
        <div style={{ opacity: s(40), font: "600 42px/1.3 Inter Tight", marginTop: 70, color: "rgba(244,241,234,.85)" }}>📤 Send this to someone<br />launching a project</div>
        <div style={{ opacity: s(56), font: "600 34px Inter Tight", marginTop: 60, color: "rgba(244,241,234,.6)" }}>@azmin_digital · voice: Yara (AI)</div>
      </div>
    </AbsoluteFill>
  );
};

export const makeShowcase = (cfg: ShowcaseConfig) => {
  const starts = cfg.clips.map((_, i) => cfg.clips.slice(0, i).reduce((t, c) => t + c.len, 0));
  const endFrom = starts[starts.length - 1] + cfg.clips[cfg.clips.length - 1].len;
  const total = endFrom + (cfg.endLen ?? 150);
  const line = (id: string) => cfg.data.lines.find((l) => l.id === id)!;
  const Component: React.FC = () => (
    <AbsoluteFill style={{ background: C.navy, fontFamily: "Inter Tight, sans-serif" }}>
      <style>{fonts}</style>
      <Audio src={staticFile("sfx/bed.m4a")} volume={(x) => interpolate(x, [0, 10, total - 30, total - 1], [0.0, 0.12, 0.12, 0], clamp)} />
      {(Object.entries(cfg.vo) as [string, number][]).map(([id, at]) => (
        <Sequence key={id} from={at} durationInFrames={f(line(id).duration) + 10}><Audio src={staticFile(line(id).src)} volume={1} /></Sequence>
      ))}
      {starts.slice(1).map((st, i) => sfx(i % 2 ? "swoosh.wav" : "whoosh.wav", st - 3, 0.35, 20))}
      {sfx("sparkle.wav", endFrom + 10, 0.4)}
      {cfg.clips.map((c, i) => (
        <Sequence key={c.src} from={starts[i]} durationInFrames={c.len}>
          <Footage src={c.src} len={c.len} freezeAfter={c.freezeAfter} />{c.chip && <Chip text={c.chip} />}
        </Sequence>
      ))}
      <Sequence from={endFrom} durationInFrames={total - endFrom}><EndCard kicker={cfg.kicker} poster={cfg.poster} /></Sequence>
      <Sequence from={0} durationInFrames={90}><Hook title={cfg.title} /></Sequence>
      <Caption cfg={cfg} />
    </AbsoluteFill>
  );
  return { Component, frames: total };
};

/** SC01 (Sat 31 Oct): Palm Crest Villas. */
export const PalmCrest = makeShowcase({
  data: pal as ShowcaseConfig["data"],
  clips: [
    { src: "sc01/a.mp4", len: 210 },                  // hook drift (0-84) + fly from the sky into the living room
    { src: "sc01/b.mp4", len: 64, freezeAfter: 57 },  // floor plan
    { src: "sc01/c.mp4", len: 120, chip: "English ⇄ العربية" },
  ],
  vo: { hook: 6, fly: 92, plan: 214, arabic: 280, end: 402 },
  title: ["This is a", "launch website."],
  kicker: "PALM CREST VILLAS · CONCEPT SITE",
  poster: "sc01/first.jpg",
});

/** SC02 (Mon 2 Nov): Azmin Cars. No prices, no real car brands. */
export const AzminCars = makeShowcase({
  data: cars as ShowcaseConfig["data"],
  clips: [
    { src: "sc02/a.mp4", len: 186 },                   // hook drift + walk around the car
    { src: "sc02/b.mp4", len: 120, chip: "Tap a colour" }, // paint picker
    { src: "sc02/c.mp4", len: 84 },                    // booking in three steps
  ],
  vo: { hook: 6, fly: 100, plan: 192, arabic: 312, end: 398 },
  title: ["This is a", "rental website."],
  kicker: "AZMIN CARS · CONCEPT SITE",
  poster: "sc02/first.jpg",
});
