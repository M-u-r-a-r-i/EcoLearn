// Client-side route guard for the logged-in pages: app/(app)/ for students,
// app/teacher/(dashboard)/ for teachers.
//
// This is a convenience, NOT the security boundary: the real check is the API's
// Depends(get_current_student_id) / Depends(get_current_teacher_id), which
// refuse every request from the wrong kind of account. The guard only spares
// someone a page of errors. It can't be done in proxy.ts (Next's middleware):
// the cookie belongs to the API's origin (localhost:8000), so the web origin
// never sees it.

"use client";

import { useEffect, type ReactNode } from "react";
import { usePathname, useRouter } from "next/navigation";

import { HOME, useAuth, type Role } from "@/components/auth-provider";
import { PageContainer } from "@/components/page-container";

const LOGIN: Record<Role, string> = { student: "/login", teacher: "/teacher/login" };

export function RequireAuth({ role = "student", children }: { role?: Role; children: ReactNode }) {
  const { status, role: current, loggedOutOnPurpose } = useAuth();
  const router = useRouter();
  const pathname = usePathname();

  useEffect(() => {
    if (status === "unauthenticated" && loggedOutOnPurpose) {
      // They pressed "Log out": a plain login page, no way back to their page.
      router.replace(LOGIN[role]);
    } else if (status === "unauthenticated") {
      // The session expired: remember where they were going — query string
      // included, so /teacher/class?id=… or /lesson?concept=… survives.
      const here = pathname + window.location.search;
      router.replace(`${LOGIN[role]}?next=${encodeURIComponent(here)}`);
    } else if (status === "authenticated" && current && current !== role) {
      // Logged in, but as the other kind of account: go to their own home.
      router.replace(HOME[current]);
    }
  }, [status, current, role, router, pathname, loggedOutOnPurpose]);

  if (status !== "authenticated" || current !== role) {
    return (
      <main className="flex flex-1 flex-col">
        <PageContainer className="flex flex-col gap-4">
          <div className="h-8 w-64 animate-pulse rounded-lg bg-muted" />
          <div className="h-4 w-96 max-w-full animate-pulse rounded bg-muted" />
          <div className="h-40 w-full animate-pulse rounded-xl bg-muted" />
        </PageContainer>
      </main>
    );
  }
  return <>{children}</>;
}
