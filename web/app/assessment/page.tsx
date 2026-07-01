// Assessment page (/assessment) — answer the concept's check question and get
// a live grade. Client Component (depends on the client-only student in Context).
//
// Flow: fetch the current concept + its check_question (getNextLesson) → student
// answers → submitAssessment (live grade, writes mastery to the backend store) →
// show a colored result → offer next actions.

"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { CheckCircle2, AlertCircle, XCircle, ArrowRight, RotateCcw } from "lucide-react";

import {
  getNextLesson,
  submitAssessment,
  type AssessmentResult,
} from "@/lib/api";
import { useStudent } from "@/components/student-provider";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";
import { Markdown } from "@/components/markdown";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { cn } from "@/lib/utils";

const CHAPTER_ID = "motion_straight_line";

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
  const { student } = useStudent();

  // Question state (loaded from getNextLesson).
  const [conceptId, setConceptId] = useState<string | null>(null);
  const [conceptName, setConceptName] = useState<string>("");
  const [question, setQuestion] = useState<string>("");
  const [loadError, setLoadError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  // Answer + grading state.
  const [answer, setAnswer] = useState("");
  const [grading, setGrading] = useState(false);
  const [submitError, setSubmitError] = useState<string | null>(null);
  const [result, setResult] = useState<AssessmentResult | null>(null);

  // Load the current concept + its check question.
  useEffect(() => {
    if (!student) {
      setLoading(false);
      return;
    }
    let cancelled = false;
    setLoading(true);
    getNextLesson(student.student_id, CHAPTER_ID)
      .then((d) => {
        if (cancelled) return;
        if (!d.lesson || !d.concept_id) {
          setLoadError(d.reason ?? "No concept to assess right now.");
          return;
        }
        setConceptId(d.concept_id);
        setConceptName(d.concept_name ?? "");
        setQuestion(d.lesson.check_question ?? "");
      })
      .catch(
        () =>
          !cancelled &&
          setLoadError(
            "Couldn't load the check question. Make sure the backend is running.",
          ),
      )
      .finally(() => !cancelled && setLoading(false));
    return () => {
      cancelled = true;
    };
  }, [student]);

  async function handleSubmit() {
    if (!conceptId || !answer.trim() || grading) return;
    setGrading(true);
    setSubmitError(null);
    try {
      const res = await submitAssessment(student!.student_id, conceptId, answer.trim());
      setResult(res);
    } catch {
      setSubmitError(
        "Couldn't grade that right now — your progress wasn't changed. Please try again.",
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
  if (!student) {
    return (
      <Centered>
        <h1 className="text-2xl font-bold text-foreground">No student yet</h1>
        <PrimaryButton asChild>
          <Link href="/onboarding">Go to onboarding</Link>
        </PrimaryButton>
      </Centered>
    );
  }
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
          <Link href="/roadmap">← Back to roadmap</Link>
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
              {/* Score — clearly separated */}
              <div className="flex items-baseline gap-2">
                <span className={cn("text-4xl font-bold", tier.accent)}>
                  {result.score}
                </span>
                <span className="text-lg text-muted-foreground">/ 3</span>
                <span className="ml-2 text-sm text-muted-foreground">
                  {tier.blurb}
                </span>
              </div>

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
                    <Link href="/lesson">
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
                  <Link href="/roadmap">See roadmap</Link>
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
            href="/lesson"
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

            <textarea
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              disabled={grading}
              rows={6}
              placeholder="Explain your reasoning…"
              className="w-full rounded-xl border border-border bg-card p-3 text-sm text-foreground outline-none transition-colors focus:border-primary focus:ring-2 focus:ring-primary/20 disabled:opacity-60"
            />

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
              {grading ? "Grading…" : "Submit answer"}
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
