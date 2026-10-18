// Lesson page (/lesson?chapter=...&concept=...) — the personalised lesson for
// the student's next concept, or for a specific concept when ?concept= is set.
//
// Client Component inside <RequireAuth>; the API knows the student from the
// session cookie, and the chapter/concept come from the URL.
//
// Since 2026-10-04 an authored lesson is a short run of steps (components/
// lesson-stepper.tsx): the story, the idea, an example to try, where the picture
// breaks, the takeaway, then the check. Older lessons with no sections keep the
// single-page layout. "Show everything on one page" is always one click away.

"use client";

import { Suspense, useState, type ReactNode } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import {
  ArrowRight,
  Atom,
  BookOpen,
  CircleHelp,
  Lightbulb,
  Sparkles,
  ThumbsDown,
  ThumbsUp,
  TriangleAlert,
  type LucideIcon,
} from "lucide-react";

import { getNextLesson, type LessonRating, type LessonSection, type NextLesson } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { useLessonView } from "@/lib/use-lesson-view";
import { useAuth } from "@/components/auth-provider";
import { cn } from "@/lib/utils";
import { EmptyState, Pill, Skeleton } from "@/components/ui-kit";
import { Markdown } from "@/components/markdown";
import { BreakNudge } from "@/components/break-nudge";
import { HelpWidget } from "@/components/help-widget";
import { LessonStepper, type LessonStep } from "@/components/lesson-stepper";
import { LessonStory } from "@/components/personal-story";
import { Button } from "@/components/ui/button";
import { useChapter, withChapter } from "@/lib/use-chapter";

export default function LessonPage() {
  return (
    <Suspense fallback={<LessonSkeleton />}>
      <LessonView />
    </Suspense>
  );
}

// What each authored section is called to a student, and how it's drawn.
type Look = { label: string; Icon: LucideIcon; kind: "plain" | "example" | "takeaway" | "caveat" };
function lookOf(heading: string): Look {
  if (/worked example/i.test(heading)) return { label: "Try an example", Icon: Lightbulb, kind: "example" };
  if (/picture breaks|breaks down/i.test(heading)) return { label: "Where it breaks", Icon: TriangleAlert, kind: "caveat" };
  if (/takeaway/i.test(heading)) return { label: "Remember this", Icon: Sparkles, kind: "takeaway" };
  if (/physics|idea|explanation/i.test(heading)) return { label: "The idea", Icon: Atom, kind: "plain" };
  return { label: heading, Icon: BookOpen, kind: "plain" };
}

