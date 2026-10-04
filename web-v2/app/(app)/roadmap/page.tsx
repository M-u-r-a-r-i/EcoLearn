// Roadmap page (/roadmap?chapter=...) — the student's learning path for a chapter,
// drawn as a level map (components/roadmap-path.tsx).
//
// Client Component: it's rendered inside <RequireAuth> (app/(app)/layout.tsx),
// which only shows it once the browser knows who is logged in, and the chapter
// comes from the URL. The API identifies the student by the session cookie.
//
// Chapters are never locked; the concepts inside one open in order (the server
// says which are `locked`). Tap a step to select it; the sheet at the bottom
// offers the action.

"use client";

import { Suspense, useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { ArrowRight, Clock, Lock, PartyPopper, Sparkles } from "lucide-react";

import { getRoadmap, type RoadmapConcept } from "@/lib/api";
import { useAuth } from "@/components/auth-provider";
import { ChapterPicker } from "@/components/chapter-picker";
import { EndCheckCard, LearningPlanCard, RevisionCard } from "@/components/learning-plan";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { PathMap, ProgressRing, StepSheet, kindOf } from "@/components/roadmap-path";
import { useChapter, withChapter } from "@/lib/use-chapter";
import { useFetch } from "@/lib/use-fetch";

// Each interest has an emoji and an accent that tints the header card.
const INTEREST_LOOK: Record<string, { emoji: string; color: string }> = {
  cricket: { emoji: "🏏", color: "#22c55e" },
  football: { emoji: "⚽", color: "#3b82f6" },
  gaming: { emoji: "🎮", color: "#a855f7" },
  smartphones: { emoji: "📱", color: "#06b6d4" },
  motorsport: { emoji: "🏎️", color: "#ef4444" },
};

export default function RoadmapPage() {
  // useSearchParams (inside useChapter) needs a Suspense boundary to prerender.
  return (
    <Suspense>
      <Roadmap />
    </Suspense>
  );
}

// What the student had finished last time they looked at this chapter, so a
// step that became "done" since then can pop. Per tab (sessionStorage), and only
// ever a convenience: if storage is blocked, nothing pops and nothing breaks.
function readDone(key: string): Set<string> | null {
  try {
    const raw = sessionStorage.getItem(key);
    return raw ? new Set(JSON.parse(raw) as string[]) : null;
  } catch {
    return null;
  }
}

function Roadmap() {
  const { student } = useAuth();
  const { chapterId, chapter, chapters, setChapter } = useChapter();

  // Fetch on load, and again whenever the chapter changes.
  const { data: concepts, loading, error } = useFetch<RoadmapConcept[]>(chapterId, () =>
    getRoadmap(chapterId),
  );

  const isDone = (c: RoadmapConcept) => c.status === "mastered" || c.progress_status === "partial";
  const doneIds = useMemo(() => (concepts ?? []).filter(isDone).map((c) => c.concept_id), [concepts]);
  const storeKey = `rm-done:${student?.student_id ?? ""}:${chapterId}`;
  // Read before the effect below writes, so this render sees the old list.
  const fresh = useMemo(() => {
    if (!concepts) return [];
    const before = readDone(storeKey);
    return before ? doneIds.filter((id) => !before.has(id)) : [];
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [concepts]);
  useEffect(() => {
    if (!concepts) return;
    try {
      sessionStorage.setItem(storeKey, JSON.stringify(doneIds));
    } catch {
      /* private window: no celebration next time, that's all */
    }
  }, [concepts, doneIds, storeKey]);

  if (!student) return null; // RequireAuth guarantees a student; this satisfies TypeScript

  const total = concepts?.length ?? 0;
  const mastered = concepts?.filter((c) => c.status === "mastered").length ?? 0;
  const done = concepts?.filter(isDone).length ?? 0;
  const locked = concepts?.filter((c) => c.locked && c.has_lesson !== false).length ?? 0;
  // has_lesson is absent only for legacy accounts; treat that as "written".
  const written = (c: RoadmapConcept) => c.has_lesson !== false;
  const readyCount = concepts?.filter(written).length ?? 0;
  // The server's personal recommendation (it may skip what the starting check
  // says they know); the first unfinished open concept if it points elsewhere.
  const nextConcept =
    concepts?.find((c) => c.recommended) ??
    concepts?.find((c) => c.status === "available" && written(c) && !c.locked);
  const allDone = total > 0 && done === total;
  const look = INTEREST_LOOK[student.interest] ?? { emoji: "⚛️", color: "#6366f1" };
  const freshNames = (concepts ?? []).filter((c) => fresh.includes(c.concept_id)).map((c) => c.name);

  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex w-full max-w-2xl flex-col gap-6">
        {/* ---------- Header card ---------- */}
        <section
          className="relative overflow-hidden rounded-3xl border border-border bg-card p-5 shadow-card"
          style={{
            backgroundImage: `radial-gradient(110% 90% at 100% 0%, color-mix(in oklab, ${look.color} 24%, transparent), transparent 62%)`,
          }}
        >
          <div className="flex items-center gap-5">
            {loading ? (
              <div className="size-28 shrink-0 animate-pulse rounded-full bg-muted" />
            ) : (
              <ProgressRing done={done} mastered={mastered} total={total} />
            )}
            <div className="flex min-w-0 flex-col gap-1">
              <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
                {look.emoji} Your learning path
              </span>
              <h1 className="text-2xl font-extrabold tracking-tight text-foreground sm:text-3xl">
                {chapter?.name ?? " "}
              </h1>
              <p className="text-sm text-muted-foreground">
                {student.name} · through <span className="capitalize">{student.interest}</span>
              </p>
              {!loading && readyCount > 0 && (
                <div className="mt-1 flex flex-wrap gap-1.5 text-xs font-semibold">
                  <span className="rounded-full bg-success/10 px-2.5 py-1 text-success">{done} done</span>
                  {mastered > 0 && (
                    <span className="rounded-full bg-amber-400/15 px-2.5 py-1 text-amber-500">
                      {mastered} mastered
                    </span>
                  )}
                  {locked > 0 && (
                    <span className="inline-flex items-center gap-1 rounded-full bg-muted px-2.5 py-1 text-muted-foreground">
                      <Lock className="size-3" aria-hidden /> {locked} to unlock
                    </span>
                  )}
                </div>
              )}
            </div>
          </div>

          {!loading && !error && readyCount > 0 && (nextConcept || allDone) && (
            <PrimaryButton asChild className="mt-5 w-full sm:w-auto">
              <Link href={withChapter("/lesson", chapterId)}>
                {allDone ? (
                  <>
                    <PartyPopper className="size-5" /> Review the chapter
                  </>
                ) : (
                  <>
                    Continue learning <ArrowRight className="size-5" />
                  </>
                )}
              </Link>
            </PrimaryButton>
          )}
        </section>

        {freshNames.length > 0 && (
          <p
            role="status"
            className="rm-sheet flex items-center gap-2 rounded-xl border border-success/30 bg-success/10 px-4 py-3 text-sm font-semibold text-success"
          >
            <Sparkles className="size-4 shrink-0" aria-hidden />
            Nice work! {freshNames.join(", ")} {freshNames.length === 1 ? "is" : "are"} done.
          </p>
        )}

        <ChapterPicker
          chapters={chapters}
          value={chapterId}
          onChange={setChapter}
          interest={student.interest}
        />

        <EndCheckCard />
        <RevisionCard />
        <LearningPlanCard chapterId={chapterId} />

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
          // Keyed by chapter so the selection resets when the chapter changes.
          <PathSection
            key={chapterId}
            concepts={concepts}
            nextId={nextConcept?.concept_id}
            chapterId={chapterId}
            fresh={fresh}
          />
        )}
      </PageContainer>
    </main>
  );
}

