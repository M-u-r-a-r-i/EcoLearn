// Lesson page (/lesson) — the personalised lesson for the student's next concept.
//
// Client Component: like the roadmap, the data depends on the client-only
// student_id (React Context), so we fetch in the browser with useEffect.

"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { ArrowRight, Lightbulb } from "lucide-react";

import { getNextLesson, type NextLesson } from "@/lib/api";
import { useStudent } from "@/components/student-provider";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { Markdown } from "@/components/markdown";
import { HelpWidget } from "@/components/help-widget";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const CHAPTER_ID = "motion_straight_line";

export default function LessonPage() {
  const { student } = useStudent();

  const [data, setData] = useState<NextLesson | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!student) {
      setLoading(false);
      return;
    }
    let cancelled = false;
    setLoading(true);
    setError(null);
    getNextLesson(student.student_id, CHAPTER_ID)
      .then((d) => !cancelled && setData(d))
      .catch(
        () =>
          !cancelled &&
          setError(
            "Couldn't load the lesson. Make sure the backend is running on " +
              (process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000") +
              ".",
          ),
      )
      .finally(() => !cancelled && setLoading(false));
    return () => {
      cancelled = true;
    };
  }, [student]);

  // ----- No student (e.g. page reloaded → context cleared) -----
  if (!student) {
    return (
      <Centered>
        <h1 className="text-2xl font-bold text-foreground">No student yet</h1>
        <p className="text-muted-foreground">
          Start at onboarding to create your learner profile.
        </p>
        <PrimaryButton asChild>
          <Link href="/onboarding">Go to onboarding</Link>
        </PrimaryButton>
      </Centered>
    );
  }

  if (loading) return <LessonSkeleton />;

  if (error) {
    return (
      <Centered>
        <p className="rounded-xl border border-destructive/30 bg-destructive/5 px-4 py-3 text-sm text-destructive">
          {error}
        </p>
        <PrimaryButton asChild>
          <Link href="/roadmap">← Back to roadmap</Link>
        </PrimaryButton>
      </Centered>
    );
  }

  // ----- Non-teaching states: done / blocked / lesson_missing -----
  if (!data || !data.lesson || data.status === "done" || data.status === "blocked") {
    return (
      <Centered>
        <h1 className="text-2xl font-bold text-foreground">
          {data?.status === "done" ? "🎉 Chapter complete!" : "Nothing to learn just yet"}
        </h1>
        <p className="max-w-md text-muted-foreground">
          {data?.reason ?? "Head back to your roadmap."}
        </p>
        <PrimaryButton asChild>
          <Link href="/roadmap">← Back to roadmap</Link>
        </PrimaryButton>
      </Centered>
    );
  }

  const { lesson, concept_name, status, reason } = data;

  return (
    <main className="flex flex-1 flex-col">
      {/* ~720px reading column with generous vertical rhythm. */}
      <PageContainer className="flex max-w-[720px] flex-col gap-8">
        {/* Title block */}
        <header className="flex flex-col gap-2">
          <Link
            href="/roadmap"
            className="text-sm font-medium text-muted-foreground hover:text-foreground"
          >
            ← Roadmap
          </Link>
          <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
            {status === "review" ? "Quick review" : "Lesson"}
          </span>
          <h1 className="text-4xl font-bold leading-tight tracking-tight text-foreground">
            {concept_name}
          </h1>
          {reason && <p className="text-muted-foreground">{reason}</p>}
        </header>

        {/* Explanation — clean prose via the Markdown renderer */}
        <article>
          <Markdown>{lesson.body}</Markdown>
        </article>

        {/* Worked example — subtly amber-tinted callout */}
        {lesson.worked_example?.trim() && (
          <Card className="border-brand-accent/30 bg-brand-accent/5 shadow-soft">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-base text-foreground">
                <Lightbulb className="size-5 text-brand-accent" />
                Worked example
              </CardTitle>
            </CardHeader>
            <CardContent>
              <Markdown>{lesson.worked_example}</Markdown>
            </CardContent>
          </Card>
        )}

        {/* Check question — clearly set apart */}
        {lesson.check_question?.trim() && (
          <Card className="border-primary/20 bg-card shadow-card">
            <CardHeader>
              <CardTitle className="text-base text-foreground">
                Check yourself
              </CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col gap-5">
              <Markdown>{lesson.check_question}</Markdown>
              <PrimaryButton asChild className="self-start">
                <Link href="/assessment">
                  Take the quick check <ArrowRight className="size-5" />
                </Link>
              </PrimaryButton>
            </CardContent>
          </Card>
        )}

        {/* "I'm stuck" help widget — live tutor, stays on the lesson. */}
        <HelpWidget studentId={student.student_id} conceptId={lesson.concept_id} />
      </PageContainer>
    </main>
  );
}

// Small helper for the centered single-message states.
function Centered({ children }: { children: React.ReactNode }) {
  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-1 flex-col items-center justify-center gap-6 text-center">
        {children}
      </PageContainer>
    </main>
  );
}

// Loading skeleton that mirrors the reading layout.
function LessonSkeleton() {
  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex max-w-[720px] flex-col gap-6">
        <div className="h-10 w-2/3 animate-pulse rounded-lg bg-muted" />
        <div className="flex flex-col gap-3">
          {Array.from({ length: 6 }).map((_, i) => (
            <div
              key={i}
              className="h-4 animate-pulse rounded bg-muted"
              style={{ width: `${90 - (i % 3) * 12}%` }}
            />
          ))}
        </div>
        <div className="h-40 animate-pulse rounded-xl bg-muted" />
        <div className="h-32 animate-pulse rounded-xl bg-muted" />
      </PageContainer>
    </main>
  );
}
