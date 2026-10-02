// The teacher's view of a class's pilot data: headline numbers, what the class
// is getting wrong (misconceptions, most common first), the hardest concepts,
// and the same numbers per interest.
//
// Every number is computed on the server (src/progress/metrics.py). The one
// choice a teacher needs to know about is spelled out on the page: accuracy is
// FIRST-TRY accuracy, because after a wrong pick the app shows the right answer
// and a retry proves little.

"use client";

import { useState } from "react";
import { BookOpen, Clock, Target, ThumbsUp, Users } from "lucide-react";

import { Markdown } from "@/components/markdown";
import { Button } from "@/components/ui/button";
import type { ClassInsights, MisconceptionInsight } from "@/lib/api";
import { cn } from "@/lib/utils";

const MISCONCEPTIONS_SHOWN = 5;

export function pct(value: number | null | undefined): string {
  return value === null || value === undefined ? "—" : `${Math.round(value * 100)}%`;
}

// Green from 70%, amber from 40%, red below — the same reading for every table.
function accuracyTone(value: number | null): string {
  if (value === null) return "text-muted-foreground";
  if (value >= 0.7) return "text-success";
  if (value >= 0.4) return "text-brand-accent";
  return "text-destructive";
}

export function ClassInsightsPanel({ insights }: { insights: ClassInsights }) {
  const { summary } = insights;
  if (summary.lessons_opened === 0 && summary.answers === 0) {
    return (
      <section className="rounded-xl border border-dashed border-border bg-card p-6 text-sm text-muted-foreground">
        <h2 className="mb-1 text-lg font-bold text-foreground">Class insights</h2>
        Nothing to show yet. Once students open lessons and answer the checks, you&apos;ll see how
        long they read, how many get it right first time, and the misconceptions that come up most.
      </section>
    );
  }

  return (
    <div className="flex flex-col gap-8">
      <SummaryTiles insights={insights} />
      <Misconceptions items={insights.misconceptions} />
      <HardestConcepts insights={insights} />
      {insights.interests.length > 0 && <ByInterest insights={insights} />}
    </div>
  );
}

function SummaryTiles({ insights }: { insights: ClassInsights }) {
  const s = insights.summary;
  const tiles = [
    {
      Icon: Users,
      label: "Active students",
      value: `${s.active_students} of ${s.students}`,
      note: "opened a lesson or answered a check",
    },
    {
      Icon: BookOpen,
      label: "Lessons opened",
      value: String(s.lessons_opened),
      note: `${s.distinct_lessons} different student × lesson`,
    },
    {
      Icon: Clock,
      label: "Reading time",
      value: `${s.active_minutes} min`,
      note:
        s.median_minutes_per_lesson === null
          ? "active time only"
          : `median ${s.median_minutes_per_lesson} min per lesson`,
    },
    {
      Icon: Target,
      label: "Right first time",
      value: pct(s.first_try_accuracy),
      note: `${s.first_try_correct} of ${s.first_try_answers} first answers`,
      tone: accuracyTone(s.first_try_accuracy),
    },
    {
      Icon: ThumbsUp,
      label: "Found it helpful",
      value: pct(s.approval),
      note: `👍 ${s.thumbs_up} · 👎 ${s.thumbs_down}`,
    },
  ];
  return (
    <section aria-label="Headline numbers" className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-5">
      {tiles.map(({ Icon, label, value, note, tone }) => (
        <div key={label} className="flex flex-col gap-1 rounded-xl border border-border bg-card p-4 shadow-soft">
          <span className="flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
            <Icon className="size-3.5" aria-hidden />
            {label}
          </span>
          <span className={cn("text-2xl font-bold text-foreground", tone)}>{value}</span>
          <span className="text-xs text-muted-foreground">{note}</span>
        </div>
      ))}
    </section>
  );
}

