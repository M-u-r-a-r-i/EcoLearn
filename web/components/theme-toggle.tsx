// Light / dark / follow-the-device, one button in the nav. The choice is a
// per-device convenience, so it lives in localStorage (wrapped in try/catch:
// private windows and locked-down school browsers may refuse storage, and the
// page must still work). The <head> script in app/layout.tsx applies the saved
// choice before the first paint, so a dark-mode user never sees a white flash.

"use client";

import { useEffect, useSyncExternalStore } from "react";
import { Monitor, Moon, Sun } from "lucide-react";

export type ThemeChoice = "system" | "light" | "dark";

export const THEME_KEY = "ecolearn-theme";
const ORDER: ThemeChoice[] = ["system", "light", "dark"];
const LABEL: Record<ThemeChoice, string> = {
  system: "Theme: same as device",
  light: "Theme: light",
  dark: "Theme: dark",
};

// A tiny store so every toggle (and the effect below) agrees on the choice.
const listeners = new Set<() => void>();

function read(): ThemeChoice {
  try {
    const value = localStorage.getItem(THEME_KEY);
    return value === "light" || value === "dark" ? value : "system";
  } catch {
    return "system";
  }
}

function write(choice: ThemeChoice) {
  try {
    if (choice === "system") localStorage.removeItem(THEME_KEY);
    else localStorage.setItem(THEME_KEY, choice);
  } catch {
    // storage refused: the choice still applies until the page is reloaded
  }
  memory = choice;
  listeners.forEach((l) => l());
}

let memory: ThemeChoice | null = null;
const getSnapshot = () => memory ?? (memory = read());
const subscribe = (l: () => void) => {
  listeners.add(l);
  return () => listeners.delete(l);
};

function apply(choice: ThemeChoice) {
  const dark =
    choice === "dark" ||
    (choice === "system" && window.matchMedia("(prefers-color-scheme: dark)").matches);
  document.documentElement.classList.toggle("dark", dark);
  document.documentElement.style.colorScheme = dark ? "dark" : "light";
}

export function ThemeToggle() {
  // "system" on the server, the saved choice in the browser: no hydration mismatch.
  const choice = useSyncExternalStore(subscribe, getSnapshot, () => "system" as ThemeChoice);

  useEffect(() => {
    apply(choice);
    if (choice !== "system") return;
    // Following the device: react when the device switches.
    const media = window.matchMedia("(prefers-color-scheme: dark)");
    const onChange = () => apply("system");
    media.addEventListener("change", onChange);
    return () => media.removeEventListener("change", onChange);
  }, [choice]);

  const next = ORDER[(ORDER.indexOf(choice) + 1) % ORDER.length];
  const Icon = choice === "dark" ? Moon : choice === "light" ? Sun : Monitor;
  return (
    <button
      type="button"
      onClick={() => write(next)}
      aria-label={`${LABEL[choice]}. Switch to ${next === "system" ? "device setting" : next}.`}
      title={LABEL[choice]}
      className="theme-toggle print:hidden"
    >
      <Icon className="size-[1.1rem]" aria-hidden />
    </button>
  );
}

// Inlined into <head> by app/layout.tsx; runs before React, before paint.
export const THEME_BOOT_SCRIPT = `try{var t=localStorage.getItem("${THEME_KEY}");var d=t==="dark"||(t!=="light"&&matchMedia("(prefers-color-scheme: dark)").matches);var e=document.documentElement;if(d)e.classList.add("dark");e.style.colorScheme=d?"dark":"light"}catch(_){}`;
