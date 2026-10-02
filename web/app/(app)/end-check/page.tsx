// The end check (/end-check): the starting check's concepts again, each with a
// new question, once the teacher opens it at the end of the pilot. The result
// is a before → after the student can see: which mix-ups they fixed, what
// they've learned since "not sure", and what is worth another look.
//
// Same flow as /start without the hobbies step: intro → one question at a time
// → result. Answers are sent once; the answer key never reaches the browser.

"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Flag, Sparkles } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { CheckQuestion } from "@/components/check-question";
import { CheckResultSummary } from "@/components/check-result";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { friendlyMessage, getEndCheck, submitEndCheck, type EndCheck } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";

export default function EndCheckPage() {
  const endCheck = useFetch("end-check", getEndCheck);
  // Right after submitting, the result comes back in the response.
  const [done, setDone] = useState<EndCheck | null>(null);

  if (endCheck.loading) {
    return (
      <Shell>
        <div className="h-8 w-64 animate-pulse rounded-lg bg-muted" />
        <div className="h-48 animate-pulse rounded-xl bg-muted" />
      </Shell>
    );
  }
  if (!endCheck.data) {
    return (
      <Shell>
        <FormError message={endCheck.error ?? "Couldn't load the end check."} />
        <RoadmapLink />
      </Shell>
    );
  }

  const state = done ?? endCheck.data;
  if (state.status === "taken" && state.comparison) {
    return (
      <Shell>
        <Heading eyebrow="Your end check" title="How far you've come" />
        <CheckResultSummary comparison={state.comparison} />
        <RoadmapLink />
      </Shell>
    );
  }
  if (state.status === "needs_start") {
    return (
      <Shell>
        <Heading eyebrow="Your end check" title="Take the starting check first" />
        <p className="text-muted-foreground">
          The end check is compared with your starting check, so that one comes first. It takes about
          five minutes.
        </p>
        <PrimaryButton asChild className="self-start">
          <Link href="/start">
            Start the starting check <ArrowRight className="size-5" />
          </Link>
        </PrimaryButton>
      </Shell>
    );
  }
  if (state.status !== "open" || !state.questions?.length) {
    return (
      <Shell>
        <Heading eyebrow="Your end check" title="Not open yet" />
        <p className="text-muted-foreground">
          Your teacher opens the end check for the whole class at the end of the course. Until then,
          keep going with your lessons.
        </p>
        <RoadmapLink />
      </Shell>
    );
  }
  return <Questions endCheck={state} onDone={setDone} />;
}

function Shell({ children }: { children: React.ReactNode }) {
  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex max-w-2xl flex-col gap-6">{children}</PageContainer>
    </main>
  );
}

function Heading({ eyebrow, title }: { eyebrow: string; title: string }) {
  return (
    <div className="flex flex-col gap-2">
      <span className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-brand-accent">
        <Flag className="size-4" aria-hidden /> {eyebrow}
      </span>
      <h1 className="text-3xl font-bold tracking-tight text-foreground">{title}</h1>
    </div>
  );
}

function RoadmapLink() {
  return (
    <Link href="/roadmap" className="self-start text-sm font-semibold text-primary hover:underline">
      Back to your roadmap
    </Link>
  );
}

function Questions({ endCheck, onDone }: { endCheck: EndCheck; onDone: (e: EndCheck) => void }) {
  const questions = endCheck.questions ?? [];
  const [started, setStarted] = useState(false);
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [sending, setSending] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function finish() {
    setSending(true);
    setError(null);
    try {
      onDone(await submitEndCheck(answers));
    } catch (err) {
      setError(friendlyMessage(err));
      setSending(false);
    }
  }

  if (!started) {
    return (
      <Shell>
        <Heading eyebrow="Your end check" title="Let's see what's changed" />
        <p className="leading-relaxed text-muted-foreground">
          {questions.length}{" "}questions on the same ideas as your starting check, but new questions —
          about five minutes. There are no marks. Afterwards you&apos;ll see which mix-ups you&apos;ve
          fixed. If you don&apos;t know an answer, say so: an honest &ldquo;not sure&rdquo; is more useful
          than a guess.
        </p>
        <div className="flex flex-wrap gap-3">
          <PrimaryButton onClick={() => setStarted(true)}>
            Let&apos;s go <ArrowRight className="size-5" />
          </PrimaryButton>
          <Button variant="ghost" asChild>
            <Link href="/roadmap">Later</Link>
          </Button>
        </div>
      </Shell>
    );
  }

  const q = questions[index];
  const picked = answers[q.concept_id];
  const last = index === questions.length - 1;

  return (
    <Shell>
      <div className="flex flex-col gap-2">
        <div className="flex items-center justify-between text-sm text-muted-foreground">
          <span>
            Question {index + 1} of {questions.length}
          </span>
          {q.chapter_name && <span>{q.chapter_name}</span>}
        </div>
        <Progress value={((index + (picked ? 1 : 0)) / questions.length) * 100} />
      </div>

      <CheckQuestion
        question={q}
        picked={picked}
        onPick={(value) => setAnswers((a) => ({ ...a, [q.concept_id]: value }))}
        disabled={sending}
      />

      <FormError message={error} />

      <div className="flex flex-wrap gap-3">
        {last ? (
          <PrimaryButton onClick={finish} disabled={!picked || sending}>
            {sending ? "Comparing…" : <>See how far I&apos;ve come <Sparkles className="size-5" /></>}
          </PrimaryButton>
        ) : (
          <PrimaryButton onClick={() => setIndex((i) => i + 1)} disabled={!picked}>
            Next <ArrowRight className="size-5" />
          </PrimaryButton>
        )}
        <Button
          variant="ghost"
          disabled={sending}
          onClick={() => (index === 0 ? setStarted(false) : setIndex((i) => i - 1))}
        >
          <ArrowLeft className="size-4" /> Back
        </Button>
      </div>
    </Shell>
  );
}
