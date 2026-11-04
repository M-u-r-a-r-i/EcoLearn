// Teacher home (/teacher): the teacher's classes, and a form to create a new
// class from a list of names. Creating a class shows every new login once, with
// printable slips (CredentialsSheet), then returns here.

"use client";

import { useState, type FormEvent } from "react";
import Link from "next/link";
import { ArrowRight, Users } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Field, FormError } from "@/components/auth-card";
import { useAuth } from "@/components/auth-provider";
import { PageHeading, Skeleton } from "@/components/ui-kit";
import {
  CredentialsSheet,
  InterestSelect,
  LevelSelect,
  RosterField,
} from "@/components/teacher-ui";
import {
  createClass,
  friendlyMessage,
  getClasses,
  type ClassSummary,
  type CredentialsResult,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";

export default function TeacherHomePage() {
  const { teacher } = useAuth();
  // Bumped after a class is created, so the list re-fetches.
  const [version, setVersion] = useState(0);
  const classes = useFetch(`classes:${version}`, getClasses);
  const [created, setCreated] = useState<CredentialsResult | null>(null);

  if (!teacher) return null; // RequireAuth guarantees a teacher

  return (
    <main className="page-shell w-full flex-1">
      <div className="teacher-home mx-auto flex w-full flex-col gap-8">
        <div className="print:hidden">
          <PageHeading
            eyebrow="Teacher"
            title={`Welcome, ${teacher.name}`}
            description="Create a class from your list of students, print their sign-in slips, and reset a password when someone forgets theirs."
          />
        </div>

        {created ? (
          <CredentialsSheet
            title={`${created.class.name}: ${created.credentials.length} accounts created`}
            credentials={created.credentials}
            onDone={() => setCreated(null)}
            doneLabel="Back to my classes"
          />
        ) : (
          <>
            <ClassList classes={classes.data} error={classes.error} loading={classes.loading} />
            <NewClassForm
              onCreated={(result) => {
                setCreated(result);
                setVersion((v) => v + 1);
              }}
            />
          </>
        )}
      </div>
    </main>
  );
}

function ClassList({
  classes,
  error,
  loading,
}: {
  classes: ClassSummary[] | null;
  error: string | null;
  loading: boolean;
}) {
  return (
    <section className="flex flex-col gap-4">
      <p className="eyebrow">Your classes</p>
      {loading && (
        <div className="surface">
          <Skeleton rows={2} />
        </div>
      )}
      {error && <FormError message={error} />}
      {classes && classes.length === 0 && (
        <p className="text-sm text-muted-foreground">
          No classes yet. Create your first one below.
        </p>
      )}
      {classes && classes.length > 0 && (
        <ul className="class-grid">
          {classes.map((c) => (
            <li key={c.class_id}>
              <Link
                href={`/teacher/class?id=${encodeURIComponent(c.class_id)}`}
                className="surface class-card card-hover"
              >
                <div className="class-card-head">
                  <span className="class-art-icon" aria-hidden>
                    <Users size={20} />
                  </span>
                  <span className="tag">{c.level}</span>
                </div>
                <h2 className="display">{c.name}</h2>
                <p>Open the dashboard</p>
                <div className="class-card-footer">
                  <span>
                    <Users size={13} aria-hidden /> {c.student_count}{" "}
                    {c.student_count === 1 ? "student" : "students"}
                  </span>
                  <ArrowRight className="class-arrow" size={16} aria-hidden />
                </div>
              </Link>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}

function NewClassForm({ onCreated }: { onCreated: (result: CredentialsResult) => void }) {
  const [name, setName] = useState("");
  const [level, setLevel] = useState("Class 11");
  const [interest, setInterest] = useState("");
  const [roster, setRoster] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setError(null);
    if (!name.trim()) return setError("Give the class a name, e.g. “11-B Physics”.");
    if (!roster.trim()) return setError("Add at least one student name.");
    setSaving(true);
    try {
      onCreated(await createClass({ name: name.trim(), level, interest, roster }));
      setName("");
      setRoster("");
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setSaving(false);
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="surface flex flex-col gap-6 p-6"
    >
      <h2 className="display text-xl font-bold text-foreground">Create a class</h2>
      <div className="grid gap-6 sm:grid-cols-2">
        <Field
          id="class-name"
          label="Class name"
          placeholder="11-B Physics"
          value={name}
          onChange={(e) => setName(e.target.value)}
          disabled={saving}
        />
        <LevelSelect value={level} onChange={setLevel} disabled={saving} />
      </div>
      <InterestSelect value={interest} onChange={setInterest} disabled={saving} />
      <RosterField value={roster} onChange={setRoster} disabled={saving} />
      <FormError message={error} />
      <Button type="submit" disabled={saving} className="self-start">
        {saving ? "Creating accounts… (a few seconds)" : "Create class and accounts"}
      </Button>
    </form>
  );
}
