// Small, self-contained toasts: "Saved", "Story hidden", "Plan ready".
//
// For confirming an action that happened somewhere the eye isn't (a button at
// the bottom of a form, a row in a list). Errors that need fixing stay next to
// the field that caused them; a toast is only for "it worked" or "it failed,
// try again" news. Written here rather than adding a package: ~60 lines, no
// dependency to vet.
//
// Accessibility: one polite live region, so a screen reader announces each
// toast once without interrupting; every toast can be dismissed, and they
// disappear on their own after a few seconds.

"use client";

import { createContext, useCallback, useContext, useMemo, useRef, useState, type ReactNode } from "react";
import { CheckCircle2, Info, X, XCircle } from "lucide-react";

import { cn } from "@/lib/utils";

type Tone = "success" | "error" | "info";
interface ToastItem {
  id: number;
  message: string;
  tone: Tone;
}

const ToastContext = createContext<((message: string, tone?: Tone) => void) | null>(null);
const DURATION_MS = 4500;
const MAX_VISIBLE = 3;

export function Toaster({ children }: { children: ReactNode }) {
  const [items, setItems] = useState<ToastItem[]>([]);
  const nextId = useRef(1);

  const dismiss = useCallback((id: number) => {
    setItems((list) => list.filter((t) => t.id !== id));
  }, []);

  const toast = useCallback(
    (message: string, tone: Tone = "success") => {
      const id = nextId.current++;
      setItems((list) => [...list, { id, message, tone }].slice(-MAX_VISIBLE));
      window.setTimeout(() => dismiss(id), DURATION_MS);
    },
    [dismiss],
  );

  const value = useMemo(() => toast, [toast]);
  const Icon = { success: CheckCircle2, error: XCircle, info: Info };
  const tone = {
    success: "text-success",
    error: "text-destructive",
    info: "text-primary",
  };

  return (
    <ToastContext.Provider value={value}>
      {children}
      <div
        role="status"
        aria-live="polite"
        className="pointer-events-none fixed inset-x-0 bottom-4 z-50 flex flex-col items-center gap-2 px-4 sm:items-end sm:px-6 print:hidden"
      >
        {items.map((t) => {
          const I = Icon[t.tone];
          return (
            <div
              key={t.id}
              className="pointer-events-auto flex w-full max-w-sm items-start gap-3 rounded-2xl border border-border bg-card px-4 py-3 text-sm text-foreground shadow-card animate-in fade-in slide-in-from-bottom-2"
            >
              <I className={cn("mt-0.5 size-4 shrink-0", tone[t.tone])} aria-hidden />
              <span className="flex-1">{t.message}</span>
              <button
                type="button"
                onClick={() => dismiss(t.id)}
                aria-label="Dismiss"
                className="text-muted-foreground hover:text-foreground"
              >
                <X className="size-4" />
              </button>
            </div>
          );
        })}
      </div>
    </ToastContext.Provider>
  );
}

/** `const toast = useToast(); toast("Saved")` — or toast("Couldn't save", "error"). */
export function useToast() {
  const toast = useContext(ToastContext);
  if (!toast) throw new Error("useToast must be used inside <Toaster>");
  return toast;
}
