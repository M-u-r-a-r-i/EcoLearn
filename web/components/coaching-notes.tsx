// Coaching notes: a short note per student for the teacher, each with the evidence it
// rests on and one small thing to try. Written by the AI from coarse facts only (it sees
// S1, S2…, never a name), checked by our rules, and replaced by a rules note whenever the
// AI is off, fails or breaks a rule. Every note says which of the two wrote it.
//
// Actions (2026-10-14): a note may propose one action (revise a concept from the student's own
// mix-ups, or check in). Nothing happens until the teacher approves it here; then the server carries
// it out by rules and the card shows what happened (right / not yet / active since).

"use client";

import { useState } from "react";
import { CheckCircle2, ClipboardList, Clock, MessageCircle, RefreshCw, RotateCcw, ShieldCheck, Sparkles } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { useToast } from "@/components/toast";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui-kit";
import {
  applyCoachingAction,
  friendlyMessage,
  generateCoachingNotes,
  getCoachingNotes,
  type CoachingAction,
  type CoachingNote,
  type CoachingRun,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";

// The case-file fields a note can cite, in words a teacher recognises.
const EVIDENCE: Record<string, string> = {
  lessons_opened: "Lessons opened",
  minutes_read: "Minutes read",
  checks_answered: "Checks answered",
  first_try_right: "Right first time",
  mastered_concepts: "Concepts mastered",
  days_since_active: "Days quiet",
  skim_share: "Skimmed lessons",
  thumbs: "Lesson ratings",
  focus_span: "Focus (said)",
  pace: "Pace (said)",
  physics_feel: "Feeling about physics (said)",
  maths_comfort: "Maths comfort (said)",
  top_hobby_level: "Hobby level (said)",
  first_step: "How they like to start (said)",
  mix_ups: "Mix-ups",
};

function when(iso: string): string {
  return new Date(iso).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

export function CoachingNotesPanel({ classId }: { classId: string }) {
  const saved = useFetch(`coaching:${classId}`, () => getCoachingNotes(classId));
  const [fresh, setFresh] = useState<CoachingRun | null>(null);
  const [working, setWorking] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const toast = useToast();
  const run = fresh ?? saved.data;

  async function make() {
    setWorking(true);
    setError(null);
    try {
      const made = await generateCoachingNotes(classId);
      setFresh(made);
      toast(
        made.reused
          ? "Notes were made less than a minute ago, so here they are again."
          : made.source === "rules"
            ? "Notes ready (made by rules: the AI isn't available)."
            : "Coaching notes are ready.",
        made.reused || made.source === "rules" ? "info" : "success",
      );
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setWorking(false);
    }
  }

  return (
    <section className="surface panel flex flex-col gap-5 print:hidden">
      <div className="dash-title">
        <div>
          <p className="eyebrow flex items-center gap-2">
            <ClipboardList className="size-3.5" aria-hidden /> Coaching notes
          </p>
          <h2 className="display text-2xl font-semibold text-foreground">One thing to try for each student</h2>
          <p className="dash-sub">
            A short note per student from what they did and said, with the evidence behind it.
            Suggestions to check, not a verdict on a child.
          </p>
        </div>
        {run && !working && (
          <Button variant="outline" onClick={make}>
            <RefreshCw className="size-4" /> Write new notes
          </Button>
        )}
      </div>

      {working ? (
        <div className="dplan flex items-center gap-3 text-sm text-foreground" role="status">
          <Sparkles className="size-5 shrink-0 animate-pulse text-primary" aria-hidden />
          Reading each student&apos;s activity and writing their notes… this can take up to a minute.
        </div>
      ) : saved.loading && !fresh ? (
        <div className="dplan">
          <Skeleton rows={3} />
        </div>
      ) : !run ? (
        <Button className="self-start" onClick={make}>
          <Sparkles className="size-5" /> Write coaching notes
        </Button>
      ) : (
        <RunView
          run={run}
          classId={classId}
          onChanged={async () => setFresh(await getCoachingNotes(classId))}
        />
      )}

      <FormError message={error ?? (fresh ? null : saved.error)} />

      <p className="flex items-start gap-2 text-xs text-muted-foreground">
        <ShieldCheck className="mt-0.5 size-3.5 shrink-0" aria-hidden />
        The AI never sees names: it reads labels like S3 and counts, and chosen answers from the
        survey, never anything a student typed. Notes that break our rules are replaced by a
        rules-based note.
      </p>
    </section>
  );
}

function RunView({
  run,
  classId,
  onChanged,
}: {
  run: CoachingRun;
  classId: string;
  onChanged: () => Promise<void>;
}) {
  const f = run.follow_through;
  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-wrap items-center gap-2 text-xs">
        {run.source === "rules" ? (
          <span className="rounded-full bg-brand-accent/10 px-2.5 py-1 font-semibold text-brand-accent">
            Rules-based notes
          </span>
        ) : (
          <span className="rounded-full bg-primary/10 px-2.5 py-1 font-semibold text-primary">
            {run.source === "mixed" ? "AI and rules" : "AI assistant"}
            {run.model ? ` · ${run.model}` : ""}
          </span>
        )}
        <span className="text-muted-foreground">Made {when(run.created_at)}</span>
      </div>
      {f && f.approved > 0 && (
        <p className="text-sm text-muted-foreground" role="status">
          <span className="font-semibold text-foreground">Follow-through: </span>
          {f.approved} approved
          {f.approved - f.check_ins > 0 &&
            ` · ${f.done} of ${f.approved - f.check_ins} revisions answered, ${f.right} right`}
          {f.check_ins > 0 && ` · ${f.came_back} of ${f.check_ins} checked-in students active since`}
        </p>
      )}
      {run.note && (
        <p className="rounded-lg border border-brand-accent/30 bg-brand-accent/5 px-3 py-2 text-sm text-foreground">
          {run.note}
        </p>
      )}
      <ul className="grid gap-3 md:grid-cols-2">
        {/* A teacher looks a student up by name, so the cards are alphabetical. */}
        {[...run.students]
          .sort((a, b) => a.name.localeCompare(b.name))
          .map((s) => (
            <NoteCard key={s.student_id} note={s} classId={classId} onChanged={onChanged} />
          ))}
      </ul>
    </div>
  );
}

function NoteCard({
  note,
  classId,
  onChanged,
}: {
  note: CoachingNote;
  classId: string;
  onChanged: () => Promise<void>;
}) {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const toast = useToast();
  const action = note.action;
  const taken = note.actions_taken ?? [];
  const alreadyWaiting =
    action?.type === "revise" &&
    taken.some((t) => t.kind === "revise" && t.concept_id === action.concept_id && t.status === "waiting");

  async function approve() {
    if (!action) return;
    setBusy(true);
    setError(null);
    try {
      if (action.type === "revise") {
        await applyCoachingAction(classId, note.student_id, "revise", action.concept_id);
        toast(`${action.concept} is now at the top of ${note.name}'s revision list.`, "success");
      } else {
        await applyCoachingAction(classId, note.student_id, "check_in");
        toast(`Noted: you'll check in with ${note.name}.`, "success");
      }
      await onChanged();
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setBusy(false);
    }
  }

  return (
    <li className="surface flex min-w-0 flex-col gap-2 p-4">
      <div className="flex items-center justify-between gap-2">
        <h3 className="min-w-0 truncate text-sm font-bold text-foreground">{note.name}</h3>
        <span
          className={
            note.source === "ai"
              ? "shrink-0 rounded-full bg-primary/10 px-2 py-0.5 text-[11px] font-semibold text-primary"
              : "shrink-0 rounded-full bg-muted px-2 py-0.5 text-[11px] font-semibold text-muted-foreground"
          }
        >
          {note.source === "ai" ? "AI" : "Rules"}
        </span>
      </div>
      <p className="text-sm text-foreground">{note.note}</p>
      <p className="text-sm text-muted-foreground">
        <span className="font-semibold text-foreground">Try: </span>
        {note.next_step}
      </p>
      <div className="flex flex-wrap gap-1.5" aria-label="Evidence">
        {note.evidence.map((e) => (
          <span key={e} className="rounded-md border border-border bg-card px-1.5 py-0.5 text-[11px] text-muted-foreground">
            {EVIDENCE[e] ?? e}
          </span>
        ))}
      </div>
      {taken.length > 0 && (
        <ul className="flex flex-col gap-1 border-t border-border pt-2" aria-label="What you approved">
          {taken.map((t) => (
            <ActionLine key={t.action_id} action={t} />
          ))}
        </ul>
      )}
      {action && !alreadyWaiting && (
        <Button variant="outline" size="sm" className="self-start" disabled={busy} onClick={approve}>
          {action.type === "revise" ? (
            <>
              <RotateCcw className="size-4" aria-hidden /> Add {action.concept} to their revision list
            </>
          ) : (
            <>
              <MessageCircle className="size-4" aria-hidden /> I&apos;ll check in with them
            </>
          )}
        </Button>
      )}
      <FormError message={error} />
    </li>
  );
}

// One approved action and what happened, with an icon and words (colour is never the only signal).
function ActionLine({ action }: { action: CoachingAction }) {
  const what =
    action.kind === "revise" ? `Revise ${action.concept_name ?? "a concept"}` : "Check in";
  const Icon = action.status === "right" || action.status === "active_since" ? CheckCircle2 : Clock;
  const tone =
    action.status === "right" || action.status === "active_since"
      ? "text-success"
      : action.status === "wrong"
        ? "text-destructive"
        : "text-muted-foreground";
  return (
    <li className="flex items-start gap-1.5 text-xs">
      <Icon className={`mt-0.5 size-3.5 shrink-0 ${tone}`} aria-hidden />
      <span>
        <span className="font-semibold text-foreground">{what}: </span>
        <span className="text-muted-foreground">{action.outcome}</span>
      </span>
    </li>
  );
}
