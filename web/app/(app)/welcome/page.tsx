// /welcome — "getting to know you": the first page a student sees after a teacher creates
// their account (components/welcome-gate.tsx sends them here). Taken once. After it comes
// the starting check (/start), the physics one.

"use client";

import { useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";

import { FormError } from "@/components/auth-card";
import { useAuth } from "@/components/auth-provider";
import { SurveyFlow } from "@/components/survey-flow";
import { useWelcomeGate } from "@/components/welcome-gate";
import { getSurvey } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";

export default function WelcomePage() {
  const { student } = useAuth();
  const { markDone } = useWelcomeGate();
  const router = useRouter();
  const survey = useFetch("survey", getSurvey);

  // Already answered (a bookmark, the back button): carry on to the roadmap.
  const taken = survey.data?.taken === true;
  useEffect(() => {
    if (taken) router.replace("/roadmap");
  }, [taken, router]);

  if (survey.loading || taken) {
    return (
      <main className="page-shell w-full flex-1">
        <div className="mx-auto w-full flex max-w-2xl flex-col gap-4">
          <div className="h-8 w-64 animate-pulse rounded-lg bg-muted" />
          <div className="h-48 animate-pulse rounded-xl bg-muted" />
        </div>
      </main>
    );
  }
  if (!survey.data) {
    return (
      <main className="page-shell w-full flex-1">
        <div className="mx-auto w-full flex max-w-2xl flex-col gap-4">
          <FormError message={survey.error ?? "Couldn't load the questions."} />
          <Link href="/roadmap" className="text-sm font-semibold text-primary hover:underline">
            Go to your roadmap
          </Link>
        </div>
      </main>
    );
  }

  const firstName = (student?.name ?? "").trim().split(/\s+/)[0] || "there";
  return (
    <SurveyFlow
      survey={survey.data}
      firstName={firstName}
      onDone={markDone}
      next={{ href: "/start", label: "Take the 5-minute check" }}
    />
  );
}