function PathSection({
  concepts,
  nextId,
  chapterId,
  fresh,
}: {
  concepts: RoadmapConcept[];
  nextId: string | undefined;
  chapterId: string;
  fresh: string[];
}) {
  const [selected, setSelected] = useState<string | null>(null);
  const [shakeId, setShakeId] = useState<string | null>(null);
  const activeId = selected ?? nextId ?? concepts[0]?.concept_id;
  const index = Math.max(0, concepts.findIndex((c) => c.concept_id === activeId));
  const active = concepts[index];

  function select(id: string) {
    setSelected(id);
    const picked = concepts.find((c) => c.concept_id === id);
    if (picked?.locked) {
      // A little "not yet" shake; cleared so tapping again replays it.
      setShakeId(id);
      setTimeout(() => setShakeId((now) => (now === id ? null : now)), 450);
    }
  }

  return (
    <>
      <PathMap
        concepts={concepts}
        nextId={nextId}
        selectedId={activeId}
        onSelect={select}
        fresh={fresh}
        shakeId={shakeId}
      />
      {active && (
        <StepSheet
          concept={active}
          kind={kindOf(active, nextId)}
          index={index}
          chapterId={chapterId}
        />
      )}
    </>
  );
}

// A clean shimmer placeholder shown while the roadmap loads.
function RoadmapSkeleton() {
  return (
    <div className="flex flex-col gap-3">
      {Array.from({ length: 5 }).map((_, i) => (
        <div key={i} className="flex items-center gap-4">
          <div className="size-16 shrink-0 animate-pulse rounded-full bg-muted" />
          <div className="h-16 flex-1 animate-pulse rounded-xl bg-muted" />
        </div>
      ))}
    </div>
  );
}
