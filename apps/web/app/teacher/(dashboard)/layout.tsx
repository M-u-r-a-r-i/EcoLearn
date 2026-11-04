// Layout for the logged-in teacher pages. "(dashboard)" is a route group: it
// puts /teacher, /teacher/class and /teacher/account behind one guard without
// adding a segment to their URLs — and leaves /teacher/login outside it.

import { RequireAuth } from "@/components/require-auth";

export default function TeacherLayout({ children }: { children: React.ReactNode }) {
  return <RequireAuth role="teacher">{children}</RequireAuth>;
}
