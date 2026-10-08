// The teacher's view of the pilot's before → after: the starting check every
// student takes after signing up, against the end check the teacher opens for
// the class at the end. Every number is computed on the server
// (src/progress/metrics.py check_gains) over PAIRED answers only: the same
// concept, before and after, so a student who skipped one check doesn't skew it.
//
// "Studied vs not studied" is spelled out on the page because it is the honest
// reading of the result: if concepts students never opened improved as much as
// the ones they studied, the gain isn't the lessons'.

"use client";

import { useState } from "react";
import { Flag } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { pct } from "@/components/class-insights";
import { Button } from "@/components/ui/button";
import {
  friendlyMessage,
  getClassChecks,
  setClassEndCheck,
  type CheckTally,
  type ClassChecks,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

export function ClassChecksPanel({
  classId,
  onChanged,
}: {
  classId: string;
  onChanged?: () => void; // so the page's snapshot can refresh
}) {
  const loaded = useFetch(`checks:${classId}`, () => getClassChecks(classId));
  // After open/close, the response replaces what was loaded.
  const [updated, setUpdated] = useState<ClassChecks | null>(null);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const data = updated ?? loaded.data;

  async function toggle(open: boolean) {
    setSaving(true);
    setError(null);
    try {
      setUpdated(await setClassEndCheck(classId, open));
      onChanged?.();
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setSaving(false);
    }
  }

  if (!data) {
    return loaded.loading ? (
      <div className="h-32 animate-pulse rounded-xl bg-muted" aria-label="Loading the checks" />
    ) : (
      <FormError message={loaded.error ?? "Couldn't load the starting and end checks."} />
    );
  }

  const s = data.summary;
  const total = data.students.length;

  return (
    <section className="flex flex-col gap-5 rounded-xl border border-border bg-card p-6 shadow-card print:hidden">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div className="flex flex-col gap-1">
          <h2 className="flex items-center gap-2 text-lg font-bold text-foreground">
            <Flag className="size-5 text-brand-accent" aria-hidden /> Starting check → end check
          </h2>
          <p className="max-w-2xl text-sm text-muted-foreground">
            Every student takes the starting check when they sign up. Open the end check at the end of
            the course: the same ideas with new questions, so you see what changed.{" "}
            {data.open
              ? `Open since ${new Date(data.opened_at!).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" })}.`
              : "It is closed: students don't see it yet."}
          </p>
        </div>
        <Button
          variant={data.open ? "outline" : "default"}
          className="shrink-0 self-start"
          disabled={saving}
          onClick={() => toggle(!data.open)}
        >
          {saving ? "Saving…" : data.open ? "Close the end check" : "Open the end check"}
        </Button>
      </div>
      <FormError message={error} />

      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Tile label="Starting check" value={`${s.students_started} of ${total}`} note="students who took it" />
        <Tile label="End check" value={`${s.students_finished} of ${total}`} note="students who took it" />
        <Tile
          label="Right answers"
          value={s.paired_answers ? `${pct(s.right_before)} → ${pct(s.right_after)}` : "—"}
          note={s.paired_answers ? `over ${s.paired_answers} paired answers` : "after the end check"}
          good={(s.right_after ?? 0) > (s.right_before ?? 0)}
        />
        <Tile
          label="Mix-ups"
          value={s.paired_answers ? `${s.before.mix_up} → ${s.after.mix_up}` : "—"}
          note={s.paired_answers ? `${s.fixed} fixed · ${s.learned} learned · ${s.slipped} slipped` : "after the end check"}
          good={s.after.mix_up < s.before.mix_up}
        />
      </div>

      {s.paired_answers > 0 && (
        <>
          <p className="rounded-lg bg-muted/60 p-3 text-sm text-muted-foreground">
            <span className="font-semibold text-foreground">Studied vs not studied.</span> Ideas whose
            lesson the student opened: {pct(s.studied.right_before)} → {pct(s.studied.right_after)} right (
            {s.studied.pairs} answers). Ideas they didn&apos;t open: {pct(s.not_studied.right_before)} →{" "}
            {pct(s.not_studied.right_after)} ({s.not_studied.pairs}). If both rise alike, the gain isn&apos;t the
            lessons&apos;.
          </p>

          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-border text-left text-muted-foreground">
                  <th className="py-2 pr-4 font-semibold">Idea</th>
                  <th className="py-2 pr-4 font-semibold">Students</th>
                  <th className="py-2 pr-4 font-semibold">Right: before → after</th>
                  <th className="py-2 font-semibold">Mix-ups fixed</th>
                </tr>
              </thead>
              <tbody>
                {s.concepts.map((c) => (
                  <tr key={c.concept_id} className="border-b border-border/60">
                    <td className="py-2 pr-4">
                      <span className="font-medium text-foreground">{c.concept_name}</span>
                      {c.chapter_name && <span className="ml-2 text-xs text-muted-foreground">{c.chapter_name}</span>}
                    </td>
                    <td className="py-2 pr-4">{c.students}</td>
                    <td className="py-2 pr-4">
                      {pct(c.right_before)} →{" "}
                      <span className={cn((c.right_after ?? 0) > (c.right_before ?? 0) && "font-semibold text-success")}>
                        {pct(c.right_after)}
                      </span>
                    </td>
                    <td className="py-2">{c.fixed}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}

      {s.students_started > 0 && (
        <details className="group">
          <summary className="cursor-pointer text-sm font-semibold text-primary">Per student</summary>
          <div className="mt-3 overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-border text-left text-muted-foreground">
                  <th className="py-2 pr-4 font-semibold">Student</th>
                  <th className="py-2 pr-4 font-semibold">Starting check</th>
                  <th className="py-2 pr-4 font-semibold">End check</th>
                  <th className="py-2 font-semibold">Fixed</th>
                </tr>
              </thead>
              <tbody>
                {data.students.map((st) => (
                  <tr key={st.student_id} className="border-b border-border/60">
                    <td className="py-2 pr-4 font-medium text-foreground">{st.name}</td>
                    <td className="py-2 pr-4">{st.before ? <Tally t={st.before} /> : <Muted>Not taken</Muted>}</td>
                    <td className="py-2 pr-4">
                      {st.after ? <Tally t={st.after} /> : <Muted>{data.open ? "Not yet" : "—"}</Muted>}
                    </td>
                    <td className="py-2">{st.fixed ?? "—"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </details>
      )}
    </section>
  );
}

function Tile({ label, value, note, good }: { label: string; value: string; note: string; good?: boolean }) {
  return (
    <div className="rounded-xl border border-border bg-background p-4">
      <div className="text-sm text-muted-foreground">{label}</div>
      <div className={cn("mt-1 text-2xl font-bold text-foreground", good && "text-success")}>{value}</div>
      <div className="text-xs text-muted-foreground">{note}</div>
    </div>
  );
}

function Tally({ t }: { t: CheckTally }) {
  return (
    <span className="flex flex-wrap gap-x-2 gap-y-0.5 [&>span]:whitespace-nowrap">
      <span className="text-success">{t.right} right</span>
      <span className="text-destructive">{t.mix_up} mix-up{t.mix_up === 1 ? "" : "s"}</span>
      <span className="text-muted-foreground">{t.unsure} not sure</span>
    </span>
  );
}

function Muted({ children }: { children: React.ReactNode }) {
  return <span className="text-muted-foreground">{children}</span>;
}
