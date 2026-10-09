// The interest + class choosers, shared by signup and (later) settings.
//
// Interests come from GET /api/interests, so promoting an interest from "draft"
// to "active" in data/interests.yaml makes it appear here with no code change.
// Chips in a wrapping grid, so 2 interests or 20 both lay out well.

"use client";

import { useEffect, useState } from "react";
import { Check } from "lucide-react";

import { InterestMark } from "@/components/ui-kit";

import { friendlyMessage, getInterests, type Interest } from "@/lib/api";
import { cn } from "@/lib/utils";

export const LEVELS = ["Class 11", "Class 12"] as const;

interface Props {
  interest: string;
  level: string;
  onInterestChange: (id: string) => void;
  onLevelChange: (level: string) => void;
  disabled?: boolean;
  // Settings shows the class but only a teacher can change it.
  levelLocked?: boolean;
}

export function InterestLevelFields({
  interest,
  level,
  onInterestChange,
  onLevelChange,
  disabled,
  levelLocked,
}: Props) {
  const [interests, setInterests] = useState<Interest[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getInterests().then(
      (list) => {
        setInterests(list);
        // Pick the first one if nothing valid is selected yet.
        if (list.length > 0 && !list.some((i) => i.id === interest)) onInterestChange(list[0].id);
      },
      (err) => setError(friendlyMessage(err)),
    );
    // Run once: the list doesn't change while the form is open.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <fieldset className="field-group" disabled={disabled}>
        <legend>Learn through…</legend>
        {error && <p className="form-error">{error}</p>}
        <div className="interest-pick-grid">
          {interests === null && !error
            ? Array.from({ length: 2 }, (_, i) => (
                <div key={i} className="h-16 animate-pulse rounded-xl bg-muted" />
              ))
            : interests?.map((opt) => (
                <button
                  key={opt.id}
                  type="button"
                  aria-pressed={interest === opt.id}
                  onClick={() => onInterestChange(opt.id)}
                  title={opt.description}
                  className={cn("interest-pick", interest === opt.id && "active")}
                  style={{ minHeight: 64 }}
                >
                  <InterestMark id={opt.id} emoji={opt.emoji} />
                  <span className="flex min-w-0 flex-col text-left">
                    <span className="text-[13px] font-bold leading-tight text-foreground">{opt.label}</span>
                    {/* Say how much is written, rather than hiding half-done
                        interests: a student can pick one and see the rest arrive. */}
                    <span className="text-[11px] font-medium leading-tight text-muted-foreground">
                      {opt.chapters_ready === opt.chapters_total
                        ? "All chapters ready"
                        : `${opt.chapters_ready} of ${opt.chapters_total} chapters`}
                    </span>
                  </span>
                  {interest === opt.id && <Check size={15} aria-hidden />}
                </button>
              ))}
        </div>
      </fieldset>

      <fieldset className="field-group" disabled={disabled}>
        <legend>Your class</legend>
        {levelLocked ? (
          <p className="text-sm text-muted-foreground">
            <span className="font-semibold text-foreground">{level}</span> · only your teacher can
            change your class.
          </p>
        ) : (
          <div className="grade-picks">
            {LEVELS.map((opt) => (
              <button
                key={opt}
                type="button"
                aria-pressed={level === opt}
                onClick={() => onLevelChange(opt)}
                className={cn("grade-pick", level === opt && "active")}
              >
                {opt}
              </button>
            ))}
          </div>
        )}
      </fieldset>
    </>
  );
}
