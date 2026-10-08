// EcoLearn landing page (the "/" route).
//
// What a first-time visitor (a student, a parent, a teacher, a hackathon judge) should
// understand in ten seconds: it teaches Class 11-12 Physics through your own interest, it
// finds your mix-ups instead of just marking you, and teachers get a real class view.
//
// Everything on this page is a claim about the app, so it only says what the app does today:
// no invented numbers, no "AI grades you" (grading is multiple choice, no model), and the AI
// story is named as AI. The page is a Server Component; the interactive parts (the interest
// showcase, the scroll reveal, the login-aware buttons) are small client components.

import Link from "next/link";
import {
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
import { PageContainer } from "@/components/page-container";
import { Button } from "@/components/ui/button";

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
    text: "A short story about your own hobby sits on top of every lesson. It is written by AI, checked by a second AI, and clearly labelled. The reviewed lesson is always there.",
  },
  {
    Icon: ShieldCheck,
    title: "Fair by design",
    text: "Answers are graded by fixed rules, never by an AI. Students use a username and password, no email: we collect as little personal data as we can.",
  },
];

export default function Home() {
  return (
    <main className="flex flex-1 flex-col">
      {/* ------------------------------------------------------------------ Hero */}
      <section
        className="relative overflow-hidden border-b border-border"
        style={{
          backgroundImage:
            "radial-gradient(70% 60% at 85% 0%, color-mix(in oklab, var(--primary) 20%, transparent), transparent 70%), radial-gradient(60% 50% at 0% 100%, color-mix(in oklab, var(--brand-accent) 14%, transparent), transparent 70%)",
        }}
      >
        <PageContainer className="flex max-w-5xl flex-col items-center gap-6 py-16 text-center sm:py-24">
          <span className="rm-sheet rounded-full bg-brand-accent/10 px-4 py-1.5 text-sm font-semibold text-brand-accent">
            ⚛️ Class 11 & 12 Physics · CBSE and ISC
          </span>
          <h1
            className="rm-sheet max-w-3xl text-balance text-5xl font-extrabold leading-[1.05] tracking-tight text-foreground sm:text-6xl"
            style={{ animationDelay: "80ms" }}
          >
            Physics, through the thing you already love
          </h1>
          <p
            className="rm-sheet max-w-2xl text-balance text-lg leading-relaxed text-muted-foreground sm:text-xl"
            style={{ animationDelay: "160ms" }}
          >
            A personal tutor that learns who you are, finds the mix-ups holding you back, and teaches
            every idea through cricket, football, gaming, phones or cars.
          </p>
          <div className="rm-sheet mt-2" style={{ animationDelay: "240ms" }}>
            <HeroActions stacked />
          </div>
          <p className="text-sm text-muted-foreground">Your teacher sets up your account, or you can create your own.</p>
        </PageContainer>
      </section>

      {/* ------------------------------------------------------------ The showcase */}
      <section className="py-16 sm:py-20">
        <PageContainer className="flex max-w-3xl flex-col gap-8">
          <Reveal className="flex flex-col items-center gap-3 text-center">
            <h2 className="text-3xl font-extrabold tracking-tight text-foreground sm:text-4xl">
              Same physics. Your world.
            </h2>
            <p className="max-w-xl text-muted-foreground">
              Pick an interest and watch one idea change shape.
            </p>
          </Reveal>
          <Reveal delay={0.1}>
            <InterestShowcase />
          </Reveal>
        </PageContainer>
      </section>

      {/* ------------------------------------------------------------ How it works */}
      <section className="border-y border-border bg-card/40 py-16 sm:py-20">
        <PageContainer className="flex max-w-5xl flex-col gap-10">
          <Reveal className="flex flex-col items-center gap-3 text-center">
            <h2 className="text-3xl font-extrabold tracking-tight text-foreground sm:text-4xl">How it works</h2>
            <p className="max-w-xl text-muted-foreground">From your first sign-in to an idea that sticks.</p>
          </Reveal>
          <ol className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {STEPS.map(({ Icon, title, text }, i) => (
              <li key={title}>
                <Reveal delay={i * 0.08} className="h-full">
                  <div className="flex h-full flex-col gap-3 rounded-2xl border border-border bg-card p-5 shadow-soft transition-all duration-200 hover:-translate-y-1 hover:shadow-card">
                    <div className="flex items-center justify-between">
                      <span className="flex size-10 items-center justify-center rounded-full bg-primary/10 text-primary">
                        <Icon className="size-5" aria-hidden />
                      </span>
                      <span className="text-sm font-bold text-muted-foreground">0{i + 1}</span>
                    </div>
                    <h3 className="text-lg font-bold text-foreground">{title}</h3>
                    <p className="text-sm leading-relaxed text-muted-foreground">{text}</p>
                  </div>
                </Reveal>
              </li>
            ))}
          </ol>
        </PageContainer>
      </section>

      {/* ------------------------------------------------------- What's different */}
      <section className="py-16 sm:py-20">
        <PageContainer className="flex max-w-5xl flex-col gap-10">
          <Reveal className="flex flex-col items-center gap-3 text-center">
            <h2 className="text-3xl font-extrabold tracking-tight text-foreground sm:text-4xl">
              Built to understand, not to rank
            </h2>
          </Reveal>
          <ul className="grid gap-4 md:grid-cols-3">
            {DIFFERENT.map(({ Icon, title, text }, i) => (
              <li key={title}>
                <Reveal delay={i * 0.1} className="h-full">
                  <div className="flex h-full flex-col gap-3 rounded-2xl border border-border bg-card p-6 shadow-soft">
                    <span className="flex size-11 items-center justify-center rounded-xl bg-brand-accent/10 text-brand-accent">
                      <Icon className="size-6" aria-hidden />
                    </span>
                    <h3 className="text-xl font-bold text-foreground">{title}</h3>
                    <p className="leading-relaxed text-muted-foreground">{text}</p>
                  </div>
                </Reveal>
              </li>
            ))}
          </ul>
        </PageContainer>
      </section>

      {/* ------------------------------------------------------------- For teachers */}
      <section className="border-y border-border bg-card/40 py-16 sm:py-20">
        <PageContainer className="grid max-w-5xl items-center gap-10 md:grid-cols-2">
          <Reveal className="flex flex-col gap-4">
            <span className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-brand-accent">
              <GraduationCap className="size-4" aria-hidden /> For teachers
            </span>
            <h2 className="text-3xl font-extrabold tracking-tight text-foreground sm:text-4xl">
              Know your class before you teach it
            </h2>
            <p className="leading-relaxed text-muted-foreground">
              Create a class from a list of names and print the login slips. See which mix-ups are most
              common and who is sure of a wrong idea, compare a starting check with an end check, and
              get a plan for the next lesson. The AI&apos;s decisions are logged and open to review.
            </p>
            <Button variant="outline" size="lg" asChild className="h-12 self-start rounded-xl px-6 font-semibold">
              <Link href="/teacher/login">Teacher login</Link>
            </Button>
          </Reveal>
          <Reveal delay={0.12}>
            <div className="flex flex-col gap-3 rounded-3xl border border-border bg-card p-5 shadow-card">
              <div className="flex items-center gap-2 text-sm font-bold text-foreground">
                <Users className="size-4 text-primary" aria-hidden /> Class 11-B · what the class got wrong
              </div>
              {[
                { name: "Newton's third law", n: 14, w: 82 },
                { name: "Inertia and the first law", n: 11, w: 64 },
                { name: "Projectile motion", n: 7, w: 41 },
              ].map((row) => (
                <div key={row.name} className="flex flex-col gap-1">
                  <div className="flex justify-between text-xs">
                    <span className="font-medium text-foreground">{row.name}</span>
                    <span className="text-muted-foreground">{row.n} students</span>
                  </div>
                  <span className="h-2 overflow-hidden rounded-full bg-muted">
                    <span className="block h-full rounded-full bg-primary" style={{ width: `${row.w}%` }} />
                  </span>
                </div>
              ))}
              <p className="text-xs text-muted-foreground">An illustration with made-up numbers.</p>
            </div>
          </Reveal>
        </PageContainer>
      </section>

      {/* ------------------------------------------------------------------ Closing */}
      <section className="py-16 sm:py-24">
        <PageContainer className="flex max-w-3xl flex-col items-center gap-6 text-center">
          <Reveal className="flex flex-col items-center gap-6">
            <h2 className="text-balance text-3xl font-extrabold tracking-tight text-foreground sm:text-5xl">
              Ready to see where you stand?
            </h2>
            <p className="max-w-xl text-muted-foreground">
              It takes a few minutes, and there are no marks. Log in with the username your teacher gave you, or
              create an account.
            </p>
            <HeroActions />
          </Reveal>
        </PageContainer>
      </section>
    </main>
  );
}
