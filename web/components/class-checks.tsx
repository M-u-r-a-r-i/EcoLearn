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
import { Flag, Sparkles, Target, Users } from "lucide-react";

import { FormError } from "@/components/auth-card";
import { pct } from "@/components/class-insights";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui-kit";
import {
  friendlyMessage,
  getClassChecks,
  setClassEndCheck,
  type CheckTally,
  type ClassChecks,
} from "@/lib/api";
import { useFetch } from "@/lib/use-fetch";
import { cn } from "@/lib/utils";

export function ClassChecksPanel({ classId }: { classId: string }) {
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
    } catch (err) {
      setError(friendlyMessage(err));
    } finally {
      setSaving(false);
    }
  }

  if (!data) {
    return loaded.loading ? (
      <div className="surface">
        <Skeleton rows={3} />
      </div>
    ) : (
      <FormError message={loaded.error ?? "Couldn't load the starting and end checks."} />
    );
  }

  const s = data.summary;
  const total = data.students.length;

  return (
    <section className="surface panel flex flex-col gap-6 print:hidden">
      <div className="dash-title">
        <div>
          <p className="eyebrow flex items-center gap-2">
            <Flag className="size-3.5" aria-hidden /> Before and after
          </p>
          <h2 className="display text-2xl font-semibold text-foreground">Starting check → end check</h2>
          <p className="dash-sub">
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

      <div className="dash-metrics">
        <Tile
          Icon={Users}
          tone="peach"
          label="Starting check"
          value={`${s.students_started} of ${total}`}
          note="students who took it"
        />
        <Tile
          Icon={Flag}
          tone="mint"
          label="End check"
          value={`${s.students_finished} of ${total}`}
          note="students who took it"
        />
        <Tile
          Icon={Target}
          tone="sky"
          label="Right answers"
          value={s.paired_answers ? `${pct(s.right_before)} → ${pct(s.right_after)}` : "—"}
          note={s.paired_answers ? `over ${s.paired_answers} paired answers` : "after the end check"}
          good={(s.right_after ?? 0) > (s.right_before ?? 0)}
        />
        <Tile
          Icon={Sparkles}
          tone="lav"
          label="Mix-ups"
          value={s.paired_answers ? `${s.before.mix_up} → ${s.after.mix_up}` : "—"}
          note={s.paired_answers ? `${s.fixed} fixed · ${s.learned} learned · ${s.slipped} slipped` : "after the end check"}
          good={s.after.mix_up < s.before.mix_up}
        />
      </div>

      {s.paired_answers > 0 && (
        <>
          <div className="flex flex-col gap-4">
            <div className="dash-title">
              <h3 className="display text-lg font-bold text-foreground">Ideas getting clearer</h3>
              <span className="dbar-legend">
                <span>
                  <i style={{ background: "var(--bar-before)" }} />
                  Before
                </span>
                <span>
                  <i style={{ background: "var(--bar-after)" }} />
                  After
                </span>
              </span>
            </div>
            <div className="dbars">
              {s.concepts
                .filter((c) => c.right_before !== null && c.right_after !== null)
                .slice(0, 8)
                .map((c) => (
                  <div key={c.concept_id} className="dbar-row">
                    <div className="dbar-name">
                      <span>{c.concept_name}</span>
                      <small>{c.students} students</small>
                    </div>
                    {(["before", "after"] as const).map((when) => {
                      const v = when === "before" ? c.right_before : c.right_after;
                      return (
                        <div key={when} className="dbar">
                          <div className="dbar-track" role="img" aria-label={`${when}: ${pct(v)} right`}>
                            <span className={`dbar-fill ${when}`} style={{ width: pct(v) }} />
                          </div>
                          <span className="dbar-pct">{pct(v)}</span>
                        </div>
                      );
                    })}
                  </div>
                ))}
            </div>
          </div>

          <p className="soft-surface p-4 text-sm leading-relaxed text-muted-foreground">
            <span className="font-semibold text-foreground">Studied vs not studied.</span> Ideas whose
            lesson the student opened: {pct(s.studied.right_before)} → {pct(s.studied.right_after)} right (
            {s.studied.pairs} answers). Ideas they didn&apos;t open: {pct(s.not_studied.right_before)} →{" "}
            {pct(s.not_studied.right_after)} ({s.not_studied.pairs}). If both rise alike, the gain isn&apos;t the
            lessons&apos;.
          </p>

          <details className="group">
            <summary className="cursor-pointer text-sm font-semibold text-primary">Idea by idea (table)</summary>
          <div className="dtable-wrap mt-3">
            <table className="dtable">
              <thead>
                <tr>
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
          </details>
        </>
      )}

      {s.students_started > 0 && (
        <details className="group">
          <summary className="cursor-pointer text-sm font-semibold text-primary">Per student</summary>
          <div className="dtable-wrap mt-3">
            <table className="dtable">
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

function Tile({
  Icon,
  tone,
  label,
  value,
  note,
  good,
}: {
  Icon: typeof Users;
  tone: string;
  label: string;
  value: string;
  note: string;
  good?: boolean;
}) {
  return (
    <div className={cn("surface dash-metric", `tone-${tone}`)}>
      <div className="dash-metric-top">
        <span className="dash-icon" aria-hidden>
          <Icon />
        </span>
        <span className="dash-label">{label}</span>
      </div>
      <span className={cn("dash-value", good && "good")}>{value}</span>
      <span className="dash-note">{note}</span>
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
