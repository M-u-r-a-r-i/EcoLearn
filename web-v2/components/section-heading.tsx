// A reusable heading for sections within a page: an optional small amber
// "eyebrow" label, a bold title, and an optional muted subtitle. Using this
// everywhere keeps heading sizes, weights, spacing, and colours consistent
// instead of each page hand-rolling its own <h2>.

import * as React from "react";

import { cn } from "@/lib/utils";

interface SectionHeadingProps {
  eyebrow?: string;
  title: string;
  subtitle?: string;
  className?: string;
}

export function SectionHeading({
  eyebrow,
  title,
  subtitle,
  className,
}: SectionHeadingProps) {
  return (
    <div className={cn("flex flex-col gap-2", className)}>
      {eyebrow && (
        <span className="text-sm font-semibold uppercase tracking-wide text-brand-accent">
          {eyebrow}
        </span>
      )}
      <h2 className="text-2xl font-bold tracking-tight text-foreground sm:text-3xl">
        {title}
      </h2>
      {subtitle && (
        <p className="max-w-2xl leading-relaxed text-muted-foreground">{subtitle}</p>
      )}
    </div>
  );
}
