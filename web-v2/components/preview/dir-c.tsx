"use client";

// Direction C: Matchday. A sports-broadcast look. Black slabs with angled
// corners, condensed italic caps, mono scoreboard numbers, neon team colour.
// The roadmap is a fixture list; the result screen is an "instant replay".

import { ArrowLeft, ArrowRight, Check, Lock, Play, Radio, Timer, Trophy, X } from "lucide-react";
import { useState, type ReactNode } from "react";

import { Confetti, usePv } from "@/components/preview/bits";
import type { ScreenProps, ScreenSet } from "@/components/preview/shell";
import { CHAPTER, CONCEPTS, CORRECT, INTERESTS, LESSON, LESSON_STEPS, OPTIONS, TEACHER, type NodeState } from "@/lib/mock/preview";

const disp = "font-pv-display font-extrabold uppercase italic tracking-tight";
const slab = "pv-cut bg-pv-slab text-pv-slab-ink";
const btn = `${disp} pv-cut-sm inline-flex items-center gap-2 bg-pv-accent px-6 py-3 text-xl text-pv-accent-ink transition-transform hover:-translate-y-0.5 disabled:opacity-40 disabled:hover:translate-y-0`;
const btnQuiet = `${disp} pv-cut-sm inline-flex items-center gap-2 bg-pv-surface2 px-6 py-3 text-xl text-pv-ink hover:bg-pv-line disabled:opacity-40`;
const label = "font-pv-mono text-xs font-bold uppercase tracking-widest text-pv-mute";

function Bar({ right }: { right?: ReactNode }) {
  return (
    <header className="flex items-center justify-between bg-pv-slab px-4 py-3 text-pv-bg">
      <span className={`${disp} text-2xl`}>Eco<span className="text-pv-accent">Learn</span></span>
      <span className="font-pv-mono text-sm">{right}</span>
    </header>
  );
}

function Ticker({ items }: { items: string[] }) {
  const row = [...items, ...items];
  return (
    <div className="overflow-hidden bg-pv-accent py-1.5 text-pv-accent-ink" aria-hidden>
      <div className="pv-tick flex w-max gap-10 whitespace-nowrap font-pv-mono text-sm font-bold uppercase">
        {row.map((t, i) => <span key={i}>● {t}</span>)}
      </div>
    </div>
  );
}

