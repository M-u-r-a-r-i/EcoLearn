// Which chapter the student is looking at, kept in the URL (?chapter=...).
//
// WHY THE URL, not React state: the roadmap → lesson → assessment pages all need
// the same chapter, a refresh must keep it, and a teacher can share a link
// straight to a chapter. The URL does all three for free.

"use client";

import { useCallback, useEffect, useState } from "react";
import { usePathname, useRouter, useSearchParams } from "next/navigation";

import { useAuth } from "@/components/auth-provider";
import { getChapters, type Chapter } from "@/lib/api";

// Class 11, chapter 2 — the first chapter students are piloting on. It has
// lessons in every in-scope interest.
export const DEFAULT_CHAPTER_ID = "motion_straight_line";

// Each class starts in its own first piloted chapter (the class is set by the teacher).
const DEFAULT_BY_LEVEL: Record<string, string> = {
  "Class 11": DEFAULT_CHAPTER_ID,
  "Class 12": "current_electricity",
};
export function defaultChapterFor(level: string | undefined): string {
  return DEFAULT_BY_LEVEL[level ?? ""] ?? DEFAULT_CHAPTER_ID;
}

// Fetch the chapter list once per page load per interest and share it between
// components. Keyed by interest because each chapter's `lessons_ready` depends
// on it, and a student can switch interest in settings.
const chaptersPromises = new Map<string, Promise<Chapter[]>>();
function loadChapters(interest: string): Promise<Chapter[]> {
  let promise = chaptersPromises.get(interest);
  if (!promise) {
    promise = getChapters(interest || undefined).catch((err) => {
      chaptersPromises.delete(interest); // let the next caller retry
      throw err;
    });
    chaptersPromises.set(interest, promise);
  }
  return promise;
}

// Uses useSearchParams, so the calling page must render inside <Suspense>.
export function useChapter() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const pathname = usePathname();
  const { student } = useAuth();
  const interest = student?.interest ?? "";
  const level = student?.level;

  const [loaded, setLoaded] = useState<{ interest: string; chapters: Chapter[] } | null>(null);
  useEffect(() => {
    let cancelled = false;
    loadChapters(interest).then(
      (list) => !cancelled && setLoaded({ interest, chapters: list }),
      () => !cancelled && setLoaded({ interest, chapters: [] }),
    );
    return () => {
      cancelled = true;
    };
  }, [interest]);
  // A list loaded for a previous interest is stale: show loading instead.
  // A student sees only their own class's chapters; a teacher moves them between classes.
  const chapters =
    loaded?.interest === interest
      ? loaded.chapters.filter((c) => !level || `Class ${c.grade}` === level)
      : null;
  const wanted = searchParams.get("chapter");
  const chapterId =
    wanted && (chapters === null || chapters.some((c) => c.id === wanted))
      ? wanted
      : defaultChapterFor(level);

  const setChapter = useCallback(
    (id: string) => {
      const params = new URLSearchParams(searchParams);
      params.set("chapter", id);
      router.push(`${pathname}?${params}`);
    },
    [searchParams, router, pathname],
  );

  const chapter = chapters?.find((c) => c.id === chapterId) ?? null;
  return { chapterId, chapter, chapters, setChapter };
}

// A link to another page that keeps the current chapter.
export function withChapter(path: string, chapterId: string, extra: Record<string, string> = {}) {
  return `${path}?${new URLSearchParams({ chapter: chapterId, ...extra })}`;
}
