// Pieces shared by the teacher pages: form controls styled like <Input>, the
// roster-entry fields, and the sheet that shows freshly created logins.
//
// THE CREDENTIALS SHEET is the one place a generated password is ever visible.
// The server stores only its hash, so once the teacher leaves this screen the
// password is gone for good (a lost slip means "reset password", not "look it
// up"). Hence the warning, and a Print button that prints ONLY the slips —
// everything else on the page is marked print:hidden.

"use client";

import { useEffect, useState } from "react";

import { LEVELS } from "@/components/interest-level-fields";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";
import { friendlyMessage, getInterests, type Interest, type StudentCredential } from "@/lib/api";
import { cn } from "@/lib/utils";

// Same look as components/ui/input.tsx, for <select> and <textarea>.
export const CONTROL =
  "w-full min-w-0 rounded-lg border border-input bg-transparent px-2.5 py-1.5 text-base outline-none " +
  "transition-colors placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-3 " +
  "focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm dark:bg-input/30";

const LABEL = "text-sm font-semibold text-foreground";

export function InterestSelect({
  value,
  onChange,
  disabled,
  label = "Default interest",
  hint = "Students can change it later in Settings.",
}: {
  value: string;
  onChange: (id: string) => void;
  disabled?: boolean;
  label?: string;
  hint?: string;
}) {
  const [interests, setInterests] = useState<Interest[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getInterests().then(
      (list) => {
        setInterests(list);
        if (list.length > 0 && !list.some((i) => i.id === value)) onChange(list[0].id);
      },
      (err) => setError(friendlyMessage(err)),
    );
    // The list doesn't change while the form is open.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="flex flex-col gap-2">
      <label htmlFor="interest" className={LABEL}>
        {label}
      </label>
      <select
        id="interest"
        className={cn(CONTROL, "h-9")}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={disabled || interests === null}
      >
        {interests === null && <option value="">Loading…</option>}
        {interests?.map((i) => (
          <option key={i.id} value={i.id}>
            {i.emoji} {i.label} — {i.chapters_ready} of {i.chapters_total} chapters ready
          </option>
        ))}
      </select>
      {error ? (
        <p className="text-sm text-destructive">{error}</p>
      ) : (
        <p className="text-xs text-muted-foreground">{hint}</p>
      )}
    </div>
  );
}

export function LevelSelect({
  value,
  onChange,
  disabled,
}: {
  value: string;
  onChange: (level: string) => void;
  disabled?: boolean;
}) {
  return (
    <div className="flex flex-col gap-2">
      <label htmlFor="level" className={LABEL}>
        Class
      </label>
      <select
        id="level"
        className={cn(CONTROL, "h-9")}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={disabled}
      >
        {LEVELS.map((l) => (
          <option key={l} value={l}>
            {l}
          </option>
        ))}
      </select>
    </div>
  );
}

export function RosterField({
  value,
  onChange,
  disabled,
}: {
  value: string;
  onChange: (text: string) => void;
  disabled?: boolean;
}) {
  const count = value.split("\n").filter((line) => line.trim()).length;
  return (
    <div className="flex flex-col gap-2">
      <label htmlFor="roster" className={LABEL}>
        Student names{" "}
        <span className="font-normal text-muted-foreground">
          ({count} {count === 1 ? "student" : "students"})
        </span>
      </label>
      <textarea
        id="roster"
        rows={8}
        className={cn(CONTROL, "font-mono")}
        placeholder={"Aarav Kumar\nMeera Iyer\nKabir Singh, cricket"}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={disabled}
      />
      <p className="text-xs text-muted-foreground">
        One name per line — paste straight from a spreadsheet. To give one student a different
        interest, add it after a comma: <span className="font-mono">Kabir Singh, cricket</span>.
        Up to 60 at a time.
      </p>
    </div>
  );
}

export function CredentialsSheet({
  title,
  credentials,
  onDone,
  doneLabel = "Done",
}: {
  title: string;
  credentials: StudentCredential[];
  onDone: () => void;
  doneLabel?: string;
}) {
  // Where students log in, printed on every slip. Read once on mount — this
  // component only ever renders in the browser, after a teacher's action.
  const [loginUrl] = useState(() =>
    typeof window === "undefined" ? "/login" : `${window.location.origin}/login`,
  );

  return (
    <section className="flex flex-col gap-6">
      <div className="flex flex-col gap-4 rounded-xl border border-border bg-card p-6 shadow-card print:hidden">
        <h2 className="text-lg font-bold text-foreground">{title}</h2>
        <p
          role="alert"
          className="rounded-xl border border-brand-accent/40 bg-brand-accent/10 px-4 py-3 text-sm text-foreground"
        >
          <strong>Print or write these down now.</strong>{" "}For the students&apos; safety EcoLearn
          keeps only a scrambled copy of each password, so this is the only time they can be
          shown. If a slip gets lost, use <em>Reset password</em> on the class page.
        </p>
        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="text-muted-foreground">
              <tr>
                <th className="py-2 pr-4 font-semibold">Name</th>
                <th className="py-2 pr-4 font-semibold">Username</th>
                <th className="py-2 font-semibold">Password</th>
              </tr>
            </thead>
            <tbody>
              {credentials.map((c) => (
                <tr key={c.student_id} className="border-t border-border">
                  <td className="py-2 pr-4">{c.name}</td>
                  <td className="py-2 pr-4 font-mono">{c.username}</td>
                  <td className="py-2 font-mono">{c.password}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="flex flex-wrap gap-3">
          <PrimaryButton type="button" onClick={() => window.print()}>
            Print sign-in slips
          </PrimaryButton>
          <Button type="button" variant="outline" onClick={onDone}>
            {doneLabel}
          </Button>
        </div>
      </div>

      {/* Printed only: one cut-out slip per student, two per row. */}
      <div className="hidden grid-cols-2 gap-4 print:grid">
        {credentials.map((c) => (
          <div
            key={c.student_id}
            className="break-inside-avoid rounded-lg border-2 border-dashed border-gray-400 p-4 text-black"
          >
            <p className="text-base font-bold">{c.name}</p>
            <p className="mt-1 text-xs">EcoLearn — log in at {loginUrl}</p>
            <p className="mt-3 text-sm">
              Username: <span className="font-mono font-bold">{c.username}</span>
            </p>
            <p className="text-sm">
              Password: <span className="font-mono font-bold">{c.password}</span>
            </p>
            <p className="mt-2 text-xs">You can change your password in Settings.</p>
          </div>
        ))}
      </div>
    </section>
  );
}
