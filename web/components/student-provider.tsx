// Holds the "currently signed-in student" in memory and shares it across pages.
//
// WHY: when onboarding calls the API it gets back a student_id. The /roadmap page
// needs that id too. Props can't cross a route navigation, so we lift the value
// into React Context — a value any component in the tree can read without passing
// props down by hand.
//
// "for now": this lives in memory and resets on a full page reload (F5). That's
// fine for the demo; later we'd persist it (localStorage / a real session).

"use client"; // Context + useState run in the browser, so this is a Client Component.

import { createContext, useContext, useState, type ReactNode } from "react";

import type { StudentProfile } from "@/lib/api";

interface StudentContextValue {
  student: StudentProfile | null;
  setStudent: (student: StudentProfile | null) => void;
}

const StudentContext = createContext<StudentContextValue | undefined>(undefined);

export function StudentProvider({ children }: { children: ReactNode }) {
  const [student, setStudent] = useState<StudentProfile | null>(null);
  return (
    <StudentContext.Provider value={{ student, setStudent }}>
      {children}
    </StudentContext.Provider>
  );
}

// A tiny hook so pages just call useStudent() instead of wiring up context.
export function useStudent() {
  const ctx = useContext(StudentContext);
  if (!ctx) {
    throw new Error("useStudent must be used inside <StudentProvider>");
  }
  return ctx;
}
