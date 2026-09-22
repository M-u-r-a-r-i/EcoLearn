// Login page (/login). A real <form>, so Enter submits and password managers
// recognise it. On success the API sets the session cookie and we go back to
// where the student was heading (?next=), or to their roadmap.

"use client";

import { Suspense, useEffect, useState, type FormEvent } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";

import { AuthCard, Field, FormError } from "@/components/auth-card";
import { useAuth } from "@/components/auth-provider";
import { PrimaryButton } from "@/components/primary-button";
import { friendlyMessage } from "@/lib/api";

// Only follow same-site paths ("/roadmap"), never "//evil.com" or a full URL —
// otherwise a crafted login link could bounce a student to another site.
function safeNext(next: string | null): string {
  return next && next.startsWith("/") && !next.startsWith("//") ? next : "/roadmap";
}

function LoginForm() {
  const { login, status } = useAuth();
  const router = useRouter();
  const next = safeNext(useSearchParams().get("next"));

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Already logged in (e.g. opened /login in a second tab)? Skip the form.
  useEffect(() => {
    if (status === "authenticated") router.replace(next);
  }, [status, router, next]);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault(); // stop the browser's own full-page form submit
    setError(null);
    setLoading(true);
    try {
      await login(username.trim(), password);
      router.replace(next);
    } catch (err) {
      setError(friendlyMessage(err));
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-5">
      <Field
        id="username"
        label="Username"
        autoComplete="username"
        autoCapitalize="none"
        spellCheck={false}
        required
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        disabled={loading}
      />
      <Field
        id="password"
        label="Password"
        type="password"
        autoComplete="current-password"
        required
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        disabled={loading}
      />
      <FormError message={error} />
      <PrimaryButton type="submit" disabled={loading} className="w-full">
        {loading ? "Logging in…" : "Log in"}
      </PrimaryButton>
      <p className="text-center text-xs text-muted-foreground">
        Forgot your password? Ask your teacher to reset it.
      </p>
    </form>
  );
}

export default function LoginPage() {
  return (
    <AuthCard
      eyebrow="Welcome back"
      title="Log in"
      subtitle="Pick up where you left off."
      footer={
        <>
          New here?{" "}
          <Link href="/signup" className="font-semibold text-primary hover:underline">
            Create an account
          </Link>
        </>
      }
    >
      {/* useSearchParams needs a Suspense boundary so the page can prerender. */}
      <Suspense>
        <LoginForm />
      </Suspense>
    </AuthCard>
  );
}
