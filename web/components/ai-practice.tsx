// "Practice with AI": an extra multiple-choice question on the idea just studied, offered after the graded check.
//
// Written by the AI from this lesson, then solved by a second AI that never sees the answer; it is shown only if the
// two agree and our own rules pass it (server: src/learner/practice.py). It NEVER counts toward progress, mastery or
// marks, and the page says so. The answer key stays on the server until the student answers. When the AI is off (for
// this student or the server) the parent doesn't render this at all; when an attempt fails, it says so kindly.

"use client";

import { useState } from "react";
import { ArrowRight, CheckCircle2, Lightbulb, RefreshCw, Sparkles } from "lucide-react";

import { OptionReview } from "@/components/check-feedback";
import { Markdown } from "@/components/markdown";
import { Button } from "@/components/ui/button";
import { answerPractice, friendlyMessage, startPractice, type PracticeResult } from "@/lib/api";
import { cn } from "@/lib/utils";

type Question = { practice_id: number; question: string; options: Record<string, string> };

export function AiPractice({ conceptId }: { conceptId: string }) {
  const [question, setQuestion] = useState<Question | null>(null);
  const [picked, setPicked] = useState("");
  const [result, setResult] = useState<PracticeResult | null>(null);
  const [busy, setBusy] = useState<"writing" | "checking" | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  async function another() {
    setBusy("writing");
    setMessage(null);
    setResult(null);
    setPicked("");
    try {
      const made = await startPractice(conceptId);
      if (made.available) {
        setQuestion({ practice_id: made.practice_id, question: made.question, options: made.options });
      } else {
        setQuestion(null);
        setMessage(made.message);
      }
    } catch (err) {
      setMessage(friendlyMessage(err));
    } finally {
      setBusy(null);
    }
  }

  async function check() {
    if (!question || !picked) return;
    setBusy("checking");
    try {
      setResult(await answerPractice(question.practice_id, picked));
    } catch (err) {
      setMessage(friendlyMessage(err));
    } finally {
      setBusy(null);
    }
  }

  const options = question ? (Object.entries(question.options) as [string, string][]) : [];

  return (
    <section className="surface flex flex-col gap-4 p-5" aria-label="Practice with AI">
      <div>
        <p className="eyebrow flex items-center gap-2">
          <Sparkles className="size-3.5" aria-hidden /> Practice with AI
        </p>
        <p className="mt-1 text-sm text-muted-foreground">
          An extra question on this idea, just for practice. It doesn&apos;t count toward your progress.
        </p>
      </div>

      {busy === "writing" ? (
        <p className="flex items-center gap-2 text-sm text-foreground" role="status">
          <Sparkles className="size-4 animate-pulse text-primary" aria-hidden /> Writing a question and checking
          it… this can take a little while.
        </p>
      ) : !question ? (
        <>
          {message && <p className="text-sm text-muted-foreground" role="status">{message}</p>}
          <Button variant="outline" className="self-start" onClick={another}>
            <Sparkles className="size-4" aria-hidden /> {message ? "Try again" : "Give me a practice question"}
          </Button>
        </>
      ) : (
        <>
          <Markdown>{question.question}</Markdown>
          {result ? (
            <>
              <OptionReview options={options} selected={result.selected_option} correct={result.correct_option} />
              <div className="flex flex-col gap-2 rounded-[13px] border border-border bg-muted/30 p-4" role="status">
                <p className="flex items-center gap-2 font-semibold text-foreground">
                  {result.correct ? (
                    <>
                      <CheckCircle2 className="size-4 text-success" aria-hidden /> Right!
                    </>
                  ) : (
                    <>
                      <Lightbulb className="size-4 text-brand-accent" aria-hidden /> Not quite
                    </>
                  )}
                </p>
                {result.why_wrong && <p className="text-sm text-muted-foreground">{result.why_wrong}</p>}
                <Markdown className="prose-sm">{result.explanation}</Markdown>
              </div>
              <Button variant="outline" className="self-start" onClick={another}>
                <RefreshCw className="size-4" aria-hidden /> Another one
              </Button>
            </>
          ) : (
            <>
              <fieldset className="flex flex-col gap-3" disabled={busy === "checking"}>
                <legend className="sr-only">Choose one answer</legend>
                {options.map(([letter, text]) => (
                  <label
                    key={letter}
                    className={cn(
                      "flex cursor-pointer items-start gap-3 rounded-[13px] border p-3.5 transition-all duration-150 has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-ring",
                      picked === letter
                        ? "border-primary bg-[color-mix(in_srgb,var(--brand)_9%,var(--surface))]"
                        : "border-border bg-card hover:border-[color-mix(in_srgb,var(--brand)_50%,var(--line))]",
                    )}
                  >
                    <input
                      type="radio"
                      name={`practice-${question.practice_id}`}
                      value={letter}
                      checked={picked === letter}
                      onChange={() => setPicked(letter)}
                      className="sr-only"
                    />
                    <span
                      className={cn(
                        "flex size-7 shrink-0 items-center justify-center rounded-[9px] font-heading text-xs font-bold",
                        picked === letter ? "bg-primary text-primary-foreground" : "bg-secondary text-muted-foreground",
                      )}
                      aria-hidden
                    >
                      {letter}
                    </span>
                    <Markdown className="prose-sm">{text}</Markdown>
                  </label>
                ))}
              </fieldset>
              <Button className="self-start" disabled={!picked || busy === "checking"} onClick={check}>
                {busy === "checking" ? "Checking…" : "Check my answer"} <ArrowRight className="size-4" aria-hidden />
              </Button>
            </>
          )}
          {message && <p className="text-sm text-muted-foreground" role="status">{message}</p>}
        </>
      )}

      <p className="text-xs text-muted-foreground">
        Written by AI from this lesson and solved by a second AI before you see it. It can still be wrong: if
        something looks off, ask your teacher.
      </p>
    </section>
  );
}
