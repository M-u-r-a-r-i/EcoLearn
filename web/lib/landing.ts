// Where a student lands right after logging in.
//
// The starting check comes first (hobbies, then the questions) until it has been
// taken, whatever page they were on when they logged out or timed out; then an
// open end check; otherwise the page they were heading for. It is only a choice
// of page: if either request fails we fall back to `next`, never block a login.

import { getDiagnostic, getEndCheck } from "@/lib/api";

export async function landingPath(next: string): Promise<string> {
  try {
    const diagnostic = await getDiagnostic();
    if (!diagnostic.taken) return "/start";
    const endCheck = await getEndCheck();
    if (endCheck.status === "open") return "/end-check";
  } catch {
    // keep `next`
  }
  return next;
}
