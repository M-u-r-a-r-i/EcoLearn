// Small building blocks of the EcoLearn house style (skill: .claude/skills/ecolearn-style),
// ported from the Replit design's ui-kit. They only render markup + the class names in
// app/ecolearn.css; no data, no logic. Reuse these before inventing a new wrapper.

import Link from "next/link";
import type { CSSProperties, ReactNode } from "react";
import { ArrowRight } from "lucide-react";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

/** Accent colour per interest (the chip behind an emoji). Unknown ids fall back to green. */
export const INTEREST_COLOR: Record<string, string> = {
  cricket: "#efb45b",
  football: "#84be89",
  gaming: "#bd9ce2",
  smartphones: "#78b9c7",
  motorsport: "#eb9170",
};

export function InterestMark({
  id,
  emoji,
  large = false,
}: {
  id: string;
  emoji: string;
  large?: boolean;
}) {
  return (
    <span
      className={cn("interest-mark", large && "large")}
      style={{ "--interest": INTEREST_COLOR[id] ?? "#79c29b" } as CSSProperties}
      aria-hidden
    >
      {emoji}
    </span>
  );
}

/** Every page starts with one: small eyebrow, big display title, muted description, optional action. */
export function PageHeading({
  eyebrow,
  title,
  description,
  action,
}: {
  eyebrow?: string;
  title: string;
  description?: ReactNode;
  action?: ReactNode;
}) {
  return (
    <div className="page-heading fade-up">
      <div>
        {eyebrow && <p className="eyebrow">{eyebrow}</p>}
        <h1 className="display">{title}</h1>
        {description && <p className="heading-description">{description}</p>}
      </div>
      {action}
    </div>
  );
}

export function Panel({
  children,
  className = "",
}: {
  children: ReactNode;
  className?: string;
}) {
  return <section className={`surface panel ${className}`}>{children}</section>;
}

export function Pill({ children, className = "" }: { children: ReactNode; className?: string }) {
  return <span className={`tag ${className}`}>{children}</span>;
}

export function Meter({
  value,
  max = 100,
  label,
}: {
  value: number;
  max?: number;
  label?: string;
}) {
  const pct = Math.max(0, Math.min(100, max > 0 ? (value / max) * 100 : 0));
  return (
    <div
      className="progress-track"
      role="progressbar"
      aria-label={label}
      aria-valuemin={0}
      aria-valuemax={100}
      aria-valuenow={Math.round(pct)}
    >
      <div className="progress-fill" style={{ width: `${pct}%` }} />
    </div>
  );
}

export function EmptyState({
  title,
  copy,
  href,
  action,
  children,
}: {
  title: string;
  copy?: ReactNode;
  href?: string;
  action?: string;
  children?: ReactNode;
}) {
  return (
    <div className="empty-state">
      <span className="empty-spark" aria-hidden>
        ✳
      </span>
      <h3>{title}</h3>
      {copy && <p>{copy}</p>}
      {href && (
        <Button asChild>
          <Link href={href}>
            {action ?? "Keep going"} <ArrowRight size={16} aria-hidden />
          </Link>
        </Button>
      )}
      {children}
    </div>
  );
}

export function Skeleton({ rows = 3 }: { rows?: number }) {
  return (
    <div className="skeleton-stack" role="status" aria-label="Loading">
      <span className="skeleton-line wide" />
      {Array.from({ length: rows }, (_, i) => (
        <span key={i} className="skeleton-line" />
      ))}
    </div>
  );
}