/* ------------------------------- Landing -------------------------------- */
function Landing({ interest }: ScreenProps) {
  const { setInterest } = usePv();
  return (
    <div>
      <Bar right={<><a href="#" className="mr-4">LOG IN</a><a href="#" className="text-pv-accent">SIGN UP</a></>} />
      <Ticker items={["Class 11 + 12 Physics", "CBSE + ISC", "5 interests", "Story first", "No email needed", "Mix-ups, not marks"]} />
      <div className="mx-auto max-w-5xl px-4 pb-16">
        <section className="grid items-end gap-8 py-10 md:grid-cols-[1.3fr_1fr]">
          <div className="pv-rise">
            <p className={label}>Season kicks off now</p>
            <h1 className={`${disp} mt-2 text-6xl leading-[0.92] sm:text-8xl`}>
              Physics, <span className="text-pv-accent">{interest.label}</span> rules.
            </h1>
            <p className="mt-5 max-w-md text-lg text-pv-mute">Every lesson opens with a story from your game. Eight questions find the mix-ups. Then the roadmap plays only what you need.</p>
            <div className="mt-6 flex flex-wrap gap-3"><a href="#" className={btn}>Kick off <ArrowRight aria-hidden /></a><a href="#how" className={btnQuiet}>How it works</a></div>
          </div>
          <div className={`${slab} p-5`}>
            <p className="font-pv-mono text-xs font-bold uppercase tracking-widest text-pv-accent">● Lesson preview · {interest.label}</p>
            <h2 className={`${disp} mt-2 text-3xl`}>{interest.tagline}</h2>
            <p className="mt-2 opacity-80">{interest.story}</p>
          </div>
        </section>

        <section aria-label="Pick an interest" className="py-4">
          <p className={label}>Pick your sport</p>
          <div className="mt-2 grid grid-cols-2 gap-2 sm:grid-cols-5">
            {INTERESTS.map((i) => (
              <button key={i.id} aria-pressed={i.id === interest.id} onClick={() => setInterest(i.id)}
                className={`${disp} pv-cut-sm flex items-center justify-center gap-2 py-4 text-xl ${i.id === interest.id ? "bg-pv-accent text-pv-accent-ink" : "bg-pv-surface text-pv-ink hover:bg-pv-surface2"}`}>
                <span aria-hidden className="not-italic">{i.emoji}</span>{i.label}
              </button>
            ))}
          </div>
        </section>

        <section id="how" className="grid gap-3 py-10 md:grid-cols-3">
          {[["01", "Starting check", "8 questions, no marks. Wrong answers name the mix-up."], ["02", "Your fixtures", "Concepts open in order. Known ones are ticked off."], ["03", "Lessons", "Story, idea, worked example, then the check. Six minutes."]].map(([n, t, d]) => (
            <div key={n} className="bg-pv-surface p-5">
              <p className="font-pv-mono text-4xl font-bold text-pv-accent">{n}</p>
              <h3 className={`${disp} mt-1 text-2xl`}>{t}</h3>
              <p className="text-pv-mute">{d}</p>
            </div>
          ))}
        </section>
        <p className="font-pv-mono text-xs text-pv-mute">NO EMAIL · USERNAME + PASSWORD · TEACHER CAN RESET</p>
      </div>
    </div>
  );
}

/* ------------------------------- Roadmap -------------------------------- */
const TAG: Record<NodeState, { word: string; cls: string; icon: ReactNode }> = {
  mastered: { word: "Mastered", cls: "bg-pv-gold text-pv-gold-ink", icon: <Trophy size={16} aria-hidden /> },
  done: { word: "Done", cls: "bg-pv-good text-pv-bg", icon: <Check size={16} strokeWidth={3} aria-hidden /> },
  next: { word: "Live · next up", cls: "bg-pv-accent text-pv-accent-ink", icon: <Radio size={16} aria-hidden /> },
  open: { word: "Open", cls: "bg-pv-surface2 text-pv-ink", icon: <Play size={14} aria-hidden /> },
  locked: { word: "Locked", cls: "bg-pv-surface2 text-pv-mute", icon: <Lock size={14} aria-hidden /> },
  soon: { word: "Coming soon", cls: "border border-dashed border-pv-mute text-pv-mute", icon: <Timer size={14} aria-hidden /> },
};

