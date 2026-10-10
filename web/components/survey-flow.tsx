// "Getting to know you" (2026-10-08): the first thing a student sees after a teacher creates
// their account. Not a test: no right answers, nothing graded, every question skippable.
//
// Intro -> five short parts (what you enjoy, your hobbies honestly, how you learn, focus and
// energy, you and physics) -> a "here's what we'll do with this" screen. The questions come
// from the server (data/survey.yaml), so changing the survey needs no web change; this file
// only knows how to draw the five question types.
//
// Answers are fixed options only (no free text about a child), sent once at the end.

"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { ArrowLeft, ArrowRight, Check, Clock, Heart, ShieldCheck, Sparkles } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { Confetti } from "@/components/check-feedback";
import { HobbyPicker } from "@/components/hobby-picker";
import { Button } from "@/components/ui/button";
import {
  friendlyMessage,
  submitSurvey,
  updateSurvey,
  type Survey,
  type SurveyAnswers,
  type SurveyQuestion,
  type SurveyTraits,
} from "@/lib/api";
import { cn } from "@/lib/utils";

type Answer = string | string[] | Record<string, string | string[]>;

function Shell({ children }: { children: React.ReactNode }) {
  return (
    <main className="page-shell w-full flex-1">
      <div className="mx-auto w-full flex max-w-2xl flex-col gap-6">{children}</div>
    </main>
  );
}

