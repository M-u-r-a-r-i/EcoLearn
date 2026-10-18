"use client";

// Direction B: Field Notes. A calm editorial notebook. Paper and ink, serif
// headings, hairline rules, no shadows, small stamps and highlighter marks.
// The roadmap is a contents page, not a game board.

import { ArrowLeft, ArrowRight, Check, Lock, Pencil, Star } from "lucide-react";
import { useState, type ReactNode } from "react";

import { Ring, usePv } from "@/components/preview/bits";
import type { ScreenProps, ScreenSet } from "@/components/preview/shell";
import { CHAPTER, CONCEPTS, CORRECT, INTERESTS, LESSON, LESSON_STEPS, OPTIONS, TEACHER, type NodeState } from "@/lib/mock/preview";

const rule = "border-pv-line";
const btn = "inline-flex items-center gap-2 rounded-[4px] border border-pv-ink bg-pv-ink px-5 py-2.5 font-semibold text-pv-bg transition-colors hover:bg-pv-accent hover:border-pv-accent hover:text-pv-accent-ink disabled:opacity-40";
const btnGhost = "inline-flex items-center gap-2 rounded-[4px] border border-pv-ink px-5 py-2.5 font-semibold text-pv-ink hover:bg-pv-surface2 disabled:opacity-40";
const hl = "bg-[linear-gradient(transparent_58%,var(--pv-gold)_58%,var(--pv-gold)_92%,transparent_92%)] px-0.5 text-pv-ink";
const kicker = "text-xs font-semibold uppercase tracking-[0.14em] text-pv-mute";

function Masthead({ right }: { right?: ReactNode }) {
  return (
    <header className={`flex items-baseline justify-between border-b-2 border-pv-ink pb-2 pt-5`}>
      <span className="font-pv-display text-2xl font-semibold tracking-tight">EcoLearn</span>
      <span className="text-sm text-pv-mute">{right}</span>
    </header>
  );
}

/* ------------------------------- Landing -------------------------------- */
function Landing({ interest }: ScreenProps) {
  const { setInterest } = usePv();
  return (
    <div className="mx-auto max-w-4xl px-4 pb-20">
      <Masthead right={<><a href="#" className="mr-4 underline">Log in</a><a href="#" className="underline">Sign up</a></>} />
      <section className="grid gap-10 py-12 md:grid-cols-[1.4fr_1fr]">
        <div className="pv-rise">
          <p className={kicker}>Physics for Class 11 and 12 · CBSE and ISC</p>
          <h1 className="mt-3 font-pv-display text-5xl font-medium leading-[1.08] sm:text-6xl">
            The physics you already know from <span className={hl}>{interest.label.toLowerCase()}</span>.
          </h1>
          <p className="mt-5 max-w-lg text-xl leading-relaxed text-pv-mute">
            EcoLearn teaches each idea through a story from your own hobby. A short starting check finds the mix-ups worth fixing, so you stop re-reading what you already understand.
          </p>
          <div className="mt-7 flex flex-wrap gap-3">
            <a href="#" className={btn}>Begin <ArrowRight size={18} aria-hidden /></a>
            <a href="#how" className={btnGhost}>How it works</a>
          </div>
        </div>
        <aside className="border-l-2 border-pv-accent pl-5">
          <p className={kicker}>From a {interest.label.toLowerCase()} lesson</p>
          <h2 className="mt-2 font-pv-display text-2xl">{interest.tagline}</h2>
          <p className="mt-2 leading-relaxed text-pv-mute">{interest.story}</p>
        </aside>
      </section>

      <section aria-label="Pick an interest" className={`border-y ${rule} py-5`}>
        <p className={kicker}>Choose your subject of interest</p>
        <div className="mt-3 flex flex-wrap gap-2">
          {INTERESTS.map((i) => (
            <button key={i.id} aria-pressed={i.id === interest.id} onClick={() => setInterest(i.id)}
              className={`rounded-full border px-4 py-2 font-semibold ${i.id === interest.id ? "border-pv-accent bg-pv-accent text-pv-accent-ink" : "border-pv-line hover:border-pv-ink"}`}>
              <span aria-hidden>{i.emoji}</span> {i.label}
            </button>
          ))}
        </div>
      </section>

      <section id="how" className="grid gap-8 py-12 md:grid-cols-3">
        {[
          ["i.", "A starting check", "Eight questions, no marks. A wrong answer names the mix-up behind it."],
          ["ii.", "A map that skips", "What you know is ticked off. What to fix is marked with a pencil."],
          ["iii.", "Lessons in your world", "Story, idea, a worked example you try first, where the picture breaks, one takeaway."],
        ].map(([n, t, d]) => (
          <div key={n}>
            <p className="font-pv-display text-3xl italic text-pv-accent">{n}</p>
            <h3 className="mt-1 font-pv-display text-xl">{t}</h3>
            <p className="mt-1 leading-relaxed text-pv-mute">{d}</p>
          </div>
        ))}
      </section>
      <p className="border-t border-pv-line pt-4 text-sm text-pv-mute">No email address is asked for. A username and a password are enough, and your teacher can reset it.</p>
    </div>
  );
}

