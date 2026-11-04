// Shared bits of the roadmap: the node states and their wording, and the progress ring.
// The tree that uses them is components/roadmap-tree.tsx.
//
// States, in the student's words:
//   Mastered  two different questions right
//   Done      right once: the path moves on, Review masters it tomorrow
//   Next up   the personal recommendation
//   Open      ready, not yet done
//   Locked    opens when the concept before it is done
//   Soon      no lesson written yet in the student's interest

"use client";

import { Check, Clock, Lock, Play, Star } from "lucide-react";

import type { RoadmapConcept } from "@/lib/api";

export type NodeKind = "mastered" | "done" | "next" | "open" | "locked" | "soon";

export function kindOf(c: RoadmapConcept, nextId: string | undefined): NodeKind {
  if (c.has_lesson === false) return "soon";
  if (c.locked) return "locked";
  if (c.status === "mastered") return "mastered";
  if (c.progress_status === "partial") return "done";
  if (c.concept_id === nextId) return "next";
  return "open";
}

const ICON: Record<NodeKind, typeof Check> = {
  mastered: Star,
  done: Check,
  next: Play,
  open: Play,
  locked: Lock,
  soon: Clock,
};
export const NODE_ICON = ICON;

export function nodeSubline(c: RoadmapConcept, kind: NodeKind): string {
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

export function nodeBlurb(concept: RoadmapConcept, kind: NodeKind): string {
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
  return blurb[kind];
}

// ---------------------------------------------------------------------------
// The progress ring: green for done, gold for the part of it that's mastered.
// ---------------------------------------------------------------------------
export function ProgressRing({
  done,
  mastered,
  total,
  size = 76,
}: {
  done: number;
  mastered: number;
  total: number;
  size?: number;
}) {
  const stroke = Math.round(size / 10);
  const r = (size - stroke) / 2;
  const len = 2 * Math.PI * r;
  const arc = (n: number) => `${total ? (len * n) / total : 0} ${len}`;
  return (
    <div
      className="relative ml-auto shrink-0"
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
            className="stroke-[color:var(--gold)]"
          />
        )}
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <span className="font-heading text-xl font-bold leading-none text-foreground">{done}</span>
        <span className="text-[10px] text-muted-foreground">of {total}</span>
      </div>
    </div>
  );
}
