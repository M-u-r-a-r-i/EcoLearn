// Layout for the logged-in part of the app. "(app)" in parentheses is a route
// group: it groups pages under one layout without adding "/app" to their URLs,
// so /roadmap, /lesson and /assessment keep their addresses.
//
// <WelcomeGate> sends a student who hasn't answered "getting to know you" to /welcome first.

import { RequireAuth } from "@/components/require-auth";
import { WelcomeGate } from "@/components/welcome-gate";

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <RequireAuth>
      <WelcomeGate>{children}</WelcomeGate>
    </RequireAuth>
  );
}