/* ------------------------------- Roadmap -------------------------------- */
const MARK: Record<NodeState, { word: string; icon: ReactNode }> = {
  mastered: { word: "Mastered", icon: <Star size={18} fill="currentColor" aria-hidden /> },
  done: { word: "Done", icon: <Check size={18} aria-hidden /> },
  next: { word: "Next up", icon: <Pencil size={18} aria-hidden /> },
  open: { word: "Open", icon: <span aria-hidden className="block h-3 w-3 rounded-full border-2 border-current" /> },
  locked: { word: "Locked", icon: <Lock size={16} aria-hidden /> },
  soon: { word: "Coming soon", icon: <span aria-hidden className="text-xs">…</span> },
};

function Roadmap({ interest }: ScreenProps) {
  const [open, setOpen] = useState("c4");
  return (
    <div className="mx-auto max-w-3xl px-4 pb-20">
      <Masthead right={`${interest.emoji} ${interest.label} · ${CHAPTER.classLevel}`} />
      <div className="flex items-center gap-5 py-8">
        <Ring size={84} stroke={6} done={5} mastered={2} total={8} track="var(--pv-line)" doneColor="var(--pv-good)" goldColor="var(--pv-gold)">
          <span className="font-pv-display text-xl">5/8</span>
        </Ring>
        <div>
          <p className={kicker}>Chapter 4 of 7</p>
          <h1 className="font-pv-display text-4xl font-medium">{CHAPTER.name}</h1>
          <p className="text-pv-mute">3 done, 2 mastered, 2 still to open.</p>
        </div>
      </div>

      <ol className="border-t-2 border-pv-ink">
        {CONCEPTS.map((c, i) => {
          const m = MARK[c.state];
          const isOpen = open === c.id;
          const dim = c.state === "locked" || c.state === "soon";
          return (
            <li key={c.id} className={`border-b ${rule}`}>
              <button onClick={() => setOpen(isOpen ? "" : c.id)} aria-expanded={isOpen}
                className="flex w-full items-center gap-4 py-4 text-left">
                <span className="w-7 font-pv-display text-lg italic text-pv-mute">{i + 1}.</span>
                <span className={`flex-1 font-pv-display text-xl ${dim ? "text-pv-mute" : ""} ${c.state === "next" ? hl : ""}`}>{c.name}</span>
                <span className={`flex items-center gap-1.5 text-sm font-semibold ${c.state === "mastered" ? "text-pv-ink" : c.state === "done" ? "text-pv-good" : c.state === "next" ? "text-pv-accent" : "text-pv-mute"}`}>
                  {m.icon}{m.word}
                </span>
              </button>
              {isOpen && (
                <div className="pv-rise pb-5 pl-11">
                  <p className="leading-relaxed text-pv-mute">{c.note}</p>
                  {c.badge === "focus" && <p className="mt-1 text-sm"><Pencil size={14} className="mr-1 inline" aria-hidden />Your starting check showed a mix-up here. Worth fixing.</p>}
                  {c.badge === "known" && <p className="mt-1 text-sm"><Check size={14} className="mr-1 inline" aria-hidden />Your starting check says you know this.</p>}
                  {!dim && <button className={`${btn} mt-3`}>{c.state === "done" || c.state === "mastered" ? "Read again" : "Start"} <ArrowRight size={16} aria-hidden /></button>}
                </div>
              )}
            </li>
          );
        })}
      </ol>

      <div className="mt-8 grid gap-6 sm:grid-cols-2">
        <div className={`border ${rule} p-4`}><p className={kicker}>Revision</p><p className="mt-1 font-pv-display text-xl">One idea is ready for a fresh question.</p><a href="#" className="text-sm underline">Revise now</a></div>
        <div className={`border ${rule} p-4`}><p className={kicker}>End check</p><p className="mt-1 font-pv-display text-xl">Not open yet.</p><p className="text-sm text-pv-mute">Your teacher opens it near the end of the term.</p></div>
      </div>
    </div>
  );
}

