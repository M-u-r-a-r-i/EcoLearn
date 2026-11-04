"use client";

// Direction A: Trailhead. A playful game map. Chunky rounded shapes, pressable
// buttons with a hard lower edge, springy motion, loud use of the interest hue.

import {
  ArrowLeft, ArrowRight, Check, ChevronDown, Flag, Hourglass, Lightbulb, Lock, Play, ShieldCheck, Sparkles, Star, Trophy, X,
} from "lucide-react";
import { useState, type ReactNode } from "react";

import { Confetti, Ring, usePv } from "@/components/preview/bits";
import type { ScreenProps, ScreenSet } from "@/components/preview/shell";
import {
  CHAPTER, CONCEPTS, CORRECT, INTERESTS, LESSON, LESSON_STEPS, OPTIONS, TEACHER, type MockConcept, type NodeState,
} from "@/lib/mock/preview";

const press =
  "font-pv-display font-semibold rounded-2xl px-6 py-3 text-lg transition-transform active:translate-y-[3px] active:shadow-none disabled:opacity-50 disabled:active:translate-y-0";
const btnPrimary = `${press} bg-pv-accent text-pv-accent-ink shadow-[0_4px_0_0_color-mix(in_oklab,var(--pv-accent),black_40%)]`;
const btnQuiet = `${press} bg-pv-surface text-pv-ink border-2 border-pv-line shadow-[0_4px_0_0_var(--pv-line)]`;
const card = "rounded-3xl border-2 border-pv-line bg-pv-surface";

function Wordmark() {
  return (
    <span className="font-pv-display text-2xl font-bold text-pv-ink">
      Eco<span className="text-pv-accent">Learn</span>
    </span>
  );
}

/* ------------------------------- Landing -------------------------------- */
function Landing({ interest }: ScreenProps) {
  const { setInterest } = usePv();
  return (
    <div className="mx-auto max-w-5xl px-4 pb-16">
      <header className="flex items-center justify-between py-4">
        <Wordmark />
        <div className="flex gap-2">
          <a className="px-3 py-2 font-bold text-pv-ink" href="#">Log in</a>
          <a className="hidden rounded-xl bg-pv-accent px-4 py-2 font-bold text-pv-accent-ink sm:block" href="#">Sign up</a>
        </div>
      </header>

      <section className="grid items-center gap-8 py-8 md:grid-cols-2">
        <div className="pv-rise">
          <p className="mb-3 inline-block rounded-full bg-pv-soft px-3 py-1 text-sm font-bold text-pv-ink">
            Class 11 and 12 Physics · CBSE and ISC
          </p>
          <h1 className="font-pv-display text-5xl font-bold leading-[1.05] sm:text-6xl">
            Physics, through <span className="text-pv-accent">{interest.label.toLowerCase()}</span>.
          </h1>
          <p className="mt-4 max-w-md text-lg text-pv-mute">
            Pick what you love. Every lesson starts with a story from your world. A five minute check shows what to fix, and your map skips what you already know.
          </p>
          <div className="mt-6 flex flex-wrap gap-3">
            <a href="#" className={btnPrimary}>Start free</a>
            <a href="#how" className={btnQuiet}>How it works</a>
          </div>
        </div>
        <div className={`${card} relative p-5`}>
          <span className="pv-float absolute -right-2 -top-5 text-6xl" aria-hidden>{interest.emoji}</span>
          <p className="text-sm font-bold uppercase tracking-wide text-pv-accent">Lesson · {interest.label}</p>
          <h2 className="mt-1 font-pv-display text-2xl font-semibold">{interest.tagline}</h2>
          <p className="mt-2 text-pv-mute">{interest.story}</p>
          <div className="mt-4 flex gap-1.5" aria-hidden>
            {[1, 1, 1, 0, 0, 0].map((d, i) => (
              <span key={i} className={`h-2.5 flex-1 rounded-full ${d ? "bg-pv-good" : "bg-pv-surface2"}`} />
            ))}
          </div>
        </div>
      </section>

      <section aria-label="Pick an interest" className="py-6">
        <h2 className="font-pv-display text-2xl font-semibold">What do you love?</h2>
        <div className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-5">
          {INTERESTS.map((i) => (
            <button
              key={i.id}
              onClick={() => setInterest(i.id)}
              aria-pressed={i.id === interest.id}
              className={`flex flex-col items-center gap-1 rounded-3xl border-2 p-4 font-pv-display text-lg font-semibold transition-transform active:translate-y-0.5 ${
                i.id === interest.id ? "border-pv-accent bg-pv-soft shadow-[0_4px_0_0_var(--pv-accent)]" : "border-pv-line bg-pv-surface shadow-[0_4px_0_0_var(--pv-line)]"
              }`}
            >
              <span className="text-3xl" aria-hidden>{i.emoji}</span>
              {i.label}
            </button>
          ))}
        </div>
      </section>

      <section id="how" className="grid gap-4 py-8 md:grid-cols-3">
        {[
          ["1", "Starting check", "Eight quick questions. No marks. Every wrong answer points at one mix-up to fix."],
          ["2", "Your map", "Concepts open in order. What you already know gets a tick, what to fix gets a flag."],
          ["3", "Lessons in your world", "Story, idea, worked example, then a check. About six minutes each."],
        ].map(([n, t, d]) => (
          <div key={n} className={`${card} p-5`}>
            <span className="grid h-10 w-10 place-items-center rounded-full bg-pv-accent font-pv-display text-xl font-bold text-pv-accent-ink">{n}</span>
            <h3 className="mt-3 font-pv-display text-xl font-semibold">{t}</h3>
            <p className="mt-1 text-pv-mute">{d}</p>
          </div>
        ))}
      </section>

      <p className="flex items-center gap-2 rounded-2xl bg-pv-surface2 p-4 text-pv-ink">
        <ShieldCheck className="shrink-0 text-pv-good" aria-hidden />
        No email needed. Just a username and password. Your teacher can reset it if you forget.
      </p>
    </div>
  );
}

