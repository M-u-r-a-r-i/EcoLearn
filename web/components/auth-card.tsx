// The shared frame for the login, signup and teacher-login pages: the house-style
// two-column layout (a sage art panel on desktop, the form on the right), plus the
// small form pieces they all use.

import Link from "next/link";
import type { ReactNode } from "react";

import { Input } from "@/components/ui/input";

function Brand() {
  return (
    <Link href="/" className="brand-lockup">
      <span className="brand-mark" aria-hidden>
        e
      </span>
      <span>
        ecolearn<span className="brand-period">.</span>
      </span>
    </Link>
  );
}

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
    <main className="auth-wrap flex-1">
      <aside className="auth-art" aria-hidden>
        <Brand />
        <div className="auth-art-copy">
          <div className="auth-big-mark">e</div>
          <p className="eyebrow">Physics, in your element</p>
          <h2 className="display">Learn it through what you love.</h2>
          <span className="auth-equation">
            <b>F</b> = m · a <span>→ a six, a corner, a pit stop</span>
          </span>
        </div>
        <p className="auth-art-foot">Class 11–12 physics · CBSE &amp; ISC</p>
      </aside>
      <section className="auth-main">
        <div className="auth-form-wrap">
          <div className="auth-mobile-brand">
            <Brand />
          </div>
          <div className="auth-topline">
            <p className="eyebrow">{eyebrow}</p>
            <h1 className="display">{title}</h1>
            <p className="auth-copy">{subtitle}</p>
          </div>
          {children}
          <p className="auth-switch">{footer}</p>
        </div>
      </section>
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
      <label htmlFor={id} className="text-xs font-bold text-foreground">
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
