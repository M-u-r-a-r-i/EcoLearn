// A number that counts up from zero when it appears (about 0.9 s). Under
// reduced motion, or when the value is 0, it just shows the number. Purely
// decoration: the final value is what's in the page for screen readers.

"use client";

import { useEffect, useState } from "react";

export function CountUp({ value, ms = 900 }: { value: number; ms?: number }) {
  const [shown, setShown] = useState(0);

  useEffect(() => {
    if (value <= 0 || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const start = performance.now();
    let frame = 0;
    const tick = (now: number) => {
      const t = Math.min(1, (now - start) / ms);
      const eased = 1 - Math.pow(1 - t, 3); // fast at first, settling at the end
      setShown(Math.round(value * eased));
      if (t < 1) frame = requestAnimationFrame(tick);
    };
    frame = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(frame);
  }, [value, ms]);

  // No animation: show the number outright (also what a screen reader reads).
  const reduce = typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  return <span aria-label={String(value)}>{value <= 0 || reduce ? value : shown}</span>;
}
