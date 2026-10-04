// Pick a chapter from the whole syllabus, grouped by class and unit.
//
// A native <select> with one <optgroup> per "Class · unit": keyboard- and
// screen-reader-friendly for free, and on phones it opens the OS picker, which
// handles 29 chapters better than any custom dropdown.
//
// Lessons are written interest by interest, so not every chapter has lessons
// for every student yet. Chapters with none stay in the list — the whole
// syllabus is visible, which is honest about where the project is — but as
// disabled "coming soon" options, so nobody walks into an empty chapter.
// Partly written chapters say how much is ready.

"use client";

import type { Chapter } from "@/lib/api";

function optionLabel(chapter: Chapter): string {
  const ready = chapter.lessons_ready;
  if (ready === undefined || ready === chapter.concept_count) return chapter.name;
  if (ready === 0) return `${chapter.name} — coming soon`;
  return `${chapter.name} (${ready} of ${chapter.concept_count} lessons ready)`;
}

export function ChapterPicker({
  chapters,
  value,
  onChange,
  interest,
}: {
  chapters: Chapter[] | null;
  value: string;
  onChange: (id: string) => void;
  interest?: string;
}) {
  if (chapters === null) {
    return <div className="h-10 w-full max-w-sm animate-pulse rounded-lg bg-muted" />;
  }
  if (chapters.length === 0) return null; // list failed to load: keep the current chapter

  // Chapters arrive in teaching order, so grouping preserves it.
  const groups: { label: string; chapters: Chapter[] }[] = [];
  for (const chapter of chapters) {
    const label = `Class ${chapter.grade} · ${chapter.unit_name}`;
    const last = groups[groups.length - 1];
    if (last?.label === label) last.chapters.push(chapter);
    else groups.push({ label, chapters: [chapter] });
  }

  const counted = chapters.every((c) => c.lessons_ready !== undefined);
  const ready = chapters.filter((c) => (c.lessons_ready ?? 0) > 0).length;

  return (
    <label className="flex flex-col gap-1 text-sm">
      <span className="font-semibold text-muted-foreground">Chapter</span>
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="h-10 w-full max-w-sm rounded-lg border border-input bg-card px-3 text-foreground shadow-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
      >
        {groups.map((group) => (
          <optgroup key={group.label} label={group.label}>
            {group.chapters.map((c) => (
              <option
                key={c.id}
                value={c.id}
                // The chapter already open stays selectable, so a shared link
                // to a coming-soon chapter still shows its name.
                disabled={c.lessons_ready === 0 && c.id !== value}
              >
                {optionLabel(c)}
              </option>
            ))}
          </optgroup>
        ))}
      </select>
      {counted && (
        <span className="text-xs text-muted-foreground">
          {ready} of {chapters.length} chapters have lessons
          {interest ? <> for <span className="capitalize">{interest}</span></> : null} so far — more
          are on the way.
        </span>
      )}
    </label>
  );
}
