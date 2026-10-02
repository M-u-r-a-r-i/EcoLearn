// "My mix-ups" (/mix-ups): every misconception the student has shown, from the
// starting check, lesson checks and the end check, and whether it's fixed.
//
// The rule (server: learner_plan.mix_up_history) is deliberately strict, so
// "fixed" means something: right on a DIFFERENT question about the idea. Right
// again on the same question, after the app explained it, is "check again".

"use client";

import Link from "next/link";
import { ArrowRight, CheckCircle2, RotateCcw, Target } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { PageContainer } from "@/components/page-container";
import { Button } from "@/components/ui/button";
import { getMixUps, type CheckSource, type MixUp, type MixUpStatus } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { withChapter } from "@/lib/use-chapter";
import { cn } from "@/lib/utils";

const SOURCE: Record<CheckSource, string> = {
  start: "your starting check",
  lesson: "a lesson check",
  end: "your end check",
  review: "a revision question",
};

const GROUPS: { status: MixUpStatus; title: string; blurb: string; Icon: typeof Target; tone: string }[] = [
  {
    status: "active",
    title: "To fix",
    blurb: "Open the lesson, then answer its check. These are the ideas to work on first.",
    Icon: Target,
    tone: "text-destructive",
  },
  {
    status: "recheck",
    title: "Check again",
    blurb:
      "You got these right after the explanation. They count as fixed once you get a different question on them right: try a new one in Revision.",
    Icon: RotateCcw,
    tone: "text-brand-accent",
  },
  {
    status: "fixed",
    title: "Fixed",
    blurb: "Right on a different question about the same idea. That's the real thing.",
    Icon: CheckCircle2,
    tone: "text-success",
  },
];

function when(iso: string | null): string {
  return iso ? new Date(iso).toLocaleDateString(undefined, { day: "numeric", month: "short" }) : "";
}

export default function MixUpsPage() {
  const { data, error, loading } = useFetch("mix-ups", getMixUps);

  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex max-w-3xl flex-col gap-8">
        <div className="flex flex-col gap-2">
          <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
            My mix-ups
          </span>
          <h1 className="text-3xl font-bold tracking-tight text-foreground">What you&apos;ve fixed so far</h1>
          <p className="text-muted-foreground">
            Every wrong answer in EcoLearn was written to catch one particular mix-up. Here are the ones
            you&apos;ve shown, and which you&apos;ve already put right.
          </p>
        </div>

        {loading ? (
          <div className="h-48 animate-pulse rounded-xl bg-muted" />
        ) : !data ? (
          <FormError message={error ?? "Couldn't load your mix-ups."} />
        ) : data.items.length === 0 ? (
          <section className="rounded-xl border border-dashed border-border bg-card p-6 text-sm text-muted-foreground">
            No mix-ups yet. When a check shows one, it appears here — and moves to &ldquo;Fixed&rdquo; once you
            get a different question on it right.
            <Link href="/roadmap" className="mt-3 block font-semibold text-primary hover:underline">
              Go to your roadmap →
            </Link>
          </section>
        ) : (
          <>
            <div className="grid grid-cols-3 gap-3">
              {GROUPS.map((g) => (
                <div key={g.status} className="rounded-xl border border-border bg-card p-4 shadow-soft">
                  <div className="flex items-center gap-1.5 text-sm text-muted-foreground">
                    <g.Icon className={cn("size-4", g.tone)} aria-hidden /> {g.title}
                  </div>
                  <div className={cn("mt-1 text-3xl font-bold", g.status === "fixed" ? "text-success" : "text-foreground")}>
                    {data.summary[g.status]}
                  </div>
                </div>
              ))}
            </div>

            {GROUPS.map((g) => {
              const items = data.items.filter((i) => i.status === g.status);
              if (items.length === 0) return null;
              return (
                <section key={g.status} className="flex flex-col gap-3">
                  <div className="flex flex-col gap-1">
                    <h2 className={cn("flex items-center gap-2 text-lg font-bold", g.tone)}>
                      <g.Icon className="size-5" aria-hidden /> {g.title}
                    </h2>
                    <p className="text-sm text-muted-foreground">{g.blurb}</p>
                  </div>
                  <ul className="flex flex-col gap-2">
                    {items.map((m) => (
                      <MixUpRow key={m.concept_id} m={m} />
                    ))}
                  </ul>
                </section>
              );
            })}
          </>
        )}
      </PageContainer>
    </main>
  );
}

function MixUpRow({ m }: { m: MixUp }) {
  const fixed = m.status === "fixed";
  return (
    <li className="flex flex-col gap-2 rounded-xl border border-border bg-card p-4 sm:flex-row sm:items-center sm:justify-between sm:gap-4">
      <div className="flex flex-col gap-1">
        <span className="font-semibold text-foreground">
          {m.concept_name}
          {m.chapter_name && <span className="ml-2 text-xs font-normal text-muted-foreground">{m.chapter_name}</span>}
        </span>
        <span className={cn("text-sm", fixed ? "text-muted-foreground line-through decoration-success/60" : "text-foreground")}>
          {m.note}
        </span>
        <span className="text-xs text-muted-foreground">
          Found in {SOURCE[m.found_in]} on {when(m.found_at)}
          {m.times > 1 && ` · came up ${m.times} times`}
          {m.sure && !fixed && " · you were sure, so it's worth a careful look"}
          {m.fixed_in && ` · ${fixed ? "fixed" : "right"} in ${SOURCE[m.fixed_in]} on ${when(m.fixed_at)}`}
        </span>
      </div>
      {m.status === "recheck" ? (
        <Button variant="outline" size="sm" asChild className="shrink-0 self-start sm:self-auto">
          <Link href={`/review?concept=${encodeURIComponent(m.concept_id)}`}>
            New question <ArrowRight className="size-4" />
          </Link>
        </Button>
      ) : !fixed &&
        (m.has_lesson ? (
          <Button variant="outline" size="sm" asChild className="shrink-0 self-start sm:self-auto">
            <Link href={withChapter("/lesson", m.chapter_id, { concept: m.concept_id })}>
              Open the lesson <ArrowRight className="size-4" />
            </Link>
          </Button>
        ) : (
          <span className="shrink-0 text-xs text-muted-foreground">Lesson coming soon</span>
        ))}
    </li>
  );
}
