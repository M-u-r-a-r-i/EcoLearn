// The top of a class page (2026-10-08): a four-number snapshot, then a "Needs attention"
// list. Everything is derived in the browser from data the page already loads (class detail,
// insights, the checks, the "getting to know you" profiles): no new API, no new numbers.
// Each attention item says who, in plain words, and where to look next.
//
// A missing piece (still loading, or it failed) just leaves its tile or item out: the
// snapshot never blocks the rest of the page.

"use client";

import { useState } from "react";
import {
  AlertTriangle,
  BookOpen,
  CheckCircle2,
  Flag,
  Moon,
  Target,
  UserRound,
  Users,
  Zap,
} from "lucide-react";

import { pct } from "@/components/class-insights";
import type { ClassChecks, ClassInsights, ClassProfiles, ClassStudent } from "@/lib/api";
import { cn } from "@/lib/utils";

const DAY_MS = 24 * 60 * 60 * 1000;
const INACTIVE_DAYS = 7;

export type ClassTab = "overview" | "insights" | "students" | "ai";

const TILE_ICON = {
  Started: { Icon: Users, tone: "mint" },
  "Right first time": { Icon: Target, tone: "peach" },
  "Getting to know you": { Icon: UserRound, tone: "lav" },
  "End check": { Icon: Flag, tone: "sky" },
} as const;

function Tile({ label, value, sub, tone }: { label: string; value: string; sub: string; tone?: "good" | "warn" }) {
  const { Icon, tone: color } = TILE_ICON[label as keyof typeof TILE_ICON] ?? { Icon: BookOpen, tone: "sun" };
  return (
    <div className={cn("surface dash-metric", `tone-${color}`)}>
      <div className="dash-metric-top">
        <span className="dash-icon" aria-hidden>
          <Icon />
        </span>
        <span className="dash-label">{label}</span>
      </div>
      <span className={cn("dash-value", tone === "good" && "good")}>{value}</span>
      <span className="dash-note">{sub}</span>
    </div>
  );
}

export function ClassSnapshot({
  students,
  insights,
  checks,
  profiles,
}: {
  students: ClassStudent[];
  insights: ClassInsights | null;
  checks: ClassChecks | null;
  profiles: ClassProfiles | null;
}) {
  const started = students.filter((s) => s.attempted > 0).length;
  const summary = insights?.summary;
  return (
    <div className="dash-metrics">
      <Tile
        label="Started"
        value={`${started} of ${students.length}`}
        sub="have answered a lesson check"
        tone={started === students.length && students.length > 0 ? "good" : undefined}
      />
      {summary && summary.first_try_answers > 0 ? (
        <Tile
          label="Right first time"
          value={pct(summary.first_try_accuracy)}
          sub={`${summary.first_try_correct} of ${summary.first_try_answers} first tries`}
        />
      ) : (
        <Tile label="Right first time" value="—" sub="no answers yet" />
      )}
      {profiles ? (
        <Tile
          label="Getting to know you"
          value={`${profiles.summary.taken} of ${profiles.summary.total}`}
          sub="have answered the first-login questions"
          tone={profiles.summary.taken === profiles.summary.total && profiles.summary.total > 0 ? "good" : undefined}
        />
      ) : (
        <Tile label="Getting to know you" value="—" sub="loading" />
      )}
      {checks ? (
        <Tile
          label="End check"
          value={checks.open ? `${checks.summary.students_finished} of ${checks.summary.students_started}` : "Not open"}
          sub={checks.open ? "have finished it" : `${checks.summary.students_started} took the starting check`}
        />
      ) : (
        <Tile label="End check" value="—" sub="loading" />
      )}
    </div>
  );
}

interface Item {
  id: string;
  Icon: typeof AlertTriangle;
  tone: "warn" | "info";
  title: string;
  detail: string;
  names: string[];
  tab?: ClassTab;
  tabLabel?: string;
}

