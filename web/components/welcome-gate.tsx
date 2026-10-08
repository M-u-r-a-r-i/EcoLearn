// First sign-in (2026-10-08): a student who hasn't answered "getting to know you" is sent
// to /welcome before anything else. Mounted inside <RequireAuth>, so it only runs for a
// logged-in student.
//
// The gate FAILS OPEN: if the survey can't be loaded (API down, a network blip) the student
// sees the page they asked for, never a dead end. It is a convenience for the pilot's data
// collection, not a security boundary. Mounted in the (app) layout, so it checks once per
// page load, not on every click.

"use client";

import { createContext, useContext, useEffect, useState, type ReactNode } from "react";
import { usePathname, useRouter } from "next/navigation";

import { PageContainer } from "@/components/page-container";
import { getSurvey } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";

const WelcomeContext = createContext<{ markDone: () => void }>({ markDone: () => {} });

// The survey page calls this when the student finishes, so the gate stops redirecting.
export function useWelcomeGate() {
  return useContext(WelcomeContext);
}

export function WelcomeGate({ children }: { children: ReactNode }) {
  const survey = useFetch("survey-gate", getSurvey);
  const [done, setDone] = useState(false);
  const router = useRouter();
  const pathname = usePathname();

  const needsSurvey = !survey.loading && survey.data !== null && !survey.data.taken && !done;
  const onWelcome = pathname === "/welcome";

  useEffect(() => {
    if (needsSurvey && !onWelcome) router.replace("/welcome");
  }, [needsSurvey, onWelcome, router]);

  // Waiting for the answer, or about to be sent to /welcome: a skeleton, not a flash of the app.
  if (survey.loading || (needsSurvey && !onWelcome)) {
    return (
      <main className="flex flex-1 flex-col">
        <PageContainer className="flex flex-col gap-4">
          <div className="h-8 w-64 animate-pulse rounded-lg bg-muted" />
          <div className="h-40 w-full animate-pulse rounded-xl bg-muted" />
        </PageContainer>
      </main>
    );
  }
  return <WelcomeContext.Provider value={{ markDone: () => setDone(true) }}>{children}</WelcomeContext.Provider>;
}
