// The shared frame for the login and signup pages: heading, a card, a footer
// link, and the small form pieces both pages use.

import type { ReactNode } from "react";

import { PageContainer } from "@/components/page-container";
import { SectionHeading } from "@/components/section-heading";
import { Input } from "@/components/ui/input";

export function AuthCard({
  eyebrow,
  title,
  subtitle,
  footer,
  children,
}: {
  eyebrow: string;
  title: string;
  subtitle: string;
  footer: ReactNode;
  children: ReactNode;
}) {
  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-1 flex-col items-center justify-center gap-8">
        <SectionHeading
          eyebrow={eyebrow}
          title={title}
          subtitle={subtitle}
          className="items-center text-center"
        />
        <div className="flex w-full max-w-md flex-col gap-6 rounded-xl border border-border bg-card p-6 shadow-card">
          {children}
        </div>
        <p className="text-sm text-muted-foreground">{footer}</p>
      </PageContainer>
    </main>
  );
}

export function Field({
  id,
  label,
  hint,
  error,
  ...inputProps
}: {
  id: string;
  label: string;
  hint?: string;
  error?: string | null;
} & React.ComponentProps<typeof Input>) {
  const describedBy = error ? `${id}-error` : hint ? `${id}-hint` : undefined;
  return (
    <div className="flex flex-col gap-2">
      <label htmlFor={id} className="text-sm font-semibold text-foreground">
        {label}
      </label>
      <Input id={id} aria-invalid={error ? true : undefined} aria-describedby={describedBy} {...inputProps} />
      {error ? (
        <p id={`${id}-error`} className="text-sm text-destructive">
          {error}
        </p>
      ) : hint ? (
        <p id={`${id}-hint`} className="text-xs text-muted-foreground">
          {hint}
        </p>
      ) : null}
    </div>
  );
}

export function FormError({ message }: { message: string | null }) {
  if (!message) return null;
  return (
    <p
      role="alert"
      className="rounded-xl border border-destructive/30 bg-destructive/5 px-4 py-3 text-sm text-destructive"
    >
      {message}
    </p>
  );
}
