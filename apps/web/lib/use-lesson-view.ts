// Record a lesson view for the pilot: that the student opened this lesson, how
// long they actively read it, and their 👍/👎.
//
// "Active" means the tab is visible AND the student has touched, scrolled or
// typed in the last two minutes. A lesson left open in a background tab, or on
// a desk during lunch, should not count as reading — the pilot numbers have to
// survive a sceptical question at the finals. The server also caps every view
// at 30 minutes and at the time since it was opened.
//
// The view starts after the lesson has been on screen for 2 s. That skips
// accidental opens, and it also means React's development double-mount (which
// runs an effect, cleans it up, and runs it again) never creates a second view:
// the first timer is cleared before it fires.

"use client";

import { useEffect, useRef, useState } from "react";

import { rateLesson, reportLessonTime, startLessonView, type LessonRating } from "@/lib/api";

const START_DELAY_MS = 2_000;
const TICK_SECONDS = 5;
const IDLE_MS = 2 * 60 * 1000;
const REPORT_EVERY_SECONDS = 30; // a heartbeat, so a crashed tab still reports

const INPUT_EVENTS = ["pointerdown", "pointermove", "keydown", "scroll", "wheel", "touchstart"] as const;

export function useLessonView(conceptId: string | null) {
  // The rating belongs to one concept; keying it means a stale value from the
  // previous lesson is never shown on the next one.
  const [saved, setSaved] = useState<{ conceptId: string; rating: LessonRating } | null>(null);
  const [ratingError, setRatingError] = useState(false);
  const busy = useRef(false);

  useEffect(() => {
    if (!conceptId) return;
    let cancelled = false;
    let viewId: string | null = null;
    let active = 0; // seconds of active reading so far
    let reported = 0;
    let lastInput = Date.now();

    const flush = () => {
      if (viewId && active > reported) {
        reported = active;
        reportLessonTime(viewId, active);
      }
    };
    const onInput = () => {
      lastInput = Date.now();
    };
    const onVisibility = () => {
      if (document.visibilityState === "hidden") flush();
    };

    const startTimer = setTimeout(() => {
      startLessonView(conceptId).then(
        (view) => {
          if (cancelled) return;
          viewId = view.view_id;
          setSaved({ conceptId, rating: view.rating });
        },
        () => {}, // metrics must never get in the way of the lesson
      );
    }, START_DELAY_MS);

    const tick = setInterval(() => {
      if (document.visibilityState === "visible" && Date.now() - lastInput < IDLE_MS) {
        active += TICK_SECONDS;
      }
      if (active - reported >= REPORT_EVERY_SECONDS) flush();
    }, TICK_SECONDS * 1000);

    for (const name of INPUT_EVENTS) window.addEventListener(name, onInput, { passive: true });
    document.addEventListener("visibilitychange", onVisibility);
    window.addEventListener("pagehide", flush);

    return () => {
      cancelled = true;
      clearTimeout(startTimer);
      clearInterval(tick);
      flush(); // leaving for another page inside the app
      for (const name of INPUT_EVENTS) window.removeEventListener(name, onInput);
      document.removeEventListener("visibilitychange", onVisibility);
      window.removeEventListener("pagehide", flush);
    };
  }, [conceptId]);

  const rating: LessonRating = saved && saved.conceptId === conceptId ? saved.rating : 0;

  // Clicking the active thumb again clears it. Optimistic: the thumb lights up
  // at once and goes back if the server says no.
  async function rate(next: LessonRating) {
    if (!conceptId || busy.current) return;
    const value: LessonRating = next === rating ? 0 : next;
    const previous = rating;
    busy.current = true;
    setRatingError(false);
    setSaved({ conceptId, rating: value });
    try {
      await rateLesson(conceptId, value);
    } catch {
      setSaved({ conceptId, rating: previous });
      setRatingError(true);
    } finally {
      busy.current = false;
    }
  }

  return { rating, rate, ratingError };
}