function LessonView() {
  const { chapterId } = useChapter();
  const params = useSearchParams();
  const conceptParam = params.get("concept") ?? undefined;
  const stepParam = Number(params.get("step")) || 0; // set by the roadmap's lesson parts
  const roadmapHref = withChapter("/roadmap", chapterId);

  const { data, loading, error } = useFetch<NextLesson>(`${chapterId}|${conceptParam ?? ""}`, () =>
    getNextLesson(chapterId, conceptParam),
  );
  // Pilot metrics: the open, the reading time and the 👍/👎. Called before any
  // early return (hooks must run in the same order every render).
  const lessonView = useLessonView(loading || !data?.lesson ? null : data.lesson.concept_id);
  const { student } = useAuth();

  if (loading) return <LessonSkeleton />;

  if (error) {
    return (
      <Centered>
        <EmptyState title="Lesson paused." copy={error} href={roadmapHref} action="Back to your path" />
      </Centered>
    );
  }

  // ----- Non-teaching states: done / blocked / lesson_missing -----
  if (!data || !data.lesson || data.status === "done" || data.status === "blocked") {
    return (
      <Centered>
        <EmptyState
          title={data?.status === "done" ? "🎉 Chapter complete!" : "Nothing to learn just yet"}
          copy={data?.reason ?? "Head back to your path."}
          href={roadmapHref}
          action="Back to your path"
        />
      </Centered>
    );
  }

  const { lesson, concept_name, status, reason } = data;
  const sections: LessonSection[] = lesson.sections ?? [];
  const hasCheck = Boolean(lesson.check || lesson.check_question?.trim());
  const assessmentHref = withChapter("/assessment", chapterId, { concept: lesson.concept_id });

  // The check, the rating and the way out: the last step (or the end of a legacy page).
  const checkBlock = (
    <div className="flex flex-col gap-5">
      {hasCheck && (
        <section className="surface lesson-check flex flex-col gap-4">
          <div className="check-header">
            <Pill>QUICK CHECK</Pill>
            <span>Take your best shot</span>
          </div>
          <h2 className="display flex items-center gap-2 text-2xl font-bold text-foreground">
            <CircleHelp className="size-6 text-primary" aria-hidden /> Check yourself
          </h2>
          <Markdown>{lesson.check?.question ?? lesson.check_question}</Markdown>
          <Button size="lg" asChild className="self-start">
            <Link href={assessmentHref}>
              Answer the question <ArrowRight className="size-5" />
            </Link>
          </Button>
        </section>
      )}
      {/* Did the interest-based explanation work? The pilot's core question. */}
      <RateLesson
        interest={student?.interest}
        rating={lessonView.rating}
        onRate={lessonView.rate}
        failed={lessonView.ratingError}
      />
    </div>
  );

  // The opening story is drawn by <LessonStory>, which puts a story written for
  // the student's hobby first when one exists (layer 3).
  const originalStory = sections.find((s) => s.heading === "The story")?.markdown;

  const steps: LessonStep[] = [];
  if (sections.length > 0) {
    steps.push({
      id: "story",
      label: "The story",
      icon: BookOpen,
      content: (
        <LessonStory
          key={lesson.concept_id}
          conceptId={lesson.concept_id}
          initial={lesson.personal_story}
          original={originalStory}
          interest={student?.interest}
        />
      ),
    });
    for (const section of sections) {
      if (section.heading === "The story") continue;
      const look = lookOf(section.heading);
      steps.push({
        id: section.heading,
        label: look.label,
        icon: look.Icon,
        content: <SectionCard section={section} look={look} />,
      });
    }
    steps.push({ id: "check", label: "Check yourself", icon: CircleHelp, content: checkBlock });
    // A student who learns by trying (survey) sees the worked example before the explanation.
    // Presentation only: every step is still there and one click away.
    if (data.prefs?.example_first) {
      const idea = steps.findIndex((s) => s.label === "The idea");
      const example = steps.findIndex((s) => s.label === "Try an example");
      if (idea !== -1 && example > idea) steps.splice(idea, 0, ...steps.splice(example, 1));
    }
  }

  return (
    <main className="page-shell lesson-shell w-full flex-1">
      {/* ~720px reading column with generous vertical rhythm. */}
      <div className="mx-auto flex max-w-[720px] flex-col gap-6">
        {/* Title block */}
        <header className="lesson-title !px-0">
          <Link href={roadmapHref} className="back-link">
            ← Your path
          </Link>
          <div className="mt-4">
            <Pill>{status === "review" ? "QUICK REVIEW" : "YOUR STORY STARTS HERE"}</Pill>
          </div>
          <h1 className="display">{concept_name}</h1>
          {reason && <p>{reason}</p>}
          {data.prefs?.gentle && <p>Take your time. There&apos;s no rush here.</p>}
        </header>
        <BreakNudge minutes={data.prefs?.break_after_minutes ?? null} key={`nudge-${lesson.concept_id}`} />

        {steps.length > 0 ? (
          // Keyed by concept so moving to the next lesson starts at step one.
          <LessonStepper
            key={lesson.concept_id}
            steps={steps}
            initialStep={stepParam}
            initialAll={data.prefs?.mode === "all"}
          />
        ) : (
          // Legacy lesson: one markdown blob, then the check.
          <>
            <article>
              <Markdown>{lesson.body}</Markdown>
            </article>
            {checkBlock}
          </>
        )}

        {/* "I'm stuck" help widget — live tutor, stays on the lesson. */}
        <HelpWidget conceptId={lesson.concept_id} />
      </div>
    </main>
  );
}

