// Assessment page (/assessment) — answer the concept's check question and get
// a live grade. Client Component inside <RequireAuth>; ?chapter= and ?concept=
// come from the URL, the student from the session cookie.
//
// Flow: fetch the concept + its check (getNextLesson) → pick an option → say how
// sure you are → submitAssessment (graded on the server, writes mastery) → a
// result screen. Multiple choice (every authored lesson) gets the interactive
// version below; an older generated lesson with a free-text question keeps the
// plain form and result.

"use client";

import { Suspense, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import {
  CheckCircle2,
  XCircle,
  ArrowRight,
  BookOpen,
  Lightbulb,
  RotateCcw,
  Trophy,
} from "lucide-react";

import {
  friendlyMessage,
  getNextLesson,
  submitAssessment,
  type AssessmentResult,
  type Confidence,
  type NextLesson,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { AiPractice } from "@/components/ai-practice";
import { Confetti, MasteryTrack, OptionReview } from "@/components/check-feedback";
import { ConfidencePicker } from "@/components/confidence-picker";
import { Pill, Skeleton } from "@/components/ui-kit";
import { Button } from "@/components/ui/button";
import { Markdown } from "@/components/markdown";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useChapter, withChapter } from "@/lib/use-chapter";
import { cn } from "@/lib/utils";

// Result styling by tier. Green = mastered (pass), amber = partial, red = not yet.
const RESULT = {
  mastered: {
    card: "border-success/30 bg-success/5",
    accent: "text-success",
    Icon: CheckCircle2,
    title: "Mastered!",
    blurb: "Two different questions right: this concept is now mastered on your roadmap.",
  },
  // Since 2026-10-03 a right answer is "partial" until a SECOND, different
  // question on the idea is right too (the revision list asks it).
  partial: {
    card: "border-success/30 bg-success/5",
    accent: "text-success",
    Icon: CheckCircle2,
    title: "Right!",
    blurb: "One more right answer, on a different question, masters it.",
  },
  not_yet: {
    card: "border-destructive/30 bg-destructive/5",
    accent: "text-destructive",
    Icon: XCircle,
    title: "Not quite yet",
    blurb: "Give it another go — re-read the lesson and try the check again.",
  },
} as const;

export default function AssessmentPage() {
  return (
    <Suspense>
      <Assessment />
    </Suspense>
  );
}

function typingInto(target: EventTarget | null): boolean {
  const el = target as HTMLElement | null;
  if (!el) return false;
  // A radio is where focus lands after picking an option: it must not block
  // the shortcuts. Text fields and buttons/links (which own Enter) do.
  if (el instanceof HTMLInputElement && (el.type === "radio" || el.type === "checkbox")) return false;
  return el.isContentEditable || ["INPUT", "TEXTAREA", "SELECT", "BUTTON", "A"].includes(el.tagName);
}

function Assessment() {
  const { chapterId } = useChapter();
  const conceptParam = useSearchParams().get("concept") ?? undefined;
  const roadmapHref = withChapter("/roadmap", chapterId);
  const lessonHref = withChapter("/lesson", chapterId, conceptParam ? { concept: conceptParam } : {});

  // The concept + its check question (loaded from getNextLesson).
  const next = useFetch<NextLesson>(`${chapterId}|${conceptParam ?? ""}`, () =>
    getNextLesson(chapterId, conceptParam),
  );
  const loading = next.loading;
  const conceptId = next.data?.lesson ? next.data.concept_id : null;
  const conceptName = next.data?.concept_name ?? "";
  // Authored lessons carry a multiple-choice check; the older generated ones
  // only have a question to answer in prose.
  const check = next.data?.lesson?.check ?? null;
  const question = check?.question ?? next.data?.lesson?.check_question ?? "";
  const options = check ? Object.entries(check.options) : [];
  const multipleChoice = options.length > 0;
  const loadError =
    next.error ??
    (next.data && !conceptId ? (next.data.reason ?? "No concept to assess right now.") : null);

  // Answer + grading state. For multiple choice the answer is the option letter.
  const [answer, setAnswer] = useState("");
  // "How sure are you?" — asked for multiple choice only, once an option is picked.
  const [confidence, setConfidence] = useState<Confidence | undefined>();
  const [grading, setGrading] = useState(false);
  const [submitError, setSubmitError] = useState<string | null>(null);
  const [result, setResult] = useState<AssessmentResult | null>(null);

  const ready = Boolean(conceptId) && answer.trim() !== "" && (!multipleChoice || Boolean(confidence));

  async function handleSubmit() {
    if (!conceptId || !ready || grading) return;
    setGrading(true);
    setSubmitError(null);
    try {
      const res = await submitAssessment(conceptId, answer.trim(), confidence);
      setResult(res);
    } catch (err) {
      setSubmitError(
        friendlyMessage(err) ||
          "Couldn't record that right now — your progress wasn't changed. Please try again.",
      );
    } finally {
      setGrading(false);
    }
  }

  function tryAgain() {
    // Re-attempt the SAME concept: clear the result, keep the question.
    setResult(null);
    setAnswer("");
    setConfidence(undefined);
    setSubmitError(null);
  }

  // Keyboard: A–D (or 1–4) pick an option, Enter checks. Only on the question
  // screen, never while the student is on a button or link (Enter would double up).
  const submitRef = useRef(handleSubmit);
  useEffect(() => {
    submitRef.current = handleSubmit;
  });
  const letters = options.map(([letter]) => letter).join("");
  useEffect(() => {
    if (!multipleChoice || result || grading) return;
    function onKey(e: KeyboardEvent) {
      if (e.metaKey || e.ctrlKey || e.altKey || typingInto(e.target)) return;
      if (e.key === "Enter") {
        submitRef.current();
        return;
      }
      const key = e.key.toUpperCase();
      const byLetter = letters.includes(key) && key.length === 1 ? key : undefined;
      const byNumber = /^[1-9]$/.test(key) ? letters[Number(key) - 1] : undefined;
      const pick = byLetter ?? byNumber;
      if (pick) setAnswer(pick);
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [multipleChoice, result, grading, letters]);

  // ----- Guard states -----
  if (loading) {
    return (
      <Centered>
        <div className="surface">
          <Skeleton rows={4} />
        </div>
      </Centered>
    );
  }
  if (loadError) {
    return (
      <Centered>
        <div className="empty-state">
          <span className="empty-spark" aria-hidden>
            ✳
          </span>
          <h3>Nothing to check yet</h3>
          <p>{loadError}</p>
          <Button asChild>
            <Link href={roadmapHref}>← Back to your path</Link>
          </Button>
        </div>
      </Centered>
    );
  }

  // ----- Result view: multiple choice -----
  if (result && multipleChoice && result.correct !== undefined) {
    const right = result.correct;
    const mastered = result.mastery_signal === "mastered";
    return (
      <main className="page-shell w-full flex-1">
        <div className="mx-auto w-full flex max-w-2xl flex-col gap-5">
          {/* The verdict */}
          <section
            aria-live="polite"
            className={cn(
              "surface relative overflow-hidden p-8 text-center",
              right && "!border-[color-mix(in_srgb,var(--brand)_45%,var(--line))] !bg-[color-mix(in_srgb,var(--brand)_9%,var(--surface))]",
            )}
          >
            {right && <Confetti />}
            <div
              className={cn(
                "rm-pop mx-auto flex size-16 items-center justify-center rounded-full",
                mastered
                  ? "bg-[#d9e9b0] text-[#3b713e] dark:bg-[#516b3e] dark:text-[#e1f3b3]"
                  : right
                    ? "bg-primary text-primary-foreground"
                    : "bg-brand-accent/15 text-brand-accent",
              )}
            >
              {mastered ? (
                <Trophy className="size-8" />
              ) : right ? (
                <CheckCircle2 className="size-8" />
              ) : (
                <Lightbulb className="size-8" />
              )}
            </div>
            <h1 className="display mt-4 text-3xl font-semibold text-foreground">
              {mastered ? "Mastered!" : right ? "Right!" : "Not quite, and that's useful"}
            </h1>
            <p className="mx-auto mt-2 max-w-md text-muted-foreground">
              {right
                ? (result.mastery_note ?? RESULT[result.mastery_signal]?.blurb)
                : "A wrong answer shows exactly what to fix. Read why below, then give it another go."}
            </p>
          </section>

          {/* The question, with what they chose and what was right */}
          <section className="flex flex-col gap-4 surface p-5">
            <Markdown>{question}</Markdown>
            <OptionReview
              options={options}
              selected={result.selected_option ?? ""}
              correct={result.correct_option ?? ""}
            />
          </section>

          {/* Why */}
          <section className="flex flex-col gap-2 surface p-5">
            <h2 className="eyebrow flex items-center gap-2">
              <Lightbulb className="size-4" aria-hidden /> Why
            </h2>
            <Markdown className="prose-sm">{result.feedback || "_No feedback returned._"}</Markdown>
            {result.missing_concepts.length > 0 && (
              <p className="mt-1 text-xs text-muted-foreground">
                Worth revisiting: {result.missing_concepts.join(", ")}
              </p>
            )}
          </section>

          {/* The road to mastered */}
          {right && (
            <section className="surface p-5">
              <MasteryTrack signal={mastered ? "mastered" : "partial"} />
              {!mastered && (
                <p className="mt-3 text-center text-xs text-muted-foreground">
                  A new question on this idea (in Review, about a day from now) makes it mastered.
                </p>
              )}
            </section>
          )}

          {/* What next */}
          <div className="flex flex-wrap gap-3">
            {right ? (
              <Button asChild>
                <Link href={withChapter("/lesson", chapterId)}>
                  Continue to next concept <ArrowRight className="size-5" />
                </Link>
              </Button>
            ) : (
              <>
                <Button onClick={tryAgain}>
                  <RotateCcw className="size-5" /> Try again
                </Button>
                <Button variant="outline" size="lg" asChild>
                  <Link href={lessonHref}>
                    <BookOpen className="size-4" /> Re-read the lesson
                  </Link>
                </Button>
              </>
            )}
            <Button variant="outline" size="lg" asChild>
              <Link href={roadmapHref}>See roadmap</Link>
            </Button>
          </div>

          {/* Optional extra practice, written by AI; never counts. Hidden when the AI is off. */}
          {next.data?.practice_available && conceptId && <AiPractice conceptId={conceptId} />}
        </div>
      </main>
    );
  }

  // ----- Result view: older free-text lessons -----
  if (result) {
    const tier = RESULT[result.mastery_signal] ?? RESULT.not_yet;
    const passed = result.score >= 2;
    return (
      <main className="page-shell w-full flex-1">
        <div className="mx-auto w-full flex max-w-2xl flex-col gap-6">
          <Card className={cn(tier.card)}>
            <CardHeader>
              <CardTitle className={cn("flex items-center gap-2 text-xl", tier.accent)}>
                <tier.Icon className="size-6" />
                {tier.title}
              </CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col gap-5">
              <div className="flex items-baseline gap-2">
                <span className={cn("text-4xl font-bold", tier.accent)}>{result.score}</span>
                <span className="text-lg text-muted-foreground">/ 3</span>
                <span className="ml-2 text-sm text-muted-foreground">{tier.blurb}</span>
              </div>

              <div className="flex flex-col gap-1 rounded-xl border border-border bg-card p-4">
                <span className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
                  Feedback
                </span>
                <Markdown className="prose-sm">
                  {result.feedback || "_No feedback returned._"}
                </Markdown>
                {result.missing_concepts.length > 0 && (
                  <p className="mt-2 text-xs text-muted-foreground">
                    Worth revisiting: {result.missing_concepts.join(", ")}
                  </p>
                )}
              </div>

              <div className="flex flex-wrap gap-3">
                {passed ? (
                  <Button asChild>
                    <Link href={withChapter("/lesson", chapterId)}>
                      Continue to next concept <ArrowRight className="size-5" />
                    </Link>
                  </Button>
                ) : (
                  <Button onClick={tryAgain}>
                    <RotateCcw className="size-5" /> Try again
                  </Button>
                )}
                {passed && (
                  <Button variant="outline" onClick={tryAgain}>
                    <RotateCcw className="size-4" /> Try again
                  </Button>
                )}
                <Button variant="outline" asChild>
                  <Link href={roadmapHref}>See roadmap</Link>
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </main>
    );
  }

  // ----- Question view -----
  const hint = !answer
    ? "Pick an answer. You can also press A–D."
    : multipleChoice && !confidence
      ? "Now say how sure you are."
      : "Ready. Press Enter or tap Check.";

  return (
    <main className="page-shell w-full flex-1">
      <div className="mx-auto w-full flex max-w-2xl flex-col gap-6">
        <div className="flex flex-col gap-2">
          <Link href={lessonHref} className="back-link">
            ← Lesson
          </Link>
          <div className="mt-2">
            <Pill>QUICK CHECK</Pill>
          </div>
          <h1 className="display text-3xl font-semibold text-foreground sm:text-4xl">{conceptName}</h1>
        </div>

        <section className="surface flex flex-col gap-5 p-5 sm:p-6">
          <Markdown>{question}</Markdown>

          {/* The profile's "sure but wrong" insight (About me): a calm nudge, never a block. */}
          {multipleChoice && next.data?.prefs?.slow_down && (
            <p className="rounded-lg border border-border bg-muted/40 px-3 py-2 text-sm text-muted-foreground">
              Before you pick: read each option once more. The wrong ones are written to feel right.
            </p>
          )}

          {multipleChoice ? (
            // One radio group, so arrow keys move between options and a screen
            // reader announces "2 of 4". Visually: big tappable cards.
            <fieldset className="flex flex-col gap-3" disabled={grading}>
              <legend className="sr-only">Choose one answer</legend>
              {options.map(([letter, text]) => (
                <label
                  key={letter}
                  className={cn(
                    "flex cursor-pointer items-start gap-3 rounded-[13px] border p-3.5 transition-all duration-150 has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-ring",
                    answer === letter
                      ? "border-primary bg-[color-mix(in_srgb,var(--brand)_9%,var(--surface))]"
                      : "border-border bg-card hover:-translate-y-px hover:border-[color-mix(in_srgb,var(--brand)_50%,var(--line))]",
                  )}
                >
                  <input
                    type="radio"
                    name="answer"
                    value={letter}
                    checked={answer === letter}
                    onChange={() => setAnswer(letter)}
                    className="sr-only"
                  />
                  <span
                    className={cn(
                      "flex size-7 shrink-0 items-center justify-center rounded-[9px] font-heading text-xs font-bold transition-colors",
                      answer === letter
                        ? "bg-primary text-primary-foreground"
                        : "bg-secondary text-muted-foreground",
                    )}
                    aria-hidden
                  >
                    {letter}
                  </span>
                  <Markdown className="prose-sm">{text}</Markdown>
                </label>
              ))}
            </fieldset>
          ) : (
            // Legacy generated lesson: free text, graded by the Assessor.
            <textarea
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              disabled={grading}
              rows={6}
              placeholder="Explain your reasoning…"
              className="w-full rounded-xl border border-border bg-card p-3 text-sm text-foreground outline-none transition-colors focus:border-primary focus:ring-2 focus:ring-primary/20 disabled:opacity-60"
            />
          )}

          {multipleChoice && answer && (
            <div className="rm-sheet">
              <ConfidencePicker
                name="answer"
                value={confidence}
                onChange={setConfidence}
                disabled={grading}
              />
            </div>
          )}

          {submitError && (
            <p role="alert" className="inline-alert">
              {submitError}
            </p>
          )}
        </section>

        {/* The one action, always in reach, saying what's still needed. */}
        <div className="sticky bottom-20 z-20 flex items-center justify-between gap-3 rounded-[18px] border border-border bg-card/95 p-2.5 pl-4 shadow-card-hover backdrop-blur md:bottom-3">
          <span role="status" className="text-sm text-muted-foreground">
            {hint}
          </span>
          <Button
            onClick={handleSubmit}
            disabled={grading || !ready}
            className="shrink-0"
          >
            {grading ? "Checking…" : multipleChoice ? "Check my answer" : "Submit answer"}
          </Button>
        </div>
      </div>
    </main>
  );
}

function Centered({ children }: { children: React.ReactNode }) {
  return (
    <main className="page-shell w-full flex-1">
      <div className="mx-auto flex w-full max-w-xl flex-col gap-6">{children}</div>
    </main>
  );
}
