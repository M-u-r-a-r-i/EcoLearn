// Client-side route guard for the pages under app/(app)/.
//
// This is a convenience, NOT the security boundary: the real check is the API's
// Depends(get_current_student_id), which refuses every learning request without
// a valid cookie. The guard only spares a logged-out student a page of errors.
// It can't be done in proxy.ts (Next's middleware): the cookie belongs to the
// API's origin (localhost:8000), so the web origin never sees it.

"use client";

import { useEffect, type ReactNode } from "react";
import { usePathname, useRouter } from "next/navigation";

import { useAuth } from "@/components/auth-provider";
import { PageContainer } from "@/components/page-container";

export function RequireAuth({ children }: { children: ReactNode }) {
  const { status } = useAuth();
  const router = useRouter();
  const pathname = usePathname();

  useEffect(() => {
    if (status === "unauthenticated") {
      // Remember where they were going, so login can send them back.
      router.replace(`/login?next=${encodeURIComponent(pathname)}`);
    }
  }, [status, router, pathname]);

  if (status !== "authenticated") {
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
