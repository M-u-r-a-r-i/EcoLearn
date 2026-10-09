// The pieces of the lesson check's result screen (2026-10-04): a burst of
// confetti for a right answer, the options replayed with what the student chose
// and what was right, and the three-step road to "mastered".
//
// Nothing here knows how answers are graded: it draws what the API said.

"use client";

import { Check, X } from "lucide-react";

import { Markdown } from "@/components/markdown";
import { cn } from "@/lib/utils";

// Confetti: fixed positions (no randomness, so it renders the same everywhere),
// fired once when the component appears. Hidden for reduced motion (globals.css).
const PIECES = [
  { x: -150, y: -120, r: 260, d: 0.0, c: "bg-success" },
  { x: -100, y: -170, r: -200, d: 0.05, c: "bg-[color:var(--gold)]" },
  { x: -60, y: -110, r: 320, d: 0.1, c: "bg-primary" },
  { x: -20, y: -190, r: -280, d: 0.02, c: "bg-brand-accent" },
  { x: 20, y: -130, r: 220, d: 0.08, c: "bg-success" },
  { x: 60, y: -180, r: -240, d: 0.04, c: "bg-primary" },
  { x: 100, y: -115, r: 300, d: 0.12, c: "bg-[color:var(--gold)]" },
  { x: 150, y: -160, r: -180, d: 0.06, c: "bg-brand-accent" },
  { x: -130, y: -60, r: 200, d: 0.14, c: "bg-primary" },
  { x: 130, y: -70, r: -220, d: 0.16, c: "bg-success" },
  { x: -80, y: -140, r: 360, d: 0.18, c: "bg-[color:var(--gold)]" },
  { x: 85, y: -145, r: -330, d: 0.2, c: "bg-primary" },
];

export function Confetti() {
  return (
    <div className="pointer-events-none absolute left-1/2 top-12 size-0" aria-hidden>
      {PIECES.map((p, i) => (
        <span
          key={i}
          className={cn("rm-confetti-piece absolute h-3 w-1.5 rounded-sm", p.c)}
          style={
            {
              "--x": `${p.x}px`,
              "--y": `${p.y}px`,
              "--r": `${p.r}deg`,
              "--d": `${p.d}s`,
            } as React.CSSProperties
          }
        />
      ))}
    </div>
  );
}

// The question's options after grading: the right one in green, the student's
// own wrong pick in red, the rest dimmed. Colour is never the only signal: each
// carries a tick or a cross and a word.
export function OptionReview({
  options,
  selected,
  correct,
}: {
  options: [string, string][];
  selected: string;
  correct: string;
}) {
  return (
    <ul className="flex flex-col gap-2.5" aria-label="Your answer and the right answer">
      {options.map(([letter, text]) => {
        const isRight = letter === correct;
        const isMine = letter === selected;
        return (
          <li
            key={letter}
            className={cn(
              "flex items-start gap-3 rounded-[13px] border p-3.5",
              isRight && "border-success/50 bg-success/10",
              isMine && !isRight && "border-destructive/50 bg-destructive/10",
              !isRight && !isMine && "border-border bg-card opacity-60",
            )}
          >
            <span
              aria-hidden
              className={cn(
                "flex size-7 shrink-0 items-center justify-center rounded-[9px] border text-sm font-bold",
                isRight
                  ? "border-success bg-success text-success-foreground"
                  : isMine
                    ? "border-destructive bg-destructive text-background"
                    : "border-border text-muted-foreground",
              )}
            >
              {isRight ? <Check className="size-4" strokeWidth={3} /> : isMine ? <X className="size-4" strokeWidth={3} /> : letter}
            </span>
            <div className="min-w-0 flex-1">
              <Markdown className="prose-sm">{text}</Markdown>
              {(isRight || isMine) && (
                <span
                  className={cn(
                    "mt-1 inline-block text-xs font-bold uppercase tracking-wide",
                    isRight ? "text-success" : "text-destructive",
                  )}
                >
                  {isRight && isMine ? "Your answer · right" : isRight ? "Right answer" : "Your answer"}
                </span>
              )}
            </div>
          </li>
        );
      })}
    </ul>
  );
}

// Right once → a new question tomorrow → mastered. Shows the student why one
// right answer isn't the end, so "mastered" doesn't look like a surprise later.
export function MasteryTrack({ signal }: { signal: "not_yet" | "partial" | "mastered" }) {
  const reached = signal === "mastered" ? 3 : signal === "partial" ? 1 : 0;
  const steps = ["Right once", "New question tomorrow", "Mastered"];
  return (
    <ol className="flex items-start" aria-label="Road to mastered">
      {steps.map((label, i) => {
        const on = i < reached;
        const gold = i === 2 && on;
        return (
          <li key={label} className="flex flex-1 flex-col items-center gap-1.5 text-center">
            <div className="flex w-full items-center">
              <span className={cn("h-1 flex-1", i === 0 ? "opacity-0" : on ? "bg-success" : "bg-muted")} />
              <span
                className={cn(
                  "flex size-8 shrink-0 items-center justify-center rounded-full border-2 text-xs font-bold",
                  gold
                    ? "border-[color:var(--gold)] bg-[color:var(--gold)] text-[#4a3a0e]"
                    : on
                      ? "border-success bg-success text-success-foreground"
                      : "border-border bg-card text-muted-foreground",
                )}
              >
                {on ? <Check className="size-4" strokeWidth={3} /> : i + 1}
              </span>
              <span className={cn("h-1 flex-1", i === steps.length - 1 ? "opacity-0" : i + 1 < reached ? "bg-success" : "bg-muted")} />
            </div>
            <span className={cn("text-[11px] font-semibold leading-tight", on ? "text-foreground" : "text-muted-foreground")}>
              {label}
            </span>
          </li>
        );
      })}
    </ol>
  );
}
