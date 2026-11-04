// A lesson as a short run of steps instead of one long scroll (2026-10-04).
//
// One idea per screen: a segmented progress bar (every segment is a button, so
// nothing is locked: jump anywhere), Back / Next at the bottom, the arrow keys,
// and "Show everything on one page" for anyone who would rather scroll. The step
// content is passed in, so this component knows nothing about physics: the lesson
// page decides the steps.
//
// Motion is CSS only and off under prefers-reduced-motion (globals.css).

"use client";

import { useEffect, useRef, useState, type ReactNode } from "react";
import { ArrowLeft, ArrowRight, Check, LayoutList, Layers, type LucideIcon } from "lucide-react";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

export interface LessonStep {
  id: string;
  label: string; // short, shown under the progress bar and on the Next button
  icon: LucideIcon;
  content: ReactNode;
}

function typingInto(target: EventTarget | null): boolean {
  const el = target as HTMLElement | null;
  if (!el) return false;
  return el.isContentEditable || ["INPUT", "TEXTAREA", "SELECT"].includes(el.tagName);
}

// `initialStep` lets the roadmap open the lesson at a given part (clamped to the steps there are);
// `initialAll` shows everything on one page (for students who prefer to scroll).
export function LessonStepper({
  steps,
  initialStep = 0,
  initialAll = false,
}: {
  steps: LessonStep[];
  initialStep?: number;
  initialAll?: boolean;
}) {
  const start = Math.max(0, Math.min(steps.length - 1, Math.floor(initialStep) || 0));
  const [index, setIndex] = useState(start);
  const [direction, setDirection] = useState<"next" | "prev">("next");
  const [visited, setVisited] = useState<Set<number>>(() => new Set([0, start]));
  const [all, setAll] = useState(initialAll);
  const top = useRef<HTMLDivElement | null>(null);
  const moved = useRef(false);

  const last = steps.length - 1;

  function go(to: number) {
    const next = Math.max(0, Math.min(last, to));
    if (next === index) return;
    setDirection(next > index ? "next" : "prev");
    setIndex(next);
    setVisited((v) => new Set(v).add(next));
    moved.current = true;
  }

  // Bring the new step into view (not on first load).
  useEffect(() => {
    if (!moved.current) return;
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    top.current?.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
  }, [index]);

  // ← / → move between steps, unless the student is typing (the "I'm stuck" box).
  useEffect(() => {
    if (all) return;
    function onKey(e: KeyboardEvent) {
      if (e.metaKey || e.ctrlKey || e.altKey || typingInto(e.target)) return;
      if (e.key === "ArrowRight") go(index + 1);
      else if (e.key === "ArrowLeft") go(index - 1);
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [index, all, last]);

  if (all) {
    return (
      <div className="flex flex-col gap-8">
        <ModeToggle all onToggle={() => setAll(false)} />
        {steps.map((s) => (
          <section key={s.id} aria-label={s.label}>
            {s.content}
          </section>
        ))}
      </div>
    );
  }

  const step = steps[index];
  const next = steps[index + 1];

  return (
    <div className="flex flex-col gap-6">
      {/* Progress: sticky under the site bar so it stays in reach while reading. */}
      <nav
        aria-label="Lesson steps"
        className="sticky top-16 z-30 -mx-4 flex flex-col gap-1.5 border-b border-border bg-background/90 px-4 py-3 backdrop-blur max-md:top-[60px]"
      >
        <ol className="flex gap-1.5">
          {steps.map((s, i) => {
            const state = i === index ? "now" : visited.has(i) ? "seen" : "todo";
            return (
              <li key={s.id} className="flex-1">
                <button
                  type="button"
                  onClick={() => go(i)}
                  aria-current={i === index ? "step" : undefined}
                  aria-label={`Step ${i + 1} of ${steps.length}: ${s.label}`}
                  className="group -my-2.5 flex w-full flex-col gap-1 py-2.5 focus-visible:outline-none"
                >
                  <span
                    className={cn(
                      "h-2 w-full rounded-full transition-colors duration-300 group-focus-visible:ring-2 group-focus-visible:ring-ring",
                      state === "now" && "bg-primary",
                      state === "seen" && "bg-primary/45",
                      state === "todo" && "bg-muted group-hover:bg-muted-foreground/30",
                    )}
                  />
                  <span
                    className={cn(
                      "hidden truncate text-left text-[11px] font-semibold sm:block",
                      state === "now" ? "text-foreground" : "text-muted-foreground",
                    )}
                  >
                    {s.label}
                  </span>
                </button>
              </li>
            );
          })}
        </ol>
        <div className="flex items-center justify-between text-xs text-muted-foreground sm:hidden">
          <span className="font-semibold text-foreground">{step.label}</span>
          <span>
            {index + 1} of {steps.length}
          </span>
        </div>
      </nav>

      <div ref={top} className="scroll-mt-32" />

      {/* The step. Keyed, so the slide-in replays on every change. */}
      <div
        key={step.id}
        className={cn(direction === "next" ? "rm-slide-next" : "rm-slide-prev", "flex flex-col gap-6")}
      >
        {step.content}
      </div>

      {/* Back / Next */}
      <div className="sticky bottom-20 z-20 flex items-center justify-between gap-3 rounded-[18px] border border-border bg-card/95 p-2.5 shadow-card-hover backdrop-blur md:bottom-3">
        <Button
          variant="ghost"
          onClick={() => go(index - 1)}
          disabled={index === 0}
        >
          <ArrowLeft className="size-4" /> Back
        </Button>
        <span className="hidden text-xs text-muted-foreground sm:inline">
          Use <kbd className="rounded border border-border px-1">←</kbd>{" "}
          <kbd className="rounded border border-border px-1">→</kbd> to move
        </span>
        {next ? (
          <Button onClick={() => go(index + 1)}>
            {next.label} <ArrowRight className="size-4" />
          </Button>
        ) : (
          <span className="flex items-center gap-1.5 px-3 text-sm font-semibold text-primary">
            <Check className="size-4" /> That&apos;s the lesson
          </span>
        )}
      </div>

      <ModeToggle all={false} onToggle={() => setAll(true)} />
    </div>
  );
}

function ModeToggle({ all, onToggle }: { all: boolean; onToggle: () => void }) {
  return (
    <button
      type="button"
      onClick={onToggle}
      className="inline-flex items-center gap-2 self-center rounded-full px-3 py-1.5 text-sm font-medium text-muted-foreground hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
    >
      {all ? <Layers className="size-4" aria-hidden /> : <LayoutList className="size-4" aria-hidden />}
      {all ? "Back to step by step" : "Show everything on one page"}
    </button>
  );
}
