// "A taste of a lesson": pick an interest and the same page re-tells a real physics idea
// through it. The five examples are short, correct and checkable (the arithmetic is in the
// comments), not lesson text: they only show what "physics through what you love" feels like.
//
// It tours the five by itself until the visitor picks one (and never when they prefer
// reduced motion), and the accent colour follows the choice.

"use client";

import { useEffect, useState } from "react";

import { cn } from "@/lib/utils";

interface Taste {
  id: string;
  emoji: string;
  label: string;
  color: string;
  concept: string;
  chapter: string;
  question: string;
  idea: string;
  numbers: string;
}

const TASTES: Taste[] = [
  {
    id: "cricket",
    emoji: "🏏",
    label: "Cricket",
    color: "#22c55e",
    concept: "Linear momentum",
    chapter: "Laws of Motion · Class 11",
    question: "Why is a fast, heavy ball so much harder to stop than a slow, light one?",
    idea: "Momentum is mass times velocity. Stopping the ball means taking away all of it.",
    // 0.16 kg x 25 m/s = 4.0 kg m/s
    numbers: "A 0.16 kg ball at 25 m/s carries 4 kg·m/s of momentum.",
  },
  {
    id: "football",
    emoji: "⚽",
    label: "Football",
    color: "#3b82f6",
    concept: "Projectile motion",
    chapter: "Motion in a Plane · Class 11",
    question: "A long goal kick hangs in the air. How do you know where it will land?",
    idea: "Split the kick in two: it keeps moving sideways at a steady speed while gravity pulls it down.",
    // R = u^2 sin(2*45deg)/g = 400/9.8 = 40.8 m
    numbers: "Kicked at 20 m/s and 45°, it lands about 41 m away.",
  },
  {
    id: "gaming",
    emoji: "🎮",
    label: "Gaming",
    color: "#a855f7",
    concept: "Equations of motion",
    chapter: "Motion in a Straight Line · Class 11",
    question: "Why does your character hit the ground harder the longer the drop?",
    idea: "In free fall, speed grows by the same amount every second. Games copy that.",
    // v = g t = 9.8 x 2 = 19.6 m/s
    numbers: "After 2 seconds of falling, you're moving at about 19.6 m/s.",
  },
  {
    id: "smartphones",
    emoji: "📱",
    label: "Smartphones",
    color: "#06b6d4",
    concept: "Electrical power",
    chapter: "Current Electricity · Class 12",
    question: "Why does your phone get warm while it charges?",
    idea: "Any current through a resistance wastes some power as heat: P = I²R.",
    // 2^2 x 0.1 = 0.4 W
    numbers: "2 A through 0.1 Ω of resistance becomes 0.4 W of heat.",
  },
  {
    id: "motorsport",
    emoji: "🏎️",
    label: "Motorsport",
    color: "#ef4444",
    concept: "Dynamics of circular motion",
    chapter: "Laws of Motion · Class 11",
    question: "Why does a car slide wide in a tight corner if it comes in too fast?",
    idea: "Turning needs a sideways force towards the centre: F = mv²/r. The tyres can only give so much.",
    // 800 x 30^2 / 90 = 8000 N
    numbers: "An 800 kg car at 30 m/s round a 90 m bend needs 8000 N of grip.",
  },
];

export function InterestShowcase() {
  const [index, setIndex] = useState(0);
  const [touched, setTouched] = useState(false);
  const [paused, setPaused] = useState(false);

  // Tour the five until the visitor takes over (and not at all for reduced motion).
  useEffect(() => {
    if (touched || paused || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const timer = setInterval(() => setIndex((i) => (i + 1) % TASTES.length), 6000);
    return () => clearInterval(timer);
  }, [touched, paused]);

  const t = TASTES[index];

  return (
    <div
      className="flex flex-col gap-5"
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
      onFocus={() => setPaused(true)}
      onBlur={() => setPaused(false)}
    >
      <div role="group" aria-label="Pick an interest" className="flex flex-wrap justify-center gap-2">
        {TASTES.map((x, i) => (
          <button
            key={x.id}
            type="button"
            aria-pressed={i === index}
            onClick={() => {
              setIndex(i);
              setTouched(true);
            }}
            className={cn(
              "inline-flex items-center gap-2 rounded-full border px-4 py-2 text-sm font-semibold transition-all duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
              i === index
                ? "-translate-y-0.5 border-transparent text-foreground shadow-card"
                : "border-border bg-card text-muted-foreground hover:border-primary/40 hover:text-foreground",
            )}
            style={i === index ? { backgroundColor: `color-mix(in oklab, ${x.color} 22%, var(--card))`, boxShadow: `0 0 0 2px ${x.color}` } : undefined}
          >
            <span aria-hidden className="text-lg">
              {x.emoji}
            </span>
            {x.label}
          </button>
        ))}
      </div>

      {/* Keyed, so the card re-enters each time the interest changes. */}
      <article
        key={t.id}
        aria-live="polite"
        className="rm-sheet relative overflow-hidden rounded-3xl border border-border bg-card p-6 shadow-card-hover sm:p-8"
        style={{
          backgroundImage: `radial-gradient(90% 100% at 100% 0%, color-mix(in oklab, ${t.color} 20%, transparent), transparent 65%)`,
        }}
      >
        <div className="flex flex-wrap items-center gap-2 text-xs font-semibold">
          <span
            className="rounded-full px-3 py-1 text-foreground"
            style={{ backgroundColor: `color-mix(in oklab, ${t.color} 28%, transparent)` }}
          >
            {t.emoji} {t.concept}
          </span>
          <span className="text-muted-foreground">{t.chapter}</span>
        </div>
        <h3 className="mt-4 text-2xl font-extrabold leading-snug tracking-tight text-foreground sm:text-3xl">
          {t.question}
        </h3>
        <p className="mt-3 text-lg leading-relaxed text-muted-foreground">{t.idea}</p>
        <p
          className="mt-5 rounded-2xl border bg-background/60 px-4 py-3 font-semibold text-foreground"
          style={{ borderColor: `color-mix(in oklab, ${t.color} 45%, var(--border))` }}
        >
          {t.numbers}
        </p>
      </article>
      <p className="text-center text-xs text-muted-foreground">
        A taste of a lesson, not the lesson itself. Every concept opens with a story like this.
      </p>
    </div>
  );
}
