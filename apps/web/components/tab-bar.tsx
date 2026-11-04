// An accessible tab bar: role=tablist, arrow keys / Home / End move between tabs, only the
// selected tab is in the tab order. The panel (role=tabpanel) is the caller's: give it
// `id={`panel-${id}`}` and `aria-labelledby={`tab-${id}`}`.

"use client";

import { useEffect, useRef, type KeyboardEvent } from "react";

import { cn } from "@/lib/utils";

export interface TabDef<T extends string> {
  id: T;
  label: string;
  count?: number; // a small number beside the label (students, items needing attention)
}

export function TabBar<T extends string>({
  tabs,
  value,
  onChange,
  label,
}: {
  tabs: TabDef<T>[];
  value: T;
  onChange: (id: T) => void;
  label: string;
}) {
  const refs = useRef<Record<string, HTMLButtonElement | null>>({});

  // On a phone the strip scrolls sideways. Bring the open tab into view (a link straight to ?tab=ai would
  // otherwise leave its own tab half off-screen). Horizontal only; the page itself is never scrolled.
  useEffect(() => {
    const el = refs.current[value];
    const strip = el?.parentElement;
    if (!el || !strip) return;
    const left = el.offsetLeft - (strip.clientWidth - el.offsetWidth) / 2;
    strip.scrollTo({ left: Math.max(0, left), behavior: "smooth" });
  }, [value]);

  function onKey(e: KeyboardEvent, index: number) {
    const last = tabs.length - 1;
    const to =
      e.key === "ArrowRight" ? (index === last ? 0 : index + 1)
      : e.key === "ArrowLeft" ? (index === 0 ? last : index - 1)
      : e.key === "Home" ? 0
      : e.key === "End" ? last
      : null;
    if (to === null) return;
    e.preventDefault();
    onChange(tabs[to].id);
    refs.current[tabs[to].id]?.focus();
  }

  return (
    <div
      role="tablist"
      aria-label={label}
      className="dash-tabs print:hidden"
    >
      {tabs.map((t, i) => {
        const on = t.id === value;
        return (
          <button
            key={t.id}
            ref={(el) => {
              refs.current[t.id] = el;
            }}
            id={`tab-${t.id}`}
            role="tab"
            type="button"
            aria-selected={on}
            aria-controls={`panel-${t.id}`}
            tabIndex={on ? 0 : -1}
            onClick={() => onChange(t.id)}
            onKeyDown={(e) => onKey(e, i)}
            className="dash-tab"
          >
            {t.label}
            {t.count !== undefined && (
              <span
                className={cn(
                  "rounded-full px-2 py-0.5 text-[11px] font-bold",
                  on ? "bg-primary/15 text-primary" : "bg-card text-muted-foreground",
                )}
              >
                {t.count}
              </span>
            )}
          </button>
        );
      })}
    </div>
  );
}