export function SurveyFlow({
  survey,
  firstName,
  onDone,
  next,
  mode = "first",
  initialAnswers,
}: {
  survey: Survey;
  firstName: string;
  onDone: () => void; // the gate learns they're finished
  next: { href: string; label: string };
  // "first": the first-login welcome. "edit": changing answers later (from Settings): no intro,
  // the form starts filled in, and finishing replaces the answers instead of storing them.
  mode?: "first" | "edit";
  initialAnswers?: SurveyAnswers;
}) {
  const editing = mode === "edit";
  const router = useRouter();
  const questions = survey.questions ?? [];
  const sections = survey.sections ?? [];
  const labelOf = (id: string) =>
    survey.hobby_options?.find((h) => h.id === id)?.label ?? id.charAt(0).toUpperCase() + id.slice(1);

  const [stage, setStage] = useState<"intro" | "steps" | "done">(editing ? "steps" : "intro");
  const [index, setIndex] = useState(0);
  const [direction, setDirection] = useState<"next" | "prev">("next");
  const [answers, setAnswers] = useState<Record<string, Answer>>(
    (initialAnswers as Record<string, Answer> | undefined) ??
      (survey.hobbies?.length ? { hobbies: survey.hobbies } : {}),
  );
  const [sending, setSending] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [traits, setTraits] = useState<SurveyTraits | null>(null);

  const hobbies = (answers.hobbies as string[] | undefined) ?? [];
  const asked = hobbies.slice(0, 2); // the survey asks about the first two they tapped
  // Always the same five parts, so "Part 2 of 5" never changes under the student's feet.
  const steps = sections;
  const step = steps[Math.min(index, steps.length - 1)];

  const set = (id: string, value: Answer | undefined) =>
    setAnswers((a) => {
      const copy = { ...a };
      if (value === undefined || (Array.isArray(value) && value.length === 0)) delete copy[id];
      else copy[id] = value;
      return copy;
    });

  function go(to: number) {
    setDirection(to > index ? "next" : "prev");
    setIndex(to);
    window.scrollTo({ top: 0 });
  }

  async function finish() {
    setSending(true);
    setError(null);
    try {
      // Per-hobby answers only exist for the first two hobbies: if they changed their picks,
      // drop answers about hobbies that are no longer in the first two (the server refuses them).
      const body: Record<string, Answer> = { ...answers };
      for (const key of ["hobby_depth", "hobby_know"]) {
        const per = body[key] as Record<string, string | string[]> | undefined;
        if (per) {
          const kept = Object.fromEntries(Object.entries(per).filter(([h]) => asked.includes(h)));
          if (Object.keys(kept).length) body[key] = kept;
          else delete body[key];
        }
      }
      const out = await (editing ? updateSurvey : submitSurvey)(body as SurveyAnswers);
      setTraits(out.traits ?? null);
      onDone();
      setStage("done");
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setSending(false);
    }
  }

  // ---------------------------------------------------------------- intro
  if (stage === "intro") {
    return (
      <Shell>
        <div className="flex flex-col gap-3">
          <span className="eyebrow">
            Welcome to EcoLearn
          </span>
          <h1 className="display text-4xl font-semibold text-foreground sm:text-4xl">
            Hi {firstName}! Let&apos;s get to know you
          </h1>
          <p className="leading-relaxed text-muted-foreground">
            Before any physics, a few questions about <strong className="text-foreground">you</strong>:
            what you love, how you like to learn, how you focus. Your lessons will be shaped by
            your answers.
          </p>
        </div>
        <ul className="grid gap-3 sm:grid-cols-3">
          {[
            { Icon: Clock, title: "About 4 minutes", text: "Just taps, no typing." },
            { Icon: Heart, title: "No right answers", text: "Be honest: it only helps you." },
            { Icon: ShieldCheck, title: "Skip anything", text: "Your teacher sees a summary, not a score." },
          ].map(({ Icon, title, text }, i) => (
            <li
              key={title}
              className="rm-sheet flex flex-col gap-1.5 surface p-4"
              style={{ animationDelay: `${i * 90}ms` }}
            >
              <Icon className="size-6 text-primary" aria-hidden />
              <span className="font-semibold text-foreground">{title}</span>
              <span className="text-sm text-muted-foreground">{text}</span>
            </li>
          ))}
        </ul>
        <Button onClick={() => setStage("steps")} className="self-start">
          Let&apos;s start <ArrowRight className="size-5" />
        </Button>
      </Shell>
    );
  }

  // ---------------------------------------------------------------- done
  if (stage === "done") {
    return (
      <Shell>
        <div className="relative flex flex-col gap-2">
          {!editing && <Confetti />}
          <span className="rm-sheet flex items-center gap-2 eyebrow">
            <Sparkles className="size-4" aria-hidden /> {editing ? "Saved" : `Thanks, ${firstName}`}
          </span>
          <h1 className="display text-4xl font-semibold text-foreground sm:text-4xl">
            {editing ? "Here's what changes now" : "Here's what we'll do with this"}
          </h1>
        </div>
        <ul className="flex flex-col gap-3">
          {(traits ? whatWeHeard(traits, labelOf, !editing) : []).map((line, i) => (
            <li
              key={line.text}
              className="rm-sheet flex items-start gap-3 surface p-4"
              style={{ animationDelay: `${i * 80}ms` }}
            >
              <span aria-hidden className="text-2xl">
                {line.emoji}
              </span>
              <span className="text-foreground">{line.text}</span>
            </li>
          ))}
        </ul>
        <p className="text-sm text-muted-foreground">
          Nothing is locked in. You can change these again whenever you like, and your teacher
          can see a short summary to help you.
        </p>
        <Button onClick={() => router.push(next.href)} className="self-start">
          {next.label} <ArrowRight className="size-5" />
        </Button>
      </Shell>
    );
  }

  // ---------------------------------------------------------------- steps
  const last = index >= steps.length - 1;
  const inThisStep = questions.filter(
    (q) => q.section === step.id && q.type !== "hobbies" && !q.type.startsWith("hobby_"),
  );

  return (
    <Shell>
      <div className="flex flex-col gap-2">
        <div className="flex items-center justify-between text-sm text-muted-foreground">
          <span className="font-semibold text-foreground">
            Part {index + 1} of {steps.length}
          </span>
          <span>
            {step.emoji} {step.title}
          </span>
        </div>
        <div
          role="progressbar"
          aria-valuemin={1}
          aria-valuemax={steps.length}
          aria-valuenow={index + 1}
          className="flex gap-1.5"
        >
          {steps.map((s, i) => (
            <span
              key={s.id}
              className={cn(
                "h-2 flex-1 rounded-full transition-colors duration-300",
                i < index ? "bg-success" : i === index ? "bg-primary" : "bg-muted",
              )}
            />
          ))}
        </div>
      </div>

      <div key={step.id} className={cn(direction === "next" ? "rm-slide-next" : "rm-slide-prev", "flex flex-col gap-8")}>
        {step.id === "interests" && (
          <HobbyPicker
            options={survey.hobby_options ?? []}
            value={hobbies}
            onChange={(next) => set("hobbies", next)}
            heading="What do you enjoy?"
            blurb="Tap a few. Tap your favourites first: we'll ask about the first two."
          />
        )}

        {step.id === "hobby" && asked.length === 0 && (
          <p className="surface !border-dashed p-5 text-muted-foreground">
            You didn&apos;t pick any hobbies, so there&apos;s nothing to ask here. That&apos;s fine: your
            examples will use your main interest.
          </p>
        )}

        {step.id === "hobby" &&
          asked.map((hobby) => (
            <section key={hobby} className="flex flex-col gap-6 surface p-5">
              <h2 className="text-2xl font-bold tracking-tight text-foreground">
                About {labelOf(hobby)}
              </h2>
              {questions
                .filter((q) => q.type === "hobby_single" || q.type === "hobby_multi")
                .map((q) => (
                  <Question
                    key={q.id}
                    q={q}
                    hobbyLabel={labelOf(hobby)}
                    value={(answers[q.id] as Record<string, string | string[]> | undefined)?.[hobby]}
                    onChange={(v) => {
                      const per = { ...((answers[q.id] as Record<string, string | string[]> | undefined) ?? {}) };
                      if (v === undefined || (Array.isArray(v) && v.length === 0)) delete per[hobby];
                      else per[hobby] = v;
                      set(q.id, Object.keys(per).length ? per : undefined);
                    }}
                  />
                ))}
            </section>
          ))}

        {inThisStep.map((q) => (
          <Question key={q.id} q={q} value={answers[q.id] as string | string[] | undefined} onChange={(v) => set(q.id, v)} />
        ))}
      </div>

      <FormError message={error} />

      <div className="sticky bottom-3 z-20 flex items-center justify-between gap-3 surface/95 p-2.5-hover backdrop-blur">
        <Button
          variant="ghost"
          size="lg"
          disabled={sending}
          onClick={() => (index === 0 ? (editing ? router.push(next.href) : setStage("intro")) : go(index - 1))}
          className="h-11 rounded-xl px-4"
        >
          <ArrowLeft className="size-4" /> Back
        </Button>
        <span className="hidden flex-1 text-center text-xs text-muted-foreground sm:block">
          Every question is optional.
        </span>
        <Button
          onClick={() => (last ? finish() : go(index + 1))}
          disabled={sending}
          className="h-11 shrink-0 px-5"
        >
          {sending ? (
            "Saving…"
          ) : last ? (
            <>
              Finish <Check className="size-5" />
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

// One question: option cards, one pick or several. Tapping the picked card again clears it
// (skipping is always allowed).
function Question({
  q,
  hobbyLabel,
  value,
  onChange,
}: {
  q: SurveyQuestion;
  hobbyLabel?: string;
  value: string | string[] | undefined;
  onChange: (v: string | string[] | undefined) => void;
}) {
  const multi = q.type === "multi" || q.type === "hobby_multi";
  const picked = multi ? ((value as string[] | undefined) ?? []) : value ? [value as string] : [];
  const full = multi && q.max !== undefined && picked.length >= q.max;
  const prompt = q.prompt.replace("{hobby}", hobbyLabel ?? "it");

  function toggle(id: string) {
    if (multi) {
      if (picked.includes(id)) onChange(picked.filter((p) => p !== id));
      else if (!full) onChange([...picked, id]);
    } else {
      onChange(picked[0] === id ? undefined : id);
    }
  }

  return (
    <fieldset className="flex flex-col gap-3">
      <legend className="flex flex-col gap-1">
        <span className="text-lg font-semibold text-foreground">{prompt}</span>
        {q.help && <span className="text-sm font-normal text-muted-foreground">{q.help}</span>}
      </legend>
      <div className="grid gap-2.5 sm:grid-cols-2">
        {(q.options ?? []).map((o) => {
          const on = picked.includes(o.id);
          return (
            <button
              key={o.id}
              type="button"
              aria-pressed={on}
              disabled={!on && full}
              onClick={() => toggle(o.id)}
              className={cn(
                "relative flex items-center gap-3 rounded-2xl border p-3.5 text-left transition-all duration-150 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:opacity-40",
                on
                  ? "-translate-y-0.5 border-primary bg-[color-mix(in_srgb,var(--brand)_9%,var(--surface))] text-primary"
                  : "border-border bg-card hover:-translate-y-0.5 hover:border-[color-mix(in_srgb,var(--brand)_50%,var(--line))]",
              )}
            >
              {o.emoji && (
                <span aria-hidden className={cn("text-2xl", on && "rm-pop")}>
                  {o.emoji}
                </span>
              )}
              <span className="flex-1 text-sm font-medium leading-snug text-foreground">{o.label}</span>
              {on && (
                <span className="rm-pop flex size-5 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground">
                  <Check className="size-3" strokeWidth={3} aria-hidden />
                </span>
              )}
            </button>
          );
        })}
      </div>
    </fieldset>
  );
}

// What the student is told we'll do with their answers: concrete, and only things the app
// really does today (src/learner/survey.py: lesson_prefs, story_notes, order_hobbies).
export function whatWeHeard(
  t: SurveyTraits,
  labelOf: (id: string) => string,
  withNextStep = true,
): { emoji: string; text: string }[] {
  const out: { emoji: string; text: string }[] = [];
  const [hobby, info] = Object.entries(t.hobby_levels)[0] ?? [];
  if (hobby && info) {
    const name = labelOf(hobby);
    out.push(
      info.level === "novice"
        ? { emoji: "🌱", text: `New to ${name}? Your ${name} examples will use plain words and explain any terms.` }
        : info.level === "expert"
          ? { emoji: "🏆", text: `You know ${name} well, so your examples will use its real terms and skip the basics.` }
          : { emoji: "🎯", text: `Your examples will be built around ${name}, pitched at someone who knows it.` },
    );
  }
  if (t.focus.span === "short") {
    out.push({ emoji: "⏱️", text: "Lessons will come in small bites, with a nudge to stretch when you've been at it a while." });
  } else if (t.focus.span === "long") {
    out.push({ emoji: "🔭", text: "You can go deep: lessons won't interrupt you." });
  }
  if (t.learning.pace === "fast") {
    out.push({ emoji: "🚀", text: "Lessons will open on one page so you can move fast. You can switch to step by step any time." });
  } else if (t.learning.pace === "step_by_step") {
    out.push({ emoji: "🐢", text: "Lessons will go one idea at a time, with examples." });
  }
  if (t.learning.first_step === "try") {
    out.push({ emoji: "✏️", text: "You'll see the worked example before the explanation, so you can try it first." });
  }
  if (t.physics.feel === "nervous" || t.physics.feel === "dread") {
    out.push({ emoji: "💛", text: "Physics can feel like a lot. We'll keep it kind and small, one step at a time." });
  }
  if (withNextStep) {
    out.push({ emoji: "🧭", text: "Next, a short physics check. It has no marks: it just shows where to start." });
  }
  return out;
}
