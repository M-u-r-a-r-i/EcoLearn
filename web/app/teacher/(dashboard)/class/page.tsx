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
import { BarChart3, Bot, Flag, Users } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { Meter, PageHeading, Skeleton } from "@/components/ui-kit";
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
  setStudentLevel,
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

type TabId = "overview" | "insights" | "ai" | "students";
const TABS: { id: TabId; label: string; Icon: typeof Flag }[] = [
  { id: "overview", label: "Overview", Icon: Flag },
  { id: "insights", label: "Insights", Icon: BarChart3 },
  { id: "ai", label: "Stories & AI", Icon: Bot },
  { id: "students", label: "Students", Icon: Users },
];

function lastActive(iso: string | null): string {
  if (!iso) return "Not started";
  return new Date(iso).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

function ClassView() {
  const classId = useSearchParams().get("id") ?? "";
  const [version, setVersion] = useState(0);
  const [tab, setTab] = useState<TabId>("overview");
  const detail = useFetch(`class:${classId}:${version}`, () => getClassDetail(classId));
  // Loaded separately so a slow or failed insights query never hides the
  // student list (and the password resets a teacher may urgently need).
  const insights = useFetch(`insights:${classId}:${version}`, () => getClassInsights(classId));
  // Logins to show once: from a reset or from adding students.
  const [sheet, setSheet] = useState<{ title: string; credentials: StudentCredential[] } | null>(
    null,
  );

  const back = (
    <Link href="/teacher" className="back-link text-primary print:hidden">
      ← All classes
    </Link>
  );

  if (detail.loading) {
    return (
      <main className="page-shell w-full flex-1">
        <div className="mx-auto w-full flex flex-col gap-4">
          {back}
          <div className="surface">
            <Skeleton rows={6} />
          </div>
        </div>
      </main>
    );
  }
  if (!detail.data) {
    return (
      <main className="page-shell w-full flex-1">
        <div className="mx-auto w-full flex flex-col gap-4">
          {back}
          <FormError message={detail.error ?? "Class not found."} />
        </div>
      </main>
    );
  }

  const { class: klass, students } = detail.data;
  const started = students.filter((s) => s.attempted > 0).length;

  return (
    <main className="page-shell w-full flex-1">
      <div className="mx-auto w-full flex flex-col gap-8">
        {back}
        <div className="print:hidden">
          <PageHeading
            eyebrow={klass.level}
            title={klass.name}
            description={`${students.length} students · ${started} have started`}
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
            <div className="dash-tabs print:hidden" role="tablist" aria-label="Class dashboard">
              {TABS.map((t) => (
                <button
                  key={t.id}
                  type="button"
                  role="tab"
                  id={`tab-${t.id}`}
                  aria-selected={tab === t.id}
                  aria-controls="dash-panel"
                  className="dash-tab"
                  onClick={() => setTab(t.id)}
                >
                  <t.Icon size={15} aria-hidden /> {t.label}
                </button>
              ))}
            </div>
            <div id="dash-panel" role="tabpanel" aria-labelledby={`tab-${tab}`} className="flex flex-col gap-8">
              {tab === "overview" && (
                <>
                  <ClassChecksPanel classId={klass.class_id} />
                  <TeachingAssistant classId={klass.class_id} />
                </>
              )}
              {tab === "insights" &&
                (insights.data ? (
                  <ClassInsightsPanel insights={insights.data} />
                ) : insights.loading ? (
                  <div className="surface">
                    <Skeleton rows={4} />
                  </div>
                ) : (
                  <FormError message={insights.error ?? "Couldn't load the class insights."} />
                ))}
              {tab === "ai" && (
                <>
                  <ClassStoriesPanel classId={klass.class_id} />
                  <AiDecisionsPanel classId={klass.class_id} />
                </>
              )}
              {tab === "students" && (
                <>
                  <StudentTable
                    students={students}
                    insights={insights.data?.students ?? []}
                    onReset={(credential) =>
                      setSheet({ title: `New password for ${credential.name}`, credentials: [credential] })
                    }
                    onLevelChanged={() => setVersion((v) => v + 1)}
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
            </div>
          </>
        )}
      </div>
    </main>
  );
}

function StudentTable({
  students,
  insights,
  onReset,
  onLevelChanged,
}: {
  students: ClassStudent[];
  insights: StudentInsight[];
  onReset: (credential: StudentCredential) => void;
  onLevelChanged: () => void;
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

  // Only a teacher can move a student between Class 11 and Class 12.
  async function changeLevel(studentId: string, level: string) {
    setError(null);
    setBusy(studentId);
    try {
      await setStudentLevel(studentId, level);
      onLevelChanged();
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setBusy(null);
    }
  }

  if (students.length === 0) {
    return <p className="text-sm text-muted-foreground">No students in this class yet.</p>;
  }

  return (
    <section className="surface panel flex flex-col gap-4">
      <div className="dash-title">
        <div>
          <p className="eyebrow">Your classroom</p>
          <h2 className="display text-2xl font-semibold text-foreground">Students</h2>
        </div>
        <span className="tag">{students.length} students</span>
      </div>
      <FormError message={error} />
      <div className="dtable-wrap">
        <table className="dtable">
          <thead>
            <tr>
              <th>Student</th>
              <th>Interest</th>
              <th>Class</th>
              <th>Mastered</th>
              <th>Reading</th>
              <th>Right first time</th>
              <th>Last active</th>
              <th>
                <span className="sr-only">Actions</span>
              </th>
            </tr>
          </thead>
          <tbody>
            {students.map((s) => {
              const m = metricsFor.get(s.student_id);
              const initials = s.name
                .split(/\s+/)
                .map((w) => w[0])
                .slice(0, 2)
                .join("")
                .toUpperCase();
              return (
                <tr key={s.student_id}>
                  <td>
                    <span className="dstudent">
                      <span className="davatar" aria-hidden>
                        {initials}
                      </span>
                      <span>
                        <b>{s.name}</b>
                        <small>{s.username}</small>
                      </span>
                    </span>
                  </td>
                  <td data-label="Interest">
                    <span className="dchip">{s.interest}</span>
                  </td>
                  <td data-label="Class">
                    <select
                      aria-label={`Class for ${s.name}`}
                      value={s.level}
                      disabled={busy !== null}
                      onChange={(e) => changeLevel(s.student_id, e.target.value)}
                      className="h-9 rounded-xl border border-input bg-card px-2 text-sm"
                    >
                      <option value="Class 11">Class 11</option>
                      <option value="Class 12">Class 12</option>
                    </select>
                  </td>
                  <td data-label="Mastered">
                    <span className="dprog">
                      <span>
                        <b>{s.mastered}</b>
                        <span className="text-muted-foreground"> of {s.attempted} tried</span>
                      </span>
                      <Meter value={s.mastered} max={Math.max(s.attempted, 1)} label={`${s.name}: ${s.mastered} mastered`} />
                    </span>
                  </td>
                  <td data-label="Reading">{m ? `${m.active_minutes} min` : "—"}</td>
                  <td data-label="Right first time">
                    {m && m.answered > 0 ? (
                      <>
                        <span className={m.first_try_accuracy === null ? "" : m.first_try_accuracy >= 0.7 ? "tone-good" : m.first_try_accuracy >= 0.4 ? "tone-mid" : "tone-bad"}>
                          {pct(m.first_try_accuracy)}
                        </span>
                        <span className="text-muted-foreground">
                          {" "}
                          ({m.first_try_correct} of {m.answered})
                        </span>
                      </>
                    ) : (
                      "—"
                    )}
                  </td>
                  <td data-label="Last active" className="text-muted-foreground">
                    {lastActive(s.last_active)}
                  </td>
                  <td className="actions text-right">
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
      className="flex flex-col gap-6 surface p-6"
    >
      <h2 className="display text-xl font-bold text-foreground">Add students</h2>
      <InterestSelect value={interest} onChange={setInterest} disabled={saving} />
      <RosterField value={roster} onChange={setRoster} disabled={saving} />
      <FormError message={error} />
      <div className="flex gap-3">
        <Button type="submit" disabled={saving}>
          {saving ? "Creating accounts…" : "Create accounts"}
        </Button>
        <Button type="button" variant="ghost" disabled={saving} onClick={() => setOpen(false)}>
          Cancel
        </Button>
      </div>
    </form>
  );
}
