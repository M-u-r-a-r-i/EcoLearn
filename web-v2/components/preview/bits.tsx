"use client";

import { createContext, useContext, useState, type ReactNode } from "react";

import type { InterestId } from "@/lib/mock/preview";

// Lets a screen (the landing's interest tiles) change the previewed interest.
export const PvContext = createContext<{ setInterest: (id: InterestId) => void }>({ setInterest: () => {} });
export const usePv = () => useContext(PvContext);

// 14 CSS confetti pieces, reusing the keyframes in globals.css. Hidden unless
// motion is welcome (the .rm-confetti-piece rule).
export function Confetti({ colors }: { colors: string[] }) {
  const pieces = Array.from({ length: 14 }, (_, i) => {
    const a = (i / 14) * Math.PI * 2;
    const r = 90 + (i % 3) * 30;
    return {
      x: Math.round(Math.cos(a) * r),
      y: Math.round(Math.sin(a) * r - 40),
      rot: (i * 67) % 360,
      d: (i % 5) * 0.04,
      c: colors[i % colors.length],
    };
  });
  return (
    <div aria-hidden className="pointer-events-none absolute left-1/2 top-24 z-10">
      {pieces.map((p, i) => (
        <span
          key={i}
          className="rm-confetti-piece absolute h-2.5 w-1.5 rounded-[1px]"
          style={{ background: p.c, ["--x" as string]: `${p.x}px`, ["--y" as string]: `${p.y}px`, ["--r" as string]: `${p.rot}deg`, ["--d" as string]: `${p.d}s` }}
        />
      ))}
    </div>
  );
}

// Which of the 3 "how sure" answers is picked, etc.
export function useToggle(initial = false): [boolean, () => void] {
  const [on, setOn] = useState(initial);
  return [on, () => setOn((v) => !v)];
}

export function Ring({ size = 64, stroke = 8, done, mastered, total, track, doneColor, goldColor, children }: {
  size?: number; stroke?: number; done: number; mastered: number; total: number;
  track: string; doneColor: string; goldColor: string; children?: ReactNode;
}) {
  const r = (size - stroke) / 2;
  const c = 2 * Math.PI * r;
  const arc = (n: number) => (c * n) / total;
  return (
    <div className="relative shrink-0" style={{ width: size, height: size }} role="img" aria-label={`${done} of ${total} done, ${mastered} mastered`}>
      <svg width={size} height={size} className="-rotate-90">
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={track} strokeWidth={stroke} />
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={doneColor} strokeWidth={stroke} strokeLinecap="round" strokeDasharray={`${arc(done)} ${c}`} />
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={goldColor} strokeWidth={stroke} strokeLinecap="round" strokeDasharray={`${arc(mastered)} ${c}`} />
      </svg>
      <div className="absolute inset-0 grid place-items-center">{children}</div>
    </div>
  );
}
