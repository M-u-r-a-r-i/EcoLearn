// A gentle "stretch your legs" nudge after the reading span the student themselves said
// suits them (survey: "how long can you study before you need a break?"). Shows once per
// lesson visit, dismissible, never blocks anything. Counts only time the tab is visible, so
// a lesson left open in the background doesn't trigger it.

"use client";

import { useEffect, useState } from "react";
import { Coffee } from "lucide-react";

import { Button } from "@/components/ui/button";

export function BreakNudge({ minutes }: { minutes: number | null }) {
  const [shown, setShown] = useState(false);
  const [dismissed, setDismissed] = useState(false);

  useEffect(() => {
    if (!minutes || dismissed) return;
    let seconds = 0;
    const tick = setInterval(() => {
      if (document.visibilityState !== "visible") return;
      seconds += 5;
      if (seconds >= minutes * 60) {
        setShown(true);
        clearInterval(tick);
      }
    }, 5000);
    return () => clearInterval(tick);
  }, [minutes, dismissed]);

  if (!minutes || !shown || dismissed) return null;
  return (
    <div
      role="status"
      className="rm-sheet fixed inset-x-4 bottom-24 z-30 mx-auto flex max-w-md items-center gap-3 rounded-2xl border border-brand-accent/40 bg-card p-4 shadow-card-hover"
    >
      <Coffee className="size-6 shrink-0 text-brand-accent" aria-hidden />
      <p className="flex-1 text-sm text-foreground">
        You&apos;ve been at it about {minutes} minutes. Stretch, sip some water, look at something far
        away. Your place is saved.
      </p>
      <Button size="sm" variant="outline" onClick={() => setDismissed(true)}>
        Keep going
      </Button>
    </div>
  );
}
