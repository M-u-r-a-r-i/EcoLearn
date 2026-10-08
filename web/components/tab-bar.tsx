// An accessible tab bar: role=tablist, arrow keys / Home / End move between tabs, only the
// selected tab is in the tab order. The panel (role=tabpanel) is the caller's: give it
// `id={`panel-${id}`}` and `aria-labelledby={`tab-${id}`}`.

"use client";

import { useRef, type KeyboardEvent } from "react";

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
      className="-mx-4 flex gap-1 overflow-x-auto border-b border-border px-4 print:hidden sm:mx-0 sm:px-0"
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
            className={cn(
              "relative -mb-px flex shrink-0 items-center gap-2 border-b-2 px-4 py-3 text-sm font-semibold transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
              on
                ? "border-primary text-foreground"
                : "border-transparent text-muted-foreground hover:text-foreground",
            )}
          >
            {t.label}
            {t.count !== undefined && (
              <span
                className={cn(
                  "rounded-full px-2 py-0.5 text-[11px] font-bold",
                  on ? "bg-primary/15 text-primary" : "bg-muted text-muted-foreground",
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
