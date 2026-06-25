// The top navigation bar, shown on every page (it's rendered once in the root
// layout). It carries the EcoLearn wordmark on the left and the primary call to
// action on the right. Because it lives in one file, changing the brand here
// updates the header across the whole site.

import Link from "next/link";

import { PrimaryButton } from "@/components/primary-button";

export function SiteNav() {
  return (
    // sticky + backdrop-blur = the bar stays at the top and softly frosts content
    // scrolling under it. border-border uses our hairline token.
    <header className="sticky top-0 z-40 w-full border-b border-border bg-background/80 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-5xl items-center justify-between px-6">
        {/* Wordmark — links home */}
        <Link
          href="/"
          className="flex items-center gap-2 text-lg font-bold tracking-tight text-foreground"
        >
          <span className="text-xl">🌱</span>
          EcoLearn
        </Link>

        {/* Primary action (uses the shared PrimaryButton, rendered as a link) */}
        <PrimaryButton asChild size="default" className="h-10 px-5 text-sm">
          <Link href="/">Get Started</Link>
        </PrimaryButton>
      </div>
    </header>
  );
}
