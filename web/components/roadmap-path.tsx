// The roadmap as a game-style level map (2026-10-04).
//
// A winding path of big round nodes, one per concept. Tap a node (or its label)
// to select it: a sheet at the bottom says what it is and offers the action.
// The geometry is fixed (every row is ROW px tall) so the connecting curve can
// be drawn as one SVG behind the buttons without measuring anything.
//
// States, in the student's words:
//   Mastered  gold    two different questions right
//   Done      green   right once: the path moves on, Review masters it tomorrow
//   Next up   pulsing the personal recommendation
//   Open      outline ready, not yet done
//   Locked    grey    opens when the concept before it is done
//   Soon      dashed  no lesson written yet in the student's interest
// Motion is plain CSS (see "Roadmap motion" in globals.css) and switches off for
// people who prefer reduced motion.

"use client";

import Link from "next/link";
import { Check, Clock, Lock, Play, Target } from "lucide-react";

import { Markdown } from "@/components/markdown";
import { PrimaryButton } from "@/components/primary-button";
import type { RoadmapConcept } from "@/lib/api";
import { withChapter } from "@/lib/use-chapter";
import { cn } from "@/lib/utils";

export type NodeKind = "mastered" | "done" | "next" | "open" | "locked" | "soon";

export function kindOf(c: RoadmapConcept, nextId: string | undefined): NodeKind {
  if (c.has_lesson === false) return "soon";
  if (c.locked) return "locked";
  if (c.status === "mastered") return "mastered";
  if (c.progress_status === "partial") return "done";
  if (c.concept_id === nextId) return "next";
  return "open";
}

// ---------------------------------------------------------------------------
// Geometry
// ---------------------------------------------------------------------------
const ROW = 112; // height of one step
const COL = 120; // width of the path column
const NODE = 64; // node diameter
const OFFSETS = [0, 20, 28, 20, 0, -20, -28, -20]; // a gentle S-curve, px from the column's centre
const cx = (i: number) => COL / 2 + OFFSETS[i % OFFSETS.length];
const cy = (i: number) => ROW * i + ROW / 2;

const NODE_STYLE: Record<NodeKind, string> = {
  mastered:
    "border-amber-500 bg-gradient-to-br from-amber-300 to-amber-500 text-amber-950 rm-glow",
  done: "border-success bg-success text-success-foreground",
  next: "border-primary bg-primary text-primary-foreground shadow-card-hover",
  open: "border-primary bg-card text-primary",
  locked: "border-border bg-muted text-muted-foreground",
  soon: "border-dashed border-border bg-muted/50 text-muted-foreground",
};

const ICON: Record<NodeKind, typeof Check> = {
  mastered: Check,
  done: Check,
  next: Play,
  open: Play,
  locked: Lock,
  soon: Clock,
};

function subline(c: RoadmapConcept, kind: NodeKind): string {
  switch (kind) {
    case "mastered":
      return "Mastered";
    case "done":
      return "Done · revise tomorrow";
    case "next":
      return "Next up";
    case "locked":
      return c.locked_reason ?? "Locked";
    case "soon":
      return "Coming soon";
    default:
      return c.attempts ? `Tried ${c.attempts}× · not right yet` : "Ready to learn";
  }
}

