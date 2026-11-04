// Teacher account (/teacher/account): change the password set when the account
// was created on the server. The same rules as a student's password change —
// the current password is required, so a borrowed session can't lock the real
// owner out.

"use client";

import { useState, type FormEvent } from "react";
import { Button } from "@/components/ui/button";

import { Field, FormError } from "@/components/auth-card";
import { useAuth } from "@/components/auth-provider";
import { PageHeading } from "@/components/ui-kit";
import { changeTeacherPassword, friendlyMessage } from "@/lib/api";

const MIN_PASSWORD_LENGTH = 8; // mirrors src/auth/passwords.py; the API still checks

export default function TeacherAccountPage() {
  const { teacher } = useAuth();
  const [current, setCurrent] = useState("");
  const [next, setNext] = useState("");
  const [confirm, setConfirm] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saved, setSaved] = useState<string | null>(null);

  if (!teacher) return null; // RequireAuth guarantees a teacher

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setError(null);
    setSaved(null);
    if (next.length < MIN_PASSWORD_LENGTH) {
      return setError(`The new password needs at least ${MIN_PASSWORD_LENGTH} characters.`);
    }
    if (next !== confirm) return setError("The two new passwords don't match.");
    setSaving(true);
    try {
      await changeTeacherPassword(current, next);
      setCurrent("");
      setNext("");
      setConfirm("");
      setSaved("Password changed.");
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setSaving(false);
    }
  }

  return (
    <main className="page-shell w-full flex-1">
      <div className="mx-auto w-full flex max-w-xl flex-col gap-8">
        <PageHeading
          eyebrow="Account"
          title={teacher.name}
          description={`Logged in as ${teacher.username}`}
        />
        <form
          onSubmit={handleSubmit}
          className="flex flex-col gap-5 surface p-6"
        >
          <h2 className="display text-xl font-bold text-foreground">Change password</h2>
          <Field
            id="current-password"
            label="Current password"
            type="password"
            autoComplete="current-password"
            required
            value={current}
            onChange={(e) => setCurrent(e.target.value)}
            disabled={saving}
          />
          <Field
            id="new-password"
            label="New password"
            type="password"
            autoComplete="new-password"
            hint={`At least ${MIN_PASSWORD_LENGTH} characters.`}
            required
            value={next}
            onChange={(e) => setNext(e.target.value)}
            disabled={saving}
          />
          <Field
            id="confirm-password"
            label="New password again"
            type="password"
            autoComplete="new-password"
            required
            value={confirm}
            onChange={(e) => setConfirm(e.target.value)}
            disabled={saving}
          />
          <FormError message={error} />
          {saved && (
            <p role="status" className="text-sm font-medium text-success">
              {saved}
            </p>
          )}
          <Button type="submit" disabled={saving} className="self-start">
            {saving ? "Changing…" : "Change password"}
          </Button>
        </form>
      </div>
    </main>
  );
}
