// Fades its children up when they scroll into view. No state: the element is marked
// "wait" by an effect and flipped to "in" by an IntersectionObserver, and the CSS for both
// lives in globals.css under prefers-reduced-motion. If JS never runs, nothing is hidden.

"use client";

import { useEffect, useRef, type ReactNode } from "react";

export function Reveal({
  children,
  className,
  delay = 0,
}: {
  children: ReactNode;
  className?: string;
  delay?: number; // seconds
}) {
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el || !("IntersectionObserver" in window)) return;
    // Already on screen (the hero): don't hide it just to show it again.
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight * 0.9) {
      el.dataset.reveal = "in";
      return;
    }
    el.dataset.reveal = "wait";
    const io = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          el.dataset.reveal = "in";
          io.disconnect();
        }
      },
      { threshold: 0.15 },
    );
    io.observe(el);
    return () => io.disconnect();
  }, []);

  return (
    <div ref={ref} className={className} style={{ ["--reveal-delay" as string]: `${delay}s` }}>
      {children}
    </div>
  );
}
