// "About me" (/about-me): what EcoLearn thinks about the student, why, and what it changes.
//
// The open learner profile (server: src/learner/profiler.py). Every adaptation is shown with its
// evidence: what the student told us in the survey ("said") and what they did ("shown": reading,
// checks, how sure they were). "That's not me" switches an insight's effect off; "Undo" brings it
// back. All of it is fixed rules, no AI, so the page can say exactly why each line is there.

"use client";

import { useState } from "react";
import { Eye, MessageCircle, RotateCcw, ShieldCheck, ThumbsDown } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { useToast } from "@/components/toast";
import { Button } from "@/components/ui/button";
import { EmptyState, PageHeading, Skeleton } from "@/components/ui-kit";
import { friendlyMessage, getLearnerProfile, setInsight, type Insight, type LearnerProfile } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

export default function AboutMePage() {
  const loaded = useFetch("learner-profile", getLearnerProfile);
  const [profile, setProfile] = useState<LearnerProfile | null>(null);
  const [busy, setBusy] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const toast = useToast();
  const data = profile ?? loaded.data;

  async function toggle(insight: Insight) {
    setBusy(insight.id);
    setError(null);
    try {
      setProfile(await setInsight(insight.id, insight.active));
      toast(insight.active ? "Got it. That's switched off for you." : "Switched back on.", "success");
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setBusy(null);
    }
  }

  const shown = data?.insights.filter((i) => i.kind === "shown") ?? [];
  const said = data?.insights.filter((i) => i.kind === "said") ?? [];

  return (
    <main className="page-shell w-full flex-1">
      <div className="mx-auto flex w-full max-w-3xl flex-col gap-8">
        <PageHeading
          eyebrow="About me"
          title="What EcoLearn thinks about you"
          description="EcoLearn changes a few small things to fit how you learn. Here is each one, why, and what it changes. If something isn't you, say so and it switches off."
        />

        {loaded.loading && !profile ? (
          <Skeleton rows={3} />
        ) : !data ? (
          <FormError message={loaded.error ?? "Couldn't load this page."} />
        ) : data.insights.length === 0 ? (
          <EmptyState
            title="Nothing to say yet"
            copy={
              data.survey_taken
                ? "Read a few lessons and answer their checks. Once there's enough to go on, it shows up here."
                : "Answer the 'getting to know you' questions and read a few lessons. Once there's enough to go on, it shows up here."
            }
            href={data.survey_taken ? "/roadmap" : "/settings/about"}
            action={data.survey_taken ? "Back to my path" : "Answer the questions"}
          />
        ) : (
          <>
            {shown.length > 0 && (
              <Group
                icon={<Eye className="size-4" aria-hidden />}
                title="What you did"
                blurb="From your reading and your checks."
                items={shown}
                busy={busy}
                onToggle={toggle}
              />
            )}
            {said.length > 0 && (
              <Group
                icon={<MessageCircle className="size-4" aria-hidden />}
                title="What you told us"
                blurb="From your 'getting to know you' answers. You can change those in Settings."
                items={said}
                busy={busy}
                onToggle={toggle}
              />
            )}
          </>
        )}

        <FormError message={error} />

        <p className="flex items-start gap-2 text-xs text-muted-foreground">
          <ShieldCheck className="mt-0.5 size-3.5 shrink-0" aria-hidden />
          Worked out by fixed rules from your answers and your reading, not by AI. Nothing here is a
          mark, and nothing is locked: you can always switch a lesson to one page or step by step.
        </p>
      </div>
    </main>
  );
}

function Group({
  icon,
  title,
  blurb,
  items,
  busy,
  onToggle,
}: {
  icon: React.ReactNode;
  title: string;
  blurb: string;
  items: Insight[];
  busy: string | null;
  onToggle: (insight: Insight) => void;
}) {
  return (
    <section className="flex flex-col gap-3" aria-label={title}>
      <div>
        <h2 className="display flex items-center gap-2 text-xl font-semibold text-foreground">
          {icon} {title}
        </h2>
        <p className="text-sm text-muted-foreground">{blurb}</p>
      </div>
      <ul className="flex flex-col gap-3">
        {items.map((insight) => (
          <InsightCard key={insight.id} insight={insight} busy={busy === insight.id} onToggle={onToggle} />
        ))}
      </ul>
    </section>
  );
}

function InsightCard({
  insight,
  busy,
  onToggle,
}: {
  insight: Insight;
  busy: boolean;
  onToggle: (insight: Insight) => void;
}) {
  return (
    <li className={cn("surface flex flex-col gap-3 p-5", !insight.active && "opacity-70")}>
      <div className="flex flex-wrap items-start justify-between gap-2">
        <h3 className="display text-lg font-semibold text-foreground">{insight.title}</h3>
        {!insight.active && <span className="tag">Switched off</span>}
      </div>
      <p className="text-sm text-foreground">{insight.detail}</p>
      {insight.evidence.length > 0 && (
        <ul className="flex flex-wrap gap-1.5" aria-label="Why we think so">
          {insight.evidence.map((e) => (
            <li key={e} className="rounded-md border border-border bg-card px-2 py-0.5 text-xs text-muted-foreground">
              {e}
            </li>
          ))}
        </ul>
      )}
      <p className="text-sm text-muted-foreground">
        <span className="font-semibold text-foreground">{insight.active ? "What changes: " : "Would change: "}</span>
        {insight.effect}
      </p>
      <div>
        <Button variant="outline" size="sm" disabled={busy} onClick={() => onToggle(insight)}>
          {insight.active ? (
            <>
              <ThumbsDown className="size-4" aria-hidden /> That&apos;s not me
            </>
          ) : (
            <>
              <RotateCcw className="size-4" aria-hidden /> Undo: switch it back on
            </>
          )}
        </Button>
      </div>
    </li>
  );
}
