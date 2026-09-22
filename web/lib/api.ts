// Typed client for the EcoLearn FastAPI backend.
//
// Every call to the backend goes through a function here, so the rest of the app
// never writes raw fetch() calls or hardcodes URLs. This mirrors the Python side:
// the UI talks to ONE module, and that module talks to the network.
//
// Who the student is travels in an httpOnly session cookie that the API sets at
// login. JavaScript can't read it (that's the point: a script injected into the
// page can't steal it), so no function here takes a student id — the browser
// attaches the cookie itself because every request uses credentials: "include".

// The base URL comes from the environment (web/.env.local). We fall back to
// localhost so the app still runs if the var is missing in development.
export const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

// ---------------------------------------------------------------------------
// The one request helper.
// ---------------------------------------------------------------------------

// An HTTP error from the API, carrying the status and FastAPI's {"detail"} text.
// status 0 means the request never got an answer (backend down, timeout, CORS).
export class ApiError extends Error {
  constructor(
    public status: number,
    public detail: string,
  ) {
    super(detail);
    this.name = "ApiError";
  }
}

// Called on any 401 from a request that expected a session, so the auth provider
// can drop the user back to the login page. A callback instead of a router
// import keeps this module free of React.
let onUnauthorized: (() => void) | null = null;
export function setUnauthorizedHandler(handler: (() => void) | null) {
  onUnauthorized = handler;
}

interface RequestOptions {
  method?: "GET" | "POST" | "PATCH";
  query?: Record<string, string | undefined>;
  body?: unknown;
  timeoutMs?: number;
  // Login and "who am I" answer 401 as a normal outcome; don't treat it as expiry.
  expectAuthFailure?: boolean;
}

// Live-LLM calls (the doubt chat) take seconds; everything else is cached.
const DEFAULT_TIMEOUT_MS = 15_000;
const LIVE_TIMEOUT_MS = 90_000;

async function request<T>(path: string, options: RequestOptions = {}): Promise<T> {
  const url = new URL(`${API_URL}${path}`);
  for (const [key, value] of Object.entries(options.query ?? {})) {
    if (value !== undefined) url.searchParams.set(key, value);
  }

  let response: Response;
  try {
    response = await fetch(url, {
      method: options.method ?? "GET",
      credentials: "include", // send the session cookie to the API's origin
      headers: options.body === undefined ? undefined : { "Content-Type": "application/json" },
      body: options.body === undefined ? undefined : JSON.stringify(options.body),
      signal: AbortSignal.timeout(options.timeoutMs ?? DEFAULT_TIMEOUT_MS),
    });
  } catch {
    // fetch() only throws when there is no HTTP answer at all.
    throw new ApiError(0, "Can't reach EcoLearn right now. Check your connection and try again.");
  }

  // fetch() does NOT throw on 4xx/5xx, so check response.ok ourselves.
  if (!response.ok) {
    const detail = await readDetail(response);
    if (response.status === 401 && !options.expectAuthFailure) onUnauthorized?.();
    throw new ApiError(response.status, detail);
  }
  return (await response.json()) as T;
}

// FastAPI errors look like {"detail": "..."} — or, for a 422, a list of problems.
async function readDetail(response: Response): Promise<string> {
  try {
    const data = await response.json();
    if (typeof data?.detail === "string") return data.detail;
    if (Array.isArray(data?.detail)) return "Please check the form and try again.";
  } catch {
    // not JSON — fall through
  }
  return response.status >= 500
    ? "Something went wrong on our side. Please try again."
    : `Request failed (${response.status}).`;
}

// A message that is safe to show a student for any error thrown here.
export function friendlyMessage(error: unknown): string {
  if (error instanceof ApiError) return error.detail;
  return "Something went wrong. Please try again.";
}

// ---------------------------------------------------------------------------
// Accounts
// ---------------------------------------------------------------------------
export interface StudentProfile {
  student_id: string;
  username: string | null; // null only for legacy name-only (Streamlit) students
  name: string;
  interest: string;
  level: string;
  created_at: string;
}

export interface RegisterInput {
  name: string;
  username: string;
  password: string;
  interest: string;
  level: string;
}

export function register(input: RegisterInput): Promise<StudentProfile> {
  return request("/api/auth/register", { method: "POST", body: input });
}

export function login(username: string, password: string): Promise<StudentProfile> {
  return request("/api/auth/login", {
    method: "POST",
    body: { username, password },
    expectAuthFailure: true,
  });
}

export function logout(): Promise<{ logged_out: boolean }> {
  return request("/api/auth/logout", { method: "POST" });
}

// 200 with the profile when the session cookie is valid, ApiError(401) otherwise.
export function getMe(): Promise<StudentProfile> {
  return request("/api/auth/me", { expectAuthFailure: true });
}

export function updateProfile(
  changes: Partial<Pick<StudentProfile, "name" | "interest" | "level">>,
): Promise<StudentProfile> {
  return request("/api/profile", { method: "PATCH", body: changes });
}

