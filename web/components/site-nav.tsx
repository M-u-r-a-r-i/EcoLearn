// The top navigation bar, shown on every page (rendered once in the root
// layout). Wordmark on the left; on the right, what depends on who's here:
// logged out → Log in + Get Started; a student → Roadmap, Settings, their name
// and Log out; a teacher → Classes, Account, their name and Log out.
// A Client Component because it reads the auth state. Hidden when printing, so
// a teacher's printed sign-in slips are just the slips.

"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";

import { HOME, useAuth } from "@/components/auth-provider";
import { PrimaryButton } from "@/components/primary-button";
import { ThemeToggle } from "@/components/theme-toggle";
import { Button } from "@/components/ui/button";

const LINK = "text-sm font-semibold text-muted-foreground hover:text-foreground";

export function SiteNav() {
  const { status, role, student, teacher, logout } = useAuth();
  const router = useRouter();

  async function handleLogout() {
    const wasTeacher = role === "teacher";
    await logout();
    router.replace(wasTeacher ? "/teacher/login" : "/login");
  }

  const name = student?.name ?? teacher?.name;

  return (
    // sticky + backdrop-blur = the bar stays at the top and softly frosts content
    // scrolling under it. border-border uses our hairline token.
    <header className="sticky top-0 z-40 w-full border-b border-border bg-background/80 backdrop-blur print:hidden">
      <div className="mx-auto flex h-16 max-w-5xl items-center justify-between gap-3 px-4 sm:px-6">
        {/* Wordmark — links home */}
        <Link
          href={status === "authenticated" && role ? HOME[role] : "/"}
          className="flex items-center gap-2 text-lg font-bold tracking-tight text-foreground"
        >
          <span className="text-xl" aria-hidden>🌱</span>
          {/* On the narrowest phones the mark alone, so the links fit on one line. */}
          <span className="hidden min-[400px]:inline">EcoLearn</span>
          <span className="sr-only min-[400px]:hidden">EcoLearn</span>
        </Link>

        {/* Nothing while loading, so logged-in users never see a flash of "Log in". */}
        {status === "authenticated" && name && (
          <nav className="flex items-center gap-1.5 sm:gap-4">
            {role === "student" ? (
              <>
                <Link href="/roadmap" className={LINK}>
                  Roadmap
                </Link>
                <Link href="/settings" className={LINK}>
                  Settings
                </Link>
              </>
            ) : (
              <>
                <Link href="/teacher" className={LINK}>
                  Classes
                </Link>
                <Link href="/teacher/account" className={LINK}>
                  Account
                </Link>
              </>
            )}
            <span className="hidden text-sm text-muted-foreground sm:inline">
              Hi, <span className="font-semibold text-foreground">{name}</span>
            </span>
            <ThemeToggle />
            <Button variant="outline" size="sm" onClick={handleLogout}>
              Log out
            </Button>
          </nav>
        )}
        {status === "unauthenticated" && (
          <nav className="flex items-center gap-2 sm:gap-3">
            <ThemeToggle />
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
