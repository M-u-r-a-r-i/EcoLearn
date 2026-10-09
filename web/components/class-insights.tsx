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
import { AlertTriangle, BookOpen, Clock, Target, ThumbsUp, Users } from "lucide-react";

import { INTEREST_COLOR } from "@/components/ui-kit";

import { Markdown } from "@/components/markdown";
import { Button } from "@/components/ui/button";
import type { ClassInsights, MisconceptionInsight } from "@/lib/api";
import { cn } from "@/lib/utils";

const MISCONCEPTIONS_SHOWN = 5;

export function pct(value: number | null | undefined): string {
  return value === null || value === undefined ? "—" : `${Math.round(value * 100)}%`;
}

// Green from 70%, amber from 40%, red below: the same reading for every table.
function accuracyClass(value: number | null): string {
  if (value === null) return "text-muted-foreground";
  if (value >= 0.7) return "tone-good";
  if (value >= 0.4) return "tone-mid";
  return "tone-bad";
}

export function ClassInsightsPanel({ insights }: { insights: ClassInsights }) {
  const { summary } = insights;
  if (summary.lessons_opened === 0 && summary.answers === 0) {
    return (
      <section className="surface !border-dashed p-6 text-sm text-muted-foreground">
        <h2 className="display mb-1 text-lg font-bold text-foreground">Class insights</h2>
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
      tone: "mint",
      label: "Active students",
      value: `${s.active_students} of ${s.students}`,
      note: "opened a lesson or answered a check",
    },
    {
      Icon: BookOpen,
      tone: "sky",
      label: "Lessons opened",
      value: String(s.lessons_opened),
      note: `${s.distinct_lessons} different student × lesson`,
    },
    {
      Icon: Clock,
      tone: "lav",
      label: "Reading time",
      value: `${s.active_minutes} min`,
      note:
        s.median_minutes_per_lesson === null
          ? "active time only"
          : `median ${s.median_minutes_per_lesson} min per lesson`,
    },
    {
      Icon: Target,
      tone: "peach",
      label: "Right first time",
      value: pct(s.first_try_accuracy),
      note: `${s.first_try_correct} of ${s.first_try_answers} first answers`,
      state: s.first_try_accuracy === null ? "" : s.first_try_accuracy >= 0.7 ? "good" : s.first_try_accuracy < 0.4 ? "bad" : "",
    },
    {
      Icon: ThumbsUp,
      tone: "sun",
      label: "Found it helpful",
      value: pct(s.approval),
      note: `👍 ${s.thumbs_up} · 👎 ${s.thumbs_down}`,
    },
    {
      // Wrong while sure: a firmly held misconception, the ones to discuss in class.
      Icon: AlertTriangle,
      tone: "peach",
      label: "Sure but wrong",
      value: String(s.sure_but_wrong),
      note:
        s.by_confidence.sure.answers > 0
          ? `right ${pct(s.by_confidence.sure.accuracy)} when sure, ${pct(s.by_confidence.guess.accuracy)} when guessing`
          : "first answers given with \"I'm sure\"",
      state: s.sure_but_wrong > 0 ? "bad" : "",
    },
  ];
  return (
    <section aria-label="Headline numbers" className="dash-metrics six">
      {tiles.map(({ Icon, tone, label, value, note, state }) => (
        <div key={label} className={cn("surface dash-metric", `tone-${tone}`)}>
          <div className="dash-metric-top">
            <span className="dash-icon" aria-hidden>
              <Icon />
            </span>
            <span className="dash-label">{label}</span>
          </div>
          <span className={cn("dash-value", state)}>{value}</span>
          <span className="dash-note">{note}</span>
        </div>
      ))}
    </section>
  );
}

