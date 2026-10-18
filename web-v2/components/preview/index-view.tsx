"use client";

// /preview: the three directions side by side, each in an iframe so every one
// has its own CSS and real viewport width (a phone frame is a true 375 px).

import Link from "next/link";
import { useEffect, useRef, useState } from "react";

import { DIRECTIONS, SCREENS } from "@/components/preview/directions";
import { INTERESTS } from "@/lib/mock/preview";

const DESKTOP = { w: 1200, h: 780 };
const PHONE = { w: 375, h: 760 };

function Frame({ dir, q, device }: { dir: "a" | "b" | "c"; q: string; device: "phone" | "desktop" }) {
  const box = useRef<HTMLDivElement>(null);
  const [scale, setScale] = useState(1);
  const size = device === "phone" ? PHONE : DESKTOP;
  useEffect(() => {
    const el = box.current;
    if (!el) return;
    const ro = new ResizeObserver(() => setScale(Math.min(1, el.clientWidth / size.w)));
    ro.observe(el);
    return () => ro.disconnect();
  }, [size.w]);
  return (
    <div className="min-w-0 flex-1" style={{ minWidth: device === "phone" ? PHONE.w + 2 : 0 }}>
      <div className="mb-2 flex items-baseline justify-between">
        <h2 className="font-bold">{DIRECTIONS[dir].name}</h2>
        <Link href={`/preview/${dir}?${q}`} className="text-sm underline">Open full</Link>
      </div>
      <div ref={box} className="w-full">
        <div className="overflow-hidden rounded-xl border border-neutral-300 bg-white shadow-sm" style={{ width: size.w * scale, height: size.h * scale }}>
          <iframe
            title={`${DIRECTIONS[dir].name} preview`}
            src={`/preview/${dir}?${q}&embed=1`}
            style={{ width: size.w, height: size.h, transform: `scale(${scale})`, transformOrigin: "top left", border: 0 }}
          />
        </div>
      </div>
    </div>
  );
}

export function IndexView() {
  const [screen, setScreen] = useState("roadmap");
  const [theme, setTheme] = useState("light");
  const [interest, setInterest] = useState("cricket");
  const [device, setDevice] = useState<"phone" | "desktop">("phone");
  const q = `screen=${screen}&theme=${theme}&interest=${interest}`;
  const pill = (on: boolean) =>
    `rounded-full border px-3 py-1.5 text-sm font-semibold ${on ? "border-transparent bg-neutral-900 text-white" : "border-neutral-300 bg-white"}`;
  return (
    <div className="min-h-screen bg-neutral-100 px-4 py-6 text-neutral-900">
      <h1 className="text-2xl font-bold">EcoLearn: three design directions</h1>
      <p className="mt-1 text-neutral-600">Same five screens, same fake data, three genuinely different designs. Click inside any frame, it is live.</p>
      <div className="mt-4 flex flex-wrap items-center gap-x-6 gap-y-2">
        <div className="flex flex-wrap gap-1" role="group" aria-label="Screen">
          {SCREENS.map((s) => <button key={s.id} className={pill(s.id === screen)} aria-pressed={s.id === screen} onClick={() => setScreen(s.id)}>{s.label}</button>)}
        </div>
        <div className="flex gap-1" role="group" aria-label="Theme">
          {["light", "dark"].map((t) => <button key={t} className={pill(t === theme)} aria-pressed={t === theme} onClick={() => setTheme(t)}>{t}</button>)}
        </div>
        <div className="flex gap-1" role="group" aria-label="Device">
          {(["phone", "desktop"] as const).map((d) => <button key={d} className={pill(d === device)} aria-pressed={d === device} onClick={() => setDevice(d)}>{d}</button>)}
        </div>
        <div className="flex gap-1" role="group" aria-label="Interest">
          {INTERESTS.map((i) => <button key={i.id} className={pill(i.id === interest)} aria-pressed={i.id === interest} aria-label={i.label} title={i.label} onClick={() => setInterest(i.id)}>{i.emoji}</button>)}
        </div>
      </div>
      <div className="mt-6 flex flex-wrap gap-6">
        {(["a", "b", "c"] as const).map((d) => <Frame key={`${d}-${device}`} dir={d} q={q} device={device} />)}
      </div>
    </div>
  );
}
