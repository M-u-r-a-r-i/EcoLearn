// Pick a chapter from the whole syllabus, grouped by class and unit.
//
// A native <select> with one <optgroup> per "Class · unit": keyboard- and
// screen-reader-friendly for free, and on phones it opens the OS picker, which
// handles 29 chapters better than any custom dropdown.

"use client";

import type { Chapter } from "@/lib/api";

export function ChapterPicker({
  chapters,
  value,
  onChange,
}: {
  chapters: Chapter[] | null;
  value: string;
  onChange: (id: string) => void;
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
              <option key={c.id} value={c.id}>
                {c.name}
              </option>
            ))}
          </optgroup>
        ))}
      </select>
    </label>
  );
}
