// The teaching assistant card on a class page: one button that asks the
// teacher agent to read this class's data and plan the next lesson.
//
// Two things a teacher should be able to see, so they're on the card:
//   * how the plan was made — the agent's steps ("Read the most common
//     misconceptions", ...), or a clear note that fixed rules wrote it when the
//     AI isn't available;
//   * that student names never go to the AI — it sees S1, S2…, and names are
//     filled in here, on our server.

"use client";

import { useState } from "react";
import { Bot, CheckCircle2, ListChecks, RefreshCw, ShieldCheck, Sparkles, XCircle } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { useToast } from "@/components/toast";
import { Markdown } from "@/components/markdown";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";
import { friendlyMessage, generateClassPlan, getClassPlan, type ClassPlan } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";

const WORKING_STEPS = [
  "Looking at the class overview…",
  "Reading the most common misconceptions…",
  "Checking concepts and prerequisites…",
  "Reading the lessons' key takeaways…",
  "Reviewing each student's activity…",
  "Writing the plan…",
];

function when(iso: string): string {
  return new Date(iso).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

export function TeachingAssistant({ classId }: { classId: string }) {
  const saved = useFetch(`plan:${classId}`, () => getClassPlan(classId));
  const [fresh, setFresh] = useState<ClassPlan | null>(null);
  const [working, setWorking] = useState(false);
  const [stepIndex, setStepIndex] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const toast = useToast();

  const plan = fresh ?? saved.data;

  async function makePlan() {
    setWorking(true);
    setError(null);
    setStepIndex(0);
    // The run is one request, so these steps are a guide to what it's doing,
    // not a live feed; the real steps are listed under the finished plan.
    const timer = setInterval(
      () => setStepIndex((i) => Math.min(i + 1, WORKING_STEPS.length - 1)),
      2500,
    );
    try {
      const made = await generateClassPlan(classId);
      setFresh(made);
      toast(
        made.reused
          ? "A plan was made less than a minute ago, so here it is again."
          : made.source === "agent"
            ? "Your plan is ready."
            : "Plan ready (made by rules: the AI isn't available).",
        made.reused || made.source !== "agent" ? "info" : "success",
      );
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      clearInterval(timer);
      setWorking(false);
    }
  }

  return (
    <section className="flex flex-col gap-4 rounded-xl border border-primary/20 bg-card p-6 shadow-card print:hidden">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="flex flex-col gap-1">
          <h2 className="flex items-center gap-2 text-lg font-bold text-foreground">
            <Bot className="size-5 text-primary" aria-hidden />
            Teaching assistant
          </h2>
          <p className="max-w-xl text-sm text-muted-foreground">
            Reads what your class did — the misconceptions they chose, who&apos;s stuck, who
            hasn&apos;t started — and plans your next lesson.
          </p>
        </div>
        {plan && !working && (
          <Button variant="outline" onClick={makePlan}>
            <RefreshCw className="size-4" /> Make a new plan
          </Button>
        )}
      </div>

      {working ? (
        <div className="flex items-center gap-3 rounded-xl bg-primary/5 p-4 text-sm text-foreground" role="status">
          <Sparkles className="size-5 shrink-0 animate-pulse text-primary" aria-hidden />
          {WORKING_STEPS[stepIndex]}
        </div>
      ) : saved.loading && !fresh ? (
        <div className="h-24 animate-pulse rounded-xl bg-muted" aria-label="Loading the latest plan" />
      ) : !plan ? (
        <PrimaryButton className="self-start" onClick={makePlan}>
          <Sparkles className="size-5" /> Plan my next lesson
        </PrimaryButton>
      ) : (
        <PlanView plan={plan} />
      )}

      <FormError message={error ?? (fresh ? null : saved.error)} />

      <p className="flex items-start gap-2 text-xs text-muted-foreground">
        <ShieldCheck className="mt-0.5 size-3.5 shrink-0" aria-hidden />
        Student names never go to the AI: it sees labels like S3, and names are filled in here.
        Check the plan before you use it — it&apos;s a suggestion, not a decision.
      </p>
    </section>
  );
}

function PlanView({ plan }: { plan: ClassPlan }) {
  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-wrap items-center gap-2 text-xs">
        {plan.source === "agent" ? (
          <span className="rounded-full bg-primary/10 px-2.5 py-1 font-semibold text-primary">
            AI assistant{plan.model ? ` · ${plan.model}` : ""}
          </span>
        ) : (
          <span className="rounded-full bg-brand-accent/10 px-2.5 py-1 font-semibold text-brand-accent">
            Rules-based plan
          </span>
        )}
        <span className="text-muted-foreground">Made {when(plan.created_at)}</span>
        {plan.reused && <span className="text-muted-foreground">· made a moment ago, so reused</span>}
      </div>

      {plan.note && (
        <p className="rounded-lg border border-brand-accent/30 bg-brand-accent/5 px-3 py-2 text-sm text-foreground">
          {plan.note}
        </p>
      )}

      <div className="rounded-xl border border-border p-5">
        <Markdown>{plan.markdown}</Markdown>
      </div>

      {plan.steps.length > 0 && (
        <details className="text-sm">
          <summary className="flex cursor-pointer items-center gap-2 font-semibold text-primary">
            <ListChecks className="size-4" aria-hidden />
            {plan.source === "agent"
              ? `How the assistant worked (${plan.steps.length} steps)`
              : "What the rules looked at"}
          </summary>
          <ol className="mt-3 flex flex-col gap-1.5 border-l-2 border-border pl-4">
            {plan.steps.map((step, i) => (
              <li key={i} className="flex items-start gap-2">
                {step.ok ? (
                  <CheckCircle2 className="mt-0.5 size-4 shrink-0 text-success" aria-label="done" />
                ) : (
                  <XCircle className="mt-0.5 size-4 shrink-0 text-muted-foreground" aria-label="failed" />
                )}
                <span className={step.ok ? "text-foreground" : "text-muted-foreground"}>{step.summary}</span>
              </li>
            ))}
          </ol>
        </details>
      )}
    </div>
  );
}
