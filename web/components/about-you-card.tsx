// Settings -> "About you": what the app took from the "getting to know you" questions, in the
// student's own terms, and a way to change it. Shows the same sentences as the end of the
// survey ("here's what we'll do with this"), so a student always knows what their answers do.
// Silent on error: Settings is useful without it.

"use client";

import Link from "next/link";
import { ArrowRight, Heart } from "lucide-react";

import { PrimaryButton } from "@/components/primary-button";
import { whatWeHeard } from "@/components/survey-flow";
import { getSurvey } from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";

export function AboutYouCard() {
  const { data, loading } = useFetch("survey-settings", getSurvey);

  if (loading) return <div className="h-40 animate-pulse rounded-xl bg-muted" aria-label="Loading" />;
  if (!data) return null;

  const labelOf = (id: string) =>
    data.hobby_options?.find((h) => h.id === id)?.label ?? id.charAt(0).toUpperCase() + id.slice(1);
  const lines = data.taken && data.traits ? whatWeHeard(data.traits, labelOf, false) : [];

  return (
    <section className="flex flex-col gap-4 rounded-xl border border-border bg-card p-6 shadow-card">
      <div className="flex flex-col gap-1">
        <h2 className="flex items-center gap-2 text-lg font-bold text-foreground">
          <Heart className="size-5 text-primary" aria-hidden /> About you
        </h2>
        <p className="text-sm text-muted-foreground">
          Your answers to &ldquo;getting to know you&rdquo; shape your lessons. People change, so you can
          change them any time.
        </p>
      </div>

      {lines.length > 0 ? (
        <ul className="flex flex-col gap-2">
          {lines.map((l) => (
            <li key={l.text} className="flex items-start gap-3 text-sm text-foreground">
              <span aria-hidden className="text-lg leading-none">
                {l.emoji}
              </span>
              <span>{l.text}</span>
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-sm text-muted-foreground">
          {data.taken ? "Nothing is set yet: every answer was skipped." : "You haven't answered these yet."}
        </p>
      )}

      {data.updated_at && (
        <p className="text-xs text-muted-foreground">
          Last updated {new Date(data.updated_at).toLocaleDateString(undefined, { day: "numeric", month: "short", year: "numeric" })}.
        </p>
      )}

      <PrimaryButton asChild className="self-start">
        <Link href={data.taken ? "/settings/about" : "/welcome"}>
          {data.taken ? "Update my answers" : "Answer them now"} <ArrowRight className="size-5" />
        </Link>
      </PrimaryButton>
    </section>
  );
}
