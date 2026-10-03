// One class (/teacher/class?id=cls_...): every student with how far they've
// got, a password reset per student, and a form to add latecomers.
//
// The class id rides in the URL (like ?chapter= on the roadmap) so a refresh or
// a bookmark keeps the page. The API answers 404 for a class that isn't this
// teacher's, so a guessed id shows "not found" and nothing else.

"use client";

import { Suspense, useState, type FormEvent } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";

import { FormError } from "@/components/auth-card";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { SectionHeading } from "@/components/section-heading";
import { ClassInsightsPanel, pct } from "@/components/class-insights";
import { TeachingAssistant } from "@/components/teaching-assistant";
import { ClassStoriesPanel } from "@/components/class-stories";
import { ClassChecksPanel } from "@/components/class-checks";
import { AiDecisionsPanel } from "@/components/ai-decisions";
import { CredentialsSheet, InterestSelect, RosterField } from "@/components/teacher-ui";
import { Button } from "@/components/ui/button";
import {
  addStudents,
  friendlyMessage,
  getClassDetail,
  getClassInsights,
  resetStudentPassword,
  type ClassStudent,
  type StudentCredential,
  type StudentInsight,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";

export default function ClassPage() {
  // useSearchParams needs a Suspense boundary so the page can prerender.
  return (
    <Suspense>
      <ClassView />
    </Suspense>
  );
}

function lastActive(iso: string | null): string {
  if (!iso) return "Not started";
  return new Date(iso).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

function ClassView() {
  const classId = useSearchParams().get("id") ?? "";
  const [version, setVersion] = useState(0);
  const detail = useFetch(`class:${classId}:${version}`, () => getClassDetail(classId));
  // Loaded separately so a slow or failed insights query never hides the
  // student list (and the password resets a teacher may urgently need).
  const insights = useFetch(`insights:${classId}:${version}`, () => getClassInsights(classId));
  // Logins to show once: from a reset or from adding students.
  const [sheet, setSheet] = useState<{ title: string; credentials: StudentCredential[] } | null>(
    null,
  );

  const back = (
    <Link href="/teacher" className="text-sm font-semibold text-primary hover:underline print:hidden">
      ← All classes
    </Link>
  );

  if (detail.loading) {
    return (
      <main className="flex flex-1 flex-col">
        <PageContainer className="flex flex-col gap-4">
          {back}
          <div className="h-8 w-64 animate-pulse rounded-lg bg-muted" />
          <div className="h-60 animate-pulse rounded-xl bg-muted" />
        </PageContainer>
      </main>
    );
  }
  if (!detail.data) {
    return (
      <main className="flex flex-1 flex-col">
        <PageContainer className="flex flex-col gap-4">
          {back}
          <FormError message={detail.error ?? "Class not found."} />
        </PageContainer>
      </main>
    );
  }

  const { class: klass, students } = detail.data;
  const started = students.filter((s) => s.attempted > 0).length;

  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-col gap-8">
        {back}
        <div className="print:hidden">
          <SectionHeading
            eyebrow={klass.level}
            title={klass.name}
            subtitle={`${students.length} students · ${started} have started`}
          />
        </div>

        {sheet ? (
          <CredentialsSheet
            title={sheet.title}
            credentials={sheet.credentials}
            onDone={() => setSheet(null)}
            doneLabel="Back to the class"
          />
        ) : (
          <>
            <ClassChecksPanel classId={klass.class_id} />
            <TeachingAssistant classId={klass.class_id} />
            {insights.data ? (
              <ClassInsightsPanel insights={insights.data} />
            ) : insights.loading ? (
              <div className="h-40 animate-pulse rounded-xl bg-muted" aria-label="Loading class insights" />
            ) : (
              <FormError message={insights.error ?? "Couldn't load the class insights."} />
            )}
            <ClassStoriesPanel classId={klass.class_id} />
            <AiDecisionsPanel classId={klass.class_id} />
            <StudentTable
              students={students}
              insights={insights.data?.students ?? []}
              onReset={(credential) =>
                setSheet({ title: `New password for ${credential.name}`, credentials: [credential] })
              }
            />
            <AddStudentsForm
              classId={klass.class_id}
              onAdded={(credentials) => {
                setVersion((v) => v + 1);
                setSheet({
                  title: `${credentials.length} ${credentials.length === 1 ? "account" : "accounts"} added`,
                  credentials,
                });
              }}
            />
          </>
        )}
      </PageContainer>
    </main>
  );
}

function StudentTable({
  students,
  insights,
  onReset,
}: {
  students: ClassStudent[];
  insights: StudentInsight[];
  onReset: (credential: StudentCredential) => void;
}) {
  const metricsFor = new Map(insights.map((row) => [row.student_id, row]));
  // Two-step reset: the first click asks, the second does it. A reset makes the
  // student's old password stop working, so it shouldn't happen on a misclick.
  const [confirming, setConfirming] = useState<string | null>(null);
  const [busy, setBusy] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function reset(studentId: string) {
    setError(null);
    setBusy(studentId);
    try {
      onReset(await resetStudentPassword(studentId));
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setBusy(null);
      setConfirming(null);
    }
  }

  if (students.length === 0) {
    return <p className="text-sm text-muted-foreground">No students in this class yet.</p>;
  }

  return (
    <section className="flex flex-col gap-3 rounded-xl border border-border bg-card p-6 shadow-card">
      <h2 className="text-lg font-bold text-foreground">Students</h2>
      <FormError message={error} />
      <div className="relative overflow-x-auto">
        <table className="w-full text-left text-sm">
          <thead className="text-muted-foreground">
            <tr>
              <th className="py-2 pr-4 font-semibold">Name</th>
              <th className="py-2 pr-4 font-semibold">Username</th>
              <th className="py-2 pr-4 font-semibold">Interest</th>
              <th className="py-2 pr-4 font-semibold">Mastered</th>
              <th className="py-2 pr-4 font-semibold">Reading</th>
              <th className="py-2 pr-4 font-semibold">Right first time</th>
              <th className="py-2 pr-4 font-semibold">Last active</th>
              <th className="py-2 font-semibold">
                <span className="sr-only">Actions</span>
              </th>
            </tr>
          </thead>
          <tbody>
            {students.map((s) => {
              const m = metricsFor.get(s.student_id);
              return (
                <tr key={s.student_id} className="border-t border-border align-middle">
                  <td className="py-2 pr-4 font-medium text-foreground">{s.name}</td>
                  <td className="py-2 pr-4 font-mono">{s.username}</td>
                  <td className="py-2 pr-4 capitalize">{s.interest}</td>
                  <td className="py-2 pr-4">
                    {s.mastered}
                    <span className="text-muted-foreground"> of {s.attempted} tried</span>
                  </td>
                  <td className="py-2 pr-4">{m ? `${m.active_minutes} min` : "—"}</td>
                  <td className="py-2 pr-4">
                    {m && m.answered > 0 ? (
                      <>
                        {pct(m.first_try_accuracy)}
                        <span className="text-muted-foreground">
                          {" "}
                          ({m.first_try_correct} of {m.answered})
                        </span>
                      </>
                    ) : (
                      "—"
                    )}
                  </td>
                  <td className="py-2 pr-4 text-muted-foreground">{lastActive(s.last_active)}</td>
                  <td className="py-2 text-right">
                    {confirming === s.student_id ? (
                      <span className="inline-flex gap-2">
                        <Button
                          size="sm"
                          variant="destructive"
                          disabled={busy !== null}
                          onClick={() => reset(s.student_id)}
                        >
                          {busy === s.student_id ? "Resetting…" : "Yes, reset"}
                        </Button>
                        <Button
                          size="sm"
                          variant="ghost"
                          disabled={busy !== null}
                          onClick={() => setConfirming(null)}
                        >
                          Cancel
                        </Button>
                      </span>
                    ) : (
                      <Button
                        size="sm"
                        variant="outline"
                        disabled={busy !== null}
                        onClick={() => setConfirming(s.student_id)}
                      >
                        Reset password
                      </Button>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </section>
  );
}

function AddStudentsForm({
  classId,
  onAdded,
}: {
  classId: string;
  onAdded: (credentials: StudentCredential[]) => void;
}) {
  const [open, setOpen] = useState(false);
  const [interest, setInterest] = useState("");
  const [roster, setRoster] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setError(null);
    if (!roster.trim()) return setError("Add at least one student name.");
    setSaving(true);
    try {
      const result = await addStudents(classId, roster, interest);
      setRoster("");
      setOpen(false);
      onAdded(result.credentials);
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setSaving(false);
    }
  }

  if (!open) {
    return (
      <Button variant="outline" className="self-start" onClick={() => setOpen(true)}>
        Add students to this class
      </Button>
    );
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col gap-6 rounded-xl border border-border bg-card p-6 shadow-card"
    >
      <h2 className="text-lg font-bold text-foreground">Add students</h2>
      <InterestSelect value={interest} onChange={setInterest} disabled={saving} />
      <RosterField value={roster} onChange={setRoster} disabled={saving} />
      <FormError message={error} />
      <div className="flex gap-3">
        <PrimaryButton type="submit" disabled={saving}>
          {saving ? "Creating accounts…" : "Create accounts"}
        </PrimaryButton>
        <Button type="button" variant="ghost" disabled={saving} onClick={() => setOpen(false)}>
          Cancel
        </Button>
      </div>
    </form>
  );
}