function Roadmap({ interest }: ScreenProps) {
  const [sel, setSel] = useState("c4");
  return (
    <div>
      <Bar right={`${interest.emoji} ${interest.label.toUpperCase()} · ${CHAPTER.classLevel.toUpperCase()}`} />
      <div className="mx-auto max-w-2xl px-4 pb-16">
        <section className={`${slab} mt-4 p-4`}>
          <p className="font-pv-mono text-xs font-bold uppercase tracking-widest text-pv-accent">Chapter 4 of 7</p>
          <h1 className={`${disp} text-4xl`}>{CHAPTER.name}</h1>
          <div className="mt-3 grid grid-cols-3 gap-2 text-center font-pv-mono">
            {[["5/8", "DONE"], ["2", "MASTERED"], ["2", "TO UNLOCK"]].map(([n, l]) => (
              <div key={l} className="border border-pv-slab-ink/20 py-2"><p className="text-2xl font-bold text-pv-accent">{n}</p><p className="text-[11px] opacity-80">{l}</p></div>
            ))}
          </div>
          <div className="mt-3 flex h-2 gap-0.5" role="img" aria-label="5 of 8 done, 2 mastered">
            {CONCEPTS.map((c) => <span key={c.id} className={`flex-1 ${c.state === "mastered" ? "bg-pv-gold" : c.state === "done" ? "bg-pv-good" : "bg-pv-slab-ink/25"}`} />)}
          </div>
        </section>

        <h2 className={`${label} mb-2 mt-6`}>Fixtures</h2>
        <ol className="space-y-2">
          {CONCEPTS.map((c, i) => {
            const t = TAG[c.state];
            const on = sel === c.id;
            const dim = c.state === "locked" || c.state === "soon";
            return (
              <li key={c.id}>
                <button onClick={() => setSel(c.id)} aria-expanded={on}
                  className={`pv-cut-sm flex w-full items-center gap-3 p-3 text-left ${c.state === "next" ? "bg-pv-accent text-pv-accent-ink" : "bg-pv-surface"} ${dim ? "opacity-80" : ""}`}>
                  <span className="w-10 font-pv-mono text-2xl font-bold opacity-60">{String(i + 1).padStart(2, "0")}</span>
                  <span className={`${disp} flex-1 text-xl leading-tight`}>{c.name}</span>
                  <span className={`pv-cut-sm flex items-center gap-1 px-2 py-1 font-pv-mono text-[11px] font-bold uppercase ${c.state === "next" ? "bg-pv-slab text-pv-slab-ink" : t.cls}`}>{t.icon}{t.word}</span>
                </button>
                {on && (
                  <div className="pv-wipe bg-pv-surface2 p-4">
                    <p>{c.note}</p>
                    {c.badge && <p className="mt-1 font-pv-mono text-xs font-bold uppercase text-pv-accent">{c.badge === "known" ? "★ You said you know it" : "▲ Focus: a mix-up showed here"}</p>}
                    <button disabled={dim} className={`${btn} mt-3`}>{c.state === "done" ? "Review" : c.state === "mastered" ? "Replay" : dim ? "Not yet" : "Start"} <ArrowRight size={18} aria-hidden /></button>
                  </div>
                )}
              </li>
            );
          })}
        </ol>
        <div className="mt-6 grid grid-cols-2 gap-2">
          <div className="bg-pv-surface p-3"><p className={label}>Revision</p><p className="font-bold">1 idea ready</p></div>
          <div className="bg-pv-surface p-3"><p className={label}>End check</p><p className="font-bold text-pv-mute">Not open yet</p></div>
        </div>
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
    <div key="s" className="space-y-4">
      <div className="border-l-4 border-pv-accent bg-pv-surface p-4">
        <p className="font-pv-mono text-xs font-bold uppercase tracking-widest text-pv-accent">Your story · AI-written · checked</p>
        <p className="mt-2 text-xl">{interest.personal}</p>
        <button className="mt-2 text-sm font-semibold underline">Something wrong with this story?</button>
      </div>
      <button aria-expanded={orig} onClick={() => setOrig(!orig)} className={`${disp} pv-cut-sm w-full bg-pv-surface2 px-4 py-3 text-left text-lg`}>{orig ? "▾" : "▸"} The original story</button>
      {orig && <p className="pv-wipe text-lg">{interest.story}</p>}
      <div className={`${slab} grid h-36 place-items-center text-7xl`} role="img" aria-label={interest.label}>{interest.emoji}</div>
    </div>,
    <div key="i" className="space-y-4"><p className="text-xl">{LESSON.idea}</p><p className={`${slab} py-6 text-center font-pv-mono text-6xl font-bold text-pv-accent`}>{LESSON.equation}</p></div>,
    <div key="w" className="space-y-4"><p className="text-xl">{LESSON.example.prompt}</p>
      {!reveal ? <button onClick={() => setReveal(true)} className={btnQuiet}>Call it first. Then reveal</button> : (
        <ol className="space-y-2">{LESSON.example.steps.map((s) => <li key={s} className="pv-wipe bg-pv-surface p-3 font-pv-mono">{s}</li>)}</ol>)}
    </div>,
    <div key="b" className="border-l-4 border-pv-bad bg-pv-surface p-4"><p className="font-pv-mono text-xs font-bold uppercase text-pv-bad">⚠ Where the picture breaks</p><p className="mt-1 text-xl">{LESSON.breaks}</p></div>,
    <div key="t" className="bg-pv-gold p-5 text-pv-gold-ink"><p className="font-pv-mono text-xs font-bold uppercase">★ Key takeaway</p><p className={`${disp} text-4xl leading-none`}>{LESSON.takeaway}</p></div>,
    <div key="c" className="space-y-3"><p className="text-xl">One question. No marks. A wrong answer shows what to fix.</p><button className={btn}>Go to the check <ArrowRight aria-hidden /></button></div>,
  ];
  return (
    <div className="flex min-h-[100dvh] flex-col">
      <Bar right={`${interest.emoji} ${LESSON.title.toUpperCase()}`} />
      <div className="mx-auto w-full max-w-2xl flex-1 px-4 pb-28">
        <nav aria-label="Lesson steps" className="mt-4 grid grid-cols-6 gap-1">
          {LESSON_STEPS.map((s, i) => (
            <button key={s} onClick={() => setStep(i)} aria-label={s} aria-current={i === step ? "step" : undefined}
              className={`pv-cut-sm py-2 font-pv-mono text-sm font-bold ${i < step ? "bg-pv-good text-pv-bg" : i === step ? "bg-pv-accent text-pv-accent-ink" : "bg-pv-surface2 text-pv-mute"}`}>{i + 1}</button>
          ))}
        </nav>
        <p className={`${label} mt-5`}>Play {step + 1} / {LESSON_STEPS.length}</p>
        <h1 className={`${disp} text-5xl`}>{LESSON_STEPS[step]}</h1>
        <div key={step} className="rm-slide-next mt-4">{body[step]}</div>
      </div>
      <div className="fixed inset-x-0 bottom-0 bg-pv-slab px-4 py-3">
        <div className="mx-auto flex max-w-2xl gap-3">
          <button disabled={step === 0} onClick={() => setStep(step - 1)} aria-label="Back" className={btnQuiet}><ArrowLeft aria-hidden /></button>
          <button disabled={step === last} onClick={() => setStep(step + 1)} className={`${btn} flex-1 justify-center`}>{step < last ? `Next · ${LESSON_STEPS[step + 1]}` : "Last play"} <ArrowRight aria-hidden /></button>
        </div>
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
      <div className="relative">
        <Bar right="INSTANT REPLAY" />
        {right && <Confetti colors={["var(--pv-accent)", "var(--pv-gold)", "var(--pv-good)", "var(--pv-ink)"]} />}
        <div className="mx-auto max-w-2xl px-4 pb-16">
          <div className={`${slab} mt-4 p-5`}>
            <p className="font-pv-mono text-xs font-bold uppercase tracking-widest text-pv-accent">{right ? "● Goal" : "● Let’s review the play"}</p>
            <h1 className={`${disp} rm-pop text-6xl leading-none`}>{right ? "Right!" : "Not quite. Useful."}</h1>
            {!right && picked && <p className="mt-2 opacity-80">{picked.mix}. That is the one to fix.</p>}
          </div>
          <ul className="mt-4 space-y-2">
            {OPTIONS.map((o) => {
              const isRight = o.key === CORRECT, isPick = o.key === pick;
              return (
                <li key={o.key} className={`pv-cut-sm flex items-center gap-3 p-3 ${isRight ? "bg-pv-good text-pv-bg" : isPick ? "bg-pv-bad text-pv-bg" : "bg-pv-surface text-pv-mute"}`}>
                  <span className="font-pv-mono text-xl font-bold">{o.key}</span><span className="flex-1">{o.text}</span>
                  {isRight && <span className="flex items-center gap-1 font-pv-mono text-xs font-bold uppercase"><Check size={16} aria-hidden /> Right answer</span>}
                  {isPick && !isRight && <span className="flex items-center gap-1 font-pv-mono text-xs font-bold uppercase"><X size={16} aria-hidden /> Your pick</span>}
                </li>
              );
            })}
          </ul>
          <div className="mt-4 bg-pv-surface p-4"><p className={label}>Why</p><p className="mt-1 text-lg">{correct.why}</p></div>
          {right && (
            <div className="mt-4 bg-pv-surface p-4"><p className={label}>Road to mastered</p>
              <ol className="mt-3 grid grid-cols-3 gap-2 text-center font-pv-mono text-xs font-bold uppercase">
                <li className="bg-pv-good p-2 text-pv-bg"><Check className="mx-auto" aria-hidden />Right once</li>
                <li className="border-2 border-dashed border-pv-accent p-2"><span className="block text-xl">1D</span>New question tomorrow</li>
                <li className="bg-pv-surface2 p-2 text-pv-mute"><Trophy className="mx-auto" aria-hidden />Mastered</li>
              </ol></div>
          )}
          <div className="mt-5 flex gap-3"><button className={btn}>{right ? "Back to fixtures" : "Re-read lesson"}</button><button className={btnQuiet} onClick={() => { setDone(false); setPick(null); setSure(null); }}>{right ? "Again" : "Try again"}</button></div>
        </div>
      </div>
    );
  return (
    <div>
      <Bar right={`${interest.emoji} CHECK · ${LESSON.title.toUpperCase()}`} />
      <div className="mx-auto max-w-2xl px-4 pb-28">
        <p className={`${label} mt-5`}>The call</p>
        <h1 className={`${disp} mt-1 text-3xl leading-tight sm:text-4xl`}>{interest.stem}</h1>
        <div className="mt-5 space-y-2" role="radiogroup" aria-label="Answers">
          {OPTIONS.map((o) => (
            <button key={o.key} role="radio" aria-checked={pick === o.key} onClick={() => setPick(o.key)}
              className={`pv-cut-sm flex w-full items-center gap-3 p-4 text-left text-lg ${pick === o.key ? "bg-pv-accent text-pv-accent-ink" : "bg-pv-surface hover:bg-pv-surface2"}`}>
              <span className="font-pv-mono text-2xl font-bold">{o.key}</span>{o.text}
            </button>
          ))}
          <button role="radio" aria-checked={pick === "?"} onClick={() => setPick("?")} className={`pv-cut-sm w-full p-3 text-left ${pick === "?" ? "bg-pv-accent text-pv-accent-ink" : "bg-pv-surface2 text-pv-mute"}`}>I’m not sure yet. Honest answer.</button>
        </div>
        {pick && (
          <div className="pv-wipe mt-5">
            <p className={label}>How sure are you?</p>
            <div className="mt-2 grid grid-cols-3 gap-2">
              {LEVELS.map((l, i) => (
                <button key={l} onClick={() => setSure(i)} aria-pressed={sure === i}
                  className={`${disp} pv-cut-sm py-3 text-lg ${sure === i ? "bg-pv-slab text-pv-slab-ink" : "bg-pv-surface2"}`}>{l}</button>
              ))}
            </div>
          </div>
        )}
      </div>
      <div className="fixed inset-x-0 bottom-0 flex items-center gap-3 bg-pv-slab px-4 py-3">
        <p className="flex-1 font-pv-mono text-xs uppercase text-pv-slab-ink opacity-80">{!pick ? "Pick an answer" : sure === null ? "Now: how sure?" : "Ready"}</p>
        <button disabled={!pick || sure === null} onClick={() => setDone(true)} className={btn}>Lock it in</button>
      </div>
    </div>
  );
}