function Misconceptions({ items }: { items: MisconceptionInsight[] }) {
  const [showAll, setShowAll] = useState(false);
  const shown = showAll ? items : items.slice(0, MISCONCEPTIONS_SHOWN);

  return (
    <section className="flex flex-col gap-4 rounded-xl border border-border bg-card p-6 shadow-card">
      <div className="flex flex-col gap-1">
        <h2 className="text-lg font-bold text-foreground">What your class is getting wrong</h2>
        <p className="text-sm text-muted-foreground">
          Every wrong option in a check was written to catch one specific misconception. These are the
          ones your students chose, most common first, counted once per student.
        </p>
      </div>

      {items.length === 0 ? (
        <p className="text-sm text-muted-foreground">No wrong answers yet.</p>
      ) : (
        <ol className="flex flex-col gap-3">
          {shown.map((m) => (
            <li
              key={`${m.concept_id}|${m.interest}|${m.option}`}
              className="flex flex-col gap-3 rounded-xl border border-border p-4"
            >
              <div className="flex flex-wrap items-baseline justify-between gap-2">
                <span className="font-semibold text-foreground">
                  {m.concept_name}
                  <span className="ml-2 rounded-full bg-muted px-2 py-0.5 text-xs font-medium capitalize text-muted-foreground">
                    {m.interest}
                  </span>
                </span>
                <span className="text-sm font-semibold text-destructive">
                  {m.students} of {m.students_answered} students
                </span>
              </div>
              {/* The share as a bar: quick to compare down the list. */}
              <div
                className="h-1.5 w-full overflow-hidden rounded-full bg-muted"
                role="img"
                aria-label={`${pct(m.share)} of the students who answered`}
              >
                <div className="h-full rounded-full bg-destructive/70" style={{ width: pct(m.share) }} />
              </div>
              {m.misconception && (
                <p className="text-sm font-medium leading-relaxed text-foreground">{m.misconception}</p>
              )}
              {m.question && (
                <details className="group text-sm">
                  <summary className="cursor-pointer font-semibold text-primary marker:text-muted-foreground">
                    See the question
                  </summary>
                  <div className="mt-3 flex flex-col gap-2 border-l-2 border-border pl-4">
                    <Markdown className="prose-sm">{m.question}</Markdown>
                    {m.option_text && (
                      <div className="text-destructive">
                        <span className="font-semibold">They chose {m.option}:</span>
                        <Markdown className="prose-sm">{m.option_text}</Markdown>
                      </div>
                    )}
                    {m.correct_option && m.correct_text && (
                      <div className="text-success">
                        <span className="font-semibold">Right answer {m.correct_option}:</span>
                        <Markdown className="prose-sm">{m.correct_text}</Markdown>
                      </div>
                    )}
                  </div>
                </details>
              )}
            </li>
          ))}
        </ol>
      )}

      {items.length > MISCONCEPTIONS_SHOWN && (
        <Button variant="outline" className="self-start" onClick={() => setShowAll((v) => !v)}>
          {showAll ? "Show fewer" : `Show all ${items.length}`}
        </Button>
      )}
    </section>
  );
}

function HardestConcepts({ insights }: { insights: ClassInsights }) {
  const rows = insights.concepts.filter((c) => c.students_answered > 0 || c.students_opened > 0);
  if (rows.length === 0) return null;
  return (
    <section className="flex flex-col gap-3 rounded-xl border border-border bg-card p-6 shadow-card">
      <div className="flex flex-col gap-1">
        <h2 className="text-lg font-bold text-foreground">Concepts, hardest first</h2>
        <p className="text-sm text-muted-foreground">
          &ldquo;Right first time&rdquo; counts each student&apos;s first answer only: after a wrong
          answer the app shows the right one, so a second try proves little.
        </p>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm">
          <thead className="text-muted-foreground">
            <tr>
              <th className="py-2 pr-4 font-semibold">Concept</th>
              <th className="py-2 pr-4 font-semibold">Right first time</th>
              <th className="py-2 pr-4 font-semibold">Opened by</th>
              <th className="py-2 pr-4 font-semibold">Median reading</th>
              <th className="py-2 font-semibold">👍 / 👎</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((c) => (
              <tr key={c.concept_id} className="border-t border-border">
                <td className="py-2 pr-4">
                  <span className="font-medium text-foreground">{c.concept_name}</span>
                  {c.chapter_name && (
                    <span className="block text-xs text-muted-foreground">{c.chapter_name}</span>
                  )}
                </td>
                <td className="py-2 pr-4">
                  <span className={cn("font-semibold", accuracyTone(c.first_try_accuracy))}>
                    {pct(c.first_try_accuracy)}
                  </span>
                  {c.students_answered > 0 && (
                    <span className="text-muted-foreground">
                      {" "}
                      ({c.first_try_correct} of {c.students_answered})
                    </span>
                  )}
                </td>
                <td className="py-2 pr-4">{c.students_opened} students</td>
                <td className="py-2 pr-4">{c.median_minutes === null ? "—" : `${c.median_minutes} min`}</td>
                <td className="py-2">
                  {c.thumbs_up} / {c.thumbs_down}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

function ByInterest({ insights }: { insights: ClassInsights }) {
  return (
    <section className="flex flex-col gap-3 rounded-xl border border-border bg-card p-6 shadow-card">
      <h2 className="text-lg font-bold text-foreground">By interest</h2>
      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm">
          <thead className="text-muted-foreground">
            <tr>
              <th className="py-2 pr-4 font-semibold">Interest</th>
              <th className="py-2 pr-4 font-semibold">Students</th>
              <th className="py-2 pr-4 font-semibold">Lessons opened</th>
              <th className="py-2 pr-4 font-semibold">Right first time</th>
              <th className="py-2 font-semibold">Found it helpful</th>
            </tr>
          </thead>
          <tbody>
            {insights.interests.map((i) => (
              <tr key={i.interest} className="border-t border-border">
                <td className="py-2 pr-4 font-medium capitalize text-foreground">{i.interest}</td>
                <td className="py-2 pr-4">{i.students}</td>
                <td className="py-2 pr-4">{i.lessons_opened}</td>
                <td className={cn("py-2 pr-4 font-semibold", accuracyTone(i.first_try_accuracy))}>
                  {pct(i.first_try_accuracy)}
                </td>
                <td className="py-2">
                  {pct(i.approval)}{" "}
                  <span className="text-muted-foreground">
                    (👍 {i.thumbs_up} · 👎 {i.thumbs_down})
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
