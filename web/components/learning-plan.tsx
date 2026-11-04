// A student's learning plan, from the starting check and their lesson answers.
//
// <LearningPlanSummary> — the full view, shown right after the starting check.
// <LearningPlanCard>    — the compact version at the top of the roadmap: an
//                         invitation to take the check, or what to focus on.
//
// The plan only ever *suggests*: nothing is locked, so every concept stays one
// click away whatever the plan says.

"use client";

import Link from "next/link";
import { ArrowRight, ChevronRight, Compass, Flag, Lightbulb, RotateCcw, Target } from "lucide-react";

import { CountUp } from "@/components/count-up";
import { Markdown } from "@/components/markdown";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";
import {
  getEndCheck,
  getLearningPlan,
  getRevision,
  type FocusItem,
  type LearningPlan,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { withChapter } from "@/lib/use-chapter";

function FocusList({ items }: { items: FocusItem[] }) {
  return (
    <ul className="flex flex-col gap-2">
      {items.map((f) => (
        <li key={f.concept_id} className="flex min-w-0 flex-col gap-2 rounded-2xl border border-border bg-card p-4">
          <div className="flex flex-col gap-0.5">
            <span className="font-heading font-bold text-foreground">
              {f.concept_name}
              {f.chapter_name && (
                <span className="ml-2 text-xs font-normal text-muted-foreground">{f.chapter_name}</span>
              )}
            </span>
            <Markdown className="prose-sm prose-p:my-0 prose-p:leading-snug prose-p:text-muted-foreground">{f.note}</Markdown>
          </div>
          {f.has_lesson ? (
            <Button variant="outline" size="sm" asChild className="shrink-0 self-start">
              <Link href={withChapter("/lesson", f.chapter_id, { concept: f.concept_id })}>
                Fix this <ArrowRight className="size-4" />
              </Link>
            </Button>
          ) : (
            <span className="shrink-0 text-xs text-muted-foreground">Lesson coming soon</span>
          )}
        </li>
      ))}
    </ul>
  );
}

export function LearningPlanSummary({ plan }: { plan: LearningPlan }) {
  const { check } = plan;
  const stats = [
    { label: "you already know", value: check.known, tone: "text-success" },
    { label: check.mix_ups === 1 ? "mix-up to fix" : "mix-ups to fix", value: check.mix_ups, tone: "text-destructive" },
    { label: "not sure yet", value: check.unsure, tone: "text-brand-accent" },
  ];
  return (
    <div className="flex flex-col gap-6">
      {check.taken && (
        <div className="grid grid-cols-3 gap-3">
          {stats.map((s) => (
            <div key={s.label} className="surface flex flex-col p-4 text-center">
              <span className={`font-heading text-3xl font-bold ${s.tone}`}>
                <CountUp value={s.value} />
              </span>
              <span className="text-xs text-muted-foreground">{s.label}</span>
            </div>
          ))}
        </div>
      )}

      {plan.focus.length > 0 ? (
        <section className="flex flex-col gap-3">
          <h2 className="display flex items-center gap-2 text-xl font-bold text-foreground">
            <Target className="size-5 text-destructive" aria-hidden /> Worth fixing first
          </h2>
          <FocusList items={plan.focus} />
        </section>
      ) : (
        check.taken && (
          <p className="rounded-xl border border-success/30 bg-success/5 p-4 text-sm text-foreground">
            No mix-ups showed up. Nice — your lessons will start from what&apos;s new to you.
          </p>
        )
      )}

      {plan.known.length > 0 && (
        <p className="flex items-start gap-2 text-sm text-muted-foreground">
          <Lightbulb className="mt-0.5 size-4 shrink-0 text-success" aria-hidden />
          <span>
            You seem to know <strong className="text-foreground">{plan.known.map((k) => k.concept_name).join(", ")}</strong>.
            Your roadmap skips ahead of {plan.known.length === 1 ? "it" : "them"} — you can still open
            {plan.known.length === 1 ? " it" : " them"} or take the check to confirm.
          </span>
        </p>
      )}

      {plan.start && (
        <div className="flex flex-col gap-3 rounded-[18px] bg-[color-mix(in_srgb,var(--brand)_9%,var(--surface))] p-5">
          <span className="text-sm text-muted-foreground">{plan.start.reason}</span>
          <PrimaryButton asChild className="self-start">
            <Link href={withChapter("/roadmap", plan.start.chapter_id)}>
              Start with {plan.start.chapter_name} <ArrowRight className="size-5" />
            </Link>
          </PrimaryButton>
        </div>
      )}
    </div>
  );
}

// The roadmap's side cards (house style `.side-action`): an icon tile, a title, one
// line, and a chevron. The whole card is the link.
function SideAction({
  href,
  tone,
  icon,
  title,
  text,
}: {
  href: string;
  tone: "revise" | "end" | "plan";
  icon: React.ReactNode;
  title: string;
  text: string;
}) {
  return (
    <Link href={href} className="side-action card-hover">
      <span className={`side-action-icon ${tone}`} aria-hidden>
        {icon}
      </span>
      <div>
        <b>{title}</b>
        <small>{text}</small>
      </div>
      <ChevronRight aria-hidden />
    </Link>
  );
}

// Shown on the roadmap only while the teacher has the end check open and the
// student hasn't taken it. Silent otherwise (and if the request fails).
export function EndCheckCard() {
  const { data } = useFetch("end-check", getEndCheck);
  if (data?.status !== "open") return null;
  return (
    <SideAction
      href="/end-check"
      tone="end"
      icon={<Flag className="size-[18px]" />}
      title="Take the end check"
      text="Five minutes to see which mix-ups you've fixed since the start."
    />
  );
}

// On the roadmap while revision questions are due. Silent otherwise.
export function RevisionCard() {
  const { data } = useFetch("revision", getRevision);
  const due = data?.due.length ?? 0;
  if (due === 0) return null;
  return (
    <SideAction
      href="/review"
      tone="revise"
      icon={<RotateCcw className="size-[18px]" />}
      title="Revise now"
      text={`${due === 1 ? "1 idea is" : `${due} ideas are`} ready: a new question on each, and they're mastered.`}
    />
  );
}

// The roadmap's version: one line to start the check, or a short plan.
export function LearningPlanCard({ chapterId }: { chapterId: string }) {
  const { data: plan } = useFetch("learning-plan", getLearningPlan);
  if (!plan) return null; // quiet while loading or if it fails: the roadmap still works

  if (!plan.check.taken) {
    return (
      <SideAction
        href="/start"
        tone="plan"
        icon={<Compass className="size-[18px]" />}
        title="Start the check"
        text="Take the 5-minute starting check, and your roadmap will skip what you already know."
      />
    );
  }

  const focus = plan.focus.filter((f) => f.has_lesson).slice(0, 3);
  const elsewhere = plan.start && plan.start.chapter_id !== chapterId;
  if (focus.length === 0 && !elsewhere) return null;

  return (
    <details className="group surface p-4" open>
      <summary className="flex cursor-pointer items-center gap-2 font-heading text-sm font-bold text-foreground">
        <Target className="size-4 text-primary" aria-hidden />
        Your plan
        {focus.length > 0 && (
          <span className="font-sans font-normal text-muted-foreground">
            · {plan.focus.length} {plan.focus.length === 1 ? "mix-up" : "mix-ups"} to fix
          </span>
        )}
      </summary>
      <div className="mt-3 flex flex-col gap-3">
        {focus.length > 0 && <FocusList items={focus} />}
        <Link href="/mix-ups" className="text-sm font-semibold text-primary hover:underline">
          All your mix-ups, and what you&apos;ve fixed →
        </Link>
        {elsewhere && plan.start && (
          <Link
            href={withChapter("/roadmap", plan.start.chapter_id)}
            className="text-sm font-semibold text-primary hover:underline"
          >
            Suggested start: {plan.start.chapter_name} →
          </Link>
        )}
      </div>
    </details>
  );
}
