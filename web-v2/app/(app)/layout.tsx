// Layout for the logged-in part of the app. "(app)" in parentheses is a route
// group: it groups pages under one layout without adding "/app" to their URLs,
// so /roadmap, /lesson and /assessment keep their addresses.

import { RequireAuth } from "@/components/require-auth";

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return <RequireAuth>{children}</RequireAuth>;
}
