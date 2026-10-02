// The opening of a lesson: the story written for this student's hobby when
// there is one, with the lesson's own (reviewed) story one click away.
//
//   ready   → "Your story" card (story, the analogy, where it stops working),
//             then the original story in a <details> box
//   pending → the original story as usual, plus a note that a version for
//             their hobby is being written; we poll and swap it in
//   none    → the original story, exactly as before
//
// The personal story is clearly labelled as AI-written and checked, so a
// student (and a teacher) always knows which text a person reviewed.

"use client";

import { useEffect, useState } from "react";
import { BookOpen, ChevronRight, Flag, ShieldCheck, Sparkles } from "lucide-react";

import { Markdown } from "@/components/markdown";
import { Button } from "@/components/ui/button";
import {
  friendlyMessage,
  getPersonalStory,
  reportPersonalStory,
  type PersonalStory,
  type StoryReportReason,
} from "@/lib/api";

const REPORT_REASONS: { value: StoryReportReason; label: string }[] = [
  { value: "wrong_physics", label: "The physics seems wrong" },
  { value: "confusing", label: "It's confusing" },
  { value: "not_appropriate", label: "It's not appropriate" },
  { value: "other", label: "Something else" },
];

const POLL_MS = 3000;
const POLL_LIMIT = 20; // about a minute; after that, the original story stays

export function LessonStory({
  conceptId,
  initial,
  original,
  interest,
}: {
  conceptId: string;
  initial: PersonalStory | undefined;
  original: string | undefined; // the lesson's own "The story" markdown
  interest: string | undefined;
}) {
  const [story, setStory] = useState<PersonalStory>(initial ?? { status: "none" });
  const [reported, setReported] = useState(false);
  const pending = story.status === "pending";

  useEffect(() => {
    if (!pending) return;
    let polls = 0;
    let cancelled = false;
    const timer = setInterval(async () => {
      polls += 1;
      try {
        const next = await getPersonalStory(conceptId);
        if (!cancelled && next.status !== "pending") setStory(next);
      } catch {
        // a failed poll just means we try again (or give up below)
      }
      if (polls >= POLL_LIMIT && !cancelled) setStory({ status: "none" });
    }, POLL_MS);
    return () => {
      cancelled = true;
      clearInterval(timer);
    };
  }, [pending, conceptId]);

  if (story.status !== "ready") {
    return (
      <div className="flex flex-col gap-4">
        {reported && (
          <p role="status" className="rounded-xl border border-success/30 bg-success/5 px-4 py-3 text-sm text-foreground">
            Thanks for telling us. That story is hidden now, and your teacher will see your report.
            Here&apos;s the lesson&apos;s own story instead.
          </p>
        )}
        {story.status === "pending" && (
          <p role="status" className="flex items-center gap-2 rounded-xl bg-primary/5 px-4 py-3 text-sm text-foreground">
            <Sparkles className="size-4 shrink-0 animate-pulse text-primary" aria-hidden />
            Writing a {story.hobby.toLowerCase()} version of this story for you…
          </p>
        )}
        {original && (
          <article>
            <h2 className="mb-3 text-2xl font-bold tracking-tight text-foreground">The story</h2>
            <Markdown>{original}</Markdown>
          </article>
        )}
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-4">
      <article className="flex flex-col gap-4 rounded-2xl border border-primary/20 bg-gradient-to-b from-primary/5 to-card p-6 shadow-card">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <h2 className="text-2xl font-bold tracking-tight text-foreground">Your story</h2>
          <span className="inline-flex items-center gap-1.5 rounded-full bg-card px-3 py-1 text-sm font-semibold text-foreground shadow-soft">
            <span aria-hidden>{story.emoji}</span> {story.hobby}
          </span>
        </div>
        <Markdown>{story.story}</Markdown>
        <div className="rounded-xl border border-border bg-card p-4">
          <p className="mb-1 text-xs font-semibold uppercase tracking-wide text-primary">
            In {story.hobby.toLowerCase()} terms
          </p>
          <Markdown className="prose-sm">{story.analogy}</Markdown>
          <p className="mt-2 text-sm text-muted-foreground">
            <span className="font-semibold">Where the comparison stops:</span> {story.limit}
          </p>
        </div>
        <p className="flex items-start gap-1.5 text-xs text-muted-foreground">
          <ShieldCheck className="mt-0.5 size-3.5 shrink-0" aria-hidden />
          Written for you by EcoLearn&apos;s AI from this lesson, and checked by a second AI. The
          lesson below was written and reviewed by people.
        </p>
        <ReportStory
          conceptId={conceptId}
          onReported={() => {
            setReported(true);
            setStory({ status: "none" });
          }}
        />
      </article>

      {original && (
        <details className="group rounded-xl border border-border bg-card px-5 py-4 shadow-soft">
          <summary className="flex cursor-pointer list-none items-center gap-2 font-semibold text-foreground marker:content-none">
            <ChevronRight className="size-5 shrink-0 text-muted-foreground transition-transform group-open:rotate-90" />
            <BookOpen className="size-5 text-brand-accent" aria-hidden />
            <span>
              {interest
                ? `Read the original ${interest.charAt(0).toUpperCase()}${interest.slice(1)} story`
                : "Read the original story"}
            </span>
          </summary>
          <div className="mt-4 border-t border-border pt-4">
            <Markdown>{original}</Markdown>
          </div>
        </details>
      )}
    </div>
  );
}

// "Something wrong with this story?" — fixed reasons, one tap. The story is
// hidden for the student straight away and goes to their teacher to review.
function ReportStory({ conceptId, onReported }: { conceptId: string; onReported: () => void }) {
  const [open, setOpen] = useState(false);
  const [sending, setSending] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function send(reason: StoryReportReason) {
    setSending(true);
    setError(null);
    try {
      await reportPersonalStory(conceptId, reason);
      onReported();
    } catch (err) {
      setError(friendlyMessage(err));
      setSending(false);
    }
  }

  if (!open) {
    return (
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="inline-flex items-center gap-1.5 self-start text-xs font-medium text-muted-foreground underline-offset-2 hover:text-foreground hover:underline"
      >
        <Flag className="size-3.5" aria-hidden /> Something wrong with this story?
      </button>
    );
  }

  return (
    <div role="group" aria-label="Report this story" className="flex flex-col gap-2 rounded-xl border border-border bg-card p-3">
      <p className="text-sm font-medium text-foreground">What&apos;s wrong with it?</p>
      <div className="flex flex-wrap gap-2">
        {REPORT_REASONS.map((r) => (
          <Button key={r.value} size="sm" variant="outline" disabled={sending} onClick={() => send(r.value)}>
            {r.label}
          </Button>
        ))}
        <Button size="sm" variant="ghost" disabled={sending} onClick={() => setOpen(false)}>
          Cancel
        </Button>
      </div>
      {error && <p className="text-sm text-destructive">{error}</p>}
    </div>
  );
}