/* ------------------------------- Roadmap -------------------------------- */
const NODE_X = [50, 74, 58, 30, 24, 46, 72, 56];
const ROW = 104;

function nodeLook(state: NodeState) {
  switch (state) {
    case "mastered": return { cls: "bg-pv-gold text-pv-gold-ink border-pv-gold", icon: <Trophy aria-hidden /> , word: "Mastered" };
    case "done": return { cls: "bg-pv-good text-pv-bg border-pv-good", icon: <Check aria-hidden strokeWidth={3} />, word: "Done" };
    case "next": return { cls: "bg-pv-accent text-pv-accent-ink border-pv-accent pv-pulse", icon: <Play aria-hidden fill="currentColor" />, word: "Next up" };
    case "open": return { cls: "bg-pv-surface text-pv-accent border-pv-accent", icon: <Star aria-hidden />, word: "Open" };
    case "locked": return { cls: "bg-pv-surface2 text-pv-mute border-pv-line", icon: <Lock aria-hidden />, word: "Locked" };
    default: return { cls: "bg-pv-surface text-pv-mute border-dashed border-pv-mute", icon: <Hourglass aria-hidden />, word: "Coming soon" };
  }
}

function Roadmap({ interest }: ScreenProps) {
  const [sel, setSel] = useState<MockConcept>(CONCEPTS[3]);
  const h = CONCEPTS.length * ROW;
  const pts = NODE_X.map((x, i) => [x * 3.6, i * ROW + ROW / 2] as const);
  const d = pts.map(([x, y], i) => (i === 0 ? `M${x} ${y}` : `C${pts[i - 1][0]} ${y - ROW / 2} ${x} ${y - ROW / 2} ${x} ${y}`)).join(" ");
  const look = nodeLook(sel.state);
  return (
    <div className="mx-auto max-w-md px-4 pb-44">
      <header className="flex items-center justify-between py-3">
        <Wordmark />
        <button className="rounded-full bg-pv-surface2 px-3 py-1.5 font-bold" aria-label={`Change chapter, now ${CHAPTER.name}`}>
          {interest.emoji} {CHAPTER.classLevel} <ChevronDown className="inline" size={16} aria-hidden />
        </button>
      </header>

      <div className={`${card} flex items-center gap-4 p-4`}>
        <Ring done={5} mastered={2} total={8} track="var(--pv-surface2)" doneColor="var(--pv-good)" goldColor="var(--pv-gold)">
          <span className="font-pv-display text-lg font-bold">5/8</span>
        </Ring>
        <div>
          <h1 className="font-pv-display text-2xl font-bold leading-tight">{CHAPTER.name}</h1>
          <p className="text-pv-mute">3 done · 2 mastered · 2 to unlock</p>
        </div>
      </div>

      <div className="mt-3 grid grid-cols-2 gap-3">
        <div className="rounded-2xl bg-pv-soft p-3">
          <p className="font-pv-display font-semibold">Revision</p>
          <p className="text-sm text-pv-mute">1 idea ready for a fresh question</p>
        </div>
        <div className="rounded-2xl bg-pv-surface2 p-3">
          <p className="font-pv-display font-semibold">End check</p>
          <p className="text-sm text-pv-mute">Your teacher hasn’t opened it yet</p>
        </div>
      </div>

      <div className="relative mt-4" style={{ height: h }}>
        <svg viewBox={`0 0 360 ${h}`} className="absolute inset-0 h-full w-full" aria-hidden preserveAspectRatio="none">
          <path d={d} fill="none" stroke="var(--pv-line)" strokeWidth="8" strokeDasharray="2 14" strokeLinecap="round" />
        </svg>
        {CONCEPTS.map((c, i) => {
          const lk = nodeLook(c.state);
          return (
            <div key={c.id} className="absolute -translate-x-1/2 -translate-y-1/2 text-center" style={{ left: `${NODE_X[i]}%`, top: i * ROW + ROW / 2 }}>
              {c.state === "next" && <span className="rm-bob absolute -top-7 left-1/2 -translate-x-1/2 rounded-lg bg-pv-ink px-2 py-0.5 text-xs font-bold text-pv-bg">START</span>}
              <button
                onClick={() => setSel(c)}
                aria-label={`${c.name}, ${lk.word}`}
                aria-pressed={sel.id === c.id}
                className={`grid h-[68px] w-[68px] place-items-center rounded-full border-4 shadow-[0_5px_0_0_rgb(0_0_0/0.18)] transition-transform active:translate-y-1 ${lk.cls} ${sel.id === c.id ? "scale-110 ring-4 ring-pv-ink/20" : ""}`}
              >
                <span className="[&>svg]:h-7 [&>svg]:w-7">{lk.icon}</span>
              </button>
              <p className="mx-auto mt-1.5 max-w-[110px] text-sm font-bold leading-tight">{c.name}</p>
            </div>
          );
        })}
      </div>

      <div className="fixed inset-x-0 bottom-0 z-20 px-4 pb-4">
        <div className={`${card} rm-sheet mx-auto max-w-md p-4 shadow-xl`} role="region" aria-label="Selected concept">
          <div className="flex items-center gap-2">
            <span className="rounded-full bg-pv-soft px-2.5 py-0.5 text-sm font-bold">{look.word}</span>
            {sel.badge === "known" && <span className="rounded-full bg-pv-good/15 px-2.5 py-0.5 text-sm font-bold text-pv-good">Know it?</span>}
            {sel.badge === "focus" && <span className="rounded-full bg-pv-gold/40 px-2.5 py-0.5 text-sm font-bold">Focus</span>}
          </div>
          <h2 className="mt-1 font-pv-display text-xl font-semibold">{sel.name}</h2>
          <p className="text-pv-mute">{sel.note}</p>
          <button disabled={sel.state === "locked" || sel.state === "soon"} className={`${btnPrimary} mt-3 w-full`}>
            {sel.state === "done" ? "Review" : sel.state === "mastered" ? "Read again" : sel.state === "locked" ? "Locked" : sel.state === "soon" ? "Coming soon" : "Start"}
          </button>
        </div>
      </div>
    </div>
  );
}

