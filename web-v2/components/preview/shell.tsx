"use client";

// One preview page: the token wrapper plus a small control bar (screen, theme,
// interest). Embedded in the /preview index, the bar hides (?embed=1) and the
// index drives these same query params.

import Link from "next/link";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
import type { ComponentType } from "react";

import { PvContext } from "@/components/preview/bits";

import { INTERESTS, interestById, type InterestInfo } from "@/lib/mock/preview";
import { DIRECTIONS, SCREENS, type ScreenId } from "@/components/preview/directions";

export type ScreenProps = { interest: InterestInfo };
export type ScreenSet = Record<ScreenId, ComponentType<ScreenProps>>;

export function PreviewShell({ dir }: { dir: "a" | "b" | "c" }) {
  const params = useSearchParams();
  const router = useRouter();
  const pathname = usePathname();
  const screen = (SCREENS.find((s) => s.id === params.get("screen"))?.id ?? "landing") as ScreenId;
  const theme = params.get("theme") === "dark" ? "dark" : "light";
  const interest = interestById(params.get("interest") ?? "cricket");
  const embed = params.get("embed") === "1";
  const Screen = DIRECTIONS[dir].screens[screen];

  function set(key: string, value: string) {
    const next = new URLSearchParams(params.toString());
    next.set(key, value);
    router.replace(`${pathname}?${next.toString()}`, { scroll: false });
  }

  const pill = (on: boolean) =>
    `rounded-full border px-3 py-1.5 text-sm font-semibold ${on ? "border-transparent bg-neutral-900 text-white" : "border-neutral-300 bg-white text-neutral-800"}`;

  return (
    <div className="flex min-h-screen flex-col">
      {!embed && (
        <div className="sticky top-0 z-50 flex flex-wrap items-center gap-2 border-b border-neutral-300 bg-neutral-100 px-4 py-2 text-neutral-900">
          <Link href="/preview" className="mr-1 text-sm font-bold underline">
            All directions
          </Link>
          <span className="text-sm font-bold">{DIRECTIONS[dir].name}</span>
          <div className="flex flex-wrap gap-1" role="group" aria-label="Screen">
            {SCREENS.map((s) => (
              <button key={s.id} onClick={() => set("screen", s.id)} className={pill(s.id === screen)} aria-pressed={s.id === screen}>
                {s.label}
              </button>
            ))}
          </div>
          <div className="flex gap-1" role="group" aria-label="Theme">
            {(["light", "dark"] as const).map((t) => (
              <button key={t} onClick={() => set("theme", t)} className={pill(t === theme)} aria-pressed={t === theme}>
                {t}
              </button>
            ))}
          </div>
          <div className="flex gap-1" role="group" aria-label="Interest">
            {INTERESTS.map((i) => (
              <button key={i.id} onClick={() => set("interest", i.id)} className={pill(i.id === interest.id)} aria-pressed={i.id === interest.id} aria-label={i.label} title={i.label}>
                {i.emoji}
              </button>
            ))}
          </div>
        </div>
      )}
      <div className="pv-root flex-1" data-dir={dir} data-theme={theme} data-interest={interest.id}>
        <PvContext.Provider value={{ setInterest: (id) => set("interest", id) }}>
          <Screen key={`${screen}-${interest.id}`} interest={interest} />
        </PvContext.Provider>
      </div>
    </div>
  );
}
