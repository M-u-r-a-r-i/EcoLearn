// Teacher login (/teacher/login). Same form as the student login, a different
// endpoint: teacher accounts live apart from student accounts, and each login
// only accepts its own kind. Teacher accounts are created on the server with
// scripts/create_teacher.py — there is no teacher signup page, on purpose.

"use client";

import { Suspense, useEffect, useState, type FormEvent } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";

import { AuthCard, Field, FormError } from "@/components/auth-card";
import { HOME, useAuth } from "@/components/auth-provider";
import { PrimaryButton } from "@/components/primary-button";
import { friendlyMessage } from "@/lib/api";

// Only follow same-site teacher paths, never "//evil.com" or a full URL.
function safeNext(next: string | null): string {
  return next && next.startsWith("/teacher") ? next : HOME.teacher;
}

function TeacherLoginForm() {
  const { teacherLogin, status, role } = useAuth();
  const router = useRouter();
  const next = safeNext(useSearchParams().get("next"));

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (status === "authenticated" && role) router.replace(role === "teacher" ? next : HOME[role]);
  }, [status, role, router, next]);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setError(null);
    setLoading(true);
    try {
      await teacherLogin(username.trim(), password);
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
        label="Teacher username"
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
        Need a teacher account? Ask whoever runs EcoLearn at your school.
      </p>
    </form>
  );
}

export default function TeacherLoginPage() {
  return (
    <AuthCard
      eyebrow="For teachers"
      title="Teacher login"
      subtitle="Set up your classes and help students back into their accounts."
      footer={
        <>
          A student?{" "}
          <Link href="/login" className="font-semibold text-primary hover:underline">
            Student login
          </Link>
        </>
      }
    >
      <Suspense>
        <TeacherLoginForm />
      </Suspense>
    </AuthCard>
  );
}
