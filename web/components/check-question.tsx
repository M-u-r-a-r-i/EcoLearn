// One multiple-choice question with an honest "I'm not sure yet" option, and
// "How sure are you?" once an option is picked, as
// used by the starting check (/start) and the end check (/end-check). Nothing
// is graded here: the pick is sent with the rest at the end, and the answer
// key never reaches the browser.

"use client";

import { HelpCircle } from "lucide-react";

import { ConfidencePicker } from "@/components/confidence-picker";
import { Markdown } from "@/components/markdown";
import type { Confidence, DiagnosticQuestion } from "@/lib/api";
import { cn } from "@/lib/utils";

export const UNSURE = "unsure";

export function CheckQuestion({
  question,
  picked,
  onPick,
  confidence,
  onConfidence,
  disabled,
  allowUnsure = true,
}: {
  question: DiagnosticQuestion;
  picked: string | undefined;
  onPick: (value: string) => void;
  confidence: Confidence | undefined;
  onConfidence: (value: Confidence) => void;
  disabled?: boolean;
  allowUnsure?: boolean; // revision questions need an answer, so they hide it
}) {
  return (
    <section className="surface flex flex-col gap-5 p-6">
      <Markdown>{question.question}</Markdown>
      <fieldset className="flex flex-col gap-3" disabled={disabled}>
        <legend className="sr-only">Choose one answer, or Not sure</legend>
        {Object.entries(question.options).map(([letter, text]) => (
          <label
            key={letter}
            className={cn(
              "flex cursor-pointer items-start gap-3 rounded-[13px] border p-3.5 transition-all has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-ring",
              picked === letter
                ? "border-primary bg-[color-mix(in_srgb,var(--brand)_9%,var(--surface))]"
                : "border-border bg-card hover:border-[color-mix(in_srgb,var(--brand)_50%,var(--line))]",
            )}
          >
            <input
              type="radio"
              name={question.concept_id}
              value={letter}
              checked={picked === letter}
              onChange={() => onPick(letter)}
              className="sr-only"
            />
            <span
              aria-hidden
              className={cn(
                "flex size-7 shrink-0 items-center justify-center rounded-[9px] font-heading text-xs font-bold",
                picked === letter ? "bg-primary text-primary-foreground" : "bg-secondary text-muted-foreground",
              )}
            >
              {letter}
            </span>
            <Markdown className="prose-sm">{text}</Markdown>
          </label>
        ))}
        {allowUnsure && (
          <label
            className={cn(
              "flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-[13px] border border-dashed p-3 text-xs font-semibold transition-all has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-ring",
              picked === UNSURE
                ? "border-primary bg-[color-mix(in_srgb,var(--brand)_9%,var(--surface))] text-primary"
                : "border-border text-muted-foreground hover:text-foreground",
            )}
          >
            <input
              type="radio"
              name={question.concept_id}
              value={UNSURE}
              checked={picked === UNSURE}
              onChange={() => onPick(UNSURE)}
              className="sr-only"
            />
            <HelpCircle className="size-5 shrink-0" aria-hidden />
            I&apos;m not sure yet
          </label>
        )}
      </fieldset>
      {picked && picked !== UNSURE && (
        <ConfidencePicker
          name={question.concept_id}
          value={confidence}
          onChange={onConfidence}
          disabled={disabled}
        />
      )}
    </section>
  );
}
