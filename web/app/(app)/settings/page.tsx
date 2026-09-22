// Settings page (/settings) — change name, interest and class, and the password.
//
// Two independent forms, each with its own saving state and message, so a
// failed password change never throws away an edited profile (and vice versa).
// Interest and class use the same fields as signup (InterestLevelFields).

"use client";

import { useState, type FormEvent } from "react";

import { Field, FormError } from "@/components/auth-card";
import { useAuth } from "@/components/auth-provider";
import { InterestLevelFields } from "@/components/interest-level-fields";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { SectionHeading } from "@/components/section-heading";
import { changePassword, friendlyMessage, updateProfile } from "@/lib/api";

const MIN_PASSWORD_LENGTH = 8; // mirrors src/auth/passwords.py; the API still checks

export default function SettingsPage() {
  const { student } = useAuth();
  if (!student) return null; // RequireAuth guarantees a student

  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex max-w-xl flex-col gap-8">
        <SectionHeading
          eyebrow="Settings"
          title="Your account"
          subtitle={student.username ? `Logged in as ${student.username}` : undefined}
        />
        <ProfileForm />
        <PasswordForm />
      </PageContainer>
    </main>
  );
}

function Saved({ message }: { message: string | null }) {
  if (!message) return null;
  return (
    <p role="status" className="text-sm font-medium text-success">
      {message}
    </p>
  );
}

function ProfileForm() {
  const { student, setStudent } = useAuth();
  const [name, setName] = useState(student?.name ?? "");
  const [interest, setInterest] = useState(student?.interest ?? "");
  const [level, setLevel] = useState(student?.level ?? "Class 11");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saved, setSaved] = useState<string | null>(null);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setError(null);
    setSaved(null);
    if (!name.trim()) {
      setError("Please enter your name.");
      return;
    }
    setSaving(true);
    try {
      setStudent(await updateProfile({ name: name.trim(), interest, level }));
      setSaved("Saved. Your lessons now follow your new choices.");
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setSaving(false);
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col gap-6 rounded-xl border border-border bg-card p-6 shadow-card"
    >
      <h2 className="text-lg font-bold text-foreground">Profile</h2>
      <Field
        id="name"
        label="Your name"
        autoComplete="given-name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        disabled={saving}
      />
      <InterestLevelFields
        interest={interest}
        level={level}
        onInterestChange={setInterest}
        onLevelChange={setLevel}
        disabled={saving}
      />
      <FormError message={error} />
      <Saved message={saved} />
      <PrimaryButton type="submit" disabled={saving} className="self-start">
        {saving ? "Saving…" : "Save changes"}
      </PrimaryButton>
    </form>
  );
}

function PasswordForm() {
  const [current, setCurrent] = useState("");
  const [next, setNext] = useState("");
  const [confirm, setConfirm] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saved, setSaved] = useState<string | null>(null);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setError(null);
    setSaved(null);
    if (next.length < MIN_PASSWORD_LENGTH) {
      setError(`The new password needs at least ${MIN_PASSWORD_LENGTH} characters.`);
      return;
    }
    if (next !== confirm) {
      setError("The two new passwords don't match.");
      return;
    }
    setSaving(true);
    try {
      await changePassword(current, next);
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
    <form
      onSubmit={handleSubmit}
      className="flex flex-col gap-5 rounded-xl border border-border bg-card p-6 shadow-card"
    >
      <h2 className="text-lg font-bold text-foreground">Change password</h2>
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
      <Saved message={saved} />
      <PrimaryButton type="submit" disabled={saving} className="self-start">
        {saving ? "Changing…" : "Change password"}
      </PrimaryButton>
    </form>
  );
}