/* -------------------------------- Lesson -------------------------------- */
function Lesson({ interest }: ScreenProps) {
  const [step, setStep] = useState(0);
  const [reveal, setReveal] = useState(false);
  const [orig, setOrig] = useState(false);
  const last = LESSON_STEPS.length - 1;
  const body: ReactNode[] = [
    <div key="s" className="space-y-6">
      <aside className="border-l-2 border-pv-accent bg-pv-soft px-4 py-3">
        <p className={kicker}>Your story · written by AI, then checked</p>
        <p className="mt-2 font-pv-display text-xl leading-relaxed">{interest.personal}</p>
        <p className="mt-2 text-sm"><button className="underline">Something wrong with this story?</button></p>
      </aside>
      <details open={orig} onToggle={(e) => setOrig(e.currentTarget.open)}>
        <summary className="cursor-pointer font-semibold underline">The original story</summary>
        <p className="mt-3 text-lg leading-relaxed">{interest.story}</p>
      </details>
      <figure className={`border ${rule} bg-pv-surface`}>
        <div className="grid h-40 place-items-center bg-pv-surface2 text-7xl" role="img" aria-label={interest.label}>{interest.emoji}</div>
        <figcaption className="px-3 py-2 text-sm italic text-pv-mute">Fig. 1. Same speed in, different stopping. Illustration.</figcaption>
      </figure>
    </div>,
    <div key="i" className="space-y-6">
      <p className="text-xl leading-relaxed">{LESSON.idea}</p>
      <p className={`border-y-2 border-pv-ink py-6 text-center font-pv-display text-6xl italic`}>{LESSON.equation}</p>
    </div>,
    <div key="w" className="space-y-5">
      <p className="text-xl leading-relaxed">{LESSON.example.prompt}</p>
      {!reveal ? <button onClick={() => setReveal(true)} className={btnGhost}>Have a go on paper, then show the working</button> : (
        <ol className="pv-rise space-y-2 border-l-2 border-pv-ink pl-4 font-pv-mono">{LESSON.example.steps.map((s) => <li key={s}>{s}</li>)}</ol>
      )}
    </div>,
    <p key="b" className="border-l-4 border-pv-bad pl-4 text-xl leading-relaxed">{LESSON.breaks}</p>,
    <p key="t" className="font-pv-display text-4xl leading-tight"><span className={hl}>{LESSON.takeaway}</span></p>,
    <div key="c" className="space-y-4"><p className="text-xl leading-relaxed">One question to see whether it landed. No marks. A wrong answer only shows what to fix.</p><button className={btn}>Start the check <ArrowRight size={18} aria-hidden /></button></div>,
  ];
  return (
    <div className="mx-auto max-w-2xl px-4 pb-24">
      <Masthead right={`${interest.emoji} ${LESSON.title}`} />
      <nav aria-label="Lesson steps" className="flex gap-1 pt-5">
        {LESSON_STEPS.map((s, i) => (
          <button key={s} onClick={() => setStep(i)} aria-label={s} aria-current={i === step ? "step" : undefined} className="group flex-1 py-2">
            <span className={`block h-1 ${i < step ? "bg-pv-ink" : i === step ? "bg-pv-accent" : "bg-pv-line"}`} />
          </button>
        ))}
      </nav>
      <p className={`${kicker} mt-4`}>Part {step + 1} of {LESSON_STEPS.length}</p>
      <h1 className="mt-1 font-pv-display text-4xl font-medium">{LESSON_STEPS[step]}</h1>
      <div key={step} className="rm-slide-next mt-6 min-h-[18rem]">{body[step]}</div>
      <div className={`mt-10 flex items-center justify-between border-t ${rule} pt-4`}>
        <button disabled={step === 0} onClick={() => setStep(step - 1)} className="flex items-center gap-2 font-semibold underline disabled:opacity-30"><ArrowLeft size={18} aria-hidden /> Back</button>
        <button disabled={step === last} onClick={() => setStep(step + 1)} className={btn}>{step < last ? LESSON_STEPS[step + 1] : "End"} <ArrowRight size={18} aria-hidden /></button>
      </div>
    </div>
  );
}

