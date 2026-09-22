// Assessment page (/assessment) — answer the concept's check question and get
// a live grade. Client Component inside <RequireAuth>; ?chapter= and ?concept=
// come from the URL, the student from the session cookie.
//
// Flow: fetch the current concept + its check_question (getNextLesson) → student
// answers → submitAssessment (live grade, writes mastery to the backend store) →
// show a colored result → offer next actions.

"use client";

import { Suspense, useState } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { CheckCircle2, AlertCircle, XCircle, ArrowRight, RotateCcw } from "lucide-react";

import {
  friendlyMessage,
  getNextLesson,
  submitAssessment,
  type AssessmentResult,
  type NextLesson,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
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
    blurb: "You nailed it — this concept is now marked mastered on your roadmap.",
  },
  partial: {
    card: "border-brand-accent/30 bg-brand-accent/5",
    accent: "text-brand-accent",
    Icon: AlertCircle,
    title: "Almost there",
    blurb: "You passed, but not full marks yet. Move on, or try again to master it.",
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
  const loadError =
    next.error ??
    (next.data && !conceptId ? (next.data.reason ?? "No concept to assess right now.") : null);

  // Answer + grading state. For multiple choice the answer is the option letter.
  const [answer, setAnswer] = useState("");
  const [grading, setGrading] = useState(false);
  const [submitError, setSubmitError] = useState<string | null>(null);
  const [result, setResult] = useState<AssessmentResult | null>(null);

  async function handleSubmit() {
    if (!conceptId || !answer.trim() || grading) return;
    setGrading(true);
    setSubmitError(null);
    try {
      const res = await submitAssessment(conceptId, answer.trim());
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
    setSubmitError(null);
  }

  // ----- Guard states -----
  if (loading) {
    return (
      <Centered>
        <div className="h-8 w-64 animate-pulse rounded-lg bg-muted" />
        <div className="h-40 w-full max-w-xl animate-pulse rounded-xl bg-muted" />
      </Centered>
    );
  }
  if (loadError) {
    return (
      <Centered>
        <p className="max-w-md text-muted-foreground">{loadError}</p>
        <PrimaryButton asChild>
          <Link href={roadmapHref}>← Back to roadmap</Link>
        </PrimaryButton>
      </Centered>
    );
  }

  // ----- Result view -----
  if (result) {
    const tier = RESULT[result.mastery_signal] ?? RESULT.not_yet;
    const passed = result.score >= 2;
    return (
      <main className="flex flex-1 flex-col">
        <PageContainer className="flex max-w-2xl flex-col gap-6">
          <Card className={cn("shadow-card", tier.card)}>
            <CardHeader>
              <CardTitle
                className={cn("flex items-center gap-2 text-xl", tier.accent)}
              >
                <tier.Icon className="size-6" />
                {tier.title}
              </CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col gap-5">
              {/* What happened. For multiple choice a score out of 3 means
                  nothing to a student, so show the letters instead. */}
              {result.correct === undefined ? (
                <div className="flex items-baseline gap-2">
                  <span className={cn("text-4xl font-bold", tier.accent)}>{result.score}</span>
                  <span className="text-lg text-muted-foreground">/ 3</span>
                  <span className="ml-2 text-sm text-muted-foreground">{tier.blurb}</span>
                </div>
              ) : (
                <p className="text-sm text-muted-foreground">
                  You chose{" "}
                  <span className={cn("font-bold", tier.accent)}>{result.selected_option}</span>
                  {!result.correct && (
                    <>
                      ; the right answer is{" "}
                      <span className="font-bold text-success">{result.correct_option}</span>
                    </>
                  )}
                  . {tier.blurb}
                </p>
              )}

              {/* Feedback — clearly separated */}
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

              {/* Next actions */}
              <div className="flex flex-wrap gap-3">
                {passed ? (
                  <PrimaryButton asChild>
                    <Link href={withChapter("/lesson", chapterId)}>
                      Continue to next concept <ArrowRight className="size-5" />
                    </Link>
                  </PrimaryButton>
                ) : (
                  <PrimaryButton onClick={tryAgain}>
                    <RotateCcw className="size-5" /> Try again
                  </PrimaryButton>
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
        </PageContainer>
      </main>
    );
  }

  // ----- Question view -----
  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex max-w-2xl flex-col gap-6">
        <div className="flex flex-col gap-1">
          <Link
            href={lessonHref}
            className="text-sm font-medium text-muted-foreground hover:text-foreground"
          >
            ← Lesson
          </Link>
          <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
            Quick check
          </span>
          <h1 className="text-3xl font-bold tracking-tight text-foreground">
            {conceptName}
          </h1>
        </div>

        <Card className="shadow-card">
          <CardHeader>
            <CardTitle className="text-base text-foreground">The question</CardTitle>
          </CardHeader>
          <CardContent className="flex flex-col gap-5">
            <Markdown>{question}</Markdown>

            {options.length > 0 ? (
              // Multiple choice: one radio group, so arrow keys move between
              // options and a screen reader announces "2 of 4".
              <fieldset className="flex flex-col gap-3" disabled={grading}>
                <legend className="sr-only">Choose one answer</legend>
                {options.map(([letter, text]) => (
                  <label
                    key={letter}
                    className={cn(
                      "flex cursor-pointer items-start gap-3 rounded-xl border p-4 transition-all",
                      answer === letter
                        ? "border-primary bg-primary/5 ring-2 ring-primary"
                        : "border-border bg-card hover:border-primary/40 hover:shadow-soft",
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
                        "flex size-7 shrink-0 items-center justify-center rounded-full border text-sm font-bold",
                        answer === letter
                          ? "border-primary bg-primary text-white"
                          : "border-border text-muted-foreground",
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

            {submitError && (
              <p className="rounded-xl border border-destructive/30 bg-destructive/5 px-4 py-3 text-sm text-destructive">
                {submitError}
              </p>
            )}

            <PrimaryButton
              onClick={handleSubmit}
              disabled={grading || !answer.trim()}
              className="self-start"
            >
              {grading ? "Checking…" : options.length > 0 ? "Check my answer" : "Submit answer"}
            </PrimaryButton>
          </CardContent>
        </Card>
      </PageContainer>
    </main>
  );
}

function Centered({ children }: { children: React.ReactNode }) {
  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-1 flex-col items-center justify-center gap-6 text-center">
        {children}
      </PageContainer>
    </main>
  );
}
