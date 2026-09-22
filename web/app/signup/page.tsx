// Signup page (/signup) — replaces the old /onboarding.
//
// Two steps in one form: (1) account — name, username, password; (2) what the
// student loves and which class they're in. Nothing is sent until the end: one
// POST /api/auth/register creates the account and logs it in (the API sets the
// session cookie), so there is never a half-made account.
//
// No email on purpose: the pilot students are minors, so we collect as little
// personal data as possible. Password resets go through a teacher.

"use client";

import { useEffect, useState, type FormEvent } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";

import { AuthCard, Field, FormError } from "@/components/auth-card";
import { useAuth } from "@/components/auth-provider";
import { InterestLevelFields } from "@/components/interest-level-fields";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";
import { ApiError, friendlyMessage } from "@/lib/api";

// Mirrors the API's rules (src/platform_api.py, src/auth/passwords.py) so the
// student hears about a problem before submitting. The API still checks: it is
// the real authority.
const USERNAME_PATTERN = /^[a-z0-9][a-z0-9_.]{2,19}$/;
const MIN_PASSWORD_LENGTH = 8;

function accountErrors(name: string, username: string, password: string) {
  return {
    name: name.trim() ? null : "Please enter your name.",
    username: USERNAME_PATTERN.test(username.trim().toLowerCase())
      ? null
      : "3–20 characters: letters, numbers, _ or . (start with a letter or number).",
    password:
      password.length >= MIN_PASSWORD_LENGTH
        ? null
        : `At least ${MIN_PASSWORD_LENGTH} characters.`,
  };
}

export default function SignupPage() {
  const { register, status } = useAuth();
  const router = useRouter();

  const [step, setStep] = useState<1 | 2>(1);
  const [name, setName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [interest, setInterest] = useState("");
  const [level, setLevel] = useState("Class 11");
  const [showErrors, setShowErrors] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (status === "authenticated" && !loading) router.replace("/roadmap");
  }, [status, loading, router]);

  const errors = accountErrors(name, username, password);
  const shown = showErrors ? errors : { name: null, username: null, password: null };

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setError(null);

    if (step === 1) {
      setShowErrors(true);
      if (!errors.name && !errors.username && !errors.password) setStep(2);
      return;
    }

    setLoading(true);
    try {
      await register({ name: name.trim(), username: username.trim(), password, interest, level });
      router.replace("/roadmap");
    } catch (err) {
      setLoading(false);
      // A taken username is a step-1 problem: send them back to fix it.
      if (err instanceof ApiError && err.status === 409) setStep(1);
      setError(friendlyMessage(err));
    }
  }

  return (
    <AuthCard
      eyebrow={`Step ${step} of 2`}
      title={step === 1 ? "Create your account" : "Tell us about you"}
      subtitle={
        step === 1
          ? "No email needed — just a username and password."
          : "We'll teach every lesson through what you love."
      }
      footer={
        <>
          Already have an account?{" "}
          <Link href="/login" className="font-semibold text-primary hover:underline">
            Log in
          </Link>
        </>
      }
    >
      <form onSubmit={handleSubmit} className="flex flex-col gap-6" noValidate>
        {step === 1 ? (
          <>
            <Field
              id="name"
              label="Your name"
              placeholder="e.g. Ananya"
              autoComplete="given-name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              error={shown.name}
            />
            <Field
              id="username"
              label="Username"
              autoComplete="username"
              autoCapitalize="none"
              spellCheck={false}
              hint="You'll log in with this. Letters, numbers, _ or ."
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              error={shown.username}
            />
            <Field
              id="password"
              label="Password"
              type="password"
              autoComplete="new-password"
              hint={`At least ${MIN_PASSWORD_LENGTH} characters.`}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              error={shown.password}
            />
          </>
        ) : (
          <InterestLevelFields
            interest={interest}
            level={level}
            onInterestChange={setInterest}
            onLevelChange={setLevel}
            disabled={loading}
          />
        )}

        <FormError message={error} />

        <div className="flex gap-3">
          {step === 2 && (
            <Button
              type="button"
              variant="outline"
              className="h-12 rounded-xl px-6"
              onClick={() => setStep(1)}
              disabled={loading}
            >
              Back
            </Button>
          )}
          <PrimaryButton type="submit" disabled={loading || (step === 2 && !interest)} className="flex-1">
            {step === 1 ? "Next →" : loading ? "Creating your account…" : "Start learning →"}
          </PrimaryButton>
        </div>
      </form>
    </AuthCard>
  );
}
