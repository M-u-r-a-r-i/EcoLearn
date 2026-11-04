// EcoLearn landing page (the "/" route).
//
// What a first-time visitor (a student, a parent, a teacher, a hackathon judge) should
// understand in ten seconds: it teaches Class 11-12 Physics through your own interest, it
// finds your mix-ups instead of just marking you, and teachers get a real class view.
//
// Everything on this page is a claim about the app, so it only says what the app does today:
// no invented numbers (the one illustration is labelled as made up), no "AI grades you"
// (grading is multiple choice, no model), and the AI story is named as AI. The page is a
// Server Component; the interactive parts (the interest showcase, the scroll reveal, the
// login-aware buttons) are small client components. Look: the house style
// (.claude/skills/ecolearn-style).

import Link from "next/link";
import type { CSSProperties } from "react";
import {
  ArrowUpRight,
  Compass,
  GraduationCap,
  Lightbulb,
  Route,
  ShieldCheck,
  Sparkles,
  UserRound,
  Users,
} from "lucide-react";

import { HeroActions } from "@/components/landing/hero-actions";
import { InterestShowcase } from "@/components/landing/interest-showcase";
import { Reveal } from "@/components/landing/reveal";
import { Button } from "@/components/ui/button";
import { InterestMark, Pill } from "@/components/ui-kit";

const INTERESTS = [
  { id: "cricket", name: "Cricket", emoji: "🏏", hint: "Spin, swing & sixes" },
  { id: "football", name: "Football", emoji: "⚽", hint: "Curves & kicks" },
  { id: "gaming", name: "Gaming", emoji: "🎮", hint: "Power up your brain" },
  { id: "smartphones", name: "Smartphones", emoji: "📱", hint: "The science in your pocket" },
  { id: "motorsport", name: "Motorsport", emoji: "🏎️", hint: "Fast cars, real forces" },
];

const STEPS = [
  {
    Icon: UserRound,
    title: "Tell us about you",
    text: "What you love, how you like to learn, how long you focus. A few taps, no right answers.",
  },
  {
    Icon: Compass,
    title: "A five-minute check",
    text: "No marks. Every wrong option points to a specific mix-up, so we learn what to fix.",
  },
  {
    Icon: Route,
    title: "Your own roadmap",
    text: "It skips what you already know and flags what to fix. Ideas open one after another, like levels.",
  },
  {
    Icon: Sparkles,
    title: "Learn, check, remember",
    text: "Each idea starts with a story. Get it right once, and a fresh question tomorrow makes it stick.",
  },
];

const DIFFERENT = [
  {
    Icon: Lightbulb,
    title: "Mix-ups, not just marks",
    text: "Most apps say wrong. EcoLearn says what you were thinking, kindly, and tracks it until it's fixed.",
  },
  {
    Icon: Sparkles,
    title: "Stories from your world",
    text: "A short story about your own hobby sits on top of every lesson. It is written by AI, checked by a second AI, and clearly labelled. The lesson, prepared in advance and checked, is always there.",
  },
  {
    Icon: ShieldCheck,
    title: "Fair by design",
    text: "Answers are graded by fixed rules, never by an AI. Students use a username and password, no email: we collect as little personal data as we can.",
  },
];

