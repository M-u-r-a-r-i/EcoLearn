// The top navigation bar, shown on every page (rendered once in the root
// layout). Wordmark on the left; on the right, what depends on who's here:
// logged out → Log in + Get Started; logged in → Roadmap, the student's name
// and Log out. A Client Component because it reads the auth state.

"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";

import { useAuth } from "@/components/auth-provider";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";

export function SiteNav() {
  const { status, student, logout } = useAuth();
  const router = useRouter();

  async function handleLogout() {
    await logout();
    router.replace("/login");
  }

  return (
    // sticky + backdrop-blur = the bar stays at the top and softly frosts content
    // scrolling under it. border-border uses our hairline token.
    <header className="sticky top-0 z-40 w-full border-b border-border bg-background/80 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-5xl items-center justify-between gap-4 px-6">
        {/* Wordmark — links home */}
        <Link
          href={status === "authenticated" ? "/roadmap" : "/"}
          className="flex items-center gap-2 text-lg font-bold tracking-tight text-foreground"
        >
          <span className="text-xl">🌱</span>
          EcoLearn
        </Link>

        {/* Nothing while loading, so logged-in students never see a flash of "Log in". */}
        {status === "authenticated" && student && (
          <nav className="flex items-center gap-2 sm:gap-4">
            <Link
              href="/roadmap"
              className="text-sm font-semibold text-muted-foreground hover:text-foreground"
            >
              Roadmap
            </Link>
            <Link
              href="/settings"
              className="text-sm font-semibold text-muted-foreground hover:text-foreground"
            >
              Settings
            </Link>
            <span className="hidden text-sm text-muted-foreground sm:inline">
              Hi, <span className="font-semibold text-foreground">{student.name}</span>
            </span>
            <Button variant="outline" size="sm" onClick={handleLogout}>
              Log out
            </Button>
          </nav>
        )}
        {status === "unauthenticated" && (
          <nav className="flex items-center gap-2 sm:gap-3">
            <Button variant="ghost" asChild>
              <Link href="/login">Log in</Link>
            </Button>
            <PrimaryButton asChild size="default" className="h-10 px-5 text-sm">
              <Link href="/signup">Get Started</Link>
            </PrimaryButton>
          </nav>
        )}
      </div>
    </header>
  );
}
