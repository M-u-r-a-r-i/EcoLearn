// The teacher's view of the AI-written personal stories in a class.
//
// A teacher reads exactly what each student saw, sees which stories students
// reported (and why), and can hide a story — the student then gets the
// lesson's own reviewed story — or show it again. Reported stories come first.
//
// This is the human check on the AI layer: the critic agent checks every story
// before a student sees it, and this page lets the teacher check the critic.

"use client";

import { useState } from "react";
import { EyeOff, Eye, Flag, Sparkles } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { Markdown } from "@/components/markdown";
import { Button } from "@/components/ui/button";
import { friendlyMessage, getClassStories, setStoryHidden, type ClassStory } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

const SHOWN = 6;

function when(iso: string): string {
  return new Date(iso).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

export function ClassStoriesPanel({ classId }: { classId: string }) {
  const [version, setVersion] = useState(0);
  const { data, error, loading } = useFetch(`stories:${classId}:${version}`, () => getClassStories(classId));
  const [showAll, setShowAll] = useState(false);

  if (loading && !data) return <div className="h-24 animate-pulse rounded-xl bg-muted" aria-label="Loading stories" />;
  if (!data) return <FormError message={error ?? "Couldn't load the personal stories."} />;

  const { summary, stories } = data;
  const shown = showAll ? stories : stories.slice(0, SHOWN);

  return (
    <section className="flex flex-col gap-4 rounded-xl border border-border bg-card p-6 shadow-card print:hidden">
      <div className="flex flex-col gap-1">
        <h2 className="flex items-center gap-2 text-lg font-bold text-foreground">
          <Sparkles className="size-5 text-primary" aria-hidden /> Personal stories
        </h2>
        <p className="text-sm text-muted-foreground">
          Short openings EcoLearn&apos;s AI wrote around each student&apos;s hobbies, checked by a second
          AI before any student saw them. Read what they read; hide anything you don&apos;t want
          shown — they&apos;ll get the lesson&apos;s own story instead.
        </p>
      </div>

      {summary.written === 0 ? (
        <p className="text-sm text-muted-foreground">
          No personal stories yet. They appear once students with hobbies open lessons (and the AI is
          set up on the server).
          {summary.not_written > 0 &&
            ` ${summary.not_written} attempt${summary.not_written === 1 ? "" : "s"} didn't pass the checks, so those students saw the lesson's own story.`}
        </p>
      ) : (
        <>
          <p className="text-sm text-foreground">
            <strong>{summary.written}</strong> written · {summary.showing} showing ·{" "}
            <span className={summary.reported ? "font-semibold text-destructive" : undefined}>
              {summary.reported} reported by students
            </span>{" "}
            · {summary.hidden_by_teacher} hidden by you
            {summary.not_written > 0 && ` · ${summary.not_written} didn't pass the checks`}
          </p>
          <ul className="flex flex-col gap-3">
            {shown.map((s) => (
              <StoryRow key={`${s.student_id}|${s.concept_id}`} story={s} onChanged={() => setVersion((v) => v + 1)} />
            ))}
          </ul>
          {stories.length > SHOWN && (
            <Button variant="outline" className="self-start" onClick={() => setShowAll((v) => !v)}>
              {showAll ? "Show fewer" : `Show all ${stories.length}`}
            </Button>
          )}
        </>
      )}
    </section>
  );
}

function StoryRow({ story: s, onChanged }: { story: ClassStory; onChanged: () => void }) {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function toggle() {
    setBusy(true);
    setError(null);
    try {
      await setStoryHidden(s.student_id, s.concept_id, !s.hidden);
      onChanged();
    } catch (err) {
      setError(friendlyMessage(err));
      setBusy(false);
    }
  }

  const status = s.hidden
    ? s.hidden_by === "student"
      ? { label: "Reported · hidden", tone: "bg-destructive/10 text-destructive" }
      : { label: "Hidden by you", tone: "bg-muted text-muted-foreground" }
    : s.reported_at
      ? { label: "Reported · shown again", tone: "bg-brand-accent/10 text-brand-accent" }
      : { label: "Showing", tone: "bg-success/10 text-success" };

  return (
    <li className={cn("flex flex-col gap-3 rounded-xl border p-4", s.reported_at ? "border-destructive/30" : "border-border")}>
      <div className="flex flex-wrap items-start justify-between gap-2">
        <div className="flex flex-col gap-0.5">
          <span className="font-semibold text-foreground">
            {s.name} <span className="font-normal text-muted-foreground">· {s.concept_name}</span>
          </span>
          <span className="text-xs text-muted-foreground">
            <span aria-hidden>{s.emoji}</span> {s.hobby}
            {s.chapter_name && ` · ${s.chapter_name}`} · {when(s.created_at)}
          </span>
        </div>
        <span className={cn("rounded-full px-2.5 py-1 text-xs font-semibold", status.tone)}>{status.label}</span>
      </div>

      {s.report_label && (
        <p className="flex items-center gap-1.5 text-sm text-destructive">
          <Flag className="size-4 shrink-0" aria-hidden />
          Student said: &ldquo;{s.report_label}&rdquo;
          {s.reported_at && <span className="text-muted-foreground">({when(s.reported_at)})</span>}
        </p>
      )}

      <details className="text-sm" open={Boolean(s.reported_at && s.hidden)}>
        <summary className="cursor-pointer font-semibold text-primary">Read the story</summary>
        <div className="mt-3 flex flex-col gap-3 border-l-2 border-border pl-4">
          <Markdown className="prose-sm">{s.story}</Markdown>
          <div>
            <span className="text-xs font-semibold uppercase tracking-wide text-primary">The analogy</span>
            <Markdown className="prose-sm">{s.analogy}</Markdown>
          </div>
          <p className="text-muted-foreground">
            <span className="font-semibold">Where it stops:</span> {s.limit}
          </p>
          {s.model && <p className="text-xs text-muted-foreground">Written by {s.model}</p>}
        </div>
      </details>

      <div className="flex items-center gap-3">
        <Button size="sm" variant={s.hidden ? "outline" : "destructive"} disabled={busy} onClick={toggle}>
          {s.hidden ? (
            <>
              <Eye className="size-4" /> Show it to {s.name.split(" ")[0]} again
            </>
          ) : (
            <>
              <EyeOff className="size-4" /> Hide this story
            </>
          )}
        </Button>
        {error && <span className="text-sm text-destructive">{error}</span>}
      </div>
    </li>
  );
}
