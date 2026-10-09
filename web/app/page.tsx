// EcoLearn landing page (the "/" route). Presentation only: the house-style hero,
// the five interests, how it works, and a closing call to action. Copy is about
// what the product really is: Class 11-12 physics (CBSE/ISC) taught through a
// student's own interest.

import Link from "next/link";
import type { CSSProperties } from "react";
import {
  ArrowRight,
  ArrowUpRight,
  BookOpen,
  CircleHelp,
  Sparkles,
  Target,
  Trophy,
} from "lucide-react";

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
  { n: "01", icon: <CircleHelp />, title: "Starting check", copy: "A few quick questions find your starting point." },
  { n: "02", icon: <Target />, title: "Your personal plan", copy: "We shape a path around what you know." },
  { n: "03", icon: <BookOpen />, title: "Stories & lessons", copy: "Physics clicks through the things you love." },
  { n: "04", icon: <Trophy />, title: "Real mastery", copy: "Review, retry and celebrate what sticks." },
];

export default function Home() {
  return (
    <main className="landing w-full flex-1">
      <section className="hero">
        <div className="hero-copy fade-up">
          <Pill className="hero-kicker">
            <Sparkles size={13} aria-hidden /> Class 11–12 physics, made personal
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
            Learn the big ideas through cricket, football, gaming, phones or motorsport. Your
            interests. Your pace. Your physics.
          </p>
          <div className="hero-actions">
            <Button size="lg" asChild>
              <Link href="/signup">
                Get started <ArrowRight size={16} aria-hidden />
              </Link>
            </Button>
            <Button size="lg" variant="outline" asChild>
              <Link href="/login">Log in</Link>
            </Button>
          </div>
          <div className="hero-proof">
            <span>Made for curious minds in Classes 11 &amp; 12 · CBSE and ISC</span>
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

      <section className="interest-section" id="interests">
        <div className="section-title">
          <div>
            <p className="eyebrow">Start with what you love</p>
            <h2 className="display">Pick your kind of play.</h2>
          </div>
          <span className="section-aside">
            Physics is already there.
            <br />
            We&rsquo;ll help you spot it.
          </span>
        </div>
        <div className="interest-grid">
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

      <section className="how-section">
        <div className="how-heading">
          <p className="eyebrow">A little progress, every day</p>
          <h2 className="display">
            From &ldquo;hmm&rdquo; to <em>&ldquo;got it.&rdquo;</em>
          </h2>
          <p>Four small steps. A much clearer picture.</p>
        </div>
        <div className="steps-line">
          {STEPS.map((s, i) => (
            <div className="step-item" key={s.n}>
              <div className={`step-icon step-${i}`}>{s.icon}</div>
              <small>{s.n}</small>
              <h3>{s.title}</h3>
              <p>{s.copy}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="landing-cta">
        <div>
          <p className="eyebrow">One question at a time</p>
          <h2 className="display">
            Your next &ldquo;aha&rdquo; is
            <br />
            closer than you think.
          </h2>
        </div>
        <Button size="lg" asChild>
          <Link href="/signup">
            Find your starting point <ArrowRight size={16} aria-hidden />
          </Link>
        </Button>
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
