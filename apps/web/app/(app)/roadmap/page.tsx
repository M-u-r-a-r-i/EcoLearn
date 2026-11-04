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

import { Suspense, useEffect, useMemo } from "react";
import Link from "next/link";
import { ArrowRight, Lock, PartyPopper, Sparkles } from "lucide-react";

import { getRoadmap, type RoadmapConcept } from "@/lib/api";
import { useAuth } from "@/components/auth-provider";
import { EndCheckCard, LearningPlanCard, RevisionCard } from "@/components/learning-plan";
import { Button } from "@/components/ui/button";
import { EmptyState, Pill } from "@/components/ui-kit";
import { ProgressRing, kindOf, type NodeKind } from "@/components/roadmap-path";
import { RoadmapTree } from "@/components/roadmap-tree";
import { useChapter, withChapter } from "@/lib/use-chapter";
import { useFetch } from "@/lib/use-fetch";

// Each interest has an emoji (its accent colour comes from data-interest on <html>).
const INTEREST_LOOK: Record<string, { emoji: string }> = {
  cricket: { emoji: "🏏" },
  football: { emoji: "⚽" },
  gaming: { emoji: "🎮" },
  smartphones: { emoji: "📱" },
  motorsport: { emoji: "🏎️" },
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
  const kinds: Record<string, NodeKind> = Object.fromEntries(
    (concepts ?? []).map((c) => [c.concept_id, kindOf(c, nextConcept?.concept_id)]),
  );
  const look = INTEREST_LOOK[student.interest] ?? { emoji: "⚛️" };
  const freshNames = (concepts ?? []).filter((c) => fresh.includes(c.concept_id)).map((c) => c.name);

  return (
    <main className="page-shell w-full flex-1">
      {/* ---------- Welcome strip ---------- */}
      <section className="welcome-strip fade-up">
        <span className="welcome-avatar" aria-hidden>
          {student.name.slice(0, 1).toUpperCase()}
        </span>
        <div className="min-w-0">
          <p className="eyebrow">
            {look.emoji} Your learning path
          </p>
          <h1 className="display">{chapter?.name ?? " "}</h1>
          <p>
            {student.name} · through <span className="capitalize">{student.interest}</span>
          </p>
        </div>
        {loading ? (
          <div className="ml-auto size-14 shrink-0 animate-pulse rounded-full bg-muted" />
        ) : (
          <ProgressRing done={done} mastered={mastered} total={total} />
        )}
      </section>

      {!loading && readyCount > 0 && (
        <div className="mb-5 flex flex-wrap gap-2 text-xs font-semibold">
          <span className="tag">{done} done</span>
          {mastered > 0 && <span className="tag">{mastered} mastered</span>}
          {locked > 0 && (
            <span className="tag inline-flex items-center gap-1">
              <Lock className="size-3" aria-hidden /> {locked} to unlock
            </span>
          )}
        </div>
      )}

      {freshNames.length > 0 && (
        <p
          role="status"
          className="rm-sheet mb-4 flex items-center gap-2 rounded-xl border border-success/30 bg-success/10 px-4 py-3 text-sm font-semibold text-success"
        >
          <Sparkles className="size-4 shrink-0" aria-hidden />
          Nice work! {freshNames.join(", ")} {freshNames.length === 1 ? "is" : "are"} done.
        </p>
      )}

      {/* On phones the side cards sit below the map, so the main action stays up here. */}
      {!loading && !error && readyCount > 0 && (nextConcept || allDone) && (
        <Button asChild className="mb-5 w-full md:hidden">
          <Link href={withChapter("/lesson", chapterId)}>
            {allDone ? "Review the chapter" : "Continue learning"} <ArrowRight className="size-4" aria-hidden />
          </Link>
        </Button>
      )}

      <div className="roadmap-toolbar">
        <div>
          <p className="eyebrow">Your map</p>
          <h2 className="display">Pick a chapter, then a concept</h2>
        </div>
        <p className="tree-legend" aria-hidden>
          <span className="l1">Chapter</span>
          <span className="l2">Concept</span>
          <span className="l3">Lesson part</span>
        </p>
      </div>

      <div className="roadmap-layout">
        <div className="flex min-w-0 flex-col gap-4">
          {!loading && !error && concepts && total > 0 && readyCount === 0 && (
            <EmptyState
              title={`The ${student.interest} lessons for this chapter are still being written.`}
              copy="Open another chapter below. The chapters you can open now are the ones not marked “coming soon”."
            />
          )}
          <RoadmapTree
            chapters={chapters}
            chapterId={chapterId}
            onChapter={setChapter}
            concepts={concepts}
            loadingConcepts={loading}
            conceptsError={error}
            kinds={kinds}
            nextId={nextConcept?.concept_id}
            fresh={fresh}
          />
        </div>

        <aside className="roadmap-aside">
          {!loading && !error && readyCount > 0 && (nextConcept || allDone) && (
            <section className="surface panel continue-card">
              <Pill>{allDone ? "CHAPTER COMPLETE" : "NEXT UP"}</Pill>
              <h3 className="display">{allDone ? "Review the chapter" : nextConcept?.name}</h3>
              <p>
                {allDone
                  ? "Every step here is done. Revisit any lesson to keep it fresh."
                  : (nextConcept?.personal_note ?? "This is where your path continues.")}
              </p>
              <Button asChild>
                <Link href={withChapter("/lesson", chapterId)}>
                  {allDone ? (
                    <>
                      <PartyPopper className="size-4" aria-hidden /> Review the chapter
                    </>
                  ) : (
                    <>
                      Continue learning <ArrowRight className="size-4" aria-hidden />
                    </>
                  )}
                </Link>
              </Button>
            </section>
          )}
          <EndCheckCard />
          <RevisionCard />
          <LearningPlanCard chapterId={chapterId} />
          <div className="aside-note">
            <span aria-hidden>✳</span>
            <p>Chapters are never locked. Steps inside a chapter open in order.</p>
          </div>
        </aside>
      </div>
    </main>
  );
}