/* --------------------------------- Check -------------------------------- */
function CheckScreen({ interest }: ScreenProps) {
  const [pick, setPick] = useState<string | null>(null);
  const [sure, setSure] = useState<number | null>(null);
  const [done, setDone] = useState(false);
  const right = pick === CORRECT;
  const picked = OPTIONS.find((o) => o.key === pick);
  const correct = OPTIONS.find((o) => o.key === CORRECT)!;
  const LEVELS = ["Guessing", "Think so", "Sure"];
  if (done)
    return (
      <div className="mx-auto max-w-2xl px-4 pb-20">
        <Masthead right="Check · result" />
        <p className={`${kicker} mt-8`}>{right ? "Correct" : "Worth a second look"}</p>
        <h1 className="mt-2 font-pv-display text-5xl font-medium">{right ? <span className={hl}>That’s right.</span> : "Not quite, and that’s useful."}</h1>
        {!right && picked && <p className="mt-3 text-lg text-pv-mute">{picked.mix}. This is the thing to fix.</p>}
        <ul className="mt-8 border-t-2 border-pv-ink">
          {OPTIONS.map((o) => {
            const isRight = o.key === CORRECT, isPick = o.key === pick;
            return (
              <li key={o.key} className={`flex gap-3 border-b ${rule} py-3 ${!isRight && !isPick ? "text-pv-mute" : ""}`}>
                <span className="w-6 font-pv-display italic">{o.key.toLowerCase()}.</span>
                <span className={`flex-1 ${isRight ? "font-semibold" : ""} ${isPick && !isRight ? "line-through decoration-pv-bad decoration-2" : ""}`}>{o.text}</span>
                {isRight && <span className="flex items-center gap-1 text-sm font-semibold text-pv-good"><Check size={16} aria-hidden /> Right answer</span>}
                {isPick && !isRight && <span className="text-sm font-semibold text-pv-bad">Your pick</span>}
              </li>
            );
          })}
        </ul>
        <div className="mt-6 border-l-2 border-pv-accent pl-4"><p className={kicker}>Why</p><p className="mt-1 text-lg leading-relaxed">{correct.why}</p></div>
        {right && (
          <div className="mt-8"><p className={kicker}>Your road to mastered</p>
            <ol className="mt-3 grid grid-cols-3 border-y border-pv-line text-center">
              <li className="border-r border-pv-line py-3"><Check className="mx-auto text-pv-good" aria-hidden /><p className="mt-1 font-semibold">Right once</p><p className="text-sm text-pv-mute">today</p></li>
              <li className="border-r border-pv-line py-3"><p className="font-pv-display text-2xl italic text-pv-accent">1d</p><p className="font-semibold">A new question</p><p className="text-sm text-pv-mute">tomorrow</p></li>
              <li className="py-3 text-pv-mute"><Star className="mx-auto" aria-hidden /><p className="mt-1 font-semibold">Mastered</p><p className="text-sm">after two</p></li>
            </ol></div>
        )}
        <div className="mt-8 flex gap-3"><button className={btn}>{right ? "Back to the contents" : "Re-read the lesson"}</button><button className={btnGhost} onClick={() => { setDone(false); setPick(null); setSure(null); }}>{right ? "Again" : "Try again"}</button></div>
      </div>
    );
  return (
    <div className="mx-auto max-w-2xl px-4 pb-24">
      <Masthead right={`${interest.emoji} Check · ${LESSON.title}`} />
      <p className={`${kicker} mt-8`}>Question 1 of 1</p>
      <h1 className="mt-2 font-pv-display text-3xl font-medium leading-snug sm:text-4xl">{interest.stem}</h1>
      <div className="mt-6 border-t-2 border-pv-ink" role="radiogroup" aria-label="Answers">
        {OPTIONS.map((o) => (
          <button key={o.key} role="radio" aria-checked={pick === o.key} onClick={() => setPick(o.key)}
            className={`flex w-full items-start gap-4 border-b ${rule} px-2 py-4 text-left text-lg ${pick === o.key ? "bg-pv-soft" : "hover:bg-pv-surface2"}`}>
            <span className={`grid h-8 w-8 shrink-0 place-items-center rounded-full border font-pv-display italic ${pick === o.key ? "border-pv-ink bg-pv-ink text-pv-bg" : "border-pv-mute"}`}>{o.key.toLowerCase()}</span>
            <span className="pt-0.5">{o.text}</span>
          </button>
        ))}
        <button role="radio" aria-checked={pick === "?"} onClick={() => setPick("?")} className={`w-full border-b ${rule} px-2 py-3 text-left italic ${pick === "?" ? "bg-pv-soft" : "text-pv-mute hover:bg-pv-surface2"}`}>I’m not sure yet. That is an honest answer.</button>
      </div>
      {pick && (
        <div className="pv-rise mt-6">
          <p className={kicker}>How sure are you?</p>
          <div className="mt-2 flex" role="radiogroup" aria-label="How sure are you?">
            {LEVELS.map((l, i) => (
              <button key={l} role="radio" aria-checked={sure === i} onClick={() => setSure(i)}
                className={`flex-1 border py-2.5 font-semibold ${i > 0 ? "-ml-px" : ""} ${sure === i ? "z-10 border-pv-ink bg-pv-ink text-pv-bg" : "border-pv-mute hover:bg-pv-surface2"}`}>{l}</button>
            ))}
          </div>
        </div>
      )}
      <div className="mt-8 flex items-center gap-4">
        <button disabled={!pick || sure === null} onClick={() => setDone(true)} className={btn}>Check my answer</button>
        <span className="text-sm text-pv-mute">{!pick ? "Pick an answer." : sure === null ? "Then say how sure you are." : ""}</span>
      </div>
    </div>
  );
}

