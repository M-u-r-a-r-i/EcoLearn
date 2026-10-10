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
import { ArrowLeft, ArrowRight, Clock, Compass, Route, Sparkles, Target } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { useAuth } from "@/components/auth-provider";
import { HobbyPicker } from "@/components/hobby-picker";
import { Confetti } from "@/components/check-feedback";
import { CheckQuestion, UNSURE } from "@/components/check-question";
import { LearningPlanSummary } from "@/components/learning-plan";
import { Skeleton } from "@/components/ui-kit";
import { Button } from "@/components/ui/button";
import {
  friendlyMessage,
  getDiagnostic,
  getLearningPlan,
  submitDiagnostic,
  type Confidence,
  type Diagnostic,
  type LearningPlan,
} from "@/lib/api";
import { rememberSkippedCheck } from "@/lib/landing";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

type Stage = "intro" | "hobbies" | "questions" | "done";

export default function StartPage() {
  const diagnostic = useFetch("diagnostic", getDiagnostic);
  // Once taken, the plan is fetched; right after submitting it comes back with the result.
  const [plan, setPlan] = useState<LearningPlan | null>(null);

  if (diagnostic.loading) {
    return (
      <Shell>
        <div className="surface">
          <Skeleton rows={4} />
        </div>
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
    <main className="page-shell start-shell mx-auto w-full flex-1">
      <div className="flex flex-col gap-6">{children}</div>
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
  const { student } = useAuth();
  const questions = diagnostic.questions ?? [];
  // Hobbies come from the first-login survey; only a student without any is asked here.
  const needsHobbies = diagnostic.hobbies.length === 0;
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
    if (index === 0) setStage(needsHobbies ? "hobbies" : "intro");
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
          <span className="eyebrow">Your starting check</span>
          <h1 className="display text-4xl font-semibold text-foreground sm:text-5xl">
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
              className="rm-sheet surface flex flex-col gap-1.5 p-4"
              style={{ animationDelay: `${i * 90}ms` }}
            >
              <Icon className="size-6 text-primary" aria-hidden />
              <span className="font-heading font-bold text-foreground">{title}</span>
              <span className="text-sm text-muted-foreground">{text}</span>
            </li>
          ))}
        </ul>
        <div className="flex flex-wrap gap-3">
          <Button onClick={() => setStage(needsHobbies ? "hobbies" : "questions")}>
            Let&apos;s go <ArrowRight className="size-5" />
          </Button>
          <Button variant="ghost" asChild>
            <Link href="/roadmap" onClick={() => student && rememberSkippedCheck(student.student_id)}>
              Skip for now
            </Link>
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
        <div className="flex flex-wrap items-center gap-3">
          {/* Hobbies are what makes the stories yours, so "Next" waits for at least one. */}
          <Button onClick={() => setStage("questions")} disabled={hobbies.length === 0}>
            Next <ArrowRight className="size-5" />
          </Button>
          <Button variant="ghost" onClick={() => setStage("intro")}>
            <ArrowLeft className="size-4" /> Back
          </Button>
          {hobbies.length === 0 && (
            <button
              type="button"
              onClick={() => setStage("questions")}
              className="ml-auto min-h-10 text-xs font-semibold text-muted-foreground underline-offset-2 hover:text-foreground hover:underline"
            >
              I&apos;d rather not say
            </button>
          )}
        </div>
        {hobbies.length === 0 && (
          <p className="text-sm text-muted-foreground">
            Pick at least one, and your lessons will open with a story about it.
          </p>
        )}
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
      <StepLabel step={needsHobbies ? 2 : 1} total={needsHobbies ? 2 : 1} />

      {/* Segmented progress: solid = answered, soft = here. */}
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
                  ? "bg-primary"
                  : i === index
                    ? "bg-primary/45"
                    : "bg-secondary",
              )}
            />
          ))}
        </div>
        {cheer && (
          <p className="rm-sheet text-sm font-semibold text-primary" key={cheer}>
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
      <div className="sticky bottom-20 z-20 flex items-center justify-between gap-3 rounded-[18px] border border-border bg-card/95 p-2.5 shadow-card-hover backdrop-blur md:bottom-3">
        <Button variant="ghost" disabled={sending} onClick={goBack}>
          <ArrowLeft className="size-4" /> Back
        </Button>
        <span role="status" className="hidden flex-1 text-center text-xs text-muted-foreground sm:block">
          {hint}
        </span>
        <Button onClick={goNext} disabled={!ready || sending} className="shrink-0">
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
        </Button>
      </div>
    </Shell>
  );
}

function StepLabel({ step, total = 2 }: { step: 1 | 2; total?: 1 | 2 }) {
  return (
    <span className="eyebrow">
      Starting check{total === 2 ? ` · step ${step} of 2` : ""} ·{" "}
      {step === 1 && total === 2 ? "what you enjoy" : "where you stand"}
    </span>
  );
}

function Done({ plan }: { plan: LearningPlan }) {
  return (
    <Shell>
      <div className="relative flex flex-col gap-2">
        <Confetti />
        <span className="rm-sheet eyebrow flex items-center gap-2">
          <Sparkles className="size-4" aria-hidden /> Your plan is ready
        </span>
        <h1 className="display text-4xl font-semibold text-foreground sm:text-5xl">
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
        <span className="eyebrow flex items-center gap-2">
          <Compass className="size-4" aria-hidden /> Your starting check
        </span>
        <h1 className="display text-4xl font-semibold text-foreground">You&apos;ve already taken it</h1>
        <p className="text-muted-foreground">
          It&apos;s taken once, as your starting point. Your plan keeps updating as you answer lesson
          checks.
        </p>
      </div>
      {plan.data ? (
        <LearningPlanSummary plan={plan.data} />
      ) : (
        <div className="surface">
          <Skeleton rows={3} />
        </div>
      )}
    </Shell>
  );
}