function Misconceptions({ items }: { items: MisconceptionInsight[] }) {
  const [showAll, setShowAll] = useState(false);
  const shown = showAll ? items : items.slice(0, MISCONCEPTIONS_SHOWN);

  return (
    <section className="surface panel flex flex-col gap-4">
      <div>
        <p className="eyebrow">Worth a second look</p>
        <h2 className="display text-2xl font-semibold text-foreground">What your class is getting wrong</h2>
        <p className="dash-sub">
          Every wrong option in a check was written to catch one specific misconception. These are the
          ones your students chose, most common first, counted once per student.
        </p>
      </div>

      {items.length === 0 ? (
        <p className="text-sm text-muted-foreground">No wrong answers yet.</p>
      ) : (
        <ol className="dmix">
          {shown.map((m, i) => (
            <li key={`${m.concept_id}|${m.interest}|${m.option}`} className="dmix-item">
              <span className="dmix-rank" aria-hidden>
                {i + 1}
              </span>
              <div className="dmix-body">
                <div className="dmix-head">
                  <b>
                    {m.concept_name} <span className="dchip">{m.interest}</span>
                  </b>
                  <span className="dmix-count">
                    {m.students} of {m.students_answered} students
                    {m.sure > 0 && <span className="font-normal"> · {m.sure} sure of it</span>}
                  </span>
                </div>
                {/* The share as a bar: quick to compare down the list. */}
                <div className="dbar">
                  <div className="dbar-track" role="img" aria-label={`${pct(m.share)} of the students who answered`}>
                    <span className="dbar-fill bad" style={{ width: pct(m.share), display: "block" }} />
                  </div>
                  <span className="dbar-pct">{pct(m.share)}</span>
                </div>
                {m.misconception && <p className="dmix-text">{m.misconception}</p>}
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
              </div>
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
    <section className="surface panel flex flex-col gap-3">
      <div>
        <p className="eyebrow">Where it gets hard</p>
        <h2 className="display text-2xl font-semibold text-foreground">Concepts, hardest first</h2>
        <p className="dash-sub">
          &ldquo;Right first time&rdquo; counts each student&apos;s first answer only: after a wrong
          answer the app shows the right one, so a second try proves little.
        </p>
      </div>
      <div className="dtable-wrap">
        <table className="dtable">
          <thead>
            <tr>
              <th>Concept</th>
              <th>Right first time</th>
              <th>Opened by</th>
              <th>Median reading</th>
              <th>👍 / 👎</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((c) => (
              <tr key={c.concept_id}>
                <td>
                  <span className="font-semibold text-foreground">{c.concept_name}</span>
                  {c.chapter_name && (
                    <span className="block text-xs text-muted-foreground">{c.chapter_name}</span>
                  )}
                </td>
                <td data-label="Right first time">
                  <span className={accuracyClass(c.first_try_accuracy)}>{pct(c.first_try_accuracy)}</span>
                  {c.students_answered > 0 && (
                    <span className="text-muted-foreground">
                      {" "}
                      ({c.first_try_correct} of {c.students_answered})
                    </span>
                  )}
                </td>
                <td data-label="Opened by">{c.students_opened} students</td>
                <td data-label="Median reading">{c.median_minutes === null ? "—" : `${c.median_minutes} min`}</td>
                <td data-label="👍 / 👎">
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
    <section className="surface panel flex flex-col gap-4">
      <div>
        <p className="eyebrow">Does the interest matter?</p>
        <h2 className="display text-2xl font-semibold text-foreground">By interest</h2>
      </div>
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {insights.interests.map((i) => (
          <div key={i.interest} className="soft-surface grid gap-2 p-4">
            <div className="flex items-center justify-between gap-2">
              <span className="flex items-center gap-2 font-heading text-base font-bold capitalize text-foreground">
                <span
                  aria-hidden
                  className="size-3 rounded-full"
                  style={{ background: INTEREST_COLOR[i.interest] ?? "var(--brand)" }}
                />
                {i.interest}
              </span>
              <span className="text-xs text-muted-foreground">
                {i.students} {i.students === 1 ? "student" : "students"}
              </span>
            </div>
            <div className="dbar">
              <div className="dbar-track" role="img" aria-label={`Right first time ${pct(i.first_try_accuracy)}`}>
                <span
                  className="dbar-fill after"
                  style={{ width: pct(i.first_try_accuracy), display: "block", background: INTEREST_COLOR[i.interest] }}
                />
              </div>
              <span className={cn("dbar-pct", accuracyClass(i.first_try_accuracy))}>{pct(i.first_try_accuracy)}</span>
            </div>
            <span className="dash-note">
              right first time · {i.lessons_opened} lessons opened · {pct(i.approval)} found it helpful (👍 {i.thumbs_up} · 👎{" "}
              {i.thumbs_down})
            </span>
          </div>
        ))}
      </div>
    </section>
  );
}