export function PathMap({
  concepts,
  nextId,
  selectedId,
  onSelect,
  fresh,
  shakeId,
}: {
  concepts: RoadmapConcept[];
  nextId: string | undefined;
  selectedId: string | undefined;
  onSelect: (id: string) => void;
  fresh: string[]; // concepts that became done since the student was last here
  shakeId: string | null;
}) {
  const n = concepts.length;
  const kinds = concepts.map((c) => kindOf(c, nextId));
  const finished = (k: NodeKind) => k === "done" || k === "mastered";

  return (
    <div className="relative" style={{ height: n * ROW }}>
      {/* The path: green once the step before it is finished, a dotted line ahead. */}
      <svg
        className="absolute left-0 top-0"
        width={COL}
        height={n * ROW}
        aria-hidden
        fill="none"
      >
        {concepts.slice(0, -1).map((c, i) => {
          const d = `M ${cx(i)} ${cy(i)} C ${cx(i)} ${cy(i) + ROW / 2}, ${cx(i + 1)} ${cy(i + 1) - ROW / 2}, ${cx(i + 1)} ${cy(i + 1)}`;
          return finished(kinds[i]) ? (
            <path
              key={c.concept_id}
              d={d}
              className="rm-draw stroke-success"
              style={{ ["--len" as string]: 150 }}
              strokeWidth={6}
              strokeLinecap="round"
            />
          ) : (
            <path
              key={c.concept_id}
              d={d}
              className="stroke-border"
              strokeWidth={5}
              strokeLinecap="round"
              strokeDasharray="1 11"
            />
          );
        })}
      </svg>

      {concepts.map((c, i) => {
        const kind = kinds[i];
        const Icon = ICON[kind];
        const selected = c.concept_id === selectedId;
        const dim = kind === "locked" || kind === "soon";
        return (
          <button
            key={c.concept_id}
            type="button"
            onClick={() => onSelect(c.concept_id)}
            aria-pressed={selected}
            aria-label={`${c.name}. ${subline(c, kind).replace(/\.$/, "")}.`}  // one full stop, even if the subline already ends in one
            className={cn(
              "absolute inset-x-0 rounded-2xl text-left transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
              selected ? "bg-primary/5 ring-1 ring-primary/30" : "hover:bg-muted/40",
            )}
            style={{ top: ROW * i + 4, height: ROW - 8 }}
          >
            {/* Node */}
            <span
              className={cn(
                "absolute flex items-center justify-center rounded-full border-4 shadow-soft transition-transform duration-200",
                selected && "scale-110",
                NODE_STYLE[kind],
                fresh.includes(c.concept_id) && "rm-pop",
                shakeId === c.concept_id && "rm-shake",
              )}
              style={{ width: NODE, height: NODE, left: cx(i) - NODE / 2, top: (ROW - 8) / 2 - NODE / 2 }}
            >
              {kind === "next" && (
                <>
                  <span className="rm-pulse absolute inset-0 rounded-full bg-primary/40" aria-hidden />
                  <span
                    className="rm-bob absolute -top-7 left-1/2 -translate-x-1/2 rounded-full bg-primary px-2.5 py-0.5 text-[10px] font-extrabold tracking-wider text-primary-foreground shadow-soft"
                    aria-hidden
                  >
                    START
                  </span>
                </>
              )}
              <Icon className="relative size-7" strokeWidth={kind === "next" || kind === "open" ? 2.5 : 3} />
            </span>

            {/* Label */}
            <span
              className="absolute inset-y-0 right-3 flex flex-col justify-center gap-0.5"
              style={{ left: COL + 4 }}
            >
              <span className="text-[11px] font-bold uppercase tracking-wider text-muted-foreground">
                Step {i + 1}
              </span>
              <span
                className={cn(
                  "text-base font-semibold leading-snug",
                  dim ? "text-muted-foreground" : "text-foreground",
                )}
              >
                {c.name}
              </span>
              <span
                className={cn(
                  "line-clamp-2 text-xs",
                  kind === "mastered"
                    ? "font-semibold text-amber-500"
                    : kind === "done"
                      ? "font-semibold text-success"
                      : "text-muted-foreground",
                )}
              >
                {subline(c, kind)}
              </span>
              {!dim && c.personal === "focus" && (
                <span className="mt-0.5 inline-flex w-fit items-center gap-1 rounded-full bg-destructive/10 px-2 py-0.5 text-[11px] font-semibold text-destructive">
                  <Target className="size-3" aria-hidden /> Focus
                </span>
              )}
              {!dim && c.personal === "known" && kind !== "done" && kind !== "mastered" && (
                <span className="mt-0.5 inline-flex w-fit rounded-full bg-success/10 px-2 py-0.5 text-[11px] font-semibold text-success">
                  Know it? Prove it
                </span>
              )}
            </span>
          </button>
        );
      })}
    </div>
  );
}

