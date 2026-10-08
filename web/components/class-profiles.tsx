// "Getting to know the class" (2026-10-08): what each student said about themselves in the
// first-login survey, next to how they actually read. Plain English, no scores: a teacher
// uses it to decide how to pitch the next lesson. Where what a student SAID about focus and
// what their lesson views SHOW disagree, both are on the row, so the teacher can judge.

"use client";

import { ChevronRight, UserRound } from "lucide-react";

import { getClassProfiles, type ClassProfiles, type ClassProfileStudent } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

const SPAN = { short: "Short", medium: "Medium", long: "Long" } as const;
const LEVEL = { novice: "New to it", fan: "Fan", player: "Player", expert: "Expert" } as const;
const FEEL = { love: "Likes it", ok: "Okay", nervous: "Nervous", dread: "Struggles" } as const;

function Bars({ title, rows }: { title: string; rows: { label: string; n: number }[] }) {
  const max = Math.max(1, ...rows.map((r) => r.n));
  return (
    <div className="flex flex-col gap-2 rounded-xl border border-border bg-card p-4 shadow-soft">
      <h3 className="text-sm font-bold text-foreground">{title}</h3>
      <ul className="flex flex-col gap-1.5">
        {rows.map((r) => (
          <li key={r.label} className="flex items-center gap-2 text-xs">
            <span className="w-16 shrink-0 text-muted-foreground">{r.label}</span>
            <span className="h-2 flex-1 overflow-hidden rounded-full bg-muted">
              <span className="block h-full rounded-full bg-primary" style={{ width: `${(r.n / max) * 100}%` }} />
            </span>
            <span className="w-5 text-right font-semibold text-foreground">{r.n}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

function saidVsShown(s: ClassProfileStudent): string | null {
  const o = s.observed;
  if (o.median_minutes === null || o.skim_share === null) return null;
  const skims = Math.round(o.skim_share * 100);
  return `Reads about ${o.median_minutes} min a lesson; ${skims}% of ${o.views} lessons skimmed (under 30 s).`;
}

function Row({ s }: { s: ClassProfileStudent }) {
  const shown = saidVsShown(s);
  return (
    <li>
      <details className="group border-t border-border first:border-t-0">
        <summary className="flex cursor-pointer list-none items-center gap-3 px-4 py-3 marker:content-none">
          <ChevronRight className="size-4 shrink-0 text-muted-foreground transition-transform group-open:rotate-90" />
          <span className="flex-1 font-medium text-foreground">{s.name}</span>
          {s.taken ? (
            <span className="flex flex-wrap justify-end gap-1.5 text-[11px] font-semibold">
              {s.focus_span && (
                <span
                  className={cn(
                    "rounded-full px-2 py-0.5",
                    s.focus_span === "short" ? "bg-brand-accent/15 text-brand-accent" : "bg-muted text-muted-foreground",
                  )}
                >
                  Focus: {SPAN[s.focus_span]}
                </span>
              )}
              {s.hobby_level && (
                <span className="rounded-full bg-muted px-2 py-0.5 text-muted-foreground">{LEVEL[s.hobby_level]}</span>
              )}
            </span>
          ) : (
            <span className="rounded-full bg-muted px-2 py-0.5 text-[11px] font-semibold text-muted-foreground">
              Not answered yet
            </span>
          )}
        </summary>
        <div className="flex flex-col gap-1.5 px-11 pb-4 text-sm text-muted-foreground">
          {s.taken ? (
            <>
              <ul className="list-disc pl-4">
                {s.summary.map((line) => (
                  <li key={line}>{line}</li>
                ))}
              </ul>
              {shown && <p className="text-foreground">Lesson views: {shown}</p>}
            </>
          ) : (
            <p>They&apos;ll be asked at their next sign-in.</p>
          )}
        </div>
      </details>
    </li>
  );
}

function Panel({ p }: { p: ClassProfiles }) {
  const { summary } = p;
  return (
    <div className="flex flex-col gap-4">
      <p className="text-sm text-muted-foreground">
        <strong className="text-foreground">
          {summary.taken} of {summary.total}
        </strong>{" "}
        students have answered. This is what they said about themselves, not a test.
      </p>
      {summary.taken > 0 && (
        <div className="grid gap-3 sm:grid-cols-3">
          <Bars
            title="How long they focus"
            rows={(["short", "medium", "long"] as const).map((k) => ({ label: SPAN[k], n: summary.focus[k] }))}
          />
          <Bars
            title="Their main hobby"
            rows={(["novice", "fan", "player", "expert"] as const).map((k) => ({ label: LEVEL[k], n: summary.hobby_level[k] }))}
          />
          <Bars
            title="Feeling about physics"
            rows={(["love", "ok", "nervous", "dread"] as const).map((k) => ({ label: FEEL[k], n: summary.physics_feel[k] ?? 0 }))}
          />
        </div>
      )}
      <ul className="overflow-hidden rounded-xl border border-border bg-card">
        {p.students.map((s) => (
          <Row key={s.student_id} s={s} />
        ))}
      </ul>
    </div>
  );
}

export function ClassProfilesPanel({ classId }: { classId: string }) {
  const profiles = useFetch(`profiles:${classId}`, () => getClassProfiles(classId));
  return (
    <section className="flex flex-col gap-3 rounded-xl border border-border bg-card p-6 shadow-card">
      <h2 className="flex items-center gap-2 text-lg font-bold text-foreground">
        <UserRound className="size-5 text-primary" aria-hidden /> Getting to know the class
      </h2>
      {profiles.loading ? (
        <div className="h-32 animate-pulse rounded-xl bg-muted" />
      ) : profiles.data ? (
        <Panel p={profiles.data} />
      ) : (
        <p className="text-sm text-destructive">{profiles.error ?? "Couldn't load this."}</p>
      )}
    </section>
  );
}