/* -------------------------------- Lesson -------------------------------- */
function Lesson({ interest }: ScreenProps) {
  const [step, setStep] = useState(0);
  const [dir, setDir] = useState<"next" | "prev">("next");
  const [reveal, setReveal] = useState(false);
  const [orig, setOrig] = useState(false);
  const go = (n: number) => { setDir(n > step ? "next" : "prev"); setStep(n); };
  const last = LESSON_STEPS.length - 1;

  const body: ReactNode[] = [
    <div key="s" className="space-y-4">
      <div className="rounded-3xl border-2 border-pv-accent bg-pv-soft p-4">
        <p className="flex items-center gap-1.5 text-sm font-bold"><Sparkles size={16} aria-hidden /> Your story · written by AI and checked</p>
        <p className="mt-2 text-lg">{interest.personal}</p>
        <button className="mt-2 text-sm font-bold underline">Something wrong with this story?</button>
      </div>
      <button onClick={() => setOrig(!orig)} aria-expanded={orig} className="flex w-full items-center justify-between rounded-2xl bg-pv-surface2 px-4 py-3 text-left font-bold">
        The original story <ChevronDown className={orig ? "rotate-180" : ""} aria-hidden />
      </button>
      {orig && <p className="px-1 text-lg">{interest.story}</p>}
      <figure className="grid h-36 place-items-center rounded-3xl bg-pv-surface2 text-7xl" aria-label={`Picture: ${interest.label}`}>{interest.emoji}</figure>
    </div>,
    <div key="i" className="space-y-4">
      <p className="text-lg">{LESSON.idea}</p>
      <p className="rounded-3xl bg-pv-surface2 py-6 text-center font-pv-display text-5xl font-bold text-pv-accent">{LESSON.equation}</p>
    </div>,
    <div key="w" className="space-y-4">
      <p className="text-lg">{LESSON.example.prompt}</p>
      {!reveal ? (
        <button onClick={() => setReveal(true)} className={btnQuiet}>Have a go, then show the working</button>
      ) : (
        <ol className="rm-sheet space-y-2">
          {LESSON.example.steps.map((s, i) => (
            <li key={i} className="rounded-2xl bg-pv-surface2 px-4 py-3 font-bold">{s}</li>
          ))}
        </ol>
      )}
    </div>,
    <div key="b" className="rounded-3xl border-2 border-dashed border-pv-bad p-4">
      <p className="flex items-center gap-2 font-pv-display text-xl font-semibold"><Flag className="text-pv-bad" aria-hidden /> Watch out</p>
      <p className="mt-2 text-lg">{LESSON.breaks}</p>
    </div>,
    <div key="t" className="rounded-3xl bg-pv-gold p-5 text-pv-gold-ink">
      <p className="flex items-center gap-2 font-pv-display text-xl font-semibold"><Lightbulb aria-hidden /> Remember this</p>
      <p className="mt-2 font-pv-display text-3xl font-bold">{LESSON.takeaway}</p>
    </div>,
    <div key="c" className="space-y-3 text-center">
      <p className="text-6xl" aria-hidden>🎯</p>
      <p className="font-pv-display text-2xl font-semibold">Ready for one question?</p>
      <p className="text-pv-mute">No marks. A wrong answer just shows what to fix.</p>
    </div>,
  ];

  return (
    <div className="mx-auto flex min-h-[100dvh] max-w-xl flex-col px-4">
      <div className="flex items-center gap-3 py-4">
        <button aria-label="Back to the map" className="rounded-full p-2 hover:bg-pv-surface2"><X aria-hidden /></button>
        <div className="flex flex-1 gap-1.5" role="list" aria-label="Lesson steps">
          {LESSON_STEPS.map((s, i) => (
            <button key={s} role="listitem" onClick={() => go(i)} aria-label={`${s}${i < step ? ", finished" : ""}`} aria-current={i === step ? "step" : undefined}
              className={`h-3 flex-1 rounded-full ${i < step ? "bg-pv-good" : i === step ? "bg-pv-accent" : "bg-pv-surface2"}`} />
          ))}
        </div>
      </div>
      <p className="font-bold text-pv-accent">{interest.emoji} Step {step + 1} of {LESSON_STEPS.length}</p>
      <h1 className="font-pv-display text-4xl font-bold">{LESSON_STEPS[step]}</h1>
      <div key={step} className={`mt-4 flex-1 pb-28 ${dir === "next" ? "rm-slide-next" : "rm-slide-prev"}`}>{body[step]}</div>
      <div className="fixed inset-x-0 bottom-0 border-t-2 border-pv-line bg-pv-bg/95 px-4 py-3 backdrop-blur">
        <div className="mx-auto flex max-w-xl gap-3">
          <button onClick={() => go(Math.max(0, step - 1))} disabled={step === 0} className={btnQuiet} aria-label="Back"><ArrowLeft aria-hidden /></button>
          <button onClick={() => go(Math.min(last, step + 1))} className={`${btnPrimary} flex-1`}>
            {step === last ? "Start the check" : `Next: ${LESSON_STEPS[step + 1]}`} <ArrowRight className="inline" size={20} aria-hidden />
          </button>
        </div>
      </div>
    </div>
  );
}

