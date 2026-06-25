// Onboarding page (/onboarding).
//
// This is a Client Component ("use client") because it has interactivity:
// useState for form fields, click handlers, an async fetch, and navigation.
// Server Components can't do those — they render once on the server.

"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { createStudent } from "@/lib/api";
import { useStudent } from "@/components/student-provider";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { SectionHeading } from "@/components/section-heading";
import { Input } from "@/components/ui/input";
import { cn } from "@/lib/utils";

const INTERESTS = [
  { value: "football", label: "Football", emoji: "⚽" },
  { value: "gaming", label: "Gaming", emoji: "🎮" },
];

const LEVELS = [
  { value: "Class 11", label: "Class 11" },
  { value: "Class 12", label: "Class 12" },
];

export default function OnboardingPage() {
  const router = useRouter();
  const { setStudent } = useStudent();

  // ----- Form state: one piece of state per choice the user makes -----
  const [name, setName] = useState("");
  const [interest, setInterest] = useState("football");
  const [level, setLevel] = useState("Class 11");

  // ----- Request state: drives the loading + error UI -----
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleStart() {
    setError(null);
    if (!name.trim()) {
      setError("Please enter your name first.");
      return;
    }

    setLoading(true); // flip ON -> button shows "Creating…" and is disabled
    try {
      // THE network call. We `await` the round-trip to FastAPI.
      const profile = await createStudent({ name: name.trim(), interest, level });
      setStudent(profile); // remember the returned student (context)
      router.push("/roadmap"); // navigate on success
    } catch {
      // Thrown by createStudent if the backend is unreachable or returns an error.
      setError(
        "Couldn't reach the backend. Make sure FastAPI is running on " +
          (process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000") +
          ".",
      );
    } finally {
      setLoading(false); // flip OFF whether we succeeded or failed
    }
  }

  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-1 flex-col items-center justify-center gap-8">
        <SectionHeading
          eyebrow="Get started"
          title="Tell us about you"
          subtitle="We'll personalise every lesson to what you love."
          className="items-center text-center"
        />

        <div className="flex w-full max-w-md flex-col gap-6 rounded-xl border border-border bg-card p-6 shadow-card">
          {/* Name */}
          <div className="flex flex-col gap-2">
            <label htmlFor="name" className="text-sm font-semibold text-foreground">
              Your name
            </label>
            <Input
              id="name"
              placeholder="e.g. Ada"
              value={name}
              onChange={(e) => setName(e.target.value)}
              disabled={loading}
            />
          </div>

          {/* Interest — selectable cards */}
          <div className="flex flex-col gap-2">
            <span className="text-sm font-semibold text-foreground">
              Learn through…
            </span>
            <div className="flex gap-3">
              {INTERESTS.map((opt) => (
                <button
                  key={opt.value}
                  type="button"
                  disabled={loading}
                  onClick={() => setInterest(opt.value)}
                  className={cn(
                    "flex-1 rounded-xl border p-5 text-center transition-all",
                    interest === opt.value
                      ? "border-primary bg-primary/5 ring-2 ring-primary shadow-soft"
                      : "border-border bg-card hover:border-primary/40 hover:shadow-soft",
                  )}
                >
                  <div className="text-3xl">{opt.emoji}</div>
                  <div className="mt-2 font-semibold text-foreground">
                    {opt.label}
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Level — selectable cards */}
          <div className="flex flex-col gap-2">
            <span className="text-sm font-semibold text-foreground">Your class</span>
            <div className="flex gap-3">
              {LEVELS.map((opt) => (
                <button
                  key={opt.value}
                  type="button"
                  disabled={loading}
                  onClick={() => setLevel(opt.value)}
                  className={cn(
                    "flex-1 rounded-xl border p-3 font-semibold transition-all",
                    level === opt.value
                      ? "border-primary bg-primary/5 ring-2 ring-primary text-foreground"
                      : "border-border bg-card text-muted-foreground hover:border-primary/40",
                  )}
                >
                  {opt.label}
                </button>
              ))}
            </div>
          </div>

          {/* Error state */}
          {error && (
            <p className="rounded-xl border border-destructive/30 bg-destructive/5 px-4 py-3 text-sm text-destructive">
              {error}
            </p>
          )}

          {/* Submit — disabled while loading; label reflects the loading state */}
          <PrimaryButton onClick={handleStart} disabled={loading} className="w-full">
            {loading ? "Creating…" : "Start Learning →"}
          </PrimaryButton>
        </div>
      </PageContainer>
    </main>
  );
}
