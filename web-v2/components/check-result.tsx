// A student's before → after: their starting check against their end check,
// concept by concept. Encouraging but honest: fixed mix-ups lead, and anything
// that slipped is shown as "worth another look", not hidden.

"use client";

import Link from "next/link";
import { ArrowRight, CheckCircle2, HelpCircle, RotateCcw, XCircle } from "lucide-react";

import type { CheckComparison, CheckOutcome } from "@/lib/api";
import { cn } from "@/lib/utils";

const OUTCOME: Record<CheckOutcome, { label: string; Icon: typeof CheckCircle2; tone: string }> = {
  right: { label: "Right", Icon: CheckCircle2, tone: "text-success" },
  mix_up: { label: "Mix-up", Icon: XCircle, tone: "text-destructive" },
  unsure: { label: "Not sure", Icon: HelpCircle, tone: "text-muted-foreground" },
};

function Outcome({ value }: { value: CheckOutcome }) {
  const { label, Icon, tone } = OUTCOME[value];
  return (
    <span className={cn("inline-flex items-center gap-1 text-sm font-medium", tone)}>
      <Icon className="size-4" aria-hidden /> {label}
    </span>
  );
}

function headline(c: CheckComparison): string {
  const fixed = `You fixed ${c.fixed} ${c.fixed === 1 ? "mix-up" : "mix-ups"}`;
  const learned = `${c.learned} ${c.learned === 1 ? "idea" : "ideas"} you weren't sure of`;
  if (c.fixed > 0 && c.learned > 0) return `${fixed} and learned ${learned}.`;
  if (c.fixed > 0) return `${fixed}.`;
  if (c.learned > 0) return `You've learned ${learned}.`;
  if (c.after.right >= c.before.right) return "You've held on to what you knew.";
  return "A few ideas are worth another look.";
}

export function CheckResultSummary({ comparison: c }: { comparison: CheckComparison }) {
  const tiles = [
    { label: "Right answers", before: c.before.right, after: c.after.right, good: "up" },
    { label: "Mix-ups", before: c.before.mix_up, after: c.after.mix_up, good: "down" },
    { label: "Not sure", before: c.before.unsure, after: c.after.unsure, good: "down" },
  ] as const;
  const review = c.concepts.filter((x) => x.after !== "right");

  return (
    <div className="flex flex-col gap-6">
      <p className="text-xl font-semibold text-foreground">{headline(c)}</p>

      <div className="grid gap-3 sm:grid-cols-3">
        {tiles.map((t) => {
          const better = t.good === "up" ? t.after > t.before : t.after < t.before;
          return (
            <div key={t.label} className="rounded-xl border border-border bg-card p-4 shadow-soft">
              <div className="text-sm text-muted-foreground">{t.label}</div>
              <div className="mt-1 flex items-baseline gap-2 text-2xl font-bold text-foreground">
                <span className="text-muted-foreground">{t.before}</span>
                <ArrowRight className="size-4 self-center text-muted-foreground" aria-label="to" />
                <span className={cn(better && "text-success")}>{t.after}</span>
                <span className="text-sm font-normal text-muted-foreground">of {c.paired}</span>
              </div>
            </div>
          );
        })}
      </div>

      <section className="flex flex-col gap-2">
        <h2 className="text-lg font-bold text-foreground">Idea by idea</h2>
        <ul className="divide-y divide-border rounded-xl border border-border bg-card">
          {c.concepts.map((x) => (
            <li key={x.concept_id} className="flex flex-col gap-1 p-4 sm:flex-row sm:items-center sm:justify-between">
              <span className="font-medium text-foreground">{x.concept_name}</span>
              <span className="flex items-center gap-2">
                <Outcome value={x.before} />
                <ArrowRight className="size-4 text-muted-foreground" aria-label="then" />
                <Outcome value={x.after} />
              </span>
            </li>
          ))}
        </ul>
      </section>

      {review.length > 0 && (
        <section className="flex flex-col gap-2 rounded-xl border border-primary/20 bg-primary/5 p-4">
          <h2 className="flex items-center gap-2 text-sm font-semibold text-foreground">
            <RotateCcw className="size-4 text-primary" aria-hidden /> Worth another look
          </h2>
          <p className="text-sm text-muted-foreground">
            {review.map((x) => x.concept_name).join(", ")}. Every lesson stays open — go back whenever
            you like.
          </p>
          <Link href="/roadmap" className="text-sm font-semibold text-primary hover:underline">
            Open your roadmap →
          </Link>
        </section>
      )}
    </div>
  );
}
