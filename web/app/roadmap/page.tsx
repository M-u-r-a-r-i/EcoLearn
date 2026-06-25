// Roadmap page (/roadmap) — the student's learning path for a chapter.
//
// Client Component, because the data it needs depends on client-only state:
// the student_id lives in React Context (set during onboarding, in the browser).
// A Server Component renders on the server and can't read that context, so the
// simplest correct approach here is to fetch in the browser with useEffect.

"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Check, Play, Lock, ArrowRight, PartyPopper } from "lucide-react";

import { getRoadmap, type RoadmapConcept, type ConceptStatus } from "@/lib/api";
import { useStudent } from "@/components/student-provider";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { Progress } from "@/components/ui/progress";
import { cn } from "@/lib/utils";

// The platform currently ships one chapter; hardcode it for now (a chapter
// picker comes later). This id matches data/curriculum/physics.yaml.
const CHAPTER_ID = "motion_straight_line";
const CHAPTER_NAME = "Motion in a Straight Line";

// Per-status visual config: node colour + icon + badge styling.
const STATUS: Record<
  ConceptStatus,
  { label: string; Icon: typeof Check; node: string; badge: string }
> = {
  mastered: {
    label: "Mastered",
    Icon: Check,
    node: "bg-success text-white border-success",
    badge: "bg-success/10 text-success",
  },
  available: {
    label: "Available",
    Icon: Play,
    node: "bg-primary text-white border-primary",
    badge: "bg-primary/10 text-primary",
  },
  locked: {
    label: "Locked",
    Icon: Lock,
    node: "bg-muted text-muted-foreground border-border",
    badge: "bg-muted text-muted-foreground",
  },
};

export default function RoadmapPage() {
  const { student } = useStudent();

  // Three pieces of state model the request lifecycle.
  const [concepts, setConcepts] = useState<RoadmapConcept[] | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch on load. The effect re-runs if `student` changes (e.g. after onboarding).
  useEffect(() => {
    if (!student) {
      setLoading(false);
      return;
    }
    let cancelled = false; // guard against setting state after unmount
    setLoading(true);
    setError(null);
    getRoadmap(student.student_id, CHAPTER_ID)
      .then((data) => {
        if (!cancelled) setConcepts(data);
      })
      .catch(() => {
        if (!cancelled)
          setError(
            "Couldn't load your roadmap. Make sure the backend is running on " +
              (process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000") +
              ".",
          );
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [student]);

  // ---- No student (e.g. page reloaded → context cleared) ----
  if (!student) {
    return (
      <main className="flex flex-1 flex-col">
        <PageContainer className="flex flex-1 flex-col items-center justify-center gap-6 text-center">
          <h1 className="text-2xl font-bold text-foreground">No student yet</h1>
          <p className="text-muted-foreground">
            Start at onboarding to create your learner profile.
          </p>
          <PrimaryButton asChild>
            <Link href="/onboarding">Go to onboarding</Link>
          </PrimaryButton>
        </PageContainer>
      </main>
    );
  }

  const total = concepts?.length ?? 0;
  const mastered = concepts?.filter((c) => c.status === "mastered").length ?? 0;
  const pct = total ? Math.round((mastered / total) * 100) : 0;
  const nextConcept = concepts?.find((c) => c.status === "available");
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
              {CHAPTER_NAME}
            </h1>
            <p className="text-muted-foreground">
              Personalised for {student.name} · through {student.interest}
            </p>
          </div>

          {/* Progress */}
          <div className="flex flex-col gap-2 rounded-xl border border-border bg-card p-4 shadow-soft">
            <div className="flex items-center justify-between text-sm">
              <span className="font-semibold text-foreground">
                {mastered} of {total} concepts mastered
              </span>
              <span className="text-muted-foreground">{pct}%</span>
            </div>
            <Progress value={pct} />
          </div>

          {/* Continue Learning */}
          {!loading && !error && total > 0 && (
            <PrimaryButton asChild className="w-full sm:w-auto sm:self-start">
              <Link href="/lesson">
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

        {!loading && !error && concepts && (
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

                  {/* Concept card */}
                  <div
                    className={cn(
                      "flex flex-1 items-center justify-between rounded-xl border bg-card px-4 py-3 transition-all",
                      isNext
                        ? "border-primary/40 shadow-card"
                        : "border-border shadow-soft",
                      c.status === "locked" && "opacity-70",
                    )}
                  >
                    <div className="flex flex-col">
                      <span className="font-semibold text-foreground">{c.name}</span>
                      <span className="text-xs text-muted-foreground">
                        {c.status === "mastered" &&
                          `Best ${c.best_score}/3 · ${c.attempts} attempt${c.attempts === 1 ? "" : "s"}`}
                        {c.status === "available" &&
                          (c.attempts
                            ? `Ready to learn · best ${c.best_score}/3`
                            : "Ready to learn")}
                        {c.status === "locked" &&
                          `Unlocks after ${c.missing_prerequisites.length} earlier concept${c.missing_prerequisites.length === 1 ? "" : "s"}`}
                      </span>
                    </div>

                    <span
                      className={cn(
                        "shrink-0 rounded-full px-2.5 py-1 text-xs font-semibold",
                        s.badge,
                      )}
                    >
                      {isNext ? "Next up" : s.label}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </PageContainer>
    </main>
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
