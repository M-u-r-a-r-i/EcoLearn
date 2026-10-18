// "How sure are you?" — one tap after picking an option, in every check.
//
// WHY: a wrong answer the student was SURE of is a firmly held misconception;
// a wrong guess may just be a guess. Teachers see the difference, and the
// pilot can compare how sure students were with how right they were.

"use client";

import type { Confidence } from "@/lib/api";
import { cn } from "@/lib/utils";

export const CONFIDENCE_OPTIONS: { value: Confidence; label: string }[] = [
  { value: "sure", label: "I'm sure" },
  { value: "think", label: "I think so" },
  { value: "guess", label: "Just guessing" },
];

export function ConfidencePicker({
  name,
  value,
  onChange,
  disabled,
}: {
  name: string;
  value: Confidence | undefined;
  onChange: (value: Confidence) => void;
  disabled?: boolean;
}) {
  return (
    <fieldset className="flex flex-col gap-2" disabled={disabled}>
      <legend className="mb-2 text-sm font-semibold text-foreground">How sure are you?</legend>
      <div className="flex flex-wrap gap-2">
        {CONFIDENCE_OPTIONS.map((o) => (
          <label
            key={o.value}
            className={cn(
              "cursor-pointer rounded-full border px-4 py-2 text-sm font-medium transition-colors has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-ring",
              value === o.value
                ? "border-primary bg-primary text-primary-foreground"
                : "border-border bg-card text-foreground hover:border-primary/50",
            )}
          >
            <input
              type="radio"
              name={`${name}-confidence`}
              value={o.value}
              checked={value === o.value}
              onChange={() => onChange(o.value)}
              className="sr-only"
            />
            {o.label}
          </label>
        ))}
      </div>
    </fieldset>
  );
}
