// Revision (/review): concepts the student has answered right once, asked again
// with a FRESH question (another interest's lesson check they've never seen).
//
// WHY: one right answer used to mean "mastered", and after a wrong pick the
// app shows the right answer, so a retry proved little. Now mastery needs two
// different questions right. Spacing them about a day apart is what makes it
// stick, so items are "due" after a wait — but nothing is locked: a concept
// that isn't due yet can still be tried.

"use client";

import { Suspense, useState } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { ArrowLeft, ArrowRight, CheckCircle2, Clock, RotateCcw, XCircle } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { CheckQuestion } from "@/components/check-question";
import { Markdown } from "@/components/markdown";
import { Button } from "@/components/ui/button";
import {
  friendlyMessage,
  getRevision,
  getRevisionQuestion,
  submitRevision,
  type Confidence,
  type RevisionItem,
  type RevisionResult,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

export default function ReviewPage() {
  return (
    <Suspense>
      <Review />
    </Suspense>
  );
}

function Review() {
  const fromLink = useSearchParams().get("concept");
  const [version, setVersion] = useState(0);
  const [open, setOpen] = useState<string | null>(fromLink);
  const queue = useFetch(`revision:${version}`, getRevision);

  if (open) {
    return (
      <Shell>
        <QuestionView
          conceptId={open}
          onBack={() => {
            setOpen(null);
            setVersion((v) => v + 1); // the queue changed
          }}
        />
      </Shell>
    );
  }

  return (
    <Shell>
      <div className="flex flex-col gap-2">
        <span className="eyebrow">Revision</span>
        <h1 className="display text-4xl font-semibold text-foreground">Make it stick</h1>
        <p className="text-muted-foreground">
          An idea counts as <span className="font-semibold text-foreground">mastered</span>{" "}once
          you&apos;ve answered two different questions on it right. These ones you&apos;ve got right
          once; here&apos;s a new question on each.
        </p>
      </div>

      {queue.loading ? (
        <div className="h-40 animate-pulse rounded-xl bg-muted" />
      ) : !queue.data ? (
        <FormError message={queue.error ?? "Couldn't load your revision list."} />
      ) : queue.data.due.length + queue.data.later.length === 0 ? (
        <section className="surface !border-dashed p-6 text-sm text-muted-foreground">
          Nothing to revise right now. When you get a lesson check right, the idea comes back here a
          day later with a new question.
          <Link href="/roadmap" className="mt-3 block font-semibold text-primary hover:underline">
            Go to your roadmap →
          </Link>
        </section>
      ) : (
        <>
          <ItemList title="Ready now" items={queue.data.due} onOpen={setOpen} />
          <ItemList
            title="Coming up"
            note="Best tried after a short break — but you can try them now."
            items={queue.data.later}
            onOpen={setOpen}
          />
        </>
      )}
    </Shell>
  );
}

function Shell({ children }: { children: React.ReactNode }) {
  return (
    <main className="page-shell w-full flex-1">
      <div className="mx-auto w-full flex max-w-2xl flex-col gap-6">{children}</div>
    </main>
  );
}

function when(iso: string): string {
  return new Date(iso).toLocaleString(undefined, { weekday: "short", hour: "numeric", minute: "2-digit" });
}

function ItemList({
  title,
  note,
  items,
  onOpen,
}: {
  title: string;
  note?: string;
  items: RevisionItem[];
  onOpen: (conceptId: string) => void;
}) {
  if (items.length === 0) return null;
  return (
    <section className="flex flex-col gap-2">
      <h2 className="display text-xl font-bold text-foreground">
        {title} <span className="text-sm font-normal text-muted-foreground">· {items.length}</span>
      </h2>
      {note && <p className="text-sm text-muted-foreground">{note}</p>}
      <ul className="flex flex-col gap-2">
        {items.map((i) => (
          <li
            key={i.concept_id}
            className="flex flex-col gap-2 surface p-4 sm:flex-row sm:items-center sm:justify-between sm:gap-4"
          >
            <div className="flex flex-col gap-0.5">
              <span className="font-semibold text-foreground">
                {i.concept_name}
                {i.chapter_name && <span className="ml-2 text-xs font-normal text-muted-foreground">{i.chapter_name}</span>}
                {i.kind === "teacher" && <span className="tag ml-2">From your teacher</span>}
                {i.kind === "refresh" && <span className="tag ml-2">Keep it fresh</span>}
              </span>
              <span className="text-sm text-muted-foreground">{i.reason}</span>
              {!i.due && (
                <span className="flex items-center gap-1 text-xs text-muted-foreground">
                  <Clock className="size-3" aria-hidden /> Best after {when(i.due_at)}
                </span>
              )}
            </div>
            <Button
              variant={i.due ? "default" : "outline"}
              size="sm"
              className="shrink-0 self-start sm:self-auto"
              onClick={() => onOpen(i.concept_id)}
            >
              New question <ArrowRight className="size-4" />
            </Button>
          </li>
        ))}
      </ul>
    </section>
  );
}

function QuestionView({ conceptId, onBack }: { conceptId: string; onBack: () => void }) {
  const question = useFetch(`revision-q:${conceptId}`, () => getRevisionQuestion(conceptId));
  const [picked, setPicked] = useState<string | undefined>();
  const [confidence, setConfidence] = useState<Confidence | undefined>();
  const [sending, setSending] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<RevisionResult | null>(null);

  async function check() {
    if (!picked || !confidence) return;
    setSending(true);
    setError(null);
    try {
      setResult(await submitRevision(conceptId, picked, confidence));
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setSending(false);
    }
  }

  const back = (
    <Button variant="ghost" className="self-start" onClick={onBack}>
      <ArrowLeft className="size-4" /> Revision list
    </Button>
  );

  if (question.loading) return <div className="h-60 animate-pulse rounded-xl bg-muted" />;
  if (!question.data) {
    return (
      <>
        {back}
        <FormError message={question.error ?? "Couldn't load the question."} />
      </>
    );
  }

  if (result) {
    const mastered = result.mastery_signal === "mastered";
    return (
      <>
        <section
          className={cn(
            "surface flex flex-col gap-4 p-6",
            result.correct
              ? "!border-success/40 !bg-success/5"
              : "!border-destructive/40 !bg-destructive/5",
          )}
        >
          <h1
            className={cn(
              "flex items-center gap-2 text-xl font-bold",
              result.correct ? "text-success" : "text-destructive",
            )}
          >
            {result.correct ? <CheckCircle2 className="size-6" /> : <XCircle className="size-6" />}
            {mastered ? `${question.data.concept_name}: mastered!` : result.correct ? "Right!" : "Not quite"}
          </h1>
          {result.mastery_note && <p className="text-sm text-foreground">{result.mastery_note}</p>}
          <div className="surface p-4">
            <Markdown className="prose-sm">{result.feedback}</Markdown>
          </div>
        </section>
        <div className="flex flex-wrap gap-3">
          <Button onClick={onBack}>
            <RotateCcw className="size-5" /> Back to revision
          </Button>
          <Button variant="outline" asChild>
            <Link href="/mix-ups">My mix-ups</Link>
          </Button>
        </div>
      </>
    );
  }

  return (
    <>
      {back}
      <div className="flex flex-col gap-1">
        <span className="eyebrow">
          New question · {question.data.chapter_name}
        </span>
        <h1 className="display text-4xl font-semibold text-foreground">{question.data.concept_name}</h1>
      </div>
      <CheckQuestion
        question={question.data}
        picked={picked}
        onPick={setPicked}
        confidence={confidence}
        onConfidence={setConfidence}
        disabled={sending}
        allowUnsure={false}
      />
      <FormError message={error} />
      <Button className="self-start" onClick={check} disabled={!picked || !confidence || sending}>
        {sending ? "Checking…" : "Check my answer"}
      </Button>
    </>
  );
}
