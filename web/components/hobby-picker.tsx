// The hobby tile picker, shared by the first-login survey and the starting check.
// Tap tiles (up to MAX_HOBBIES), plus up to MAX_OWN hobbies of the student's own: short
// labels only, so no sentence about a child is ever stored. The ORDER they tap is kept:
// the survey asks about the first two.

"use client";

import { useState } from "react";
import { Check } from "lucide-react";

import { Button } from "@/components/ui/button";
import type { HobbyOption } from "@/lib/api";
import { cn } from "@/lib/utils";

export const MAX_HOBBIES = 8;
const MAX_OWN = 2;
const OWN_HOBBY = /^[A-Za-z][A-Za-z &'-]{1,23}$/;
// Mirrors the server's block list (src/learner/diagnostic.py, _UNSUITABLE_HOBBY_RE) so a student hears about it
// where they typed it, not four screens later when the survey is sent. The server is still the authority.
const UNSUITABLE_HOBBY =
  /(?<![a-z])(gambl|bet(s|ting)?(?![a-z])|casino|poker|lotter|vap(e|es|ing)(?![a-z])|smok|cigar|drug|weed(?![a-z])|alcohol|beer|wine(?![a-z])|whisk|vodka|drunk|bomb|weapon|guns?(?![a-z])|sex|porn|nude|dating|kiss|kill|suicid|self.?harm|hurt.?my|ignore|instruction|prompt|jailbreak)/i;

export function HobbyPicker({
  options,
  value,
  onChange,
  heading = "What do you enjoy?",
  blurb = "Tap a few. Your lessons stay in the interest you chose; your hobbies shape the short personal story at the start of each lesson. Optional.",
}: {
  options: HobbyOption[];
  value: string[];
  onChange: (next: string[]) => void;
  heading?: string;
  blurb?: string;
}) {
  const [own, setOwn] = useState("");
  const [ownError, setOwnError] = useState<string | null>(null);
  const listed = new Set(options.map((o) => o.id));
  const ownOnes = value.filter((h) => !listed.has(h));
  const full = value.length >= MAX_HOBBIES;

  function toggle(id: string) {
    if (value.includes(id)) onChange(value.filter((h) => h !== id));
    else if (!full) onChange([...value, id]);
  }

  function addOwn() {
    const label = own.trim();
    if (!label) return;
    if (!OWN_HOBBY.test(label)) {
      setOwnError("Keep it short: letters and spaces, up to 24 characters.");
      return;
    }
    if (UNSUITABLE_HOBBY.test(label)) {
      setOwnError("That one can't be used for lessons. Pick one from the list, or type a different one.");
      return;
    }
    if (ownOnes.length >= MAX_OWN || full) {
      setOwnError(`You can add up to ${MAX_OWN} of your own.`);
      return;
    }
    setOwnError(null);
    setOwn("");
    if (!value.includes(label.toLowerCase())) onChange([...value, label.toLowerCase()]);
  }

  return (
    <div className="flex flex-col gap-5">
      <div className="flex flex-col gap-2">
        <h1 className="display text-4xl font-semibold text-foreground">{heading}</h1>
        <p className="text-muted-foreground">{blurb}</p>
      </div>

      <ul className="grid grid-cols-3 gap-2.5 sm:grid-cols-4">
        {options.map((o) => {
          const on = value.includes(o.id);
          return (
            <li key={o.id}>
              <button
                type="button"
                aria-pressed={on}
                disabled={!on && full}
                onClick={() => toggle(o.id)}
                className={cn(
                  "relative flex w-full flex-col items-center gap-1 rounded-[18px] border p-3 text-center text-sm font-semibold transition-all duration-150 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:opacity-40",
                  on
                    ? "-translate-y-0.5 border-primary bg-[color-mix(in_srgb,var(--brand)_9%,var(--surface))] text-primary"
                    : "border-border bg-card text-foreground hover:-translate-y-0.5 hover:border-[color-mix(in_srgb,var(--brand)_50%,var(--line))]",
                )}
              >
                <span aria-hidden className={cn("text-3xl", on && "rm-pop")}>
                  {o.emoji}
                </span>
                <span className="leading-tight">{o.label}</span>
                {on && (
                  <span className="rm-pop absolute right-1.5 top-1.5 flex size-5 items-center justify-center rounded-full bg-primary text-primary-foreground">
                    <Check className="size-3" strokeWidth={3} aria-hidden />
                  </span>
                )}
              </button>
            </li>
          );
        })}
        {ownOnes.map((h) => (
          <li key={h}>
            <button
              type="button"
              aria-pressed
              onClick={() => toggle(h)}
              className="relative flex w-full flex-col items-center gap-1 rounded-[18px] border border-primary bg-[color-mix(in_srgb,var(--brand)_9%,var(--surface))] p-3 text-center text-sm font-semibold capitalize text-primary"
            >
              <span aria-hidden className="text-3xl">
                ✨
              </span>
              <span className="leading-tight">{h}</span>
              <span className="absolute right-1.5 top-1.5 flex size-5 items-center justify-center rounded-full bg-primary text-primary-foreground">
                <Check className="size-3" strokeWidth={3} aria-hidden />
              </span>
            </button>
          </li>
        ))}
      </ul>

      <p className="text-sm text-muted-foreground" aria-live="polite">
        {value.length === 0 ? "None picked yet." : `${value.length} of ${MAX_HOBBIES} picked.`}
      </p>

      <div className="flex flex-col gap-1">
        <label htmlFor="own-hobby" className="text-sm font-semibold text-muted-foreground">
          Something else?
        </label>
        <div className="flex max-w-sm gap-2">
          <input
            id="own-hobby"
            value={own}
            maxLength={24}
            onChange={(e) => setOwn(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                e.preventDefault();
                addOwn();
              }
            }}
            placeholder="e.g. kite flying"
            className="h-11 flex-1 rounded-xl border border-input bg-card px-3 text-sm text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          />
          <Button type="button" variant="outline" onClick={addOwn}>
            Add
          </Button>
        </div>
        {ownError && <p className="text-sm text-destructive">{ownError}</p>}
      </div>
    </div>
  );
}
