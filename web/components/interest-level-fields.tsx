// The interest + class choosers, shared by signup and (later) settings.
//
// Interests come from GET /api/interests, so promoting an interest from "draft"
// to "active" in data/interests.yaml makes it appear here with no code change.
// Chips in a wrapping grid, so 2 interests or 20 both lay out well.

"use client";

import { useEffect, useState } from "react";

import { friendlyMessage, getInterests, type Interest } from "@/lib/api";
import { cn } from "@/lib/utils";

export const LEVELS = ["Class 11", "Class 12"] as const;

interface Props {
  interest: string;
  level: string;
  onInterestChange: (id: string) => void;
  onLevelChange: (level: string) => void;
  disabled?: boolean;
}

export function InterestLevelFields({
  interest,
  level,
  onInterestChange,
  onLevelChange,
  disabled,
}: Props) {
  const [interests, setInterests] = useState<Interest[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getInterests().then(
      (list) => {
        setInterests(list);
        // Pick the first one if nothing valid is selected yet.
        if (list.length > 0 && !list.some((i) => i.id === interest)) onInterestChange(list[0].id);
      },
      (err) => setError(friendlyMessage(err)),
    );
    // Run once: the list doesn't change while the form is open.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <fieldset className="flex flex-col gap-2" disabled={disabled}>
        <legend className="mb-2 text-sm font-semibold text-foreground">Learn through…</legend>
        {error && <p className="text-sm text-destructive">{error}</p>}
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
          {interests === null && !error
            ? Array.from({ length: 2 }, (_, i) => (
                <div key={i} className="h-24 animate-pulse rounded-xl bg-muted" />
              ))
            : interests?.map((opt) => (
                <button
                  key={opt.id}
                  type="button"
                  aria-pressed={interest === opt.id}
                  onClick={() => onInterestChange(opt.id)}
                  title={opt.description}
                  className={cn(
                    "rounded-xl border p-4 text-center transition-all",
                    interest === opt.id
                      ? "border-primary bg-primary/5 ring-2 ring-primary shadow-soft"
                      : "border-border bg-card hover:border-primary/40 hover:shadow-soft",
                  )}
                >
                  <div className="text-3xl">{opt.emoji}</div>
                  <div className="mt-2 text-sm font-semibold text-foreground">{opt.label}</div>
                  {/* Say how much is written, rather than hiding half-done
                      interests: a student can pick one and see the rest arrive. */}
                  <div className="mt-1 text-xs text-muted-foreground">
                    {opt.chapters_ready === opt.chapters_total
                      ? "All chapters ready"
                      : `${opt.chapters_ready} of ${opt.chapters_total} chapters ready`}
                  </div>
                </button>
              ))}
        </div>
      </fieldset>

      <fieldset className="flex flex-col gap-2" disabled={disabled}>
        <legend className="mb-2 text-sm font-semibold text-foreground">Your class</legend>
        <div className="flex gap-3">
          {LEVELS.map((opt) => (
            <button
              key={opt}
              type="button"
              aria-pressed={level === opt}
              onClick={() => onLevelChange(opt)}
              className={cn(
                "flex-1 rounded-xl border p-3 font-semibold transition-all",
                level === opt
                  ? "border-primary bg-primary/5 ring-2 ring-primary text-foreground"
                  : "border-border bg-card text-muted-foreground hover:border-primary/40",
              )}
            >
              {opt}
            </button>
          ))}
        </div>
      </fieldset>
    </>
  );
}