// ---------------------------------------------------------------------------
// The sheet: what the selected step is, and the one thing to do next.
// ---------------------------------------------------------------------------
export function StepSheet({
  concept,
  kind,
  index,
  chapterId,
}: {
  concept: RoadmapConcept;
  kind: NodeKind;
  index: number;
  chapterId: string;
}) {
  const blurb: Record<NodeKind, string> = {
    mastered: "You've answered two different questions on this right. It's yours.",
    done: "Right once. A new question tomorrow (in Review) makes it mastered.",
    next: "This is where your path continues.",
    open: concept.attempts
      ? "You've tried this one. Read the lesson again, then retry the check."
      : "Read the lesson, then answer one question.",
    locked: concept.locked_reason ?? "Finish the step before it first.",
    soon: "The lesson for this is still being written in your interest.",
  };
  const cta: Partial<Record<NodeKind, string>> = {
    next: "Start lesson",
    open: concept.attempts ? "Try again" : "Start lesson",
    done: "Review lesson",
    mastered: "Revisit lesson",
  };
  const href = withChapter("/lesson", chapterId, { concept: concept.concept_id });

  return (
    <section
      key={concept.concept_id}
      aria-live="polite"
      className="rm-sheet sticky bottom-3 z-20 flex items-center gap-3 rounded-2xl border border-border bg-card/95 p-3 shadow-card-hover backdrop-blur"
    >
      <div className="flex min-w-0 flex-1 flex-col gap-0.5">
        <span className="text-[11px] font-bold uppercase tracking-wider text-muted-foreground">
          Step {index + 1}
        </span>
        <h2 className="line-clamp-2 text-base font-bold leading-snug text-foreground">{concept.name}</h2>
        <p className="line-clamp-2 text-xs text-muted-foreground">{blurb[kind]}</p>
        {concept.personal_note && kind !== "locked" && kind !== "soon" && (
          <div
            className={cn(
              "line-clamp-2 flex items-start gap-1 text-xs",
              concept.personal === "focus" ? "text-destructive" : "text-success",
            )}
          >
            {concept.personal === "focus" && <Target className="mt-px size-3 shrink-0" aria-hidden />}
            <Markdown className="prose-sm prose-p:my-0 prose-p:leading-snug prose-p:text-inherit">{concept.personal_note}</Markdown>
          </div>
        )}
      </div>
      {cta[kind] ? (
        <PrimaryButton asChild className="h-11 shrink-0 px-5">
          <Link href={href}>
            <Play className="size-4" /> {cta[kind]}
          </Link>
        </PrimaryButton>
      ) : (
        <PrimaryButton disabled className="h-11 shrink-0 px-5">
          {kind === "locked" ? <Lock className="size-4" /> : <Clock className="size-4" />}
          {kind === "locked" ? "Locked" : "Soon"}
        </PrimaryButton>
      )}
    </section>
  );
}

// ---------------------------------------------------------------------------
// The progress ring: green for done, gold for the part of it that's mastered.
// ---------------------------------------------------------------------------
export function ProgressRing({
  done,
  mastered,
  total,
}: {
  done: number;
  mastered: number;
  total: number;
}) {
  const size = 112;
  const stroke = 11;
  const r = (size - stroke) / 2;
  const len = 2 * Math.PI * r;
  const arc = (n: number) => `${total ? (len * n) / total : 0} ${len}`;
  return (
    <div
      className="relative shrink-0"
      style={{ width: size, height: size }}
      role="img"
      aria-label={`${done} of ${total} concepts done, ${mastered} mastered`}
    >
      <svg width={size} height={size} className="-rotate-90" fill="none">
        <circle cx={size / 2} cy={size / 2} r={r} strokeWidth={stroke} className="stroke-muted" />
        {done > 0 && (
          <circle
            cx={size / 2}
            cy={size / 2}
            r={r}
            strokeWidth={stroke}
            strokeLinecap="round"
            strokeDasharray={arc(done)}
            className="stroke-success"
          />
        )}
        {mastered > 0 && (
          <circle
            cx={size / 2}
            cy={size / 2}
            r={r}
            strokeWidth={stroke}
            strokeLinecap="round"
            strokeDasharray={arc(mastered)}
            className="stroke-amber-400"
          />
        )}
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <span className="text-2xl font-extrabold leading-none text-foreground">{done}</span>
        <span className="text-xs text-muted-foreground">of {total} done</span>
      </div>
    </div>
  );
}
