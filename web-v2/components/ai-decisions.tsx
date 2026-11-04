// "How the AI decided" — the teacher's window into the agents (2026-10-03).
//
// WHY: a teacher (and a judge) should be able to see that AI output never goes
// straight to a child. Every personal story passes fixed rule checks, then a
// second model acting as critic; a rejected draft is rewritten once, and if it
// still fails, the student simply gets the reviewed lesson story. This panel
// shows each of those decisions with its reasons, plus how often the teaching
// assistant fell back to its rules plan and how many model calls failed.
// All numbers come from the server (platform_api.get_class_ai_decisions).

"use client";

import { ArrowRight, Bot, CheckCircle2, ShieldCheck, XCircle } from "lucide-react";

import type { AiDecisions, DecisionStep, DecisionTrailStep } from "@/lib/api";
import { getClassAiDecisions } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

const STEP_LABEL: Record<DecisionStep, string> = {
  format: "Format check",
  fit: "Writer",
  rules: "Rule checks",
  critic: "AI critic",
  model: "Model",
};

const STEP_PASS: Record<DecisionStep, string> = {
  format: "readable",
  fit: "found a fit",
  rules: "passed (length, no numbers, no links)",
  critic: "approved the draft",
  model: "answered",
};

export function AiDecisionsPanel({ classId }: { classId: string }) {
  const { data, loading, error } = useFetch(`ai-decisions:${classId}`, () => getClassAiDecisions(classId));

  if (loading) return <div className="h-40 animate-pulse rounded-xl bg-muted" aria-label="Loading AI decisions" />;
  if (!data) {
    return <p className="text-sm text-destructive">{error ?? "Couldn't load how the AI decided."}</p>;
  }

  return (
    <section className="flex flex-col gap-5 rounded-xl border border-border bg-card p-6 shadow-card print:hidden">
      <div className="flex flex-col gap-1">
        <h2 className="flex items-center gap-2 text-lg font-bold text-foreground">
          <ShieldCheck className="size-5 text-primary" aria-hidden /> How the AI decided
        </h2>
        <p className="max-w-3xl text-sm text-muted-foreground">
          AI never writes straight to a student. Each personal story passes fixed rule checks, then a
          second AI acting as a critic. A rejected draft is rewritten once; if it still fails, the
          student gets the reviewed lesson story instead. Here is every one of those decisions.
        </p>
      </div>

      <Pipeline d={data} />
      <Tiles d={data} />
      <Log d={data} />
    </section>
  );
}

// The guardrail pipeline as a flow, with this class's counts on each stage.
function Pipeline({ d }: { d: AiDecisions }) {
  const s = d.stories;
  const stages = [
    { label: "Writer drafts", value: s.attempted, note: `${s.declined} declined: no honest fit` },
    { label: "Rule checks", value: s.rules_rejections, note: "drafts sent back (numbers, links, length)" },
    { label: "AI critic", value: s.critic_rejections, note: `of ${s.critic_checks} drafts rejected` },
    { label: "Shown", value: s.shown, note: `${s.rewritten} after a rewrite` },
  ];
  return (
    <ol className="grid gap-2 sm:grid-cols-4" aria-label="The story guardrails">
      {stages.map((st, i) => (
        <li key={st.label} className="relative flex flex-col gap-0.5 rounded-xl border border-border bg-background p-3">
          <span className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
            {i + 1}. {st.label}
          </span>
          <span className="text-2xl font-bold text-foreground">{st.value}</span>
          <span className="text-xs text-muted-foreground">{st.note}</span>
          {i < stages.length - 1 && (
            <ArrowRight
              className="absolute -right-2.5 top-1/2 z-10 hidden size-4 -translate-y-1/2 text-muted-foreground sm:block"
              aria-hidden
            />
          )}
        </li>
      ))}
    </ol>
  );
}

