// The starting check (/start): a few minutes after signup that tell EcoLearn
// what a student already understands, which mix-ups they hold, and what they
// enjoy — so the roadmap can skip what they know and point at what to fix.
//
// Flow: intro → hobbies → one question at a time → their plan.
// Nothing is graded in front of them question by question: it's a starting
// point, not a test, and "Not sure" is always an honest option. Answers are
// sent once at the end; the answer key never reaches the browser.
//
// Interactive since 2026-10-04: tile-style hobby picker, a segmented progress
// bar, keyboard shortcuts (A–D, U for "not sure", S/T/G for how sure, Enter), a
// slide between questions, and a plan reveal that counts up. Motion is CSS-only
// and off under reduced motion.

"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Check, Clock, Compass, Route, Sparkles, Target } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { Confetti } from "@/components/check-feedback";
import { CheckQuestion, UNSURE } from "@/components/check-question";
import { LearningPlanSummary } from "@/components/learning-plan";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";
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

// Keyboard shortcuts must not fire while the student types in a text field, or
// on a button/link (which own Enter). A radio is where focus lands after
// picking an option, so it does not block them.
function typingInto(target: EventTarget | null): boolean {
  const el = target as HTMLElement | null;
  if (!el) return false;
  if (el instanceof HTMLInputElement && (el.type === "radio" || el.type === "checkbox")) return false;
  return el.isContentEditable || ["INPUT", "TEXTAREA", "SELECT", "BUTTON", "A"].includes(el.tagName);
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
  const [direction, setDirection] = useState<"next" | "prev">("next");
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

  const q = questions[index];
  const picked = q ? answers[q.concept_id] : undefined;
  const last = index === questions.length - 1;
  // An option needs "how sure?" too; "not sure" already says it.
  const ready = Boolean(q) && (picked === UNSURE || (!!picked && !!confidence[q.concept_id]));

  function goNext() {
    if (!ready || sending) return;
    if (last) {
      finish();
    } else {
      setDirection("next");
      setIndex((i) => i + 1);
    }
  }
  function goBack() {
    if (sending) return;
    if (index === 0) setStage("hobbies");
    else {
      setDirection("prev");
      setIndex((i) => i - 1);
    }
  }

  // Keys: A–D (or 1–4) pick, U / 0 = not sure, S / T / G = how sure, Enter = next.
  const latest = useRef({ goNext, q, picked });
  useEffect(() => {
    latest.current = { goNext, q, picked };
  });
  useEffect(() => {
    if (stage !== "questions") return;
    function onKey(e: KeyboardEvent) {
      if (e.metaKey || e.ctrlKey || e.altKey || typingInto(e.target)) return;
      const { goNext: next, q: cur, picked: now } = latest.current;
      if (!cur) return;
      if (e.key === "Enter") {
        next();
        return;
      }
      const key = e.key.toUpperCase();
      const letters = Object.keys(cur.options);
      const choose = (value: string) => setAnswers((a) => ({ ...a, [cur.concept_id]: value }));
      if (key === "U" || key === "0") choose(UNSURE);
      else if (letters.includes(key)) choose(key);
      else if (/^[1-9]$/.test(key) && letters[Number(key) - 1]) choose(letters[Number(key) - 1]);
      else if (now && now !== UNSURE) {
        const sure = { S: "sure", T: "think", G: "guess" }[key] as Confidence | undefined;
        if (sure) setConfidence((c) => ({ ...c, [cur.concept_id]: sure }));
      }
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [stage]);

  if (stage === "intro") {
    return (
      <Shell>
        <div className="flex flex-col gap-3">
          <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
            Your starting check
          </span>
          <h1 className="text-3xl font-extrabold tracking-tight text-foreground sm:text-4xl">
            Let&apos;s find where you stand
          </h1>
          <p className="leading-relaxed text-muted-foreground">
            {questions.length}{" "}quick questions. If you don&apos;t know an answer, say so: a guess
            would send you the wrong way.
          </p>
        </div>
        <ul className="grid gap-3 sm:grid-cols-3">
          {[
            { Icon: Clock, title: "About 5 minutes", text: "One question at a time." },
            { Icon: Target, title: "No marks", text: "It only shapes your path." },
            { Icon: Route, title: "Your own roadmap", text: "Skips what you know, flags what to fix." },
          ].map(({ Icon, title, text }, i) => (
            <li
              key={title}
              className="rm-sheet flex flex-col gap-1.5 rounded-2xl border border-border bg-card p-4 shadow-soft"
              style={{ animationDelay: `${i * 90}ms` }}
            >
              <Icon className="size-6 text-primary" aria-hidden />
              <span className="font-semibold text-foreground">{title}</span>
              <span className="text-sm text-muted-foreground">{text}</span>
            </li>
          ))}
        </ul>
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
            {hobbies.length === 0 ? "Skip this" : "Next"} <ArrowRight className="size-5" />
          </PrimaryButton>
          <Button variant="ghost" onClick={() => setStage("intro")}>
            <ArrowLeft className="size-4" /> Back
          </Button>
        </div>
      </Shell>
    );
  }

  const pickIt = (value: string) => setAnswers((a) => ({ ...a, [q.concept_id]: value }));
  const cheer =
    index === 0
      ? "No marks. Honest answers help most."
      : last
        ? "Last one!"
        : index === Math.floor(questions.length / 2)
          ? "Halfway there."
          : null;
  const hint = !picked
    ? "Pick an answer (A–D), or press U for not sure."
    : picked !== UNSURE && !confidence[q.concept_id]
      ? "How sure? Press S, T or G."
      : last
        ? "Press Enter to see your plan."
        : "Press Enter for the next question.";

  return (
    <Shell>
      <StepLabel step={2} />

      {/* Segmented progress: green = answered, indigo = here. */}
      <div className="flex flex-col gap-2">
        <div className="flex items-center justify-between text-sm text-muted-foreground">
          <span className="font-semibold text-foreground">
            Question {index + 1} of {questions.length}
          </span>
          {q.chapter_name && <span className="truncate pl-3">{q.chapter_name}</span>}
        </div>
        <div
          role="progressbar"
          aria-valuemin={1}
          aria-valuemax={questions.length}
          aria-valuenow={index + 1}
          className="flex gap-1.5"
        >
          {questions.map((x, i) => (
            <span
              key={x.concept_id}
              className={cn(
                "h-2 flex-1 rounded-full transition-colors duration-300",
                i < index || (i === index && ready)
                  ? "bg-success"
                  : i === index
                    ? "bg-primary"
                    : "bg-muted",
              )}
            />
          ))}
        </div>
        {cheer && (
          <p className="rm-sheet text-sm font-medium text-brand-accent" key={cheer}>
            {cheer}
          </p>
        )}
      </div>

      <div key={q.concept_id} className={direction === "next" ? "rm-slide-next" : "rm-slide-prev"}>
        <CheckQuestion
          question={q}
          picked={picked}
          onPick={pickIt}
          confidence={confidence[q.concept_id]}
          onConfidence={(value) => setConfidence((c) => ({ ...c, [q.concept_id]: value }))}
          disabled={sending}
        />
      </div>

      <FormError message={error} />

      {/* Back / Next, always in reach, saying what's still needed. */}
      <div className="sticky bottom-3 z-20 flex items-center justify-between gap-3 rounded-2xl border border-border bg-card/95 p-2.5 shadow-card-hover backdrop-blur">
        <Button variant="ghost" size="lg" disabled={sending} onClick={goBack} className="h-11 rounded-xl px-4">
          <ArrowLeft className="size-4" /> Back
        </Button>
        <span role="status" className="hidden flex-1 text-center text-xs text-muted-foreground sm:block">
          {hint}
        </span>
        <PrimaryButton onClick={goNext} disabled={!ready || sending} className="h-11 shrink-0 px-5">
          {sending ? (
            "Building your plan…"
          ) : last ? (
            <>
              See my plan <Sparkles className="size-5" />
            </>
          ) : (
            <>
              Next <ArrowRight className="size-5" />
            </>
          )}
        </PrimaryButton>
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
        <h1 className="text-3xl font-extrabold tracking-tight text-foreground">What do you enjoy?</h1>
        <p className="text-muted-foreground">
          Tap a few. EcoLearn uses them to make examples feel like yours. Optional.
        </p>
      </div>

      <ul className="grid grid-cols-3 gap-2.5 sm:grid-cols-4">
        {options.map((o) => {
          const on = value.includes(o.id);
          return (
            <li key={o.id}>
              <button
                type="button"
                aria-pressed={on}
                disabled={!on && full}
                onClick={() => toggle(o.id)}
                className={cn(
                  "relative flex w-full flex-col items-center gap-1 rounded-2xl border p-3 text-center text-sm font-medium transition-all duration-150 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:opacity-40",
                  on
                    ? "-translate-y-0.5 border-primary bg-primary/10 text-foreground shadow-card ring-2 ring-primary"
                    : "border-border bg-card text-foreground hover:-translate-y-0.5 hover:border-primary/50 hover:shadow-soft",
                )}
              >
                <span aria-hidden className={cn("text-3xl", on && "rm-pop")}>
                  {o.emoji}
                </span>
                <span className="leading-tight">{o.label}</span>
                {on && (
                  <span className="rm-pop absolute right-1.5 top-1.5 flex size-5 items-center justify-center rounded-full bg-primary text-primary-foreground">
                    <Check className="size-3" strokeWidth={3} aria-hidden />
                  </span>
                )}
              </button>
            </li>
          );
        })}
        {ownOnes.map((h) => (
          <li key={h}>
            <button
              type="button"
              aria-pressed
              onClick={() => toggle(h)}
              className="relative flex w-full flex-col items-center gap-1 rounded-2xl border border-primary bg-primary/10 p-3 text-center text-sm font-medium capitalize text-foreground ring-2 ring-primary"
            >
              <span aria-hidden className="text-3xl">
                ✨
              </span>
              <span className="leading-tight">{h}</span>
              <span className="absolute right-1.5 top-1.5 flex size-5 items-center justify-center rounded-full bg-primary text-primary-foreground">
                <Check className="size-3" strokeWidth={3} aria-hidden />
              </span>
            </button>
          </li>
        ))}
      </ul>

      <p className="text-sm text-muted-foreground" aria-live="polite">
        {value.length === 0 ? "None picked yet." : `${value.length} of ${MAX_HOBBIES} picked.`}
      </p>

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
      <div className="relative flex flex-col gap-2">
        <Confetti />
        <span className="rm-sheet flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-brand-accent">
          <Sparkles className="size-4" aria-hidden /> Your plan is ready
        </span>
        <h1 className="text-3xl font-extrabold tracking-tight text-foreground sm:text-4xl">
          Here&apos;s where you stand
        </h1>
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
