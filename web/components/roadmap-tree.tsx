// The roadmap as a tree that opens as you choose (2026-10-09).
//
//   level 1  chapters      a solid green rail, big round nodes, grouped by unit
//   level 2  concepts      a dashed orange branch, square-ish nodes (the old path map's states)
//   level 3  lesson parts  a dotted purple twig: the story, the idea, an example... each one
//                          opens the lesson at that part
//
// Only one chapter and one concept are open at a time. Chapters are never locked;
// concepts inside a chapter open in order (the server says which are `locked`).
// Presentation + navigation only: the data comes from the roadmap and lesson endpoints.

"use client";

import Link from "next/link";
import { useState } from "react";
import { BookOpen, ChevronDown, Clock, Lock, Play, Target } from "lucide-react";

import { Markdown } from "@/components/markdown";
import { Button } from "@/components/ui/button";
import { NODE_ICON, nodeBlurb, nodeSubline, type NodeKind } from "@/components/roadmap-path";
import { Skeleton } from "@/components/ui-kit";
import { getNextLesson, type Chapter, type RoadmapConcept } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { withChapter } from "@/lib/use-chapter";
import { cn } from "@/lib/utils";

// How the lesson's authored sections are named to a student (same words as the lesson page).
function partLabel(heading: string): string {
  if (/worked example/i.test(heading)) return "Try an example";
  if (/picture breaks|breaks down/i.test(heading)) return "Where it breaks";
  if (/takeaway/i.test(heading)) return "Remember this";
  if (/physics|idea|explanation/i.test(heading)) return "The idea";
  return heading;
}

export function RoadmapTree({
  chapters,
  chapterId,
  onChapter,
  concepts,
  loadingConcepts,
  conceptsError,
  kinds,
  nextId,
  fresh,
}: {
  chapters: Chapter[] | null;
  chapterId: string;
  onChapter: (id: string) => void;
  concepts: RoadmapConcept[] | null;
  loadingConcepts: boolean;
  conceptsError: string | null;
  kinds: Record<string, NodeKind>;
  nextId: string | undefined;
  fresh: string[];
}) {
  const [chapterOpen, setChapterOpen] = useState(true);
  if (chapters === null) {
    return (
      <div className="surface">
        <Skeleton rows={6} />
      </div>
    );
  }

  // Chapters arrive in teaching order; group them by unit.
  const groups: { unit: string; items: Chapter[] }[] = [];
  for (const c of chapters) {
    const last = groups[groups.length - 1];
    if (last && last.unit === c.unit_name) last.items.push(c);
    else groups.push({ unit: c.unit_name, items: [c] });
  }
  let number = 0;

  return (
    <div className="tree" aria-label="Chapters">
      {groups.map((g) => (
        <section key={g.unit} className="tree-unit-group">
          <h3 className="tree-unit">{g.unit}</h3>
          <ol className="tree-l1">
            {g.items.map((c) => {
              number += 1;
              const open = c.id === chapterId && chapterOpen;
              const ready = c.lessons_ready;
              const soon = ready === 0;
              return (
                <li key={c.id} className={cn("tree-item", open && "is-open", soon && "is-soon")}>
                  <button
                    type="button"
                    className="tree-row l1"
                    aria-expanded={open}
                    disabled={soon && c.id !== chapterId}
                    onClick={() => {
                      if (c.id === chapterId) setChapterOpen((v) => !v);
                      else {
                        setChapterOpen(true);
                        onChapter(c.id);
                      }
                    }}
                  >
                    <span className="tree-node l1" aria-hidden>
                      {soon ? <Clock size={20} /> : number}
                    </span>
                    <span className="tree-text">
                      <span className="tree-title">{c.name}</span>
                      <span className="tree-meta">
                        {soon
                          ? "Coming soon"
                          : ready === undefined || ready === c.concept_count
                            ? `${c.concept_count} concepts`
                            : `${ready} of ${c.concept_count} lessons ready`}
                      </span>
                    </span>
                    {!soon && <ChevronDown className="tree-chevron" size={18} aria-hidden />}
                  </button>

                  {open && (
                    <ConceptBranch
                      chapterId={c.id}
                      concepts={concepts}
                      loading={loadingConcepts}
                      error={conceptsError}
                      kinds={kinds}
                      nextId={nextId}
                      fresh={fresh}
                    />
                  )}
                </li>
              );
            })}
          </ol>
        </section>
      ))}
    </div>
  );
}

