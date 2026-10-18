// /settings/about — change your "getting to know you" answers. The same questions as the
// first-login welcome, but filled in with what you said before; saving replaces your answers
// (the old set is kept server-side as history, and your teacher only sees the current one).

"use client";

import Link from "next/link";

import { FormError } from "@/components/auth-card";
import { useAuth } from "@/components/auth-provider";
import { SurveyFlow } from "@/components/survey-flow";
import { getSurvey } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";

export default function UpdateAboutPage() {
  const { student } = useAuth();
  const survey = useFetch("survey-edit", getSurvey);

  if (survey.loading) {
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
          <FormError message={survey.error ?? "Couldn't load your answers."} />
          <Link href="/settings" className="text-sm font-semibold text-primary hover:underline">
            Back to settings
          </Link>
        </div>
      </main>
    );
  }

  const firstName = (student?.name ?? "").trim().split(/\s+/)[0] || "there";
  return (
    <SurveyFlow
      mode="edit"
      survey={survey.data}
      initialAnswers={survey.data.answers}
      firstName={firstName}
      onDone={() => {}}
      next={{ href: "/settings", label: "Back to settings" }}
    />
  );
}