function Tiles({ d }: { d: AiDecisions }) {
  const s = d.stories;
  const items = [
    {
      label: "Safe fallbacks",
      value: s.blocked + s.errors + s.declined,
      note: `reviewed story shown instead: ${s.blocked} blocked, ${s.declined} no fit, ${s.errors} model down`,
    },
    {
      label: "Human review",
      value: s.reported + s.hidden_by_teacher,
      note: `${s.reported} reported by students, ${s.hidden_by_teacher} hidden by you`,
    },
    {
      label: "Teaching assistant",
      value: d.plans.total,
      note: d.plans.total
        ? `plans: ${d.plans.agent} by the AI, ${d.plans.rules} by the rules fallback`
        : "no plans yet",
    },
    {
      label: "Model calls",
      value: d.calls.total,
      note: d.calls.total ? `${d.calls.failed} failed, then a fallback took over` : "none logged yet",
    },
  ];
  return (
    <div className="flex flex-col gap-2">
      <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
        {items.map((t) => (
          <div key={t.label} className="rounded-xl border border-border bg-background p-3">
            <div className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">{t.label}</div>
            <div className="text-2xl font-bold text-foreground">{t.value}</div>
            <div className="text-xs text-muted-foreground">{t.note}</div>
          </div>
        ))}
      </div>
      {d.plans.latest_note && (
        <p className="text-xs text-muted-foreground">
          Latest teaching-assistant fallback: {d.plans.latest_note}
        </p>
      )}
    </div>
  );
}

function Log({ d }: { d: AiDecisions }) {
  if (d.log.length === 0) {
    return (
      <p className="rounded-lg border border-dashed border-border p-4 text-sm text-muted-foreground">
        No personal stories yet. They&apos;re written in the background once an AI model is set up, and
        every decision will be listed here.
      </p>
    );
  }
  return (
    <div className="flex flex-col gap-2">
      <h3 className="text-sm font-semibold text-foreground">Decision log, newest first</h3>
      <ul className="flex flex-col gap-2">
        {d.log.map((e) => (
          <li key={`${e.student_id}|${e.concept_id}`}>
            <details className="group rounded-xl border border-border bg-background">
              <summary className="flex cursor-pointer flex-col gap-1 p-3 sm:flex-row sm:items-center sm:justify-between">
                <span className="text-sm">
                  <span className="font-semibold text-foreground">{e.name}</span>
                  <span className="text-muted-foreground">
                    {" "}
                    · {e.concept_name} · {e.emoji} {e.hobby}
                  </span>
                </span>
                <span
                  className={cn(
                    "text-xs font-medium",
                    e.status === "ready" && !e.hidden ? "text-success" : "text-muted-foreground",
                  )}
                >
                  {e.outcome}
                </span>
              </summary>
              <div className="border-t border-border p-3">
                {e.trail.length === 0 ? (
                  <p className="text-xs text-muted-foreground">
                    Written before step-by-step records existed ({e.attempts} draft
                    {e.attempts === 1 ? "" : "s"}).
                  </p>
                ) : (
                  <ol className="flex flex-col gap-2">
                    {e.trail.map((t, i) => (
                      <Step key={i} t={t} />
                    ))}
                  </ol>
                )}
                {e.model && (
                  <p className="mt-2 flex items-center gap-1 text-xs text-muted-foreground">
                    <Bot className="size-3" aria-hidden /> Writer model: {e.model}
                  </p>
                )}
              </div>
            </details>
          </li>
        ))}
      </ul>
    </div>
  );
}

function Step({ t }: { t: DecisionTrailStep }) {
  return (
    <li className="flex items-start gap-2 text-sm">
      {t.passed ? (
        <CheckCircle2 className="mt-0.5 size-4 shrink-0 text-success" aria-label="passed" />
      ) : (
        <XCircle className="mt-0.5 size-4 shrink-0 text-destructive" aria-label="rejected" />
      )}
      <div className="flex flex-col">
        <span className="text-foreground">
          <span className="font-medium">Draft {t.attempt} · {STEP_LABEL[t.step]}</span>{" "}
          <span className="text-muted-foreground">
            {t.passed ? STEP_PASS[t.step] : t.step === "fit" ? "declined" : "rejected it"}
            {t.model && t.step === "critic" ? ` (${t.model})` : ""}
          </span>
        </span>
        {t.problems.map((p, i) => (
          <span key={i} className="text-xs text-muted-foreground">
            “{p}”
          </span>
        ))}
      </div>
    </li>
  );
}