/* --------------------------------- Check -------------------------------- */
const SURE = ["Sure", "Think so", "Guessing"] as const;

function CheckScreen({ interest }: ScreenProps) {
  const [pick, setPick] = useState<string | null>(null);
  const [sure, setSure] = useState<string | null>(null);
  const [done, setDone] = useState(false);
  const right = pick === CORRECT;
  const picked = OPTIONS.find((o) => o.key === pick);

  if (done) {
    return (
      <div className="relative mx-auto max-w-xl px-4 pb-16 pt-8">
        {right && <Confetti colors={["var(--pv-gold)", "var(--pv-accent)", "var(--pv-good)"]} />}
        <div className="text-center">
          <div className={`rm-pop mx-auto grid h-24 w-24 place-items-center rounded-full ${right ? "bg-pv-good text-pv-bg" : "bg-pv-gold text-pv-gold-ink"}`}>
            {right ? <Check size={56} strokeWidth={3} aria-hidden /> : <Lightbulb size={52} aria-hidden />}
          </div>
          <h1 className="mt-4 font-pv-display text-4xl font-bold">{right ? "Right!" : "Not quite, and that’s useful"}</h1>
          {!right && picked && <p className="mt-1 text-lg text-pv-mute">{picked.mix}. Let’s fix that.</p>}
        </div>
        <div className="mt-6 space-y-2">
          {OPTIONS.map((o) => {
            const isRight = o.key === CORRECT, isPick = o.key === pick;
            return (
              <div key={o.key} className={`flex items-start gap-3 rounded-2xl border-2 p-3 ${isRight ? "border-pv-good bg-pv-good/10" : isPick ? "border-pv-bad bg-pv-bad/10" : "border-pv-line opacity-70"}`}>
                <span className="mt-0.5 grid h-7 w-7 shrink-0 place-items-center rounded-full bg-pv-surface2 font-bold">{o.key}</span>
                <span className="flex-1">{o.text}</span>
                {isRight && <span className="flex items-center gap-1 font-bold text-pv-good"><Check size={18} aria-hidden /> Right answer</span>}
                {isPick && !isRight && <span className="flex items-center gap-1 font-bold text-pv-bad"><X size={18} aria-hidden /> Your pick</span>}
              </div>
            );
          })}
        </div>
        <div className={`${card} mt-4 p-4`}>
          <p className="font-pv-display text-lg font-semibold">Why</p>
          <p>{OPTIONS.find((o) => o.key === CORRECT)!.why}</p>
        </div>
        {right ? (
          <div className={`${card} mt-4 p-4`}>
            <p className="font-pv-display text-lg font-semibold">Your road to mastered</p>
            <ol className="mt-3 flex items-center justify-between text-center text-sm font-bold">
              <li className="flex-1"><span className="mx-auto grid h-10 w-10 place-items-center rounded-full bg-pv-good text-pv-bg"><Check aria-hidden /></span>Right once</li>
              <li className="flex-1"><span className="mx-auto grid h-10 w-10 place-items-center rounded-full border-2 border-dashed border-pv-accent text-pv-accent">1d</span>New question tomorrow</li>
              <li className="flex-1"><span className="mx-auto grid h-10 w-10 place-items-center rounded-full bg-pv-surface2 text-pv-mute"><Trophy aria-hidden /></span>Mastered</li>
            </ol>
          </div>
        ) : null}
        <div className="mt-5 flex gap-3">
          <button onClick={() => { setDone(false); setPick(null); setSure(null); }} className={`${btnQuiet} flex-1`}>{right ? "Again" : "Try again"}</button>
          <button className={`${btnPrimary} flex-1`}>{right ? "Back to the map" : "Re-read the lesson"}</button>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-xl px-4 pb-32">
      <div className="flex items-center gap-3 py-4">
        <button aria-label="Close" className="rounded-full p-2 hover:bg-pv-surface2"><X aria-hidden /></button>
        <span className="font-bold text-pv-accent">{interest.emoji} Check · Newton’s second law</span>
      </div>
      <h1 className="font-pv-display text-3xl font-bold leading-tight">{interest.stem}</h1>
      <div className="mt-5 space-y-3" role="radiogroup" aria-label="Answers">
        {OPTIONS.map((o) => (
          <button key={o.key} role="radio" aria-checked={pick === o.key} onClick={() => setPick(o.key)}
            className={`flex w-full items-center gap-3 rounded-2xl border-2 p-4 text-left text-lg transition-transform active:translate-y-0.5 ${pick === o.key ? "border-pv-accent bg-pv-soft shadow-[0_4px_0_0_var(--pv-accent)]" : "border-pv-line bg-pv-surface shadow-[0_4px_0_0_var(--pv-line)]"}`}>
            <span className={`grid h-9 w-9 shrink-0 place-items-center rounded-xl font-pv-display text-lg font-bold ${pick === o.key ? "bg-pv-accent text-pv-accent-ink" : "bg-pv-surface2"}`}>{o.key}</span>
            {o.text}
          </button>
        ))}
        <button role="radio" aria-checked={pick === "?"} onClick={() => setPick("?")}
          className={`w-full rounded-2xl border-2 border-dashed p-3 text-pv-mute ${pick === "?" ? "border-pv-accent bg-pv-soft text-pv-ink" : "border-pv-line"}`}>
          I’m not sure yet. That’s a fine answer.
        </button>
      </div>
      {pick && (
        <div className="rm-sheet mt-5">
          <p className="font-pv-display text-lg font-semibold">How sure are you?</p>
          <div className="mt-2 grid grid-cols-3 gap-2">
            {SURE.map((s) => (
              <button key={s} onClick={() => setSure(s)} aria-pressed={sure === s}
                className={`rounded-xl border-2 py-2.5 font-bold ${sure === s ? "border-pv-accent bg-pv-accent text-pv-accent-ink" : "border-pv-line bg-pv-surface"}`}>{s}</button>
            ))}
          </div>
        </div>
      )}
      <div className="fixed inset-x-0 bottom-0 border-t-2 border-pv-line bg-pv-bg/95 px-4 py-3 backdrop-blur">
        <div className="mx-auto flex max-w-xl items-center gap-3">
          <p className="flex-1 text-sm text-pv-mute">{!pick ? "Pick an answer" : !sure ? "Now say how sure you are" : "Ready"}</p>
          <button disabled={!pick || !sure} onClick={() => setDone(true)} className={btnPrimary}>Check</button>
        </div>
      </div>
    </div>
  );
}

/* -------------------------------- Teacher ------------------------------- */
function Teacher(_: ScreenProps) {
  void _;
  const T = TEACHER;
  const steps: [string, number][] = [["Drafts", T.ai.drafts], ["Rule check", T.ai.drafts - T.ai.rule], ["Critic", T.ai.drafts - T.ai.rule - T.ai.critic], ["Shown", T.ai.shown]];
  return (
    <div className="mx-auto max-w-5xl px-4 pb-16">
      <header className="flex items-center justify-between py-4"><Wordmark /><span className="font-bold">Teacher · Ms Nair</span></header>
      <h1 className="font-pv-display text-4xl font-bold">{T.className}</h1>
      <p className="text-pv-mute">{T.students} students · end check is open</p>

      <div className="mt-4 grid grid-cols-2 gap-3 md:grid-cols-4">
        {T.tiles.map((t, i) => (
          <div key={t.label} className={`${card} p-4 ${i === 2 ? "bg-pv-soft" : ""}`}>
            <p className="text-sm font-bold text-pv-mute">{t.label}</p>
            <p className="font-pv-display text-3xl font-bold">{t.value}</p>
            <p className="text-sm text-pv-mute">{t.sub}</p>
          </div>
        ))}
      </div>

      <div className="mt-4 grid gap-4 md:grid-cols-2">
        <section className={`${card} p-4`}>
          <h2 className="font-pv-display text-xl font-semibold">Studied vs not studied</h2>
          <p className="text-sm text-pv-mute">Right answers, start then end. A rough comparison, not a trial.</p>
          {T.compare.map((c) => (
            <div key={c.label} className="mt-3">
              <p className="font-bold">{c.label}</p>
              <div className="mt-1 h-3 rounded-full bg-pv-surface2"><div className="h-3 rounded-full bg-pv-line" style={{ width: `${c.before}%` }} /></div>
              <div className="mt-1 h-3 rounded-full bg-pv-surface2"><div className="h-3 rounded-full bg-pv-accent" style={{ width: `${c.after}%` }} /></div>
              <p className="text-sm text-pv-mute">{c.before}% → {c.after}%</p>
            </div>
          ))}
        </section>
        <section className={`${card} p-4`}>
          <h2 className="font-pv-display text-xl font-semibold">Most common mix-ups</h2>
          <ul className="mt-2 space-y-2">
            {T.misconceptions.map((m) => (
              <li key={m.name} className="flex items-center justify-between rounded-xl bg-pv-surface2 px-3 py-2">
                <span className="font-bold">{m.name}</span>
                <span className="text-sm">{m.count} students · {m.sure} were sure</span>
              </li>
            ))}
          </ul>
        </section>
      </div>

      <section className={`${card} mt-4 p-4`}>
        <h2 className="flex items-center gap-2 font-pv-display text-xl font-semibold"><Sparkles aria-hidden /> Teaching assistant <span className="rounded-full bg-pv-soft px-2 py-0.5 text-xs font-bold">AI plan</span></h2>
        <ol className="mt-2 list-decimal space-y-1 pl-5">{T.plan.map((p) => <li key={p}>{p}</li>)}</ol>
        <button className={`${btnQuiet} mt-3 !py-2 !text-base`}>Plan again</button>
      </section>

      <section className={`${card} mt-4 p-4`}>
        <h2 className="font-pv-display text-xl font-semibold">How the AI decided</h2>
        <p className="text-sm text-pv-mute">Every personal story passes these steps before a student sees it.</p>
        <div className="mt-3 grid grid-cols-4 gap-2 text-center">
          {steps.map(([l, n]) => (
            <div key={l} className="rounded-2xl bg-pv-surface2 p-2"><p className="font-pv-display text-2xl font-bold">{n}</p><p className="text-xs font-bold">{l}</p></div>
          ))}
        </div>
        <p className="mt-2 text-sm text-pv-mute">{T.ai.rule} dropped by the rule check, {T.ai.critic} by the critic, {T.ai.human} sent to a person.</p>
      </section>

      <section className={`${card} mt-4 overflow-x-auto p-4`}>
        <h2 className="font-pv-display text-xl font-semibold">Students</h2>
        <table className="mt-2 w-full text-left">
          <thead className="text-sm text-pv-mute"><tr><th className="py-1">Name</th><th>Done</th><th>Mix-ups</th><th /></tr></thead>
          <tbody>
            {T.students_list.map((s) => (
              <tr key={s.name} className="border-t border-pv-line"><td className="py-2 font-bold">{s.name}</td><td>{s.done} of 8</td><td>{s.mixups}</td>
                <td className="text-right"><button className="rounded-lg bg-pv-surface2 px-3 py-1 text-sm font-bold">Reset password</button></td></tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}

export const screensA: ScreenSet = { landing: Landing, roadmap: Roadmap, lesson: Lesson, check: CheckScreen, teacher: Teacher };
