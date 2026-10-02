// Roadmap page (/roadmap?chapter=...) — the student's learning path for a chapter.
//
// Client Component: it's rendered inside <RequireAuth> (app/(app)/layout.tsx),
// which only shows it once the browser knows who is logged in, and the chapter
// comes from the URL. The API identifies the student by the session cookie.

"use client";

import { Suspense } from "react";
import Link from "next/link";
import { Check, Clock, Play, ArrowRight, PartyPopper, Target } from "lucide-react";

import { getRoadmap, type RoadmapConcept, type ConceptStatus } from "@/lib/api";
import { useAuth } from "@/components/auth-provider";
import { ChapterPicker } from "@/components/chapter-picker";
import { LearningPlanCard } from "@/components/learning-plan";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { Progress } from "@/components/ui/progress";
import { useChapter, withChapter } from "@/lib/use-chapter";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

// Per-status visual config: node colour + icon + badge styling.
const STATUS: Record<
  ConceptStatus,
  { label: string; Icon: typeof Check; node: string; badge: string }
> = {
  mastered: {
    label: "Mastered",
    Icon: Check,
    node: "bg-success text-success-foreground border-success",
    badge: "bg-success/10 text-success",
  },
  available: {
    label: "Available",
    Icon: Play,
    node: "bg-primary text-primary-foreground border-primary",
    badge: "bg-primary/10 text-primary",
  },
};

export default function RoadmapPage() {
  // useSearchParams (inside useChapter) needs a Suspense boundary to prerender.
  return (
    <Suspense>
      <Roadmap />
    </Suspense>
  );
}