/* -------------------------------- Teacher ------------------------------- */
function Teacher(_: ScreenProps) {
  void _;
  const T = TEACHER;
  return (
    <div className="mx-auto max-w-5xl px-4 pb-20">
      <Masthead right="Teacher · Ms Nair" />
      <p className={`${kicker} mt-8`}>Class report</p>
      <h1 className="font-pv-display text-4xl font-medium">{T.className}</h1>
      <div className="mt-6 grid grid-cols-2 border-y-2 border-pv-ink md:grid-cols-4">
        {T.tiles.map((t, i) => (
          <div key={t.label} className={`px-4 py-4 ${i > 0 ? "md:border-l md:border-pv-line" : ""}`}>
            <p className={kicker}>{t.label}</p>
            <p className="mt-1 font-pv-display text-3xl">{t.value}</p>
            <p className="text-sm text-pv-mute">{t.sub}</p>
          </div>
        ))}
      </div>
      <div className="mt-10 grid gap-10 md:grid-cols-2">
        <section>
          <h2 className="font-pv-display text-2xl">Studied and not studied</h2>
          <p className="text-sm text-pv-mute">Right answers, start → end. A rough comparison, not a trial.</p>
          <table className="mt-3 w-full text-left"><tbody>
            {T.compare.map((c) => (
              <tr key={c.label} className={`border-t ${rule}`}><th className="py-2 font-semibold">{c.label}</th><td className="font-pv-mono">{c.before}% → <span className={hl}>{c.after}%</span></td></tr>
            ))}</tbody></table>
        </section>
        <section>
          <h2 className="font-pv-display text-2xl">Common mix-ups</h2>
          <ol className="mt-3">{T.misconceptions.map((m, i) => (
            <li key={m.name} className={`flex items-baseline gap-3 border-t ${rule} py-2`}><span className="font-pv-display italic text-pv-mute">{i + 1}.</span><span className="flex-1 font-semibold">{m.name}</span><span className="text-sm text-pv-mute">{m.count} students, {m.sure} sure</span></li>
          ))}</ol>
        </section>
      </div>
      <section className="mt-10 border-l-2 border-pv-accent bg-pv-soft px-5 py-4">
        <p className={kicker}>Teaching assistant · AI-written plan</p>
        <ol className="mt-2 list-decimal space-y-1 pl-5 text-lg">{T.plan.map((p) => <li key={p}>{p}</li>)}</ol>
      </section>
      <section className="mt-10">
        <h2 className="font-pv-display text-2xl">How the AI decided</h2>
        <p className="text-sm text-pv-mute">Each personal story is drafted, checked by rules, then by a second model, and only then shown.</p>
        <p className="mt-3 text-lg leading-relaxed">Of <b>{T.ai.drafts}</b> drafts, <b>{T.ai.rule}</b> failed the rule check and <b>{T.ai.critic}</b> were turned down by the critic. <b>{T.ai.human}</b> went to a person. <b>{T.ai.shown}</b> reached students.</p>
      </section>
      <section className="mt-10 overflow-x-auto">
        <h2 className="font-pv-display text-2xl">Students</h2>
        <table className="mt-2 w-full text-left"><thead className={kicker}><tr><th className="py-2">Name</th><th>Done</th><th>Mix-ups</th><th /></tr></thead>
          <tbody>{T.students_list.map((s) => (
            <tr key={s.name} className={`border-t ${rule}`}><td className="py-2.5 font-semibold">{s.name}</td><td>{s.done} of 8</td><td>{s.mixups}</td><td className="text-right"><button className="text-sm underline">Reset password</button></td></tr>
          ))}</tbody></table>
      </section>
    </div>
  );
}

export const screensB: ScreenSet = { landing: Landing, roadmap: Roadmap, lesson: Lesson, check: CheckScreen, teacher: Teacher };
