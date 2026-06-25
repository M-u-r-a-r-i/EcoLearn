// EcoLearn landing page (the "/" route).
//
// Presentation only — no data wiring yet. It uses our design-system pieces:
//   • SiteNav (rendered site-wide in app/layout.tsx)
//   • PageContainer — shared max-width + padding
//   • PrimaryButton — the branded primary action
// and our brand tokens as Tailwind utilities (bg-background, text-foreground,
// text-brand-accent, …), all defined once in app/globals.css.

import Link from "next/link";

import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";

export default function Home() {
  return (
    // flex-1 = fill the space left under the sticky nav.
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-1 flex-col items-center justify-center gap-7 text-center">
        {/* Amber "eyebrow" badge — shows off the reusable brand-accent token */}
        <span className="rounded-full bg-brand-accent/10 px-4 py-1.5 text-sm font-semibold text-brand-accent">
          🌱 Personalised learning
        </span>

        {/* Hero headline */}
        <h1 className="max-w-3xl text-balance text-5xl font-extrabold leading-tight tracking-tight text-foreground sm:text-6xl">
          Learn anything, through what you love
        </h1>

        {/* One-line subtitle */}
        <p className="max-w-xl text-balance text-lg leading-relaxed text-muted-foreground sm:text-xl">
          EcoLearn personalises every lesson to a student&apos;s passions —
          turning the things they love into the way they learn.
        </p>

        {/* Primary call-to-action (shared branded button) */}
        <PrimaryButton asChild className="mt-2">
          <Link href="/">Get Started</Link>
        </PrimaryButton>
      </PageContainer>
    </main>
  );
}