export function changePassword(currentPassword: string, newPassword: string): Promise<unknown> {
  return request("/api/auth/change-password", {
    method: "POST",
    body: { current_password: currentPassword, new_password: newPassword },
    expectAuthFailure: true, // a wrong current password is a 401 too, not an expired session
  });
}

// ---------------------------------------------------------------------------
// Curriculum (public — the signup page needs interests before anyone logs in)
// ---------------------------------------------------------------------------
export interface Chapter {
  id: string;
  name: string;
  unit_id: string;
  unit_name: string;
  grade: number; // 11 or 12
  domain: string;
  concept_count: number;
}

export function getChapters(): Promise<Chapter[]> {
  return request("/api/chapters");
}

export interface Interest {
  id: string;
  label: string;
  emoji: string;
  description: string;
  status: string;
}

export function getInterests(): Promise<Interest[]> {
  return request("/api/interests");
}

// ---------------------------------------------------------------------------
// One concept on the roadmap, as returned by GET /api/roadmap.
// ---------------------------------------------------------------------------
// Nothing is ever locked — prerequisites are hints (see missing_prerequisites).
export type ConceptStatus = "mastered" | "available";

export interface RoadmapConcept {
  concept_id: string;
  name: string;
  order: number;
  status: ConceptStatus;
  progress_status: string;
  best_score: number;
  attempts: number;
  missing_prerequisites: string[]; // uncleared prerequisites — a "brush up first" hint
}

export function getRoadmap(chapterId: string): Promise<RoadmapConcept[]> {
  return request("/api/roadmap", { query: { chapter_id: chapterId } });
}

// ---------------------------------------------------------------------------
// A lesson's content (the pre-generated, polished markdown).
// ---------------------------------------------------------------------------
// One "## heading" block of an authored lesson, so the page can decide what to
// show and what to tuck behind a click.
export interface LessonSection {
  heading: string;
  markdown: string;
}

// The check question as the browser is allowed to see it: the question and the
// options, never the answer key. Grading happens on the server.
export interface LessonCheck {
  question: string;
  options: Record<string, string>; // {"A": "...", "B": "...", ...}
}

export interface Lesson {
  concept_id: string;
  interest: string;
  body: string; // markdown — the whole lesson (legacy shape)
  worked_example: string; // markdown (legacy, empty for authored lessons)
  check_question: string; // markdown / text (legacy)
  metadata: Record<string, unknown>;
  // Present for authored lessons (everything written since 2026-09):
  title?: string;
  sections?: LessonSection[];
  check?: LessonCheck;
}

export type LessonStatus =
  | "new"
  | "review"
  | "done"
  | "blocked"
  | "lesson_missing";

// The "envelope" get_next_lesson returns: it always has a status + reason, and
// a lesson only when there's something to teach (lesson is null otherwise).
export interface NextLesson {
  status: LessonStatus;
  reason: string;
  concept_id: string | null;
  concept_name: string | null;
  lesson: Lesson | null;
}

// conceptId is optional: pass it to open a specific concept instead of the
// engine's pick.
export function getNextLesson(chapterId: string, conceptId?: string): Promise<NextLesson> {
  return request("/api/next-lesson", { query: { chapter_id: chapterId, concept_id: conceptId } });
}

// ---------------------------------------------------------------------------
// POST /api/help — a live, grounded answer. The ONE expensive call: it runs real
// LLM work on the server, so the UI must show a "thinking" state.
// ---------------------------------------------------------------------------
export interface HelpResponse {
  concept_id: string;
  concept_name: string;
  answer: string; // markdown
  verdict: string;
  attempts: number;
}

export function askHelp(conceptId: string, question: string): Promise<HelpResponse> {
  return request("/api/help", {
    method: "POST",
    body: { concept_id: conceptId, question },
    timeoutMs: LIVE_TIMEOUT_MS,
  });
}

// ---------------------------------------------------------------------------
// POST /api/assessment — grade the answer and update mastery in the store,
// the single source of truth the roadmap reads from.
// ---------------------------------------------------------------------------
export interface MasteryRow {
  status: string;
  best_score: number;
  attempts: number;
  [key: string]: unknown;
}

export interface AssessmentResult {
  concept_id: string;
  score: number; // 0-3
  mastery_signal: "mastered" | "partial" | "not_yet";
  feedback: string;
  missing_concepts: string[];
  graded_question: string;
  mastery: MasteryRow;
  // Multiple-choice grading only (authored lessons); absent for legacy lessons.
  correct?: boolean;
  selected_option?: string;
  correct_option?: string;
}

// `answer` is the chosen option letter ("A".."D") for authored lessons, or free
// text for the older generated ones. Multiple-choice grading is a lookup against
// the lesson file, so it answers immediately — no model call.
export function submitAssessment(conceptId: string, answer: string): Promise<AssessmentResult> {
  return request("/api/assessment", {
    method: "POST",
    body: { concept_id: conceptId, answer },
    timeoutMs: LIVE_TIMEOUT_MS, // legacy free-text grading is still a live call
  });
}
