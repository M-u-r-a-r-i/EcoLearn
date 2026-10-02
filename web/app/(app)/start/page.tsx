// The starting check (/start): a few minutes after signup that tell EcoLearn
// what a student already understands, which mix-ups they hold, and what they
// enjoy — so the roadmap can skip what they know and point at what to fix.
//
// Flow: intro → hobbies → one question at a time → their plan.
// Nothing is graded in front of them question by question: it's a starting
// point, not a test, and "Not sure" is always an honest option. Answers are
// sent once at the end; the answer key never reaches the browser.

"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Check, Compass, Sparkles } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { CheckQuestion, UNSURE } from "@/components/check-question";
import { LearningPlanSummary } from "@/components/learning-plan";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import {
  friendlyMessage,
  getDiagnostic,
  getLearningPlan,
  submitDiagnostic,
  type Confidence,
  type Diagnostic,
  type HobbyOption,
  type LearningPlan,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

const MAX_HOBBIES = 8;
const MAX_OWN = 2;
const OWN_HOBBY = /^[A-Za-z][A-Za-z &'-]{1,23}$/;

type Stage = "intro" | "hobbies" | "questions" | "done";

export default function StartPage() {
  const diagnostic = useFetch("diagnostic", getDiagnostic);
  // Once taken, the plan is fetched; right after submitting it comes back with the result.
  const [plan, setPlan] = useState<LearningPlan | null>(null);

  if (diagnostic.loading) {
    return (
      <Shell>
        <div className="h-8 w-64 animate-pulse rounded-lg bg-muted" />
        <div className="h-48 animate-pulse rounded-xl bg-muted" />
      </Shell>
    );
  }
  if (!diagnostic.data) {
    return (
      <Shell>
        <FormError message={diagnostic.error ?? "Couldn't load the starting check."} />
        <Link href="/roadmap" className="text-sm font-semibold text-primary hover:underline">
          Go to your roadmap
        </Link>
      </Shell>
    );
  }
  if (plan) return <Done plan={plan} />;
  if (diagnostic.data.taken) return <AlreadyTaken />;
  return <StartingCheck diagnostic={diagnostic.data} onDone={setPlan} />;
}

function Shell({ children }: { children: React.ReactNode }) {
  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex max-w-2xl flex-col gap-6">{children}</PageContainer>
    </main>
  );
}

function StartingCheck({
  diagnostic,
  onDone,
}: {
  diagnostic: Diagnostic;
  onDone: (plan: LearningPlan) => void;
}) {
  const questions = diagnostic.questions ?? [];
  const [stage, setStage] = useState<Stage>("intro");
  const [hobbies, setHobbies] = useState<string[]>(diagnostic.hobbies);
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [confidence, setConfidence] = useState<Record<string, Confidence>>({});
  const [sending, setSending] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function finish() {
    setSending(true);
    setError(null);
    try {
      const out = await submitDiagnostic(answers, hobbies, confidence);
      onDone(out.plan);
    } catch (err) {
      setError(friendlyMessage(err));
      setSending(false);
    }
  }

  if (stage === "intro") {
    return (
      <Shell>
        <div className="flex flex-col gap-3">
          <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
            Your starting check
          </span>
          <h1 className="text-3xl font-bold tracking-tight text-foreground">
            Let&apos;s find where you stand
          </h1>
          <p className="leading-relaxed text-muted-foreground">
            {questions.length}{" "}quick questions, about five minutes. There are no marks — this only
            helps EcoLearn skip what you already understand and spot the mix-ups worth fixing
            first. If you don&apos;t know an answer, say so: a guess would send you the wrong way.
          </p>
        </div>
        <div className="flex flex-wrap gap-3">
          <PrimaryButton onClick={() => setStage("hobbies")}>
            Let&apos;s go <ArrowRight className="size-5" />
          </PrimaryButton>
          <Button variant="ghost" asChild>
            <Link href="/roadmap">Skip for now</Link>
          </Button>
        </div>
      </Shell>
    );
  }

  if (stage === "hobbies") {
    return (
      <Shell>
        <StepLabel step={1} />
        <HobbyPicker options={diagnostic.hobby_options} value={hobbies} onChange={setHobbies} />
        <div className="flex gap-3">
          <PrimaryButton onClick={() => setStage("questions")}>
            Next <ArrowRight className="size-5" />
          </PrimaryButton>
          <Button variant="ghost" onClick={() => setStage("intro")}>
            <ArrowLeft className="size-4" /> Back
          </Button>
        </div>
      </Shell>
    );
  }

  const q = questions[index];
  const picked = answers[q.concept_id];
  const last = index === questions.length - 1;
  const pick = (value: string) => setAnswers((a) => ({ ...a, [q.concept_id]: value }));
  // An option needs "how sure?" too; "not sure" already says it.
  const ready = picked === UNSURE || (!!picked && !!confidence[q.concept_id]);

  return (
    <Shell>
      <StepLabel step={2} />
      <div className="flex flex-col gap-2">
        <div className="flex items-center justify-between text-sm text-muted-foreground">
          <span>
            Question {index + 1} of {questions.length}
          </span>
          {q.chapter_name && <span>{q.chapter_name}</span>}
        </div>
        <Progress value={((index + (ready ? 1 : 0)) / questions.length) * 100} />
      </div>

      <CheckQuestion
        question={q}
        picked={picked}
        onPick={pick}
        confidence={confidence[q.concept_id]}
        onConfidence={(value) => setConfidence((c) => ({ ...c, [q.concept_id]: value }))}
        disabled={sending}
      />

      <FormError message={error} />

      <div className="flex flex-wrap gap-3">
        {last ? (
          <PrimaryButton onClick={finish} disabled={!ready || sending}>
            {sending ? "Building your plan…" : <>See my plan <Sparkles className="size-5" /></>}
          </PrimaryButton>
        ) : (
          <PrimaryButton onClick={() => setIndex((i) => i + 1)} disabled={!ready}>
            Next <ArrowRight className="size-5" />
          </PrimaryButton>
        )}
        <Button
          variant="ghost"
          disabled={sending}
          onClick={() => (index === 0 ? setStage("hobbies") : setIndex((i) => i - 1))}
        >
          <ArrowLeft className="size-4" /> Back
        </Button>
      </div>
    </Shell>
  );
}

function StepLabel({ step }: { step: 1 | 2 }) {
  return (
    <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
      Starting check · step {step} of 2 · {step === 1 ? "what you enjoy" : "where you stand"}
    </span>
  );
}

function HobbyPicker({
  options,
  value,
  onChange,
}: {
  options: HobbyOption[];
  value: string[];
  onChange: (next: string[]) => void;
}) {
  const [own, setOwn] = useState("");
  const [ownError, setOwnError] = useState<string | null>(null);
  const listed = new Set(options.map((o) => o.id));
  const ownOnes = value.filter((h) => !listed.has(h));
  const full = value.length >= MAX_HOBBIES;

  function toggle(id: string) {
    if (value.includes(id)) onChange(value.filter((h) => h !== id));
    else if (!full) onChange([...value, id]);
  }

  function addOwn() {
    const label = own.trim();
    if (!label) return;
    if (!OWN_HOBBY.test(label)) {
      setOwnError("Keep it short: letters and spaces, up to 24 characters.");
      return;
    }
    if (ownOnes.length >= MAX_OWN || full) {
      setOwnError(`You can add up to ${MAX_OWN} of your own.`);
      return;
    }
    setOwnError(null);
    setOwn("");
    if (!value.includes(label.toLowerCase())) onChange([...value, label.toLowerCase()]);
  }

  return (
    <div className="flex flex-col gap-5">
      <div className="flex flex-col gap-2">
        <h1 className="text-3xl font-bold tracking-tight text-foreground">What do you enjoy?</h1>
        <p className="text-muted-foreground">
          Pick a few (up to {MAX_HOBBIES}). EcoLearn will use them to make examples feel like
          yours. Optional.
        </p>
      </div>
      <div className="flex flex-wrap gap-2">
        {options.map((o) => {
          const on = value.includes(o.id);
          return (
            <button
              key={o.id}
              type="button"
              aria-pressed={on}
              disabled={!on && full}
              onClick={() => toggle(o.id)}
              className={cn(
                "inline-flex items-center gap-1.5 rounded-full border px-3.5 py-2 text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:opacity-40",
                on
                  ? "border-primary bg-primary text-primary-foreground"
                  : "border-border bg-card text-foreground hover:border-primary/50",
              )}
            >
              <span aria-hidden>{o.emoji}</span>
              {o.label}
              {on && <Check className="size-3.5" aria-hidden />}
            </button>
          );
        })}
        {ownOnes.map((h) => (
          <button
            key={h}
            type="button"
            aria-pressed
            onClick={() => toggle(h)}
            className="inline-flex items-center gap-1.5 rounded-full border border-primary bg-primary px-3.5 py-2 text-sm font-medium capitalize text-primary-foreground"
          >
            {h} <Check className="size-3.5" aria-hidden />
          </button>
        ))}
      </div>
      <div className="flex flex-col gap-1">
        <label htmlFor="own-hobby" className="text-sm font-semibold text-muted-foreground">
          Something else?
        </label>
        <div className="flex max-w-sm gap-2">
          <input
            id="own-hobby"
            value={own}
            maxLength={24}
            onChange={(e) => setOwn(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                e.preventDefault();
                addOwn();
              }
            }}
            placeholder="e.g. kite flying"
            className="h-10 flex-1 rounded-lg border border-input bg-card px-3 text-sm text-foreground shadow-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          />
          <Button type="button" variant="outline" onClick={addOwn}>
            Add
          </Button>
        </div>
        {ownError && <p className="text-sm text-destructive">{ownError}</p>}
      </div>
    </div>
  );
}

function Done({ plan }: { plan: LearningPlan }) {
  return (
    <Shell>
      <div className="flex flex-col gap-2">
        <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
          Your plan is ready
        </span>
        <h1 className="text-3xl font-bold tracking-tight text-foreground">Here&apos;s where you stand</h1>
      </div>
      <LearningPlanSummary plan={plan} />
    </Shell>
  );
}

function AlreadyTaken() {
  const plan = useFetch("learning-plan", getLearningPlan);
  return (
    <Shell>
      <div className="flex flex-col gap-2">
        <span className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-brand-accent">
          <Compass className="size-4" aria-hidden /> Your starting check
        </span>
        <h1 className="text-3xl font-bold tracking-tight text-foreground">You&apos;ve already taken it</h1>
        <p className="text-muted-foreground">
          It&apos;s taken once, as your starting point. Your plan keeps updating as you answer lesson
          checks.
        </p>
      </div>
      {plan.data ? (
        <LearningPlanSummary plan={plan.data} />
      ) : (
        <div className="h-40 animate-pulse rounded-xl bg-muted" />
      )}
    </Shell>
  );
}