function ConceptBranch({
  chapterId,
  concepts,
  loading,
  error,
  kinds,
  nextId,
  fresh,
}: {
  chapterId: string;
  concepts: RoadmapConcept[] | null;
  loading: boolean;
  error: string | null;
  kinds: Record<string, NodeKind>;
  nextId: string | undefined;
  fresh: string[];
}) {
  // The recommended concept starts open, so "Start lesson" is one tap away.
  const [picked, setPicked] = useState<string | null | undefined>(undefined);
  const [shake, setShake] = useState<string | null>(null);
  const openId = picked === undefined ? (nextId ?? null) : picked;

  if (loading) {
    return (
      <div className="tree-branch l2 fade-up">
        <Skeleton rows={3} />
      </div>
    );
  }
  if (error) return <p className="inline-alert tree-branch l2">{error}</p>;
  if (!concepts || concepts.length === 0) return null;

  return (
    <ol className="tree-branch l2 fade-up" aria-label="Concepts in this chapter">
      {concepts.map((c, i) => {
        const kind = kinds[c.concept_id] ?? "open";
        const Icon = NODE_ICON[kind];
        const open = openId === c.concept_id;
        const dim = kind === "locked" || kind === "soon";
        return (
          <li key={c.concept_id} className={cn("tree-item l2", open && "is-open")}>
            <button
              type="button"
              className="tree-row l2"
              aria-expanded={open}
              onClick={() => {
                setPicked(open ? null : c.concept_id);
                if (kind === "locked") {
                  setShake(c.concept_id);
                  setTimeout(() => setShake((s) => (s === c.concept_id ? null : s)), 450);
                }
              }}
            >
              <span
                className={cn(
                  "tree-node l2",
                  `kind-${kind}`,
                  fresh.includes(c.concept_id) && "rm-pop",
                  shake === c.concept_id && "rm-shake",
                )}
                aria-hidden
              >
                <Icon size={18} strokeWidth={kind === "next" || kind === "open" ? 2.5 : 3} />
              </span>
              <span className="tree-text">
                <span className={cn("tree-title", dim && "is-dim")}>
                  <span className="tree-step">{i + 1}.</span> {c.name}
                </span>
                <span className="tree-meta">{nodeSubline(c, kind)}</span>
                {!dim && c.personal === "focus" && (
                  <span className="tree-flag focus">
                    <Target size={11} aria-hidden /> Focus
                  </span>
                )}
                {!dim && c.personal === "known" && kind !== "done" && kind !== "mastered" && (
                  <span className="tree-flag known">Know it? Prove it</span>
                )}
              </span>
              <ChevronDown className="tree-chevron" size={16} aria-hidden />
            </button>

            {open && <ConceptDetail concept={c} kind={kind} chapterId={chapterId} />}
          </li>
        );
      })}
    </ol>
  );
}

function ConceptDetail({
  concept,
  kind,
  chapterId,
}: {
  concept: RoadmapConcept;
  kind: NodeKind;
  chapterId: string;
}) {
  const playable = kind !== "locked" && kind !== "soon";
  // The lesson's own parts, so the twig matches what the student will actually see.
  const lesson = useFetch(`parts:${chapterId}:${concept.concept_id}`, () =>
    playable ? getNextLesson(chapterId, concept.concept_id) : Promise.resolve(null),
  );
  const sections = lesson.data?.lesson?.sections ?? [];
  const parts: string[] =
    sections.length > 0
      ? [
          "The story",
          ...sections.filter((s) => s.heading !== "The story").map((s) => partLabel(s.heading)),
          "Check yourself",
        ]
      : [];

  const cta: Partial<Record<NodeKind, string>> = {
    next: "Start lesson",
    open: concept.attempts ? "Try again" : "Start lesson",
    done: "Review lesson",
    mastered: "Revisit lesson",
  };
  const href = (step?: number) =>
    withChapter("/lesson", chapterId, {
      concept: concept.concept_id,
      ...(step ? { step: String(step) } : {}),
    });

  return (
    <div className="tree-branch l3 fade-up">
      <p className="tree-blurb">{nodeBlurb(concept, kind)}</p>
      {concept.personal_note && playable && (
        <div className={cn("tree-note", concept.personal === "focus" ? "focus" : "known")}>
          <Markdown className="prose-sm prose-p:my-0 prose-p:leading-snug prose-p:text-inherit">
            {concept.personal_note}
          </Markdown>
        </div>
      )}

      {playable && parts.length > 0 && (
        <ol className="tree-parts" aria-label="Parts of this lesson">
          {parts.map((label, i) => (
            <li key={label + i} className="tree-item l3">
              <Link href={href(i)} className="tree-row l3">
                <span className="tree-node l3" aria-hidden />
                <span className="tree-title">{label}</span>
              </Link>
            </li>
          ))}
        </ol>
      )}
      {playable && lesson.loading && <Skeleton rows={2} />}

      {cta[kind] ? (
        <Button asChild className="self-start">
          <Link href={href()}>
            <Play className="size-4" aria-hidden /> {cta[kind]}
          </Link>
        </Button>
      ) : (
        <Button disabled className="self-start">
          {kind === "locked" ? <Lock className="size-4" /> : <Clock className="size-4" />}
          {kind === "locked" ? "Locked" : "Soon"}
        </Button>
      )}
      {playable && parts.length > 0 && (
        <span className="tree-hint">
          <BookOpen size={12} aria-hidden /> Tap a part to jump straight to it.
        </span>
      )}
    </div>
  );
}