// One authored section as a card. The worked example is a "try it first" reveal,
// the takeaway is highlighted, the caveat is marked as one.
function SectionCard({ section, look }: { section: LessonSection; look: Look }) {
  const { Icon } = look;
  const title = (
    <h2 className="display flex items-center gap-2 text-2xl font-bold text-foreground">
      <Icon
        className={cn(
          "size-6",
          look.kind === "takeaway" ? "text-brand-accent" : look.kind === "caveat" ? "text-destructive" : "text-primary",
        )}
        aria-hidden
      />
      {section.heading}
    </h2>
  );

  if (look.kind === "example") {
    return (
      <Reveal title={title} button="Show the worked example" intro="Have a go in your head first, then check your working.">
        <Markdown>{section.markdown}</Markdown>
      </Reveal>
    );
  }

  return (
    <section
      className={cn(
        "surface lesson-section-card flex flex-col gap-3",
        look.kind === "takeaway" &&
          "!border-[color-mix(in_srgb,var(--gold)_50%,var(--line))] !bg-[color-mix(in_srgb,var(--gold)_12%,var(--surface))]",
        look.kind === "caveat" && "!border-[color-mix(in_srgb,var(--danger)_30%,var(--line))]",
      )}
    >
      {title}
      <Markdown>{section.markdown}</Markdown>
    </section>
  );
}

function Reveal({
  title,
  intro,
  button,
  children,
}: {
  title: ReactNode;
  intro: string;
  button: string;
  children: ReactNode;
}) {
  const [open, setOpen] = useState(false);
  return (
    <section className="surface lesson-section-card flex flex-col gap-4">
      {title}
      {open ? (
        <div className="rm-sheet">{children}</div>
      ) : (
        <>
          <p className="text-muted-foreground">{intro}</p>
          <Button className="self-start" onClick={() => setOpen(true)}>
            <Lightbulb className="size-4" /> {button}
          </Button>
        </>
      )}
    </section>
  );
}

// 👍 / 👎 for the lesson. Two toggle buttons (aria-pressed), so a screen reader
// says "Helpful, toggle button, pressed". Pressing the active one clears it.
function RateLesson({
  interest,
  rating,
  onRate,
  failed,
}: {
  interest?: string;
  rating: LessonRating;
  onRate: (rating: LessonRating) => void;
  failed: boolean;
}) {
  const choices = [
    { value: 1 as const, label: "Yes, it helped", Icon: ThumbsUp, on: "border-primary bg-primary/10 text-primary" },
    { value: -1 as const, label: "Not really", Icon: ThumbsDown, on: "border-destructive bg-destructive/10 text-destructive" },
  ];
  return (
    <section
      aria-label="Rate this lesson"
      className="surface flex flex-col gap-3 px-5 py-4 sm:flex-row sm:items-center sm:justify-between"
    >
      <p className="font-medium text-foreground">
        Did the {interest ? <span className="capitalize">{interest}</span> : "story"} explanation
        work for you?
      </p>
      <div className="flex gap-2">
        {choices.map(({ value, label, Icon, on }) => (
          <button
            key={value}
            type="button"
            aria-pressed={rating === value}
            onClick={() => onRate(value)}
            className={cn(
              "inline-flex items-center gap-2 rounded-full border px-4 py-2 text-sm font-semibold transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
              rating === value ? on : "border-border text-muted-foreground hover:border-primary/40 hover:text-foreground",
            )}
          >
            <Icon className="size-4" aria-hidden />
            {label}
          </button>
        ))}
      </div>
      {failed && (
        <p role="status" className="text-sm text-destructive sm:basis-full">
          Couldn&apos;t save that — try again.
        </p>
      )}
      {!failed && rating !== 0 && (
        <p role="status" className="sr-only">
          Thanks, saved.
        </p>
      )}
    </section>
  );
}

// Small helper for the centered single-message states.
function Centered({ children }: { children: React.ReactNode }) {
  return <main className="page-shell mx-auto w-full max-w-xl flex-1">{children}</main>;
}

// Loading skeleton.
function LessonSkeleton() {
  return (
    <main className="page-shell mx-auto w-full max-w-[720px] flex-1">
      <div className="surface">
        <Skeleton rows={6} />
      </div>
    </main>
  );
}