/* -------------------------------- Teacher ------------------------------- */
function Teacher(_: ScreenProps) {
  void _;
  const T = TEACHER;
  return (
    <div>
      <Bar right="TEACHER · MS NAIR" />
      <Ticker items={[`${T.className}`, "End check open", `${T.tiles[2].value} right answers`, `${T.tiles[3].value} mix-ups`]} />
      <div className="mx-auto max-w-5xl px-4 pb-16">
        <h1 className={`${disp} mt-5 text-5xl`}>{T.className}</h1>
        <div className="mt-4 grid grid-cols-2 gap-2 md:grid-cols-4">
          {T.tiles.map((t) => (
            <div key={t.label} className={`${slab} p-4`}><p className="font-pv-mono text-[11px] font-bold uppercase tracking-widest opacity-70">{t.label}</p><p className="font-pv-mono text-3xl font-bold text-pv-accent">{t.value}</p><p className="text-sm opacity-70">{t.sub}</p></div>
          ))}
        </div>
        <div className="mt-4 grid gap-4 md:grid-cols-2">
          <section className="bg-pv-surface p-4"><h2 className={`${disp} text-2xl`}>Studied vs not studied</h2>
            {T.compare.map((c) => (
              <div key={c.label} className="mt-3"><div className="flex justify-between font-pv-mono text-sm"><span>{c.label}</span><span>{c.before}% → {c.after}%</span></div>
                <div className="mt-1 h-3 bg-pv-surface2"><div className="h-3 bg-pv-accent" style={{ width: `${c.after}%` }} /></div></div>
            ))}<p className="mt-3 text-sm text-pv-mute">A rough comparison, not a trial.</p></section>
          <section className="bg-pv-surface p-4"><h2 className={`${disp} text-2xl`}>League of mix-ups</h2>
            <ol className="mt-2">{T.misconceptions.map((m, i) => (
              <li key={m.name} className="flex items-center gap-3 border-t border-pv-line py-2"><span className="font-pv-mono text-xl font-bold text-pv-accent">{i + 1}</span><span className="flex-1 font-semibold">{m.name}</span><span className="font-pv-mono text-sm">{m.count} · {m.sure} sure</span></li>))}</ol></section>
        </div>
        <section className="mt-4 border-l-4 border-pv-accent bg-pv-surface p-4"><p className="font-pv-mono text-xs font-bold uppercase tracking-widest text-pv-accent">Teaching assistant · AI plan</p>
          <ol className="mt-2 list-decimal space-y-1 pl-5 text-lg">{T.plan.map((p) => <li key={p}>{p}</li>)}</ol></section>
        <section className="mt-4 bg-pv-surface p-4"><h2 className={`${disp} text-2xl`}>How the AI decided</h2>
          <div className="mt-3 grid grid-cols-5 gap-1 text-center font-pv-mono">
            {[["DRAFTS", T.ai.drafts], ["RULES ✕", T.ai.rule], ["CRITIC ✕", T.ai.critic], ["HUMAN", T.ai.human], ["SHOWN", T.ai.shown]].map(([l, n]) => (<div key={l} className="bg-pv-surface2 py-2"><p className="text-2xl font-bold">{n}</p><p className="text-[10px] font-bold">{l}</p></div>))}
          </div></section>
        <section className="mt-4 overflow-x-auto bg-pv-surface p-4"><h2 className={`${disp} text-2xl`}>Students</h2>
          <table className="mt-2 w-full text-left"><thead className={label}><tr><th className="py-1">Name</th><th>Done</th><th>Mix-ups</th><th /></tr></thead>
            <tbody>{T.students_list.map((s) => (<tr key={s.name} className="border-t border-pv-line"><td className="py-2 font-semibold">{s.name}</td><td className="font-pv-mono">{s.done}/8</td><td className="font-pv-mono">{s.mixups}</td><td className="text-right"><button className="pv-cut-sm bg-pv-surface2 px-3 py-1 text-sm font-bold">Reset password</button></td></tr>))}</tbody></table></section>
      </div>
    </div>
  );
}

export const screensC: ScreenSet = { landing: Landing, roadmap: Roadmap, lesson: Lesson, check: CheckScreen, teacher: Teacher };