export default function Home() {
  return (
    <main className="landing w-full flex-1">
      <section className="hero">
        <div className="hero-copy fade-up">
          <Pill className="hero-kicker">
            <Sparkles size={13} aria-hidden /> Class 11 &amp; 12 Physics · CBSE and ISC
          </Pill>
          <h1 className="display">
            Physics makes
            <br />
            more sense{" "}
            <em>
              when
              <br />
              it&rsquo;s your world.
            </em>
          </h1>
          <p>
            A personal tutor that learns who you are, finds the mix-ups holding you back, and teaches every idea
            through cricket, football, gaming, phones or cars.
          </p>
          <div className="hero-actions">
            <HeroActions />
          </div>
          <div className="hero-proof">
            <span>Your teacher sets up your account, or you can create your own.</span>
          </div>
        </div>
        <div className="hero-art" role="img" aria-label="A cricket bat tracing a motion arc">
          <div className="art-grid" />
          <div className="art-orbit orbit-one" />
          <div className="art-orbit orbit-two" />
          <div className="art-stamp stamp-top">
            MOTION
            <br />
            <b>01</b>
          </div>
          <div className="art-ball float">🏏</div>
          <div className="arc-label label-a">v = Δx / Δt</div>
          <div className="arc-label label-b">
            PHYSICS
            <br />
            IN PLAY
          </div>
          <div className="art-note">
            <span className="note-dot" /> Your path, your pace
          </div>
        </div>
      </section>

      {/* ------------------------------------------------------------ The showcase */}
      <section className="interest-section" id="interests">
        <div className="section-title">
          <div>
            <p className="eyebrow">Start with what you love</p>
            <h2 className="display">Same physics. Your world.</h2>
          </div>
          <span className="section-aside">
            Pick an interest and watch
            <br />
            one idea change shape.
          </span>
        </div>
        <Reveal>
          <InterestShowcase />
        </Reveal>
        <div className="interest-grid mt-8">
          {INTERESTS.map((i, n) => (
            <Link
              href="/signup"
              key={i.id}
              className="interest-card card-hover"
              style={{ "--delay": `${n * 60}ms` } as CSSProperties}
            >
              <InterestMark id={i.id} emoji={i.emoji} large />
              <span className="interest-card-name">{i.name}</span>
              <small>{i.hint}</small>
              <ArrowUpRight className="interest-arrow" size={17} aria-hidden />
            </Link>
          ))}
        </div>
      </section>

      {/* ------------------------------------------------------------ How it works */}
      <section className="how-section">
        <div className="how-heading">
          <p className="eyebrow">A little progress, every day</p>
          <h2 className="display">
            From &ldquo;hmm&rdquo; to <em>&ldquo;got it.&rdquo;</em>
          </h2>
          <p>From your first sign-in to an idea that sticks.</p>
        </div>
        <div className="steps-line">
          {STEPS.map(({ Icon, title, text }, i) => (
            <div className="step-item" key={title}>
              <div className={`step-icon step-${i}`}>
                <Icon />
              </div>
              <small>0{i + 1}</small>
              <h3>{title}</h3>
              <p>{text}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ------------------------------------------------------- What's different */}
      <section className="interest-section">
        <div className="section-title">
          <div>
            <p className="eyebrow">What makes it different</p>
            <h2 className="display">Built to understand, not to rank.</h2>
          </div>
        </div>
        <ul className="grid gap-4 md:grid-cols-3">
          {DIFFERENT.map(({ Icon, title, text }, i) => (
            <li key={title}>
              <Reveal delay={i * 0.1} className="h-full">
                <div className="surface panel flex h-full flex-col gap-3">
                  <span className="tone-peach" aria-hidden>
                    <span className="dash-icon" style={{ width: 44, height: 44 }}>
                      <Icon style={{ width: 22, height: 22 }} />
                    </span>
                  </span>
                  <h3 className="display text-xl font-bold text-foreground">{title}</h3>
                  <p className="text-sm leading-relaxed text-muted-foreground">{text}</p>
                </div>
              </Reveal>
            </li>
          ))}
        </ul>
      </section>

      {/* ------------------------------------------------------------- For teachers */}
      <section className="interest-section">
        <div className="grid items-center gap-10 md:grid-cols-2">
          <Reveal className="flex flex-col gap-4">
            <p className="eyebrow flex items-center gap-2">
              <GraduationCap className="size-4" aria-hidden /> For teachers
            </p>
            <h2 className="display text-4xl font-semibold text-foreground">Know your class before you teach it.</h2>
            <p className="leading-relaxed text-muted-foreground">
              Create a class from a list of names and print the login slips. See which mix-ups are most common and who
              is sure of a wrong idea, compare a starting check with an end check, and get a plan for the next lesson.
              The AI&apos;s decisions are logged and open to review.
            </p>
            <Button variant="outline" size="lg" asChild className="self-start">
              <Link href="/teacher/login">Teacher login</Link>
            </Button>
          </Reveal>
          <Reveal delay={0.12}>
            <div className="surface panel flex flex-col gap-3">
              <div className="flex items-center gap-2 font-heading text-sm font-bold text-foreground">
                <Users className="size-4 text-primary" aria-hidden /> Class 11-B · what the class got wrong
              </div>
              {[
                { name: "Newton's third law", n: 14, w: 82 },
                { name: "Inertia and the first law", n: 11, w: 64 },
                { name: "Projectile motion", n: 7, w: 41 },
              ].map((row) => (
                <div key={row.name} className="dbar-row">
                  <div className="dbar-name">
                    <span>{row.name}</span>
                    <small>{row.n} students</small>
                  </div>
                  <div className="dbar-track">
                    <span className="dbar-fill bad" style={{ width: `${row.w}%`, display: "block" }} />
                  </div>
                </div>
              ))}
              <p className="text-xs text-muted-foreground">An illustration with made-up numbers.</p>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ------------------------------------------------------------------ Closing */}
      <section className="landing-cta">
        <div>
          <p className="eyebrow">One question at a time</p>
          <h2 className="display">
            Ready to see
            <br />
            where you stand?
          </h2>
          <p className="mt-3 max-w-md text-sm opacity-80">
            It takes a few minutes, and there are no marks. Log in with the username your teacher gave you, or create an
            account.
          </p>
        </div>
        <HeroActions />
        <span className="cta-decoration" aria-hidden>
          ✳
        </span>
      </section>

      <footer className="landing-footer">
        <Link href="/" className="brand-lockup">
          <span className="brand-mark" aria-hidden>
            e
          </span>
          <span>
            ecolearn<span className="brand-period">.</span>
          </span>
        </Link>
        <span>Physics, in your element.</span>
        <Link href="/teacher/login">
          For teachers <ArrowUpRight size={13} aria-hidden />
        </Link>
      </footer>
    </main>
  );
}