function Roadmap() {
  const { student } = useAuth();
  const { chapterId, chapter, chapters, setChapter } = useChapter();

  // Fetch on load, and again whenever the chapter changes.
  const { data: concepts, loading, error } = useFetch<RoadmapConcept[]>(chapterId, () =>
    getRoadmap(chapterId),
  );

  if (!student) return null; // RequireAuth guarantees a student; this satisfies TypeScript

  const total = concepts?.length ?? 0;
  const mastered = concepts?.filter((c) => c.status === "mastered").length ?? 0;
  const pct = total ? Math.round((mastered / total) * 100) : 0;
  // has_lesson is absent only for legacy accounts; treat that as "written".
  const written = (c: RoadmapConcept) => c.has_lesson !== false;
  const readyCount = concepts?.filter(written).length ?? 0;
  // The server's personal recommendation (it may skip what the starting check
  // says they know); the first unfinished concept if it points elsewhere.
  const nextConcept =
    concepts?.find((c) => c.recommended) ??
    concepts?.find((c) => c.status === "available" && written(c));
  const allDone = total > 0 && mastered === total;

  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex w-full max-w-2xl flex-col gap-8">
        {/* ---------- Header ---------- */}
        <div className="flex flex-col gap-4">
          <div className="flex flex-col gap-1">
            <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
              Your learning path
            </span>
            <h1 className="text-3xl font-bold tracking-tight text-foreground">
              {chapter?.name ?? " "}
            </h1>
            <p className="text-muted-foreground">
              Personalised for {student.name} · through {student.interest}
            </p>
          </div>

          <ChapterPicker
            chapters={chapters}
            value={chapterId}
            onChange={setChapter}
            interest={student.interest}
          />

          <LearningPlanCard chapterId={chapterId} />

          {/* Progress — pointless for a chapter with nothing written yet. */}
          {(loading || readyCount > 0) && (
            <div className="flex flex-col gap-2 rounded-xl border border-border bg-card p-4 shadow-soft">
              <div className="flex items-center justify-between text-sm">
                <span className="font-semibold text-foreground">
                  {mastered} of {total} concepts mastered
                </span>
                <span className="text-muted-foreground">{pct}%</span>
              </div>
              <Progress value={pct} />
            </div>
          )}

          {/* Continue Learning */}
          {!loading && !error && readyCount > 0 && (nextConcept || allDone) && (
            <PrimaryButton asChild className="w-full sm:w-auto sm:self-start">
              <Link href={withChapter("/lesson", chapterId)}>
                {allDone ? (
                  <>
                    <PartyPopper className="size-5" /> Review the chapter
                  </>
                ) : (
                  <>
                    Continue Learning <ArrowRight className="size-5" />
                  </>
                )}
              </Link>
            </PrimaryButton>
          )}
        </div>

        {/* ---------- Body: loading / error / path ---------- */}
        {loading && <RoadmapSkeleton />}

        {error && (
          <p className="rounded-xl border border-destructive/30 bg-destructive/5 px-4 py-3 text-sm text-destructive">
            {error}
          </p>
        )}

        {!loading && !error && concepts && total > 0 && readyCount === 0 && (
          <div className="flex flex-col gap-2 rounded-xl border border-dashed border-border bg-card p-6 text-center">
            <Clock className="mx-auto size-8 text-muted-foreground" aria-hidden />
            <p className="font-semibold text-foreground">
              The <span className="capitalize">{student.interest}</span> lessons for this chapter are
              still being written.
            </p>
            <p className="text-sm text-muted-foreground">
              Pick another chapter from the list above. The chapters you can open now are the ones
              not marked &ldquo;coming soon&rdquo;.
            </p>
          </div>
        )}

        {!loading && !error && concepts && readyCount > 0 && (
          <div className="relative flex flex-col gap-3">
            {/* The continuous vertical line that turns the nodes into a path.
                left-5 (20px) aligns with the centre of the 40px node circles. */}
            <div
              className="absolute bottom-6 left-5 top-6 w-px bg-border"
              aria-hidden
            />

            {concepts.map((c) => {
              const s = STATUS[c.status];
              const isNext = c.concept_id === nextConcept?.concept_id;
              if (!written(c)) return <ComingSoonConcept key={c.concept_id} name={c.name} />;
              return (
                <div key={c.concept_id} className="relative flex items-center gap-4">
                  {/* Node circle */}
                  <div
                    className={cn(
                      "z-10 flex size-10 shrink-0 items-center justify-center rounded-full border-2 shadow-soft",
                      s.node,
                    )}
                  >
                    <s.Icon className="size-5" strokeWidth={2.5} />
                  </div>

                  {/* Concept card — every concept opens its lesson; nothing is locked. */}
                  <Link
                    href={withChapter("/lesson", chapterId, { concept: c.concept_id })}
                    className={cn(
                      "flex flex-1 items-center justify-between rounded-xl border bg-card px-4 py-3 transition-all hover:border-primary/40 hover:shadow-card focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
                      isNext
                        ? "border-primary/40 shadow-card"
                        : "border-border shadow-soft",
                    )}
                  >
                    <div className="flex flex-col">
                      <span className="font-semibold text-foreground">{c.name}</span>
                      <span className="text-xs text-muted-foreground">
                        {/* Checks are multiple choice: right or not yet, so no "2/3". */}
                        {c.status === "mastered" &&
                          `Got it right · ${c.attempts} attempt${c.attempts === 1 ? "" : "s"}`}
                        {c.status === "available" &&
                          (c.attempts
                            ? `Tried ${c.attempts}× · not right yet`
                            : "Ready to learn")}
                        {/* Nothing is locked; uncleared prerequisites are only a hint. */}
                        {c.status === "available" &&
                          c.missing_prerequisites.length > 0 &&
                          ` · builds on ${c.missing_prerequisites.length} earlier concept${c.missing_prerequisites.length === 1 ? "" : "s"}`}
                      </span>
                      {c.personal_note && (
                        <span
                          className={cn(
                            "mt-1 flex items-start gap-1 text-xs",
                            c.personal === "focus" ? "text-destructive" : "text-success",
                          )}
                        >
                          {c.personal === "focus" && <Target className="mt-px size-3 shrink-0" aria-hidden />}
                          {c.personal_note}
                        </span>
                      )}
                    </div>

                    <span
                      className={cn(
                        "shrink-0 rounded-full px-2.5 py-1 text-xs font-semibold",
                        !isNext && c.status !== "mastered" && c.personal === "focus"
                          ? "bg-destructive/10 text-destructive"
                          : !isNext && c.status !== "mastered" && c.personal === "known"
                            ? "bg-success/10 text-success"
                            : s.badge,
                      )}
                    >
                      {isNext
                        ? "Next up"
                        : c.status !== "mastered" && c.personal === "focus"
                          ? "Focus"
                          : c.status !== "mastered" && c.personal === "known"
                            ? "Know it?"
                            : s.label}
                    </span>
                  </Link>
                </div>
              );
            })}
          </div>
        )}
      </PageContainer>
    </main>
  );
}

// A concept whose lesson isn't written yet in this interest: on the path, so
// the chapter's shape is visible, but not a link to an empty page.
function ComingSoonConcept({ name }: { name: string }) {
  return (
    <div className="relative flex items-center gap-4" aria-disabled="true">
      <div className="z-10 flex size-10 shrink-0 items-center justify-center rounded-full border-2 border-border bg-muted text-muted-foreground">
        <Clock className="size-5" />
      </div>
      <div className="flex flex-1 items-center justify-between rounded-xl border border-dashed border-border bg-card/60 px-4 py-3">
        <span className="font-semibold text-muted-foreground">{name}</span>
        <span className="shrink-0 rounded-full bg-muted px-2.5 py-1 text-xs font-semibold text-muted-foreground">
          Coming soon
        </span>
      </div>
    </div>
  );
}

// A clean shimmer placeholder shown while the roadmap loads.
function RoadmapSkeleton() {
  return (
    <div className="flex flex-col gap-3">
      {Array.from({ length: 5 }).map((_, i) => (
        <div key={i} className="flex items-center gap-4">
          <div className="size-10 shrink-0 animate-pulse rounded-full bg-muted" />
          <div className="h-16 flex-1 animate-pulse rounded-xl bg-muted" />
        </div>
      ))}
    </div>
  );
}
