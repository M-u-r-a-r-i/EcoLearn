import type { ScreenSet } from "@/components/preview/shell";
import { screensA } from "@/components/preview/dir-a";
import { screensB } from "@/components/preview/dir-b";
import { screensC } from "@/components/preview/dir-c";

export const SCREENS = [
  { id: "landing", label: "Landing" },
  { id: "roadmap", label: "Roadmap" },
  { id: "lesson", label: "Lesson" },
  { id: "check", label: "Check" },
  { id: "teacher", label: "Teacher" },
] as const;
export type ScreenId = (typeof SCREENS)[number]["id"];

export const DIRECTIONS: Record<"a" | "b" | "c", { name: string; screens: ScreenSet }> = {
  a: { name: "A · Trailhead", screens: screensA },
  b: { name: "B · Field Notes", screens: screensB },
  c: { name: "C · Matchday", screens: screensC },
};