// The class's loose ends, in the order a teacher should look at them.
function attentionItems(
  students: ClassStudent[],
  insights: ClassInsights | null,
  checks: ClassChecks | null,
  profiles: ClassProfiles | null,
  now: number,
): Item[] {
  const items: Item[] = [];
  const notStarted = students.filter((s) => s.attempted === 0);
  if (notStarted.length > 0) {
    items.push({
      id: "not-started",
      Icon: BookOpen,
      tone: "warn",
      title: `${notStarted.length} ${notStarted.length === 1 ? "student hasn't" : "students haven't"} started`,
      detail: "No lesson check answered yet. A login slip may be lost, or they're stuck at the first step.",
      names: notStarted.map((s) => s.name),
      tab: "students",
      tabLabel: "Students and password resets",
    });
  }
  const quiet = students.filter(
    (s) => s.attempted > 0 && s.last_active !== null && now - Date.parse(s.last_active) > INACTIVE_DAYS * DAY_MS,
  );
  if (quiet.length > 0) {
    items.push({
      id: "quiet",
      Icon: Moon,
      tone: "info",
      title: `${quiet.length} ${quiet.length === 1 ? "student has" : "students have"} gone quiet`,
      detail: `Nothing for more than ${INACTIVE_DAYS} days.`,
      names: quiet.map((s) => s.name),
      tab: "students",
      tabLabel: "Students",
    });
  }
  const sure = insights?.summary.sure_but_wrong ?? 0;
  if (sure > 0) {
    items.push({
      id: "sure-wrong",
      Icon: Target,
      tone: "warn",
      title: `${sure} first ${sure === 1 ? "try was" : "tries were"} wrong but "I'm sure"`,
      detail: "These are firmly held mix-ups, the ones worth a minute of class time.",
      names: [],
      tab: "insights",
      tabLabel: "Most common mix-ups",
    });
  }
  const skims = (profiles?.students ?? []).filter(
    (s) => s.observed.views >= 3 && s.observed.skim_share !== null && s.observed.skim_share >= 0.5,
  );
  if (skims.length > 0) {
    items.push({
      id: "skims",
      Icon: Zap,
      tone: "info",
      title: `${skims.length} ${skims.length === 1 ? "student skims" : "students skim"} their lessons`,
      detail: "Half or more of their lessons were open under 30 seconds. They may be rushing to the check.",
      names: skims.map((s) => s.name),
      tab: "insights",
      tabLabel: "Getting to know the class",
    });
  }
  const unsurveyed = (profiles?.students ?? []).filter((s) => !s.taken);
  if (unsurveyed.length > 0) {
    items.push({
      id: "unsurveyed",
      Icon: UserRound,
      tone: "info",
      title: `${unsurveyed.length} ${unsurveyed.length === 1 ? "student hasn't" : "students haven't"} answered "getting to know you"`,
      detail: "They'll be asked at their next sign-in.",
      names: unsurveyed.map((s) => s.name),
    });
  }
  if (checks?.open) {
    const waiting = checks.summary.students_started - checks.summary.students_finished;
    if (waiting > 0) {
      items.push({
        id: "end-check",
        Icon: Flag,
        tone: "info",
        title: `${waiting} ${waiting === 1 ? "student hasn't" : "students haven't"} finished the end check`,
        detail: "The before and after comparison only counts students who did both.",
        names: [],
        tab: "overview",
        tabLabel: "Starting check to end check",
      });
    }
  }
  return items;
}

export function NeedsAttention({
  students,
  insights,
  checks,
  profiles,
  onOpenTab,
}: {
  students: ClassStudent[];
  insights: ClassInsights | null;
  checks: ClassChecks | null;
  profiles: ClassProfiles | null;
  onOpenTab: (tab: ClassTab) => void;
}) {
  const [now] = useState(() => Date.now()); // fixed for this visit (render stays pure)
  const items = attentionItems(students, insights, checks, profiles, now);

  return (
    <section aria-labelledby="attention-title" className="surface panel flex flex-col gap-3">
      <div>
        <p className="eyebrow flex items-center gap-2">
          <AlertTriangle className="size-3.5" aria-hidden /> Worth a look today
        </p>
        <h2 id="attention-title" className="display text-2xl font-semibold text-foreground">
          Needs attention
        </h2>
      </div>
      {items.length === 0 ? (
        <p className="flex items-center gap-2 text-sm text-muted-foreground">
          <CheckCircle2 className="size-4 text-success" aria-hidden /> Nothing needs attention right now.
        </p>
      ) : (
        <ul className="flex flex-col divide-y divide-border">
          {items.map((it) => (
            <li key={it.id} className="flex flex-col gap-1.5 py-3 first:pt-0 last:pb-0">
              <div className="flex items-start gap-3">
                <span
                  className={cn(
                    "mt-0.5 flex size-8 shrink-0 items-center justify-center rounded-full",
                    it.tone === "warn" ? "bg-brand-accent/15 text-brand-accent" : "bg-primary/10 text-primary",
                  )}
                >
                  <it.Icon className="size-4" aria-hidden />
                </span>
                <div className="flex min-w-0 flex-1 flex-col gap-1">
                  <span className="font-semibold text-foreground">{it.title}</span>
                  <span className="text-sm text-muted-foreground">{it.detail}</span>
                  {it.names.length > 0 && (
                    <span className="flex flex-wrap gap-1.5 pt-0.5">
                      {it.names.slice(0, 6).map((n) => (
                        <span key={n} className="rounded-full bg-muted px-2.5 py-0.5 text-xs font-medium text-foreground">
                          {n}
                        </span>
                      ))}
                      {it.names.length > 6 && (
                        <span className="px-1 py-0.5 text-xs text-muted-foreground">and {it.names.length - 6} more</span>
                      )}
                    </span>
                  )}
                </div>
                {it.tab && (
                  <button
                    type="button"
                    onClick={() => onOpenTab(it.tab!)}
                    aria-label={`Open: ${it.tabLabel}`}
                    className="shrink-0 rounded-lg px-2 py-1 text-xs font-semibold text-primary hover:bg-primary/10 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring print:hidden"
                  >
                    Open
                  </button>
                )}
              </div>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
