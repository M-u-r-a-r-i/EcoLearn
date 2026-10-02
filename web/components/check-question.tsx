// One multiple-choice question with an honest "I'm not sure yet" option, as
// used by the starting check (/start) and the end check (/end-check). Nothing
// is graded here: the pick is sent with the rest at the end, and the answer
// key never reaches the browser.

"use client";

import { HelpCircle } from "lucide-react";

import { Markdown } from "@/components/markdown";
import type { DiagnosticQuestion } from "@/lib/api";
import { cn } from "@/lib/utils";

export const UNSURE = "unsure";

export function CheckQuestion({
  question,
  picked,
  onPick,
  disabled,
}: {
  question: DiagnosticQuestion;
  picked: string | undefined;
  onPick: (value: string) => void;
  disabled?: boolean;
}) {
  return (
    <section className="flex flex-col gap-5 rounded-xl border border-border bg-card p-6 shadow-card">
      <Markdown>{question.question}</Markdown>
      <fieldset className="flex flex-col gap-3" disabled={disabled}>
        <legend className="sr-only">Choose one answer, or Not sure</legend>
        {Object.entries(question.options).map(([letter, text]) => (
          <label
            key={letter}
            className={cn(
              "flex cursor-pointer items-start gap-3 rounded-xl border p-4 transition-all",
              picked === letter
                ? "border-primary bg-primary/5 ring-2 ring-primary"
                : "border-border bg-card hover:border-primary/40 hover:shadow-soft",
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
                "flex size-7 shrink-0 items-center justify-center rounded-full border text-sm font-bold",
                picked === letter ? "border-primary bg-primary text-primary-foreground" : "border-border text-muted-foreground",
              )}
            >
              {letter}
            </span>
            <Markdown className="prose-sm">{text}</Markdown>
          </label>
        ))}
        <label
          className={cn(
            "flex cursor-pointer items-center gap-3 rounded-xl border border-dashed p-4 text-sm transition-all",
            picked === UNSURE
              ? "border-brand-accent bg-brand-accent/5 ring-2 ring-brand-accent"
              : "border-border text-muted-foreground hover:border-brand-accent/50",
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
      </fieldset>
    </section>
  );
}
