// Where a student lands right after logging in.
//
// The starting check comes first (hobbies, then the questions) until it has been
// taken, whatever page they were on when they logged out or timed out; then an
// open end check; otherwise the page they were heading for. It is only a choice
// of page: if either request fails we fall back to `next`, never block a login.
//
// A student who chose "Skip for now" is not sent back to the check at every login:
// the choice is remembered on this device (the roadmap still invites them to take it).

import { getDiagnostic, getEndCheck } from "@/lib/api";

const skipKey = (studentId: string) => `ecolearn-skip-check:${studentId}`;

export function rememberSkippedCheck(studentId: string): void {
  try {
    localStorage.setItem(skipKey(studentId), "1");
  } catch {
    // storage blocked: they will just be offered the check again next time
  }
}

function skippedCheck(studentId: string): boolean {
  try {
    return localStorage.getItem(skipKey(studentId)) === "1";
  } catch {
    return false;
  }
}

export async function landingPath(next: string, studentId: string): Promise<string> {
  try {
    const diagnostic = await getDiagnostic();
    if (!diagnostic.taken && !skippedCheck(studentId)) return "/start";
    const endCheck = await getEndCheck();
    if (endCheck.status === "open") return "/end-check";
  } catch {
    // keep `next`
  }
  return next;
}
