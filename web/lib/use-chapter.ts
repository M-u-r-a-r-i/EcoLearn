// Which chapter the student is looking at, kept in the URL (?chapter=...).
//
// WHY THE URL, not React state: the roadmap → lesson → assessment pages all need
// the same chapter, a refresh must keep it, and a teacher can share a link
// straight to a chapter. The URL does all three for free.

"use client";

import { useCallback, useEffect, useState } from "react";
import { usePathname, useRouter, useSearchParams } from "next/navigation";

import { getChapters, type Chapter } from "@/lib/api";

// Class 11, chapter 2 — the first chapter students are piloting on.
export const DEFAULT_CHAPTER_ID = "motion_straight_line";

// Fetch the chapter list once per page load and share it between components.
let chaptersPromise: Promise<Chapter[]> | null = null;
function loadChapters(): Promise<Chapter[]> {
  chaptersPromise ??= getChapters().catch((err) => {
    chaptersPromise = null; // let the next caller retry
    throw err;
  });
  return chaptersPromise;
}

// Uses useSearchParams, so the calling page must render inside <Suspense>.
export function useChapter() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const pathname = usePathname();
  const chapterId = searchParams.get("chapter") ?? DEFAULT_CHAPTER_ID;

  const [chapters, setChapters] = useState<Chapter[] | null>(null);
  useEffect(() => {
    loadChapters().then(setChapters, () => setChapters([]));
  }, []);

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
